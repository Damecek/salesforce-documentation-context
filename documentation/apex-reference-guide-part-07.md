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

`showAbsoluteUrl, referenceDepth, expandReferences, referencesAsList)` on page 1701.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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

Type: `ConnectApi.ExternalAuthIdentityProviderInput` on page 2085

A `ConnectApi.ExternalAuthIdentityProviderInput` input class.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProvider` on page 2361

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

Type: `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` on page 2084

A `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` input class

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2362


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

Type: `ConnectApi.ExternalAuthIdentityProvider` on page 2361

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

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2362

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

Type: `ConnectApi.ExternalAuthIdentityProviderList` on page 2363

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

Type: `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` on page 2084

A `ConnectApi.ExternalAuthIdentityProviderCredentialsInput` input class.

Return Value

Type: `ConnectApi.ExternalAuthIdentityProviderCredentials` on page 2362

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

Type: ConnectApi.OCIUpdateReservationInputRepresentation on page 2131

Data to update one or more Omnichannel Inventory item reservations.

Return Value

Type: ConnectApi.OCIUpdateReservationOutputRepresentation on page 2482

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


### Apex Reference Guide OptimizationFiles Class

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

### OptimizationFiles Class

```

Fetch files associated with optimization requests for Enhanced Scheduling and Optimization. Requires Field Service to be enabled for
the org and the running user to have Field Service enabled.

Namespace

ConnectApi


Apex Reference Guide OptimizationFiles Class

#### OptimizationFiles Methods These methods are for OptimizationFiles . All methods are static.

IN THIS SECTION:

##### FetchOptimizationFiles(fetchFilesInput)

Fetch the files generated for an optimization request in Enhanced Scheduling and Optimization.

##### **`FetchOptimizationFiles(fetchFilesInput)`**

Fetch the files generated for an optimization request in Enhanced Scheduling and Optimization.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FetchFilesOutputRepresentation

   FetchOptimizationFiles(ConnectApi.fetchFilesInput fetchFilesInput)

```

Parameters

```
   fetchFilesInput
```

Type: `ConnectApi.fetchFilesInput`

The input representation containing the ID of the optimization request for which to retrieve the associated files.

Return Value

Type: `ConnectApi.FetchFilesOutputRepresentation`

Usage

Use FetchOptimizationFiles to retrieve the Content Version files produced for a completed optimization request. Each file in the response
corresponds to a file created in the org and is keyed by filename in the returned map.

Example

```
   ConnectApi.fetchFilesInput input = new ConnectApi.fetchFilesInput();

       input.optimizationRequestId = '0XxXXXXXXXXXXXXX';

       ConnectApi.FetchFilesOutputRepresentation output =

       ConnectApi.OptimizationFiles.FetchOptimizationFiles(input);

       Map<String, ConnectApi.CreatedFile> files = output.createdFiles;

```


### Apex Reference Guide Orchestration Class

```
       for (String fileName : files.keySet()) {

       ConnectApi.CreatedFile file = files.get(fileName);

      System.debug(fileName + ': id=' + file.contentVersionId + ', success=' + file.success);

       }

### Orchestration Class

```

Get orchestration instances.

Namespace

ConnectApi

#### Orchestration Methods

### These methods are for Orchestration . All methods are static.

IN THIS SECTION:

##### getOrchestrationInstance(instanceId)

Get an orchestration instance associated with an orchestration instance ID.

getOrchestrationInstanceCollection(relatedRecordId)
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


Apex Reference Guide Orchestration Class

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


### Apex Reference Guide OrderPaymentSummary Class

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


### Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

IN THIS SECTION:

##### adjustPreview(orderSummaryId, adjustInput)

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

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


Apex Reference Guide OrderSummary Class

Return Value

Type: `ConnectApi.PreviewCancelOutputRepresentation`

SEE ALSO:

createCreditMemo(orderSummaryId, creditMemoInput)

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)

##### submitCancel(orderSummaryId, changeInput) **`previewReturn(orderSummaryId, changeInput)`**

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


Apex Reference Guide OrderSummary Class

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


### Apex Reference Guide OrderSummaryCreation Class

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


### Apex Reference Guide Organization Class

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryOutputRepresentation

   createOrderSummary(ConnectApi.OrderSummaryInputRepresentation orderSummaryInput)

```

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


