the sign-up request has been processed.


Standard Objects SignupRequest

**Field Name** **Details**

```
CreatedOrgInstance

Edition

ErrorCode

FirstName

LastName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The server instance of the new trial org, for example, “na8.” This field is available in API version
29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The Salesforce template that is used to create the trial org. Possible values are `Partner`
`Group`, `Professional`, `Partner Professional`, `Sales Enterprise`,
`Professional TSO`, `Enterprise`, `Partner Enterprise`, `Service`
`Professional`, `Enterprise TSO`, `Developer`, and `Partner Developer` .
This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code if the sign-up request isn’t successful. The system provides this read-only field
for support purposes.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The first name of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The last name of the admin user for the trial sign-up.


Standard Objects SignupRequest

**Field Name** **Details**

```
PreferredLanguage

ResolvedTemplateId

ShouldConnectToEnvHub

SignupEmail

SignupSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the trial org being created. Specify the language using a language code listed
[under Fully Supported Languages in Supported Languages in Salesforce Help. For example,](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
use _`zh_CN`_ for simplified Chinese. The value you select overrides the language set by the
locale. If you specify an invalid language, the org defaults to the default language of the country.
Likewise, if you specify a language that isn’t supported by the Salesforce edition associated
with your trial template, the trial org defaults to the default language of the country. This field
is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Populated during the sign-up request and for internal use by Salesforce. This field is available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
When set to `true`, the trial org is connected to the Environment Hub. The sign-up must take
place in the hub main org or a spoke org. This field is available in API version 35.0 and later.

**Type**
email

**Properties**
Create, Filter, Group, Sort

**Description**
The email address of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects SignupRequest

**Field Name** **Details**

**Description**
A user-specified description of the trial sign-up, up to 60 characters. This field is available in
API version 36.0 and later.

```
Status

Subdomain

SuppressSignupEmails

TemplateId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the request. Possible values are `New`, `In Progress`, `Error`, or `Success` .
The default is `New` .

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The My Domain name for the new trial org used in the org’s login and application URLs. In
Developer Edition orgs, your name must contain at least 3 characters and no more than 27
characters. In all other editions, it must be at least 3 characters and no more than 34 characters.
It can include letters, numbers, and hyphens, but you can’t start the name with a hyphen.

If you don’t choose a My Domain during sign-up, Salesforce assigns one for you based on your
company name. If you don’t like the one we set, you can change it.

[For details, see My Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=domain_name_overview.htm&language=en_US)

**Type**
boolean

**Properties**
Filter, Group, Nillable, Sort

**Description**
When set to `true`, no sign-up emails are sent when the trial org is created. This field is used
for the Proxy Signup feature and is available in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Trialforce template that is the basis for the trial sign-up. Salesforce
must approve the template. If you don’t specify an edition, a template ID is required.


Standard Objects SignupRequest

**Field Name** **Details**

```
TrialDays

TrialSourceOrgId

Username

```

Usage

**Type**
anyType

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The duration of the trial sign-up in days. Must be equal to or less than the trial days for the
approved Trialforce template. If not provided, it defaults to the trial duration specified for the
Trialforce template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the Trialforce Source Organization (TSO) from which the Trialforce
template was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The username of the admin user for the trial sign-up. It must follow the address convention
[specified in RFC822: www.w3.org/Protocols/rfc822/#z10.](http://www.w3.org/Protocols/rfc822/#z10)

The Java class uses REST API to create a SignupRequest object. It authenticates to the Trialforce Management Organization (TMO) and
then posts a request to the SignupRequest object.

Here are the variables to specify in this example.

**•** SERVER—The name of the host server for the TMO, for example, _`yourInstance`_ .salesforce.com.

**•** USERNAME—The admin username for the TMO.

**•** PASSWORD—The concatenation of the admin password and the security token for the TMO. To get an email with the security token,
from your personal settings in Salesforce, select **Reset My Security Token** and click **Reset Security Token** .

**•** CLIENT_ID—From Setup in Salesforce, in the Quick Find box, enter _`Apps`_, and then select **Apps** . Under Connected Apps, click **New** .
Enter values for the required fields (Callback URL is required, but you can initially set it to any valid URL because it’s not used). Grant
full access for the OAuth scopes in the Selected OAuth Scopes selector, and click **Save** . Then copy the value of Consumer Key and
use it for this variable.

**•** CLIENT_SECRET—On the same page, click **Click to reveal** . Then copy the value of Consumer Secret and use it for this variable.

```
public class IsvSignupDriver {

   private static final String SERVER = server_name : port ;

```


Standard Objects SignupRequest

```
      private static final String USERNAME = tmo_username ;

      private static final String PASSWORD = tmo_passwordsecurity_token ;

      private static final String CLIENT_ID = consumer_key ;

      private static final String CLIENT_SECRET = consumer_secret ;

      private static SignupRequestInfo signupRequest = null;

      public static String createSignupRequest (SignupRequestInfo sr)

       throws JSONException, IOException {

        JSONObject createResponse = null;

        signupRequest = sr;

        JSONObject loginResponse = login(SERVER, USERNAME, PASSWORD);

        String instanceUrl = loginResponse.getString("instance_url");

        String accessToken = loginResponse.getString("access_token");

        createResponse = create(instanceUrl, accessToken);

        System.out.println("Created SignupRequest object: " + createResponse + "\n");

        return createResponse.toString();

      }

      /* Authenticates to the TMO using the required credentials */

      private static JSONObject login(String server, String username, String password)

       throws ClientProtocolException, IOException, JSONException {

        String authEndPoint = server + "/services/oauth2/token";

        HttpClient httpclient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(authEndPoint);

           List<NameValuePair> params = new ArrayList<NameValuePair>();

           params.add(new BasicNameValuePair("grant_type", "password"));

           params.add(new BasicNameValuePair("client_id", CLIENT_ID));

           params.add(new BasicNameValuePair("client_secret", CLIENT_SECRET));

           params.add(new BasicNameValuePair("username", username));

           params.add(new BasicNameValuePair("password", password));

           post.setEntity(new UrlEncodedFormEntity(params, Consts.UTF_8));

           BasicResponseHandler handler = new BasicResponseHandler();

           String response = httpclient.execute(post, handler);

           return new JSONObject(response);

        } finally {

           httpclient.getConnectionManager().shutdown();

        }

      }

      /* Posts a request to the SignupRequest object */

      private static JSONObject create(String instanceUrl, String accessToken)

       throws ClientProtocolException, IOException, JSONException {

        HttpClient httpClient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(instanceUrl +

            "/services/data/v27.0/sobjects/SignupRequest/");

             post.setHeader("Authorization", "Bearer " + accessToken);

             post.setHeader("Content-Type", "application/json");

```


Standard Objects SignupRequest

```
             JSONObject requestBody = new JSONObject();

             requestBody.put("TemplateId", signupRequest.getTemplateID());

             requestBody.put("SignupEmail", signupRequest.getEmail());

             requestBody.put("username", signupRequest.getUsername());

             requestBody.put("Country", "US");

             requestBody.put("Company", signupRequest.getCompanyName());

             requestBody.put("lastName", signupRequest.getLastName());

             StringEntity entity = new StringEntity(requestBody.toString());

             post.setEntity(entity);

             BasicResponseHandler handler = new BasicResponseHandler();

             String response = httpClient.execute(post, handler);

             return new JSONObject(response);

        } finally {

           httpClient.getConnectionManager().shutdown();

        }

      }

   }

```

Error Codes

If the sign-up fails, the system generates an error code that can help you identify the cause. This table shows the most important error
codes.


### Standard Objects Site

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**•** SignupRequestFeed–Feed tracking is available for the object.

**•** SignupRequestHistory–History is available for tracked fields of the object.

**•** SignupRequestOwnerSharingRule–Sharing rules are available for the object

**•** SignupRequestShare–Sharing is available for the object.

### Site

Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.


Standard Objects Site

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
AdminId

AnalyticsTrackingCode

ArchiveStatus

ArchivedById

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The site administrator designated as the contact for the site. This user receives
site-related communications from site visitors and from Salesforce.

This is a relationship field.

**Relationship Name**
Admin

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking code associated with your site. This code can be used by services
like Google Analytics to track page request data for your site.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The archived status of a site. Possible values are:

**•** `NotArchived`

**•** `TemporaritlyArchived`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Site

**Field** **Description**

**Description**
The user that archived the site.

**Relationship Name:**
ArchivedBy

**Relationship Type:**
Lookup

**Refers To:**
User

```
ArchivedDate

ClickjackProtectionLevel

DailyBandwidthLimit

DailyBandwidthUsed

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the site was archived.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sets the clickjack protection level. The options are:

**•** `AllowAllFraming` —Allow framing by any page (no protection)

**•** `SameOriginOnly` —Allow framing by the same origin only
(recommended)

**•** `NoFraming` —Don’t allow framing by any page (most protection)

This field is available in API version 30.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily bandwidth limit for the sites in your organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Site

**Field** **Description**

**Description**
The current rolling 24-hour daily bandwidth usage for the sites in your
organization.

```
DailyRequestTimeLimit

DailyRequestTimeUsed

Description

GuestRecordDefaultOwnerId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily service request time limit for the sites in your
organization. Service request time is calculated as the total server time in minutes
required to generate pages for the site.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily service request time for the sites in your
organization.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
An optional description of the site.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user in the Salesforce org that is the default owner of records created by
unauthenticated (guest) users.

This is a relationship field.

**Relationship Name**
GuestRecordDefaultOwner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects Site

**Field** **Description**

```
GuestUserId

MasterLabel

MonthlyPageViewsEntitlement

Name

OptionsAllowGuestPaymentsApi

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The site or Experience Cloud sites specific user that anonymous, unauthenticated
users run as when interacting with the site.

This is a relationship field.

**Relationship Name**
GuestUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the site as it appears in the user interface.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views allowed for the current calendar month for the sites
in your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name used when referencing the site in the API.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
Indicates whether unauthenticated guest users can access the Payments API
( `true` ) or not ( `false` ). The default is `false` . This field is available in API version
49.0 and later.

```
OptionsAllowGuestSupportApi

OptionsAllowHomePage

OptionsAllowStandardAnswersPages

OptionsAllowStandardIdeasPages

OptionsAllowStandardLookups

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable unauthenticated users to access the Support API.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard page associated with the Home tab
( `/home/home.jsp` ).

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an answers Experience
Cloud site. If you want to use default Answers pages (such as AnswersHome),
enable these pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an Ideas Experience Cloud
site. If you want to use default Ideas pages (such as IdeasHome), enable these
pages.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable the standard lookup pages. These are the windows
associated with lookup fields on Visualforce pages.

```
OptionsAllowStandardPortalPages

OptionsAllowStandardSearch

OptionsBrowserXssProtection

OptionsCachePublicVfPagesInProxies

OptionsContentSniffingProtection

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable authenticated users to access the standard Salesforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard search pages. To allow public users to perform
standard searches, enable these pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the browser's cross-site scripting protection.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether proxy servers cache this site’s publicly available pages only for
unauthenticated guest users ( `true` ) or not ( `false` ). When this field is `false`,
this site’s cache-enabled Visualforce pages are cached in the web browser for
both authenticated and unauthenticated users. The default is `true` . See
[Configure Site Caching in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable content-sniffing protection.

```
OptionsCookieConsent

OptionsCspUpgradeInsecureRequests

OptionsEnableFeeds

OptionsHasStoredPathPrefix

OptionsRedirectToCustomDomain

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether only required Salesforce-supplied cookies are allowed within
the site ( `true` ) or all cookies types are allowed: required, functional, and
advertising ( `false` ). The default is `false` . This field is available in API version
52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
boolean

**Properties**
Filter

**Description**
The option that displays the Syndication Feeds related list, where you can create
and manage syndication feeds for users on your public sites. This field is visible
only if you have the feature enabled for your organization.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether this Experience Cloud site has a customized urlPathPrefix
( `true` ) or instead uses the Experience Cloud site's `UrlPathPrefix` plus `/s`
( `false` ). The default is `false` . In other sites, this field has no effect. This field
is available in API version 50.0 and later.

**Type**
boolean


Standard Objects Site

**Field** **Description**

**Properties**
Filter

**Description**
Indicates whether requests to this site’s system-managed URLs are redirected to
the HTTPS custom domain serving this site ( `true` ) or not ( `false` ).
System-managed site URLs end in `*.my.salesforce-sites.com` or
`*.my.site.com` . In Experience Cloud sites, the default is `false` . In Salesforce
Sites, the default is `true` .

If multiple custom domains serve this site and this field is set to true, requests
are routed to the site’s primary custom URL only if it’s an HTTPS custom domain.
Otherwise, requests are redirected to the first HTTPS custom domain associated
with this site, in alphanumeric order. If no HTTPS custom domain serves this site,
this option has no effect.

This field is available in API version 52.0 and later.

```
OptionsReferrerPolicyOriginWhenCrossOrigin

OptionsRequireHttps

SiteType

Status

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable referrer policy (origin-when-cross-origin).

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Identifies whether the site is a Visualforce (Salesforce Sites) or a Site.com site.
`SiteType` is available in API version 21.0 and later. In API version 26.0 and
later, if Experience Cloud sites are enabled for your Salesforce org, the site could
also be a Network Visualforce or Network Site.com site.

**Type**
picklist


Standard Objects Site

**Field** **Description**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status for the site. For example, `Active` or `In Maintenance` .

```
Subdomain

TopLevelDomain

UrlPathPrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If you enabled Salesforce Sites or Digital Experiences before you enabled enhanced
domains on your My Domain, this field returns this site’s previous subdomain.
For example, if your domain was `mycompany.force.com`, then
`mycompany` is the subdomain.

If you enabled Salesforce Sites or Digital Experiences after you enabled enhanced
domains, this field returns a null value.

**Type**
url

**Properties**
Filter, Nillable

**Description**
The optional branded custom Web address that you registered with a third-party
domain name registrar. The custom Web address acts as an alias to your Salesforce
address.

Beginning with API version 21.0, `TopLevelDomain` is no longer available.
Instead, use the Domain and DomainSite objects.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique Salesforce URL that the public uses to access this site.

Use this read-only object to query or retrieve information on your site.


### Standard Objects SiteDetail

Associated Objects

This object has the following associated objects. Unless noted, these associated objects are available in the same API version as this
object.

**SiteFeed**

Feed tracking is available for the object.

**SiteHistory**

History is available for tracked fields of the object.

### SiteDetail

Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
   GET

```

Fields

**Field** **Details**

```
DurableId

IsRegistrationEnabled

SecureUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Site object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the site allows users to sign up.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SiteDomain

**Field** **Details**

**Description**
The URL of the website.

Note: SiteDetail fields are exposed in SOAP API version 45.0 and later. You can use Tooling API to query for SiteDetail fields in
guest user mode in API version 44.0 and earlier. In API version 45.0 and later, use SOAP API to get this data in guest user mode.
SiteDetail is still exposed in Tooling API to User Profiles with the ViewSetup permission.

### SiteDomain SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API version

21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects instead.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
Domain

SiteId

```

**Type**
url

**Properties**
Filter, Sort

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects SiteEventLog

**Field** **Description**

**Description**
The ID of the associated Site.

```
DomainType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS. This field is available in
version 24.0 of the API.

Use this read-only object to query the domains that are associated with each site in your organization.

### SiteEventLog SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version 62.0

and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects SiteEventLog

**Field** **Details**

```
CpuTime

DatabaseTotalTime

HttpHeaders

HttpMethod

IsApi

IsError

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DB_CPU_TIME. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP headers that were sent in the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: GET, POST, PUT, and so on.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

The default value is `false` .

**Type**
boolean


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was an error page.

The default value is `false` .

```
IsFirstRequest

IsGuest

IsSecure

LoginKey

PageName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page is the first Visualforce transaction in the request.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was a guest (unauthenticated) request.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this request is secure.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
GeJCsym5eyvtEK2I.

**Type**
string


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Visualforce page that was requested.

```
QueryString

RequestIdentifier

RequestStatus

RequestType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query, if one was performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action. This field can have a blank
value.

For example:

**•** `S`  - Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F`  - Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U`  - Undefined.

**•** `A` —Authorization error.

**•** `R`  - Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

**Type**
String


Standard Objects SiteEventLog

**Field** **Details**

**Description**
The request type.

Possible values are:

**•** `page` —a normal request for a page

**•** `content_UI` —a content request for a page that originated in the user interface

**•** `content_apex` —a content request initiated by an Apex call

**•** `PDF_UI` —a request for a page in PDF format through the user interface

**•** `PDF_apex` —a request for PDF format by an Apex call (usually a Web Service call)

```
RunTime

SessionKey

SiteIdentifier

Timestamp

Uri

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Site.com site.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: `20130715233322.670` .

**Type**
string


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `home/home.jsp` .

```
UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943YAS` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.


### Standard Objects SiteHistory SiteHistory

Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.

To access this object, Salesforce Sites must be enabled for your organization.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer Portal users can't access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
DataType

Field

NewValue

OldValue

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType


### Standard Objects SiteIframeWhitelistUrl

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
The last value of the field before it was changed.

```
SiteId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

### SiteIframeWhitelistUrl

Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is available
in API version 44.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.


### Standard Objects SiteRedirectMapping

Fields

**Field Name** **Details**

```
SiteId

Url

### SiteRedirectMapping

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the site to include in the inline frame.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain allowed to frame your Salesforce site or Experience Cloud site page.
Accepts these formats: example, example.com, *example.com, and
https://example.com.

Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only if Digital Experiences is enabled for your org and Create and Set Up Experiences is enabled.


Standard Objects SiteRedirectMapping

Fields

**Field** **Details**

```
Action

IsActive

IsDynamic

SiteId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the redirect.

Possible values are:

**•** `Permanent`

**•** `Temporary`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the redirect is enabled.

Default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a redirect rule is dynamic.

Default value is `false` . This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the site for the redirect.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup


### Standard Objects Skill

**Field** **Details**

**Refers To**
Site

```
Source

Target

```

Usage

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the site you want to redirect.

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the Experience Cloud site you want to users to visit.

If you build a new site on Experience Cloud but you also have an old site on a different platform, ensure that users visit the new site. Use
SiteRedirectMapping to redirect users from the external site to the Experience Cloud site.

### Skill

Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available in
API version 24.0 and later.

Note: For information about WDC skills on a user's profile, see the ProfileSkill topic.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects Skill

**Field Name** **Details**

**Description**
The description of the skill.

```
DeveloperName

Language

LastViewedDate

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the skill.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the skill.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the skill.


### Standard Objects SkillLevelDefinition

**Field Name** **Details**

```
TypeId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The skill type associated with the skill.

This field is a relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
Type

**Refers To**
SkillType

**Chat**
Use this object to assign Chat users to groups based on their abilities. The skills associated with a LiveChatButton determine which
agents receive chat requests that come in through that button.

**Field Service**
Use this object to track certifications and areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page. When you assign a skill to a service resource,
you can specify their skill level and the duration of the skill.

**•** Add it as a required skill via the Skill Requirements related list on any work type, work order, or work order line item. When you
add a required skill to a work record, you can specify the skill level.

**Workforce Engagement**
Use this object to specify areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page.

**•** Add it as a required skill via the Skill Requirements related list on a job profile.

### SkillLevelDefinition

Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version
51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SkillLevelDefinition

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
Description

IsAutoApproved

LearningContent

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Describes the mapping.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this mapping auto-approves.

The default value is 'false'.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The titles of the Trailhead modules associated to this mapping.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the Skill Level Definition.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects SkillLevelProgress

**Field** **Details**

**Refers To**
Group, User

```
SkillId

### `SkillLevel`

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill that this mapping is for.

This is a relationship field.

**Relationship Name**
### Skill

**Relationship Type**
Lookup

**Refers To**
### Skill

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The level to assign for the skill.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelDefinitionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelDefinitionShare on page 67**
Sharing is available for the object.

### SkillLevelProgress

Represents training progress for a given user. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SkillLevelProgress

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
CompletedCount

CompletedDate

OwnerId

ServiceResourceId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of modules that have been completed towards this Skill Mapping.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this progress was completed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of skill level progress.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SkillLevelProgress

**Field** **Details**

**Description**
The Service Resource that will be granted a service resource skill when the progress is
complete.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
SkillLevelDefinitionId

SkillMasterLabel

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The corresponding skill mapping for this progress.

This is a relationship field.

**Relationship Name**
SkillLevelDefinition

**Relationship Type**
Lookup

**Refers To**
SkillLevelDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The master label of the Skill associated with the associated SkillLevelDefinition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the progress.

Possible values are:

**•** `A` —Approved


### Standard Objects SkillProfile

**Field** **Details**

**•** `R` —Review

### • S —Started

The default value is 'S'.

```
TotalCount

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total number of modules that need to be completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelProgressOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelProgressShare on page 67**
Sharing is available for the object.

### SkillProfile

Represents a join between Skill and Profile. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the profile.


### Standard Objects SkillRequirement

**Field Name** **Details**

```
SkillId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

Use this object to assign specific skills to specific profiles.

### SkillRequirement

Represents a skill that is required to complete a particular task in Field Service, Omni-Channel, Salesforce Scheduler, or Workforce
Engagement. Skill requirements can be added to pending service routing objects in Omni-Channel. They can be added to work types,
work orders, and work order line items in Field Service and Lightning Scheduler. And they can be added to job profiles in Workforce
Engagement. This object is available in API version 38.0 and later. You also can add skill requirements to work items in Omni-Channel
skills-based routing using API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

If you want to use SkillRequirement for Field Service use cases, then Field Service must be enabled.

If you want to use SkillRequirement only for Omni-Channel skills-based routing use cases, then you don't need Field Service to be enabled.

If you want to use SkillRequirement for Workforce Engagement use cases, then Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
IsAdditionalSkill

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects SkillRequirement

**Field Name** **Details**

**Description**
Indicates that a skill is additional. After a designated timeout period, a skill marked
as additional is dropped from Omni-Channel routing. The case is then routed to
the best-matched agent even if they don’t have all the skills.

```
LastReferencedDate

LastViewedDate

RelatedRecordId

SkillId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null,
this record might only have been referenced ( `LastReferencedDate` ) and
not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the skill is required for. The related record can be a work order,
work order line item, work type, or pending service routing record.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
WorkOrder, WorkOrderLineItem, WorkType

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SkillRequirement

**Field Name** **Details**

**Description**
The skill that is required.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

```
SkillLevel

SkillNumber

SkillPriority

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The level of the skill required. Skill levels can range from zero to 99.99. Depending
on your business needs, you can have the skill level to reflect years of experience,
certification levels, or license classes.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the skill requirement.

**Type**
int

**Properties**
Aggregatable, Create, Filter, Group, Nillable, Sort, Update

**Description**
For additional skills, specify the order in which skills are dropped if after the
specified timeout no agent with that skill is available. Higher priority-value skills
are dropped first. Lower priority-value skills, for example 0, are dropped last. Skills
with the same priority value are dropped as a group. You can set skill priority
using skills-based routing rules or Apex code.


### Standard Objects SkillUser

Usage

**Field Service**
Skill requirements help dispatchers assign work orders to service resources with the proper expertise. You can still assign a work order,
work order line item, or related service appointment to a service resource that does _not_ have the specified skills, so skill requirements
serve more as a suggestion than a rule.

Note: If you’re using the Field Service managed package, use matching rules to ensure that appointments are only assigned to
service resources who possess the skills listed on the parent work order.

If many of your work orders require the same skills, add skill requirements to work types to save time and keep your processes consistent.
When you add a skill requirement to a work type, work orders and work order line items that use that type automatically inherit the skill
requirement. For example, if all annual maintenance visits for your Classic Refrigerator product require a Refrigerator Maintenance skill
level of at least 50, add that skill requirement to the Annual Maintenance Visit work type. When you create a work order for a customer’s
annual fridge maintenance, applying that work type adds the skill requirement as well.

**Omni-Channel**

We recommend that you use Omni-Channel flow or skills-based routing rules to create skills-based routing requests. When you do so,
work items are routed by creating a PendingServiceRouting object. The PendingServiceRouting object can have multiple SkillRequirements
objects associated with it. When a work item requires multiple skills, it’s routed to an agent who has all of the required skills. The
PendingServiceRouting object adds attributes to the work item that represent the skill (skill id), priority, skill proficiency, and timestamp.

**Workforce Engagement**

Workforce Engagement uses skill requirements to assign shifts to agents who have the right skills. You can still assign shifts to service
resources if they don’t have those skills.

In a non-Omni workflow, create a scheduling rule that matches agents to shifts based on their skills and the job profile's skill requirements.
Shift scheduling tools can then assign agents with the right skills.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**SkillRequirementChangeEvent (API version 54.0)**
Change events are available for the object.

**SkillRequirementFeed**

Feed tracking is available for the object.

**SkillRequirementHistory**

History is available for tracked fields of the object.

### SkillUser

Represents a join between Skill and User. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`


### Standard Objects SlackChannelRelatedRecord

Fields

**Field Name** **Details**

```
SkillId

UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the user.

Use this object to assign specific skills to specific users.

### SlackChannelRelatedRecord

Represents the related record mapping between a Slack channel and a Salesforce record that’s made when you create a Salesforce
channel. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the related record mapping.


### Standard Objects SlaProcess

**Field** **Details**

```
RelatedRecord

SlackChannel

TopLevelTeam

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The Salesforce record ID associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack channel ID of the Salesforce channel associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack Enterprise org ID associated with the Salesforce channel.

Use this object to retrieve and query the related record mapping between a Slack channel and a Salesforce record. You can select this
object in Salesforce Flow Builder and Slack Workflow Builder to trigger actions when a Salesforce channel is created.

This object is read only. You can’t create, modify, or delete the related record mappings between Slack channels and Salesforce records
using this object.

### SlaProcess

Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.

An entitlement process is a timeline that includes all the steps (MilestoneType records) that your support team must complete to resolve
cases. Each process includes the logic necessary to determine how to enforce the correct service level for your customers.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`, `describeLayout()`


Standard Objects SlaProcess

Special Access Rules

As of Summer ’20 and later, only Salesforce admin users, users with access to the Case, Entitlement, or Work Order objects, and users
with the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
BusinessHoursId

Description

IsActive

IsVersionDefault

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
textarea

**Properties**
Filter, Nillable

**Description**
A description of the entitlement process.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the entitlement process is active ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the entitlement process is the default version ( `true` ) or not
( `false` ).

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
dateTime


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the SlaProcess was last viewed.

```
Name

NameNorm

SObjectType

StartDateField

```

**Type**
string

**Properties**
Filter, idLookup

**Description**
The name of the entitlement process.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The read-only value for the unique name of the entitlement process or the entitlement
process version. If entitlement versioning is enabled, this value is automatically
generated for each version of an entitlement process in this form: _`process`_
_`name`_ +_v + _`x`_, where _`x`_ is the version number (for example, “gold_support_v2”).

If entitlement versioning isn’t enabled, this value is the same as `Name` .

This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Restricted picklist, Filter, Group, Sort

**Description**
The type of records that the entitlement process can run on. Its values are:

**•** _`Case`_

**•** _`Work Order`_

An entitlement process runs only on records that match its type. For example, a Case
entitlement process that’s applied to an entitlement runs only on cases associated
with the entitlement, not on work orders. As a best practice, therefore, manage
customers’ work orders and cases on separate entitlements.

The field label in the user interface is Entitlement Process Type.

**Type**
picklist


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Restricted picklist

**Description**
The criteria for cases to enter the entitlement process. Cases can enter the process
based on:

**•** The creation date on a case

**•** A custom date/time field on a case

```
VersionMaster

VersionNotes

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence of versions to which this entitlement process belongs. This
field’s contents can be any value as long as it is identical among all versions of the
entitlement process.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the entitlement process version.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the entitlement process. Must be 1 or greater.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.


### Standard Objects Snippet

Usage

Use this object to query entitlement processes on entitlements.

SEE ALSO:

Entitlement

MilestoneType

CaseMilestone

### Snippet

Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates. This
object is available in API version 47.0 and later.

Supported Calls

`create(),delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
Description

DeveloperName

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the snippet. Limited to 32 KB.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This field value is unique to your org and is required for a Snippet to be resolved
in marketing content. Label is **API Name** .

**Type**
dateTime


Standard Objects Snippet

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

Type

Value

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the snippet.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of content a snippet includes. Allowable values are: Date, Image, Link, Text. This
field is for organizational purposes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body content of a snippet. This field can contain plain or rich text. The value of a snippet
is resolved when a marketing email is sent. The field does not support emojis, HTML, or image
files.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects SnippetAssignment

**SnippetFeed**

Feed tracking is available for the object.

### SnippetAssignment

Represents a relationship between a snippet and a campaign. Assignments are required to use snippet content in Account Engagement
emails and email templates. A snippet can be assigned to more than one campaign. This object is available in API version 47.0 and later.

Supported Calls

create( ), delete( ), describeLayout( ), describeSObjects( ), getDeleted( ), getUpdated( ), query( ), retrieve( )

Special Access Rules

Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
ParentId

SnippetId

### SoapApiEventLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related snippet record

SOAP API events contain details about your org's SOAP API request activity. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects SoapApiEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiType

ClientIp

ClientName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The name of the client that’s using Salesforce services. This field is an optional parameter
that can be passed in API calls. If blank, the caller didn't specify a client in the CallOptions
header.

```
CpuTime

DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

ExceptionMessage

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how much activity is occurring in the database. A high value for this field suggests
that adding indexes or filters on your queries would benefit performance.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

```
LoginKey

MethodName

ObjectName

RequestIdentifier

RequestSize

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the calling Apex method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request. For example: `Account`,
`Opportunity`, `Contact`, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The size of the callout request body, in bytes.

```
RequestStatus

ResponseSize

RowsProcessed

RunTime

```

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the request. For example: `150` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.


Standard Objects SoapApiEventLog

**Field** **Details**

```
SessionKey

Timestamp

Uri

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.


### Standard Objects SocialPersona

**Field** **Details**

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### SocialPersona

Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version 22.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AreWeFollowing

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a Salesforce social account is following the social persona or
not.


Standard Objects SocialPersona

**Field Name** **Details**

```
AuthorLabels

AvatarUrl

Bio

ExternalId

ExternalPictureURL

Followers

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Comma-separated list of author type tags.

**Type**
string

**Properties**
Nillable

**Description**
Retrieves the user's social network avatar. It's a read-only field and you can't
specify or update its value.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Biography of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona on the social network.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL to the picture of the social persona on the social network.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPersona

**Field Name** **Details**

**Description**
Number of followers that the social persona has.

```
Following

InfluencerScore

IsBlacklisted

IsDefault

IsFollowingUs

IsVerified

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of people that the social persona is following.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 score describing the influence of the social persona. No longer used.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is blacklisted or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona supplies the default avatar image that’s
displayed on the contact or account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is following a Salesforce social account or
not.

**Type**
boolean


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is verified or not.

```
LastReferencedDate

LastViewedDate

ListedCount

MediaProvider

MediaType

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network type of the social persona.

**Type**
string


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social persona.

```
NumberOfFriends

NumberOfTweets

ParentId

ProfileType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of friends that the social persona has.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of tweets made by the social persona.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact parent record for the social persona.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead, SocialPost

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of profile. Values are:

**•** `Person`

**•** `Page`


Standard Objects SocialPersona

**Field Name** **Details**

```
ProfileUrl

Provider

R6SourceId

RealName

SourceApp

TopicType

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Social network, such as Facebook or Twitter, of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Real name of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Salesforce product that created the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of topic, such as keyword or managed.


### Standard Objects SocialPost

Usage

The fields on a SocialPersona object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected a post from the social persona. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SocialPersonaHistory (API version 26.0)**
History is available for tracked fields of the object.

### SocialPost

Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AnalyzerScore

AssignedTo

AttachmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Score set on the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
User in Social Studio that the social post is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the first attachment on the social post. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `APPLICATION`

**•** `AUDIO`

**•** `IMAGE`

**•** `LINK`

**•** `TEXT`

**•** `UNKNOWN`

**•** `VIDEO`

```
AttachmentUrl

Classification

CommentCount

Content

DeletedById

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the first attachment on the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Classification for the social post, such as inquiry or customer case.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of comments on the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
If the social post is deleted, ID of the person who deleted the social post.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

```
EngagementLevel

ExternalPostId

Handle

HarvestDate

Headline

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Engagement level of the social post, such as reviewed or resolved.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social post in its social network.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Handle of the person who posted the social post.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when Social Studio collected the social post.

**Type**
string


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Headline of the social post.

```
HiddenById

InboundLinkCount

IsOutbound

KeywordGroupName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the social post is hidden, ID of the person who hid it.

This is a relationship field.

**Relationship Name**
HiddenBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of links on the inbound social post.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social post is outbound or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field that is no longer used.


Standard Objects SocialPost

**Field Name** **Details**

```
Language

LastReferencedDate

LastViewedDate

LikedBy

LikesAndVotes

MediaProvider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Language of the social post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the managed social account in the social network that liked the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 number of likes and votes on the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social post.


Standard Objects SocialPost

**Field Name** **Details**

```
MediaType

MessageType

Name

Notes

OutboundSocialAccountId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of social network of the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of message. Values are:

**•** `Comment` —Facebook comment

**•** `Direct` —Twitter direct message

**•** `Post` —Facebook post

**•** `Private` —Facebook private message

**•** `Reply` —Twitter or Facebook reply

**•** `Retweet` —Twitter retweet

**•** `Tweet` —Twitter tweet

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes added by Social Hub actions for the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the social account used for outbound social posts.


Standard Objects SocialPost

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
OutboundSocialAccount

**Relationship Type**
Lookup

**Refers To**
ExternalSocialAccount

```
OwnerId

ParentId

PersonaId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the social post.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent record of the social post, for example, the ID of a case.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
ID of the social persona who made the post.

This is a relationship field.

**Relationship Name**
Persona

**Relationship Type**
Lookup

**Refers To**
SocialPersona

```
PostPriority

PostTags

PostUrl

Posted

Provider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of the social post set in Social Studio.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of tags on the social post.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the social post.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Sort, Update

**Description**
Date and time when the social post was made.

**Type**
picklist


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Social network of the social post.

```
R6PostId

R6SourceId

R6TopicId

Recipient

RecipientType

ReplyToId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique ID of the post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the author in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for either the topic profile or the managed account in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recipient of the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the recipient of the social post, such as a person.

**Type**
reference


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Dynamically generated from replyToExternalPostId in Social Studio.

This is a relationship field.

**Relationship Name**
ReplyTo

**Relationship Type**
Lookup

**Refers To**
SocialPost

```
ResponseContextExternalId

ReviewScale

ReviewScore

ReviewedStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External ID, such as a conversation ID, author ID, or post ID, for the item you’re
responding to.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review scale for the social post.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review score for the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the social post review.


Standard Objects SocialPost

**Field Name** **Details**

```
Sentiment

Shares

SourceTags

SpamRating

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Sentiment of the social post. Values are:

**•** `Negative`

**•** `Neutral`

**•** `Positive`

**•** `SomewhatNegative`

**•** `SomewhatPositive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post has been shared.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of author type tags.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Spam rating of the social post. Values are:

**•** `NotSpam`

**•** `Spam`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
Status of the social post. Values are:

**•** `DELETED`

**•** `FAILED`

**•** `HIDDEN`

**•** `PENDING`

**•** `PENDING_APPROVAL`

**•** `RECALL_APPROVAL`

**•** `REJECTED_APPROVAL`

**•** `REPLIED`

**•** `SENT`

**•** `UNKNOWN`

```
StatusMessage

ThreadSize

TopicProfileName

TopicType

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status message for the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the topic profile for the social post in Social Studio.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of topic. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `Keyword`

**•** `Managed`

```
TruncatedContent

UniqueCommentors

ViewCount

WhoId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Truncated content of the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of unique people who commented on the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post was viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Polymorphic ID of a person such as a lead or a contact.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead


### Standard Objects Solution

Usage

The fields on a SocialPost object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected the post from the social network. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SocialPostChangeEvent (API version 48.0)**
Change events are available for the object.

**SocialPostFeed (API version 26.0)**
Feed tracking is available for the object.

**SocialPostHistory (API version 26.0)**
History is available for tracked fields of the object.

**SocialPostOwnerSharingRule**

Sharing rules are available for the object.

**SocialPostShare**

Sharing is available for the object.

### Solution

Represents a detailed description of a customer issue and the resolution of that issue.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsDeleted

IsHtml

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean


Standard Objects Solution

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution is an HTML solution ( `true` ) or not ( `false` ).

```
IsOutOfDate

IsPublished

IsPublishedInPublicKb

IsReviewed

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Read-only field that indicates whether a solution master has been updated since the translated
version was created ( `true` ) or not ( `false` ). Note that this field does not appear in the page
layout of master solutions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published ( `true` ) or not ( `false` ). A solution’s
published state does not affect how it can be used, or whether you can query, update, or
delete it. Label is **Public** . Prior to Spring ‘14, the label was **Visible in Self-Service Portal**

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published as a Public Solution ( `true` ) or not
( `false` ). Label is **Visible in Public Knowledge Base** .

This field only applies to solutions, not articles in the public knowledge base.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution has been reviewed ( `true` ) or not ( `false` ). This flag can
only be set indirectly via the `Status` picklist. Each predefined `Status` value implies an
`IsReviewed` value. Label is **Reviewed** .


Standard Objects Solution

**Field** **Details**

```
LastReferencedDate

LastViewedDate

OwnerId

ParentId

RecordTypeId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the Solution.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
ID of the master solution, if this is the translation of a master solution.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects Solution

**Field** **Details**

**Description**
ID of the RecordType to which the Solution is associated.

```
SolutionLanguage

SolutionName

SolutionNote

SolutionNumber

Status

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
The language that the solution is written in, such as `French` or `Chinese`
`(Traditional)` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. If a client application creates a new Solution and a value for this field is unspecified,
a hyphen (-), the default value for this field, is used. Limit: 255 characters. Label is **Title** .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the Solution record. Limit: 32,000 characters. Label is **Solution Details** . If you
have HTML Solutions enabled, any HTML tags used in this field are verified before the object
is created or updated. If invalid HTML is entered, an error is thrown. Any JavaScript used in
this field is removed before the object is created or updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An identifying number that is assigned automatically when a solution is created. It can’t be
set directly, and it can’t be modified.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects SolutionStatus

**Field** **Details**

**Description**
Required. The status of the solution. Directly controls the `IsReviewed` value. To obtain
the status values in the picklist, a client application can query the SolutionStatus.

```
TimesUsed

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times this solution has been used. Label is **Num Related Case** .

Use this object to manage your organization’s solutions. Client applications can create, update, delete, and query Attachment records
associated with a solution.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SolutionFeed (API version 18.0)**
Feed tracking is available for the object.

**SolutionHistory**

History is available for tracked fields of the object.

SEE ALSO:

CategoryData

CategoryNode

### SolutionStatus

Represents the status of a Solution, such as Draft, Reviewed, and so on.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects SolutionStatus

Fields

**Field** **Details**

```
ApiName

IsDefault

IsReviewed

MasterLabel

SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default solution status value ( `true` ) or not ( `false` ) in the
picklist. Only one value can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this solution status value represents a reviewed Solution ( `true` ) or not
( `false` ). Multiple solution status values can represent a reviewed Solution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this solution status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the solution status picklist. These numbers are not
guaranteed to be sequential, as some previous solution status values might have been
deleted.


### Standard Objects SolutionTag

Usage

This object represents a value in the solution status picklist. The solution status picklist provides additional information about the status
of a Solution, such as whether a given status value represents a reviewed or unreviewed solution. Your client application can query this
object to retrieve the set of values in the solution status picklist, and then use that information while processing Solution objects to
determine more information about a given solution. For example, the application could test whether a given case has been reviewed
or not based on its `Status` value and the value of the `IsReviewed` property in the associated SolutionStatus record.

SEE ALSO:

### Solution SolutionTag

Associates a word or short phrase with a Solution.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter


### Standard Objects SOSDeployment

**Field Name** **Details**

**Description**
ID of the parent TagDefinition object that owns the tag.

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

SolutionTag stores the relationship between its parent TagDefinition and the Solution being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### SOSDeployment

Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API
version 34.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SOSDeployment

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
Language

MasterLabel

OptionsIsBackwardFacingCameraEnabled

OptionsIsEnabled

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the deployment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether customers can use the backwards-facing camera on their
mobile devices to talk to SOS agents.

**Type**
boolean

**Properties**
Create, Filter, Update


### Standard Objects SOSSession

**Field Name** **Details**

**Description**
Determines whether the deployment is enabled for customers to request new
SOS video calls.

```
OptionsIsVoiceOnlyMode

QueueId

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether video functionality is disabled for customers, making it so
customers can only talk to SOS agents using only audio.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the queue that’s associated with the SOS deployment.

Use this object to query and manage SOS deployments.

### SOSSession

This object is automatically created for each SOS session and stores information about the session. This object is available in API versions
34.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AppVersion

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The version of the customer’s mobile application in which SOS is implemented.

```
CaseId

ContactId

DeploymentId

EndTime

IpAddress

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the SOS deployment that the SOS session originated from.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session ended.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
To protect the customer’s privacy, this field is now blank.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The date and time that the session record was last referenced by a user.

```
LastViewedDate

Name

OpentokSession

OwnerId

SessionDuration

SessionRecordingUrl

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the session.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The ID of the OpenTok session that’s associated with the SOS video call.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the session record’s owner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time that the SOS session lasted.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SOSSession

**Field Name** **Details**

**Description**
The URL where the SOS session recording is stored.

```
SosVersion

StartTime

SystemInfo

WaitDuration

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of SOS that was used in your organization’s mobile application when
this session occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session began.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the customer’s mobile device from which the SOS call
originated, such as the device’s operating system.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time the customer waited before an agent accepted the SOS
session and the call began.

Use this object to query and manage SOS session records.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects SOSSessionActivity

**SOSSessionFeed**

Feed tracking is available for the object.

**SOSSessionHistory**

History is available for tracked fields of the object.

**SOSSessionOwnerSharingRule**

Sharing rules are available for the object.

**SOSSessionShare**

Sharing is available for the object.

### SOSSessionActivity

Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object is
available in API version 34.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ActivityTime

Name

SessionId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the activity occurred.

**Type**
string

**Properties**
Autonumber, Defaulted on create, idLookup, Filter, Sort

**Description**
The name of the activity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the SOS session that’s associated with the event.


### Standard Objects StagedEmail

**Field Name** **Details**

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of activity that occurred.

Use this object to query and manage SOS session activities.

### StagedEmail

For internal use only.

### StagedInviteeEmail

Represents an email address that is included on a calendar event but that doesn’t match an existing user, contact, or lead record. This
object is available in API version 66.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on.

Fields

**Field** **Details**

```
Name

OwnerId

```

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The invited email address.

**Type**
reference


### Standard Objects StagedUnmtchdEmailAddr

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the record owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### StagedUnmtchdEmailAddr

Represents data about an email address identified by Einstein Activity Capture that doesn’t match to an existing user, contact, or lead
record. These addresses are only stored temporarily. Related to StagedUnmtchdEmailAddrRela, which represents data about the email
message or calendar event activity associated with an unmatched email. This object is available in API version 66.0 and later.

These addresses are only stored temporarily. An unmatched email address is automatically deleted from StagedUnmtchdEmailAddr if
it converts into a contact record. To convert, a user saves it from their Suggested Contacts list or the address crosses a threshold in the
automatic contact creation setting. An unmatched email address is also deleted after 30 days from the initial appearance without
subsequent activity.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.

Fields

**Field** **Details**

```
CreatedContactOrLeadId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the contact or lead record created from a suggestion. Read only.


Standard Objects StagedUnmtchdEmailAddr

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
CreatedContactOrLead

**Refers To**
Contact, Lead

```
EmailAddress

FirstName

IgnoreSuggestionEndDate

LastInteractionDate

LastName

```

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address of the suggested contact. This address doesn’t match any existing user,
contact, or lead. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
First name of the suggested contact.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If a user dismisses a suggestion, it isn't suggested again until this date.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the user last interacted with the unmatched email address through email or a
scheduled calendar event. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Last name of the suggested contact.


### Standard Objects StagedUnmtchdEmailAddrRela

**Field** **Details**

```
OccurrenceCount

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of times the user and the unmatched email address occur together. (Read
only.)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the user associated with the unknown email address. (Read only.)

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

### StagedUnmtchdEmailAddrRela

Represents data about the message or event activity associated with an email address that Einstein Activity Capture can’t match with
an existing user, contact, or lead record. Related to StagedUnmtchdEmailAddr, which represents data about the unmatched email
address. This object is available in API version 66.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.


Standard Objects StagedUnmtchdEmailAddrRela

Fields

**Field** **Details**

```
RelatedActivityId

SourceActivity

StagedUnmatchedEmailAddressId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related activity record, such as an email message or calendar event.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedActivity

**Refers To**
EmailMessage, Event, StagedEmail

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The activity type. Possible values are:

**•** `Event`

**•** `StagedEmail`

**•** `EmailAddress`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related unmatched email address record.

This field is a relationship field.

**Relationship Name**
StagedUnmatchedEmailAddress

**Relationship Type**
Master-detail

**Refers To**
StagedUnmtchdEmailAddr


### Standard Objects Stamp Stamp

Represents a User Specialty. This object is available in API version 39.0 and later.

Create User Specialty labels. Specialties can be any term you want, up to 50 characters, including spaces and underscores.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Description**

```
Description

MasterLabel

ParentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Use this field to describe what the user specialty means and how it applies to a
user. You have a 255 character maximum including spaces and underscores.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The User Specialty label that appears under the user’s profile picture. You can
create any label you want as long as it’s within the 50 character maximum,
including spaces and underscores.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id of the org or network.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Organization


### Standard Objects StampAssignment StampAssignment

Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.

Assign a User Specialty to users. This label appears beneath their profile photo.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
StampId

SubjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique id generated when creating a user specialty.

This is a relationship field.

**Relationship Name**
### Stamp

**Relationship Type**
Lookup

**Refers To**
### Stamp

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id for the user getting the User Specialty label.

This is a relationship field.

**Relationship Name**
Subject

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects StandardInvocableActionType StandardInvocableActionType

Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This object
is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Marketing Cloud Growth edition and the Manage Flow user permission or View Flows user permission are required.

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

Namespace

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name and namespace combination of the invocable action. This combination
must be unique.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code of the invocable action. For a full list of supported languages and their
[codes, see Supported Languages. This field is available in API version 60.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the invocable action. This display value is the internal label that doesn’t get
translated. This field is available in API version 60.0 and later.

**Type**
string


### Standard Objects StandardShippingRate

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the invocable action. Enter a value only if you’re using the invocable action
in Flow Builder or with Apex.

### StandardShippingRate

Standard shipping rate for a store. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The StandardShippingRate object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ConditionFactor

ConditionRangeMax

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Conditions that affect the shipping rate.

Possible values are:

**•** `OrderPriceFactor` —Condition based on the order price value.

**•** `OrderWeightFactor` —Condition based on delivery weight. This value is available
in API version 62.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum value of the shipping rate condition.


Standard Objects StandardShippingRate

**Field** **Details**

```
ConditionRangeMin

CurrencyIsoCode

Name

Price

ShippingCarrierMethodId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Minimum value of the shipping rate condition. This value can't be negative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the standard shipping rate.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Price of standard shipping.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shipping service carrier method. This field is available in API version 61.0 and later.

This field is a relationship field.


Standard Objects StandardShippingRate

**Field** **Details**

**Relationship Name**
ShippingCarrierMethod

**Relationship Type**
Lookup

**Refers To**
ShippingCarrierMethod

```
ShippingZoneId

TransitTimeMax

TransitTimeMin

TransitTimeUnit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping zone.

This field is a relationship field.

**Relationship Name**
ShippingZone

**Relationship Type**
Parent-detail

**Refers To**
ShippingRateArea (the master object)

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum value of the shipping transit time. This field is available in API version 61.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum value of the shipping transit time. This value can't be negative. This field is available
in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects StaticResource

**Field** **Details**

**Description**
Unit of value for shipping transit time. This field is available in API version 61.0 and later.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

```
WeightUnit

### StaticResource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of measurement for the weight of the cart items. This field is available in API version
62.0 and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

Represents a static resource that can be used in Visualforce markup.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Body

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Required. Encoded file data.


Standard Objects StaticResource

**Field** **Details**

```
BodyLength

CacheControl

ContentType

Description

Name

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the file (in bytes).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The sharing policy for the static resource when cached. The cache control can have one of
these values:

**•** `Private` specifies that the static resource is accessible to all authenticated users. The
static resource is stored on the Salesforce server in a user’s individual cache for the
duration of the session.

**•** `Public` specifies that the static resource is accessible after caching to all internet traffic,
including unauthenticated users. The resource is stored on the Salesforce server in a
shared cache, which results in faster load times.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Type of content. Label is **Mime Type** . Limit: 120 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the static resource. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the static resource.


Standard Objects StaticResource

**Field** **Details**

```
NamespacePrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

Use static resources to upload content that you can reference in Visualforce markup, including archives (such as .zip and .jar files), images,
stylesheets, JavaScript, and other files. Using a static resource is preferable to uploading a file to the Documents tab because:

**•** You can package a collection of related files into a directory hierarchy and upload that hierarchy as a .zip or .jar archive.

**•** You can reference a static resource in page markup by name using the `$Resource` global variable instead of hard-coding
document IDs.

Encoded Data

The API sends and receives the binary file data encoded as a base64 data type. Prior to creating a record, clients must encode the binary
file data as base64. Upon receiving an API response, clients must decode the base64 data to binary. The SOAP client usually handles this
conversion.


### Standard Objects StoreIntegratedService

Maximum Static Resource Size

You can create or update static resources to a maximum size of 5 MB. An organization can have up to 250 MB of static resources, total.

SEE ALSO:

ApexComponent

ApexPage

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

### StoreIntegratedService

Represents an association between an integration and a store. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The StoreIntegratedService object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Integration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The integration ID.

Possible values are:

**•** If the integration is a RegisteredExternalService:

**–** The ID of the RegisteredExternalService OR

**–** [ServiceProviderType]__[DeveloperName]

**•** ServiceProviderType: Price, Inventory, Tax, or Shipment

**•** DeveloperName of RegisteredExternalService

**•** If the integration is a PaymentGateway:

**–** The ID of the PaymentGateway

**•** If the integration is a Flow:


### Standard Objects StreamingChannel

**Field** **Details**

**–** [ServiceProviderType]__[NamespacePrefix]__[ApiName]

**–** If NamespacePrefix is null, it’s [ServiceProviderType]__[ApiName]

**•** ServiceProviderType: Flow

**•** ApiName and NamespacePrefix of FlowDefinitionView

**•** If the integration is the Salesforce Standard pricing:

**–** [ServiceProviderType]__B2B_STOREFRONT__StandardPricing

**•** ServiceProviderType: Price

```
ServiceProviderType

StoreId

### StreamingChannel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The type of integration service provider.

Possible values are:

**•** `Flow`

**•** `Inventory`

**•** `Payment`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique ID for the store.

Represents a channel that is the basis for notifying listeners of generic Streaming API events. This object is available in API version 29.0
and later.


Standard Objects StreamingChannel

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** You can create a permission set and grant users read and create access to all streaming channels in the org. This access isn’t for a
specific channel, like with user sharing.

**•** You can apply user sharing to StreamingChannel. You can restrict access to receiving or sending events on a channel by sharing
channels with specific users or groups. Channels shared with public read-only or read-write access send events only to clients
subscribed to the channel that also are using a user session associated with the set of shared users or groups. Only users with
read-write access to a shared channel can generate events on the channel, or modify the actual StreamingChannel record.

Fields

**Field** **Details**

```
Description

IsDynamic

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the StreamingChannel. Limit: 255 characters.

**Label:** Description

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the channel gets dynamically created on subscribe if necessary, `false` otherwise.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:


Standard Objects StreamingChannel

**Field** **Details**

```
LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Descriptive name of the streaming channel. Limit: 80 characters, alphanumeric
and “_”, “/” characters only. Must start with “/u/”. This value identifies the channel and must
be unique.

**Label:** Streaming Channel Name

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the streaming channel.

**Label:** Owner Name

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Dynamic Streaming Channel

Streaming API generic streaming supports dynamic streaming channel creation, which creates a StreamingChannel when a client first
subscribes to the channel. To enable dynamic streaming channels in your org, from Setup, enter _`User Interface`_ in the Quick


### Standard Objects Salesforce Surveys Object Model

Find box, then select **User Interface** . Enable **Enable Dynamic Streaming Channel Creation** . You can also enable dynamic channel
creation in Metadata API using EventSettings.

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/intro_stream.htm)_

### Salesforce Surveys Object Model

Learn about how Salesforce Surveys objects relate to one another in Salesforce.

[This diagram represents the object model for Salesforce Surveys. For more details and a larger image, visit the Data Model Gallery.](https://developer.salesforce.com/docs/platform/data-models/guide/salesforce-surveys.html)

### Survey

Represents a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the Survey object using the Object Manager.

Fields

**Field Name** **Details**

```
ActiveVersionID

```

**Type**
reference


Standard Objects Survey

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the survey version currently activated.

```
Description

DeveloperName

IsPartialSaveEnabled

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Nillable

**Description**
The description of the survey. This field isn’t visible in the UI.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The survey’s unique API name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to save the partial responses for the survey ( `true` ) or not
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey.


Standard Objects Survey

**Field Name** **Details**

```
LatestVersionId

Name

NamespacePrefix

OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the most recent version of this survey.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the survey that appears in the UI. This field is read-only from API
version 50.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who created the survey.


### Standard Objects SurveyEmailBranding

**Field Name** **Details**

```
SurveyType

TotalVersionsCount

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of the survey. The default value is Survey.

Possible values are:

**•** `ASSESSMENT`  - Survey type for sales enablement teams. Available from
API version 58.0 and later.

**•** `BASIC`  - Survey with a question page with like or dislike, long text, multiple
selection, NPS, rating, short text, and single selection questions, and without
inserted participant responses, display logic, and page branching logic.

**•** `SURVEY`  - Survey with all the available features.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of versions of the survey.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyChangeEvent on page 68**
Change events are available for the object.

**SurveyFeed (API version 42.0)**
Feed tracking is available for the object.

**SurveyOwnerSharingRule**

Sharing rules are available for the object.

**SurveyShare**

Sharing is available for the object.

### SurveyEmailBranding

Represents the configuration settings for invitation emails sent to survey participants for a particular survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects SurveyEmailBranding

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Note: You can’t define custom fields for the SurveyEmailBranding object using the Object Manager.

Fields

**Field Name** **Details**

```
Body

DeveloperName

FooterImageId

FromEmailAddress

HeaderImageId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The body text of the invitation email.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique API name of the email branding configuration.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the footer of the invitation email.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address that appears in the “From” field when the invitation is sent to
participants.

**Type**
reference


Standard Objects SurveyEmailBranding

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the header of the invitation email.

```
Language

MasterLabel

Subject

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the emails. Available languages include:

**•** Chinese (Simplified)

**•** Chinese (Traditional)

**•** Danish

**•** Dutch

**•** English

**•** Finnish

**•** French

**•** German

**•** Italian

**•** Japanese

**•** Korean

**•** Norwegian

**•** Portuguese (Brazilian)

**•** Russian

**•** Spanish

**•** Spanish (Mexican)

**•** Swedish

**•** Thai

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for these email configuration settings.

**Type**
string


### Standard Objects SurveyEngagementContext

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The subject of the invitation email.

### SurveyEngagementContext

Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API
version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Note: You can’t define custom fields for the SurveyEngagementContext object using the Object Manager.

Fields

**Field** **Details**

```
ContextType

ContextValue

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context type based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects SurveyInvitation

**Field** **Details**

**Description**
Name of the record.

```
OwnerId

### `SurveyInvitationId`

SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the record's owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey response.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyEngagementContextShare**

Sharing is available for the object.

### SurveyInvitation

Represents the invitation sent to a participant to complete the survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects SurveyInvitation

Fields

**Field Name** **Details**

```
CommunityId

ContactId

EmailBrandingId

InvitationLink

InviteExpiryDateTime

IsDefault

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that you want to send the survey to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact who received the invitation. This field is available in API v49.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the survey email branding object that’s associated with this invitation.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL to the survey that is sent to participants. To query on this field, you need
access to the associated Survey record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the survey invitation expires.

**Type**
boolean


Standard Objects SurveyInvitation

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether this is the default survey invitation to use when the survey
is sent to participants.

```
LastReferencedDate

LastViewedDate

LeadId

Name

OptionsAllowGuestUserResponse

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
survey invitation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead who received the invitation. This field is available in API v49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the survey invitation that appears in the UI.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects SurveyInvitation

**Field Name** **Details**

**Description**
Determines whether participants who don’t have a Salesforce account can
complete the survey.

```
OptionsAllowParticipantAccessTheirResponse

OptionsCollectAnonymousResponse

OwnerId

ParticipantId

ResponseStatus

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can access a copy of their responses after they
complete the survey.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can complete the survey anonymously.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the participant if the participant is a Salesforce contact, user, or lead.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a participant’s response to the survey that’s associated with the
survey invitation. Possible values include:

**•** `NotStarted`  - For an invitation with a `ParticipantID`, it means
that the recipient hasn’t opened the survey. For an invitation without the


Standard Objects SurveyInvitation

**Field Name** **Details**

`ParticipantID`, it means that none of the recipients have opened the
survey.

**•** `Started`                       - For an invitation with a `ParticipantID`, it means that
the recipient opened the survey. For an invitation without the
`ParticipantID`, it means that the survey has been opened by at least
one recipient.

**•** `Paused`                       - For an invitation with a `ParticipantID`, it means that the
recipient has paused the survey. For an invitation without the
`ParticipantID`, it means that the survey has been paused by any one
of the recipients. Paused isn't available for invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.

**•** `PartiallyCompleted`                       - For an invitation with a `ParticipantID`
field, it means that the recipient has partially completed the survey. For an
invitation without the `ParticipantID` field, it means that at least one
recipient has partially completed the survey. Available in API version 63.0
and later.

**•** `Completed`                       - For an invitation with a `ParticipantID`, it means that
the recipient has submitted the survey. For an invitation without the
`ParticipantID`, it means that the invitation has been submitted by at
least one recipient.

```
SurveyId

UUID

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the survey that’s sent in the invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique user ID that's added to a survey invitation generated for a contact,
lead,or user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SurveyPage

**Field Name** **Details**

**Description**
ID of the user who received the invitation. This field is available in API v49.0 and
later.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyInvitationChangeEvent (API version 62.0)**
Change events are available for the object.

**SurveyInvitationOwnerSharingRule**

Sharing rules are available for the object.

**SurveyInvitationShare**

Sharing is available for the object.

### SurveyPage

Represents a page, such as the title page or a question page, in a survey.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyPage object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of this SurveyPage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the survey page that appears in the UI.


### Standard Objects SurveyQuestion

**Field** **Details**

```
SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The version of the survey that the page belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyPageChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestion

Represents a question in a survey.

Supported Calls

`describeLayout()describeSObjects()getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestion object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

IsDeprecated

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the SurveyQuestion. The API name must be unique within a particular
version of the survey.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects SurveyQuestion

**Field** **Details**

**Description**
Indicates whether the question was deleted from the survey.

```
Name

PageDisplayOrder

PageName

QuestionChoiceCount

QuestionName

QuestionOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the page is displayed. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the page. This field is available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of choices for the question. This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
The label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SurveyQuestion

**Field** **Details**

**Description**
The order in which the question is displayed.

The label for the page. This field is available in API version 52.0 and later.

```
QuestionType

RelatedQuestionId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of question. Possible values include:

**•** `Boolean` —This value is available in API v49.0 and later.

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `FreeText`

**•** `Image`

**•** `Matrix` —This value is available in API v55.0 and later.

**•** `MultipleChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `RadioButton`

**•** `StackRank`

**•** `Rating`

**•** `ShortText` —This value is available in API v49.0 and later.

**•** `Slider`

**•** `Toggle`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent question. This field is blank when the question itself is the parent question.
This field is available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.


Standard Objects SurveyQuestion

**Field** **Details**

```
SubQuestionDisplayOrder

 SurveyPageId

 SurveyVersionId

ValidationType

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed within the parent question. This field is available
in API v55.0 and later, with Feedback Management - Starter and Feedback Management Growth licenses.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Lookup to the SurveyPage that contains the question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the question belongs to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The validations available for the short-text question. Possible values include:

**•** Custom - Cu

**•** Number - Nu

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChangeEvent on page 68**
Change events are available for the object.


### Standard Objects SurveyQuestionChoice SurveyQuestionChoice

Represents an answer choice that a participant can select for a survey question.

Supported Calls

`describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionChoice object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

DisplayOrder

IsDeprecated

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of the SurveyQuestionChoice object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question choice is displayed within the parent question. This field is
available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a question choice was deleted from the survey.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A label for the question choice that appears in the UI.


### Standard Objects SurveyQuestionResponse

**Field** **Details**

```
QuestionId

SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyQuestion object that this choice belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the survey that this question choice belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChoiceChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionResponse

Represents a participant’s answer to a specific question.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionResponse object using the Object Manager.

Fields

**Field** **Details**

```
ChoiceValue

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for the following question types:


Standard Objects SurveyQuestionResponse

**Field** **Details**

**•** Multiple choice

**•** Picklist

**•** Radio

**•** Ranking

```
Datatype

DateTimeValue

DateValue

InvitationId

IsTrueOrFalse

```

**Type**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type of the question response. Possible values are:

**•** `Boolean` This value is available in API v49.0 and later.

**•** `Date`

**•** `Double`

**•** `Int`

**•** `Number`

**•** `String`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date time.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyInvitation that was sent to the survey participant.

**Type**
boolean


Standard Objects SurveyQuestionResponse

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Response provided by a participant for a question type which has only two possible values:
True and False.

```
NumberValue

QuestionChoiceId

QuestionId

Rank

ResponseId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Net Promoter Score (NPS)

**•** Rating

**•** Score

**•** Slider

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of SurveyQuestionChoice that a participant chose in response to a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyQuestion that a participant provided an answer for.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank provided by a participant for an answer choice for the ranking question type.

**Type**
reference


### Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyResponse that is the parent of this SurveyQuestionResponse.

```
 ResponseShortText

 ResponseValue

 SurveyVersionId

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the response provided by a participant for a text type question.

**Type**
textarea

**Properties**
Nillable

**Description**
Response provided by a participant for a question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the response belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionResponseChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionScore

Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring,
[slider, and Net Promoter Score](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/product-specific-terms/net-promoter-and-nps.pdf) [®] (NPS [®] ).

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`


Standard Objects SurveyQuestionScore

Note: You can’t define custom fields for the SurveyQuestionScore object using the Object Manager.

Fields

**Field** **Details**

```
CumulativeScore

DateResponse

Name

QuestionChoiceId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the responses provided by all the participants for a question of the following types:
rating, scoring, and slider. For a question of the type ranking, sum of the weights provided
by all the participants for each item.

Note: This field is only applicable for the overall score type.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date selected by one or more participants for a question of the type date.

Note: This field is only applicable for the individual score type.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
For an overall score type record:

**•** Name of a question.

**•** Name of an item in a question of the type ranking.

For an individual score type record:

**•** Name of an item in a question of the type ranking.

**•** Name of a question of the type date.

**•** Response provided by one or more participants for questions of the following types:
picklist, multiple choice, rating, ranking, score, slider, NPS.

**Type**
reference


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the answer choice selected by one or more participants. For an individual
score type record, this field is applicable for questions of the following types: picklist, radio,
multi choice, ranking and rating. For an overall score type record, this field is applicable for
questions of the type ranking.

```
QuestionDeveloperName

QuestionId

QuestionName

QuestionSkippedCount

ResponseCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the question for which response is recorded. The API name must be unique
within a particular version of the survey.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the question for which response is recorded.

**Type**
textarea

**Properties**
Nillable

**Description**
Name of the question for which response is recorded.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of participants who didn’t respond to the question.

Note: This field is only applicable for the overall score type.

**Type**
int


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
For an overall score type record, number of participants who responded to the question. For
an individual score type record, number of participants who selected a particular answer
choice.

```
ResponseValue

Score

ScoreType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Answer choice selected by one or more participants for a question of the following types:
rating, slider, score, NPS. Rank provided by the participant for an item in a question of the
type ranking.

Note: This field is only applicable for the individual score type.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For an individual score type record, percentage of participants who selected a particular
answer choice.

Note: For questions of the type ranking, the percentage of participants who have
provided the same rank to an item.

For overall score type record:

**•** Average score of questions of the following question types: rating, scoring, and slider.

**•** Score of an NPS type question.

**•** Average weight provided by all participants for each item in question of the type ranking.

**•** Number of participants who responded to the question for the following question types:
date, radio, multi choice, and picklist.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the score calculated for a record. Possible values are:

**•** `Individual`


### Standard Objects SurveyResponse

**Field** **Details**

**•** `Overall`

```
 SurveyId

 SurveyInvitationId

 SurveyVersionId

### SurveyResponse

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey that contains the question for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey version for which scores are calculated.

Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and
when the survey was completed.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```

Note: You can’t define custom fields for the SurveyResponse object using the Object Manager.

Fields

**Field Name** **Details**

```
CompletionDateTime

```

**Type**
dateTime


Standard Objects SurveyResponse

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the participant completed the survey.

```
DataMapperExecutionStatus

InterviewGuid

InterviewId

InvitationId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of all the survey data maps after a response is received. This field is available
in API v49.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

Possible values are:

**•** `Pending`

**•** `InProgress`

**•** `Success`

**•** `Error`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable

**Description**
An automatically-generated, unique ID for a saved survey response.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FlowInterview object that’s associated with this response.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyInvitation object that’s associated with this response.


Standard Objects SurveyResponse

**Field Name** **Details**

```
IpAddress

Language

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the device the participant used to take the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language that the participant used to complete the survey.

Possible values are:

**•** `af` —Afrikaans

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)

**•** `ar_EG` —Arabic (Egypt)

**•** `ar_IQ` —Arabic (Iraq)

**•** `ar_JO` —Arabic (Jordan)

**•** `ar_KW` —Arabic (Kuwait)

**•** `ar_LB` —Arabic (Lebanon)

**•** `ar_LY` —Arabic (Libya)

**•** `ar_MA` —Arabic (Morocco)

**•** `ar_OM` —Arabic (Oman)

**•** `ar_QA` —Arabic (Qatar)

**•** `ar_SA` —Arabic (Saudi Arabia)

**•** `ar_SD` —Arabic (Sudan)

**•** `ar_SY` —Arabic (Syria)

**•** `ar_TN` —Arabic (Tunisia)

**•** `ar_YE` —Arabic (Yemen)

**•** `bg` —Bulgarian

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `da` —Danish

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `en_AU` —English (Australian)

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

**•** `es_CR` —Spanish (Costa Rica)

**•** `es_DO` —Spanish (Dominican Republic)

**•** `es_EC` —Spanish (Ecuador)

**•** `es_GT` —Spanish (Guatemala)

**•** `es_HN` —Spanish (Honduras)

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)

**•** `es_PA` —Spanish (Panama)

**•** `es_PE` —Spanish (Peru)

**•** `es_PR` —Spanish (Puerto Rico)

**•** `es_PY` —Spanish (Paraguay)

**•** `es_SV` —Spanish (El Salvador)

**•** `es_US` —Spanish (United States)

**•** `es_UY` —Spanish (Uruguay)


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `es_VE` —Spanish (Venezuela)

**•** `et` —Estonian

**•** `eu` —Basque

**•** `fa` —Farsi

**•** `fi` —Finnish

**•** `fr` —French

**•** `fr_BE` —French (Belgium)

**•** `fr_CA` —French (Canadian)

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo

**•** `mk` —Macedonian

**•** `ml` —Malayalam

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that another Salesforce object last referenced this
SurveyResponse object.


Standard Objects SurveyResponse

**Field Name** **Details**

```
LastViewedDate

Latitude

Location

Longitude

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that someone last viewed this SurveyResponse object.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude of the participant’s location.

**Type**
location

**Properties**
Nillable

**Description**
The latitude and longitude coordinates of the participant’s location.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude of the participant’s location.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the participant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:


Standard Objects SurveyResponse

**Field Name** **Details**

**•** NotStarted — The participant hasn't opened the survey.

**•** Started — The participant has opened the survey.

**•** Paused — The participant has paused the survey. Paused isn't available for
invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.

**•** PartiallyCompleted — The participant has partially completed the survey.
Available in API version 63.0 and later.

**•** Completed — The participant has completed the survey.

```
SubmitterId

SurveyId

SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user, contact, or lead who completed the survey.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey that the participant completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the version of the survey that the participant completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects SurveySubject

**SurveyResponseChangeEvent on page 68**
Change events are available for the object.

### SurveySubject

Represents a relationship between a survey and another object, such as an account or a case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

ParentId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the SurveySubject record was last referenced by another
object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the SurveySubject record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the SurveySubject record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects SurveySubject

**Field Name** **Details**

**Description**
Unique identifier of the SurveyInvitation object or SurveyResponse object that is
associated with this survey-object relationship.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
SurveyInvitation, SurveyResponse

```
SubjectEntityType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object that the survey is associated with. Possible values include:

**•** _`Account`_

**•** _`Asset`_

**•** _`Banker`_

**•** _`BranchUnit`_

**•** _`BranchUnitBusinessMember`_

**•** _`BranchUnitCustomer`_

**•** _`BusinessLicenseApplication`_

**•** _`BusinessMilestone`_

**•** _`Campaign`_

**•** _`CareProgram`_

**•** _`Case`_

**•** _`Claim`_

**•** _`ClaimParticipant`_

**•** _`Contact`_

**•** _`Employee`_

**•** _`Event`_

**•** _`Incident`_

**•** _`IndividualApplication`_

**•** _`InsurancePolicy`_

**•** _`InsurancePolicyParticipant`_

**•** _`Lead`_

**•** _`LearningItemSubmission`_ —Available in API version 58.0 and later.

**•** _`LiveChatTranscript`_


Standard Objects SurveySubject

**Field Name** **Details**

**•** _`LoyaltyProgram`_

**•** _`LoyaltyProgramMember`_

**•** _`LoyaltyProgramPartner`_

**•** _`MaterialityStakeholder`_

**•** _`MessagingSession`_

**•** _`Opportunity`_

**•** _`Order`_

**•** _`PersonalLifeEvent`_

**•** _`Producer`_

**•** _`Product2`_

**•** _`Promotion`_

**•** _`RebateProgram`_

**•** _`RetailStore`_

**•** _`ServiceAppointment`_

**•** _`ServiceResource`_

**•** _`Solution`_

**•** _`Task`_

**•** _`TransactionJournal`_

**•** _`User`_

**•** _`VideoCall`_

**•** _`Visit`_

**•** _`VoiceCall`_

**•** _`VolunteerProject`_

**•** _`WorkOrder`_

**•** Custom Objects

```
SubjectId

SurveyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the object that’s associated with the survey.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects SurveyVersion

**Field Name** **Details**

**Description**
Unique identifier of the survey that’s associated with the record that’s represented
by `SubjectId` .

```
SurveyInvitationId

SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation that's associated with another object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey response that's associated with another object.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveySubjectChangeEvent (API version 62.0)**
Change events are available for the object.

### SurveyVersion

Represents a version of a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the SurveyVersion object using the Object Manager.

Fields

**Field Name** **Details**

```
BrandingSetId

```

**Type**
reference


Standard Objects SurveyVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the branding set associated with the survey version.

```
Description

IsTemplate

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of this survey version.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the survey version is a template. Template surveys are
automatically shared with all users in your Salesforce org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey
version.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey version.

**Type**
string

**Properties**
Filter, Group, Sort

Filter, Group, Sort

Filter, Group, idLookup, Sort


### Standard Objects SurveyVersionAddlInfo

**Field Name** **Details**

**Description**
The name of the survey that appears in the UI.

```
SurveyId

SurveyStatus

VersionNumber

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey associated with the survey version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The version number of the survey.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyVersionChangeEvent on page 68**
Change events are available for the object.

### SurveyVersionAddlInfo

Represents additional information about a survey version. This information defines the default settings of a survey version. This object
is available in API version 49.0 and later.


Standard Objects SurveyVersionAddlInfo

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
EmailSender

EmailTemplateId

EngagementContextMetadata

InvitationSharingRole

Language

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The organization-wide email address used to send a survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email template that's used to send an automated survey invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom metadata created to get the engagement context from the participants.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the users that share edit access to a survey invitation.

Possible values are:

**•** `InvitationRecordCreator`  - Owner of the record that's associated with a
survey invitation.

**•** `SurveyOwner`

**Type**
picklist


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Language used to create the survey.

Possible values are:

**•** `af` —Afrikaans

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)

**•** `ar_EG` —Arabic (Egypt)

**•** `ar_IQ` —Arabic (Iraq)

**•** `ar_JO` —Arabic (Jordan)

**•** `ar_KW` —Arabic (Kuwait)

**•** `ar_LB` —Arabic (Lebanon)

**•** `ar_LY` —Arabic (Libya)

**•** `ar_MA` —Arabic (Morocco)

**•** `ar_OM` —Arabic (Oman)

**•** `ar_QA` —Arabic (Qatar)

**•** `ar_SA` —Arabic (Saudi Arabia)

**•** `ar_SD` —Arabic (Sudan)

**•** `ar_SY` —Arabic (Syria)

**•** `ar_TN` —Arabic (Tunisia)

**•** `ar_YE` —Arabic (Yemen)

**•** `bg` —Bulgarian

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh

**•** `da` —Danish

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `en_AU` —English (Australian)


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

**•** `es_CR` —Spanish (Costa Rica)

**•** `es_DO` —Spanish (Dominican Republic)

**•** `es_EC` —Spanish (Ecuador)

**•** `es_GT` —Spanish (Guatemala)

**•** `es_HN` —Spanish (Honduras)

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)

**•** `es_PA` —Spanish (Panama)

**•** `es_PE` —Spanish (Peru)

**•** `es_PR` —Spanish (Puerto Rico)

**•** `es_PY` —Spanish (Paraguay)

**•** `es_SV` —Spanish (El Salvador)

**•** `es_US` —Spanish (United States)

**•** `es_UY` —Spanish (Uruguay)

**•** `es_VE` —Spanish (Venezuela)

**•** `et` —Estonian

**•** `eu` —Basque

**•** `fa` —Farsi

**•** `fi` —Finnish

**•** `fr` —French

**•** `fr_BE` —French (Belgium)

**•** `fr_CA` —French (Canadian)


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo

**•** `mk` —Macedonian

**•** `ml` —Malayalam

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
Name

SurveyQuestionId

SurveyVersionId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the survey question embedded in the email template used to send automated survey
invitations.

**Type**
reference


### Standard Objects SvcCatalogCategory

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the survey version. This field is unique within your organization

### SvcCatalogCategory

Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
DeveloperName

ImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique developer name for the catalog item category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Allows a builder to pick an image displayed in the catalog.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup


Standard Objects SvcCatalogCategory

**Field** **Details**

**Refers To**
ContentAsset

```
IsActive

Language

ParentCategoryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows service catalog builders to deprecate categories or create in-draft categories.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

**Type**
reference


### Standard Objects SvcCatalogCategoryItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Parent category of this category. Allows categories to be grouped up to a max depth of 3.

This field is a relationship field.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
### SvcCatalogCategory

```
SortOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the order that the category is displayed to the end user.

### SvcCatalogCategoryItem

Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This
object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
IsPrimaryCategory

```

**Type**
boolean


Standard Objects SvcCatalogCategoryItem

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the category is the primary category for a catalog item.

The default value is `false` .

```
SortOrder

SvcCatalogCategoryId

SvcCatalogItemDefId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the order in which catalog items appear by default when you're viewing all items
in a single category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the category for which the service category item belongs.

This field is a relationship field.

**Relationship Name**
SvcCatalogCategory

**Relationship Type**
Lookup

**Refers To**
SvcCatalogCategory

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service category item definition.

This field is a relationship field.

**Relationship Name**
SvcCatalogItemDef

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef


### Standard Objects SvcCatalogFilterCriteria SvcCatalogFilterCriteria

Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API version
60.0 and later.

Supported SOAP API Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Supported REST API Methods

```
   DELETE, GET, HEAD, PATCH, POST, Query

```

Special Access Rules

To access this object, get the Service Catalog Access permission set license.

Fields

**Field** **Details**

```
CriteriaRelation

Description

DeveloperName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Possible values are:

**•** `AllConditionsAreMet`

**•** `AnyConditionIsMet`

**Type**
textarea

**Properties**
Nillable

**Description**
A description that states the restriction placed on a user’s access to a catalog items eligibility.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:


Standard Objects SvcCatalogFilterCriteria

**Field** **Details**

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
FullName

IsActive

Language

```

**Type**
string

**Properties**
Create, Group, Nillable

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies if the eligibility rule is active.

The default value is `false` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Supported languages for eligibility rules

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean


Standard Objects SvcCatalogFilterCriteria

**Field** **Details**

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
ManageableState

MasterLabel

Metadata

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the manageable state of a catalog item that is contained in a package.

Possible values are:

**•** `beta` —Managed-Beta

**•** `deleted` —Managed-Proposed-Deleted

**•** `deprecated` —Managed-Proposed-Deprecated

**•** `deprecatedEditable` —SecondGen-Installed-Deprecated

**•** `installed` —Managed-Installed

**•** `installedEditable` —SecondGen-Installed-Editable

**•** `released` —Managed-Released

**•** `unmanaged` —Unmanaged

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the eligibility rule record.

**Type**
complexvalue

**Properties**
Create, Nillable, Update

**Description**
The metadata type associated with the SvcCatalogFilterCriteria object.


### Standard Objects SvcCatalogItemDef

**Field** **Details**

```
NamespacePrefix

NumOfRelatedItems

### SvcCatalogItemDef

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of catalog items that has the eligibility rule.

Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The definition of the catalog item. This field is visible on the Service Catalog page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Description**
The unique developer name for the catalog item.

```
FlowName

FulfillmentFlowId

ImageId

ImageReference

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow called when the user navigates to the request page for the catalog item. Available
in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the fulfillment flow. Available in API version 56.0 and later.

This field is a relationship field.

**Relationship Name**
FulfillmentFlow

**Relationship Type**
Lookup

**Refers To**
SvcCatalogFulfillmentFlow

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The image ID used for the catalog item.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
string


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Derived field from `ImageId` to expose `ContentAssetId` on item definitions. Available
in API version 61.0 and later.

```
InternalNotes

IsActive

IsAvailableToAllCustomers

IsFeatured

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A place for the Service Catalog Builder to leave internal notes about the catalog item.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived field from `Status` to indicate whether the service catalog item is active.

The default value is `false` .

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Udpate

**Description**
Indicates whether the Service Catalog item is available to all customers. The default value is
`false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a catalog item is marked as a favorite for the org. Favorites display as a
featured item on the Service Catalog home page.

The default value is `false` .


Standard Objects SvcCatalogItemDef

**Field** **Details**

```
IsGuestAccessible

IsOutOfSync

Language

Product

ShortDescription

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Service Catalog item can be accessed by guest users. The default value
is `false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fulfillment flow that the Service Catalog item is based on has been
updated. Available in API version 58.0 and later.

The default value is `false` . If value is `true`, try updating and saving the service catalog
item again.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Supported languages for catalog items.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The product associated with the Service Catalog item. The value is derived from `UsageType` .
Available in API version 59.0 and later.

Possible values are:

**•** `FinancialServices`

**•** `ServiceCatalog` —Default

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
The short description of the catalog item.

```
Status

UsageType

### SvcCatalogRequest

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows the Service Catalog Builder to control whether the flow is displayed to users within
the Service Catalog.

Possible values are:

**•** `Deprecated`

**•** `Draft` —Default

**•** `PendingChanges`

**•** `Published`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business type for which the Service Catalog is used. Available in API version 57.0 and
later.

Possible values are:

**•** `CustomerService`

**•** `Employee` —Default

**•** `FinancialServices`

**•** `Industry`

Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects SvcCatalogRequest

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
CatalogItemDescription

CatalogItemName

CatalogItemVersion

ClosedDate

CurrencyIsoCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description for the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Version for the catalog item.

This is a calculated field. Available in API version 58.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was closed. This field is automatically populated when
`IsClosed` is 'true'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
ISO code of the currency. Must be one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as USD, GBP, or JPY. Must be unique within your
organization. Default value is `USD` -U.S. Dollar.

```
FlowInterviewGuid

IsClosed

ItemFlowVersion

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique GUID associated with the automation that was executed as part of the catalog item.
Available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the request has been resolved. This field is automatically checked when
`ClosedDate` is populated.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Version for the item flow.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
Name

OwnerId

Status

SubmitterId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Service Catalog request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID for the owner record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service catalog request. Available in API version 60.0 and later.

Possible values are:

**•** `CompletedExecution` —Default

**•** `CreatedRequest`

**•** `StartedExecution`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SvcCatalogRequest

**Field** **Details**

**Description**
ID for the submitter record.

This is a relationship field.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
User

```
SvcCatalogItemDefinitionId

TargetCustomerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The catalog item that was used to create this request.

This is a relationship field.

**Relationship Name**
SvcCatalogItemDefinition

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer ID that the request was submitted for. For example, when an agent runs a
catalog item for a given contact, the contact is represented by the `TargetCustomerId` .
Available in API version 61.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
TargetCustomer

**Relationship Type**
Lookup

**Refers To**
Contact, User


### Standard Objects SvcCatalogReqRelatedItem SvcCatalogReqRelatedItem

Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Name

RelatedExternalId

RelatedInternalRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the related item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text containing an ID from any external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce record related to this request. This reference must be for an object that has
the following characteristics.

**•** It's a standard object.

**•** It must allow custom fields.

**•** It's referencable (that is, it can be the target of a lookup).

**•** It can be the target of a custom lookup field.


### Standard Objects Swarm

**Field** **Details**

**•** It contains a Name field.

**•** It isn't dependent on a junction object.

**•** It isn't a virtual object or a setup object.

This is a polymorphic relationship field.

**Relationship Name**
RelatedInternalRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssociatedLocation, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, BusinessBrand, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, Contract, ContractLineItem, Customer, DataUseLegalBasis,
DataUsePurpose, Employee, EngagementChannelType, Entitlement, Idea, Individual,
InternalOrganizationUnit, Lead, Location, MessagingEndUser, Opportunity, Order, OrderItem,
PartyConsent, Pricebook2, ProcessException, Product2, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, QuickText, Recommendation, Seller, ServiceContract, SocialPersona, SocialPost,
Solution, SurveyInvitation, SurveySubject, UserProvisioningRequest, VoiceCall

```
SvcCatalogRequestId

### Swarm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The SvcCatalogRequest record.

This is a relationship field.

**Relationship Name**
SvcCatalogRequest

**Relationship Type**
Lookup

**Refers To**
SvcCatalogRequest

Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem
can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.


Standard Objects Swarm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
CollaborationRoomId

CollaborationTool

CollaborationUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the collaboration room.

This field is a relationship field.

**Relationship Name**
CollaborationRoom

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tool used for swarming.

Possible values are:

**•** `None`

**•** `Slack`

The default value is `None` .

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Swarm

**Field** **Details**

**Description**
URL of the Slack channel or thread.

```
EndedDateTime

HelpNeeded

IsDedicatedChannel

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm ended.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the swarm is happening in a dedicated channel ( `true` ) or in an existing channel
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.


Standard Objects Swarm

**Field** **Details**

```
MessageKey

Name

OwnerId

RelatedRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Slack thread or message.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the swarm owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup


Standard Objects Swarm

**Field** **Details**

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

```
StartedDateTime

Status

UsageType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm started.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

**•** `Waiting (Custom)`

The default value is `New` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of swarm.

Possible values are:

**•** `CareMgmt` —Care Coordination

**•** `DealRoom` —Sales Channel

**•** `PartnerChannel` —Partner Account Channel

**•** `Swarming`

The default value is `Swarming` .


### Standard Objects SwarmMember

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmFeed on page 55**
Feed tracking is available for the object.

**SwarmHistory on page 63**
History is available for tracked fields of the object.

**SwarmOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmShare on page 67**
Sharing is available for the object.

### SwarmMember

Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
AssignedDateTime

CompletedDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member is added to the swarm.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member exits the swarm or the swarm closes.


Standard Objects SwarmMember

**Field** **Details**

```
HelpNeeded

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm or record number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce user assigned to a swarm.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


Standard Objects SwarmMember

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RelatedRecordId

Status

SwarmId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm member or swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

The default value is `New` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the swarm the member belongs to.

This field is a relationship field.


### Standard Objects TabDefinition

**Field** **Details**

**Relationship Name**
Swarm

**Relationship Type**
Lookup

**Refers To**
Swarm

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmMemberFeed on page 55**
Feed tracking is available for the object.

**SwarmMemberHistory on page 63**
History is available for tracked fields of the object.

**SwarmMemberOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmMemberShare on page 67**
Sharing is available for the object.

### TabDefinition

Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Unique identifier for the tab. Always retrieve this value before using it, because
the value isn’t guaranteed to stay the same from one release to the next. Simplify
queries by using this field instead of making multiple queries.


Standard Objects TabDefinition

**Field Name** **Details**

```
IsAvailableInAloha

IsAvailableInDesktop

IsAvailableInLightning

IsAvailableInMobile

IsCustom

Label

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available on desktop.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Lightning Experience.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in the Salesforce mobile app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is a custom tab created by admins in the org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects TagDefinition

**Field Name** **Details**

**Description**

The localized label corresponding to the `MasterLabel` field in the Tooling
API object.

```
MobileUrl

Name

SobjectName

Url

### TagDefinition

```

Defines the attributes of child Tag objects.

Supported Calls

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab in the Salesforce mobile app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The developer name of the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of the sObject corresponding to the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab on desktop.

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`


Standard Objects TagDefinition

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Detail**

```
Name

Type

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
Identifies the tag word or phrase.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Defines the visibility of a tag. Possible value are:

**•** **Public** : The tag can be viewed and manipulated between all users in an organization.

**•** **Personal** : The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

When you create a tag for a record, an association is created with to a corresponding TagDefinition:

**•** If the value in the tag's `Name` field is new, a new TagDefinition record is automatically created and becomes the parent of the tag.

**•** If the value in the tag's `Name` field already exists in a TagDefinition, that TagDefinition automatically becomes the parent of the tag.

Each TagDefinition record has a one-to-many relationship with its child tag records.

The following standard objects represent tags for records:

**•** AccountTag

**•** AssetTag

**•** CampaignTag

**•** CaseTag

**•** ContactTag

**•** ContractTag

**•** DocumentTag

**•** EventTag

**•** LeadTag


### Standard Objects Task

**•** NoteTag

**•** OpportunityTag

**•** SolutionTag

### • TaskTag

Custom objects may also be tagged. Tags for custom objects are identified by a suffix of two underscores immediately followed by the
word `tag` . For example, a custom object named `Meeting` has a corresponding tag named Meeting__tag in that organization’s
WSDL. Meeting__tag is only valid for `Meeting` objects.

TagDefinition is useful for mass operations on any tag record. For instance, if you want to rename existing tags, you can search for the
appropriate TagDefinition object, update it, and the child tag's `Name` values are also changed. The following Java example replaces all
`WC` tags with the phrase `West Coast` :

```
   public void tagDefinitionSample() {

     String soqlQuery = "SELECT Id, Name FROM TagDefinition " +

       "WHERE Name = 'WC'";

     QueryResult qResult = null;

     try {

       qResult = connection.query(soqlQuery);

      TagDefinition tagDef = (TagDefinition) qResult.getRecords()[0];

      tagDef.setName("West Coast");

      connection.update(new SObject[]{tagDef});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### Task

Represents a business activity such as making a phone call or other to-do items. In the user interface, Task and Event records are collectively
referred to as activities.

Note: Task fields related to calls are exclusive to Salesforce CRM Call Center. Also, `query()`, `delete()`, and `update()`
aren't allowed with tasks related to more than one contact in API versions 23.0 and earlier.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Field Type**

```
AccountId

```

**Type**
reference


Standard Objects Task

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the related Account. The `AccountId` is determined as follows.

If the value of `WhatId` is any of these objects, Salesforce uses that object's `AccountId` .

**•** Account

**•** Opportunity

**•** Contract

**•** Custom object that is a child of Account

If the value of the `WhatId` field is any other object, and the value of the `WhoId` field is a
Contact object, then Salesforce uses that contact’s `AccountId` . (If your organization uses
Shared Activities, then Salesforce uses the `AccountId` of the primary contact.)

Otherwise, Salesforce sets the value of the `AccountId` field to `null` .

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

CallDisposition

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the due date of the task. This field has a timestamp that is always set to midnight
in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant; do not
attempt to alter it to accommodate time zone differences. Label is **Due Date** .

This field can’t be set or updated for a recurring task ( `IsRecurrence` is `true` ).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.


Standard Objects Task

**Field** **Field Type**

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

```
CallDurationInSeconds

CallObject

CallType

CompletedDateTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Duration of the call in seconds.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of a call center. Limit is 255 characters.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The type of call being answered. Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

When working with PushTopic, the `CallType` values display as `1` for `Inbound`, `0` for
`Internal`, and `2` for `Outbound` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.


Standard Objects Task

**Field** **Field Type**

**•** For insert, if the task is saved with a Closed status the field is set. If the task is saved with
an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is no change
to the field.

The status is a dynamic enum. If the Closed mapping is changed it won’t cause an update
of existing tasks. Only new insert/update operations are affected.

```
ConnectionReceivedId

ConnectionSentId

Description

IsArchived

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if Salesforce to Salesforce is enabled. This field is supported in API versions 14.0 and earlier.
In API version 15.0 and later, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains a text description of the task. The text provided in the Description field shows in
the Comments field on the task record detail page.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event has been archived. The default value of this field is `false` .


Standard Objects Task

**Field** **Field Type**

```
IsClosed

IsHighPriority

IsRecurrence

IsReminderSet

IsVisibleInSelfService

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task has been completed ( `true` ) or not ( `false` ). The default value
of this field is `false` . Is only set indirectly via the `Status` picklist. Label is **Closed** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. This field is derived from the `Priority` field. The default
value of this field is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task is scheduled to repeat itself ( `true` ) or only occurs once ( `false` ).
The default value of this field is `false` . This field is read-only on update, but not on create.
If this field value is `true`, then `RecurrenceStartDateOnly`,
`RecurrenceEndDateOnly`, `RecurrenceType`, and any recurrence fields associated
with the given recurrence type must be populated. See Usage section.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a popup reminder has been set for the task ( `true` ) or not ( `false` ). The
default value of this field is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a task associated with an object can be viewed in the Customer Portal
( `true` ) or not ( `false` ).


Standard Objects Task

**Field** **Field Type**

If your organization has digital experiences enabled, tasks marked
`IsVisibleInSelfService` are visible to any external user in the Experience Cloud
site, as long as the user has access to the record the task was created on.

```
OwnerId

Priority

RecurrenceActivityId

RecurrenceDayOfMonth

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group who owns the record. Label is **Assigned To ID** . This field accepts
Groups of type Queue only.

In the user interface, Group IDs correspond with the queue’s list view names. To create or
update tasks assigned to Group, use v48.0 or later.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates the importance or urgency of a task, such as high or low. The default
value of this field is `Normal` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Not required on create. ID of the main record of the recurring task. Subsequent
occurrences have the same value in this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Task

**Field** **Field Type**

**Description**
The day of the month in which the task repeats.

```
RecurrenceDayOfWeekMask

RecurrenceEndDateOnly

RecurrenceInstance

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the task repeats. This field contains a bitmask. The
values are as follows:

**•** `Sunday = 1`

**•** `Monday = 2`

**•** `Tuesday = 4`

**•** `Wednesday = 8`

**•** `Thursday = 16`

**•** `Friday = 32`

**•** `Saturday = 64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the task repeats. This field has a timestamp that is always set to
midnight in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant;
do not attempt to alter it to accommodate time zone differences.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring task.

Possible values are:

**•** `First` —1st

**•** `Fourth` —4th

**•** `Last` —last

**•** `Second` —2nd


Standard Objects Task

**Field** **Field Type**

**•** `Third` —3rd

```
RecurrenceInterval

RecurrenceMonthOfYear

RecurrenceRegeneratedType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring tasks.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year in which the task repeats.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents what triggers a repeating task to repeat. Add this field to a page layout together
with the `RecurrenceInterval` field, which determines the number of days between
the triggering date (due date or close date) and the due date of the next repeating task in
the series.

Label is **Repeat This Task** . This field has the following picklist values:

**•** **None** : The task doesn’t repeat.

**•** **After due date** : The next repeating task will be due the specified number of days after
the current task’s due date.

**•** **After the task is closed** : The next repeating task will be due the specified number of
days after the current task is closed.

**•** **(Task closed)** : This task, now closed, was opened as part of a repeating series.

When tasks in a series are set to repeat after their due date, Salesforce doesn’t create
recurrences that would have been due in the past. Instead, Salesforce keeps adding the
interval until a repeated task has a due date in the future.

For example, suppose that someone sets a task to repeat three days after it’s due. But, that
person doesn’t complete the task (mark it Closed) until five days after it’s due. Instead of
creating a task that’s already overdue, Salesforce gives the new task a due date of tomorrow.
This due date is equivalent to 6 days after the due date; two intervals of three days each.

If that person completes the repeating task (marks it Closed) before the due date, the next
task is still due three days after the due date.


Standard Objects Task

**Field** **Field Type**

```
RecurrenceStartDateOnly

RecurrenceTimeZoneSidKey

RecurrenceType

ReminderDateTime

Status

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the recurring task begins. Must be a date and time before
`RecurrenceEndDateOnly` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone associated with the recurring task. For example, “UTC-8:00” for Pacific Standard
Time.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the task repeats. For example, daily, weekly, or every nth month (where
“nth” is defined in `RecurrenceInstance` ).

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the time when the reminder is scheduled to fire, if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then the user may have deselected the
reminder checkbox in the Salesforce user interface, or the reminder has already fired at the
time indicated by the value.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates the status of the task. The default value of this field is `Not Started` .
Each predefined `Status` field implies a value for the `IsClosed` flag. To obtain picklist
values, query the TaskStatus object.


Standard Objects Task

**Field** **Field Type**

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

This field can’t be updated for recurring tasks ( `IsRecurrence` is `true` ).

```
Subject

TaskSubtype

TaskWhoIds

```

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the task, such as “Call” or “Send Quote.” Limit: 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific task subtypes.
This field can't be updated.

`TaskSubtype` values:

**•** `Task`

**•** `Email`

**•** `LinkedIn` —Available in API version 56.0 and later.

**•** `ListEmail`

**•** `Cadence`

**•** `Call`

The `Cadence` subtype is an internal value used by Sales Engagement, and can’t be set
manually.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs related to this task. This `JunctionIdList` field is
linked to the `TaskWhoRelations` child relationship. `TaskWhoIds` is only available
when the shared activities setting is enabled. The first contact or lead ID in the list becomes


Standard Objects Task

**Field** **Field Type**

the primary `WhoId` if you don’t specify a primary `WhoId` . If you set the `EventWhoIds`
field to null, all entries in the list are deleted and the value of `WhoId` is added as the first
entry.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

```
Type

WhatCount

WhatId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of task, such as Call or Meeting.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Count of related TaskRelations
pertaining to `WhatId` . Count of the `WhatId` must be _`1`_ or less.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatId` s are polymorphic. Polymorphic means a `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID` .

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,


Standard Objects Task

**Field** **Field Type**

CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant, ContactRequest,
Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo, DelegatedAccount,
DocumentChecklistItem, EnrollmentEligibilityCriteria, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
ListEmail, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoCount

WhoId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Count of related TaskRelations
pertaining to `WhoId` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .

Beginning in API version 37.0, if the contact or lead ID in the `WhoId` field is not in the
`TaskWhoIds` list, no error occurs and the ID is added to the `TaskWhoIds` as the primary
`WhoId` . If `WhoId` is set to null, an arbitrary ID from the existing `TaskWhoIds` list is
promoted to the primary position.

This is a polymorphic relationship field.


Standard Objects Task

**Field** **Field Type**

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

**Recurring Tasks**

**•** Recurring tasks are available in API version 16.0 and later.

**•** After a task is created, it can’t be changed from recurring to nonrecurring or vice versa.

**•** When a user creates a series of recurring tasks, Salesforce creates a main record and subsequent occurrences. For the main record,
`IsRecurrence` is set to `true` and other fields that define the recurrence pattern are populated. The ID of the main record of
the recurring task is saved in the subsequent occurrences, in the `RecurrenceActivityId` field.

**•** When you delete a recurring task series through the API, all open and closed task occurrences in the series are removed. However,
when you delete a recurring task series through the user interface, only open tasks occurrences ( `IsClosed` is `false` ) in the
series are removed.

**•** If `IsRecurrence` is `true`, then `RecurrenceStartDateOnly`, `RecurrenceEndDateOnly`, `RecurrenceType`,
and any properties associated with the given recurrence type (see the following table) must be populated.

**•** When you change the `RecurrenceStartDateOnly` field or the recurrence pattern, all open tasks occurrences in the series
are deleted and new open task occurrences are created based on the new recurrence pattern. The following fields determine the
recurrence pattern: `RecurrenceType`, `RecurrenceTimeZoneSidKey`, `RecurrenceInterval`,
`RecurrenceDayOfWeekMask`, `RecurrenceDayOfMonth`, `RecurrenceInstance`, and
`RecurrenceMonthOfYear` .

**•** When you change the value of `RecurrenceEndDateOnly` to an earlier date (for example, from January 20 to January 10), all
open task occurrences in the series with the `ActivityDate` value greater than the new end date value are deleted. Other open
and closed task occurrences in the series are not affected.

**•** When you change the value of `RecurrenceEndDateOnly` to a later date (for example, from January 10 to January 20), new
task occurrences are created up to the new end date. Existing open and closed tasks in the series are not affected.

This table describes the usage of recurrence fields for Salesforce Classic recurring events. Each recurrence type must have all of its
properties set. All unused properties must be set to null.

**RecurrenceType Value** **Properties** **Example Pattern**

RecursDaily RecurrenceInterval Every second day

RecursEveryWeekday RecurrenceDayOfWeekMask Every weekday - can’t be Saturday or Sunday

RecursMonthly RecurrenceDayOfMonth Every second month, on the third day of the month
RecurrenceInterval

RecursMonthlyNth RecurrenceInterval RecurrenceInstance Every second month, on the last Friday of the month
RecurrenceDayOfWeekMask


Standard Objects Task

**RecurrenceType Value** **Properties** **Example Pattern**

RecursWeekly RecurrenceInterval Every three weeks on Wednesday and Friday
RecurrenceDayOfWeekMask

RecursYearly RecurrenceDayOfMonth Every March on the 26th day of the month
RecurrenceMonthOfYear

RecursYearlyNth RecurrenceDayOfWeekMask The first Saturday in every October
RecurrenceInstanceRecurrenceMonthOfYear

**JunctionIdList**

The `JunctionIdList` field is now implemented in the Event and Task objects. With a single API call, it’s easy to create
many-to-many relationships between the Event or Task object with contacts, leads, or users.

To create a Task with related Contacts without `JunctionIdList`, you first have to create the task, then use the returned task
ID to create the `TaskRelation` records. If the `TaskRelation` save call fails, error handling is your responsibility because the
task has already been committed to the database.

```
     public void createTasksOld(Contact[] contacts) {

      Task task = new Task();

      task.setSubject("New Task");

      SaveResult[] results = null;

      try {

      results = connection.create(new Task[] {

       task

      });

      if (results[0].isSuccess()) {

       TaskRelation[] relations = new TaskRelation[contacts.size()];

       for (int i = 0; i < contacts.length; i++) {

       relations[i] = new TaskRelation();

       relations[i].setTaskId(results[0].getID());

       relations[i].setRelationId(contacts[i].getID());

       }

       results = connection.create(relations);

      }

      } catch (ConnectionException ce) {

      ce.printStackTrace();

      }

     }

```

To create a task using `JuncionIdList`, IDs are pulled from the related contacts and both the task and the `TaskRelation`
records are created in one API call. If the `TaskRelation` fails, the task is rolled back because it’s all done in a single API call.

```
     public void createTaskNew(Contact[] contacts) {

      String[] contactIds = new String[contacts.size()];

      for (int i = 0; i < contacts.size(); i++) {

      contactIds[i] = contacts[i].getID();

      }

      Task task = new Task();

      task.setSubject("New Task");

      task.setTaskWhoIds(contactIds);

      SaveResult[] results = null;

      try {

```


### Standard Objects TaskPriority

```
      results = connection.create(new Task[] {

       task

      });

      } catch (ConnectionException ce) {

      ce.printStackTrace();

      }

     }

```

**Shared Field-Level Security for Event and Task Objects**

Metadata deployments for the Task object should always include the field-level security for the Event object. Shared field-level security
prevents each object from changing the field-level security of the associated object.

Metadata deployments that include field-level security for only one of either the Event or Task objects can cause field-level security
changes to the other object that aren't reflected in the metadata.

**•** If field-level security is enabled for one object, then field-level security is enabled for both objects.

**•** If field-level security is disabled for one object, then it's disabled for both objects.

Note: A missing entry in the metadata is treated as field-level security being disabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaskChangeEvent (API version 44.0)**
Change events are available for the object.

**TaskFeed (API version 20.0)**
Feed tracking is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskPriority

Represents the importance or urgency of a task, such as High, Normal, or Low.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer and Partner Portal users can’t access this object.


Standard Objects TaskPriority

Fields

**Field** **Details**

```
ApiName

IsDefault

IsHighPriority

MasterLabel

SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task priority value ( `true` ) or not ( `false` ) in the
picklist. Only one value in the picklist can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task priority value represents a high priority task ( `true` ) or not
( `false` ). Multiple task priority values can represent a high-priority task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task priority value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number used to sort this value in the task priority picklist. These numbers aren’t guaranteed
to be sequential, as some previous task priority values might have been deleted.


### Standard Objects TaskRelation

Usage

This object represents a value in the task priority picklist. The task priority picklist provides additional information about the importance
of a task, such as whether a given priority value represents a high priority. Your client application can query on this object to retrieve
the set of values in the task priority picklist, and then use that information while processing task objects to determine more information
about a given task. For example, the application could test whether a given task is high priority based on its `Priority` value and the
value of the `IsHighPriority` field in the associated TaskPriority object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskRelation

Represents the relationship between a task and a lead, contacts, and other objects related to the task. If Shared Activities is enabled, this
object doesn’t support triggers, workflow, or data validation rules. This object is available in API version 24.0 and later.

### TaskRelation is only available if you’ve enabled Shared Activities in your organization. TaskRelation allows the following relationships:

**•** A task can be related to one lead or up to 50 contacts.

**•** A task can also be related to one account, asset, campaign, case, contract, opportunity, product, solution, or custom object.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `queryAll()`,

```
   retrieve()

```

Fields

**Field Name** **Details**

```
AccountId

IsWhat

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects TaskRelation

**Field Name** **Details**

**Description**
Indicates whether the relation is an Account, Opportunity, Campaign, Case, other
standard object, or a custom object. Value is `false` if `RelationId` is a
contact or lead and `true` otherwise.

```
RelationId

TaskId

```

Usage

**See contacts associated with a task**

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Indicates the `WhatId` or `WhoId` in the relationship. For more information, see
`Task` .

For information on IDs, see ID Field Type.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the ID of the associated Task.

For information on IDs, see ID Field Type.

```
  public void queryWhosOfTaskSample() {

     String soqlQuery = "SELECT Id, Subject, (SELECT RelationId, Relation.Name, IsWhat

   from TaskRelations WHERE isWhat = false) FROM Task WHERE Id = '00T x0000005OKEN'";

    QueryResult qResult = null;

    try {

       qResult = connection.query(soqlQuery);

       TaskRelation relation1 =

  (TaskRelation)qResult.getRecords()[0].getTaskRelations().getRecords()[0];

    }catch (ConnectionException ce) {

       ce.printStackTrace();

     }

   }

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects TaskStatus

**TaskRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

### Task

TaskWhoRelation

### TaskStatus

Represents the status of a task, such as Not Started, Completed, or Closed.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ApiName

IsClosed

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task status value represents a closed task ( `true` ) or not ( `false` ).
Multiple task status values can represent a closed task.

**Type**
boolean


### Standard Objects TaskTag

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task status value ( `true` ) or not ( `false` ) in the
picklist.

```
 MasterLabel

 SortOrder

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task status value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the task status picklist. These numbers aren’t guaranteed
to be sequential, as some previous task status values might have been deleted.

This object represents a value in the task status picklist. The task status picklist provides additional information about the status of a task
, such as whether a given status value represents an open or closed task. Your client application can query this object to retrieve the set
of values in the task status picklist, and then use that information while processing task records to determine more information about
a given task. For example, the application could test whether a given task is open or closed based on the task `Status` value and the
value of the `IsClosed` property in the associated TaskStatus record.

SEE ALSO:

Overview of Salesforce Objects and Fields

### TaskTag

Associates a word or short phrase with a task .

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects TaskTag

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

TaskTag stores the relationship between its parent TagDefinition and the task being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.


### Standard Objects TaskWhoRelation

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### TaskWhoRelation

Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.

### TaskWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared

Activities for your organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
AccountId

RelationId

TaskId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the task.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects TaxEngine

**Field Name** **Details**

**Description**
Indicates whether the person related to the task is a lead or contact.

Usage

Here's a Java example that queries contacts associated with a task.

```
   public void queryWhosOfTaskSample() {

      String soqlQuery = "SELECT Id, Subject, (SELECT RelationId, Relation.Name, IsWhat from

    TaskWhoRelations) FROM Task WHERE Id = '00Tx0000005OKEN'";

      QueryResult qResult = null;

      try {

        qResult = connection.query(soqlQuery);

        TaskWhoRelation relation1 =

   (TaskWhoRelation)qResult.getRecords()[0].getTaskWhoRelations().getRecords()[0];

      } catch (ConnectionException ce) {

        ce.printStackTrace();

      }

   }

```

SEE ALSO:

Task

TaskRelation

### TaxEngine

A tax engine represents both an instance of a tax engine provider as well as the merchant credentials for that specific instance. When
Subscription Management calculates tax on an order item, it sends a request through Subscription Management Tax Calculation API to
an external tax engine. The Salesforce tax engine record contains information passed to the external tax engine, such as This object is
available in API version 55.0 and later.

The merchant credentials are stored in a named credential record in Salesforce. The named credential record is referenced in the tax
engine object’s Merchant Credentials field.

The tax adapter Apex class ID is stored in the tax engine provider. When a user calls Calculate Tax API, Subscription Management interacts
with the external tax provider using the adapter class and the named credentials.

The tax engine address and seller code from the TaxEngine record are also used in the interaction.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects TaxEngine

Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. If your org has Subscription Management
and Commerce Subscriptions enabled, then Subscription Management takes precedence.

Special Access Rules

This object is available with Subscription Management, Commerce Subscriptions, and Billing (Revenue Cloud). If your org has Subscription
Management and Commerce Subscriptions enabled, then Subscription Management takes precedence.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengine.htm)

Fields

**Field** **Details**

```
Description

ExternalReference

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider and merchant credential.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Shows information about the external platform used for the tax engine.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TaxEngine

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
MerchantCredentialId

SellerCode

Status

TaxEngineAddress

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Looks up to the merchant credential setup entity in Salesforce. CommerceTax Tax Calculation
API sends this information to the external tax engine for use in the tax calculation process.

This field is a relationship field.

**Relationship Name**
MerchantCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Seller code of the transaction for which the tax engine integration log was captured.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows the status of the tax engine.

Possible values are:

**•** `Active` —This tax engine is available for use.

**•** `Inactive` —This tax engine isn't available for use.

**Type**
address

**Properties**
Filter


Standard Objects TaxEngine

**Field** **Details**

**Description**
[The compound form of the tax engine address. Read-only. See Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
for details on compound address fields.

```
TaxEngineCity

TaxEngineCountry

TaxEngineGeocodeAccuracy

TaxEngineLatitude

TaxEngineLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
[Accuracy level of the geocode for the tax engine address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLongitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects TaxEngine

**Field** **Details**

**Description**
Used with TaxEngineLatitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

```
TaxEngineName

TaxEnginePostalCode

TaxEngineProviderId

TaxEngineState

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the tax engine.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Postal code maximum size is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Id of the tax engine provider.

This field is a relationship field.

**Relationship Name**
TaxEngineProvider

**Relationship Type**
Lookup

**Refers To**
TaxEngineProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. State maximum size is 80 characters.


### Standard Objects TaxEngineInteractionLog

**Field** **Details**

```
TaxEngineStreet

TaxPrvdAccountIdentifier

Type

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the external tax provider’s account. This field is only available if
Commerce Subscriptions is enabled for your org. Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the tax engine used to calculate tax. This field is only available if Commerce
Subscriptions is enabled for your org. Available in API version 63.0 and later.

Possible values are:

**•** `CommerceTaxExtension` —Commerce Tax Extension

**•** `RevenueCloudTaxExtension` —Revenue Cloud Tax Extension

**•** `StandardTaxEngine` —Standard Tax Extension

**•** `StripeNative` —Stripe Native

### TaxEngineInteractionLog

A record of a communication with an external tax engine following a tax calculation request. This object is available in API version 55.0
and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```


Standard Objects TaxEngineInteractionLog

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineinteractionlog.htm)

Fields

**Field** **Details**

```
Description

DocumentCode

EffectiveDate

InteractionHttpStatusCode

InteractionType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined description for providing more information about the tax engine
interaction log.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Document code of the transaction for which the tax engine integration log was captured.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the tax engine request takes effect. This date is available for reference and
bookkeeping only and doesn’t have any impact on tax calculation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HHTP result code of the external callout made to a third-party tax engine provider. Refer
to your third-party tax engine provider’s documentation for details about the specific codes
returned.

**Type**
picklist


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of request made to the tax engine. In Subscription Management Summer
‘22, only `CalculateTax` is supported.

Possible values are:

**•** `CalculateTax`

```
LastReferencedDate

LastViewedDate

ReferenceEntity

RequestBody

RequestContentType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record on which tax was calculated.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API request.

**Type**
picklist


Standard Objects TaxEngineInteractionLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of data passed in the request. For example, `application/html` or
`text/csv` .

```
RequestLength

RequestName

ResponseBody

ResponseContentType

ResponseLength

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the request body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the request.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API response.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the method used to deliver the tax calculation API response, such as
`application/html` or `text/vnd.salesforce.quip-template` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the response body.


Standard Objects TaxEngineInteractionLog

**Field** **Details**

```
ResponseName

ResultCode

TaxEngineId

TaxEngineInteractionLogNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the response from the tax engine.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The code describing the result of the request.

Possible values are:

**•** `AdapterException` —The Apex adapter interface for the tax provider threw an
exception.

**•** `Success` —The request was successful.

**•** `TaxEngineError` —An error occurred while processing the request. See the log for
details.

**•** `ValidationError` —A validation error occurred. Check that the request is complete
and valid.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax engine used in the tax calculation process.

This field is a relationship field.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects TaxEngineProvider

**Field** **Details**

**Description**
A system-generated number for a log entry.

### TaxEngineProvider

Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce,
and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine record
represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API version
55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxengineprovider.htm)

Fields

**Field** **Details**

```
ApexAdapterId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Id of the Apex adapter used by this tax provider. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
ApexAdapter

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
textarea


### Standard Objects TaxGeoConfig

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider.

```
DeveloperName

Language

MasterLabel

NamespacePrefix

### TaxGeoConfig

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used by this tax engine provider. Values appear based on their language codes
in Salesforce, such as `da` for Danish or `th` for Thai.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label used for the tax engine’s API in Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Apex namespace prefix of the API used for the tax engine. In a packaging context, a
namespace prefix is a one to 15-character alphanumeric identifier that distinguishes your
package and its contents from packages of other developers on AppExchange.

Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.


Standard Objects TaxGeoConfig

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxGeoConfig object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
GeoCountryId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The GeoCountry associated with the TaxGeoConfig.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.


Standard Objects TaxGeoConfig

**Field** **Details**

```
Name

OwnerId

RoundingStrategyType

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the TaxGeoConfig.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the TaxGeoConfig record. By default, the asset owner is the user who created
the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the tax rounding strategy associated with the TaxGeoConfig.

Possible values are:

**•** `Rounding Down`

**•** `Rounding Off`

**•** `Rounding Up`

The default value is `Rounding Off` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects TaxPolicy

**TaxGeoConfigShare on page 67**
Sharing is available for the object.

SEE ALSO:

GeoCountry

### TaxPolicy

A tax policy contains a group of tax treatments, where each treatment represents parameters to determine how a particular product is
taxed for a transaction line item. Tax policies are related to products, which pass the policy on to the resulting order items. When you
activate an order, Subscription Management assigns a tax treatment to each order item based on the tax policy's DefaultTaxTreatmentId,
then uses the tax treatment to calculate tax. This object is available in API version 55.0 and later.

Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxpolicy.htm)

Fields

**Field** **Details**

```
DefaultTaxTreatmentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When you order a product, the order product receives this tax treatment.

This field is a relationship field.

**Relationship Name**
DefaultTaxTreatment

**Relationship Type**
Lookup


Standard Objects TaxPolicy

**Field** **Details**

**Refers To**
TaxTreatment

```
Description

LastReferencedDate

LastViewedDate

Name

Status

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for providing more information about the tax policy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the tax policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
To calculate tax for order products, products must have an active tax policy. Tax policies are
created with a Draft status before being assigned to a product or order product. After
activating a tax policy, you can't edit certain policy fields.


### Standard Objects TaxRate

**Field** **Details**

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

```
TreatmentSelection

### TaxRate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management chooses a tax treatment to assign to order products
related to this tax policy. In API version 55.0, only `Default` is supported.

Possible values are:

**•** `Default` —The order product receives the tax treatment defined in the tax policy's
`DefaultTreatmentId` field.

**•** `LegalEntity` —Assigns a tax treatment based on matching legal entities between
the order product and tax treatment.

**•** `Manual` —Order products don't receive tax treatments based on the tax policy; users
must provide the treatment on their own instead.

Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The TaxRate object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
GeoCountryId

```

**Type**
reference


Standard Objects TaxRate

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the GeoCountry for which the tax rate applies. You can define only one tax rate per
GeoCountry and tax code combination.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

```
LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't viewed it directly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique ID of the tax rate.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects TaxRate

**Field** **Details**

**Description**
The TaxRate record owner. By default, the record owner is the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Priority

Rate

TaxCode

```

Associated Objects

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The tax percentage rate that will be applied to orders.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The code used to calculate the tax rate for the invoice line.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaxRateChangeEvent on page 68**
Change events are available for the object.

**TaxRateFeed on page 55**
Feed tracking is available for the object.

**TaxRateHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects TaxTreatment

**TaxRateOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TaxRateShare on page 67**
Sharing is available for the object.

### TaxTreatment

A tax treatment contains details about how Salesforce and external engines calculate taxes, and the tax engine to use for tax calculation.
The IsTaxable field determines whether tax is calculated for the product in the transaction. The tax code, tax engine, and product code
are sent via API to the external tax calculation service. When you invoice an order item that has a tax treatment, the invoice line inherits
the tax treatment from the order item’s related billing schedule. The invoice line’s TaxCode field is populated based on the code that
the tax engine used for calculation. This object is available in API version 55.0 and later.

Each product requires a tax policy to determine whether to apply tax. The tax treatments determine how taxable products are taxed.
Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_taxtreatment.htm)

Fields

**Field** **Details**

```
Description

IsTaxable

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for providing more information about the tax treatment.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects TaxTreatment

**Field** **Details**

**Description**
Determines whether Subscription Management calculates tax for order items covered by
the tax treatment. When this value is True, Subscription Management calls the CalculateTax
API for the order item during order item creation.

The default value is 'False'.

This field is available when Subscription Management is enabled.

```
LastReferencedDate

LastViewedDate

Name

ProductCode

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the tax treatment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Code of the product that the tax treatment applies to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects TaxTreatment

**Field** **Details**

**Description**
Status of the tax treatment.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

```
TaxCode

TaxEngineId

TaxPolicyId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference code used when tax is calculated in an external tax engine.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax engine for the tax treatment. A tax engine represents both an instance of a tax engine
provider as well as the merchant credentials for that specific instance. When Subscription
Management begins the tax calculation process for an order item, it uses the tax engine
from the order item’s tax treatment.

If the tax treatment’s `IsTaxable` value is True, the treatment requires a tax engine.

This field is a relationship field.

This field is available when Subscription Management is enabled.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax treatment’s parent tax policy. A tax policy is a group of tax treatments, where each
treatment represents a rule for how to invoice a customer for an order item. Tax policies are
related to products, which pass the policy on to the resulting order items. When you activate


### Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

an order, Subscription Management assigns a tax treatment to each order item based on
the tax policy's DefaultTaxTreatmentId, then uses the tax treatment to calculate tax.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

### TenantScrAIPrmptInjection

Stores generative AI prompt injection data. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

InputSource

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin of this prompt.


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

```
Language

MaskedPrompt

MaskedResponse

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Language of the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
Masked prompt or input text.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response from the LLM. If masking is enabled, this may contain placeholder
text.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantScrAIPrmptInjection

**Field** **Details**

**Description**
The name of the metric for which data is being collected.

```
PlannerLlm

Prompt

PromptTimestamp

PromptTokens

Response

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The LLM being used by the Planner.

**Type**
textarea

**Properties**
Nillable

**Description**
The hydrated version of prompt text before data masking is applied. The actual prompt sent
to the LLM will mask sensitive data if data masking is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when this prompt injection happened.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of tokens used in the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response after unmasking.

**Type**
string


### Standard Objects TenantSecret

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this triggered Transaction Security Policy event.

```
TenantName

### TenantSecret

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

This object stores an encrypted organization-specific key fragment that’s used with the primary secret (KDF seed) to produce org-specific
data encryption keys. This object is available in API version 34.0 and later.

You can rotate tenant secrets of the `Data` type once every four hours in a sandbox org or every 24 hours in production orgs. You can
rotate tenant secrets of the `SearchIndex` type one time every seven days.

Note: This information is about Shield Platform Encryption and not Classic Encryption.

Supported Calls

`create()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Description

KeyDerivationMode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The description of the tenant secret.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The key derivation mode applied to customer-supplied key material. Modes are:

**PBKDF2**
The customer-supplied key material is used by the Shield KMS to create a
derived data encryption key.

**NONE**
The customer-supplied key material is used by the Shield KMS as the final
data encryption key to directly encrypt and decrypt data.

Available in API version 43.0 and later.

```
RemoteKeyCertificate

RemoteKeyIdentifier

RemoteKeyServiceID

SecretValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the certificate whose public key is used to encrypt the
`SecretValue` during a remote key callout.

Available in API version 45.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique key identifier for key material fetched from a remote key service.

Available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The named credential used to fetch remote key material from a remote key
service.

Available in API version 45.0 and later.

**Type**
base64

**Properties**
Create, Nillable, Update


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The encrypted 256-bit secret value encoded in base64.

```
SecretValueCertificate

SecretValueHash

Source

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The certificate needed to upload a customer-supplied tenant secret. Each
certificate has a unique name.

**Type**
base64

**Properties**
Create

**Description**

The matching tenant secret hash for an uploaded customer-supplied tenant
secret.

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the encryption key material. Values are:

**HSM**
A Salesforce-generated tenant secret.

**Uploaded**
A customer-supplied tenant secret or data encryption key.

**Remote**
A tenant secret or data encryption key fetched from a key service outside of
Salesforce. Available in API version 44.0 and later.Tenant secrets with a
`Source` value of Remote are listed as Fetched on the Key Management
page in Setup.

Available in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The status of the tenant secret. Values are:

**Active**
Can be used to encrypt and decrypt new or existing data.

**Archived**
Can’t encrypt new data. Can be used to decrypt data previously encrypted
with this key when it was active.

**Destroyed**
Can’t encrypt or decrypt data. Data encrypted with this key when it was active
can no longer be decrypted. Files and attachments encrypted with this key
can no longer be downloaded.

You can update the `Status` field through the API in versions 44.0 or later.

```
Type

Version

```

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of tenant secret. The `Type` field is available in API version 39.0 and
later. The following values appear in the `Type` picklist:

**•** `Analytics` —CRM Analytics data (available in API version 39.0 and later).

**•** `Data` —data stored in the Salesforce database. Includes data in encrypted
fields, files, and attachments but not search index files. Tenant secrets created
in API version 34.0 and later default to the `Data` type.

**•** `Database` —transactional database including standard and custom fields,
metadata, and Apex (available in API version 62.0 and later).

**•** `DeterministicData` —data stored in the Salesforce database. Includes
data in encrypted fields, files, and attachments, but not search index files
(available in API version 39.0 and later).

**•** `EventBus` —Change Data Capture event data (available in API version 43.0
and later).

**•** `SearchIndex` —search index files (available in API version 39.0 and later).

For Hyperforce orgs on API version 63.0 and later, create secrets of type
`SearchIndex` with the DataEncryptionKey object. For Hyperforce orgs
on API version 62.0 and earlier, and for all non-Hyperforce orgs, create secrets
of type `SearchIndex` with the TenantSecret object.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecret

**Field Name** **Details**

**Description**

The version number of this secret. The version number is unique within your org.

Usage

Use this object to create or update an org-specific tenant secret or customer-supplied key material.

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, the video How To Use Salesforce APIs Collection With Postman by Sudipta Deb provides step](https://www.youtube.com/watch?v=DJ7_iW2B5tA)
by step instructions on getting started using REST with Salesforce.

Example 1:

Build an automated tenant secret creation and activation solution similar to the following.

**1.** Start by creating an Apex class to create the tenant secret. Specify the value of the tenant secret to encrypt data of a particular type.

```
     global class CreateNewSecret implements Schedulable {

       global void execute(SchedulableContext SC) {

         TenantSecret secret = new TenantSecret ();

         secret.description = 'Created new secret from scheduled job';

         secret.type= 'Database';

         insert secret;

       }

     }

```

Note: `Type` is available in API version 39.0 and later. `Type` is optional; all tenant secrets default to the `Data` type.

**2.** Schedule the Apex class to run at the specified interval.

This Apex code only needs to be run a single time to schedule the job. This code runs the job every 90 days.

```
     CreateNewSecret secret = new CreateNewSecret();

     String schedule = '0 0 0 1 JAN,APR,JUL,OCT ?';

     String jobID = system.schedule('Automated secret creation and activation', schedule,

     secret);

```

**3.** Validate that the job is scheduled.

**4.** Validate that tenant secrets are created after the job is run.

Example 2

Upload a customer-supplied tenant secret.

**1.** [Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)
Help.


Standard Objects TenantSecret

**2.** Then upload your matching key material and key material hash. Include the unique name of the compatible certificate. The key
material is uploaded in encrypted form.

```
         TenantSecret secret = new TenantSecret ();

         secret.description = 'New uploaded secret';

         secret.type= 'Data';

         secret.SecretValue = ...

         EncodingUtil.base64Decode('...');;

         secret.SecretValueCertificate = ...;

         secret.SecretValueHash = ...

         EncodingUtil.base64Decode('...');

         insert secret;

```

[You can use this script to generate a customer-supplied tenant secret and tenant secret hash.](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok_script.htm&type=5&language=en_US)

**3.** Validate that the key material is uploaded.

Example 3

Opt out of key derivation on a key-by-key basis when you upload key material. When you upload your key material, specify
`'Source':Uploaded` and `'KeyDerivationMode':'NONE'`, and set non-null values for the SecretValueCertificate,
SecretValue, and SecretValueHash.

Example 4

Import a tenant secret of the `Data` type.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.SecretValue = "<previously_exported_secret_as_a_String>";

   update secret;

```

Example 5

Export a tenant secret by writing the `secret.SecretValue` to a file. Here’s an example that uses a tenant secret of the `Data`
type.

```
   TenantSecret secret = [SELECT SecretValue FROM TenantSecret WHERE Type = 'Data' AND Version

    = 2];

   secret.SecretValue =...;

   update secret;

```

Example 6

Destroy a tenant secret of the `Data` type.

Warning: Your tenant secret is unique to your organization and to the specific data to which it applies. When you destroy a
tenant secret, related data isn’t accessible unless you previously exported the key and then import the key back into Salesforce.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.SecretValue = NULL;

```


### Standard Objects TenantSecurityAIGtwyUsage

```
   secret.Status = Destroyed;

   update secret;

```

Example 7

Change the `Status` of a tenant secret from Archived to Destroyed. Include the SecretValue and new tenant secret Status.

```
   TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];

   secret.Status = Destroyed;

   update secret;

```

Cache-Only Key Service customers can change the Status of cache-only key tenant secrets. For example, reactivate a cache-only key by
changing its Status from Destroyed to Active.

Example 8

Create a callout connection that fetches a cache-only key tenant secret from a key service outside of Salesforce.

**1.** Make sure that your org has at least one active Data in Salesforce key, either Salesforce-generated or customer-supplied. Then turn
on Allow Cache-Only Keys with BYOK from the Advanced Settings page in Setup.

**2.** [Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)
Help.

**3.** [Create and assemble your key material.](https://help.salesforce.com/articleView?id=security_pe_byok_cache_create.htm&language=en_US)

**4.** Create a named credential to serve as your authenticated callout mechanism. You can define your named credential through Setup
[or directly with Apex. Specify a BYOK-compatible certificate and an HTTPS endpoint.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

**5.** Configure the connection to your remote key service. This connection uses a named credential and its associated certificate to fetch
a specified cache-only key tenant secret.

```
     remote_params = { 'Source': 'Remote',

     'RemoteKeyIdentifier': ...,

     'RemoteKeyServiceId': ...,

     'RemoteKeyCertificate': ...}

     sf.TenantSecret.create(remote_params)

```

SEE ALSO:

System Fields

### TenantSecurityAIGtwyUsage

Stores Einstein generative AI gateway usage data. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityAIGtwyUsage

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Cloud

DetailIdentifier

Feature

MaskedPrompt

MaskedResponse

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Cost cloud ID.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The AI feature for which the gateway request was made.

**Type**
textarea

**Properties**
Nillable

**Description**
Masked prompt or input text.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response from the LLM. If masking is enabled, this may contain placeholder
text.


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

```
MetricIdentifier

MetricsType

Model

Name

ObjectName

Prompt

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the model to which the request was sent.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Name of the Salesforce object is referenced in the prompt.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityAIGtwyUsage

**Field** **Details**

**Description**
The hydrated version of prompt text before data masking is applied. The actual prompt sent
to the LLM will mask sensitive data if data masking is enabled.

```
PromptTemplateDevName

PromptTemplateVersionNo

PromptTokens

Response

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the prompt template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the prompt template.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of tokens used in the prompt.

**Type**
textarea

**Properties**
Nillable

**Description**
The generated response after unmasking.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant of this AI gateway usage event.

**Type**
string


### Standard Objects TenantSecurityAlertRuleSelectedTenant

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant of this AI gateway usage event.

### TenantSecurityAlertRuleSelectedTenant

Stores information about a Security Center alert rule for tenants. This object is available for Security Center subscribers in API version
55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Name

NotificationRuleIdentifier

### `Tenant`

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the corresponding TenantSecurityNotificationRule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Description**
The ID of the tenant (org) that this record is for.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityAlertRuleSelectedTenantChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityAlertRuleSelectedTenantFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityAlertRuleSelectedTenantHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityAlertRuleSelectedTenantOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityAlertRuleSelectedTenantShare on page 67**
Sharing is available for the object.

### TenantSecurityApiAnomaly

[Stores detected anomalies in how users typically make API calls. Fore more information, see Threat Detection. This object is available to](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
Security Center subscribers in API version 53.0 and later.

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Description**
The ID of the individual detail record. This field is unique within your org.

```
EventDate

EventIdentifier

EventName

MetricIdentifier

MetricsType

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Api Anomaly.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

```
Operation

QueriedEntities

RequestIdentifier

RowsProcessed

Score

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API call that generated the event. For example, Query.

**Type**
textarea

**Properties**
Nillable

**Description**
The type of entities associated with the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total row count for the current operation.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
A number from 0 through 100 that represents the anomaly score for the API execution or
export tracked by this event. The anomaly score shows how the current API activity differs
from the user’s typical activity. A low score indicates that the user’s current API activity is
similar to the usual activity, and a high score indicates that it’s different.


Standard Objects TenantSecurityApiAnomaly

**Field** **Details**

```
SecurityEventData

Summary

Tenant

TenantName

Uri

```

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the API activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows how much as a percentage that the feature contributed to triggering this anomaly
event. The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the API anomaly that caused this event.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .


### Standard Objects TenantSecurityCertificate

**Field** **Details**

```
UserAgent

UserIdentifier

Username

```

Associated Objects

**Type**
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityApiAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityApiAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityApiAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityApiAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityApiAnomalyShare on page 67**
Sharing is available for the object.

### TenantSecurityCertificate

Stores metric details related to public key certificate information. The certificate binds the public key to the identity of an entity. This
object is available in API version 63.0 and later.


Standard Objects TenantSecurityCertificate

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

CertCreatedDate

```

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on this certificate. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action was taken.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate was created.


Standard Objects TenantSecurityCertificate

**Field** **Details**

```
DetailIdentifier

ExpirationDate

IsActive

IsCaSigned

IsPlatformEncrypted

IsPrivateKeyExportable

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate expires.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is active.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is signed by the issuer (true) or not (false).

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Whether this certificate is encrypted with Platform Encryption.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate’s private key is exportable.


Standard Objects TenantSecurityCertificate

**Field** **Details**

```
KeySize

MetricIdentfier

MetricsType

Name

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the public key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user-friendly name for the certificate.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this certificate.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant with this certificate.


### Standard Objects TenantSecurityConnectedApp TenantSecurityConnectedApp

Stores the details for a connected app that was added to or removed from a Security Center tenant. This object is available to Security
Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the connected app within a tenant.

Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who performed the action on the connected app.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the action was taken.


Standard Objects TenantSecurityConnectedApp

**Field** **Details**

```
AppName

AuthorizedBy

AuthorizedDate

DetailIdentifier

LastUsedDate

MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected app.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who authorized the connected app to be installed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the connected app was authorized for installation.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date that the connected app was used for authentication.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.


Standard Objects TenantSecurityConnectedApp

**Field** **Details**

```
MetricsType

Name

Publisher

Scope

Tenant

TenantName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents if the relevant tenant is the original publisher of the connected app for all
connected tenants in the org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The scope or scopes assigned to the connected app. A scope defines the type of protected
resource that the connected app can access.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the relevant tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


### Standard Objects TenantSecurityConfigAgent

**Field** **Details**

**Description**
The name of the tenant that the connected app is connected to.

```
Version

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the connected app.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityConnectedAppChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityConnectedAppFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityConnectedAppHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityConnectedAppOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityConnectedAppShare on page 67**
Sharing is available for the object.

### TenantSecurityConfigAgent

Stores metric details related to implemented Agentforce Agents This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for Security Center subscribers. This object is read-only.


Standard Objects TenantSecurityConfigAgent

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

AgentName

AgentType

AssignedTopics

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action taken on the configured agent within a tenant.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action was taken.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the configured agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of agent.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityConfigAgent

**Field** **Details**

**Description**
The list of agent topics.

```
DetailIdentifier

MetricIdentifier

MetricsType

Name

Status

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status, active or inactive, of the agent version.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
The ID of the tenant.

```
TenantName

Version

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tenant.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number.

### TenantSecurityCredentialStuffing

[Stores when a user successfully logs in to Salesforce during an identified credential stuffing attack. For more information, see Threat](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
[Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
AcceptLanguage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
List of HTTP headers that specify the natural language, such as English, that the client
understands.

```
DetailIdentifier

EventDate

EventIdentifier

EventName

LoginType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Credential Stuffing.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. For the list of possible values, see the LoginType
[field of LoginHistory in the Object Reference.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

```
LoginUrl

MetricIdentifier

MetricsType

Name

Score

Summary

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the login page. For example, `login.salesforce.com` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Indicates that a user successfully logged in to Salesforce during an identified credential
stuffing attack. The value of this field is always 1.

**Type**
textarea

**Properties**
Nillable


Standard Objects TenantSecurityCredentialStuffing

**Field** **Details**

**Description**
A summary of the threat that caused this event to be created.

```
Tenant

TenantName

UserAgent

UserIdentifier

Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time the event was created.


### Standard Objects TenantSecurityCustomMetricSetup

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityCredentialStuffingChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityCredentialStuffingFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityCredentialStuffingHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityCredentialStuffingOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityCredentialStuffingShare on page 67**
Sharing is available for the object.

### TenantSecurityCustomMetricSetup

Represents the configuration for a custom metric within Security Center. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomMetricIdentifier

CustomObjectIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for the custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the custom object for this custom metric.


Standard Objects TenantSecurityCustomMetricSetup

**Field** **Details**

```
CustomObjectName

DiffFieldIdentifierList

DisplayFieldIdentifierList

Description

MetricDisplayType

MetricGroup

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the custom object for this custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for `Diff` display.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for display.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The display type for this metric. For example, `diff` or `non-diff.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects TenantSecurityCustomMetricDetail

**Field** **Details**

**Description**
The category of the custom metric. Some category examples include
`Authentication` and `Configuration` .

```
MetricName

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The `MetricName` and `Name` fields have the same value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The `MetricName` and `Name` fields have the same value.

### TenantSecurityCustomMetricDetail

Stores TenantSecurityCustomMetricStat drill down details. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Whether the metric detail record was added, updated, or removed.


Standard Objects TenantSecurityCustomMetricDetail

**Field** **Details**

```
ActionBy

ActionDate

CustomObjectIdentifier

DiffFieldValueListHash

FieldValueListHash

MetricStatIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user who performs the action.

**Type**
dateTime

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
When this change was made.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to a Custom Object in which the metric details are stored.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The hash of custom metric `diff` fields value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The hash of custom metric fields value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to TenantSecurityCustomMetricStat.


### Standard Objects TenantSecurityCustomMetricStat

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Custom Object Api Name associates to the custom metric.

### TenantSecurityCustomMetricStat

Represents custom metric data within Security Center. This object is available in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
ChangeCount

CustomMetricIdentifier

EndProcessTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this metric was changed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the custom metric.

**Type**
dateTime


Standard Objects TenantSecurityCustomMetricStat

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The end time of the metric being processed.

```
MetricCount

MetricIdentifier

MetricName

Name

PreviousMetricIdentifier

StartProcessTime

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of times this metric was recorded.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the custom metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous unique identifier of this metric.

**Type**
dateTime


### Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The start time of the metric being processed.

### `Tenant`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant with the custom metric.

### TenantSecurityEncryptedField

Represents fields encrypted under your Shield Platform Encryption policy. This object is available in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the encryption policy within a tenant. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
string


Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
This field is reserved for future use.

```
ActionDate

DetailIdentifier

EncryptionType

FieldName

FieldType

MetricIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of encryption for the field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the encrypted field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of field being encrypted.

**Type**
string


Standard Objects TenantSecurityEncryptedField

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

```
MetricsType

Name

ObjectName

Tenant

TenantName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of encryption policy collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object for this encrypted field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with Shield Encryption.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tenant that this record is for.


### Standard Objects TenantSecurityGuestUserAnomaly TenantSecurityGuestUserAnomaly

Represents metric details for guest user anomaly events detected by Threat Detection. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

EventDate

EventIdentifier

EventName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects TenantSecurityGuestUserAnomaly

**Field** **Details**

**Description**
The name of the event.

```
MetricIdentifier

MetricsType

Name

RequestedObjects

Score

SoqlCommands

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The objects requested by the customers.

**Type**
double

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Specifies how significantly the guest user behavior deviates from the other guest users. It is
formatted as a number between 0 and 1.

**Type**
textarea


Standard Objects TenantSecurityGuestUserAnomaly

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
SOQL commands run by the guest user.

```
Summary

Tenant

TenantName

TotalControllerEvents

UserAgent

UserIdentifier

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text summary of the anomaly that caused this event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of times controllers were triggered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User Agent for this event.

**Type**
string


### Standard Objects TenantSecurityEncryptionPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID.

```
UserType

Username

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of user of this event. For example, a guest user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the event was
created.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityGuestUserAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityGuestUserAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityGuestUserAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityGuestUserAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityGuestUserAnomalyShare on page 67**
Sharing is available for the object.

### TenantSecurityEncryptionPolicy

Stores tenant encryption policy status. This object is available in API version 58.0 and later.


Standard Objects TenantSecurityEncryptionPolicy

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

DetailIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on the encryption policy within a tenant. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.


Standard Objects TenantSecurityEncryptionPolicy

**Field** **Details**

```
MetricIdentifier

MetricsType

Name

PolicyName

PolicyStatus

Tenant

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of encryption policy collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the policy.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Status of the policy. Possible values are:

**•** `-1` —No license.

**•** `0` —Not Enabled.

**•** `-1` —Enabled

**Type**
string


### Standard Objects TenantSecurityFeature

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with Shield Encryption.

```
TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that this record is for.

### TenantSecurityFeature

Stores org features across all tenants in Security Center. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

FeatureDescription

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityFeature

**Field** **Details**

**Description**
The description of the feature.

```
FeatureName

IsEnabled

MetricIdentifier

MetricsType

Name

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the feature.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feature is enabled or disabled.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of feature collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the feature for which data is being collected.

**Type**
string


### Standard Objects TenantSecurityHealthCheckBaselineTrend

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant where the feature was applied.

```
TenantName

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the connected tenant where the feature was enabled or disabled.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityFeatureChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityFeatureFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityFeatureHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityFeatureOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityFeatureShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckBaselineTrend

Stores metric details related to Health Check baseline settings. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get details about which metrics are collected and for which tenants, and
changes made to the Health Check baseline. This object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.


Standard Objects TenantSecurityHealthCheckBaselineTrend

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

ApiName

BaselineDescription

BaselineIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of action. For example, added, updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user or admin that made the change.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the change.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the metric used by the API and managed packages.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For custom baselines, the name of the custom baseline file.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects TenantSecurityHealthCheckBaselineTrend

**Field** **Details**

**Description**
The ID of the baseline.

```
BaselineName

DetailIdentifier

IsDefault

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the baseline.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the baseline is default or custom. The default is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the type of metric collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of data collected. For example, SecurityHealthCheckBaselineMetric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects TenantSecurityHealthCheckDetail

**Field** **Details**

**Description**
The name of the metric for the data collected.

### `Tenant`

```
TenantName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was scored by the Security Health Check.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was scored by the Security Health Check.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckBaselineTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityHealthCheckBaselineTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckBaselineTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckBaselineTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckBaselineTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckDetail

Stores the details of Health Check scores for a connected tenant. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get settings and risks per tenant on a selected date. This object is available
to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityHealthCheckDetail

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
HealthCheckSettingIdentifier

HealthCheckTrendKey

Name

OrgValue

RiskType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check setting. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Health Check trend related to the Health Check detail records.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org’s value for the security setting.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security setting value.

Possible values are:


Standard Objects TenantSecurityHealthCheckDetail

**Field** **Details**

**•** `HIGH_RISK`

**•** `MEDIUM_RISK`

**•** `MEETS_STANDARD`

```
Setting

SettingGroup

SettingRiskCategory

StandardValue

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting. For example, Minimum Password Length.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting group in Setup that this setting is in. For example, Password
Policies.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security settings.

Possible values are:

**•** `HIGH_RISK`

**•** `INFORMATIONAL`

**•** `LOW_RISK`

**•** `MEDIUM_RISK`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended standard value for the security setting.

**Type**
string


### Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckDetailChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityHealthCheckDetailFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckDetailHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckDetailOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckDetailShare on page 67**
Sharing is available for the object.

### TenantSecurityHealthCheckTrend

Stores the history of Security Health Check scores for a connected tenant within Security Center. Health Check in Security Center displays
Health Check scores and the average risk settings for all your tenants in one place. This object belongs to the parent tenant and stores
Health Check data pushed from child tenants. This object is available for Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Baseline

```

**Type**
string


Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The definition of an org’s security settings standards.

```
HighRisk

Informational

LowRisk

MediumRisk

Name

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data that isn't sensitive for your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data with low sensitivity for your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data with moderate sensitivity for your
company.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.


Standard Objects TenantSecurityHealthCheckTrend

**Field** **Details**

```
ProcessedTime

Score

ScoreDelta

Tenant

TenantOriginalIdentifier

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the Health Check score was calculated.

**Type**
double

**Properties**
Filter, Sort

**Description**
The summary score that shows how your org measures against a security baseline.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The percentage amount that the Health Check score changed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check Trend record for a tenant. This field is unique within your org.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckTrendChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityLicense

**TenantSecurityHealthCheckTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityHealthCheckTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityHealthCheckTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityLicense

Stores license usage information within Security Center. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Action

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of change made to the license. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when this change was made.


Standard Objects TenantSecurityLicense

**Field** **Details**

```
DetailIdentifier

ExpirationDate

MetricIdentifier

MetricsType

Name

Status

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which this license expires.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of license collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the license.


Standard Objects TenantSecurityLicense

**Field** **Details**

```
Tenant

TenantName

TotalLicenses

UsedLicenses

UsedLicensesLastUpdated

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant with this license.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The total number of licenses.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of used licenses.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the used licenses were last updated for this tenant.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLicenseChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityLogin

**TenantSecurityLicenseFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLicenseHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLicenseOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLicenseShare on page 67**
Sharing is available for the object.

### TenantSecurityLogin

Stores the login details of a single user to a tenant, grouped by date and type. You can query this object to find out how many times the
user logged in to a specific tenant using a specific login type (for example, username/password or SSO). This object is available to Security
Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

LastLoginDate

LoginCount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last time the user logged in.

**Type**
int


Standard Objects TenantSecurityLogin

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of times the user has logged in to the tenant.

```
MetricIdentifier

MetricsType

Name

Tenant

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

The supported metric types are:

**•** LOGIN_PWLESS

**•** LOGIN_PWLESS2FA

**•** LOGIN_UNPW

**•** LOGIN_UNPW2FA

**•** LOGIN_SSO

**•** LOGIN_SSO2FA

**•** LOGIN_OAUTH

**•** LOGIN_OAUTH2FA

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityLogin

**Field** **Details**

**Description**
The ID of the tenant that was scored.

```
TenantName

UserEmail

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityLoginChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityLoginFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLoginHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLoginOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLoginShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityLoginIpRangeTrend TenantSecurityLoginIpRangeTrend

Stores details of changes related to login IP ranges in Security Center. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only for Security Center subscribers. This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

Description

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of change made to the login IP range. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when this change was made.

**Type**
string


Standard Objects TenantSecurityLoginIpRangeTrend

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The description of the login IP range record.

```
DetailIdentifier

IpEndAddress

IpRangeIdentifier

IpStartAddress

MetricIdentifier

MetricsType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The end IP address of the login IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of the login IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string


Standard Objects TenantSecurityLoginIpRangeTrend

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of metric for the data collected.

```
Name

ProfileIdentifier

ProfileName

Tenant

TenantName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the profile that is assigned to this login IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile that is assigned to this login IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.


### Standard Objects TenantSecurityMobilePolicyTrend

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLoginIpRangeTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityLoginIpRangeTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityLoginIpRangeTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityLoginIpRangeTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityLoginIpRangeTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityMobilePolicyTrend

Stores metrics related to changes in mobile security policies across all tenants in Security Center. This object is available to Security Center
subscribers in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The change made to the mobile security policy. For example, a new policy was added,
updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Description**
The user who made the change.

```
ActionDate

ConnectedApp

DetailIdentifier

EffectiveDate

IsEnabled

MetricIdentifier

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the mobile security policy change.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app that is associated with the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date a mobile security policy is enforced.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A value indicating whether the mobile security policy is enabled. The default is `false`,
which means policies are disabled.

**Type**
string


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The foreign key of the metric.

```
MetricsType

MobilePlatform

Name

PolicyType

RuleValue

RuleValueType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of mobile security policy data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The mobile operating system of the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for which data is collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of mobile security policy. For example, Block Calendar.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The value of the security notification rule.

**Type**
string


Standard Objects TenantSecurityMobilePolicyTrend

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of rule value. For example, boolean or text.

```
SeverityLevel

Tenant

TenantName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The severity level of the security threat. For example, `CRITICAL` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPackageChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPackageFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPackageHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPackageOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPackageShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityMonitorMetric TenantSecurityMonitorMetric

Stores the daily count and daily count change for a metric within Security Center. This object is available to Security Center subscribers
in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
ChangeCount

Count

EndProcessTime

MetricIdentifier

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
How much the relevant metric changed.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The current metric count.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process ended.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


Standard Objects TenantSecurityMonitorMetric

**Field** **Details**

**Description**
The ID of the type of metric counted. This field is unique within your organization.

```
MetricsType

Name

PreviousMetricIdentifier

StartProcessTime

Tenant

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous ID of the type of metric that was counted. This field is unique within your
organization.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was scored.


### Standard Objects TenantSecurityNotification

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityMonitorMetricChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityMonitorMetricFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityMonitorMetricHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityMonitorMetricOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityMonitorMetricShare on page 67**
Sharing is available for the object.

### TenantSecurityNotification

Stores information about notifications that were triggered in Security Center as a function of the Alerts feature. For more information,
[see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 54.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
MetricCount

MetricIdentifier

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The metric count that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects TenantSecurityNotification

**Field** **Details**

**Description**
The ID of the type of metric that was counted.

```
MetricsType

Name

NotificationDate

NotificationType

Operator

RecipientEmails

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The metric for which the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the triggered notification rule.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The type of notification sent. For example, a Chatter feed or push notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The quantity of metrics used to measure.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects TenantSecurityNotification

**Field** **Details**

**Description**
The email addresses of the recipients who receive security notifications.

```
RuleName

Tenant

TenantName

Threshold

TriggerType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the notification rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant for which the notification was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The org name of the tenant for which the notification was triggered.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The threshold value that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger that set off the notification. For example, a security change was made.


### Standard Objects TenantSecurityNotificationRule

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityNotificationFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityNotificationHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityNotificationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityNotificationShare on page 67**
Sharing is available for the object.

### TenantSecurityNotificationRule

Stores an alert configured in the Security Center Alerts feature to notify recipients of changes made to security settings. For more
[information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
MetricsType

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of data being collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects TenantSecurityNotificationRule

**Field** **Details**

**Description**
The name of the metric for which data is being collected.

```
NotificationRuleIdentifier

NotificationType

Operator

RecipientEmails

RuleName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the alert that was triggered. This field is unique within your organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of notification used for the alert. The options are:

**•** `Email`

**•** `In-App`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operator for the change that triggered the alert. For example, greater than.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The email addresses for the recipients of the alert details.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom alert that triggered the notification. This field is unique within your
organization.


Standard Objects TenantSecurityNotificationRule

**Field** **Details**

```
Status

Threshold

TriggerType

Version

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The status of the alert setting. The options are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The threshold value that triggered the alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger used for the alert. The values are:

**•** `Always`

**•** `On Change`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the custom alert.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationRuleChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantSecurityMetricDetailLink

**TenantSecurityNotificationRuleFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityNotificationRuleHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityNotificationRuleOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityNotificationRuleShare on page 67**
Sharing is available for the object.

### TenantSecurityMetricDetailLink

Represents the link between the metric count and metric drill down. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

MetricIdentifier

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
string


### Standard Objects TenantSecurityPackage

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

### `Tenant`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

### TenantSecurityPackage

Stores details about managed and unmanaged packages that are added, updated, or removed from a tenant in Security Center. Use this
object to identify whether new packages are installed, upgraded, or uninstalled from your connected tenants. This object is available to
Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on a package within a tenant. The options are:

**•** `Added`

**•** `Removed`


Standard Objects TenantSecurityPackage

**Field** **Details**

```
ActionDate

AppExchangeReady

DetailIdentifier

InstalledBy

MetricIdentifier

MetricsType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the action was taken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the package has passed AppExchange review.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user that installed the package.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.


Standard Objects TenantSecurityPackage

**Field** **Details**

```
Name

NamespacePrefix

PackageName

Publisher

ReleaseStatus

Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the package.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the package being added to or removed from the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the publisher that created the package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The release status of the package. The options are:

**•** `Beta`

**•** `Released`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityPolicy

**Field** **Details**

**Description**
The ID of the tenant that the package was added to or removed from.

```
TenantName

Version

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that the package was added to or removed from.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the package.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPackageChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPackageFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPackageHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPackageOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPackageShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicy

[Stores security policies created and deployed in Security Center. For more information, see Define and Deploy Security Policies. This](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects TenantSecurityPolicy

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
ApiName

Description

Name

PolicyData

PolicyIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The API name of the policy.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the policy.

**Type**
textarea

**Properties**
Create, Update

**Description**
The policy details contained in JSON format.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of this policy. Contains a unique virtual key from child to parent.


Standard Objects TenantSecurityPolicy

**Field** **Details**

```
PolicyType

SourceRowIdentifier

Status

Version

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The type of policy. For example, Health Check Baseline.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy that is applied to the tenant. This value is specific to the org that owns
this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the policy. For example, the policy is active or inactive.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The version of the policy.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects TenantSecurityPolicyDeployment

**TenantSecurityPolicyShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicyDeployment

[Stores the status of deployments of a Security Center policy on a tenant. For more information, see Define and Deploy Security Policies.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
This object is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
DeploymentDate

DeploymentStatus

Description

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date the deployment was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the deployment. For example, Not Deployed, Processing, Deployed, or Failed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the deployment status.


Standard Objects TenantSecurityPolicyDeployment

**Field** **Details**

```
Name

PolicyIdentifier

StatusDate

Tenant

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the TenantSecurityPolicy entity.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date that the status of the deployment was provided.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant for which the policy was deployed.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyDeploymentChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyDeploymentFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyDeploymentHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyDeploymentOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects TenantSecurityPolicySelectedTenant

**TenantSecurityPolicyDeploymentShare on page 67**
Sharing is available for the object.

### TenantSecurityPolicySelectedTenant

[Stores the list of tenants selected for a Security Center policy. For more information, see Define and Deploy Security Policies. This object](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
is available to Security Center subscribers in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is read/write.

Fields

**Field** **Details**

```
Name

PolicyIdentifier

### `Tenant`

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the policy for the selected tenant.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.


### Standard Objects TenantSecurityReportAnomaly

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicySelectedTenantChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicySelectedTenantFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicySelectedTenantHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicySelectedTenantOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPolicySelectedTenantShare on page 67**
Sharing is available for the object.

### TenantSecurityReportAnomaly

Stores anomalies in how users run or export reports, including unsaved reports, as detected by Threat Detection. For more information,
[see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DetailIdentifier

EventDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the detail record. This field is unique within your org.

**Type**
dateTime


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
The most granular setting is milliseconds.

```
EventIdentifier

EventName

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Report Anomaly.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

```
Report

Score

SecurityEventData

Summary

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the report for which this anomaly event was detected. If the anomaly resulted
from a user executing an unsaved report, the value of this field is null.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
A number from 0 through 100 that represents the anomaly score for the report execution
or export tracked by this event. The anomaly score indicates how the user’s current report
activity differs from their typical activity. A low score indicates that the current report activity
is similar to the user’s usual activity. A high score indicates that it’s different.

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the report activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time, but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows as a percentage how much a particular feature contributed to this anomaly event.
The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the report anomaly that caused this event.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityReportAnomaly

**Field** **Details**

**Description**
The ID of the tenant that was targeted in the event.

```
TenantName

UserIdentifier

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time the event was created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityReportAnomalyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityReportAnomalyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityReportAnomalyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityReportAnomalyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityReportAnomalyShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecuritySessionHijacking TenantSecuritySessionHijacking

Stores information about session hijacking events as detected by Threat Detection within connected tenants in Security Center. For
[more information, see Threat Detection. This object is available for Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
CurrentIp

CurrentPlatform

CurrentScreen

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the IP address didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousIp` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the platform didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousPlatform` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Description**
The screen of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the screen didn’t contribute to the observed fingerprint deviation, the
value of this field is the same as the `PreviousScreen` field.

```
CurrentUserAgent

CurrentWindow

DetailIdentifier

EventDate

EventIdentifier

```

**Type**
textarea

**Properties**
Nillable

**Description**
The user agent of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the user agent didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousUserAgent` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the observed fingerprint that deviates from the previous fingerprint.
The difference between the current and previous values is one indicator that a session
hijacking attack has occurred. If the window didn’t contribute to the observed fingerprint
deviation, the value of this field is the same as the `PreviousWindow` field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
The most granular setting is milliseconds.

**Type**
string


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

```
EventName

MetricIdentifier

MetricsType

Name

PreviousIp

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Session Hijacking.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the `CurrentIp`
field for the newly observed IP address.


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

```
PreviousPlatform

PreviousScreen

PreviousUserAgent

PreviousWindow

Score

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentPlatform` field for the newly observed platform.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The screen of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentScreen` field for the newly observed screen.

**Type**
textarea

**Properties**
Nillable

**Description**
The user agent of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentUserAgent` field for the newly observed user agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the previous fingerprint. The difference between the current and
previous values is one indicator that a session hijacking attack has occurred. See the
`CurrentWindow` field for the newly observed window.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort


Standard Objects TenantSecuritySessionHijacking

**Field** **Details**

**Description**
Specifies how much the new fingerprint deviates from the previous one. The score is from
6.0 through 21.0. The event exposes five field pairs (such as `CurrentIp` and
`PreviousIp` ) to view the before and after data for browser features that contributed to
this anomaly. See the `SecurityEventData` field for all contributing features in JSON
format. A large deviation score (6.0 or more) between two intra-session fingerprints indicates
that two different browsers are active in the same session. The presence of two active browsers
usually means that session hijacking has occurred.

```
SecurityEventData

Summary

Tenant

TenantName

```

**Type**
textarea

**Properties**
Nillable

**Description**
[The set of browser fingerprint features that triggered this event. See the Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
[documentation for the possible features. For example, a user’s current browser fingerprint](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
diverges from the previously known fingerprint. If Salesforce concludes the user’s session
was hijacked, it fires this event, and the contributing features are captured in this field in
JSON format. Each feature describes a browser fingerprint property, such as the browser user
agent, window, or platform. The data includes the current and previous values for each
feature.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the threat that caused this event. The summary lists the browser fingerprint
features that most contributed to the threat detection, along with their contribution to the
total score.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


### Standard Objects TenantSecurityTenantInfo

**Field** **Details**

**Description**
The name of the tenant that was targeted in the event.

```
UserIdentifier

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecuritySessionHijackingChangeEvent on page 68**
Change events are available for the object.

**TenantSecuritySessionHijackingFeed on page 55**
Feed tracking is available for the object.

**TenantSecuritySessionHijackingHistory on page 63**
History is available for tracked fields of the object.

**TenantSecuritySessionHijackingOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecuritySessionHijackingShare on page 67**
Sharing is available for the object.

### TenantSecurityTenantInfo

Stores information on changes related to the tenant history. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects TenantSecurityTenantInfo

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
DetailIdentifier

Instance

MyDomainName

Name

SandboxAlias

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier for this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The instance that the tenant is being hosted on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the domain for this tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which the data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias specified by the user when the user creates a Sandbox.


Standard Objects TenantSecurityTenantInfo

**Field** **Details**

```
SandboxType

Status

Tenant

TenantName

TenantType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type specified by the user when the user creates a Sandbox.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the tenant. For example, active or inactive.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The type of tenant in this org.


### Standard Objects TenantSecurityTransactionPolicyTrend

Usage

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTenantInfoChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityTenantInfoFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityTenantInfoHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityTenantInfoOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityTenantInfoShare on page 67**
Sharing is available for the object.

### TenantSecurityTransactionPolicyTrend

Stores changes to the count of Transaction Security Policies for a connected tenant within Security Center. This object is available for
Security Center subscribers in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`


Standard Objects TenantSecurityTransactionPolicyTrend

**Field** **Details**

**•** `UPDATED`

```
ActionBy

ActionConfig

ActionDate

DetailIdentifier

EventName

MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a JSON description for how a user is alerted to an action on the policy. For example:

**•** `In-app`

**•** `Email`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this change was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event of the corresponding Transaction Security Policy.

**Type**
string


Standard Objects TenantSecurityTransactionPolicyTrend

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

```
MetricsType

Name

Tenant

TenantName

TransactionPolicyState

TransactionPolicyType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The state of the transaction security policy. The possible states are `ENABLED` or `DISABLED` .

**Type**
string


### Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of policy configured. The available types are standard policy or a custom Apex
policy.

Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityPolicyFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityPolicyHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityPolicyOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityPolicyShare on page 67**
Sharing is available for the object.

### TenantSecurityTrigTransactionSecurityPol

Stores metric details related to Transaction Security Policy triggering events. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read only.

Fields

**Field** **Details**

```
ApexClass

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Description**
The name of the Apex class used to evaluate the policy.

```
ApexIdentifier

ClientIp

DetailIdentifier

FlowIdentifier

FlowName

LoginKey

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Flow used to evaluate the policy.

**Type**
String


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

```
MetricIdentfier

MetricsType

Name

Policy Identifier

PolicyName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy being evaluated.


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

```
PolicyOutcome

PolicyType

RequestIdentifier

RowVersion

SessionKey

Tenant

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects TenantSecurityTrigTransactionSecurityPol

**Field** **Details**

**Description**
The ID of the tenant of this triggered the Transaction Security Policy event.

```
TenantName

Timestamp

Triggered Timestamp

Uri

UserIdentifier

Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The access time of Salesforce services in GMT. Milliseconds are the most granular setting.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The time at which the Transaction Security event was generated.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

**Description**
The username of the user who’s using Salesforce services through the UI or the API.

### TenantSecurityTrustedIpRangeTrend

Stores details of changes related to trusted IP ranges in Security Center.This object is available for Security Center subscribers in API
version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime


Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
When this change was made.

```
Description

DetailIdentifier

IpEndAddress

IpRangeIdentifier

IpStartAddress

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A description of the trusted IP range. For example, "Trusting the IP addresses from NA-West
region".

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The end IP address of a trusted IP range. For example, `10.0.0.0 – 10.255.255.255` .

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of a trusted IP range. For example, `10.0.0.0 – 10.255.255.255` .


Standard Objects TenantSecurityTrustedIpRangeTrend

**Field** **Details**

```
MetricIdentifier

MetricsType

Name

Tenant

TenantName

UsageOptions

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.


### Standard Objects TenantSecurityUserActivity

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTrustedIpRangeTrendChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityTrustedIpRangeTrendFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityTrustedIpRangeTrendHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityTrustedIpRangeTrendOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityTrustedIpRangeTrendShare on page 67**
Sharing is available for the object.

### TenantSecurityUserActivity

Stores details related to how a user interacts with a tenant. Use this object to determine whether to reevaluate a user’s access to your
org for security purposes. You can check whether a user has never logged in, hasn’t been active for 90 days, has a frozen account, or
isn’t using multi-factor authentication. This object is available to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
DetailIdentifier

LastLoginDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TenantSecurityUserActivity

**Field** **Details**

**Description**
The last time the user logged in.

```
MetricIdentifier

MetricsType

Name

Tenant

TenantName

UserCreatedDate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where the user activity happened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TenantSecurityUserActivity

**Field** **Details**

**Description**
The date that the user was created.

```
UserEmail

UserLicense

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserActivityChangeEvent on page 68**
Change events are available for the object.

**TenantSecurityUserActivityFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityUserActivityHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityUserActivityOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityUserActivityShare on page 67**
Sharing is available for the object.


### Standard Objects TenantSecurityUserPerm TenantSecurityUserPerm

Stores information on permissions assigned to a user. Use this object to see which tenants a user is assigned to. This object is available
to Security Center subscribers in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object can only be read and queried.

Fields

**Field** **Details**

```
Action

ActionBy

ActionDate

Context

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken regarding the user’s permission. The options are:

**•** `Added`

**•** `Removed`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the permission action was taken.

**Type**
string


Standard Objects TenantSecurityUserPerm

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile or permission set assigned to the user.

```
ContextType

DetailIdentifier

MetricIdentifier

MetricsType

Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Indicates the method through which the permission was granted. The options are:

**•** `Permission Set`

**•** `Profile`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of metric that the assigned permission represents.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.


Standard Objects TenantSecurityUserPerm

**Field** **Details**

```
Tenant

TenantName

UserEmail

UserLicense

Username

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s email address.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserPermChangeEvent on page 68**
Change events are available for the object.


### Standard Objects TenantUsageEntitlement

**TenantSecurityUserPermFeed on page 55**
Feed tracking is available for the object.

**TenantSecurityUserPermHistory on page 63**
History is available for tracked fields of the object.

**TenantSecurityUserPermOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantSecurityUserPermShare on page 67**
Sharing is available for the object.

### TenantUsageEntitlement

Represents a data structure that contains information about the features or functionalities that a Salesforce org has access to. This object
is available in API version 28.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AmountUsed

CurrentAmountAllowed

EndDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The quantity of an entitlement that has been used.

**Type**
double

**Properties**
Filter, Sort

**Description**
The amount of an entitlement that a tenant is allowed to use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The end date of the setting, based on license end dates that entitle the org to that setting.


Standard Objects TenantUsageEntitlement

**Field** **Details**

```
Frequency

HasRollover

IsPersistentResource

MasterLabel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How often the tenant's entitlement data is automatically reviewed to see how much of the
entitlement has been used.

Possible values are:

**•** `Daily`

**•** `Fortnightly`

**•** `Monthly`

**•** `Once`

**•** `Quarterly`

**•** `Weekly`

**•** `Yearly`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that a certain amount of a customer's unused entitlements from a set time period
can be added to the next set time period. This field is reserved for future use.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the data that will be saved and available for future use even after closing a
session.

The default value is `false` .

**Type**
string

**Properties**
Group, Nillable


Standard Objects TenantUsageEntitlement

**Field** **Details**

**Description**
The overarching name of an element in your organization. A MasterLabel is visible to
customers.

```
OverageGrace

ResourceGroupKey

Setting

StartDate

UsageDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the Allowed Amount that a customer can use without incurring an
additional charge. The default value is 100% (no overage grace). This field is reserved for
future use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Tracks resource usage across different segments for the same setting. For example, a Messages
entitlement that tracks email messages and SMS messages separately could have one
ResourceGroupKey of SMS and another ResourceGroupKey of Email. In most cases though,
TenantUsageEntitlements are configured for the org and not by segment.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A rule or attribute that can be used to configure the appearance or actions in an organization.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
This date is the earliest start date of any license contributing to the provisioning aggregation
output.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects Territory

**Field** **Details**

**Description**
The date an event occurred that deducted from the tenant's entitlement.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantUsageEntitlementChangeEvent on page 68**
Change events are available for the object.

**TenantUsageEntitlementFeed on page 55**
Feed tracking is available for the object.

**TenantUsageEntitlementHistory on page 63**
History is available for tracked fields of the object.

**TenantUsageEntitlementOwnerSharingRule on page 65**
Sharing rules are available for the object.

**TenantUsageEntitlementShare on page 67**
Sharing is available for the object.

### Territory

Represents a flexible collection of accounts and users where the users have at least read access to the accounts, regardless of who owns
the accounts. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Standard and partner users can access this object. Users assigned to the Manage Territories permission set can edit this object.

Fields

**Field** **Details**

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects Territory

**Field** **Details**

**Description**
Account access level granted to users assigned to this territory.

```
CaseAccessLevel

ContactAccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Case access level granted to users assigned to this territory.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
A value that represents the type of access granted to the target Group, UserRole, or
User for any associated contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: When `DefaultContactAccess` is set to “Controlled by Parent,”
you can’t create or update this field.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the territory that is 1,000 characters or less.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Territory Name** in the user interface.


Standard Objects Territory

**Field** **Details**

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
ForecastUserId

MayForecastManagerShare

Name

OpportunityAccessLevel

ParentTerritoryID

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Forecast Manager, who is the user to whom forecasts from this territory’s
child territories roll up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecast manager can manually share their own forecast.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A name for the territory. Limit is 80 characters. Corresponds to **Label** on the user
interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Opportunity access level granted to users assigned to this territory.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Territory immediately above this territory in the territory hierarchy. Label is **Parent**
**Territory ID** .


### Standard Objects TerritoryMgmtObjectConfig

**Field** **Details**

```
RestrictOppTransfer

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the opportunities associated with this territory are kept within the
bounds of this territory and this territory’s children when account assignment rules
are run ( `true` ), or if opportunities associated with this territory can be assigned to
other nodes of the territory hierarchy when account assignment rules are run ( `false` ).
Label is **Confine Opportunity Assignment** .

Use the Territory object to query your organization’s territory hierarchy. Use it to obtain valid territory IDs when querying or modifying
records associated with territories.

SEE ALSO:

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem

UserTerritory

### TerritoryMgmtObjectConfig

Represents territory management settings and defaults for a particular object. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only standard and partner users can access this object.

Fields

**Field** **Details**

```
DefaultAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects TerritoryMgmtObjectConfig

**Field** **Details**

**Description**
The default access level of the defined object for all territories.

```
DeveloperName

Language

MasterLabel

Object

State

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org where the territory model was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The readable label for this entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The name of the Enterprise Territory Management object.

Possible values are:

**•** `Lead`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the supported object.


### Standard Objects Territory2 Territory2

Represents a sales territory. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
AccountAccessLevel

CaseAccessLevel

ContactAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default account record access levels for users that are assigned
to the territory. Values are:

**•** `Read Only`

**•** `Read/Write`

**•** `Owner`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default case record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
picklist


Standard Objects Territory2

**Field Name** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the default contact record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

```
Description

DeveloperName

ForecastUserId

Name

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the territory. The field label in the user interface is `Territory`
`Description` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of a territory’s forecast manager. To select a
`ForecastUserId`, select someone in the list of users assigned to the territory.

**Type**
string


Standard Objects Territory2

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the territory. The field label in the user interface is `Territory`
`Label` .

```
OpportunityAccessLevel

ParentTerritory2Id

Territory2ModelId

Territory2TypeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default opportunity record access levels for users that are assigned
to the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory’s parent territory (if any). If the territory has no parent
territory, this value is `null` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory model that the territory belongs to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the territory type that the territory belongs to.


### Standard Objects Territory2AlignmentLog Territory2AlignmentLog

Represents the start and end status of a territory assignment rule run job. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users can’t view territory models in other states (such as `Planning`
or `Archived` ).

Fields

**Field** **Details**

```
EndTime

Filter

RunAsId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the assignment rule run job finished.

**Type**
textarea

**Properties**
Nillable

**Description**
Criteria to filter the rule jobs. For example, {RULE_LAST_MOD_DATE_FORM=2021-08-31,
RULE_LAST_MOD_DATE_TO=2021-09-15}.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Salesforce user who started the assignment rule run job.

This is a relationship field.


Standard Objects Territory2AlignmentLog

**Field** **Details**

**Relationship Name**
RunAs

**Relationship Type**
Lookup

**Refers To**
User

```
StartTime

Status

Territory2Id

Territory2ModelId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user started the assignment rule run job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the assignment rule run job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory for which the assignment rule run was performed. If the assignment
rule run was for the territory model, this value is null.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects Territory2Model

**Field** **Details**

**Description**
The ID of the territory model for which the assignment rule run was performed.

This is a relationship field.

**Relationship Name**
### Territory2Model

**Relationship Type**
Lookup

**Refers To**
### Territory2Model

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**Territory2AlignmentLogChangeEvent**

Change events are available for the object.

### Territory2Model

Represents a territory model. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
ActivatedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Territory2Model

**Field Name** **Details**

**Description**
The date when the territory model was activated.

```
DeactivatedDate

Description

DeveloperName

LastOppTerrAssignEndDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory model was archived.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory model.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Model Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. The date when the opportunity territory assignment filter was last
run. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15
/ API version 33).


### Standard Objects Territory2ModelHistory

**Field Name** **Details**

```
LastRunRulesEndDate

Name

State

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the last rules run was completed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory model name. The field label in the user interface is `Label` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The state of the territory model. Values are: `Planning`, `Activating`,
`Activation Failed`, `Active`, `Archiving`, `Archiving Failed`,
`Archived`, `Deleting`, and `Deletion Failed` .

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**Territory2ModelChangeEvent (API version 62.0)**
Change events are available for the object.

**Territory2ModelFeed**

Feed tracking is available for the object.

### **Territory2ModelHistory**

History is available for tracked fields of the object.

### Territory2ModelHistory

Represents the history of changes to the values in the fields on a territory model. Available if Sales Territories has been enabled.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects Territory2ModelHistory

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

Territory2ModelId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field whose value was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the territory model whose history is tracked.


### Standard Objects Territory2ObjectExclusion

Usage

This object is automatically generated whenever any field value changes on a territory model record. Use this object it to identify those
changes.

### Territory2ObjectExclusion

Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This object
is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your org’s sharing settings. Users can’t view territory models in other states (such as `Planning`
or `Archived` ).

Fields

**Field** **Details**

```
Note

ObjectId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Account object to exclude from the territory assignment rule.

This is a polymorphic relationship field.

**Relationship Name**
Object

**Relationship Type**
Lookup


### Standard Objects Territory2ObjSharingConfig

**Field** **Details**

**Refers To**
Account

```
Territory2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory to exclude from the territory model assignment rule.

This is a relationship field.

**Relationship Name**
### Territory2

**Relationship Type**
Lookup

**Refers To**
### Territory2

### Territory2ObjSharingConfig

Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

Only standard and partner users can access this object. Any standard or partner user can view object sharing configuration records in
an active model. Users without the Manage Territories permission can’t view territory records in the `Planning` or `Archived` state.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The access level of the object for the particular territory.


### Standard Objects Territory2Type

**Field** **Details**

```
Territory2Id

TerritoryMgmtObjectConfigId

### Territory2Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The territory on which the access level is defined.

This field is a relationship field.

**Relationship Name**
### Territory2

**Relationship Type**
Lookup

**Refers To**
### Territory2

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The object configuration record the territory access level is related to.

This field is a relationship field.

**Relationship Name**
TerritoryMgmtObjectConfig

**Relationship Type**
Lookup

**Refers To**
TerritoryMgmtObjectConfig

Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has been
enabled for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard and partner users can access this object.


Standard Objects Territory2Type

Fields

**Field Name** **Details**

```
Description

DeveloperName

Language

MasterLabel

Priority

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Type Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the label in the user interface.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required The user interface label for the territory type.

**Type**
int


### Standard Objects TerritoryAdminAssignment

**Field Name** **Details**

**Properties**
Create, Filter, Group, SortUpdate

**Description**
Required. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring
’15 / API version 33). Lets you specify a priority for a territory type. For opportunity
assignments, the filter examines all territories assigned to the account that the
opportunity is assigned to. The account-assigned territory whose territory type
priority is highest is then assigned to the opportunity. The `priority` field
value on each territory type must be unique. Further, if there are multiple territories
with the same territory type (and therefore the same priority) assigned to the
account, no territory is assigned to the opportunity.

### TerritoryAdminAssignment

Represents designated team members who can administer specific territories and their descendants. This object is available in API version
63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To designate team members, assign them the Administer Territory Operations permission.

Fields

**Field** **Details**

```
CanManageHierarchy

CanManageMembers

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user update and delete the territory and its descendants, and create descendants.

The default value is `false` .

**Type**
boolean


Standard Objects TerritoryAdminAssignment

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user assign other team members to the territory and its descendants. Also lets the
user update the user territory association log.

The default value is `false` .

```
CanManageRecordAssociations

Territory2Id

Territory2ModelId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user add and remove assignments for records, author rules, and assign and run rules
for the territory and its descendants.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory you’re letting the user administer. The user can also administer this
territory’s descendants.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory model that includes the territory you’re letting the user administer.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model


### Standard Objects TestSuiteMembership

**Field** **Details**

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the user you’re letting administer the territory and its descendants. Requires that
the user is assigned the Administer Territory Operations permission set.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Refers To**
Group, User

### TestSuiteMembership

Associates an Apex class with an ApexTestSuite. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
ApexClassId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The Apex class whose tests are to be executed.

This is a relationship field.

**Relationship Name**
ApexClass


### Standard Objects ThirdPartyAccountLink

**Field Name** **Description**

**Relationship Type**
Lookup

**Refers To**
ApexClass

```
ApexTestSuiteId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The test suite to which the Apex class is assigned.

This is a relationship field.

**Relationship Name**
ApexTestSuite

**Relationship Type**
Lookup

**Refers To**
ApexTestSuite

Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.

The following SOQL query returns the membership object that relates this Apex class to this test suite.

```
SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'

   AND ApexTestSuiteId = '05FD00000004CDBMA2'

```

SEE ALSO:

ApexTestSuite

### ThirdPartyAccountLink

Represents the list of external users who authenticated using an authentication provider. This object is available in API version 32.0 and
later.

A list of third-party account links is generated when users of an organization authenticate using an external authentication provider. Use
this object to list and revoke a given user's social sign-on connections (such as Facebook [©] ).


Standard Objects ThirdPartyAccountLink

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
description.

```
   A callout was unsuccessful because of pending uncommitted work related to a process, flow,

    or Apex operation.

   Commit or roll back the work, and then try again.

```

To avoid this error, execute DML operations and queries in separate, asynchronous calls.

Fields

**Field Name** **Details**

```
Handle

IsNotSsoUsable

Provider

RemoteIdentifier

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The username in the third-party system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Sort

**Description**
Support for single sign-on.

If _`true`_, the link can't be used for a single sign-on flow. It's only available OAuth
access and refresh tokens.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The third-party account provider name.

**Type**
string


Standard Objects ThirdPartyAccountLink

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The unique ID for the user in the third-party system.

```
SsoProvider

SsoProviderId

SsoProviderName

ThirdPartyAccountLinkKey

```

**Type**
AuthProvider

**Properties**
Filter, Nillable, Sort

**Description**
The foreign key to the AuthProvider on page 883 of the third-party system.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The ID associated with the `SsoProvider` value.

This is a relationship field.

**Relationship Name**
SsoProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name associated with the AuthProvider of the third-party system, in case
the user has no access to the provider foreign key (the `SsoProvider` value).

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A concatenated string including the organization ID, the `SsoProviderId`
value, the `SsoProvider` value, and the `RemoteIdentifier` value.


Standard Objects ThirdPartyAccountLink

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The Salesforce user associated with this third-party account link.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Admins (with the Manage Users permission) querying this object can see all the links for all users in the organization. Without the Manage
Users permission, users can only retrieve their own links. Users sometimes don't have access to the `SsoProvider` value (the foreign
key). In this case, use the `SsoProviderName` to render the name of the provider for the associated link.

Use the Apex method `Auth.AuthToken.revokeAccess()` to revoke a link. To use this method, the `IsNotSsoUsable`
field must be `false` .

To make the ThirdPartyAccountLink standard object writable for Salesforce admins, contact Salesforce Customer Support. With this
feature, you can easily add or delete third-party account links using the API, but you can’t update existing account links.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `query()` call returns up to 500 rows.
A queryMore() call returns 500 more, up to 2,500 total. No more records are returned after 2,500. To make sure that you don’t miss any
records, issue a `COUNT()` query in a SELECT clause for ThirdPartyAccountLink. This query gives you the total number of records. If there
are more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2000 OFFSET 0

```

Then, run another query with an offset of 2,000.

```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2000 OFFSET 2000

```

Continue to increase the offset by 2,000 until you have results for all records.


### Standard Objects ThreatDetectionFeedback ThreatDetectionFeedback

Represents feedback provided by a user about a Threat Detection event that occurred in your org. The feedback specifies whether the
event was malicious, suspicious, not a threat, or unknown. Each ThreatDetectionFeedback object is associated with one of these Threat
Detection storage events: ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore, or SessionHijackingEventStore.
This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Response

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the severity of the threat.

Possible values are:

**•** `Malicious`

**•** `Not a Threat`

**•** `Suspicious`

**•** `Unknown`


Standard Objects ThreatDetectionFeedback

**Field** **Details**

```
ThreatDetectionEventId

ThreatDetectionFeedbackNumber

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the unique ID of one of these associated Threat Detection storage events:

**•** [ApiAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_apianomalyeventstore.htm)

**•** [CredentialStuffingEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_credentialstuffingeventstore.htm)

**•** [ReportAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_reportanomalyeventstore.htm)

**•** [SessionHijackingEventStore](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_sessionhijackingeventstore.htm)

For example, `0fjRM000000005p` .

This is a polymorphic relationship field.

**Relationship Name**
ThreatDetectionEvent

**Relationship Type**
Lookup

**Refers To**
ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore,
SessionHijackingEventStore

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number used as the unique name for this object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID. For example, `005000000000123` .

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects TimeSheet

**Field** **Details**

```
Username

```

Associated Object

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the object was
created.

This object has the following associated object. It’s available in the same API version as this object.

**ThreatDetectionFeedbackFeed**

Feed tracking is available for the object.

SEE ALSO:

_Salesforce Help_ [: Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_detection.htm&type=5&language=en_US)

### TimeSheet

Represents a schedule of a service resource’s time in Field Service or Workforce Engagement. This object is available in API v47.0 and
later.

Time sheets are composed of time sheet entries, which typically track individual tasks like travel or asset repair.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects TimeSheet

**Field Name** **Details**

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
`Currency ISO Code` .

```
EndDate

LastReferencedDate

LastViewedDate

OwnerId

ServiceResourceId

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The last day the time sheet covers.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the time sheet.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource whose time is being tracked with the time sheet.


Standard Objects TimeSheet

**Field Name** **Details**

```
StartDate

Status

TimeSheetEntryCount

TimeSheetNumber

TotalDurationInHours

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the time sheet covers.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet. The picklist includes the following values, which
can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The number of related time sheet entries.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the time sheet.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in hours.


### Standard Objects TimeSheetEntry

**Field Name** **Details**

```
TotalDurationInMinutes

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in minutes.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetFeed**

Feed tracking is available for the object.

**TimeSheetHistory**

History is available for tracked fields of the object.

**TimeSheetOwnerSharingRule**

Sharing rules are available for the object.

**TimeSheetShare**

Sharing is available for the object.

### TimeSheetEntry

Represents a span of time that a service resource spends on a field service task. This object is available in API version 47.0 and later.

Time sheets are composed of time sheet entries. Time sheet entries typically track individual tasks like travel or asset repair.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects TimeSheetEntry

Fields

**Field Name** **Details**

```
CurrencyIsoCode

Description

DurationInMinutes

EndTime

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
`Currency ISO Code` .

Time sheet entries inherit their time sheet’s currency code. Updates to a time
sheet’s currency code aren’t reflected in existing time sheet entries’ currency
code.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes on how the time was spent. For example, “This service took longer than
normal because the machine was jammed.”

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Minutes recorded on the time sheet entry.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects TimeSheetEntry

**Field Name** **Details**

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

```
LastViewedDate

LocationTimeZone

StartTime

Status

Subject

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the location where the activity occurred.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity began.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet entry. The picklist includes the following values,
which can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
string


Standard Objects TimeSheetEntry

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Activity performed; for example, repair, lunch, or travel.

```
TimeSheetEntryNumber

TimeSheetId

Type

WorkOrderId

WorkOrderLineItemId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the time sheet entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The time sheet associated with the time sheet entry.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of work performed. The picklist includes the following values, which
can be customized:

**•** Direct

**•** Indirect

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order related to the time sheet entry. Work orders are searchable by
their content.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects TimeSlot

**Field Name** **Details**

**Description**
The work order line item related to the time sheet entry. Work order line items
are searchable by their content.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetEntryChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetEntryFeed**

Feed tracking is available for the object.

**TimeSheetEntryHistory**

History is available for tracked fields of the object.

### TimeSlot

Represents a period of time on a specified day of the week during which work can be performed in Field Service, Salesforce Scheduler,
or Workforce Engagement. Operating hours consist of one or more time slots. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DayOfWeek

EndTime

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The day of the week when the time slot takes place.

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot ends.


Standard Objects TimeSlot

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

MaxAppointments

OperatingHoursId

StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced ( `LastReferencedDate` )
and not viewed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of appointments for a single time slot. Available in API version
47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The operating hours that the time slot belongs to. An operating hours’ time slots
appear in the Operating Hours related list.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
time


Standard Objects TimeSlot

**Field Name** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot starts.

```
RecordSetFilterCriteriaId

TimeSlotNumber

Type

WorkTypeGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria selected for the time slot.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the time slot. The name is auto-populated to a day and time
format—for example, `Monday 9:00 AM - 10:00 PM` —but you can
manually update it if you wish.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are _`Normal`_ and _`Extended`_ . You may
choose to use _`Extended`_ to represent overtime shifts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects TimeSlotHistory

**Field Name** **Details**

**Description**
Work type group assigned to the time slot. Available in API version 47.0 and later.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

Usage

Operating hours are composed of time slots, which indicate the hours of operation for a particular day. After you create operating hours,
create time slots for each day. For example, if the operating hours should be 8 AM to 5 PM Monday through Friday, create five time slots,
one per day. To reflect breaks such as lunch hours, create multiple time slots in a day: for example, _`Monday 8:00 AM – 12:00`_
_`PM`_ and _`Monday 1:00 PM – 5:00 PM`_ .

Tip: Time slots don’t come with any built-in rules, but you can create Apex triggers that limit time slot settings in your org. For
example, you may want to restrict the start and end times on time slots to half-hour increments, or to prohibit end times later
than 8 PM.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[TimeSlotChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **TimeSlotHistory (API version 62.0)**

History is available for tracked fields of the object.

### TimeSlotHistory

Represents the history of changes made to tracked fields on a time slot. This object is available in API version 38.0 and later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for time slot fields must be configured.


### Standard Objects TodayGoal

Fields

**Field Name** **Details**

```
Field

NewValue

OldValue

TimeSlotId

### TodayGoal

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the time slot being tracked. The history is displayed on the detail page for
this record.

Sets the quarterly sales goal on the performance chart. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects TodayGoal

Fields

**Field** **Details**

```
IsLocked

MayEdit

Name

OwnerId

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the goal is locked, or `false` if it’s not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the goal can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the goal.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the creator of the goal.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects Topic

**Field** **Details**

**Description**
The ID of the user of the goal.

This field is unique within your organization.

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

```
Value

```

Usage

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The customizable sales goal for the quarter.

This object is specific to the performance chart and has no impact on forecast quotas or any other type of goal. The performance chart
is available on the home page when Seller Home is not enabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TodayGoalChangeEvent on page 68**
Change events are available for the object.

**TodayGoalShare on page 67**
Sharing is available for the object.

### Topic

Represents a topic on a Chatter post or record. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`


Standard Objects Topic

Fields

**Field Name** **Details**

```
Description

ManagedTopicType

Name

NetworkId

TalkingAbout

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of managed topic. Values are:

**•** `Content`

**•** `Featured`

**•** `Navigational`

This field is available in API version 44.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

Note: You can change only the spacing and capitalization of a topic
name with the update property.

**Description**
Name of the topic.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort

**Description**
Identifier of the Experience Cloud site to which the topic belongs. This field is
available only if digital experiences is enabled in your org.

**Type**
int

**Properties**
Filter, Group, Sort


### Standard Objects TopicAssignment

**Field Name** **Details**

**Description**
Number of people talking about the topic over the last two months, based on
factors such as topic additions and comments on posts with the topic.

Usage

Use this object to query a specific topic or to get a list of all topics, even those used solely in private groups and on records, and the
number of people talking about them.

Use this object to create, edit, or delete topics. To create a topic, you must have the Create Topics permission. To edit a topic, you must
have the Edit Topics permission. To delete a topic, you must have the Delete Topics or Modify All Data permission.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TopicFeed (API version 29.0)**
Feed tracking is available for the object.

### TopicAssignment

Represents the assignment of a topic to a specific feed item, record, or file. This object is available in API version 28.0 and later.

Administrators must enable topics for objects before users can add topics to records of that object type. Topics for most objects are
available in API version 30.0 and later. Topics for ContentDocument are available in API version 37.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `delete()`, `getDeleted()`, `getUpdate()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EntityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the feed item, record, or file.

This is a polymorphic relationship field.

**Relationship Name**
Entity


Standard Objects TopicAssignment

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Asset, Campaign, Case, Contact, ContentDocument, Contract, Event,
FeedItem, Lead, Opportunity, Order, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shift, Shipment, Solution, Task, WorkOrder,
WorkOrderLineItem

```
EntityKeyPrefix

EntityType

NetworkId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The first three digits of the `EntityID` field, which identify the object type
(account, opportunity, etc). This read-only field is available in API version 32.0
and later.

Interface label is “Record Key Prefix,” which appears only in reports.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The standard name for the object type (account, opportunity, etc). This read-only
field is available in API version 33.0 and later.

Note: Querying topic assignments for the ManagedContentVersion entity
type isn’t supported.

Interface label is “Object Type,” which appears only in reports.

Tip: In most cases, you should use this field rather than
`EntityKeyPrefix`, which exists primarily to support older reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the TopicAssignment belongs. This field is
available only if digital experiences is enabled in your org.


### Standard Objects TopicLocalization

**Field Name** **Details**

```
TopicId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the topic.

This is a relationship field.

**Relationship Name**
### Topic

**Relationship Type**
Lookup

**Refers To**
### Topic

Use this object to query the assignments of topics to feed items, records, or files. To assign or remove topics, you must have the “Assign
Topics” permission.

In SOQL `SELECT` syntax, this object supports nested semi-joins, allowing queries on Knowledge articles assigned to specific topics.
For example:

```
SELECT parentId FROM KnowledgeArticleViewStat

   WHERE parentId in (SELECT KnowledgeArticleId FROM KnowledgeArticleVersion

   WHERE publishStatus = 'Online' AND language = 'en_US'

   AND Id in (select EntityId from TopicAssignment where TopicId ='0T0xx0000000xxx'))

```

There is no SOQL limit if the logged-in user has the “View All Data” permission. If they do have that permission, do one of the following:

**•** Specify a LIMIT clause of 1,100 records or fewer.

**•** Filter on `Id` or `Entity` when using a `WHERE` clause with "=".

Important: Deleting this object's records removes all its data. This action is irreversible.

Note: When you create a report type on the TopicAssignment object, all queries are generated in SQL, which does not enforce
the 1,100 record limit clause.

SEE ALSO:

### Topic

FeedItem

### TopicLocalization

Represents the translated version of a topic name. Topic localization applies only to navigational and featured topics in Experience Cloud
sites. This object is available in API version 33.0 and later.


Standard Objects TopicLocalization

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Users with the Translation Workbench enabled can view topic translations, but the Customize Application, Manage Translation, or
Manage Categories permission is required to create or update them.

Fields

**Field Name** **Details**

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The combined language and locale ISO code, which controls the language for
labels displayed in an application. (The values in this field are not related to the
default locale selection.)

This picklist contains the following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`


Standard Objects TopicLocalization

**Field Name** **Details**

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

The following end-user only languages are available.

**•** Arabic: `ar`

**•** Bulgarian: `bg`

**•** Croatian: `hr`

**•** Czech: `cs`

**•** English (UK): `en_GB`

**•** Greek: `el`

**•** Hebrew: `iw`

**•** Hungarian: `hu`

**•** Indonesian: `in`

**•** Polish: `pl`

**•** Portuguese (European): `pt_PT`

**•** Romanian: `ro`

**•** Slovak: `sk`

**•** Slovenian: `sl`

**•** Turkish: `tr`

**•** Ukrainian: `uk`

**•** Vietnamese: `vi`

The following platform languages are available for organizations that use Salesforce
exclusively as a platform.

**•** Albanian: `sq`

**•** Afrikaans: `af`

**•** Amharic: `am`

**•** Arabic (Algeria): `ar_DZ`

**•** Arabic (Bahrain): `ar_BH`

**•** Arabic (Egypt): `ar_EG`

**•** Arabic (Iraq): `ar_IQ`

**•** Arabic (Jordan): `ar_JO`

**•** Arabic (Kuwait): `ar_KW`

**•** Arabic (Lebanon): `ar_LB`

**•** Arabic (Libya): `ar_LY`

**•** Arabic (Morocco): `ar_MA`

**•** Arabic (Oman): `ar_OM`

**•** Arabic (Qatar): `ar_QA`

**•** Arabic (Saudi Arabia): `ar_SA`

**•** Arabic (Sudan): `ar_SD`


Standard Objects TopicLocalization

**Field Name** **Details**

**•** Arabic (Syria): `ar_SY`

**•** Arabic (Tunisia): `ar_TN`

**•** Arabic (United Arab Emirates): `ar_AE`

**•** Arabic (Yemen): `ar_YE`

**•** Armenian: `hy`

**•** Basque: `eu`

**•** Bosnian: `bs`

**•** Bengali: `bn`

**•** Burmese: `my`

**•** Catalan: `ca`

**•** Chinese (Hong Kong): `zh_HK`

**•** Chinese (Singapore): `zh_SG`

**•** Chinese (Malaysia): `zh_MY`

**•** Dutch (Belgium): `nl_BE`

**•** English (Australia): `en_AU`

**•** English (Belgium): `en_BE`

**•** English (Canada): `en_CA`

**•** English (Cyprus): `en_CY`

**•** English (Germany): `en_DE`

**•** English (Hong Kong): `en_HK`

**•** English (India): `en_IN`

**•** English (Ireland): `en_IE`

**•** English (Israel): `en_IL`

**•** English (Malaysia): `en_MY`

**•** English (Malta): `en_MT`

**•** English (Netherlands): `en_NL`

**•** English (New Zealand): `en_NZ`

**•** English (Philippines): `en_PH`

**•** English (Singapore): `en_SG`

**•** English (South Africa): `en_ZA`

**•** English (United Arab Emirates): `en_AE`

**•** Estonian: `et`

**•** Farsi: `fa`

**•** French (Belgium): `fr_BE`

**•** French (Canada): `fr_CA`

**•** French (Luxembourg): `fr_LU`

**•** French (Morocco): `fr_MA`

**•** French (Switzerland): `fr_CH`


Standard Objects TopicLocalization

**Field Name** **Details**

**•** Georgian: `ka`

**•** German (Austria): `de_AT`

**•** German (Belgium): `de_BE`

**•** German (Luxembourg): `de_LU`

**•** German (Switzerland): `de_CH`

**•** Greek (Cyprus): `el_CY`

**•** Greenlandic: `kl`

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Icelandic: `is`

**•** Irish: `ga`

**•** Italian (Switzerland): `it_CH`

**•** Kannada: `kn`

**•** Kazakh: `kk`

**•** Khmer: `km`

**•** Latvian: `lv`

**•** Lithuanian: `lt`

**•** Luxembourgish: `lb`

**•** Macedonian: `mk`

**•** Malay: `ms`

**•** Malayalam: `ml`

**•** Maltese: `mt`

**•** Marathi: `mr`

**•** Montenegrin: `sh_ME`

**•** Romanian (Moldova): `ro_MD`

**•** Romansh: `rm`

**•** Russian (Armenia): `ru_AM`

**•** Russian (Belarus): `ru_BY`

**•** Russian (Kazakhstan): `ru_KZ`

**•** Russian (Kyrgyzstan): `ru_KG`

**•** Russian (Lithuania): `ru_LT`

**•** Russian (Moldova): `ru_MD`

**•** Russian (Poland): `ru_PL`

**•** Russian (Ukraine): `ru_UA`

**•** Samoan: `sm`

**•** Serbian (Cyrillic): `sr`


Standard Objects TopicLocalization

**Field Name** **Details**

**•** Serbian (Latin): `sh`

**•** Spanish (Argentina): `es_AR`

**•** Spanish (Bolivia): `es_BO`

**•** Spanish (Chile): `es_CL`

**•** Spanish (Colombia): `es_CO`

**•** Spanish (Costa Rica): `es_CR`

**•** Spanish (Dominican Republic): `es_DO`

**•** Spanish (Ecuador): `es_EC`

**•** Spanish (El Salvador): `es_SV`

**•** Spanish (Guatemala): `es_GT`

**•** Spanish (Honduras): `es_HN`

**•** Spanish (Nicaragua): `es_NI`

**•** Spanish (Panama): `es_PA`

**•** Spanish (Paraguay): `es_PY`

**•** Spanish (Peru): `es_PE`

**•** Spanish (Puerto Rico): `es_PR`

**•** Spanish (United States): `es_US`

**•** Spanish (Uruguay): `es_UY`

**•** Spanish (Venezuela): `es_VE`

**•** Swahili: `sw`

**•** Tagalog: `tl`

**•** Tamil: `ta`

**•** Te reo: `mi`

**•** Telugu: `te`

**•** Urdu: `ur`

**•** Welsh: `cy`

**•** Xhosa: `xh`

**•** Zulu: `zu`

```
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.


### Standard Objects TopicUserEvent

**Field Name** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
ParentId

Value

### TopicUserEvent

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID that identifies the topic. After a TopicLocalization record is created, this ID can’t
be modified.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the topic name. Label is **Topic Name Translation** .

Represents an action (such as comment, post, like, or share) made by a user on a topic. This object is available in API version 42.0 and
later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with the Modify All Data permission can view and delete these data.


Standard Objects TopicUserEvent

Fields

**Field** **Details**

```
ActionEnum

NetworkId

TopicId

UserId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action taken by a user on a topic. The possible values are:

**•** LIKE

**•** COMMENT

**•** POST

**•** ASSIGN

**•** SHARE

**•** FAVORITE

**•** UNFAVORITE

**•** AT_MENTION

**•** BANG_MENTION

**•** COMMENT_LIKE

**•** USER_ENDORSEMENT

**•** SKILL_PEER_ENDORSEMENT

**•** SKILL_SELF_ENDORSEMENT

**•** BEST_ANSWER

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site where the action was performed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifier of the topic.

**Type**
reference


### Standard Objects TopInsight

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Unique Salesforce user ID.

Usage

Use the TopicUserEvent object to delete topic-related activities by Experience Cloud site users who would like all their topic-related
activities to be removed from a site.

### TopInsight

For internal use only.

### TransactionSecurityPolicy

Represents a transaction security policy definition.

This object is available in API version 42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionConfig

ApexPolicyId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Describes the action to take when the matching Transaction Security policy is triggered. Also
indicates the type of notifications selected and the ID of the intended recipient. The recipient
must be active and assigned the Modify All Data and View Setup user permissions. Multiple
actions can be taken. The actions available depend on the `Event Type` field.

**Type**
reference


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Apex `TxnSecurity.PolicyCondition` or
`TxnSecurity.EventCondition` interface for this policy.

```
BlockMessage

CustomEmailContent

Description

```

**Type**
string

**Properties**
Create,Filter, Nillable, Sort, Update

**Description**
The custom message sent to a user when a policy blocks their action. Used in Real-Time
Event Monitoring only. Maximum of 1000 characters. This field is null when the default
message option is selected in the UI. Available only when `EventName` is set to `ApiEvent`,
`ListViewEvent`, `BulkApiResultEventStore`, or `ReportEvent` . Available
in API version 49.0 and later.

Include org- or policy-specific information in your custom message, such as the name of the
responsible administrator or the business unit. Be careful about what you include. Too much
information on how the policy was designed. can aid a malicious user.

Two-factor authentication (2FA) isn’t supported in Lightning Experience, so events like
`ListView` and `ReportEvent` are upgraded to Block in Lightning.

Custom messages aren’t translatable.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The administrator-created custom email content sent when a policy is triggered. Used in
Real-Time Event Monitoring only. Maximum of 1333 characters. This field is null when the
Custom Email Content setting is selected in the UI but no message content is entered. This
field is available in API version 54.0 and later.

Custom messages aren’t translatable.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description entered for this policy.


Standard Objects TransactionSecurityPolicy

**Field** **Details**

```
DeveloperName

EventName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API, or program name, for this policy.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Real-Time Event Monitoring only. Indicates the name of the event the policy monitors.
Valid values are:

**•** `ApiEvent` —Tracks these user-initiated read-only API calls: `query()`,
`queryMore()`, and `count()` . Captures API requests through SOAP API and Bulk
API for the Enterprise and Partner WSDLs. Tooling API calls and API calls originating from
a Salesforce mobile app aren’t captured.

**•** `ApiAnomalyEventStore` —Tracks anomalies in how users make API calls.
ApiAnomalyEventStore is an object that stores the event data of `ApiAnomalyEvent` .
This object is available in API version 50.0 and later.

**•** `BulkApiResultEventStore` —Tracks when a user downloads the results of a
Bulk API request. `BulkApiResultEventStore` is a big object that stores the
event data of `BulkApiResultEvent` . This object is available in API version 50.0
and later.

**•** `CredentialStuffingEventStore` —Tracks when a user successfully logs into
Salesforce during an identified credential stuffing attack. Credential stuffing refers to
large-scale automated login requests using stolen user credentials.This value is available
in API 49.0 and later.

**•** `FileEventStore` —Tracks when a user downloads, previews, or uploads a file.
FileEventStore is a big object that stores the event data of FileEvent. This object is available
in API version 57.0 and later.

**•** `GuestUserAnomalyEventStore` —Tracks data access anomalies that are caused
by guest user permission misconfiguration. GuestUserAnomalyEventStore is an object
that stores the event data of GuestUserAnomalyEvent. This object is available in API
version 60.0 and later.

**•** `ListViewEvent` —Tracks when users access data with list views using Lightning
Experience, Salesforce Classic, or the API. It doesn’t track list views of Setup entities.

**•** `LoginAnomalyEventStore` —Stores the records of data access anomalies that
are caused by potentially malicious login actions.This object is available in API version
64.0 and later.


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**•** `LoginAsEvent` —Tracks the login activity of admins who log in to Salesforce as other
users.This object is available in API version 46.0 and later.

**•** `LoginEvent` —LoginEvent tracks the login activity of users who log in to Salesforce.

**•** `PermissionSetEventStore` —Tracks changes to permission sets and permission
set groups.

**•** `ReportAnomalyEventStore` —Tracks anomalies in how users run or export
reports, including unsaved reports. This value is available in API 49.0 and later.

**•** `ReportEvent` —Tracks when reports are run in your org.

**•** `SessionHijackingEventStore` —Tracks when unauthorized users gain
ownership of a Salesforce user’s session with a stolen session identifier. To detect such
an event, Salesforce evaluates how significantly a user’s current browser fingerprint
diverges from the previously known fingerprint using a probabilistically inferred
significance of change. This value is available in API 49.0 and later.

```
EventType

ExecutionUserId

MasterLabel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Legacy Transaction Security only. Indicates the type of event the policy monitors.
Valid values are:

**•** `AccessResource` —Notifies you when the selected resource has been accessed.

**•** `AuditTrail` —Reserved for future use.

**•** `DataExport` —Notifies you when any API query is made, such as from the Data Loader
API client, or when a Report export occurs.

**•** `Entity` —Notifies you on use of an object type such as an authentication provider or
chatter post.

**•** `Login` —Notifies you when a user logs in.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. The ID of an active user who is assigned the Modify
All Data and View Setup user permissions. As of Summer '20, Legacy Transaction Security is
a retired feature in all Salesforce orgs.

**Type**
string


Standard Objects TransactionSecurityPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The policy’s name.

Important: Where possible, we changed noninclusive terms to align with our
company value of Equality. We maintained certain terms to avoid any effect on
customer implementations.

```
NamespacePrefix

ResourceName

State

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. A resource used to narrow down the conditions
under which the policy triggers. For example, with a `DataExport` event, you can select
a resource Lead to specifically monitor export activity occurring on your Lead entities. The
resources available depend on the `EventType` field.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Description**
Indicates whether the policy is active. Valid values are:

**•** `Disabled`

**•** `Enabled`

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of validation that the policy uses. The valid values are:

**•** `CustomApexPolicy`  - Created with Apex editor.

**•** `CustomConditionBuilderPolicy`  - Created with Condition Builder

.

### TransactionSecurityEventLog

Transaction Security event logs contain details about policy execution. Legacy transaction security policy details are supported in API
version 38.0 and later. Enhanced transaction security policy details are supported in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApexIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.


Standard Objects TransactionSecurityEventLog

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ClientIp

CpuTime

EvaluationTime

EventName

FlowIdentifier

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the event, which is `Transaction Security Event` .

**Type**
String


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

```
LoginKey

PlannerIdentifier

PolicyIdentifier

PolicyOutcome

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated. For example: `00530000009M943` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

Possible values are:

**•** `Error` —The policy caused an undefined error when it executed.

**•** `ExemptNoAction` —The user is exempt from transaction security policies, so the
policy didn’t trigger.

**•** `MeteringBlock` —The policy took longer than 3 seconds to process, so the user was
blocked from performing the operation.

**•** `MeteringNoAction` —The policy took longer than 3 seconds to process, but the
user isn't blocked from performing the operation.

**•** `NoAction` —The policy didn't trigger.


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**•** `Notified` —A notification was sent to the recipient.

```
PolicyType

RequestIdentifier

Result

RunTime

SendEmailNotification

SendInAppNotification

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique id for a given request. For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The outcome of evaluating the policy. For example: `NOT TRIGGERED` .

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
Boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to send an email notification. The default value is `false` .

**Type**
Boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects TransactionSecurityEventLog

**Field** **Details**

**Description**
Indicates whether to send an in-app notification. The default value is `false` .

```
SessionKey

Timestamp

TriggeredTimestamp

Uri

UserIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
DateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time at which the Transaction Security event was generated in ISO8601-compatible
format. For example: 2015-07-27T11:32:59.555Z.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who is using Salesforce services through the UI or the API.
For example: `00530000009M943` .


### Standard Objects Translation Translation

The Translation object represents the languages enabled for translation in your Salesforce org. This object is available in API version 47.0
and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** To view this object, you must have the “View Setup and Configuration” permission.

**•** To use the `create()`, `update()`, and `upsert()` calls, Translation Workbench must be enabled in your org.

**•** To manage translations, Translation Workbench must be enabled in your org. Specify translators for each language through the
### Translation Language Settings Setup page.

Fields

**Field** **Details**

```
CanManage

IsActive

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the language is available for translation ( `true` ) or not ( `false` ).

Specify translators for each language through the Translation Language Setup page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the translated values for this language display to users ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code. See the Salesforce Help for a full list of languages and their codes.


### Standard Objects TravelMode TravelMode

Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such as
Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is available
in API version 54.0 and later.

Fields

**Field** **Details**

```
CanUseTollRoads

IsLocked

IsTransportingHazmat

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is allowed to drive on toll roads.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is transporting hazardous materials.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects TravelMode

**Field** **Details**

```
LastViewedDate

MayEdit

Name

OwnerId

TransportType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` =)
but not viewed it.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the travel mode.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


### Standard Objects TwoFactorInfo

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of transportation.

Possible values are:

**•** `Bicycle`

**•** `Car` -Default.

**•** `Heavy Truck`

**•** `Light Truck`

**•** `Walking`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TravelModeFeed**

Feed tracking is available for the object.

**TravelModeOwnerSharingRule**

Sharing rules are available for the object.

**TravelModeShare**

Sharing is available for the object.

### TwoFactorInfo

Stores a user’s secret for multi-factor operations. Use this object when customizing multi-factor authentication in your organization.
(Note that multi-factor authentication was formerly called two-factor authentication.) This object is available in API version 32.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You need the Manage Multi-Factor Authentication in API permission to create or update this object.


### Standard Objects TwoFactorMethodsInfo

Fields

**Field Name** **Details**

```
SharedKey

Type

UserId

### TwoFactorMethodsInfo

```

**Type**
string

**Properties**
Create, Group, Sort, Update

**Description**

This field is never read-enabled, though it is write-enabled. A request for this
value always returns `null` . The value must be a base32-encoded string of a
20-byte secret.

You can use the Apex method
`Auth.SessionManagement.getQrCode()` to get a value to write to
this field.

Note: If you write a secret to this field, in API version 37.0 and later the
user gets an email notification that a new identity verification method
was added to the user’s account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The multi-factor method.

**•** `TOTP` —The time-based one-time password.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the user who’s associated with the authentication secret.

Stores information about which identity verification methods a user has registered. This object is available in API version 37.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects TwoFactorMethodsInfo

Special Access Rules

You need the Manage MFA in API user permission to access this object. Note that multi-factor authentication (MFA) was formerly called
two-factor authentication.

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
description.

```
   A callout was unsuccessful because of pending uncommitted work related to a process, flow,

    or Apex operation.

   Commit or roll back the work, and then try again.

```

To avoid this error, execute DML operations and queries in separate, asynchronous calls.

Fields

**Field Name** **Details**

```
ExternalId

HasBuiltInAuthenticator

HasSalesforceAuthenticator

HasSecurityKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique system-generated numerical identifier for the user.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a built-in authenticator on their device, such as
Touch ID or Windows Hello. The user can verify their identity by using the built-in
authenticator.

This field is available in API version 53.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has connected the Salesforce Authenticator mobile app. The
user can verify identity by approving a notification sent to the app. If the user
sets a trusted location in the app, Salesforce Authenticator verifies automatically
when the user is in the trusted location.

**Type**
boolean


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a WebAuthn-compatible security key. This field
includes all security keys registered or used after Summer ’22. The user can verify
their identity by inserting the security key into a USB port to generate credentials.

```
HasTempCode

HasTotp

HasU2F

HasUserVerifiedEmailAddress

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has a temporary verification code generated by a Salesforce
admin or user with Manage Multi-Factor Authentication in User Interface
permission.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has connected an authenticator app that generates verification
codes, also known as time-based one-time passwords (TOTP). The user can verify
identity by entering a code generated by the app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has registered a U2F security key. The user can verify identity
by inserting the security key into a USB port to generate credentials.

Note: For U2F security keys registered or used after Summer ’22, use
HasSecurityKey instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user's email address is verified.

This parameter is available in API version 43.0 and later.


Standard Objects TwoFactorMethodsInfo

**Field Name** **Details**

```
HasUserVerifiedMobileNumber

HasVerifiedMobileNumber

UserId

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has self-registered and verified a mobile phone number.
Salesforce can text a verification code to the user at that number.

This parameter is available in API version 43.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has a mobile phone number that was added by an administrator
or self-registered by the user. Salesforce can text a verification code to the user
at that number.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who’s associated with the identity verification methods.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `[query()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_query.htm)` call returns up to 500 rows.
A `[queryMore()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_querymore.htm)` call returns 500 more, up to 2,500 total. No more records are returned after 2,500.

To make sure that you don’t miss any records, issue a `COUNT()` query in a SELECT clause for TwoFactorMethodInfo. This query gives
you the total number of records. If there are more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
  SELECT <desired fields> FROM TwoFactorMethodsInfo LIMIT 2000 OFFSET 0

```


### Standard Objects TwoFactorTempCode

Then, run another query with an offset of 2,000.

```
     SELECT <desired fields> FROM TwoFactorMethodsInfo LIMIT 2000 OFFSET 2000

```

Continue to increase the offset by 2,000 until you have results for all records.

### TwoFactorTempCode

Stores information about a user’s temporary verification code for confirming their identity when logging in. This object is available in
API version 37.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You need the Manage Multi-Factor Authentication in API permission to access this object. (Note that multi-factor authentication was
formerly called two-factor authentication.)

Fields

**Field Name** **Details**

```
Expiration

Identifier

TempCode

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when the temporary verification code expires. The code expires
in 1 to 24 hours after it’s generated. Salesforce admins and non-admin users with
the Manage Multi-Factor Authentication in User Interface permission set the
expiration time when generating the code.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique identifier for the temporary code. This is a required field that can take
any value.

**Type**
encryptedstring


### Standard Objects UiAgentInteractionEventLog

**Field Name** **Details**

**Description**
A request for this value always returns `null` .

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the user who’s associated with the temporary verification code.

### UiAgentInteractionEventLog

This log tracks client side interactions and events with the Agentforce panel. It is limited to Salesforce Lightning Experience, Salesforce
Mobile, and Conversation Preview within Agentforce Builder. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AgentType

AppName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app this logline has executed.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

BrowserName

BrowserVersion

ButtonLabel

Channel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returned with every session (from bots runtime API). The session begins with co-pilot panel
is opened and ends when the user logs out of Salesforce, closes the browser tab or exits the
browser. For mobile, this id is present throughout the entire time the app is open, and only
changes upon cold start or logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Browser major.minor version. Some browseers may not provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the user interacts with a message by clicking a message-level button, this is the label
of the button the user selects.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the channel. For example, mobile, LEX, or Playground.

```
ClientGeolocation

ClientIdentifier

ClientIp

Components

ConnectionType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Client geographic location in format Country/State.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API client ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Client IP address.

**Type**
textarea

**Properties**
Nillable

**Description**
An array of strings that contain the names of the components, including the namespace and
the name of the component. This should include both input and output components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection. For example, WiFi.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
DeviceModel

DevicePlatform

DeviceSessionIdentifier

FeedbackIdentifier

HasToxicityWarning

IsAgentPanelExited

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The device model.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The application experience

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Auto-generated ID on the client-side that stays the same for the duration of the browser tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The turn ID from Agents V1 API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Flag to identify whether the message contains a toxicity warning.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Description**
A boolean field that is true if the user clicks on a button to navigate away from an agent
panel.

The default value is `false` .

```
LightningType

LightningTypeMessage

LoginKey

MessageIdentifier

MobileSdkAppType

MobileSdkVersion

```

**Type**
textarea

**Properties**
Nillable

**Description**
An array of strings that contains the name of the ES type(s).

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
This is the ES type message associated with the co-pilot response (i.e. “Inform” or “Inquire”)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the login id to allow tracking of all events from user login to logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returned with every message (from bots runtime API).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK version.

```
ObjectType

OperatingSystemName

OperatingSystemVersion

PageContext

PageObjectIdentifier

PageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object for ES Type recordInfo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the operating system.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the component hosting the main content of the page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object id, if any, of the record being displayed.

**Type**
string


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object type of the page being displayed.

```
PageUrl

RequestIdentifier

SdkAppVersion

SessionKey

TaskName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Raw url of the page log occurred on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK app version this logline has executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the session id to allow tracking of all events in a session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This will describe the nature of the event being logged.


Standard Objects UiAgentInteractionEventLog

**Field** **Details**

```
Timestamp

UiEventElapsedTime

UiEventTimestamp

UiRootActivityIdentifier

UserIdentifier

UserType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The elapsed time for the UI event.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time when the message was logged according to the client.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the root activity, if any, when this message was logged.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID of the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of user.


### Standard Objects UiFormulaCriterion

**Field** **Details**

```
VoiceOrText

### UiFormulaCriterion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Whether the input by the user was “voice” or “text”.

Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
LeftHandSide

OperatorId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the field that the filter is based on. For example, `AMOUNT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter operator. Valid values are:

**•** `CONTAINS`

**•** `EQUAL`

**•** `GE` —greater than or equal

**•** `GT` —greater than

**•** `LE` —less than or equal

**•** `LT` —less than

**•** `NE` —not equal


### Standard Objects UiFormulaRule

**Field** **Details**

This is a relationship field.

**Relationship Name**
Operator

**Relationship Type**
Lookup

**Refers To**
null

```
ParentKeyPrefix

RightHandSide

RuleId

### UiFormulaRule

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix of the parent ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the value used to evaluate the component’s visibility. For example, 1000000.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the formula rule ID.

This is a relationship field.

**Relationship Name**
Rule

**Relationship Type**
Lookup

**Refers To**
### UiFormulaRule

Represents a set of one or more filters that define the conditions under which a component displays on a Lightning page. This object is
available in API version 47.0 and later.


Standard Objects UiFormulaRule

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AssociatedElementId

BooleanFilter

DeveloperName

Formula

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a parent component that UiFormulaRule is associated with, such as PromptVersion.

This is a relationship field.

**Relationship Name**
AssociatedElement

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter logic applied to UiFormulaRule. References the UI formula rule stored
by UiFormulaCriterion based on the sortIndex, such as ((1 && 3) || 2).

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the API name of the UiFormulaRule.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
textarea

**Properties**
Nillable


### Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
Represents the formula source string of UiFormulaRule.

```
Language

MasterLabel

ParentKeyPrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the language of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. Represents the label of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix for AssociatedElementId.

### UiTelemetryNavTmEventLog

UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from the
[UI Telemetry Resource Timing Event on page 2413 and includes requests initiated with either the Fetch API or the XMLHttpRequest API.](https://fetch.spec.whatwg.org/)
This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects UiTelemetryNavTmEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as `Salesforce.com IP` .

```
ConnectEnd

ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
string


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

```
DevicePlatform

DeviceSessionIdentifier

DomComplete

DomContentLoadedEventEnd

DomContentLoadedEventStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the page’s `readyState` property is set to `complete` .
Indicates that the page and its subresources have finished loading.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler completes.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

**Type**
double


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler starts.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

```
DomInteractive

DomainLookupEnd

DomainLookupStart

Duration

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the page’s `readyState` is set to `interactive` . Indicates
that the page has finished loading, but subresources, such as images and scripts, are still
loading.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`LOAD_EVENT_END` time.

```
EncodedBodySize

FetchStart

FirstInterimResponseStart

InitiatorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTML element that initiates the resource load.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
LoadEventEnd

LoadEventStart

LoginKey

MobileSdkAppType

MobileSdkVersion

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `load` event handler completes.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `load` event handler begins.

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile SDK version number.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
NavigationType

NextHopProtocol

OperatingSystemName

OperatingSystemVersion

PageContext

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of navigation timing data.

**Possible Values**

**•** `navigate` : a user interaction or a script initiated navigation.

**•** `reload` : a reload initiated navigation.

**•** back_forward: navigation traverses the browser’s history.

**•** `prerender` : a prerender hint initiated navigation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Application-Layer Protocol Negotiation (ALPN) Protocol ID that fetches the resource.

**Possible Values**
`http/0.9`, `http/1.0`, `h2`, `h2c`, `h3`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `USER_AGENT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
PageObjectIdentifier

PageObjectType

PageUrl

RedirectCount

RedirectEnd

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the top-level Lightning Experience page that the user opened. The page
can contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of redirects since the last non-redirect navigation in the current browsing
context.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
RedirectStart

RenderBlockingStatus

RequestIdentifier

RequestStart

ResponseEnd

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

```
ResponseStart

ResponseStatus

SdkAppVersion

SecureConnectionStart

ServerRequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The HTTP response status code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The request ID for the server request that’s used to find associated server logs.


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

```
SessionKey

StartTime

Timestamp

TransferSize

UiEventElapsedTime

UiEventTimestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the resource, including the response header and the response payload
body.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryNavTmEventLog

**Field** **Details**

**Description**
The time at which this event occurs, measured in milliseconds.

```
UiRootActivityIdentifier

UiThreadResponseDelay

UnloadEventEnd

UnloadEventStart

Url

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the root activity when the event occurs.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `unload` event handler completes.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the page’s `unload` event handler starts.

To calculate the processing time for the `unload` event handler, subtract the
`UNLOAD_EVENT_START` time from the `UNLOAD_EVENT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The URL of the request.

```
UserIdentifier

UserType

WorkerStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
If a service worker is installed, the time in milliseconds when the active service worker receives
the `fetch` event.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

### UiTelemetryRsrcTmEventLog

UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 64.0 and later.](https://fetch.spec.whatwg.org/)

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects UiTelemetryRsrcTmEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP.”

```
ConnectEnd

ConnectStart

ConnectionType

DecodedBodySize

DeviceModel

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser establishes a connection to a server so that it
can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds after the browser completes the Domain Name System (DNS) lookup
and begins connecting to a server so that it can retrieve a resource.

To calculate the Transport Control Protocol (TCP) handshake time, subtract the
`CONNECT_START` time from the `CONNECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

```
DevicePlatform

DeviceSessionIdentifier

DomainLookupEnd

DomainLookupStart

Duration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
double


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`RESPONSE_END` time.

```
EncodedBodySize

FetchStart

FirstInterimResponseStart

InitiatorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size in octets of the HTTP message body before the removal of any applied content
encoding.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource from the server, not
including redirects. Occurs before the DNS lookup and the connection to the server is
established.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the interim 1xx response
from the server.

To calculate the time from when the browser sends a request to when it starts to receive an
interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The HTML element that initiates the resource load.

```
LoginKey

MobileSdkAppType

MobileSdkVersion

NextHopProtocol

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile SDK version number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ALPN Protocol ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the operating system.

**Type**
string


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version number.

```
PageContext

PageObjectIdentifier

PageObjectType

PageUrl

RedirectEnd

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience page that the user opened. The page can
contain one or more Lightning components. Multiple record IDs can be associated with
`PAGE_URL` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**

The time in milliseconds when the browser receives the last byte of the response of the final
redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

```
RedirectStart

RenderBlockingStatus

RequestIdentifier

RequestStart

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to fetch a resource that initiates a redirect.

To calculate the total redirection time, subtract the `REDIRECT_START` time from the
`REDIRECT_END` time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status that indicates whether the resource can block or delay the browser from rendering
page content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
ResponseEnd

ResponseStart

ResponseStatus

SdkAppVersion

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the resource’s last byte or when the
transport connection closes, whichever comes first.

To calculate the total time used to fetch a resource without redirects, subtract the
`FETCH_START` time from the `RESPONSE_END` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser receives the first byte of the response from the
server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The HTTP response status code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

```
SecureConnectionStart

ServerRequestIdentifier

SessionKey

StartTime

Timestamp

TransferSize

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The time in milliseconds when the browser begins the handshake process that secures the
connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The requestId for the server request that’s used to find associated server logs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session starts.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the browser starts to fetch the resource, including redirects.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects UiTelemetryRsrcTmEventLog

**Field** **Details**

**Description**
The size in octets of the resource, including the response header and the response payload
body.

```
UiEventElapsedTime

UiEventTimestamp

UiRootActivityIdentifier

UiThreadResponseDelay

Url

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the message was logged and when the browser
tab started meaning

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The difference in milliseconds between when the event is logged and when the browser
tab is opened.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the root activity when the event occurs.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds from when the browser receives the response to when it executes
the callback. This delay occurs if the main Javascript thread is busy when the response is
received.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the request.


### Standard Objects UndecidedEventRelation

**Field** **Details**

```
UserIdentifier

UserType

WorkerStart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when the active service worker receives the `fetch` event, if a
service worker is installed.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

### UndecidedEventRelation

Represents event participants (invitees or attendees) with the status `Not Responded` for a given event. This object is available in
API versions 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

```

**Type**
reference


Standard Objects UndecidedEventRelation

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

```
RelationId

RespondedDate

Response

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
This field is always `null` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment` .


### Standard Objects UnifiedActivity

**Field Name** **Details**

```
Type

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.

**Query invitees who have not responded to an invitation to an event**

```
  SELECT eventId, type, response FROM UndecidedEventRelation WHERE

  eventid='00UTD000000ZH5LA'

```

SEE ALSO:

AcceptedEventRelation

DeclinedEventRelation

### UnifiedActivity

Represents an activity that is automatically captured from Einstein Activity Capture (EAC) or other activity data, such as calls, manually
logged tasks, and emails. This object consists of fields common to all types of activity-related objects such as Event, Task, EmailMessage,
VoiceCall, VideoCall, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime


Standard Objects UnifiedActivity

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible values are:

**•** `UnifiedActivity`

**•** `UnifiedEmail`

**•** `UnifiedMeeting`

**•** `UnifiedTask`

**•** `UnifiedVideoCall`

**•** `UnifiedVoiceCall`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a polymorphic relationship field.


### Standard Objects UnifiedActivityInsight

**Field** **Details**

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage, Event, Task, VideoCall, VoiceCall

```
InternalEventKey

IsInsightAvailable

Snippet

Subject

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the task or event.

### UnifiedActivityInsight

Represents an insight related to a unified activity. This object is available for reports and dashboards in the Winter ’24 release and later.


Standard Objects UnifiedActivityInsight

Supported Calls

`describeSObjects()`, `query()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

AggregatedKeywordOccurrences

InsightType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the unified activity that this insight is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of keyword occurrences that triggered this insight. This field is the sum of
occurrences for all the attached UnifiedActivityInsightKeyword objects.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Type of the insight.


### Standard Objects UnifiedActivityParticipant

**Field** **Details**

```
OwnerId

Scope

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. ID of the owner of the insight. Only user-scoped insights have owners
( `Scope` = `USER` ).

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The scope of the insight.

Possible values are:

**•** `ORG`

**•** `USER`

### UnifiedActivityParticipant

Represents a participant in an activity. For example, a participant in a voice call is someone who initiated the call or someone who
received the call.This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.


Standard Objects UnifiedActivityParticipant

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity that the person participated in.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The channel-specific address used to identify the participant in an external communication.
For example, an email address in an email or a phone number in a voice call. The value is
captured at the time of the communication; it doesn’t change if the contact’s email address
or phone number is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The role of the participant in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`


### Standard Objects UnifiedActivityRelation

**Field** **Details**

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

```
PersonId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person who participated in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

### UnifiedActivityRelation

Represents a relationship between an activity and a related record that’s a target or topic of the activity. For example, a related record
can be an opportunity, account, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)


### Standard Objects UnifiedActvtyInsightKeyword

Fields

**Field** **Details**

```
ActivityId

RelatedId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity. This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedVideoCall, UnifiedVoiceCall

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the related record. This field is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Contract, Lead, Opportunity, User

### UnifiedActvtyInsightKeyword

Represents a keyword in a communication that triggered the activity insight. This object is available for reports and dashboards in the
Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.


### Standard Objects UnifiedEmail

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
InsightId

Keyword

Occurrences

### UnifiedEmail

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity insight associated with the keyword.

This field is a relationship field.

**Relationship Name**
Insight

**Relationship Type**
Lookup

**Refers To**
UnifiedActivityInsight

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Keyword mentioned in the communication.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Number of times the keyword was mentioned in the communication.

Represents an email that was captured or synced from an EmailMessage or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.


Standard Objects UnifiedEmail

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

ActivitySubType

ActivityType

DetailId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the email in the Coordinated Universal Time (UTC) time zone.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedEmail` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UnifiedEmail

**Field** **Details**

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object. If the email was captured from Einstein Activity Capture,
this field returns a blank value.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
Direction

InternalEventKey

IsInsightAvailable

IsPrivate

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The direction in which the email was sent or received.

Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean


### Standard Objects UnifiedEmailParticipant

**Field** **Details**

**Properties**
Defaulted on create Filter

**Description**
Indicates whether the activity's sensitive fields ( `Subject` and `Snippet` ) are masked
( `true` ) or visible ( `false` ) for non-owners.

The default value is `false` .

```
Snippet

Subject

```

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the email content. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the email.

### UnifiedEmailParticipant

Represents a participant in an email. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedEmailParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedEmail

**Type**
string

**Properties**
Filter, Nillable

**Description**
Email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Participant’s role in the email.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedMeeting

**Field** **Details**

```
PersonId

### UnifiedMeeting

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the email.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a meeting that was captured or synced from an Event record. This object is available for reports and dashboards in the Winter
’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects UnifiedMeeting

**Field** **Details**

**Description**
The date and time of the meeting in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

InternalEventKey

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedMeeting` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.


### Standard Objects UnifiedMeetingParticipant

**Field** **Details**

```
IsInsightAvailable

Snippet

Subject

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the event description. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the meeting.

### UnifiedMeetingParticipant

Represents a participant in a meeting. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedMeetingParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the meeting that the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedMeeting

**Type**
string

**Properties**
Filter, Nillable

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the meeting.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedTask

**Field** **Details**

```
PersonId

### UnifiedTask

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact, lead, or user participating in the meeting.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a business activity such as a to-do item. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects UnifiedTask

**Field** **Details**

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

```
ActivitySubType

ActivityType

DetailId

InternalEventKey

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedTask` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
Task

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.


### Standard Objects UnifiedTaskParticipant

**Field** **Details**

```
IsInsightAvailable

Snippet

Subject

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the task body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
The subject line of the task.

### UnifiedTaskParticipant

Represents a participant in a task. This object is available for reports and dashboards in the Winter ’24 release and later.

Important: Starting in Summer ’25, this object isn’t available unless Activity 360 Reporting was enabled in your org in Spring ’25
[or earlier. See Knowledge Article: Einstein Activity Capture Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


Standard Objects UnifiedTaskParticipant

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedTask

**Type**
string

**Properties**
Filter, Nillable

**Description**
Username of the participant. The username is captured at the time of the communication;
it doesn’t change if the contact’s username is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`


### Standard Objects UnifiedVideoCall

**Field** **Details**

```
PersonId

### UnifiedVideoCall

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact, lead, or user participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Represents a video call that is captured or synced from the VideoCall or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.


Standard Objects UnifiedVideoCall

**Field** **Details**

```
ActivitySubType

ActivityType

CallDurationInSeconds

DetailId

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVideoCall` .

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the video call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup


### Standard Objects UnifiedVideoCallParticipant

**Field** **Details**

**Refers To**
VideoCall

```
InternalEventKey

IsInsightAvailable

Snippet

Subject

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it.

The default value is `false` .

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the video call.

### UnifiedVideoCallParticipant

Represents a participant in a video call. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects UnifiedVideoCallParticipant

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

ChannelAddress

ListenRatio

ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the video call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedVideoCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the video call.

**Type**
picklist


### Standard Objects UnifiedVoiceCall

**Field** **Details**

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

```
PersonId

TalkRatio

### UnifiedVoiceCall

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was talking versus listening in the video call.

Represents a voice call that is captured or synced from a VoiceCall or Task record. This object is available for reports and dashboards in
the Winter ’24 release and later.


Standard Objects UnifiedVoiceCall

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityDateTime

ActivitySubType

ActivityType

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVoiceCall` .


Standard Objects UnifiedVoiceCall

**Field** **Details**

```
CallDurationInSeconds

DetailId

InternalEventKey

IsInsightAvailable

Snippet

```

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the voice call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
VoiceCall

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string


### Standard Objects UnifiedVoiceCallParticipant

**Field** **Details**

**Properties**
Nillable

**Description**
An abbreviation of the voice call content. This field has a maximum length of 255 characters.

```
Subject

```

**Type**
string

**Properties**
None

**Description**
Contains the subject of the voice call.

### UnifiedVoiceCallParticipant

Represents a participant in a voice call. This object is available for reports and dashboards in the Winter ’24 release and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

Special Access Rules

We’re retiring Einstein Activity Capture Activity 360 Reporting. Starting in Summer ’25, this object isn’t available with Einstein Activity
[Capture unless Activity 360 Reporting was enabled in your org in Spring ’25 or earlier. See Knowledge Article: Einstein Activity Capture](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)
[Activity 360 Reporting, Activity Metrics, Activities Dashboard Upcoming Retirement](https://help.salesforce.com/s/articleView?id=004633781&type=1&language=en_US)

Fields

**Field** **Details**

```
ActivityId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the voice call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity


Standard Objects UnifiedVoiceCallParticipant

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
UnifiedVoiceCall

```
ChannelAddress

ListenRatio

ParticipantType

PersonId

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The phone number of the participant. The phone number is captured at the time of the
communication; it doesn’t change if the contact’s phone number is updated later.

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the voice call.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`

**•** `To`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects UnitOfMeasure

**Field** **Details**

**Description**
ID of the person participating in the voice call.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

```
TalkRatio

### UnitOfMeasure

```

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was talking versus listening in the voice call.

Defines the units and systems of units used to express and account for quantities. This object is available in API version 61.0 and later.

Examples of units of measure include Litre (for volume), Kilogram (for weight), and single units (such as Can, sachet, and packet).

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConversionFactor

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The factor or rate that's used to convert this unit of measurement to the base unit. For
example, for the Weight unit of measure class, the default unit of measure is pounds (lbs).
Then, all units of measure records with the Weight unit of measure class are converted to


Standard Objects UnitOfMeasure

**Field** **Details**

equate 1 unit to 1 pound. If the unit of measure is kilogram, the conversion factor is 2.2 as 1
pound consists of 2.2 kilograms.

```
Description

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of this unit of measure.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the unit of measure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.


Standard Objects UnitOfMeasure

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
Group, User

```
Type

Sequence

Status

UnitCode

UnitOfMeasureClassId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The type of the unit of measure. For example, weight, distance, period.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequence number assigned to the unit of measure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the unit of measure.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Code for the unit of measure.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects UriEventLog

**Field** **Details**

**Description**
The class associated with the unit of measurement.

This field is a relationship field.

**Relationship Name**
UnitOfMeasureClass

**Refers To**
UnitOfMeasureClass

### UriEventLog

URI events contain details about user interaction with the web browser UI. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.


Standard Objects UriEventLog

**Field** **Details**

```
DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

LoginKey

ReferrerUri

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how much activity is occurring in the database.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The referring URI of the page that’s receiving the request.


Standard Objects UriEventLog

**Field** **Details**

```
RequestIdentifier

RequestStatus

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .


Standard Objects UriEventLog

**Field** **Details**

```
Timestamp

Uri

UserIdentifier

UserType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a


### Standard Objects UsageImpactFactor

**Field** **Details**

customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### UsageImpactFactor

Represents a collection of fields to set up the Usage Impact Factors used across jurisdictions and programs.This object is available in API
version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
IsActive

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Factor is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Factor.


Standard Objects UsageImpactFactor

**Field** **Details**

```
ShortForm

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Factor.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Factor

Possible values are:

**•** `AdjustedGrossAnnual` —Adjusted Gross Annual

**•** `AdjustedGrossAnnualMMBTU` —Adjusted Gross Annual MMBTU

**•** `AdjustedGrossAnnualkW` —Adjusted Gross Annual kW

**•** `AdjustedGrossAnnualkWSummer` —Adjusted Gross Annual kW Summer

**•** `AdjustedGrossAnnualkWWinter` —Adjusted Gross Annual kW Winter

**•** `AdjustedGrossAnnualkWh` —Adjusted Gross Annual kWh

**•** `GrossAnnualMMBTU` —Gross Annual MMBTU

**•** `GrossAnnualkW` —Gross Annual kW

**•** `GrossAnnualkWh` —Gross Annual kWh

**•** `NetAnnual` —Net Annual

**•** `NetLifetime` —Net Lifetime

**•** `NetToGross` —Net To Gross

**•** `NetToGrossFR` —Net To Gross FR

**•** `UsefulLife` —Useful Life

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.


### Standard Objects UsageImpactGroup

**[UsageImpactFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactFactorShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroup

Represents a collection of fields to set up the Usage Impact Groups used across jurisdictions and programs. This object is available in
API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
Description

IsActive

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects UsageImpactGroupFactor

**Field** **Details**

**Description**
The name of the Usage Impact Group.

```
ShortForm

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Group.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Group.

Possible values are:

**•** `ForwardMarkets` —Forward Markets

**•** `Planning`

**•** `Production`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupFactor

Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0 and
later.


Standard Objects UsageImpactGroupFactor

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
FactorValue

IsActive

Name

UnitOfMeasureId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Defines the value of the Usage Impact Group Factor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group Factor is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Factor.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The UnitOfMeasure object associated with the Usage Impact Group Factor.

This field is a relationship field.


Standard Objects UsageImpactGroupFactor

**Field** **Details**

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

```
UsageImpactFactorId

UsageImpactGroupVersionId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Factor object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactFactor

**Relationship Type**
Lookup

**Refers To**
UsageImpactFactor

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroupVersion

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects UsageImpactGroupPgmMeasure

**[UsageImpactGroupFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupFactorShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupPgmMeasure

Represents a junction between the program, product, and Usage Impact Group version. This object is available in API version 58.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
Description

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Program Measure.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Program Measure.


Standard Objects UsageImpactGroupPgmMeasure

**Field** **Details**

```
Product2Id

ProgramId

UsageImpactGroupVersionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Usage Impact Group Program Measure.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Program object associated with the Usage Impact Group Program Measure.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup

**Refers To**
Program

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version associated with the Energy Saving Group Association.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup


### Standard Objects UsageImpactGroupVersion

**Field** **Details**

**Refers To**
### UsageImpactGroupVersion

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupPgmMeasureChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupPgmMeasureFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupPgmMeasureHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupPgmMeasureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupPgmMeasureShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### UsageImpactGroupVersion

Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

Fields

**Field** **Details**

```
ApprovedMeasureExtlid

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The approved Measure Category ID assigned by a regulator.


Standard Objects UsageImpactGroupVersion

**Field** **Details**

```
Description

EndDate

IsActive

Name

StartDate

TechResourceManualCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Version.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group Version is active.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Version.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UsageImpactGroupVersion

**Field** **Details**

**Description**
The code and version of the Technical Reference Manual which is the source for the values
associated with this Usage Impact Group Version. This is necessary for regulatory reporting.

```
UsageImpactGroupId

Version

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group object associated with the Usage Impact Group Version.

This field is a relationship field.

**Relationship Name**
UsageImpactGroup

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroup

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the Usage Impact Group Version.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupVersionShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects User User

Represents a user in your organization.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

**•** To create or update a User record, you must have the Manage Internal Users permission. If the user is a Customer Portal user, you
must have the Manage Customer Users permission. If the user is a partner portal user, you must have the Manage External Users
permission. But the `describeSObjects` call always returns `createable` as `true` .

**•** If digital experiences is enabled, to create or update external users for Customer Portal, partner portal, or Experience Cloud sites, you
must also have the Manage External Users permission.

**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

But internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** When requested by portal users, queries that look up to the User object, such as `owner.name` or `owner.email` sometimes
don’t return values when the portal user making the request doesn’t have Read access to the User record being queried.

The behavior depends on the number of domains associated with the lookup field. If the object can look up to more than one
domain, `owner.name` returns a value, but other detail fields don’t. For example, Case owner can look up to the User or Queue
objects. In this case, portal users can see only the value of `owner.name` . Other User detail fields, such as `owner.email` or
`owner.phone` don’t return a value.

If the object can look up to only a single domain, such as Account owner, then no detail fields return values, including `owner.name` .

**•** To change ownership of a record by updating its `OwnerId` field, you must have both the Transfer Record permission and Read
access to the User record of the new record owner.

**•** To view the `NumberOfFailedLogins` field, you must have the Manage User permission.

Fields

**Field** **Details**

```
AboutMe

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
Information about the user, such as areas of interest or skills. This field is available even if
Chatter is disabled.

```
AccountId

```

`Address` (beta)

```
Alias

BadgeText

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Account associated with a Customer Portal user.

This field is null for Salesforce users.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields for details on
compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user’s alias. For example, `jsmith` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Experience Cloud site role, displayed on the user profile page just below the user name.


Standard Objects User

**Field** **Details**

```
BannerPhotoUrl

CallCenterId

City

CommunityNickname

CompanyName

ContactId

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's banner photo. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If Salesforce CRM Call Center is enabled, represents the call center that this user is assigned
to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city associated with the user. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique name used to identify this user in the Experience Cloud site.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the user’s company.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
ID of the Contact associated with this account. The contact must have a value in the
`AccountId` field or an error occurs.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

```
Country

CountryCode

CurrentStatus

DefaultCurrencyIsoCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country associated with the user. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code associated with the user.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text that describes what the user is working on.

Note: If you update this field, the API automatically adds a post of type
`UserStatus` on the user’s profile in Chatter.

This field is deprecated in API version 25.0. To achieve similar behavior, post to the
user directly by creating a FeedItem with the user’s ParentId.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
The user's default currency setting for new records. For example, if a user in France sets
`DefaultCurrencyIsoCode` to euros, then that’s their default currency.

Only applicable for organizations that use multiple currencies.

```
DefaultDivision

DefaultGroupNotificationFrequency

DelegatedApproverId

Department

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the user's Chatter group email notifications
when the user joins groups. The valid values are:

**•** `P` —Email on every post

**•** `D` —Daily digests

**•** `W` —Weekly digests

**•** `N` —Never

The default value is `N` . For Professional, Enterprise, Unlimited, and Developer Edition
organizations that existed before API version 22.0, the default value remains `D` .

This field is available in API version 21.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable,Sort, Update

**Description**
Id of the user who is a delegated approver for this user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company department associated with the user.


Standard Objects User

**Field** **Details**

```
DigestFrequency

Division

Email

EmailEncodingKey

EmailPreferencesAutoBcc

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The send frequency of the user’s Chatter personal email digest. The valid values
are:

**•** `D` = Daily

**•** `W` = Weekly

**•** `N` = Never

The default value is `D` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The division associated with this user, similar to Department, and unrelated to
`DefaultDivision` .

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The user’s email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The email encoding for the user, such as `ISO-8859-1` or `UTF-8` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the user receives copies of sent emails. This option applies only if
compliance BCC emails aren’t enabled.


Standard Objects User

**Field** **Details**

```
EmployeeNumber

EndDay

Extension

Fax

FederationIdentifier

FirstName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s employee number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally stops working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s phone extension number.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s fax number.

**Type**
string

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Indicates the value that must be listed in the `Subject` element of a Security Assertion
Markup Language (SAML) _IDP certificate_ to authenticate the user for a client application using
single sign-on. This value must be specified if the `SAML User ID Type` is Assertion
contains Federation ID from the User record. Otherwise, this field can’t be edited.

**Type**
string


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s first name.

```
ForecastEnabled

FullPhotoUrl

GeocodeAccuracy

HasUserVerifiedEmail

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user is enabled for forecasts ( `true` ) or not ( `false` ). Forecast user
has access to the forecasts page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo. This field is available even if Chatter is disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's email is verified ( `true` ) or not ( `false` ). The default value is
`false` . This field is available in API version 63.0 and later.


Standard Objects User

**Field** **Details**

```
HasUserVerifiedPhone

IndividualId

IsActive

IsPartner

IsPortalEnabled

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's phone number is verified ( `true` ) or not ( `false` ). The default
value is false. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this user. This field is available if Data Protection
and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user has access to log in ( `true` ) or not ( `false` ). You can modify a
User's active status from the user interface or via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is a partner who has access to the partner portal ( `true` ) or not
( `false` ). This field isn’t available for release 9.0 and later. Instead, use `UserType` with the
value `Partner` or `Power Partner` .

**Type**
boolean


Standard Objects User

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an active, external, user has access to Experience Cloud sites or portals
( `true` ) or not ( `false` ).

This field is only available if one of these conditions is true:

**•** Digital experiences is enabled and you have community or portal user licenses

**•** Portals are enabled

Note: Users with External Identity licenses can access Experience Cloud sites even
if the flag is false.

```
IsPortalSelfRegistered

IsPrmSuperUser

IsProfilePhotoActive

JigsawImportLimitOverride

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is a Customer Portal user who self-registered for your organization's
Customer Portal ( `true` ) or not ( `false` ). This field isn’t available for release 9.0 and earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Available for partner portal users only. Indicates whether the user has super user access in
the partner portal ( `true` ) or not ( `false` ).

This field is available in API version 24.0 and later.

Note: This field isn’t automatically enabled. Contact Salesforce to enable this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has a profile photo ( `true` ) or not ( `false` ). This field is available
in API version 36.0 and later.

**Type**
int


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data.com user’s monthly addition limit. The value must be between zero and the
organization’s monthly addition limit. Label is **Data.com Monthly Addition Limit** . This
field is available in API version 27.0 and later.

```
LanguageLocaleKey

LastLoginDate

LastName

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The user’s language, such as French or Chinese (Traditional). Label is **Language** .

Note: In API version 47.0 and later, when using the DescribeSObjectResult API to
return PicklistEntry values from this picklist, the `active` value indicates whether
the language is in the user’s **Displayed Languages** ( `true` ) or the user’s **Available**
**Languages** ( `false` ). All other languages aren’t in the returned `active` value
array.

In API version 46.0 and earlier, the PicklistEntry `active` values indicate whether the
language is in either the user’s **Displayed Languages** or **Available Languages** lists
( `true` ) or not in either list ( `false` ).

**Type**
dateTime

**Properties**
Filter, Sort, Nillable

**Description**
The date and time when the user last successfully logged in. This value is updated if 60
seconds elapses since the user’s last login.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user’s last name.

**Type**
datetime

**Properties**
Filter, Nillable, Sort


Standard Objects User

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Latitude

LocaleSidKey

Longitude

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) but not viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the geolocation of an address. Acceptable values are
numbers between –90 and 90 up to 15 decimal places. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. The value of the field affects formatting and
parsing of values, especially numeric values, in the user interface. It doesn’t affect the API.

The field values are named according to the language, and the country if necessary, using
two-letter ISO codes. The set of names is based on the ISO standard. You can also manually
set a user’s locale in the user interface, and then use that value for inserting or updating other
users via the API.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the geolocation of an address. Acceptable values are
numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.


Standard Objects User

**Field** **Details**

```
Manager

ManagerId

MediumBannerPhotoUrl

MiddleName

MobilePhone

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
User lookup field used to select the user's manager. This field establishes a hierarchical
relationship, preventing you from selecting a user that directly or indirectly reports to
themselves.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Id of the user who manages this user.

This is a relationship field.

**Relationship Name**
Manager

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the medium-sized user profile banner photo.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s middle name. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
phone


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s mobile device number.

```
Name

NumberOfFailedLogins

OfflineTrialExpirationDate

PasswordExpirationDate

Phone

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` . Limited to 203 characters, including
whitespaces.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of failed login attempts for the user’s account. When the maximum number of
failed login attempts is reached, the counter resets and the user’s account is locked. If there’s
a successful login before the maximum number of failed login attempts is reached, the
counter resets and the user’s account remains unlocked.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user’s Connect Offline trial expires.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user’s password expires. This field is available in API version 63.0
and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects User

**Field** **Details**

**Description**
The user’s phone number.

```
PortalRole

PostalCode

ProfileId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the user in the Customer Portal (either Executive, Manager, User, or PersonAcount).

In API version 15.0 and earlier, if you set this field to null, the system automatically included
a portal role. In API version 16.0 and above, when you set this field to null, a portal role is not
automatically created. When this field is null and a `ContactId` is provided, the user is
assigned to the User role.

The Update property is available in API version 43.0 and later.

The field is available if Customer Portal is enabled OR digital experiences is enabled and
Experience Cloud sites have available partner portal, Customer Portal, or High-Volume Portal
User licenses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s postal or ZIP code. Label is **Zip/Postal Code** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the user’s Profile. Use this value to cache metadata based on profile. In earlier
releases, this was `RoleId` .

If you change the user’s profile, the user’s license also changes, because every profile belongs
to exactly one user license type.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile


Standard Objects User

**Field** **Details**

```
ReceivesAdminInfoEmails

ReceivesInfoEmails

SenderEmail

SenderName

Signature

SmallBannerPhotoUrl

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives email for administrators from Salesforce ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives informational email from Salesforce ( `true` ) or not
( `false` ).

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address used as the From address when the user sends emails. This address is the
same value shown in Setup on the My Email Settings page.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name used as the email sender when the user sends emails. This name is the same value
shown in Setup on the My Email Settings page.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The signature text added to emails. This text is the same value shown in Setup on the My
Email Settings page.

**Type**
url


Standard Objects User

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the small user profile banner photo.

```
SmallPhotoUrl

StartDay

State

StateCode

Street

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo. This field is available even if Chatter is
disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally starts working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state associated with the User. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code associated with the user.

**Type**
textarea


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address associated with the User.

```
SuAccessExpirationDate

Suffix

TimeZoneSidKey

Title

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expiration date for allowing Salesforce Customer Support to log in as this user with Login
As functionality. After this date, the user must grant login access to Salesforce Customer
Support again. This field is available in API version 63.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s name suffix. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. A User time zone affects the offset used when
displaying or entering times in the user interface. But the API doesn’t use a User time zone
when querying or setting values.

Values for this field are named using region and key city, according to ISO standards. You
can also manually set one User time zone in the user interface, and then use that value for
creating or updating other User records via the API.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s business title, such as Vice President.


Standard Objects User

**Field** **Details**

```
Username

UserPermissionsCallCenterAutoLogin

UserPermissionsChatterAnswersUser

UserPermissionsInteractionUser

UserPermissionsJigsawProspectingUser

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Contains the name that a user enters to log in to the API or the user interface. The
value for this field must be in the form of an email address, using all lowercase characters. It
must also be unique across all organizations. If you try to create or update a User with a
duplicate value for this field, the operation is rejected.

Each inserted User also counts as a license. Every organization has a maximum number of
licenses. If you attempt to exceed the maximum number of licenses by inserting User records,
the create request is rejected.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if Salesforce CRM Call Center is enabled. Indicates whether the user is enabled to
use the auto login feature of the call center ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the portal user is enabled to use the Chatter Answers feature ( `true` ) or
not ( `false` ). This field defaults to `false` when a Customer Portal user is created from
the API.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user can run flows or not. Label is **Flow User** .

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
Indicates whether the user is allocated one Data.com user license ( `true` ) or not ( `false` ).
The Data.com user lets the user add Data.com contact and lead records to Salesforce in
supported editions. Label is **Data.com User** .

```
UserPermissionsKnowledgeUser

UserPermissionsLiveAgentUser

UserPermissionsMarketingUser

UserPermissionsOfflineUser

UserPermissionsSFContentUser

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Salesforce Knowledge ( `true` ) or not ( `false` ).
Label is **Knowledge User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Chat ( `true` ) or not ( `false` ). Label is **Live**
**Agent User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to manage campaigns in the user interface
( `true` ) or not ( `false` ). Label is **Marketing User** .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to use Offline Edition ( `true` ) or not ( `false` ).
Label is **Offline User** .

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
Indicates whether the user is allocated one Salesforce CRM Content User License ( `true` ) or
not ( `false` ). Label is **Salesforce CRM Content User** . The Salesforce CRM Content User
license grants the user access to the Salesforce CRM Content application.

```
UserPermissionsSiteforceContributorUser

UserPermissionsSiteforcePublisherUser

UserPermissionsSupportUser

UserPermissionsWirelessUser

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Contributor feature license ( `true` ) or
not ( `false` ). Label is **Site.com Contributor User** . The Site.com Contributor feature license
grants the user access to the Site.com application. Users with a Contributor license can use
Site.com Studio to edit site content only.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Publisher feature license ( `true` ) or not
( `false` ). Label is **Site.com Publisher User** . The Site.com Publisher feature license grants
the user access to the Site.com application. Users with a Publisher license can build and style
websites, control the layout and functionality of pages and page elements, and add and edit
content.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user can use the Salesforce console.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if the Wireless permission is enabled. Indicates whether the user is enabled to use
Wireless Edition ( `true` ) or not ( `false` ). Label is **Wireless User** .


Standard Objects User

**Field** **Details**

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.

```
UserPermissionsWorkDotComUserFeature

UserPreferencesActivityRemindersPopup

UserPreferencesAllowConversationReminders

UserPreferencesApexPagesDeveloperMode

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the WDC feature is enabled for the user ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder window automatically opens when an activity reminder is due.
Corresponds to the `Trigger alert when reminder comes due` checkbox at
the Reminders page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, voice and call reminders are displayed as notification cards in Lightning
Experience. Corresponds to the `Show conversation reminders in Lightning`
`Experience` checkbox in the Activity Reminders page in the personal settings in the user
interface.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, indicates that the user has enabled developer mode for editing Visualforce
pages and controllers.


Standard Objects User

**Field** **Details**

```
UserPreferencesAutoForwardCall

UserPreferencesContentEmailAsAndWhen

UserPreferencesContentNoEmail

UserPreferencesEnableAutoSubForFeeds

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user receives Dialer calls simultaneously in their browser and on their
forwarding number.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, a user with Salesforce CRM Content subscriptions receives a once-daily email
summary if activity occurs on the subscribed content, libraries, tags, or authors. To receive
email, the `UserPreferencesContentNoEmail` field must also be `false` .

The default value is `false` .

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, a user with Salesforce CRM Content subscriptions receives email notifications
if activity occurs on the subscribed content, libraries, tags, or authors. To receive real-time
email alerts, set this field to `false` and set the
`UserPreferencesContentEmailAsAndWhen` field to `true` .

The default value is `false` .

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user automatically subscribes to feeds for any objects that the user creates.
This field is available in API version 25.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesDisableAllFeedsEmail

UserPreferencesDisableAutoSubForFeeds

UserPreferencesDisableBookmarkEmail

UserPreferencesDisableChangeCommentEmail

UserPreferencesDisableEndorsementEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email for all updates to Chatter feeds, based
on the types of feed emails and digests the user has enabled. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically subscribes to feeds for any objects that the user creates.
This field is deprecated in API version 25.0 and later. Starting with API version 25.0, use
`UserPreferencesEnableAutoSubForFeeds` to enable or disable auto-follow
for objects a user creates.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
Chatter feed item after the user has bookmarked it. This field is available in API version 24.0
and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
change the user has made, such as an update to their profile. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the member automatically receives email every time someone endorses
them for a topic.

```
UserPreferencesDisableFileShareNotificationsForApi

UserPreferencesDisableFollowersEmail

UserPreferencesDisableLaterCommentEmail

UserPreferencesDisableLikeEmail

UserPreferencesDisableMentionsPostEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, email notifications are sent from the person who shared the file to the users
that the file is shared with. This field is available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone starts following
the user in Chatter. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
feed item after the user has commented on the feed item. This field is available in API version
24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone likes their post or
comment. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time they’re mentioned in posts.
This field is available in API version 24.0 and later.

```
UserPreferencesDisableProfilePostEmail

UserPreferencesDisableSharePostEmail

UserPreferencesDisableFeedbackEmail

UserPreferencesDisCommentAfterLikeEmail

UserPreferencesDisMentionsCommentEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone posts to the user’s
profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time their post is shared. This
field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives emails related to WDC feedback. The user
receives these emails when someone requests or offers feedback, shares feedback with the
user, or reminds the user to answer a feedback request.

This field isn’t visible as of API version 54.0.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on a
post that the user liked. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time the user is mentioned in
comments. This field is available in API version 24.0 and later.

```
UserPreferencesDisableMessageEmail

UserPreferencesDisableRewardEmail

UserPreferencesDisableWorkEmail

UserPreferencesDisProfPostCommentEmail

UserPreferencesEnableVoiceCallRecording

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email for Chatter messages sent to the user.
This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives emails related to WDC rewards. The user
receives these emails when someone gives a reward to the user.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user receives emails related to WDC feedback, goals, and coaching. The
user must also sign up for individual emails listed on the WDC email settings page. When
`true`, the user doesn’t receive any emails related to WDC feedback, goals, or coaching even
if they’re signed up for individual emails.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false`, the user automatically receives email every time someone comments on
posts on the user’s profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects User

**Field** **Details**

**Description**
When `true`, voice call recording is enabled for the user.

```
UserPreferencesEnableVoiceLocalPresence

UserPreferencesEventRemindersCheckboxDefault

UserPreferencesHideBiggerPhotoCallout

UserPreferencesHideChatterOnboardingSplash

UserPreferencesHideCSNDesktopTask

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, local numbers are shown when the user calls customers with Sales Dialer.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder popup is automatically set on the user's events. Corresponds to
the `By default, set reminder on Events to...` checkbox on the
Reminders page in the user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, users can choose to hide the callout text below the large profile photo.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the initial Chatter onboarding prompts don’t appear.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Chatter recommendations panel never displays the recommendation to
install Chatter Desktop. This field is available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesHideCSNGetChatterMobileTask

UserPreferencesHideEndUserOnboardingAssistantModal

UserPreferencesHideLightningMigrationModal

UserPreferencesHideSecondChatterOnboardingSplash

UserPreferencesHideS1BrowserUI

UserPreferencesHideSfxWelcomeMat

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Chatter recommendations panel never displays the recommendation to
install Chatter Mobile. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the secondary Chatter onboarding prompts don’t appear.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls the interface that the user sees when logging in to Salesforce from a supported
mobile browser. If `false`, the user is automatically redirected to the Salesforce mobile
web. If `true`, the user sees the full Salesforce site. The default value is `false` . Label is
**Salesforce User** .

This field is available in API version 29.0 or later.

**Type**
boolean


Standard Objects User

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Controls whether a user sees the Lightning Experience new user message. That message
welcomes users to the new interface and provides step-by-step instructions that describe
how to return to Salesforce Classic.

```
UserPreferencesJigsawListUser

UserPreferencesLightningExperiencePreferred

UserPreferencesLiveAgentMiawSetupDeflection

UserPreferencesNativeEmailClient

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the user is a Data.com List user so shares record additions from a pool.
UserPermissionsJigsawProspectingUser must also be set to `true` . Label is **Data.com List**
**User** . This field is available in API version 27.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, redirects the user to the Lightning Experience interface. Label is **Switch to**
**Lightning Experience** . This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, disables the pop-up to deflect users on Chat setup nodes to the Messaging
setup. The default value is `false` . This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Use this field to set a default email preference for the user’s native email client. This field is
available in API version 47.0 and later. The default value is `false`, corresponding to the
Salesforce docked email composer.


Standard Objects User

**Field** **Details**

```
UserPreferencesOptOutOfTouch

UserPreferencesOutboundBridge

UserPreferencesPathAssistantCollapsed

UserPreferencesProcessAssistantCollapsed

UserPreferencesReceiveNoNotificationsAsApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
This field is deprecated in API version 29.0. When `false`, the user automatically accesses
the Salesforce Touch app when logging in to Salesforce from an iPad. If `true`, automatic
access to the Salesforce Touch app is turned off and the user’s iPad is directed to the full
Salesforce site instead. The default value is `false` .

Note: Salesforce Touch must be enabled before this field is visible.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, outbound calls are made through the user’s phone.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, Sales Path appears collapsed or hidden to the user. This field is available in API
version 35.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, Sales Path appears collapsed or hidden to the user. This field is available in API
versions 33.0 and 34.0 only. In API versions 35.0 and later, use
`UserPreferencesPathAssistantCollapsed` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for _approvers_ .


Standard Objects User

**Field** **Details**

**•** If `true`, emails are _disabled_ .

**•** If `false`, emails are _enabled_ .

The default value is `false` .

Note: The `Receive Approval Request Emails` setting in the UI
controls this field and the

```
                     UserPreferencesReceiveNotificationsAsDelegatedApprover
```

field.

**•** Setting: **If I’m an approver or delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Only if I’m an approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: **Only if I’m a delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Never**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

```
UserPreferencesReceiveNotificationsAsDelegatedApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for _delegated approvers_ .

**•** If `true`, emails are _enabled_ .

**•** If `false`, emails are _disabled_ .

The default value is `false` .

Note: The `Receive Approval Request Emails` setting in the UI
controls this field and the
`UserPreferencesReceiveNoNotificationsAsApprover` field.

**•** Setting: **If I’m an approver or delegated approver**


Standard Objects User

**Field** **Details**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Only if I’m an approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: **Only if I’m a delegated approver**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: **Never**

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

```
UserPreferencesReminderSoundOff

UserPreferencesShowCityToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a sound automatically plays when an activity reminder is due. Corresponds to
the `Play a reminder sound` checkbox on the Reminders page in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. City is visible only to
internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

City is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowCityToGuestUsers` is `true`,
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

The default value is `false` . This field is available in API version 26.0 and later.

```
UserPreferencesShowCityToGuestUsers

UserPreferencesShowCountryToExternalUsers

UserPreferencesShowCountryToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. When `true`, city is
visible to guest users. Guest users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated with each site. When
`false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCityToExternalUsers`, making the user’s city visible
to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. Country is visible
only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Country is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowCountryToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. When `true`,
country is visible to guest users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site. When `false`, this field returns the value `#N/A` .


Standard Objects User

**Field** **Details**

When `true`, this field overrides the value `false` in
`UserPreferencesShowCountryToExternalUsers`, making the user’s country
visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

```
UserPreferencesShowEmailToExternalUsers

UserPreferencesShowEmailToGuestUsers

UserPreferencesShowFaxToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. Email
address is visible only to internal members of the user’s organization when this field is `false` .
Email address is visible to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. When
`true`, the email address is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowEmailToExternalUsers`, making the user’s email address
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. Fax number
is visible only to internal members of the user’s organization when this field is `false` . Fax
number is visible to external members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowFaxToGuestUsers

UserPreferencesShowManagerToExternalUsers

UserPreferencesShowManagerToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. When `true`,
the fax number field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowFaxToExternalUsers`, making the user’s fax number
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. Manager is
visible only to internal members of the user’s organization when this field is `false` . Manager
is visible to external members in an Experience Cloud site when this field is `true` . External
users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. When `true`,
the manager field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowManagerToExternalUsers`, making the user’s manager
visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowMobilePhoneToExternalUsers

UserPreferencesShowMobilePhoneToGuestUsers

UserPreferencesShowPostalCodeToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile device number field in the user’s contact information.
The number is visible only to internal members of the user’s organization when this field is
`false` . The number is visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer Portal, or partner portal
licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile phone field in the user’s contact information. When
`true`, the mobile phone field is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowMobilePhoneToExternalUsers`, making the user’s
mobile phone visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. Postal
code is visible only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Postal code is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowPostalCodeToGuestUsers`
is `true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

The default value is `false` . This field is available in API version 26.0 and later.

```
UserPreferencesShowPostalCodeToGuestUsers

UserPreferencesShowProfilePicToGuestUsers

UserPreferencesShowStateToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. When
`true`, postal code is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowPostalCodeToExternalUsers`, making the user’s
postal code visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the user’s profile photo. When `true`, the photo is visible to guest
users in an Experience Cloud site. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site.

When `false`, this field returns the stock photo. The default value is `false` . This field is
available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. State is visible only
to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

State is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowStateToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


Standard Objects User

**Field** **Details**

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

```
UserPreferencesShowStateToGuestUsers

UserPreferencesShowStreetAddressToExternalUsers

UserPreferencesShowStreetAddressToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. When `true`, state
is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowStateToExternalUsers, making the user’s state visible to external
members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. The address
is visible only to internal members of the user’s organization when this field is `false` . The
address is visible to external members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. When
`true`, the street address field is visible to guest users. Guest users can access public Site.com
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowStreetAddressToExternalUsers`, making the user’s
street address visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowTitleToExternalUsers

UserPreferencesShowTitleToGuestUsers

UserPreferencesShowWorkPhoneToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. Title is visible
only to internal members of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value `#N/A` .

Title is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but `UserPreferencesShowTitleToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `true` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. When `true`,
title is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title visible to external members.

The default value is `false` . This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone number field in the user’s contact information. The
number is visible only to internal members of the user’s organization when this field is
`false` . The number is visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer Portal, or partner portal
licenses.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 26.0 and later.


Standard Objects User

**Field** **Details**

```
UserPreferencesShowWorkPhoneToGuestUsers

UserPreferencesSortFeedByComment

UserPreferencesSuppressEventSFXReminders

UserPreferencesSuppressTaskSFXReminders

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone field in the user’s contact information. When `true`,
the work phone field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true`, this field overrides the value `false` in
`UserPreferencesShowWorkPhoneToExternalUsers`, making the user’s work
phone visible to guests.

When `false`, this field returns the value `#N/A` . The default value is `false` . This field is
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies the data value used in sorting a user’s feed. When `true`, the feed is sorted by most
recent comment activity. When `false`, the feed is sorted by post date.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, event reminders don’t appear. Corresponds to the **Show event reminders**
**in Lightning Experience** checkbox on the Activity Reminders page in the user interface.
This field is related to UserPreference and customizing activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, task reminders don’t appear. Corresponds to the **Show task reminders in**
**Lightning Experience** . checkbox on the Activity Reminders page in the user interface. This
field is related to UserPreference and customizing activity reminders.


Standard Objects User

**Field** **Details**

```
UserPreferencesTaskRemindersCheckboxDefault

UserPreferencesUserDebugModePref

UserRoleId

UserType

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a reminder popup is automatically set on the user's tasks. Corresponds to the
`By default, set reminder on Tasks to...` checkbox on the Reminders
page in the user interface. This field is related to UserPreference and customizing activity
reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the Lightning Component framework executes in debug mode for the user.
Corresponds to the `Debug Mode` checkbox on the Advanced User Details page of personal
settings in the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user’s UserRole. Label is **Role ID** .

This is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort, Restricted picklist

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and
later, valid values include:


Standard Objects User

**Field** **Details**

**•** Standard: user license. This user type also includes Salesforce Platform and Salesforce
Platform One user licenses. Label is **Standard** .

**•** PowerPartner: User whose access is limited because they’re a partner and typically access
the application through a partner portal or Experience Cloud site. Label is **Partner** .

**•** CspLitePortal: user whose access is limited because they’re an org's customer and access
the application through a Customer Portal or Experience Cloud site. Label is **High Volume**
**Portal** .

**•** CustomerSuccess: user whose access is limited because they’re an org's customer and
access the application through a Customer Portal. Label is **Customer Portal User** .

**•** PowerCustomerSuccess: user whose access is limited because they’re an org's customer
and access the application through a Customer Portal. Label is **Customer Portal**
**Manager** .

Users with this license type can view and edit data they directly own or data owned by
or shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is **Chatter Free** .

**•** Guest: user whose access is limited because they’re an unauthenticated user without
login credentials. Label is **Guest** .

```
WirelessEmail

```

Usage

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Wireless email address associated with this user. For use with Salesforce Wireless Edition.
This field is available only if the Wireless and Email permissions are enabled for your
organization.

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.

Use this object to query information about users and to provision and modify users in your organization. Unlike other objects, the records
in the User table represent actual users—not data owned by users. Any user can query or describe User records.


Standard Objects User

For example, the following SOQL code finds users with a particular user role.

```
   SELECT Id, Username

   FROM User

   WHERE UserRoleId='00ED0000000xicT'

```

Each portal user is associated with a portal account. A portal account can have a maximum of three portal roles (Executive, Manager,
and User). You can select the default number of roles to be created from the user interface. The role hierarchy is maintained when you
insert and delete portal roles, and roles are created bottom-up. Deleting the User role causes the Manager role to be renamed to User
role. Deleting both the Executive and User roles causes the Manager role to be renamed to User role. Before deleting a role, you must
assign users under that role to another role.

Deactivate Users

You can’t delete a user in the user interface or the API. You can deactivate a user in the user interface; and you can deactivate or disable
a Customer Portal or partner portal user in the user interface or the API. Because users can never be deleted, we recommend that you
exercise caution when creating them.

[Be aware of the expected behaviors when deactivating users. See Considerations for Deactivating Users. The user interface provides](https://help.salesforce.com/s/articleView?id=platform.users_deactivate_considerations.htm&type=5&language=en_US)
options to auto-remove a user from teams, but the removal isn’t supported in API.

If you deactivate a user, any EntitySubscription where the user is associated with the ParentId or SubscriberId field, meaning all subscriptions
both to and from the user, are soft deleted. If the user is reactivated, the subscriptions are restored. However, if you deactivate multiple
users at once and these users follow each other, their subscriptions are hard deleted. In this case, the user-to-user EntitySubscription is
deleted twice (double deleted). Such subscriptions can’t be restored upon user reactivation.

Passwords

For security reasons, you can’t query User passwords via the API or the user interface. But the API allows you to set and reset User
passwords using the `setPassword()` and `resetPassword()` calls. The password lockout status and the ability to reset the
User locked-out status isn’t available via the API. Check and reset the User password lockout status using the user interface.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserChangeEvent (API version 44.0)**
Change events are available for the object.

**UserFeed (API version 18.0)**
Feed tracking is available for the object.

**UserShare**

Sharing is available for the object.

SEE ALSO:

_SOAP API Developer Guide_ [: Frequently-Occurring Fields](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_objects_fequently_occurring_fields.htm)

UserRole

UserLicense


### Standard Objects UserAccessChange UserAccessChange

Represents a change related to user access. This object is available in API version 57.0 and later.

### UserAccessChange records are created through different access-related operations. For example, being assigned to or removed from a

permission set.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To access UserAccessChange records, users must have the View Setup and Configuration permission.

Fields

**Field** **Details**

```
Source

### UserAccessPolicy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
### The source of the user access change. For example, UserAccessPolicyId .

Represents a user access policy. This object is available in API version 57.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To create or modify user access policies, users must have the Manage User Access Policies permission.


Standard Objects UserAccessPolicy

Fields

**Field** **Details**

```
BooleanFilter

Description

DeveloperName

Language

MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logic that determines how your user criteria filters are applied in the user access policy.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name for the user access policy.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the user access policy. In the UI, this field is Label.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserAccessPolicy

**Field** **Details**

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

```
Order

Status

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the order for which active policy is applied when a user meets the criteria for
multiple policies. Must be an integer from 0 to 10,000. Only the active policy with the lowest
`Order` value is applied. This field is required only if the `Status` field is set to `Active` .

Available in API version 61.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user access policy.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Design`

**•** `Failed`

**•** `Migrate`

**•** `Testing`

**•** `Updating`

The default value is `Design` .


### Standard Objects UserAccountTeamMember

**Field** **Details**

```
TriggerType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of user record trigger for which this user access policy runs.

Possible values are:

**•** `Create` —The user access policy runs when a user who matches the policy criteria is
created.

**•** `CreateAndUpdate` —The user access policy runs when a user who matches the
policy criteria is either created or updated.

**•** `Update` —The user access policy runs when a user who matches the policy criteria is
updated.

[For more information, see User Access Policies in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.perm_user_access_policies.htm&type=5&language=en_US)

### UserAccountTeamMember

Represents a User on the default account team of another User.

See also OpportunityTeamMember, which represents a User on the opportunity team of an Opportunity

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal and Chatter Free users can't access this object.

Fields

**Field** **Details**

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


Standard Objects UserAccountTeamMember

**Field** **Details**

**Description**
Required. For Account records that the user has added to his or her default account
team, the level of access the account team member has. . The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for accounts.

```
CaseAccessLevel

ContactAccessLevel

OpportunityAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the account team member has to Case records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for cases.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. ForContact records related to the account, the level of access that the
account team member has. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for contacts. When `DefaultContactAccess` is set to
`Controlled by Parent`, you can’t create or update this field.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


Standard Objects UserAccountTeamMember

**Field** **Details**

**Description**
Required. Level of access that the team member has to Opportunity records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for opportunities.

```
 OwnerId

 TeamMemberRole

 UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default account team.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the user has added his
or her default account team. The valid values are set by the organization’s administrator
in the Account Team Roles picklist. Label is **Team Role** .

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default account team. This field
cannot be updated.

This object is available only in organizations that have enabled the account teams functionality, which can be done using the user
interface.

If you attempt to create a record that matches an existing record, the create call updates any modified fields and returns the existing
record.

You can set up a User record so the default account team includes the others who typically work with them on accounts.


### Standard Objects UserAppInfo UserAppInfo

Stores the last Lightning app logged in to. If the user hasn’t logged into Salesforce or if the user lost access to the last accessed app, the
### UserAppInfo object stores a Null value. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AppDefinitionId

FormFactor

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the last Lightning app that the user logged in to. This field is available
in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The relative size of the app as displayed. Values are:

**•** Small—suitable for a small device like a mobile phone

**•** Medium—suitable for a tablet

**•** Large—suitable for a large display device, like a monitor

It’s possible to have three versions of the app as the one last logged in to, where
each version has a different form factor.


### Standard Objects UserAppMenuCustomization

**Field Name** **Details**

```
UserId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that used this app.

This is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Lookup

**Refers To**
### User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserAppInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### UserAppMenuCustomization

Represents an individual user’s settings for items in the app menu or App Launcher. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ApplicationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15-character ID for the application associated with the menu item.


Standard Objects UserAppMenuCustomization

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
Application

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

```
OwnerId

SortOrder

```

Usage

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user for these specific settings.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.

See the AppMenuItem object for the organization-wide default settings This object contains the fields representing any changes the
user made to the menu.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects UserAppMenuItem

**UserAppMenuCustomizationOwnerSharingRule**

Sharing rules are available for the object.

**UserAppMenuCustomizationShare**

Sharing is available for the object.

### UserAppMenuItem

Represents the organization-wide settings for items in the app menu or App Launcher that the requesting user has access to in Setup.
This object is available in API version 35.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
AppMenuItemId

ApplicationId

Description

IconUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the application associated with the menu item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A description of this menu item.

**Type**
url


Standard Objects UserAppMenuItem

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon for the menu item’s application.

```
InfoUrl

IsUsingAdminAuthorization

IsVisible

Label

LogoUrl

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL for more information about the application.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the app is pre-authorized for certain users by the administrator.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the app is visible to the user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The app’s name.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The logo for the menu item’s application. The default is the initials of the `Label`
value.


Standard Objects UserAppMenuItem

**Field Name** **Details**

```
MobileStartUrl

Name

SortOrder

StartUrl

Type

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location mobile users are directed to after they’ve authenticated. This is only
used with connected apps.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The API name of the item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location users are directed to after they’ve authenticated. For a connected
app, this is the location specified by the `StartUrl` . Otherwise it’s the
application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of application represented by this item. The types are:

**•** ConnectedApplication


### Standard Objects UserAuthCertificate

**Field Name** **Details**

**•** Network

**•** ServiceProvider

**•** TabSet

```
UserSortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that represents where the user set this item in the menu (or App
Launcher). For example, an item with a sort order value of 5 will appear between
items with sort order values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both
values. For example, if you want the user-sorted items to appear first, followed
by the organization order for the rest, use:

```
  SELECT ApplicationId,SortOrder,UserSortOrder FROM

  AppMenuItem order by userSortOrder NULLS LAST,

  sortOrder NULLS LAST

```

See the AppMenuItem object for the organization-wide default settings This object contains the fields the requesting user has permission
to see.

### UserAuthCertificate

Represents a user authentication certificate in your org. A user certificate is a unique PEM-encoded X.509 digital certificate to authenticate
individual users to your org. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in orgs with `Let users authenticate with a certificate` enabled in Identity Verification.
Only users with the Manage Internal Users permission can access this object.


Standard Objects UserAuthCertificate

Fields

**Field** **Details**

```
CertificateChain

CertificateChainLength

DeveloperName

ExpirationDate

Fingerprint

```

**Type**
base64

**Properties**
Create, Update

**Description**
The uploaded PEM files can contain a single certificate or up to 10 certificates in a certificate
chain. Uploaded PEM files can’t be larger than 1 MB.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-generated length of the certificate or certificate chain in the uploaded PEM file.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, Salesforce generates one for each record,
which slows performance.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The expiration date of the uploaded certificate.

**Type**
string

**Properties**
Filter. Group, idLookup, Sort


Standard Objects UserAuthCertificate

**Field** **Details**

**Description**
The unique fingerprint of the uploaded certificate.

```
Language

MasterLabel

SerialNumber

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language in which to display the certificate.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexico)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazil)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A descriptive name for the certificate.

**Type**
string

**Properties**
Filter, Group, Sort


### Standard Objects UserConfigTransferButton

**Field** **Details**

**Description**
The serial number of the uploaded certificate.

```
UserID

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user associated with the certificate.

### UserConfigTransferButton

Represents the association between a Chat configuration and a live chat button. This association allows users associated with a specific
configuration to transfer chats to a button queue.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
LiveChatButtonId

LiveChatUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the live chat button that agents can transfer chats to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserConfigTransferSkill

**Field Name** **Details**

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId` .

### UserConfigTransferSkill

Represents the association between a Chat configuration and a skill. This association allows users associated with a specific configuration
to transfer chats to agents who have that skill.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

SkillId

### UserCustomBadge

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the skill group that agents can transfer chats to.

Represents a custom badge for a user. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects UserCustomBadgeLocalization

Fields

**Field Name** **Details**

```
BadgeType

CustomText

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of badge. Valid values are:

**•** `Customer`

**•** `Partner`

**•** `Employee`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Custom text for the badge.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site or org that the badge is in.

### UserCustomBadgeLocalization

Represents the translated version of a custom badge for a user. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Translation Workbench must be enabled for your org.

**•** Users with the “Customize Application” or “Manage Translation” permission can create or update UserCustomBadge translations.


Standard Objects UserCustomBadgeLocalization

Fields

**Field Name** **Details**

```
Language

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language the UserCustomBadge is translated into.

This picklist contains these fully supported languages.

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.


### Standard Objects UserDailyMetric

**Field Name** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
ParentId

Value

### UserDailyMetric

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the UserCustomBadge.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the UserCustomBadge. Label is **Translation Text** .

Represents the daily engagement metrics for a user. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

```

**Type**
int


Standard Objects UserDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Call Back Later.

```
AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Unqualified.

**Type**
int


Standard Objects UserDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this user in the day.

This is a calculated field.

```
AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsNotDeliveredCount

AllEmailsOutOfOfficeCount

AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this user in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of emails sent by this user in the day.

This is a calculated field.

```
AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

DailyCutOffTimeStamp

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls by this user with all call results in the day.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.


Standard Objects UserDailyMetric

**Field** **Details**

```
Date

DateInt

HardBounceTrackableSends

LinkClickTrackableSends

OpenTrackableSends

OutOfOfficeTrackableSends

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date on which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The date on which the engagement occurred, in yyyymmdd format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 53.0 and later.


Standard Objects UserDailyMetric

**Field** **Details**

```
RecipientReplies

RecipientSends

ReplyTrackableRecipientSends

ReplyTrackableSends

SoftBounceTrackableSends

SomeEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who responded to an email. Available in API version 53.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who were sent an email. Available in API version 53.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with reply tracking. Available in API version
53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This is a calculated field.

```
SomeEmailsDeliveredRate

TrackableRecipientSendReplyRt

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This is a calculated field.


Standard Objects UserDailyMetric

**Field** **Details**

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserDailyMetric

**Field** **Details**

**Description**
The number of unique recipients who clicked a link in an email sent by the user on the day.

```
UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

UserId

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by the user on the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by the user on the day.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserDailyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserDailyMetricShare on page 67**
Sharing is available for the object.


### Standard Objects UserDailyMetricOwnerSharingRule UserDailyMetricOwnerSharingRule

Represents the rules for sharing the user daily metric with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines the level of access users have to records. Values are:

**•** `Read` (read only)

**•** `Edit` (read/write)

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the sharing rule. Maximum length is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a


### Standard Objects UserDefinedLabel

**Field** **Details**

letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
GroupId

Name

UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the source group. Records that are owned by users in the source group trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the UI. Maximum length is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that you are granting access to.

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

UserDailyMetric

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### UserDefinedLabel

Represents a label created by a user to help organize, track, and find records. This object is available in API version 61.0 and later.


Standard Objects UserDefinedLabel

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Color

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Hexadecimal value of the color used to help organize the UserDefinedLabel records.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly. For example,
accessed through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.
For example, accessed through a list view or related record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the UserDefinedLabel record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects UserDefinedLabelAssignment

**Field** **Details**

**Description**
ID of the user or group that owns the label.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
TotalAssignments

Type

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Calculated field. Number of related UserDefinedLabelAssignment records. Available in API
version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of user-defined label.

Possible values are:

**•** `Starred`

**•** `Tag`

### • User

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserDefinedLabelShare on page 67**
Sharing is available for the object.

### UserDefinedLabelAssignment

Represents a relationship between a record label and the item the user assigned it to. This object is available in API version 61.0 and
later.


Standard Objects UserDefinedLabelAssignment

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EntityType

ItemId

LabelId

OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object label of the Item record derived from ItemId. Available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Item record added to the UserDefinedLabel record.

This field is a polymorphic relationship field.

**Relationship Name**
Item

**Refers To**
Account, ActionCadence, ActionCadenceStepTracker, CallTemplate, Case, Contact,
EmailTemplate, FlowOrchestrationWorkItem, Lead, Opportunity, Task

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the UserDefinedLabel record that the Item record is assigned to.

This field is a relationship field.

**Relationship Name**
Label

**Refers To**
UserDefinedLabel

**Type**
reference


### Standard Objects UserDevice

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
SortOrder

SubjectOrName

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Order of the assigned items for a given UserDefinedLabel record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Item record. If it's a task, the value is the subject of the Item record.

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelAssignmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserDefinedLabelAssignmentShare on page 67**
Sharing is available for the object.

### UserDevice

Represents information unique to a device. Available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects UserDevice

Special Access Rules

You must have View Devices enabled to see devices.

Fields

**Field Name** **Details**

```
BrowserType

DeviceNativeUid

DeviceType

IsVerified

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser used for login.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A unique string used to identify a mobile device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The device used to log in to Salesforce. The picklist options are:

**•** `Desktop`

**•** `Tablet`

**•** `iPad`

**•** `iPhone`

**•** `Phone`

**•** `Unknown`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


Standard Objects UserDevice

**Field Name** **Details**

```
LastLoginHistoryId

Name

PlatformType

PlatformVersion

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most recent LoginHistory associated with the device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and can’t be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operating system of the device. The picklist options are:

**•** iOS

**•** Android

**•** OSX

**•** Linux

**•** Phone

**•** Windows

**•** AppleApp

**•** Blackberry

**•** Other

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the operating system running on the device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects UserDeviceApplication

**Field Name** **Details**

**Description**
The activity status of the device. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

```
UserId

UserLastSeen

UserProvidedDeviceIdentifier

### UserDeviceApplication

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the user’s last access.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
An identifier for the user’s device such as the International Mobile Equipment
Identity (IMEI) number or the device serial number.

Note: This field isn’t automatically populated. The developer must provide
values.

Represents information on applications installed on a device that is accessing Salesforce. Available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects UserDeviceApplication

Special Access Rules

You must have View Devices enabled to see devices.

Fields

**Field Name** **Details**

```
ApplicationType

Name

Status

UserDeviceId

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application used to log in to Salesforce.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and cannot be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The activity status of the device application. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events.
`UserDeviceId` is a generated value that’s created when the mobile app is
initially run after installation.

**Type**
reference


### Standard Objects UserDeviceHistory

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.

### UserDeviceHistory

Represents tracking information on the UserDevice sObject. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data that has changed.

Possible values are:

**•** `Address`

**•** `AnyType`

**•** `AutoNumber`

**•** `Base64`

**•** `BitVector`

**•** `Boolean`

**•** `Content`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `DateOnly`

**•** `DateTime`

**•** `Division`

**•** `Double`


Standard Objects UserDeviceHistory

**Field** **Details**

**•** `DynamicEnum`

**•** `Email`

**•** `EncryptedBase64`

**•** `EncryptedText`

**•** `EntityId`

**•** `EnumOrId`

**•** `ExternalId`

**•** `Fax`

**•** `File`

**•** `HtmlMultiLineText`

**•** `HtmlStringPlusClob`

**•** `InetAddress`

**•** `Json`

**•** `Location`

**•** `MultiEnum`

**•** `MultiLineText`

**•** `Namespace`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Raw`

**•** `RecordType`

**•** `SfdcEncryptedText`

**•** `SimpleNamespace`

**•** `StringPlusClob`

**•** `Switchable_PersonName`

**•** `Text`

**•** `TimeOnly`

**•** `Url`

**•** `YearQuarter`

```
Field

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The field that has changed.

Possible values are:


Standard Objects UserDeviceHistory

**Field** **Details**

**•** `BrowserType` —Browser

**•** `DeviceNativeUid` —Device Native ID

**•** `DeviceType` —Device Type

**•** `HashedBrowserFingerPrint` —Hashed Browser Fingerprint

**•** `IsVerified` —Is Device Verified

**•** `LastLoginHistory` —Login History

**•** `Name`

**•** `PlatformType` —Platform or OS Type

**•** `PlatformVersion` —Platform or OS Version

**•** `RawBrowserFingerPrint` —Raw Browser Fingerprint Data

**•** `Status` —Device Status

**•** `User`

**•** `UserLastSeen` —Last time user was seen

**•** `UserProvidedDeviceIdentifier` —User provided device identifier

**•** `created` —Created.

**•** `feedEvent` —Feed event

**•** `individualMerged` —Individual Merged

**•** `locked` —Record locked.

**•** `ownerAccepted` —Owner (Accepted)

**•** `ownerAssignment` —Owner (Assignment)

**•** `unlocked` —Record unlocked.

```
NewValue

OldValue

UserDeviceId

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value after a change has occurred.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value before a change has occurred.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects UserEmailCalendarSync

**Field** **Details**

**Description**
The ID of the UserDevice object.

### UserEmailCalendarSync

Represents the user assignments of an Einstein Activity Capture configuration. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Einstein Activity Capture in your org.

Fields

**Field** **Details**

```
AssignedId

ConfigurationId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user or profile. Only Einstein Activity users can be added to a configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Einstein Activity Capture configuration. The configuration is created in Salesforce
Setup. After the configuration is created, the autogenerated ID is visible on the Configurations
tab. From Setup, in the Quick Find box, enter _`Einstein Activity Capture`_, and
then select **Settings** . Click the Configurations tab.

Use UserEmailCalendarSync to add and remove users to an Einstein Activity Capture configuration. You can add users to a configuration
via a user ID or a profile ID. You can add a profile to only one configuration and assign a profile to only one user.


### Standard Objects UserEmailPreferredPerson

This example adds two users to an Einstein Activity Capture configuration.

```
   // Create a list of UserEmailCalendarSync records

   List<UserEmailCalendarSync> usersToAdd = new ArrayList<>();

   // Populate the UserEmailCalendarSync record with the ID of

   // the user or profile, and with the ID of the Activity Capture configuration you are

   adding them to

   UserEmailCalendarSync user1 = new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',

    AssignedId = '005xxxxxxxxxxxx');

   UserEmailCalendarSync user2= new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',

    AssignedId = '005xxxxxxxxxxxx');

   // add the UserEmailCalendarSync users to your list

   usersToAdd.add(user1);

   usersToAdd.add(user2);

   // Insert the list of UserEmailCalendarSync into the database

   Database.SaveResult[] results = Database.insertImmediate(usersToAdd);

```

This example removes a user from an Einstein Activity Capture configuration.

To remove a user, call `UserEmailCalendarSync()`, passing in `null` for `ConfigurationId` .

```
   UserEmailCalendarSync user2Remove= new UserEmailCalendarSync(ConfigurationId = "", AssignedId

    ='005xxxxxxxxxxxx');

   Database.SaveResult results =Database.insertImmediate(user2Remove);

### UserEmailPreferredPerson

```

Represents a mapping for a user’s preferred record for an email address when multiple records match an email field.This object is available
in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ‘20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
Email

```

**Type**
email


Standard Objects UserEmailPreferredPerson

**Field** **Details**

**Properties**
Create, Filter,Group, idLookup, Sort, Update

**Description**
Required. The unique email the mapping applies to. This field is unique for each user.

```
Name

OwnerId

PersonRecordId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto-generated field.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The userId that owns the record. Each record is only accessible to the owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The recordId of a contact, lead, or user that represents the preferred record for the
email address. Use cascade delete for contact and lead, and delete if the personId is a
deactivated user record.

This is a polymorphic relationship field.

**Relationship Name**
PersonRecord

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


### Standard Objects UserEmailPreferredPersonShare

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserEmailPreferredPersonChangeEvent (API version 62.0)**
Change events are available for the object.

### **UserEmailPreferredPersonShare**

Sharing is available for the object.

### UserEmailPreferredPersonShare

Represents a sharing entry on a UserEmailPreferredPerson object. Sharing is not customizable for UserEmailPreferredPerson records.This
object is available in API version 44.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccessLevel

ParentId

```

**Type**
picklist

**Properties**
Create, Filter,Group, Restricted picklist, Sort, Update

**Description**
Required. The level of access allowed. Values can be:

**•** `All`

**•** `Edit`

**•** `Read`

.

**Type**
reference

**Properties**
Create, Filter,Group, Sort,


Standard Objects UserEmailPreferredPersonShare

**Field** **Details**

**Description**
Id of the parent record, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
UserEmailPreferredPerson

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter,Group, Nillable, Restricted picklist, Sort,

**Description**
Required. Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` . All other
`RowCause` values are read-only. After the sharing entry is created, this field can’t be edited.
Valid values can include:

**•** `Manual` —The User or Group has access because a user with All access manually shared
the record with them.

**•** `Owner` —The User is the owner of the record or is in a role above the record owner in
the role hierarchy.

**Type**
reference

**Properties**
Create, Filter,Group, Sort,

**Description**
Required. ID of the user or group that has been given access to the
`UserEmailPreferredPerson` record. The `UserOrGroupID` is polymorphic. The
label is `User/Group Id` .

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects UserLicense UserLicense

Represents a user license in your organization. A user license entitles a user to specific functionality and determines the profiles and
permission sets available to the user.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
LicenseDefinitionKey

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A string that uniquely identifies a particular user license. Label is `License Def. ID` .
Values are:

**AUL** : corresponds to the Salesforce Platform user license

**AUL1** : corresponds to the Salesforce Platform One user license

**AUL_LIGHT** corresponds to the Salesforce Platform Light user license

**FDC_ONE** corresponds to the Lightning Platform - One App user license

**FDC_SUB** corresponds to the Lightning Platform App Subscription user license

**Overage_Platform_Portal_User** corresponds to the Overage Authenticated Website user
license

**PID_STRATEGIC_PRM** : corresponds to the Gold Partner user license

**PID_CHATTER** corresponds to the Chatter Only user license

**PID_CONTENT** corresponds to the Content Only user license

**PID_Customer_Portal_Basic** : corresponds to the Customer Portal Manager Standard user
license and the Customer Portal User license

**PID_Customer_Portal_Standard** : corresponds to the Customer Portal Manager Custom
user license

**PID_FDC_FREE** corresponds to the Lightning Platform Free user license

**PID_IDEAS** corresponds to the Ideas Only user license

**PID_Ideas_Only_Portal** corresponds to the Ideas Only Portal user license

**PID_Ideas_Only_Site** corresponds to the Ideas Only Site user license

**PID_KNOWLEDGE** corresponds to the Knowledge Only user license

**PID_Customer_Community** corresponds to the Customer Community license.


Standard Objects UserLicense

**Field** **Details**

**PID_Customer_Community_Login** corresponds to the Customer Community Login
license.

**PID_Partner_Community** corresponds to the Partner Community license.

**PID_Partner_Community_Login** corresponds to the Partner Community Login license.

**PID_Limited_Customer_Portal_Basic** : corresponds to the Limited Customer Portal
Manager Standard user license

**PID_Limited_Customer_Portal_Standard** : corresponds to the Limited Customer Portal
Manager Custom user license

**PID_Overage_Customer_Portal_Basic** : corresponds to the Overage Customer Portal
Manager Standard user license

**PID_Overage_High Volume Customer Portal** corresponds to the Overage High Volume
Customer Portal user license

**Platform_Portal_User** : corresponds to the Authenticated Website user license

**POWER_PRM** : corresponds to the Partner user license

**POWER_SSP** : corresponds to the Customer Portal Manager user license

**SFDC** : corresponds to the Full CRM user license

```
MasterLabel

MonthlyLoginsEntitlement

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user license label.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum number of customer or partner portal logins allowed per month. A `null`
value in this field means the user license is charged according to the number of users rather
than the number of logins.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission


Standard Objects UserLicense

**Field** **Details**

```
MonthlyLoginsUsed

Name

Status

TotalLicenses

UsedLicenses

```

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
The number of successful logins for all users associated with a customer or partner portal
user license. This field has a non- `null` value if `MonthlyLoginsEntitlement` has
a non- `null` value.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The internal name of the user license.

Note: Your organization may also include custom user licenses.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current status of the user license. Valid values for this field are `Active` and `Disabled` .

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of user licenses in the organization.

This field is available in API version 32.0 and later.

**Type**
int


### Standard Objects UserListView

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The number of user licenses that are assigned to active users in the organization.

This field is available in API version 32.0 and later.

This field isn’t filterable in API version 64.0 or later when using it in a WHERE clause in a SOQL
query. Instead, you have to process the data after fetching all the records.

UsedLicensesLastUpdated

Usage

**Type**
dateTime

**Properties**
aggregate, Filter, Sort

**Description**
The timestamp of the query. If your license count exceeds your org’s allotted threshold, the
count timestamp reflects the previous day, otherwise the timestamp reflects the current day
and time.

This field is available in API version 41.0 and later.

Users with the “View Setup and Configuration” permission can use the UserLicense object to view the set of currently defined user
licenses in your organization.

The UserLicense object is currently used by bulk user creation to determine the user license to which each profile and permission set
belongs. For example, if you use the API to create portal users and you want to know which profile belongs to each portal user license,
you can query this object for each profile and check the `LicenseDefinitionKey` to identify the associated user license.

SEE ALSO:

Profile

PermissionSet

### UserListView

Represents the customizations a user made to a list view. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects UserListView

Fields

**Name** **Details**

```
LastViewedChart

ListViewId

SobjectType

UserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The last chart a user viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the list view.

This is a relationship field.

**Relationship Name**
ListView

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The API name of the sObject for the user list view.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects UserListViewCriterion

**Name** **Details**

**Refers To**
### User UserListViewCriterion

Represents the criterion for a user’s customized list view. The criterion consists of the filters or sort order a user added to a list view for
the Salesforce Mobile app. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Name** **Details**

```
ColumnName

Operation

SortOrder

UserListViewId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the column in the user list view.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which the list view is evaluated compared to other UserListViewCriterion objects
for the given UserListView.

**Type**
reference


### Standard Objects UserLocationAssignment

**Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user list view.

This is a relationship field.

**Relationship Name**
UserListView

**Relationship Type**
Lookup

**Refers To**
UserListView

```
Value

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field values used to filter the list view. For example, a value of `94105` if the Field is
`Billing Zip/Postal Code` shows only rows that have a billing ZIP code of 94105.

### UserLocationAssignment

Represents the assignment between a location and a user. This object is available in API version 57.0 and later.

Supported Calls:

create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(), undelete(), update(),
upsert()

Special Access Rules:

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

### `UserLocationAssignmentNumber`

**Type**
text


Standard Objects UserLocationAssignment

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for the association

```
AssignedTo

Location

Username

IsActive

```

Usage:

**Type**
foreignkey (user)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
User being associated with the location

**Type**
foreignkey (location)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Location being associated to the User

**Type**
string (derived)

**Properties**
Filter, Sort

**Description**
Username of the User that is associated to the Location

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Whether the location is active or not

The UserLocationAssignment object associates a user to specified work locations. To assign a user to multiple locations, create Multiple
UserLocationAssignment objects. Use the isActive field to indicates the user's current active location.


### Standard Objects UserLogin UserLogin

Represents the settings that affect a user’s ability to log into an organization. To access this object, you need the
`UserPermissions.ManageUsers` permission. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
IsFrozen

IsPasswordLocked

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true` [, the user account associated with this object is frozen. If a user's account](https://help.salesforce.com/s/articleView?id=platform.users_freeze.htm&language=en_US)
is frozen, they can't log in, but their account isn't deactivated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the user account associated with this object is locked because of too
many login failures. From the API, you can set this field to `false`, but not `true` .

Note: If the Lockout effective period is set to Forever (must be reset by
admin) in your org’s Password Policies Setup page, this field isn’t set to
`false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated user account. This field can’t be updated.


### Standard Objects UserMembershipSharingRule

Usage

To query for all frozen users in your organization:

```
   SELECT Id, UserId

   FROM UserLogin

   WHERE IsFrozen = true

```

[To freeze or unfreeze multiple users, use Data Loader.](https://help.salesforce.com/s/articleView?id=000387522&type=1&language=en_US)

### UserMembershipSharingRule

Represents the rules for sharing user records from a source group to a target group. A user record contains details about a user. Users
who are members of the source group can be shared with members of the target group. The source and target groups can be based
on roles, portal roles, public groups, or territories. This object is available in API version 26.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts


Standard Objects UserMembershipSharingRule

**Field** **Details**

on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
GroupId

Name

UserAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target group being given access.


### Standard Objects UserMonthlyMetric

Usage

Use this object to manage sharing rules for user records. Source and target groups can include internal users, portal users, Chatter or
Chatter External users.

### UserMonthlyMetric

Represents the monthly engagement metrics for a user. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Meaningful Connect.

**Type**
int


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Not Interested.

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails sent by this user in the month.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent by this user in the month.

This is a calculated field.

```
AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

DeliveredRecipientCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user that soft bounced in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls with all call results for this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received an email. Available in API version 53.0
and later.

This is a calculated field.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
DeliveredRecipientRate

HardBounceTrackableSends

HrdBncTrackableRecipientSends

LinkClickTrackableSends

LinkClkTrackableRecipientSends

Month

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients who successfully received an email. Available in API
version 53.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with hard bounce tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with link click tracking. Available in API
version 53.0 and later.

**Type**
date


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

```
MonthInt

OooTrackableRecipientSends

OpenTrackableRecipientSends

OpenTrackableSends

OutOfOfficeTrackableSends

```

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with out-of-office tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with open tracking. Available in API version
53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 53.0 and later.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
RecipientReplies

RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

RecipientsSoftBounce

ReplyTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who responded to an email. Available in API version 53.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who were sent an email. Available in API version 53.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of email recipients who were sent an email that hard bounced. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who responded with an out-of-office reply. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email that soft bounced. Available in API version
54.0 and later.

**Type**
int


Standard Objects UserMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with reply tracking. Available in API version
53.0 and later.

```
ReplyTrackableSends

SftBncTrackableRecipientSends

SoftBounceTrackableSends

SomeEmailsDeliveredCount

SomeEmailsDeliveredRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with soft bounce tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This field is a calculated field.

```
TrackableRecipientSendHrdBncRt

TrackableRecipientSendOooRate

TrackableRecipientSendReplyRt

TrackableRecipientSendSftBncRt

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients who hard bounced an email with hard bounce tracking.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that resulted in out-of-office replies
from unique recipients. This field is a calculated field. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that soft
bounced.

This field is a calculated field. Available in API version 54.0 and later.


Standard Objects UserMonthlyMetric

**Field** **Details**

```
TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects UserMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This field is a calculated field.

```
TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

UserId

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who clicked a link in an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by this user in the month.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.


### Standard Objects UserMonthlyMetricOwnerSharingRule

**Field** **Details**

This is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Lookup

**Refers To**
### User

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

### **UserMonthlyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserMonthlyMetricShare on page 67**
Sharing is available for the object.

### UserMonthlyMetricOwnerSharingRule

Represents the rules for sharing the user monthly metric with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects UserMonthlyMetricOwnerSharingRule

**Field** **Details**

**Description**
Determines the level of access users have to records. Values are:

**•** `Read` (read only)

**•** `Edit` (read/write)

```
Description

DeveloperName

GroupId

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the sharing rule. Maximum length is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the source group. Records that are owned by users in the source group trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the UI. Maximum length is 80 characters.


### Standard Objects UserPackageLicense

**Field** **Details**

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that you are granting access to.

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

UserMonthlyMetric

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### UserPackageLicense

Represents a license for an installed managed package, assigned to a specific user. This object is available in API version 31.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve() update()`

Fields

**Field Name** **Details**

```
IsRevoked

LastCreatedByChangeId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Reserved for internal use. This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserPackageLicense

**Field Name** **Details**

**Description**
ID of the user access change record related to this managed package license assignment. This
field is available only if user access policies are enabled. This field is available in API version 58.0
and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

```
LastDeletedByChangeId

PackageLicenseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user access change record related to this managed package license assignment being
revoked. This field is available only if user access policies are enabled. This field is available in API
version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The 18-character Globally Unique ID (GUID) that identifies the package license

This is a relationship field.

**Relationship Name**
PackageLicense

**Relationship Type**
Lookup

**Refers To**
PackageLicense


### Standard Objects UserPermissionAccess

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The User ID of the user licensed to use this package

Use this object, in conjunction with PackageLicense, to provide users access to a managed package installed in your organization.

### UserPermissionAccess

Represents the permissions accessibility for a current user. Available in API version 41.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
LastCacheUpdate

Permissions<PermissionName>

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of either the user info or org info, whichever is later.

**Type**
boolean

**Properties**
Filter

**Description**
The name of the permission, such as `PermissionsActivateContract` or
`PermissionsAuthorApex` and whether it’s available to the user ( `true` ) or not
( `false` ).


### Standard Objects UserPrioritizedRecord

Usage

API users without `PermissionsViewSetup` can use this object to check if their own sessions have access to a feature.

SEE ALSO:

Profile

PermissionSet

### UserPrioritizedRecord

Represents records that Pipeline Inspection, Account Intelligence, Contact Intelligence, and Lead Intelligence users flag as important for
tracking in pipeline and intelligence views and filters. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To use UserPrioritizedRecord in Pipeline Inspection and the Account Intelligence, Contact Intelligence, and Lead Intelligence views,
enable the Pipeline Inspection user permission and the Pipeline Inspection setting.

Fields

**Field** **Details**

```
OwnerId

TargetId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who marked this record as important.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


### Standard Objects UserPreference

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the target object that is marked as important. Supported objects include:

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

```
TargetKeyPrefix

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The key prefix of the target object that is marked as important.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserPrioritizedRecordOwnerSharingRule on page 65**
Sharing rules are available for the object.

**UserPrioritizedRecordShare on page 67**
Sharing is available for the object.

### UserPreference

Represents a functional preference for a specific user in your organization.


Standard Objects UserPreference

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can't access this object.

Only users with the View All Data or Manage Users permission can access UserPreference records of other users but all users can access
their own UserPreference record.

Note: This behavior does not affect other types of user access such as Create or Edit.

Fields

**Field** **Details**

```
Preference

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the user preference. Supported values are:

**•** `57` (Event Reminder Default Lead Time)

**•** `58` (Task Reminder Default Time)

**•** `91` (Prevent Logs on Load)

**•** `92` (Autocomplete Apex After Key Press)

**•** `93` (Visualforce Viewstate Inspector)

**•** `94` (Forecasting Displayed Type)

**•** `96` (Editor Theme)

**•** `97` (Editor Font Size)

**•** `98` (Pinned Folders)

**•** `99` (Enable Query Plan)

**•** `100` (Enable New Open Dialog)

**•** `101` (Email Transport Type)

**•** `102` (Pinned Wave Folders)

**•** `108` (Density)

**•** `109` (Lightning Flow Builder)

**•** `111` (Format with Tabs)

**•** `112` (Format Tab Width)

**•** `113` (Format Print Width)

**•** `114` (Record Page Activities Display)

**•** `118` (Lightning Flow Explorer)


Standard Objects UserPreference

**Field** **Details**

**•** `119` (For internal use only)

**•** `120` (Simple Auth Option)

**•** `122` (Sales Alert Notifications Snooze Time)

**•** `131` (Color Scheme)

`Event Reminder Default Lead Time` and `Task Reminder Default`
`Time` are related to these fields on the User object:

**•** `UserPreferencesEventRemindersCheckboxDefault`

**•** `UserPreferencesTaskRemindersCheckboxDefault`

**•** `UserPreferencesSuppressEventSFXReminders`

**•** `UserPreferencesSuppressTaskSFXReminders`

`Enable New Open Dialog` is reserved for future use.

When creating SOQL queries, `tolabel` is required to return accurate results. For example,

```
                   select Id, tolabel(Preference), Value, UserId from
```

`UserPreference` .

`108` (Density) is available in API v44.0 and later.

```
UserId

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user associated with this role. The corresponding field label is **User ID** .

Admin users can create and edit preferences for other users.

Standard users can delete their own preferences only. For a standard user, the value of the
`UserId` field must be their own UserId.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The value of the user preference. For `Event Reminder Default Lead Time`, the
values are increasing intervals of time from 0 minutes to 2 days. For `Task Reminder`
`Default Time`, the values are half-hours from 12:00 AM to 11:30 PM. To view the
respective sets of values, access the Reminders in your personal settings in the online
application.


### Standard Objects UserProfile

Usage

Use this object to query the set of currently configured user preferences in your organization. In your client application, you can query
the User object to obtain valid User IDs to access the UserPreference object.

All users can invoke the supported calls with this object. Standard users can invoke these calls, but only on their own preferences.

### UserProfile

Represents a Chatter user profile.

Note: This object has been deprecated as of API version 32.0. Use the User object to query information about a user in API version
32.0 and later.

Supported Calls

`describeLayout()`, `query()`, `retrieve()`

Special Access Rules

**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** Any fields that have been restricted in visibility will be returned empty, whether or not they are, and will not be removed from the
field listing.

Fields

**Field** **Details**

```
AboutMe

```

`Address` (beta)

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Information about the user, such as areas of interest or skills.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects UserProfile

**Field** **Details**

**Description**
The compound form of the address. Read-only. See Address
Compound Fields for details on compound address fields.

```
City

CompanyName

Country

Email

Fax

FirstName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company associated with the user profile.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country associated with the user profile.

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address associated with the user profile.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The fax number associated with the user profile.

**Type**
string


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s first name.

```
FullPhotoUrl

IsActive

IsBadged

LastName

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo if Chatter is enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has access to log in ( `true` ) or not
( `false` ). You can modify a User's active status from the user interface
or via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is visually badged ( `true` ) or not ( `false` ).
Users of the same Chatter user type (internal, external) are badged.
Different user types are not badged.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s last name.


Standard Objects UserProfile

**Field** **Details**

`Latitude` (beta)

`Longitude` (beta)

```
ManagerId

MobilePhone

Name

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who manages this user.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s mobile or cellular phone number.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` .


Standard Objects UserProfile

**Field** **Details**

```
Phone

PostalCode

SmallPhotoUrl

State

Street

Title

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s phone number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s postal or ZIP code. Label is **Zip/Postal Code** .

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo if Chatter is
enabled.

The URL is updated every time a photo is uploaded and reflects the
most recent photo. If a newer photo is uploaded, the URL returned
for an older photo isn’t guaranteed to return a photo. Query this field
for the URL of the most recent photo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state associated with the user profile.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address associated with the user profile.

**Type**
string


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s business title, such as “Vice President.”

```
UserPreferencesActivityRemindersPopup

UserPreferencesApexPagesDeveloperMode

UserPreferencesDisableAllFeedsEmail

UserPreferencesDisableBookmarkEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder window automatically opens when an
activity reminder is due. Corresponds to the `Trigger alert`
`when reminder comes due` checkbox at the Reminders
page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, indicates that the user has enabled developer mode
for editing Visualforce pages and controllers.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email for all updates
to Chatter feeds, based on the types of feed emails and digests the
user has enabled.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a Chatter feed item after the user has
bookmarked it.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableChangeCommentEmail

UserPreferencesDisableEndorsementEmail

UserPreferencesDisableFeedbackEmail

UserPreferencesDisableFileShareNotificationsForApi

UserPreferencesDisableFollowersEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a change the user has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the member automatically receives email every time
someone endorses them for a topic.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives emails related to WDC
feedback. This includes when someone requests or offers feedback,
shares feedback with the user, or reminds the user to answer a
feedback request.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, email notifications are sent from the person who
shared the file to the users that the file is shared with.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone starts following the user in Chatter.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableLaterCommentEmail

UserPreferencesDisableLikeEmail

UserPreferencesDisableMentionsPostEmail

UserPreferencesDisableMessageEmail

UserPreferencesDisableProfilePostEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a feed item after the user has commented
on the feed item.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone likes their post or comment.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
they’re mentioned in posts.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email for Chatter
messages sent to the user.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone posts to the user’s profile.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesDisableRewardEmail

UserPreferencesDisableSharePostEmail

UserPreferencesDisableWorkEmail

UserPreferencesDisCommentAfterLikeEmail

UserPreferencesDisMentionsCommentEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives emails related to WDC
rewards. This includes when someone someone gives a reward to
the user.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time their
post is shared.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user receives emails related to WDC feedback,
goals, and coaching. The user must also sign up for individual emails
listed on the WDC email settings page. When `true`, the user will
not receive any emails related to WDC feedback, goals, or coaching
even if they are signed up for individual emails.

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on a post that the user liked.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
When `false`, the user automatically receives email every time the
user is mentioned in comments.

```
UserPreferencesDisProfPostCommentEmail

UserPreferencesEnableAutoSubForFeeds

UserPreferencesEventRemindersCheckboxDefault

UserPreferencesHideChatterOnboardingSplash

UserPreferencesHideCSNDesktopTask

```

**Type**
boolean

**Properties**
Filter

**Description**
When `false`, the user automatically receives email every time
someone comments on posts on the user’s profile.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the user automatically subscribes to feeds for any
objects that the user creates.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder popup is automatically set on the user's
events. Corresponds to the `By default, set reminder`
`on Events to...` checkbox on the Reminders page in the
user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the initial Chatter onboarding prompts do not appear.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
When `true`, the Chatter recommendations panel never displays
the recommendation to install Chatter Desktop.

```
UserPreferencesHideCSNGetChatterMobileTask

UserPreferencesHideS1BrowserUI

UserPreferencesHideSecondChatterOnboardingSplash

UserPreferencesReminderSoundOff

UserPreferencesShowCityToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the Chatter recommendations panel never displays
the recommendation to install Chatter Mobile.

**Type**
boolean

**Properties**
Filter

**Description**
Controls the interface that the user sees when logging in to Salesforce
from a supported mobile browser. If `false`, the user is automatically
redirected to the Salesforce mobile web. If `true`, the user sees the
full Salesforce site. The default value is `false` . Label is **Salesforce**
**User** .This field is available in API version 29.0 or later.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the secondary Chatter onboarding prompts do not
appear.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a sound automatically plays when an activity reminder
is due. Corresponds to the `Play a reminder sound`
checkbox on the Reminders page in the user interface.

**Type**
boolean


Standard Objects UserProfile

**Field** **Details**

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
City is visible only to internal members of the user’s organization
when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

City is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowCityToGuestUsers` is `true`,
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

```
UserPreferencesShowCityToGuestUsers

UserPreferencesShowCountryToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the city field in the user’s contact information.
When `true`, city is visible to guest users. Guest users can access
public Site.com and Salesforce sites, and public pages in Experience
Cloud sites, via the Guest User license associated with each site. When
`false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCityToExternalUsers`, making
the user’s city visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. Country is visible only to internal members of the user’s
organization when:


Standard Objects UserProfile

**Field** **Details**

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Country is visible to external members in an Experience Cloud site
when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowCountryToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

```
UserPreferencesShowCountryToGuestUsers

UserPreferencesShowEmailToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the country field in the user’s contact
information. When `true`, country is visible to guest users. Guest
users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated
with each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowCountryToExternalUsers`,
making the user’s country visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the email address field in the user’s contact
information. Email address is visible only to internal members of the
user’s organization when this field is `false` . Email address is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesShowFaxToExternalUsers

UserPreferencesShowManagerToExternalUsers

UserPreferencesShowMobilePhoneToExternalUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the fax number field in the user’s contact
information. Fax number is visible only to internal members of the
user’s organization when this field is `false` . Fax number is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the manager field in the user’s contact
information. Manager is visible only to internal members of the user’s
organization when this field is `false` . Manager is visible to external
members in an Experience Cloud site when this field is `true` .
External users are users with Community, Customer Portal, or partner
portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the mobile device number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false` . The number is
visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer
Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.


Standard Objects UserProfile

**Field** **Details**

```
UserPreferencesShowPostalCodeToExternalUsers

UserPreferencesShowPostalCodeToGuestUsers

UserPreferencesShowProfilePicToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. Postal code is visible only to internal members
of the user’s organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Postal code is visible to external members in an Experience Cloud
site when:

**•** This field is `true`, or

**•** This field is `false` but

```
   UserPreferencesShowPostalCodeToGuestUsers
```

is `true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `false` . This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s
contact information. When `true`, postal code is visible to guest
users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license
associated with each site. When `false`, this field returns the value
`#N/A` .

When `true`, this field overrides the value `false` in
`UserPreferencesShowPostalCodeToExternalUsers`,
making the user’s postal code visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
Indicates the visibility of the user’s profile photo. When `true`, the
photo is visible to guest users in an Experience Cloud site. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site.

When `false`, this field returns the stock photo. The default value
is `false` . This field is available in API version 28.0 and later.

```
UserPreferencesShowStateToExternalUsers

UserPreferencesShowStateToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. State is visible only to internal members of the user’s
organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

State is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowStateToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the state field in the user’s contact
information. When `true`, state is visible to guest users. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowStateToExternalUsers, making the user’s state
visible to external members.


Standard Objects UserProfile

**Field** **Details**

The default value is `false` . This field is available in API version 28.0
and later.

```
UserPreferencesShowStreetAddressToExternalUsers

UserPreferencesShowTitleToExternalUsers

UserPreferencesShowTitleToGuestUsers

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the street address field in the user’s contact
information. The address is visible only to internal members of the
user’s organization when this field is `false` . The address is visible
to external members in an Experience Cloud site when this field is
`true` . External users are users with Community, Customer Portal,
or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the business title field in the user’s contact
information. Title is visible only to internal members of the user’s
organization when:

**•** This field is `false` . When `false`, this field returns the value
`#N/A` .

Title is visible to external members in an Experience Cloud site when:

**•** This field is `true`, or

**•** This field is `false` but
`UserPreferencesShowTitleToGuestUsers` is
`true`, which overrides this field’s value.

External users are users with Community, Customer Portal, or partner
portal licenses.

The default value is `true` . This field is available in API version 26.0
and later.

**Type**
boolean

**Properties**
Filter


Standard Objects UserProfile

**Field** **Details**

**Description**
Indicates the visibility of the business title field in the user’s contact
information. When `true`, title is visible to guest users. Guest users
can access public Site.com and Salesforce sites, and public pages in
Experience Cloud sites, via the Guest User license associated with
each site. When `false`, this field returns the value `#N/A` .

When `true`, this field overrides the value `false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title
visible to external members.

The default value is `false` . This field is available in API version 28.0
and later.

```
UserPreferencesShowWorkPhoneToExternalUsers

UserPreferencesTaskRemindersCheckboxDefault

```

Usage

**Type**
boolean

**Properties**
Filter

**Description**
Indicates the visibility of the work phone number field in the user’s
contact information. The number is visible only to internal members
of the user’s organization when this field is `false` . The number is
visible to external members in an Experience Cloud site when this
field is `true` . External users are users with Community, Customer
Portal, or partner portal licenses.

When `false`, this field returns the value `#N/A` . The default value
is `false` . This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, a reminder popup is automatically set on the user's
tasks. Corresponds to the `By default, set reminder on`
`Tasks to...` checkbox on the Reminders page in the user
interface. This field is related to UserPreference and customizing
activity reminders.

Use this object to query Chatter—related information about the user. While the User object contains all the information about a user
and is historically tied to user management, UserProfile is a read-only entity that contains the information that is relevant in a Chatter
context.


### Standard Objects UserProvAccount

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserProfileFeed (API version 18.0–26.0)**
Feed tracking is available for the object.

### UserProvAccount

Represents information that links a Salesforce user account with an account in a third-party (target) system, such as Google, for users of
connected apps with Salesforce user provisioning enabled. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConnectedAppId

DeletedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The 15 character application ID.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the associated user account in the target system was deleted. This
value is automatically updated during the provisioning and reconciling processes.


Standard Objects UserProvAccount

**Field** **Details**

```
ExternalEmail

ExternalFirstName

ExternalLastName

ExternalUserId

ExternalUsername

IsKnownLink

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The username as stored in the target system for the associated user account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects UserProvAccount

**Field** **Details**

**Description**
Setting the `IsKnownLink` value to `true` implies the administrator or another user is
managing the relationship between the Salesforce user account and the third-party user
account, manually. This field helps Salesforce coordinate updates between the
UserProvAccountStaging object and the UserProvAccount object while committing staged
accounts. Typically, for a matching user account (the same `ExternalUserId` for both
objects), Salesforce copies the values from the UserProvAccountStaging object to the
UserProvAccount object.

However, if Salesforce encounters a UserProvAccountStaging object with a matching
`ExternalUserId` but different `LinkState` and `SalesforceUserId` values
during this process, Salesforce checks the UserProvAccount `IsKnownLink` value. If the
`IsKnownLink` value is `true`, Salesforce doesn’t copy the `LinkState` and
`SalesforceUserId` values from the UserProvAccountStaging object to the
UserProvAccount object (all other values are copied).

The default is `false`, meaning Salesforce manages the account relationship.

```
LinkState

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce organization
and the associated user account in the target system. The valid values are:

**•** `linked`  - changes to the account in the Salesforce organization are queued to be
updated for the associated user account in the target system.

**•** `duplicate`  - an associated account in the target system exists.

**•** `orphaned` —no associated account exists in the target system.

**•** `ignored`  - changes to the account in the Salesforce organization have no effect on
the associated user account in the target system.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Namepointing, Sort, Update


### Standard Objects UserProvAccountStaging

**Field** **Details**

**Description**
The user ID of the owner of this object—typically a Salesforce administrator.

```
SalesforceUserId

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID for the user account in the Salesforce organization that is associated with the
user account in the target system.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
### User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the account in the target system. The valid values are:

**•** `Active`

**•** `Deactivated`

**•** `Deleted`

### UserProvAccountStaging

Temporarily stores user account information while a user completes the User Provisioning Wizard. This information that is stored in the
UserProvAccount object when you click the button to collect and analyze accounts on the target system.

User provisioning links a Salesforce user account with an account in a third-party (target) system. To configure user provisioning, you
use a User Provisioning Wizard that guides you through the setup process. As you enter values about account details in the wizard, these
values are stored in this object until you click the button to collect and analyze accounts on the target system. The general user provisioning
configuration details are stored in the UserProvisioningConfig object.


Standard Objects UserProvAccountStaging

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ConnectedAppId

ExternalEmail

ExternalFirstName

ExternalLastName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15 character connected app ID.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvAccountStaging

**Field Name** **Details**

**Description**

The last name as stored in the target system for the associated user account.

```
ExternalUserId

ExternalUsername

LinkState

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce
organization and the associated user account in the target system. The valid
values are:

**•** `linked`  - a user account matches one in the target system.

**•** `duplicate`  - an associated account in the target system exists.

**•** `orphaned` —no associated account exists in the target system.

**•** `ignored`  - changes to the account in the Salesforce organization have
no effect on the associated user account in the target system.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The unique name for this object.

**Type**
reference


Standard Objects UserProvAccountStaging

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.

```
SalesforceUserId

Status

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user ID for the user account in the Salesforce organization that is associated
with the user account in the target system.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the account in the target system. The valid values are:

**•** `Active`

**•** `Deactivated`

**•** `Deleted`

When committing fields from a UserProvAccountStaging to a UserProvAccount object, Salesforce looks up the UserProvAccount record
where `UserProvAccountStaging.ExternalUserId = UserProvAccount.ExternalUserId` .

**•** If an `ExternalUserId` doesn't match an existing account, Salesforce creates a UserProvAccount record based on the
UserProvAccountStaging record.

**•** If an `ExternalUserId` matches, then Salesforce checks the `UserProvAccount.isKnownLink` value, and does the
following.

**–** If `UserProvAccount.IsKnownLink = true`, Salesforce copies the UserProvAccountStaging values to the
UserProvAccount object, except for the `ExternalUserId` and `LinkState` values.


### Standard Objects UserProvMockTarget

**–** If `UserProvAccount.IsKnownLink = false`, Salesforce copies all of the UserProvAccountStaging values to the
UserProvAccount object.

### UserProvMockTarget

Represents an entity for testing user data before committing the data to a third-party system for user provisioning.

During the user provisioning process, user account information is sent to a third-party system to create, update or delete a user account
on that system. While configuring user provisioning for your organization using a flow or Apex action, you can use this object to confirm
the associated flow or Apex code is sending the desired data. After confirming the correct fields and values, you can update the flow or
Apex action to send the data to the target system.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ExternalEmail

ExternalFirstName

ExternalLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The last name as stored in the target system for the associated user account.


### Standard Objects UserProvisioningConfig

**Field Name** **Details**

```
ExternalUserId

ExternalUsername

Name

OwnerId

### UserProvisioningConfig

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.

Represents information for a flow to use during a user provisioning request process, such as the attributes for an update. This object is
available in API version 34.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects UserProvisioningConfig

Fields

**Field Name** **Details**

```
ApprovalRequired

ConnectedAppId

DeveloperName

Enabled

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Denotes whether approvals are required for provisioning users for the associated
connected app. If the value is null, no approval is required.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 18-digit application ID for the connected app.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean


Standard Objects UserProvisioningConfig

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether user provisioning is enabled for the associated connected app
( `true` ) or not ( `false` ).

```
EnabledOperations

Language

LastReconDateTime

MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the operations, as comma-separated values, that create a
UserProvisioningRequest object for the associated connected app. Allowed values
are:

**•** `Create`

**•** `Update`

**•** `EnableAndDisable` (activation and deactivation)

**•** `SuspendAndRestore` (freeze and unfreeze)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The two- to five-character code that represents the language and locale ISO. This
code controls the language for labels displayed in an application.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The date and time when user accounts were last reconciled between Salesforce
and the target system.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects UserProvisioningConfig

**Field Name** **Details**

**Description**

The primary label for this object. This value is the internal label that doesn’t get
translated.

```
NamedCredentialId

NamespacePrefix

Notes

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the named credential that’s used for a request. The named
credential identifies the third-party system and the third-party authentication
settings.

This is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
textarea


### Standard Objects UserProvisioningLog

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**

A utility field for administrators to add any additional information about the
configuration. This field is for internal reference only, and is not used by any
process.

```
OnUpdateAttributes

ReconFilter

UserAccountMapping

### UserProvisioningLog

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the user attributes, as comma-separated values, that generate a
UserProvisioningRequest object during an update.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When collecting and analyzing users on a third-party system, the plug-in uses
this filter to limit the scope of the collection.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Stores the attributes used to link the Salesforce user to the account on the
third-party system, in JSON format.

For example:

```
  {"linkingSalesforceUserAttribute":"Username",

  "linkingTargetUserAttribute":"Email"}

```

Represents messages generated during the process of provisioning users for third-party applications. This object is available in API version
33.0 and later.


Standard Objects UserProvisioningLog

Some messages for this object are generated automatically by Salesforce, and others are created by the developers of the user provisioning
plugin. Developers can use this object to log messages from the flow associated with the user provisioning process or the Apex plugin
that calls the target system. Administrators can use this object as a log of all user provisioning activity and as a troubleshooting tool if
desired behavior is missing. This object is available as a custom report type.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Details

ExternalUserId

ExternalUsername

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value of this field depends on the log entry. For example, if the target system returns an
error, the error message may be recorded in this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username set in the target system for the associated user account.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.

**Type**
reference


Standard Objects UserProvisioningLog

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce ID of the Group or User who owns this object.

```
Status

UserId

UserProvisioningRequestId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the user provisioning request. Based on the context of the log, it can contain
different values, such as an HttpStatusCode.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the user making the request.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the user provisioning request.

This is a relationship field.

**Relationship Name**
UserProvisioningRequest

**Relationship Type**
Lookup

**Refers To**
UserProvisioningRequest


### Standard Objects UserProvisioningRequest UserProvisioningRequest

Represents an individual provisioning request to create, update, or delete a single user account in a third-party service system (or another
Salesforce organization). This object is available in API version 33.0 and later.

A UserProvisioningRequest (UPR) record is created for each provisioning action for each user, and for each connected app available to
the user. For example, if a user has two connected apps, and a provisioning request is sent to two different services to create an account
for the user, Salesforce creates two UPR objects. Provisioning actions include creating, updating, or deleting a user account.

Supported Calls

`create()`, `delete()`,
`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppName

ApprovalStatus

ConnectedAppId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique name of the connected app associated with the service provider.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the approval for the current request. If the user provisioning setup for the
connected app does not have an approval process enabled, the status is `Not Required` .
If an approval process is enabled, supported values are:

**•** `Required`  - An approval process is enabled in the user provisioning setup for the
associated connected app, but there is no response to the request yet.

**•** `Not Required`  - An approval process is not enabled in the user provisioning setup
for the associated connected app.

**•** `Approved`

**•** `Denied`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvisioningRequest

**Field** **Details**

**Description**

The 18-digit application ID for the connected app.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

```
ExternalUserId

ManagerId

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user in the target system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Salesforce ID of the user who manages the user specified in the `SalesforceUserId`
field. If an approval process is configured for the user provisioning request. this value allows
the manager to approve the request. Available in API version 34.0 and later.

This is a relationship field.

**Relationship Name**
Manager

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.


Standard Objects UserProvisioningRequest

**Field** **Details**

```
Operation

OwnerId

ParentID

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The Apex method called by the trigger associated with the provisioning request (typically a
change to the User object). Supported values are:

**•** `Create`

**•** `Read`

**•** `Update`

**•** `Deactivate`

**•** `Activate`

**•** `Freeze`

**•** `Unfreeze`

**•** `Reconcile`

**•** `Linking`

For example, when the User object field `isActive` is set to `false`, the UPR object
`Operation` field value is set to `Deactivate` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce ID of the Group or User who owns this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
When a retry event is created, the failed UPR is cloned and resubmitted. This field contains
a lookup to the failed UPR that was cloned to create the current record.


Standard Objects UserProvisioningRequest

**Field** **Details**

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
UserProvisioningRequest

```
Retry Count

SalesforceUserId

ScheduleDate

State

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of retry attempts performed on a UPR. Retry Count enables custom business logic
such as “Retry 5 times then stop and notify your admin.”

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the user making the request.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
When to send this request to the service provider.

Note: Scheduling is not implemented yet. Currently, provisioning changes are queued
immediately to be sent to the service provider.

**Type**
picklist


Standard Objects UserProvisioningRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of this request. Supported values are:

**•** `New`

**•** `Requested`

**•** `Completed`

**•** `Failed`

**•** `Collecting`

**•** `Collected`

**•** `Analyzing`

**•** `Analyzed`

**•** `Committing`

**•** `Retried`

**•** `Manually Completed`

The `State` goes from `New` to `Requested` to `Completed` or `Failed`, unless a
reconciliation process is occurring. For details about the reconciliation process `State` value
changes, see Usage.

The `State` goes from `Failed` to `Retried` or `Manually Completed` when
troubleshooting UPR failures. For details about handling failures, see State Values for Managing
Provisioning Failures.

```
UserProvAccountId

UserProvConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID value of the associated UserProvAccount object.

This is a relationship field.

**Relationship Name**
UserProvAccount

**Relationship Type**
Lookup

**Refers To**
UserProvAccount

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects UserProvisioningRequest

**Field** **Details**

**Description**

The ID value of the associated UserProvisioningConfig object. Available in API version 34.0
and later.

This is a relationship field.

**Relationship Name**
UserProvConfig

**Relationship Type**
Lookup

**Refers To**
UserProvisioningConfig

Usage

The `State` value changes during a reconciliation process ( `Operation = Reconcile` ) to gather and compare users on the
third-party system to Salesforce users. Typically, when a UPR entry is first created, it has a `State` value of `New` . When a collection
process is triggered, the `State` transitions to `Collecting` until that process is finished and the `State` is `Collected` . When
an analyze process is triggered, the `State` transitions to `Analyzing` until that process is finished and the `State` is `Analyzed` .
If a process commits the request, the `State` then transitions to `Committing`, and the properties move from the
UserProvAccountStaging object to the UserProvAccount object. When those properties are saved in the UserProvAccount object, the
`State` transitions to `Completed` .

However, the `State` does not necessarily start at `New` . For example, UserProvAccountStaging entries can be inserted programmatically.
If a process is initiated that triggers linking these rows to accounts on the third-party service, a UPR entry could start with the `Analyzing`
`State` .

Also, the `State` cannot go backwards from an active task. For example, a successful `AnalyzingState` must progress to `Analyzed` ;
unless the active process fails, and then the `State` must change to `Failed` . Certain `State` transitions cannot be made
programmatically and must be triggered by Salesforce.

The following table shows the `State` transitions that can occur for each `State` value. Each row corresponds to a current `State`
value and each column corresponds to a new `State` after a potential transition.

**•**   - the transition to this value is not allowed.

**•**   - the transition to this value is allowed.

**•**   - only Salesforce can transition the `State` to this value.


### Standard Objects UserRecordAccess

State Values for Managing Provisioning Failures

The `state` value changes to `Failed` for several reasons, such as network outages, session timeouts, permissions issues, and record
locks. The `Failed` state can transition to either `Retried` or `Manually Completed` to indicate what action was taken to
address the failure. Actions can include correcting the root cause of the failure and requesting that the provisioning engine retry the
UPR. Or, it can be completing the action against the target manually. Each UPR is an independent transaction and it’s possible the retry
causes a failure with a different root cause. So it’s hard to distinguish failed events that you addressed from the ones that require more
action.

If you tried to correct the cause of the failure and requested the provisioning engine to retry the UPR, you can mark the failed UPR
`Retried` . Or, if the action against the target was completed manually, you can mark it `Manually Completed` .

When a retry event is created, the failed UPR is cloned, and resubmitted. The `ParentID` field contains a lookup to the failed UPR to
use to clone the new UPR. The `Retry Count` field contains the number of retry attempts that were performed on a UPR. With the
`Retry Count` field, you can add custom business logic like "Retry 5 times then stop and notify your admin."

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserProvisioningRequestOwnerSharingRule (API version 34.0)**
Sharing rules are available for the object.

**UserProvisioningRequestShare (API version 34.0)**
Sharing is available for the object.

### UserRecordAccess

Represents a user’s access to a set of records. This object is read only and is available in API version 24.0 and later. This object doesn’t
consider whether a user’s access is blocked by a restriction rule.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects UserRecordAccess

Fields

**Field** **Details**

```
HasAllAccess

HasDeleteAccess

HasEditAccess

HasTransferAccess

HasReadAccess

MaxAccessLevel

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user can share the record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has delete access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has edit access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has transfer access to the record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has read access to the record ( `true` ) or not ( `false` ).

**Type**
picklist

**Properties**
Group, Nillable, Restricted picklist, Sort


Standard Objects UserRecordAccess

**Field** **Details**

**Description**
Indicates a user’s maximum level of access to a record.

Valid values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `Delete`

**•** `Transfer`

**•** `All`

```
RecordId

UserId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
ID of the record.

**Type**
reference

**Properties**
Filter, Group

**Description**
ID of the user.

Use this object to query a user’s access to records. You can only query records of objects listed on the Sharing Settings Setup page. You
can’t create, delete, or update any records using this object.

[Note: UserRecordAccess doesn’t consider whether a user’s access is blocked due to a restriction rule. If a user’s access is blocked](https://developer.salesforce.com/docs/atlas.en-us.260.0.restriction_rules.meta/restriction_rules/restriction_rules_about.htm)
even though query results state that they should have access, check to see if a restriction rule on the object prevents the user’s
access.

Up to 200 record IDs can be queried. You can include an `ORDER BY` clause for any field that is being selected in the query.

The following sample query returns the records, whether the queried user has read and transfer access to each record, and the user’s
maximum access level to each record.

```
SELECT RecordId, HasReadAccess, HasTransferAccess, MaxAccessLevel

   FROM UserRecordAccess

   WHERE UserId = [single ID]

   AND RecordId = [single ID] //or Record IN [list of IDs]

```


### Standard Objects UserRelatedRecordContent

The following query returns the records to which a queried user has read access.

```
   SELECT RecordId

      FROM UserRecordAccess

      WHERE UserId = [single ID]

      AND RecordId = [single ID] //or Record IN [list of IDs]

      AND HasReadAccess = true

```

Using API version 30.0 and later, UserRecordAccess is a foreign key on the records. You can’t filter by or provide the `UserId` or
`RecordId` fields when using this object as a lookup or foreign key. The previous sample queries can be run as:

```
   SELECT Id, Name, UserRecordAccess.HasReadAccess, UserRecordAccess.HasTransferAccess,

   UserRecordAccess.MaxAccessLevel

       FROM Account

   SELECT Id, Name, UserRecordAccess.HasReadAccess

       FROM Account

```

SOQL restrictions:

**•** When the running user is querying a user's access to a set of records, records that the running user doesn’t have read access to are
filtered out of the results.

**•** When filtering by `UserId` and `RecordId` only, you must use `SELECT RecordId` and optionally one or more of the access
level fields: `HasReadAccess`, `HasEditAccess`, `HasDeleteAccess`, `HasTransferAccess`, and `HasAllAccess` .
You can include `MaxAccessLevel` .

**•** When filtering by `UserId`, `RecordId`, and an access level field, you must use `SELECT RecordId` only.

SEE ALSO:

_Developer Guide_ [: Restriction Rules](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

### UserRelatedRecordContent

Represents the link between a managed content record, an account, event, or opportunity record, and a user record. This object is
reserved for future use.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContentOwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserRole

**Field** **Details**

**Description**
The user who owns the managed content record associated with the given account, event,
or opportunity record.

This field is a relationship field.

**Relationship Name**
ContentOwner

**Refers To**
### User

```
ManagedContentId

RelatedRecordId

### UserRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the managed content record created for the associated Salesforce record. One
unique managed content record is created per account, event, or opportunity record per
user.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Refers To**
ManagedContent

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Salesforce record (e.g., account, opportunity, or event) associated with the
managed content record.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Refers To**
Account, Event, Opportunity

Represents a user role in your organization.


Standard Objects UserRole

Note: This object was called “Role” in previous versions of the API documentation.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with the View Roles and Role Hierarchy permission can access this object, and only users with
the Manage Roles permission can edit this object.

Fields

**Field** **Details**

```
CaseAccessForAccountOwner

ContactAccessForAccountOwner

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The case access level for the account owner.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The contact access level for the account owner.

Note: When `DefaultContactAccess` is set to `Controlled`
`by Parent`, you can’t create or update this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org.
It must begin with a letter, not include spaces, not end with an underscore,
and not contain two consecutive underscores. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the


Standard Objects UserRole

**Field** **Details**

changes are reflected in a subscriber’s organization. Corresponds to **Role**
**Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one
for each record.

```
ForecastUserId

IsPartner

MayForecastManagerShare

Name

OpportunityAccessForAccountOwner

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the forecast manager associated with this role. Label is **User ID** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user role is a partner who has access to the partner
portal ( `true` ) or not ( `false` ). This field is not available for release 9.0 and
later. Instead, use `PortalType` with the value `Partner` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecast manager can manually share their own
forecast.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the role. Corresponds to **Label** on the user interface.

**Type**
picklist


Standard Objects UserRole

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The opportunity access level for the account owner. Note that you
can’t set a user role with an opportunity access less than that specified in
organization-wide defaults.

```
ParentRoleId

PortalAccountId

PortalAccountOwnerId

PortalRole

PortalType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent role.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account. This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account’s owner. This field is read-only.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The portal role: Executive, Manager, User, or PersonAccount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This value indicates the type of portal for the role:


### Standard Objects UserServicePresence

**Field** **Details**

**•** None: Salesforce application role.

**•** CustomerPortal: Customer portal role.

**•** Partner: partner portal role. The field `IsPartner` used in release 8.0
will map to this value.

This field replaces `IsPartner` beginning with release 9.0.

```
 RollupDescription

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the forecast rollup. Label is **Description** .

Use this object to query the set of currently configured user roles in your organization. Use it in your client application to obtain valid
UserRole IDs to use when querying or modifying a User record.

Users with the View Roles and Role Hierarchy permission can query or describe this object. If your client application logs in with the
“Manage Users” permission, it can query, create, update, or delete UserRole records.

Note: You can’t update any field for a portal role.

For example, the following code finds all roles that are not assigned to any users.

```
SELECT Id, Name, DeveloperName

FROM UserRole

WHERE Id NOT IN (SELECT UserRoleId

           FROM User

           WHERE UserRoleId !='000000000000000')

```

SEE ALSO:

Overview of Salesforce Objects and Fields

### UserServicePresence

Represents a presence user’s real-time presence status. This object is available in API version 32.0 and later.

Supported Calls

`delete()`, `query()`, `getDeleted()`, `getUpdated()`, `retrieve()`, `undelete()`


Standard Objects UserServicePresence

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AtCapacityDuration

AverageCapacity

ConfiguredCapacity

ConfiguredInterruptCapacity

IdleDuration

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is at full capacity. This field is updated when the agent’s capacity
changes, such as when the agent is assigned, declines, or closes a work item. Available in
API versions 34.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The user’s average capacity. This field is updated when the agent’s capacity changes, such
as when the agent is assigned, declines, or closes a work item. Available in API versions 34.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured primary capacity.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured interruptible capacity. Available in version 57.0 and later when
the Interruptible Capacity feature is enabled.

**Type**
int


Standard Objects UserServicePresence

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is idle. This field is updated when the agent’s capacity changes,
such as when the agent is assigned, declines, or closes a work item. Available in API versions
34.0 and later.

```
IsAway

IsCurrentState

Name

OwnerId

ServicePresenceStatusId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user’s status is `Away` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a presence status is the user’s current state. If `true`, the agent is in that
presence status. Available in API versions 34.0 and later.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the `UserServicePresence` entity. For external routing, allows
the entity to be used in the Streaming API to listen to events whenever a
`UserServicePresence` record is created, modified, or deleted.

**Type**
reference


Standard Objects UserServicePresence

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The ID of the presence status that’s associated with the presence user that’s specified by the
`UserId` .

```
StatusDuration

StatusEndDate

StatusStartDate

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

This field is a calculated field: StatusEndDate - StatusStartDate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date of the user service presence status. Available in API versions 34.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Omni-Channel user.


### Standard Objects UserSetupEntityAccess

Usage

Apex triggers aren’t supported with `UserServicePresence` .

In API version 41.0 or later, `UserServicePresence` records can be deleted programmatically. The Customize Application permission
is required.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserServicePresenceChangeEvent (API version 62.0)**
Change events are available for the object.

**UserServicePresenceOwnerSharingRule**

Sharing rules are available for the object.

**UserServicePresenceShare**

Sharing is available for the object.

### UserSetupEntityAccess

Represents the enabled custom permissions of the running user. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DeveloperName

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the custom permission in the API.

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects UserSetupEntityAccess

**Field** **Details**

**Description**
This field isn't used.

```
KeyPrefix

LastCacheUpdate

NamespacePrefix

SetupEntityId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first 3 characters of the `SetupEntityId` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of the running user's info.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that’s associated with the custom permission. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the custom permission assigned to the user.


### Standard Objects UserShare

Usage

API users without the View Setup and Configuration permission can use this object to check their assigned custom permissions.

### UserShare

Represents a sharing entry on a user record. This object is available in API version 26.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only standard users or users with the Customize Application permission can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
IsActive

RowCause

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the User has access to log in ( `true` ) or not ( `false` ).
You can modify a User's active status from the user interface or via the API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .


Standard Objects UserShare

**Field** **Details**

All other `RowCause` values are read-only. After the sharing entry is created, this
field can’t be edited.

Possible values include:

**•** `Manual` —The User or Group has access to the user record because a User with
“All” access manually shared the User with them.

**•** `Rule` —The User or Group has access to the user record via a User sharing rule.

**•** `GuestRule` —The User or Group has access via a User guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

```
UserAccessLevel

UserId

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the specified user. The specified user is
denoted by the `UserId` . The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s
default `UserAccessLevel` .

`UserAccessLevel` can be updated only if `RowCause` is set to `Manual`
`Sharing` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User being shared.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


### Standard Objects UserSharedFeature

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the User. This field can’t be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit User records owned by other users.

### UserSharedFeature

For internal use only.

### UserTeamMember

Represents a single User on the default opportunity team of another User.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** This object is available only in organizations that have enabled the team selling functionality.

**•** Customer Portal users can’t access this object.


Standard Objects UserTeamMember

Fields

**Field** **Details**

```
OpportunityAccessLevel

OwnerId

TeamMemberRole

UserId

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the team member has to opportunities for which the user has
added his or her default opportunity team. The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default access
level for opportunities.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default opportunity team. This field can’t be updated.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the User has added his or her
default opportunity team. The valid values are set by the organization’s administrator in the
Opportunity Team Roles picklist. Label is **Team Role** .

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default opportunity team. This field can’t
be updated.


### Standard Objects UserTerritory

Usage

If you attempt to create a record that matches an existing record, the create request updates any modified fields and returns the existing
record.

Users can set up their default opportunity team to include other users that typically work with them on opportunities.

SEE ALSO:

OpportunityTeamMember

### UserTerritory

Represents a User who has been assigned to a Territory.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** Only available if territory management has been enabled for your organization.

**•** As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with
the Manage Territories permission can edit this object.

Fields

**Field** **Details**

```
IsActive

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is active in the given territory ( `true` ), or inactive in the
given territory ( `false` ):

**•** Users who are active in a territory are explicitly assigned to the territory and can
have open opportunities, closed opportunities, or no opportunities associated
with that territory.

**•** Users who are inactive in a territory are not explicitly assigned to the territory, but
own an open or closed opportunity that is associated with the territory. For
example, a user may have been transferred out of a territory, but still own
opportunities in his or her old territory.

Until a user is deleted from a territory (not simply removed from the territory), the
record is not returned in a `getDeleted()` call.


### Standard Objects UniqueQueryEventLog

**Field** **Details**

```
 IsDeleted

TerritoryId

UserId

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the Territory to which the user has been assigned. This field is required when
creating a record in API version 20.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the user. This field is required when creating a record.

If a user is inactive in a territory, and the opportunities they own that are associated with the territory are all closed, the user is not returned
in the Territories related list on the User page in Setup. Regardless of whether the user is inactive or the opportunities are closed, the
user is returned in the Quotas related list.

SEE ALSO:

Territory

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem

### UniqueQueryEventLog

Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This object is available in API version 65.0 and later.


Standard Objects UniqueQueryEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

LoginKey

PlannerIdentifier

QueryIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the bot.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The bot session ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string


Standard Objects UniqueQueryEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The text of the SOQL query run or the Id of the report or list view run.

```
QueryType

RequestIdentifier

SessionKey

SqlIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The input type to the optimizer that was translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier generated for the database query. (Its SQL Id in the ELF);

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.


### Standard Objects UserTerritory2Association UserTerritory2Association

Represents an association (by assignment) between a territory and a user record. Available only if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users based on your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived` ).

Fields

Note: UserTerritory2Association doesn’t support adding custom fields.

**Field Name** **Details**

```
IsActive

RoleInTerritory2

Territory2Id

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is active ( `true` ) or inactive ( `false` ) in the given
territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The role of the user in a territory. Possible values are: Owner, Administrator, Sales
Rep. Label is `Role in Territory` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the user is assigned to.


### Standard Objects UserTerritory2AssocLog

**Field Name** **Details**

```
UserId

### UserTerritory2AssocLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user who is assigned to the territory.

Represents a log of when a user is assigned and unassigned from a territory. This object is available in API version 57.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

To see this object, enable Sales Territory and User Tracking on the Territory Settings page. Activate a territory model to start the tracking.

Fields

**Field** **Details**

```
CurrencyIsoCode

EndDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of currency.

Possible values are:

**•** `EUR` —Euro

**•** `INR` —Indian Rupee

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects UserTerritory2AssocLog

**Field** **Details**

**Description**
Date when the user is unassigned from a territory. If the end date is empty, the user is still
assigned.

```
Name

RoleInTerritory2

StartDate

Territory2Id

Territory2ModelId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Auto-generated unique name of the log.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s role in the territory between the start and end date. The picklist is, by default, empty.
Add values to this field using Object Manager.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the user is assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the territory associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

**Type**
reference


### Standard Objects UserUIPreference

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory model associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model

```
UserId

### UserUIPreference

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user associated with the log.

This field is a relationship field.

**Relationship Name**
### User

**Refers To**
### User

Represents user preferences for Salesforce components. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
AsyncOperationTrackers

```

**Type**
textarea


Standard Objects UserUIPreference

**Field** **Details**

**Properties**
Create, Update

**Description**
Stores a JSON object that maps each quote ID to its asynchronous sales transaction request
details, which includes a tracker ID and the start date. This field is available with Revenue
Cloud in API version 66.0 and later.

```
Name

ObjectScope

PreferenceAttribute

SourceScope

UserId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-generated number for the user preferences. Read-only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the object that the preference applies to. For example, the preference
applies to the Quote object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type of preference.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the component, feature, or product that the preference is for. For example, a
preference for column widths that's associated with the Transaction Line Table component
in Revenue Cloud.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects UserWorkList

**Field** **Details**

**Description**
The user associated with the user preferences.

This field is a relationship field.

**Relationship Name**
### User

**Relationship Type**
Master-detail

**Refers To**
User (the master object)

```
Value

### UserWorkList

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The JSON for the user's preferences.

Represents a list of work items in the My List tab for Sales Engagement users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsActive

ListType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the work list is active or not.

**Type**
picklist


### Standard Objects UserWorkListItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of list, such as a call or email.

```
 Name

 OwnerId

### UserWorkListItem

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work list.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the list.

Represents an individual work item in the My List tab for Sales Engagement users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
PriorityOrder

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order of the item in the list.


### Standard Objects VendorCallCenterStatusMap

**Field** **Details**

```
RelatedRecordId

UserWorkListId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the related record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related work list.

### VendorCallCenterStatusMap

Stores a mapping between a call center vendor agent status and a Salesforce presence status for an associated call center. This object
is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Omni-Channel and Service Cloud Voice must be enabled.

Fields

**Field** **Details**

```
CallCenterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a call center.

This is a relationship field.

**Relationship Name**
CallCenter


### Standard Objects VerificationHistory

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CallCenter

```
ExternalStatus

ServicePresenceStatusId

### VerificationHistory

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Status value to set for the call center vendor agent.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a presence status that can be assigned to a service channel.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

Represents the past six months of your org users’ attempts to verify their identity. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Only users with Manage Users permission can access this object.


Standard Objects VerificationHistory

Fields

**Field Name** **Details**

```
Activity

EventGroup

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action the user attempted that requires identity verification. The label is User
Activity. Available values are:

**•** `AccessReports` —The user attempted to access reports or dashboards.

**•** `Apex` —The user attempted to access a Salesforce resource with a verification
Apex method.

**•** `ChangeEmail` —The user attempted to change an email address.

**•** `ConnectSms` —The user attempted to connect a phone number.

**•** `ConnectToopher` —The user attempted to connect Salesforce
Authenticator.

**•** `ConnectTotp` —The user attempted to connect a one-time password
generator.

**•** `ConnectU2F` —The user attempted to register a U2F security key.

**•** `ConnectWebAuth` —The user attempted to register a built-in
authenticator.

**•** `ConnectedApp` —The user attempted to access a connected app.

**•** `EnableLL` —The user attempted to enroll in Lightning Login.

**•** `ExportPrintReports` —The user attempted to export or print reports
or dashboards.

**•** `ExternalClientApp`  - The user attempted to access an external client
app.

**•** `ExtraVerification` —Reserved for future use.

**•** `ListView` —The user attempted to access a list view.

**•** `Login` —The user attempted to log in.

**•** `Registration` —Reserved for future use.

**•** `TempCode` —The user attempted to generate a temporary verification code.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
ID of the verification attempt. Verification can involve several attempts and use
different verification methods. For example, in a user’s session, a user enters an
invalid verification code (first attempt). The user then enters the correct code and


Standard Objects VerificationHistory

**Field Name** **Details**

successfully verifies identity (second attempt). Both attempts are part of a single
verification and, therefore, have the same ID. The label is Verification Attempt.

```
LoginGeoId

LoginHistoryId

Policy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
successful or unsuccessful identity verification attempt. Due to the nature of
geolocation technology, the accuracy of geolocation fields (for example, country,
city, postal code) can vary.

This is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

