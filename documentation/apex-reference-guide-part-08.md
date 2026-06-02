comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Available to Guest Users

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ZoneSearchPage searchInZone(String communityId, String zoneId,

   String q, ConnectApi.ZoneSearchResultType filter, String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Zones Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   zoneId
```

Type: String

ID of a zone.

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

A `ZoneSearchResultType` enum value. One of the following:

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ZoneSearchPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchInZone(communityId, zoneId, q, filter, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchInZone(communityId, zoneId, q, filter, language)`**

Search articles or questions in a zone, and specify the language of the results.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

36.0


Apex Reference Guide Zones Class

Available to Guest Users

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ZoneSearchPage searchInZone(String communityId, String zoneId,

   String q, ConnectApi.ZoneSearchResultType filter, String language)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   zoneId
```

Type: String

ID of a zone.

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

```
   language
```

Type: String

The language of the articles or questions. The value must be a Salesforce supported locale code.

Return Value

Type: `ConnectApi.ZoneSearchPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchInZone(communityId, zoneId, q, filter, language, result)


Apex Reference Guide Zones Class

#### Zones Test Methods These test methods are for Zones . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchInZone(communityId, zoneId, q, filter, result)`**

Register a `ConnectApi.ZoneSearchPage` object to be returned when `searchInZone(communityId, zoneId,`
`q, filter)` is called in a test context. Use the method with the same parameters or you receive an exception.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Signature

```
   public static Void setTestSearchInZone(String communityId, String zoneId, String q,

   ConnectApi.ZoneSearchResultType filter, ConnectApi.ZoneSearchPage result)

```

Parameters

```
   communityId
```

Type: String

Use either the ID for an Experience Cloud site, `internal`, or `null` .

```
   zoneId
```

Type: String

The ID of a zone.

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

A `ZoneSearchResultType` enum value. One of the following:

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

```
   result
```

Type: `ConnectApi.ZoneSearchPage`

The object containing test data.


Apex Reference Guide Zones Class

Return Value

Type: Void

SEE ALSO:

searchInZone(communityId, zoneId, q, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchInZone(communityId, zoneId, q, filter, pageParam, pageSize,`**

```
  result)

```

Register a `ConnectApi.ZoneSearchPage` object to be returned when `searchInZone(communityId, zoneId,`
`q, filter, pageParam, pageSize)` is called in a test context. Use the method with the same parameters or you receive
an exception.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Signature

```
   public static Void setTestSearchInZone(String communityId, String zoneId, String q,

   ConnectApi.ZoneSearchResultType filter, String pageParam, Integer pageSize,

   ConnectApi.ZoneSearchPage result)

```

Parameters

```
   communityId
```

Type: String

Use either the ID for an Experience Cloud site, `internal`, or `null` .

```
   zoneId
```

Type: String

The ID of a zone.

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

A `ZoneSearchResultType` enum value. One of the following:

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.


Apex Reference Guide Zones Class

```
   pageParam
```

Type: String

Specifies the page token to be used to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   result
```

Type: `ConnectApi.ZoneSearchPage`

The object containing test data.

Return Value

Type: Void

SEE ALSO:

searchInZone(communityId, zoneId, q, filter, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchInZone(communityId, zoneId, q, filter, language, result)`**

Register a `ConnectApi.ZoneSearchPage` object to be returned when `searchInZone(communityId, zoneId,`
`q, filter, language)` is called in a test context. Use the method with the same parameters or you receive an exception.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

36.0

Signature

```
   public static Void setTestSearchInZone(String communityId, String zoneId, String q,

   ConnectApi.ZoneSearchResultType filter, String language, ConnectApi.ZoneSearchPage

   result)

```

Parameters

```
   communityId
```

Type: String

Use either the ID for an Experience Cloud site, `internal`, or `null` .

```
   zoneId
```

Type: String

The ID of a zone.


### Apex Reference Guide ConnectApi Input Classes

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

```
   language
```

Type: String

The language of the articles or questions. The value must be a Salesforce supported locale code. In an `<apex:page>`, the default
value is the language of the page. Otherwise, the default value is the user's locale.

```
   result
```

Type: `ConnectApi.ZoneSearchPage`

The object containing test data.

Return Value

Type: Void

SEE ALSO:

searchInZone(communityId, zoneId, q, filter, language)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ConnectApi Input Classes Some ConnectApi methods take arguments that are instances of ConnectApi input classes.

Input classes are concrete unless marked abstract in this documentation. Concrete input classes have public constructors that have no
parameters.

Some methods have parameters that are typed with an abstract class. You must pass in an instance of a concrete child class for these
parameters.

Most input class properties can be set. Read-only properties are noted in this documentation.

#### ConnectApi.AbstractBaseSequenceInputRepresentation

The sequence for refunds and payment credits.

This class is abstract.

Superclass of:

**•** ConnectApi.RefundSequenceItemInputRepresentation

**•** ConnectApi.PaymentCreditSequenceItemInputRepresentation


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double The amount being refunded. Required 65.0

`orderPaymentSummaryId` String The order payment summary’s ID. Required 65.0

#### ConnectApi.AbstractCheckoutAddressInput

A checkout address.

This class is abstract.

Superclass of:

**•** `ConnectApi.CartShippingAddressInput`

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`city` String City of the address. Optional 53.0

`companyName` String Company name of the address. Optional 59.0

`country` String

ISO code of the address country. Must Required 53.0
match one of the valid ISO codes defined
within the org’s State-Country picklist.

`firstName` String First name of the contact. Optional 57.0

`id` String ID of the address. Required 53.0

`lastName` String Last name of the contact. Optional 57.0

`name` String Name of the contact. Required 53.0

`postalCode` String ZIP code of the address. Optional 53.0

`region` String

ISO code of the address region. Must match Optional 53.0
one of the valid ISO codes defined within
the org’s State-Country picklist.

`shipToPhoneNumber` String Phone number of the contact. Optional 63.0

`street` String Street of the address. Required 53.0

#### ConnectApi.AbstractList

Primitive list input.

This class is abstract.

Superclass of:

**•** ConnectApi.BooleanList

**•** ConnectApi.DoubleList

**•** ConnectApi.LongList


Apex Reference Guide ConnectApi Input Classes

**•** ConnectApi.StringList

No additional properties.

SEE ALSO:

ConnectApi.SearchFilter

#### ConnectApi.ActionInfoInputRepresentation

Recommended action information.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String

Name of the Lightning web component Optional 60.0
used for dynamically rendering the
recommended action.

`parameters` String Parameters required for processing and Required 60.0
displaying the recommended action.

#### ConnectApi.ActionLinkDefinitionInput

The definition of an action link. An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate
a file download, or invoke an API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can
include a request body and header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and
third-party services into the feed so that users can drive productivity and accelerate innovation.

Usage

You can use context variables in the `actionUrl`, `headers`, and `requestBody` properties. Use context variables to pass information
about the user who executed the action link to your server-side code. Salesforce substitutes the value when the action link is executed.

The available context variables are:


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionType` `ConnectApi.` Defines the type of action link. Values are:

```
         ActionLinkType
```

**•** `Api` —The action link calls a
synchronous API at the action URL.
Salesforce sets the status to
`SuccessfulStatus` or
`FailedStatus` based on the HTTP
status code returned by your server.

**•** `ApiAsync` —The action link calls an
asynchronous API at the action URL. The
action remains in a `PendingStatus`
state until a third party makes a request
to

```
                   /connect/action-links/ actionLinkId
```

to set the status to
`SuccessfulStatus` or
`FailedStatus` when the
asynchronous operation is complete.

**•** `Download` —The action link
downloads a file from the action URL.

**•** `Ui` —The action link takes the user to a
web page at the action URL.

Use `Ui` if you need to load a page before
the user performs an action, for example, to
have the user provide input or view
something before the action happens.

Note: Invoking `ApiAsync` action
links from an app requires a call to
set the status. However, there isn’t
currently a way to set the status of
an action link using Apex. To set the
status, use Connect REST API. See the
[Action Link resource in the Connect](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/)
[REST API Developer Guidefor more](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/)
information.

`actionUrl` String

The action link URL. For example, a `Ui`
action link URL is a Web page. A
`Download` action link URL is a link to the
file to download. `Ui` and `Download`

action link URLs are provided to clients. An
`Api` or `ApiAsync` action link URL is a
REST resource. `Api` and `ApiAsync`
action link URLs aren’t provided to clients.
Links to Salesforce can be relative. All other


Required 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

links must be absolute and start with
`https://` .

Tip: To avoid issues due to upgrades
or changing functionality in your API,
we recommend using a versioned
API for `actionUrl`, for example,

```
                       https://www.example.com/
```

`api/v1/exampleResource` .
If your API isn’t versioned, you can
use the `expirationDate`
property of the

```
                       ConnectApi.ActionLinkGroup
```

`DefinitionInput` class to
avoid issues due to upgrades or
changing functionality in your API.

`excludedUserId` String

`groupDefault` Boolean

Optional 33.0

Can be defined in an
action link template

using the `User`
`Visibility` and

```
Custom User
```

`Alias` fields.

Optional 33.0

Can be defined in an
action link template.

Optional 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

ID of a single user to exclude from
performing the action. If you specify an
`excludedUserId`, you can’t specify a
`userId` .

`true` if this action is the default action link
in the action link group; `false` otherwise.
There can be only one default action link
per action link group. The default action link
gets distinct styling in the Salesforce UI.

The request headers for the `Api` and
`ApiAsync` action link types.

[See Action Links Overview, Authentication,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_features_action_links_overview.htm)
[and Security.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_features_action_links_overview.htm)

Key for the set of labels to show in the user
interface. A set includes labels for these
states: NewStatus, PendingStatus,
SuccessStatus, FailedStatus. For example, if

you use the `Approve` key, you get these
labels: Approve, Pending, Approved, Failed.

For a complete list of keys and labels, see
[Action Links Labels.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)

If none of the predefined labels work for
your action link, use a custom label. To use


```
headers

```

List< `ConnectApi.`

```
RequestHeader
```

`Input` 

`labelKey` String

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

a custom label, create an action link
[template. See Create Action Link Templates.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/action_link_group_template_create.htm)

Required 33.0

Can be defined in an
action link template.

Optional 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

```
method

```

`ConnectApi.` One of these HTTP methods:

```
HttpRequest
```

**•** `HttpDelete` —Returns HTTP 204 on

`Method` success. Response body or output class

is empty.

**•** `HttpGet` —Returns HTTP 200 on
success.

**•** `HttpHead` —Returns HTTP 200 on
success. Response body or output class
is empty.

**•** `HttpPatch` —Returns HTTP 200 on
success or HTTP 204 if the response
body or output class is empty.

**•** `HttpPost` —Returns HTTP 201 on
success or HTTP 204 if the response
body or output class is empty.
Exceptions are the batch posting
resources and methods, which return
HTTP 200 on success.

**•** `HttpPut` —Return HTTP 200 on
success or HTTP 204 if the response
body or output class is empty.

`requestBody` String The request body for `Api` action links.

Note: Escape quotation mark
characters in the `requestBody`
value.

`requires` Boolean `true` to require the user to confirm the
`Confirmation` action; `false` otherwise.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`userId` String

SEE ALSO:

The ID of the user who can execute the
action. If not specified or `null`, any user
can execute the action. If you specify a
`userId`, you can’t specify an
`excludedUserId` .

Optional 33.0

Can be defined in an
action link template

using the `User`
`Visibility` and

```
Custom User
```

`Alias` fields.

#### ConnectApi.ActionLinkGroupDefinitionInput ConnectApi.ActionLinkGroupDefinitionInput

The definition of an action link group. All action links must belong to a group. Action links in a group are mutually exclusive and share
some properties. Define standalone actions in their own action group.

Action link definition can be sensitive to a third party (for example, OAuth bearer token headers). For this reason, only calls made from
the Apex namespace that created the action link definition can read, modify, or delete the definition. In addition, the user making the
call must have created the definition or have View All Data permission.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
actionLinks

```

```
List<ConnectApi.

ActionLink

DefinitionInput>

```

The action links that make up this group. Required to 33.0
instantiate this

Within an action link group, action links are
displayed in the order listed in the

`actionLinks` property of the

#### `ConnectApi.ActionLinkGroup`

`DefinitionInput` class. Within a feed
item, action link groups are displayed in the
order specified in the
`actionLinkGroupIds` property of
the

```
ConnectApi.AssociatedActions
```

`CapabilityInput` class.

You can create up to three action links in a
`Primary` group and up to four in an
`Overflow` group.


action link group
without a template.

To instantiate from a
template, don’t
specify a value.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
category

```

```
ConnectApi.

PlatformAction

GroupCategory

```

Indicates the priority and relative locations Required to 33.0
of action links in an associated feed item. instantiate this
Values are: action link group

**•** `Primary` —The action link group is
displayed in the body of the feed
element.

**•** `Overflow` —The action link group is
displayed in the overflow menu of the
feed element.

action link group
without a template.

To instantiate from a
template, don’t
specify a value.

`ConnectApi.` Defines the number of times an action link Required to 33.0
`ActionLink` can be executed. Values are: instantiate this
`ExecutionsAllowed` action link group

`executions` `ConnectApi.` Defines the number of times an action link Required to
`Allowed` `ActionLink` can be executed. Values are: instantiate this

`ExecutionsAllowed` action link group

**•** `Once` —An action link can be executed

without a template.

**•** `Once` —An action link can be executed
only one time across all users.

**•** `OncePerUser` —An action link can
be executed only one time for each
user.

**•** `Unlimited` —An action link can be
executed an unlimited number of times
by each user. If the action link’s
`actionType` is `Api` or
`ApiAsync`, you can’t use this value.

To instantiate from a
template, don’t
specify a value.

`expirationDate` `Datetime` ISO 8601 date string, for example, Required to 33.0
2011-02-25T18:24:31.000Z, that represents instantiate this

the date and time this action link group is
removed from associated feed items and
can no longer be executed. The
`expirationDate` must be within one
year of the creation date.

If the action link group definition includes
an OAuth token, it is a good idea to set the
expiration date of the action link group to
the same value as the expiration date of the
OAuth token so that users can’t execute the
action link and get an OAuth error.

To set a date when instantiating from a
template, see Set the Action Link Group
[Expiration Time in Design Action Link](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)
[Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)


action link group
without a template.

Optional to
instantiate from a
template.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

To instantiate 33.0
without a template,
don’t specify a value.

Required to
instantiate this

```
templateBindings List<ConnectApi.ActionLinkTemplateBindingInput>

templateId String

```

SEE ALSO:

A collection of key-value pairs to fill in
binding variable values or a custom user
alias from an action link template. To
instantiate this action link group from an
action link template that uses binding
variables, you must provide values for all the

action link group
variables. See Define Binding Variables in
from a template that
[Design Action Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)
uses binding
variables.

The ID of the action link group template
from which to instantiate this action link
group.

To instantiate 33.0
without a template,
don’t specify a value.

Required to
instantiate this

action link group
from a template.

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)

[Define an Action Link in a Template and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link_template.htm)

createActionLinkGroupDefinition(communityId, actionLinkGroup)

#### ConnectApi.ActionLinkTemplateBindingInput

A key-value pair to fill in a binding variable value from an action link template.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`key` String The name of the binding variable key Required 33.0
specified in the action link template in

Setup. For example, if the binding variable
in the template is
`{!Binding.firstName}`, the key is

```
                  firstName

```

`value` String

SEE ALSO:

The value of the binding variable key. For Required 33.0
example, if the key is `firstName`, this
value could be `Joan` .

ConnectApi.ActionLinkGroupDefinitionInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ActivationAdditionalAttributesConfigInput

Represents the additional attributes configuration for the market segment activation input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`activationPlatformAttrId` String Activation platform attribute ID. 60.0

`dataSourceType` String Type of data source. 60.0

`entityName` String Name of the entity. 60.0

`filterExpression` List< Attribute filter expression. 60.0
`ConnectApi.AttributeFilterInput`                        

`isRolluppable` Boolean Indicates whether the attribute can roll up 60.0
( `true` ) or not ( `false` ).

`label` String Label of the attribute. 60.0

`name` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

`queryPathConfig` List< Query path from the `activateOn` entity 60.0
`ConnectApi.QueryPathInputConfig`                        - to the additional attribute entity.

`referenceAttributeName` String Developer name of the reference attribute. 60.0

`source` `DataExportAttributeSourceEnum` Activation attribute source. 60.0

**•** `Direct`

**•** `Related`

`type` `DataExportAttributeTypeEnum` Type of activation attribute. 60.0

**•** `Computed_Dimension`

**•** `Computed_Measure`

**•** `Model`

**•** `Model_Related`

**•** `Non_Aggregatable_Computed_Measure`

#### ConnectApi.ActivationContactPointInput

Represents the activation contact point input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributesConfig` List< Attributes for the contact point. 60.0
`ConnectApi.ContactPointAttributeInput`                            

`entityName` String Entity name for the contact point. 60.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalPlatformHashMethod` String External platform hash method for the 60.0
contact point.

`filterExpression` List< Filter expression for the contact point. 60.0
`ConnectApi.DMOFilterInput`                    

`queryPathConfig` List< Query path configuration list. 60.0
`ConnectApi.QueryPathInputConfig`                        

`sourcesConfig` List< Source configurations for the contact point. 60.0
`ConnectApi.ContactPointSourceInput`                          

`type` `ContactPointTypeRepresentationEnum` Type of contact point. 60.0

**•** `Email`

**•** `Maid`

**•** `Ott`

**•** `Phone`

**•** `Push`

**•** `Subscriber_Key_Email`

**•** `Subscriber_Key_Phone`

**•** `WhatsApp`

#### ConnectApi.ActivationDefinitionInput

Represents the activation definition input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`activationTargetName` String Name of the activation target. Either 60.0
`activationTargetName` or

`dataExportDefinitionId` must
be present.

`activationTargetSubjectConfig` `ActivationTargetSubjectConfigInputRepresentation` Subject configuration for the activation 60.0
target.

`attributeLimitingExpressionConfig` <List `ConnectApi.AttributeLimitingExpressionInput`       - Limiting expression configuration for the 63.0
activation.

`attributesConfig` List< Additional attributes for the activation. 60.0
`ConnectApi.ActivationAdditionalAttributesConfigInput`                                       

`contactPointsConfig` <List `ConnectApi.ActivationContactPointInput`     - Contact points configuration for the 60.0
activation target.

`curatedEntity` `CuratedEntityInputRepresentation` Curated entity details for the activation. 60.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`customerFileSource` `ActivationPlatformCustomerFileSourceEnum` Customer file source of the activation 60.0
platform.

**•** `First_And_Third_Party`

**•** `First_Party`

**•** `Third_Party`

`dataExportDefinitionId` String Activation target ID for the activation. Either 60.0
`activationTargetName` or

`dataExportDefinitionId` must
be present.

`dataSourcesConfig` List< Data source configuration for the activation. 60.0
`ConnectApi.DataSourceNameConfigInput`                           

`dataSpaceName` String Data space name for the activation. 60.0

`description` String Description of the activation. 60.0

`directDmoFiltersConfig` List< Direct DMO filters for the activation. 60.0
`ConnectApi.DMOFilterInput`                    

`limitValue` Integer Audience limit value for the activation. 63.0

`marketSegmentId` String Segment ID of the segment the activation 60.0
needs to be created against. Either

`marketSegmentID` or
`segmentApiName` must be present.

`name` String Name of the activation. 60.0

`refreshType` String Indicates the refresh type for the activation, 60.0
either `Full` or `Incremental` .

`relatedDmoFiltersConfig` List< DMO filters on related attributes for the 60.0
`ConnectApi.DMOFilterInput`                    - activation.

`segmentApiName` String Developer name of the segment the 60.0
activation needs to be created against.

Either `marketSegmentID` or
`segmentApiName` must be present.

`shouldExcludeDeletes` Boolean

`shouldExcludeUpdates` Boolean

Indicates whether to exclude records 60.0
removed since the last refresh ( `true` ) or
not ( `false` ) .

Indicates whether to exclude records 60.0
modified since the last refresh ( `true` ) or
not ( `false` ) .


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`staticDataConfig` List< Configuration of static data, which adds 60.0
`ConnectApi.StaticDataInput`                    - metadata or campaign details in the ouput.

For example, `campaignId` or
`campaignName` .

SEE ALSO:

createActivation(input)

updateActivation(activationId, input)

#### ConnectApi.ActivationTargetInput

Input details for the activation target.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`connector` `ConnectApi.DataConnectorInput` Details about the connector for the Required 60.0
activation target.

`dataSpaceName` String Data space name for the activation target. Required 60.0

`description` String Description of the activation target. Required 60.0

```
egressProperties ConnectApi.EgressPropertiesInput

```

`isCappingEnabled` Boolean

Egress properties for the activation target, Optional 60.0
which are applicable only for file-based
activation targets.

Indicates whether communication capping Required 60.0
is enabled for the activation target
`(true)` or not `(false)` .

`name` String Name of the activation target. Required 60.0

`platformType` `DataConnectorTypeEnum` Data connector type of the activation target. Required 60.0

**•** `AmazonS3`

**•** `AzureBlob`

**•** `DataCloud`

**•** `GoogleCloudStorage`

**•** `SalesforceMarketingCloud`

**•** `Sftp`

SEE ALSO:

createActivationTarget(input)

updateActivationTarget(activationTargetId, input)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ActivationTargetSubjectConfigInput

Represents the activation target subject configuration input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`developerName` String Developer name of activation target subject 60.0
configuration.

`queryPathConfig` <List `ConnectApi.QueryPathInputConfig`    - Path of the activation target subject 60.0
configuration.

#### ConnectApi.ActivitySharingInput

Defines who a captured email or event is shared with.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`groupsTo` List< `String` 
```
ShareWith

```

List of IDs for the groups that you share the Optional 39.0
activity with. Valid only if `sharingType`
is `MyGroups` .

```
sharingType

```

#### ConnectApi. Type of sharing operation. Values are: Required 39.0

```
Activity
```

**•** `Everyone` —The activity is shared

`SharingType` with everyone.

**•** `MyGroups` —The activity is shared
only with a selection of the context
user’s groups.

**•** `OnlyMe` —The activity is private.

#### ConnectApi.AddressRequest

Address input representation for a payment method or card payment method.

**Name** **Type** **Description** **Required or** **Available Version**
**Optional**

`city` String Payment method city. Optional 51.0

`companyName` String Payment method company name. Optional 51.0

`country` String Payment method country. Optional 51.0

`postalCode` String Payment method postal code. Optional 51.0

`state` String Payment method state. Optional 51.0

`street` String Payment method street. Optional 51.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.AdjustItemInputRepresentation

A price adjustment to an OrderItemSummary. It only supports discounts, not increases.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`adjustmentType` String Describes how the amount is calculated. It Required 49.0
can have one of these values:

**•** `AmountTaxOnly` —Value of amount
is the tax-only adjustment only.
Available in version 65.0 and later.

**•** `AmountWithTax` —Value of amount
is the adjustment, including tax.

**•** `AmountWithoutTax` —Value of
amount is the adjustment, not including
tax. Tax is calculated on the value and
added.

**•** `Percentage` —Value of amount is a
percentage discount. It is divided by
100, and then multiplied by the
TotalPrice and TotalTaxAmount of the
OrderItemSummary to determine the
adjustment amount.

**•** `ProductOnly` ——Value of amount
is the product-only adjustment only.
Available in version 65.0 and later.

`amount` Double Value used to calculate the adjustment Required 49.0
amount, as described by the

adjustmentType. It must be a negative
value.

`description` String Description of the adjustment. Optional 49.0

`orderItem` String ID of the OrderItemSummary. Required 49.0

```
   SummaryId

```

`reason` String Reason for the adjustment. The value must Required 49.0
match one of the picklist values on the

Reason field of the
OrderItemSummaryChange object.

#### ConnectApi.AdjustOrderItemSummaryInputRepresentation

Price adjustments to order item summaries that together make up a price adjustment to an order, with options for adjusting items in
the process of being fulfilled.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
adjustItems

```

#### List< ConnectApi. List of price adjustments to order item Required 49.0

`AdjustItemInput` summaries.
`Representation` 

`allocatedItems` String Process to use for order item summary Optional 55.0
`ChangeOrderType` quantities that are currently being fulfilled,
defined as `QuantityAllocated`                       `QuantityFulfilled` . Values are:

**•** `Disallowed` —When distributing
the adjustment, ignore any quantities
being fulfilled. If an order item
summary’s entire quantity is being
fulfilled, return an error. This is the
default value.

**•** `InFulfillment` —When
distributing the adjustment, include
quantities being fulfilled. Create a
separate change order for the
adjustments made to those quantities.

**•** `PreFulfillment` —When
distributing the adjustment, include
quantities being fulfilled. Include the
adjustments made to those quantities
in the change order for pre-fulfillment
quantity adjustments.

individualLineItemTaxAdjustments Boolean

#### ConnectApi.AlternativeInput

Specifies whether to create multiple lines Optional 59.0
for each tax adjustment or one line with all
tax adjustments. The default value is false.

Alternative representation for an extension on a feed element.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`text` String Text representation of the extension. Required 40.0

```
Representation

```

`thumbnailUrl` String Thumbnail URL to the extension. Optional 40.0

`title` String Title of the extension. Optional 40.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.AlternativePaymentMethod

A payment method that doesn't have a defined Salesforce entity such as CardPaymentMethod or DigitalWallet. Common examples of
alternative payment methods include CashOnDeliver, Klarna, and Direct Debit. AlternativePaymentMethod functions the same as any
other type of payment method for processing transactions in the payment gateway.

Subclass of ConnectApi.BasePaymentMethodRequest

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String Salesforce Payments account to which this Required 54.0
payment method is linked.

`comments` String Details about a record added by a user. Optional 54.0
Maximum of 1,000 characters.

`email` String Email address of the card holder. Optional 54.0

`gatewayToken` String A unique, alphanumeric ID, called a token, Required 54.0
that a payment gateway generates when it

first processes a payment. The token
replaces the actual payment data so that
the data is kept secure. This token is stored
as encrypted text, and can be used for
recurring payments.

`gatewayToken` String Detailed information about the gateway Required 54.0
`Details` token.

`name` String Name that you assign to the payment Optional 54.0
method object.

#### ConnectApi.AnnouncementInput

An announcement.

**Property** **Type** **Description** **Required or** **Available**
**Optional**

`body` `ConnectApi.MessageBodyInput` Text of the announcement. Required for 31.0
creating an

announcement if

```
                                         feedItemId
```

isn’t specified

Don’t specify for
updating an
announcement.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional**

`expirationDate` Datetime

The Salesforce UI displays an announcement
until 11:59 p.m. on this date unless another
announcement is posted first. The Salesforce
UI ignores the time value in the
`expirationDate` . However, you can use
the time value to create your own display
logic in your own UI.

Required for 31.0
creating an
announcement

Optional for
updating an
announcement

`feedItemId` String ID of an `AdvancedTextPost` feed item Required for 36.0
that is the body of the announcement. creating an

announcement if
`body` isn’t
specified

Don’t specify for
updating an
announcement.

`isArchived` Boolean Specifies whether the announcement is Optional 36.0
archived.

`parentId` String

`sendEmails` Boolean

SEE ALSO:

ID of the parent entity for the announcement, Required for 36.0
that is, a group ID when the announcement creating an
appears in a group. announcement if

```
                  feedItemId
```

isn’t specified

Specifies whether the announcement is sent
as an email to all group members regardless
of their email setting for the group. If Chatter
emails aren’t enabled for the organization,
announcement emails aren’t sent. Default
value is `false` .

Don’t specify for
updating an
announcement.

Optional for 36.0
creating an
announcement

Don’t specify for
updating an
announcement

postAnnouncement(communityId, groupId, announcement)

postAnnouncement(communityId, announcement)

#### ConnectApi.ArticleTopicAssignmentJobInput

An article and topic assignment job.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### operation ConnectApi. Type of operation to perform on articles and Required 40.0

`ArticleTopicJobType` topics. Values are:

**•** `AssignTopicsToArticle` —Assign
topics to articles in a data category.

**•** `UnassignTopicsFromArticle` —Unassign
topics from articles in a data category.

`topicNames` `ConnectApi.TopicNamesInput` List of topic names to assign to or unassign Required 40.0
from articles.

#### ConnectApi.AssignedResourcesInput

Contains information about assigned resources for a service appointment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`extendedFields` <List `ConnectApi.ExtendedFieldInput`    - Use to add values to any of the fields, Optional 53.0
including custom fields.

`isPrimaryResource` Boolean Indicates whether an assigned resource is Optional 53.0
a primary resource.

Note: For multi-resource
appointments, only one resource can
be a primary resource.

`isRequiredResource` Boolean Indicates whether an assigned resource is Optional 53.0
a required resource.

`serviceResourceId` String The ID of the service resource assigned to Optional 53.0
the service appointment.

#### ConnectApi.AssociatedActionsCapabilityInput

A list of action link groups to associate with a feed element. To associate an action link group with a feed element, the call must be made
from the Apex namespace that created the action link definition. In addition, the user making the call must have created the definition
or have View All Data permission.

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke an
API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body and
header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services into the
feed so that users can drive productivity and accelerate innovation.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionLink` List<String> The action link group IDs to associate with Required 33.0
`GroupIds` the feed element. Associate one `Primary`
and up to 10 total action link groups to a
feed item. Action link groups are returned
in the order specified in this property.

An action link group ID is returned from a
call to `ConnectApi.ActionLinks.`

```
                    createActionLinkGroupDefinition

                    (communityId,
```

`actionLinkGroup)` .

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.AssociateRecordsWithRecipientInput

Records associated with the survey invitation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`associateRecord` List<String> ID of the associated records. Required 50.0

```
   Ids

```

`recipientId` String Participant ID with whose invitation the Required 50.0
record should be associated.

SEE ALSO:

ConnectApi.SurveyInvitationEmailInput

#### ConnectApi.AttributeFilterInput

Represents the attribute filter input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributeId` String ID of the attribute. 60.0

`attributeName` String Name of the attribute. 60.0

`dateUnits` Datetime Date unit filter. 60.0

`operator` String Operator of the attribute. 60.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`type` `FilterOperatorDataTypeEnum` Type of attribute. 60.0

**•** `FilterOperatorDataTypeBoolean`

**•** `FilterOperatorDataTypeDate`

**•** `FilterOperatorDataTypeDateOnly`

**•** `FilterOperatorDataTypeExactlyRelativeDate`

**•** `FilterOperatorDataTypeNumber`

**•** `FilterOperatorDataTypeRelateToNowDate`

**•** `FilterOperatorDataTypeText`

`value` List< `String`   - Filter values. 60.0

#### ConnectApi.AttributeLimitingExpressionInput

Represents the limiting expression input for an activation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributeName` String Name of the attribute. 63.0

`entityName` String Name of the entity. 63.0

`order` `FilterSortOrderEnum` The sort order for filtering. 63.0

**•** `FilterSortOrderAsc`

**•** `FilterSortOrderDesc`

`queryPathConfig` List< Query path configuration input. 63.0
`ConnectApi.QueryPathInputConfig`                        

`type` String Type of attribute. 63.0

#### ConnectApi.AttributeSetInputRepresentation

Attribute set information input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributes` List< `String`   - List of up to 5 attribute API names. Required Optional 62.0
if creating a new attribute set.

`id` String

If updating an attribute set, the ID of the Optional 62.0
existing attribute set for the variation parent
product.

`name` String Attribute set name for a new attribute set. Optional 62.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.AudienceCriteriaInput

Custom recommendation audience criteria type.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

Superclass for:

**•** ConnectApi.CustomListAudienceCriteriaInput

**•** ConnectApi.NewUserAudienceCriteriaInput

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Optional 36.0

If not specified,
defaults to
`CustomList` .

```
type

```

SEE ALSO:

#### ConnectApi. Specifies the custom recommendation

`Recommendation` audience criteria type. One of these values:

```
Audience
```

**•** `CustomList` —A custom list of users

`CriteriaType` makes up the audience.

**•** `MaxDaysInCommunity` —New
members make up the audience.

ConnectApi.RecommendationAudienceInput

#### ConnectApi.AudienceCriterionInput

Personalization audience criterion.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Required when 48.0
creating an audience

Optional when
updating an
audience

```
criterion

```

#### List< ConnectApi. List of mappings of audience criteria fields

`AudienceCriterion` and values.
`ValueInput` 

`criterionNumber` Integer Number associated with the audience Optional 48.0
criterion in a formula. For example, (1 AND

2) OR 3. If unspecified, criteria are assigned
numbers in the order that they’re added.

Required when 48.0
creating an audience

Optional when
updating an
audience

```
criterionOperator

```

#### ConnectApi. Operator used in the personalization

`AudienceCriteria` audience criterion. Values are:

```
Operator
```

**•** `Contains`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `Includes`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `NotIncludes`

**•** `StartsWith`

Required when 48.0
creating an audience

Optional when
updating an
audience

```
criterionType

```

SEE ALSO:

#### ConnectApi. Type of personalization audience criterion.

`AudienceCriteria` Values are:

```
Type
```

**•** `Audience` —Criterion based on
audience.

**•** `Default` —Audience has no criteria.

**•** `Domain` —Criterion based on domain.

**•** `FieldBased` —Criterion based on
object fields.

**•** `GeoLocation` —Criterion based on
location.

**•** `Permission` —Criterion based on
standard or custom permissions.

**•** `Profile` —Criterion based on profile.

ConnectApi.AudienceInput

#### ConnectApi.AudienceCriterionValueInput

Audience criterion value.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`audienceId` String ID of an audience. Required if creating 53.0
or updating an

audience with the

```
                                   Audience
```

criterion type.

`city` String City of a user. Optional if creating 48.0
or updating an

audience with the

```
                                   GeoLocation
```

criterion type


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`country` String Country of a user. Required if creating 48.0
or updating an

audience with the

```
                                     GeoLocation
```

criterion type

`domainId` String Domain ID of a user. Required if creating 48.0
or updating an

audience with the
`Domain` criterion
type

`entityField` String Field of an object. Required if creating 48.0
or updating an

audience with the

```
                                     FieldBased
```

criterion type

`entityType` String Type of object. Required if creating 48.0
or updating an

audience with the

```
                                     FieldBased
```

criterion type

`fieldValue` String Value of a field. Required if creating 48.0
or updating an

audience with the

```
                                     FieldBased
```

criterion type

`isEnabled` Boolean Specifies whether the permission is enabled Required if creating 48.0
( `true` ) or not ( `false` ) for a user. or updating an

audience with the

```
                                     Permission
```

criterion type

`permission` String Valid API name of a standard user or custom Required if creating 48.0
permission. or updating an

audience with the

```
                                     Permission
```

criterion type

`profileId` String Profile ID of a user. Required if creating 48.0
or updating an

audience with the
`Profile` criterion
type


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`subdivision` String Subdivision of a user. Required if creating 48.0
or updating an

audience with the

```
                                     GeoLocation
```

criterion type and
using the `city`
property

SEE ALSO:

ConnectApi.AudienceCriterionInput

#### ConnectApi.AudienceInput

A personalization audience.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Required when 48.0
creating an audience

Optional when
updating an
audience

```
criteria

```

#### List< ConnectApi. List of audience criteria to update or add.

`AudienceCriterion` An audience can have up to 100 criteria.
`Input` 

`customFormula` String Custom formula for the audience criteria. Required when 48.0
For example, (1 AND 2) OR 3. creating an audience

with the

```
                                  formulaFilterType
```

set to

```
                                  CustomLogicMatches

```

Optional, otherwise

#### formulaFilterType ConnectApi. Formula filter type for the personalization

`FormulaFilterType` audience. Values are:

**•** `AllCriteriaMatch` —All audience
criteria are true (AND operation).

**•** `AnyCriterionMatches` —Any
audience criterion is true (OR operation).

**•** `CustomLogicMatches` —Audience
criteria match the custom formula (for
example, (1 AND 2) OR 3).


Required when 48.0
creating an audience

Optional when
updating an
audience

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the audience.

#### ConnectApi.AuditParamsRequest

Audit Parameters input.

This class is abstract.

Superclass of ConnectApi.BaseRequest.

Required when 48.0
creating an audience

Optional when
updating an
audience

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`email` String Email of the client that made the request. Optional 50.0

`ipAddress` String IP address of the client that made the Optional 50.0
request.

`macAddress` String Mac address of the client that made the Optional 50.0
request.

`phone` String Phone number of the client that made the Optional 50.0
request.

#### ConnectApi.AuthApiPaymentMethodRequest

Payment method input representation for payment authorizations.

Subclass of ConnectApi.BaseApiPaymentMethodRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`card` `ConnectApi.Card` Card payment method information. Required 51.0

```
PaymentMethod PaymentMethodRequest

#### ConnectApi.AuthorizationReversalRequest

```

Authorization reversal input consumed by authorization reversal service.

Subclass of ConnectApi.BaseRequest.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String

Account for the payment authorization 51.0
reversal. Must match the payment
authorization's account.

`amount` Double Amount of adjustment applied to the 51.0
payment authorization.

`comments` String

Users can add comments to provide 51.0
additional details about a record. Maximum
of 1,000 characters.

`effectiveDate` Datetime Date that the adjustment takes effect on the 51.0
authorization.

#### ConnectApi.AuthorizationRequest

Payment Authorization input consumed by the Payment Authorization service.

Subclass of ConnectApi.BaseRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String Salesforce account that contains the Required 51.0
payment transaction being authorized.

`amount` Double Authorization amount. Required 51.0

`comments` String Optional comments for the payment Optional 51.0
authorization.

`currencyIsoCode` String Three-letter ISO 4217 currency code Required 51.0
associated with the payment group record.

`effectiveDate` Datetime Date that the authorization will be applied Required 51.0
to the transaction.

`paymentGatewayId` String Payment gateway that processes the Required 51.0
authorization.

```
paymentGroup

paymentMethod

```

#### ConnectApi. Payment group for the authorization. The Optional 51.0

`PaymentGroup` payload must reference either a
`Request` `paymentGroup` or a

`paymentGroupId`, but not both.

#### ConnectApi. Payment method used in the payment Required 51.0

`AuthApiPayment` gateway for the authorization transaction.

```
MethodRequest

```


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.BankPaymentMethodRequest

Bank payment method input representation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountHolder` String First name of the bank account holder. Optional 65.0

```
   FirstName

```

`accountHolder` String Last name of the bank account holder. Optional 65.0

```
   LastName

```

`accountHolderName` String Name of the bank account holder. Required 65.0

#### accountHolder ConnectApi. Bank account holder type. Valid values are: Optional 65.0

```
   Type AccountHolderType
```

**•** `Business`

**•** `Individual`

`accountId` String Salesforce account to which this payment Required 65.0
method is linked.

`accountNumber` String Unique account number for the bank Required 65.0
account.

#### accountType ConnectApi. Bank account type. Valid values are: Optional 65.0

```
            AccountType
```

**•** `Business`

**•** `Savings`

for e.g. Savings/Checking

`autoPay` Boolean Indicates whether a token for recurring Optional 65.0
payments is being requested ( `true` ) or not

( `false` ). The token lets the payment
method be used for recurring payments.

`bankCode` String Routing number is a unique nine-digit code Required 65.0
that identifies the bank.

#### bankType ConnectApi. Bank type. Valid values are: Optional 65.0

```
            BankType
```

**•** `ACH` —Automated Clearing House
transaction

**•** `BACS` —Bankers' Automated Clearing
Services transaction

**•** `BECS` —Bulk Electronic Clearing System
transaction

**•** `SepaDebit` —Single Euro Payments
Area transaction

`comments` String Comments for providing more information Optional 65.0
about the bank.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`email` String Email address of the bank account holder. Optional 65.0

`mandate` String Authorization from the account holder to Optional 65.0
debit their payment method.

`nickName` String Nick name of the bank account holder. Optional 65.0

#### standardEntry ConnectApi. Three-letter code that identifies the type of Optional 65.0

`ClassCode` `StandardEntryClassCode` electronic payment transaction being
processed within the Automated Clearing
House (ACH) network. Valid values are:

**•** `CCD` —Corporate Credit or Debit

**•** `PPD` —Prearranged Payment and
Deposit

**•** `TEL` —Telephone-Initiated Entry

**•** `WEB` —Internet Initiated/Mobile

#### ConnectApi.BannerPhotoInput

A banner photo.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cropHeight` Integer Height of the crop rectangle in pixels. Optional 36.0

`cropWidth` Integer Width of the crop rectangle in pixels. Optional 36.0

`cropX` Integer

`cropY` Integer

`fileId` String

X position of the crop rectangle from the Optional 36.0
left edge of the image in pixels. Top left is
position (0,0).

Y position of the crop rectangle from the Optional 36.0
top edge of the image in pixels. Top left is
position (0,0).

18 character ID of an existing file. The key Required 36.0
prefix must be 069 and the file must be an
image and be smaller than 2 GB.

Note: Images uploaded on the
Group page and on the User page
don’t have file IDs and therefore can’t
be used.

`versionNumber` Integer Version number of an existing file. If not Optional 36.0
provided, the latest version is used.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.BaseApiPaymentMethodRequest

Payment method API input representation.

This class is abstract.

Superclass of:

**•** ConnectApi.AuthApiPaymentMethodRequest

**•** ConnectApi.PostAuthApiPaymentMethodRequest

**•** ConnectApi.SaleApiPaymentMethodRequest

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### address ConnectApi. Payment method address. Required 51.0

```
            AddressRequest

```

`id` String Payment method record ID. Used in Required 51.0
payment transactions.

`saveForFuture` Boolean Shows whether Salesforce saves the Required 51.0
payment method for future use.

#### ConnectApi.BaseComparisonInput

Represents the base comparison input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`filtersConfig` List< Logical comparison input list wrapper. 60.0
`ConnectApi.TypeAndFilterInput`                       

`operator` String Operator of the comparison. 60.0

#### ConnectApi.BasePaymentMethodRequest

Base payment method input representation.

This class is abstract.

Superclass of:

**•** ConnectApi.AlternativePaymentMethod

**•** ConnectApi.CardPaymentMethodRequest

No additional properties.

#### ConnectApi.BaseRequest

Base parameters for making a request to the payment gateway.

This class is abstract.


Apex Reference Guide ConnectApi Input Classes

Subclass of ConnectApi.AuditParamsRequest.

Superclass of:

**•** ConnectApi.AuthorizationRequest

**•** ConnectApi.AuthorizationReversalRequest

**•** ConnectApi.CaptureRequest

**•** ConnectApi.PaymentMethodTokenizationRequest

**•** ConnectApi.PostAuthRequest

**•** ConnectApi.RefundRequest

**•** ConnectApi.SaleRequest

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalData` Map<String, String> An optional map of additional parameters Optional 50.0
to be sent to the payment gateway.

`idempotencyKey` String Idempotency key. Optional 50.0

#### ConnectApi.BatchInput

Construct a set of inputs to be passed into a method at the same time.

Use this constructor when there isn’t a binary input:

#### `ConnectApi.BatchInput(Object input)`

Use this constructor to pass one binary input:

#### `ConnectApi.BatchInput(Object input, ConnectApi.BinaryInput binary)`

Use this constructor to pass multiple binary inputs:

#### `ConnectApi.BatchInput(Object input, List<ConnectApi.BinaryInput> binaries)`

The constructors takes these parameters:

**Argument** **Type** **Description** **Available**
**Version**

`input` Object An individual input object to be used in the batch 32.0
operation. For example, for

`postFeedElementBatch()`, this should
be `ConnectApi.FeedElementInput` .

`binary` `ConnectApi.BinaryInput` A binary file to associate with the input object. 32.0


Apex Reference Guide ConnectApi Input Classes

**Argument** **Type** **Description** **Available**
**Version**

#### binaries List< ConnectApi.BinaryInput > A list of binary files to associate with the input 32.0

object.

SEE ALSO:

[Post a Batch of Feed Elements](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_batch.htm)

[Post a Batch of Feed Elements with a New (Binary) File](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_batch_binary.htm)

#### ConnectApi.BinaryInput Create a ConnectApi.BinaryInput object to attach files to feed items and comments, to add repository files, to create managed

content, and to replace managed content variants.

The constructor is:

#### `ConnectApi.BinaryInput(blob, contentType, filename)`

The constructor takes these arguments:

**Argument** **Type** **Description** **Available Version**

`blob` Blob Contents of the file to be used for input 28.0

`contentType` String MIME type description of the content, such as `image/jpg` 28.0

`filename` String File name with the file extension, such as UserPhoto.jpg 28.0

SEE ALSO:

[Post a Feed Element with a New File (Binary) Attachment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_binary.htm)

[Post a Comment with a New File](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_3.htm)

ConnectApi.BatchInput

#### ConnectApi.BookmarksCapabilityInput

Create or update a bookmark on a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isBookmarked` Boolean

```
ByCurrentUser

```

SEE ALSO:

Specifies if the feed element should be No 32.0
bookmarked for the user ( `true` ) or not
( `false` ).

ConnectApi.FeedElementCapabilitiesInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.BooleanList

List of Boolean values.

Subclass of ConnectApi.AbstractList.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`values` List<Boolean> List of Boolean values to filter on, for Optional 63.0
example, `[true, false]` .

#### ConnectApi.BotVersionActivationInput

Activation status of the bot version.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
status

```

#### ConnectApi. Activation status of the bot version. Values Optional 50.0

`BotVersion` are:

```
ActivationStatus
```

**•** `Active`

**•** `Inactive`

Activation status must be specified in the
_`status`_ or _`postBody`_ parameter.

#### ConnectApi.BusinessObjectivesInputRepresentation

A business objective, or goal, and insights associated with it.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`businessObjectiveId` String ID of the business objective. Required 62.0

```
insightSummary

```

`ConnectApi.BusObjInsights` A summary of insights about the business Optional 62.0
`InputRepresentation` objective.
on page 2026

#### ConnectApi.BusObjAssociationsInputRepresentation

Business objective association.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String Association ID for the business objective, or Required 59.0
goal.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
type

```

#### ConnectApi. Definition category of the business Required 59.0

`GoalDefinition` objective, or goal. Values are:

```
CategoryEnum
```

**•** `Webstore`

#### ConnectApi.BusObjInputRepresentation

A business objective, or goal.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
associations

```

<List `ConnectApi.BusObjAssociations` List of business objective associations. Optional 59.0

```
InputRepresentation
```

on page 2025>

`description` String Description of the business objective. Optional 59.0

`labelName` String Label name of the business objective. Required 59.0

#### ConnectApi.BusObjInsightsInputRepresentation

Insights associated with a business objective, or goal.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`targetCompletionDate` Datetime Target date for completion of the goal. Optional 62.0

`targetValue` Double Target value for the goal. Optional 62.0

#### ConnectApi.BusObjRecommendationInputRepresentation

Recommended action for a business objective, or goal.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`acceptanceLabel` String Text indicating user acceptance of the Optional 60.0
recommended action.

```
actionInfo

```

```
ConnectApi.ActionInfo

InputRepresentation
```

on page 1995

Name and parameters required for Optional 60.0
processing and displaying the
recommended action.

`businessObjectiveId` String 18-character business objective ID
associated with the recommended action.


Required to create a 60.0
recommended
action.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`channelId` String Associated channel ID for the recommended Required 61.0
action.

`description` String Detailed description of the recommended Optional 60.0
action.

`domain` String Domain category of the recommended Optional 60.0
action (e.g., "Product").

`externalName` String External identifier used for recommended Optional 61.0
action tracking.

`externalState` String JSON string containing data required for Optional 60.0
executing the recommended action.

`goalId` String 18-character GoalAssignment ID linked to Optional 61.0
the recommended action.

`grouping` String

Free-form categorization field to keep track Optional 62.0
of additional groupings of the
recommended actions.

`iconName` String SLDS icon name representing the Optional 60.0
recommended action domain.

`imageId` String Content asset file ID for the recommended Optional 60.0
action display image.

`name` String Display name of the recommended action.

Required to create a 60.0
recommended
action.

```
output

```

`ConnectApi.ActionInfo` Stores the last executed snapshot of the Optional 61.0
`InputRepresentation` recommended action.
on page 1995

`recommendationId` String 18-character unique identifier for the
recommended action.

Required to update 60.0
a recommended
action.

`rejectionLabel` String Text indicating user rejection of the Optional 60.0
recommended action.

`score` String Impact score of the recommended action Optional 60.0
(value between 0-100).

`secondaryState` String Optional state field for additional filtering of Optional 62.0
recommended action states.

`state` String

Primary state of the recommended action Optional 60.0
(e.g., "ACTIVE", "INACTIVE", "ACCEPTED",
"NOT_EXPIRING").


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`tertiaryState` String Optional state field for additional filtering of Optional 62.0
recommended action states.

#### ConnectApi.CalculateCartInput

Custom fields for a cart calculation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`customFields` List< `SObject`   - Array of sObjects and custom fields for the Optional 63.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, the WebCart,
CartItem, and CartDeliveryGroup sObjects
are supported. Field-level security rules from
[the shopper profile are applied to the](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
custom fields. The rules are applied for
registered shoppers and for the guest
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

#### ConnectApi.CalculateTaxRequest

Request to sent through the tax adapter to the external tax engine. Inputs with a `TaxTransactionType` of Debit represent a tax
calculation request. Inputs with a `TaxTransactionType` of Credit represent a tax cancellation request.

Subclass of ConnectApi.TaxTransactionRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isCommit` Boolean Commits the transaction for tax calculation. Required 55.0

`isHeaderTaxRequested` Boolean Indicates whether header tax is enabled in Optional 66.0
the tax engine ( `true` ) or not ( `false` ).

`shouldVoidTax` Boolean

Optional 65.0
Indicates whether to void the tax transaction
associated with a document that's

mentioned as the
`referenceDocumentCode` property
value with `taxType` property value as
`Actual` and `isCommit` property value
set to `true` .

Keep these considerations in mind when
you use this property.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** If the `shouldVoidTax` property
value is set to `true`, then the operation
returns a response with
`documentCode` property value
updated to

```
                      referenceDocumentCode
```

property value that was originally sent
in the request payload. The response
also includes the
`taxTransactionType` property
value as `Void` . This indicates that the
document specified in the

```
                      referenceDocumentCode
```

property value is voided.

**•** If document is locked or you can't void
the tax transaction for any reason, then
you can use the Tax Calculation request
to perform another transaction such as
a Credit Tax request. In this scenario, the
response includes the
`documentCode` property value that
was sent in the request payload.

**•** If the document that's mentioned in the

```
                      referenceDocumentCode
```

property value isn't available in the tax
engine, then an error response occurs
with ResultCode on page 577 value as
`ReferenceDocumentCodeMissing` .

`taxEngineId` String ID of the Salesforce tax engine entity used Required 55.0
to represent the external tax engine.

```
taxTransactionType

```

`ConnectApi.` Type of tax transaction. Values are: Required 55.0

```
TaxTransaction
```

**•** `Credit` —Transaction is a credit

`Type` transaction.

**•** `Debit` —Transaction is a debit
transaction.

**•** `Void` —Reserved for internal use in
case of input. In case of output, this
value specifies that the tax engine has
voided the document that's mentioned
as the `referenceDocumentCode`
property value.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
taxType

```

#### ConnectApi. Type of tax calculation. Values are: Required 55.0

```
CalculateTax
```

**•** `Actual` —Calculated tax represents

`Type` the final taxed amount for the

transaction.

**•** `Estimated` —Calculated tax
represents only an estimated value
before the transaction is finalized.

#### ConnectApi.CancelAllOrderItemsInputRepresentation

Cancellation of all items in an order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeItemFees` <List `ConnectApi.ChangeItemFeeWithTaxInputRepresentation` 

List of input data for fees, including taxes, Optional 63.0
associated with the order items being
canceled.

`excludedItems` List<String> List of items excluded from cancellation. Optional 63.0

`reason` String Reason for the cancellation. The value must Required 63.0
match one of the picklist values on the

Reason field of the Order Product Summary
Change object.

`reasonText` String Reason text used for the return insights. The Optional 63.0
value has a max of 255 characters.

#### ConnectApi.CanvasCapabilityInput

Create or update a canvas app associated with a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`description` String A description of the canvas app. The Optional 32.0
maximum size is 255 characters.

`developerName` String The API name (developer name) of the client Required 32.0
app.

`height` String The height of the canvas app in pixels. Optional 32.0

`namespacePrefix` String A unique namespace prefix for the canvas Optional 32.0
app.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`parameters` String JSON parameters passed to the canvas app. Optional 32.0

`thumbnailUrl` String

A thumbnail URL to a preview image. The Optional 32.0
maximum thumbnail size is 120 pixels by
120 pixels.

`title` String A title for the canvas link. Required 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.CapacityRequestInputRepresentation

Request related to a location’s fulfillment order capacity.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String Unique string that identifies the request. Required 55.0
Can be a UUID. Use the action request IDs

in response data to identify which requests
succeeded or failed.

`locationId` String ID of the location associated with the Required 55.0
request.

#### ConnectApi.CaptureRequest

Payment capture input consumed by the payment capture service.

Subclass of ConnectApi.BaseRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String ID of the account linked to the capture Optional 50.0
request.

`amount` Double Amount captured from the previous Required 50.0
authorization.

`clientContext` String Context for payment APIs. Used for a Optional 50.0
payment caller to re-establish context.

`comments` String Comments for the payment capture. Optional 50.0

`effectiveDate` Datetime Date when the payment becomes effective. Optional 50.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isFinalCapture` Boolean Indicates whether the current capture Optional 64.0
payment transaction is the final request

( `true` ) or not ( `false` ). Default value is
`false`, but it also depends on the card
type associated with the payment
authorization.

```
paymentGroup

```

#### ConnectApi. Details about the payment group record Optional 50.0

`PaymentGroup` associated with the payment request.

```
Request

```

#### ConnectApi.CardPaymentMethodRequest

Card payment method input representation.

Subclass of ConnectApi.BasePaymentMethodRequest.

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

`accountId` String Salesforce Payments account to which this Required 51.0
payment method is linked.

`autoPay` Boolean Indicates whether a token for recurring Optional 55.0
payments is being requested ( `true` ) or not

( `false` ). The token lets the payment method
be used for recurring payments.

#### cardCategory ConnectApi. Card processing type. Valid values are: Required 51.0

```
          CardCategory
```

**•** `CreditCard`

**•** `DebitCard`

`cardHolder` String First name of the card holder. Required 51.0

```
FirstName

```

`cardHolder` String Last name of the card holder. Required 51.0

```
LastName

```

`cardHolderName` String Full name of the card holder. Required 51.0

`cardNumber` String Card number. Required 51.0

`cardType` String Card network type. Valid values are: Required 51.0

**•** `AmericanExpress`

**•** `DinersClub`

**•** `JCB`

**•** `MasterCard`

**•** `Maestro`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

**•** `Visa`

`comments` String Optional comments for the card payment Optional 51.0
method.

`cvv` String Card Verification Value. Optional 51.0

`email` String Email address of the card holder. Required 51.0

`expiryMonth` Integer Card expiration month. Required 51.0

`expiryYear` Integer Card expiration year. Required 51.0

`nickName` String Optional nickname for the card. Optional 51.0

`startMonth` Integer Month the card becomes active. Optional 51.0

`startYear` Integer Year the card becomes active. Optional 51.0

#### ConnectApi.PromotionCartAdjustmentGroupInput

Cart adjustment group for a promotion.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`adjustmentBasis` String ID of the associated coupon, if applicable. Optional 60.0

```
   Reference

```

`adjustment` String Description of the price adjustment. Optional 60.0

```
   Description

#### adjustmentType ConnectApi. Type of price adjustment. Valid values are: Required 60.0

            AdjustmentType
```

**•** `AdjustmentAmount` —The
adjustment is a fixed amount.

**•** `AdjustmentPercentage` —The
adjustment is a percentage.

`adjustmentValue` String Price value of the adjustment. Optional 60.0

`baseAmount` String Total amount of the adjustment. Optional 60.0

`cartId` String ID of the cart. Required 60.0

`id` String ID of the cart adjustment group. Required 60.0

`priceAdjustment` String ID of the related promotion. Optional 60.0

```
   CauseId

```

`priority` Integer Where in the sequence of adjustments this Optional 60.0
adjustment was applied.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.cartCouponInput

Cart coupon input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`couponCode` String The coupon code. Required 54.0

#### ConnectApi.PromotionCartDeliveryGroupInput

Cart delivery group input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartDelivery` String ID of the cart delivery group. Required 57.0

```
   GroupId

#### cartDelivery List< ConnectApi. List of cart delivery group methods. Optional 60.0

   GroupMethods PromotionCart

            DeliveryGroupInput
```

`on page 2034`           

`deliveryMethodId` String ID of the order delivery method. Optional 57.0—59.0

#### ConnectApi.CartEvaluateShippingInput

Shipping address and custom fields used to calculate shipping costs for a cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`customFields` List< `SObject`   - Array of sObjects and custom fields for the Optional 63.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, the WebCart,
CartItem, and CartDeliveryGroup sObjects
are supported. Field-level security rules from
[the shopper profile are applied to the](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
custom fields. The rules are applied for
registered shoppers and for the guest
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`shippingAddress` `ConnectApi.CartShippingAddressInputRepresentation` Shipping address for a cart. Required 63.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CartEvaluateTaxInput

Shipping address and custom fields used to calculate taxes for a cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`customFields` List< `SObject`   - Array of sObjects and custom fields for the Optional 63.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, the WebCart,
CartItem, and CartDeliveryGroup sObjects
are supported. Field-level security rules from
[the shopper profile are applied to the](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
custom fields. The rules are applied for
registered shoppers and for the guest
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`shippingAddress` `ConnectApi.CartShippingAddressInputRepresentation` Shipping address for a cart. Required 63.0

#### ConnectApi.CartFromQuoteInput

Input representation for creating a cart from a quote.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`operationType` String

SEE ALSO:

Operation type for creating a cart from a Required 67.0
quote.

Valid values:

**•** `CONVERT_TO_CART` —Create a cart
from a quote only when its status is
`Approved` or `Accepted` .

When the user completes checkout by
converting the quote to a cart, the
method sets the `QuoteId` field on
[the Order object using the quote ID.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_order.htm)

**•** `DUPLICATE_TO_CART` —Duplicate
the quote to a cart.

createCartFromQuote(webstoreId, quoteId, cartFromQuoteInput)

ConnectApi.CartFromQuoteOutput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CartInventoryReservationInputRepresentation (Pilot)

Input representation to create or update a reservation.

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on
the basis of generally available products and features. This feature is made available on an AS IS basis and use of this feature is at
your sole risk.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`durationIn` Integer Reservation duration in seconds. Required 58.0

```
   Seconds

#### ConnectApi.CartItemInput

```

An item in a cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartDeliveryGroupId` String ID of the cart delivery group. Optional 59.0

`customFields` List< `SObject`   - Array of sObjects and custom fields for the Optional 61.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, only the CartItem
sObject is supported. Field-level security
[rules from the shopper profile are applied](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
to the custom fields. The rules are applied
for registered shoppers and for the guest
shopper profile. The custom fields can be
of type Checkbox, Currency, Date, Email,
LongTextArea, Number, Percent, Phone,
Text, TextArea, Url, Address, or Location. The
`customFields` property isn't supported
in stores built on an Aura template. See
[Create a Cart and Cart Item with Custom](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Fields in a Commerce Store.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`productId` String ID of the product.

Required when 49.0
adding an item to a
cart

Not supported when
updating a cart item

`productSellingModelId` String The ID of the product selling model Optional 59.0
associated with Product2.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantity` String Quantity of the cart item. Use a value that Required 49.0
can be converted to BigDecimal.

`subscriptionTerm` Integer on page 3936 The total number of terms in the Optional 59.0
subscription period.

#### subType ConnectApi. Subtype of item in a cart.Possible values are: Optional 64.0

```
            CartItemSubType
```

**•** `Bonus` —A bonus product.

**•** `Gift` —A gift product.

#### type ConnectApi. Type of item in a cart. Value is Product .

```
         CartItemType
```

**•** `DeliveryCharge`

**•** `Product`

Required when 49.0
adding an item to a
cart

Not supported when
updating a cart item

#### ConnectApi.CartItemPromotionCollectionInputRepresentation

Promotions for a cart item.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
items

```

#### List< ConnectApi. List of cart items to get the associated Required 52.0

`CartItemPromotion` promotions.
`InputRepresentation` 

#### ConnectApi.CartItemPromotionInputRepresentation

ID of a cart item associated with a promotion.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartItemId` String ID of the item associated with the cart. Optional 52.0

#### ConnectApi.CartMessagesVisibilityInput

Set the visibility for cart messages.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`visibility` Boolean Specifies whether to set cart messages as Required 50.0
visible ( `true` ) or not ( `false` ).


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CartInput

A cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`currencyIsoCode` String Currency ISO code of the cart. Optional 57.0

`customFields` List< `SObject`   - Array of sObjects and custom fields for the Optional 61.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, only the WebCart
sObject is supported. Field-level security
[rules from the shopper profile are applied](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
to the custom fields. The rules are applied
for registered shoppers and for the guest
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`effective` String ID of the buyer account or guest buyer Optional 49.0
`AccountId` profile for which the request is made. If
unspecified, the default value is determined
from context.

`isSecondary` Boolean

Specifies whether the cart is secondary Optional 53.0
( `true` ) or not ( `false` ). If unspecified,
defaults to `false` .

`name` String Name of the cart. The name can have up to Optional 49.0
250 Unicode characters. Avoid using special

characters in the cart name, including
`\"'<>@!$#&%\{[]}` .

If unspecified, a cart name is generated
automatically using the pattern,

```
                 Untitled Cart - [Date]
```

`[Time]` .

`orderOwnerId` String ID of the owner of the order. Optional 58.0

#### type ConnectApi. Type of cart. Vaues are: Optional 49.0

```
         CartType
```

**•** `Cart` —Cart created by a customer.

**•** `PayNowReadOnly` —Clone of a
Template cart that the customer can
check out with using the Pay Now
feature.

**•** `Template` —Cart created by an
internal user.

If unspecified, defaults to `Cart` .


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`typeAsString` String Type of the cart provided as a string. Optional 59.0

#### ConnectApi.CartShippingAddressInput

A cart shipping address.

Subclass of `ConnectApi.AbstractCheckoutAddressInput`

No additional properties.

#### ConnectApi.CartToWishlistInput

Copy products from a cart to a wishlist.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`wishlistId` String ID of the wishlist to copy cart products to. Required 50.0

#### ConnectApi.CdpAssetReferenceInput

Refernce to the model asset to use for the prediction request.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String ID of the asset. One of `id` or `name` 58.0
is required.

`name` String Name of the asset. One of `id` or `name` 58.0
is required.

`namespace` String Namespace of the asset. The `default` Optional 58.0
namespace is used by default.

#### ConnectApi.CdpCalculatedInsightInput

Input representation for a calculated insight.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`apiName` String API name of the calculated insight with
suffix __cio.


Required for creating 57.0
a calculated insight

Optional for
updating a
calculated insight

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`createdFrom` Boolean

```
Package

```

Specifies whether the calculated insight was Optional 57.0
created from an installed package ( `true` )
or not ( `false` ).

`dataSpaceName` String Name of the data space. Optional 57.0

Required for creating 57.0
a calculated insight

Optional for
updating a
calculated insight

```
definitionType

```

#### ConnectApi. Definition type of the calculated insight.

`CalculatedInsight` Values are:

```
DefinitionTypeEnum
```

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

`description` String Calculated insight description. Optional 57.0

`displayName` String Calculated insight display name.

Required for creating 57.0
a calculated insight

Optional for
updating a
calculated insight

`draft` Boolean Specifies whether to save the calculated Optional 57.0
insight as draft ( `true` ) or not ( `false` ).

`expression` String Calculated insight ANSI SQL expression.

Required for creating 57.0
a calculated insight

Optional for
updating a
calculated insight

`packagedCalculated` String API name of the packaged calculated Optional 57.0
`InsightApiName` insight.

#### ConnectApi.CdpIdentityResolutionConfigInput

Input representation for creating an identity resolution ruleset.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
configurationType

```

#### ConnectApi. Source object for an identity resolution Required 57.0

`CdpIdentityResolution` ruleset. Values are:

```
ConfigurationType
```

**•** `Account`

**•** `Individual`

`description` String Description of the identity resolution ruleset. Optional 57.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`doesRun` Boolean Specifies whether automatic job run Optional 57.0
`Automatically` scheduling is enabled for the ruleset ( `true` )
or not ( `false` ). If unspecified, defaults to
`false` .

`label` String User friendly name of the identity resolution Required 57.0
ruleset.

```
matchRules

reconciliationRules

```

#### List< ConnectApi. List of match rules for the identity resolution Optional 57.0

`CdpIdentityResolution` ruleset.
`MatchRule` 
#### List< ConnectApi. List of reconciliation rules for the identity Required 57.0

`CdpIdentityResolution` resolution ruleset.
`ReconciliationRule` 

`rulesetId` String Extended ID of the ruleset used to Optional 57.0
differentiate between rulesets created for

comparison. The ruleset ID must be unique
and can't be longer than 4 characters.

#### ConnectApi.CdpIdentityResolutionConfigPatchInput

Input representation for updating an identity resolution ruleset.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`description` String Description of the identity resolution ruleset. Optional 57.0

`doesRun` Boolean Specifies whether automatic job run Optional 57.0
`Automatically` scheduling is enabled for the ruleset ( `true` )
or not ( `false` ). If unspecified, defaults to
`false` .

`label` String User friendly name of the identity resolution Required 57.0
ruleset.

```
matchRules

reconciliationRules

```

#### List< ConnectApi. List of match rules for the identity resolution Optional 57.0

`CdpIdentityResolution` ruleset.
`MatchRule` 
#### List< ConnectApi. List of reconciliation rules for the identity Required 57.0

`CdpIdentityResolution` resolution ruleset.
`ReconciliationRule` 

#### ConnectApi.CdpIdentityResolutionMatchCriterion

Input representation for an identity resolution ruleset's match rule criterion.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`caseSensitiveMatch` Boolean Specifies whether the criterion match is case Optional 58.0
sensitive ( `true` ) or not ( `false` ). Available

[only when matching is based on the party](https://help.salesforce.com/s/articleView?id=data.c360_a_match_rules.htm&type=5&language=en_US)
[identifier.](https://help.salesforce.com/s/articleView?id=data.c360_a_match_rules.htm&type=5&language=en_US)

`entityName` String API name of the Data Model Object the Required 57.0
match rule applies to.

`fieldName` String Name of the field the criterion applies to. Required 57.0

```
matchMethodType

```

#### ConnectApi. Match method for a match rule criterion. Required 57.0

`CdpIdentityResolution` Values are:

```
MatchMethodType
```

**•** `Exact` —Exact match.

**•** `ExactNormalized` —Exact
normalized match.

**•** `Fuzzy` —Fuzzy match with medium
precision.

**•** `FuzzyHigh` —Fuzzy match with high
precision.

**•** `FuzzyLow` —Fuzzy match with low
precision.

#### partyIdentification ConnectApi. Party Identifier information. Optional 57.0

```
Info CdpIdentityResolution

         MatchCriterionParty

         IdentificationInfo

```

`shouldMatch` Boolean Specifies whether blank fields can be used Required 57.0
`OnBlank` for matching ( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.CdpIdentityResolutionMatchRule

#### ConnectApi.CdpIdentityResolutionMatchCriterionPartyIdentificationInfo

Input representation for information when party identification is used in an identity resolution ruleset's match rule criterion.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`partyName` String Party identification name. Required if the 57.0
match rule criterion

uses party
identification for
matching


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`partyType` String Party identification type. Optional 57.0

SEE ALSO:

ConnectApi.CdpIdentityResolutionMatchCriterion

#### ConnectApi.CdpIdentityResolutionMatchRule

Input representation for an identity resolution ruleset’s match rule.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
criteria

```

#### List< ConnectApi. Object and field the match rule applies to Required 57.0

`CdpIdentityResolution` and the match method applied.
`MatchCriterion` 

`label` String User friendly name for the identity Required 57.0
resolution match rule.

SEE ALSO:

ConnectApi.CdpIdentityResolutionConfigInput

ConnectApi.CdpIdentityResolutionConfigPatchInput

#### ConnectApi.CdpIdentityResolutionReconciliationFieldRule

Input representation for an identity resolution ruleset's reconciliation rule for a field.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fieldName` String The field that this reconciliation rule applies Required 57.0
to.

```
ruleType

```

#### `ConnectApi.`

```
CdpIdentityResolution

ReconciliationRuleType

```

Default reconciliation rule applied to fields Required 57.0
in the object the reconciliation rule applies
to. Values are:

**•** `LastUpdated`

**•** `MostFrequent`

**•** `SourceSequence`

`shouldIgnore` Boolean Specifies whether to ignore an empty value Required 57.0
`EmptyValue` ( `true` ) or not ( `false` ).


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Required if 57.0
`ruleType` is

```
SourceSequence

```

```
sources

```

SEE ALSO:

#### List< ConnectApi. If ruleType is SourceSequence, a

`CdpIdentityResolution` prioritized list of data sources.
`ReconciliationSource` 

#### ConnectApi.CdpIdentityResolutionReconciliationRule ConnectApi.CdpIdentityResolutionReconciliationRule

Input representation for an identity resolution ruleset's default reconciliation rule for an object.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`entityName` String API name of the Data Model Object the Required 57.0
reconciliation rule applies to.

Field-specific reconciliation rules that Optional 57.0
override this default rule for the specified
field.

Default reconciliation rule applied to fields Required 57.0
in the object the reconciliation rule applies
to. Values are:

**•** `LastUpdated`

**•** `MostFrequent`

**•** `SourceSequence`

```
fields

ruleType

```

#### List< ConnectApi.

```
CdpIdentityResolution

ReconciliationField
```

`Rule` 
#### `ConnectApi.`

```
CdpIdentityResolution

ReconciliationRuleType

```

`shouldIgnore` Boolean Specifies whether to ignore an empty value Required 57.0
`EmptyValue` ( `true` ) or not ( `false` ).

Required if 57.0
`ruleType` is

```
SourceSequence

```

```
sources

```

SEE ALSO:

#### List< ConnectApi. If ruleType is SourceSequence, a

`CdpIdentityResolution` list of data sources in priority order.
`ReconciliationSource` 

ConnectApi.CdpIdentityResolutionConfigInput

ConnectApi.CdpIdentityResolutionConfigPatchInput

#### ConnectApi.CdpIdentityResolutionReconciliationSource

Input representation for an identity resolution default reconciliation rule or field-specific rule using the `SourceSequence` match
method.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String

SEE ALSO:

If the `ruleType` for a reconciliation rule
is `SourceSequence`, API name of a
source Data Lake Object.

Required if 57.0
`ruleType` is

```
SourceSequence

```

ConnectApi.CdpIdentityResolutionReconciliationRule

ConnectApi.CdpIdentityResolutionReconciliationFieldRule

ConnectApi.CdpIdentityResolutionReconciliationFieldRule

#### ConnectApi.CdpIdentityResolutionRunNowInput

Input representation for running an identity resolution ruleset job on demand.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`callingApp` String Calling application. Optional 57.0

`callingAppInfo` String Calling application information. Optional 57.0

#### ConnectApi.CdpMlBasePredictInput

Base input representation for a prediction request.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`model` `ConnectApi.CdpAssetReferenceInput` A reference to the model to use to generate Required 59.0
the prediction.

`settings` `ConnectApi.CdpMlPredictSettingsInput` The model configuration settings to use to Optional 59.0
generate the prediction.

`type` `CdpMlPredictTypeEnum` Type of input data for the prediction. Required 59.0

**•** `RawData` -Raw data.

**•** `RecordOverrides` -Record IDs with
user-provided overrides.

**•** `Records` -Record IDs.

SEE ALSO:

predict(predict)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CdpMlPredictSettingsInput

Input representation for the model settings used to generate a prediction.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`aggregateFunctions` List< `String`    - List of aggregate functions for the Optional 59.0
prediction.

`maxPrescriptions` Integer

`maxTopFactors` Integer

Maximum number of recommendations. Optional 59.0
The default value is `-1` (unlimited) and the
allowed range is `-1` through `200` .

Maximum number of top factors. The Optional 59.0
default value is `0` and the allowed range is
`0` through `3` .

`prescriptionImpactPercentage` Integer The minimum impact percentage of the Optional 59.0
prescriptions to return. Only prescriptions

whose impact percentage is greater than
or equal to the specified percentage are
returned. The default value is `0` and the
allowed range is `0` through `100` .

#### ConnectApi.CdpQueryInput

Data query input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`sql` String ANSI-standard SQL query. Required 52.0

SEE ALSO:

queryANSISql(input)

queryANSISql(input, batchSize, offset, orderby)

queryANSISql(input, batchSize, offset, orderby, dataspace)

queryAnsiSqlV2(input)

queryAnsiSqlV2(input, dataspace)

#### ConnectApi.CdpSegmentDbtInput

Segment dbt input.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
models

```

SEE ALSO:

#### List< ConnectApi. List of models. The segment data build tool Required 55.0

`CdpSegmentDbt` currently supports a single SQL model.
`ModelInput` 

#### ConnectApi.CdpSegmentInput ConnectApi.CdpSegmentDbtModelInput

Segment dbt model input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Dbt model name. Required 55.0

`sql` String

SEE ALSO:

ConnectApi.CdpSegmentDbtInput

Dbt SQL. Required 55.0

Dbt SQL date strings must be in ISO 8601
format, for example,
2011-02-25T18:24:31.000Z.

For details about supported validations, see
[Supported Validations for Segment Data](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_features_cdp_cbt_validations.htm)
[Build Tool Model SQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_features_cdp_cbt_validations.htm)

#### ConnectApi.CdpSegmentInput

Segment input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalMetadata` Map<String, String> Map of additional metadata.

Optional for creating 55.0
a segment

Not supported for
updating a segment

`dataSpace` String

Segment dataspace. In API version 59.0 and Optional 57.0–58.0
later, this property is not available. Use the
`dataspace` request parameter instead.

`description` String Segment description. Optional 55.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`developerName` String Segment developer name.

Required for creating 55.0
a segment

Not supported for
updating a segment

`displayName` String Segment display name. Optional 57.0

```
includeDbt

```

#### ConnectApi. Segment data build tool. Required 55.0

```
CdpSegment

DbtInput

```

#### publishSchedule ConnectApi. Publish refresh schedule. Values are: Optional 55.0

```
         PublishSchedule
```

**•** `One` —Refreshes every hour. Used to
rapidly publish UI and DBT-based
segments.

**•** `Four` —Refreshes every four hours.
Used to rapidly publish UI and
DBT-based segments.

**•** `Twelve` —Refreshes every twelve
hours.

**•** `TwentyFour` —Refreshes every
twenty-four hours.

`publishSchedule` String Date indicating the end of the publish
`EndDate` schedule.

`publishSchedule` String Datetime indicating the start of the publish
`StartDateTime` schedule.

Optional if 55.0

```
publishSchedule
```

isn’t specified

Optional if 55.0

```
publishSchedule
```

isn’t specified

`segmentOnApiName` String API name of the SegmentOn entity. Optional 57.0

#### segmentType ConnectApi. Type of segment. Value is:

```
         SegmentType
```

**•** `Dbt` —Data build tool

After a segment is created, the segment
type can’t be changed.

#### ConnectApi.ChangeInputRepresentation

Required for creating 55.0
a segment

Not supported for
updating a segment

A list of changes to OrderItemSummaries that make up an order change, such as a cancel or return.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
changeItems

```

SEE ALSO:

#### List< ConnectApi. List of changes to OrderItemSummaries. Required 48.0

```
ChangeItemInput
```

`Representation` 

previewCancel(orderSummaryId, changeInput)

previewReturn(orderSummaryId, changeInput)

submitCancel(orderSummaryId, changeInput)

submitReturn(orderSummaryId, changeInput)

ConnectApi.ChangeItemFeeInputRepresentation

Input representation for Change Item Fee Input

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double

Positive value used to calculate the fee Required 57.0
amount, as described by the
`amountType` .

`amountType` String Describes how the fee amount is calculated. Required 57.0
Valid values are:

**•** `AmountWithTax` —Value of
`amount` is the fee amount, including
tax.

**•** `AmountWithoutTax` —Value of
`amount` is the fee amount, not
including tax. Tax is calculated on the
value and added.

**•** `Percentage` —Value of `amount` is
a percentage. To determine the fee
amount, `amount` is divided by 100,
and then multiplied by the TotalPrice
and TotalTaxAmount of the associated
OrderItemSummary, prorated for the
quantity being returned.

**•** `PercentageGross` —Value of
`amount` is a percentage. To determine
the fee amount, `amount` is divided by
100, and then multiplied by the
TotalLineAmountWithTax of the
associated OrderItemSummary,


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

prorated for the quantity being
returned.

`description` String Description of the fee. Required 57.0

`priceBookEntryId` String ID of the price book entry associated with
the fee product.

Required unless 57.0
price books are
optional in the org

`product2Id` String ID of the product representing the fee. Required 57.0

`reason` String Reason for the fee. The value must match Required 57.0
an entry in the

OrderProductSummaryChange object’s
Reason picklist.

SEE ALSO:

ConnectApi.ChangeInputRepresentation

ConnectApi.ChangeItemInputRepresentation

previewCancel(orderSummaryId, changeInput)

previewReturn(orderSummaryId, changeInput)

submitCancel(orderSummaryId, changeInput)

submitReturn(orderSummaryId, changeInput)

#### ConnectApi.ChangeItemFeeTaxInputRepresentation

Input representation of taxes associated with a change item fee.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double Tax amount of the change item fee. Required 63.0

`description` String Description of the change item fee. Required 63.0

`rate` Double Tax rate for the change item fee. Required 63.0

`taxEffectiveDate` String Effective date for the tax. Required 63.0

`type` String Describes how the fee amount is calculated. Required 63.0
Valid values are:

**•** `Actual`

**•** `Estimated`


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ChangeItemFeeWithTaxInputRepresentation

Input representation of a change item fee with taxes.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double Positive value used to calculate the fee Required 63.0
amount.

`changeItemFeeTaxes` <List `ConnectApi.ChangeItemFeeTaxInputRepresentation`    - List of taxes associated with the change item Required 63.0
fees.

`description` String Description of the fee. Required 63.0

`orderDeliveryGroupSummaryId` String ID of the order delivery group summary. Required 63.0

`priceBookEntryId` String ID of the price book entry associated with
the fee product.

Required unless 63.0
price books are
optional in the org

`product2Id` String ID of the product representing the fee. Required 63.0

`reasonText` String Reason for the cancellation. The value must Required 63.0
match one of the picklist values on the

Reason field of the Order Product Summary
Change object.

#### ConnectApi.ChangeItemInputRepresentation

Change to an order item summary, such as a return or cancel. You specify whether to prorate the associated shipping charge based on
the price change. The order item summary can’t be a shipping charge.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeItemFees` List< `ChangeItemFee` - List of input data for fees associated with Optional 57.0
the order item being returned or canceled.

`orderItemSummaryId` String ID of the order item summary. Required 48.0

`quantity` Double

Quantity to change. Use a positive value. Required 48.0
For example, a value of 2 means “cancel or
return 2 units.”

`reason` String Reason for the change. The value must Required 48.0
match one of the picklist values on the

Reason field of the
OrderItemSummaryChange object.

`reasonForChangeText` String Reason text used for the return insights. The Optional 59.0
value has a max of 255 characters.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`shippingReductionFlag` Boolean Specifies whether to prorate the shipping Required 48.0
charge.

SEE ALSO:

ConnectApi.ChangeInputRepresentation

previewCancel(orderSummaryId, changeInput)

previewReturn(orderSummaryId, changeInput)

submitCancel(orderSummaryId, changeInput)

submitReturn(orderSummaryId, changeInput)

#### ConnectApi.ChangeOrderAdjustmentGroupSummaryInputRepresentation

A change to an order adjustment group summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeType` String Whether a new order adjustment group Required 66.0
summary is being created or an existing

summary is being updated. Valid values are
New or Update.

`orderAdjustmentGroupSummary` SObject The order adjustment group summary Required 66.0
sObject representation that contains the

changes for the Order Adjustment Group
Summary entity.

`referenceId` String

The unique reference ID for this order Optional 66.0
adjustment group summary. This field is
valid only if the Change Type value is New.

#### ConnectApi.ChangeOrderDeliveryGroupSummaryInputRepresentation

A change to an order delivery group summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeType` String Whether a new order delivery group Required 66.0
summary is being created or an existing

summary is being updated. Valid values are
New or Update.

`orderDeliveryGroupSummary` SObject The order delivery group summary sObject Required 66.0
representation that contains the changes


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

for the Order Delivery Group Summary
entity.

`referenceId` String

The unique reference ID for this order Optional 66.0
delivery group summary. This field is valid
only if the Change Type value is New.

#### ConnectApi.ChangeOrderItemAdjustmentLineSummaryInputRepresentation

A change to an order item adjustment line summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeType` String Whether a new order item adjustment line Required 66.0
summary is being created or an existing

summary is being updated. Valid values are
New or Update.

`orderItemAdjustmentLineSummary` SObject The order item adjustment line summary Required 66.0
sObject representation that contains the

changes for the Order Item Adjustment Line
Summary entity.

`referenceId` String

The unique reference ID for this adjustment Optional 66.0
line summary. This field is valid only if the
Change Type value is New.

#### ConnectApi.ChangeOrderItemSummaryInputRepresentation

A change to an order item summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeType` String

`orderItemSummary` SObject

`referenceId` String

Whether a new order item summary is being Required 66.0
created or an existing summary is being
updated. Valid values are New or Update.

The order item summary sObject Required 66.0
representation that contains the changes
for the Order Item Summary entity.

The unique reference ID for this order item Optional 66.0
summary. This field is valid only if the
Change Type value is New.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ChangeOrderItemTaxLineItemSummaryInputRepresentation

A change to an order item tax line item summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeType` String Whether a new order item tax line item Required 66.0
summary is being created or an existing

summary is being updated. Valid values are
New or Update.

`orderItemTaxLineItemSummary` SObject The order item tax line item summary Required 66.0
sObject representation that contains the

changes for the Order Item Tax Line
Summary entity.

`referenceId` String

The unique reference ID for this order tax Optional 66.0
line item summary. This field is valid only if
the Change Type value is New.

#### ConnectApi.ChangeOrderSummaryInputRepresentation

A change to an order summary. There are several general validations for this input. The maximum number of changes allowed per
request is 100. You must include at least one change for an entity, and each change that's associated with an entity counts as one change.
You can modify only order item summaries in Ordered status.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeOrdersReferenceNumber` String

The order reference number value for the Optional 66.0
Change Order associated with the current
request.

`changeReason` String The reason for the change. It has to be an Required 66.0
active Picklist value from the

OrderItemSummaryChange entity Reason
field.

`orderAdjustmentGroupSummaries` <List `ChangeOrderAdjustmentGroupSummaryInputRepresentation` - The list of order adjustment group Optional 66.0
summaries changes.

`orderDeliveryGroupSummaries` <List `ChangeOrderDeliveryGroupSummaryInputRepresentation` - The list of order delivery group summaries Optional 66.0
changes.

`orderItemAdjustmentLineSummaries` < `ChangeOrderItemAdjustmentLineSummaryInputRepresentation` List - The list of order item adjustment line Optional 66.0
summaries changes.

`orderItemSummaries` <List `ChangeOrderItemSummaryInputRepresentation` - The list of order item summaries changes. Optional 66.0

`orderItemTaxLineItemSummaries` <List `ChangeOrderItemTaxLineItemSummaryInputRepresentation` - The list of order item tax line item Optional 66.0
summaries changes.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderSummary` SObject

The order summary sObject representation Optional 66.0
that contains the changes for the Order
Summary.

#### ConnectApi.ChatterGroupInput

Chatter group input.

**Property** **Type** **Description** **Available**

`announcement` String

The 18-character ID of an announcement. 31.0

An announcement displays in a designated location in the
Salesforce UI until 11:59 p.m. on its expiration date, unless it’s
deleted or replaced by another announcement.

`canHave` Boolean `true` if this group allows Chatter customers, `false` otherwise. 29.0
`ChatterGuests` After this property is set to `true`, it cannot be set to `false` .

`description` String The “Description” section of the group. 29.0

```
information

```

#### ConnectApi. The “Information” section of a group. If the group is private, this 28.0

`GroupInformation` section is visible only to members.

```
Input

```

`isArchived` Boolean `true` if the group is archived, `false` otherwise. Defaults to 29.0
`false` .

`isAuto` Boolean `true` if automatic archiving is turned off for the group, `false` 29.0
`ArchiveDisabled` otherwise. Defaults to `false` .

`name` String The name of the group. 29.0

`owner` String The ID of the group owner. This property is available for PATCH 29.0
requests only.

#### visibility ConnectApi. Group visibility type. 29.0

```
          GroupVisibilityType
```

**•** `PrivateAccess` —Only members of the group can see
posts to this group.

**•** `PublicAccess` —All users within the Experience Cloud
site can see posts to this group.

**•** `Unlisted` —Reserved for future use.

SEE ALSO:

createGroup(communityId, groupInput)

updateGroup(communityId, groupId, groupInput)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ChatterStreamInput

A Chatter feed stream.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`description` String Description of the stream, up to 1,000 Optional 39.0
characters.

`name` String Name of the stream, up to 120 characters.

Required when 39.0
creating a stream

Optional when
updating a stream

List of up to 25 entities whose feeds are Optional 39.0
included in the stream.

Adding an entity that is already added
results in no operation. Including the same

entity in `subscriptionsToAdd` and
`subscriptionsToRemove` results in
no operation.

List of entities whose feeds are removed
from the stream.

Removing an entity that is already removed
results in no operation. Including the same
entity in `subscriptionsToAdd` and

`subscriptionsToRemove` results in
no operation.

```
subscriptions

ToAdd

subscriptions

ToRemove

```

#### List< ConnectApi.

```
Stream

Subscription
```

`Input` 
#### List< ConnectApi.

```
Stream

Subscription
```

`Input` 

Optional when 39.0
updating a stream

Not supported when
creating a stream

#### ConnectApi.CommentCapabilitiesInput

A container for all capabilities that can be included with a comment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`content` `ConnectApi.ContentCapabilityInput` Content to attach to the comment. Optional 32.0

`feedEntityShare` `ConnectApi.FeedEntityShareCapabilityInput` Feed entity to share to the comment. Optional 42.0

`record` `ConnectApi.RecordCapabilityInput` Existing knowledge article to attach to the Optional 42.0
comment.

SEE ALSO:

ConnectApi.CommentInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CommentInput

Comment input used to add rich comments, for example, comments that include mentions or file attachments.

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

```
attachment

```

#### ConnectApi. Specifies an attachment for the comment. Valid Optional 28.0–31.0

`FeedItem` values are:

```
AttachmentInput
```

**•** `ContentAttachmentInput`

**•** `NewFileAttachmentInput`

`LinkAttachmentInput` is not permitted
for comments.

Important: As of version 32.0, use the
`capabilities` property.

#### body ConnectApi. Description of message body. The body can Required 28.0

`MessageBodyInput` contain up to 10,000 characters and 25

mentions. Because the character limit can
change, clients should make a
`describeSObjects()` call on the
FeedItem or FeedComment object and look at
the length of the `Body` or `CommentBody`
field to determine the maximum number of
allowed characters.

To edit this property in a comment, use

```
                  updateComment(communityId,
```

`commentId, comment)` . Editing
comments is supported in version 34.0 and later.

Rich text and inline images are supported in
comment bodies in version 35.0 and later. Inline
images in content bodies must use content
document (069) image files previously uploaded
to Salesforce. Entity links are supported in
version 43.0 and later.

```
capabilities

```

#### ConnectApi. Specifies any capabilities for the comment, such Optional 32.0

`CommentCapability` as a file attachment.

```
Input

```


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

`threadParentId` String ID of the parent comment for a threaded Optional 44.0
comment.

SEE ALSO:

[Post a Comment with a Mention](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_2.htm)

[Post a Comment with a New File](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_3.htm)

[Post a Comment with an Existing File](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_4.htm)

[Post a Rich-Text Comment with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_richtext_inlineimage.htm)

[Post a Rich-Text Feed Comment with a Code Block](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_comment_richtext_code_snippet.htm)

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

postCommentToFeedElement(communityId, feedElementId, comment, feedElementFileUpload)

#### ConnectApi.CommerceAddressFieldInput

Commerce address field input. This is used to reference custom fields for the address.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`dataName` String The name of the custom address field. Required 54.0

`text` String The value of the custom address field. Optional 54.0

#### ConnectApi.CommerceAddressInput

Commerce address input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`addressType` String Type of address, for example, `Shipping` Optional 54.0
or `Billing` .

`city` String The address city. Optional 54.0

```
commerceAddress

FieldInputList

```

#### List< ConnectApi. A list of custom address fields, if any. Optional 54.0

```
CommerceAddress
```

`FieldInput` 

`companyName` String The address company name. Optional 57.0

`country` String

The address country, specified using the ISO Optional 54.0
country code. For example, `US` for United
States.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`countryCode` String Two-character country code. For example, Optional 54.0–58.0
US for United States.

`firstName` String The address first name. Optional 57.0

`isDefault` Boolean Indicates whether a contact’s address is the Optional 54.0
preferred method of communication

( `true` ) or not ( `false` ). The default value
is `false` .

`lastName` String The address last name. Optional 57.0

`middleName` String The address middle name. Optional 57.0

`name` String Name of the contact. Required 54.0

`phoneNumber` String The phone number associated with the Optional 57.0
address, including a valid country code. For

example, `+1xxxxxxxxxx` (for a US
number).

`postalCode` String Zip code or postal code for the address. Optional 54.0

`region` String

The address state, specified using the ISO Optional 54.0
state code. For example, CA for California
state.

`regionCode` String The address state code. For example, `CA` Optional 54.0–58.0
for California state.

`street` String The address street. Optional 54.0

#### ConnectApi.CommerceNoteInput

Input representation for a note associated with a quote.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`content` String Comments from both the buyer and sales Optional 67.0
representative on a specific quote.

#### ConnectApi.CompositeCommerceProductInputRepresentation

Composite product input.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### attributeSetInfo ConnectApi. Attribute set information for a variation Optional 62.0

`ProductAttributeSetInputRepresentation` parent product.

`categoryIds` List<String> List of category IDs associated with the Optional 61.0
product.

`productFields` Map<String, String> A map of product field names and their Required 61.0
values.

#### productMedia ConnectApi. Media associated with the product. Optional 61.0

```
            ProductMedia

#### ConnectApi.CompositeCommerceVariationInputRepresentation

```

Composite product variations input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`parentProductId` String ID of the variation parent product. Required 62.0

#### variations List< ConnectApi. List of variation products and their Required 62.0

`ProductVariationInputRepresentation`                            - attributes.

#### ConnectApi.ConfirmHeldFOCapacityInputRepresentation

Request to confirm held fulfillment order capacity at one or more locations. Can correspond to one action call.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
confirmHeldFO

CapacityRequests

```

#### List< ConnectApi. List of requests to confirm held fulfillment Required 55.0

`ConfirmHeldFO` order capacity at one or more locations.

```
CapacityRequest
```

`InputRepresentation` 

#### ConnectApi.ConfirmHeldFOCapacityRequestInputRepresentation

Request to confirm held fulfillment order capacity at one or more locations.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allOrNothing` Boolean Controls whether a single failed request Optional 55.0
cancels all other requests in the list ( _`true`_ )

or whether some requests can succeed if


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

others fail ( _`false`_ ). The default value is
_`false`_ .

List of requests to confirm held fulfillment Required 55.0
order capacity. Each request is for one
fulfillment order assigned to one location.

```
capacityRequests

```

#### List< ConnectApi.

```
CapacityRequest
```

`InputRepresentation` 

#### ConnectApi.ContactPointAttributeInput

Represents the attribute of an activation contact point.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String Label of the attribute. 60.0

`name` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

#### ConnectApi.ContactPointSourceInput

Represents the configuration input for contact point sources.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`dataSourceId` String Record ID of the data source. 60.0

`dataSourcePreference` `ContactPointPrefEnum` Type of contact point. 60.0

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`

**•** `ContactPointPrefPrimary`

`dataSourcePriority` Integer Priority of the data source. 60.0

`id` String ID of the data source. 60.0

`name` String Name of the data source. 60.0

#### ConnectApi.ConnectionDbSchemaCollectionInput

Represents the input for a database schema collection.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`advancedAttributes` Map<String, String>

SEE ALSO:

The database name and other Required 63.0
connector-specific properties that are
required to fetch a list of database schemas.

getDatabaseSchemas(connectionId, getDatabaseSchemasInput)

ConnectApi.ContactPointAttributeInput

Represents the attribute of an activation contact point.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String Label of the attribute. 60.0

`name` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

ConnectApi.ContactPointSourceInput

Represents the configuration input for contact point sources.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`dataSourceId` String Record ID of the data source. 60.0

`dataSourcePreference` `ContactPointPrefEnum` Type of contact point. 60.0

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`

**•** `ContactPointPrefPrimary`

`dataSourcePriority` Integer Priority of the data source. 60.0

`id` String ID of the data source. 60.0

`name` String Name of the data source. 60.0

ConnectApi.ContactPointAttributeInput

Represents the attribute of an activation contact point.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String Label of the attribute. 60.0

`name` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

ConnectApi.ContactPointSourceInput

Represents the configuration input for contact point sources.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`dataSourceId` String Record ID of the data source. 60.0

`dataSourcePreference` `ContactPointPrefEnum` Type of contact point. 60.0

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`

**•** `ContactPointPrefPrimary`

`dataSourcePriority` Integer Priority of the data source. 60.0

`id` String ID of the data source. 60.0

`name` String Name of the data source. 60.0

#### ConnectApi.ContentCapabilityInput

Attach or update a file on a comment. Use this class to attach a new file or update a file that has already been uploaded to Salesforce.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

To attach or remove files from a feed post (instead of a comment) in version 36.0 and later, use ConnectApi.FilesCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`content` String ID of the existing content. Required for existing 32.0
`DocumentId` content

`description` String Description of the file to be uploaded. Optional 32.0

```
sharingOption

```

#### ConnectApi. Sharing option of the file. Values are: Optional 35.0

```
FileSharing
```

**•** `Allowed` —Resharing of the file is

`Option` allowed.

**•** `Restricted` —Resharing of the file
is restricted.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`title` String

SEE ALSO:

Title of the file. This value is used as the file Required for new 32.0
name for new content. For example, if the content
title is My Title, and the file is a .txt file, the
file name is My Title.txt.

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.ContentHubFieldValueInput

Fields of the item type.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String

Name of the item field. Required 39.0

When updating the metadata of a repository
file, only the name field can be updated.

`value` String Value of the item field. Required 39.0

SEE ALSO:

#### ConnectApi.ContentHubItemInput ConnectApi.ContentHubItemInput

Item type ID and fields of the item type.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### fields List< ConnectApi. List of fields for the item. Required to create a 39.0

`ContentHub` SharePoint file in a

`FieldValue` repository because
`Input`        - the file name is
required; otherwise
optional

`itemTypeId` String

ID of the item type, such as Required to create a 39.0
`L3NpdGVzL0FDRVRfRklMRUNPTk5FQ1RfSU5U:` file in a repository

```
5f33e0f4-b33c-4127-b9e4-dd5a73dd2f1b:
```

`0c847e7c-d4a2-4136-bfda-c468fae2d087:0x0101` .

To get the `itemTypeId`, use one of the
`getAllowedItemTypes()` methods.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ContractInputRepresentation

Input to create and update contract.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isAutoDocgenRequired` Boolean Specifies whether automatic document Required 56.0
generation is required or not.

`recordTypeName` String Contract record type name. Optional 56.0

`sourceObjectId` String Source record ID. Required 56.0

`templateName` String Document template name for document Optional 56.0
generation.

#### ConnectApi.CouponCodeRedemptionInput

Input representation for coupon code redemption.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`buyer` String ID of the buyer account or email address for Required 60.0
a guest user.

`couponCodes` List< `String`   - List of coupon codes. Required 58.0

`effectiveAccountId` String ID of the account. Required 58.0–59.0

`transactionId` String ID of the transaction, which must be a valid Required 58.0
cart ID.

#### ConnectApi.CreateCreditMemoInputRepresentation

A list of change orders used to create a credit memo.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeOrderIds` List<String> List of IDs of the change orders. Required 48.0

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

#### ConnectApi.CreateInvoiceFromChangeOrdersInputRepresentation

OrderSummary and associated change orders to create Invoices for.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeOrderIds` List<String> List of IDs of change orders to create Required 56.0
Invoices for.

`orderSummaryId` String ID of the associated Order Summary. Required 56.0

SEE ALSO:

createMultipleInvoices(invoicesInput)

#### ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation

Data about the change orders to create Invoices for.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### invoicesFrom List< ConnectApi. List of OrderSummary IDs with the IDs of Required 56.0

`ChangeOrders` `CreateInvoiceFrom` the associated change orders to create
`ChangeOrders` Invoices for. Each entry in the list generates
`InputRepresentation`                - one invoice, which combines the change
orders in that entry.

SEE ALSO:

createMultipleInvoices(invoicesInput)

#### ConnectApi.CreateOrderPaymentSummaryInputRepresentation

An OrderSummary for which to create an OrderPaymentSummary, with the payment authorization or payments to include in it.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderSummaryId` String ID of the OrderSummary. Required 48.0

`name` String Name of the OrderPaymentSummary. Optional 66.0

`payment` String ID of the payment authorization. Either a payment 48.0
`AuthorizationId` authorization or at
least one payment is
required.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`paymentIds` List<String> List of IDs of the payments. Either a payment 48.0
authorization or at

least one payment is
required.

SEE ALSO:

createOrderPaymentSummary(orderPaymentSummaryInput)

#### ConnectApi.CreateQuoteFromCartInput

Input representation for creating a quote from a cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalFields` Map<String, String> Map of standard and custom Quote fields, Required 66.0
such as expiration date and buyer email.

`comments` String Comments submitted by the buyer when Optional 66.0
requesting a quote.

`contextDefinitionName` String Context defination name provided by the Optional 66.0
buyer when requesting a quote.

`deleteCart` Boolean Indicate whether to delete the cart ( `true` ) Optional 66.0
or not ( `false` ) after the quote is created.

SEE ALSO:

createQuoteFromCart(webstoreId, activeCartOrId, createQuoteFromCartInput)

ConnectApi.CreateQuoteFromCartOutput

#### ConnectApi.CreateQuoteFromProductInput

Input representation for creating a quote from a product.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalFields` Map<String, String> Key-value pairs for quote entity fields, Required 67.0
including both standard and custom fields,

used to set additional quote properties
during creation.

`comments` String

Buyer-provided comments when requesting Optional 67.0
a quote, including special requests, bulk
pricing inquiries, or additional notes.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`contextDefinitionName` String Context definition name for Revenue Cloud Optional 67.0
(RLM) when requesting a quote.

`quantity` String Quantity of the product to include in the Required 67.0
quote.

SEE ALSO:

createQuoteFromProduct(webstoreId, productId, createQuoteFromProductInput)

ConnectApi.CreateQuoteFromProductOutput

#### ConnectApi.CreateServiceAppointmentInput

Contains information to create a service appointment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`assignedResources` <List `ConnectApi.AssignedResourcesInput`    - Represents the service resources to be Optional 53.0
assigned to a service appointment.

Note: When creating an
appointment, use

`extendedFields` to add values
to any of the fields, including custom
fields, in `assignedResources`
as long as you have edit access to
those fields.

`lead` `ConnectApi.LeadInput` Represents a prospect or lead.

Note: Required to create a service
appointment for unauthenticated
guest users.

Required if 53.0

```
serviceAppointment
```

isn’t provided.

`schedulingPolicyId` String The ID of the Optional 53.0

```
                 AppointmentSchedulingPolicy
```

object. If no scheduling policy is passed in
the request body, the default configurations
are used. The only scheduling policy
configuration that is used in determining
time slots is the enforcement of account
visiting hours.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`serviceAppointment` `ConnectApi.ServiceAppointmentInput` Represents the service appointment details Required if `lead` 53.0
to book an appointment. isn’t provided.

Note: When creating an
appointment, use

`extendedFields` to add values
to any of the fields, including custom
fields, in `assignedResources`
as long as you have edit access to
those fields.

#### ConnectApi.CredentialCustomHeaderInput

Credential custom header input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`headerName` String Header name. Required 58.0

`headerValue` String Header value. Required 58.0

`id` String Header ID. Optional 58.0

`sequenceNumber` Integer Sequence number. Required 58.0

SEE ALSO:

ConnectApi.ExternalCredentialInput

ConnectApi.NamedCredentialInput

#### ConnectApi.CredentialInput

Credential input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
authentication

Protocol

```

#### ConnectApi. Authentication protocol of the external Required 56.0

`Credential` credential. Values are:

```
Authentication
```

**•** `AwsSv4`
```
Protocol

```

**•** `AwsSv4`

**•** `Basic`

**•** `Custom`

**•** `Jwt`

**•** `OAuth`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
authentication

ProtocolVariant

credentials

```

`ConnectApi.` Authentication protocol variant of the Optional 57.0
`Credential` external credential. Values are:

```
Authentication
```

**•** `AwsSv4_STS` —AWS Signature

`ProtocolVariant` Version 4 with Security Token Service.

**•** `ClientCredentialsClientSecret` —OAuth
2.0 Client Credentials client secret. Client
secrets are sent in the callout’s request
body.

**•** `ClientCredentialsClientSecretBasic` —OAuth
2.0 Client Credentials client secret. Client
secrets are sent in the callout’s
authorization header, as with Basic
authentication.

**•** `ClientCredentialsJwtAssertion` —OAuth
2.0 Client Credentials JSON Web Token
assertion.

**•** `JwtBearer` —OAuth 2.0 JSON Web
Token bearer flow.

**•** `NoAuthentication` —No
authentication.

**•** `RolesAnywhere` —AWS Signature
Version 4 with Identity and Access
Management (IAM) Roles Anywhere.

If specified, the authentication protocol
variant must match the actual protocol
variant of the external credential.

Map<String,

```
ConnectApi.

Credential
```

`ValueInput` 

Map of protocol-specific credentials. Required 56.0

Authentication protocols have credential
allowlists and encryption rules.

**•** `AwsSv4` - `awsAccessKeyId` (not
encrypted),

```
  awsSecretAccessKey
```

(encrypted), `awsRoleArn` (not
encrypted)

**•** `Custom` —Any credential name is valid
(user sets encryption rules)

`externalCredential` String Fully qualified developer name of the Required 56.0
external credential.

`principalName` String Name of the external credential named Required if 56.0
principal. `principalType`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

is

```
                                     NamedPrincipal

```

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: Required 56.0

```
Credential
```

**•** `AwsStsPrincipal`
```
PrincipalType

```

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`

#### ConnectApi.CredentialValueInput

Credential value input.

Authentication protocols have credential allowlists and encryption rules.

**•** `AwsSv4` - `awsAccessKeyId` (not encrypted), `awsSecretAccessKey` (encrypted), `awsRoleArn` (not encrypted)

**•** `Custom` —Any credential name is valid (user sets encryption rules)

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`encrypted` Boolean Specifies whether the value of the credential Required 56.0
is encrypted ( `true` ) or not ( `false` ).

`revision` Integer Revision number of a short-lived credential, Optional 58.0
such as OAuthToken. If the provided revision

isn’t the latest version, the authentication
endpoint refreshes the credential.

`value` String Value of the credential. Required 56.0

SEE ALSO:

ConnectApi.CredentialInput

#### ConnectApi.CreditMemoInputRepresentation

The credit memo that’s being issued as credit. The specified amount from the credit memo balance is issued as payment credit.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double The amount of the credit memo balance Required 65.0
that’s being issued as credit.

`id` String The ID of the credit memo. Required 65.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CuratedEntityInput

Represents the input details for a curated entity.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String DMO label of the curated entity. 60.0

`name` String DMO API name of the curated entity. 60.0

#### ConnectApi.CustomListAudienceCriteriaInput

Criteria for the custom list type of custom recommendation audience.

Subclass of ConnectApi.AudienceCriteriaInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Required to update 36.0
a recommendation
audience

Don’t use or specify

```
member

OperationType

```

#### ConnectApi. The operation to carry out on the audience

`Recommendation` members. Values are:

```
AudienceMember
```

**•** `Add` —Adds specified members to the

`OperationType` audience.

**•** `Remove` —Removes specified `null` to create a
recommendation
members from the audience.
audience

`members` List<String>

A collection of user IDs.

When updating an audience, you can
include up to 100 members. An audience
can have up to 100,000 members, and each
Experience Cloud site can have up to 100
audiences.

Required to update 36.0
a recommendation
audience

Don’t use or specify

`null` to create a

recommendation
audience

#### ConnectApi.DataConnectorInput

Input details for the data connector.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

outputFormat String Output format for the activation target. Required 60.0

#### ConnectApi.DataSourceNameConfigInput

Represents the data source name configuration input.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Data source API name for the activation. 60.0

#### ConnectApi.DeliveryAddressInputRepresentation

Delivery address.

While each field is optional, at least one combination (latitude and longitude, country and postal code, or city, state, and country) must
be included. The fields can't be left empty.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`city` String City in the state for the delivery address. Optional 63.0

`country` String Country code for the delivery address. Optional 63.0

`latitude` Double Latitude for the delivery address. Optional 63.0

`longitude` Double Longitude for the delivery address. Optional 63.0

`postalCode` String Postal code of the delivery address. Optional 63.0

`state` String State in the country for the delivery address. Optional 63.0

#### ConnectApi.DeliveryEstimationProductInputRepresentation

Delivery estimation product information.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Product name. Optional 63.0

`productId` String ID of the product. Optional 63.0

`quantity` Double Product quantity. Required 63.0

`stockKeepingUnit` String Product's stock keeping unit (SKU). Required 63.0

#### ConnectApi.DeliveryRoutingEngineInputRepresentation

Input for the Delivery Routing Engine, which retrieves routing rules to determine which fulfillment locations should fulfill products for
a given delivery address.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`deliveryAddress` `ConnectApi.DeliveryAddressInputRepresentation` The destination address for delivery. Use a Required 67.0
valid address format.

**•** Coordinates: latitude and longitude

**•** Postal: country code and postal code

**•** Geographic: country code, state, and
city

```
excludeLocations ConnectApi.LocationListInputRepresentation

```

Locations that are excluded from routing Optional 67.0
consideration. Don't leave any identifier
blank. The list can contain up to 100 items.

`fulfillmentCriteria` String The name of the fulfillment criteria group Required 67.0
`GroupName` used for routing.

`locationGroupName` String The name of the location group where Required 67.0
routing is happening.

`products` <List `ConnectApi.RoutingProductInputRepresentation` - The list of products to route. Enter a value Required 67.0
between 1 to 2,000 items.

#### ConnectApi.DirectMessageCapabilityInput

Create or update the members of a direct message.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`membersToAdd` List<String> List of user IDs for members to include in
the direct message.

`membersToRemove` List<String> List of user IDs for members to remove from
the direct message.


Required when 39.0
creating a direct
message (POST)

Optional when
updating a direct
message (PATCH)

Optional when 40.0
updating a direct
message (PATCH)

Not supported when
creating a direct
message (POST)

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`subject` String Subject of the direct message.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.DistinctValueRefinementInput

Attribute-based refinement with distinct values for product search.

This class is a subclass of ConnectApi.RefinementInput.

Optional when 39.0
creating a direct
message (POST)

Not supported when
updating a direct
message (PATCH)

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`values` List<String> Comma-separated list of attribute values. It Required 52.0
considers attribute labels for localization.

#### ConnectApi.DistributePickedQuantitiesInputRepresentation

Input representation to Distribute Picked Quantities

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### distributeToOrders <List ConnectApi.DistributeToOrdersInputRepresentation > List of orders that need quantities 58.0

distributed.

`optimization` String Criteria used for distributing picked 58.0
`Criteria` quantities to orders.

`quantities` <List `ConnectApi.ItemQuantityInputRepresentation` Quantities for each item picked. 58.0
`PickedList` `on page 2106` 
#### ConnectApi.DistributeToOrdersInputRepresentation

Input representation of a single element within the Distribute To Orders list.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalOrderId` String ID of the external order. Required 58.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`itemQuantities` <List `ConnectApi.ItemQuantityInputRepresentation`    - List of order item quantities. Required 58.0

#### ConnectApi.DMOFilterInput

Represents the DMO filter input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`entityFilter` `BaseComparisonInputRepresentation` Entity filter. 60.0

`entityFilterType` String Type of the entity filter. 60.0

`entityName` String Name of the entity. 60.0

`filterLimit` `DmoFilterLimitInputRepresentation` Filter limit. 60.0

`inheritedFilter` `BaseComparisonInputRepresentation` Inherited filter. 60.0

`inheritedFilterType` String Type of the inherited filter. 60.0

`queryPathConfigForActivateOnToContainer` List< Path from the activation to the container. 60.0
`ConnectApi.QueryPathInputConfig`                        

`queryPathConfigFromContainerToEntity` List< Path from the container to the entity. 60.0
`ConnectApi.QueryPathInputConfig`                        
#### ConnectApi.DmoFilterLimitInput

Represents the DMO filter limit input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributeName` String Name of the attribute. 60.0

`maxNumberOfValues` Integer Max number of values to return. 60.0

`order` `FilterSortOrderEnum` The sort order for filtering. 60.0

**•** `FilterSortOrderAsc`

**•** `FilterSortOrderDesc`

#### ConnectApi.DoubleList

List of double values.

Subclass of ConnectApi.AbstractList.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`values` List<Double> List of Double values to filter on. Optional 63.0

#### ConnectApi.EgressPropertiesInput

Represents the input details for egress properties of the activation target.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`childFolder` String

Path of the child folder. The child folder is Optional 60.0
created in the parent directory for copying
activation files.

`customFilename` String Custom name of the output file. Either Optional 60.0
`customFilename` or

`predeterminedFilename` must be
present.

`fileNameType` `EgressFileNameTypeEnum` Type of egress file name. Required 60.0

**•** `Custom`

**•** `Predetermined`

`filenameDateSuffixFormat` String Date suffix format for the output file name. Required 60.0
Use the format

`yyyy-MM-dd-HH-mm-ss` or
`yyyy-MM-dd-HH-mm-ss-SSS` .

`isSubfolderCreationEnabled` Boolean Indicates whether subfolder creation is Optional 60.0
enabled ( `true` ) or not ( `false` ). If `true`,

a custom subfolder is created. The default
is `false` .

`outputCompressionFormat` `CompressionFormatEnum` Compression format for the output file. Required 60.0

**•** `Bzip2`

**•** `Gzip`

**•** `None` -No compression

`outputDelimiter` `FileDelimiterEnum` Field delimiter for the output file. Required 60.0

**•** `BrokenPipe`

**•** `Caret`

**•** `Colon`

**•** `Comma`

**•** `Hash`

**•** `Pipe`

**•** `Semicolon`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `Slash`

**•** `Tab`

**•** `Tilde`

**•** `Underscore`

`outputFormat` String Output format for the activation target. Required 60.0

`outputMaxFileSizeMegaBytes` Long Maximum size of the output file in Required 60.0
megabytes from `1` through `500` .

`outputMaxRecordsPerFile` Long Maximum number of records in the output Required 60.0
file from `1` through `100000` .

`predeterminedFilename` `PreDeterminedFileNameEnum` Predetermined name of the output file. Optional 60.0
Either `customFilename` or

`predeterminedFilename` must be
present.

**•** `Activation`

**•** `Segment`

**•** `SegmentActivation`

ConnectApi.EinsteinLlmAdditionalConfigInput

Additional configuration information for the LLM provider.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
additional

Parameters

```

Map<String, Map of parameters and values for the LLM Optional 60.0
#### ConnectApi. provider.

`WrappedValue` 

`application` String Name of the application. Required 60.0

```
Name

```

`enable` Boolean

```
PiiMasking

```

Specifies whether to mask personally Optional 60.0
identifiable information (PII) ( `true` ) or not
( `false` ).

`frequency` Double Use to reduce the repetitiveness of Optional 60.0
`Penalty` generated tokens. The higher the value, the
stronger a penalty is applied to previously
present tokens, proportional to how many
times they already appeared in the prompt
or in prior generations. Minimum value is
`0.0` . Maximum value is `1.0` .


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`maxTokens` Integer Maximum number of tokens to generate. Optional 60.0

`num` Integer Number of generation requests to send to Optional 60.0
`Generations` the LLM provider.

`presence` Double Use to reduce the repetitiveness of Optional 60.0
`Penalty` generated tokens. This value is similar to
frequency penalty, except that this penalty
is applied equally to all tokens that already
appeared, regardless of their exact
frequencies. Minimum value is `0.0`, and
maximum value is `1.0` .

`stopSequences` List<String> Generated text is cut at the end of the Optional 60.0
earliest occurrence of a stop sequence.

`temperature` Double Sampling temperature to use. Higher values Optional 60.0
mean the model takes more risks. Lower

temperatures mean that generations are
less random. Minimum value is `0.0`, and
maximum value is `1.0`

ConnectApi.EinsteinPromptTemplateGenerationsInput

Prompt template input parameters to use for generation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
additional

Config

```

#### ConnectApi. Configuration information for the LLM Required 60.0

`EinsteinLlm` provider.

```
Additional

ConfigInput

```

`citationMode` String Mode of citations for the specified prompt Optional 62.0
template. Valid values are:

**•** `post_generation` —Citations are
generated after the generated response
for the specified prompt template.

**•** `off` —Citations aren't generated for
the specified prompt template.

`inputParams` Map<String, Parameters and values to resolve the Required 60.0
`ConnectApi.WrappedValue`              - specified prompt template.

`isPreview` Boolean Specifies whether to only resolve the Required 60.0
prompt template ( `true` ) or to resolve the


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

prompt template and generate an LLM
response ( `false` ).

`outputLanguage` String Language code for the language to Optional 61.0
generate the LLM response in. See

[Supported Languages in Prompt Template](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_localize_responses.htm&type=5&language=en_US)
[Responses.](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_localize_responses.htm&type=5&language=en_US)

`tags` ConnectApi.WrappedValue

Map of wrapped values, such as free-form Optional 62.0
user feedback, that can be used to resolve
a specified prompt template.

#### ConnectApi.EnsurePaymentCreditInputRepresentation

The credit memo information and, optionally, the payment sequence details for issuing credits. The credit memo amount is distributed
to the payment methods specified in the payment sequence until the amount is fully applied. If you don’t specify a payment sequence,
the default payment sequence for Ensure Payment is used.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`creditMemo` `CreditMemoInputRepresentation` The credit memo that’s being credited. Required 65.0

`paymentCreditSequence` <List `ConnectApi.PaymentCreditSequenceInputRepresentation` - The ordering sequence of payments being Optional 65.0
used for the payment credit application.

#### ConnectApi.EnsureFundsAsyncInputRepresentation

ID of an Invoice to ensure funds for and apply them to.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`invoiceId` String ID of the Invoice. Required 48.0

`isAllowPartial` Boolean If true, the invoice can be funded through Required 60.0
multiple, partial payments. Optionally,

define a sequence to capture multiple
payments. If false, the invoice must be
funded through a single payment. Default
value is false.

`isConsiderReservedBalanceAmount` Boolean If true, the reserved balance amount is used Optional 59.0
for the Order Summary to fund the invoice.

If not enough reserved balance amount, any
available balance that isn’t reserved by
another Order Summary is used. If false, any
available balance is used.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`sequences` String The payment sequence in which the funds Optional 60.0
are captured for the invoice.

SEE ALSO:

ensureFundsAsync(orderSummaryId, ensureFundsInput)

#### ConnectApi.EnsureRefundsAsyncInputRepresentation

ID of a credit memo to ensure refunds for, an amount of excess funds to refund, or both. At least one is required. Also includes any
invoices for fees that reduce the refund amount, such as return fees. If multiple payment methods are available, you can specify how to
distribute the refund.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`creditMemoId` String ID of the credit memo that represents a Either 48.0
refund amount. `creditMemoId`

or `excessFunds`
`Amount` is required

`excessFunds` Double Amount of excess funds to refund. Either 49.0

```
   Amount excessFunds
```

`Amount` or

```
                                     creditMemoId
```

is required

```
invoicesToPay

```

#### List< ConnectApi. List of invoices for any fees that reduce the Optional 56.0

`InvoiceToPay` refund, such as return fees.
`InputRepresentation` 

`isAllowPartial` Boolean This value controls the behavior when the Optional 56.0
amounts included in the `sequences` list

don’t cover the entire refund amount. If this
value is false, then the default refund logic
is applied to ensure the remaining refund
amount. If this value is true, then the
unrefunded balance remains on the credit
memo. If you don’t specify a `sequences`
list, this value is ignored and the default
refund logic is applied. The default value is
false.

`isReservedBalanceAmountConsidered` Boolean If true, the refundable amount is used to Optional 59.0
open the payment balance for the

reservedBalanceAmount in the Order
Payment Summaries. The remaining
refundable amount considers the sequence


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

of order payment summaries, if provided. If
false, any reserved balance amount for
exchanges is refunded.

#### sequences List< ConnectApi. Ordered list of refund amounts and Optional 56.0

`Sequence` OrderPaymentSummaries to apply them to.

`OrderPaymentSummary` An OrderPaymentSummary must either
`InputRepresentation`                - belong to the order summary or be a
reference to the order summary in the
OrderPaymentSummaryReference entity.
The process traverses this list in order and
stops when it's refunded the full amount.

SEE ALSO:

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

#### ConnectApi.EntityLinkSegmentInput

An entity link segment.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`entityId` String

ID of the entity to link to. Required 43.0

Only users with access to the entity see it.
It’s hidden for users without access.

#### ConnectApi.EstimateDeliveryDateInputRepresentation

Delivery date estimation information.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`deliveryAddress` ConnectApi.DeliveryAddressInputRepresentation Delivery address. Optional 63.0
on page 2073

`locations` String List of location external references. Optional 63.0

`products` ConnectApi.DeliveryEstimationProductInputRepresentation List of products included in delivery Required 63.0
on page 2073 estimation.

`shippingCarrier` ConnectApi.ShippingCa **r** ierInputRepresentation Shipping carrier used to deliver the order. Required 63.0
on page 2173


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ExtendedFieldInput

Contains information about the extended field.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String The name of the field, including custom Optional 53.0
field.

`value` String The value of the field. Optional 53.0

#### ConnectApi.ExtensionInput

An extension.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`alternative` `ConnectApi.AlternativeInput` Alternative representation of the extension. Required 40.0

```
   Representation

```

`extensionId` String ID of the extension. Required 40.0

`payload` String Payload associated with the extension. Required 40.0

`payloadVersion` String

SEE ALSO:

#### ConnectApi.ExtensionsCapabilityInput

Payload version that identifies the structure Optional 40.0
of the payload associated with the
extension.

#### ConnectApi.ExtensionsCapabilityInput

Create or update extensions associated with a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### itemsToAdd List< ConnectApi. List of extensions to associate with the feed

`ExtensionInput`         - element.


Required for creating 40.0
an extension

Optional for
updating an
extension

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`itemsToRemove` List<String> List of attachment IDs to remove from the
feed element.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.ExternalAuthIdentityProviderCredentialInput

External auth identity provider credential input.

Optional for 41.0
updating an
extension

Don’t specify for
creating an
extension

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`credentialName` String Name of the external auth identity provider Required 62.0
credential.

`credentialValue` String Value of the external auth identity provider Required 62.0
credential.

SEE ALSO:

#### ConnectApi.ExternalAuthIdentityProviderCredentialsInput ConnectApi.ExternalAuthIdentityProviderCredentialsInput

External auth identity provider credentials input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
credentials

```

SEE ALSO:

#### <List ConnectApi.ExternalAuthIdentity List of external auth identity provider Required 62.0

`ProviderCredentialInput` credentials to populate.
on page 2084>

createExternalAuthIdentityProviderCredentials(fullName, requestBody)

updateExternalAuthIdentityProviderCredentials(fullName, requestBody)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ExternalAuthIdentityProviderInput

External auth identity provider input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
authenticationFlow

authenticationProtocol

```

#### ConnectApi. Authentication flow to get tokens to call Required 62.0

`IdentityProvider` protected APIs. Values are:
`AuthFlow` on

**•** `AuthorizationCode`

page 2671

**•** `ClientCredentials`

#### ConnectApi. Authentication protocol required to access Required 62.0

`IdentityProvider` the external system. Values are:

```
AuthProtocol
```

**•** `OAuth`

on page 2671

`authorizeUrl` String Authorization endpoint URL for the external Required when the 62.0
system. `authenticationProtocol`

is `OAuth` and the

```
                                  authenticationFlow
```

is
`AuthorizationCode` .
Otherwise, Optional.

```
clientAuthentication

```

#### `ConnectApi.`

```
IdentityProvider

ClientAuth

```

Client authentication method that describes Optional 63.0
how credentials are sent to the
authorization server. Values are:

**•** `ClientSecretBasic`

**•** `ClientSecretPost`

The default value is
`ClientSecretBasic` .

`description` String Description of the external auth identity Optional 62.0
provider.

`fullName` String

Full name of the external auth identity Required 62.0
provider. The full name can include a
namespace prefix.

`label` String External auth identity provider label. Required 62.0

List of custom request parameters to Optional 63.0
customize and extend requests to the
identity provider’s token endpoint.

```
parameters

```

#### List< ConnectApi.

```
ExternalAuth

IdentityProvider
```

`Parameter` 

`standardExternal` String Reference to a standard external auth Optional 63.0
`IdentityProvider` identity provider.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`tokenUrl` String

`userInfoUrl` String

SEE ALSO:

Token endpoint URL to retrieve tokens from Required 62.0
the external system. Required for all OAuth
2.0 authentication flows.

User info URL to retrieve user profile Optional 62.0
information from the external system.

Applicable only when the
`authenticationProtocol` is
`OAuth` .

createExternalAuthIdentityProvider(requestBody)

updateExternalAuthIdentityProvider(developerName, requestBody)

#### ConnectApi.ExternalAuthIdentityProviderParameterInput

External auth identity provider parameter input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`parameterName` String The name of the external auth identity Required 63.0
provider parameter.

```
parameterType

```

#### ConnectApi. Parameter type for an external auth identity Required 63.0

`ExternalAuth` provider. Values are:

```
IdentityProvider
```

**•** `AuthorizeRequestQueryParameter`
```
ParameterType

```

**•** `AuthorizeRequestQueryParameter`

**•** `IdentityProviderOptions`

`parameterValue` String

**•** `ManagedByComponent`

**•** `ManagedByFeature`

**•** `RefreshRequestBodyParameter`

**•** `RefreshRequestHttpHeader`

**•** `RefreshRequestQueryParameter`

**•** `TokenRequestBodyParameter`

**•** `TokenRequestHttpHeader`

**•** `TokenRequestQueryParameter`

If `parameterType` describes a literal Optional 63.0
value then the literal value is stored in this
property.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`sequenceNumber` Integer Specifies the order of parameters to apply Optional 63.0
when an external auth identity provider has

more than one parameter. Priority is from
lower to higher numbers, for example, `1` is
the highest priority.

SEE ALSO:

ConnectApi.ExternalAuthIdentityProviderInput

#### ConnectApi.ExternalCredentialInput

Input used to create or update an external credential.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
authentication

Protocol

authentication

ProtocolVariant

```

#### ConnectApi. Authentication protocol of the external Required 58.0

`Credential` credential. Values are:

```
Authentication
```

**•** `AwsSv4`
```
Protocol

```

**•** `Custom`

**•** `Jwt`

**•** `OAuth`

#### ConnectApi. Authentication protocol variant of the Optional 58.0

`Credential` external credential. Values are:

```
Authentication
```

**•** `AwsSv4_STS` —AWS Signature

`ProtocolVariant` Version 4 with Security Token Service.

**•** `ClientCredentialsClientSecret` —OAuth
2.0 Client Credentials client secret. Client
secrets are sent in the callout’s request
body.

**•** `ClientCredentialsClientSecretBasic` —OAuth
2.0 Client Credentials client secret. Client
secrets are sent in the callout’s
authorization header, as with Basic
authentication.

**•** `ClientCredentialsJwtAssertion` —OAuth
2.0 Client Credentials JSON Web Token
assertion.


**•** `AwsSv4`

**•** `Basic`

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `JwtBearer` —OAuth 2.0 JSON Web
Token bearer flow.

**•** `NoAuthentication` —No
authentication.

**•** `RolesAnywhere` —AWS Signature
Version 4 with Identity and Access
Management (IAM) Roles Anywhere.

If specified, the authentication protocol
variant must match the actual protocol
variant of the external credential.

```
customHeaders

```

#### List< ConnectApi. List of credential custom headers. Optional 58.0

```
CredentialCustom
```

`HeaderInput` 

`developerName` String Fully qualified developer name of the
external credential.

Required for creating 58.0
an external
credential

Optional for
updating an external
credential

`masterLabel` String External credential label. Required 58.0

```
parameters

principals

```

#### List< ConnectApi. List of external credential parameters. Optional depending 58.0

`ExternalCredential` on
`ParameterInput` - `authenticationProtocol`

and

```
                          authenticationVariant

#### List< ConnectApi. List of principals the credential has. Optional 58.0

ExternalCredential
```

`PrincipalInput` 

#### ConnectApi.ExternalCredentialParameterInput

External credential parameter input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String Parameter ID. Optional 58.0

`parameter` String Parameter description. Optional 58.0

```
Description

```

`parameterName` String Parameter name of the external credential. Required 58.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
parameterType

```

#### ConnectApi. Parameter type of the external credential. Required 58.0

`ExternalCredential` Values are:

```
ParameterType
```

**•** `AdditionalRefreshStatusCode`

**•** `AuthParameter`

**•** `AuthProvider`

**•** `AuthProviderUrl`

**•** `AuthProviderUrlQueryParameter`

**•** `JwtBodyClaim`

**•** `JwtHeaderClaim`

**•** `ManagedByComponent`

**•** `ManagedByFeature`

**•** `SfHttpRequestExtensionName`

**•** `SigningCertificate`

`parameterValue` String Parameter value of the external credential. Required 58.0

SEE ALSO:

ConnectApi.ExternalCredentialInput

#### ConnectApi.ExternalCredentialPrincipalInput ConnectApi.ExternalCredentialPrincipalInput

External credential principal input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String ID of the principal external credential Optional 58.0
parameter.

```
parameters

```

#### List< ConnectApi. List of external credential parameters. Optional 58.0

```
ExternalCredential
```

`ParameterInput` 

`principalName` String Principal name. Required 58.0

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: Required 58.0

```
CredentialPrincipal
```

**•** `AwsStsPrincipal`
```
Type

```

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`sequenceNumber` Integer Sequence number. Required 58.0

SEE ALSO:

ConnectApi.ExternalCredentialInput

ConnectApi.NamedCredentialInput

#### ConnectApi.FeedElementCapabilitiesInput

A container for all capabilities that can be included when creating a feed element.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
associated

Actions

bookmarks

canvas

content

directMessage

extensions

feedEntityShare

files

```

#### ConnectApi. Describes actions added to the feed Optional 33.0

`AssociatedActions` element.

```
CapabilityInput

#### ConnectApi. Describes bookmarks added to the feed Optional 32.0
```

`BookmarksCapability` element.

```
Input

#### ConnectApi. Describes a canvas app added to the feed Optional 32.0
```

`CanvasCapability` element.

```
Input

#### ConnectApi. Describes content added to the feed Optional 32.0–35.0
```

`ContentCapability` element.

```
Input
```

Important: This class isn’t available
for feed posts in version 36.0 and
later. In version 36.0 and later, use
ConnectApi.FilesCapabilityInput.

#### ConnectApi. Describes the direct message. Optional 39.0

```
DirectMessage

CapabilityInput

#### ConnectApi. Describes the extensions associated with Optional 40.0
```

`ExtensionsCapability` the feed element.

```
Input

#### ConnectApi. Describes the feed entity shared with the Optional 39.0
```

`FeedEntityShare` feed element.

```
CapabilityInput

#### ConnectApi. Describes files attached to the feed element. Optional 36.0

FilesCapability

Input

```


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
link

poll

questionAnd

Answers

status

topics

```

SEE ALSO:

#### ConnectApi. Describes a link added to the feed element. Optional 32.0

```
LinkCapability

Input

#### ConnectApi. Describes a poll added to the feed element. Optional 32.0

PollCapability

Input

#### ConnectApi. Describes a question and answer capability Optional 32.0
```

`QuestionAndAnswers` added to the feed element.

```
CapabilityInput

#### ConnectApi. Describes the status of the feed element. Optional 44.0

StatusCapability

Input

#### ConnectApi. Describes topics assigned to the feed Optional 38.0
```

`TopicsCapability` element.

```
Input

```

ConnectApi.FeedElementInput

#### ConnectApi.FeedElementCapabilityInput

A feed element capability.

In API version 30.0 and earlier, most feed items can have comments, likes, topics, and so on. In version 31.0 and later, every feed item
(and feed element) can have a unique set of _capabilities_ . If a capability property exists on a feed element, that capability is available, even
if the capability property doesn’t have a value. For example, if the `ChatterLikes` capability property exists on a feed element (with
or without a value), the context user can like that feed element. If the capability property doesn’t exist, it isn’t possible to like that feed
element. A capability can also contain associated data. For example, the `Moderation` capability contains data about moderation
flags.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

This class is a superclass of:

**•** ConnectApi.AssociatedActionsCapabilityInput

**•** ConnectApi.BookmarksCapabilityInput

**•** ConnectApi.CanvasCapabilityInput

**•** ConnectApi.ContentCapabilityInput

**•** ConnectApi.DirectMessageCapabilityInput

**•** ConnectApi.ExtensionsCapabilityInput

**•** ConnectApi.FeedEntityShareCapabilityInput

**•** ConnectApi.FilesCapabilityInput

**•** ConnectApi.LinkCapabilityInput


Apex Reference Guide ConnectApi Input Classes

**•** ConnectApi.MuteCapabilityInput

**•** ConnectApi.PollCapabilityInput

**•** ConnectApi.QuestionAndAnswersCapabilityInput

**•** ConnectApi.ReadByCapabilityInput

**•** ConnectApi.RecordCapabilityInput

**•** ConnectApi.StatusCapabilityInput

**•** ConnectApi.TopicsCapabilityInput

#### ConnectApi.FeedElementInput

Feed elements are the top-level items that a feed contains. Feeds are feed element containers.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

Superclass of ConnectApi.FeedItemInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
capabilities

```

#### ConnectApi. The capabilities that define auxiliary Optional 31.0

`FeedElement` information on this feed element.

```
CapabilitiesInput

```

#### feedElementType ConnectApi. The type of feed element this input

`FeedElementType` represents.


Required when 31.0
creating a feed
element

Optional when
updating a feed
element

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`subjectId` String The ID of the parent this feed element is Required 31.0
being posted to. This value can be the ID of

a user, group, or record, or the string `me` to
indicate the context user.

In version 45.0 and later, you can move a
feed element from one public group to
another by setting this property to the ID of
the new public group. You can’t include or
change any other properties when moving
a feed element.

SEE ALSO:

[Post a Feed Element with a Mention](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_mention.htm)

[Post a Feed Element with Existing Content](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_content.htm)

[Post a Feed Element with a New File (Binary) Attachment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_binary.htm)

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)

[Define an Action Link in a Template and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link_template.htm)

[Share a Feed Element (in Version 39.0 and Later)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_share_feed_element_comment.htm)

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

#### ConnectApi.FeedEntityShareCapabilityInput

Share a feed entity with a feed post or comment.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`feedEntityId` String ID of the feed entity to share with the feed Required 39.0
post or comment.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.FeedItemInput

Used to create rich feed items, for example, feed items that include @mentions or files.

Subclass of ConnectApi.FeedElementInput as of version 31.0.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

```
attachment

body

```

`ConnectApi.Feed` Specifies the attachment for the feed item. The feed Optional 28.0–31.0
`ItemAttachment` item type is inferred based on the provided attachment.

```
Input
```

Important: As of API version 32.0, use the
inherited `capabilities` property.

`ConnectApi.` Message body. The body can contain up to 10,000 Required unless 28.0
`MessageBody` characters and 25 mentions. Because the character the feed item
`Input` limit can change, clients should make a has a link

`describeSObjects()` call on the FeedItem or capability or a
FeedComment object and look at the length of the content
`Body` or `CommentBody` field to determine the capability.
maximum number of allowed characters.

If you specify `originalFeedElementId` to share
a feed item, use the `body` property to add the first
comment to the feed item.

To edit this property in a feed item, use

```
         updateFeedElement(communityId,
```

`feedElementId, feedElement)` . Editing
feed posts is supported in version 34.0 and later.

`isBookmarked` Boolean Specifies if the new feed item should be bookmarked Optional 28.0–31.0
`ByCurrentUser` for the user ( `true` ) or not ( `false` ).

Important: As of API version 32.0, use the

```
                   capabilities.bookmarks.isBookmarkedByCurrentUser
```

property.

`original` String To share a feed element, specify its 18-character ID. Optional 31.0–38.0

```
FeedElementId
```

Important: As of API version 39.0, use the

```
                   capabilities.feedEntity
```

`Share.feedEntityId` property.

`original` String To share a feed item, specify its 18-character ID. Optional 28.0–31.0

```
FeedItemId
```

Important: In API version 32.0–38.0, use the
`originalFeedElementId` property. In
API version 39.0 and later, use the

```
                   capabilities.feedEntity
```

`Share.feedEntityId` property.

`visibility` `ConnectApi.` Type of users who can see a feed item. Optional 28.0

```
       FeedItem
```

**•** `AllUsers` —Visibility is not limited to internal
`VisibilityType` users.
Enum

**•** `InternalUsers` —Visibility is limited to
internal users.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

Default values:

**•** For external users, the default value is `AllUsers` .
External users must use this value to see their posts.

**•** For internal users, the default value is
`InternalUsers` . Internal users can accept this
value or use the value `AllUsers` to allow
external users to see their posts.

If the parent of the feed item is a user, group, or direct
message, the `visibility` of the feed item must
be `AllUsers` .

#### ConnectApi.fetchFilesInput

Input representation for a fetch optimization files operation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`optimizationRequestId` String The ID of the optimization request for which Required 66.0
to retrieve the associated files.

SEE ALSO:

FetchOptimizationFiles(fetchFilesInput)

#### ConnectApi.FileIdInput

Attach a file that has already been uploaded or remove a file from a feed element.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String ID of a file that has already been uploaded. Required 36.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### operationType ConnectApi. Operation to carry out on the file. Values are:

```
         OperationType
```

**•** `Add` —Adds the file to the feed
element.

**•** `Remove` —Removes the file from the
feed element.

`Remove` operations are processed before
`Add` operations. Adding content that is
already added and removing content that
is already removed result in no operation.

SEE ALSO:

#### ConnectApi.FilesCapabilityInput ConnectApi.FilesCapabilityInput

Optional 36.0

If not specified,
defaults to `Add` .

Attach up to 10 files that have already been uploaded or remove one or more files from a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### items List< ConnectApi. List of file IDs and operations to be carried Required 36.0

`FileIdInput`        - out on those files.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.SearchFilter

Filter input for object search.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`field` String Field to use in the filter. Optional 63.0

#### operator ConnectApi. Filter operator. Values are: Optional 63.0

```
         FilterOperator
```

**•** `EqOp` —Equal

**•** `ExcludesOp` —Excludes

**•** `GtOp` —Greater than

**•** `GteOp` —Greater than or equal

**•** `InOp` —In


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `IncludesOp` —Includes

**•** `LikeOp` —Like

**•** `LtOp` —Less than

**•** `LteOp` —Less than or equal

**•** `NeOp` —Not equal

**•** `NinOp` —Not in

#### values List< ConnectApi. Values of the filter, it can be a List of String, Optional 63.0

`AbstractList`           - Boolean, Long, or Double. Do not mix data

types for filter values, for example, `["A",`
`"B", "C"]` is valid, but `["A", -7,`
`false]` isn't.

SEE ALSO:

ConnectApi.SearchRequest

#### ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation

Data used to calculate inventory availability and fulfillment routes for one order involving the fewest number of shipment splits.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`excludeLocations` List< `String`    - List of locations to exclude from the routing Optional 55.0
calculations.

`maximumNumber` Integer

```
OfSplits

```

Maximum allowable number of shipment Required 54.0
splits. Routing options that involve more
than this number of splits are not returned.

Note: Each split represents an
additional shipment. Specifying a
maximum of 0 returns only locations
that can fulfill the entire order in a
single shipment. A maximum of 1
returns combinations of locations
that can fulfill the order in one or two
shipments, and so on.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### orderedItems <List ConnectApi.FindRoutesWithFewestSplits

`UsingOCIItemInputRepresentation`                   

SEE ALSO:

Each list element represents a quantity of a At least one element 54.0
product to be routed for fulfillment and the is required
assigned location group or location.

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

#### ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation ConnectApi.FindRoutesWithFewestSplitsInputRepresentation

Data used to calculate order fulfillment routes involving the fewest number of shipment splits.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Each list element represents the available At least one element 51.0
quantity of a product at an inventory is required
location.

```
locationAvailable

Inventory

```

#### List< ConnectApi.

```
LocationAvailability
```

`InputRepresentation` 

`maximumNumber` Integer The maximum allowable number of Required 51.0
`OfSplits` shipment splits. Routing options that involve
more than this number of splits are not
returned.

Note: Each split represents an
additional shipment. Specifying a
maximum of 0 returns only locations
that can fulfill the entire order in a
single shipment. A maximum of 1
returns combinations of locations
that can fulfill the order in one or two
shipments, and so on.

```
orderedQuantities

```

SEE ALSO:

#### List< ConnectApi. Each list element represents a quantity of a At least one element 51.0

`QuantityWithSku` product to be routed for fulfillment. is required
`InputRepresentation` 

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)

#### ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation

Data used to calculate order fulfillment routes involving the fewest number of shipment splits, taking into account inventory availability.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`findRoutesWithFewestSplitsUsingOCIInputs` < `ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation` List         - Each list element represents a routing At least one element 54.0
request for one order. is required

ociExpandAttributes Collection The string value groupEligibilityExclusion Optional 59.0
excludes specific locations.

SEE ALSO:

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

#### ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation

A quantity of a product and a location group or location assigned to fulfill it.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locationGroup` String The External Reference of the location group Required 54.0
`Identifier` or location assigned to the order item. If you
specify a location group, inventory is
considered for all locations belonging to
that group.

`quantity` Double Quantity of the product. Required 54.0

`stockKeepingUnit` String SKU of the product. Required 54.0

SEE ALSO:

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation

ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation

#### ConnectApi.FormFieldInput

Marketing integration form field.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the marketing integration form Required 53.0
field.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### type ConnectApi. Type of marketing integration form field. Required 53.0

`FormFieldType` Values are:

**•** `Boolean`

**•** `Date`

**•** `EmailAddress`

**•** `Number`

**•** `Text`

SEE ALSO:

#### ConnectApi.FormInput ConnectApi.FormInput

Marketing integration form.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### formFieldsList List< ConnectApi. Fields for the marketing integration form. Required 53.0

`FormFieldInput`            

`formName` String Name of the marketing integration form. Required 53.0

`member` String

```
Identification

Code

```

The member identification code (MID) of Required 53.0
the Marketing Cloud Engagement account
associated with the form.

#### ConnectApi.FormSubmissionFieldInput

Marketing integration form field submission.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the marketing integration form Required 53.0
field.

`value` String Value of the marketing integration form Required 53.0
field.

SEE ALSO:

ConnectApi.FormSubmissionInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.FormSubmissionInput

Marketing integration form submission.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
formFieldsList

```

#### List< ConnectApi. Fields for the marketing integration form. Required 53.0

```
FormField
```

`SubmissionInput` 

#### ConnectApi.FulfillmentGroupInputRepresentation

A list of OrderItemSummaries to be fulfilled together, and the fulfillment location to handle them. The fulfillment type is one of the values
defined for the Type field on the FulfillmentOrder object, such as “Warehouse” or “Retail Store.” The specified type is assigned to the
FulfillmentOrder for this fulfillment group.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fulfilledFrom` String ID of the fulfillment location. Required 48.0

```
LocationId

```

`fulfillmentType` String Fulfillment type. One of the Type field values Required 48.0
defined for FulfillmentOrders.

#### orderItem List< ConnectApi. List of OrderItemSummaries. Required 48.0

```
Summaries OrderItem

         SummaryInput
```

`Representation`         

`referenceId` String Reference to this input for use in Optional 50.0
troubleshooting failures. This value is only

used by the APIs for creating fulfillment
orders for multiple order delivery group
summaries.

SEE ALSO:

#### ConnectApi.FulfillmentOrderInputRepresentation

createFulfillmentOrders(fulfillmentOrderInput)

#### ConnectApi.FulfillmentOrderInputRepresentation

An OrderDeliveryGroupSummary that defines a delivery method and recipient, and a list of fulfillment groups to assign to FulfillmentOrders.
Each fulfillment group is a set of OrderItemSummaries that match the OrderDeliveryGroupSummary and share the same fulfillment
location. The method creates a FulfillmentOrder for each fulfillment group and a FulfillmentOrderLineItem for each OrderItemSummary.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`defaultActivationStatus` String

Optional 58.0
Default activation status for a new fulfillment
order. If you don't specify a value, the default

value is `Allocated`, which belongs to
the `Activated` status category. This
default can be changed, but the
replacement status must also have a status
category of `Activated` .

List of fulfillment groups that specify the Required 48.0
OrderItemSummaries and fulfillment
locations.

```
fulfillmentGroups

```

#### List< ConnectApi.

```
FulfillmentGroup

Input
```

`Representation` 

`orderDelivery` String ID of the OrderDeliveryGroupSummary. Required 48.0

```
GroupSummaryId

```

`orderSummaryId` String ID of the OrderSummary. Required 48.0

SEE ALSO:

createFulfillmentOrders(fulfillmentOrderInput)

#### ConnectApi.FulfillmentOrderInvoiceInputRepresentation

Instantiate and include this object with no properties when creating an invoice.

This input class has no properties.

SEE ALSO:

createInvoice(fulfillmentOrderId, invoiceInput)

#### ConnectApi.FulfillmentOrderLineItemInputRepresentation

A FulfillmentOrderLineItem and quantity to cancel. You can cancel less than the full quantity, in which case you reallocate the canceled
quantity to a different FulfillmentOrder.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fulfillmentOrder` String ID of the FulfillmentOrderLineItem. Required 48.0

```
LineItemId

```


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantity` Double Quantity to cancel. Required 48.0

SEE ALSO:

#### ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation

cancelFulfillmentOrderLineItems(fulfillmentOrderId, cancelFulfillmentOrderLineItemsInput)

#### ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation

A list of FulfillmentOrderLineItems and quantities to cancel.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
fulfillment

OrderLine

ItemsToCancel

```

SEE ALSO:

#### List< ConnectApi. List of FulfillmentOrderLineItems and Required 48.0

`FulfillmentOrder` quantities.

```
LineItemInput
```

`Representation` 

cancelFulfillmentOrderLineItems(fulfillmentOrderId, cancelFulfillmentOrderLineItemsInput)

#### ConnectApi.GetFOCapacityValuesRequestInputRepresentation

Locations to get fulfillment order capacity information for.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locationIds` List<String> List of IDs of the locations to get fulfillment Required 55.0
order capacity information for.

#### ConnectApi.GroupInformationInput

Chatter group information input.

**Property** **Type** **Description** **Available Version**

`text` String The text in the “Information” section of a group. 28.0

`title` String The title of the “Information” section of a group. 28.0

SEE ALSO:

ConnectApi.ChatterGroupInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.HashtagSegmentInput

Include a hashtag in a feed item or comment.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Available Version**

`tag` String Text of the hash tag without the # (hash tag) prefix 28.0

Note: Closing square brackets ( ] ) are not supported in hash
tag text. If the text contains a closing square bracket ( ] ), the
hash tag ends at the bracket.

SEE ALSO:

ConnectApi.MessageBodyInput

#### ConnectApi.HoldFOCapacityInputRepresentation

Request to hold fulfillment order capacity at one or more locations. Can correspond to one action call.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
holdFOCapacity

Requests

```

#### List< ConnectApi. List of requests to hold fulfillment order Required 55.0

`HoldFOCapacity` capacity at one or more locations.

```
RequestInput
```

`Representation` 

#### ConnectApi.HoldFOCapacityRequestInputRepresentation

Request to hold fulfillment order capacity at one or more locations.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allOrNothing` Boolean Controls whether a single failed request Optional 55.0
cancels all other requests in the list ( _`true`_ )

or whether some requests can succeed if
others fail ( _`false`_ ). The default value is
_`false`_ .

List of requests to hold fulfillment order Required 55.0
capacity. Each request is for one fulfillment
order at one location.

```
capacityRequests

```

#### List< ConnectApi.

```
CapacityRequest
```

`InputRepresentation` 

#### ConnectApi.InlineImageSegmentInput

An inline image segment.


Apex Reference Guide ConnectApi Input Classes

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`altText` String Alt text for the inline image.

Optional 35.0

If not specified, the
title of the inline

image file is used as
the alt text.

`fileId` String ID of the inline image file. Required 35.0

SEE ALSO:

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput

#### ConnectApi.InnerEnsureFundsAsyncInputRepresentation

ID of an Invoice and ID of the associated OrderSummary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`invoiceId` String ID of the Invoice to ensure funds for. Required 56.0

`isAllowPartial` Boolean If true, the invoice can be funded through Required 60.0
multiple, partial payments. Optionally,

define a sequence to capture multiple
payments. If false, the invoice must be
funded through a single payment. Default
value is false.

`isConsiderReservedBalanceAmount` Boolean If true, the reserved balance amount is used Optional 59.0
for the Order Summary to fund the invoice.

If not enough reserved balance amount, any
available balance that isn’t reserved by
another Order Summary is used. If false, any
available balance is used.

`orderSummaryId` String ID of the OrderSummary associated with Required 56.0
the Invoice.

`sequences` String The payment sequence in which the funds Optional 60.0
are captured for the invoice.

SEE ALSO:

multipleEnsureFundsAsync(multipleEnsureFundsInput)

ConnectApi.MultipleEnsureFundsAsyncInputRepresentation


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.InviteInput

An invitation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`invitees` List< `String`   - List of email addresses to send the invitation Required 39.0
to.

`message` String Message to include in the invitation. Optional 39.0

#### ConnectApi.InvoiceToPayInputRepresentation

Invoice for a fee.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`invoiceId` String ID of the invoice for a fee. Required 56.0

SEE ALSO:

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

ConnectApi.EnsureRefundsAsyncInputRepresentation

#### ConnectApi.ItemQuantityInputRepresentation

Representation for Item Quantity Input

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalItemId` String ID of the external item. Required 58.0

`quantity` Double Quantity of the external item. Required 58.0

#### ConnectApi.LeadInput

Contains information about a lead or guest user.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`company` String The company of the lead. Optional 53.0

`email` String The email address of the lead. Optional 53.0

`extendedFields` <List `ConnectApi.ExtendedFieldInput`    - Use to add values to any of the fields, Optional 53.0
including custom fields.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`firstName` String The first name of the lead. Optional 53.0

`lastName` String The last name of the lead. Optional 53.0

`phone` String The phone number of the lead. Optional 53.0

#### ConnectApi.LinkCapabilityInput

Create or update a link on a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`url` String Link URL. The URL can be to an external site. Required 32.0

`urlName` String Description of the link. Optional 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.LinkSegmentInput

Include a link segment in a feed item or comment.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Available Version**

`url` String URL to be used for the link 28.0

SEE ALSO:

ConnectApi.MessageBodyInput

#### ConnectApi.LocationAvailabilityInputRepresentation

The available quantity of a product at an inventory location.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalReferenceId` String The external reference ID of the inventory Optional 51.0
location.

`quantity` Double The available quantity of the product. Required 51.0

`stockKeepingUnit` String The Stock Keeping Unit of the product. Required 51.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.LocationInputRepresentation

Inventory location data used to calculate shipping distance.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`countryCode` String The country code of the location. Required 51.0

`locationIdentifier` String The identifier of the location. Required 51.0

`postalCode` String The postal code of the location. Required 51.0

#### ConnectApi.LocationListInputRepresentation

A list of location identifiers used to specify locations excluded from routing consideration.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locations` List<String>

#### ConnectApi.LongList

List of long values.

Subclass of ConnectApi.AbstractList.

The list of location identifiers to exclude. Required 67.0
Don't leave any identifier blank. The list can
contain up to 100 items.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`values` List<Long> List of Long values to filter on. Optional 63.0

#### ConnectApi.ManagedContentBodyInput

Input representation for the body of a piece of managed content.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`nodeMap` `Object` Body of the managed content version. The Required 60.0
format must be Map<String, Object>,

where map values are either primitive values
like String, Integer, Double, Boolean, or
another Map<String, Object>.

SEE ALSO:

ConnectApi.ManagedContentDocumentInput

ConnectApi.ManagedContentVariantUpdateInput

#### ConnectApi.ManagedContentChannelCreateRepresentation

Input class to create a managed content channel.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cacheControlMax` Long Cache control max age value in seconds. Optional 62.0

```
   Age

```

`domain` String ID or name of the domain assigned to the Optional 62.0
public channel.

`isDedicated` Boolean Specifies whether the channel has off-core Optional 63.0
`ContentDelivery` dedicated content delivery enabled ( `true` )
or not ( `false` ). Orgs hosted on Hyperforce
use off-core dedicated content delivery to
deliver content in public channels with high
performance and low latency.

`isDomainLocked` Boolean Specifies whether the domain is locked and Optional 62.0
can’t be changed ( `true` ) or not ( `false` ).

`isSearchable` Boolean

Specifies whether the text contents of the Optional 62.0
channel are searchable ( `true` ) or not
( `false` ).

`mediaCacheControl` Long Media cache control max age value in Optional 62.0
`MaxAge` seconds.

`name` String Name of the managed content channel. Required 62.0

`targetId` String ID of the target associated with the Required for all 62.0
managed content channel. channel types except

```
                                  Public

                                  Unauthenticated

```


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
type

```

SEE ALSO:

#### ConnectApi. Type of managed content channel. Values Required 62.0

`ManagedContent` are:

```
ChannelType
```

**•** `CloudToCloud` —Cloud-to-Cloud
integrated channel.

**•** `Community` —Experience Cloud site
channel.

**•** `ConnectedApp` —Channel served
by a connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is
publicly available.

**•** `UserPermission` —Channel
backed by a system permission. All
published content is available only to
users with the permission.

postManagedContentChannel(ManagedContentCreateInputParam)

#### ConnectApi.ManagedContentChannelUpdateRepresentation

Input class to update a managed content channel.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cacheControlMax` Long Cache control max age value in seconds. Optional 62.0

```
Age

```

`domain` String ID or name of the domain assigned to the Optional 62.0
public channel.

`isDedicated` Boolean Specifies whether the channel has off-core Optional 63.0
`ContentDelivery` dedicated content delivery enabled ( `true` )
or not ( `false` ). Orgs hosted on Hyperforce
use off-core dedicated content delivery to
deliver content in public channels with high
performance and low latency.

`isDomainLocked` Boolean Specifies whether the domain is locked and Optional 62.0
can’t be changed ( `true` ) or not ( `false` ).

`isSearchable` Boolean

Specifies whether the text contents of the Optional 62.0
channel are searchable ( `true` ) or not
( `false` ).


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`mediaCacheControl` Long Media cache control max age value in Optional 62.0
`MaxAge` seconds.

`name` String Name of the managed content channel. Required 62.0

`targetId` String ID of the target associated with the Required for all 62.0
managed content channel. channel types except

```
                                     Public

                                     Unauthenticated

```

SEE ALSO:

patchManagedContentChannel(channelId, ManagedContentChannelInput)

#### ConnectApi.ManagedContentDocumentCloneInput

Managed content clone input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`apiName` String API name of the cloned content. Optional 61.0

`contentSpaceOr` String

```
FolderId

```

`includeVariants` Boolean

`title` String

SEE ALSO:

ID of the target folder for the cloned Optional 61.0
content. If unspecified, defaults to the folder
of the source content.

Specifies whether to include variants Optional 61.0
( `true` ) or not ( `false` ) when cloning the
content. If unspecified, default is `false` .

Title of the cloned content. If unspecified, Optional 61.0
“clone of” is appended to the source
content’s title.

cloneManagedContentDocument(contentKeyOrId, ManagedContentCloneInputParam)

#### ConnectApi.ManagedContentDocumentInput

Input representation for a piece of managed content.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`apiName` String API name of the managed content. Optional 61.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
contentBody

```

#### ConnectApi. Body of the managed content. Required 60.0

```
ManagedContent

BodyInput

```

`contentKey` String Content key to assign to the managed Optional 60.0
content. A content key is a universally

unique identifier (UUID) such as
MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

`contentSpaceOr` String Content space or folder ID where the Required 60.0
`FolderId` content is created.

`contentType` String

Fully qualified name of the content type to Required 60.0
create.

If you’re uploading a binary file using a
multipart/form-data message,

`contentType` must be
`sfdc_cms__image` or
`sfdc_cms__doc` .

You can't create a Form using
`sfdc_cms__form` . The
`sfdc_cms__form` content type isn't
supported.

`externalId` String External ID of the managed content. Optional 60.0

`title` String Title of the managed content. Required 60.0

`urlName` String URL name of the managed content within Optional 60.0
the org.

#### ConnectApi.ManagedContentProviderInstanceInput

Create or update a managed content provider instance.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`instanceKey` String Provider instance key.


Required to create a 65.0
provider instance

At least one property
is required to update
a provider instance.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isDefault` Boolean Specifies whether the instance is the default
instance ( `true` ) or not ( `false` ).

`name` String Name of the provider instance.

`providerLightning` String ID of the provider lightning component.

```
ComponentId

```

SEE ALSO:

updateManagedContentProviderInstance(providerInstanceId, providerInstanceInput)

createManagedContentProvider(providerInstanceInput)

#### ConnectApi.ManagedContentPublishInput

Input for publishing content.

Required to create a 65.0
provider instance

At least one property
is required to update
a provider instance.

Required to create a 65.0
provider instance

At least one property
is required to update
a provider instance.

Required to create a 65.0
provider instance

This property isn’t
supported for

updating a provider
instance.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`contentIds` List<String> IDs of content to publish. All variants of the
content are published.

Required if 60.0
`variantIds` isn’t
specified

`contextContent` String ID of the context workspace. If specified, Optional 61.0
`SpaceId` content from other workspaces is published
if it is shared to the specified workspace. If
unspecified, the context workspace is
derived from the content’s origin workspace.
All content in the request should belong to
the same origin workspace.

`description` String Description for publish action. Optional 60.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`includeContent` Boolean Specifies whether to include content Optional 60.0
`References` references ( `true` ) or not ( `false` ).

`variantIds` List<String> IDs of variants to publish. All variants must
be from the same content space.

#### ConnectApi.ManagedContentSpaceInput

Create a managed content space.

Required if 60.0
`contentIds` isn’t
specified

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`apiName` String API name of the managed content space. Optional 64.0

`defaultLanguage` String Default language of the managed content Optional 64.0
space.

`description` String Description of the managed content space. Optional 64.0

`name` String Name of the managed content space. Required 64.0

```
spaceType

```

SEE ALSO:

#### ConnectApi. Type of managed content space. Values are: Optional 64.0

```
ManagedContent
```

**•** `Content`
```
SpaceType

```

**•** `Content`

**•** `Marketing`

postManagedContentSpace(ManagedContentSpaceInput)

#### ConnectApi.ManagedContentSpaceChannelInputRepresentation

Channel to add or remove from a managed content space.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`channelId` String ID of the channel to add or remove from the Required 62.0
managed content space.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
operation

```

SEE ALSO:

#### ConnectApi. Operation to perform on the channel and Required 62.0

`ManagedContent` managed content space.

```
SpaceChannel
```

**•** `Add` —Add a channel to a managed
`Operation` on
content space.
page 2672

**•** `Remove` —Remove a channel from a
managed content space.

#### ConnectApi.ManagedContentSpaceChannelsInputRepresentation ConnectApi.ManagedContentSpaceChannelsInputRepresentation

Channels to add or remove from the managed content space.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
spaceChannels

```

SEE ALSO:

#### List< ConnectApi. List of channels to add or remove from the Required 62.0

`ManagedContent` managed content space.

```
SpaceChannel

Input
```

`Representation` 

patchManagedContentSpaceChannels(contentSpaceId, spaceChannels)

#### ConnectApi.ManagedContentSpaceUpdateInput

Update the name or description of a managed content space.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`description` String Description of the managed content space. 64.0

`name` String Name of the managed content space. 64.0

SEE ALSO:

patchManagedContentSpace(contentSpaceId, ManagedContentSpaceUpdateInput)

#### ConnectApi.ManagedContentUnpublishInput

Input for unpublishing content.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`contentIds` List<String> IDs of content to unpublish. All variants of
the content are unpublished.

Required if 60.0
`variantIds` isn’t
specified

`contextContent` String ID of the context workspace. If specified, Optional 61.0
`SpaceId` content from other workspaces is
unpublished if it is shared to the specified
workspace. If unspecified, the context
workspace is derived from the content’s
origin workspace. All content in the request
should belong to the same origin
workspace.

`description` String Description for unpublish action. Optional 60.0

`variantIds` List<String> IDs of variants to unpublish. All variants
must be from the same content space.

#### ConnectApi.ManagedContentVariantUpdateInput

Input representation for replacing a managed content variant.

Required if 60.0
`contentIds` isn’t
specified

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`apiName` String API name of the managed content variant. Optional 63.0

```
contentBody

```

#### ConnectApi. Body of the managed content variant. Optional 60.0

```
ManagedContent

BodyInput

```

`title` String Title of the managed content variant. Optional 60.0

`urlName` String URL name of the managed content variant Optional 60.0
within the org.

#### ConnectApi.ManagedTopicPositionCollectionInput

A collection of relative positions of managed topics.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### managedTopic List< ConnectApi. List of relative positions of managed topics. Required 32.0

`Positions` `ManagedTopic` This list can include `Featured` and

`PositionInput`         - `Navigational` managed topics and

doesn’t need to include all managed topics.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

For more information about reordering
managed topics, see the example in
reorderManagedTopics(communityId,
managedTopicPositionCollection).

#### ConnectApi.ManagedTopicPositionInput

Relative position of a managed topic.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`managedTopicId` String ID of existing managed topic. Required 32.0

`position` Integer

SEE ALSO:

Relative position of the managed topic, Required 32.0
indicated by zero-indexed, ascending whole
numbers.

ConnectApi.ManagedTopicPositionCollectionInput

#### ConnectApi.MarkupBeginSegmentInput

The beginning tag for rich text markup.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`altText` String Alternative text for the `Hyperlink` Optional 45.0
segment.

#### markupType ConnectApi. Type of rich text markup. Required 35.0

```
         MarkupType
```

**•** `Bold` —Bold tag.

**•** `Code` —Code tag.

**•** `Hyperlink` —Hyperlink anchor tag.

**•** `Italic` —Italic tag.

**•** `ListItem` —List item tag.

**•** `OrderedList` —Ordered list tag.

**•** `Paragraph` —Paragraph tag.

**•** `Strikethrough` —Strikethrough
tag.

**•** `Underline` —Underline tag.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `UnorderedList` —Unordered list
tag.

Markup segments with a `markupType`
of `Code` can include only text segments.

`url` String

SEE ALSO:

URL for the `Hyperlink` segment. Required for 45.0
Supported hyperlink URLs start with `Hyperlink`
`http://` or `https://` .

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput

#### ConnectApi.MarkupEndSegmentInput

The end tag for rich text markup.

Subclass of ConnectApi.MessageSegmentInput

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### markupType ConnectApi. Type of rich text markup. Required 35.0

```
         MarkupType
```

**•** `Bold` —Bold tag.

**•** `Code` —Code tag.

**•** `Hyperlink` —Hyperlink anchor tag.

**•** `Italic` —Italic tag.

**•** `ListItem` —List item tag.

**•** `OrderedList` —Ordered list tag.

**•** `Paragraph` —Paragraph tag.

**•** `Strikethrough` —Strikethrough
tag.

**•** `Underline` —Underline tag.

**•** `UnorderedList` —Unordered list
tag.

SEE ALSO:

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.MCSFolderShareInput

Target to share a managed content space folder with.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`targetId` String

SEE ALSO:

ID of the target to share the managed Optional 63.0
content space folder with.

Supported target IDs are the root folder IDs
of workspaces. To get the root folder ID for

a space, use the

```
getManagedContentSpace(contentSpaceId)
```

method.

#### ConnectApi.MCSFolderShareCollectionUpdateInput ConnectApi.MCSFolderShareCollectionUpdateInput

Update the targets that a managed content space folder is shared with.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

List of target IDs to share the managed
content space folder with.

Supported target IDs are the root folder IDs
of workspaces. To get the root folder ID for

a space, use the

```
getManagedContentSpace(contentSpaceId)
```

method.

Comma-separated list of target IDs to
unshare the managed content space folder
with.

Required if 63.0

```
unshareWith
```

isn’t specified

Required if 63.0
`shareWith` isn’t
specified

```
shareWith

```

#### List< ConnectApi.

```
MCSFolder
```

`ShareInput` 

`unshareWith` List<String>

SEE ALSO:

getMCSFolderShares(folderId)

#### ConnectApi.MentionSegmentInput

Include an @mention of a user or group in a feed post or comment. When creating a feed post or comment, you can include up to 25
mentions.

Subclass of ConnectApi.MessageSegmentInput.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available Version**

`id` String

`username` String

SEE ALSO:

#### ConnectApi.MessageBodyInput

ID of the user or group to mention.

To mention a user, use either `id` or `username` . You can’t include
both.

To mention a group, you must use `id` .

28.0

Groups are available in 29.0.

User name of the user to mention. 38.0

To mention a user, use either `id` or `username` . You can’t include
both.

#### ConnectApi.MessageBodyInput

Add rich messages to feed items and comments.

**Property** **Type** **Description** **Available Version**

```
messageSegments

```

SEE ALSO:

#### List< ConnectApi. List of message segments contained in the body 28.0

```
MessageSegment
```

`Input` 

ConnectApi.FeedItemInput

ConnectApi.CommentInput

ConnectApi.AnnouncementInput

#### ConnectApi.MessageSegmentInput

Used to add rich message segments to feed items and comments.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

Superclass for:

**•** ConnectApi.EntityLinkSegmentInput

**•** ConnectApi.HashtagSegmentInput

**•** ConnectApi.InlineImageSegmentInput

**•** ConnectApi.LinkSegmentInput

**•** ConnectApi.MarkupBeginSegmentInput

**•** ConnectApi.MarkupEndSegmentInput

**•** ConnectApi.MentionSegmentInput

**•** ConnectApi.TextSegmentInput


Apex Reference Guide ConnectApi Input Classes

[Use the ConnectApiHelper repository on GitHub to simplify many of the tasks accomplished with ConnectApi.MessageSegmentInput,](https://github.com/forcedotcom/ConnectApiHelper)
such as posting with inline images, rich text, and mentions.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
type

```

SEE ALSO:

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

#### ConnectApi. The type of message segment. Values are: Required 23.0

```
MessageSegment
```

**•** `EntityLink`
```
Type

```

**•** `EntityLink`

**•** `FieldChange`

**•** `FieldChangeName`

**•** `FieldChangeValue`

**•** `Hashtag`

**•** `InlineImage`

**•** `Link`

**•** `MarkupBegin`

**•** `MarkupEnd`

**•** `Mention`

**•** `MoreChanges`

**•** `ResourceLink`

**•** `Text`

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput

#### ConnectApi.MultipleEnsureFundsAsyncInputRepresentation

List of Invoices and the associated OrderSummaries.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
asyncInputs

```

SEE ALSO:

#### List< ConnectApi. List of Invoices to ensure funds for and the Required 56.0

`InnerEnsureFunds` associated OrderSummaries.

```
AsyncInput
```

`Representation` 

multipleEnsureFundsAsync(multipleEnsureFundsInput)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.MultipleFulfillmentOrderInputRepresentation

List of inputs for creating fulfillment orders.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
fulfillmentOrders

```

#### List< ConnectApi. Each element contains the data to create Required 50.0

`FulfillmentOrder` one fulfillment order.
`InputRepresentation` 

#### ConnectApi.MultipleFulfillmentOrderInvoicesInputRepresentation

The FulfillmentOrders to create Invoices for.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fulfillmentOrderIds` List<String> List of IDs of FulfillmentOrders to create At least one ID is 52.0
Invoices for. required.

#### ConnectApi.MuteCapabilityInput

Mute or unmute a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isMutedByMe` Boolean

SEE ALSO:

Indicates whether the feed element is Required 35.0
muted for the context user. Default value is

`false` .

setIsMutedByMe(communityId, feedElementId, isMutedByMe)

#### ConnectApi.NamedCredentialCalloutOptionsInput

Named credential callout options input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allowMergeFields` Boolean Specifies whether to allow merge fields in Required 58.0
`InBody` the HTTP body ( `true` ) or not ( `false` ).

`allowMergeFields` Boolean Specifies whether to allow merge fields in Required 58.0
`InHeader` the HTTP header ( `true` ) or not ( `false` ).


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`generate` Boolean

```
Authorization

Header

```

SEE ALSO:

#### ConnectApi.NamedCredentialInput

Specifies whether to generate an Required 58.0
authorization header ( `true` ) or not
( `false` ).

#### ConnectApi.NamedCredentialInput

Input used to create or update a named credential.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
calloutOptions

```

#### ConnectApi. Callout options. Required 58.0

```
NamedCredential

CalloutOptionsInput

```

`calloutUrl` String URL of the named credential in a callout. Required 58.0

```
customHeaders

```

#### List< ConnectApi. Custom HTTP headers. Optional 58.0

```
CredentialCustom
```

`HeaderInput` 

`description` String Description of the named credential. Optional 64.0

`developerName` String Named credential developer name.

Required for creating 58.0
a named credential

Optional for
updating a named
credential

External credentials used by the named Required 58.0
credential. In version 58.0 and later only one
external credential is supported.

```
external

Credentials

```

#### List< ConnectApi.

```
ExternalCredential
```

`Input` 

`masterLabel` String Named credential label. Required 58.0

```
network

Connection

parameters

```

#### ConnectApi. PrivateConnect outbound network Optional depending 58.0

`NetworkConnection` connection. on `type`

```
Input

#### List< ConnectApi. Named credential parameters. Optional 58.0

NamedCredential
```

`ParameterInput` 


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
type

```

#### ConnectApi. Type of named credential. Values are: Required 58.0

```
NamedCredential
```

**•** `PrivateEndpoint`
```
Type
```

**•** `SecuredEndpoint`

#### ConnectApi.NamedCredentialParameterInput

Named credential parameter input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String ID of the parameter. Optional 58.0

`parameter` String Description of the parameter. Optional 58.0

```
Description

```

`parameterName` String Name of the parameter. Required 58.0

```
parameterType

```

#### ConnectApi. Type of named credential parameter. Values Required 58.0

`NamedCredential` are:

```
ParameterType
```

**•** `AllowedManagedPackageNamespaces`

**•** `ClientCertificate`

**•** `ConnectionStatus`

**•** `SfHttpRequestExtensionName`

`parameterValue` String Value of the parameter. Required 58.0

SEE ALSO:

ConnectApi.NamedCredentialInput

#### ConnectApi.NBAStrategyInput

A recommendation strategy.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`contextRecordId` String

ID of the context record. For example, if the Optional 45.0
next best action is on a case detail page, the
ID of the case.

`maxResults` Integer Maximum number of results. Valid values Optional 45.0
are from 1 to 25. The default is 3.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`strategyContext` Map<String, String> Variable and value mappings for the Optional 45.0
strategy.

`debugTrace` Boolean Specifies whether to return trace and debug Optional 45.0
information in the response ( `true` ) or not

( `false` ). If unspecified, the default is

`false` .

#### ConnectApi.NetworkConnectionInput

Network connection input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`developerName` String Developer name of the network connection. Required 58.0

`namespace` String Namespace of the network connection. Optional 58.0

SEE ALSO:

ConnectApi.NamedCredentialInput

#### ConnectApi.NewUserAudienceCriteriaInput

Criteria for the new members type of custom recommendation audience.

Subclass of ConnectApi.AudienceCriteriaInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`value` Double The maximum number of days since a user Required 36.0
became a site member. For example, if you

specify _`30`_, anyone who became a site
member in the last 30 days is included in
the new members audience.

#### ConnectApi.OAuthCredentialAuthUrlInput

OAuth authentication flow.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`external` String Fully qualified developer name of the Required 56.0
`Credential` external credential.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`principalName` String Name of the external credential named Required if 56.0
principal. `principalType`

is

```
                                     NamedPrincipal

```

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: Required 56.0

```
CredentialPrincipal
```

**•** `AwsStsPrincipal`
```
Type

```

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`

`returnUrl` String Return URL to apply to the authentication Optional 56.0
URL.

#### ConnectApi.OCICreateReservationInputRepresentation

Data to reserve inventory at one or more Omnichannel Inventory locations or location groups.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String A UUID that identifies the request. Use the Required 51.0
action request IDs in response data to

identify which requests succeeded or failed.
If the

```
                  OmnichannelInventoryService
```

class's `createReservation` method
is called, the actionRequestId is used for the
reservationId.

`allowPartial` Boolean

```
Reservations

```

When true, if the system can’t create the Optional 51.0
entire reservation, then it attempts to create
a partial reservation.

A list of product quantities and locations or At least one element 51.0
location groups. The list can include up to is required
100 elements.

```
createRecords

```

#### List< ConnectApi.

```
OCICreateReservation

SingleInput
```

`Representation` 

`expirationSeconds` Integer A length of time in seconds. If the Optional 51.0
reservation isn’t fulfilled within this amount

of time after the `reservationTime`,
then it expires. The maximum value is
14400.

`externalRefId` String External reference ID. Optional 51.0

`reservationTime` String The time at which to record the reservation. Optional 51.0
Example: 2020-07-24T21:13:00Z


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.OCICreateReservationSingleInputRepresentation

A quantity of a product and an Omnichannel Inventory location or location group at which to reserve it.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locationGroupIdentifier` String Identifier of the location group at which to Either 51.0
reserve inventory. locationGroupIdentifier

or locationIdentifier
is required, but not
both

`locationIdentifier` String Identifier of the location at which to reserve Either 51.0
inventory. locationGroupIdentifier

or locationIdentifier
is required, but not
both

`quantity` Double The quantity of the product to reserve. Required 51.0

`stockKeepingUnit` String The SKU of the product to reserve. Required 51.0

#### ConnectApi.OCIFulfillReservationInputRepresentation

A list of inventory reservations to fulfill.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
fulfillmentRecords

```

#### List< ConnectApi. A list of inventory reservations. The list can At least one element 51.0

`OCIFulfillReservation` include up to 100 elements. is required.

```
SingleInput
```

`Representation` 

`reservationId` String The ID of the inventory reservation. Optional 58.0

#### ConnectApi.OCIFulfillReservationSingleInputRepresentation

An inventory reservation to fulfill.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String

A UUID that identifies the request. Use the Required 51.0
action request IDs in response data to
identify which requests succeeded or failed.

`externalRefId` String The external reference ID of the location Optional 51.0
that’s fulfilling the reservation.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locationIdentifier` String The identifier of the location that’s fulfilling Required 51.0
the reservation.

`quantity` Double The quantity being fulfilled. Required 51.0

`reservationId` String The ID of the inventory reservation. Optional 58.0

`stockKeepingUnit` String The SKU of the product being fulfilled. Required 51.0

#### ConnectApi.OCIGetInventoryAvailabilityInputRepresentation

Details of a request to retrieve inventory availability.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`includeRelated` Boolean Specifies whether the returned inventory Optional 64.0
`Products` level includes variant products if the given
product has variants. When set to `true`,
only one product ID is accepted. There's a
limit of 100 variant products. If the total of
variants exceeds 100, no variants are
included in the inventory level.

`locationGroup` String The External Reference of a location group Optional; can’t 51.0
`Identifier` to retrieve inventory availability data for. combine with
Specifying this value retrieves inventory data `locationGroupIdentifiers`
for all locations belonging to this group. or

```
                                     locationIdentifiers

```

`locationGroup` List<String> A list of up to 100 External References of Optional; can’t 51.0
`Identifiers` location groups to retrieve inventory combine with

availability data for. `locationGroupIdentifier`

or

```
                                     locationIdentifiers

```

`locationIdentifiers` List<String>

`stockKeepingUnit` String

A list of up to 100 External References of Optional; can’t 51.0
locations to retrieve inventory availability combine with
data for. `locationGroupIdentifier`

or

```
                 locationGroupIdentifiers

```

The SKU of a product to retrieve inventory
availability data for. Specifying a SKU with
no locations or location groups returns
availability data for that SKU at all inventory

locations that aren’t assigned to location
groups.


Optional; can’t 51.0
combine with

```
stockKeepingUnits

```

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`stockKeepingUnits` List<String> A list of up to 100 SKUs of products to
retrieve inventory availability data for.

Optional; can’t 51.0
combine with

```
stockKeepingUnit

```

`useCache` Boolean

Specifies whether to fetch the inventory Optional 51.0
data from the cache. The default value is

`true` .

#### ConnectApi.OCIReleaseReservationInputRepresentation

Details of one or more inventory reservations to release.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
releaseRecords

```

#### List< ConnectApi. List of inventory reservations to release. The At least one element 51.0

`OCIReleaseReservation` list can include up to 100 elements. is required.

```
SingleInput
```

`Representation` 

`reservationId` String The ID of the inventory reservation. Optional 58.0

#### ConnectApi.OCIReleaseReservationSingleInputRepresentation

A single inventory reservation to release.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String

A UUID that identifies the request. Use the Required 51.0
action request IDs in response data to
identify which requests succeeded or failed.

`externalRefId` String The external reference ID of the location or Optional 51.0
location group that has the reservation.

`locationGroupIdentifier` String The identifier of the location group that has The identifier for a 51.0
the reservation. location or location

group, but not both,
is required.

`locationIdentifier` String The identifier of the location that has the The identifier for a 51.0
reservation. location or location

group, but not both,
is required.

`quantity` Double The quantity of reserved inventory to Required 51.0
release.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`reservationId` String The ID of the inventory reservation. Optional 58.0

`stockKeepingUnit` String The SKU of the product to release. Required 51.0

#### ConnectApi.OCITransferReservationInputRepresentation

A list of inventory reservation transfers and specifies whether a single failure cancels the entire list.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allOrNothing` String

```
TransferId

```

Controls whether a single failed transfer Optional 51.0
cancels all other transfers in the
`transferRecords` list.

**•** To allow some transfers in the
`transferRecords` list to succeed
when others fail, don’t include this
property.

**•** To cancel all the transfers in the
`transferRecords` list when any
of them fail, set this property to a UUID.
The ID must be unique, but isn’t
otherwise used in this version.

`reservationId` String The ID of the inventory reservation. Optional 58.0

```
transferRecords

```

#### List< ConnectApi. A list of inventory reservation transfers. The At least one element 51.0

`OCITransferReservation` list can include up to 100 elements. is required.

```
SingleInput
```

`Representation` 

#### ConnectApi.OCITransferReservationSingleInputRepresentation

An inventory reservation transfer.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String

A UUID that identifies the request. Use the Required 51.0
action request IDs in response data to
identify which requests succeeded or failed.

`externalRefId` String The external reference ID of the location Optional 51.0
receiving the transfer.

`fromLocationGroupIdentifier` String The identifier of the location group sending The identifier for a 51.0
the reservation. sending location or


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

location group, but
not both, is required

`fromLocationIdentifier` String The identifier of the location sending the The identifier for a 51.0
reservation. sending location or

location group, but
not both, is required

`ignoreAvailabilityCheck` Boolean

If true, force the transfer even if the receiving Optional 52.0
location doesn’t have sufficient available
inventory. The default value is false.

`quantity` Double The quantity of inventory being transferred. Required 51.0

`reservationId` String The ID of the inventory reservation. Optional 58.0

`stockKeepingUnit` String The SKU of the product being transferred. Required 51.0

`toLocationGroupIdentifier` String The identifier of the location group receiving The identifier for a 51.0
the reservation. receiving location or

location group, but
not both, is required

`toLocationIdentifier` String The identifier of the location receiving the The identifier for a 51.0
reservation. receiving location or

location group, but
not both, is required

#### ConnectApi.OCIUpdateReservationInputRepresentation

Data to update one or more Omnichannel Inventory item reservations.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionRequestId` String

`allowPartialReservations` Boolean

Unique and idempotent action request ID. Required 61.0
Use in response data to identify which
requests succeeded or failed.

When true, if the system can’t update the Optional 61.0
entire reservation, then it attempts to
update a partial reservation.

`externalRefId` String External reference ID. Optional 61.0

`reservationId` String The ID of the inventory reservation. Optional 61.0

`reservationTime` String The time the reservation was updated. Optional 61.0
Example: 2020-07-24T21:13:00Z.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`updateAllOrNothingRecords` List Controls whether a single failed request Optional 61.0
updates all other requests in the list (true)

or whether some requests can succeed if
others fail (false). The default value is false.

A list of product quantities and locations or At least one element 61.0
location groups. The list can have up to 100 is required
elements.

```
updateRecords

```

List
#### ConnectApi.OCIUpdateReservationSingleInputRepresentation

on page 2132 []

#### ConnectApi.OCIUpdateReservationSingleInputRepresentation

Data to update one Omnichannel Inventory reservation item.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`locationGroupIdentifier` String Identifier of the location group where the Either 61.0
inventory is reserved. locationGroupIdentifier

or locationIdentifier
are required, but not
both

`locationIdentifier` String Identifier of the location where the Either 61.0
inventory is reserved. locationGroupIdentifier

or locationIdentifier
are required, but not
both

`quantity` Double The quantity of the product to update. Required 61.0

`stockKeepingUnit` String The SKU of the product to update. Required 61.0

#### ConnectApi.SearchOrderBy

Order by parameter for object search.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`field` String Field to sort the results by. Optional 63.0

#### order ConnectApi. Order direction. Values are: Optional 63.0

```
         SearchOrder
```

**•** `Ascending`

**•** `Descending`

Default value is `Ascending` .


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### orderNulls ConnectApi. Null value order. Values are: Optional 63.0

```
            OrderNulls
```

**•** `Firsts` —Null values are sorted first.

**•** `Lasts` —Null values are sorted last.

Default value is `Firsts` .

SEE ALSO:

ConnectApi.SearchRequest

#### ConnectApi.OrderItemSummaryInputRepresentation

An OrderItemSummary and quantity.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderItem` String ID of the OrderItemSummary. Required 48.0

```
   SummaryId

```

`quantity` Double Quantity to include. Can't contain a fraction Required 48.0
or a decimal.

SEE ALSO:

ConnectApi.FulfillmentGroupInputRepresentation

ConnectApi.FulfillmentOrderInputRepresentation

createFulfillmentOrders(fulfillmentOrderInput)

#### ConnectApi.OrderItemSummaryAdjustmentCollectionInput

Collection of order item summaries.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
orderItem

Summaries

```

#### List< ConnectApi. List of order item summaries. Required 53.0

```
OrderItemSummary
```

`AdjustmentInput` 

#### ConnectApi.OrderItemSummaryAdjustmentInput

Order item summary.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderItem` String ID of the order item summary. Required 53.0

```
   SummaryId

```

SEE ALSO:

ConnectApi.OrderItemSummaryAdjustmentCollectionInput

#### ConnectApi.OrderSummaryAdjustmentAggregatesAsyncInput

Order summary IDs for calculating adjustment aggregates.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderSummaryIds` List< String> List of order summary IDs. Required 55.0

#### ConnectApi.OrderSummaryInputRepresentation

An order from which to create an OrderSummary. Optionally, you can specify OrderSummary-specific information such as its Status and
whether it is managed in Salesforce Order Management.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`businessModel` String The order’s business model. It can have one Optional 53.0
of these values:

**•** B2B

**•** B2C

`externalReference` String Used internally to prevent duplicate records. Optional 56.0
`Identifier` This value is case-sensitive.

`name` String Specifies an OrderNumber to assign to the Optional 50.0
order summary.

`orderId` String ID of the original order. Required 48.0

`orderLifeCycleType` String Specifies whether the order is managed in Optional 49.0
Salesforce Order Management or by an

external system. It can have one of these
values:

**•** `MANAGED` —Managed in Salesforce
Order Management.

**•** `UNMANAGED` —Managed by an
external system.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

If no value is specified, the default is
`MANAGED` .

`sourceProcess` String

Describes the order process creating the Optional 57.0
OrderSummary. It can have one of these
values:

**•** `Exchange—An Exchange`

```
  process.

```

**•** `OrderOnBehalf` —An Order on
Behalf Of process.

**•** `Standard` —Any process other than
Exchange or Order on Behalf Of.

If no value is specified, the default is
`Standard` .

`status` String Specifies a status to assign to the order Optional 50.0
summary. The value must match one of the

picklist values on the Status field of the
OrderSummary object.

SEE ALSO:

createOrderSummary(orderSummaryInput)

#### ConnectApi.OrderSummaryLookupInput

Order summary lookup input.

**Property** **Type** **Description**

**Required** **Available**
**or** **Version**
**Optional**

`orderSummaryIdOrRefNumber` String Either the order Required 58.0
summary ID or

reference number
value.

#### verification ConnectApi.OrderSummaryVerificationInput Verification attributes Optional 58.0

for guest shoppers.

#### ConnectApi.OrderSummaryVerificationInput

Order summary verification input.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`email` String Guest shopper or registered buyer’s email Optional 58.0
address.

`lastName` String Guest shopper or registered buyer’s last Optional 58.0
name.

`phoneNumber` String Guest shopper or registered buyer’s phone Optional 58.0
number.

#### ConnectApi.OrderToCartInput

Input for action adding an order to a cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartStateOrId` String

Cart state ( `active` or `current` ) or the Required 57.0
ID of the cart to which the products from
an order are to be copied.

#### ConnectApi.PaymentCreditSequenceInputRepresentation

The order in which the credit amount is applied to specified payment methods. The sequence determines the order that the credit is
applied to each payment during processing. The amount credited to each payment method is determined in each order payment
summary.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double The amount of the payment credit. Required 65.0

`creditType` String The type of credit to be used. This value is Required 65.0
based on the Credit Type field of the

Payment Credit Transaction, which is
customizable.

`orderPaymentSummaryId` String

An ordered list of payment summaries that Required 65.0
determines what payment methods the
amount is credited to and in what order.

#### ConnectApi.PaymentCreditSequenceItemInputRepresentation

Order Payment Summary ID, credit amount, and credit type for individual payment credit items. Each item represents a specific payment
method and the amount of credit to be applied to it with the type of credit transaction.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`creditType` String

The type of payment credit that will be Required 65.0
issued. Must be a valid value on the Credit
Type picklist.

#### ConnectApi.PaymentGroupRequest

Payment group input consumed by a payment group service.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`createPaymentGroup` Boolean Specifies whether Salesforce needs to create Optional 50.0
a payment group ( `true` ) or not ( `false` ).

`currencyIsoCode` String Three-letter ISO 4217 currency code Optional 50.0
associated with the payment group record.

`id` String ID of the payment group record. Optional 50.0

`sourceObjectId` String Source object ID of the payment group Optional 50.0
record. Supports only OrderId.

#### ConnectApi.PaymentInfoInputRepresentation

Payment information about additional funds required for an order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`lastPaymentGatewayLogId` String Last payment gateway log ID for the new Optional 60.0
order payment summary.

`name` String Overrides the default name of the order Optional 60.0
payment summary created.

`paymentAuthorizationId` String Payment authorization ID to be used if Optional 60.0
needed to fund the exchange order.

`paymentIds` List< `String` - Payment IDs for the new order payment Optional 60.0
summary.

`paymentMethodId` String Payment method ID for the new order Optional 60.0
payment summary.

#### ConnectApi.PaymentInitiationSourceInputRepresentation

Payment initiation source input representation.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### application ConnectApi. Application that initiated this payment, such Optional 63.0

`Application` as Revenue Lifecycle Management (RLM).

`channel` String Channel that submitted the payment. Optional 63.0

`customFields` Map<String, String> Map containing custom field names and Optional 63.0
their corresponding IDs.

`process` String

Process or component of the application Optional 63.0
that submitted the payment, such as the
Billing component of RLM.

`standard` Map<String, String> Map of standard reference fields and their Optional 63.0
`References` corresponding IDs.

#### ConnectApi.PaymentMethodTokenizationRequest

Payment method tokenization input consumed by the payment tokenization service.

Subclass of ConnectApi.BaseRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### address ConnectApi. Address of the payment method. Required 52.0

```
         AddressRequest

```

Required, if 65.0

```
cardPaymentMethod
```

isn't provided.

Required, if 52.0

```
bankPaymentMethod
```

isn't provided.

```
bankPayment

Method

cardPayment

Method

```

#### ConnectApi. Object representation of the bank payment

BankPayment method.
MethodRequest

#### ConnectApi. Object representation of the card payment

`CardPayment` method.

```
MethodRequest

```

`paymentGatewayId` String ID of the card payment method's payment Required 52.0
gateway.

`savedByMerchant` Boolean Indicates whether the payment method Optional 62.0
tokenization is configured to be saved by

merchant ( `true` ) or not ( `false` ). Default
value is `false` .

#### ConnectApi.PhotoInput

Specify how to crop a photo that has already been uploaded.

**Property** **Type** **Description** **Available version**

`cropSize` Integer The length, in pixels, of any edge of the crop square. 29.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available version**

`cropX` Integer The position X, in pixels, from the left edge of the image to the start of 29.0
the crop square. Top left is position (0,0).

`cropY` Integer The position Y, in pixels, from the top edge of the image to the start of 29.0
the crop square. Top left is position (0,0).

`fileId` String 18 character ID of an existing file. The key prefix must be 069 and the file 25.0
must be an image and be smaller than 2 GB.

Note: Images uploaded on the Group page and on the User page
don’t have file IDs and therefore can’t be used.

`versionNumber` Integer Version number of the existing content. If not provided, the latest version 25.0
is used.

SEE ALSO:

setPhotoWithAttributes(communityId, groupId, photo)

setPhotoWithAttributes(communityId, groupId, photo, fileUpload)

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo)

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo, fileUpload)

setPhotoWithAttributes(communityId, userId, photo)

setPhotoWithAttributes(communityId, userId, photo, fileUpload)

#### ConnectApi.PinCapabilityInput

Pin or unpin a feed element to a feed.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`entityId` String ID of the entity to pin or unpin. In version Required 41.0
41.0 and later, `entityId` must be a feed

item ID. In version 41.0–42.0, only one feed
item can be pinned per feed. In version 43.0
and later, three feed items can be pinned
per feed.

`isPinned` Boolean Specifies whether to pin ( `true` ) or unpin Required 41.0
( `false` ) the entity.

#### ConnectApi.PollCapabilityInput

Create, update, or vote on a poll on a feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`choices` List<String> The choices used to create a new poll. You Required for creating 32.0
must specify 2–10 poll choices for each poll. a poll

`myChoiceId` String ID of an existing choice on the feed poll. Required for voting 32.0
Used to vote on an existing poll. on a poll

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.PostAuthApiPaymentMethodRequest

Payment method input for post authorization.

Subclass of ConnectApi.BaseApiPaymentMethodRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
alternativePaymentMethod

cardPaymentMethod

```

#### ConnectApi. Alternative payment method. Required 54.0

```
AlternativePayment

Method

#### ConnectApi. Card payment method. Required 54.0

CardPayment

MethodRequest

```

#### ConnectApi.PostAuthRequest

Payment post authorization input consumed by the payment post authorization service.

Subclass of ConnectApi.BaseRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String ID of the account of the customer for the Required 54.0
authorized payment.

`amount` Double Amount of the post authorization. Required 54.0

`comments` String Comments for payment post authorization. Optional 54.0
Maximum of 1000 characters.

`currencyIsoCode` String Three-letter ISO 4217 currency code Optional 54.0
associated with the payment group record.

`effectiveDate` Datetime Date that the payment post authorization Required 54.0
occurs.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`paymentGatewayId` String Payment gateway that evaluates the post Required 54.0
authorization.

```
paymentGroup

paymentMethod

```

#### ConnectApi. Payment group associated with or to be Optional 54.0

`PaymentGroup` created for the request. Request must
`Request` contain either a paymentGroupId or

paymentGroup, but not both.

#### ConnectApi. Payment method sent for the post Required 54.0

`PostAuthApi` authorization.

```
PaymentMethod

Request

```

#### ConnectApi.PreviewCartToExchangeOrderInputRepresentation

Information required to preview a cart to exchange order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`exchangeCartId` String ID of the cart used for adding items to the Required 60.0
exchange order.

`orderSummaryId` String Order summary ID. Required 60.0

`referenceId` String Return order ID. Required 60.0

`reservationType` String The type of the reservation. Optional 61.0

#### ConnectApi.PricingInput

Pricing for multiple products.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### pricingLineItems List< ConnectApi. Up to 500 line items for pricing. Required 49.0

`PricingLineItemInput`             
#### ConnectApi.PricingLineItemInput

Pricing line item.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`productId` String ID of the product to price. Required 49.0

SEE ALSO:

ConnectApi.PricingInput

#### ConnectApi.ProductSearchGroupingInput

Grouping information for product search results.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
groupingOption

topProductType

```

#### ConnectApi. Grouping option for search results. Values Required 52.0

`CommerceSearch` are:

```
GroupingOption
```

**•** `BestMatch` —Search results are
grouped by the best-match product of
the variation group.

**•** `NoGrouping` —Search results aren’t
grouped.

**•** `VariationParent` —Search results
are grouped by the variation parent.

#### ConnectApi. Type of the top product to return for each Optional 52.0—62.0

`CommerceSearch` product group in search results. Value is:

```
TopProductType
```

**•** `VariationParent`

If `NoGrouping` is specified for
`groupingOption`,
`topProductType` is ignored.

#### ConnectApi.ProductSearchInput

Product search.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`categoryId` String

Category ID returns results for products in
this category or its subcategories. If you omit
`categoryId` from the request, all
categories are searched. If you specify

`categoryId` and `searchTerm`, only
products in the specified category are
searched.


Required if 52.0
`searchTerm` isn’t
specified

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fields` List<String> Product fields to return in search results. Optional 52.0
Search results include fields you have access

to. If unspecified, returns the `Name`,
`Description`, `StockKeepingUnit`,
`ProductCode`, and `Family` fields.

```
grouping

```

#### ConnectApi. Specifies whether to group products in Optional 52.0

`ProductSearch` search results and how to group them. If
`GroupingInput` unspecified, the default is the value

specified in **Search**             - **Results Display**
**Settings**           - **Results Grouping** .

`includePrices` Boolean

Specifies whether to include prices for Optional 52.0
products in search results ( `true` ) or not
( `false` ). If unspecified, defaults to `false` .

`includeQuantity` Boolean Specifies whether to include purchase Optional 52.0
`Rule` quantity rule information for products in
search results ( `true` ) or not ( `false` ). If
unspecified, defaults to `false` .

`page` Integer

Number of the page you want returned. Optional 52.0
Starts at 0. If you pass in `null` or 0, the first
page is returned.

`pageSize` Integer Specifies the number of items per page. Optional 52.0
Valid values are from 1 through 200. If

unspecified, the default is the value
specified in Results per Page in **Search**                        **Results Display Settings** .

#### refinements List< ConnectApi.

`RefinementInput`          

List up to nine refinements (facets) for Optional 52.0
search results. Buyers or shoppers can select
up to 20 values for each refinement.

`searchTerm` String List of up to 32 space-separated search
terms.

Required if 52.0
`categoryId` isn’t
specified

`sortRuleId` String ID of the sort rule that specifies the order of Optional 52.0
products in the search results.

#### ConnectApi.ProductVariationInputRepresentation

Variation product input.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`variationAttributes` Map<String, String> Mapping of variation attributes (API name Required 62.0
and value) associated with the product.

#### ConnectApi.PromotionCartDeliveryGroupInput

IDs of the cart delivery group and its delivery method.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartDelivery` String ID of the cart delivery group. Required 57.0

```
   GroupId

```

`deliveryMethodId` String ID of the order delivery method. Required 57.0

SEE ALSO:

ConnectApi.PromotionEvaluateInput

evaluate(salesTransaction)

#### ConnectApi.PromotionCartInput

Cart during promotion evaluation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
cartAdjustment

Groups

cartDelivery

Groups

cartItems

```

#### ConnectApi. Collection of cart adjustment groups Optional 60.0

PromotionCart associated with the items in the cart.
AdjustmentGroupInput[]

#### List< ConnectApi. A collection of items in the cart. Required 57.0

```
PromotionCart
```

`ItemInput` 

#### ConnectApi.

PromotionCart
DeliveryGroupInput[]

Collection of cart delivery groups associated
with the items in the cart. Available if
shipping promotions are enabled.

Required when 60.0
evaluating shipping
promotions

`currencyIsoCode` String Three-letter ISO 4217 currency code Required for 57.0
associated with the cart. multi-currency orgs

`id` String ID of the cart. Optional 57.0

SEE ALSO:

ConnectApi.PromotionEvaluateInput

evaluate(salesTransaction)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.PromotionCartItemInput

Item in a cart during promotion evaluation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cartDelivery` String ID of the cart delivery group.

```
GroupId

```

Required when 57.0
evaluating shipping
promotions

`cartId` String ID of the cart. Optional 57.0

`id` String ID of the cart item. Must be unique across Required 57.0
all items in the cart.

`itemDescription` String Description of the cart item. Optional 57.0

`itemName` String Name of the cart item. Optional 57.0

`listPrice` String List price of the cart item. Optional 57.0

`product2Id` String Product ID of the cart item. Required if `sku` isn’t 57.0
specified

`quantity` String Number of items in the cart. Required 57.0

`salesPrice` String

Sales price of the cart item. This is the price
per quantity and the value used to compute
the discount. If `salesPrice` and
`totalLineBaseAmount` are specified,
`totalLineBaseAmount` is used.

Required if 57.0

```
totalLineBaseAmount
```

isn’t specified

Required if 57.0
`product2Id` isn’t
specified

`sku` String Stock keeping unit (SKU) of the cart item.

#### subType ConnectApi. Subtype of item in a cart.Possible values are: Optional 64.0

```
         CartItemSubType
```

**•** `Bonus` —A bonus product.

`totalLineBase` String

```
Amount

```

**•** `Gift` —A gift product.

Total amount for the cart item, equal to sales
price multiplied by quantity. This value is
used to compute the discount. If
`salesPrice` and

`totalLineBaseAmount` are specified,
`totalLineBaseAmount` is used.

Required if 57.0
`salesPrice` isn’t
specified

`totalListBase` String Total amount for the cart item based on list Optional 57.0
`Amount` price and quantity.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### type ConnectApi. Type of item in a cart. Values are:

```
         CartItemType
```

**•** `DeliveryCharge`

**•** `Product`

SEE ALSO:

ConnectApi.PromotionCartInput

#### ConnectApi.PromotionEvaluateInput

evaluate(salesTransaction)

#### ConnectApi.PromotionEvaluateInput

Find promotions that the customer is eligible for and compute their discounts.

Required when 57.0
evaluating shipping
promotions

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cart` `ConnectApi.PromotionCart` Cart and its items. Required 57.0

```
         Input

```

`cartDelivery` <List `ConnectApi.PromotionCartDeliveryGroupInput` 
```
Groups

```

`couponCodes` List<String>

List of cart delivery groups associated with
the items in the cart. Available if shipping
promotions are enabled.

Collection of coupon codes to enable Optional 57.0
promotions. A customer can apply a
maximum of two coupons per cart.

Required when 57.0
evaluating shipping
promotions

`effectiveAccount` String ID of the account for which the request is
`Id` made.

Required if 57.0
`segments` isn’t
specified

`isItemizeHeader` Boolean

```
Adjustments

```

Specifies whether order-level adjustments Optional 57.0
are itemized ( `true` ) or not ( `false` ). If
unspecified, the default value is `false` .

```
parentProducts

productCategories

```

#### List< ConnectApi. Collection of parent product IDs mapped to Optional 57.0

`PromotionParent` their variation product IDs.
`ProductsInput` 
#### List< ConnectApi. Collection of product IDs mapped to their Optional 57.0

`PromotionProduct` associated category IDs.
`CategoriesInput` 

`segments` List<String> All promotions associated with promotion Optional 57.0
segments specified in this collection are

active and can be evaluated against the cart.
Additionally, any segments associated with


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

a store or buyer group are also still evaluated
against the cart. If this field is not present,
only the promotions associated with a store
or buyer group are evaluated.

`webStoreId` String

SEE ALSO:

evaluate(salesTransaction)

ID of the store for which the request is Optional 57.0
made. If unspecified, defined segments
must be used instead.

#### ConnectApi.PromotionParentProductsInput

IDs of a parent product and variation product.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`childProductId` String ID of the variation product. Required 57.0

`parentProductId` String ID of the parent product. Required 57.0

SEE ALSO:

ConnectApi.PromotionEvaluateInput

evaluate(salesTransaction)

#### ConnectApi.PromotionProductCategoriesInput

IDs of a product and associated category.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`categoryId` String ID of the category. Required 57.0

`productId` String ID of the product. Required 57.0

SEE ALSO:

ConnectApi.PromotionEvaluateInput

evaluate(salesTransaction)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.QuantityWithSkuInputRepresentation

A quantity of a product.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantity` Double Quantity of the product. Required 51.0

`stockKeepingUnit` String SKU of the product. Required 51.0

#### ConnectApi.QueryPathInput

Represents the query path input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fieldLabel` String Label of the field. 60.0

`fieldName` String Name of the field. 60.0

`objectLabel` String Label of the object. 60.0

`objectName` String Name of the object. 60.0

#### ConnectApi.QueryPathInputConfig

Represents the query path configuration input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### queryPaths List< ConnectApi.QueryPathInput > List of query path configurations. 60.0 ConnectApi.QuerySqlInput

Represents the input to create an SQL query.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`adaptiveTimeout` Integer Amount of time (in seconds) for the query Optional 63.0
engine to respond to the request. `0` will

return the queryId, status, and metadata,
but no data associated with the SQL. The
maximum value is `15` .


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`querySettings` Map<String, String> Settings to adjust the query execution Optional 62.0
behavior:

**•** `date_style` —Order of Year, Month,
and Day for parsing date strings, for
example `MDY` and `DMY` .

**•** `lc_time` —Locale for date literals
using ISO language and country code,
for example `en_US` and `de_AT` .

**•** `query_timeout` —Execution limit
in milliseconds before the query is
terminated, for example `1800000ms` .

`rowLimit` Long Maximum number of rows to include in the Optional 62.0
response. Fewer rows may be returned.

`sql` String SQL expression. Required 62.0

#### sqlParameters <List ConnectApi.QuerySqlParameterItem > Value and type information about the SQL Optional 62.0

parameters.

SEE ALSO:

querySql(input)

querySql(input, dataspace)

querySql(input, workloadName, dataspace)

#### ConnectApi.QuerySqlParameterItem

Represents the parameter fields for an SQL query input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the SQL parameter. Required 62.0

`type` `TypeEnum` Type of the SQL parameter. Required 62.0

**•** `ArrayOfX`

**•** `BigInt`

**•** `Bool`

**•** `Char`

**•** `Date`

**•** `Double`

**•** `Foat`

**•** `Integer`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `Numeric`

**•** `Oid`

**•** `SmallInt`

**•** `Time`

**•** `Timestamp`

**•** `TimestampTZ`

**•** `Unspecified`

**•** `Varchar`

`value` String Value of the SQL parameter. Required 62.0

#### ConnectApi.QuestionAndAnswersCapabilityInput

Create or edit a question feed element or set the best answer of the existing question feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`bestAnswerId` String

`questionTitle` String

SEE ALSO:

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

A comment ID to use as a best answer for a
question feed element. The best answer
comment must already exist on the
question feed element.

Title for a question feed element.

To edit the title of a question, use

```
updateFeedElement(communityId,
```

`feedElementId, feedElement)` .
Editing question titles is supported in
version 34.0 and later.

Required to update 32.0
a feed element.

Not supported when
posting a feed
element.

Required to post a 32.0
feed element.

Not supported when
updating a feed
element.

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.RangeRefinementInput

Attribute-based refinement with minimum or maximum numeric values for product search.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributeType` String Type of search attribute for the refinement. Required 64.0
Values are:

**•** `Custom`

**•** `Standard`

**•** `PricebookEntry`

`max` String Maximum value for range refinement. Required if `min` isn't 64.0
specified

`min` String Minimum value for range refinement. Required if `max` isn't 64.0
specified

`nameOrId` String Developer name of the attribute for the Required 64.0
refinement.

`type` String Type of the refinement. Values is: Required 64.0

**•** `Range`

#### ConnectApi.RankAverageDistanceInputRepresentation

An order recipient’s geographic location and information about sets of inventory locations that can fulfill the order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`deliveryCountryCode` String The country code of the order recipient. Required 51.0

`deliveryPostalCode` String The postal code of the order recipient. Required 51.0

`distanceUnit` String Specify _`mi`_ or _`km`_ to return average 51.0
distances in miles or kilometers, respectively.

`sortResult` String

Specify _`ASC`_ or _`DESC`_ to rank the results 51.0
by average shipping distance in ascending
or descending order, respectively.

```
targetLocations

```

#### List< ConnectApi. Each element is a set of inventory locations At least one element 51.0

`TargetLocation` that can combine to fulfill the order. is required
`InputRepresentation` 

#### ConnectApi.ReadByCapabilityInput

Mark feed elements as read by the context user.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isReadByMe` Boolean Specifies to mark the feed element as read Required 40.0
( `true` ) for the context user.

`lastReadDateByMe` Datetime Specifies the last date, in ISO 8601 format, Optional 40.0
when the feed element is marked as read

for the context user. If you don’t specify a
date or you specify a future date, the current
system date is used.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.SequenceOrderPaymentSummaryInputRepresentation

Amount to apply to specified OrderPaymentSummary as part of a payment or refund.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double Amount to apply to the Optional 56.0
OrderPaymentSummary.

`orderPayment` String ID of the OrderPaymentSummary to apply Required 56.0
`SummaryId` the Amount to.

SEE ALSO:

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

ConnectApi.EnsureRefundsAsyncInputRepresentation

#### ConnectApi.sharedOrderPaymentSummarySequenceInputRepresentation

Shared order payment summary sequence.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderPaymentSummaryId` String Shared order payment summary ID. Required 60.0

`reservedBalanceAmount` Double Balance amount to be reserved. Required 60.0

#### ConnectApi.SubmitCartToExchangeOrderInputRepresentation

Information required for a submit cart to exchange order action.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`exchangeCartId` String ID of the cart used for adding items to the Required 60.0
exchange order.

`orderNumber` String Order number. Optional 60.0

`orderSummaryId` String Order summary ID. Required 60.0

`paymentInfoList` <List `ConnectApi.PaymentInfoInputRepresentation`
`on page 2137`        

List of payment information when additional Optional 60.0
funds are needed for the newly created
exchange order.

`referenceId` String Return order ID. Optional 60.0

`reservationType` String The reservation that's created by the submit Optional 61.0
API. The possible values are Full, which

means there’s a reservation against the
exchange cart, or None if there’s no
reservation.

`sequences` < `ConnectApi.sharedOrderPaymentSummarySequenceInputRepresentation` List
`on page 2152`        

Ordered list of order payment summaries Optional 60.0
and reserved balance amounts to apply
them to.

#### ConnectApi.RecipientEngagementContextInput

Context based on which the survey invitation is sent to a participant.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`recipient` Map<String, String> Map each recipient with the context based Required 50.0
`Engagement` on which the survey invitation is emailed.

```
Context

```

`recipientId` String Participant ID with whom the engagement Required 50.0
context should be associated.

SEE ALSO:

ConnectApi.SurveyInvitationEmailInput

#### ConnectApi.RecommendationAudienceInput

A custom recommendation audience.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`criteria` `ConnectApi.AudienceCriteriaInput` The criteria for the custom recommendation
audience type.

```
memberOperation ConnectApi.
```

Important: This property is
```
Type Recommendation
```
available only in version 35.0. In
```
         AudienceMember
```
version 36.0 and later, use
```
         OperationType
```
ConnectApi.CustomListAudienceCriteriaInput.

Optional 36.0

If not specified when
creating a

recommendation
audience, the
audience criteria
type defaults to
custom list.

Required to update 35.0 only
a recommendation
audience

Don’t use or specify

`null` to create a

The operation to carry out on the audience
recommendation
members.
audience

**•** `Add` —Adds specified members to the
audience.

**•** `Remove` —Removes specified
members from the audience.

`members` List<String>
Important: This property is
available only in version 35.0. In
version 36.0 and later, use
ConnectApi.CustomListAudienceCriteriaInput.

A collection of user IDs.

When updating an audience, you can
include up to 100 members. An audience

can have up to 100,000 members, and each
Experience Cloud site can have up to 100
audiences.

`name` String The unique name of the custom
recommendation audience.

SEE ALSO:

createRecommendationAudience(communityId, recommendationAudience)


Required to update 35.0 only
a recommendation
audience

Don’t use or specify

`null` to create a

recommendation
audience

Optional to update a 35.0
recommendation
audience

Required to create a
recommendation
audience

Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.RecommendationDefinitionInput

A custom recommendation definition.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`actionUrl` String

URL for acting on the custom
recommendation, for example, the URL to
join a group.

Required to create a 35.0
recommendation
definition

Optional to update a
recommendation
definition

Required to create a 35.0
recommendation
definition

Optional to update a
recommendation
definition

Required to create a 35.0
recommendation
definition

Optional to update a
recommendation
definition

Required to create a 35.0
recommendation
definition

Optional to update a
recommendation
definition

`actionUrlName` String Text label for the action URL in the user
interface, for example, “Launch.”

`explanation` String Explanation, or body, of the custom
recommendation.

`name` String Name of the custom recommendation
definition. The name is displayed in Setup.

`title` String Title of the custom recommendation Optional 35.0
definition.

SEE ALSO:

createRecommendationDefinition(communityId, recommendationDefinition)

#### ConnectApi.RecommendationReactionInput

A reaction to a recommendation produced by a recommendation strategy.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`aiModel` String Reserved for future use. Optional 47.0

`contextRecordId` String

ID of the context record. For example, if the Optional 45.0
next best action is on a case detail page, the
ID of the case.

`executionId` String ID of the original recommendation strategy Optional 45.0
execution.

`externalId` String External ID of the recommendation. This ID Optional 46.0
doesn’t need to be a Salesforce 18-character

ID. For example, it can be a product number
from an external system.

`onBehalfOfId` String ID of the user or entity for which the Optional 45.0
reaction took place.

```
reactionType

```

#### ConnectApi. Type of reaction to a recommendation. Required 45.0

`Recommendation` Values are:

```
ReactionType
```

**•** `Accepted`

**•** `Rejected`

`recommendation` String Reserved for future use. Optional 46.0

```
Mode

```

`recommendation` Double Reserved for future use. Optional 46.0

```
Score

```

`strategyName` String Name of the recommendation strategy. Required 45.0

`targetActionId` String ID of the target action. Optional 45.0

`targetActionName` String Name of the target action. Required 45.0

`targetId` String ID of the recommendation that is being Required 45.0
reacted to.

#### ConnectApi.RecordCapabilityInput

Attach an existing knowledge article to a comment.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`recordId` String ID of the existing knowledge article to Required 42.0
attach.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.RecordsetFilterCriteriaInput

A set of recordset filter criteria applied to records, such as service appointment records.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`criteriaIds` List<String> Recordset filter criteria IDs. Required 53.0

`enforceSharing` Boolean

Determines whether record sharing checks Optional 53.0
are enforced ( `true` ) or not ( `false` ) during
the execution of this call.

`filteredObjectName` String Object that the filter is applied to. Required 53.0

`recordIds` List<String> List of record IDs of the filtered object. Required 53.0

SEE ALSO:

evaluateRecordsetFilterCriteria(recordsetFilterCriteriaInput)

#### ConnectApi.ReferencedRefundRequest

Referenced refund input.

Subclass of ConnectApi.RefundRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String ID of the account linked to the referenced Optional 50.0
refund request.

`amount` Double Amount refunded. Required 50.0

`clientContext` String Context for payment APIs. Used for a Optional 50.0
payment caller to re-establish context.

`comments` String Optional comments for the refund. Optional 50.0

`effectiveDate` Datetime Date when the refund becomes effective. Optional 50.0

#### paymentGroup ConnectApi. Payment group details associated with the Optional 50.0

`PaymentGroupRequest` refund request.

#### ConnectApi.RefinementInput

Attribute-based refinement input for product search.

This class is abstract and is a superclass of ConnectApi.DistinctValueRefinementInput.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
attributeType

```

#### ConnectApi. Search attribute type. Required 52.0

```
CommerceSearch
```

**•** `Custom`
```
AttributeType

```

**•** `Custom`

**•** `ProductAttribute`

`nameOrId` String

**•** `Standard`

Developer name of the attribute. In version Required 52.0
52.0 and later, the ID of the attribute isn’t
supported.

```
type

```

#### ConnectApi. Search facet type. Value is: Required 52.0

```
CommerceSearch
```

**•** `DistinctValue`
```
FacetType

```

**•** `DistinctValue`

**•** `Range`

#### ConnectApi.RefundInstructionsHintInputRepresentation

The payment credit sequence, credit types, and refund sequence that provide information for optimal refund processing.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`paymentCreditSequenceItems` List< The Order Payment Summary ID, credit Required 65.0
`ConnectApi.PaymentCreditSequenceItemInputRepresentation`                                 - amount, and credit type for individual

payment credit items. Each item represents
a specific payment method and the amount
of credit to be applied to it.

`refundSequenceItems` <List `ConnectApi.RefundSequenceItemInputRepresentation` - The Order Payment Summary ID and Required 65.0
amount for the individual refund items in a

sequence. Each item has a payment method
and refund amount to be processed for that
method.

#### ConnectApi.RefundRequest

Refund input.

This class is abstract.

Subclass of ConnectApi.BaseRequest.

No additional properties.

Superclass of ConnectApi.ReferencedRefundRequest.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.RefundSequenceItemInputRepresentation

The Order Payment Summary ID and amount for the individual refund items in a sequence. Each item has a payment method and refund
amount to be processed for that method.

Subclass of ConnectApi.AbstractBaseSequenceInputRepresentation.

#### ConnectApi.ReleaseHeldFOCapacityInputRepresentation

Request to release held fulfillment order capacity at one or more locations. Can correspond to one action call.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
releaseHeldFO

CapacityRequests

```

#### List< ConnectApi. List of requests to release held fulfillment Required 55.0

`ReleaseHeldFO` order capacity at one or more locations.

```
CapacityRequest
```

`InputRepresentation` 

#### ConnectApi.ReleaseHeldFOCapacityRequestInputRepresentation

Request to release held fulfillment order capacity at one or more locations.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allOrNothing` Boolean Controls whether a single failed request Optional 55.0
cancels all other requests in the list ( _`true`_ )

or whether some requests can succeed if
others fail ( _`false`_ ). The default value is
_`false`_ .

```
capacityRequests

```

#### List< ConnectApi. List of requests to release held fulfillment Required 55.0

`CapacityRequest` order capacity. Each request is for capacity
`InputRepresentation` - for one fulfillment order held at one

location.

#### ConnectApi.RequestHeaderInput

An HTTP request header name and value pair.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String The name of the request header. Required 33.0

`value` String The value of the request header. Required 33.0

SEE ALSO:

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ReturnItemsInputRepresentation

Data about products and delivery charges to return, as well as associated return fees.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

The payment credit sequence, credit types, Optional 65.0
and refund sequence that provide
information for optimal refund processing.

```
refundInstructionsHint

returnOrderItem

DeliveryCharges

returnOrderItemFees

returnOrderItems

```

SEE ALSO:

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.`

```
RefundInstructionsHint

InputRepresentation>

```

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.` List of ReturnOrderLineItems to return that Optional 52.0
`ReturnOrderItem` represent delivery charges.

```
DeliveryCharge

InputRepresentation>

```

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.` List of ReturnOrderLineItems to process that Optional 56.0
`ReturnOrderItemFee` represent return fees.

```
InputRepresentation>

```

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.`

```
ReturnOrderItem

InputRepresentation>

```

List of ReturnOrderLineItems to process that Required 52.0
represent products, along with data about
how to process them.

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderInputRepresentation

Data for creating a ReturnOrder and ReturnOrderLineItems.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderSummaryId` [String](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm)

ID of the OrderSummary containing the Required 50.0
items to be returned. The OrderSummary’s
OrderLifeCycleType must be Managed.

The payment credit sequence, credit types, Optional 65.0
and refund sequence that provide
information for optimal refund processing.

```
refundInstructionsHint

```

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.`

```
RefundInstructionsHint

InputRepresentation>

```

`returnOrder` [String](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm) The LifeCycleType of the ReturnOrder. Required 51.0
`LifeCycleType` Possible values are:

**•** Managed—Process the ReturnOrder
using the APIs and actions. It can
generate change orders and affects
financial fields and rollup calculations.

**•** Unmanaged—The ReturnOrder is for
tracking purposes only. It isn’t involved


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

in any financial calculations and doesn’t
generate any change orders. The system
doesn’t prevent the creation of
duplicate ReturnOrderLineItems in an
unmanaged ReturnOrder for the same
OrderItem.

```
returnOrderLineItems

```

[List](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm) `<ConnectApi.` List of data for creating At least one element 50.0
`ReturnOrderLineItem` ReturnOrderLineItems. is required

```
InputRepresentation>

```

`status` [String](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm)

SEE ALSO:

createReturnOrder(returnOrderInput)

Status to assign the ReturnOrder. This value Required 51.0
must match an entry in the ReturnOrder
object’s Status picklist.

#### ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation

ID of a ReturnOrderLineItem representing a delivery charge.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`returnOrder` String ID of a ReturnOrderLineItem to return. Required 52.0

```
LineItemId

```

SEE ALSO:

ConnectApi.ReturnItemsInputRepresentation

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderItemFeeInputRepresentation

ID of a ReturnOrderLineItem representing a return fee, and instructions for updating it. After the update, the ReturnOrderLineItem is
read-only. Any remaining quantity of the fee to be processed is added to a new ReturnOrderLineItem.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantityReturned` Double Quantity of the ReturnOrderLineItem to Required 56.0
process. When the fee is a fixed amount, the

charge is determined by multiplying the
total fee amount by this value divided by
the expected quantity. For example, if the


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

fee amount is $10 and the expected
quantity is 2, then if the
`quantityReturned` is 1, $5 is charged.
This value normally equals the quantity
returned of the ReturnOrderLineItem for the
returned item that the fee applies to. The
value must be greater than zero. If this value
plus `quantityToCancel` is less than
the expected quantity, then the remaining
quantity to be returned is added to a new
ReturnOrderLineItem.

`quantityToCancel` Double Quantity of the ReturnOrderLineItem to Required 56.0
remove. This value normally equals the

quantity canceled of the
ReturnOrderLineItem for the returned item
that the fee applies to. This value can also
be used to cancel a portion of the fee. The
value must be zero or greater. If this value
plus `quantityReturned` is less than
the expected quantity, then the remaining
quantity to be returned is added to a new
ReturnOrderLineItem.

`returnOrder` String ID of the ReturnOrderLineItem representing Required 56.0
`LineItemId` the return fee.

SEE ALSO:

ConnectApi.ReturnItemsInputRepresentation

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderItemInputRepresentation

ID of a ReturnOrderLineItem and instructions for updating it. After the update, the ReturnOrderLineItem is read-only. Any remaining
quantity to be returned is added to a new ReturnOrderLineItem.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantityReceived` Double The quantity of the ReturnOrderLineItem Optional 52.0
that has been received. The value must be

zero or greater. This value isn’t used by any
standard features, but is provided for use in
customizations.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantityRejected` Double The quantity of the ReturnOrderLineItem Optional 52.0
that has been rejected for return. The value

must be zero or greater. This value isn’t used
by any standard features, but is provided for
use in customizations.

`quantityReturned` Double The quantity of the ReturnOrderLineItem Required 52.0
that has been returned. The value must be

greater than zero. If this value plus
quantityToCancel is less than the expected
return quantity, then the remaining quantity
to be returned is added to a new
ReturnOrderLineItem.

`quantityToCancel` Double The quantity of the ReturnOrderLineItem to Optional 52.0
remove because it’s not being returned. The

value must be zero or greater. If this value
plus quantityReturned is less than the
expected return quantity, then the
remaining quantity to be returned is added
to a new ReturnOrderLineItem.

`reasonForRejection` String The reason why the rejected quantity, if any, Optional 52.0
was rejected. This value isn’t used by any

standard features, but is provided for use in
customizations.

`returnOrder` String The ID of the ReturnOrderLineItem. Required 52.0

```
   LineItemId

```

SEE ALSO:

ConnectApi.ReturnItemsInputRepresentation

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderLineItemInputRepresentation

Data for creating a ReturnOrderLineItem for an order item being returned, including data to create ReturnOrderLineItems representing
any return fees associated with it.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`canReduceShipping` Boolean Whether to refund any associated shipping Required 50.0
charge.

`orderItemSummaryId` String ID of the associated OrderItemSummary. If Required 50.0
the OrderItemSummary already has an


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

associated ReturnOrderLineItem, then you
must specify a different
`reasonForReturn` . Duplicating the
reason breaks the financial calculations.

`quantityExpected` Double

Quantity expected to be returned. This value Required 50.0
also applies to any fees specified in
`returnOrderLineItemFees` .

`quantityReceived` Double Quantity already physically returned. Optional 50.0

`reasonForReturn` String

Reason for the return. The value must match Required if the 50.0
an entry in both the OrderSummaryChange `returnOrder`
Reason field and the ReturnOrderLineItem `LifeCycleType`
object’s ReasonForReturn picklist. is MANAGED.

#### returnOrder List< ConnectApi. List of input data for return fees associated Optional 56.0

`LineItemFees` `ReturnOrder` with the order item being returned. A
`LineItemFee` ReturnOrderLineItem of Type Fee is created
`InputRepresentation`            - to represent each fee.

SEE ALSO:

ConnectApi.ReturnOrderInputRepresentation

createReturnOrder(returnOrderInput)

#### ConnectApi.ReturnOrderLineItemFeeInputRepresentation

Data for creating a ReturnOrderLineItem that represents a return fee.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double

Value used to calculate the fee amount, as Required 56.0
described by the `amountType` . It must
be a positive value.

`amountType` String Describes how the fee amount is calculated. Required 56.0
It can have one of these values:

**•** `AmountTaxOnly` —Value of
`amount` is the tax-only adjustment
only. Available in version 65.0 and later.

**•** `AmountWithTax` —Value of
`amount` is the fee amount, including
tax.

**•** `AmountWithoutTax` —Value of
`amount` is the fee amount, not


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

including tax. Tax is calculated on the
value and added.

**•** `Percentage` —Value of `amount` is
a percentage. To determine the fee
amount, `amount` is divided by 100,
and then multiplied by the TotalPrice
and TotalTaxAmount of the associated
OrderItemSummary, prorated for the
quantity being returned.

**•** `PercentageGross` —Value of
`amount` is a percentage. To determine
the fee amount, `amount` is divided by
100, and then multiplied by the
TotalLineAmountWithTax of the
associated OrderItemSummary,
prorated for the quantity being
returned.

**•** `ProductOnly` —Value of `amount`
is the product-only adjustment only.
Available in version 65.0 and later.

`description` String Description of the fee. Required 56.0

`product2Id` String ID of the product representing the fee. Required 56.0

`reason` String

SEE ALSO:

Reason for the fee. The value must match Required 56.0
an entry in the ReturnOrderLineItem object’s
ReasonForReturn picklist.

ConnectApi.ReturnOrderInputRepresentation

createReturnOrder(returnOrderInput)

ConnectApi.ReturnOrderLineItemInputRepresentation

#### ConnectApi.RoutingProductInputRepresentation

A product to route, including its SKU and requested quantity.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`quantity` Double The quantity of the requested product. Enter Required 67.0
a value greater than 0.

`stockKeepingUnit` String The product's stock keeping unit (SKU). Required 67.0


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.SaleApiPaymentMethodRequest

Payment method request for sale.

Subclass of ConnectApi.BaseApiPaymentMethodRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`cardPaymentMethod` `ConnectApi.CardPaymentMethodRequest` Payment method used in a sale request. Required 54.0

#### ConnectApi.SaleRequest

Payment sale input consumed by the payment sale service.

Subclass of ConnectApi.BaseRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String Reference to account. Required 54.0

`amount` Double The amount of the sale request. Required 54.0

`comments` String Optional comment for the sale request. Optional 54.0

`currencyIsoCode` String Three-letter ISO 4217 currency code Required 54.0
associated with the payment output.

`effectiveDate` Datetime Date that the sale request takes effect. Required 54.0

`submittedBy` Boolean

```
Merchant

```

Indicates whether the sale request is Optional 62.0
submitted by the merchant ( `true` ) or not
( `false` ). Default value is `false`,

`paymentGatewayId` String The payment gateway that receives the sale Required 54.0
request.

`paymentGroup` `ConnectApi.Payment` Payment group information for the sale Optional 54.0
`GroupRequest` request.

```
paymentMethod

```

#### ConnectApi.SaleApi Payment method used within the sale Reqiured 54.0

`PaymentMethod` request.

```
Request

```

#### ConnectApi.ScheduledRecommendationInput

A scheduled custom recommendation.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

Optional for creating 36.0
a scheduled
recommendation

If not specified,
defaults to
`DefaultChannel` .

```
channel

```

```
ConnectApi.

Recommendation

Channel

```

A way to tie custom recommendations
together. For example, display
recommendations in specific places in the
UI or show recommendations based on time
of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom `DefaultChannel`
recommendation channel. Not used by Don’t use when
default. Work with your community
updating a
manager to define custom channels.
scheduled
For example, community managers can
recommendation
use Experience Builder to determine
where recommendations appear.

**•** `CustomChannel2` —Custom
recommendation channel. Not used by
default. Work with your community
manager to define custom channels.

**•** `CustomChannel3` —Custom
recommendation channel. Not used by
default. Work with your community
manager to define custom channels.

**•** `CustomChannel4` —Custom
recommendation channel. Not used by
default. Work with your community
manager to define custom channels.

**•** `CustomChannel5` —Custom
recommendation channel. Not used by
default. Work with your community
manager to define custom channels.

**•** `DefaultChannel` —Default
recommendation channel.
Recommendations appear by default
on the Home and Question Detail pages
of Customer Service and Partner Central
Experience Builder templates. They also
appear in the feed in the Salesforce
mobile web and anywhere community
managers add recommendations using
Experience Builder.

Use these channel values; you can’t rename
or create other channels.

`enabled` Boolean Indicates whether scheduling is enabled. If Optional 35.0
`true`, the custom recommendation is

enabled and appears in Experience Cloud
sites. If `false`, custom recommendations


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

in feeds in Salesforce mobile web aren’t
removed, but no new custom
recommendations appear. In Customer
Service and Partner Central sites, disabled
custom recommendations no longer
appear.

`rank` Integer

Relative rank of the scheduled custom Optional 35.0
recommendation indicated by ascending
whole numbers starting with 1.

Setting the rank is comparable to an
insertion into an ordered list. The scheduled

custom recommendation is inserted into
the position specified by the `rank` . The
`rank` of all the scheduled custom
recommendations after it is pushed down.
See Ranking scheduled custom
recommendations example.

If the specified `rank` is larger than the size
of the list, the scheduled custom
recommendation is put at the end of the
list. The `rank` of the scheduled custom
recommendation is the size of the list,
instead of the one specified.

If a `rank` is not specified, the scheduled
custom recommendation is put at the end
of the list.

`recommendation` String ID of the audience for this scheduled custom Optional 35.0
`AudienceId` recommendation.When updating a
scheduled custom recommendation, specify
`ALL` to remove the association between a
custom recommendation audience and a
scheduled custom recommendation.

`recommendation` String

```
DefinitionId

```

ID of the custom recommendation
definition that this scheduled
recommendation schedules.


Required to create a 35.0
scheduled
recommendation

You can’t specify a

```
recommendation

DefinitionId
```

when updating a
scheduled
recommendation.

Apex Reference Guide ConnectApi Input Classes

**Ranking scheduled custom recommendations example**

If you have these scheduled custom recommendations:

**Scheduled Recommendations** **Rank**

ScheduledRecommendationA 1

ScheduledRecommendationB 2

ScheduledRecommendationC 3

And you include this information in the Scheduled Custom Recommendation Input:

**Scheduled Recommendation** **Rank**

ScheduledRecommendationD 2

The result is:

**Scheduled Recommendation** **Rank**

ScheduledRecommendationA 1

ScheduledRecommendationD 2

ScheduledRecommendationB 3

ScheduledRecommendationC 4

SEE ALSO:

createScheduledRecommendation(communityId, scheduledRecommendation)

#### ConnectApi.SearchDataCategory

Data category input for object search.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`categories` List<String> List of data category names to filter. Optional 63.0

`groupName` String Name of the data category group to filter. Optional 63.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
operator

```

SEE ALSO:

#### ConnectApi. Data category operator. Optional 63.0

```
DataCategory
```

**•** `Above` —Queries the data category

`Operator` and all of its parent categories.

**•** `AboveOrBelow` —Queries the data
category, all of its parent categories, and
all of its subcategories.

**•** `At` —Queries the data category.

**•** `Below` —Queries the data category
and all of its subcategories.

#### ConnectApi.SearchRequest ConnectApi.SearchRequest

Search request input for searching an object.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`q` String Query term to search on. Query term must Required 63.0
be two or more characters.

`configurationName` String

Name of the search configuration to apply. Optional 63.0
Look up search configuration names from
Search Manager.

```
dataCategories

```

#### List< ConnectApi. List of data categories to filter. Optional 63.0

```
SearchData
```

`Category` 

`displayFields` List<String>

List of fields to display and return in the Optional 63.0
search results. By default, the fields displayed
are defined by the search layout.

#### filters List< ConnectApi. List of filters to apply. Optional 63.0

`SearchFilter`        

`highlights` Boolean

`offset` Integer

Specifies whether search generates a text Optional 63.0
highlight ( `true` ) or not ( `false` ). The
default value is `false` .

Search page offset position. Default value is Optional 63.0
`0`, which indicates displaying results from
the beginning without skipping any entries.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### orderBy List< ConnectApi. Order by input for object search. Optional 63.0

`SearchOrderBy`           

`pageSize` Integer

`spellcheck` Boolean

SEE ALSO:

find(objectApiName, request)

Number of results in a page. Valid values are Optional 63.0
from 1 through 1999. If unspecified the
default value is `20` .

Specifies whether search should apply Optional 63.0
spellcheck ( `true` ) or not ( `false` ). The
default value is `true` .

#### ConnectApi.SellerDetailsRequest

Seller details for the tax calculation

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`code` String Code used to identify the seller of the taxed 55.0
items.

#### ConnectApi.ServiceAppointmentInput

Contains information about the service appointment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalInformation` String Additional details about the service Optional 53.0
appointment.

`appointmentMode` ConnectApi.SvcApptModeEnum Mode of the service appointment. Optional 60.0

**•** `Group`                 - Service appointment mode
is Group.

**•** `Regular`                 - Default mode of service
appointment.

`appointmentType` String Type of the appointment. Optional 53.0

`attendeeLimit` Integer Maximum number of customers that’s
allowed to attend the service appointment.

Required if the 60.0
appointment mode
is Group.

`city` String Name of the city. Optional 53.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`comments` String Comments about the appointment. Optional 53.0

`contactId` String ID of the contact associated with the parent Optional 53.0
record.

`country` String Name of the country. Optional 53.0

`description` String Description of the appointment. Optional 53.0

`engagementChannelTypeId` String

ID of the engagement channel type to Optional 56.0
associate with the appointment.

You can use engagement channel type only
if:

**•** **Schedule Appointments Using**
**Engagement Channels** is enabled in
Salesforce Scheduler Settings in your
Salesforce org.

**•** Shifts are defined in the scheduling
policy. For more information on setting
up shifts in the scheduling policy, see
[Define Shift Rules in Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel
types are not supported with
operating hours rules in the
scheduling policy.

`extendedFields` <List `ConnectApi.ExtendedFieldInput` - Values to add to any of the fields, including Optional 53.0
custom fields.

`parentRecordId` String ID of the parent record associated with the Required if `lead` 53.0
account. isn’t provided.

`postalCode` String Postal code of the city. Optional 53.0

`schedEndTime` Datetime Time at which the appointment is scheduled Optional 53.0
to end.

`schedStartTime` Datetime Time at which the appointment is scheduled Optional 53.0
to start.

`serviceTerritoryId` String ID of the service territory associated with Optional 53.0
the service appointment.

`state` String Name of the state. Optional 53.0

`street` String Name of the street. Optional 53.0

`subject` String Short phrase describing the appointment. Optional 53.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`workTypeId` String

ID of the work type associated with the Optional 53.0
service appointment. If specified, it is added
to the service appointment record.

#### ConnectApi.ShiftsFromPatternInput

Shifts from a pattern.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`schedulingEnd` String Scheduling end date in YYYY-MM-DD Required if
`Date` format. `scheduling`

```
                                  Occurrences
```

Provide `schedulingEndDate` or

isn’t provided

Scheduling end date in YYYY-MM-DD Required if 51.0
format. `scheduling`

Provide `schedulingEndDate` or
`schedulingOccurrences` . Don’t
provide both.

`scheduling` Integer

```
Occurrences

```

Number of scheduling occurrences.

Provide `schedulingEndDate` or
`schedulingOccurrences` . Don’t
provide both.

Required if 51.0

```
schedulingEnd
```

`Date` isn’t provided

`schedulingStart` String Scheduling start date in YYYY-MM-DD Required 51.0
`Date` format.

`serviceResourceId` String

ID of the service resource to assign shifts to. Optional 51.0–52.0

In version 53.0 and later, use
`serviceResourceIdList` .

`serviceResourceId` List<String> List of service resource IDs to assign shifts Optional 53.0
`List` to.

`serviceTerritoryId` String ID of the service territory to assign shifts to. Optional 51.0

`shiftStatus` String Status of the shifts. Default values are: Optional 52.0

**•** `Confirmed`

**•** `Published`

**•** `Tentative`

Additional status values can be created.

#### ConnectApi.ShippingCarrierInputRepresentation

Shipping carrier.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalReference` String Unique code, reference, or identifier for the Optional 63.0
shipping carrier used by external systems.

`shippingCarrierMethods` ListConnectApi.ShippingCaierMethodInputRepresentation **r** List of shipping carrier methods. Required 63.0
on page 2174

#### ConnectApi.ShippingCarrierMethodInputRepresentation

Shipping carrier method external references.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalReference` String

#### ConnectApi.StaticDataInput

Represents the static data input.

Unique code, reference, or identifier for the Required 63.0
shipping carrier method used by external
systems.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the static attribute. 60.0

`value` String Value of the static attribute. 60.0

#### ConnectApi.StatusCapabilityInput

Change the status of a feed post or comment.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### feedEntityStatus ConnectApi. Status of the feed post or comment. Values Required 37.0

`FeedEntityStatus` are:

**•** `Draft` —The feed post isn’t published
but is visible to the author and users
with Modify All Data or View All Data
permission. Comments can’t be drafts.

**•** `Isolated` —The feed post or
comment is isolated, and only admins
can see it.

**•** `PendingReview` —The feed post or
comment isn’t approved yet and
therefore isn’t published or visible.

**•** `Published` —The feed post or
comment is approved and visible.

Posts that have a status of
`PendingReview` or `Published` can’t
be changed to a status of `Draft` and vice
versa. Only admins can change the status
of a post or comment to or from
`Isolated` status.

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.StreamSubscriptionInput

An entity to subscribe to for a Chatter feed stream.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`entityId` String The ID of any feed-enabled entity, such as Required 39.0
a group, record, or user, that the context

user can access. When subscribed, the
entity’s feed is included in the feed stream.

SEE ALSO:

ConnectApi.ChatterStreamInput

#### ConnectApi.StringList

List of string values.


Apex Reference Guide ConnectApi Input Classes

Subclass of ConnectApi.AbstractList.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`values` List<String> List of string values to filter on, for example, Optional 63.0

`["A", "B", "C"]` .

#### ConnectApi.SurveyInvitationEmailInput

Survey invitation email.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`allowGuest` Boolean

```
UserResponse

```

Specifies whether participants who don't Required 50.0
have a Salesforce account can respond
( `true` ) or not ( `false` ).

`allowParticipants` Boolean Specifies whether participants can see their Required 50.0
`AccessTheirResponse` responses ( `true` ) or not ( `false` ).

Maps each recipient with another record Optional 50.0
that must be associated with the recipient's
survey invitation.

```
associateRecords

WithRecipients

```

#### List< ConnectApi.

```
AssociateRecordsWith
```

`RecipientInput` 

`body` String Content of the email. Specify the email body Optional 50.0
in case you don't specify an email template.

The email body must contain one of these
merge fields:

**•** To embed a link to launch the survey:

[[SURVEY_INVITATION_URL]]

**•** To embed a survey question:
{{{SurveyQuestion.QuestionName}}} and
{{{SurveyQuestion.QuestionHtmlContent}}}

`collectAnonymous` Boolean Specifies whether participants can respond Required 50.0
`Response` anonymously ( `true` ) or not ( `false` ).

`communityId` String ID of the site that's used to open the survey Optional 50.0
for users outside your org.

`emailTemplateId` String ID of the Lightning email template that's Optional 50.0
used to send the survey invitation. The

template must contain the required merge
fields that embed either the survey link or a
question in the email. Only Lightning email
templates are used to send survey
invitations.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`fromEmailAddress` String Email ID of the user or the org-wide email Required 50.0
address associated with the user's profile.

`invitation` Datetime Date on which the survey invitation expires. Optional 50.0

```
   ExpirationDate

```

`invitationOwner` String ID of the owner of the survey invitation Optional 50.0
records.

`isPersonal` Boolean Specifies whether a unique invitation is Required 50.0
`Invitation` created for each participant ( `true` ) or not
( `false` ). When a participant responds
using a personal invitation, the response
record is associated with the participant's
Salesforce record.

```
recipient

Engagement

Contexts

```

#### List< ConnectApi. Maps each recipient with the context based Optional 50.0

`RecipientEngagement` on which the survey invitation is emailed.
`ContextInput` 

`recipients` List<String>

`sendEmail` Boolean

```
ThroughUma

```

List of up to 300 IDs of leads, contacts, or Required 50.0
users to whom the survey invitation is
emailed.

Specifies whether to send the email through Optional 65.0
Marketing Cloud ( `true` ) or not ( `false` ).
If unspecified, defaults to `false` .

`shareInvitations` List<String> IDs of the users with whom the survey Optional 50.0
`With` invitation records must be shared. The
invitation records are shared with Read
access.

`subject` String Subject of the email. Specify the subject in Optional 50.0
case you don't specify an email template.

`surveyQuestion` List<String> IDs of the questions that are embedded in Optional 50.0
`Ids` the email. You can send an email invitation
for questions of these types: Net Promoter
Score (NPS), rating, and score.

#### ConnectApi.TargetCollectionInput

Collection of targets to create.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### targets List< ConnectApi. List of targets to create. Required 48.0

`TargetInput`        


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.TargetCollectionUpdateInput

Collection of targets to update.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
targets

```

#### List< ConnectApi. List of targets to update. Required 48.0

```
TargetUpdate
```

`Input` 

#### ConnectApi.TargetInput

Target to create.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`audienceId` String ID of the audience to assign to the target. Required 48.0

`groupName` String Group name of the target. Groups bundle Required 48.0
related target and audience pairs. You can

have up to 2,000 groups and 500 targets
per group. To determine the group name
for targets of type
`ExperienceVariation` [, see](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Personalization Target Developer and Group](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Names in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm) _Experience Cloud Developer_
_Guide_ .

`priority` Integer

Priority of the target. Within a group, priority Optional 48.0
determines which target is returned if the
user matches more than one audience.

#### publishStatus ConnectApi. The publish status of the target. Values are: Optional 48.0

```
         PublishStatus
```

**•** `Draft`

`targetType` String

**•** `Live`

We recommend setting the publish status
to `Draft` . If you specify `Live`, your
changes revert after you publish the site.

Type of target, indicating the nature of the Required 48.0
data being targeted. Supported values
include:

**•** `ExperienceVariation` (version
48.0 and later)

**•** Custom object API names, such as
_**`CustomObjectName`**_ `__c` (version
48.0 and later)


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `NavigationLinkSet` (version 49.0
and later)

**•** `Topic` (version 49.0 and later)

**•** `CollaborationGroup` (version
49.0 and later)

**•** `KnowledgeArticle` (version 49.0
and later)

**•** `ContentDocument` (version 49.0
and later)

**•** `ManagedContent` (version 49.0 and
later)

**•** `Report` (version 49.0 and later)

**•** `Dashboard` (version 49.0 and later)

You can have up to 2,500
`ExperienceVariation` targets and
25,000 record targets.

`targetValue` String Value of the target. If `targetType` is Required 48.0
`ExperienceVariation`,

`targetValue` is the developer name of
the experience variation. If `targetType`
is _**`CustomObjectName`**_ `__c`,
`targetValue` is the ID of the custom
object. To determine the developer name
for targets of type
`ExperienceVariation` [, see](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Personalization Target Developer and Group](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Names in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm) _Experience Cloud Developer_
_Guide_ .

SEE ALSO:

ConnectApi.TargetCollectionInput

#### ConnectApi.TargetLocationInputRepresentation

A set of inventory locations that together can fulfill an order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### locations List< ConnectApi. A list of locations with information about Required 51.0

`LocationInputRepresentation`                      - their country and postal codes.


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.TargetUpdateInput

Target to update.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`audienceId` String ID of the audience to assign to the target. Required if 48.0
`priority` isn’t

specified. Otherwise,
Optional

`priority` Integer

Priority of the target. Within a group, priority Required if 48.0
determines which target is returned if the `audienceId` isn’t
user matches more than one audience. specified. Otherwise,

Optional

`targetId` String ID of the target to update. Required 48.0

SEE ALSO:

ConnectApi.TargetCollectionUpdateInput

#### ConnectApi.TaxAddressRequest

Address input representation for tax calculation.

**Name** **Type** **Description** **Required or** **Available Version**
**Optional**

`city` String City. Optional 55.0

`country` String Country. Optional 55.0

`latitude` Double Latitude. Optional 55.0

`locationCode` String Location code. Optional 55.0

`longitude` Double Longitude. Optional 55.0

`postalCode` String Postal code. Optional 55.0

`state` String State. Optional 55.0

`street` String Street. Optional 55.0

#### ConnectApi.TaxAddressesRequest

Addresses, including the Bill To address, Ship From address, Ship to address, and Sold To address.


Apex Reference Guide ConnectApi Input Classes

**Name** **Type** **Description** **Required or** **Available Version**
**Optional**

```
billTo

shipFrom

shipTo

soldTo

```

#### ConnectApi. Bill To address. Optional 55.0

```
TaxAddress

Request

#### ConnectApi. Ship From address. Optional 55.0

TaxAddress

Request

#### ConnectApi. Ship To address. Optional 55.0

TaxAddress

Request

#### ConnectApi. Sold To address. Optional 55.0

TaxAddress

Request

```

#### ConnectApi.TaxCustomerDetailsRequest

Customer details for the tax calculation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`accountId` String ID of the customer's account. Optional 55.0

`code` String Customer code. Optional 55.0

`exemptionNo` String Tax exemption number. Optional 55.0

`exemptionReason` String Tax exemption reason. Optional 55.0

#### ConnectApi.TaxLineItemRequest

A list of line items passed to the tax engine for tax calculation.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
addresses

```

#### `ConnectApi.`

```
TaxAddresses

Request

```

Addresses, including the Bill To address, Ship Optional 55.0
From address, Ship To address, and Sold To
address.

`amount` Double Amount of the line item. Optional 55.0

`description` String Description of the line item. Optional 55.0

`effectiveDate` Datetime Date to apply the tax calculation to the line Optional 55.0
item.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`legalEntity` String Legal entity that's related to the tax Optional 63.0
treatment.

`lineNumber` String Line number of the line item. Optional 55.0

`productCode` String Product code of the line item. Optional 55.0

`productId` String ID of the product. Optional 63.0

`productSKU` String

Unique identifier of a product that can be Optional 64.0
used to identify products that are exempted
from tax.

`quantity` Double Quantity of the line item. Optional 55.0

`taxCode` String Tax code for the line item. Optional 55.0

`unitPrice` Double Unit price of the product. Optional 63.0

#### ConnectApi.TaxTransactionRequest

Information about the tax transaction sent to the tax adapter as part of a tax calculation request.

This class is abstract.

Superclass of ConnectApi.CalculateTaxRequest.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
addresses

```

#### `ConnectApi.`

```
TaxAddresses

Request

```

Addresses, including the Bill To address, Ship Optional 55.0
From address, Ship to address, and Sold To
address.

`currencyIsoCode` String Three-letter ISO 4217 currency code Optional 55.0
associated with the payment group record.

```
customerDetails

```

#### ConnectApi. Customer details for the tax calculation. Optional 55.0

```
TaxCustomer

DetailsRequest

```

`description` String Information about whether the tax Optional 55.0
transaction failed or was successful.

`documentCode` String Document code. Optional 55.0

`effectiveDate` Datetime The date that tax is applied to the taxed Required 55.0
entity.

```
lineItems

```

#### List< ConnectApi. The line items on which tax was calculated. Required 55.0

```
TaxLine
```

`ItemRequest` 


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`referenceDocumentCode` String

The original document code. Used in case Optional 55.0
of subsequent transactions such as credit
tax.

`referenceEntityId` String ID of the reference entity used during tax Optional 55.0
calculation.

`transactionDate` Datetime The date that the tax transaction occurred. Optional 53.0

#### ConnectApi.TextClassificationsInputRepresentation

Text classification information associating classifiers and text to be classified.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

classifiers List< `String` - List of classifiers according to which text has Required 59.0
to be classified.

textList List< `String` - List of text to be classified. Required 59.0

#### ConnectApi.TextSegmentInput

Include a text segment in a feed item or comment.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Available Version**

`text` String Plain text for this segment. If hashtags or links are detected in _`text`_, 28.0
they’re included in the comment as hashtag and link segments. Mentions

aren’t detected in _`text`_ and aren’t separated out of the text. Mentions
require `ConnectApi.MentionSegmentInput` .

SEE ALSO:

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput

#### ConnectApi.TopicInput

Update a topic’s name or description or merge topics.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available Version**

`description` String Description of the topic 29.0

`idsToMerge` List<String>

`name` String

SEE ALSO:

List of up to five secondary topic IDs to merge with the primary topic 33.0

If any of the secondary topics are navigational or featured topics, they
lose their topic type, topic images, and children topics. Their feed items

are reassigned to the primary topic. If you merge a topic with a content
topic, the content associations are preserved. If you merge a topic with
an inactive endorsee, the endorsement isn’t mapped to the primary
topic.

Name of the topic 29.0

Use this property to change only the capitalization and spacing of the
topic name.

updateTopic(communityId, topicId, topic)

#### ConnectApi.TopicNamesInput

A list of topic names to replace currently assigned topics. Also a list of suggested topics to assign.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`topicNames` List<String> A list of up to 10 topic names for a feed item Required 35.0
or 100 topic names for a record.

`topicSuggestions` List<String>

SEE ALSO:

A list of suggested topics to assign to a Optional 37.0
record or feed item to improve future topic
suggestions.

reassignTopicsByName(communityId, recordId, topicNames)

ConnectApi.ArticleTopicAssignmentJobInput

#### ConnectApi.TopicsCapabilityInput

Assign topics to a feed element.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`contextTopic` String Name of the parent topic in the site to Optional 38.0
`Name` which the feed element belongs.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`topics` List<String> List of topics to assign to the feed element. Required 38.0

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.TypeAndFilterInput

Represents the wrapper for logical comparison filters.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`filter` `BaseComparisonInputRepresentation` Filter for the entity. 60.0

`type` String Name of the entity. 60.0

#### ConnectApi.updateQuoteInput

Input representation for updating the quote status and optionally creating an associated note.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`note` `ConnectApi.CommerceNoteInputRepresentation` Note to be added to the quote. Optional 67.0

`status` String

SEE ALSO:

New status to apply to the quote. If not Required 67.0
specified, the existing status remains
unchanged.

Valid values:

**•** `Draft` —Renogiate the quote.

**•** `Denied` —Decline the quote.

updateQuote(webstoreId, quoteId, updateQuoteInput)

ConnectApi.UpdateQuoteOutput

updateQuote(webstoreId, quoteId, updateQuoteInput)

ConnectApi.UpdateQuoteOutput

#### ConnectApi.UpdateServiceAppointmentInput

Contains information to update a service appointment.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`serviceAppointmentId` String The ID of the service appointment to be Required 53.0
modified.

`assignedResources` <List `ConnectApi.AssignedResourcesInput` 

Represents the service resources who are Optional 53.0
assigned to a service appointment.

When updating an appointment, pass the
complete list of required resources. If you

don’t pass a resource who is already
assigned to the appointment, the API
deletes that assigned resource. For example,
suppose that an existing service
appointment has assigned resources: A and
B and you pass B and C in assigned
resources in the PATCH request. The API
checks the resource availability of B and C
for existing work type and service territory,
and if both are available, the service
appointment gets updated with:

**•** Resource A—Deleted

**•** ResourceB—Updated

**•** ResourceC—Created

However, if you don’t pass any of the
assigned resources, the API assumes there’s
no change.

Note: When creating an
appointment, use

`extendedFields` to add values
to any of the fields, including custom
fields, in `assignedResources`
as long as you have edit access to
those fields.

`lead` `ConnectApi.LeadInput` Represents a prospect or lead.

Note: Required to create a service
appointment for unauthenticated
guest users.

Required if 53.0

```
serviceAppointment
```

isn’t provided.

`schedulingPolicyId` String The ID of the Optional 53.0

```
                 AppointmentSchedulingPolicy
```

object. If no scheduling policy is passed in
the request body, the default configurations
are used. The only scheduling policy
configuration that is used in determining


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

time slots is the enforcement of account
visiting hours.

```
serviceAppointment ConnectApi.ServiceAppointmentInput

```

Represents the service appointment details Required if `lead` 53.0
to book an appointment. When updating isn’t provided.
an appointment, pass only the fields that
must be updated.

Note: When creating an
appointment, use

`extendedFields` to add values
to any of the fields, including custom
fields, in `assignedResources`
as long as you have edit access to
those fields.

#### ConnectApi.UpDownVoteCapabilityInput

Upvote or downvote a feed element or a comment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### vote ConnectApi. Type of vote for a feed element or comment. Required 41.0

`UpDownVoteValue` Values are:

**•** `Down`

**•** `None`

**•** `Up`

#### ConnectApi.UserInput

Update a user’s About Me information.

**Property** **Type** **Description** **Available Version**

`aboutMe` String

SEE ALSO:

The `aboutMe` property of a `ConnectApi.UserDetail` output 29.0
object. This property populates the About Me section of the user profile,
which is visible to all members of an Experience Cloud site or org.

updateUser(communityId, userId, userInput)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.WishlistInput

Create a wishlist.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the wishlist. Required 49.0

```
products

```

#### List< ConnectApi. List of products to add to the wishlist. Optional 49.0

```
WishlistItem
```

`Input` 

#### ConnectApi.WishlistItemInput

Item to update or add to a wishlist.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`productId` String ID of the product to update or add to the Required 49.0
wishlist.

SEE ALSO:

#### ConnectApi.WishlistInput ConnectApi.WishlistUpdateInput

Update a wishlist name.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Wishlist name to update. Required 50.0

#### ConnectApi.WrappedValue

Value wrapped for use as an object.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`value` `Object` Value to wrap. Required 60.0

#### Retired ConnectApi Input Classes These ConnectApi input classes are retired.


Apex Reference Guide ConnectApi Input Classes

IN THIS SECTION:

##### ConnectApi.CanvasAttachmentInput

Used to attach a canvas app to a feed item.

ConnectApi.ContentAttachmentInput
Used to attach existing content to a comment or feed item.

ConnectApi.DatacloudOrderInput
Input representation for a Datacloud order to purchase contacts or companies and retrieve purchase information.

ConnectApi.FeedItemAttachmentInput
Used to attach a file to a feed item.

ConnectApi.LinkAttachmentInput
Add links to a feed item.

ConnectApi.NewFileAttachmentInput
Attach a new file to a feed item.

ConnectApi.PollAttachmentInput
Attach a poll to a feed item.

ConnectApi.SocialPostMassApprovalInput
List of social post ids and the action to approve or reject publishing them.

##### ConnectApi.CanvasAttachmentInput

Used to attach a canvas app to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.CanvasCapabilityInput.

Subclass of Connectapi.FeedItemAttachmentInput.

**Property** **Type** **Description** **Available Version**

`description` String Optional. The description of the canvas app. 29.0–31.0

`developerName` String The developer name (API name) of the canvas app 29.0–31.0

`height` String Optional. The height of the canvas app in pixels. Default height is 200 29.0–31.0
pixels.

`namespacePrefix` String Optional. The namespace prefix of the Developer Edition organization in 29.0–31.0
which the canvas app was created.

`parameters` String

Optional. Parameters passed to the canvas app in JSON format. Example: 29.0–31.0

```
{'isUpdated'='true'}

```

`thumbnailUrl` String Optional. A URL to a thumbnail image for the canvas app. Maximum 29.0–31.0
dimensions are 120x120 pixels.

`title` String The title of the link used to call the canvas app. 29.0–31.0


Apex Reference Guide ConnectApi Input Classes

##### ConnectApi.ContentAttachmentInput

Used to attach existing content to a comment or feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.ContentCapabilityInput.

Subclass of ConnectApi.FeedItemAttachmentInput.

**Property** **Type** **Description** **Available Version**

`contentDocumentId` String ID of the existing content. 28.0–31.0

##### ConnectApi.DatacloudOrderInput

Input representation for a Datacloud order to purchase contacts or companies and retrieve purchase information.

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

`companyIds` String

`contactIds` String

A comma-separated list of
identification numbers for the
companies to be purchased.

You can’t include any contact IDs or
your purchase fails.

A comma-separated list of
identification numbers for the
contacts to be purchased.

You can’t include any company IDs
or your purchase fails.

Required to 32.0
purchase
companies

Required to 32.0
purchase
contacts

`userType` ConnectDatacloudUserTypeEnum Indicates the Data.com user type to Optional 32.0
be used. There are two user types.

**•** `Monthly` (default)

**•** `Listpool`

SEE ALSO:

postOrder(orderInput)

##### ConnectApi.FeedItemAttachmentInput

Used to attach a file to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.FeedElementCapabilityInput.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

Superclass for:

**•** ConnectApi.CanvasAttachmentInput


Apex Reference Guide ConnectApi Input Classes

**•** ConnectApi.ContentAttachmentInput

##### • ConnectApi.LinkAttachmentInput • ConnectApi.NewFileAttachmentInput • ConnectApi.PollAttachmentInput ConnectApi.LinkAttachmentInput

Add links to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.LinkCapabilityInput.

Subclass of ConnectApi.FeedItemAttachmentInput.

**Property** **Type** **Description** **Available Version**

`url` String URL to be used for the link 28.0–31.0

`urlName` String Title of the link 28.0–31.0

##### ConnectApi.NewFileAttachmentInput

Attach a new file to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.ContentCapabilityInput.

The actual binary file, that is the attachment, is provided as part of the BinaryInput in the method that takes this attachment input, such
as `postFeedItem` or `postComment` .

Subclass of ConnectApi.FeedItemAttachmentInput.

**Property** **Type** **Description** **Available Version**

`description` String Description of the file to be uploaded. 28.0–31.0

`title` String

The title of the file. This value is required and is also used as the file 28.0–31.0
name. For example, if the title is My Title, and the file is a .txt file, the
file name is My Title.txt.

##### ConnectApi.PollAttachmentInput

Attach a poll to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, use ConnectApi.PollCapabilityInput.

Subclass of ConnectApi.FeedItemAttachmentInput.

**Property** **Type** **Description** **Available Version**

`pollChoices` List<String> The text labels for the poll items. Polls must contain between 2 to 10 poll 28.0–31.0
choices.


### Apex Reference Guide ConnectApi Output Classes

##### ConnectApi.SocialPostMassApprovalInput

List of social post ids and the action to approve or reject publishing them.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isApproved` Boolean

Specifies whether to approve ( `true` ) or Optional 46.0
reject ( `false` ) publishing the social posts.
If unspecified, defaults to `false` .

`socialPost` List<String> A list of up to 200 social post IDs. Required 46.0

```
IdList

##### ConnectApi Output Classes Most ConnectApi methods return instances of ConnectApi output classes.

```

All properties are read-only, except for instances of output classes created within test code.

All output classes are concrete unless marked abstract in this documentation.

[All concrete output classes have no-argument constructors that you can invoke only from test code. See Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### ConnectApi.AbstractCartItem

A cart item.

This class is abstract.

Superclass of:

**•** ConnectApi.CartItem

**•** ConnectApi.CartItemWithoutPrice

**Property Name** **Type** **Description** **Available Version**

##### billingFrequency ConnectApi. Reserved for future use. 59.0

```
           BillingFrequency

```

`cartDeliveryGroupId` String ID of the cart delivery group. 60.0

`cartId` String ID of the cart. 49.0

`cartItemId` String ID of the item. 49.0

`childProduct` Integer on page 3936 Number of child products in the cart that are 62.0
`Count` associated with the item. A cart item can have child
products if the `productClass` of the item is
`Bundle` . For nested bundles, which include a child
product that's also a bundle,
`childProductCount` includes all child
products.

`customFields` List< `SObject` - Array of sObjects and viewable custom fields for the 61.0
sObjects. Standard fields are ignored. Currently, only


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

the CartItem sObject is supported. Field-level security
[rules from the shopper profile are applied to the](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
custom fields. The rules are applied for registered
shoppers and for the guest shopper profile.

`isShipping` Boolean

```
ChargeNot

Applicable

```

Specifies whether the shipping charge for the cart 64.0
item is waived ( `true` ) or not ( `false` ). If the value
is `true`, the cart item is classified as a digital product.

#### messagesSummary ConnectApi. Messages summary for the item. 49.0

```
           CartMessagesSummary

```

`name` String Name of the item. 49.0

`parentCartItemId` String ID of the item’s parent cart item. The value is empty 62.0
if the item is a top-level cart item.

#### productDetails ConnectApi. Summary of the product details. 49.0

```
           CartItemProduct

```

`productId` String ID of the product. 49.0

`productSelling` String Reserved for future use. 59.0

```
ModelId

```

`promotion` String Promotion display name for a bonus product. 64.0

```
DisplayName

```

`quantity` String Quantity of the item. 49.0

#### sellingModelType ConnectApi. Reserved for future use. 60.0

```
           SellingModelType

#### subType ConnectApi. Subtype of item in a cart. Values are: 64.0

           CartItemSubType
```

**•** `Bonus` —A bonus product.

**•** `Gift` —A gift product.

`subscriptionTerm` Integer on page 3936 Reserved for future use. 59.0

#### type ConnectApi. Type of item in a cart. Values are: 49.0

```
           CartItemType
```

**•** `DeliveryCharge`

**•** `Product`

SEE ALSO:

ConnectApi.CartItemResult

#### ConnectApi.AbstractContentHubItemType

An item type associated with a repository folder.


Apex Reference Guide ConnectApi Output Classes

This class is abstract.

Superclass of:

**•** ConnectApi.ContentHubItemTypeDetail

**•** ConnectApi.ContentHubItemTypeSummary

**Property Name** **Type** **Description** **Available Version**

#### ConnectApi. Support for content streaming. Values are: 39.0

```
ContentHub
```

**•** `ContentStreamAllowed`
```
StreamSupport

```

#### `contentStream ConnectApi.`

```
Support ContentHub
```

**•** `ContentStreamAllowed`

**•** `ContentStreamNotAllowed`

**•** `ContentStreamRequired`

`description` String Description of the item type. 39.0

`displayName` String Display name of the item type. 39.0

`id` String ID of the item type. 39.0

`isVersionable` Boolean Indicates whether the item type can have versions. 39.0

`url` String URL to the detailed information of the item type. 39.0

#### ConnectApi.AbstractDirectoryEntrySummary

A directory entry with summary information.

This class is abstract.

Superclass of:

**•** ConnectApi.RepositoryGroupSummary

**•** ConnectApi.RepositoryUserSummary

**Property Name** **Type** **Description** **Available Version**

`domain` String Domain of the directory entry. 39.0

`email` String Email of the directory entry. 39.0

`id` String ID of the directory entry. 39.0

#### type ConnectApi. Type of directory entry. Values are: 39.0

```
           ContentHub
```

**•** `GroupEntry`
```
           DirectoryEntry
```

**•** `UserEntry`
```
           Type

#### ConnectApi.AbstractExtensionInformation

```

Extension information.

This class is abstract.

Superclass of ConnectApi.LightningExtensionInformation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### extension ConnectApi. Information type of the extension. Values are: 40.0

```
   InformationType ExtensionInformation
```

**•** `Lightning`
```
             Type

#### ConnectApi.AbstractGatewayCommonResponse

```

Payment gateway response fields commonly used in payment services.

This class is abstract.

Superclass of ConnectApi.AbstractGatewayResponse.

**Property Name** **Type** **Description** **Available Version**

`gatewayAvsCode` String

Used to verify the address mapped to a payment 50.0
method when the payments platform requests
tokenization from the payment gateway.

`gatewayDate` Datetime Date when the notification occurred. Some gateways 50.0
don’t send this value.

`gatewayMessage` String

`gatewayResultCode` String

`gatewayResultCodeDescription` String

Error messages that the gateway returned for the 50.0
notification request. Maximum length of 255
characters.

Gateway-specific result code. You can map the result 50.0
code to a Salesforce-specific result code. Maximum
length of 64 characters.

A description of the gateway-specific result code that 50.0
a payment gateway returned. Maximum length of
1,000 characters.

`salesforceResultCode` String The Salesforce result code for the gateway result 50.0
code.

#### ConnectApi.AbstractGatewayResponse

Payment gateway response fields used in sale, authorization, and capture services.

This class is abstract.

Subclass of ConnectApi.AbstractGatewayCommonResponse.

Super class of:

**•** ConnectApi.AuthReversalGatewayResponse

**•** ConnectApi.AuthorizationGatewayResponse

**•** ConnectApi.AuthorizationReversalResponse

**•** ConnectApi.CaptureGatewayResponse

**•** ConnectApi.PaymentMethodTokenizationGatewayResponse


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.PostAuthGatewayResponse

**•** ConnectApi.RefundGatewayResponse

**•** ConnectApi.SaleGatewayResponse

**Property Name** **Type** **Description** **Available Version**

`gatewayReferenceDetails` String Provides information about the gateway 50.0
communication.

`gatewayReferenceNumber` String Unique transaction ID created by the payment 50.0
gateway.

#### ConnectApi.AbstractManagedContentChannelRepresentation

Managed content channel.

This class is abstract.

Super class of:

**•** ConnectApi.ManagedContentChannel

**•** ConnectApi.ManagedContentChannelSummary

No additional properties.

SEE ALSO:

ConnectApi.ManagedContentChannelsRepresentation

#### ConnectApi.AbstractManagedContentDeliveryDocument

Managed content delivery document.

This class is abstract.

Superclass of:

**•** ConnectApi.ManagedContentDeliveryDocument

**•** ConnectApi.ManagedContentDeliveryDocumentSummary

**Property Name** **Type** **Description** **Available Version**

`contentKey` String Globally unique identifier (GUID) for the managed 55.0
content.

```
contentType

```

#### ConnectApi. Type of managed content. 55.0

```
ManagedContent

TypeSummary

```

`language` String Language locale of the managed content. 55.0

`managedContentId` String ID of the managed content. 55.0

`publishedDate` Datetime Most recent publish date of the managed content. 55.0

`resourceUrl` String URL to the single content delivery resource. 55.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`title` String Title of the managed content. 55.0

`unauthenticatedUrl` String Public URL for the managed content. 55.0

`urlName` String URL name of the managed content. 55.0

SEE ALSO:

ConnectApi.ManagedContentDeliveryDocumentCollection

#### ConnectApi.AbstractManagedContentReference

Managed content reference.

This class is abstract.

Superclass of:

**•** ConnectApi.ManagedContentReference

**•** ConnectApi.ManagedContentReferenceSummary

**Property Name** **Type** **Description** **Available Version**

`contentKey` String Unique identifier for the managed content reference. 54.0

`managedContentId` String ID of the managed content reference. 54.0

`resourceUrl` String URL to the single content delivery resource. 55.0

SEE ALSO:

ConnectApi.ManagedContentDeliveryDocumentCollection

#### ConnectApi.AbstractMessageBody

Abstract message body.

This class is abstract.

Superclass of:

**•** ConnectApi.FeedBody

**•** ConnectApi.MessageBody

**Name** **Type** **Description** **Available**
**Version**

`isRichText` Boolean Indicates whether the body is rich text. 35.0

#### messageSegments List< ConnectApi. List of message segments 28.0

`MessageSegment`           


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`text` String Display-ready text. Use this text if you don’t want to process 28.0
the message segments.

#### ConnectApi.AbstractNBAAction

A recommended action of recommendation strategy.

This class is abstract.

Superclass of ConnectApi.NBAFlowAction.

**Property Name** **Type** **Description** **Available Version**

`parameters` List< `ConnectApi.NBAActionParameter`   - List of parameters to pass to the action. 45.0

#### type ConnectApi. Type of action. Values are: 45.0

```
             NBAActionType
```

**•** `Flow` —Automated process tool with multiple
subtypes.

SEE ALSO:

ConnectApi.NBARecommendation

#### ConnectApi.AbstractNBATarget

A recommendation target of a recommendation strategy.

This class is abstract.

Superclass of ConnectApi.NBANativeRecommendation.

**Property Name** **Type** **Description** **Available Version**

#### type ConnectApi. Type of target. Values are: 45.0

```
             NBATargetType
```

**•** `Recommendation`

SEE ALSO:

ConnectApi.NBARecommendation

#### ConnectApi.AbstractPicklistValueAttributes

Picklist value attributes.

This class is abstract.

Superclass of:

**•** ConnectApi.CaseStatusPicklistValueAttributes


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.LeadStatusPicklistValueAttributes

**•** ConnectApi.OpportunityStagePicklistValueAttributes

**•** ConnectApi.WorkStepPicklistValueAttribute

**Property Name** **Type** **Description** **Available Version**

```
picklistAtrributes
```

`ValueType` [sic]

SEE ALSO:

#### ConnectApi. Indicates the type of picklist attribute value. Values 66.0

`PicklistAttributes` are:

```
ValueType
```

**•** `CaseStatus`

**•** `LeadStatus`

**•** `OpportunityStage`

**•** `Standard`

**•** `WorkStepStatus`

ConnectApi.PicklistValue

#### ConnectApi.AbstractRecommendation

A Chatter, custom, or static recommendation.

This class is abstract.

Superclass of:

**•** ConnectApi.EntityRecommendation

**•** ConnectApi.NonEntityRecommendation

ConnectApi.NonEntityRecommendation isn’t used in version 34.0 and later. In version 34.0 and later,
ConnectApi.EntityRecommendation is used for all recommendations.

**Property Name** **Type** **Description** **Available Version**

```
explanation

platformAction

Group

```

#### ConnectApi. The Chatter, custom, or static recommendation 32.0

`Recommendation` explanation.

```
Explanation

#### ConnectApi. A platform action group instance with state 34.0
```

`PlatformAction` appropriate for the context user.

```
Group

```

#### recommendation ConnectApi. Specifies the type of record being recommended. 32.0

```
Type RecommendationType

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`url` String URL for the Chatter, custom, or static 34.0
recommendation.

SEE ALSO:

ConnectApi.RecommendationsCapability

ConnectApi.RecommendationCollection

#### ConnectApi.AbstractRecommendationExplanation

Explanation for a Chatter recommendation.

This class is abstract.

Superclass of ConnectApi.RecommendationExplanation.

**Property Name** **Type** **Description** **Available Version**

`summary` String Summary explanation for the Chatter 32.0
recommendation.

```
type

```

#### ConnectApi. Indicates the reason for the Chatter recommendation. 32.0

```
Recommendation
```

**•** `ArticleHasRelatedContent` —Articles

`ExplanationType` with related content to a context article.

**•** `ArticleViewedTogether` —Articles often
viewed together with the article that the context
user just viewed.

**•** `ArticleViewedTogetherWithViewers` —Articles
often viewed together with other records that
the context user views.

**•** `Custom` —Custom recommendations.

**•** `FilePopular` —Files with many followers or
views.

**•** `FileViewedTogether` —Files often viewed
at the same time as other files that the context
user views.

**•** `FollowedTogetherWithFollowees` —Users
often followed together with other records that
the context user follows.

**•** `GroupMembersFollowed` —Groups with
members that the context user follows.

**•** `GroupNew` —Recently created groups.

**•** `GroupPopular` —Groups with many active
members.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ItemViewedTogether` —Records often
viewed at the same time as other records that
the context user views.

**•** `PopularApp` —Applications that are popular.

**•** `RecordOwned` —Records that the context user
owns.

**•** `RecordParentOfFollowed` —Parent
records of records that the context user follows.

**•** `RecordViewed` —Records that the context
user recently viewed.

**•** `TopicFollowedTogether` —Topics often
followed together with the record that the
context user just followed.

**•** `TopicFollowedTogetherWithFollowees` —Topics
often followed together with other records that
the context user follows.

**•** `TopicPopularFollowed` —Topics with
many followers.

**•** `TopicPopularLiked` —Topics on posts that
have many likes.

**•** `UserDirectReport` —Users who report to
the context user.

**•** `UserFollowedTogether` —Users often
followed together with the record that the
context user followed .

**•** `UserFollowsSameUsers` —Users who
follow the same users as the context user.

**•** `UserManager` —The context user’s manager.

**•** `UserNew` —Recently created users.

**•** `UserPeer` —Users who report to the same
manager as the context user.

**•** `UserPopular` —Users with many followers.

**•** `UserViewingSameRecords` —Users who
view the same records as the context user.

#### ConnectApi.AbstractRecordField

A field on a record.

This class is abstract.

Superclass of:

**•** ConnectApi.BlankRecordField


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.LabeledRecordField

Message segments in a feed item are typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as
`ConnectApi.FeedItemCapability` . Record fields are typed as `ConnectApi.AbstractRecordField` . These classes
are all abstract and have several concrete subclasses. At runtime you can use `instanceof` to check the concrete types of these objects
and then safely proceed with the corresponding downcast. When you downcast, you must have a default case that handles unknown
subclasses.

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

**Name** **Type** **Description** **Available Version**

`type` String Type of the field. One of these values: 29.0

**•** `Address`

**•** `Blank`

**•** `Boolean`

**•** `Compound`

**•** `CreatedBy`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `LastModifiedBy`

**•** `Location`

**•** `Name`

**•** `Number`

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `Reference`

**•** `Text`

**•** `Time`

SEE ALSO:

ConnectApi.RecordViewSection

#### ConnectApi.AbstractRecordView

A view of any record in the org, including a custom object record. This object is used if a specialized object, such as User or ChatterGroup,
isn’t available for the record type.

This class is abstract.

Subclass of ConnectApi.ActorWithId.

Superclass of:

**•** ConnectApi.RecordSummary


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.RecordView

**Name** **Type** **Description** **Available Version**

`name` String The localized name of the record. 29.0

#### ConnectApi.AbstractRepositoryFile

A repository file.

This class is abstract.

Subclass of ConnectApi.AbstractRepositoryItem.

Superclass of:

**•** ConnectApi.RepositoryFileDetail

**•** ConnectApi.RepositoryFileSummary

**Property Name** **Type** **Description** **Available Version**

`checkinComment` String Checkin comment of the file. 39.0

`contentBody` String Text of the file’s content if available, otherwise `null` . 43.0

`contentItemSize` Long Class on page 4011 Length in bytes of the content of the file, including 65.0
files that are larger than 2 GB.

`contentSize` Integer Length in bytes of the content of the file, for files that 39.0
are smaller than 2 GB.

`downloadUrl` String URL to the repository file content. 39.0

`external` String URL of this file’s content in the external system. 39.0

```
   ContentUrl

```

`external` String URL of this file in the external system. 39.0

```
   DocumentUrl

#### external ConnectApi. External file permission information, such as available 39.0
```

`FilePermission` `ExternalFile` groups, available permission types, and current
`Information` `PermissionInformation` sharing status, or `null` if

```
                        includeExternalFilePermissionsInfo
```

is `false` .

`mimeType` String Mime type of the file. 39.0

`previewUrl` String URL to the thumbnail preview (240 x 180 PNG). 39.0

```
   Thumbnail

```

`previewUrl` String URL to the big thumbnail preview (720 x 480 PNG). 39.0

```
   ThumbnailBig

```

`previewUrl` String URL to the tiny thumbnail preview (120 x 90 PNG). 39.0

```
   ThumbnailTiny

```

`previewsUrl` String URL to the previews. 39.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`title` String Title of the file. 39.0

`versionId` String ID of the file version in the external system. 39.0

#### ConnectApi.AbstractRepositoryFolder

A repository folder.

This class is abstract.

Subclass of ConnectApi.AbstractRepositoryItem.

Superclass of:

**•** ConnectApi.RepositoryFolderDetail

**•** ConnectApi.RepositoryFolderSummary

**Property Name** **Type** **Description** **Available Version**

`externalFolderUrl` String URL of this folder in the external system. 39.0

`folderItemsUrl` String URL that lists the files and folders in this folder. 39.0

`path` String Absolute path of the folder in the external system. 39.0

#### ConnectApi.AbstractRepositoryItem

A repository item.

This class is abstract.

Superclass of:

**•** ConnectApi.AbstractRepositoryFile

#### • ConnectApi.AbstractRepositoryFolder

**Property Name** **Type** **Description** **Available Version**

`createdBy` String Name of the user who created the item. 39.0

`createdDate` Datetime Date the item was created. 39.0

`description` String Description of the Item. 39.0

`id` String ID of the item. 39.0

`itemTypeUrl` String URL to the item type information. 39.0

`modifiedBy` String Name of the user who last modified the item. 39.0

`modifiedDate` Datetime Date the item was last modified. 39.0

`motif` `ConnectApi.Motif` Motif of the item. 39.0

`name` String Name of the item. 39.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### repository ConnectApi. Item external repository. 39.0

```
             Reference

```

`type` String Item type, `file` or `folder` . 39.0

`url` String The URL to the item. 39.0

#### ConnectApi.AbstractUserMissionActivity

User activity associated with missions.

This class is abstract.

Superclass of:

**•** ConnectApi.UserMission

**•** ConnectApi.UserMissionActivity

**Property Name** **Type** **Description** **Available Version**

`activityCount` Integer Number of mission activities of the specified type for 45.0
the user.

`activityType` String Type of mission activity for a user. Values are: 45.0

**•** `FeedItemAnswerAQuestion` —User
answered a question.

**•** `FeedItemLikeSomething` —User liked a
post or comment.

**•** `FeedItemMarkAnswerAsBest` —User
marked an answer as the best answer.

**•** `FeedItemPostQuestion` —User posted a
question.

**•** `FeedItemReceiveAComment` —User
received a comment on a post.

**•** `FeedItemReceiveALike` —User received
a like on a post or comment.

**•** `FeedItemReceiveAnAnswer` —User
received an answer to a question.

**•** `FeedItemWriteAComment` —User
commented on a post.

**•** `FeedItemWriteAPost` —User made a post.

**•** `FeedItemYourAnswerMarkedBest`                       User’s answer was marked as the best answer.

SEE ALSO:

ConnectApi.UserMissionActivityCollection


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ActionInfoOutputRepresentation

Recommended action information.

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the Lightning web component used for 60.0
dynamically rendering the recommended action.

`parameters` String Parameters required for processing and displaying 60.0
the recommended action.

#### ConnectApi.ActionLinkDefinition

The definition of an action link. Action link definition can be sensitive to a third party (for example, OAuth bearer token headers). For this
reason, only calls made from the Apex namespace that created the action link definition can read, modify, or delete the definition. In
addition, the user making the call must have created the definition or have View All Data permission.

**Property Name** **Type** **Description** **Available Version**

`actionUrl` String The action link URL. For example, a `Ui` action link 33.0
URL is a Web page. A `Download` action link URL is

a link to the file to download. `Ui` and `Download`
action link URLs are provided to clients. An `Api` or
`ApiAsync` action link URL is a REST resource. `Api`
and `ApiAsync` action link URLs aren’t provided to
clients. Links to Salesforce can be relative. All other
links must be absolute and start with `https://` .

`createdDate` Datetime ISO 8601 format date string, for example, 33.0
2011-02-25T18:24:31.000Z.

`excludedUserId` String

ID of a single user to exclude from performing the 33.0
action. If you specify an `excludedUserId`, you
can’t specify a `userId` .

`groupDefault` Boolean `true` if this action is the default action link in the 33.0
action link group; `false` otherwise. There can be

only one default action link per action link group. The
default action link gets distinct styling in the
Salesforce UI.

#### headers List< ConnectApi. The request headers for the Api and ApiAsync 33.0

`RequestHeader`         - action link types.

`id` String The 18-character ID for the action link definition. 33.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`label` String

A custom label to display on the action link button. 34.0
A `label` value can be set only in an action link
template.

Action links have four statuses: NewStatus,
PendingStatus, SuccessStatus, and FailedStatus. These
strings are appended to the label for each status:

**•** _label_

**•** _label_ Pending

**•** _label_ Success

**•** _label_ Failed

For example, if the value of `label` is “See Example,”
the values of the four action link states are: See
Example, See Example Pending, See Example Success,
and See Example Failed.

An action link can use either `label` or `labelKey`
to generate label names, it can’t use both. If `label`
has a value, the value of `labelKey` is `None` . If
`labelKey` has a value other than `None`, the value
of `label` is `null` .

`labelKey` String Key for the set of labels to show in the user interface. 33.0
A set includes labels for these states: NewStatus,

PendingStatus, SuccessStatus, FailedStatus. For
example, if you use the `Approve` key, you get these
labels: Approve, Pending, Approved, Failed.

[For a complete list of label keys, see Action Links](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)
[Labels in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm) _Connect REST API Developer Guide_ .

`method` `ConnectApi.` The HTTP method. One of these values: 33.0

```
          HttpRequestMethod
```

**•** `HttpDelete` —Returns HTTP 204 on success.
Response body or output class is empty.

**•** `HttpGet` —Returns HTTP 200 on success.

**•** `HttpHead` —Returns HTTP 200 on success.
Response body or output class is empty.

**•** `HttpPatch` —Returns HTTP 200 on success or
HTTP 204 if the response body or output class is
empty.

**•** `HttpPost` —Returns HTTP 201 on success or
HTTP 204 if the response body or output class is
empty. Exceptions are the batch posting
resources and methods, which return HTTP 200
on success.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `HttpPut` —Return HTTP 200 on success or
HTTP 204 if the response body or output class is
empty.

`modifiedDate` Datetime ISO 8601 format date string, for example, 33.0
2011-02-25T18:24:31.000Z.

`requestBody` String The request body for `Api` and `ApiAsync` action 33.0
link types.

Note: Escape quotation mark characters in
the `requestBody` value.

`requires` Boolean `true` to require the user to confirm the action; 33.0
`Confirmation` `false` otherwise.

`templateId` String

The ID of the action link template from which to 33.0
instantiate this action link. If the action link isn’t
associated with a template, the value is `null` .

`type` `ConnectApi.` Defines the type of action link. Values are: 33.0

```
          ActionLinkType
```

**•** `Api` —The action link calls a synchronous API at
the action URL. Salesforce sets the status to
`SuccessfulStatus` or `FailedStatus`
based on the HTTP status code returned by your
server.

**•** `ApiAsync` —The action link calls an
asynchronous API at the action URL. The action
remains in a `PendingStatus` state until a
third party makes a request to

```
                      /connect/action-links/ actionLinkId
```

to set the status to `SuccessfulStatus` or
`FailedStatus` when the asynchronous
operation is complete.

**•** `Download` —The action link downloads a file
from the action URL.

**•** `Ui` —The action link takes the user to a web page
at the action URL.

Note: Invoking `ApiAsync` action links from
an app requires a call to set the status.
However, there isn’t currently a way to set the
status of an action link using Apex. To set the
status, use Connect REST API. See the Action
[Link resource in the Connect REST API](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/)
[Developer Guidefor more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/)


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`userId` String The ID of the user who can execute the action. If not 33.0
specified or `null`, any user can execute the action.

If you specify a `userId`, you can’t specify an
`excludedUserId` .

SEE ALSO:

#### ConnectApi.ActionLinkGroupDefinition ConnectApi.ActionLinkDiagnosticInfo

Any diagnostic information that may exist for an executed action link. Diagnostic info is provided only for users who can access the
action link.

**Property Name** **Type** **Description** **Available Version**

`diagnosticInfo` String

Any diagnostic information returned when an action 33.0
link is executed. Diagnostic information is provided
only for users who can access the action link.

`url` String The URL for this action link diagnostic information. 33.0

#### ConnectApi.ActionLinkGroupDefinition

The definition of an action link group. Information in the action link group definition can be sensitive to a third party (for example, OAuth
bearer token headers). For this reason, only calls made from the Apex namespace that created the action link group definition can read,
modify, or delete the definition. In addition, the user making the call must have created the definition or have View All Data permission.

**Property Name** **Type** **Description** **Available Version**

#### actionLinks List< ConnectApi. A collection of action link definitions that make up 33.0

`ActionLinkDefinition`             - the action link group. Within an action link group,

action links are displayed in the order listed in the
`actionLinks` property of the

#### `ConnectApi.ActionLinkGroupDefinitionInput`

class. Within a feed item, action link groups are
displayed in the order specified in the
`actionLinkGroupIds` property of the

```
                     ConnectApi.AssociatedActionsCapabilityInput
```

class.

```
category

```

#### ConnectApi. Indicates the priority and location of the action links. 33.0

`PlatformAction` Values are:

```
GroupCategory
```

**•** `Primary` —The action link group is displayed
in the body of the feed element.

**•** `Overflow` —The action link group is displayed
in the overflow menu of the feed element.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`createdDate` Datetime ISO 8601 date string, for example, 33.0
2011-02-25T18:24:31.000Z.

```
executions

Allowed

```

#### ConnectApi. Defines the number of times an action link can be 33.0

`ActionLink` executed. Values are:

```
ExecutionsAllowed
```

**•** `Once` —An action link can be executed only one
time across all users.

**•** `OncePerUser` —An action link can be
executed only one time for each user.

**•** `Unlimited` —An action link can be executed
an unlimited number of times by each user. If the
action link’s `actionType` is `Api` or
`ApiAsync`, you can’t use this value.

`expirationDate` Datetime ISO 8601 date string, for example, 33.0
2011-02-25T18:24:31.000Z, that represents the date

and time this action group expires and can no longer
be executed. If the value is `null`, there isn’t an
expiration date.

`id` String 18-character ID of the action link group definition. 33.0

`modifiedDate` Datetime ISO 8601 date string, for example, 33.0
2011-02-25T18:24:31.000Z.

`templateId` String

The ID of the action link group template from which 33.0
to instantiate this action link group, or `null` if this
group isn’t associated with a template.

`url` String The URL for this action link group definition. 33.0

#### ConnectApi.ActivitySharingResult

The results of sharing a captured email or event.

**Property Name** **Type** **Description** **Available Version**

`success` Boolean Whether the share operation succeeded or not. 39.0

#### ConnectApi.Activation

Represents an activation output.

**Property Name** **Type** **Description** **Available Version**

`activationDefinitionId` String ID of the activation definition. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`activationPlatformCustomerFileSourceEnum` `ConnectApi.` Customer file source of the activation platform. 60.0

```
             ActivationPlatformCustomerFileSourceEnum
```

**•** `First_And_Third_Party`

**•** `First_Party`

**•** `Third_Party`

`activationRecordSchema` String

JSON schema representing the activation JSON 62.0
payload in the activationRecord field of the
AudienceDMO.

`activationTarget` `ConnectApi.` Activation target details. 60.0

```
          ActivationTargetRepresentation

```

`activationTargetId` String Activation target ID for the activation. 60.0

`activationTargetName` String Activation target name for the activation. 60.0

`activationTargetObjectPath` List< `ConnectApi.` Object path for the activation target. 60.0
`QueryPathConfigList`            

`activationTargetSubject` `ConnectApi.` Activation target subject for the activation. 60.0

```
          ActivationTargetSubject

```

`attributesConfig` `ConnectApi.` Attributes for the activation. 60.0

```
          ActivationAttributeConfig

```

`contactPointsConfig` `ConnectApi.` Contact points for the activation. 60.0

```
          ContactPointsConfig

```

`curatedEntityApiName` String API name of the entity curated by the activation. 60.0

`curatedEntityId` String ID of the entity curated by the activation. 60.0

`curatedEntityName` String Name of the entity curated by the activation. 60.0

`dataSourcesConfig` `ConnectApi.` Data sources for the activation. 60.0

```
          ActivationDataSources

```

`dataSpaceName` String Data space name for the activation. 60.0

`dataspaceId` String Data space ID for the activation. 60.0

`description` String Description of the activation. 60.0

`developerName` String Developer name for the activation. 60.0

`directDmoFiltersConfig` `ConnectApi.` Direct DMO filters for the activation. 60.0

```
          DmoFilterConfig

```

`enabled` Boolean Indicates if the activation is enabled `(true)` or not 60.0
`(false)` .

`historyAudienceDmoApiName` String API name for the history audience DMO. 60.0

`historyAudienceDmoLabel` String Name of the history audience DMO. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`lastPublishDate` Datetime Last publish timestamp of the activation. Use the 60.0
format `yyyy-mm-dd` .

`lastPublishStatus` `ConnectApi.` Last publish status of the activation. 60.0

```
             DataExportRunStatusEnum
```

**•** `Error`

**•** `Partner_Error`

**•** `Partner_Processing`

**•** `Publishing`

**•** `Queued`

**•** `Segment_Error`

**•** `Skipped`

**•** `Success`

`lastPublishStatusErrorMsg` String Error message encountered during last publish. 60.0

`latestAudienceDmoApiName` String API name for the latest audience DMO. 62.0

`latestAudienceDmoLabel` String Name for the latest audience DMO. 62.0

`latestAudienceDmoLastRunTimestamp` Datetime Timestamp of the last run for the latest audience 62.0
DMO. Use the format `yyyy-mm-dd` .

`membershipName` String Membership name of the activation. 60.0

`refreshType` `ConnectApi.` Refresh type of the activation. 60.0

```
              DataExportRefreshModeEnum
```

**•** `Full_Refresh`

**•** `Incremental`

`relatedDmoFiltersConfig` `ConnectApi.` DMO filters on related attributes for the activation. 60.0

```
             DmoFilterConfig

```

`segmentApiName` String API name for the activation segment. 60.0

`segmentDefinitionId` String Definition ID for the activation segment. 60.0

`segmentId` String ID for the activation segment. 60.0

`shouldExcludeDeletes` Boolean Indicates whether to exclude records removed since 60.0
the last refresh `(true)` or not `(false)` .

`shouldExcludeUpdates` Boolean Indicates whether to exclude records modified since 60.0
the last refresh `(true)` or not `(false)` .

`staticDataConfig` `ConnectApi.` Static data of the activation. 60.0

```
             StaticDataConfig

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### status ConnectApi. Status of the activation. 60.0

```
             ActivationStatusEnum
```

**•** `Active`

**•** `Processing`

**•** `Error`

**•** `Inactive`

SEE ALSO:

createActivation(input)

getActivation(activationId)

updateActivation(activationId, input)

#### ConnectApi.ActivationAttribute

Represents the activation attribute output.

**Property Name** **Type** **Description** **Available Version**

`activationPlatformAttrId` String ID of the activation platform attribute. 60.0

`attributeLabel` String Label of the activation attribute. 60.0

`attributeName` String Name of the activation attribute. 60.0

`curatedFieldId` String Curated ID field for the activation attribute. 60.0

`dataSourceType` String Data source type for the activation attribute. 60.0

`entityName` String Entity name of the activation attribute. 60.0

`filterExpression` `ConnectApi.AttributeFilterExpression` Filter expression for the activation attribute. 60.0

#### path List< ConnectApi. Query path for the activation attributes. 60.0

`QueryPathConfigList`               

`preferredName` String Preferred name of the activation attribute. 60.0

`refAttrDeveloperName` String Developer name of the referrence attribute. 60.0

`source` `DataExportAttributeSourceEnum` Activation attribute source. 60.0

**•** `Direct`

**•** `Related`

`type` `DataExportAttributeTypeEnum` Type of activation attribute. 60.0

**•** `Computed_Dimension`

**•** `Computed_Measure`

**•** `Model`

**•** `Model_Related`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Non_Aggregatable_Computed_Measure`

#### ConnectApi.ActivationAttributeConfig

Represents the configuration for activation attributes.

**Property Name** **Type** **Description** **Available Version**

#### attributes List< ConnectApi.ActivationAttribute > List of activation attributes. 60.0 ConnectApi.ActivationCollection

Represents a collection of activations.

**Property Name** **Type** **Description** **Available Version**

#### activations List< ConnectApi. List of activations. 60.0

`ActivationRepresentation`                   

`batchSize` Integer Number of results returned. If unspecified, the default 60.0
value is `20` .

`offset` Integer Number of records to skip for the next request. 60.0

`orderByExpression` String Sort order for the result set. 60.0

SEE ALSO:

getActivations()

getActivationsPaginated(batchSize, offset, orderBy, filters)

#### ConnectApi.ActivationContactPointFieldConfig

Represents an activation contact point field configuration output.

**Property Name** **Type** **Description** **Available Version**

`attributeId` String ID of the attribute. 60.0

`attributeLabel` String Label of the attribute. 60.0

`attributeName` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

#### ConnectApi.ActivationContactPointsFieldConfig

Represents the activation contact points field configuration output.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`contactPointFields` <List `ConnectApi.ActivationContactPointFieldConfig`    - List of contact point fields. 60.0

#### ConnectApi.ActivationContactPointSourceConfig

Represents an activation contact point source configuration output.

**Property Name** **Type** **Description** **Available Version**

`dataSourceId` String ID of the data source. 60.0

`dataSourceName` String Name of the data source. 60.0

`dataSourcePreference` `ContactPointPrefEnum` Type of contact point. 60.0

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`

**•** `ContactPointPrefPrimary`

`dataSourcePriority` Integer Priority of the data source. 60.0

#### ConnectApi.ActivationContactPointsSourceConfig

Represents the activation contact points source configuration output.

**Property Name** **Type** **Description** **Available Version**

#### contactPointSources <List ConnectApi.ActivationContactPointSourceConfig > List of contact point source configurations. 60.0 ConnectApi.ActivationData

Represents the activation data for an Audience Data Model Object (DMO).

**Property Name** **Type** **Description** **Available Version**

`activatedEntityFqk` String Fully Qualified Key (FQK) of the activated entity. 60.0

`activatedOnId` String ActivateOn entity ID, such as the Individual.Id or the 60.0
Unified Individual.Id.

`activationRecord` String Activated attributes payload as JSON BLOB. 60.0

`deltaType` `AudienceDMODeltaTypeEnum` Delta type of the activation. 60.0

**•** `A` —ADDED

**•** `D` —DELETED

**•** `E` —EXISTING

**•** `U` —UPDATED


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`publishDate` String Date that the activation was published. 60.0

`segmentId` String Unique ID for each segment. 60.0

`segmentOnId` String

Key identifier based on the SegmentOn enity. Same 60.0
as Activated-entity-id when ActivateOn =
SegmentOn.

`segmentedEntityFqk` String Fully Qualified Key (FQK) of the segmented entity. 60.0

#### ConnectApi.ActivationDataSources

Represents the activation data sources configuration output.

**Property Name** **Type** **Description** **Available Version**

#### dataSources <List ConnectApi.ActivationDataSourceConfig > List of activation data source configurations. 60.0 ConnectApi.ActivationDataSourceConfig

Represents an activation data source configuration output.

**Property Name** **Type** **Description** **Available Version**

`dataSourceId` String ID of the data source for the activation. 60.0

`dataSourceName` String Name of the data source for the activation. 60.0

`marketSegmentActivationId` String ID of the market segment activation. 60.0

#### ConnectApi.ActivationExternalPlatformAttributeConfig

Represents the attribute configuration for an activation external platform.

**Property Name** **Type** **Description** **Available Version**

`attributes` List< List of attributes for the external platform. 64.0
#### ConnectApi.ActivationExternalPlatformAttribute > ConnectApi.ActivationExternalPlatformAttribute

Represents an attribute for an activation external platform.

**Property Name** **Type** **Description** **Available Version**

`destinationName` String Destination name of the external platform attribute. 64.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`displayName` String

Display name of the external platform attribute. This 64.0
field is applicable only for ecoSystem external
platforms.

#### ConnectApi.ActivationExternalPlatformCollection

Represents a collection of activation external platforms.

**Property Name** **Type** **Description** **Available Version**

#### platforms <List ConnectApi.ActivationExternalPlatform > List of activation external platforms. 64.0

SEE ALSO:

getActivationExternalPlatforms()

getActivationExternalPlatformsPaginated(limit, offset, orderBy)

#### ConnectApi.ActivationExternalPlatform

Represents information about an activation external platform.

**Property Name** **Type** **Description** **Available Version**

#### attributeConfig ConnectApi.ActivationExternalPlatformAttributeConfig Attribute configuration for the external platform. 64.0

`createdBy` `ConnectApi.CdpUser` User who created the external platform. 57.0

`createdDate` String When the external platform was created. 57.0

`creationType` `ActivationPlatformCreationTypeEnum` Creation type of the external platform. 64.0

**•** `Json`

**•** `Manual`

`id` String The 18-character ID of the external platform. 57.0

`keyPrefixName` String Namespace prefix of the external platform. 64.0

`label` String Label of the external platform. 57.0

`lastModifiedBy` `ConnectApi.CdpUser` User who last modified the external platform. 57.0

`lastModifiedDate` String When the external platform was last modified. 57.0

`name` String Name of the external platform. 57.0

`namespace` String Name space of the external platform. 57.0

`privacyType` `ActivationPlatformPrivacyTypeEnum` Privacy type of the external platform. 64.0

**•** `NotApplicable`

**•** `ServiceProvider`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ThirdParty`

**•** `UpdateFailed`

`status` `ActivationPlatformStatusEnum` Status of the external platform. 64.0

**•** `Active`

**•** `Error`

**•** `Inactive`

**•** `Processing`

`type` `ActivationPlatformTypeEnum` Platform type of the external platform. 64.0

**•** `Advertising`

**•** `Analytics`

**•** `Marketing`

**•** `Publishing`

**•** `Technology`

`url` String URL of the external platform. 57.0

#### ConnectApi.ActivationTarget

Represents an activation target.

**Property Name** **Type** **Description** **Available Version**

`connector` `ConnectApi.DataConnector` Details about the connector that is used for the 60.0
activation target.

`dataSpace` String Data space name for the activation target. 60.0

`description` String Description of the activation target. 60.0

`egressProperties` `ConnectApi.EgressPropertiesRepresentation` Egress properties for the activation target, which are 60.0
applicable only for file-based activation targets.

`historyAudienceDmoApiName` String API name for the history audience DMO. 60.0

`historyAudienceDmoLabel` String Name of the history audience DMO. 60.0

`isCappingEnabled` Boolean Indicates whether communication capping is enabled 60.0
for the activation `(true)` or not `(false)` .

`isEnabled` Boolean Indicates whether the activation target is enabled 60.0
`(true)` or not `(false)` .

`latestAudienceDmoApiName` String API name for the latest audience DMO. 62.0

`latestAudienceDmoLabel` String Name of the latest audience DMO. 62.0

`organizationId` String Organization ID of the activation target. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`platformName` String Platform name for the activation target. 60.0

`platformPrivacyType` String Platform privacy type for the activation target. Derived 60.0
from Activation Platform.

`platformType` `DataConnectorTypeEnum` Data connector type of the activation target. 60.0

**•** `AmazonS3`

**•** `AzureBlob`

**•** `DataCloud`

**•** `GoogleCloudStorage`

**•** `SalesforceMarketingCloud`

**•** `Sftp`

`status` `ActivationTargetStatusEnum` Status of the activation target. 60.0

**•** `Active`

**•** `Processing`

**•** `Error`

**•** `Inactive`

SEE ALSO:

createActivationTarget(input)

getActivationTarget(activationTargetId)

updateActivationTarget(activationTargetId, input)

#### ConnectApi.ActivationTargetCollection

Represents a collection of activation targets.

**Property Name** **Type** **Description** **Available Version**

#### activationTargets List< ConnectApi.ActivationTarget > List of activation targets. 60.0

`batchSize` Integer Number of results returned. Values are from `1` 60.0
through `200` .

`offset` Integer Start offset of the next batch of results. 60.0

`orderByExpression` String Expression that determines the order of the results. 60.0

SEE ALSO:

getActivationTargets()

getActivationTargetsPaginated(batchSize, offset, orderBy, filters)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ActivationTargetSubject

Represents an activation target subject output.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Developer name of the activation target subject. 60.0

`masterLabel` String Master label of the activation target subject. 60.0

#### queryPathConfigListRepresentation List< ConnectApi. Query path for the activation target. 60.0

`QueryPathConfigList`               

ConnectApi.ActivitySharingResult

The results of sharing a captured email or event.

**Property Name** **Type** **Description** **Available Version**

`success` Boolean Whether the share operation succeeded or not. 39.0

#### ConnectApi.Actor

Actor.

This class is abstract.

Superclass of:

#### • ConnectApi.ActorWithId

**•** ConnectApi.RecommendedObject

**•** ConnectApi.UnauthenticatedUser

**Name** **Type** **Description** **Available Version**

`name` String Name of the actor, such as the group name. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`type` String One of the following: 28.0

**•** `file`

**•** `group`

**•** `recommendedObject` (version 34.0 and later)

**•** `unauthenticateduser`

**•** `user`

**•** _`record type name`_ —the name of the record type, such
as `myCustomObject__c` or Account

SEE ALSO:

ConnectApi.CaseCommentCapability

ConnectApi.EntityRecommendation

ConnectApi.EditCapability

ConnectApi.FeedEntitySummary

ConnectApi.FeedItem

ConnectApi.FeedItemSummary

ConnectApi.Subscription

#### ConnectApi.ActorWithId

Actor with ID.

This class is abstract.

Subclass of ConnectApi.Actor.

Superclass of:

**•** ConnectApi.AbstractRecordView

**•** ConnectApi.ArticleSummary

**•** ConnectApi.ChatterGroup

**•** ConnectApi.ContentHubRepository

**•** ConnectApi.File

**•** ConnectApi.RelatedFeedPost

**•** ConnectApi.User

**Name** **Type** **Description** **Available Version**

`id` String Actor’s 18-character ID 28.0

#### `motif ConnectApi.`

```
         Motif

```

An icon that identifies the actor as a user, group, file, or custom 28.0
object. The icon isn’t the user or group photo, and it isn’t a preview
of the file. The motif can also contain the object’s base color.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

#### mySubscription ConnectApi. If the context user is following the item, this contains information 28.0

`Reference` about the subscription, else returns `null` .

`url` String Connect REST API URL for the resource 28.0

SEE ALSO:

ConnectApi.FeedElement

ConnectApi.FeedEntitySummary

ConnectApi.GroupRecord

ConnectApi.MentionSegment

ConnectApi.RecordSummaryList

#### ConnectApi.Address

Address.

**Name** **Type** **Description** **Available Version**

`city` String Name of the city 28.0

`country` String Name of the country 28.0

`formattedAddress` String Formatted address per the locale of the context user 28.0

`state` String Name of the state, province, or so on 28.0

`street` String Street number 28.0

`zip` String Zip or postal code 28.0

SEE ALSO:

ConnectApi.DatacloudCompany

ConnectApi.DatacloudContact

ConnectApi.UserDetail

#### ConnectApi.AdjustOrderSummaryOutputRepresentation

Output representation of the financial changes for an adjust items action. For a preview action, these values are the expected output.
For a submit action, these values are the actual output.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. Expected (for preview) or actual (for submit) financial 49.0

`ChangeItem` values for the price adjustment action. Most of the
`OutputRepresentation` values match the change order values. If two change


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

orders are returned, then these values combine them.
The sign of a value in this output is the opposite of
the corresponding value on a change order record.
For example, a discount is a positive value in
`changeBalances` and a negative value on a
change order record.

`inFulfillment` String ID of the change Order that holds the financial 55.0
`ChangeOrderId` changes applicable to OrderItemSummary quantities
that are in the process of being fulfilled. This change
Order is only created for a request that specified an
`allocatedItemsChangeOrderType` of
InFulfillment. For an adjustPreview call, this value is
always null.

`orderSummaryId` String ID of the OrderSummary. 49.0

`postFulfillment` String ID of the change Order that holds the financial 49.0
`ChangeOrderId` changes applicable to OrderItemSummary quantities
that have been fulfilled. For an adjustPreview call,
this value is always null.

`preFulfillment` String ID of the change Order that holds the financial 49.0
`ChangeOrderId` changes applicable to OrderItemSummary quantities
that have not been fulfilled. If the request specified
an `allocatedItemsChangeOrderType` of
PreFulfillment, this change Order also includes the
changes applicable to OrderItemSummary quantities
that are in the process of being fulfilled. For an
adjustPreview call, this value is always null.

#### ConnectApi.Alternative

Alternative representation for an extension on a feed element.

**Property Name** **Type** **Description** **Available Version**

`text` String Text representation of the extension. 40.0

```
   Representation

```

`thumbnailUrl` String Thumbnail URL to the extension. 40.0

`title` String Title of the extension. 40.0

#### ConnectApi.AlternativePaymentMethodOutput

Alternative payment method details output.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`accountId` String Salesforce Payments account to which this payment 56.0
method is linked.

`comments` String Details about a record added by a user. Maximum of 56.0
1,000 characters.

`email` String Email address of the card holder. 56.0

`gatewayToken` String A unique, alphanumeric ID, called a token, that a 56.0
payment gateway generates when it first processes

a payment. The token replaces the actual payment
data so that the data is kept secure. This token is
stored as encrypted text, and can be used for
recurring payments.

`gatewayToken` String Detailed information about the gateway token. 56.0

```
   Details

```

`name` String Name that you assign to the payment method object. 56.0

#### ConnectApi.Announcement

An announcement displays in a designated location in the Salesforce UI until 11:59 p.m. on its expiration date, unless it’s deleted or
replaced by another announcement.

**Name** **Type** **Description** **Available Version**

`expirationDate` Datetime The Salesforce UI displays an announcement until 11:59 31.0
p.m. on this date unless another announcement is posted

first. The Salesforce UI ignores the time value in the
`expirationDate` . However, you can use the time value
to create your own display logic in your own UI.

#### `feedElement ConnectApi.`

```
         FeedElement

```

The feed element that contains the body of the 31.0
announcement and its associated comments, likes, and so
on.

`id` String 18-character ID of the announcement. 31.0

`isArchived` Boolean Specifies whether the announcement is archived. 36.0

`sendEmails` Boolean Specifies whether the announcement is sent as an email 36.0
to all group members.

`url` String The URL to the announcement. 33.0

SEE ALSO:

#### ConnectApi.AnnouncementPage

ConnectApi.ChatterGroup


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.AnnouncementPage

A collection of announcements.

**Name** **Type** **Description** **Available Version**

#### announcements List<ConnectApi A collection of ConnectApi.Announcement objects. 31.0

```
            .Announcement>

```

`currentPageUrl` String Connect REST API URL identifying the current page. 31.0

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 31.0
if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 31.0
`null` if there isn’t a previous page.

#### ConnectApi.SearchAppliedOrderBy

The applied order for object search.

**Property Name** **Type** **Description** **Available Version**

`field` String Field used to sort the results. 63.0

#### order ConnectApi. Order direction. Values are: 63.0

```
             OrderDirection
```

**•** `Ascending`

**•** `Descending`

#### orderNulls ConnectApi. Null value order. Values are: 63.0

```
             OrderNulls
```

**•** `Firsts` —Null values are sorted first.

**•** `Lasts` —Null values are sorted last.

SEE ALSO:

ConnectApi.ObjectQueryInfo

ConnectApi.SearchObject

#### ConnectApi.ApprovalCapability

If a feed element has this capability, it includes information about an approval.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`id` String

The work item ID. The work item ID is `null` if there 32.0
isn’t a pending work item associated with the
approval record.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
postTemplate

Fields

```

#### List< ConnectApi. The details of the approval post template field. 32.0

```
ApprovalPost
```

`TemplateField` 

`processInstance` String The process instance step ID. The associated record 32.0
`StepId` represents one step in an approval process.

```
status

```

SEE ALSO:

#### ConnectApi. The status of the approval. 32.0

```
WorkflowProcess

Status

```

ConnectApi.FeedElementCapabilities

#### ConnectApi.ApprovalIntent

Approval intent for a social post.

**Property Name** **Type** **Description** **Available Version**

`isRecallable` Boolean Specifies whether the social post can be recalled 45.0
( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.ApprovalPostTemplateField

Approval post template field.

**Name** **Type** **Description** **Available Version**

`displayName` String The field name. 28.0

`displayValue` String The field value or `null` if the field is set to `null` . 28.0

#### `record ConnectApi.`

```
         Reference

```

SEE ALSO:

ConnectApi.ApprovalCapability

#### ConnectApi.ArticleItem

A record ID. 28.0

If no record exists or if the reference is `null`, this value is `null` .

Article item in question and answers suggestions.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String Id of the article. 32.0

`rating` Double The rating of the article. 32.0

`title` String Title of the article. 32.0

`urlLink` String Link URL of the article. 32.0

`viewCount` Integer Number of votes given to the article. 32.0

SEE ALSO:

ConnectApi.QuestionAndAnswersSuggestions

#### ConnectApi.ArticleSummary

A knowledge article summary.

Subclass of ConnectApi.ActorWithId.

**Property Name** **Type** **Description** **Available Version**

`articleType` String Type of the knowledge article. 37.0

`knowledgeArticle` String ID of the knowledge article version. 39.0

```
   VersionId

```

`lastPublishedDate` Datetime Last published date of the knowledge article. 37.0

`rating` Double The rating of the article. 37.0

`summary` String Summary of the knowledge article contents. 37.0

`title` String Title of the knowledge article. 37.0

`urlName` String URL name of the knowledge article. 37.0

`viewCount` Integer Number of times the knowledge article has been 38.0
viewed.

#### ConnectApi.AssociatedActionsCapability

If a feed element has this capability, it has platform actions associated with it.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### platformAction List< ConnectApi. The platform action groups associated with a feed 33.0

`Groups` `PlatformActionGroup`   - element. Platform action groups are returned in the
order specified in the

```
                        ConnectApi.AssociatedActions
```

`CapabilityInput` class.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.AsyncOutputRepresentation

Output representation of the async operation.

Subclass of ConnectApi.BaseAsyncOutputRepresentation.

No additional properties.

SEE ALSO:

multipleEnsureFundsAsync(multipleEnsureFundsInput)

ConnectApi.MultipleAsyncOutputRepresentation

#### ConnectApi.AttributeFilter

Represents the attribute filter output.

**Property Name** **Type** **Description** **Available Version**

`attributeId` String ID of the attribute. 60.0

`attributeName` String Name of the attribute. 60.0

`dateUnits` Datetime Date units for the attribute. 60.0

`operator` String Operator for the attribute. 60.0

`type` `FilterOperatorDataTypeEnum` Type of attribute. 60.0

**•** `FilterOperatorDataTypeBoolean`

**•** `FilterOperatorDataTypeDate`

**•** `FilterOperatorDataTypeDateOnly`

**•** `FilterOperatorDataTypeExactlyRelativeDate`

**•** `FilterOperatorDataTypeNumber`

**•** `FilterOperatorDataTypeRelateToNowDate`

**•** `FilterOperatorDataTypeText`

`values` List<String> Values for the attribute. 60.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.AttributeFilterExpression

Represents the activation attribute filter expression.

**Property Name** **Type** **Description** **Available Version**

`conjunction` `FilterConjunctionEnum` Conjunction for the activation attribute filter 60.0
expression.

**•** `FilterConjunctionAnd`

**•** `FilterConjunctionOr`

#### filters List< ConnectApi.AttributeFilter > List of attribute filters. 60.0 ConnectApi.Audience

A personalization audience.

**Property Name** **Type** **Description** **Available Version**

```
criteria

```

#### List< ConnectApi. Criteria details for the audience. 48.0

```
AudienceCriteria
```

`Detail` 

`customFormula` String Custom formula for the audience criteria. For 48.0
example, (1 AND 2) OR 3.

#### formulaFilterType ConnectApi. Formula filter type for the personalization audience. 48.0

`FormulaFilterType` Values are:

**•** `AllCriteriaMatch` —All audience criteria
are true (AND operation).

**•** `AnyCriterionMatches` —Any audience
criterion is true (OR operation).

**•** `CustomLogicMatches` —Audience criteria
match the custom formula (for example, (1 AND
2) OR 3).

`id` String ID of the audience. 48.0

`name` String Name of the audience. 48.0

```
targets

```

#### List< ConnectApi. Target assignments for the audience. 48.0

```
AudienceTarget
```

`Assignment` 

`url` String URL to this audience. 48.0

SEE ALSO:

#### ConnectApi.AudienceCollection


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.AudienceCollection

Collection of personalization audiences.

**Property Name** **Type** **Description** **Available Version**

#### audiences List< ConnectApi. Collection of audiences. 48.0

`Audience`            
#### ConnectApi.AudienceCriteria

Custom recommendation audience criteria.

This class is abstract.

This class is a superclass of:

**•** ConnectApi.CustomListAudienceCriteria

**•** ConnectApi.NewUserAudienceCriteria

**Property Name** **Type** **Description** **Available Version**

```
type

```

SEE ALSO:

#### ConnectApi. Specifies the custom recommendation audience 36.0

`RecommendationAudience` criteria type. One of these values:

```
CriteriaType
```

**•** `CustomList` —A custom list of users makes
up the audience.

**•** `MaxDaysInCommunity` —New members
make up the audience.

ConnectApi.RecommendationAudience

#### ConnectApi.AudienceCriteriaDetail

Personalization audience criteria.

**Property Name** **Type** **Description** **Available Version**

```
criterion

```

#### List< ConnectApi. List of mappings of audience criteria fields and values. 48.0

```
AudienceCriterion
```

`Detail` 

`criterionNumber` Integer Number associated with the audience criterion in a 48.0
formula. For example, (1 AND 2) OR 3. If unspecified,

criteria are assigned numbers in the order that they’re
added.

```
criterionOperator

```

#### ConnectApi. Operator used in the personalization audience 48.0

`AudienceCriteria` criterion. Values are:

```
Operator
```

**•** `Contains`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `Includes`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `NotIncludes`

**•** `StartsWith`

```
criterionType

```

SEE ALSO:

#### ConnectApi.Audience

#### ConnectApi. Type of personalization audience criterion. Values 48.0

`AudienceCriteria` are:

```
Type
```

**•** `Audience` —Criterion based on audience.

**•** `Default` —Audience has no criteria.

**•** `Domain` —Criterion based on domain.

**•** `FieldBased` —Criterion based on object
fields.

**•** `GeoLocation` —Criterion based on location.

**•** `Permission` —Criterion based on standard
or custom permissions.

**•** `Profile` —Criterion based on profile.

#### ConnectApi.AudienceCriterionDetail

Audience criterion information.

**Property Name** **Type** **Description** **Available Version**

`value` Map<String, String> Mapping of an audience criterion value and field. 48.0

SEE ALSO:

ConnectApi.AudienceCriteriaDetail

#### ConnectApi.AudienceDMOCollection

Represents a collection of Audience Data Model Object (DMO) records.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`batchSize` Integer Batch size 60.0

`data` List< `ConnectApi.ActivationData`   - List of Audience DMO records. 60.0

`offset` Integer Start offset of the next batch. 60.0

SEE ALSO:

getActivationData(activationId)

#### ConnectApi.AudienceTarget

Personalization audience assigned to a target.

**Property Name** **Type** **Description** **Available Version**

`audienceName` String Name of the audience assigned to the target. 48.0

`id` String ID of the audience assigned to the target. 48.0

`url` String URL to the audience assigned to the target. 48.0

SEE ALSO:

ConnectApi.Target

#### ConnectApi.AudienceTargetAssignment

Target assignments for a personalization audience.

**Property Name** **Type** **Description** **Available Version**

#### formulaScope ConnectApi. Formula scope of the target. 51.0

```
             FormulaScope

```

`groupName` String Group name of the target. Groups bundle related 48.0
target and audience pairs.

`id` String ID of the target. 48.0

`isMatch` Boolean Specifies whether the target matches the current 48.0
context ( `true` ) or doesn’t ( `false` ).

`priority` Integer

Priority of the target. Within a group, priority 48.0
determines which target is returned if the user
matches more than one audience.

#### publishStatus ConnectApi. Publish status of the target. Values are: 48.0

```
          PublishStatus
```

**•** `Draft`

**•** `Live`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`targetType` String Type of target, indicating the nature of the data being 48.0
targeted.

`targetValue` String Value of the target. 48.0

`url` String URL to the target. 48.0

SEE ALSO:

ConnectApi.Audience

#### ConnectApi.AuthReversalGatewayResponse

Authorization Reversal Gateway Response Representation.

Subclass of ConnectApi.AbstractGatewayResponse.

No additional properties.

#### ConnectApi.AuthorizationGatewayResponse

Payment gateway authorization response representation.

Subclass of ConnectApi.AbstractGatewayResponse.

**Property Name** **Type** **Description** **Available Version**

`gatewayAuthorizationCode` String Gateway authorization code. 51.0

#### ConnectApi.AuthorizationResponse

Payment Authorization output representation.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error representation for the payment authorization. 51.0

```
             ErrorResponse

```

```
gatewayResponse

```

#### ConnectApi. Gateway response representation for the payment 51.0

`AuthorizationGateway` authorization.

```
Response

```

`isMultiCapture` Boolean

```
Supported

```

Indicates whether the authorization status from a 64.0
payment gateway, such as Stripe, supports multiple
captures ( `true` ) or not ( `false` ).

```
payment

Authorization

```

#### ConnectApi. Payment authorization representation. 51.0

```
Payment

AuthorizationResponse

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
paymentGateway

Logs

paymentGroup

paymentMethod

```

#### List< ConnectApi. Gateway log list representation for the payment 51.0

`GatewayLog` authorization.
`Response` 
#### ConnectApi. Payment group representation for the payment 51.0

`PaymentGroup` authorization.

```
Response

#### ConnectApi. Payment method representation for the payment 51.0
```

`Payment` authorization.

```
MethodResponse

```

#### ConnectApi.AuthorizationReversalResponse

Authorization Reversal output representation.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error response representation for the authorization 51.0

`ErrorResponse` reversal.

```
gatewayResponse

paymentAuthAdjustment

```

#### ConnectApi. Gateway response representation for authorization 51.0

`AuthReversal` reversal.

```
GatewayResponse

#### ConnectApi. Payment authorization adjustment response 51.0
```

`PaymentAuth` representation for the authorization reversal.

```
AdjustmentResponse

```

#### paymentGatewayLogs List< ConnectApi. Gateway log collection representation for the 51.0

`GatewayLogResponse`           - authorization reversal.

#### ConnectApi.AvailableLocationOutputRepresentation

A set of inventory locations that can combine to fulfill an order.

**Property Name** **Type** **Description** **Available Version**

`locations` List< `String` - A list of inventory locations. 51.0

SEE ALSO:

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation

ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.AverageDistanceResultOutputRepresentation

Wraps inventory location shipping distance calculation results.

**Property Name** **Type** **Description** **Available Version**

```
distanceCalculation

```

#### ConnectApi. Results of the shipping distance calculations. 51.0

```
DistanceCalculation

OutputRepresentation

```

#### ConnectApi.BalanceStatePreviewOutputRepresentation

The generated preview of all balances for an order or a cart, including totals, adjustments, and taxes.

**Property Name** **Type** **Description** **Available Version**

`grandTotalAmount` Double The grand total of the exchanges, including 61.0
adjustments, fees, delivery cost, and taxes.

`totalAdjustmentAmount` Double The total amount the order was adjusted by, not 61.0
including tax.

`totalAdjustmentAmountWithTax` Double The total amount the order was adjusted by, 61.0
including tax.

`totalAmount` Double The total amount being return, not including tax. 61.0

`totalAmountWithTax` Double The total amount being return, including tax. 61.0

`totalDeliveryAmount` Double The total cost for delivery, not including tax. 61.0

`totalDeliveryAmountWithTax` Double The total cost for delivery, including tax. 61.0

`totalFeeAmount` Double The combined total of all fees charged, not including 61.0
tax.

`totalFeeAmountWithTax` Double The combined total of all fees charged, including tax. 61.0

`totalTaxAmount` Double The combined total of all taxes. 61.0

#### ConnectApi.BannerCapability

If a feed element has this capability, it has a banner motif and style.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`motif` `ConnectApi.Motif` A banner motif. 31.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`style` `ConnectApi.BannerStyle` Decorates a feed item with a color and set of icons. 31.0
Possible value:

**•** `Announcement` —An announcement displays
in a designated location in the Salesforce UI until
11:59 p.m. on its expiration date, unless it’s
deleted or replaced by another announcement.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.BannerPhoto

A banner photo.

**Property Name** **Type** **Description** **Available Version**

`bannerPhotoUrl` String URL to the banner photo in a large format. This URL 36.0
is available only to authenticated users.

`bannerPhoto` String 18-character version ID of the banner photo. 36.0

```
   VersionId

```

`url` String URL to the banner photo. 36.0

SEE ALSO:

ConnectApi.ChatterGroup

ConnectApi.UserDetail

#### ConnectApi.BaseAsyncOutputRepresentation

Base Order Management async output class.

This class is abstract.

Subclass of ConnectApi.BaseOutputRepresentation.

Superclass of:

**•** ConnectApi.AsyncOutputRepresentation

**•** ConnectApi.EnsureFundsAsyncOutputRepresentation

**•** ConnectApi.EnsureRefundsAsyncOutputRepresentation

**Property Name** **Type** **Description** **Available Version**

`background` String ID of the background operation. 48.0

```
   OperationId

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.BaseComparison

Represents the abstract class for a base comparison output.

**Property Name** **Type** **Description** **Available Version**

`filters` List< `ConnectApi.TypeAndFilter`   - List of logical comparison filters. 60.0

`operator` String operator 60.0

#### ConnectApi.BaseInvoiceOutputRepresentation

Base Order Management Invoice output class.

This class is abstract.

Subclass of ConnectApi.BaseOutputRepresentation.

Superclass of ConnectApi.ChangeOrdersInvoiceOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`invoiceId` String ID of the created invoice. 56.0

#### ConnectApi.BaseManagedSocialAccount

Base information describing a managed social account or fan page of a social network.

This class is abstract.

Superclass of ConnectApi.ManagedSocialAccount.

**Property Name** **Type** **Description** **Available Version**

`defaultResponse` String Default response account to use when replying to 44.0
`AccountId` posts sent to this account.

`displayName` String Real name (or user name if real name not available) 44.0
for this account on the social network.

`externalPictureUrl` String URL to the account's avatar image. 44.0

`id` String Internal SFDC ID for this managed social account. 44.0

`label` String Label for the social account. 44.0

`profileUrl` String URL to the account's profile. 44.0

#### socialNetwork ConnectApi. Social network that this account belongs to. Values 44.0

`SocialNetworkProvider` are:

**•** `Facebook`

**•** `GooglePlus`

**•** `Instagram`

**•** `InstagramBusiness`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `KakaoTalk`

**•** `Kik`

**•** `Line`

**•** `LinkedIn`

**•** `Messenger`

**•** `Other`

**•** `Pinterest`

**•** `QQ`

**•** `Rypple`

**•** `SinaWeibo`

**•** `SMS`

**•** `Snapchat`

**•** `Telegram`

**•** `Twitter`

**•** `VKontakte`

**•** `WeChat`

**•** `WhatsApp`

**•** `YouTube`

`uniqueName` String Unique name used for distinguishing same name fan 44.0
pages; acts like a user name for a fan page.

`username` String Unique user name or handle for this account on the 44.0
social network.

#### ConnectApi.BaseOutputRepresentation

Base Order Management output class.

This class is abstract.

Superclass of:

**•** ConnectApi.AdjustOrderSummaryOutputRepresentation

**•** ConnectApi.BaseAsyncOutputRepresentation

**•** ConnectApi.BaseInvoiceOutputRepresentation

**•** ConnectApi.ConfirmHeldFOCapacityOutputRepresentation

**•** ConnectApi.CreateCreditMemoOutputRepresentation

**•** ConnectApi.CreateMultipleInvoicesFromChangeOrdersOutputRepresentation

**•** ConnectApi.CreateOrderPaymentSummaryOutputRepresentation

**•** ConnectApi.EnsureFundsAsyncOutputRepresentation

**•** ConnectApi.EnsureRefundsAsyncOutputRepresentation

**•** ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation

**•** ConnectApi.FindRoutesWithFewestSplitsWithInventoryOutputRepresentation

**•** ConnectApi.FulfillmentGroupOutputRepresentation

**•** ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation

**•** ConnectApi.FulfillmentOrderInvoiceOutputRepresentation

**•** ConnectApi.FulfillmentOrderOutputRepresentation

**•** ConnectApi.GetFOCapacityValuesOutputRepresentation

**•** ConnectApi.HoldFOCapacityOutputRepresentation

**•** ConnectApi.MultipleAsyncOutputRepresentation

**•** ConnectApi.MultipleFulfillmentOrderInvoicesOutputRepresentation

**•** ConnectApi.MultipleFulfillmentOrderOutputRepresentation

**•** ConnectApi.OrderSummaryOutputRepresentation

**•** ConnectApi.PreviewCancelOutputRepresentation

**•** ConnectApi.PreviewReturnOutputRepresentation

**•** ConnectApi.ProductDetailsOutputRepresentation

**•** ConnectApi.RankAverageDistanceOutputRepresentation

**•** ConnectApi.RegisterGuestBuyerOutputRepresentation

**•** ConnectApi.ReleaseHeldFOCapacityOutputRepresentation

**•** ConnectApi.ReturnItemsOutputRepresentation

**•** ConnectApi.ReturnOrderItemSplitLineOutputRepresentation

**•** ConnectApi.ReturnOrderOutputRepresentation

**•** ConnectApi.SubmitCancelOutputRepresentation

**•** ConnectApi.SubmitReturnOutputRepresentation

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. Any errors that were returned. 48.0

`ErrorResponse`            

`success` Boolean Indicates whether the transaction was successful. 48.0

#### ConnectApi.BatchResult

The result of an operation returned by a batch method.

Usage

Calls to batch methods return a list of `BatchResult` objects. Each element in the `BatchResult` list corresponds to the strings
in the list parameter passed to the batch method. The first element in the `BatchResult` list matches the first string passed in the
list parameter, the second element corresponds with the second string, and so on. If only one string is passed, the `BatchResult` list
contains a single element.


Apex Reference Guide ConnectApi Output Classes

Example

The following example shows how to obtain and iterate through the returned `ConnectApi.BatchResult` objects. The code
adds two group IDs to a list. One of group IDs is incorrect, which causes a failure when the code calls the batch method. After it calls the
batch method, it iterates through the results to determine whether the operation was successful or not for each group ID in the list. The
code writes the ID of every group that was processed successfully to the debug log. The code writes an error message for every failed
group.

This example generates one successful operation and one failure.

```
   List<String> myList = new List<String>();

   // Add one correct group ID.

   myList.add('0F9D00000000oOT');

   // Add one incorrect group ID.

   myList.add('0F9D00000000izf');

   ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterGroups.getGroupBatch(null,

   myList);

   // Iterate through each returned result.

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print the group ID.

        ConnectApi.ChatterGroupSummary groupSummary;

        if(batchResult.getResult() instanceof ConnectApi.ChatterGroupSummary) {

          groupSummary = (ConnectApi.ChatterGroupSummary) batchResult.getResult();

        }

        System.debug('SUCCESS');

        System.debug(groupSummary.id);

      }

      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

```


Apex Reference Guide ConnectApi Output Classes

IN THIS SECTION:

##### BatchResult Methods These are instance methods for BatchResult .

SEE ALSO:

getCommentBatch(communityId, commentIds)

getFeedElementBatch(communityId, feedElementIds)

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, readBy)

postFeedElementBatch(communityId, feedElements)

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, isReadByMe)

getMembershipBatch(communityId, membershipIds)

getGroupBatch(communityId, groupIds)

getUserBatch(communityId, userIds)

addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems, currencyIsoCode)

addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems)

getAudienceBatch(communityId, audienceIds)

getTargetBatch(communityId, targetIds)

getMotifBatch(communityId, idOrPrefixList)

##### BatchResult Methods These are instance methods for BatchResult .

IN THIS SECTION:

###### getError()

If an error occurred, returns a `ConnectApi.ConnectApiException` object providing the error code and description.

getErrorMessage()
Returns a String that contains an error message.

getErrorTypeName()
Returns a String that contains the name of the error type.

getResult()
Returns an object that contains the results of the batch operation. The object is typed according to the batch method. For example,
if you call `getMembershipBatch()`, a successful call to BatchResult `getResult()` returns a
`ConnectApi.GroupMembership` object.

isSuccess()
Returns a Boolean that is set to `true` if the batch operation was successful for this object, `false` otherwise.

###### getError()

If an error occurred, returns a `ConnectApi.ConnectApiException` object providing the error code and description.


Apex Reference Guide ConnectApi Output Classes

Signature

```
   public ConnectApi.ConnectApiException getError()

```

Return Value

Type: `ConnectApi.ConnectApiException`

###### getErrorMessage()

Returns a String that contains an error message.

Signature

```
   public String getErrorMessage()

```

Return Value

Type: String

Usage

The error message doesn’t make a round trip through a Visualforce view state, because exceptions can’t be serialized.

###### getErrorTypeName()

Returns a String that contains the name of the error type.

Signature

```
   public String getErrorTypeName()

```

Return Value

Type: String

###### getResult()

Returns an object that contains the results of the batch operation. The object is typed according to the batch method. For example, if
###### you call getMembershipBatch(), a successful call to BatchResult getResult() returns a

`ConnectApi.GroupMembership` object.

Signature

```
   public Object getResult()

```

Return Value

Type: Object


Apex Reference Guide ConnectApi Output Classes

###### isSuccess()

Returns a Boolean that is set to `true` if the batch operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

#### ConnectApi.BestLocationPerSKUOutputRepresentation

A recommended fulfillment location for a specific SKU, including available quantity and score.

**Property Name** **Type** **Description** **Available Version**

`errors` List< `ConnectApi.ErrorResponse`   - Any errors that were returned. 67.0

`locationId` String The location's ID. 67.0

`quantityAvailable` Integer The quantity available to order at this location. 67.0

```
   ToOrder

```

`success` Boolean Indicates whether the request succeeded. 67.0

`unitScore` Double The score for this SKU at this location. 67.0

#### ConnectApi.BlankRecordField

Record field displayed as a place holder in a grid of fields.

Subclass of ConnectApi.AbstractRecordField.

#### ConnectApi.PromotionBonusProduct

Bonus product for a promotion.

**Property Name** **Type** **Description** **Available Version**

`adjustmentBasis` String ID of the associated coupon, if applicable. 58.0

```
   Reference

```

`bonusProductId` String ID of the bonus product. 58.0

`causeId` String ID of the related promotion. 58.0

#### qualifyingItems List< ConnectApi. List of qualifying cart items and their related quantity. 58.0

```
             Promotion

             CartItemKey on
```

`page 2258`            


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.BookmarksCapability

If a feed element has this capability, the context user can bookmark it.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isBookmarked` Boolean

```
ByCurrentUser

```

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.BookmarkSummary

Summary of a bookmark.

Indicates whether the feed element has been 32.0
bookmarked by the context user ( `true` ) or not
( `false` ).

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.BotInfoRepresentation

Information about the bot associated with the conversation application.

**Property Name** **Type** **Description** **Available Version**

`botId` String ID of the bot. 54.0

`botName` String Name of the bot. 54.0

`lastModifiedDate` Datetime Last modified date of the bot definition. 54.0

#### ConnectApi.BotVersionActivationInfo

Success or failure information of the bot version activation.

**Property Name** **Type** **Description** **Available Version**

`isActivated` Boolean Indicates whether the bot is active or not. 51.0

`messages` List<String> Failure messages. 50.0

`success` Boolean Indicates whether the activation was successful or 50.0
not.

#### ConnectApi.BusObjAssociationsOutputRepresentation

Association details of a business objective


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String 18-character unique identifier for the business 59.0
objective association.

```
type

```

#### ConnectApi. Definition category of the business objective, or goal. 59.0

`GoalDefinition` Values are:

```
CategoryEnum
```

**•** `Webstore`

#### ConnectApi.BusObjInsightsOutputRepresentation

Insights related to a business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String

`current` Double

The three-letter ISO currency code associated with 62.0
the KPI values. For example, 'USD' for US dollars or
'EUR' for euros.

The current value of the KPI metric. This represents 59.0
the most recent measurement or calculation of the
business objective's key performance indicator.

```
insights

```

#### List< ConnectApi. A collection of insights related to the business 62.0

`InsightsOutput` objective.
`Representation` 

`kpiDashboardUrl` String The URL to the dashboard where the KPI details and 62.0
visualizations can be viewed.

`kpiSummaryText` String A human-readable summary of the KPI's performance, 62.0
including the change from the previous value.

`last` Double

`period` String

The previous value of the KPI metric, used for 59.0
comparison with the current value to track progress
or changes over time.

The time period between the current and last values, 59.0
such as 'Daily', 'Weekly', 'Monthly', or 'Quarterly'. This
indicates the frequency of KPI measurements.

`targetCompletionDate` Datetime Target date for completion of the goal. 62.0

`targetValue` Double Target value for the goal. 62.0

```
unit

```

#### ConnectApi. Unit for an insight. Values are: 59.0

```
ConnectInsight
```

**•** `Count`
```
UnitEnum

```

**•** `Count`

**•** `Currency`

**•** `Dollar`

**•** `Number`

**•** `Percent`


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.BusObjOutputRepresentation

Business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

```
associations

```

#### List< ConnectApi. List of business objective associations. 59.0

```
BusObjAssociations
```

`OutputRepresentation` 

`description` String Description of the business objective. 59.0

`displayName` String Display name of the business objective. 59.0

`id` String ID of the business objective. 59.0

#### ConnectApi.BusObjRecommendationsOutputRepresentation

Details of the recommended actions for a business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

`active` Integer Count of active recommended actions. 59.0

`complete` Integer Count of completed recommended actions. 59.0

`total` Integer Count of total recommended actions, including both 59.0
completed and active.

#### ConnectApi.BusObjSummaryOutputRepresentation

Summary of a business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the business objective. 59.0

`id` String ID of the business objective. 59.0

```
insightSummary

```

#### ConnectApi. Summary of insights related to the business objective. 59.0

```
BusObjInsights

OutputRepresentation

```

`kpi` String Key performance indicator associated with the 61.0
business objective.

`labelName` String Display name of the business objective. 59.0

```
recommendationSummary

```

#### ConnectApi. Summary of recommended actions for the business 59.0

`BusObjRecommendations` objective.

```
OutputRepresentation

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.BusinessObjectivesOutputRepresentation

List of business objectives, or goals.

**Property Name** **Type** **Description** **Available Version**

```
businessObjectives

```

#### List< ConnectApi. List of created business objectives. 59.0

```
BusObj
```

`OutputRepresentation` 

#### ConnectApi.BusinessObjectivesSummaryOutputRepresentation

List of summaries for business objectives, or goals.

**Property Name** **Type** **Description** **Available Version**

```
businessObjectivesSummary

```

#### List< ConnectApi. List of business objective summaries. 59.0

```
BusObjSummary
```

`OutputRepresentation` 

#### ConnectApi.BuyerProductSummaryRepresentation

Representation of the buyer's product summary.

**Property Name** **Type** **Description** **Available Version**

`id` String> ID of the product. 66.0

`name` String Name of the product. 66.0

`image` `ConnectApi.ProductImageOutputRepresentation` Product summary information for the line item. 66.0

`variationAttributes` `ConnectApi.ProductVariationAttributesRepresentation` List of variation attributes (color, size, and so on) 66.0
associated with the product.

`fields` Map<String, Product summary details for the line item. 66.0
`[ConnectApi.RecordFieldRepresentation](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_recordField.htm)`                      

`sku` String Stock Keeping Unit (SKU) of the product. 66.0

`canViewProduct` Boolean Indicates whether the context user can view the 66.0
product ( `true` ) or not ( `false` ).

`success` Boolean Indicates whether the request was successful ( `true` ) 66.0
or not ( `false` ).

#### ConnectApi.BundleCapability

If a feed element has this capability, it has a container of feed elements called a _bundle_ .

This class is abstract.

Subclass of ConnectApi.FeedElementCapability.


Apex Reference Guide ConnectApi Output Classes

Superclass of:

**•** ConnectApi.GenericBundleCapability

**•** ConnectApi.TrackedChangeBundleCapability

**Property Name** **Type** **Description** **Available Version**

#### `bundleType ConnectApi.`

```
          BundleType

```

Defines this feed element's bundle type. The bundle 31.0
type determines what additional information appears
in the bundle.

#### page ConnectApi. A collection of feed elements. 31.0

```
           FeedElementPage

```

`totalElements` Integer The total number of feed elements that this bundle 31.0
aggregates.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.CalculateCartResult

Result of a cart calculate request. Includes a cart summary with calculated cart values.

Subclass of ConnectApi.CommerceResultRepresentationBase

**Property Name** **Type** **Description** **Available Version**

`data` ConnectApi.CartSummary A cart summary with calculated cart values. 62.0

#### ConnectApi.CartFromQuoteOutput

Representation of the response for creating a cart from a quote.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the cart created from the quote. 67.0

`errors` List< Detailed error message if the create cart from a quote 67.0
`ConnectApi.QuoteError`             - operation was unsuccessful.

#### ConnectApi.CalculateTaxResponse

Shows the results of a tax calculation request.

Subclass of ConnectApi.TaxTransactionResponse.

**Property Name** **Type** **Description** **Available Version**

#### adapterError ConnectApi. Adapter error. 55.0

```
           ErrorResponse

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
status

taxEngineLogs

taxTransactionType

```

#### ConnectApi. Status of a tax transaction. Values are: 55.0

```
TaxTransaction
```

**•** `Committed` —Tax has been committed to the

`Status` transaction.

**•** `Uncommitted` —Tax hasn’t been committed
to the transaction.

#### List< ConnectApi. Tax engine logs. 55.0

```
TaxEngine
```

`LogResponse` 

#### ConnectApi. Type of tax transaction. Values are: 55.0

```
TaxTransaction
```

**•** `Credit` —Transaction is a credit transaction.
```
Type

```

**•** `Credit` —Transaction is a credit transaction.

**•** `Debit` —Transaction is a debit transaction.

**•** `Void` —Reserved for internal use in case of input.
In case of output, this value specifies that the tax
engine has voided the document that's
mentioned as the
`referenceDocumentCode` property value.

#### taxType ConnectApi. Type of tax calculation. Values are: 55.0

```
           CalculateTaxType
```

**•** `Actual` —Calculated tax represents the final
taxed amount for the transaction.

**•** `Estimated` —Calculated tax represents only
an estimated value before the transaction is
finalized.

#### ConnectApi.CallCollaborationCapability

If a feed element has this capability, it has a recording comment.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`commentEndTime` Integer End time of the comment on the media player, in 51.0
seconds.

`commentStartTime` Integer Start time of the comment on the media player, in 51.0
seconds.

SEE ALSO:

ConnectApi.FeedElementCapabilities


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CancelAllOrderItemsAsyncOutputRepresentation

ID of the asynchronous background operation.

Subclass of ConnectApi.BaseAsyncOutputRepresentation on page 2236.

**Property Name** **Type** **Description** **Available Version**

`asyncOperationLogId` String ID of the background operation. 63.0

#### ConnectApi.CandidateAnswersStatus

The status of candidate answers on a feed element.

**Property Name** **Type** **Description** **Available Version**

`hasCandidate` Boolean Indicates whether candidate answers are available 41.0
`Answers` for a question.

`hasCandidate` Boolean Indicates whether any candidate answers are 41.0
`AnswersPublished` published.

`hasCandidate` Boolean Indicates whether any candidate answers are rated. 41.0

```
   AnswersRated

```

SEE ALSO:

ConnectApi.QuestionAndAnswersCapability

#### ConnectApi.CanvasCapability

If a feed element has this capability, it renders a canvas app.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`description` String A description of the canvas app. The maximum size 32.0
is 255 characters.

`developerName` String The API name (developer name) of the client app. 32.0

`height` String The height of the canvas app in pixels. 32.0

`icon` `ConnectApi.Icon` The icon for the canvas app. 32.0

`namespacePrefix` String A unique namespace prefix for the canvas app. 32.0

`parameters` String JSON parameters passed to the canvas app. 32.0

`thumbnailUrl` String A thumbnail URL to a preview image. The maximum 32.0
thumbnail size is 120 pixels by 120 pixels.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`title` String A title for the canvas link. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.CapacityResponseOutputRepresentation

Response to a request related to a location’s fulfillment capacity.

**Property Name** **Type** **Description** **Available Version**

`actionRequestId` String Unique string that identifies the original capacity 55.0
request.

#### error ConnectApi. Error returned by the request, if any. 55.0

```
             ErrorResponse

```

`success` Boolean Indicates whether the request was successful. 55.0

#### ConnectApi.CaptureGatewayResponse

Gateway capture response.

Subclass of ConnectApi.AbstractGatewayResponse.

No additional properties.

#### ConnectApi.CaptureResponse

Capture output.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error response representation for an authorization 50.0

`ErrorResponse` capture.

#### `gatewayResponse ConnectApi.`

```
          CaptureGatewayResponse

#### `payment ConnectApi.`

          PaymentResponse

```

Gateway log response containing details about 50.0
gateway logs created during the process of the
capture request.

Payment response object for the capture request. 50.0
Contains the information related to a payment object
created during request processing.

#### paymentGatewayLogs List< ConnectApi. Gateway log collection for an authorization capture. 50.0

`GatewayLogResponse`           
#### paymentGroup ConnectApi. Payment group associated with the capture request. 50.0

```
          PaymentGroupResponse

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CardPaymentMethodOutput

Card payment method details output.

**Property Name** **Type** **Description** **Available Version**

`accountId` String Salesforce Payments account to which this payment 56.0
method is linked.

`autoPay` Boolean Indicates whether a token for recurring payments is 56.0
being requested ( `true` ) or not ( `false` ). The token

lets the payment method be used for recurring
payments.

`cardBin` String

Bank Identification Number (BIN). The BIN is the first 56.0
4-6 numbers on a payment card that identifies the
card issuer.

#### cardCategory ConnectApi. 56.0

**•** `CreditCard`
CardCategory

**•** `DebitCard`

`cardHolderFirstName` String First name of the card holder 56.0

`cardHolderLastName` String Last name of the card holder 56.0

`cardHolderName` String Full name of card holder 56.0

`cardLastFour` String Last four digits on a card. 56.0

`cardType` ConnectApi.CardType Credit card issuer. 56.0

**•** `AmericanExpress`

**•** `DinersClub`

**•** `JCB`

**•** `Maestro`

**•** `MasterCard`

**•** `Visa`

`comments` String Details about a record added by a user. Maximum of 56.0
1,000 characters.

`displayCardNumber` String Card displayed number 56.0

`email` String Email address of the card holder. 56.0

`expiryMonth` Integer Card expiration month 56.0

`expiryYear` Integer Card expiration year 56.0

`nickName` String Optional card nickname 56.0

`startMonth` Integer Month when card becomes active 56.0

`startYear` Integer Year when card becomes active 56.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CartCoupon

Cart Coupon representation.

**Property Name** **Type** **Description** **Available Version**

`cartCouponId` String ID of the cart coupon code. 54.0

`couponCode` String The coupon code a buyer can use to manually apply 54.0
a promotion to the cart.

#### ConnectApi.CartCouponCollection

Collection of coupons related to a cart.

**Property Name** **Type** **Description** **Available Version**

#### cartCoupons ConnectApi.CartCouponList Collection of coupons. 54.0

`cartId` String ID of the cart. 54.0

#### cartStatus ConnectApi. Status of the cart. Values are: 54.0

```
             CartStatus
```

**•** `Active—` Cart is created and available for
modifications, like adding or removing products
or promotions.

**•** `Checkout—` Cart is in checkout. If the customer
modifies the cart, the current checkout session
is canceled.

**•** `Closed—` Checkout is complete and an order
was created. The cart cannot be modified.

**•** `PendingClosed—` Cart is marked to be closed,
but the request isn't completed yet. The cart can’t
be modified. This value is available in API version
57.0 and later.

**•** `PendingDelete—` Cart is marked for delete,
but the request isn't completed yet. The cart can’t
be modified.

**•** `Processing—` Cart is processing. For example,
taxes are being calculated. The cart can’t be
modified.

`ownerId` String ID of the user who owns the cart. 54.0

#### ConnectApi.CartCouponList

List of coupons for a cart.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`coupons` List< `ConnectApi.CartCoupon`    - List of coupons associated with a cart. 54.0

#### ConnectApi.PromotionCartDeliveryGroupMethod

Cart delivery group method for a promotion.

**Property Name** **Type** **Description** **Available Version**

#### cartDelivery List< ConnectApi. List of cart delivery method adjustments. 60.0

```
   MethodAdjustments PromotionCart

             DeliveryMethod

             Adjustment on
```

`page 2544`            

`cartDelivery` String ID of the cart delivery method. 60.0

```
   MethodId

```

`price` String Price 60.0

`shippingRateId` String ID of the shipping rate. 62.0

`totalAdjustment` String Total amount of the adjustment. 60.0

```
   BaseAmount

```

`totalNetAmount` String Final price of the cart item after all adjustments. 60.0

#### ConnectApi.PromotionCartDeliveryGroup

Cart delivery group for a promotion.

**Property Name** **Type** **Description** **Available Version**

`cartDeliveryGroupId` String ID of the cart delivery group. 60.0

#### cartDelivery List< ConnectApi. List of methods for the delivery group. 60.0

```
   GroupMethods PromotionCart

             DeliveryGroupMethod
```

`on page 2254`            

`id` String ID of the cart. 60.0

#### ConnectApi.CartInventoryItemReservationOutputRepresentation (Pilot)

Inventory item reservation.

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on


Apex Reference Guide ConnectApi Output Classes

the basis of generally available products and features. This feature is made available on an AS IS basis and use of this feature is at
your sole risk.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code for this reservation item. 58.0

`errorMessage` String Error message for this reservation item. 58.0

`id` String ID for this reservation item. 58.0

`itemReservation` String Item reservation source ID for this reservation item. 58.0

```
   SourceId

```

`productId` String Product ID for this reservation item. 58.0

`quantity` Double Quantity for this reservation item. 58.0

`reservedAt` String Reserved at location or group ID for this reservation 58.0
`LocationId` item.

#### ConnectApi.CartInventoryReservationOutputRepresentation (Pilot)

Inventory Reservation

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on
the basis of generally available products and features. This feature is made available on an AS IS basis and use of this feature is at
your sole risk.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code for this reservation. 58.0

`errorMessage` String Error message for this reservation. 58.0

#### inventoryItem List< ConnectApi. Collection of inventory item reservations. 58.0

```
   Reservations CartInventory

             ItemReservation
```

`OutputRepresentation`                

`reservation` String Reservation identifier. 58.0

```
   Identifier

```

`success` Boolean Indicates whether the transaction was successful. 58.0

#### ConnectApi.CartItem

An item in a cart.

Subclass of ConnectApi.AbstractCartItem.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Currency ISO code of the cart. 57.0

`cartData` `ConnectApi.` Collection of items in the cart. 64.0

```
             CartItemCollection

```

`firstPymt` String

```
TotalAmount

```

`firstPymt` String

```
TotalListPrice

```

For subscription items, the first payment amount 60.0
after adjustments and taxes. For non-subscription
products, the value is the same as `totalAmount` .

For subscription items, the total list price of the first 63.0
payment. For non-subscription items, the value is the
same as `totalListPrice` .

`firstPymtTotalPrice` String For subscription items, the first term price, including 60.0
adjustments but excluding taxes. For

non-subscription items, the total price, including
adjustments but excluding taxes.

`firstPymtTotalTax` String

For subscription items, the tax amount on the first 60.0
payment. For non-subscription products, the value
is the same as `totalTax` .

`itemizedAdjustment` String Total itemized adjustment amount for the item, 52.0
`Amount` including promotions and excluding taxes.

`listPrice` String List price for the item. 49.0

`productClass` `ConnectApi.` Class of product. Values are: 62.0

```
          ProductClass
```

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

`salesPrice` String Sales price for the item. 49.0

`totalAdjustment` String Total adjustment amount for the item. 50.0

```
Amount

```

`totalAmount` String Total amount for the item. 49.0

`totalListPrice` String Total list price for the item. 49.0

`totalPrice` String Total price for the item including adjustments but 49.0
excluding taxes.

`totalTax` String Total tax for the item. 49.0

`unitAdjusted` String

```
Price

```

Unit price, including tier level discounts, for the item. 50.0
This value is informational only and isn’t used in
pricing calculations.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`unitAdjusted` String

```
PriceWithItemAdj

```

`unitAdjustment` String

```
Amount

```

`unitItem` String

```
AdjustmentAmount

#### ConnectApi.CartItemBasic

```

Represents limited details about a cart item.

Unit price, including both tier and item level 61.0
discounts, for the item. This value is informational
only and isn’t used in pricing calculations.

Tier level adjustments made to the unit price for the 50.0
item. This value is informational only and isn’t used
in pricing calculations.

Item level adjustments made to the unit price for the 61.0
item. This value is informational only and isn’t used
in pricing calculations.

**Property Name** **Type** **Description** **Available Version**

`cartItemId` String ID of the cart item. 60.0

`name` String Name of the cart item. 60.0

`productId` String ID of the product associated with the cart item. 60.0

`quantity` String Quantity of the cart item. 60.0

#### type ConnectApi. Type of item in a cart. Value is Product. 60.0

```
           CartItemType

#### ConnectApi.CartItemBasicResult

```

Represents the result of a cart request.

**Property Name** **Type** **Description** **Available Version**

#### cartItem ConnectApi.CartItemBasic Item in a cart. 60.0

```
           on page 2257

```

`message` String Error message when the request is not successful. 60.0

`status` String Status of the request. 60.0

#### ConnectApi.CartItemCollection

A collection of items in a cart.

**Property Name** **Type** **Description** **Available Version**

`approaching` List<String> List of approaching discounts for the cart items. 64.0

```
Discounts

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### cartCoupons ConnectApi. Collection of coupons in the cart. 59.0

```
             CartCouponCollection

#### cartItems List< ConnectApi. Collection of cart item results. 49.0
```

`CartItemResult`            
#### cartPromotions ConnectApi. Collection of promotions in the cart. 59.0

```
             CartPromotionCollection

#### cartSummary ConnectApi. Summary of the cart. 49.0

             CartSummary

```

`currentPage` Integer Current page of cart items. The value matches the 60.0
requested page number, unless the requested page

number exceeds the total number of pages. In this
scenario, the current page is the highest available
page number.

`currentPageToken` String Token identifying the current page. 49.0

`currentPageUrl` String Connect REST API URL identifying the current page. 49.0

`hasErrors` Boolean Specifies whether at least one of the results contains 49.0
an error.

`nextPageToken` String Token identifying the next page, or `null` if there 49.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 49.0
`null` if there isn’t a next page.

`previousPageToken` String Token identifying the previous page, or `null` if 49.0
there isn’t a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 49.0
or `null` if there isn’t a previous page.

`totalItemCount` Integer Total number of unique products in the cart. 60.0

`totalNumberOfPages` Integer Total number of pages for the given page size. 60.0

#### ConnectApi.PromotionCartItemKey

Cart item key for a bonus product in a promotion.

**Property Name** **Type** **Description** **Available Version**

`cartItemId` String ID of the cart item. 58.0

`cartItem` String Quantity ID of the cart item. 58.0

```
   QuantityIdentifier

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CartItemProduct

Product summary for a cart item.

**Property Name** **Type** **Description** **Available Version**

`fields` Map<String, String> Map of product fields and values. 49.0

`name` String Name of the product. 49.0

#### productClass ConnectApi. Class of product. Values are: 63.0

```
             ProductClass
```

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

`productId` String ID of the product. 49.0

`productSubscriptionInformation` Reserved for future use. 59.0

```
purchaseQuantityRule

```

#### ConnectApi. If one exists, purchase quantity rule for the product. 52.0

```
PurchaseQuantity

Rule

```

`productUrlName` String SEO-friendly URL name for the product. 64.0

`sku` String SKU of the product. 49.0

#### thumbnailImage ConnectApi. Thumbnail image of the product. 49.0

```
           ProductMedia

```

`variationAttributes` Map<String, Variation attributes associated with the product. 50.0

#### `ConnectApi.`

```
           CartProduct
```

`Attribute`          

SEE ALSO:

ConnectApi.AbstractCartItem

ConnectApi.WishlistItem

#### ConnectApi.CartItemPromotionCollectionOutputRepresentation

Promotions for the items in a cart.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Currency code associated with the cart. 53.0

`items` Map<String, Collection of promotions. 52.0

#### `ConnectApi.`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
              CartPromotionList
```

`Representation`            
#### ConnectApi.CartItemResult

Result after requesting a cart item.

**Property Name** **Type** **Description** **Available Version**

#### cartItem ConnectApi. Cart item. 49.0

```
             AbstractCartItem

```

`message` String Message when the request isn’t successful. 49.0

`status` String Status for the request. 49.0

SEE ALSO:

ConnectApi.CartItemCollection

ConnectApi.WishlistToCartResult

#### ConnectApi.CartItemWithoutPrice

An item without price information in a cart.

Subclass of ConnectApi.AbstractCartItem.

No additional properties.

#### ConnectApi.CartMessage

Cart message.

**Property Name** **Type** **Description** **Available Version**

`message` String Cart message. 49.0

`messageId` String ID of the object supplying the message. 49.0

`relatedEntityId` String ID of the entity, for example, cart, cart item, or cart 49.0
tax, associated with the message.

#### severity ConnectApi. Severity of cart message. Values are: 49.0

```
             CartMessageSeverity
```

**•** `Error`

**•** `Info`

**•** `Warning`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`type` String

Type of message. Standard values include 49.0
`Inventory`, `Taxes`, `Pricing`, `Shipping`,
`Entitlement`, `SystemError`, and `Other` .

`visible` Boolean Specifies whether the message is visible ( `true` ) or 49.0
dismissed ( `false` ).

SEE ALSO:

#### ConnectApi.CartMessagesSummary ConnectApi.CartMessagesSummary

Cart messages summary.

**Property Name** **Type** **Description** **Available Version**

`errorCount` Integer In `ConnectApi.CartItemResult`, the count 49.0
of messages with the `Error` severity level.

`hasErrors` Boolean Specifies whether there are messages related to the 49.0
entity ( `true` ) or not ( `false` ).

#### limitedMessages List< ConnectApi. In ConnectApi.CartItemResult, a limited 49.0