### Apex Reference Guide PardotBusinessUnitContext Class

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

Namespace

ConnectApi

#### PardotBusinessUnitContext Methods

### These methods are for PardotBusinessUnitContext . All methods are static.

IN THIS SECTION:

##### getBusinessUnitContext()

Get the Pardot business units the context user has access to.

getBusinessUnitContextByIsCurrentStatus(isCurrent)
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


### Apex Reference Guide Payments Class

##### **`getBusinessUnitContextByIsCurrentStatus(isCurrent)`**

Get the Pardot business units the context user has access to by specifying the current status.

API Version

55.0

Requires Chatter

No

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


Apex Reference Guide Payments Class

##### postAuth(postAuthorizePayment)

Confirms that the merchant is ready to capture payment of an existing pre-authorized transaction.

reverseAuthorization(AuthReversalInput, authorizationId)
Reverses a payment authorization.

capture(AuthCaptureInput, authorizationId)
Capture an authorized payment.

refund(ReferencedRefundInput, paymentId)
Refund an authorized payment.

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


Apex Reference Guide Payments Class

API Version

54.0

Requires Chatter

No

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


Apex Reference Guide Payments Class

Return Value

Type: `ConnectApi.AuthorizationReversalResponse`

##### **`capture(AuthCaptureInput, authorizationId)`**

Capture an authorized payment.

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


Apex Reference Guide Payments Class

Signature

```
   global static ConnectApi.ReferencedRefundResponse

   refund(ConnectApi.ReferencedRefundRequest ReferencedRefundInput, String paymentId)

```

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


Apex Reference Guide Payments Class

API Version

52.0

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

```


### Apex Reference Guide Personalization Class Personalization Class

Get assigned personalization audiences that match the user context. Create, get, update, and delete an audience. Get personalization
targets that match the user context, based on the assigned audiences that include the user. Create and update targets. Get and delete
a target.

Namespace

ConnectApi

Note: Personalization varies what the user can see in the browser but doesn’t secure data in any way. To prevent users accessing
sensitive data, use standard Salesforce security features, such as sharing rules and permission sets.

#### Personalization Methods

### These methods are for Personalization . All methods are static.

IN THIS SECTION:

createAudience(communityId, audience)
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


Apex Reference Guide Personalization Class

updateTargets(communityId, target)
Update targets.

##### **`createAudience(communityId, audience)`**

Create an audience.

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


Apex Reference Guide Personalization Class

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

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


Apex Reference Guide Personalization Class

Requires Chatter

No

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


Apex Reference Guide Personalization Class

ID of the audience.

```
   includeAudienceCriteria
```

Type: Boolean

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


Apex Reference Guide Personalization Class

##### **`getAudiences(communityId, ipAddress, domain, userId, publishStatus,`**

```
  includeAudienceCriteria, targetTypes, recordId)

```

Get a list of assigned audiences that match the user context and record information.

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


Apex Reference Guide Personalization Class

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


Apex Reference Guide Personalization Class

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


Apex Reference Guide Personalization Class

##### **`getTarget(communityId, targetId)`**

Get a target.

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


Apex Reference Guide Personalization Class

Signature

```
   public static ConnectApi.BatchResult[] getTargetBatch(String communityId, List<String>

   targetIds)

```

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


Apex Reference Guide Personalization Class

ID of the Experience Cloud site.

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


Apex Reference Guide Personalization Class

```
   groupNames
