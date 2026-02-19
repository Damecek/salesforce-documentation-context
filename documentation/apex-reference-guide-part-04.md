Type: String

ID of the topic.

```
   maxResults
```

Type: Integer

The maximum number of articles returned for each topic ID. Values can be from 1 to 25. The default value is 5.

Return Value

Type: `ConnectApi.KnowledgeArticleVersionCollection`

##### **`getTrendingArticles(communityId, maxResults)`**

Get trending articles for an Experience Cloud site.

API Version

36.0

Available to Guest Users

36.0

Requires Chatter

No

Signature

```
   public static ConnectApi.KnowledgeArticleVersionCollection getTrendingArticles(String

   communityId, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   maxResults
```

Type: Integer

The maximum number of articles returned. Values can be from 0 to 25. Default is 5.


Apex Reference Guide Knowledge Class

Return Value

Type: `ConnectApi.KnowledgeArticleVersionCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingArticles(communityId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTrendingArticlesForTopic(communityId, topicId, maxResults)`**

Get the trending articles for a topic in an Experience Cloud site.

API Version

36.0

Available to Guest Users

36.0

Requires Chatter

No

Signature

```
   public static ConnectApi.KnowledgeArticleVersionCollection

   getTrendingArticlesForTopic(String communityId, String topicId, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID of the topic.

```
   maxResults
```

Type: Integer

The maximum number of articles returned. Values can be from 0 to 25. Default is 5.


Apex Reference Guide Knowledge Class

Return Value

Type: `ConnectApi.KnowledgeArticleVersionCollection`

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingArticlesForTopic(communityId, topicId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### Knowledge Test Methods These test methods are for Knowledge . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTrendingArticles(communityId, maxResults, result)`**

Register a `ConnectApi.KnowledgeVersionArticleCollection` object to be returned when the matching
`ConnectApi.getTrendingArticles` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

36.0

Signature

```
   public static Void setTestGetTrendingArticles(String communityId, Integer maxResults,

   ConnectApi.KnowledgeArticleVersionCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   maxResults
```

Type: Integer

The maximum number of articles returned. Values can be from 0 to 25. Default is 5.

```
   result
```

Type: `ConnectApi.KnowledgeArticleVersionCollection`

Object containing test data.


Apex Reference Guide Knowledge Class

Return Value

Type: Void

SEE ALSO:

getTrendingArticles(communityId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTrendingArticlesForTopic(communityId, topicId, maxResults, result)`**

Register a `ConnectApi.KnowledgeVersionArticleCollection` object to be returned when the matching
`ConnectApi.getTrendingArticlesForTopic` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

36.0

Signature

```
   public static Void setTestGetTrendingArticlesForTopic(String communityId, String topicId,

   Integer maxResults, ConnectApi.KnowledgeArticleVersionCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID of the topic.

```
   maxResults
```

Type: Integer

The maximum number of articles returned. Values can be from 0 to 25. Default is 5.

```
   result
```

Type: `ConnectApi.KnowledgeArticleVersionCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTrendingArticlesForTopic(communityId, topicId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


### Apex Reference Guide LightningScheduler Class LightningScheduler Class

Create and update service appointments.

Namespace

ConnectApi

#### LightningScheduler Methods

### These methods are for LightningScheduler . All methods are static.

IN THIS SECTION:

##### createServiceAppointment(createServiceAppointmentInput)

Create a service appointment.

updateServiceAppointment(updateServiceAppointmentInput)
Update a service appointment.

##### **`createServiceAppointment(createServiceAppointmentInput)`**

Create a service appointment.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ServiceAppointmentOutput

   createServiceAppointment(ConnectApi.CreateServiceAppointmentInput

   createServiceAppointmentInput)

```

Parameters

```
   createServiceAppointmentInput
```

Type: `ConnectApi.CreateServiceAppointmentInput`

Input parameters to create a service appointment.

Return Value

Type: `ConnectApi.ServiceAppointmentOutput`


Apex Reference Guide LightningScheduler Class

Usage

Considerations for using engagement channel types with the `service-appointments` resource:

**•** Enable **Schedule Appointments Using Engagement Channels** in Salesforce Scheduler Settings in your Salesforce org.

**•** When you create or modify appointments, shifts must be defined in the scheduling policy. For more information on setting up shifts
[in the scheduling policy, see Define Shift Rules in Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating hours rules in the scheduling policy.

**•** When you use engagement channel type and shifts to create a service appointment, Salesforce Scheduler considers the default
value for the Appointment Type (if not specified). However, Salesforce Scheduler only considers the engagement channel type and
Appointment Type is ignored.

Example

For an account (existing user):

```
   ConnectApi.ExtendedFieldInput extendedFieldEmail = new ConnectApi.ExtendedFieldInput();

   extendedFieldEmail.name = 'Email';

   extendedFieldEmail.value = 'rachael.adams@salesforce.com';

   ConnectApi.ExtendedFieldInput extendedFieldPhone = new ConnectApi.ExtendedFieldInput();

   extendedFieldPhone.name = 'Phone';

   extendedFieldPhone.value = '1234567890';

   List<ConnectApi.ExtendedFieldInput> extendedFieldList = new

   List<ConnectApi.ExtendedFieldInput>();

   extendedFieldList.add(extendedFieldEmail);

   extendedFieldList.add(extendedFieldPhone);

   ConnectApi.ServiceAppointmentInput serviceAppInput = new

   ConnectApi.ServiceAppointmentInput();

   serviceAppInput.extendedFields = extendedFieldList;

   serviceAppInput.engagementChannelTypeId = '0eFRM00000000Bv2AI';

   serviceAppInput.serviceTerritoryId = '0Hhxx0000004C92CAE';

   serviceAppInput.workTypeId = '08qxx0000004C92AAE';

   serviceAppInput.parentRecordId = '001xx000003GYR1AAO';

   serviceAppInput.schedStartTime = DateTime.valueOf('2021-05-28 12:15:00');

   serviceAppInput.schedEndTime = DateTime.valueOf('2021-05-28 12:45:00');

   serviceAppInput.appointmentMode = 'Group';

   serviceAppInput.attendeeLimit = 20;

   ConnectApi.AssignedResourcesInput asResourceInput = new ConnectApi.AssignedResourcesInput();

   asResourceInput.serviceResourceId = '0Hnxx0000004CAiCAM';

   asResourceInput.isRequiredResource = true;

   asResourceInput.isPrimaryResource = true;

   List<ConnectApi.AssignedResourcesInput> asResourceInputList = new

   List<ConnectApi.AssignedResourcesInput>();

   asResourceInputList.add(asResourceInput);

   ConnectApi.CreateServiceAppointmentInput createInput = new

   ConnectApi.CreateServiceAppointmentInput();

```


Apex Reference Guide LightningScheduler Class

```
   createInput.serviceAppointment = serviceAppInput;

   createInput.assignedResources = asResourceInputList;

   try{

     ConnectApi.ServiceAppointmentOutput appointmentResult =

   ConnectApi.LightningScheduler.createServiceAppointment(createInput);

     String serviceAppointmentId = appointmentResult.result.serviceAppointmentId;

     List<String> assignedResourceIds = appointmentResult.result.assignedResourceIds;

   }catch(ConnectApi.ConnectApiException ex){

     //Handle Exception

   }

```

For a lead (authenticated guest user):

```
   ConnectApi.LeadInput leadInput = new ConnectApi.LeadInput();

   leadInput.firstName = 'Rachel';

   leadInput.lastName = 'Adams';

   leadInput.phone = '012-345-6789';

   leadInput.email = 'rachel.adams@salesforce.com';

   leadInput.company = 'Salesforce';

   ConnectApi.ExtendedFieldInput extendedFieldEmail = new ConnectApi.ExtendedFieldInput();

   extendedFieldEmail.name = 'Email';

   extendedFieldEmail.value = 'rachael.adams@salesforce.com';

   ConnectApi.ExtendedFieldInput extendedFieldPhone = new ConnectApi.ExtendedFieldInput();

   extendedFieldPhone.name = 'Phone';

   extendedFieldPhone.value = '1234567890';

   List<ConnectApi.ExtendedFieldInput> extendedFieldList = new

   List<ConnectApi.ExtendedFieldInput>();

   extendedFieldList.add(extendedFieldEmail);

   extendedFieldList.add(extendedFieldPhone);

   ConnectApi.ServiceAppointmentInput serviceAppInput = new

   ConnectApi.ServiceAppointmentInput();

   serviceAppInput.extendedFields = extendedFieldList;

   serviceAppInput.engagementChannelTypeId = '0eFRM00000000Bv2AI';

   serviceAppInput.serviceTerritoryId = '0Hhxx0000004C92CAE';

   serviceAppInput.workTypeId = '08qxx0000004C92AAE';

   serviceAppInput.schedStartTime = DateTime.valueOf('2021-05-28 12:15:00');

   serviceAppInput.schedEndTime = DateTime.valueOf('2021-05-28 12:45:00');

   ConnectApi.AssignedResourcesInput asResourceInput = new ConnectApi.AssignedResourcesInput();

   asResourceInput.serviceResourceId = '0Hnxx0000004CAiCAM';

   asResourceInput.isRequiredResource = true;

   asResourceInput.isPrimaryResource = true;

   List<ConnectApi.AssignedResourcesInput> asResourceInputList = new

   List<ConnectApi.AssignedResourcesInput>();

   asResourceInputList.add(asResourceInput);

   ConnectApi.CreateServiceAppointmentInput createInput = new

   ConnectApi.CreateServiceAppointmentInput();

```


Apex Reference Guide LightningScheduler Class

```
   createInput.serviceAppointment = serviceAppInput;

   createInput.assignedResources = asResourceInputList;

   createInput.lead = leadInput;

   try{

     ConnectApi.ServiceAppointmentOutput appointmentResult =

   ConnectApi.LightningScheduler.createServiceAppointment(createInput);

     String serviceAppointmentId = appointmentResult.result.serviceAppointmentId;

     List<String> assignedResourceIds = appointmentResult.result.assignedResourceIds;

   }catch(ConnectApi.ConnectApiException ex){

     //Handle Exception

   }

```

SEE ALSO:

[Service Appointments](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_service_appointments.htm)

##### **`updateServiceAppointment(updateServiceAppointmentInput)`**

Update a service appointment.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ServiceAppointmentOutput

   updateServiceAppointment(ConnectApi.UpdateServiceAppointmentInput

   updateServiceAppointmentInput)

```

Parameters

```
   updateServiceAppointmentInput
```

Type: `ConnectApi.UpdateServiceAppointmentInput`

Input parameters to update a service appointment.

Return Value

Type: `ConnectApi.ServiceAppointmentOutput`

Usage

Considerations for using engagement channel types with the `service-appointments` resource:

**•** Enable **Schedule Appointments Using Engagement Channels** in Salesforce Scheduler Settings in your Salesforce org.


Apex Reference Guide LightningScheduler Class

**•** When you create or modify appointments, shifts must be defined in the scheduling policy. For more information on setting up shifts
[in the scheduling policy, see Define Shift Rules in Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating hours rules in the scheduling policy.

**•** When you use engagement channel type and shifts to modify an appointment, Salesforce Scheduler considers the default value for
the Appointment Type (if not specified). However, Salesforce Scheduler only considers the engagement channel type and Appointment
Type is ignored.

Example

```
   ConnectApi.ExtendedFieldInput extendedFieldEmail = new ConnectApi.ExtendedFieldInput();

   extendedFieldEmail.name = 'Email';

   extendedFieldEmail.value = 'rachel.adams@salesforce.com.example';

   ConnectApi.ExtendedFieldInput extendedFieldPhone = new ConnectApi.ExtendedFieldInput();

   extendedFieldPhone.name = 'Phone';

   extendedFieldPhone.value = '0123456789';

   ConnectApi.ExtendedFieldInput extendedFieldStatus = new ConnectApi.ExtendedFieldInput();

   extendedFieldStatus.name = 'Status';

   extendedFieldStatus.value = 'None';

   List<ConnectApi.ExtendedFieldInput> extendedFieldList = new

   List<ConnectApi.ExtendedFieldInput>();

   extendedFieldList.add(extendedFieldEmail);

   extendedFieldList.add(extendedFieldPhone);

   extendedFieldList.add(extendedFieldStatus);

   ConnectApi.ServiceAppointmentInput serviceAppInput = new

   ConnectApi.ServiceAppointmentInput();

   serviceAppInput.extendedFields = extendedFieldList;

   serviceAppInput.serviceTerritoryId = '0Hhxx0000004C92CAE';

   serviceAppInput.workTypeId = '08qxx0000004C92AAE';

   serviceAppInput.schedStartTime = DateTime.valueOf('2021-05-28 12:15:00');

   serviceAppInput.schedEndTime = DateTime.valueOf('2021-05-28 12:45:00');

   ConnectApi.AssignedResourcesInput asResourceInput = new ConnectApi.AssignedResourcesInput();

   asResourceInput.serviceResourceId = '0Hnxx0000004CAiCAM';

   asResourceInput.isRequiredResource = true;

   asResourceInput.isPrimaryResource = true;

   //Multi-resource

   ConnectApi.AssignedResourcesInput asResourceInputReq = new

   ConnectApi.AssignedResourcesInput();

   asResourceInputReq.serviceResourceId = '0Hnxx0000004CAgCAM';

   asResourceInputReq.isRequiredResource = true;

   asResourceInputReq.isPrimaryResource = false;

   List<ConnectApi.AssignedResourcesInput> asResourceInputList = new

   List<ConnectApi.AssignedResourcesInput>();

   asResourceInputList.add(asResourceInput);

   asResourceInputList.add(asResourceInputReq);

```


### Apex Reference Guide ManagedContent Class

```
   ConnectApi.UpdateServiceAppointmentInput updateInput = new

   ConnectApi.UpdateServiceAppointmentInput();

   updateInput.serviceAppointment = serviceAppInput;

   updateInput.assignedResources = asResourceInputList;

   updateInput.serviceAppointmentId = '08pxx0000004CYqAAM';

   try{

     ConnectApi.ServiceAppointmentOutput appointmentResult =

   ConnectApi.LightningScheduler.updateServiceAppointment(updateInput);

     String serviceAppointmentId = appointmentResult.result.serviceAppointmentId;

     List<String> assignedResourceIds = appointmentResult.result.assignedResourceIds;

   }catch(ConnectApi.ConnectApiException ex){

     //Handle Exception

   }

```

SEE ALSO:

[Service Appointments](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_service_appointments.htm)

### ManagedContent Class

Clone managed content. Create and get managed content. Create, delete, or update a digital asset management (DAM) provider instance.
Delete and replace variants. Get channels. Get a managed content space. Get DAM providers. Get targets that managed content space
folders can be shared with. Get and update targets that managed content space folders are shared with. Publish and unpublish content.

Namespace

ConnectApi

#### ManagedContent Methods

### These methods are for ManagedContent . All methods are static.

IN THIS SECTION:

cloneManagedContentDocument(contentKeyOrId, ManagedContentCloneInputParam)
Clone a piece of managed content.

createManagedContent(ManagedContentInputParam)
Create managed content.

createManagedContentProvider(providerInstanceInput)
Create a digital asset management (DAM) provider instance.

createManagedContentWithMedia(ManagedContentInputParam, contentData)
Create managed content with content data.

deleteManagedContentProviderInstance(providerInstanceId)
Delete a digital asset management (DAM) provider instance.

deleteManagedContentVariant(variantId)
Delete a managed content variant.


Apex Reference Guide ManagedContent Class

getAllContent(channelId, pageParam, pageSize, language, managedContentType, includeMetadata, startDate, endDate)
Get all managed content versions for a channel.

getAllContent(channelId, pageParam, pageSize, language, managedContentType, includeMetadata, startDate, endDate,
showAbsoluteUrl)
Get all managed content versions for a channel with absolute URLs.

getAllDeliveryChannels(pageParam, pageSize)
Get managed content delivery channels for the context user.

getAllManagedContent(communityId, pageParam, pageSize, language, managedContentType)
Get all managed content versions for an Experience Cloud site.

getAllManagedContent(communityId, pageParam, pageSize, language, managedContentType, showAbsoluteUrl)
Get all managed content versions for an Experience Cloud site with absolute URLs.

getContentByContentKeys(channelId, contentKeys, pageParam, pageSize, language, managedContentType, includeMetadata,
startDate, endDate, showAbsoluteUrl)
Get managed content versions for a channel using a list of content keys.

getContentByIds(channelId, managedContentIds, pageParam, pageSize, language, managedContentType, includeMetadata, startDate,
endDate)
Get managed content versions for a channel using a list of managed content IDs.

getContentByIds(channelId, managedContentIds, pageParam, pageSize, language, managedContentType, includeMetadata, startDate,
endDate, showAbsoluteUrl)
Get managed content versions for a channel with absolute URLs using a list of managed content IDs.

getManagedContentByContentKeys(communityId, contentKeys, pageParam, pageSize, language, managedContentType,
showAbsoluteUrl)
Get managed content versions for an Experience Cloud site using a list of content keys.

getManagedContentByIds(communityId, managedContentIds, pageParam, pageSize, language, managedContentType)
Get managed content versions for an Experience Cloud site using a list of managed content IDs.

getManagedContentByIds(communityId, managedContentIds, pageParam, pageSize, language, managedContentType,
showAbsoluteUrl)
Get managed content versions for an Experience Cloud site with absolute URLs using a list of managed content IDs.

getManagedContentByTopics(communityId, topics, pageParam, pageSize, language, managedContentType)
Get managed content versions using a list of content topic names.

getManagedContentByTopics(communityId, topics, pageParam, pageSize, language, managedContentType, showAbsoluteUrl)
Get managed content versions with absolute URLs using a list of content topic names.

getManagedContentByTopicsAndContentKeys(communityId, contentKeys, topics, pageParam, pageSize, language,
managedContentType, showAbsoluteUrl)
Get managed content versions using a list of content keys and content topic names.

getManagedContentByTopicsAndIds(communityId, managedContentIds, topics, pageParam, pageSize, language,
managedContentType)
Get managed content versions using a list of managed content IDs and content topic names.

getManagedContentByTopicsAndIds(communityId, managedContentIds, topics, pageParam, pageSize, language,
managedContentType, showAbsoluteUrl)
Get managed content versions with absolute URLs using a list of managed content IDs and content topic names.


Apex Reference Guide ManagedContent Class

getManagedContentProviders()
Get digital asset management (DAM) providers.

getManagedContentProvidersForSpace(contentSpaceId)
Get digital asset management (DAM) providers for a managed content space.

getMCSFolderShares(folderId)
Get targets that a managed content space folder is shared with.

getMCSFolderShareTargets(folderId)
Get targets that a managed content space folder can be shared with.

patchMCSFolderShares(folderId, mcsFolderShareCollectionUpdateInput)
Update the targets that a managed content space folder is shared with.

publish(publishInput)
Publish content.

replaceManagedContentVariant(variantId, ManagedContentVariantInputParam)
Replace a managed content variant.

replaceManagedContentVariantWithMedia(variantId, ManagedContentVariantInputParam, contentData)
Replace a managed content variant, including content data.

unpublish(unpublishInput)
Unpublish content.

updateManagedContentProviderInstance(providerInstanceId, providerInstanceInput)
Update a digital asset management (DAM) provider instance.

##### **`cloneManagedContentDocument(contentKeyOrId, ManagedContentCloneInputParam)`**

Clone a piece of managed content.

API Version

61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDocumentClone cloneManagedContentDocument(String

   contentKeyOrId, ConnectApi.ManagedContentDocumentCloneInput

   ManagedContentCloneInputParam)

```

Parameters

```
   contentKeyOrId
```

Type: String

Content key or ID of the managed content to clone.


Apex Reference Guide ManagedContent Class

```
   ManagedContentCloneInputParam
```

Type: `ConnectApi.ManagedContentDocumentCloneInput`

`ConnectApi.ManagedContentDocumentCloneInput` class specifying the details for the cloned content.

Return Value

Type: `ConnectApi.ManagedContentDocumentClone`

##### **`createManagedContent(ManagedContentInputParam)`**

Create managed content.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDocument

   createManagedContent(ConnectApi.ManagedContentDocumentInput ManagedContentInputParam)

```

Parameters

```
   ManagedContentInputParam
```

Type: `ConnectApi.ManagedContentDocumentInput`

A `ConnectApi.ManagedContentDocumentInput` input class with information to create managed content.

Return Value

Type: `ConnectApi.ManagedContentDocument`

##### **`createManagedContentProvider(providerInstanceInput)`**

Create a digital asset management (DAM) provider instance.

API Version

65.0

Requires Chatter

No


Apex Reference Guide ManagedContent Class

Signature

```
   public static ConnectApi.ManagedContentProviderInstance

   createManagedContentProvider(ConnectApi.ManagedContentProviderInstanceInput

   providerInstanceInput)

```

Parameters

```
   providerInstanceInput
```

Type: `ConnectApi.ManagedContentProviderInstanceInput`

`ConnectApi.ManagedContentProviderInstanceInput` class with the required information to create an instance.

Return Value

Type: `ConnectApi.ManagedContentProviderInstance`

##### **`createManagedContentWithMedia(ManagedContentInputParam, contentData)`**

Create managed content with content data.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDocument

   createManagedContentWithMedia(ConnectApi.ManagedContentDocumentInput

   ManagedContentInputParam, ConnectApi.BinaryInput contentData)

```

Parameters

```
   ManagedContentInputParam
```

Type: `ConnectApi.ManagedContentDocumentInput`

A `ConnectApi.ManagedContentDocumentInput` input class with information to create managed content.

```
   contentData
```

Type: `ConnectApi.BinaryInput`

A new binary file of the content data for the managed content.

Return Value

Type: `ConnectApi.ManagedContentDocument`

##### **`deleteManagedContentProviderInstance(providerInstanceId)`**

Delete a digital asset management (DAM) provider instance.


Apex Reference Guide ManagedContent Class

You can’t delete a DAM provider instance that’s in use. Delete managed content that’s associated with a DAM provider instance before
deleting the instance.

API Version

65.0

Requires Chatter

No

Signature

```
   public static Void deleteManagedContentProviderInstance(String providerInstanceId)

```

Parameters

```
   providerInstanceId
```

Type: String

ID of the provider instance to delete.

Return Value

Type: Void

##### **`deleteManagedContentVariant(variantId)`**

Delete a managed content variant.

API Version

60.0

Requires Chatter

No

Signature

```
   public static Void deleteManagedContentVariant(String variantId)

```

Parameters

```
   variantId
```

Type: String

ID of the variant to delete.

Return Value

Type: Void


Apex Reference Guide ManagedContent Class

##### **`getAllContent(channelId, pageParam, pageSize, language, managedContentType,`**

```
  includeMetadata, startDate, endDate)

```

Get all managed content versions for a channel.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getAllContent(String channelId,

   Integer pageParam, Integer pageSize, String language, String managedContentType, Boolean

   includeMetadata, String startDate, String endDate)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   includeMetadata
```

Type: Boolean

Specifies whether to include metadata in the response ( `true` ) or not ( `false` ). The default value is `false` .


Apex Reference Guide ManagedContent Class

```
   startDate
```

Type: String

Publish start date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   endDate
```

Type: String

Publish end date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getAllContent(channelId, pageParam, pageSize, language, managedContentType,`**

```
  includeMetadata, startDate, endDate, showAbsoluteUrl)

```

Get all managed content versions for a channel with absolute URLs.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getAllContent(String channelId,

   Integer pageParam, Integer pageSize, String language, String managedContentType, Boolean

   includeMetadata, String startDate, String endDate, Boolean showAbsoluteUrl)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.


Apex Reference Guide ManagedContent Class

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   includeMetadata
```

Type: Boolean

Specifies whether to include metadata in the response ( `true` ) or not ( `false` ). The default value is `false` .

```
   startDate
```

Type: String

Publish start date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   endDate
```

Type: String

Publish end date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getAllDeliveryChannels(pageParam, pageSize)`**

Get managed content delivery channels for the context user.

API Version

48.0–61.0

In version 62.0 and later, use `getChannels(pageParam, pageSize)` in the `ManagedContentDelivery` class to get
all delivery channels.

Available to Guest Users

48.0

Requires Chatter

No


Apex Reference Guide ManagedContent Class

Signature

```
   public static ConnectApi.ManagedContentChannelCollection getAllDeliveryChannels(Integer

   pageParam, Integer pageSize)

```

Parameters

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ManagedContentChannelCollection`

##### **`getAllManagedContent(communityId, pageParam, pageSize, language,`**

```
  managedContentType)

```

Get all managed content versions for an Experience Cloud site.

API Version

47.0

Available to Guest Users

47.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getAllManagedContent(String

   communityId, Integer pageParam, Integer pageSize, String language, String

   managedContentType)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.


Apex Reference Guide ManagedContent Class

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getAllManagedContent(communityId, pageParam, pageSize, language,`**

```
  managedContentType, showAbsoluteUrl)

```

Get all managed content versions for an Experience Cloud site with absolute URLs.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getAllManagedContent(String

   communityId, Integer pageParam, Integer pageSize, String language, String

   managedContentType, Boolean showAbsoluteUrl)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   pageParam
```

Type: Integer


Apex Reference Guide ManagedContent Class

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getContentByContentKeys(channelId, contentKeys, pageParam, pageSize, language,`**

```
  managedContentType, includeMetadata, startDate, endDate, showAbsoluteUrl)

```

Get managed content versions for a channel using a list of content keys.

API Version

51.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getContentByContentKeys(String

   channelId, List<String> contentKeys, Integer pageParam, Integer pageSize, String

   language, String managedContentType, Boolean includeMetadata, String startDate, String

   endDate, Boolean showAbsoluteUrl)

```


Apex Reference Guide ManagedContent Class

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   contentKeys
```

Type: List<String>

List of up to 50 content keys for the managed content. A content key is a universally unique identifier (UUID) such as
MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   includeMetadata
```

Type: Boolean

Specifies whether to include metadata in the response ( `true` ) or not ( `false` ). The default value is `false` .

```
   startDate
```

Type: String

Publish start date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   endDate
```

Type: String

Publish end date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`


Apex Reference Guide ManagedContent Class

##### **`getContentByIds(channelId, managedContentIds, pageParam, pageSize, language,`**

```
  managedContentType, includeMetadata, startDate, endDate)

```

Get managed content versions for a channel using a list of managed content IDs.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getContentByIds(String

   channelId, List<String> managedContentIds, Integer pageParam, Integer pageSize, String

   language, String managedContentType, Boolean includeMetadata, String startDate, String

   endDate)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String


Apex Reference Guide ManagedContent Class

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   includeMetadata
```

Type: Boolean

Specifies whether to include metadata in the response ( `true` ) or not ( `false` ). The default value is `false` .

```
   startDate
```

Type: String

Publish start date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   endDate
```

Type: String

Publish end date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getContentByIds(channelId, managedContentIds, pageParam, pageSize, language,`**

```
  managedContentType, includeMetadata, startDate, endDate, showAbsoluteUrl)

```

Get managed content versions for a channel with absolute URLs using a list of managed content IDs.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getContentByIds(String

   channelId, List<String> managedContentIds, Integer pageParam, Integer pageSize, String

   language, String managedContentType, Boolean includeMetadata, String startDate, String

   endDate, Boolean showAbsoluteUrl)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.


Apex Reference Guide ManagedContent Class

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   includeMetadata
```

Type: Boolean

Specifies whether to include metadata in the response ( `true` ) or not ( `false` ). The default value is `false` .

```
   startDate
```

Type: String

Publish start date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   endDate
```

Type: String

Publish end date in ISO 8601 format, for example, 2011-02-25T18:24:31.000Z.

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByContentKeys(communityId, contentKeys, pageParam, pageSize,`**

```
  language, managedContentType, showAbsoluteUrl)

```

Get managed content versions for an Experience Cloud site using a list of content keys.

API Version

51.0

Available to Guest Users

51.0


Apex Reference Guide ManagedContent Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection

   getManagedContentByContentKeys(String communityId, List<String> contentKeys, Integer

   pageParam, Integer pageSize, String language, String managedContentType, Boolean

   showAbsoluteUrl)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   contentKeys
```

Type: List<String>

List of up to 50 content keys for the managed content. A content key is a universally unique identifier (UUID) such as
MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`


Apex Reference Guide ManagedContent Class

##### **`getManagedContentByIds(communityId, managedContentIds, pageParam, pageSize,`**

```
  language, managedContentType)

```

Get managed content versions for an Experience Cloud site using a list of managed content IDs.

API Version

47.0

Available to Guest Users

47.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getManagedContentByIds(String

   communityId, List<String> managedContentIds, Integer pageParam, Integer pageSize, String

   language, String managedContentType)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .


Apex Reference Guide ManagedContent Class

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByIds(communityId, managedContentIds, pageParam, pageSize,`**

```
  language, managedContentType, showAbsoluteUrl)

```

Get managed content versions for an Experience Cloud site with absolute URLs using a list of managed content IDs.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getManagedContentByIds(String

   communityId, List<String> managedContentIds, Integer pageParam, Integer pageSize, String

   language, String managedContentType, Boolean showAbsoluteUrl)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.


Apex Reference Guide ManagedContent Class

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByTopics(communityId, topics, pageParam, pageSize, language,`**

```
  managedContentType)

```

Get managed content versions using a list of content topic names.

API Version

47.0

Available to Guest Users

47.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getManagedContentByTopics(String

   communityId, List<String> topics, Integer pageParam, Integer pageSize, String language,

   String managedContentType)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   topics
```

Type: List<String>

Comma-separated list of up to 15 content topic names.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ManagedContent Class

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByTopics(communityId, topics, pageParam, pageSize, language,`**

```
  managedContentType, showAbsoluteUrl)

```

Get managed content versions with absolute URLs using a list of content topic names.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection getManagedContentByTopics(String

   communityId, List<String> topics, Integer pageParam, Integer pageSize, String language,

   String managedContentType, Boolean showAbsoluteUrl)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   topics
```

Type: List<String>

Comma-separated list of up to 15 content topic names.


Apex Reference Guide ManagedContent Class

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByTopicsAndContentKeys(communityId, contentKeys, topics,`**

```
  pageParam, pageSize, language, managedContentType, showAbsoluteUrl)

```

Get managed content versions using a list of content keys and content topic names.

API Version

51.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection

   getManagedContentByTopicsAndContentKeys(String communityId, List<String> contentKeys,

   List<String> topics, Integer pageParam, Integer pageSize, String language, String

   managedContentType, Boolean showAbsoluteUrl)

```


Apex Reference Guide ManagedContent Class

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   contentKeys
```

Type: List<String>

List of up to 50 content keys for the managed content. A content key is a universally unique identifier (UUID) such as
MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   topics
```

Type: List<String>

Comma-separated list of up to 15 content topic names.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentByTopicsAndIds(communityId, managedContentIds, topics,`**

```
  pageParam, pageSize, language, managedContentType)

```

Get managed content versions using a list of managed content IDs and content topic names.

API Version

47.0


Apex Reference Guide ManagedContent Class

Available to Guest Users

47.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection

   getManagedContentByTopicsAndIds(String communityId, List<String> managedContentIds,

   List<String> topics, Integer pageParam, Integer pageSize, String language, String

   managedContentType)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.

```
   topics
```

Type: List<String>

Comma-separated list of up to 15 content topic names.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`


Apex Reference Guide ManagedContent Class

##### **`getManagedContentByTopicsAndIds(communityId, managedContentIds, topics,`**

```
  pageParam, pageSize, language, managedContentType, showAbsoluteUrl)

```

Get managed content versions with absolute URLs using a list of managed content IDs and content topic names.

API Version

50.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVersionCollection

   getManagedContentByTopicsAndIds(String communityId, List<String> managedContentIds,

   List<String> topics, Integer pageParam, Integer pageSize, String language, String

   managedContentType, Boolean showAbsoluteUrl)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of managed content IDs. HTTP/2 clients support up to 200 IDs. HTTP/1.1 clients don’t.

```
   topics
```

Type: List<String>

Comma-separated list of up to 15 content topic names.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. For performance reasons, we recommend 25 or fewer
items per page. If you pass in `null`, the default size is 25.

```
   language
```

Type: String


Apex Reference Guide ManagedContent Class

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the context user’s language. If the context user’s language isn’t available, the language defaults to the content type’s original
language.

```
   managedContentType
```

Type: String

Developer name of the content type, such as `cms_document` or `cms_image` .

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentVersionCollection`

##### **`getManagedContentProviders()`**

Get digital asset management (DAM) providers.

API Version

65.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentProviderCollection getManagedContentProviders()

```

Return Value

Type: `ConnectApi.ManagedContentProviderCollection`

##### **`getManagedContentProvidersForSpace(contentSpaceId)`**

Get digital asset management (DAM) providers for a managed content space.

API Version

66.0

Requires Chatter

No


Apex Reference Guide ManagedContent Class

Signature

```
   public static ConnectApi.ManagedContentProviderCollection

   getManagedContentProvidersForSpace(String contentSpaceId)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

Return Value

Type: `ConnectApi.ManagedContentProviderCollection`

##### **`getMCSFolderShares(folderId)`**

Get targets that a managed content space folder is shared with.

##### To get the targets that a managed content space folder can be shared with, use getMCSFolderShareTargets(folderId) .

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.MCSFolderShareCollection getMCSFolderShares(String folderId)

```

Parameters

```
   folderId
```

Type: String

ID of the folder.

Return Value

Type: `ConnectApi.MCSFolderShareCollection`

##### **`getMCSFolderShareTargets(folderId)`**

Get targets that a managed content space folder can be shared with.

##### To get the targets that a managed content space folder is shared with, use getMCSFolderShares(folderId) .

API Version

63.0


Apex Reference Guide ManagedContent Class

Requires Chatter

No

Signature

```
   public static ConnectApi.MCSFolderShareTargetCollection getMCSFolderShareTargets(String

   folderId)

```

Parameters

```
   folderId
```

Type: String

ID of the folder.

Return Value

Type: `ConnectApi.MCSFolderShareTargetCollection`

##### **`patchMCSFolderShares(folderId, mcsFolderShareCollectionUpdateInput)`**

Update the targets that a managed content space folder is shared with.

Workspaces are the only supported sharing targets. To get the targets that a managed content space folder is shared with, use
`getMCSFolderShares(folderId)` . To get the targets that a managed content space folder can be shared with, use
`getMCSFolderShareTargets(folderId)` .

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.MCSFolderShareCollection patchMCSFolderShares(String folderId,

   ConnectApi.MCSFolderShareCollectionUpdateInput mcsFolderShareCollectionUpdateInput)

```

Parameters

```
   folderId
```

Type: String

ID of the folder.

```
   mcsFolderShareCollectionUpdateInput
```

Type: `ConnectApi.MCSFolderShareCollectionUpdateInput`

`ConnectApi.MCSFolderShareCollectionUpdateInput` input class with the targets to share and unshare.


Apex Reference Guide ManagedContent Class

Return Value

Type: `ConnectApi.MCSFolderShareCollection`

##### **`publish(publishInput)`**

Publish content.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentPublishOutput

   publish(ConnectApi.ManagedContentPublishInput publishInput)

```

Parameters

```
   publishInput
```

Type: `ConnectApi.ManagedContentPublishInput`

A `ConnectApi.ManagedContentPublishInput` request body specifying the content to publish.

Return Value

Type: `ConnectApi.ManagedContentPublishOutput`

##### **`replaceManagedContentVariant(variantId, ManagedContentVariantInputParam)`**

Replace a managed content variant.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVariant replaceManagedContentVariant(String

   variantId, ConnectApi.ManagedContentVariantUpdateInput ManagedContentVariantInputParam)

```


Apex Reference Guide ManagedContent Class

Parameters

```
   variantId
```

Type: String

ID of the managed content variant to replace.

```
   ManagedContentVariantInputParam
```

Type: `ConnectApi.ManagedContentVariantUpdateInput`

A `ConnectApi.ManagedContentVariantUpdateInput` input class with information about the managed content
variant that is replacing the existing variant.

Return Value

Type: `ConnectApi.ManagedContentVariant`

##### **`replaceManagedContentVariantWithMedia(variantId,`**

```
  ManagedContentVariantInputParam, contentData)

```

Replace a managed content variant, including content data.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentVariant

   replaceManagedContentVariantWithMedia(String variantId,

   ConnectApi.ManagedContentVariantUpdateInput ManagedContentVariantInputParam,

   ConnectApi.BinaryInput contentData)

```

Parameters

```
   variantId
```

Type: String

ID of the managed content variant to replace.

```
   ManagedContentVariantInputParam
```

Type: `ConnectApi.ManagedContentVariantUpdateInput`

A `ConnectApi.ManagedContentVariantUpdateInput` input class with information about the managed content
variant that is replacing the existing variant.

```
   contentData
```

Type: `ConnectApi.BinaryInput`

A new binary file to replace the content data of the managed content variant.


Apex Reference Guide ManagedContent Class

Return Value

Type: `ConnectApi.ManagedContentVariant`

##### **`unpublish(unpublishInput)`**

Unpublish content.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentUnpublishOutput

   unpublish(ConnectApi.ManagedContentUnpublishInput unpublishInput)

```

Parameters

```
   unpublishInput
```

Type: `ConnectApi.ManagedContentUnpublishInput`

A `ConnectApi,ManagedContentUnpublishInput` request body specifying the content to unpublish.

Return Value

Type: `ConnectApi.ManagedContentUnpublishOutput`

##### **`updateManagedContentProviderInstance(providerInstanceId,`**

```
  providerInstanceInput)

```

Update a digital asset management (DAM) provider instance.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentProviderInstance

   updateManagedContentProviderInstance(String providerInstanceId,

   ConnectApi.ManagedContentProviderInput providerInstanceInput)

```


Apex Reference Guide ManagedContent Class

Parameters

```
   providerInstanceId
```

Type: String

ID of the provider instance to update.

```
   providerInstanceInput
```

Type: `ConnectApi.ManagedContentProviderInstanceInput`

`ConnectApi.ManagedContentProviderInstanceInput` class with the required information to update an instance.

Return Value

Type: `ConnectApi.ManagedContentProviderInstance`

#### Retired ManagedContent Methods

These methods for `ManagedContent` are retired.

IN THIS SECTION:

##### getAllDeliveryChannels(pageParam, pageSize)

Get managed content delivery channels for the context user.

getManagedContentSpace(contentSpaceId)
Get a managed content space.

##### **`getAllDeliveryChannels(pageParam, pageSize)`**

Get managed content delivery channels for the context user.

API Version

48.0–61.0

In version 62.0 and later, use `getChannels(pageParam, pageSize)` in the `ManagedContentDelivery` class to get
all delivery channels.

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentChannelCollection getAllDeliveryChannels(Integer

   pageParam, Integer pageSize)

```


### Apex Reference Guide ManagedContentChannels Class

Parameters

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ManagedContentChannelCollection`

##### **`getManagedContentSpace(contentSpaceId)`**

Get a managed content space.

API Version

55.0–63.0

In version 64.0 and later, use getManagedContentSpace(contentSpaceId) in the `ManagedContentSpaces` class to get a managed
content space.

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentSpace getManagedContentSpace(String

   contentSpaceId)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

Return Value

Type: `ConnectApi.ManagedContentSpace`

### ManagedContentChannels Class

Get managed content channels. Create, get, update, or delete a managed content channel.

Namespace

ConnectApi


Apex Reference Guide ManagedContentChannels Class

#### ManagedContentChannels Methods These methods are for ManagedContentChannels . All methods are static.

IN THIS SECTION:

##### deleteManagedContentChannel(channelId)

Delete a managed content channel.

##### getManagedContentChannel(channelId)

Get a managed content channel.

getManagedContentChannels(pageParam, pageSize, showDetails)
Get managed content channels.

patchManagedContentChannel(channelId, ManagedContentChannelInput)
Update a managed content channel.

postManagedContentChannel(ManagedContentCreateInputParam)
Create a managed content channel.

##### **`deleteManagedContentChannel(channelId)`**

Delete a managed content channel.

API Version

62.0

Requires Chatter

No

Signature

```
   public static Void deleteManagedContentChannel(String channelId)

```

Parameters

```
   channelId
```

Type: String

ID of the managed content channel to delete.

Return Value

Type: Void

##### **`getManagedContentChannel(channelId)`**

Get a managed content channel.


Apex Reference Guide ManagedContentChannels Class

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentChannel getManagedContentChannel(String channelId)

```

Parameters

```
   channelId
```

Type: String

ID of the managed content channel.

Return Value

Type: `ConnectApi.ManagedContentChannel`

##### **`getManagedContentChannels(pageParam, pageSize, showDetails)`**

Get managed content channels.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentChannelsRepresentation

   getManagedContentChannels(Integer pageParam, Integer pageSize, Boolean showDetails)

```

Parameters

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25.

```
   showDetails
```

Type: Boolean


Apex Reference Guide ManagedContentChannels Class

Specifies whether to show the channels’ detailed information ( `true` ) or summary information only ( `false` ). If you pass in `null`,
the default is `false` .

Return Value

Type: `ConnectApi.ManagedContentChannelsRepresentation`

##### **`patchManagedContentChannel(channelId, ManagedContentChannelInput)`**

Update a managed content channel.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentChannel patchManagedContentChannel(String

   channelId, ConnectApi.ManagedContentChannelUpdateRepresentation

   ManagedContentChannelInput)

```

Parameters

```
   channelId
```

Type: String

ID of the managed content channel to update.

```
   ManagedContentChannelInput
```

Type: `ConnectApi.ManagedContentChannelUpdateRepresentation`

`ConnectApi.ManagedContentChannelUpdateRepresentation` input class with the updates.

Return Value

Type: `ConnectApi.ManagedContentChannel`

##### **`postManagedContentChannel(ManagedContentCreateInputParam)`**

Create a managed content channel.

API Version

62.0

Requires Chatter

No


### Apex Reference Guide ManagedContentDelivery Class

Signature

```
   public static ConnectApi.ManagedContentChannel

   postManagedContentChannel(ConnectApi.ManagedContentChannelCreateRepresentation

   ManagedContentCreateInputParam)

```

Parameters

```
   ManagedContentCreateInputParam
```

Type: `ConnectApi.ManagedContentChannelCreateRepresentation`

`ConnectApi.ManagedContentChannelCreateRepresentation` input class describing the managed content
channel.

Return Value

Type: `ConnectApi.ManagedContentChannel`

### ManagedContentDelivery Class

Get collection items. Get a managed content channel. Get managed content.

Namespace

ConnectApi

#### ManagedContentDelivery Methods

### These methods are for ManagedContentDelivery . All methods are static.

IN THIS SECTION:

getChannels(pageParam, pageSize)
Get managed content delivery channels for the context user.

getCollectionItemsForChannel(channelId, collectionKeyOrId, language)
Get collection items for a channel.

getCollectionItemsForChannel(channelId, collectionKeyOrId, language, pageToken, pageSize)
Get a page of collection items for a channel.

getCollectionItemsForSite(siteId, collectionKeyOrId, language)
Get collection items for an Experience Cloud site.

getCollectionItemsForSite(siteId, collectionKeyOrId, language, pageToken, pageSize)
Get a page of collection items for an Experience Cloud site.

getManagedContentDeliveryChannel(channelId)
Get a managed content delivery channel.

getManagedContentForChannel(channelId, contentKeyOrId, showAbsoluteUrl)
Get a piece of published content for a channel.


Apex Reference Guide ManagedContentDelivery Class

getManagedContentForChannel(channelId, contentKeyOrId, language, showAbsoluteUrl)
Get a piece of published content in a specified language for a channel.

getManagedContentForChannel(channelId, contentKeyOrId, language, showAbsoluteUrl, referenceDepth, expandReferences,
referencesAsList)
Get a piece of published content in a specified language with references for a channel.

getManagedContentForSite(siteId, contentKeyOrId, showAbsoluteUrl)
Get a piece of published content for an Experience Cloud site.

getManagedContentForSite(siteId, contentKeyOrId, language, showAbsoluteUrl)
Get a piece of published content in a specified language for an Experience Cloud site.

getManagedContentForSite(siteId, contentKeyOrId, language, showAbsoluteUrl, referenceDepth, expandReferences, referencesAsList)
Get a piece of published content in a specified language with references for an Experience Cloud site.

getManagedContentsForChannel(channelId, managedContentIds, contentKeys, contentTypeFQN, language, publishStartDate,
publishEndDate, includeContentBody, referenceDepth, expandReferences, referencesAsList, pageParam, pageSize, showAbsoluteUrl)
Get a collection of published contents for a channel.

getManagedContentsForSite(siteId, managedContentIds, contentKeys, contentTypeFQN, language, publishStartDate, publishEndDate,
includeContentBody, referenceDepth, expandReferences, referencesAsList, pageParam, pageSize, showAbsoluteUrl)
Get a collection of published contents for an Experience Cloud site.

##### **`getChannels(pageParam, pageSize)`**

Get managed content delivery channels for the context user.

API Version

62.0

Available to Guest Users

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryChannelsRepresentation getChannels(Integer

   pageParam, Integer pageSize)

```

Parameters

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ManagedContentDelivery Class

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ManagedContentDeliveryChannelsRepresentation`

##### **`getCollectionItemsForChannel(channelId, collectionKeyOrId, language)`**

Get collection items for a channel.

API Version

56.0

Available to Guest Users

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentCollectionItems

   getCollectionItemsForChannel(String channelId, String collectionKeyOrId, String language)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   collectionKeyOrId
```

Type: String

Collection key or ID of the collection. A collection key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

Return Value

Type: `ConnectApi.ManagedContentCollectionItems`


Apex Reference Guide ManagedContentDelivery Class

Example

This example gets a collection of a custom content type that includes references to images and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentCollectionItems collection =

   ConnectApi.ManagedContentDelivery.getCollectionItemsForChannel('0apXXXXXXXXXXXXXXX','MCVXXXXXXXXXXXXXXXXXXXXXXXXX','en_US');

   System.debug(collection.items); //before ApexWrapper is unwrapped

   for(ConnectApi.ManagedContentCollectionItem item : collection.items)

   {

    //unwrap ApexWrapper

    Map<String,Object> unwrappedItem =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(item.body.get('contentBody'));

    //replace the wrapped object with the unwrapped object

    item.body.put('contentBody', unwrappedItem);

   }

   System.debug(collection.items); //after ApexWrapper is unwrapped

##### **`getCollectionItemsForChannel(channelId, collectionKeyOrId, language,`**

  pageToken, pageSize)

```

Get a page of collection items for a channel.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentCollectionItems

   getCollectionItemsForChannel(String channelId, String collectionKeyOrId, String language,

   Integer pageToken, Integer pageSize)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.


Apex Reference Guide ManagedContentDelivery Class

```
   collectionKeyOrId
```

Type: String

Collection key or ID of the collection. A collection key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   pageToken
```

Type: Integer

Integer specifying a page token of items. If you pass in null, the default value is 0, which returns the first page token.

```
   pageSize
```

Type: Integer

Number of items per page. Valid values are from 1 through 250. If you pass in null, the default size is 50.

Return Value

Type: `ConnectApi.ManagedContentCollectionItems`

##### **`getCollectionItemsForSite(siteId, collectionKeyOrId, language)`**

Get collection items for an Experience Cloud site.

API Version

56.0

Available to Guest Users

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentCollectionItems getCollectionItemsForSite(String

   siteId, String collectionKeyOrId, String language)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   collectionKeyOrId
```

Type: String


Apex Reference Guide ManagedContentDelivery Class

Collection key or ID of the collection. A collection key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

Return Value

Type: `ConnectApi.ManagedContentCollectionItems`

Example

This example gets a collection of a custom content type that includes references to images and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentCollectionItems collection =

   ConnectApi.ManagedContentDelivery.getCollectionItemsForSite('0DMXXXXXXXXXXXXXXX','MCVXXXXXXXXXXXXXXXXXXXXXXXXX','en_US');

   System.debug(collection.items); //before ApexWrapper is unwrapped

   for(ConnectApi.ManagedContentCollectionItem item : collection.items)

   {

    //unwrap ApexWrapper

    Map<String,Object> unwrappedItem =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(item.body.get('contentBody'));

    //replace the wrapped object with the unwrapped object

    item.body.put('contentBody', unwrappedItem);

   }

   System.debug(collection.items); //after ApexWrapper is unwrapped

##### **`getCollectionItemsForSite(siteId, collectionKeyOrId, language, pageToken,`**

  pageSize)

```

Get a page of collection items for an Experience Cloud site.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No


Apex Reference Guide ManagedContentDelivery Class

Signature

```
   public static ConnectApi.ManagedContentCollectionItems getCollectionItemsForSite(String

   siteId, String collectionKeyOrId, String language, Integer pageToken, Integer pageSize)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   collectionKeyOrId
```

Type: String

Collection key or ID of the collection. A collection key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   pageToken
```

Type: Integer

Integer specifying a page token of items. If you pass in null, the default value is 0, which returns the first page token.

```
   pageSize
```

Type: Integer

Number of items per page. Valid values are from 1 through 250. If you pass in null, the default size is 50.

Return Value

Type: `ConnectApi.ManagedContentCollectionItems`

##### **`getManagedContentDeliveryChannel(channelId)`**

Get a managed content delivery channel.

API Version

62.0

Available to Guest Users

62.0

Requires Chatter

No


Apex Reference Guide ManagedContentDelivery Class

Signature

```
   public static ConnectApi.ManagedContentDeliveryChannelRepresentation

   getManagedContentDeliveryChannel(String channelId)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

Return Value

Type: `ConnectApi.ManagedContentDeliveryChannelRepresentation`

##### **`getManagedContentForChannel(channelId, contentKeyOrId, showAbsoluteUrl)`**

Get a piece of published content for a channel.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument

   getManagedContentForChannel(String channelId, String contentKeyOrId, Boolean

   showAbsoluteUrl)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .


Apex Reference Guide ManagedContentDelivery Class

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`

Usage

This method returns content only if it's published in the default language of the channel. If you request content that isn’t published in
the default language of the channel, you get a `ConnectApi.NotFoundException` . To get content for a channel in another
##### language use getManagedContentForChannel(channelId, contentKeyOrId, language, showAbsoluteUrl) or getManagedContentForChannel(channelId, contentKeyOrId, language,

`showAbsoluteUrl, referenceDepth, expandReferences, referencesAsList)` on page 1659.

Example

This example gets a custom content type with an image reference and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentDeliveryDocument res =

      ConnectApi.ManagedContentDelivery.getManagedContentForChannel

   ('0apXXXXXXXXXXXXXXX','MCLXXXXXXXXXXXXXXXXXXXXXXXXX',true);

   //before contentBody field ApexWrapper is unwrapped

   system.debug(res.contentBody);

   //unwrap contentBody field in res

   Map<String,Object> contentBody =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(res.contentBody);

   //after contentBody field ApexWrapper is unwrapped, but image field still wrapped

   system.debug(contentBody);

   //before image field ApexWrapper is unwrapped

   system.debug(contentBody.get('Image'));

   //unwrap Image field in contentBody

   Map<String,Object> Image =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(contentBody.get('Image'));

   //after image field ApexWrapper is unwrapped

   system.debug(Image);

   //replace wrapped primary_image in contentBody with unwrapped version

   contentBody.put('Image', Image);

   //after contentBody field ApexWrapper is unwrapped, with image field also unwrapped

   system.debug(contentBody);

##### **`getManagedContentForChannel(channelId, contentKeyOrId, language,`**

  showAbsoluteUrl)

```

Get a piece of published content in a specified language for a channel.


Apex Reference Guide ManagedContentDelivery Class

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument

   getManagedContentForChannel(String channelId, String contentKeyOrId, String language,

   Boolean showAbsoluteUrl)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . The requested language must be added to the channel, otherwise,
you get a `ConnectApi.NotFoundException` . If the requested translation isn’t available, the language defaults to the
channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`

##### **`getManagedContentForChannel(channelId, contentKeyOrId, language,`**

```
  showAbsoluteUrl, referenceDepth, expandReferences, referencesAsList)

```

Get a piece of published content in a specified language with references for a channel.


Apex Reference Guide ManagedContentDelivery Class

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument

   getManagedContentForChannel(String channelId, String contentKeyOrId, String language,

   Boolean showAbsoluteUrl, Integer referenceDepth, Boolean expandReferences, Boolean

   referencesAsList)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . The requested language must be added to the channel, otherwise,
you get a `ConnectApi.NotFoundException` . If the requested translation isn’t available, the language defaults to the
channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocument` output class is null. If unspecified, the default value is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .


Apex Reference Guide ManagedContentDelivery Class

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocument` output class ( `true` ). If you specify `false`, the references are
returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`

##### **`getManagedContentForSite(siteId, contentKeyOrId, showAbsoluteUrl)`**

Get a piece of published content for an Experience Cloud site.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument getManagedContentForSite(String

   siteId, String contentKeyOrId, Boolean showAbsoluteUrl)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`


Apex Reference Guide ManagedContentDelivery Class

Example

This example gets a custom content type with an image reference and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentDeliveryDocument res =

      ConnectApi.ManagedContentDelivery.getManagedContentForSite

   ('0DMXXXXXXXXXXXXXXX','MCLXXXXXXXXXXXXXXXXXXXXXXXXX',true);

   //before contentBody field ApexWrapper is unwrapped

   system.debug(res.contentBody);

   //unwrap contentBody field in res

   Map<String,Object> contentBody =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(res.contentBody);

   //after contentBody field ApexWrapper is unwrapped, but image field still wrapped

   system.debug(contentBody);

   //before image field ApexWrapper is unwrapped

   system.debug(contentBody.get('Image'));

   //unwrap Image field in contentBody

   Map<String,Object> Image =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(contentBody.get('Image'));

   //after image field ApexWrapper is unwrapped

   system.debug(Image);

   //replace wrapped primary_image in contentBody with unwrapped version

   contentBody.put('Image', Image);

   //after contentBody field ApexWrapper is unwrapped, with image field also unwrapped

   system.debug(contentBody);

##### **`getManagedContentForSite(siteId, contentKeyOrId, language, showAbsoluteUrl)`**

```

Get a piece of published content in a specified language for an Experience Cloud site.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide ManagedContentDelivery Class

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument getManagedContentForSite(String

   siteId, String contentKeyOrId, String language, Boolean showAbsoluteUrl)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`

##### **`getManagedContentForSite(siteId, contentKeyOrId, language, showAbsoluteUrl,`**

```
  referenceDepth, expandReferences, referencesAsList)

```

Get a piece of published content in a specified language with references for an Experience Cloud site.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide ManagedContentDelivery Class

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocument getManagedContentForSite(String

   siteId, String contentKeyOrId, String language, Boolean showAbsoluteUrl, Integer

   referenceDepth, Boolean expandReferences, Boolean referencesAsList)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   contentKeyOrId
```

Type: String

Content key or ID of the content. A content key is a unique identifier such as MCA4CCV5QS2BAB5H7YRCRPTCWGZQ.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the channel or site’s default language. If the channel or site’s default language isn’t available, the language defaults to the primary
language of the content space.

```
   showAbsoluteUrl
```

Type: Boolean

For public channels only, specifies whether to return the absolute `unauthenticatedUrl` in the output class. The default value
is `false` .

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocument` output class is null. If unspecified, the default value is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocument` output class ( `true` ). If you specify `false`, the references are
returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocument`

##### **`getManagedContentsForChannel(channelId, managedContentIds, contentKeys,`**

```
  contentTypeFQN, language, publishStartDate, publishEndDate,

```


Apex Reference Guide ManagedContentDelivery Class

```
  includeContentBody, referenceDepth, expandReferences, referencesAsList,

  pageParam, pageSize, showAbsoluteUrl)

```

Get a collection of published contents for a channel.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocumentCollection

   getManagedContentsForChannel(String channelId, List<String> managedContentIds,

   List<String> contentKeys, String contentTypeFQN, String language, String

   publishStartDate, String publishEndDate, Boolean includeContentBody, Integer

   referenceDepth, Boolean expandReferences, Boolean referencesAsList, Integer pageParam,

   Integer pageSize, Boolean showAbsoluteUrl)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of up to 100 managed content IDs. Specify either managed content IDs or content keys.

```
   contentKeys
```

Type: List<String>

Comma-separated list of up to 50 content keys. Specify either managed content IDs or content keys.

```
   contentTypeFQN
```

Type: String

Fully qualified name of the managed content type.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the configured fallback language or the channel’s default language. If the content isn’t available in the fallback language and the
channel’s default language, we return an error.

```
   publishStartDate
```

Type: String


Apex Reference Guide ManagedContentDelivery Class

ISO 8601 formatted publish start date.

```
   publishEndDate
```

Type: String

ISO 8601 formatted publish end date.

```
   includeContentBody
```

Type: Boolean

Specifies whether to return the content body ( `true` ) or the content summary ( `false` ). If unspecified, the default value is `false` .

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class is null. If unspecified, the default value
is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class ( `true` ). If you specify `false`, the
references are returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25. If you specify

`true` for _`expandReferences`_ or _`includeContentBody`_, the maximum page size you can specify is 25.

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocumentCollection`

Example

This example gets Event custom content type records and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentDeliveryDocumentCollection resCol =

      ConnectApi.ManagedContentDelivery.getManagedContentsForChannel('0apXXXXXXXXXXXXXXX',

   null, new List<String>{'MCLXXXXXXXXXXXXXXXXXXXXXXXXX'}, 'Event', null, null, null, true,

```


Apex Reference Guide ManagedContentDelivery Class

```
   3, true, false, null, 25, true);

   Map<String, Object> contentBodyMap = new Map<String,Object>();

   for(ConnectApi.AbstractManagedContentDeliveryDocument res1 : resCol.contents)

   {

    //cast the abstract object as the ManagedContentDeliveryDocument subclass that contains

   contentBody

    ConnectApi.ManagedContentDeliveryDocument res =

   (ConnectApi.ManagedContentDeliveryDocument)res1;

    //before contentBody field ApexWrapper is unwrapped

    system.debug(res.contentBody);

    //unwrap contentBody field in res

    Map<String,Object> contentBody =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(res.contentBody);

    //after contentBody field ApexWrapper is unwrapped, but image field still wrapped

    system.debug(contentBody);

    //before image field ApexWrapper is unwrapped

    system.debug(contentBody.get('Image'));

    //unwrap Image field in contentBody

    Map<String,Object> Image =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(contentBody.get('Image'));

    //after image field ApexWrapper is unwrapped

    system.debug(Image);

    //replace wrapped primary_image in contentBody with unwrapped version

    contentBody.put('Image', Image);

    //after contentBody field ApexWrapper is unwrapped, with image field also unwrapped

    system.debug(contentBody);

    //put unwrapped contentBody in map

    contentBodyMap.put(res.contentKey, contentBody);

   }

   //check unwrapped contentBody map

   System.debug(contentBodyMap);

##### **`getManagedContentsForSite(siteId, managedContentIds, contentKeys,`**

  contentTypeFQN, language, publishStartDate, publishEndDate,

  includeContentBody, referenceDepth, expandReferences, referencesAsList,

  pageParam, pageSize, showAbsoluteUrl)

```

Get a collection of published contents for an Experience Cloud site.


Apex Reference Guide ManagedContentDelivery Class

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocumentCollection

   getManagedContentsForSite(String siteId, List<String> managedContentIds, List<String>

   contentKeys, String contentTypeFQN, String language, String publishStartDate, String

   publishEndDate, Boolean includeContentBody, Integer referenceDepth, Boolean

   expandReferences, Boolean referencesAsList, Integer pageParam, Integer pageSize, Boolean

   showAbsoluteUrl)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of up to 100 managed content IDs. Specify either managed content IDs or content keys.

```
   contentKeys
```

Type: List<String>

Comma-separated list of up to 50 content keys. Specify either managed content IDs or content keys.

```
   contentTypeFQN
```

Type: String

Fully qualified name of the managed content type.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the configured fallback language or the channel’s default language. If the content isn’t available in the fallback language and the
channel’s default language, we return an error.

```
   publishStartDate
```

Type: String

ISO 8601 formatted publish start date.

```
   publishEndDate
```

Type: String

ISO 8601 formatted publish end date.


Apex Reference Guide ManagedContentDelivery Class

```
   includeContentBody
```

Type: Boolean

Specifies whether to return the content body ( `true` ) or the content summary ( `false` ). If unspecified, the default value is `false` .

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class is null. If unspecified, the default value
is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class ( `true` ). If you specify `false`, the
references are returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25. If you specify

`true` for _`expandReferences`_ or _`includeContentBody`_, the maximum page size you can specify is 25.

```
   showAbsoluteUrl
```

Type: Boolean

Specifies whether to show absolute URLs in the output class ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocumentCollection`

Example

This example gets custom content type Event records and uses the
`ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

```
   ConnectApi.ManagedContentDeliveryDocumentCollection resCol =

     ConnectApi.ManagedContentDelivery.getManagedContentsForSite('0DMXXXXXXXXXXXXXXX', null,

    new List<String>{'MCLXXXXXXXXXXXXXXXXXXXXXXXXX'}, 'Event', null, null, null, true, 3,

   true, false, null, 25, true);

   Map<String, Object> contentBodyMap = new Map<String,Object>();

   for(ConnectApi.AbstractManagedContentDeliveryDocument res1 : resCol.contents)

   {

```


Apex Reference Guide ManagedContentDelivery Class

```
    //cast the abstract object as the ManagedContentDeliveryDocument subclass that contains

   contentBody

    ConnectApi.ManagedContentDeliveryDocument res =

   (ConnectApi.ManagedContentDeliveryDocument)res1;

    //before contentBody field ApexWrapper is unwrapped

    system.debug(res.contentBody);

    //unwrap contentBody field in res

    Map<String,Object> contentBody =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(res.contentBody);

    //after contentBody field ApexWrapper is unwrapped, but image field still wrapped

    system.debug(contentBody);

    //before image field ApexWrapper is unwrapped

    system.debug(contentBody.get('Image'));

    //unwrap Image field in contentBody

    Map<String,Object> Image =

   (Map<String,Object>)ConnectApi.ConnectUtilities.unwrapApexWrapper(contentBody.get('Image'));

    //after image field ApexWrapper is unwrapped

    system.debug(Image);

    //replace wrapped primary_image in contentBody with unwrapped version

    contentBody.put('Image', Image);

    //after contentBody field ApexWrapper is unwrapped, with image field also unwrapped

    system.debug(contentBody);

    //put unwrapped contentBody in map

    contentBodyMap.put(res.contentKey, contentBody);

   }

   //check unwrapped contentBody map

   System.debug(contentBodyMap);

#### Retired ManagedContentDelivery Methods

```

These methods for `ManagedContentDelivery` are retired.

IN THIS SECTION:

getManagedContentChannel(channelId)
Get a managed content delivery channel.

getManagedContentsForChannel(channelId, managedContentIds, contentKeys, contentTypeFQN, language, publishStartDate,
publishEndDate, includeContentBody, referenceDepth, expandReferences, referencesAsList, pageParam, pageSize)
Get a collection of published contents for a channel.


Apex Reference Guide ManagedContentDelivery Class

getManagedContentsForSite(siteId, managedContentIds, contentKeys, contentTypeFQN, language, publishStartDate, publishEndDate,
includeContentBody, referenceDepth, expandReferences, referencesAsList, pageParam, pageSize)
Get a collection of published contents for an Experience Cloud site.

##### **`getManagedContentChannel(channelId)`**

Get a managed content delivery channel.

API Version

54.0–61.0

In version 62.0 and later, use `getManagedContentDeliveryChannel(channelId)` to get a managed content delivery
channel.

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentChannelDetail getManagedContentChannel(String

   channelId)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

Return Value

Type: `ConnectApi.ManagedContentChannelDetail`

##### **`getManagedContentsForChannel(channelId, managedContentIds, contentKeys,`**

```
  contentTypeFQN, language, publishStartDate, publishEndDate,

  includeContentBody, referenceDepth, expandReferences, referencesAsList,

  pageParam, pageSize)

```

Get a collection of published contents for a channel.

API Version

55.0—57.0

##### In version 58.0 and later, use getManagedContentsForChannel(channelId, managedContentIds,

```
   contentKeys, contentTypeFQN, language, publishStartDate, publishEndDate,

```


Apex Reference Guide ManagedContentDelivery Class

```
   includeContentBody, referenceDepth, expandReferences, referencesAsList, pageParam,
```

`pageSize, showAbsoluteUrl)` .

Available to Guest Users

55.0—57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocumentCollection

   getManagedContentsForChannel(String channelId, List<String> managedContentIds,

   List<String> contentKeys, String contentTypeFQN, String language, String

   publishStartDate, String publishEndDate, Boolean includeContentBody, Integer

   referenceDepth, Boolean expandReferences, Boolean referencesAsList, Integer pageParam,

   Integer pageSize)

```

Parameters

```
   channelId
```

Type: String

ID of the channel.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of up to 100 managed content IDs. Specify either managed content IDs or content keys.

```
   contentKeys
```

Type: List<String>

Comma-separated list of up to 50 content keys. Specify either managed content IDs or content keys.

```
   contentTypeFQN
```

Type: String

Fully qualified name of the managed content type.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the configured fallback language or the channel’s default language. If the content isn’t available in the fallback language and the
channel’s default language, we return an error.

```
   publishStartDate
```

Type: String

ISO 8601 formatted publish start date.

```
   publishEndDate
```

Type: String

ISO 8601 formatted publish end date.


Apex Reference Guide ManagedContentDelivery Class

```
   includeContentBody
```

Type: Boolean

Specifies whether to return the content body ( `true` ) or the content summary ( `false` ). If unspecified, the default value is `false` .

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class is null. If unspecified, the default value
is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class ( `true` ). If you specify `false`, the
references are returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25. If you specify

`true` for _`expandReferences`_ or _`includeContentBody`_, the maximum page size you can specify is 25.

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocumentCollection`

##### **`getManagedContentsForSite(siteId, managedContentIds, contentKeys,`**

```
  contentTypeFQN, language, publishStartDate, publishEndDate,

  includeContentBody, referenceDepth, expandReferences, referencesAsList,

  pageParam, pageSize)

```

Get a collection of published contents for an Experience Cloud site.

API Version

55.0—57.0

##### In version 58.0 and later, use getManagedContentsForSite(siteId, managedContentIds, contentKeys,

```
   contentTypeFQN, language, publishStartDate, publishEndDate, includeContentBody,
```

`referenceDepth, expandReferences, referencesAsList, pageParam, pageSize, showAbsoluteUrl)` .


Apex Reference Guide ManagedContentDelivery Class

Available to Guest Users

55.0—57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentDeliveryDocumentCollection

   getManagedContentsForSite(String siteId, List<String> managedContentIds, List<String>

   contentKeys, String contentTypeFQN, String language, String publishStartDate, String

   publishEndDate, Boolean includeContentBody, Integer referenceDepth, Boolean

   expandReferences, Boolean referencesAsList, Integer pageParam, Integer pageSize)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   managedContentIds
```

Type: List<String>

Comma-separated list of up to 100 managed content IDs. Specify either managed content IDs or content keys.

```
   contentKeys
```

Type: List<String>

Comma-separated list of up to 50 content keys. Specify either managed content IDs or content keys.

```
   contentTypeFQN
```

Type: String

Fully qualified name of the managed content type.

```
   language
```

Type: String

Language locale for the managed content, for example, `en_US` . If the requested translation isn’t available, the language defaults
to the configured fallback language or the channel’s default language. If the content isn’t available in the fallback language and the
channel’s default language, we return an error.

```
   publishStartDate
```

Type: String

ISO 8601 formatted publish start date.

```
   publishEndDate
```

Type: String

ISO 8601 formatted publish end date.

```
   includeContentBody
```

Type: Boolean

Specifies whether to return the content body ( `true` ) or the content summary ( `false` ). If unspecified, the default value is `false` .


### Apex Reference Guide ManagedContentSpaces Class

```
   referenceDepth
```

Type: Integer

An integer 0–3 specifying the depth of references. If you specify 0, the `references` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class is null. If unspecified, the default value
is 0.

```
   expandReferences
```

Type: Boolean

Specifies whether to include details of references ( `true` ) or summaries of references ( `false` ) in the output class. If unspecified,
the default value is `false` .

```
   referencesAsList
```

Type: Boolean

Specifies whether to return the references as a list in the `referencesList` property of the
`ConnectApi.ManagedContentDeliveryDocumentCollection` output class ( `true` ). If you specify `false`, the
references are returned as key value pairs in the `references` property. If unspecified, the default value is `false` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25. If you specify

`true` for _`expandReferences`_ or _`includeContentBody`_, the maximum page size you can specify is 25.

Return Value

Type: `ConnectApi.ManagedContentDeliveryDocumentCollection`

### ManagedContentSpaces Class

Get channels in a managed content space. Add or remove channels from a managed content space.

Namespace

ConnectApi

#### ManagedContentSpaces Methods

### These methods are for ManagedContentSpaces . All methods are static.

IN THIS SECTION:

getManagedContentSpace(contentSpaceId)
Get a managed content space.

getManagedContentSpaceChannels(contentSpaceId, pageParam, pageSize)
Get channels for a managed content space.


Apex Reference Guide ManagedContentSpaces Class

getManagedContentSpaces(pageParam, pageSize, nameFragment)
Get managed content spaces.

patchManagedContentSpace(contentSpaceId, ManagedContentSpaceUpdateInput)
Update the name or description of a managed content space.

patchManagedContentSpaceChannels(contentSpaceId, spaceChannels)
Add or remove channels from a managed content space.

postManagedContentSpace(ManagedContentSpaceInput)
Create a managed content space.

##### **`getManagedContentSpace(contentSpaceId)`**

Get a managed content space.

API Version

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentSpace getManagedContentSpace(String

   contentSpaceId)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

Return Value

Type: `ConnectApi.ManagedContentSpace`

##### **`getManagedContentSpaceChannels(contentSpaceId, pageParam, pageSize)`**

Get channels for a managed content space.

API Version

62.0

Requires Chatter

No


Apex Reference Guide ManagedContentSpaces Class

Signature

```
   public static ConnectApi.ManagedContentSpaceChannelsRepresentation

   getManagedContentSpaceChannels(String contentSpaceId, Integer pageParam, Integer

   pageSize)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25. Items are sorted by the
last modified date.

Return Value

Type: `ConnectApi.ManagedContentSpaceChannelsRepresentation`

##### **`getManagedContentSpaces(pageParam, pageSize, nameFragment)`**

Get managed content spaces.

API Version

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentSpaceCollectionRepresentation

   getManagedContentSpaces(Integer pageParam, Integer pageSize, String nameFragment)

```

Parameters

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 250. If you pass in `null`, the default size is 25.


Apex Reference Guide ManagedContentSpaces Class

```
   nameFragment
```

Type: String

Name fragment to filter spaces that contain the value in the workspace name.

Return Value

Type: `ConnectApi.ManagedContentSpaceCollectionRepresentation`

##### **`patchManagedContentSpace(contentSpaceId, ManagedContentSpaceUpdateInput)`**

Update the name or description of a managed content space.

API Version

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentSpace patchManagedContentSpace(String

   contentSpaceId, ConnectApi.ManagedContentSpaceUpdateInput ManagedContentSpaceUpdateInput)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

```
   ManagedContentSpaceUpdateInput
```

Type: `ConnectApi.ManagedContentSpaceUpdateInput`

`ConnectApi.ManagedContentSpaceUpdateInput` class with the updated name or description.

Return Value

Type: `ConnectApi.ManagedContentSpace`

##### **`patchManagedContentSpaceChannels(contentSpaceId, spaceChannels)`**

Add or remove channels from a managed content space.

API Version

62.0

Requires Chatter

No


Apex Reference Guide ManagedContentSpaces Class

Signature

```
   public static ConnectApi.ManagedContentSpaceChannelsRepresentation

   patchManagedContentSpaceChannels(String contentSpaceId,

   ConnectApi.ManagedContentSpaceChannelsInputRepresentation spaceChannels)

```

Parameters

```
   contentSpaceId
```

Type: String

ID of the managed content space.

```
   spaceChannels
```

Type: `ConnectApi.ManagedContentSpaceChannelsInputRepresentation`

`ConnectApi.ManagedContentSpaceChannelsInputRepresentation` input class with the channels to add or
remove from the managed content space.

Return Value

Type: `ConnectApi.ManagedContentSpaceChannelsRepresentation`

##### **`postManagedContentSpace(ManagedContentSpaceInput)`**

Create a managed content space.

API Version

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedContentSpace

   postManagedContentSpace(ConnectApi.ManagedContentSpaceInput ManagedContentSpaceInput)

```

Parameters

```
   ManagedContentSpaceInput
```

Type: `ConnectApi.ManagedContentSpaceInput`

`ConnectApi.ManagedContentSpaceInput` class describing the space to create.

Return Value

Type: `ConnectApi.ManagedContentSpace`


### Apex Reference Guide ManagedTopics Class ManagedTopics Class

Get managed topics in an Experience Cloud site. Create, delete, and reorder managed topics.

Namespace

ConnectApi

#### ManagedTopics Methods

### These methods are for ManagedTopics . All methods are static.

IN THIS SECTION:

createManagedTopic(communityId, recordId, managedTopicType)
Create a managed topic of a specific type for an Experience Cloud site.

createManagedTopic(communityId, recordId, managedTopicType, parentId)
Create a child managed topic for an Experience Cloud site.

createManagedTopicByName(communityId, name, managedTopicType)
Create a managed topic of a specific type by name for an Experience Cloud site.

createManagedTopicByName(communityId, name, managedTopicType, parentId)
Create a child managed topic by name for an Experience Cloud site.

deleteManagedTopic(communityId, managedTopicId)
Delete a managed topic from an Experience Cloud site.

getManagedTopic(communityId, managedTopicId)
Get a managed topic in an Experience Cloud site.

getManagedTopic(communityId, managedTopicId, depth)
Get a managed topic, including its parent and children managed topics, in an Experience Cloud site.

getManagedTopics(communityId)
Get the featured and navigational managed topics for an Experience Cloud site.

getManagedTopics(communityId, managedTopicType)
Get managed topics of the specified type for an Experience Cloud site.

getManagedTopics(communityId, managedTopicType, depth)
Get managed topics of the specified type, including their parent and children managed topics, in an Experience Cloud site.

getManagedTopics(communityId, managedTopicType, recordIds, depth)
Get managed topics of the specified type, including their parent and children managed topics, that are associated with topics in an
Experience Cloud site.

getManagedTopics(communityId, managedTopicType, pageParam, pageSize)
Get a page of managed topics.

reorderManagedTopics(communityId, managedTopicPositionCollection)
Reorder the relative positions of managed topics in an Experience Cloud site.


Apex Reference Guide ManagedTopics Class

##### **`createManagedTopic(communityId, recordId, managedTopicType)`**

Create a managed topic of a specific type for an Experience Cloud site.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic createManagedTopic(String communityId, String

   recordId, ConnectApi.ManagedTopicType managedTopicType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID of the topic.

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Specify the type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

You can create up to 25 `Featured` and 5,000 `Content` topics. You can create up to eight levels of `Navigational` managed
topics with 25 top-level topics and 10 children topics per level for a maximum of 2,775 `Navigational` topics.

Return Value

Type: `ConnectApi.ManagedTopic`

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can create managed
topics.


Apex Reference Guide ManagedTopics Class

##### **`createManagedTopic(communityId, recordId, managedTopicType, parentId)`**

Create a child managed topic for an Experience Cloud site.

API Version

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic createManagedTopic(String communityId, String

   recordId, ConnectApi.ManagedTopicType managedTopicType, String parentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID of the topic.

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Specify `Navigational` for the type of managed topic to create a child managed topic.

You can create up to 25 `Featured` and 5,000 `Content` topics. You can create up to eight levels of `Navigational` managed
topics with 25 top-level topics and 10 children topics per level for a maximum of 2,775 `Navigational` topics.

```
   parentId
```

Type: String

ID of the parent managed topic.

You can create up to eight levels (parent, direct children, their children, etc.) of managed topics and up to 10 children managed
topics per managed topic.

Return Value

Type: `ConnectApi.ManagedTopic`

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can create managed
topics.

##### **`createManagedTopicByName(communityId, name, managedTopicType)`**

Create a managed topic of a specific type by name for an Experience Cloud site.


Apex Reference Guide ManagedTopics Class

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic createManagedTopicByName(String communityId,

   String name, ConnectApi.ManagedTopicType managedTopicType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   name
```

Type: String

Name of the topic.

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Specify the type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

You can create up to 25 `Featured` and 5,000 `Content` topics. You can create up to eight levels of `Navigational` managed
topics with 25 top-level topics and 10 children topics per level for a maximum of 2,775 `Navigational` topics.

Return Value

Type: `ConnectApi.ManagedTopic`

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can create managed
topics.

##### **`createManagedTopicByName(communityId, name, managedTopicType, parentId)`**

Create a child managed topic by name for an Experience Cloud site.

API Version

35.0


Apex Reference Guide ManagedTopics Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic createManagedTopicByName(String communityId,

   String name, ConnectApi.ManagedTopicType managedTopicType, String parentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   name
```

Type: String

Name of the topic.

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Specify `Navigational` for the type of managed topic to create a child managed topic.

You can create up to 25 `Featured` and 5,000 `Content` topics. You can create up to eight levels of `Navigational` managed
topics with 25 top-level topics and 10 children topics per level for a maximum of 2,775 `Navigational` topics.

```
   parentId
```

Type: String

ID of the parent managed topic.

You can create up to eight levels (parent, direct children, their children, etc.) of managed topics and up to 10 children managed
topics per managed topic.

Return Value

Type: `ConnectApi.ManagedTopic`

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can create managed
topics.

##### **`deleteManagedTopic(communityId, managedTopicId)`**

Delete a managed topic from an Experience Cloud site.

API Version

32.0

Requires Chatter

No


Apex Reference Guide ManagedTopics Class

Signature

```
   public static deleteManagedTopic(String communityId, String managedTopicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicId
```

Type: String

ID of managed topic.

Return Value

Type: Void

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can delete managed
topics.

##### **`getManagedTopic(communityId, managedTopicId)`**

Get a managed topic in an Experience Cloud site.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic getManagedTopic(String communityId, String

   managedTopicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ManagedTopics Class

```
   managedTopicId
```

Type: String

ID of managed topic.

Return Value

Type: `ConnectApi.ManagedTopic`

##### **`getManagedTopic(communityId, managedTopicId, depth)`**

Get a managed topic, including its parent and children managed topics, in an Experience Cloud site.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopic getManagedTopic(String communityId, String

   managedTopicId, Integer depth)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicId
```

Type: String

ID of managed topic.

```
   depth
```

Type: Integer

Specify an integer 1–8. If you specify 1, the `children` property of the `ConnectApi.ManagedTopic` output class is `null` .
If you specify 2, the `children` property of the `ConnectApi.ManagedTopic` output class contains the direct children
managed topics, if any, of the managed topic. If you specify 3–8, you get the direct children managed topics and their children
managed topics if there are any. If depth isn’t specified, it defaults to 1.

Return Value

Type: `ConnectApi.ManagedTopic`


Apex Reference Guide ManagedTopics Class

##### **`getManagedTopics(communityId)`**

Get the featured and navigational managed topics for an Experience Cloud site.

##### To get the content topics for an Experience Cloud site, use getManagedTopics(communityId, managedTopicType) .

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ManagedTopicCollection`

##### **`getManagedTopics(communityId, managedTopicType)`**

Get managed topics of the specified type for an Experience Cloud site.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId,

   ConnectApi.ManagedTopicType managedTopicType)

```


Apex Reference Guide ManagedTopics Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

If you specify `Content`, up to 50 topics are returned. If you want more than 50 `Content` topics, use

`getManagedTopics(communityId, managedTopicType, pageParam, pageSize)` .

Return Value

Type: `ConnectApi.ManagedTopicCollection`

##### **`getManagedTopics(communityId, managedTopicType, depth)`**

Get managed topics of the specified type, including their parent and children managed topics, in an Experience Cloud site.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId,

   ConnectApi.ManagedTopicType managedTopicType, Integer depth)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`


Apex Reference Guide ManagedTopics Class

Type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

```
   depth
```

Type: Integer

Specify an integer 1–8. If you specify 1, the `children` property of the `ConnectApi.ManagedTopic` output class is `null` .
If you specify 2, the `children` property of the `ConnectApi.ManagedTopic` output class contains the direct children
managed topics, if any, of the managed topic. If you specify 3–8, you get the direct children managed topics and their children
managed topics if there are any. If depth isn’t specified, it defaults to 1.

Return Value

Type: `ConnectApi.ManagedTopicCollection`

##### **`getManagedTopics(communityId, managedTopicType, recordIds, depth)`**

Get managed topics of the specified type, including their parent and children managed topics, that are associated with topics in an
Experience Cloud site.

API Version

38.0

Available to Guest Users

38.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId,

   ConnectApi.ManagedTopicType managedTopicType, List<String> recordIds, Integer depth)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Type of managed topic.


Apex Reference Guide ManagedTopics Class

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

```
   recordIds
```

Type: List<String>

A list of up to 100 topic IDs associated with the managed topics.

If you list more than 10 topic IDs, you can’t specify 2–8 for _`depth`_ .

```
   depth
```

Type: Integer

Specify an integer 1–8. If you specify 1, the `children` property of the `ConnectApi.ManagedTopic` output class is `null` .
If you specify 2, the `children` property of the `ConnectApi.ManagedTopic` output class contains the direct children
managed topics, if any, of the managed topic. If you specify 3–8, you get the direct children managed topics and their children
managed topics if there are any. If depth isn’t specified, it defaults to 1.

Return Value

Type: `ConnectApi.ManagedTopicCollection`

##### **`getManagedTopics(communityId, managedTopicType, pageParam, pageSize)`**

Get a page of managed topics.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId,

   ConnectApi.ManagedTopicType managedTopicType, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ManagedTopics Class

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 50.

Return Value

Type: `ConnectApi.ManagedTopicCollection`

##### **`reorderManagedTopics(communityId, managedTopicPositionCollection)`**

Reorder the relative positions of managed topics in an Experience Cloud site.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection reorderManagedTopics(String communityId,

   ConnectApi.ManagedTopicPositionCollectionInput managedTopicPositionCollection)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicPositionCollection
```

Type: `ConnectApi.ManagedTopicPositionCollectionInput`

A collection of relative positions of managed topics. This collection can include only `Featured` and `Navigational` topics
and doesn’t have to include all managed topics.


Apex Reference Guide ManagedTopics Class

Return Value

Type: `ConnectApi.ManagedTopicCollection`

Usage

Only community managers (users with the Create and Set Up Experiences or Manage Experiences permission) can reorder managed
topics.

You can reorder parent managed topics or children managed topics with the same parent. If you don’t include all managed topics in
the `ConnectApi.ManagedTopicPositionCollectionInput`, the managed topics are reordered by respecting the
positions indicated in the `ConnectApi.ManagedTopicPositionCollectionInput` and then by pushing down any
managed topics that aren’t included in the `ConnectApi.ManagedTopicPositionCollectionInput` to the next available
position.

Example

If you have these managed topics:

**Managed Topic** **Position**

ManagedTopicA 0

ManagedTopicB 1

ManagedTopicC 2

ManagedTopicD 3

ManagedTopicE 4

And you reorder managed topics by including this information in `ConnectApi.ManagedTopicPositionCollectionInput` :

**Managed Topic** **Position**

ManagedTopicD 0

ManagedTopicE 2

The result is:

**Managed Topic** **Position**

ManagedTopicD 0

ManagedTopicA 1

ManagedTopicE 2

ManagedTopicB 3

ManagedTopicC 4


Apex Reference Guide ManagedTopics Class

#### Retired ManagedTopics Methods

These methods for `ManagedTopics` are retired.

IN THIS SECTION:

##### getManagedTopics(communityId, managedTopicType, recordId, depth)

Get managed topics of the specified type, including their parent and children managed topics, that are associated with a given topic
in an Experience Cloud site.

##### **`getManagedTopics(communityId, managedTopicType, recordId, depth)`**

Get managed topics of the specified type, including their parent and children managed topics, that are associated with a given topic in
an Experience Cloud site.

API Version

35.0–37.0

Important: In version 38.0 and later, use `getManagedTopics(communityId, managedTopicType, recordIds,`
`depth)` .

Available to Guest Users

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedTopicCollection getManagedTopics(String communityId,

   ConnectApi.ManagedTopicType managedTopicType, String recordId, Integer depth)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   managedTopicType
```

Type: `ConnectApi.ManagedTopicType`

Type of managed topic.

**•** `Content` —Topics that are associated with native content.

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud site.

A topic can be associated with all three managed topic types, so a topic can be a `Featured`, `Navigational`, and `Content`
topic.


### Apex Reference Guide MarketingIntegration Class

```
   recordId
```

Type: String

ID of the topic associated with the managed topics.

```
   depth
```

Type: Integer

Specify an integer 1–8. If you specify 1, the `children` property of the `ConnectApi.ManagedTopic` output class is `null` .
If you specify 2, the `children` property of the `ConnectApi.ManagedTopic` output class contains the direct children
managed topics, if any, of the managed topic. If you specify 3–8, you get the direct children managed topics and their children
managed topics if there are any. If depth isn’t specified, it defaults to 1.

Return Value

Type: `ConnectApi.ManagedTopicCollection`

### MarketingIntegration Class

Get, save, and submit a microsites marketing integration form for an Experience Cloud site.

Namespace

ConnectApi

#### MarketingIntegration Methods

### The following are methods for MarketingIntegration . All methods are static. MarketingIntegration methods make calls to Marketing Cloud Engagement REST APIs to create, query, and insert data to the

[data extension object. If the API returns errors, ConnectinApex error messages include the error code and message from Marketing Cloud](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/error-handling.htm)
Engagement.

IN THIS SECTION:

##### getForm(siteId, formId)

Get a marketing integration form for an Experience Cloud site.

saveForm(siteId, formInput)
Save a marketing integration form for an Experience Cloud site.

submitForm(siteId, formId, formSubmissionInput)
Submit a marketing integration form for an Experience Cloud site.

##### **`getForm(siteId, formId)`**

Get a marketing integration form for an Experience Cloud site.

API Version

53.0


Apex Reference Guide MarketingIntegration Class

Requires Chatter

No

Signature

```
   public static ConnectApi.Form getForm(String siteId, String formId)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   formId
```

Type: String

ID of the form.

Return Value

Type: `ConnectApi.Form`

##### **`saveForm(siteId, formInput)`**

Save a marketing integration form for an Experience Cloud site.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Form saveForm(String siteId, ConnectApi.FormInput formInput)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   formInput
```

Type: `ConnectApi.FormInput`

A `ConnectApi.FormInput` object to save.

Return Value

Type: `ConnectApi.Form`


### Apex Reference Guide Mentions Class

Usage

This method attempts to create a read-only data extension in Marketing Cloud Engagement. A Marketing Cloud Engagement admin
can change the read-only setting. We recommend keeping the data extension as read-only to maintain schema consistency with the
form.

##### **`submitForm(siteId, formId, formSubmissionInput)`**

Submit a marketing integration form for an Experience Cloud site.

API Version

53.0

Available to Guest Users

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FormSubmission submitForm(String siteId, String formId,

   ConnectApi.FormSubmissionInput formSubmissionInput)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   formId
```

Type: String

ID of the form.

```
   formSubmissionInput
```

Type: `ConnectApi.FormSubmissionInput`

A `ConnectApi.FormSubmissionInput` object to submit.

Return Value

Type: `ConnectApi.FormSubmission`

### Mentions Class

Access information about mentions. A mention is an “@” character followed by a user or group name. When a user or group is mentioned,
they receive a notification.


Apex Reference Guide Mentions Class

Namespace

ConnectApi

#### Mentions Methods These methods are for Mentions . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### getMentionCompletions(communityId, q, contextId)

Get the first page of possible users and groups to mention in a feed item body or comment body.

getMentionCompletions(communityId, q, contextId, type, pageParam, pageSize)
Get a page of possible mention proposals of the specified type.

getMentionValidations(communityId, parentId, recordIds, visibility)
Get information about whether the mentions are valid for the context user.

##### **`getMentionCompletions(communityId, q, contextId)`**

Get the first page of possible users and groups to mention in a feed item body or comment body.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.MentionCompletionPage getMentionCompletions (String communityId,

   String q, String contextId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

A search term for matching user and group names. Searching for a group requires a minimum of 2 characters. Searching for a user
doesn’t require a minimum number of characters. This parameter does not support wildcards.

```
   contextId
```

Type: String


Apex Reference Guide Mentions Class

A feed item ID (for a mention in a comment) or a feed subject ID (for a mention in a feed item) that narrows search results, with
more useful results listed first. Use a group ID for groups that allow customers to ensure mention completion results include customers.

Return Value

Type: `ConnectApi.MentionCompletionPage`

Usage

Call this method to generate a page of proposed mentions that a user can choose from when they enter characters after @ in a feed
item body or a comment body.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetMentionCompletions(communityId, q, contextId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getMentionCompletions(communityId, q, contextId, type, pageParam, pageSize)`**

Get a page of possible mention proposals of the specified type.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Mentions getMentionCompletions (String communityId, String q,

   String contextId, ConnectApi.MentionCompletionType type, Integer pageParam, Integer

   pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

A search term for matching user and group names. Searching for a group requires a minimum of 2 characters. Searching for a user
doesn’t require a minimum number of characters. This parameter does not support wildcards.

```
   contextId
```

Type: String


Apex Reference Guide Mentions Class

A feed item ID (for a mention in a comment) or a feed subject ID (for a mention in a feed item) that narrows search results, with
more useful results listed first. Use a group ID for groups that allow customers to ensure mention completion results include customers.

```
   type
```

Type: `ConnectApi.MentionCompletionType`

Type of mention completion.

**•** `All` —All mention completions, regardless of the type of record to which the mention refers.

**•** `Group` —Mention completions for groups.

**•** `User` —Mention completions for users.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.MentionCompletionPage`

Usage

Call this method to generate a page of proposed mentions that a user can choose from when they enter characters after @ in a feed
item body or a comment body.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetMentionCompletions(communityId, q, contextId, type, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getMentionValidations(communityId, parentId, recordIds, visibility)`**

Get information about whether the mentions are valid for the context user.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Mentions getMentionValidations(String communityId, String

   parentId, List<String> recordIds, ConnectApi.FeedItemVisibilityType visibility)

```


Apex Reference Guide Mentions Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   parentId
```

Type: String

The feed item parent ID.

```
   recordIds
```

Type: List<String>

A comma-separated list of IDs to be mentioned. The maximum value is 25.

```
   visibility
```

Type: `ConnectApi.FeedItemVisibilityType`

Type of users who can see a feed item.

**•** `AllUsers` —Visibility is not limited to internal users.

**•** `InternalUsers` —Visibility is limited to internal users.

Return Value

Type: `ConnectApi.MentionValidations`

Usage

Call this method to check whether the record IDs returned from a call to `ConnectApi.Mentions.getMentionCompletions`
are valid for the context user. For example, the context users can’t mention private groups they don’t belong to. If such a group were
included in the list of mention validations, the `ConnectApi.MentionValidations.hasErrors` property would be `true`
and the group would have a `ConnectApi.MentionValidation.valdiationStatus` of `Disallowed` .

#### Mentions Test Methods These test methods are for Mentions . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetMentionCompletions(communityId, q, contextId, result)`**

Register a `ConnectApi.MentionCompletionPage` object to be returned when `getMentionCompletions(String,`

`String, String)` is called in a test context.

API Version

29.0

Signature

```
   public static Void setTestGetMentionCompletions (String communityId, String q, String

   contextId, ConnectApi.MentionCompletionPage result)

```


Apex Reference Guide Mentions Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

A search term for matching user and group names. Searching for a group requires a minimum of 2 characters. Searching for a user
doesn’t require a minimum number of characters. This parameter does not support wildcards.

```
   contextId
```

Type: String

A feed item ID (for a mention in a comment) or a feed subject ID (for a mention in a feed item) that narrows search results, with
more useful results listed first. Use a group ID for groups that allow customers to ensure mention completion results include customers.

```
   result
```

Type: `ConnectApi.MentionCompletionPage`

A `ConnectApi.MentionCompletionPage` object containing test data.

Return Value

Type: Void

SEE ALSO:

getMentionCompletions(communityId, q, contextId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetMentionCompletions(communityId, q, contextId, type, pageParam,`**

```
  pageSize, result)

```

Register a `ConnectApi.MentionCompletionPage` object to be returned when `getMentionCompletions(String,`

`String, String, ConnectApi.MentionCompletionType, Integer, Integer)` is called in a test context.

API Version

29.0

Signature

```
   public static Void setTestGetMentionCompletions (String communityId, String q, String

   contextId, ConnectApi.MentionCompletionType type, Integer pageParam, Integer pageSize,

   ConnectApi.MentionCompletionPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


### Apex Reference Guide Missions Class

```
   q
```

Type: String

A search term for matching user and group names. Searching for a group requires a minimum of 2 characters. Searching for a user
doesn’t require a minimum number of characters. This parameter does not support wildcards.

```
   contextId
```

Type: String

A feed item ID (for a mention in a comment) or a feed subject ID (for a mention in a feed item) that narrows search results, with
more useful results listed first. Use a group ID for groups that allow customers to ensure mention completion results include customers.

```
   type
```

Type: `ConnectApi.MentionCompletionType`

Type of mention completion.

**•** `All` —All mention completions, regardless of the type of record to which the mention refers.

**•** `Group` —Mention completions for groups.

**•** `User` —Mention completions for users.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   result
```

Type: `ConnectApi.MentionCompletionPage`

A `ConnectApi.MentionCompletionPage` object containing test data.

Return Value

Type: Void

SEE ALSO:

getMentionCompletions(communityId, q, contextId, type, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### Missions Class

Export and purge mission activity for users. Get a user’s mission progress. Update mission activity counts for users.

Namespace

ConnectApi

#### Missions Methods

### These methods are for Missions . All methods are static.


Apex Reference Guide Missions Class

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### exportUserMissionsActivities(communityId, userId)

Export mission activity for a user.

getUserMissionsProgress(communityId, userId)
Get mission activity progress for a user.

purgeUserMissionsActivities(communityId, userId)
Start a job to purge mission activity for a user.

purgeUserMissionsActivities(communityId)
Start a job to purge mission activity for all users.

updateUserMissionActivityCount(activityType, activityCount, communityId, userId)
Update the mission activity count for a user.

##### **`exportUserMissionsActivities(communityId, userId)`**

Export mission activity for a user.

API Version

45.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserMissionActivitiesJob exportUserMissionsActivities(String

   communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

Return Value

Type: `ConnectApi.UserMissionActivitiesJob`

Usage

You can export these activities with this method.


Apex Reference Guide Missions Class

**•** `FeedItemAnswerAQuestion` —User answered a question.

**•** `FeedItemLikeSomething` —User liked a post or comment.

**•** `FeedItemMarkAnswerAsBest` —User marked an answer as the best answer.

**•** `FeedItemPostQuestion` —User posted a question.

**•** `FeedItemReceiveAComment` —User received a comment on a post.

**•** `FeedItemReceiveALike` —User received a like on a post or comment.

**•** `FeedItemReceiveAnAnswer` —User received an answer to a question.

**•** `FeedItemWriteAComment` —User commented on a post.

**•** `FeedItemWriteAPost` —User made a post.

**•** `FeedItemYourAnswerMarkedBest` —User’s answer was marked as the best answer.

##### **`getUserMissionsProgress(communityId, userId)`**

Get mission activity progress for a user.

API Version

46.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserMissionActivityCollection getUserMissionsProgress(String

   communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

Return Value

Type: `ConnectApi.UserMissionActivityCollection`

##### **`purgeUserMissionsActivities(communityId, userId)`**

Start a job to purge mission activity for a user.


Apex Reference Guide Missions Class

API Version

45.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserMissionActivitiesJob purgeUserMissionsActivities(String

   communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

Return Value

Type: `ConnectApi.UserMissionActivitiesJob`

Usage

This method purges these activities.

**•** `FeedItemAnswerAQuestion` —User answered a question.

**•** `FeedItemLikeSomething` —User liked a post or comment.

**•** `FeedItemMarkAnswerAsBest` —User marked an answer as the best answer.

**•** `FeedItemPostQuestion` —User posted a question.

**•** `FeedItemReceiveAComment` —User received a comment on a post.

**•** `FeedItemReceiveALike` —User received a like on a post or comment.

**•** `FeedItemReceiveAnAnswer` —User received an answer to a question.

**•** `FeedItemWriteAComment` —User commented on a post.

**•** `FeedItemWriteAPost` —User made a post.

**•** `FeedItemYourAnswerMarkedBest` —User’s answer was marked as the best answer.

##### **`purgeUserMissionsActivities(communityId)`**

Start a job to purge mission activity for all users.

API Version

49.0


Apex Reference Guide Missions Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserMissionActivitiesJob purgeUserMissionsActivities(String

   communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.UserMissionActivitiesJob`

Usage

This method purges these activities.

**•** `FeedItemAnswerAQuestion` —User answered a question.

**•** `FeedItemLikeSomething` —User liked a post or comment.

**•** `FeedItemMarkAnswerAsBest` —User marked an answer as the best answer.

**•** `FeedItemPostQuestion` —User posted a question.

**•** `FeedItemReceiveAComment` —User received a comment on a post.

**•** `FeedItemReceiveALike` —User received a like on a post or comment.

**•** `FeedItemReceiveAnAnswer` —User received an answer to a question.

**•** `FeedItemWriteAComment` —User commented on a post.

**•** `FeedItemWriteAPost` —User made a post.

**•** `FeedItemYourAnswerMarkedBest` —User’s answer was marked as the best answer.

##### **`updateUserMissionActivityCount(activityType, activityCount, communityId,`**

```
  userId)

```

Update the mission activity count for a user.

API Version

45.0

Requires Chatter

Yes


### Apex Reference Guide NamedCredentials Class

Signature

```
   public static ConnectApi.UserMissionActivityStatus

   updateUserMissionActivityCount(ConnectApi.UserMissionActivityType activityType, Integer

   activityCount, String communityId, String userId)

```

Parameters

```
   activityType
```

Type: `ConnectApi.UserMissionActivityType`

Type of mission activity for a user. Values are:

**•** `FeedItemAnswerAQuestion` —User answered a question.

**•** `FeedItemLikeSomething` —User liked a post or comment.

**•** `FeedItemMarkAnswerAsBest` —User marked an answer as the best answer.

**•** `FeedItemPostQuestion` —User posted a question.

**•** `FeedItemReceiveAComment` —User received a comment on a post.

**•** `FeedItemReceiveALike` —User received a like on a post or comment.

**•** `FeedItemReceiveAnAnswer` —User received an answer to a question.

**•** `FeedItemWriteAComment` —User commented on a post.

**•** `FeedItemWriteAPost` —User made a post.

**•** `FeedItemYourAnswerMarkedBest` —User’s answer was marked as the best answer.

```
   activityCount
```

Type: Integer

Number of mission activities of the specified type for the user.

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

Return Value

Type: `ConnectApi.UserMissionActivityStatus`

### NamedCredentials Class

Create, refresh, get, delete, replace, and update credentials. Create and get external credentials. Create and get named credentials. Create,
get, delete, and update external auth identity providers. Get the URL for the OAuth token flow for an external credential.

Note: Managed packages can access only the named credentials and external credentials that are included in or created from
the package’s Apex code. If a managed package tries to access non-packaged named credentials and external credentials that a
Salesforce admin created in the org, an error occurs.


Apex Reference Guide NamedCredentials Class

Namespace

ConnectApi

#### NamedCredentials Methods These methods are for NamedCredentials . All methods are static.

IN THIS SECTION:

createCredential(requestBody)
Create a credential.

createCredential(requestBody, action)
Refresh an OAuth or AWS Roles Anywhere credential.

createExternalAuthIdentityProvider(requestBody)
Create an external auth identity provider.

createExternalAuthIdentityProviderCredentials(fullName, requestBody)
Create external auth identity provider credentials.

createExternalCredential(requestBody)
Create an external credential.

createNamedCredential(requestBody)
Create a named credential.

deleteCredential(externalCredential, principalName, principalType)
Delete a credential.

deleteCredential(externalCredential, principalName, principalType, authenticationParameters)
Delete a credential with authentication parameters.

deleteExternalAuthIdentityProvider(developerName)
Delete an external auth identity provider.

deleteExternalCredential(developerName)
Delete an external credential.

deleteNamedCredential(developerName)
Delete a named credential.

getCredential(externalCredential, principalName, principalType)
Get a credential.

getExternalAuthIdentityProvider(fullName)
Get an external auth identity provider.

getExternalAuthIdentityProviderCredentials(fullName)
Get external auth identity provider credentials.

getExternalAuthIdentityProviders()
Get a list of external auth identity providers in the org.

getExternalCredential(developerName)
Get an external credential, including the named credentials and principals associated with it and the type and status of each principal.


Apex Reference Guide NamedCredentials Class

getExternalCredentials()
Get external credentials that the user can authenticate to.

getNamedCredential(developerName)
Get a named credential.

getNamedCredentials()
Get a list of named credentials for the org.

getOAuthCredentialAuthUrl(requestBody)
Get the URL for the OAuth token flow for an external credential.

patchCredential(requestBody)
Update custom credentials.

updateCredential(requestBody)
Replace a credential.

updateExternalAuthIdentityProvider(developerName, requestBody)
Update an external auth identity provider.

updateExternalAuthIdentityProviderCredentials(fullName, requestBody)
Replace external auth identity provider credentials.

updateExternalCredential(developerName, requestBody)
Update an external credential.

updateNamedCredential(developerName, requestBody)
Update a named credential.

SEE ALSO:

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/HTViewHelpDoc?id=named_credentials_about.htm&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

##### **`createCredential(requestBody)`**

Create a credential.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Credential createCredential(ConnectApi.CredentialInput

   requestBody)

```


Apex Reference Guide NamedCredentials Class

Parameters

```
   requestBody
```

Type: `ConnectApi.CredentialInput`

A `ConnectApi.CredentialInput` class.

Return Value

Type: `ConnectApi.Credential`

##### **`createCredential(requestBody, action)`**

Refresh an OAuth or AWS Roles Anywhere credential.

API Version

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Credential createCredential(ConnectApi.CredentialInput

   requestBody, ConnectApi.CreateCredentialAction action)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.CredentialInput`

A `ConnectApi.CredentialInput` class.

```
   action
```

Type: `ConnectApi.CreateCredentialAction`

Action to take when creating the credential. Value is:

**•** `Refresh`

Return Value

Type: `ConnectApi.Credential`

##### **`createExternalAuthIdentityProvider(requestBody)`**

Create an external auth identity provider.

API Version

62.0


Apex Reference Guide NamedCredentials Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProvider

   createExternalAuthIdentityProvider(ConnectApi.ExternalAuthIdentityProviderInput

   requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.ExternalAuthIdentityProviderInput` on page 2036

A `ConnectApi.ExternalAuthIdentityProviderInput` input class.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProvider` on page 2301

##### **`createExternalAuthIdentityProviderCredentials(fullName, requestBody)`**

Create external auth identity provider credentials.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProviderCredentials

   createExternalAuthIdentityProviderCredentials(String fullName,

   ConnectApi.ExternalAuthIdentityProviderCredentialsInput requestBody)

```

Parameters

```
   fullName
```

Type: String

Full name of the external auth identity provider to create credentials for.

```
   requestBody
```

Type: `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` on page 2035

A `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` input class

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2303


Apex Reference Guide NamedCredentials Class

##### **`createExternalCredential(requestBody)`**

Create an external credential.

API Version

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalCredential

   createExternalCredential(ConnectApi.ExternalCredentialInput requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.ExternalCredentialInput`

Input used to create or update an external credential.

Return Value

Type: `ConnectApi.ExternalCredential`

##### **`createNamedCredential(requestBody)`**

Create a named credential.

API Version

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NamedCredential

   createNamedCredential(ConnectApi.NamedCredentialInput requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.NamedCredentialInput`

Input used to create or update a named credential.


Apex Reference Guide NamedCredentials Class

Return Value

Type: `ConnectApi.NamedCredential`

##### **`deleteCredential(externalCredential, principalName, principalType)`**

Delete a credential.

This method deletes the user external credentials that store the encrypted access tokens used for named credential callouts, not the
external credential itself. You can delete an external credential only in the UI or by using REST API.

API Version

56.0

Requires Chatter

No

Signature

```
   public static Void deleteCredential(String externalCredential, String principalName,

   ConnectApi.CredentialPrincipalType principalType)

```

Parameters

```
   externalCredential
```

Type: String

Fully qualified developer name of the external credential.

```
   principalName
```

Type: String

Name of the external credential named principal.

```
   principalType
```

Type: `ConnectApi.CredentialPrincipalType`

Type of credential principal. Values are:

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`

Return Value

Type: Void

##### **`deleteCredential(externalCredential, principalName, principalType,`**

```
  authenticationParameters)

```

Delete a credential with authentication parameters.


Apex Reference Guide NamedCredentials Class

This method deletes the user external credentials that store the encrypted access tokens used for named credential callouts, not the
external credential itself. You can delete an external credential only in the UI or by using REST API.

API Version

59.0

Requires Chatter

No

Signature

```
   public static Void deleteCredential(String externalCredential, String principalName,

   ConnectApi.CredentialPrincipalType principalType, List<String> authenticationParameters)

```

Parameters

```
   externalCredential
```

Type: String

Fully qualified developer name of the external credential.

```
   principalName
```

Type: String

Name of the external credential named principal.

```
   principalType
```

Type: `ConnectApi.CredentialPrincipalType`

Type of credential principal. Values are:

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`

```
   authenticationParameters
```

Type: List<String>

List of authentication parameters only for custom protocols, for example `myApiKey,myApiSecret` . If unspecified, all credentials
are deleted.

Return Value

Type: Void

##### **`deleteExternalAuthIdentityProvider(developerName)`**

Delete an external auth identity provider.

API Version

66.0


Apex Reference Guide NamedCredentials Class

Requires Chatter

No

Signature

```
   public static Void deleteExternalAuthIdentityProvider(String developerName)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the external auth identity provider.

Return Value

Type: Void

##### **`deleteExternalCredential(developerName)`**

Delete an external credential.

API Version

66.0

Requires Chatter

No

Signature

```
   public static Void deleteExternalCredential(String developerName)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the external credential.

Return Value

Type: Void

##### **`deleteNamedCredential(developerName)`**

Delete a named credential.

API Version

66.0


Apex Reference Guide NamedCredentials Class

Requires Chatter

No

Signature

```
   public static Void deleteNamedCredential(String developerName)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the named credential.

Return Value

Type: Void

##### **`getCredential(externalCredential, principalName, principalType)`**

Get a credential.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Credential getCredential(String externalCredential, String

   principalName, ConnectApi.CredentialPrincipalType principalType)

```

Parameters

```
   externalCredential
```

Type: String

Fully qualified developer name of the external credential.

```
   principalName
```

Type: String

Name of the external credential named principal.

```
   principalType
```

Type: `ConnectApi.CredentialPrincipalType`

Type of credential principal. Values are:

**•** `AwsStsPrincipal`

**•** `NamedPrincipal`


Apex Reference Guide NamedCredentials Class

**•** `PerUserPrincipal`

Return Value

Type: `ConnectApi.Credential`

##### **`getExternalAuthIdentityProvider(fullName)`**

Get an external auth identity provider.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProvider

   getExternalAuthIdentityProvider(String fullName)

```

Parameters

```
   fullName
```

Type: String

Full name of the external auth identity provider.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProvider` on page 2301

##### **`getExternalAuthIdentityProviderCredentials(fullName)`**

Get external auth identity provider credentials.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProviderCredentials

   getExternalAuthIdentityProviderCredentials(String fullName)

```


Apex Reference Guide NamedCredentials Class

Parameters

```
   fullName
```

Type: String

Full name of the external auth identity provider.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2303

##### **`getExternalAuthIdentityProviders()`**

Get a list of external auth identity providers in the org.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProviderList

##### `getExternalAuthIdentityProviders()`

```

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderList` on page 2303

##### **`getExternalCredential(developerName)`**

Get an external credential, including the named credentials and principals associated with it and the type and status of each principal.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalCredential getExternalCredential(String developerName)

```

Parameters

```
   developerName
```

Type: String


Apex Reference Guide NamedCredentials Class

Fully qualified developer name of the external credential.

Return Value

Type: `ConnectApi.ExternalCredential`

##### **`getExternalCredentials()`**

Get external credentials that the user can authenticate to.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalCredentialList getExternalCredentials()

```

Return Value

Type: `ConnectApi.ExternalCredentialList`

##### **`getNamedCredential(developerName)`**

Get a named credential.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NamedCredential getNamedCredential(String developerName)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the named credential.

Return Value

Type: `ConnectApi.NamedCredential`


Apex Reference Guide NamedCredentials Class

##### **`getNamedCredentials()`**

Get a list of named credentials for the org.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NamedCredentialList getNamedCredentials()

```

Return Value

Type: `ConnectApi.NamedCredentialList`

##### **`getOAuthCredentialAuthUrl(requestBody)`**

Get the URL for the OAuth token flow for an external credential.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OAuthCredentialAuthUrl

   getOAuthCredentialAuthUrl(ConnectApi.OAuthCredentialAuthUrlInput requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.OAuthCredentialAuthUrlInput`

A `ConnectApi.OAuthCredentialAuthUrlInput` class indicating the OAuth authentication flow.

Return Value

Type: `ConnectApi.OAuthCredentialAuthUrl`


Apex Reference Guide NamedCredentials Class

Usage

Accepts input parameters representing a specific external credential and, optionally, a named principal. Returns the URL a user must
visit to begin the authentication flow, ultimately returning authentication tokens to Salesforce. Use this method as part of building a
customized or branded user interface to help users initiate authentication.

Example

```
   ConnectApi.OAuthCredentialAuthUrlInput input = new ConnectApi.OAuthCredentialAuthUrlInput();

   input.externalCredential = 'MyExternalCredentialDeveloperName';

   input.principalType = ConnectApi.CredentialPrincipalType.PerUserPrincipal;

   input.principalName = 'MyPrincipal'; // Only required when principalType = NamedPrincipal

   ConnectApi.OAuthCredentialAuthUrl output =

   ConnectApi.NamedCredentials.getOAuthCredentialAuthUrl(input);

   String authenticationUrl = output.authenticationUrl; // Redirect users to this URL to

   authenticate in the browser

##### **`patchCredential(requestBody)`**

```

Update custom credentials.

##### This method updates custom credentials. To replace a credential, use updateCredential(requestBody) .

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Credential patchCredential(ConnectApi.CredentialInput

   requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.CredentialInput`

A `ConnectApi.CredentialInput` class. Only the custom credentials in the input class are updated.

Return Value

Type: `ConnectApi.Credential`

##### **`updateCredential(requestBody)`**

Replace a credential.


Apex Reference Guide NamedCredentials Class

This method uses the `ConnectApi.CredentialInput` and the `ConnectApi.CredentialValueInput` input classes
to replace a credential’s values. In the UI, these values appear as the credential’s authentication parameters. To update a credential, use
`patchCredential(requestBody)` .

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Credential updateCredential(ConnectApi.CredentialInput

   requestBody)

```

Parameters

```
   requestBody
```

Type: `ConnectApi.CredentialInput`

A `ConnectApi.CredentialInput` class.

Return Value

Type: `ConnectApi.Credential`

##### **`updateExternalAuthIdentityProvider(developerName, requestBody)`**

Update an external auth identity provider.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProvider

   updateExternalAuthIdentityProvider(String developerName,

   ConnectApi.ExternalAuthIdentityProviderInput requestBody)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the external auth identity provider.


Apex Reference Guide NamedCredentials Class

```
   requestBody
```

Type: `ConnectApi.ExternalAuthIdentityProviderInput`

Input used to create or update an external auth identity provider.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProvider`

##### **`updateExternalAuthIdentityProviderCredentials(fullName, requestBody)`**

Replace external auth identity provider credentials.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalAuthIdentityProviderCredentials

   updateExternalAuthIdentityProviderCredentials(String fullName,

   ConnectApi.ExternalAuthIdentityProviderCredentialsInput requestBody)

```

Parameters

```
   fullName
```

Type: String

The external auth identity provider credentials to replace.

```
   requestBody
```

Type: `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` on page 2035

A `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` input class.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2303

##### **`updateExternalCredential(developerName, requestBody)`**

Update an external credential.

API Version

66.0


Apex Reference Guide NamedCredentials Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalCredential updateExternalCredential(String

   developerName, ConnectApi.ExternalCredentialInput requestBody)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the external credential.

```
   requestBody
```

Type: `ConnectApi.ExternalCredentialInput`

Input used to create or update an external credential.

Return Value

Type: `ConnectApi.ExternalCredential`

##### **`updateNamedCredential(developerName, requestBody)`**

Update a named credential.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NamedCredential updateNamedCredential(String developerName,

   ConnectApi.NamedCredentialInput requestBody)

```

Parameters

```
   developerName
```

Type: String

Fully qualified developer name of the named credential.

```
   requestBody
```

Type: `ConnectApi.NamedCredentialInput`

Input used to create or update a named credential.


### Apex Reference Guide NavigationMenu Class

Return Value

Type: `ConnectApi.NamedCredential`

### NavigationMenu Class

Get navigation menu items for an Experience Cloud site.

Namespace

ConnectApi

#### NavigationMenu Methods

### These methods are for NavigationMenu . All methods are static.

IN THIS SECTION:

##### getCommunityNavigationMenu(communityId, navigationLinkSetId, navigationLinkSetDeveloperName, publishStatus, includeImageUrl,

addHomeMenuItem, menuItemTypesToSkip)
Get navigation menu items for an Experience Cloud site.

##### getCommunityNavigationMenu(communityId, navigationLinkSetId, navigationLinkSetDeveloperName, publishStatus, includeImageUrl,

addHomeMenuItem, menuItemTypesToSkip, effectiveAccountId)
Get navigation menu items for an Experience Cloud based on an effective account.

##### **`getCommunityNavigationMenu(communityId, navigationLinkSetId,`**

```
  navigationLinkSetDeveloperName, publishStatus, includeImageUrl,

  addHomeMenuItem, menuItemTypesToSkip)

```

Get navigation menu items for an Experience Cloud site.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NavigationMenuItemCollection getCommunityNavigationMenu(String

   communityId, String navigationLinkSetId, String navigationLinkSetDeveloperName,

   ConnectApi.PublishStatus publishStatus, Boolean includeImageUrl, Boolean addHomeMenuItem,

   List<ConnectApi.NavigationMenuItemType> menuItemTypesToSkip)

```


Apex Reference Guide NavigationMenu Class

Parameters

```
   communityId
```

Type: String

ID of an Experience Cloud site.

```
   navigationLinkSetId
```

Type: String

ID of the navigation link set.

```
   navigationLinkSetDeveloperName
```

Type: String

Developer name of the navigation link set.

```
   publishStatus
```

Type: `ConnectApi.PublishStatus`

Publish status of the navigation menu item. Values are:

**•** `Draft`

**•** `Live`

```
   includeImageUrl
```

Type: Boolean

Specifies whether to include the image URL with the menu item ( `true` ) or not ( `false` ).

```
   addHomeMenuItem
```

Type: Boolean

Specifies whether to add the Home menu item ( `true` ) or not ( `false` ).

```
   menuItemTypesToSkip
```

Type: List< `ConnectApi.NavigationMenuItemType`       

List of menu item types to filter out of the results. Values are:

**•** `DataSourceDriven` —Menu items dynamically added from a data source.

**•** `Event` —Event, such as logging in, logging out, or switching accounts.

**•** `ExternalLink` —URL outside of your site.

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.

**•** `SalesforceObject` —Objects such as accounts, cases, contacts, and custom objects.

**•** `SystemLink` —System link, such as a link to Builder, Workspaces, or Setup.

Return Value

Type: `ConnectApi.NavigationMenuItemCollection`


Apex Reference Guide NavigationMenu Class

Usage

Supported navigation menu item types are:

**•** `DataSourceDriven` —Menu items dynamically added from a data source.

**•** `Event` —Event, such as logging in, logging out, or switching accounts.

**•** `ExternalLink` —URL outside of your site.

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.

**•** `SalesforceObject` —Objects such as accounts, cases, contacts, and custom objects.

**•** `SystemLink` —System link, such as a link to Builder, Workspaces, or Setup.

##### **`getCommunityNavigationMenu(communityId, navigationLinkSetId,`**

```
  navigationLinkSetDeveloperName, publishStatus, includeImageUrl,

  addHomeMenuItem, menuItemTypesToSkip, effectiveAccountId)

```

Get navigation menu items for an Experience Cloud based on an effective account.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NavigationMenuItemCollection getCommunityNavigationMenu(String

   communityId, String navigationLinkSetId, String navigationLinkSetDeveloperName,

   ConnectApi.PublishStatus publishStatus, Boolean includeImageUrl, Boolean addHomeMenuItem,

   List<ConnectApi.NavigationMenuItemType> menuItemTypesToSkip, String effectiveAccountId)

```

Parameters

```
   communityId
```

Type: String

ID of an Experience Cloud site.

```
   navigationLinkSetId
```

Type: String

ID of the navigation link set.


Apex Reference Guide NavigationMenu Class

```
   navigationLinkSetDeveloperName
```

Type: String

Developer name of the navigation link set.

```
   publishStatus
```

Type: `ConnectApi.PublishStatus`

Publish status of the navigation menu item. Values are:

**•** `Draft`

**•** `Live`

```
   includeImageUrl
```

Type: Boolean

Specifies whether to include the image URL with the menu item ( `true` ) or not ( `false` ).

```
   addHomeMenuItem
```

Type: Boolean

Specifies whether to add the Home menu item ( `true` ) or not ( `false` ).

```
   menuItemTypesToSkip
```

Type: List< `ConnectApi.NavigationMenuItemType`       

List of menu item types to filter out of the results. Values are:

**•** `DataSourceDriven` —Menu items dynamically added from a data source.

**•** `Event` —Event, such as logging in, logging out, or switching accounts.

**•** `ExternalLink` —URL outside of your site.

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.

**•** `SalesforceObject` —Objects such as accounts, cases, contacts, and custom objects.

**•** `SystemLink` —System link, such as a link to Builder, Workspaces, or Setup.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If unspecified, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.NavigationMenuItemCollection`

Usage

Supported navigation menu item types are:

**•** `DataSourceDriven` —Menu items dynamically added from a data source.

**•** `Event` —Event, such as logging in, logging out, or switching accounts.

**•** `ExternalLink` —URL outside of your site.


### Apex Reference Guide NextBestAction Class

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.

**•** `SalesforceObject` —Objects such as accounts, cases, contacts, and custom objects.

**•** `SystemLink` —System link, such as a link to Builder, Workspaces, or Setup.

### NextBestAction Class

Execute recommendation strategies, get recommendations, manage recommendation reactions.

Namespace

ConnectApi

Usage

Community users can't access this class. Portal and guest users can access strategies only through the Suggested Actions component.

#### NextBestAction Methods

### These methods are for NextBestAction . All methods are static.

IN THIS SECTION:

deleteRecommendationReaction(reactionId)
Delete a recommendation reaction.

executeStrategy(strategyName, maxResults, contextRecordId)
Execute a strategy.

executeStrategy(strategyName, maxResults, contextRecordId, debugTrace)
Execute a strategy and request a trace.

executeStrategy(strategyName, strategyInput)
Execute a strategy using an input class.

getRecommendation(recommendationId)
Get a recommendation.

getRecommendationReaction(reactionId)
Get a recommendation reaction.

getRecommendationReactions(onBehalfOfId, createdById, targetId, contextRecordId, pageParam, pageSize)
Get recommendation reactions.

setRecommendationReaction(reaction)
Record user reactions to recommendations.


Apex Reference Guide NextBestAction Class

##### **`deleteRecommendationReaction(reactionId)`**

Delete a recommendation reaction.

API Version

45.0

Requires Chatter

No

Signature

```
   public static Void deleteRecommendationReaction(String reactionId)

```

Parameters

```
   reactionId
```

Type: String

ID of the recommendation reaction or other sObject that caused the user to react.

Return Value

Type: Void

Usage

Users with the Manage Next Best Action Recommendations or Modify All Data permission can delete recommendation reactions.

##### **`executeStrategy(strategyName, maxResults, contextRecordId)`**

Execute a strategy.

API Version

45.0

Available to Guest Users

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NBARecommendations executeStrategy(String strategyName, Integer

   maxResults, String contextRecordId)

```


Apex Reference Guide NextBestAction Class

Parameters

```
   strategyName
```

Type: String

Name of the strategy.

```
   maxResults
```

Type: Integer

Maximum number of results. Valid values are from 1 to 25. The default is 3.

```
   contextRecordId
```

Type: String

ID of the context record. For example, if the next best action is on a case detail page, the ID of the case.

Return Value

Type: `ConnectApi.NBARecommendations`

##### **`executeStrategy(strategyName, maxResults, contextRecordId, debugTrace)`**

Execute a strategy and request a trace.

API Version

45.0

Available to Guest Users

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NBARecommendations executeStrategy(String strategyName, Integer

   maxResults, String contextRecordId, Boolean debugTrace)

```

Parameters

```
   strategyName
```

Type: String

Name of the strategy.

```
   maxResults
```

Type: Integer

Maximum number of results. Valid values are from 1 to 25. The default is 3.

```
   contextRecordId
```

Type: String


Apex Reference Guide NextBestAction Class

ID of the context record. For example, if the next best action is on a case detail page, the ID of the case.

```
   debugTrace
```

Type: Boolean

Specifies whether to return trace and debug information in the response ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.NBARecommendations`

##### **`executeStrategy(strategyName, strategyInput)`**

Execute a strategy using an input class.

API Version

45.0

Available to Guest Users

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NBARecommendations executeStrategy(String strategyName,

   ConnectApi.NBAStrategyInput strategyInput)

```

Parameters

```
   strategyName
```

Type: String

Name of the strategy.

```
   strategyInput
```

Type: `ConnectApi.NBAStrategyInput`

A `ConnectApi.NBAStrategyInput` body.

Return Value

Type: `ConnectApi.NBARecommendations`

##### **`getRecommendation(recommendationId)`**

Get a recommendation.


Apex Reference Guide NextBestAction Class

API Version

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Recommendation getRecommendation(String recommendationId)

```

Parameters

```
   recommendationId
```

Type: String

ID of the recommendation.

Return Value

Type: `ConnectApi.Recommendation`

##### **`getRecommendationReaction(reactionId)`**

Get a recommendation reaction.

API Version

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecommendationReaction getRecommendationReaction(String

   reactionId)

```

Parameters

```
   reactionId
```

Type: String

ID of the recommendation reaction or other sObject that caused the user to react.

Return Value

Type: `ConnectApi.RecommendationReaction`


Apex Reference Guide NextBestAction Class

Usage

Users with the Manage Next Best Action Recommendations or Modify All Data permission can get recommendation reactions.

##### **`getRecommendationReactions(onBehalfOfId, createdById, targetId,`**

```
  contextRecordId, pageParam, pageSize)

```

Get recommendation reactions.

API Version

45.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecommendationReactions getRecommendationReactions(String

   onBehalfOfId, String createdById, String targetId, String contextRecordId, Integer

   pageParam, Integer pageSize)

```

Parameters

```
   onBehalfOfId
```

Type: String

Use the ID of the user who is indirectly reacting to the recommendation to filter the results.

```
   createdById
```

Type: String

Use the ID of the user or record that created the recommendation reaction to filter the results.

```
   targetId
```

Type: String

Use the ID of the target to filter the results.

```
   contextRecordId
```

Type: String

Use the ID of a context record to filter the results.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.RecommendationReactions`


### Apex Reference Guide OmnichannelInventoryService Class

Usage

Users with the Manage Next Best Action Recommendations or Modify All Data permission can get recommendation reactions.

##### **`setRecommendationReaction(reaction)`**

Record user reactions to recommendations.

API Version

45.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecommendationReaction

   setRecommendationReaction(ConnectApi.RecommendationReactionInput reaction)

```

Parameters

```
   reaction
```

Type: `ConnectApi.RecommendationReactionInput`

A `ConnectApi.RecommendationReactionInput` object representing a reaction to a recommendation produced by a
recommendation strategy.

Return Value

Type: `ConnectApi.RecommendationReaction`

### OmnichannelInventoryService Class

Route orders to inventory locations in Order Management.

Namespace

ConnectApi

#### OmnichannelInventoryService Methods

### These methods are for OmnichannelInventoryService . All methods are static.


Apex Reference Guide OmnichannelInventoryService Class

IN THIS SECTION:

##### createReservation(createReservationInputRepresentation)

Create an inventory reservation in Omnichannel Inventory.

fulfillReservation(fulfillReservationInputRepresentation)
Fulfill one or more inventory reservations.

getInventoryAvailability(inventoryAvailabilityInputRepresentation)
Retrieve inventory availability data for one or more products at one or more inventory locations or location groups.

getInventoryAvailabilityUploadStatus(uploadId)
Retrieve the status of an inventory availability upload job.

getPublishLocationStructureStatus(uploadId)
Retrieve the status of a publish location structure job.

publishLocationStructure()
Asynchronously publish information about your inventory locations and location groups to Omnichannel Inventory. The publish
includes records whose IsEnabled and ShouldSyncWithOci fields are both _`true`_ . This method returns an ID that you can use to
retrieve the status of the publish job.

releaseReservation(releaseReservationInputRepresentation)
Release one or more existing inventory reservations to free up that inventory.

submitInventoryAvailabilityUpload(fileUpload)
Upload an inventory availability data file to Omnichannel Inventory.

transferReservation(transferReservationInputRepresentation)
Transfer one or more inventory reservations between locations or location groups. This API doesn’t change physical quantities, but
reduces the reserved quantity at the source and increases it at the destination.

updateReservation(updateReservationInputRepresentation)
Updates an existing reservation in Omnichannel Inventory. Add, remove, and update quantities for existing SKUs in the reservation.

##### **`createReservation(createReservationInputRepresentation)`**

Create an inventory reservation in Omnichannel Inventory.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OCICreateReservationOutputRepresentation

   createReservation(ConnectApi.OCICreateReservationInputRepresentation

   createReservationInputRepresentation)

```


Apex Reference Guide OmnichannelInventoryService Class

Parameters

```
   createReservationInputRepresentation
```

Type: `ConnectApi.OCICreateReservationInputRepresentation`

Data to reserve inventory at one or more Omnichannel Inventory locations or location groups.

Return Value

Type: `ConnectApi.OCICreateReservationOutputRepresentation`

##### **`fulfillReservation(fulfillReservationInputRepresentation)`**

Fulfill one or more inventory reservations.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIFulfillReservationOutputRepresentation

   fulfillReservation(ConnectApi.OCIFulfillReservationInputRepresentation

   fulfillReservationInputRepresentation)

```

Parameters

```
   fulfillReservationInputRepresentation
```

Type: `ConnectApi.OCIFulfillReservationInputRepresentation`

Wraps a list of inventory reservations to fulfill.

Return Value

Type: `ConnectApi.OCIFulfillReservationOutputRepresentation`

##### **`getInventoryAvailability(inventoryAvailabilityInputRepresentation)`**

Retrieve inventory availability data for one or more products at one or more inventory locations or location groups.

API Version

51.0

Requires Chatter

No


Apex Reference Guide OmnichannelInventoryService Class

Signature

```
   public static ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation

   getInventoryAvailability(ConnectApi.OCIGetInventoryAvailabilityInputRepresentation

   inventoryAvailabilityInputRepresentation)

```

Parameters

```
   inventoryAvailabilityInputRepresentation
```

Type: `ConnectApi.OCIGetInventoryAvailabilityInputRepresentation`

Details of a request to retrieve inventory availability.

Return Value

Type: `ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation`

##### **`getInventoryAvailabilityUploadStatus(uploadId)`**

Retrieve the status of an inventory availability upload job.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIUploadInventoryAvailabilityStatusOutputRepresentation

   getInventoryAvailabilityUploadStatus(String uploadId)

```

Parameters

```
   uploadId
```

Type: String

The upload ID of the upload job.

Return Value

Type: `ConnectApi.OCIUploadInventoryAvailabilityStatusOutputRepresentation`

##### **`getPublishLocationStructureStatus(uploadId)`**

Retrieve the status of a publish location structure job.

API Version

51.0


Apex Reference Guide OmnichannelInventoryService Class

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIPublishLocationStructureStatusOutputRepresentation

   getPublishLocationStructureStatus(String uploadId)

```

Parameters

```
   uploadId
```

Type: String

The upload ID of the publish job.

Return Value

Type: `ConnectApi.OCIPublishLocationStructureStatusOutputRepresentation`

##### **`publishLocationStructure()`**

Asynchronously publish information about your inventory locations and location groups to Omnichannel Inventory. The publish includes
records whose IsEnabled and ShouldSyncWithOci fields are both _`true`_ . This method returns an ID that you can use to retrieve the status
of the publish job.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIPublishLocationStructureOutputRepresentation

##### `publishLocationStructure()`

```

Return Value

Type: `ConnectApi.OCIPublishLocationStructureOutputRepresentation`

##### **`releaseReservation(releaseReservationInputRepresentation)`**

Release one or more existing inventory reservations to free up that inventory.

API Version

51.0


Apex Reference Guide OmnichannelInventoryService Class

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIReleaseReservationOutputRepresentation

   releaseReservation(ConnectApi.OCIReleaseReservationInputRepresentation

   releaseReservationInputRepresentation)

```

Parameters

```
   releaseReservationInputRepresentation
```

Type: `ConnectApi.OCIReleaseReservationInputRepresentation`

Details of one or more inventory reservations to release.

Return Value

Type: `ConnectApi.OCIReleaseReservationOutputRepresentation`

##### **`submitInventoryAvailabilityUpload(fileUpload)`**

Upload an inventory availability data file to Omnichannel Inventory.

API Version

51.0 (NDJSON), 63.0 (CSV)

Requires Chatter

No

Signature

```
   public static ConnectApi.OCIUploadInventoryAvailabilityOutputRepresentation

   submitInventoryAvailabilityUpload(ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

NDJSON or CSV file containing inventory availability data.

Return Value

Type: `ConnectApi.OCIUploadInventoryAvailabilityOutputRepresentation`

Usage

To create an inventory data file, format the data as a series of NDJSON or CSV entries that represent locations and individual inventory
records.


Apex Reference Guide OmnichannelInventoryService Class

Inventory Import Data Considerations:

**•** Separate the top-level entries with line feeds, not commas. Each entry must be on a single line.

**•** When the system reads a location entry, it assigns the subsequent inventory entries to that location until it reads another location
entry.

**•** Legacy NDJSON requires that you specify a header record for each location entry
( `{"location":"wickenburg","mode":"UPDATE"}` ). The header isn’t required for a high-performance NDJSON layout
or CSV file.

**•** Each inventory record entry requires a unique recordId. Best practice is to use a UUID. The recordId protects against importing
duplicate data. The recordId is provided in NDJSON and automatically generated for CSV.

**•** Each inventory record entry requires an effectiveDate.

**•** If provided, each futures entry requires a nonzero quantity and a future expectedDate.

Note: The file must be in NDJSON or CSV format. For larger collections, use the Commerce API or split the data into multiple files.
The Commerce API accepts GZIP, NDJSON, or CSV files up to 100 MB.

This example illustrates the data format:

Note: For readability, this example shows the first few entries on multiple lines. In the import file, each location and inventory
record entry must be on a single line.

```
   {

     "location":"Warehouse-A", // location identifier

    "mode":"UPDATE" // must be UPDATE (other operations might be available in future releases)

   }

   {

    "recordId":"0a87539d-f3dd-47bc-91c7-9c752e39dbe0", // unique identifier for the inventory

    record

     "onHand":10,

     "sku":"12389156",

     "effectiveDate":"2020-12-08T14:05:22.790896-07:00",

     "futures":[ // list of future restocks

      {

      "quantity":1,

      "expectedDate":"2021-04-18T14:05:22.781-07:00"

      },

      {

      "quantity":5,

      "expectedDate":"2021-05-18T14:05:22.781-07:00"

      }

     ],

     "safetyStockCount":0

   }

   {

     "recordId":"0a87539d-f3dd-47bc-91c7-9c752e312345",

     "onHand":10,

     "sku":"9485728",

     "effectiveDate":"2020-12-08T14:05:22.790896-07:00",

     "futures":[

      {

      "quantity":10,

      "expectedDate":"2021-04-18T14:05:22.781-07:00"

      }

     ],

```


Apex Reference Guide OmnichannelInventoryService Class

```
     "safetyStockCount":0

   }

   {"location":"Warehouse-B","mode":"UPDATE"}

   {"recordId":"0a87539d-f3dd-47bc-91c7-9c75abc123de","onHand":10,"sku":"12389156","effectiveDate":"2020-12-08T14:05:22.790896-07:00","futures":[{"quantity":1,"expectedDate":"2021-04-18T14:05:22.781-07:00"}],"safetyStockCount":0}

   {"recordId":"0a87539d-f3dd-47bc-91c7-9c75abc98765","onHand":10,"sku":"93867201","effectiveDate":"2020-12-08T14:05:22.790896-07:00","futures":[{"quantity":5,"expectedDate":"2021-04-18T14:05:22.781-07:00"}],"safetyStockCount":0}

##### **`transferReservation(transferReservationInputRepresentation)`**

```

Transfer one or more inventory reservations between locations or location groups. This API doesn’t change physical quantities, but
reduces the reserved quantity at the source and increases it at the destination.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OCITransferReservationOutputRepresentation

   transferReservation(ConnectApi.OCITransferReservationInputRepresentation

   transferReservationInputRepresentation)

```

Parameters

```
   transferReservationInputRepresentation
```

Type: `ConnectApi.OCITransferReservationInputRepresentation`

Wraps a list of inventory reservation transfers and specifies whether a single failure cancels the entire list.

Return Value

Type: `ConnectApi.OCITransferReservationOutputRepresentation`

##### **`updateReservation(updateReservationInputRepresentation)`**

Updates an existing reservation in Omnichannel Inventory. Add, remove, and update quantities for existing SKUs in the reservation.

API Version

61.0

Requires Chatter

No


### Apex Reference Guide OMSAnalytics Class

Signature

```
   public static ConnectApi.OCIUpdateReservationOutputRepresentation

   updateReservation(ConnectApi.OCIUpdateReservationInputRepresentation

   updateReservationInputRepresentation)

```

Parameters

```
   updateReservationInputRepresentation
```

Type: ConnectApi.OCIUpdateReservationInputRepresentation on page 2081

Data to update one or more Omnichannel Inventory item reservations.

Return Value

Type: ConnectApi.OCIUpdateReservationOutputRepresentation on page 2422

### OMSAnalytics Class

Get products with return rates, get text classified into different classifications using text analysis, and capture the return reasons from
external sources based on the product ids.

Namespace

ConnectApi

IN THIS SECTION:

### OMSAnalytics Class These methods are for OMSAnalytics . All methods are static. OMSAnalytics Class These methods are for OMSAnalytics . All methods are static.

Namespace

ConnectApi

IN THIS SECTION:

getTextClassificationsBulkResults(ids)
Gets text classification results for request IDs.

productsExpand(scope, products, expand)
Fetches expanded details of a product that aren’t found in the sObject. The expanded variable fields, such as return reasons, are
added as output. This method supports an extensibility framework that lets the context user override the existing implementation
so they can fetch the data from third-party apps. The application doesn’t require two separate APIs to get return reasons.

productsReturnRate(pageParam, pageSize)
Gets pages of data showing the return rates of products that are calculated by the Customer Data Platform. Return data is paginated
in descending order.


Apex Reference Guide OMSAnalytics Class

productsReturnRate(pageParam, pageSize)
Get a page of products and their return rates.

productsReturnRate(pageParam, pageSize, products)
Get a page of products and their return rates for a list of product IDs.

submitTextClassificationsRequest(textClassificationsRequestInput, llmType)
Submits a text classification request to Einstein

##### **`getTextClassificationsBulkResults(ids)`**

Gets text classification results for request IDs.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TextClassificationsBulkResultsOutputRepresentation

   getTextClassificationsBulkResults(List<String> ids)

```

Parameters

```
   ids
```

Type: List(String)

List of request IDs.

Return Value

Type: `ConnectApi.TextClassificationsBulkResultsOutputRepresentation`

Example

```
   List <String> requestIds = new List <String> ();

        requestIds.add(requestId);

        ConnectApi.TextClassificationsBulkResultsOutputRepresentation output =

   ConnectApi.OMSAnalytics.getTextClassificationsBulkResults(requestIds);

##### **`productsExpand(scope, products, expand)`**

```

Fetches expanded details of a product that aren’t found in the sObject. The expanded variable fields, such as return reasons, are added
as output. This method supports an extensibility framework that lets the context user override the existing implementation so they can
fetch the data from third-party apps. The application doesn’t require two separate APIs to get return reasons.


Apex Reference Guide OMSAnalytics Class

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductsListOutputRepresentation productsExpand(String scope,

   List<String> products, List<ConnectApi.ProductExpandType> expand)

```

Parameters

```
   scope
```

Type: String

The scope for the extensibility framework. Requires a web store ID.

##### _`products`_

Type: List )String)

A list of IDs to fetch details for.

```
   expand
```

Type: List )String)

Output representation for expand feature.

Return Value

Type: `ConnectApi.ProductsListOutputRepresentation`

Example

```
   String scope = 'webstoreId eq ' + ws.Id;

        ConnectApi.ProductsListOutputRepresentation output =

   ConnectApi.OMSAnalytics.productsExpand(scope, productIds, new List

   <ConnectApi.ProductExpandType> {

        ConnectApi.ProductExpandType.ReturnReasons

        });

##### **`productsReturnRate(pageParam, pageSize)`**

```

Gets pages of data showing the return rates of products that are calculated by the Customer Data Platform. Return data is paginated in
descending order.

API Version

59.0


Apex Reference Guide OMSAnalytics Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductReturnRateListOutputRepresentation

   productsReturnRate(Integer pageParam, Integer pageSize)

```

Parameters

```
   page
```

Type: String

The page number for the list of products. Starts at 0.

##### _`products`_

Type: List )String)

A list of IDs to fetch details for.

```
   pageSize
```

Type: List )Integer)

The number of products that are returned on each page.

Return Value

Type: ConnectApi.ProductReturnRateListOutputRepresentation

Example

```
   ConnectApi.ProductReturnRateListOutputRepresentation output =

   ConnectApi.OMSAnalytics.productsReturnRate(page, pageSize);

##### **`productsReturnRate(pageParam, pageSize)`**

```

Get a page of products and their return rates.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductReturnRateListOutputRepresentation

   productsReturnRate(Integer pageParam, Integer pageSize)

```


Apex Reference Guide OMSAnalytics Class

Parameters

```
   pageParam
```

Type: Integer

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ProductReturnRateListOutputRepresentation`

##### **`productsReturnRate(pageParam, pageSize, products)`**

Get a page of products and their return rates for a list of product IDs.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductReturnRateListOutputRepresentation

   productsReturnRate(Integer pageParam, Integer pageSize, List<String> products)

```

Parameters

```
   pageParam
```

Type: Integer

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

##### _`products`_

Type: List<String>

List of product IDs.

Return Value

Type: `ConnectApi.ProductReturnRateListOutputRepresentation`


### Apex Reference Guide Orchestration Class

##### **`submitTextClassificationsRequest(textClassificationsRequestInput, llmType)`**

Submits a text classification request to Einstein

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TextClassificationsOutputRepresentation

   submitTextClassificationsRequest(ConnectApi.TextClassificationsInputRepresentation

   textClassificationsRequestInput, String llmType)

```

Parameters

```
   textClassificationsRequestInput
```

Type: ConnectApi.TextClassificationsInputRepresentation

Text classification containing a list of text strings and classifiers. Each text string is classified into classifiers based on analysis.

```
   llmType
```

Type: List )String)

The large language model that’s used for analysis. Supports Open AI only.

Return Value

Type: ConnectApi.TextClassificationsOutputRepresentation

Example

```
   ConnectApi.TextClassificationsInputRepresentation textClassificationsInputRepresentation

   = new ConnectApi.TextClassificationsInputRepresentation();

   textClassificationsInputRepresentation.textList = textList;

   textClassificationsInputRepresentation.classifiers = classifiers;

   List < String > requestIds = new List < String > ();

### Orchestration Class

```

Get orchestration instances.

Namespace

ConnectApi


Apex Reference Guide Orchestration Class

#### Orchestration Methods These methods are for Orchestration . All methods are static.

IN THIS SECTION:

##### getOrchestrationInstance(instanceId)

Get an orchestration instance associated with an orchestration instance ID.

##### getOrchestrationInstanceCollection(relatedRecordId)

Get orchestration instances associated with a Salesforce record that’s configured as a context record for orchestration interactive
steps.

getOrchestrationInstanceCollection(relatedRecordId, relatedOrchestrationId)
Get orchestration instances associated with either a Salesforce record or an orchestration that’s configured as context for orchestration
interactive steps.

##### **`getOrchestrationInstance(instanceId)`**

Get an orchestration instance associated with an orchestration instance ID.

API Version

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrchestrationInstance getOrchestrationInstance(String

   instanceId)

```

Parameters

```
   instanceId
```

Type: String

The ID of orchestration instance to get details for.

Return Value

Type: `ConnectApi.OrchestrationInstance`

##### **`getOrchestrationInstanceCollection(relatedRecordId)`**

Get orchestration instances associated with a Salesforce record that’s configured as a context record for orchestration interactive steps.

API Version

54.0


Apex Reference Guide Orchestration Class

Requires Chatter

No

Signature

```
   public static ConnectApi.OrchestrationInstanceCollection

   getOrchestrationInstanceCollection(String relatedRecordId)

```

Parameters

```
   relatedRecordId
```

Type: String

The ID of a record configured as a context record for orchestration interactive steps.

Return Value

Type: `ConnectApi.OrchestrationInstanceCollection`

##### **`getOrchestrationInstanceCollection(relatedRecordId, relatedOrchestrationId)`**

Get orchestration instances associated with either a Salesforce record or an orchestration that’s configured as context for orchestration
interactive steps.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrchestrationInstanceCollection

   getOrchestrationInstanceCollection(String relatedRecordId, String relatedOrchestrationId)

```

Parameters

```
   relatedRecordId
```

Type: String

The ID of a record configured as a context record for orchestration interactive steps. You must specify either _`relatedRecordId`_
or _`relatedOrchestrationId`_ .

```
   relatedOrchestrationId
```

Type: String

The ID of an orchestration configured as context for orchestration interactive steps. You must specify either _`relatedRecordId`_
or _`relatedOrchestrationId`_ .


### Apex Reference Guide OrderPaymentSummary Class

Return Value

Type: `ConnectApi.OrchestrationInstanceCollection`

### OrderPaymentSummary Class

Work with payments in Order Management.

Namespace

ConnectApi

#### OrderPaymentSummary Methods

### These methods are for OrderPaymentSummary . All methods are static.

IN THIS SECTION:

##### createOrderPaymentSummary(orderPaymentSummaryInput)

Create an OrderPaymentSummary for an OrderSummary. Specify a payment authorization or payments that share the same payment
method. In an org with the multicurrency feature enabled, the OrderPaymentSummary inherits the CurrencyIsoCode value from the
OrderSummary.

##### **`createOrderPaymentSummary(orderPaymentSummaryInput)`**

Create an OrderPaymentSummary for an OrderSummary. Specify a payment authorization or payments that share the same payment
method. In an org with the multicurrency feature enabled, the OrderPaymentSummary inherits the CurrencyIsoCode value from the
OrderSummary.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CreateOrderPaymentSummaryOutputRepresentation

   createOrderPaymentSummary(ConnectApi.CreateOrderPaymentSummaryInputRepresentation

   orderPaymentSummaryInput)

```

Parameters

```
   orderPaymentSummaryInput
```

Type: `ConnectApi.CreateOrderPaymentSummaryInputRepresentation`

The OrderSummary and payment authorization or payments.


### Apex Reference Guide OrderSummary Class

Return Value

Type: `ConnectApi.CreateOrderPaymentSummaryOutputRepresentation`

Example

```
   String orderSummaryId = '1Osxx0000004CCG';

   String paymentId1 = '0a3xx0000000085AAA';

   String paymentId2 = '0a3xx0000000085BBB';

   ConnectApi.CreateOrderPaymentSummaryInputRepresentation orderPaymentSummaryInput = new

   ConnectApi.CreateOrderPaymentSummaryInputRepresentation();

   orderPaymentSummaryInput.orderSummaryId = orderSummaryId;

   List<String> paymentList = new List<String>();

   paymentList.add(paymentId1);

   paymentList.add(paymentId2);

   orderPaymentSummaryInput.paymentIds = paymentList;

   ConnectApi.CreateOrderPaymentSummaryOutputRepresentation result =

   ConnectApi.OrderPaymentSummary.createOrderPaymentSummary(orderPaymentSummaryInput);

### OrderSummary Class

```

Work with orders in Order Management.

Namespace

ConnectApi

#### OrderSummary Methods

### These methods are for OrderSummary . All methods are static.

IN THIS SECTION:

adjustPreview(orderSummaryId, adjustInput)
Retrieve the expected results of adjusting the price of one or more OrderItemSummaries from an OrderSummary, without actually
executing the adjustment. The response data contains the financial changes that would result from submitting the proposed
adjustment.

adjustSubmit(orderSummaryId, adjustInput)
Adjust the price of one or more OrderItemSummaries from an OrderSummary, and create corresponding change orders.

createCreditMemo(orderSummaryId, creditMemoInput)
Create a credit memo to represent the refund for one or more change orders associated with an OrderSummary.

createMultipleInvoices(invoicesInput)
Create Invoices to represent the charges for one or more change orders. Create Invoices for change orders that increase order
amounts, such as for return fees. When you ensure the refund for a return, include the invoices for any associated return fees in the
request.


Apex Reference Guide OrderSummary Class

ensureFundsAsync(orderSummaryId, ensureFundsInput)
Ensure funds for an Invoice and apply them to it and optional define a sequence to capture payments in. If needed, capture authorized
funds by sending a request to a payment provider. This method inserts a background operation into an asynchronous job queue
and returns the ID of that operation so you can track its status. Payment gateway responses appear in the payment gateway log and
do not affect the background operation status.

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)
Ensure refunds for a CreditMemo or excess funds by sending a request to a payment provider. This method inserts a background
operation into an asynchronous job queue and returns the ID of that operation so you can track its status. Payment gateway responses
appear in the payment gateway log and don’t affect the background operation status.

multipleEnsureFundsAsync(multipleEnsureFundsInput)
Ensure and apply funds for one or more Invoices. If needed, capture authorized funds by sending a request to a payment provider.
This method inserts a background operation into an asynchronous job queue and returns the ID of that operation so you can track
its status. Payment gateway responses appear in the payment gateway log and do not affect the background operation status.

previewCancel(orderSummaryId, changeInput)
Retrieve the expected change order values for canceling one or more OrderItemSummaries from an OrderSummary, without actually
executing the cancel.

previewReturn(orderSummaryId, changeInput)
Retrieve the expected change order values for a simple return of one or more OrderItemSummaries from an OrderSummary, without
actually executing the return.

submitCancel(orderSummaryId, changeInput)
Cancel one or more OrderItemSummaries from an OrderSummary, and create a corresponding change order.

submitReturn(orderSummaryId, changeInput)
Return one or more OrderItemSummaries from an OrderSummary, and create a corresponding change order. This return is a simple
return that creates a change order but not a ReturnOrder.

##### **`adjustPreview(orderSummaryId, adjustInput)`**

Retrieve the expected results of adjusting the price of one or more OrderItemSummaries from an OrderSummary, without actually
executing the adjustment. The response data contains the financial changes that would result from submitting the proposed adjustment.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.AdjustOrderSummaryOutputRepresentation adjustPreview(String

   orderSummaryId, ConnectApi.AdjustOrderItemSummaryInputRepresentation adjustInput)

```

Parameters

```
   orderSummaryId
```

Type: String


Apex Reference Guide OrderSummary Class

ID of the OrderSummary.

```
   adjustInput
```

Type: `ConnectApi.AdjustOrderItemSummaryInputRepresentation`

Price adjustments to order item summaries that together make up a price adjustment to an order, with options for adjusting items
in the process of being fulfilled.

Return Value

Type: `ConnectApi.AdjustOrderSummaryOutputRepresentation`

Usage

When a price adjustment is applied to an OrderItemSummary, its quantities are considered in three groups:

**Pre-fulfillment**
QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**In-fulfillment**
QuantityAllocated - QuantityFulfilled

**Post-fulfillment**
QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the _`allocatedItemsChangeOrderType`_
input property:

**•** Distribute the adjustment evenly between pre-fulfillment and post-fulfillment quantities. Ignore in-fulfillment quantities. Submitting
the adjustment would create one change order for the adjustments to pre-fulfillment quantities and one change order for the
adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Submitting the adjustment
would create one change order for the adjustments to both pre-fulfillment and in-fulfillment quantities, and one change order for
the adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Submitting the adjustment
would create one change order for the adjustments to pre-fulfillment quantities, one change order for the adjustments to in-fulfillment
quantities, and one change order for the adjustments to post-fulfillment quantities.

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

##### adjustSubmit(orderSummaryId, adjustInput) **`adjustSubmit(orderSummaryId, adjustInput)`**

Adjust the price of one or more OrderItemSummaries from an OrderSummary, and create corresponding change orders.

API Version

49.0


Apex Reference Guide OrderSummary Class

Requires Chatter

No

Signature

```
   public static ConnectApi.AdjustOrderSummaryOutputRepresentation adjustSubmit(String

   orderSummaryId, ConnectApi.AdjustOrderItemSummaryInputRepresentation adjustInput)

```

Parameters

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   adjustInput
```

Type: `ConnectApi.AdjustOrderItemSummaryInputRepresentation`

Price adjustments to order item summaries that together make up a price adjustment to an order, with options for adjusting items
in the process of being fulfilled.

Return Value

Type: `ConnectApi.AdjustOrderSummaryOutputRepresentation`

Usage

When a price adjustment is applied to an OrderItemSummary, its quantities are considered in three groups:

**Pre-fulfillment**
QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**In-fulfillment**
QuantityAllocated - QuantityFulfilled

**Post-fulfillment**
QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the _`allocatedItemsChangeOrderType`_
input property:

**•** Distribute the adjustment evenly between pre-fulfillment and post-fulfillment quantities. Ignore in-fulfillment quantities. Create one
change order for the adjustments to pre-fulfillment quantities and one change order for the adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to both pre-fulfillment and in-fulfillment quantities, and one change order for the adjustments to post-fulfillment
quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to pre-fulfillment quantities, one change order for the adjustments to in-fulfillment quantities, and one change
order for the adjustments to post-fulfillment quantities.

After submitting a price adjustment, process refunds as appropriate:

**•** If the discount only applied to OrderItemSummaries for which payment hasn’t been captured, it doesn’t require a refund. This
situation normally applies to OrderItemSummaries in the US that haven’t been fulfilled.


Apex Reference Guide OrderSummary Class

**•** If the discount applied to OrderItemSummaries that haven’t been fulfilled and for which payment has been captured, process a
refund. In this case, pass the _`totalExcessFundsAmount`_ from the output representation to the `ensureRefundsAsync()`
method.

**•** If the discount applied to OrderItemSummaries that have been fulfilled, process a refund. Pass the
_`postFulfillmentChangeOrderId`_ from the output representation to the `createCreditMemo()` method, then pass
the CreditMemo to the `ensureRefundsAsync()` method.

**•** If the discount applied to both fulfilled and unfulfilled OrderItemSummaries for which payment has been captured, process both
refunds. Pass the _`postFulfillmentChangeOrderId`_ from the output representation to the `createCreditMemo()`
method, then pass the credit memo and the _`totalExcessFundsAmount`_ from the output representation to the
`ensureRefundsAsync()` method.

SEE ALSO:

##### createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

adjustPreview(orderSummaryId, adjustInput)

##### **`createCreditMemo(orderSummaryId, creditMemoInput)`**

Create a credit memo to represent the refund for one or more change orders associated with an OrderSummary.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CreateCreditMemoOutputRepresentation createCreditMemo(String

   orderSummaryId, ConnectApi.CreateCreditMemoInputRepresentation creditMemoInput)

```

Parameters

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   creditMemoInput
```

Type: `ConnectApi.CreateCreditMemoInputRepresentation`

The list of change order IDs.

Return Value

Type: `ConnectApi.CreateCreditMemoOutputRepresentation`


Apex Reference Guide OrderSummary Class

##### **`createMultipleInvoices(invoicesInput)`**

Create Invoices to represent the charges for one or more change orders. Create Invoices for change orders that increase order amounts,
such as for return fees. When you ensure the refund for a return, include the invoices for any associated return fees in the request.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CreateMultipleInvoicesFromChangeOrdersOutputRepresentation

   createMultipleInvoices(ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation

   invoicesInput)

```

Parameters

```
   invoicesInput
```

Type: `ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation`

Data about the change orders to create Invoices for.

Return Value

Type: `ConnectApi.CreateMultipleInvoicesFromChangeOrdersOutputRepresentation`

SEE ALSO:

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

createReturnOrder(returnOrderInput)

returnItems(returnOrderId, returnItemsInput)

##### **`ensureFundsAsync(orderSummaryId, ensureFundsInput)`**

Ensure funds for an Invoice and apply them to it and optional define a sequence to capture payments in. If needed, capture authorized
funds by sending a request to a payment provider. This method inserts a background operation into an asynchronous job queue and
returns the ID of that operation so you can track its status. Payment gateway responses appear in the payment gateway log and do not
affect the background operation status.

API Version

48.0

Requires Chatter

No


Apex Reference Guide OrderSummary Class

Signature

```
   public static ConnectApi.EnsureFundsAsyncOutputRepresentation ensureFundsAsync(String

   orderSummaryId, ConnectApi.EnsureFundsAsyncInputRepresentation ensureFundsInput)

```

Parameters

```
   isConsiderReservedBalanceAmount
```

Type: Boolean

If true, the reserved balance amount is used for the Order Summary to fund the invoice. If not enough reserved balance amount,
any available balance that isn’t reserved by another Order Summary is used. If false, any available balance is used.

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   ensureFundsInput
```

Type: `ConnectApi.EnsureFundsAsyncInputRepresentation`

The ID of the Invoice. If multiple payments are allowed, you can also specify a sequence to capture payments for the invoice.

Return Value

Type: `ConnectApi.EnsureFundsAsyncOutputRepresentation`

Usage

This method checks the OrderPaymentSummaries associated with the specified OrderSummary for funds to apply to the Invoice balance
following this logic:

Note: If multiple OrderPaymentSummaries have equal `BalanceAmount` values, their order of selection is random.

**1.** Verify that the Invoice balance doesn’t exceed the total `BalanceAmount` of all the OrderPaymentSummaries associated with
the OrderSummary.

**2.** If an OrderPaymentSummary has a `BalanceAmount` equal to the Invoice balance, apply the funds from that
OrderPaymentSummary.

**3.** If no exact match was found, apply funds from the OrderPaymentSummary with the largest `BalanceAmount` .

**4.** If the Invoice still has a balance to ensure, repeat steps 2 and 3 until the full balance is ensured or no captured funds remain.

**5.** If the Invoice still has a balance, look for an OrderPaymentSummary with an authorized amount equal to the remaining Invoice
balance. If one exists, capture and apply the funds from that OrderPaymentSummary.

**6.** If no exact match was found, capture and apply funds from the OrderPaymentSummary with the largest authorized amount.

**7.** If the Invoice still has a balance to ensure, repeat steps 5 and 6 until the full balance is ensured.

Note: If the method creates a payment, the payment record’s ClientContext value isn’t predictable. Don't use it in custom logic.

SEE ALSO:

multipleEnsureFundsAsync(multipleEnsureFundsInput)


Apex Reference Guide OrderSummary Class

##### **`ensureRefundsAsync(orderSummaryId, ensureRefundsInput)`**

Ensure refunds for a CreditMemo or excess funds by sending a request to a payment provider. This method inserts a background operation
into an asynchronous job queue and returns the ID of that operation so you can track its status. Payment gateway responses appear in
the payment gateway log and don’t affect the background operation status.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.EnsureRefundsAsyncOutputRepresentation ensureRefundsAsync(String

   orderSummaryId, ConnectApi.EnsureRefundsAsyncInputRepresentation ensureRefundsInput)

```

Parameters

```
   isConsiderReservedBalanceAmount
```

Type: Boolean

If true, the refundable amount is used to open the payment balance for the reservedBalanceAmount in the Order Payment Summaries.
The remaining refundable amount considers the sequence of order payment summaries, if provided. If false, any reserved balance
amount for exchanges is refunded.

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   ensureRefundsInput
```

Type: `ConnectApi.EnsureRefundsAsyncInputRepresentation`

ID of a credit memo to ensure refunds for, an amount of excess funds to refund, or both. At least one is required. Also includes any
invoices for fees that reduce the refund amount, such as return fees. If multiple payment methods are available, you can specify how
to distribute the refund.

Return Value

Type: `ConnectApi.EnsureRefundsAsyncOutputRepresentation`

Usage

This method applies the refund to the OrderPaymentSummaries associated with the specified OrderSummary following this logic.

Note: If multiple OrderPaymentSummaries have equal `AvailableToRefund` amounts, their order of selection is random.

**1.** Verify that the CreditMemo balance and excess funds amount don't exceed the total `AvailableToRefund` amount of all the
OrderPaymentSummaries associated with the OrderSummary.

**2.** If `sequences` is specified, follow these steps.

**a.** Traverse the `sequences` list in order and apply the specified refund amounts to the specified OrderPaymentSummaries.


Apex Reference Guide OrderSummary Class

**b.** If the specified CreditMemo and excess funds are fully refunded, or if `isAllowPartial` is true, then the action stops here.

**3.** If a CreditMemo is specified, follow these steps.

**a.** If an OrderPaymentSummary has an `AvailableToRefund` amount matching the CreditMemo’s remaining balance, apply
the refund to that payment.

**b.** If no exact match was found but one or more OrderPaymentSummary has a large enough `AvailableToRefund` amount
to cover the balance, use the OrderPaymentSummary with the smallest `AvailableToRefund` amount.

**c.** If no single OrderPaymentSummary has a large enough `AvailableToRefund` amount, use multiple OrderPaymentSummaries
in descending order of `AvailableToRefund` amount. This ensures the fewest OrderPaymentSummaries are used.

**4.** If only one OrderPaymentSummary is specified but has multiple payments, follow these steps.

**a.** If a payment has an amount matching the CreditMemo’s remaining balance, apply the refund to that payment.

**b.** If no exact match was found but one or more payment has a large enough amount to cover the balance, use the payment with
the smallest amount.

**c.** If no single payment has a large enough amount, use multiple payments in descending order of amount. This ensures the fewest
payments are used.

**5.** If an excess funds amount is specified, follow these steps.

**a.** Examine those OrderPaymentSummaries. If one has an `AvailableToRefund` amount matching the excess funds amount,
apply the refund to that OrderPaymentSummary.

**b.** If no exact match was found but one or more OrderPaymentSummary has a large enough `AvailableToRefund` amount
to cover the balance, use the OrderPaymentSummary with the smallest `AvailableToRefund` amount.

**c.** If no single OrderPaymentSummary has a large enough `AvailableToRefund` amount, use multiple OrderPaymentSummaries
in descending order of `AvailableToRefund` amount. This ensures the fewest OrderPaymentSummaries are used.

Note: If the method creates a refund, the refund record’s ClientContext value isn’t predictable. Don't use it in custom logic.

SEE ALSO:

createReturnOrder(returnOrderInput)

returnItems(returnOrderId, returnItemsInput)

createMultipleInvoices(invoicesInput)

##### **`multipleEnsureFundsAsync(multipleEnsureFundsInput)`**

Ensure and apply funds for one or more Invoices. If needed, capture authorized funds by sending a request to a payment provider. This
method inserts a background operation into an asynchronous job queue and returns the ID of that operation so you can track its status.
Payment gateway responses appear in the payment gateway log and do not affect the background operation status.

API Version

56.0

Requires Chatter

No


Apex Reference Guide OrderSummary Class

Signature

```
   public static ConnectApi.MultipleAsyncOutputRepresentation

   multipleEnsureFundsAsync(ConnectApi.MultipleEnsureFundsAsyncInputRepresentation

   multipleEnsureFundsInput)

```

Parameters

```
   multipleEnsureFundsInput
```

Type: `ConnectApi.MultipleEnsureFundsAsyncInputRepresentation`

List of Invoices and the associated OrderSummaries.

Return Value

Type: `ConnectApi.MultipleAsyncOutputRepresentation`

Usage

For each Invoice in the request, this method checks the OrderPaymentSummaries associated with the specified OrderSummary for funds
to apply to the Invoice balance following this logic.

Note: If multiple OrderPaymentSummaries have equal `BalanceAmount` values, their order of selection is random.

**1.** Verify that the Invoice balance doesn’t exceed the total `BalanceAmount` of all the OrderPaymentSummaries associated with
the OrderSummary.

**2.** If an OrderPaymentSummary has a `BalanceAmount` equal to the invoice balance, apply the funds from that
OrderPaymentSummary.

**3.** If no exact match was found, apply funds from the OrderPaymentSummary with the largest `BalanceAmount` .

**4.** If the Invoice still has a balance to ensure, repeat steps 2 and 3 until the full balance is ensured or no captured funds remain.

**5.** If the Invoice still has a balance, look for an OrderPaymentSummary with an authorized amount equal to the remaining Invoice
balance. If one exists, capture and apply the funds from that OrderPaymentSummary.

**6.** If no exact match was found, capture and apply funds from the OrderPaymentSummary with the largest authorized amount.

**7.** If the Invoice still has a balance to ensure, repeat steps 5 and 6 until the full balance is ensured.

Note: If the method creates a payment, the payment record’s ClientContext value isn’t predictable. Don't use it in custom logic.

SEE ALSO:

ensureFundsAsync(orderSummaryId, ensureFundsInput)

##### **`previewCancel(orderSummaryId, changeInput)`**

Retrieve the expected change order values for canceling one or more OrderItemSummaries from an OrderSummary, without actually
executing the cancel.

API Version

48.0


Apex Reference Guide OrderSummary Class

Requires Chatter

No

Signature

```
   public static ConnectApi.PreviewCancelOutputRepresentation previewCancel(String

   orderSummaryId, ConnectApi.ChangeInputRepresentation changeInput)

```

Parameters

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   changeInput
```

Type: `ConnectApi.ChangeInputRepresentation`

A list of changes to OrderItemSummaries that make up an order change, such as a cancel or return.

Return Value

Type: `ConnectApi.PreviewCancelOutputRepresentation`

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

submitCancel(orderSummaryId, changeInput)

##### **`previewReturn(orderSummaryId, changeInput)`**

Retrieve the expected change order values for a simple return of one or more OrderItemSummaries from an OrderSummary, without
actually executing the return.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PreviewReturnOutputRepresentation previewReturn(String

   orderSummaryId, ConnectApi.ChangeInputRepresentation changeInput)

```

Parameters

```
   orderSummaryId
```

Type: String


Apex Reference Guide OrderSummary Class

ID of the OrderSummary.

```
   changeInput
```

Type: `ConnectApi.ChangeInputRepresentation`

A list of changes to OrderItemSummaries that make up an order change, such as a cancel or return.

Return Value

Type: `ConnectApi.PreviewReturnOutputRepresentation`

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

submitReturn(orderSummaryId, changeInput)

##### **`submitCancel(orderSummaryId, changeInput)`**

Cancel one or more OrderItemSummaries from an OrderSummary, and create a corresponding change order.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SubmitCancelOutputRepresentation submitCancel(String

   orderSummaryId, ConnectApi.ChangeInputRepresentation changeInput)

```

Parameters

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   changeInput
```

Type: `ConnectApi.ChangeInputRepresentation`

A list of changes to OrderItemSummaries that make up an order change, such as a cancel or return.


Apex Reference Guide OrderSummary Class

Return Value

Type: `ConnectApi.SubmitCancelOutputRepresentation`

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

previewCancel(orderSummaryId, changeInput)

##### **`submitReturn(orderSummaryId, changeInput)`**

Return one or more OrderItemSummaries from an OrderSummary, and create a corresponding change order. This return is a simple
return that creates a change order but not a ReturnOrder.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SubmitReturnOutputRepresentation submitReturn(String

   orderSummaryId, ConnectApi.ChangeInputRepresentation changeInput)

```

Parameters

```
   orderSummaryId
```

Type: String

ID of the OrderSummary.

```
   changeInput
```

Type: `ConnectApi.ChangeInputRepresentation`

A list of changes to OrderItemSummaries that make up an order change, such as a cancel or return.

Return Value

Type: `ConnectApi.SubmitReturnOutputRepresentation`


### Apex Reference Guide OrderSummaryCreation Class

Usage

After submitting a return, process a refund. Pass the _`changeOrderId`_ from the output representation to the `createCreditMemo()`
method, then pass the credit memo to the `ensureRefundsAsync()` method.

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

previewReturn(orderSummaryId, changeInput)

### OrderSummaryCreation Class

Create Order Summaries in Order Management.

Namespace

ConnectApi

#### OrderSummaryCreation Methods

### These methods are for OrderSummaryCreation . All methods are static.

IN THIS SECTION:

##### createOrderSummary(orderSummaryInput)

Create an OrderSummary based on an order. That order is considered the original order for the OrderSummary. Subsequent change
orders that apply to the OrderSummary are also represented as orders. You can specify whether the order is managed in Salesforce
Order Management or by an external system. Most Salesforce Order Management APIs can run only on orders that it manages.

##### **`createOrderSummary(orderSummaryInput)`**

Create an OrderSummary based on an order. That order is considered the original order for the OrderSummary. Subsequent change
orders that apply to the OrderSummary are also represented as orders. You can specify whether the order is managed in Salesforce Order
Management or by an external system. Most Salesforce Order Management APIs can run only on orders that it manages.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryOutputRepresentation

   createOrderSummary(ConnectApi.OrderSummaryInputRepresentation orderSummaryInput)

```


### Apex Reference Guide Organization Class

Parameters

```
   orderSummaryInput
```

Type: `ConnectApi.OrderSummaryInputRepresentation`

Input object that wraps the ID of the source order.

Return Value

Type: `ConnectApi.OrderSummaryOutputRepresentation`

### Organization Class

Access information about an org.

Namespace

ConnectApi

#### Organization Methods

### These methods are for Organization . All methods are static.

IN THIS SECTION:

##### getSettings()

Get information about the context user and the org, including which features are enabled.

##### **`getSettings()`**

Get information about the context user and the org, including which features are enabled.

API Version

28.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrganizationSettings getSettings()

```

Return Value

Type: `ConnectApi.OrganizationSettings`

### PardotBusinessUnitContext Class

Get the Pardot business units the context user has access to.


Apex Reference Guide PardotBusinessUnitContext Class

Namespace

ConnectApi

#### PardotBusinessUnitContext Methods These methods are for PardotBusinessUnitContext . All methods are static.

IN THIS SECTION:

##### getBusinessUnitContext()

Get the Pardot business units the context user has access to.

##### getBusinessUnitContextByIsCurrentStatus(isCurrent)

Get the Pardot business units the context user has access to by specifying the current status.

##### **`getBusinessUnitContext()`**

Get the Pardot business units the context user has access to.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PardotBusinessUnitContextOutput getBusinessUnitContext()

```

Return Value

Type: `ConnectApi.PardotBusinessUnitContextOutput`

##### **`getBusinessUnitContextByIsCurrentStatus(isCurrent)`**

Get the Pardot business units the context user has access to by specifying the current status.

API Version

55.0

Requires Chatter

No


### Apex Reference Guide Payments Class

Signature

```
   public static ConnectApi.PardotBusinessUnitContextOutput

   getBusinessUnitContextByIsCurrentStatus(Boolean isCurrent)

```

Parameters

```
   isCurrent
```

Type: Boolean

Specifies whether to return only the business unit that’s selected as the context user's current business unit context in the business
unit switcher of the Pardot Lightning app ( `true` ) or to return only the business units that aren’t selected as the context user's current
business unit context ( `false` ).

Return Value

Type: `ConnectApi.PardotBusinessUnitContextOutput`

### Payments Class

Authorize a payment, capture an authorized payment, and refund an authorized payment.

Namespace

ConnectApi

#### Payments Methods

### These methods are for Payments . All methods are static.

To access Payments methods, you need these permissions.

**•** Salesforce Order Management License

**•** PaymentsAPIUser user permission. This permission is available with the Salesforce Order Management License. Your Salesforce admin
assigns it to your profile.

IN THIS SECTION:

authorize(authorizePayment)
Authorize a payment.

postAuth(postAuthorizePayment)
Confirms that the merchant is ready to capture payment of an existing pre-authorized transaction.

reverseAuthorization(AuthReversalInput, authorizationId)
Reverses a payment authorization.

capture(AuthCaptureInput, authorizationId)
Capture an authorized payment.

refund(ReferencedRefundInput, paymentId)
Refund an authorized payment.


Apex Reference Guide Payments Class

sale(sale)
Captures a payment without any prior authorization and creates a payment entity. The payment sale transaction is a combination
of an Authorize transaction and Capture transaction. This payment sale method allows merchants to request that the funds are
transferred to the merchant account in a single command, with no further action (such as charging a credit card) from the merchant.

tokenizePaymentMethod(tokenizePaymentMethodInput)
Method to take the input parameters of the payment method you want to tokenize and then pass them to the payment gateway's
tokenization service. The results of the tokenization request are returned as a response from the payment gateway.

##### **`authorize(authorizePayment)`**

Authorize a payment.

API Version

51.0

Requires Chatter

No

Signature

```
   global static ConnectApi.AuthorizationResponse authorize(ConnectApi.AuthorizationRequest

   authorizePayment)

```

Parameters

```
   authorizePayment
```

Type: `ConnectApi.AuthorizationRequest`

Represents a payment authorization.

Return Value

Type: `ConnectApi.AuthorizationResponse`

##### **`postAuth(postAuthorizePayment)`**

Confirms that the merchant is ready to capture payment of an existing pre-authorized transaction.

API Version

54.0

Requires Chatter

No


Apex Reference Guide Payments Class

Signature

```
   global static ConnectApi.PostAuthorizationResponse postAuth(ConnectApi.PostAuthRequest

   postAuthorizePayment)

```

Parameters

```
   postAuthorizePayment
```

Type: `ConnectApi.PostAuthRequest`

Information about the payment, payment method, and payment gateway from the original payment authorization.

Return Value

Type: `ConnectApi.PostAuthorizationResponse`

##### **`reverseAuthorization(AuthReversalInput, authorizationId)`**

Reverses a payment authorization.

API Version

51.0

Requires Chatter

No

Signature

```
   global static ConnectApi.AuthorizationReversalResponse

   reverseAuthorization(ConnectApi.AuthorizationReversalRequest AuthReversalInput, String

   authorizationId)

```

Parameters

```
   AuthReversalInput
```

Type: `ConnectApi.AuthorizationReversalRequest`

Input information for the payment authorization reversal.

```
   authorizationId
```

Type: String

The ID of the payment authorization to be reversed.

Return Value

Type: `ConnectApi.AuthorizationReversalResponse`

##### **`capture(AuthCaptureInput, authorizationId)`**

Capture an authorized payment.


Apex Reference Guide Payments Class

API Version

50.0

Requires Chatter

No

Signature

```
   global static ConnectApi.CaptureResponse capture(ConnectApi.CaptureRequest

   AuthCaptureInput, String authorizationId)

```

Parameters

```
   AuthCaptureInput
```

Type: `ConnectApi.CaptureRequest`

A `ConnectApi.CaptureRequest` object with information about the payment capture.

```
   authorizationId
```

Type: String

ID of the payment authorization. Required.

Return Value

Type: `ConnectApi.CaptureResponse`

##### **`refund(ReferencedRefundInput, paymentId)`**

Refund an authorized payment.

To access Payments methods, you need these permissions.

**•** Salesforce Order Management License

**•** PaymentsAPIUser user permission. This permission is available with the Salesforce Order Management License. Your Salesforce admin
assigns it to your profile.

API Version

50.0

Requires Chatter

No

Signature

```
   global static ConnectApi.ReferencedRefundResponse

   refund(ConnectApi.ReferencedRefundRequest ReferencedRefundInput, String paymentId)

```


Apex Reference Guide Payments Class

Parameters

```
   ReferencedRefundInput
```

Type: `ConnectApi.ReferencedRefundRequest`

A `ConnectApi.ReferencedRefundRequest` object with information about the refund.

```
   paymentId
```

Type: String

ID of the payment to be refunded. Required.

Return Value

Type: `ConnectApi.ReferencedRefundResponse`

##### **`sale(sale)`**

Captures a payment without any prior authorization and creates a payment entity. The payment sale transaction is a combination of an
Authorize transaction and Capture transaction. This payment sale method allows merchants to request that the funds are transferred to
the merchant account in a single command, with no further action (such as charging a credit card) from the merchant.

API Version

54.0

Requires Chatter

No

Signature

```
   global static ConnectApi.SaleResponse sale(ConnectApi.SaleRequest sale)

```

Parameters

##### _`sale`_

Type: `ConnectApi.SaleRequest`

Payment sale input class.

Return Value

Type: `ConnectApi.SaleResponse`

##### **`tokenizePaymentMethod(tokenizePaymentMethodInput)`**

Method to take the input parameters of the payment method you want to tokenize and then pass them to the payment gateway's
tokenization service. The results of the tokenization request are returned as a response from the payment gateway.

API Version

52.0


### Apex Reference Guide Personalization Class

Requires Chatter

No

Signature

```
   global static ConnectApi.PaymentMethodTokenizationResponse

   tokenizePaymentMethod(ConnectApi.PaymentMethodTokenizationRequest

   tokenizePaymentMethodInput)

```

Parameters

```
   tokenizePaymentMethodInput
```

Type: `ConnectApi.PaymentMethodTokenizationRequest`

Information about the payment method to be tokenized.

Return Value

Type: `ConnectApi.PaymentMethodTokenizationResponse`

Usage

Accepts input parameters representing a payment method and passes them in a tokenization request to the payment gateway. The
results of the tokenization request are returned as a response from the payment gateway. If the tokenization was successful, the response
contains the tokenized value and details about the tokenization process. Otherwise, the response contains an error message and details
about the error.

Example

```
   ConnectApi.PaymentMethodTokenizationRequest request = new

   ConnectApi.PaymentMethodTokenizationRequest();

   request.paymentGatewayId = ‘0b0xx0000001Ja5AAE’;

   ConnectApi.CardPaymentMethodRequest cpmRequest = new ConnectApi.CardPaymentMethodRequest();

   cpmRequest.cardHolderName = ‘Jo Manager’;

   cpmRequest.expiryMonth = 11;

   cpmRequest.expiryYear = 2222;

   cpmRequest.cardNumber = ‘4111111111111111’;

   cpmRequest.cvv = ‘111’;

   cpmRequest.cardCategory = ConnectApi.CardCategory.CreditCard;

   cpmRequest.cardType = ConnectApi.CardType.Visa.name();

   request.cardPaymentMethod = cpmRequest;

   ConnectApi.PaymentMethodTokenizationResponse response =

   ConnectApi.Payments.tokenizePaymentMethod(request);

### Personalization Class

```

Get assigned personalization audiences that match the user context. Create, get, update, and delete an audience. Get personalization
targets that match the user context, based on the assigned audiences that include the user. Create and update targets. Get and delete
a target.


Apex Reference Guide Personalization Class

Namespace

ConnectApi

Note: Personalization varies what the user can see in the browser but doesn’t secure data in any way. To prevent users accessing
sensitive data, use standard Salesforce security features, such as sharing rules and permission sets.

#### Personalization Methods These methods are for Personalization . All methods are static.

IN THIS SECTION:

##### createAudience(communityId, audience)

Create an audience.

createTargets(communityId, target)
Create targets.

deleteAudience(communityId, audienceId)
Delete an audience.

deleteTarget(communityId, targetId)
Delete a target.

getAudience(communityId, audienceId, includeAudienceCriteria)
Get an audience.

getAudienceBatch(communityId, audienceIds)
Get audience information for a comma-separated list of audience IDs.

getAudiences(communityId, ipAddress, domain, userId, publishStatus, includeAudienceCriteria, targetTypes, recordId)
Get a list of assigned audiences that match the user context and record information.

getAudiences(communityId, ipAddress, domain, userId, publishStatus, includeAudienceCriteria, targetTypes)
Get a list of assigned audiences that match the user context.

getTarget(communityId, targetId)
Get a target.

getTargetBatch(communityId, targetIds)
Get target information for a comma-separated list of target IDs.

getTargets(communityId, ipAddress, domain, userId, publishStatus, recordId, targetTypes, includeAudience,
includeAllMatchingTargetsWithinGroup, groupNames)
Get a list of targets that match the user context, based on the assigned audiences that include the user.

updateAudience(communityId, audienceId, audience)
Update an audience.

updateTargets(communityId, target)
Update targets.

##### **`createAudience(communityId, audience)`**

Create an audience.


Apex Reference Guide Personalization Class

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Audience createAudience(String communityId,

   ConnectApi.AudienceInput audience)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   audience
```

Type: `ConnectApi.AudienceInput`

A `ConnectApi.AudienceInput` object that defines the audience.

Return Value

Type: `ConnectApi.Audience`

##### **`createTargets(communityId, target)`**

Create targets.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TargetCollection createTargets(String communityId,

   ConnectApi.TargetCollectionInput target)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.


Apex Reference Guide Personalization Class

```
   target
```

Type: `ConnectApi.TargetCollectionInput`

A `ConnectApi.TargetCollectionInput` object that defines the targets.

Return Value

Type: `ConnectApi.TargetCollection`

##### **`deleteAudience(communityId, audienceId)`**

Delete an audience.

API Version

48.0

Requires Chatter

No

Signature

```
   public static Void deleteAudience(String communityId, String audienceId)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   audienceId
```

Type: String

ID of the audience.

Return Value

Type: Void

##### **`deleteTarget(communityId, targetId)`**

Delete a target.

API Version

48.0

Requires Chatter

No


Apex Reference Guide Personalization Class

Signature

```
   public static Void deleteTarget(String communityId, String targetId)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   targetId
```

Type: String

ID of the target.

Return Value

Type: Void

##### **`getAudience(communityId, audienceId, includeAudienceCriteria)`**

Get an audience.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Audience getAudience(String communityId, String audienceId,

   Boolean includeAudienceCriteria)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   audienceId
```

Type: String

ID of the audience.

```
   includeAudienceCriteria
```

Type: Boolean


Apex Reference Guide Personalization Class

Specifies whether to include audience criteria ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.Audience`

##### **`getAudienceBatch(communityId, audienceIds)`**

Get audience information for a comma-separated list of audience IDs.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BatchResult[] getAudienceBatch(String communityId, List<String>

   audienceIds)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   audienceIds
```

Type: List<String>

Comma-separated list of audience IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.Audience` object and errors for audiences
that didn’t load.

##### **`getAudiences(communityId, ipAddress, domain, userId, publishStatus,`**

```
  includeAudienceCriteria, targetTypes, recordId)

```

Get a list of assigned audiences that match the user context and record information.


Apex Reference Guide Personalization Class

API Version

51.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.AudienceCollection getAudiences(String communityId, String

   ipAddress, String domain, String userId, ConnectApi.PublishStatus publishStatus, Boolean

   includeAudienceCriteria, List<String> targetTypes, String recordId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   ipAddress
```

Type: String

IP address of the user. If `null`, no audiences with location criteria are returned.

```
   domain
```

Type: String

Name of the user’s Salesforce custom domain. If `null`, no audiences with domain criteria are returned.

```
   userId
```

Type: String

ID of the user. If `null`, defaults to the ID of the context user.

```
   publishStatus
```

Type: `ConnectApi.PublishStatus`

Publish status of the audience. Values are:

**•** `Draft`

**•** `Live`

If `null`, defaults to `Live` .

```
   includeAudienceCriteria
```

Type: Boolean

Specifies whether to include audience criteria ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

```
   targetTypes
```

Type: List<String>

Comma-separated list of target types to filter the results. Supported values include:

**•** `ExperienceVariation` (version 48.0 and later)


Apex Reference Guide Personalization Class

**•** Custom object API names, such as _**`CustomObjectName`**_ `__c` (version 48.0 and later)

**•** `NavigationLinkSet` (version 49.0 and later)

**•** `Topic` (version 49.0 and later)

**•** `CollaborationGroup` (version 49.0 and later)

**•** `KnowledgeArticle` (version 49.0 and later)

**•** `ContentDocument` (version 49.0 and later)

**•** `ManagedContent` (version 49.0 and later)

**•** `Report` (version 49.0 and later)

**•** `Dashboard` (version 49.0 and later)

If `null`, all target types are returned.

```
   recordId
```

Type: String

ID of the record for field based criteria. If `null`, all applicable audiences with field based criteria are returned.

Return Value

Type: `ConnectApi.AudienceCollection`

##### **`getAudiences(communityId, ipAddress, domain, userId, publishStatus,`**

```
  includeAudienceCriteria, targetTypes)

```

Get a list of assigned audiences that match the user context.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.AudienceCollection getAudiences(String communityId, String

   ipAddress, String domain, String userId, ConnectApi.PublishStatus publishStatus, Boolean

   includeAudienceCriteria, List<String> targetTypes)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.


Apex Reference Guide Personalization Class

```
   ipAddress
```

Type: String

IP address of the user. If `null`, no audiences with location criteria are returned.

```
   domain
```

Type: String

Name of the user’s Salesforce custom domain. If `null`, no audiences with domain criteria are returned.

```
   userId
```

Type: String

ID of the user. If `null`, defaults to the ID of the context user.

```
   publishStatus
```

Type: `ConnectApi.PublishStatus`

Publish status of the audience. Values are:

**•** `Draft`

**•** `Live`

If `null`, defaults to `Live` .

```
   includeAudienceCriteria
```

Type: Boolean

Specifies whether to include audience criteria ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

```
   targetTypes
```

Type: List<String>

Comma-separated list of target types to filter the results. Supported values include:

**•** `ExperienceVariation` (version 48.0 and later)

**•** Custom object API names, such as _**`CustomObjectName`**_ `__c` (version 48.0 and later)

**•** `NavigationLinkSet` (version 49.0 and later)

**•** `Topic` (version 49.0 and later)

**•** `CollaborationGroup` (version 49.0 and later)

**•** `KnowledgeArticle` (version 49.0 and later)

**•** `ContentDocument` (version 49.0 and later)

**•** `ManagedContent` (version 49.0 and later)

**•** `Report` (version 49.0 and later)

**•** `Dashboard` (version 49.0 and later)

If `null`, all target types are returned.

Return Value

Type: `ConnectApi.AudienceCollection`

##### **`getTarget(communityId, targetId)`**

Get a target.


Apex Reference Guide Personalization Class

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Target getTarget(String communityId, String targetId)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   targetId
```

Type: String

ID of the target.

Return Value

Type: `ConnectApi.Target`

##### **`getTargetBatch(communityId, targetIds)`**

Get target information for a comma-separated list of target IDs.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BatchResult[] getTargetBatch(String communityId, List<String>

   targetIds)

```


Apex Reference Guide Personalization Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   targetIds
```

Type: List<String>

Comma-separated list of target IDs.

Return Value

Type: `ConnectApi.BatchResult`

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.Target` object and errors for targets
that didn’t load.

##### **`getTargets(communityId, ipAddress, domain, userId, publishStatus, recordId,`**

```
  targetTypes, includeAudience, includeAllMatchingTargetsWithinGroup,

  groupNames)

```

Get a list of targets that match the user context, based on the assigned audiences that include the user.

API Version

48.0

Available to Guest Users

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TargetCollection getTargets(String communityId, String

   ipAddress, String domain, String userId, ConnectApi.PublishStatus publishStatus, String

   recordId, List<String> targetTypes, Boolean includeAudience, Boolean

   includeAllMatchingTargetsWithinGroup, List<String> groupNames)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   ipAddress
```

Type: String

IP address of the user. If `null`, no audiences with location criteria are returned.


Apex Reference Guide Personalization Class

```
   domain
```

Type: String

Name of the user’s Salesforce custom domain. If `null`, no audiences with domain criteria are returned.

```
   userId
```

Type: String

ID of the user. If `null`, the default is the ID of the context user.

```
   publishStatus
```

Type: `ConnectApi.PublishStatus`

Publish status of the target. Values are:

**•** `Draft`

**•** `Live`

```
   recordId
```

Type: String

ID of the record, if you want to specify field based criteria in audiences.

```
   targetTypes
```

Type: List<String>

Comma-separated list of target types to filter the results. Supported values include:

**•** `ExperienceVariation` (version 48.0 and later)

**•** Custom object API names, such as _**`CustomObjectName`**_ `__c` (version 48.0 and later)

**•** `NavigationLinkSet` (version 49.0 and later)

**•** `Topic` (version 49.0 and later)

**•** `CollaborationGroup` (version 49.0 and later)

**•** `KnowledgeArticle` (version 49.0 and later)

**•** `ContentDocument` (version 49.0 and later)

**•** `ManagedContent` (version 49.0 and later)

**•** `Report` (version 49.0 and later)

**•** `Dashboard` (version 49.0 and later)

If `null`, all target types are returned.

```
   includeAudience
```

Type: Boolean

Specifies whether to include the matching audience ( `true` ) or not ( `false` ). If `null`, the default is `false` .

```
   includeAllMatchingTargetsWithinGroup
```

Type: Boolean

Specifies whether to include all the matching targets within a target group ( `true` ) or not ( `false` ). If `null`, the default is `false` .
If `false`, the first matching target within each group, based on priority within the group, is returned.

```
   groupNames
```

Type: List<String>

A comma-separated list of group names. Groups bundle related target and audience pairs.


Apex Reference Guide Personalization Class

Return Value

Type: `ConnectApi.TargetCollection`

##### **`updateAudience(communityId, audienceId, audience)`**

Update an audience.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Audience updateAudience(String communityId, String audienceId,

   ConnectApi.AudienceInput audience)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   audienceId
```

Type: String

ID of the audience.

```
   audience
```

Type: `ConnectApi.AudienceInput`

A `ConnectApi.AudienceInput` object that defines the updates to the audience.

Return Value

Type: `ConnectApi.Audience`

##### **`updateTargets(communityId, target)`**

Update targets.

API Version

48.0

Requires Chatter

No


### Apex Reference Guide PickTicket Class

Signature

```
   public static ConnectApi.TargetCollection updateTargets(String communityId,

   ConnectApi.TargetCollectionUpdateInput target)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   target
```

Type: `ConnectApi.TargetCollectionUpdateInput`

A `ConnectApi.TargetCollectionUpdateInput` object that defines the updates for the targets.

Return Value

Type: `ConnectApi.TargetCollection`

### PickTicket Class

Create tickets to fulfill orders.

Namespace

ConnectApi

#### PickTicket Methods

### These methods are for PickTicket . All methods are static.

IN THIS SECTION:

##### distributePickedQuantities(distributePickedQuantitiesInput)

Distribute picked quantities among orders in a pick ticket.

##### distributePickedQuantities(distributePickedQuantitiesInput)

Distribute picked quantities among orders in a pick ticket.

API Version

58.0

Requires Chatter

No


### Apex Reference Guide QuestionAndAnswers Class

Signature

```
   public static ConnectApi.DistributePickedQuantitiesOutputRepresentation

   distributePickedQuantities(ConnectApi.DistributePickedQuantitiesInputRepresentation

   distributePickedQuantitiesInput)

```

Parameters

```
   distributePickedQuantitiesInput
```

Type: `ConnectApi.DistributePickedQuantitiesInputRepresentation`

Input to distribute picked quantities.

Return Value

Type: `ConnectApi.DistributePickedQuantitiesOutputRepresentation`

### QuestionAndAnswers Class

Access question and answers suggestions.

Namespace

ConnectApi

IN THIS SECTION:

#### QuestionAndAnswers Methods
### These methods are for QuestionAndAnswers . All methods are static.

#### QuestionAndAnswers Methods

### These methods are for QuestionAndAnswers . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### getSuggestions(communityId, q, subjectId, includeArticles, maxResults)

Get question and answers suggestions.

setTestGetSuggestions(communityId, q, subjectId, includeArticles, maxResults, result)
##### Register a ConnectApi.QuestionAndAnswersSuggestions object to be returned when getSuggestions is

called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

updateQuestionAndAnswers(communityId, feedElementId, questionAndAnswersCapability)
Choose or change the best answer for a question.

##### **`getSuggestions(communityId, q, subjectId, includeArticles, maxResults)`**

Get question and answers suggestions.


Apex Reference Guide QuestionAndAnswers Class

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.QuestionAndAnswersSuggestions getSuggestions(String communityId,

   String q, String subjectId, Boolean includeArticles, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   subjectId
```

Type: String

Specify a subject ID to search only questions on that object. If the ID is a topic or a user, the ID is ignored.

```
   includeArticles
```

Type: Boolean

Specify `true` to include knowledge articles in the search results. To return only questions, specify `false` .

```
   maxResults
```

Type: Integer

The maximum number of results to return for each type of item. Possible values are 1–10. The default value is 5.

Return Value

Type: `ConnectApi.QuestionAndAnswersSuggestions`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetSuggestions(communityId, q, subjectId, includeArticles, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide QuestionAndAnswers Class

##### **`setTestGetSuggestions(communityId, q, subjectId, includeArticles, maxResults,`**

```
  result)

```

Register a `ConnectApi.QuestionAndAnswersSuggestions` object to be returned when `getSuggestions` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetSuggestions(String communityId, String q, String subjectId,

   Boolean includeArticles, Integer maxResults, ConnectApi.QuestionAndAnswersSuggestions

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   subjectId
```

Type: String

Specify a subject ID to search only questions on that object. If the ID is a topic or a user, the ID is ignored.

```
   includeArticles
```

Type: Boolean

Specify `true` to include knowledge articles in the search results. To return only questions, specify `false` .

```
   maxResults
```

Type: Integer

The maximum number of results to return for each type of item. Possible values are 1–10. The default value is 5.

```
   result
```

Type: `ConnectApi.QuestionAndAnswersSuggestions`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getSuggestions(communityId, q, subjectId, includeArticles, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide QuestionAndAnswers Class

##### **`updateQuestionAndAnswers(communityId, feedElementId,`**

```
  questionAndAnswersCapability)

```

Choose or change the best answer for a question.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.QuestionAndAnswersCapability updateQuestionAndAnswers(String

   communityId, String feedElementId, ConnectApi.QuestionAndAnswersCapabilityInput

   questionAndAnswersCapability)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementId
```

Type: String

ID of the feed element.

```
   questionAndAnswersCapability
```

Type: `ConnectApi.QuestionAndAnswersCapabilityInput`

Specify the best answer (comment ID) for the question.

Return Value

Type: `ConnectApi.QuestionAndAnswersCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.QuestionAndAnswersCapabilityInput qaInput = new

   ConnectApi.QuestionAndAnswersCapabilityInput();

   qaInput.bestAnswerId = '0D7D00000000lMAKAY';

   ConnectApi.QuestionAndAnswersCapability qa =

   ConnectApi.QuestionAndAnswers.updateQuestionAndAnswers(null, '0D5D0000000XZjJ', qaInput);

```


### Apex Reference Guide Recommendations Class Recommendations Class

Get and reject Chatter, custom, and static recommendations. Create, get, update, and delete custom recommendation audiences, custom
recommendation definitions, and scheduled custom recommendations.

For Next Best Action recommendations, see NextBestAction Class.

Namespace

ConnectApi

#### Recommendations Methods

### These methods are for Recommendations . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

createRecommendationAudience(communityId, recommendationAudience)
Create an audience for a custom recommendation.

createRecommendationAudience(communityId, name)
Create an audience for a custom recommendation.

createRecommendationDefinition(communityId, recommendationDefinition)
Create a custom recommendation definition.

createRecommendationDefinition(communityId, name, title, actionUrl, actionUrlName, explanation)
Create a custom recommendation definition with the specified parameters.

createScheduledRecommendation(communityId, scheduledRecommendation)
Create a scheduled custom recommendation.

createScheduledRecommendation(communityId, recommendationDefinitionId, rank, enabled, recommendationAudienceId, channel)
Create a scheduled custom recommendation with the specified parameters.

deleteRecommendationAudience(communityId, recommendationAudienceId)
Delete a custom recommendation audience.

deleteRecommendationDefinition(communityId, recommendationDefinitionId)
Delete a custom recommendation definition.

deleteRecommendationDefinitionPhoto(communityId, recommendationDefinitionId)
Delete a custom recommendation definition photo.

deleteScheduledRecommendation(communityId, scheduledRecommendationId, deleteDefinitionIfLast)
Delete a scheduled custom recommendation.

getRecommendationAudience(communityId, recommendationAudienceId)
Get information about a custom recommendation audience.

getRecommendationAudienceMembership(communityId, recommendationAudienceId)
Get the members of a custom recommendation audience.

getRecommendationAudienceMembership(communityId, recommendationAudienceId, pageParam, pageSize)
Get a page of custom recommendation audience members.


Apex Reference Guide Recommendations Class

getRecommendationAudiences(communityId)
Get custom recommendation audiences.

getRecommendationAudiences(communityId, pageParam, pageSize)
Get a page of custom recommendation audiences.

getRecommendationDefinition(communityId, recommendationDefinitionId)
Get a custom recommendation definition.

getRecommendationDefinitionPhoto(communityId, recommendationDefinitionId)
Get a custom recommendation definition photo.

getRecommendationDefinitions(communityId)
Get custom recommendation definitions.

getRecommendationForUser(communityId, userId, action, objectId)
Get the Chatter, custom, or static recommendation for the context user for the specified action and object ID.

getRecommendationsForUser(communityId, userId, contextAction, contextObjectId, channel, maxResults)
Get the Chatter recommendations, such as user, group, file, article, record, and topic recommendations for the context user. Get the
custom and static recommendations for the context user.

getRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, channel, maxResults)
Get the Chatter, custom, and static recommendations for the context user for the specified action.

getRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, channel, maxResults)
Get the Chatter, custom, and static recommendations for the context user for the specified action and object category.

getScheduledRecommendation(communityId, scheduledRecommendationId)
Get a scheduled custom recommendation.

getScheduledRecommendations(communityId, channel)
Get scheduled custom recommendations.

rejectRecommendationForUser(communityId, userId, action, objectId)
Reject a Chatter, custom, or static recommendation for the context user for the specified action and object ID.

rejectRecommendationForUser(communityId, userId, action, objectEnum)
Reject a static recommendation for the context user.

updateRecommendationAudience(communityId, recommendationAudienceId, recommendationAudience)
Update a custom recommendation audience.

updateRecommendationDefinition(communityId, recommendationDefinitionId, name, title, actionUrl, actionUrlName, explanation)
Update a custom recommendation definition with the specified parameters.

updateRecommendationDefinition(communityId, recommendationDefinitionId, recommendationDefinition)
Update a custom recommendation definition.

updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId, fileUpload)
Update a custom recommendation definition photo with a file that hasn’t been uploaded.

updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId, fileId, versionNumber)
Update a custom recommendation definition photo with an uploaded file.

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo)
Update a custom recommendation definition photo with an uploaded file that requires cropping.

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo, fileUpload)
Update a custom recommendation definition photo with a file that hasn’t been uploaded and requires cropping.


Apex Reference Guide Recommendations Class

updateScheduledRecommendation(communityId, scheduledRecommendationId, scheduledRecommendation)
Update a scheduled custom recommendation.

updateScheduledRecommendation(communityId, scheduledRecommendationId, rank, enabled, recommendationAudienceId)
Update a scheduled custom recommendation with the specified parameters.

##### **`createRecommendationAudience(communityId, recommendationAudience)`**

Create an audience for a custom recommendation.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationAudience createRecommendationAudience(String

   communityId, ConnectApi.RecommendationAudienceInput recommendationAudience)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudience
```

Type: `ConnectApi.RecommendationAudienceInput`

A `ConnectApi.RecommendationAudienceInput` object.

Return Value

Type: `ConnectApi.RecommendationAudience`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`createRecommendationAudience(communityId, name)`**

Create an audience for a custom recommendation.

API Version

35.0


Apex Reference Guide Recommendations Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationAudience createRecommendationAudience(String

   communityId, String name)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   name
```

Type: String

Name of the audience.

Return Value

Type: `ConnectApi.RecommendationAudience`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`createRecommendationDefinition(communityId, recommendationDefinition)`**

Create a custom recommendation definition.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinition createRecommendationDefinition(String

   communityId, ConnectApi.RecommendationDefinitionInput recommendationDefinition)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Recommendations Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinition
```

Type: `ConnectApi.RecommendationDefinitionInput`

A `ConnectApi.RecommendationDefinitionInput` object.

Return Value

Type: `ConnectApi.RecommendationDefinition`

Usage

Recommendation definitions allow you to create custom recommendations that appear in Experience Cloud sites, encouraging users
to watch videos, take training and more.

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

These recommendations appear by default on the Customer Service template. They appear on the home and question detail pages and
in the feed in Salesforce mobile web. They also appear anywhere community managers add recommendations using Experience Builder
in the Customer Service template.

So that users don’t see the same recommendations all the time, Salesforce periodically removes and brings back custom recommendations
that haven’t been accepted or dismissed.

##### **`createRecommendationDefinition(communityId, name, title, actionUrl,`**

```
  actionUrlName, explanation)

```

Create a custom recommendation definition with the specified parameters.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinition createRecommendationDefinition(String

   communityId, String name, String title, String actionUrl, String actionUrlName, String

   explanation)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide Recommendations Class

```
   name
```

Type: String

Name of the custom recommendation definition. The name is displayed in Setup.

```
   title
```

Type: String

Title of the custom recommendation definition.

```
   actionUrl
```

Type: String

URL for acting on the custom recommendation, for example, the URL to join a group.

```
   actionUrlName
```

Type: String

Text label for the action URL in the user interface, for example, “Launch.”

```
   explanation
```

Type: String

Explanation, or body, of the custom recommendation.

Return Value

Type: `ConnectApi.RecommendationDefinition`

Usage

Recommendation definitions allow you to create custom recommendations that appear in Experience Cloud sites, encouraging users
to watch videos, take training and more.

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

These recommendations appear by default on the Customer Service template. They appear on the home and question detail pages and
in the feed in Salesforce mobile web. They also appear anywhere community managers add recommendations using Experience Builder
in the Customer Service template.

So that users don’t see the same recommendations all the time, Salesforce periodically removes and brings back custom recommendations
that haven’t been accepted or dismissed.

##### **`createScheduledRecommendation(communityId, scheduledRecommendation)`**

Create a scheduled custom recommendation.

API Version

35.0

Requires Chatter

Yes


Apex Reference Guide Recommendations Class

Signature

```
   public static ConnectApi.ScheduledRecommendation createScheduledRecommendation(String

   communityId, ConnectApi.ScheduledRecommendationInput scheduledRecommendation)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   scheduledRecommendation
```

Type: `ConnectApi.ScheduledRecommendationInput`

A `ConnectApi.ScheduledRecommendationInput` object.

Return Value

Type: `ConnectApi.ScheduledRecommendation`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`createScheduledRecommendation(communityId, recommendationDefinitionId, rank,`**

```
  enabled, recommendationAudienceId, channel)

```

Create a scheduled custom recommendation with the specified parameters.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendation createScheduledRecommendation(String

   communityId, String recommendationDefinitionId, Integer rank, Boolean enabled, String

   recommendationAudienceId, ConnectApi.RecommendationChannel channel)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide Recommendations Class

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   rank
```

Type: Integer

Relative rank of the scheduled custom recommendation indicated by ascending whole numbers starting with 1.

Setting the rank is comparable to an insertion into an ordered list. The scheduled custom recommendation is inserted into the
position specified by the `rank` . The `rank` of all the scheduled custom recommendations after it is pushed down. See Ranking
scheduled custom recommendations example.

If the specified `rank` is larger than the size of the list, the scheduled custom recommendation is put at the end of the list. The
`rank` of the scheduled custom recommendation is the size of the list, instead of the one specified.

If a `rank` is not specified, the scheduled custom recommendation is put at the end of the list.

```
   enabled
```

Type: Boolean

Indicates whether scheduling is enabled. If `true`, the custom recommendation is enabled and appears in Experience Cloud sites.
If `false`, custom recommendations in feeds in Salesforce mobile web aren’t removed, but no new custom recommendations
appear. In Customer Service and Partner Central sites, disabled custom recommendations no longer appear.

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation definition that this scheduled recommendation schedules.

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

Use these channel values; you can’t rename or create other channels.

Return Value

Type: `ConnectApi.ScheduledRecommendation`


Apex Reference Guide Recommendations Class

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

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

##### **`deleteRecommendationAudience(communityId, recommendationAudienceId)`**

Delete a custom recommendation audience.

API Version

35.0

Requires Chatter

Yes


Apex Reference Guide Recommendations Class

Signature

```
   public static Void deleteRecommendationAudience(String communityId, String

   recommendationAudienceId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation audience.

Return Value

Type: Void

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`deleteRecommendationDefinition(communityId, recommendationDefinitionId)`**

Delete a custom recommendation definition.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static Void deleteRecommendationDefinition(String communityId, String

   recommendationDefinitionId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String


Apex Reference Guide Recommendations Class

ID of the custom recommendation definition.

Return Value

Type: Void

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`deleteRecommendationDefinitionPhoto(communityId, recommendationDefinitionId)`**

Delete a custom recommendation definition photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static Void deleteRecommendationDefinitionPhoto(String communityId, String

   recommendationDefinitionId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

Return Value

Type: Void

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.


Apex Reference Guide Recommendations Class

##### **`deleteScheduledRecommendation(communityId, scheduledRecommendationId,`**

```
  deleteDefinitionIfLast)

```

Delete a scheduled custom recommendation.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static Void deleteScheduledRecommendation(String communityId, String

   scheduledRecommendationId, Boolean deleteDefinitionIfLast)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   scheduledRecommendationId
```

Type: String

ID of the scheduled custom recommendation.

```
   deleteDefinitionIfLast
```

Type: Boolean

If `true` and if this is the last scheduled custom recommendation of a custom recommendation definition, deletes the custom
recommendation definition. Default is `false` .

Return Value

Type: Void

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

Deleting a scheduled custom recommendation is comparable to a deletion in an ordered list. All scheduled custom recommendations
after the deleted scheduled custom recommendation receive a new, higher rank automatically.

##### **`getRecommendationAudience(communityId, recommendationAudienceId)`**

Get information about a custom recommendation audience.


Apex Reference Guide Recommendations Class

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationAudience getRecommendationAudience(String

   communityId, String recommendationAudienceId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation audience.

Return Value

Type: `ConnectApi.RecommendationAudience`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationAudienceMembership(communityId, recommendationAudienceId)`**

Get the members of a custom recommendation audience.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserReferencePage getRecommendationAudienceMembership(String

   communityId, String recommendationAudienceId)

```


Apex Reference Guide Recommendations Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation audience.

Return Value

Type: `ConnectApi.UserReferencePage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationAudienceMembership(communityId, recommendationAudienceId,`**

```
  pageParam, pageSize)

```

Get a page of custom recommendation audience members.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserReferencePage getRecommendationAudienceMembership(String

   communityId, String recommendationAudienceId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation audience.

```
   pageParam
```

Type: Integer


Apex Reference Guide Recommendations Class

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of members per page.

Return Value

Type: `ConnectApi.UserReferencePage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationAudiences(communityId)`**

Get custom recommendation audiences.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationAudiencePage getRecommendationAudiences(String

   communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.RecommendationAudiencePage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.


Apex Reference Guide Recommendations Class

##### **`getRecommendationAudiences(communityId, pageParam, pageSize)`**

Get a page of custom recommendation audiences.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationAudiencePage getRecommendationAudiences(String

   communityId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of audiences per page.

Return Value

Type: `ConnectApi.RecommendationAudiencePage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationDefinition(communityId, recommendationDefinitionId)`**

Get a custom recommendation definition.

API Version

35.0


Apex Reference Guide Recommendations Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinition getRecommendationDefinition(String

   communityId, String recommendationDefinitionId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

Return Value

Type: `ConnectApi.RecommendationDefinition`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationDefinitionPhoto(communityId, recommendationDefinitionId)`**

Get a custom recommendation definition photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo getRecommendationDefinitionPhoto(String communityId,

   String recommendationDefinitionId)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Recommendations Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

Return Value

Type: `ConnectApi.Photo`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationDefinitions(communityId)`**

Get custom recommendation definitions.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinitionPage getRecommendationDefinitions(String

   communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.RecommendationDefinitionPage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.


Apex Reference Guide Recommendations Class

##### **`getRecommendationForUser(communityId, userId, action, objectId)`**

Get the Chatter, custom, or static recommendation for the context user for the specified action and object ID.

API Version

33.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType action, String objectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectId
```

Type: String

Specifies the object to act on.

**•** If _`action`_ is `follow`, _`objectId`_ is a user ID, file ID, record ID, or topic ID (version 36.0 and later).

**•** If _`action`_ is `join`, _`objectId`_ is a group ID.

**•** If _`action`_ is `view`, _`objectId`_ is a user ID, file ID, group ID, record ID, custom recommendation ID (version 34.0 and later),
the enum `Today` for static recommendations (version 35.0 and later), or an article ID (version 37.0 and later).

Return Value

Type: `ConnectApi.RecommendationCollection`


Apex Reference Guide Recommendations Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationForUser(communityId, userId, action, objectId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecommendationsForUser(communityId, userId, contextAction, contextObjectId,`**

```
  channel, maxResults)

```

Get the Chatter recommendations, such as user, group, file, article, record, and topic recommendations for the context user. Get the
custom and static recommendations for the context user.

API Version

36.0

Available to Guest Users

38.0

Note: Only article and file recommendations are available to guest users.

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType contextAction, String

   contextObjectId, ConnectApi.RecommendationChannel channel, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`


Apex Reference Guide Recommendations Class

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.


Apex Reference Guide Recommendations Class

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, contextAction, contextObjectId, channel, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecommendationsForUser(communityId, userId, action, contextAction,`**

```
  contextObjectId, channel, maxResults)

```

Get the Chatter, custom, and static recommendations for the context user for the specified action.

API Version

36.0

Available to Guest Users

38.0

Note: Only article and file recommendations are available to guest users.

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType action,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId,

   ConnectApi.RecommendationChannel channel, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.


Apex Reference Guide Recommendations Class

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`


Apex Reference Guide Recommendations Class

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, channel, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecommendationsForUser(communityId, userId, action, objectCategory,`**

```
  contextAction, contextObjectId, channel, maxResults)

```

Get the Chatter, custom, and static recommendations for the context user for the specified action and object category.

API Version

36.0

Available to Guest Users

38.0

Note: Only article and file recommendations are available to guest users.

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType action, String

   objectCategory, ConnectApi.RecommendationActionType contextAction, String

   contextObjectId, ConnectApi.RecommendationChannel channel, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .


Apex Reference Guide Recommendations Class

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectCategory
```

Type: String

**•** If _`action`_ is `follow`, _`objectCategory`_ is `users`, `files`, `topics`, or `records` .

**•** If _`action`_ is `join`, _`objectCategory`_ is `groups` .

**•** If _`action`_ is `view`, _`objectCategory`_ is `users`, `files`, `groups`, `records`, `custom`, `apps`, or `articles`
(version 37.0 and later).

You can also specify a key prefix, the first three characters of the object ID, as the _`objectCategory`_ . Valid values are:

**•** If _`action`_ is `follow`, _`objectCategory`_ is `005` (users), `069` (files), `0TO` (topics), or `001` (accounts), for example.

**•** If _`action`_ is `join`, _`objectCategory`_ is `0F9` (groups).

**•** If _`action`_ is `view`, _`objectCategory`_ is `005` (users), `069` (files), `0F9` (groups), `0RD` (custom recommendations), `T`
(static recommendations), `001` (accounts), or `kA0` (articles), for example, (version 370 and later).

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.


Apex Reference Guide Recommendations Class

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.


Apex Reference Guide Recommendations Class

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, channel,
maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getScheduledRecommendation(communityId, scheduledRecommendationId)`**

Get a scheduled custom recommendation.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendation getScheduledRecommendation(String

   communityId, String scheduledRecommendationId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   scheduledRecommendationId
```

Type: String

ID of the scheduled custom recommendation.

Return Value

Type: `ConnectApi.ScheduledRecommendation`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getScheduledRecommendations(communityId, channel)`**

Get scheduled custom recommendations.


Apex Reference Guide Recommendations Class

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendationPage getScheduledRecommendations(String

   communityId, ConnectApi.RecommendationChannel channel)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

Return Value

Type: `ConnectApi.ScheduledRecommendationPage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.


Apex Reference Guide Recommendations Class

##### **`rejectRecommendationForUser(communityId, userId, action, objectId)`**

Reject a Chatter, custom, or static recommendation for the context user for the specified action and object ID.

API Version

33.0

Requires Chatter

Yes

Signature

```
   public static rejectRecommendationForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, String objectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation. Supported values are:

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectId
```

Type: String

Specifies the object to take action on.

**•** If _`action`_ is `follow`, _`objectId`_ is a user ID, file ID, record ID, or topic ID (version 36.0 and later).

**•** If _`action`_ is `join`, _`objectId`_ is a group ID.

**•** If _`action`_ is `view`, _`objectId`_ is a custom recommendation ID, the enum `Today` for static recommendations, or an article
ID (version 37.0 and later).

Return Value

Type: Void

##### **`rejectRecommendationForUser(communityId, userId, action, objectEnum)`**

Reject a static recommendation for the context user.


Apex Reference Guide Recommendations Class

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static rejectRecommendationForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, ConnectApi.RecommendedObjectType objectEnum)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation. Supported values are:

**•** `view` —View a static recommendation.

```
   objectEnum
```

Type: `ConnectApi.RecommendedObjectType`

Specifies the object type to take action on.

**•** `Today` —Static recommendations that don’t have an ID, for example, the Today app recommendation.

Return Value

Type: Void

##### **`updateRecommendationAudience(communityId, recommendationAudienceId,`**

```
  recommendationAudience)

```

Update a custom recommendation audience.

API Version

35.0

Requires Chatter

Yes


Apex Reference Guide Recommendations Class

Signature

```
   public static ConnectApi.RecommendationAudience updateRecommendationAudience(String

   communityId, String recommendationAudienceId, ConnectApi.RecommendationAudienceInput

   recommendationAudience)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation audience.

```
   recommendationAudience
```

Type: `ConnectApi.RecommendationAudienceInput`

A `ConnectApi.RecommendationAudienceInput` object.

Return Value

Type: `ConnectApi.RecommendationAudience`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinition(communityId, recommendationDefinitionId, name,`**

```
  title, actionUrl, actionUrlName, explanation)

```

Update a custom recommendation definition with the specified parameters.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinition updateRecommendationDefinition(String

   communityId, String recommendationDefinitionId, String name, String title, String

   actionUrl, String actionUrlName, String explanation recommendationDefinition)

```


Apex Reference Guide Recommendations Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   name
```

Type: String

Name of the custom recommendation definition. The name is displayed in Setup.

```
   title
```

Type: String

Title of the custom recommendation definition.

```
   actionUrl
```

Type: String

URL for acting on the custom recommendation, for example, the URL to join a group.

```
   actionUrlName
```

Type: String

Text label for the action URL in the user interface, for example, “Launch.”

```
   explanation
```

Type: String

Explanation, or body, of the custom recommendation.

Return Value

Type: `ConnectApi.RecommendationDefinition`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinition(communityId, recommendationDefinitionId,`**

```
  recommendationDefinition)

```

Update a custom recommendation definition.

API Version

35.0


Apex Reference Guide Recommendations Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationDefinition updateRecommendationDefinition(String

   communityId, String recommendationDefinitionId, ConnectApi.RecommendationDefinitionInput

   recommendationDefinition)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   recommendationDefinition
```

Type: `ConnectApi.RecommendationDefinitionInput`

A `ConnectApi.RecommendationDefinitionInput` object containing the properties to update.

Return Value

Type: `ConnectApi.RecommendationDefinition`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId,`**

```
  fileUpload)

```

Update a custom recommendation definition photo with a file that hasn’t been uploaded.

API Version

35.0

Requires Chatter

Yes


Apex Reference Guide Recommendations Class

Signature

```
   public static ConnectApi.Photo updateRecommendationDefinitionPhoto(String communityId,

   String recommendationDefinitionId, ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId,`**

```
  fileId, versionNumber)

```

Update a custom recommendation definition photo with an uploaded file.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo updateRecommendationDefinitionPhoto(String communityId,

   String recommendationDefinitionId, String fileId, Integer versionNumber)

```


Apex Reference Guide Recommendations Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   fileId
```

Type: String

ID of a file already uploaded. The file must be an image, and be smaller than 2 GB.

```
   versionNumber
```

Type: Integer

Version number of the existing file. Specify either an existing version number, or `null` to get the latest version.

Return Value

Type: `ConnectApi.Photo`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinitionPhotoWithAttributes(communityId,`**

```
  recommendationDefinitionId, photo)

```

Update a custom recommendation definition photo with an uploaded file that requires cropping.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo updateRecommendationDefinitionPhotoWithAttributes(String

   communityId, String recommendationDefinitionId, ConnectApi.PhotoInput photo)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Recommendations Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object specifying the file ID, version number, and cropping parameters.

Return Value

Type: `ConnectApi.Photo`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateRecommendationDefinitionPhotoWithAttributes(communityId,`**

```
  recommendationDefinitionId, photo, fileUpload)

```

Update a custom recommendation definition photo with a file that hasn’t been uploaded and requires cropping.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo updateRecommendationDefinitionPhotoWithAttributes(String

   communityId, String recommendationDefinitionId, ConnectApi.PhotoInput photo,

   ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.


Apex Reference Guide Recommendations Class

```
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object specifying the cropping parameters.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`updateScheduledRecommendation(communityId, scheduledRecommendationId,`**

```
  scheduledRecommendation)

```

Update a scheduled custom recommendation.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendation updateScheduledRecommendation(String

   communityId, String scheduledRecommendationId, ConnectApi.ScheduledRecommendationInput

   scheduledRecommendation)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   scheduledRecommendationId
```

Type: String

ID of the scheduled custom recommendation.

```
   scheduledRecommendation
```

Type: `ConnectApi.ScheduledRecommendationInput`


Apex Reference Guide Recommendations Class

A `ConnectApi.ScheduledRecommendationInput` object containing the properties to update.

Return Value

Type: `ConnectApi.ScheduledRecommendation`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

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

##### **`updateScheduledRecommendation(communityId, scheduledRecommendationId, rank,`**

```
  enabled, recommendationAudienceId)

```

Update a scheduled custom recommendation with the specified parameters.

API Version

35.0


Apex Reference Guide Recommendations Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendation updateScheduledRecommendation(String

   communityId, String scheduledRecommendationId, Integer rank, Boolean enabled, String

   recommendationAudienceId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   scheduledRecommendationId
```

Type: String

ID of the scheduled custom recommendation.

```
   rank
```

Type: Integer

Relative rank of the scheduled custom recommendation indicated by ascending whole numbers starting with 1.

Setting the rank is comparable to an insertion into an ordered list. The scheduled custom recommendation is inserted into the
position specified by the `rank` . The `rank` of all the scheduled custom recommendations after it is pushed down. See Ranking
scheduled custom recommendations example.

If the specified `rank` is larger than the size of the list, the scheduled custom recommendation is put at the end of the list. The
`rank` of the scheduled custom recommendation is the size of the list, instead of the one specified.

If a `rank` is not specified, the scheduled custom recommendation is put at the end of the list.

```
   enabled
```

Type: Boolean

Indicates whether scheduling is enabled. If `true`, the custom recommendation is enabled and appears in Experience Cloud sites.
If `false`, custom recommendations in feeds in Salesforce mobile web aren’t removed, but no new custom recommendations
appear. In Customer Service and Partner Central sites, disabled custom recommendations no longer appear.

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation definition that this scheduled recommendation schedules.

Return Value

Type: `ConnectApi.ScheduledRecommendation`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.


Apex Reference Guide Recommendations Class

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

#### Recommendations Test Methods These test methods are for Recommendations . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

IN THIS SECTION:

setTestGetRecommendationForUser(communityId, userId, action, objectId, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRecommendationsForUser(communityId, userId, contextAction, contextObjectId, channel, maxResults, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, channel, maxResults, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide Recommendations Class

setTestGetRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, channel,
maxResults, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

##### **`setTestGetRecommendationForUser(communityId, userId, action, objectId, result)`**

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

33.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, String objectId,

   ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectId
```

Type: String

Specifies the object to take action on.

**•** If _`action`_ is `follow`, _`objectId`_ is a user ID, file ID, record ID, or topic ID (version 36.0 and later).

**•** If _`action`_ is `join`, _`objectId`_ is a group ID.

**•** If _`action`_ is `view`, _`objectId`_ is a user ID, file ID, group ID, record ID, custom recommendation ID, the enum `Today` for
static recommendations, or an article ID (version 37.0 and later).


Apex Reference Guide Recommendations Class

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationForUser(communityId, userId, action, objectId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecommendationsForUser(communityId, userId, contextAction,`**

```
  contextObjectId, channel, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId,

   ConnectApi.RecommendationChannel channel, Integer maxResults,

   ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`


Apex Reference Guide Recommendations Class

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, contextAction, contextObjectId, channel, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Recommendations Class

##### **`setTestGetRecommendationsForUser(communityId, userId, action, contextAction,`**

```
  contextObjectId, channel, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, ConnectApi.RecommendationActionType

   contextAction, String contextObjectId, ConnectApi.RecommendationChannel channel, Integer

   maxResults, ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.


Apex Reference Guide Recommendations Class

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, channel, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecommendationsForUser(communityId, userId, action, objectCategory,`**

```
  contextAction, contextObjectId, channel, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide Recommendations Class

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, String objectCategory,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId,

   ConnectApi.RecommendationChannel channel, Integer maxResults,

   ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectCategory
```

Type: String

**•** If _`action`_ is `follow`, _`objectCategory`_ is `users`, `files`, `records`, or `topics` .

**•** If _`action`_ is `join`, _`objectCategory`_ is `groups` .

**•** If _`action`_ is `view`, _`objectCategory`_ is `users`, `files`, `groups`, `records`, `custom`, `apps`, or `articles`
(version 37.0 and later).

You can also specify a key prefix, the first three characters of the object ID, as the _`objectCategory`_ . Valid values are:

**•** If _`action`_ is `follow`, _`objectCategory`_ is `005` (users), `069` (files), `0TO` (topics), or `001` (accounts), for example.

**•** If _`action`_ is `join`, _`objectCategory`_ is `0F9` (groups).

**•** If _`action`_ is `view`, _`objectCategory`_ is `005` (users), `069` (files), `0F9` (groups), `0RD` (custom recommendations), `T`
(static recommendations), `001` (accounts), or `kA0` (articles), for example, (version 370 and later).

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:


Apex Reference Guide Recommendations Class

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, record ID, or topic ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, record ID, or article ID (version 37.0 and
later).

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   channel
```

Type: `ConnectApi.RecommendationChannel`

A way to tie custom recommendations together. For example, display recommendations in specific places in the UI or show
recommendations based on time of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels. For example, community managers can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, channel, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Recommendations Class

#### Retired Recommendations Methods

These methods for `Recommendations` are retired.

IN THIS SECTION:

##### createScheduledRecommendation(communityId, recommendationDefinitionId, rank, enabled, recommendationAudienceId)

Create a scheduled custom recommendation with the specified parameters.

getRecommendationsForUser(communityId, userId, contextAction, contextObjectId, maxResults)
Get the Chatter recommendations, such as user, group, file, and record recommendations for the context user. Get the custom and
static recommendations for the context user.

getRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, maxResults)
Get the Chatter, custom, and static recommendations for the context user for the specified action.

getRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, maxResults)
Get the Chatter, custom, and static recommendations for the context user for the specified action and object category.

getScheduledRecommendations(communityId)
Get scheduled custom recommendations.

setTestGetRecommendationsForUser(communityId, userId, contextAction, contextObjectId, maxResults, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, maxResults, result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, maxResults,
result)
Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

##### **`createScheduledRecommendation(communityId, recommendationDefinitionId, rank,`**

```
  enabled, recommendationAudienceId)

```

Create a scheduled custom recommendation with the specified parameters.

API Version

35.0 only

##### Important: In version 36.0 and later, use createScheduledRecommendation(communityId,

`recommendationDefinitionId, rank, enabled, recommendationAudienceId, channel)` .

Requires Chatter

Yes


Apex Reference Guide Recommendations Class

Signature

```
   public static ConnectApi.ScheduledRecommendation createScheduledRecommendation(String

   communityId, String recommendationDefinitionId, Integer rank, Boolean enabled, String

   recommendationAudienceId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recommendationDefinitionId
```

Type: String

ID of the custom recommendation definition.

```
   rank
```

Type: Integer

Relative rank of the scheduled custom recommendation indicated by ascending whole numbers starting with 1.

Setting the rank is comparable to an insertion into an ordered list. The scheduled custom recommendation is inserted into the
position specified by the `rank` . The `rank` of all the scheduled custom recommendations after it is pushed down. See Ranking
scheduled custom recommendations example.

If the specified `rank` is larger than the size of the list, the scheduled custom recommendation is put at the end of the list. The
`rank` of the scheduled custom recommendation is the size of the list, instead of the one specified.

If a `rank` is not specified, the scheduled custom recommendation is put at the end of the list.

```
   enabled
```

Type: Boolean

Indicates whether scheduling is enabled. If `true`, the custom recommendation is enabled and appears in Experience Cloud sites.
If `false`, custom recommendations in feeds in Salesforce mobile web aren’t removed, but no new custom recommendations
appear. In Customer Service and Partner Central sites, disabled custom recommendations no longer appear.

```
   recommendationAudienceId
```

Type: String

ID of the custom recommendation definition that this scheduled recommendation schedules.

Return Value

Type: `ConnectApi.ScheduledRecommendation`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

**Ranking scheduled custom recommendations example**

If you have these scheduled custom recommendations:


Apex Reference Guide Recommendations Class

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

##### **`getRecommendationsForUser(communityId, userId, contextAction, contextObjectId,`**

```
  maxResults)

```

Get the Chatter recommendations, such as user, group, file, and record recommendations for the context user. Get the custom and static
recommendations for the context user.

API Version

33.0–35.0

##### Important: In version 36.0 and later, use getRecommendationsForUser(communityId, userId,

`contextAction, contextObjectId, channel, maxResults)` .

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType contextAction, String

   contextObjectId, Integer maxResults)

```


Apex Reference Guide Recommendations Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, contextAction, contextObjectId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Recommendations Class

##### **`getRecommendationsForUser(communityId, userId, action, contextAction,`**

```
  contextObjectId, maxResults)

```

Get the Chatter, custom, and static recommendations for the context user for the specified action.

API Version

33.0–35.0

##### Important: In version 36.0 and later, use getRecommendationsForUser(communityId, userId, action,

`contextAction, contextObjectId, channel, maxResults)` .

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType action,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId, Integer

   maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String


Apex Reference Guide Recommendations Class

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecommendationsForUser(communityId, userId, action, objectCategory,`**

```
  contextAction, contextObjectId, maxResults)

```

Get the Chatter, custom, and static recommendations for the context user for the specified action and object category.

API Version

33.0–35.0

##### Important: In version 36.0 and later, use getRecommendationsForUser(communityId, userId, action,

`objectCategory, contextAction, contextObjectId, channel, maxResults)` .

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RecommendationCollection getRecommendationsForUser(String

   communityId, String userId, ConnectApi.RecommendationActionType action, String

```


Apex Reference Guide Recommendations Class

```
   objectCategory, ConnectApi.RecommendationActionType contextAction, String

   contextObjectId, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectCategory
```

Type: String

**•** If _`action`_ is `follow`, _`objectCategory`_ is `users`, `files`, or `records` .

**•** If _`action`_ is `join`, _`objectCategory`_ is `groups` .

**•** If _`action`_ is `view`, _`objectCategory`_ is `users`, `files`, `groups`, `records`, `custom`, or `apps` .

You can also specify a key prefix, the first three characters of the object ID, as the _`objectCategory`_ . Valid values are:

**•** If _`action`_ is `follow`, _`objectCategory`_ is `005` (users), `069` (files), or `001` (accounts), for example.

**•** If _`action`_ is `join`, _`objectCategory`_ is `0F9` (groups).

**•** If _`action`_ is `view`, _`objectCategory`_ is `005` (users), `069` (files), `0F9` (groups), `0RD` (custom recommendations), `T`
(static recommendations), or `001` (accounts), for example.

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .


Apex Reference Guide Recommendations Class

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

If you want to get recommendations based on a recent action performed, such as following a user, use _`contextAction`_ and
_`contextObjectId`_ together. For example, if you just followed Pam, you specify `follow` for _`contextAction`_ and Pam’s user
ID for _`contextObjectId`_ .

This method only recommends users who are followed by people who follow Pam. In this example, John follows Pam so the method
returns a recommendation for you to follow Suzanne since John also follows Suzanne.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, maxResults,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getScheduledRecommendations(communityId)`**

Get scheduled custom recommendations.

API Version

35.0 only


Apex Reference Guide Recommendations Class

Important: In version 36.0 and later, use `getScheduledRecommendations(communityId, channel)` .

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ScheduledRecommendationPage getScheduledRecommendations(String

   communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ScheduledRecommendationPage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`setTestGetRecommendationsForUser(communityId, userId, contextAction,`**

```
  contextObjectId, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

33.0–35.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId, Integer

   maxResults, ConnectApi.RecommendationCollection result)

```


Apex Reference Guide Recommendations Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, contextAction, contextObjectId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecommendationsForUser(communityId, userId, action, contextAction,`**

```
  contextObjectId, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide Recommendations Class

API Version

33.0–35.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, ConnectApi.RecommendationActionType

   contextAction, String contextObjectId, Integer maxResults,

   ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .


Apex Reference Guide Recommendations Class

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecommendationsForUser(communityId, userId, action, objectCategory,`**

```
  contextAction, contextObjectId, maxResults, result)

```

Register a `ConnectApi.RecommendationCollection` object to be returned when `getRecommendationsForUser`
is called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

33.0–35.0

Requires Chatter

Yes

Signature

```
   public static Void setTestGetRecommendationsForUser(String communityId, String userId,

   ConnectApi.RecommendationActionType action, String objectCategory,

   ConnectApi.RecommendationActionType contextAction, String contextObjectId, Integer

   maxResults, ConnectApi.RecommendationCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   action
```

Type: `ConnectApi.RecommendationActionType`


Apex Reference Guide Recommendations Class

Specifies the action to take on a recommendation.

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

```
   objectCategory
```

Type: String

**•** If _`action`_ is `follow`, _`objectCategory`_ is `users`, `files`, or `records` .

**•** If _`action`_ is `join`, _`objectCategory`_ is `groups` .

**•** If _`action`_ is `view`, _`objectCategory`_ is `users`, `files`, `groups`, `records`, `custom`, or `apps` .

You can also specify a key prefix, the first three characters of the object ID, as the _`objectCategory`_ . Valid values are:

**•** If _`action`_ is `follow`, _`objectCategory`_ is `005` (users), `069` (files), or `001` (accounts), for example.

**•** If _`action`_ is `join`, _`objectCategory`_ is `0F9` (groups).

**•** If _`action`_ is `view`, _`objectCategory`_ is `005` (users), `069` (files), `0F9` (groups), `0RD` (custom recommendations), `T`
(static recommendations), or `001` (accounts), for example.

```
   contextAction
```

Type: `ConnectApi.RecommendationActionType`

Action that the context user just performed. Supported values are:

**•** `follow`

**•** `view`

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   contextObjectId
```

Type: String

ID of the object that the context user just performed an action on.

**•** If _`contextAction`_ is `follow`, _`contextObjectId`_ is a user ID, file ID, or record ID.

**•** If _`contextAction`_ is `view`, _`contextObjectId`_ is a user ID, file ID, group ID, or record ID.

Use _`contextAction`_ and _`contextObjectId`_ together to get new recommendations based on the action just performed.
If you don’t want recommendations based on a recent action, specify `null` .

```
   maxResults
```

Type: Integer

Maximum number of recommendation results; default is 10. Values must be from 1 to 99.

```
   result
```

Type: `ConnectApi.RecommendationCollection`

Object containing test data.


### Apex Reference Guide RecordFilterCriteriaFamily Class

Return Value

Type: Void

SEE ALSO:

getRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### RecordFilterCriteriaFamily Class

Filter records on recordset filter criteria.

Namespace

ConnectApi

#### RecordFilterCriteriaFamily Methods

### These methods are for RecordFilterCriteriaFamily . All methods are static.

IN THIS SECTION:

##### evaluateRecordsetFilterCriteria(recordsetFilterCriteriaInput)

Filter records on recordset filter criteria.

##### **`evaluateRecordsetFilterCriteria(recordsetFilterCriteriaInput)`**

Filter records on recordset filter criteria.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecordsetFilterCriteriaCollection

   evaluateRecordsetFilterCriteria(ConnectApi.RecordsetFilterCriteriaInput

   recordsetFilterCriteriaInput)

```

Parameters

```
   recordsetFilterCriteriaInput
```

Type: `ConnectApi.RecordsetFilterCriteriaInput`

`ConnectApi.RecordsetFilterCriteriaInput` object providing a set of recordset filter criteria and records.


### Apex Reference Guide Records Class

Return Value

Type: `ConnectApi.RecordsetFilterCriteriaCollection`

Usage

Field service must be enabled.

### Records Class

Access information about record motifs, which are small icons used to distinguish record types in the Salesforce UI.

Namespace

ConnectApi

#### Records Methods

### These methods are for Records . All methods are static.

IN THIS SECTION:

##### getMotif(communityId, idOrPrefix)

Get a motif that contains the URLs for a set of small, medium, and large motif icons for a record. It can also contain a base color for
the record.

getMotifBatch(communityId, idOrPrefixList)
Get a motif for a list of objects.

##### **`getMotif(communityId, idOrPrefix)`**

Get a motif that contains the URLs for a set of small, medium, and large motif icons for a record. It can also contain a base color for the
record.

API Version

28.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Motif getMotif(String communityId, String idOrPrefix)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Records Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   idOrPrefix
```

Type: String

An ID or key prefix.

Return Value

Type: `ConnectApi.Motif`

Usage

Each Salesforce record type has its own set of motif icons.

##### **`getMotifBatch(communityId, idOrPrefixList)`**

Get a motif for a list of objects.

API Version

31.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BatchResult[] getMotifBatch(String communityId, List<String>

   idOrPrefixList)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   idOrPrefixList
```

Type: List<String>

A list of object IDs or prefixes.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.Motif` object and errors for motifs that
didn’t load.


### Apex Reference Guide RecordUi Class

Example

```
   String communityId = null;

   List<String> prefixIds = new List<String> { '001', '01Z', '069' };

   // Get info about the motifs of all records in the list.

   ConnectApi.BatchResult[] batchResults = ConnectApi.Records.getMotifBatch(communityId,

   prefixIds);

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print the color of each motif.

        ConnectApi.Motif motif;

        if(batchResult.getResult() instanceof ConnectApi.Motif) {

           motif = (ConnectApi.Motif) batchResult.getResult();

        }

        System.debug('SUCCESS');

        System.debug(motif.color);

      }

      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

### RecordUi Class

```

Get picklist values by record type.

Namespace

ConnectApi

#### RecordUi Methods

### These methods are for RecordUi . All methods are static.

IN THIS SECTION:

##### getPicklistValuesByRecordType(objectApiName, recordTypeId)

Get the values for all the picklist fields of a specific record type.

##### **`getPicklistValuesByRecordType(objectApiName, recordTypeId)`**

Get the values for all the picklist fields of a specific record type.

API Version

66.0


### Apex Reference Guide RegisterGuestBuyer Class

Available to Guest Users

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PicklistValuesCollection getPicklistValuesByRecordType(String

   objectApiName, String recordTypeId)

```

Parameters

```
   objectApiName
```

Type: String

[API name of a User Interface API supported object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm#ui_api_get_started_supported_objects)

```
   recordTypeId
```

Type: String

ID of a record type.

Return Value

Type: `ConnectApi.PicklistValuesCollection`

Usage

This method is especially useful for getting dependent picklist values. For example, if an object has a tree of dependent picklists
(Continents__c, Countries__c, Cities__c), use this method to get all the values for each picklist in one request.

### RegisterGuestBuyer Class

Register a guest buyer for a webstore using an account ID, enabling a guest buyer to order on behalf of another buyer.

Namespace

ConnectApi

#### RegisterGuestBuyer Methods

### These methods are for RegisterGuestBuyer . All methods are static. Your org must have the Order Management Growth license

or Order Management as part of Connected Commerce.

IN THIS SECTION:

registerGuestBuyer(webstoreId, accountId)
Register a guest buyer for a webstore using an account ID. This method enables a guest buyer to order on behalf of another buyer.


### Apex Reference Guide Repricing Class

##### **`registerGuestBuyer(webstoreId, accountId)`**

Register a guest buyer for a webstore using an account ID. This method enables a guest buyer to order on behalf of another buyer.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RegisterGuestBuyerOutputRepresentation registerGuestBuyer(String

   webstoreId, String accountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   accountId
```

Type: String

ID of the account for which the request is made.

Return Value

Type: `ConnectApi.RegisterGuestBuyerOutputRepresentation on page 2507`

### Repricing Class

Perform functions related to repricing orders in Order Management.

Namespace

ConnectApi

#### Repricing Methods

### These methods are for Repricing . All methods are static.

IN THIS SECTION:

productDetails(webstoreId, skuOrProductId, effectiveAccountId, currencyCode, locale)
Get details of a product in a web store.

searchProducts(webstoreId, searchTerm, pageParam, pageSize, effectiveAccountId, facets)
Search products in a webstore.


Apex Reference Guide Repricing Class

##### **`productDetails(webstoreId, skuOrProductId, effectiveAccountId, currencyCode,`**

```
  locale)

```

Get details of a product in a web store.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetailsOutputRepresentation productDetails(String

   webstoreId, String skuOrProductId, String effectiveAccountId, String currencyCode,

   String locale)

```

Parameters

```
   webstoreId
```

Type: String

ID of the WebStore.

```
   skuOrProductId
```

Type: String

SKU or ID of the Product.

```
   effectiveAccountId
```

Type: String

Effective Account ID. Required for B2B stores. For other stores, pass null.

```
   currencyCode
```

Type: String

ISO currency code. If you pass null, the default store value is used.

```
   locale
```

Type: String

Locale. If you pass null, the default store value is used.

```
   excludeAttributeSetInfo
```

Type: Bolean

Specifies whether the attribute set information for the product is returned.

```
   excludeBundleChildrenInfo
```

Type: Bolean

Specifies whether the child product information for the product bundle is returned.

```
   excludeMedia
```

Type: String

Specifies whether the media groups and default images of the product are returned.


Apex Reference Guide Repricing Class

```
   excludeQuantityRule
```

Type: Bolean

Specifies whether the quantity rule information for the product is returned.

```
   excludeVariationInfo
```

Type: Bolean

Specifies whether the variation information for the product is returned.

```
   excludePrices
```

Type: Bolean

Specifies whether the prices for the product is returned.

Return Value

Type: `ConnectApi.ProductDetailsOutputRepresentation`

##### **`searchProducts(webstoreId, searchTerm, pageParam, pageSize,`**

```
  effectiveAccountId, facets)

```

Search products in a webstore.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchOutputRepresentation searchProducts(String

   webstoreId, String searchTerm, Integer pageParam, Integer pageSize, String

   effectiveAccountId, String facets)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   searchTerm
```

Type: String

Term used for the search.

```
   pageParam
```

Type: Integer

Maximum number of search results pages to return. If you don't specify a value, the default is 1.

```
   pageSize
```

Type: Integer


### Apex Reference Guide ReturnOrder Class

Number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 20.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If unspecified, defaults to the account ID for the context user.

```
   facets
```

Type: String

A list of facet names to filter the search.For example, `["size_medium", "color_red"]` is encoded to

```
    WyJzaXplX21lZGl1bSIsICJjb2xvcl9yZWQiXQ==

```

Return Value

Type: `ConnectApi.ProductSearchOutputRepresentation` on page 2476

### ReturnOrder Class

Process ReturnOrders in Order Management, limited to 2,000 requests per hour.

Namespace

ConnectApi

#### ReturnOrder Methods

### These methods are for ReturnOrder . All methods are static.

IN THIS SECTION:

##### createReturnOrder(returnOrderInput)

Create a ReturnOrder and ReturnOrderLineItems for items belonging to an OrderSummary.

returnItems(returnOrderId, returnItemsInput)
Process ReturnOrderLineItems belonging to a ReturnOrder. Processing a ReturnOrderLineItem generates a change Order and makes
that ReturnOrderLineItem read-only. The change order for a returned item or delivery charge has a positive amount and should be
used to create a credit memo. The change order for a return fee has a negative amount and should be used to create an invoice. If
a processed ReturnOrderLineItem has any remaining expected quantity, then the API creates a separate ReturnOrderLineItem
representing that quantity.

##### **`createReturnOrder(returnOrderInput)`**

Create a ReturnOrder and ReturnOrderLineItems for items belonging to an OrderSummary.

API Version

50.0

Requires Chatter

No


Apex Reference Guide ReturnOrder Class

Signature

```
   public static ConnectApi.ReturnOrderOutputRepresentation

   createReturnOrder(ConnectApi.ReturnOrderInputRepresentation returnOrderInput)

```

Parameters

```
   returnOrderInput
```

Type: `ConnectApi.ReturnOrderInputRepresentation`

Data for creating a ReturnOrder and ReturnOrderLineItems.

Return Value

Type: `ConnectApi.ReturnOrderOutputRepresentation`

SEE ALSO:

##### returnItems(returnOrderId, returnItemsInput) **`returnItems(returnOrderId, returnItemsInput)`**

Process ReturnOrderLineItems belonging to a ReturnOrder. Processing a ReturnOrderLineItem generates a change Order and makes
that ReturnOrderLineItem read-only. The change order for a returned item or delivery charge has a positive amount and should be used
to create a credit memo. The change order for a return fee has a negative amount and should be used to create an invoice. If a processed
ReturnOrderLineItem has any remaining expected quantity, then the API creates a separate ReturnOrderLineItem representing that
quantity.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ReturnItemsOutputRepresentation returnItems(String

   returnOrderId, ConnectApi.ReturnItemsInputRepresentation returnItemsInput)

```

Parameters

```
   returnOrderId
```

Type: String

ID of the ReturnOrder.

```
   returnItemsInput
```

Type: `ConnectApi.ReturnItemsInputRepresentation`

Data about products and delivery charges to return, as well as associated return fees.


### Apex Reference Guide Routing Class

Return Value

Type: `ConnectApi.ReturnItemsOutputRepresentation`

SEE ALSO:

createMultipleInvoices(invoicesInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

createReturnOrder(returnOrderInput)

### Routing Class

Route orders to inventory locations in Order Management.

Namespace

ConnectApi

#### Routing Methods

### These methods are for Routing . All methods are static.

IN THIS SECTION:

confirmHeldFOCapacity(confirmHeldFOCapacityInput)
Confirm held fulfillment order capacity at one or more locations. This call decreases a location’s held capacity and increases its
assigned fulfillment order count. Confirm held capacity when you assign a fulfillment order to a location.

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)
Returns combinations of inventory locations that can fulfill an order within a specified limit of shipment splits. By default, checks up
to 1,000,000 potential routes, returning a maximum of 10,000 results.

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)
For one or more order summaries, find inventory availability using Omnichannel Inventory and identify the fulfillment routes with
fewest splits. By default, checks up to 1,000,000 potential routes, returning a maximum of 10,000 results. This method combines the
functionality of the `getInventoryAvailability()` and `findRoutesWithFewestSplits()` methods.

getFOCapacityValues(getFOCapacityValuesInput)
Get information about the current fulfillment order capacity of one or more locations.

holdFOCapacity(holdFOCapacityInput)
Hold fulfillment order capacity at a location. Holding capacity at a location reserves a space for a fulfillment order that you’ll assign
to it.

rankAverageDistance(rankAverageDistanceInputRepresentation)
Calculates the average distance from sets of inventory locations to an order recipient, and ranks them. Use this method to compare
the average shipping distances for different sets of locations that can fulfill an order. While this method is executing, you can’t invoke
another Apex callout.

releaseHeldFOCapacity(releaseHeldFOCapacityInput)
Release held fulfillment order capacity at one or more locations. This call decreases a location’s held capacity without changing its
assigned fulfillment order count. Release held capacity when you cancel the assignment of a fulfillment order to a location.


Apex Reference Guide Routing Class

##### **`confirmHeldFOCapacity(confirmHeldFOCapacityInput)`**

Confirm held fulfillment order capacity at one or more locations. This call decreases a location’s held capacity and increases its assigned
fulfillment order count. Confirm held capacity when you assign a fulfillment order to a location.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ConfirmHeldFOCapacityOutputRepresentation

   confirmHeldFOCapacity(ConnectApi.ConfirmHeldFOCapacityInputRepresentation

   confirmHeldFOCapacityInput)

```

Parameters

```
   confirmHeldFOCapacityInput
```

Type: `ConnectApi.ConfirmHeldFOCapacityInputRepresentation`

The input includes, for each fulfillment order, the location where capacity is held for it.

Return Value

Type: `ConnectApi.ConfirmHeldFOCapacityOutputRepresentation`

##### **`findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)`**

Returns combinations of inventory locations that can fulfill an order within a specified limit of shipment splits. By default, checks up to
1,000,000 potential routes, returning a maximum of 10,000 results.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation

   findRoutesWithFewestSplits(ConnectApi.FindRoutesWithFewestSplitsInputRepresentation

   findRoutesWithFewestSplitsInputRepresentation)

```


Apex Reference Guide Routing Class

Parameters

```
   findRoutesWithFewestSplitsInputRepresentation
```

Type: `ConnectApi.FindRoutesWithFewestSplitsInputRepresentation`

The input includes the ordered item quantities, data about available inventory, and, optionally, a maximum allowable number of
shipment splits.

Return Value

Type: `ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation`

##### **`findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)`**

For one or more order summaries, find inventory availability using Omnichannel Inventory and identify the fulfillment routes with fewest
splits. By default, checks up to 1,000,000 potential routes, returning a maximum of 10,000 results. This method combines the functionality
of the `getInventoryAvailability()` and `findRoutesWithFewestSplits()` methods.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation

   findRoutesWithFewestSplitsUsingOCI(ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation

   findRoutesWithFewestSplitsUsingOCIInput)

```

Parameters

```
   findRoutesWithFewestSplitsUsingOCIInput
```

Type: `ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation`

The input includes, for each order, the ordered item quantities, the assigned location group or locations, and, optionally, a maximum
allowable number of shipment splits and a list of locations to exclude from the calculation.

Return Value

Type: `ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation`

SEE ALSO:

getInventoryAvailability(inventoryAvailabilityInputRepresentation)

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)

##### **`getFOCapacityValues(getFOCapacityValuesInput)`**

Get information about the current fulfillment order capacity of one or more locations.


Apex Reference Guide Routing Class

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.GetFOCapacityValuesOutputRepresentation

   getFOCapacityValues(ConnectApi.GetFOCapacityValuesRequestInputRepresentation

   getFOCapacityValuesInput)

```

Parameters

```
   getFOCapacityValuesInput
```

Type: `ConnectApi.GetFOCapacityValuesRequestInputRepresentation`

Locations to get fulfillment order capacity information about.

Return Value

Type: `ConnectApi.GetFOCapacityValuesOutputRepresentation`

##### **`holdFOCapacity(holdFOCapacityInput)`**

Hold fulfillment order capacity at a location. Holding capacity at a location reserves a space for a fulfillment order that you’ll assign to it.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.HoldFOCapacityOutputRepresentation

   holdFOCapacity(ConnectApi.HoldFOCapacityInputRepresentation holdFOCapacityInput)

```

Parameters

```
   holdFOCapacityInput
```

Type: `ConnectApi.HoldFOCapacityInputRepresentation`

The input includes, for each fulfillment order, the location to hold capacity for it.

Return Value

Type: `ConnectApi.HoldFOCapacityOutputRepresentation`


Apex Reference Guide Routing Class

##### **`rankAverageDistance(rankAverageDistanceInputRepresentation)`**

Calculates the average distance from sets of inventory locations to an order recipient, and ranks them. Use this method to compare the
average shipping distances for different sets of locations that can fulfill an order. While this method is executing, you can’t invoke another
Apex callout.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RankAverageDistanceOutputRepresentation

   rankAverageDistance(ConnectApi.RankAverageDistanceInputRepresentation

   rankAverageDistanceInputRepresentation)

```

Parameters

```
   rankAverageDistanceInputRepresentation
```

Type: `ConnectApi.RankAverageDistanceInputRepresentation`

An order recipient’s geographic location and information about sets of inventory locations that can fulfill the order.

Return Value

Type: `ConnectApi.RankAverageDistanceOutputRepresentation`

##### **`releaseHeldFOCapacity(releaseHeldFOCapacityInput)`**

Release held fulfillment order capacity at one or more locations. This call decreases a location’s held capacity without changing its
assigned fulfillment order count. Release held capacity when you cancel the assignment of a fulfillment order to a location.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ReleaseHeldFOCapacityOutputRepresentation

   releaseHeldFOCapacity(ConnectApi.ReleaseHeldFOCapacityInputRepresentation

   releaseHeldFOCapacityInput)

```


### Apex Reference Guide SalesforceInbox Class

Parameters

```
   releaseHeldFOCapacityInput
```

Type: `ConnectApi.ReleaseHeldFOCapacityInputRepresentation`

The input includes, for each fulfillment order, the location that holds the capacity to release.

Return Value

Type: `ConnectApi.ReleaseHeldFOCapacityOutputRepresentation`

### SalesforceInbox Class

Access information about Automated Activity Capture, which is available in Einstein and Salesforce Inbox.

Namespace

ConnectApi

#### SalesforceInbox Methods

### These methods are for SalesforceInbox . All methods are static.

IN THIS SECTION:

##### shareActivity(activityId, sharingInfo)

Share emails or events with certain groups of users.

##### **`shareActivity(activityId, sharingInfo)`**

Share emails or events with certain groups of users.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ActivitySharingResult shareActivity(String activityId,

   ConnectApi.ActivitySharingInput sharingInfo)

```

Parameters

```
   activityId
```

Type: String

The ID of the activity.


### Apex Reference Guide Search Class

```
   sharingInfo
```

Type: `ConnectApi.ActivitySharingInput`

A `ConnectApi.ActivitySharingInput` object.

Return Value

Type: `ConnectApi.ActivitySharingResult`

Usage

This method is a feature of both Sales Cloud Einstein and Inbox. It lets users connect their email and calendar to Salesforce. Then, their
emails and events are automatically added to related Salesforce records. Users can specify who their individual emails and events are
shared with.

### Search Class

Search objects using keywords or a natural language query.

Namespace

ConnectApi

#### Search Methods

### These methods are for Search . All methods are static.

IN THIS SECTION:

##### answer(q)

Search objects using a natural language query and return an answer.

answer(q, objectApiName)
Search an object using a natural language query and return an answer.

answer(q, objectApiName, displayFields)
Search an object using a natural language query and display fields.

findAndGroup(q)
Search objects using keyword search and return result groups.

findAndGroup(q, configurationName)
Search objects using keyword search and a configuration. The search returns result groups.

findAndGroup(q, configurationName, highlights)
Search objects using keyword search, a configuration, and highlights. The search returns result groups.

find(objectApiName, request)
Search an object using keywords and return results.

##### **`answer(q)`**

Search objects using a natural language query and return an answer.


Apex Reference Guide Search Class

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SearchAnswer answer(String q)

```

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.

Return Value

Type: `ConnectApi.SearchAnswer`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`answer(q, objectApiName)`**

Search an object using a natural language query and return an answer.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SearchAnswer answer(String q, String objectApiName)

```


Apex Reference Guide Search Class

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.

```
   objectApiName
```

Type: String

API name of the object.

Return Value

Type: `ConnectApi.SearchAnswer`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`answer(q, objectApiName, displayFields)`**

Search an object using a natural language query and display fields.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SearchAnswer answer(String q, String objectApiName, List<String>

   displayFields)

```

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.

```
   objectApiName
```

Type: String

API name of the object.

```
   displayFields
```

Type: List<String>


Apex Reference Guide Search Class

List of fields to display and return in the search answer. The default is the citation field.

Return Value

Type: `ConnectApi.SearchAnswer`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`findAndGroup(q)`**

Search objects using keyword search and return result groups.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SearchResultGroups findAndGroup(String q)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

Return Value

Type: `ConnectApi.SearchResultGroups`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`findAndGroup(q, configurationName)`**

Search objects using keyword search and a configuration. The search returns result groups.


Apex Reference Guide Search Class

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SearchResultGroups findAndGroup(String q, String

   configurationName)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

```
   configurationName
```

Type: String

Search configuration to apply.

Return Value

Type: `ConnectApi.SearchResultGroups`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`findAndGroup(q, configurationName, highlights)`**

Search objects using keyword search, a configuration, and highlights. The search returns result groups.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No


Apex Reference Guide Search Class

Signature

```
   public static ConnectApi.SearchResultGroups findAndGroup(String q, String

   configurationName, Boolean highlights)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

```
   configurationName
```

Type: String

Search configuration to apply.

```
   highlights
```

Type: Boolean

Specifies whether search generates a text highlight ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.SearchResultGroups`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`find(objectApiName, request)`**

Search an object using keywords and return results.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ScopedSearchResults find(String objectApiName,

   ConnectApi.SearchRequest request)

```


Apex Reference Guide Search Class

Parameters

```
   objectApiName
```

Type: String

API name of the object to search.

```
   request
```

Type: `ConnectApi.SearchRequest`

`ConnectApi.SearchRequest` input class with more information about what and how to search.

Return Value

Type: `ConnectApi.ScopedSearchResults`

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

#### Search Test Methods These test methods are for Search . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAnswer(q, result)`**

Registers a `ConnectApi.SearchAnswer` object to be returned when the matching `answer(q)` method is called in a test
context. Use the method with the same parameters or you receive an exception.

API Version

63.0

Signature

```
   public static Void setTestAnswer(String q, ConnectApi.SearchAnswer result)

```

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.

```
   result
```

Type: `ConnectApi.SearchAnswer`

Object containing test data.

Return Value

Type: Void


Apex Reference Guide Search Class

##### **`setTestAnswer(q, objectApiName, result)`**

Registers a `ConnectApi.SearchAnswer` object to be returned when the matching `answer(q, objectApiName)` method
is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

63.0

Signature

```
   public static Void setTestAnswer(String q, String objectApiName, ConnectApi.SearchAnswer

   result)

```

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.

```
   objectApiName
```

Type: String

API name of the object.

```
   result
```

Type: `ConnectApi.SearchAnswer`

Object containing test data.

Return Value

Type: Void

##### **`setTestAnswer(q, objectApiName, displayFields, result)`**

Registers a `ConnectApi.SearchAnswer` object to be returned when the matching `answer(q, objectApiName,`
`displayFields)` method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

62.0

Signature

```
   public static Void setTestAnswer(String q, String objectApiName, List<String>

   displayFields, ConnectApi.SearchAnswer result)

```

Parameters

```
   q
```

Type: String

Natural language query to search for in the org.


Apex Reference Guide Search Class

```
   objectApiName
```

Type: String

API name of the object.

```
   displayFields
```

Type: List<String>

List of fields to display and return in the search results. By default, the fields displayed are defined by the search layout.

```
   result
```

Type: `ConnectApi.SearchAnswer`

Object containing test data.

Return Value

Type: Void

##### **`setTestFindAndGroup(q, result)`**

Registers a `ConnectApi.SearchResultGroups` object to be returned when the matching `findAndGroup(q)` method is
called in a test context. Use the method with the same parameters or you receive an exception.

API Version

63.0

Signature

```
   public static Void setTestFindAndGroup(String q, ConnectApi.SearchResultGroups result)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

```
   result
```

Type: `ConnectApi.SearchResultGroups`

Object containing test data.

Return Value

Type: Void

##### **`setTestFindAndGroup(q, configurationName, result)`**

Registers a `ConnectApi.SearchResultGroups` object to be returned when the matching `findAndGroup(q,`
`configurationName)` method is called in a test context. Use the method with the same parameters or you receive an exception.


Apex Reference Guide Search Class

API Version

63.0

Signature

```
   public static Void setTestFindAndGroup(String q, String configurationName,

   ConnectApi.SearchResultGroups result)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

```
   configurationName
```

Type: String

Search configuration to apply.

```
   result
```

Type: `ConnectApi.SearchResultGroups`

Object containing test data.

Return Value

Type: Void

##### **`setTestFindAndGroup(q, configurationName, highlights, result)`**

Registers a `ConnectApi.SearchResultGroups` object to be returned when the matching `findAndGroup(q,`
`configurationName, highlights)` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

63.0

Signature

```
   public static Void setTestFindAndGroup(String q, String configurationName, Boolean

   highlights, ConnectApi.SearchResultGroups result)

```

Parameters

```
   q
```

Type: String

One or more keywords to search for in the org.

```
   configurationName
```

Type: String

Search configuration to apply.


### Apex Reference Guide Sites Class

```
   highlights
```

Type: Boolean

Specifies whether search generates a text highlight ( `true` ) or not ( `false` ).

```
   result
```

Type: `ConnectApi.SearchResultGroups`

Object containing test data.

Return Value

Type: Void

##### **`setTestFind(objectApiName, request, result)`**

Registers a `ConnectApi.ScopedSearchResults` object to be returned when the matching `find(objectApiName,`
`request)` method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

63.0

Signature

```
   public static Void setTestFind(String objectApiName, ConnectApi.SearchRequest request,

   ConnectApi.ScopedSearchResults result)

```

Parameters

```
   objectApiName
```

Type: String

API name of the object to search.

```
   request
```

Type: `ConnectApi.SearchRequest`

`ConnectApi.SearchRequest` input class with more information about what and how to search.

```
   result
```

Type: `ConnectApi.ScopedSearchResults`

Object containing test data.

Return Value

Type: Void

### Sites Class

Search an Experience Cloud site.


Apex Reference Guide Sites Class

Namespace

ConnectApi

#### Sites Methods These methods are for Sites . All methods are static.

IN THIS SECTION:

##### searchSite(siteId, queryTerm, pageToken, pageSize, language)

Search an Experience Cloud site.

##### **`searchSite(siteId, queryTerm, pageToken, pageSize, language)`**

Search an Experience Cloud site.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SiteSearchResult searchSite(String siteId, String queryTerm,

   String pageToken, Integer pageSize, String language)

```

Parameters

```
   siteId
```

Type: String

ID for the Experience Cloud site.

```
   queryTerm
```

Type: String

White-space separated words used to search for relevant content. Provide a maximum of 1024 characters, composed of up to 32
words and white spaces. Logical operators aren’t supported.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   pageSize
```

Type: Integer


### Apex Reference Guide SmartDataDiscovery Class

Specifies the number of items per page. Valid values are from 1 through 240. If you pass in `null`, the default size is 25.

```
   language
```

Type: String

Language locale for the context user. If unspecified or if the specified language locale isn’t available, the default value is `en_US` .

Return Value

Type: `ConnectApi.SiteSearchResult`

### SmartDataDiscovery Class

Get predictions on Salesforce objects.

Use the `ConnectApi.SmartDataDiscovery.predict` method to get predictions on Salesforce objects. For more information,
[see Get Predictions in Apex.](https://help.salesforce.com/articleView?id=bi_edd_prediction_apex.htm&language=en_US)

### SocialEngagement Class

Manage information about social accounts or fan pages for social networks.

Note: Social Studio was retired on November 18, 2024.

Namespace

ConnectApi

SEE ALSO:

_Knowledge Article_ [: Marketing Cloud Social Studio Retirement](https://help.salesforce.com/s/articleView?id=000392005&type=1&language=en_US)

#### SocialEngagement Methods

### These methods are for SocialEngagement . All methods are static.

IN THIS SECTION:

deleteSocialPost(socialPostId, socialAccountId)
Delete a social post from its social network.

followSocialPersona(socialPersonaId, socialAccountId)
Follow a social persona in its social network.

followSocialPostPersona(socialPostId, socialAccountId)
Follow a social persona on a social post in its social network.

getIntents(socialPostId)
Get available intents for a social post.

getManagedSocialAccount(id)
Get a managed social account that is in the org and assigned to the user.


Apex Reference Guide SocialEngagement Class

getManagedSocialAccounts()
Gets a list of managed social accounts that are in the org and assigned to the user.

getManagedSocialAccounts(socialNetwork)
Get a list of managed social accounts that are in the org and assigned to the user.

getRelationship(id, socialPersonaId)
Get the follow relationship between a managed social account and a social persona.

hideSocialPost(socialPostId, socialAccountId)
Hide a social post in its social network.

likeSocialPost(socialPostId, socialAccountId)
Like a social post in its social network.

massApprove(massApproval)
Approve or reject the publishing of a large number of social posts.

recallApproval(socialPostId)
Recall an approval request to publish a social post.

unfollowSocialPersona(socialPersonaId, socialAccountId)
Stop following a social persona in its social network.

unfollowSocialPostPersona(socialPostId, socialAccountId)
Stop following a social persona of a social post in its social network.

unhideSocialPost(socialPostId, socialAccountId)
Unhide a social post in its social network.

unlikeSocialPost(socialPostId, socialAccountId)
Unlike a social post in its social network.

##### **`deleteSocialPost(socialPostId, socialAccountId)`**

Delete a social post from its social network.

Note: Deleting a social post from its social network doesn’t delete the record from Salesforce.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DeleteSocialPostIntent deleteSocialPost(String socialPostId,

   String socialAccountId)

```


Apex Reference Guide SocialEngagement Class

Parameters

```
   socialPostId
```

Type: String

ID of the social post to delete.

```
   socialAccountId
```

Type: String

ID of the social account that deletes the post.

Return Value

Type: `ConnectApi.DeleteSocialPostIntent`

##### **`followSocialPersona(socialPersonaId, socialAccountId)`**

Follow a social persona in its social network.

API Version

45.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FollowSocialPersonaIntent followSocialPersona(String

   socialPersonaId, String socialAccountId)

```

Parameters

```
   socialPersonaId
```

Type: String

ID of the social persona to follow.

```
   socialAccountId
```

Type: String

ID of the social account that follows the social persona.

Return Value

Type: `ConnectApi.FollowSocialPersonaIntent`

##### **`followSocialPostPersona(socialPostId, socialAccountId)`**

Follow a social persona on a social post in its social network.


Apex Reference Guide SocialEngagement Class

API Version

45.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FollowSocialPersonaIntent followSocialPostPersona(String

   socialPostId, String socialAccountId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post authored by the social persona to follow.

```
   socialAccountId
```

Type: String

ID of the social account that follows the social persona.

Return Value

Type: `ConnectApi.FollowSocialPersonaIntent`

##### **`getIntents(socialPostId)`**

Get available intents for a social post.

API Version

45.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SocialPostIntents getIntents(String socialPostId)

```

Parameters

```
   socialPostId
```

Type: String

ID of a social post.


Apex Reference Guide SocialEngagement Class

Return Value

Type: `ConnectApi.SocialPostIntents`

##### **`getManagedSocialAccount(id)`**

Get a managed social account that is in the org and assigned to the user.

API Version

44.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedSocialAccount getManagedSocialAccount(String id)

```

Parameters

```
   id
```

Type: String

Description: Internal SFDC ID for this managed social account.

Return Value

Type: `ConnectApi.ManagedSocialAccount`

##### **`getManagedSocialAccounts()`**

Gets a list of managed social accounts that are in the org and assigned to the user.

API Version

44.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedSocialAccounts getManagedSocialAccounts()

```

Return Value

Type: `ConnectApi.ManagedSocialAccounts`


Apex Reference Guide SocialEngagement Class

##### **`getManagedSocialAccounts(socialNetwork)`**

Get a list of managed social accounts that are in the org and assigned to the user.

API Version

44.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ManagedSocialAccounts

   getManagedSocialAccounts(ConnectApi.SocialNetworkProvider socialNetwork)

```

Parameters

```
   socialNetwork
```

Type: `ConnectApi.SocialNetworkProvider`

Description: Filters results based on the social network. Values are:

**•** `Facebook`

**•** `GooglePlus`

**•** `Instagram`

**•** `InstagramBusiness`

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


Apex Reference Guide SocialEngagement Class

Return Value

Type: `ConnectApi.ManagedSocialAccounts`

##### **`getRelationship(id, socialPersonaId)`**

Get the follow relationship between a managed social account and a social persona.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SocialAccountRelationship getRelationship(String id, String

   socialPersonaId)

```

Parameters

```
   id
```

Type: String

ID of the managed social account.

```
   socialPersonaId
```

Type: String

ID of the social persona.

Return Value

Type: `ConnectApi.SocialAccountRelationship`

##### **`hideSocialPost(socialPostId, socialAccountId)`**

Hide a social post in its social network.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.HideSocialPostIntent hideSocialPost(String socialPostId, String

   socialAccountId)

```


Apex Reference Guide SocialEngagement Class

Parameters

```
   socialPostId
```

Type: String

ID of the social post to hide.

```
   socialAccountId
```

Type: String

ID of the social account that hides the post.

Return Value

Type: `ConnectApi.HideSocialPostIntent`

##### **`likeSocialPost(socialPostId, socialAccountId)`**

Like a social post in its social network.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.LikeSocialPostIntent likeSocialPost(String socialPostId, String

   socialAccountId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post to like.

```
   socialAccountId
```

Type: String

ID of the social account that likes the post.

Return Value

Type: `ConnectApi.LikeSocialPostIntent`

##### **`massApprove(massApproval)`**

Approve or reject the publishing of a large number of social posts.


Apex Reference Guide SocialEngagement Class

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SocialPostMassApprovalOutput

   massApprove(ConnectApi.SocialPostMassApprovalInput massApproval)

```

Parameters

```
   massApproval
```

Type: `ConnectApi.SocialPostMassApprovalInput`

A `ConnectApi.SocialPostMassApprovalInput` body that includes a list of social post IDs and the action to approve
or reject publishing them.

Return Value

Type: `ConnectApi.SocialPostMassApprovalOutput`

##### **`recallApproval(socialPostId)`**

Recall an approval request to publish a social post.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static Void recallApproval(String socialPostId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post.

Return Value

Type: Void


Apex Reference Guide SocialEngagement Class

##### **`unfollowSocialPersona(socialPersonaId, socialAccountId)`**

Stop following a social persona in its social network.

API Version

45.0–61.0

Requires Chatter

No

Signature

```
   public static Void unfollowSocialPersona(String socialPersonaId, String socialAccountId)

```

Parameters

```
   socialPersonaId
```

Type: String

ID of the social persona to stop following.

```
   socialAccountId
```

Type: String

ID of the social account that stops following the social persona.

Return Value

Type: Void

##### **`unfollowSocialPostPersona(socialPostId, socialAccountId)`**

Stop following a social persona of a social post in its social network.

API Version

45.0–61.0

Requires Chatter

No

Signature

```
   public static Void unfollowSocialPostPersona(String socialPostId, String socialAccountId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post authored by the social persona to stop following.


Apex Reference Guide SocialEngagement Class

```
   socialAccountId
```

Type: String

ID of the social account that stops following the social persona.

Return Value

Type: Void

##### **`unhideSocialPost(socialPostId, socialAccountId)`**

Unhide a social post in its social network.

API Version

46.0–61.0

Requires Chatter

No

Signature

```
   public static Void unhideSocialPost(String socialPostId, String socialAccountId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post to unhide.

```
   socialAccountId
```

Type: String

ID of the social account that unhides the post.

Return Value

Type: Void

##### **`unlikeSocialPost(socialPostId, socialAccountId)`**

Unlike a social post in its social network.

API Version

46.0–61.0

Requires Chatter

No


### Apex Reference Guide Surveys Class

Signature

```
   public static Void unlikeSocialPost(String socialPostId, String socialAccountId)

```

Parameters

```
   socialPostId
```

Type: String

ID of the social post to unlike.

```
   socialAccountId
```

Type: String

ID of the social account that unlikes the post.

Return Value

Type: Void

### Surveys Class

Send survey invitations by email.

Namespace

ConnectApi

#### Surveys Methods

### These methods are for Surveys . All methods are static.

IN THIS SECTION:

##### sendSurveyInvitationEmail(surveyID, SurveyEmailInput)

Email survey invitations to up to 300 participants. You can email either leads, contacts, or users in your org. Either a link to launch
the survey or a question can be embedded in the email invitations.

##### **`sendSurveyInvitationEmail(surveyID, SurveyEmailInput)`**

Email survey invitations to up to 300 participants. You can email either leads, contacts, or users in your org. Either a link to launch the
survey or a question can be embedded in the email invitations.

API Version

50.0

Requires Chatter

No


### Apex Reference Guide TaxPlatform Class

Signature

```
   public static ConnectApi.SurveyInvitationEmailOutput sendSurveyInvitationEmail(String

   surveyID, ConnectApi.SurveyInvitationEmailInput SurveyEmailInput)

```

Parameters

```
   surveyID
```

Type: String

ID of the survey.

```
   SurveyEmailInput
```

Type: `ConnectApi.SurveyInvitationEmailInput`

A `ConnectApi.SurveyInvitationEmailInput` object.

Return Value

Type: `ConnectApi.SurveyInvitationEmailOutput`

### TaxPlatform Class

Apply or cancel tax.

Namespace

ConnectApi

#### TaxPlatform Methods

### These methods are for TaxPlatform . All methods are static.

IN THIS SECTION:

##### calculateTax(calculateTax)

Apply tax or cancel tax.

##### **`calculateTax(calculateTax)`**

Apply tax or cancel tax.

API Version

55.0

Requires Chatter

No


### Apex Reference Guide Topics Class

Signature

```
   global static ConnectApi.CalculateTaxResponse calculateTax(ConnectApi.CalculateTaxRequest

   calculateTax)

```

Parameters

```
   calculateTax
```

Type: `ConnectApi.CalculateTaxRequest`

Represents a request to calculate tax for one or more line items.

Return Value

Type: `ConnectApi.CalculateTaxResponse`

### Topics Class

Access information about topics, such as their descriptions, the number of people talking about them, related topics, and information
about groups contributing to the topic. Update a topic’s name or description, merge topics, and add and remove topics from records
and feed items.

Namespace

ConnectApi

#### Topics Methods

### These methods are for Topics . All methods are static.

These methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

**•** `getGroupsRecentlyTalkingAboutTopic(communityId, topicId)`

**•** `getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)`

**•** `getRecentlyTalkingAboutTopicsForUser(communityId, userId)`

[All other methods in this class count toward the Salesforce Platform total API request allocations, which are per org and span a 24-hour](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
period.

IN THIS SECTION:

assignTopic(communityId, recordId, topicId)
Assign a topic to a record or feed item.

assignTopicByName(communityId, recordId, topicName)
Assign a topic to a record or feed item.

createTopic(communityId, name, description)
Create a topic.

createTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory, topicNames)
Create topic and article assignment rules by data category.


Apex Reference Guide Topics Class

deleteTopic(communityId, topicId)
Delete a topic.

getGroupsRecentlyTalkingAboutTopic(communityId, topicId)
Get information about the five groups that most recently contributed to a topic.

getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)
Get up to five topics most recently used in a group.

getRecentlyTalkingAboutTopicsForUser(communityId, userId)
Get up to five topics most recently used by a user.

getRelatedTopics(communityId, topicId)
Get up to five topics most closely related to a topic.

getTopic(communityId, topicId)
Get a topic.

getTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory)
Get topic and article assignment rules by data category.

getTopics(communityId, recordId)
Get the first page of topics assigned to a record or feed item.

getTopics(communityId)
Get the first page of topics for the org or Experience Cloud site.

getTopics(communityId, sortParam)
Get the first page of sorted topics for the org or community.

getTopics(communityId, pageParam, pageSize)
Get a page of topics.

getTopics(communityId, pageParam, pageSize, sortParam)
Get a page of sorted topics.

getTopics(communityId, q, sortParam)
Get the sorted topics that match the search criteria.

getTopics(communityId, q, pageParam, pageSize)
Get a page of topics that match the search criteria.

getTopics(communityId, q, pageParam, pageSize, sortParam)
Get a page of sorted topics that match the search criteria.

getTopics(communityId, q, exactMatch)
Get the topic that matches the exact, case-insensitive name.

getTopicsOrFallBackToRenamedTopics(communityId, q, exactMatch, fallBackToRenamedTopics)
Get the most recent renamed topic match, if there isn’t an exact match.

getTopicSuggestions(communityId, recordId, maxResults)
Get up to a specified number of suggested topics for a record or feed item.

getTopicSuggestions(communityId, recordId)
Get suggested topics for a record or feed item.

getTopicSuggestionsForText(communityId, text, maxResults)
Get up to a specified number of suggested topics for a string of text.


Apex Reference Guide Topics Class

getTopicSuggestionsForText(communityId, text)
Get suggested topics for a string of text.

getTrendingTopics(communityId)
Get trending topics for the org or Experience Cloud site.

getTrendingTopics(communityId, maxResults)
Get up to a specified number of trending topics for the org or Experience Cloud site.

mergeTopics(communityId, topicId, idsToMerge)
Merge up to five secondary topics with a primary topic.

reassignTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory, topicNames)
Reassign topic and article assignment rules by data category by deleting the existing rules and creating new rules.

reassignTopicsByName(communityId, recordId, topicNames)
Reassign all the topics on a record or feed item, that is, remove all the assigned topics on a record or feed item and add topics.
Optionally, provide a list of suggested topics to assign to a record or feed item to improve future topic suggestions.

unassignTopic(communityId, recordId, topicId)
Remove a topic from a record or feed item.

updateTopic(communityId, topicId, topic)
Update the description or name of a topic or merge up to five secondary topics with a primary topic.

updateTopicsForArticlesInDataCategory(communityId, dataCategoryGroup, dataCategory, articleTopicAssignmentJob)
Assign topics to articles and unassign topics from articles in a data category.

##### **`assignTopic(communityId, recordId, topicId)`**

Assign a topic to a record or feed item.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic assignTopic(String communityId, String recordId, String

   topicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.


Apex Reference Guide Topics Class

```
   topicId
```

Type: String

ID for a topic.

Return Value

Type: `ConnectApi.Topic`

Usage

Only users with the Assign Topics permission can add existing topics to records or feed items. Administrators must enable topics for
objects before users can add topics to records of that object type.

##### **`assignTopicByName(communityId, recordId, topicName)`**

Assign a topic to a record or feed item.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic assignTopicByName(String communityId, String recordId,

   String topicName)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

The ID of the record or feed item to which to assign the topic.

```
   topicName
```

Type: String

The name of a new or existing topic.

Return Value

Type: `ConnectApi.Topic`


Apex Reference Guide Topics Class

Usage

Only users with the Assign Topics permission can add existing topics to records or feed items. Only users with the Create Topics permission
can add new topics to records or feed items. Administrators must enable topics for objects before users can add topics to records of that
object type.

##### **`createTopic(communityId, name, description)`**

Create a topic.

API Version

36.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic createTopic(String communityId, String name, String

   description)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   name
```

Type: String

The name of the topic.

```
   description
```

Type: String

The description of the topic.

Return Value

Type: `ConnectApi.Topic`

Usage

Only users with the Create Topics permission can create a topic.

##### **`createTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory,`**

```
  topicNames)

```

Create topic and article assignment rules by data category.


Apex Reference Guide Topics Class

API Version

40.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage createTopicDataCategoryRules(String communityId,

   String dataCategoryGroup, String dataCategory, ConnectApi.TopicNamesInput topicNames)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   dataCategoryGroup
```

Type: String

The data category group used by articles.

```
   dataCategory
```

Type: String

The data category used by articles.

```
   topicNames
```

Type: `ConnectApi.TopicNamesInput`

A `ConnectApi.TopicNamesInput` object with the names of topics to assign to articles in a data category.

Return Value

Type: `ConnectApi.TopicPage`

##### **`deleteTopic(communityId, topicId)`**

Delete a topic.

API Version

29.0

Requires Chatter

No

Signature

```
   public static Void deleteTopic(String communityId, String topicId)

```


Apex Reference Guide Topics Class

Parameters

```
   communityId
```

Type: String,

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

Return Value

Type: Void

Usage

Only users with the Delete Topics or Modify All Data permission can delete topics.

Topic deletion is asynchronous. If a topic is requested before the deletion completes, the response is successful and the
`isBeingDeleted` property of `ConnectApi.Topic` is `true` in version 33.0 and later. If a topic is requested after the deletion
completes, the response is `ConnectApi.NotFoundException` .

##### **`getGroupsRecentlyTalkingAboutTopic(communityId, topicId)`**

Get information about the five groups that most recently contributed to a topic.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupSummaryPage

   getGroupsRecentlyTalkingAboutTopic(String communityId, String topicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.


Apex Reference Guide Topics Class

Return Value

Type: `ConnectApi.ChatterGroupSummaryPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetGroupsRecentlyTalkingAboutTopic(communityId, topicId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)`**

Get up to five topics most recently used in a group.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.TopicPage getRecentlyTalkingAboutTopicsForGroup(String

   communityId, String groupId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupId
```

Type: String

ID for a group.

Return Value

Type: `ConnectApi.TopicPage`


Apex Reference Guide Topics Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecentlyTalkingAboutTopicsForGroup(communityId, groupId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecentlyTalkingAboutTopicsForUser(communityId, userId)`**

Get up to five topics most recently used by a user.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.TopicPage getRecentlyTalkingAboutTopicsForUser(String

   communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for a user.

Return Value

Type: `ConnectApi.TopicPage`


Apex Reference Guide Topics Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecentlyTalkingAboutTopicsForUser(communityId, userId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRelatedTopics(communityId, topicId)`**

Get up to five topics most closely related to a topic.

Two topics that are assigned to the same feed item at least three times are related.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getRelatedTopics(String communityId, String topicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

Return Value

Type: `ConnectApi.TopicPage`


Apex Reference Guide Topics Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRelatedTopics(communityId, topicId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTopic(communityId, topicId)`**

Get a topic.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic getTopic(String communityId, String topicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

Return Value

Type: `ConnectApi.Topic`

##### **`getTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory)`**

Get topic and article assignment rules by data category.

API Version

40.0


Apex Reference Guide Topics Class

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopicDataCategoryRules(String communityId, String

   dataCategoryGroup, String dataCategory)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   dataCategoryGroup
```

Type: String

The data category group used by articles.

```
   dataCategory
```

Type: String

The data category used by articles.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, recordId)`**

Get the first page of topics assigned to a record or feed item.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, String recordId)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Topics Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.

Return Value

Type: `ConnectApi.TopicPage`

Usage

Administrators must enable topics for objects before users can add topics to records of that object type.

##### **`getTopics(communityId)`**

Get the first page of topics for the org or Experience Cloud site.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, sortParam)`**

Get the first page of sorted topics for the org or community.

API Version

29.0


Apex Reference Guide Topics Class

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, ConnectApi.TopicSort

   sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   sortParam
```

Type: `ConnectApi.TopicSort`

Values are:

**•** `popularDesc` —Sorts topics by popularity with the most popular first. This value is the default.

**•** `alphaAsc` —Sorts topics alphabetically.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, pageParam, pageSize)`**

Get a page of topics.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, Integer pageParam,

   Integer pageSize)

```


Apex Reference Guide Topics Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, pageParam, pageSize, sortParam)`**

Get a page of sorted topics.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, Integer pageParam,

   Integer pageSize, ConnectApi.TopicSort sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide Topics Class

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.TopicSort`

Values are:

**•** `popularDesc` —Sorts topics by popularity with the most popular first. This value is the default.

**•** `alphaAsc` —Sorts topics alphabetically.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, q, sortParam)`**

Get the sorted topics that match the search criteria.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, String q,

   ConnectApi.TopicSort sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Specifies the string to search. The string must contain at least two characters, not including wildcards.

```
   sortParam
```

Type: `ConnectApi.TopicSort`

Values are:

**•** `popularDesc` —Sorts topics by popularity with the most popular first. This value is the default.

**•** `alphaAsc` —Sorts topics alphabetically.


Apex Reference Guide Topics Class

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, q, pageParam, pageSize)`**

Get a page of topics that match the search criteria.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, String q, Integer

   pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Specifies the string to search. The string must contain at least two characters, not including wildcards.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, q, pageParam, pageSize, sortParam)`**

Get a page of sorted topics that match the search criteria.


Apex Reference Guide Topics Class

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, String q, Integer

   pageParam, Integer pageSize, ConnectApi.TopicSort sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Specifies the string to search. The string must contain at least two characters, not including wildcards.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.TopicSort`

Values are:

**•** `popularDesc` —Sorts topics by popularity with the most popular first. This value is the default.

**•** `alphaAsc` —Sorts topics alphabetically.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopics(communityId, q, exactMatch)`**

Get the topic that matches the exact, case-insensitive name.


Apex Reference Guide Topics Class

API Version

33.0

Available to Guest Users

33.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTopics(String communityId, String q, Boolean

   exactMatch)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Specifies the string to search. The string must contain at least two characters, not including wildcards.

```
   exactMatch
```

Type: Boolean

Specify `true` to find a topic by its exact, case-insensitive name.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopicsOrFallBackToRenamedTopics(communityId, q, exactMatch,`**

```
  fallBackToRenamedTopics)

```

Get the most recent renamed topic match, if there isn’t an exact match.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

No


Apex Reference Guide Topics Class

Signature

```
   public static ConnectApi.TopicPage getTopicsOrFallBackToRenamedTopics(String communityId,

   String q, Boolean exactMatch, Boolean fallBackToRenamedTopics)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Specifies the string to search. The string must contain at least two characters, not including wildcards.

```
   exactMatch
```

Type: Boolean

Specify `true` to find a topic by its exact, case-insensitive name or to find the most recent renamed topic match if there isn’t an
exact match.

```
   fallBackToRenamedTopics
```

Type: Boolean

Specify `true` and if there isn’t an exact match, the most recent renamed topic match is returned. If there are multiple renamed
topic matches, only the most recent is returned. If there are no renamed topic matches, an empty collection is returned.

Return Value

Type: `ConnectApi.TopicPage`

##### **`getTopicSuggestions(communityId, recordId, maxResults)`**

Get up to a specified number of suggested topics for a record or feed item.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicSuggestionPage getTopicSuggestions(String communityId,

   String recordId, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide Topics Class

```
   recordId
```

Type: String

ID for a record or feed item.

```
   maxResults
```

Type: Integer

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

Return Value

Type: `ConnectApi.TopicSuggestionPage`

Usage

Administrators must enable topics for objects before users can see suggested topics for records of that object type.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestions(communityId, recordId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTopicSuggestions(communityId, recordId)`**

Get suggested topics for a record or feed item.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicSuggestionPage getTopicSuggestions(String communityId,

   String recordId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.


Apex Reference Guide Topics Class

Return Value

Type: `ConnectApi.TopicSuggestionPage`

Usage

Administrators must enable topics for objects before users can see suggested topics for records of that object type.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestions(communityId, recordId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTopicSuggestionsForText(communityId, text, maxResults)`**

Get up to a specified number of suggested topics for a string of text.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicSuggestionPage getTopicSuggestionsForText(String

   communityId, String text, Integer maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

String of text.

```
   maxResults
```

Type: Integer

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

Return Value

Type: `ConnectApi.TopicSuggestionPage`


Apex Reference Guide Topics Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestionsForText(communityId, text, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTopicSuggestionsForText(communityId, text)`**

Get suggested topics for a string of text.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicSuggestionPage getTopicSuggestionsForText(String

   communityId, String text)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

String of text.

Return Value

Type: `ConnectApi.TopicSuggestionPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestionsForText(communityId, text, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Topics Class

##### **`getTrendingTopics(communityId)`**

Get trending topics for the org or Experience Cloud site.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTrendingTopics(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.TopicPage`

Usage

The more frequently people add a specific topic to their posts and comments and comment on or like posts with the same topic over
a short period, the more likely it is to become a trending topic. For example, if your coworkers are attending the upcoming Dreamforce
conference and have started discussing it in Chatter, you might see a trending topic for Dreamforce. A trending topic is not solely based
on popularity and usually relates to a one-time or infrequent event that has a spike in activity, such as a conference or a project deadline.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingTopics(communityId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTrendingTopics(communityId, maxResults)`**

Get up to a specified number of trending topics for the org or Experience Cloud site.

API Version

29.0


Apex Reference Guide Topics Class

Available to Guest Users

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage getTrendingTopics(String communityId, Integer

   maxResults)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   maxResults
```

Type: Integer

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

Return Value

Type: `ConnectApi.TopicPage`

Usage

The more frequently people add a specific topic to their posts and comments and comment on or like posts with the same topic over
a short period, the more likely it is to become a trending topic. For example, if your coworkers are attending the upcoming Dreamforce
conference and have started discussing it in Chatter, you might see a trending topic for Dreamforce. A trending topic is not solely based
on popularity and usually relates to a one-time or infrequent event that has a spike in activity, such as a conference or a project deadline.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingTopics(communityId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`mergeTopics(communityId, topicId, idsToMerge)`**

Merge up to five secondary topics with a primary topic.

API Version

33.0


Apex Reference Guide Topics Class

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic mergeTopics(String communityId, String topicId,

   List<String> idsToMerge)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

The ID for the primary topic for the merge. If this topic is a managed topic, it retains its topic type, topic images, and children topics.

```
   idsToMerge
```

Type: List<String>

A list of up to five comma-separated secondary topic IDs to merge with the primary topic. If any of the secondary topics are navigational
or featured topics, they lose their topic type, topic images, and children topics. Their feed items are reassigned to the primary topic.
If you merge a topic with a content topic, the content associations are preserved. If you merge a topic with an inactive endorsee,
the endorsement isn’t mapped to the primary topic.

Return Value

Type: `ConnectApi.Topic`

Usage

Only users with the Delete Topics or Modify All Data permission can merge topics.

##### **`reassignTopicDataCategoryRules(communityId, dataCategoryGroup, dataCategory,`**

```
  topicNames)

```

Reassign topic and article assignment rules by data category by deleting the existing rules and creating new rules.

API Version

40.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage reassignTopicDataCategoryRules(String communityId,

   String dataCategoryGroup, String dataCategory, ConnectApi.TopicNamesInput topicNames)

```


Apex Reference Guide Topics Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   dataCategoryGroup
```

Type: String

The data category group used by articles.

```
   dataCategory
```

Type: String

The data category used by articles.

```
   topicNames
```

Type: `ConnectApi.TopicNamesInput`

A `ConnectApi.TopicNamesInput` object with the names of topics to reassign to articles in a data category.

Return Value

Type: `ConnectApi.TopicPage`

##### **`reassignTopicsByName(communityId, recordId, topicNames)`**

Reassign all the topics on a record or feed item, that is, remove all the assigned topics on a record or feed item and add topics. Optionally,
provide a list of suggested topics to assign to a record or feed item to improve future topic suggestions.

API Version

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage reassignTopicsByName(String communityId, String

   recordId, ConnectApi.TopicNamesInput topicNames)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

The ID of the record or feed item to which to assign the topic.

```
   topicNames
```

Type: `ConnectApi.TopicNamesInput`


Apex Reference Guide Topics Class

A list of topics to replace the currently assigned topics. Optionally, a list of suggested topics to assign to improve future topic
suggestions.

Return Value

Type: `ConnectApi.TopicPage`

Usage

Only users with the Assign Topics permission can remove topics from records or feed items and add existing topics to records or feed
items. Only users with the Create Topics permission can add new topics to records or feed items. Administrators must enable topics for
objects before users can add topics to records of that object type.

##### **`unassignTopic(communityId, recordId, topicId)`**

Remove a topic from a record or feed item.

API Version

29.0

Requires Chatter

No

Signature

```
   public static Void unassignTopic(String communityId, String recordId, String topicId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.

```
   topicId
```

Type: String

ID for a topic.

Return Value

Type: Void

Usage

Only users with the Assign Topics permission can remove topics from feed items or records. Administrators must enable topics for objects
before users can add topics to records of that object type.


Apex Reference Guide Topics Class

##### **`updateTopic(communityId, topicId, topic)`**

Update the description or name of a topic or merge up to five secondary topics with a primary topic.

API Version

29.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Topic updateTopic(String communityId, String topicId,

   ConnectApi.TopicInput topic)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

```
   topic
```

Type: `ConnectApi.TopicInput`

A `ConnectApi.TopicInput` object containing the name and description of the topic or up to five comma-separated secondary
topic IDs to merge with the primary topic.

Return Value

Type: `ConnectApi.Topic`

Usage

Only users with the Edit Topics or Modify All Data permission can update topic names and descriptions. Only users with the Delete Topics
or Modify All Data permission can merge topics.

##### **`updateTopicsForArticlesInDataCategory(communityId, dataCategoryGroup,`**

```
  dataCategory, articleTopicAssignmentJob)

```

Assign topics to articles and unassign topics from articles in a data category.

API Version

40.0


Apex Reference Guide Topics Class

Requires Chatter

No

Signature

```
   public static ConnectApi.TopicPage updateTopicsForArticlesInDataCategory(String

   communityId, String dataCategoryGroup, String dataCategory,

   ConnectApi.ArticleTopicAssignmentJobInput articleTopicAssignmentJob)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   dataCategoryGroup
```

Type: String

The data category group used by articles.

```
   dataCategory
```

Type: String

The data category used by articles.

```
   articleTopicAssignmentJob
```

Type: `ConnectApi.ArticleTopicAssignmentJobInput`

A `ConnectApi.ArticleTopicAssignmentJobInput` object that indicates the operation to take on which topics.

Return Value

Type: `ConnectApi.TopicPage`

#### Topics Test Methods These test methods are for Topics . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetGroupsRecentlyTalkingAboutTopic(communityId, topicId, result)`**

Register a `ConnectApi.ChatterGroupSummaryPage` object to be returned when the matching
`ConnectApi.getGroupsRecentlyTalkingAboutTopic` method is called in a test context. Use the method with the
same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetGroupsRecentlyTalkingAboutTopic(String communityId, String

   topicId, ConnectApi.ChatterGroupSummaryPage result)

```


Apex Reference Guide Topics Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

```
   result
```

Type: `ConnectApi.ChatterGroupSummaryPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getGroupsRecentlyTalkingAboutTopic(communityId, topicId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecentlyTalkingAboutTopicsForGroup(communityId, groupId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching
`ConnectApi.getRecentlyTalkingAboutTopicsForGroup` method is called in a test context. Use the method with
the same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetRecentlyTalkingAboutTopicsForGroup(String communityId,

   String groupId, ConnectApi.TopicPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupId
```

Type: String

ID for a group.

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.


Apex Reference Guide Topics Class

Return Value

Type: Void

SEE ALSO:

getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecentlyTalkingAboutTopicsForUser(communityId, userId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching
`ConnectApi.getRecentlyTalkingAboutTopicsForUser` method is called in a test context. Use the method with the
same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetRecentlyTalkingAboutTopicsForUser(String communityId,

   String userId, ConnectApi.TopicPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for a user.

```
   result
```

Type: `ConnectApi.TopicPage`

Specify the test topics page.

Return Value

Type: Void

SEE ALSO:

getRecentlyTalkingAboutTopicsForUser(communityId, userId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRelatedTopics(communityId, topicId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching `ConnectApi.getRelatedTopics` method
is called in a test context. Use the method with the same parameters or you receive an exception.


Apex Reference Guide Topics Class

API Version

29.0

Signature

```
   public static Void setTestGetRelatedTopics(String communityId, String topicId,

   ConnectApi.TopicPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   topicId
```

Type: String

ID for a topic.

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRelatedTopics(communityId, topicId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTopicSuggestions(communityId, recordId, maxResults, result)`**

Register a `ConnectApi.TopicSuggestionPage` object to be returned when the matching
`ConnectApi.getTopicSuggestions` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetTopicSuggestions(String communityId, String recordId,

   Integer maxResults, ConnectApi.TopicSuggestionPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide Topics Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.

```
   maxResults
```

Type: Integer

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

```
   result
```

Type: `ConnectApi.TopicSuggestionPage`

Specify the test topic suggestions page.

Return Value

Type: Void

SEE ALSO:

getTopicSuggestions(communityId, recordId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTopicSuggestions(communityId, recordId, result)`**

Register a `ConnectApi.TopicSuggestionPage` object to be returned when the matching
`ConnectApi.getTopicSuggestions` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetTopicSuggestions(String communityId, String recordId,

   ConnectApi.TopicSuggestionPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   recordId
```

Type: String

ID for a record or feed item.

```
   result
```

Type: `ConnectApi.TopicSuggestionPage`


Apex Reference Guide Topics Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopicSuggestions(communityId, recordId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTopicSuggestionsForText(communityId, text, maxResults, result)`**

Register a `ConnectApi.TopicSuggestionPage` object to be returned when the matching
`ConnectApi.getTopicSuggestionsForText` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetTopicSuggestionsForText(String communityId, String text,

   Integer maxResults, ConnectApi.TopicSuggestionPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

String of text.

```
   maxResults
```

Type: Integer

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

```
   result
```

Type: `ConnectApi.TopicSuggestionPage`

Object containing test data.


Apex Reference Guide Topics Class

Return Value

Type: Void

SEE ALSO:

getTopicSuggestionsForText(communityId, text, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTopicSuggestionsForText(communityId, text, result)`**

Register a `ConnectApi.TopicSuggestionPage` object to be returned when the matching
`ConnectApi.getTopicSuggestionsForText` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetTopicSuggestionsForText(String communityId, String text,

   ConnectApi.TopicSuggestionPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

String of text.

```
   result
```

Type: `ConnectApi.TopicSuggestionPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopicSuggestionsForText(communityId, text)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTrendingTopics(communityId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching `ConnectApi.getTrendingTopics`
method is called in a test context. Use the method with the same parameters or you receive an exception.


Apex Reference Guide Topics Class

API Version

29.0

Signature

```
   public static Void setTestGetTrendingTopics(String communityId, ConnectApi.TopicPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTrendingTopics(communityId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTrendingTopics(communityId, maxResults, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching `ConnectApi.getTrendingTopics`
method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestGetTrendingTopics(String communityId, Integer maxResults,

   ConnectApi.TopicPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   maxResults
```

Type: Integer


### Apex Reference Guide UserProfiles Class

Maximum number of topic suggestions that get returned. The default is 5. Value must be greater than 0 and less than or equal to
25.

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTrendingTopics(communityId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### UserProfiles Class

Access user profile data. The user profile data populates the profile page (also called the Chatter profile page). This data includes user
information (such as address, manager, and phone number), some user capabilities (permissions), and a set of subtab apps, which are
custom tabs on the profile page.

Namespace

ConnectApi

#### UserProfiles Methods

### These methods are for UserProfiles . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

deleteBannerPhoto(communityId, userId)
Delete a user’s banner photo.

deletePhoto(communityId, userId)
Delete a user’s photo.

getBannerPhoto(communityId, userId)
Get a user’s banner photo.

getPhoto(communityId, userId)
Get a user’s photo.

getUserProfile(communityId, userId)
Get the user profile of the context user.

setBannerPhoto(communityId, userId, fileId, versionNumber)
Set an uploaded file as a user’s banner photo.


Apex Reference Guide UserProfiles Class

setBannerPhoto(communityId, userId, fileUpload)
Set a file that hasn’t been uploaded as a user’s banner photo.

setBannerPhotoWithAttributes(communityId, userId, bannerPhoto)
Set and crop an uploaded file as a user’s banner photo.

setBannerPhotoWithAttributes(communityId, userId, bannerPhoto, fileUpload)
Set and crop a file that hasn’t been uploaded as a user’s banner photo.

setPhoto(communityId, userId, fileId, versionNumber)
Set an uploaded file as a user’s photo.

setPhoto(communityId, userId, fileUpload)
Set a file that hasn’t been uploaded as a user’s photo.

setPhotoWithAttributes(communityId, userId, photo)
Set and crop an uploaded file as a user’s photo.

setPhotoWithAttributes(communityId, userId, photo, fileUpload)
Set and crop a file that hasn’t been uploaded as a user’s photo.

##### **`deleteBannerPhoto(communityId, userId)`**

Delete a user’s banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static Void deleteBannerPhoto(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

Return Value

Type: Void


Apex Reference Guide UserProfiles Class

##### **`deletePhoto(communityId, userId)`**

Delete a user’s photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static Void deletePhoto(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

Return Value

Type: Void

##### **`getBannerPhoto(communityId, userId)`**

Get a user’s banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto getBannerPhoto(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide UserProfiles Class

```
   userId
```

Type: String

ID of the user.

Return Value

Type: `ConnectApi.BannerPhoto`

##### **`getPhoto(communityId, userId)`**

Get a user’s photo.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo getPhoto(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for a user.

Return Value

Type: `ConnectApi.Photo`

##### **`getUserProfile(communityId, userId)`**

Get the user profile of the context user.

API Version

29.0


Apex Reference Guide UserProfiles Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserProfile getUserProfile(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for a user.

Return Value

Type: `ConnectApi.UserProfile`

##### **`setBannerPhoto(communityId, userId, fileId, versionNumber)`**

Set an uploaded file as a user’s banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String communityId, String userId,

   String fileId, Integer versionNumber)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

```
   fileId
```

Type: String


Apex Reference Guide UserProfiles Class

ID of the uploaded file to use as the user banner. The key prefix must be 069, and the image must be smaller than 8 MB.

```
   versionNumber
```

Type: Integer

Version number of the file. Specify an existing version number or, to get the latest version, specify `null` .

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhoto(communityId, userId, fileUpload)`**

Set a file that hasn’t been uploaded as a user’s banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String communityId, String userId,

   ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.BannerPhoto`


Apex Reference Guide UserProfiles Class

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhotoWithAttributes(communityId, userId, bannerPhoto)`**

Set and crop an uploaded file as a user’s banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String communityId,

   String userId, ConnectApi.BannerPhotoInput bannerPhoto)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

```
   bannerPhoto
```

Type: `ConnectApi.BannerPhotoInput`

A `ConnectApi.BannerPhotoInput` object that specifies the ID and version of the file, and how to crop the file.

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhotoWithAttributes(communityId, userId, bannerPhoto, fileUpload)`**

Set and crop a file that hasn’t been uploaded as a user’s banner photo.

API Version

36.0


Apex Reference Guide UserProfiles Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String communityId,

   String userId, ConnectApi.BannerPhotoInput bannerPhoto, ConnectApi.BinaryInput

   fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID of the user.

```
   bannerPhoto
```

Type: `ConnectApi.BannerPhotoInput`

A `ConnectApi.BannerPhotoInput` object specifying the cropping parameters.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhoto(communityId, userId, fileId, versionNumber)`**

Set an uploaded file as a user’s photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhoto(String communityId, String userId, String

   fileId, Integer versionNumber)

```


Apex Reference Guide UserProfiles Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   fileId
```

Type: String

ID of an uploaded file. The file must be an image, and be smaller than 2 GB.

```
   versionNumber
```

Type: Integer

Version number of the existing file. Specify either an existing version number, or `null` to get the latest version.

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhoto(communityId, userId, fileUpload)`**

Set a file that hasn’t been uploaded as a user’s photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhoto(String communityId, String userId,

   ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String


Apex Reference Guide UserProfiles Class

ID for the context user or the keyword `me` .

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(communityId, userId, photo)`**

Set and crop an uploaded file as a user’s photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String communityId, String userId,

   ConnectApi.PhotoInput photo)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object specifying the file ID, version number, and cropping parameters.

Return Value

Type: `ConnectApi.Photo`


### Apex Reference Guide Zones Class

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(communityId, userId, photo, fileUpload)`**

Set and crop a file that hasn’t been uploaded as a user’s photo.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String communityId, String userId,

   ConnectApi.PhotoInput photo, ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   userId
```

Type: String

ID for the context user or the keyword `me` .

```
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object specifying the cropping parameters.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

### Zones Class

Access information about Chatter Answers zones in your organization. Zones organize questions into logical groups, with each zone
having its own focus and unique questions.


Apex Reference Guide Zones Class

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

Namespace

ConnectApi

#### Zones Methods These methods are for Zones . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### getZone(communityId, zoneId)

Get a zone.

getZones(communityId)
Get a list of zones.

getZones(communityId, pageParam, pageSize)
Get a page of zones.

searchInZone(communityId, zoneId, q, filter)
Search articles or questions in a zone.

searchInZone(communityId, zoneId, q, filter, pageParam, pageSize)
Search a page of articles or questions in a zone.

searchInZone(communityId, zoneId, q, filter, language)
Search articles or questions in a zone, and specify the language of the results.

##### **`getZone(communityId, zoneId)`**

Get a zone.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Zone getZone(String communityId, String zoneId)

```


Apex Reference Guide Zones Class

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

The ID of a zone.

Return Value

Type: `ConnectApi.Zone`

##### **`getZones(communityId)`**

Get a list of zones.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ZonePage getZones(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ZonePage`

##### **`getZones(communityId, pageParam, pageSize)`**

Get a page of zones.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)


Apex Reference Guide Zones Class

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Zone getZones(String communityId, Integer pageParam, Integer

   pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ZonePage`

##### **`searchInZone(communityId, zoneId, q, filter)`**

Search articles or questions in a zone.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0

Available to Guest Users

37.0

Requires Chatter

Yes


Apex Reference Guide Zones Class

Signature

```
   public static ConnectApi.ZoneSearchPage searchInZone(String communityId, String zoneId,

   String q, ConnectApi.ZoneSearchResultType filter)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

A `ZoneSearchResultType` enum value. One of the following:

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

Return Value

Type: `ConnectApi.ZoneSearchPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchInZone(communityId, zoneId, q, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchInZone(communityId, zoneId, q, filter, pageParam, pageSize)`**

Search a page of articles or questions in a zone.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

29.0


Apex Reference Guide Zones Class

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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


Apex Reference Guide Zones Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchInZone(communityId, zoneId, q, filter, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchInZone(communityId, zoneId, q, filter, language)`**

Search articles or questions in a zone, and specify the language of the results.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

36.0

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.ZoneSearchResultType`

**•** `Article` —Search results contain only articles.


Apex Reference Guide Zones Class

**•** `Question` —Search results contain only questions.

```
   language
```

Type: String

The language of the articles or questions. The value must be a Salesforce supported locale code.

Return Value

Type: `ConnectApi.ZoneSearchPage`

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchInZone(communityId, zoneId, q, filter, language, result)

#### Zones Test Methods These test methods are for Zones . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Zones Class

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

Return Value

Type: Void

SEE ALSO:

searchInZone(communityId, zoneId, q, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Zones Class

```
   zoneId
```

Type: String

The ID of a zone.

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchInZone(communityId, zoneId, q, filter, language, result)`**

Register a `ConnectApi.ZoneSearchPage` object to be returned when `searchInZone(communityId, zoneId,`
`q, filter, language)` is called in a test context. Use the method with the same parameters or you receive an exception.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

API Version

36.0


### Apex Reference Guide ConnectApi Input Classes

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

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ConnectApi Input Classes Some ConnectApi methods take arguments that are instances of ConnectApi input classes.

Input classes are concrete unless marked abstract in this documentation. Concrete input classes have public constructors that have no
parameters.

Some methods have parameters that are typed with an abstract class. You must pass in an instance of a concrete child class for these
parameters.


Apex Reference Guide ConnectApi Input Classes

Most input class properties can be set. Read-only properties are noted in this documentation.

#### ConnectApi.AbstractBaseSequenceInputRepresentation

The sequence for refunds and payment credits.

This class is abstract.

Superclass of:

**•** ConnectApi.RefundSequenceItemInputRepresentation

**•** ConnectApi.PaymentCreditSequenceItemInputRepresentation

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


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.AbstractList

Primitive list input.

This class is abstract.

Superclass of:

**•** ConnectApi.BooleanList

**•** ConnectApi.DoubleList

**•** ConnectApi.LongList

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


Required 33.0

Can be defined in an
action link template.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

[Action Link resource in the Connect](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)
[REST API Developer Guidefor more](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)
information.

`actionUrl` String

`excludedUserId` String

`groupDefault` Boolean

The action link URL. For example, a `Ui`
action link URL is a Web page. A
`Download` action link URL is a link to the
file to download. `Ui` and `Download`

action link URLs are provided to clients. An
`Api` or `ApiAsync` action link URL is a
REST resource. `Api` and `ApiAsync`
action link URLs aren’t provided to clients.
Links to Salesforce can be relative. All other
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

ID of a single user to exclude from
performing the action. If you specify an
`excludedUserId`, you can’t specify a
`userId` .

`true` if this action is the default action link
in the action link group; `false` otherwise.
There can be only one default action link
per action link group. The default action link
gets distinct styling in the Salesforce UI.


Required 33.0

Can be defined in an
action link template.

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

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

The request headers for the `Api` and
`ApiAsync` action link types.

[See Action Links Overview, Authentication,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_action_links_overview.htm)
[and Security.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_action_links_overview.htm)

Key for the set of labels to show in the user
interface. A set includes labels for these
states: NewStatus, PendingStatus,
SuccessStatus, FailedStatus. For example, if

you use the `Approve` key, you get these
labels: Approve, Pending, Approved, Failed.

For a complete list of keys and labels, see
[Action Links Labels.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)

If none of the predefined labels work for
your action link, use a custom label. To use
a custom label, create an action link
[template. See Create Action Link Templates.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/action_link_group_template_create.htm)

Optional 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

```
headers

```

List< `ConnectApi.`

```
RequestHeader
```

`Input` 

`labelKey` String

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`requestBody` String The request body for `Api` action links.

Note: Escape quotation mark
characters in the `requestBody`
value.

`requires` Boolean `true` to require the user to confirm the
`Confirmation` action; `false` otherwise.

`userId` String

SEE ALSO:

The ID of the user who can execute the
action. If not specified or `null`, any user
can execute the action. If you specify a
`userId`, you can’t specify an
`excludedUserId` .

Optional 33.0

Can be defined in an
action link template.

Required 33.0

Can be defined in an
action link template.

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


action link group
without a template.

To instantiate from a
template, don’t
specify a value.

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

You can create up to three action links in a
`Primary` group and up to four in an
`Overflow` group.

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

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)

[Define an Action Link in a Template and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link_template.htm)

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

#### ConnectApi.AssociatedActionsCapabilityInput

A list of action link groups to associate with a feed element. To associate an action link group with a feed element, the call must be made
from the Apex namespace that created the action link definition. In addition, the user making the call must have created the definition
or have View All Data permission.

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke an
API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body and
header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services into the
feed so that users can drive productivity and accelerate innovation.

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

#### ConnectApi.AudienceCriteriaInput

Custom recommendation audience criteria type.

This class is abstract and has no public constructor. You can make an instance only of a subclass.

Superclass for:

**•** ConnectApi.CustomListAudienceCriteriaInput

**•** ConnectApi.NewUserAudienceCriteriaInput


Apex Reference Guide ConnectApi Input Classes

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

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `NotIncludes`

**•** `StartsWith`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

[Post a Batch of Feed Elements](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_batch.htm)

[Post a Batch of Feed Elements with a New (Binary) File](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_batch_binary.htm)

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

[Post a Feed Element with a New File (Binary) Attachment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_binary.htm)

[Post a Comment with a New File](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_3.htm)

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
on page 1982

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

on page 1981>

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

on page 1951

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
on page 1951

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
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

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
with ResultCode on page 559 value as
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

`on page 1990`           

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
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

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
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`shippingAddress` `ConnectApi.CartShippingAddressInputRepresentation` Shipping address for a cart. Required 63.0

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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
[Create a Cart and Cart Item with Custom](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Fields in a Commerce Store.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`productId` String ID of the product.

Required when 49.0
adding an item to a
cart

Not supported when
updating a cart item

`productSellingModelId` String The ID of the product selling model Optional 59.0
associated with Product2.

`quantity` String Quantity of the cart item. Use a value that Required 49.0
can be converted to BigDecimal.

`subscriptionTerm` Integer on page 3819 The total number of terms in the Optional 59.0
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


Apex Reference Guide ConnectApi Input Classes

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

#### ConnectApi.CartInput

A cart.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`currencyIsoCode` String Currency ISO code of the cart. Optional 57.0

`customFields` List< `SObject` - Array of sObjects and custom fields for the Optional 61.0
sObjects. Standard fields are ignored. The

custom fields must already be defined for
the sObject. Currently, only the WebCart
sObject is supported. Field-level security
[rules from the shopper profile are applied](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
to the custom fields. The rules are applied
for registered shoppers and for the guest
[shopper profile. See Create a Cart and Cart](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Item with Custom Fields in a Commerce](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)
[Store.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_commerce_cart_custom.htm)

`effective` String ID of the buyer account or guest buyer Optional 49.0
`AccountId` profile for which the request is made. If


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

unspecified, the default value is determined
from context.

`isSecondary` Boolean

`name` String

Specifies whether the cart is secondary Optional 53.0
( `true` ) or not ( `false` ). If unspecified,
defaults to `false` .

Name of the cart. The name can have up to Optional 49.0
250 Unicode characters. If unspecified,
defaults to the generated name.

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### partyIdentification ConnectApi. Party Identifier information. Optional 57.0

```
   Info CdpIdentityResolution

            MatchCriterionParty

            IdentificationInfo

```

`shouldMatch` Boolean Specifies whether blank fields can be used Required 57.0
`OnBlank` for matching ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.CdpIdentityResolutionMatchRule ConnectApi.CdpIdentityResolutionMatchCriterionPartyIdentificationInfo

Input representation for information when party identification is used in an identity resolution ruleset's match rule criterion.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`partyName` String Party identification name. Required if the 57.0
match rule criterion

uses party
identification for
matching

`partyType` String Party identification type. Optional 57.0

SEE ALSO:

#### ConnectApi.CdpIdentityResolutionMatchCriterion ConnectApi.CdpIdentityResolutionMatchRule

Input representation for an identity resolution ruleset’s match rule.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
criteria

```

#### List< ConnectApi. Object and field the match rule applies to Required 57.0

`CdpIdentityResolution` and the match method applied.
`MatchCriterion` 


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

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

#### settings ConnectApi.CdpMlPredictSettingsInput The model configuration settings to use to Optional 59.0

generate the prediction.

`type` `CdpMlPredictTypeEnum` Type of input data for the prediction. Required 59.0

**•** `RawData` -Raw data.

**•** `RecordOverrides` -Record IDs with
user-provided overrides.

**•** `Records` -Record IDs.

SEE ALSO:

predict(predict)

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
models

```

SEE ALSO:

#### List< ConnectApi. List of models. The segment data build tool Required 55.0

`CdpSegmentDbt` currently supports a single SQL model.
`ModelInput` 

ConnectApi.CdpSegmentInput

#### ConnectApi.CdpSegmentDbtModelInput

Segment dbt model input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Dbt model name. Required 55.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`sql` String

SEE ALSO:

ConnectApi.CdpSegmentDbtInput

Dbt SQL. Required 55.0

Dbt SQL date strings must be in ISO 8601
format, for example,
2011-02-25T18:24:31.000Z.

For details about supported validations, see
[Supported Validations for Segment Data](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_cdp_cbt_validations.htm)
[Build Tool Model SQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_cdp_cbt_validations.htm)

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

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
prorated for the quantity being
returned.

`description` String Description of the fee. Required 57.0

`priceBookEntryId` String ID of the price book entry associated with
the fee product.

Required unless 57.0
price books are
optional in the org

`product2Id` String ID of the product representing the fee. Required 57.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

#### ConnectApi.ChangeItemFeeWithTaxInputRepresentation

Input representation of a change item fee with taxes.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`amount` Double Positive value used to calculate the fee Required 63.0
amount.

#### changeItemFeeTaxes <List ConnectApi.ChangeItemFeeTaxInputRepresentation > List of taxes associated with the change item Required 63.0

fees.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available**

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

Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.CommentCapabilitiesInput

A container for all capabilities that can be included with a comment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`content` `ConnectApi.ContentCapabilityInput` Content to attach to the comment. Optional 32.0

`feedEntityShare` `ConnectApi.FeedEntityShareCapabilityInput` Feed entity to share to the comment. Optional 42.0

`record` `ConnectApi.RecordCapabilityInput` Existing knowledge article to attach to the Optional 42.0
comment.

SEE ALSO:

#### ConnectApi.CommentInput ConnectApi.CommentInput

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

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

`threadParentId` String ID of the parent comment for a threaded Optional 44.0
comment.

SEE ALSO:

[Post a Comment with a Mention](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_2.htm)

[Post a Comment with a New File](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_3.htm)

[Post a Comment with an Existing File](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_feed_element_4.htm)

[Post a Rich-Text Comment with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_richtext_inlineimage.htm)

[Post a Rich-Text Feed Comment with a Code Block](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_comment_richtext_code_snippet.htm)

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

#### ConnectApi.CompositeCommerceProductInputRepresentation

Composite product input.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### attributeSetInfo ConnectApi. Attribute set information for a variation Optional 62.0

`ProductAttributeSetInputRepresentation` parent product.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`categoryIds` List<String> List of category IDs associated with the Optional 61.0
product.

`productFields` Map<String, String> A map of product field names and their Required 61.0
values.

#### productMedia ConnectApi. Media associated with the product. Optional 61.0

```
            ProductMedia

#### ConnectApi.ConfirmHeldFOCapacityInputRepresentation

```

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

ConnectApi.ContactPointAttributeInput

Represents the attribute of an activation contact point.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String Label of the attribute. 60.0

`name` String Name of the attribute. 60.0

`preferredName` String Preferred name of the attribute. 60.0

ConnectApi.ContactPointSourceInput

Represents the configuration input for contact point sources.


Apex Reference Guide ConnectApi Input Classes

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

`title` String

SEE ALSO:

Title of the file. This value is used as the file Required for new 32.0
name for new content. For example, if the content
title is My Title, and the file is a .txt file, the
file name is My Title.txt.

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.ContentHubFieldValueInput

Fields of the item type.


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`changeOrderIds` List<String> List of IDs of change orders to create Required 56.0
Invoices for.

`orderSummaryId` String ID of the associated Order Summary. Required 56.0

SEE ALSO:

createMultipleInvoices(invoicesInput)

#### ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation ConnectApi.CreateMultipleInvoicesFromChangeOrdersInputRepresentation

Data about the change orders to create Invoices for.


Apex Reference Guide ConnectApi Input Classes

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

`paymentIds` List<String> List of IDs of the payments. Either a payment 48.0
authorization or at

least one payment is
required.

SEE ALSO:

createOrderPaymentSummary(orderPaymentSummaryInput)

#### ConnectApi.CreateServiceAppointmentInput

Contains information to create a service appointment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`assignedResources` <List `ConnectApi.AssignedResourcesInput`    - Represents the service resources to be Optional 53.0
assigned to a service appointment.

Note: When creating an
appointment, use

`extendedFields` to add values


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

authentication

ProtocolVariant

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

**•** `Custom`

**•** `Jwt`

**•** `OAuth`

#### ConnectApi. Authentication protocol variant of the Optional 57.0

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


**•** `AwsSv4`

**•** `Basic`

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

**•** `RolesAnywhere` —AWS Signature
Version 4 with Identity and Access
Management (IAM) Roles Anywhere.

If specified, the authentication protocol
variant must match the actual protocol
variant of the external credential.

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

```
credentials

```

Map<String,

#### `ConnectApi.`

```
Credential
```

`ValueInput` 

`externalCredential` String Fully qualified developer name of the Required 56.0
external credential.

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

#### ConnectApi.CuratedEntityInput

Represents the input details for a curated entity.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`label` String DMO label of the curated entity. 60.0

`name` String DMO API name of the curated entity. 60.0

#### ConnectApi.CustomListAudienceCriteriaInput

Criteria for the custom list type of custom recommendation audience.

Subclass of ConnectApi.AudienceCriteriaInput.


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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
`PickedList` `on page 2056` 
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
on page 2024

`locations` String List of location external references. Optional 63.0

`products` ConnectApi.DeliveryEstimationProductInputRepresentation List of products included in delivery Required 63.0
on page 2025 estimation.

`shippingCarrier` ConnectApi.ShippingCa **r** ierInputRepresentation Shipping carrier used to deliver the order. Required 63.0
on page 2123


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
on page 2035>

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

page 2608

#### ConnectApi. Authentication protocol required to access Required 62.0

`IdentityProvider` the external system. Values are:

```
AuthProtocol
```

**•** `OAuth`

on page 2608

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

[Post a Feed Element with a Mention](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_mention.htm)

[Post a Feed Element with Existing Content](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_content.htm)

[Post a Feed Element with a New File (Binary) Attachment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_binary.htm)

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)

[Define an Action Link in a Template and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link_template.htm)

[Share a Feed Element (in Version 39.0 and Later)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_share_feed_element_comment.htm)

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

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

#### ConnectApi.FileIdInput

Attach a file that has already been uploaded or remove a file from a feed element.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`id` String ID of a file that has already been uploaded. Required 36.0

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### items List< ConnectApi. List of file IDs and operations to be carried Required 36.0

`FileIdInput`           - out on those files.

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`excludeLocations` List< `String`    - List of locations to exclude from the routing Optional 55.0
calculations.

`maximumNumber` Integer

```
OfSplits

#### orderedItems <List ConnectApi.FindRoutesWithFewestSplits
```

`UsingOCIItemInputRepresentation`                   

SEE ALSO:

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

Each list element represents a quantity of a At least one element 54.0
product to be routed for fulfillment and the is required
assigned location group or location.

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation

#### ConnectApi.FindRoutesWithFewestSplitsInputRepresentation

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`findRoutesWithFewestSplitsUsingOCIInputs` < `ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation` List  - Each list element represents a routing At least one element 54.0
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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.FormSubmissionFieldInput

Marketing integration form field submission.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the marketing integration form Required 53.0
field.

`value` String Value of the marketing integration form Required 53.0
field.

SEE ALSO:

#### ConnectApi.FormSubmissionInput ConnectApi.FormSubmissionInput

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.GroupInformationInput

Chatter group information input.

**Property** **Type** **Description** **Available Version**

`text` String The text in the “Information” section of a group. 28.0

`title` String The title of the “Information” section of a group. 28.0

SEE ALSO:

ConnectApi.ChatterGroupInput

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


Apex Reference Guide ConnectApi Input Classes

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

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

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

#### ConnectApi.LocationInputRepresentation

Inventory location data used to calculate shipping distance.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`countryCode` String The country code of the location. Required 51.0

`locationIdentifier` String The identifier of the location. Required 51.0

`postalCode` String The postal code of the location. Required 51.0

#### ConnectApi.LongList

List of long values.

Subclass of ConnectApi.AbstractList.

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
page 2609

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

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

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

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

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

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

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

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

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

`strategyContext` Map<String, String> Variable and value mappings for the Optional 45.0
strategy.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

on page 2082 []

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

`querySettings` Map<String, String> Settings to allow the adjustment of query Optional 62.0
execution, such as date and time. For


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

example, `lc_time`, `date_style`, and
`external_client_context` .

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

**•** `Numeric`

**•** `Oid`

**•** `SmallInt`

**•** `Time`

**•** `Timestamp`

**•** `TimestampTZ`

**•** `Unspecified`

**•** `Varchar`


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`value` String Value of the SQL parameter. Required 62.0

#### ConnectApi.QuestionAndAnswersCapabilityInput

Create or edit a question feed element or set the best answer of the existing question feed element.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`bestAnswerId` String

`questionTitle` String

SEE ALSO:

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`attributeType` String Type of search attribute for the refinement. Required 64.0
Values are:

**•** `Custom`

**•** `Standard`

**•** `PricebookEntry`

`max` String Maximum value for range refinement. Required if `min` isn't 64.0
specified


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`isReadByMe` Boolean Specifies to mark the feed element as read Required 40.0
( `true` ) for the context user.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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
`on page 2087`        

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
`on page 2102`        

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

`paymentCreditSequenceItems` List< The Order Payment Summary ID, credit 65.0
`ConnectApi.PaymentCreditSequenceItemInputRepresentation`                                 - amount, and credit type for individual

payment credit items. Each item represents
a specific payment method and the amount
of credit to be applied to it.

`refundSequenceItems` <List `ConnectApi.RefundSequenceItemInputRepresentation` - The Order Payment Summary ID and 65.0
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

[Define an Action Link and Post with a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_define_post_action_link.htm)


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ReturnItemsInputRepresentation

Data about products and delivery charges to return, as well as associated return fees.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
returnOrderItem

DeliveryCharges

returnOrderItemFees

returnOrderItems

```

SEE ALSO:

#### List< ConnectApi. List of ReturnOrderLineItems to return that Optional 52.0

`ReturnOrderItem` represent delivery charges.

```
DeliveryCharge
```

`InputRepresentation` 
#### List< ConnectApi. List of ReturnOrderLineItems to process that Optional 56.0

`ReturnOrderItemFee` represent return fees.
`InputRepresentation` 

#### List< ConnectApi.

```
ReturnOrderItem
```

`InputRepresentation` 

List of ReturnOrderLineItems to process that Required 52.0
represent products, along with data about
how to process them.

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderInputRepresentation

Data for creating a ReturnOrder and ReturnOrderLineItems.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`orderSummaryId` String

ID of the OrderSummary containing the Required 50.0
items to be returned. The OrderSummary’s
OrderLifeCycleType must be Managed.

`returnOrder` String The LifeCycleType of the ReturnOrder. Required 51.0
`LifeCycleType` Possible values are:

**•** Managed—Process the ReturnOrder
using the APIs and actions. It can
generate change orders and affects
financial fields and rollup calculations.

**•** Unmanaged—The ReturnOrder is for
tracking purposes only. It isn’t involved
in any financial calculations and doesn’t
generate any change orders. The system
doesn’t prevent the creation of
duplicate ReturnOrderLineItems in an
unmanaged ReturnOrder for the same
OrderItem.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

```
returnOrderLineItems

```

#### List< ConnectApi. List of data for creating At least one element 50.0

`ReturnOrderLineItem` ReturnOrderLineItems. is required
`InputRepresentation` 

`status` String

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
fee amount is $10 and the expected
quantity is 2, then if the
`quantityReturned` is 1, $5 is charged.
This value normally equals the quantity
returned of the ReturnOrderLineItem for the
returned item that the fee applies to. The
value must be greater than zero. If this value


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

`quantityRejected` Double The quantity of the ReturnOrderLineItem Optional 52.0
that has been rejected for return. The value

must be zero or greater. This value isn’t used
by any standard features, but is provided for
use in customizations.

`quantityReturned` Double The quantity of the ReturnOrderLineItem Required 52.0
that has been returned. The value must be

greater than zero. If this value plus


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

associated ReturnOrderLineItem, then you
must specify a different
`reasonForReturn` . Duplicating the
reason breaks the financial calculations.

`quantityExpected` Double

Quantity expected to be returned. This value Required 50.0
also applies to any fees specified in
`returnOrderLineItemFees` .

`quantityReceived` Double Quantity already physically returned. Optional 50.0


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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
including tax. Tax is calculated on the
value and added.

**•** `Percentage` —Value of `amount` is
a percentage. To determine the fee
amount, `amount` is divided by 100,
and then multiplied by the TotalPrice
and TotalTaxAmount of the associated
OrderItemSummary, prorated for the
quantity being returned.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

`ConnectApi.SaleApi` Payment method used within the sale Reqiured 54.0
`PaymentMethod` request.

```
Request

```

#### ConnectApi.ScheduledRecommendationInput

A scheduled custom recommendation.

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

#### `ConnectApi.`

```
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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Ranking scheduled custom recommendations example**

If you have these scheduled custom recommendations:

**Scheduled Recommendations** **Rank**

ScheduledRecommendationA 1

ScheduledRecommendationB 2

ScheduledRecommendationC 3

And you include this information in the Scheduled Custom Recommendation Input:

**Scheduled Recommendation** **Rank**

ScheduledRecommendationD 2


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

#### ConnectApi.ServiceAppointmentInput

Contains information about the service appointment.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`additionalInformation` String Additional details about the service Optional 53.0
appointment.

`appointmentMode` ConnectApi.SvcApptModeEnum Mode of the service appointment. Optional 60.0

**•** `Group`                    - Service appointment mode
is Group.

**•** `Regular`                    - Default mode of service
appointment.

`appointmentType` String Type of the appointment. Optional 53.0

`attendeeLimit` Integer Maximum number of customers that’s
allowed to attend the service appointment.

Required if the 60.0
appointment mode
is Group.

`city` String Name of the city. Optional 53.0

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`extendedFields` <List `ConnectApi.ExtendedFieldInput`    - Values to add to any of the fields, including Optional 53.0
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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`externalReference` String Unique code, reference, or identifier for the Optional 63.0
shipping carrier used by external systems.

`shippingCarrierMethods` ListConnectApi.ShippingCaierMethodInputRepresentation **r** List of shipping carrier methods. Required 63.0
on page 2123

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`name` String Name of the static attribute. 60.0

`value` String Value of the static attribute. 60.0

#### ConnectApi.StatusCapabilityInput

Change the status of a feed post or comment.

This class is a subclass of ConnectApi.FeedElementCapabilityInput.

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


Apex Reference Guide ConnectApi Input Classes

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

List< `ConnectApi.` Maps each recipient with the context based Optional 50.0
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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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
`ExperienceVariation` [, see](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Personalization Target Developer and Group](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

[Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm) _Experience Cloud Developer_
_Guide_ .

`priority` Integer

Priority of the target. Within a group, priority Optional 48.0
determines which target is returned if the
user matches more than one audience.

`publishStatus` `ConnectApi.` The publish status of the target. Values are: Optional 48.0

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`targetValue` String Value of the target. If `targetType` is Required 48.0
`ExperienceVariation`,

`targetValue` is the developer name of
the experience variation. If `targetType`
is _**`CustomObjectName`**_ `__c`,
`targetValue` is the ID of the custom
object. To determine the developer name
for targets of type
`ExperienceVariation` [, see](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Personalization Target Developer and Group](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
[Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm) _Experience Cloud Developer_
_Guide_ .

SEE ALSO:

ConnectApi.TargetCollectionInput

#### ConnectApi.TargetLocationInputRepresentation

A set of inventory locations that together can fulfill an order.

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

#### locations List< ConnectApi. A list of locations with information about Required 51.0

`LocationInputRepresentation`                      - their country and postal codes.

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

**Name** **Type** **Description** **Required or** **Available Version**
**Optional**

```
billTo

shipFrom

shipTo

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

```


Apex Reference Guide ConnectApi Input Classes

**Name** **Type** **Description** **Required or** **Available Version**
**Optional**

```
soldTo

```

#### ConnectApi. Sold To address. Optional 55.0

```
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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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

`referenceDocumentCode` String

The original document code. Used in case Optional 55.0
of subsequent transactions such as credit
tax.

`referenceEntityId` String ID of the reference entity used during tax Optional 55.0
calculation.

`transactionDate` Datetime The date that the tax transaction occurred. Optional 53.0

#### ConnectApi.TextClassificationsInputRepresentation

Text classification information associating classifiers and text to be classified.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

classifiers List< `String`      - List of classifiers according to which text has Required 59.0
to be classified.

textList List< `String`     - List of text to be classified. Required 59.0

#### ConnectApi.TextSegmentInput

Include a text segment in a feed item or comment.

Subclass of ConnectApi.MessageSegmentInput.

**Property** **Type** **Description** **Available Version**

`text` String Plain text for this segment. If hashtags or links are detected in _`text`_, 28.0
they’re included in the comment as hashtag and link segments. Mentions

aren’t detected in _`text`_ and aren’t separated out of the text. Mentions
require `ConnectApi.MentionSegmentInput` .

SEE ALSO:

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

[Post a Rich-Text Feed Element with Inline Image](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_post_feed_element_richtext_inlineimage.htm)

ConnectApi.MessageBodyInput

#### ConnectApi.TopicInput

Update a topic’s name or description or merge topics.

**Property** **Type** **Description** **Available Version**

`description` String Description of the topic 29.0

`idsToMerge` List<String>

List of up to five secondary topic IDs to merge with the primary topic 33.0

If any of the secondary topics are navigational or featured topics, they
lose their topic type, topic images, and children topics. Their feed items

are reassigned to the primary topic. If you merge a topic with a content
topic, the content associations are preserved. If you merge a topic with
an inactive endorsee, the endorsement isn’t mapped to the primary
topic.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available Version**

`name` String

SEE ALSO:

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

`topics` List<String> List of topics to assign to the feed element. Required 38.0

SEE ALSO:

ConnectApi.FeedElementCapabilitiesInput

#### ConnectApi.TypeAndFilterInput

Represents the wrapper for logical comparison filters.


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`filter` `BaseComparisonInputRepresentation` Filter for the entity. 60.0

`type` String Name of the entity. 60.0

#### ConnectApi.UpdateServiceAppointmentInput

Contains information to update a service appointment.

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available Version**

`aboutMe` String

SEE ALSO:

The `aboutMe` property of a `ConnectApi.UserDetail` output 29.0
object. This property populates the About Me section of the user profile,
which is visible to all members of an Experience Cloud site or org.

updateUser(communityId, userId, userInput)

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`value` `Object` Value to wrap. Required 60.0

#### Retired ConnectApi Input Classes

##### These ConnectApi input classes are retired.

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


Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Available Version**

`parameters` String

Optional. Parameters passed to the canvas app in JSON format. Example: 29.0–31.0

```
{'isUpdated'='true'}

```

`thumbnailUrl` String Optional. A URL to a thumbnail image for the canvas app. Maximum 29.0–31.0
dimensions are 120x120 pixels.

`title` String The title of the link used to call the canvas app. 29.0–31.0

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

Apex Reference Guide ConnectApi Input Classes

**Property** **Type** **Description** **Required or** **Available**
**Optional** **Version**

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

**•** ConnectApi.ContentAttachmentInput

##### • ConnectApi.LinkAttachmentInput • ConnectApi.NewFileAttachmentInput

**•** ConnectApi.PollAttachmentInput

##### ConnectApi.LinkAttachmentInput

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


### Apex Reference Guide ConnectApi Output Classes

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

[All concrete output classes have no-argument constructors that you can invoke only from test code. See Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### ConnectApi.AbstractCartItem

A cart item.

This class is abstract.

Superclass of:

**•** ConnectApi.CartItem


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.CartItemWithoutPrice

**Property Name** **Type** **Description** **Available Version**

`billingFrequency` `ConnectApi.` Reserved for future use. 59.0

```
             BillingFrequency

```

`cartDeliveryGroupId` String ID of the cart delivery group. 60.0

`cartId` String ID of the cart. 49.0

`cartItemId` String ID of the item. 49.0

`childProduct` Integer on page 3819 Number of child products in the cart that are 62.0
`Count` associated with the item. A cart item can have child
products if the `productClass` of the item is
`Bundle` . For nested bundles, which include a child
product that's also a bundle,
`childProductCount` includes all child
products.

`customFields` List< `SObject`   - Array of sObjects and viewable custom fields for the 61.0
sObjects. Standard fields are ignored. Currently, only

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

`messagesSummary` `ConnectApi.` Messages summary for the item. 49.0

```
          CartMessagesSummary

```

`name` String Name of the item. 49.0

`parentCartItemId` String ID of the item’s parent cart item. The value is empty 62.0
if the item is a top-level cart item.

`productDetails` `ConnectApi.` Summary of the product details. 49.0

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

`sellingModelType` `ConnectApi.` Reserved for future use. 60.0

```
          SellingModelType

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### subType ConnectApi. Subtype of item in a cart. Values are: 64.0

```
             CartItemSubType
```

**•** `Bonus` —A bonus product.

**•** `Gift` —A gift product.

`subscriptionTerm` Integer on page 3819 Reserved for future use. 59.0

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


Apex Reference Guide ConnectApi Output Classes

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

Error messages that the gateway returned for the 50.0
notification request. Maximum length of 255
characters.

Gateway-specific result code. You can map the result 50.0
code to a Salesforce-specific result code. Maximum
length of 64 characters.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`gatewayResultCodeDescription` String

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**•** ConnectApi.LabeledRecordField

Message segments in a feed item are typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as
#### ConnectApi.FeedItemCapability . Record fields are typed as ConnectApi.AbstractRecordField . These classes

are all abstract and have several concrete subclasses. At runtime you can use `instanceof` to check the concrete types of these objects
and then safely proceed with the corresponding downcast. When you downcast, you must have a default case that handles unknown
subclasses.

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.


Apex Reference Guide ConnectApi Output Classes

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

**•** ConnectApi.RecordView

**Name** **Type** **Description** **Available Version**

`name` String The localized name of the record. 29.0


Apex Reference Guide ConnectApi Output Classes

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

`contentItemSize` Long Class on page 3893 Length in bytes of the content of the file, including 65.0
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

`title` String Title of the file. 39.0

`versionId` String ID of the file version in the external system. 39.0


Apex Reference Guide ConnectApi Output Classes

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

#### repository ConnectApi. Item external repository. 39.0

```
             Reference

```

`type` String Item type, `file` or `folder` . 39.0

`url` String The URL to the item. 39.0


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.ActionInfoOutputRepresentation

Recommended action information.

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the Lightning web component used for 60.0
dynamically rendering the recommended action.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

[For a complete list of label keys, see Action Links](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)
[Labels in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm) _Connect REST API Developer Guide_ .

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

**•** `HttpPut` —Return HTTP 200 on success or
HTTP 204 if the response body or output class is
empty.

`modifiedDate` Datetime ISO 8601 format date string, for example, 33.0
2011-02-25T18:24:31.000Z.

`requestBody` String The request body for `Api` and `ApiAsync` action 33.0
link types.

Note: Escape quotation mark characters in
the `requestBody` value.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`requires` Boolean `true` to require the user to confirm the action; 33.0
`Confirmation` `false` otherwise.

`templateId` String

The ID of the action link template from which to 33.0
instantiate this action link. If the action link isn’t
associated with a template, the value is `null` .

#### type ConnectApi. Defines the type of action link. Values are: 33.0

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
[Link resource in the Connect REST API](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)
[Developer Guidefor more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)

`userId` String The ID of the user who can execute the action. If not 33.0
specified or `null`, any user can execute the action.

If you specify a `userId`, you can’t specify an
`excludedUserId` .

SEE ALSO:

ConnectApi.ActionLinkGroupDefinition

#### ConnectApi.ActionLinkDiagnosticInfo

Any diagnostic information that may exist for an executed action link. Diagnostic info is provided only for users who can access the
action link.


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### activationPlatformCustomerFileSourceEnum ConnectApi. Customer file source of the activation platform. 60.0

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

#### activationTarget ConnectApi. Activation target details. 60.0

```
          ActivationTargetRepresentation

```

`activationTargetId` String Activation target ID for the activation. 60.0

`activationTargetName` String Activation target name for the activation. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`lastPublishStatusErrorMsg` String Error message encountered during last publish. 60.0

`latestAudienceDmoApiName` String API name for the latest audience DMO. 62.0

`latestAudienceDmoLabel` String Name for the latest audience DMO. 62.0

`latestAudienceDmoLastRunTimestamp` Datetime Timestamp of the last run for the latest audience 62.0
DMO. Use the format `yyyy-mm-dd` .

`membershipName` String Membership name of the activation. 60.0

#### refreshType ConnectApi. Refresh type of the activation. 60.0

```
              DataExportRefreshModeEnum
```

**•** `Full_Refresh`

**•** `Incremental`

#### relatedDmoFiltersConfig ConnectApi. DMO filters on related attributes for the activation. 60.0

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

#### staticDataConfig ConnectApi. Static data of the activation. 60.0

```
             StaticDataConfig

#### status ConnectApi. Status of the activation. 60.0

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


Apex Reference Guide ConnectApi Output Classes

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

**•** `Non_Aggregatable_Computed_Measure`

#### ConnectApi.ActivationAttributeConfig

Represents the configuration for activation attributes.

**Property Name** **Type** **Description** **Available Version**

#### attributes List< ConnectApi.ActivationAttribute > List of activation attributes. 60.0 ConnectApi.ActivationCollection

Represents a collection of activations.

**Property Name** **Type** **Description** **Available Version**

#### activations List< ConnectApi. List of activations. 60.0

`ActivationRepresentation`                   


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**Property Name** **Type** **Description** **Available Version**

#### contactPointFields <List ConnectApi.ActivationContactPointFieldConfig > List of contact point fields. 60.0 ConnectApi.ActivationContactPointSourceConfig

Represents an activation contact point source configuration output.

**Property Name** **Type** **Description** **Available Version**

`dataSourceId` String ID of the data source. 60.0

`dataSourceName` String Name of the data source. 60.0

`dataSourcePreference` `ContactPointPrefEnum` Type of contact point. 60.0

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ContactPointPrefPrimary`

`dataSourcePriority` Integer Priority of the data source. 60.0

#### ConnectApi.ActivationContactPointsSourceConfig

Represents the activation contact points source configuration output.

**Property Name** **Type** **Description** **Available Version**

`contactPointSources` <List `ConnectApi.ActivationContactPointSourceConfig`    - List of contact point source configurations. 60.0

#### ConnectApi.ActivationData

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

#### dataSources <List ConnectApi.ActivationDataSourceConfig > List of activation data source configurations. 60.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ActivationDataSourceConfig

Represents an activation data source configuration output.

**Property Name** **Type** **Description** **Available Version**

`dataSourceId` String ID of the data source for the activation. 60.0

`dataSourceName` String Name of the data source for the activation. 60.0

`marketSegmentActivationId` String ID of the market segment activation. 60.0

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

`platformName` String Platform name for the activation target. 60.0

`platformPrivacyType` String Platform privacy type for the activation target. Derived 60.0
from Activation Platform.

`platformType` `DataConnectorTypeEnum` Data connector type of the activation target. 60.0

**•** `AmazonS3`

**•** `AzureBlob`

**•** `DataCloud`

**•** `GoogleCloudStorage`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.ActivationTargetSubject

Represents an activation target subject output.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Developer name of the activation target subject. 60.0

`masterLabel` String Master label of the activation target subject. 60.0

#### queryPathConfigListRepresentation List< ConnectApi. Query path for the activation target. 60.0

`QueryPathConfigList`               


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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

**Property Name** **Type** **Description** **Available Version**

#### platformAction List< ConnectApi. The platform action groups associated with a feed 33.0

`Groups` `PlatformActionGroup`   - element. Platform action groups are returned in the
order specified in the

#### `ConnectApi.AssociatedActions`

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.AudienceCollection ConnectApi.AudienceCollection

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


Apex Reference Guide ConnectApi Output Classes

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