```

Type: List<String>

A comma-separated list of group names. Groups bundle related target and audience pairs.

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


### Apex Reference Guide PickTicket Class

Requires Chatter

No

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


### Apex Reference Guide QuestionAndAnswers Class

Requires Chatter

No

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

getSuggestions(communityId, q, subjectId, includeArticles, maxResults)
Get question and answers suggestions.

setTestGetSuggestions(communityId, q, subjectId, includeArticles, maxResults, result)
Register a `ConnectApi.QuestionAndAnswersSuggestions` object to be returned when `getSuggestions` is
called with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

updateQuestionAndAnswers(communityId, feedElementId, questionAndAnswersCapability)
Choose or change the best answer for a question.


Apex Reference Guide QuestionAndAnswers Class

##### **`getSuggestions(communityId, q, subjectId, includeArticles, maxResults)`**

Get question and answers suggestions.

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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


Apex Reference Guide QuestionAndAnswers Class

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

SEE ALSO:

##### setTestGetSuggestions(communityId, q, subjectId, includeArticles, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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


Apex Reference Guide QuestionAndAnswers Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getSuggestions(communityId, q, subjectId, includeArticles, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


### Apex Reference Guide Recommendations Class

Example

```
   ConnectApi.QuestionAndAnswersCapabilityInput qaInput = new

   ConnectApi.QuestionAndAnswersCapabilityInput();

   qaInput.bestAnswerId = '0D7D00000000lMAKAY';

   ConnectApi.QuestionAndAnswersCapability qa =

   ConnectApi.QuestionAndAnswers.updateQuestionAndAnswers(null, '0D5D0000000XZjJ', qaInput);

### Recommendations Class

```

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


Apex Reference Guide Recommendations Class

deleteScheduledRecommendation(communityId, scheduledRecommendationId, deleteDefinitionIfLast)
Delete a scheduled custom recommendation.

getRecommendationAudience(communityId, recommendationAudienceId)
Get information about a custom recommendation audience.

getRecommendationAudienceMembership(communityId, recommendationAudienceId)
Get the members of a custom recommendation audience.

getRecommendationAudienceMembership(communityId, recommendationAudienceId, pageParam, pageSize)
Get a page of custom recommendation audience members.

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


Apex Reference Guide Recommendations Class

updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId, fileUpload)
Update a custom recommendation definition photo with a file that hasn’t been uploaded.

updateRecommendationDefinitionPhoto(communityId, recommendationDefinitionId, fileId, versionNumber)
Update a custom recommendation definition photo with an uploaded file.

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo)
Update a custom recommendation definition photo with an uploaded file that requires cropping.

updateRecommendationDefinitionPhotoWithAttributes(communityId, recommendationDefinitionId, photo, fileUpload)
Update a custom recommendation definition photo with a file that hasn’t been uploaded and requires cropping.

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


Apex Reference Guide Recommendations Class

can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`createRecommendationAudience(communityId, name)`**

Create an audience for a custom recommendation.

API Version

35.0

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


Apex Reference Guide Recommendations Class

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


Apex Reference Guide Recommendations Class

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


Apex Reference Guide Recommendations Class

##### **`createScheduledRecommendation(communityId, scheduledRecommendation)`**

Create a scheduled custom recommendation.

API Version

35.0

Requires Chatter

Yes

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


Apex Reference Guide Recommendations Class

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


Apex Reference Guide Recommendations Class

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by default on the Home and Question
Detail pages of Customer Service and Partner Central Experience Builder templates. They also appear in the feed in the Salesforce
mobile web and anywhere community managers add recommendations using Experience Builder.

Use these channel values; you can’t rename or create other channels.

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

##### **`deleteRecommendationAudience(communityId, recommendationAudienceId)`**

Delete a custom recommendation audience.


Apex Reference Guide Recommendations Class

API Version

35.0

Requires Chatter

Yes

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


Apex Reference Guide Recommendations Class

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

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


Apex Reference Guide Recommendations Class

Deleting a scheduled custom recommendation is comparable to a deletion in an ordered list. All scheduled custom recommendations
after the deleted scheduled custom recommendation receive a new, higher rank automatically.

##### **`getRecommendationAudience(communityId, recommendationAudienceId)`**

Get information about a custom recommendation audience.

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


Apex Reference Guide Recommendations Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserReferencePage getRecommendationAudienceMembership(String

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

```
   pageParam
```

Type: Integer

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


Apex Reference Guide Recommendations Class

Return Value

Type: `ConnectApi.RecommendationAudiencePage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

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


Apex Reference Guide Recommendations Class

can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

##### **`getRecommendationDefinition(communityId, recommendationDefinitionId)`**

Get a custom recommendation definition.

API Version

35.0

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


Apex Reference Guide Recommendations Class

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


Apex Reference Guide Recommendations Class

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.RecommendationDefinitionPage`

Usage

Community managers can access, create, and delete audiences, definitions, and schedules for custom recommendations. (Community
managers are users with the Create and Set Up Experiences or Manage Experiences permission.) Users with the Modify All Data permission
can also access, create, and delete custom recommendation audiences, custom recommendation definitions, and scheduled custom
recommendations.

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


Apex Reference Guide Recommendations Class

**•** If _`action`_ is `follow`, _`objectId`_ is a user ID, file ID, record ID, or topic ID (version 36.0 and later).

**•** If _`action`_ is `join`, _`objectId`_ is a group ID.

**•** If _`action`_ is `view`, _`objectId`_ is a user ID, file ID, group ID, record ID, custom recommendation ID (version 34.0 and later),
the enum `Today` for static recommendations (version 35.0 and later), or an article ID (version 37.0 and later).

Return Value

Type: `ConnectApi.RecommendationCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecommendationForUser(communityId, userId, action, objectId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Recommendations Class

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

setTestGetRecommendationsForUser(communityId, userId, contextAction, contextObjectId, channel, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Recommendations Class

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

setTestGetRecommendationsForUser(communityId, userId, action, contextAction, contextObjectId, channel, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Recommendations Class

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


Apex Reference Guide Recommendations Class

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

setTestGetRecommendationsForUser(communityId, userId, action, objectCategory, contextAction, contextObjectId, channel,
maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

Usage

### Apex methods in the RecordUi class can’t be used in packages that use push upgrades.

#### RecordUi Methods

### These methods are for RecordUi . All methods are static.

IN THIS SECTION:

##### getPicklistValuesByRecordType(objectApiName, recordTypeId)

Get the values for all the picklist fields of a specific record type.

##### **`getPicklistValuesByRecordType(objectApiName, recordTypeId)`**

Get the values for all the picklist fields of a specific record type.


### Apex Reference Guide RegisterGuestBuyer Class

API Version

66.0

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

[API name of a User Interface API supported object.](https://developer.salesforce.com/docs/atlas.en-us.262.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm#ui_api_get_started_supported_objects)

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

Important: This Apex method can’t be used in packages that use push upgrades.

### RegisterGuestBuyer Class

Register a guest buyer for a webstore using an account ID, enabling a guest buyer to order on behalf of another buyer.

Namespace

ConnectApi

#### RegisterGuestBuyer Methods

### These methods are for RegisterGuestBuyer . All methods are static. Your org must have the Order Management Growth license

or Order Management as part of Connected Commerce.


### Apex Reference Guide Repricing Class

IN THIS SECTION:

##### registerGuestBuyer(webstoreId, accountId)

Register a guest buyer for a webstore using an account ID. This method enables a guest buyer to order on behalf of another buyer.

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

Type: `ConnectApi.RegisterGuestBuyerOutputRepresentation on page 2567`

### Repricing Class

Perform functions related to repricing orders in Order Management.

Namespace

ConnectApi

#### Repricing Methods

### These methods are for Repricing . All methods are static.


Apex Reference Guide Repricing Class

IN THIS SECTION:

##### productDetails(webstoreId, skuOrProductId, effectiveAccountId, currencyCode, locale)

Get details of a product in a web store.

searchProducts(webstoreId, searchTerm, pageParam, pageSize, effectiveAccountId, facets)
Search products in a webstore.

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


Apex Reference Guide Repricing Class

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


### Apex Reference Guide ReturnOrder Class

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

Type: `ConnectApi.ProductSearchOutputRepresentation` on page 2537

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


Apex Reference Guide ReturnOrder Class

API Version

50.0

Requires Chatter

No

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


### Apex Reference Guide Routing Class

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


Apex Reference Guide Routing Class

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


Apex Reference Guide Routing Class

Requires Chatter

No

Signature

```
   public static ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation

   findRoutesWithFewestSplits(ConnectApi.FindRoutesWithFewestSplitsInputRepresentation

   findRoutesWithFewestSplitsInputRepresentation)

```

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


Apex Reference Guide Routing Class

Return Value

Type: `ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation`

SEE ALSO:

getInventoryAvailability(inventoryAvailabilityInputRepresentation)

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)

##### **`getFOCapacityValues(getFOCapacityValuesInput)`**

Get information about the current fulfillment order capacity of one or more locations.

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


Apex Reference Guide Routing Class

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


### Apex Reference Guide SalesforceInbox Class

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


### Apex Reference Guide Search Class

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

answer(q)
Search objects using a natural language query and return an answer.

answer(q, objectApiName)
Search an object using a natural language query and return an answer.

answer(q, objectApiName, displayFields)
Search an object using a natural language query and display fields.


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAnswer(q, result)`**

Registers a `ConnectApi.SearchAnswer` object to be returned when the matching `answer(q)` method is called in a test
context. Use the method with the same parameters or you receive an exception.


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


Apex Reference Guide Search Class

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


### Apex Reference Guide Sites Class

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

Namespace

ConnectApi

#### Sites Methods

### These methods are for Sites . All methods are static.

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


### Apex Reference Guide SmartDataDiscovery Class

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


Apex Reference Guide SocialEngagement Class

Namespace

ConnectApi

SEE ALSO:

_Knowledge Article_ [: Marketing Cloud Social Studio Retirement](https://help.salesforce.com/s/articleView?id=000392005&type=1&language=en_US)

#### SocialEngagement Methods These methods are for SocialEngagement . All methods are static.

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


Apex Reference Guide SocialEngagement Class

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


### Apex Reference Guide Surveys Class

Return Value

Type: Void

##### **`unlikeSocialPost(socialPostId, socialAccountId)`**

Unlike a social post in its social network.

API Version

46.0–61.0

Requires Chatter

No

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


### Apex Reference Guide TaxPlatform Class

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


### Apex Reference Guide Topics Class

IN THIS SECTION:

##### calculateTax(calculateTax)

Apply tax or cancel tax.

##### **`calculateTax(calculateTax)`**

Apply tax or cancel tax.

API Version

55.0

Requires Chatter

No

Signature

```
   global static ConnectApi.CalculateTaxResponse calculateTax(ConnectApi.CalculateTaxRequest

   calculateTax)

```

Parameters

##### _`calculateTax`_

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


Apex Reference Guide Topics Class

**•** `getRecentlyTalkingAboutTopicsForUser(communityId, userId)`

[All other methods in this class count toward the Salesforce Platform total API request allocations, which are per org and span a 24-hour](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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

Return Value

Type: `ConnectApi.ChatterGroupSummaryPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetGroupsRecentlyTalkingAboutTopic(communityId, topicId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)`**

Get up to five topics most recently used in a group.

API Version

29.0

Available to Guest Users

32.0


Apex Reference Guide Topics Class

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

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecentlyTalkingAboutTopicsForGroup(communityId, groupId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRecentlyTalkingAboutTopicsForUser(communityId, userId)`**

Get up to five topics most recently used by a user.

API Version

29.0

Available to Guest Users

32.0

Requires Chatter

Yes


Apex Reference Guide Topics Class

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

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRecentlyTalkingAboutTopicsForUser(communityId, userId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

Return Value

Type: `ConnectApi.TopicPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRelatedTopics(communityId, topicId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTopicSuggestions(communityId, recordId)`**

Get suggested topics for a record or feed item.

API Version

29.0


Apex Reference Guide Topics Class

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

Return Value

Type: `ConnectApi.TopicSuggestionPage`

Usage

Administrators must enable topics for objects before users can see suggested topics for records of that object type.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestions(communityId, recordId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Topics Class

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

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopicSuggestionsForText(communityId, text, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Topics Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Topics Class

Usage

The more frequently people add a specific topic to their posts and comments and comment on or like posts with the same topic over
a short period, the more likely it is to become a trending topic. For example, if your coworkers are attending the upcoming Dreamforce
conference and have started discussing it in Chatter, you might see a trending topic for Dreamforce. A trending topic is not solely based
on popularity and usually relates to a one-time or infrequent event that has a spike in activity, such as a conference or a project deadline.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingTopics(communityId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getTrendingTopics(communityId, maxResults)`**

Get up to a specified number of trending topics for the org or Experience Cloud site.

API Version

29.0

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


Apex Reference Guide Topics Class

Usage

The more frequently people add a specific topic to their posts and comments and comment on or like posts with the same topic over
a short period, the more likely it is to become a trending topic. For example, if your coworkers are attending the upcoming Dreamforce
conference and have started discussing it in Chatter, you might see a trending topic for Dreamforce. A trending topic is not solely based
on popularity and usually relates to a one-time or infrequent event that has a spike in activity, such as a conference or a project deadline.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTrendingTopics(communityId, maxResults, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`mergeTopics(communityId, topicId, idsToMerge)`**

Merge up to five secondary topics with a primary topic.

API Version

33.0

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

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


Apex Reference Guide Topics Class

A `ConnectApi.ArticleTopicAssignmentJobInput` object that indicates the operation to take on which topics.

Return Value

Type: `ConnectApi.TopicPage`

#### Topics Test Methods These test methods are for Topics . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Topics Class

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

Return Value

Type: Void

SEE ALSO:

getRecentlyTalkingAboutTopicsForGroup(communityId, groupId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRecentlyTalkingAboutTopicsForUser(communityId, userId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching
`ConnectApi.getRecentlyTalkingAboutTopicsForUser` method is called in a test context. Use the method with the
same parameters or you receive an exception.

API Version

29.0


Apex Reference Guide Topics Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRelatedTopics(communityId, topicId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching `ConnectApi.getRelatedTopics` method
is called in a test context. Use the method with the same parameters or you receive an exception.

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


Apex Reference Guide Topics Class

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRelatedTopics(communityId, topicId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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


Apex Reference Guide Topics Class

Return Value

Type: Void

SEE ALSO:

getTopicSuggestions(communityId, recordId, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopicSuggestions(communityId, recordId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide Topics Class

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

Return Value

Type: Void

SEE ALSO:

getTopicSuggestionsForText(communityId, text, maxResults)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTopicSuggestionsForText(communityId, text, result)`**

Register a `ConnectApi.TopicSuggestionPage` object to be returned when the matching
`ConnectApi.getTopicSuggestionsForText` method is called in a test context. Use the method with the same parameters
or you receive an exception.


Apex Reference Guide Topics Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetTrendingTopics(communityId, result)`**

Register a `ConnectApi.TopicPage` object to be returned when the matching `ConnectApi.getTrendingTopics`
method is called in a test context. Use the method with the same parameters or you receive an exception.

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


Apex Reference Guide Topics Class

```
   result
```

Type: `ConnectApi.TopicPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTrendingTopics(communityId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


### Apex Reference Guide UserProfiles Class UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


Apex Reference Guide UserProfiles Class

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


### Apex Reference Guide Zones Class

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

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

Namespace

ConnectApi

#### Zones Methods

### These methods are for Zones . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

getZone(communityId, zoneId)
Get a zone.

getZones(communityId)
Get a list of zones.


Apex Reference Guide Zones Class

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


Apex Reference Guide Zones Class

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


Apex Reference Guide Zones Class

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide Zones Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchInZone(communityId, zoneId, q, filter, pageParam, pageSize)`**

Search a page of articles or questions in a zone.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
