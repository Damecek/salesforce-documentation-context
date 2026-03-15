
```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedElementPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedFilter filter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.


Apex Reference Guide ChatterFeeds Class

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`


Apex Reference Guide ChatterFeeds Class

**•** `Groups`

**•** `News`

**•** `People`

**•** `Record`

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince,

  showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   Boolean showInternalOnly, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

35.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out. Currently, feed elements scoped
to sites have a User or a Group parent record. However, other parent record types could be scoped to sites in the future.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, customFilter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, String customFilter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`


Apex Reference Guide ChatterFeeds Class

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.


Apex Reference Guide ChatterFeeds Class

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, ConnectApi.FeedFilter filter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String


Apex Reference Guide ChatterFeeds Class

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.


Apex Reference Guide ChatterFeeds Class

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, customFilter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, String customFilter,

   ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedElementPage` response body.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String


Apex Reference Guide ChatterFeeds Class

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, updatedSince, showInternalOnly, customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRelatedPosts(communityId, feedElementId, filter, maxResults, result)`**

Register a `ConnectApi.RelatedFeedPosts` object to be returned when the matching
`ConnectApi.getRelatedPosts(communityId, feedElementId, filter, maxResults)` method is called
in a test context. Use the method with the same parameters or you receive an exception.

API Version

37.0

Signature

```
   public static Void setTestGetRelatedPosts(String communityId, String feedElementId,

   ConnectApi.RelatedFeedPostType filter, Integer maxResults, ConnectApi.RelatedFeedPosts

   result)

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

ID of the feed element. The feed element must be a question.

```
   filter
```

Type: `ConnectApi.RelatedFeedPostType`

Specifies the type of related feed post. Values are:

**•** `Answered` —Related questions that have at least one answer.

**•** `BestAnswer` —Related questions that have a best answer.

**•** `Generic` —All types of related questions, including answered, with a best answer, and unanswered.

**•** `Unanswered` —Related questions that don’t have answers.


Apex Reference Guide ChatterFeeds Class

`Generic` is the default value.

```
   maxResults
```

Type: Integer

The maximum number of results to return. You can return up to 25 results; 5 is the default.

```
   result
```

Type: `ConnectApi.RelatedFeedPosts`

Object containing test data.

In version 37.0 and later, related feed posts are questions.

Return Value

Type: Void

##### setTestGetTopUnansweredQuestions(communityId, result) (Pilot)

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Signature

```
   public static Void setTestGetTopUnansweredQuestions(String communityId,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopUnansweredQuestions(communityId) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### setTestGetTopUnansweredQuestions(communityId, filter, result) (Pilot)

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Signature

```
   public static Void setTestGetTopUnansweredQuestions(String communityId,

   ConnectApi.TopUnansweredQuestionsFilterType filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the filter for the feed. `UnansweredQuestionsWithCandidateAnswers` is the only valid value.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopUnansweredQuestions(communityId, filter) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### setTestGetTopUnansweredQuestions(communityId, pageSize, result) (Pilot)

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.


Apex Reference Guide ChatterFeeds Class

API Version

42.0

Signature

```
   public static Void setTestGetTopUnansweredQuestions(String communityId, Integer pageSize,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopUnansweredQuestions(communityId, pageSize) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### setTestGetTopUnansweredQuestions(communityId, filter, pageSize, result) (Pilot)

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Signature

```
   public static Void setTestGetTopUnansweredQuestions(String communityId,

   ConnectApi.FeedFilter filter, Integer pageSize, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the filter for the feed. `UnansweredQuestionsWithCandidateAnswers` is the only valid value.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getTopUnansweredQuestions(communityId, filter, pageSize) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q,

   ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, sortParam, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

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
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

44.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q, Boolean

   threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, threadedCommentsCollapsed)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, pageParam, pageSize, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q, String

   pageParam, Integer pageSize, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .D

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, pageParam, pageSize, sortParam,`**

```
  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q, String

   pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedElementPage result)

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, pageParam, pageSize,`**

```
  threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

44.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q, String

   pageParam, Integer pageSize, Boolean threadedCommentsCollapsed,

   ConnectApi.FeedElementPage result)

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
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, recentCommentCount, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElements(String communityId, String q, Integer

   recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, q, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String q, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

32.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

The type of feed. The only valid value is `Home` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, q, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String q, ConnectApi.FeedElementPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If feed type is `UserProfile`, _`subjectId`_
can be any user ID. If _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Order of feed items in the feed.

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Search term. Searches keywords in the user or group name. A minimum of one character is required. This parameter doesn’t support
wildcards. This parameter is required.


Apex Reference Guide ChatterFeeds Class

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   recentCommentCount
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q, filter,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `searchFeedElementsInFeed` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

35.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedFilter filter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.UserProfile` .

```
   subjectId
```

Type: String

ID of any user. To specify the context user, use the user ID or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

The amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

One or more keywords to search for in the feed elements visible to the context user. The search string can contain wildcards and
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.FeedFilter`

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out. Currently, feed elements scoped
to sites have a User or a Group parent record. However, other parent record types could be scoped to sites in the future.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q, customFilter,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.


Apex Reference Guide ChatterFeeds Class

API Version

40.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, String customFilter,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

The amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

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

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

One or more keywords to search for in the feed elements visible to the context user. The search string can contain wildcards and
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q,

  showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.


Apex Reference Guide ChatterFeeds Class

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q,

  showInternalOnly, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

32.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly,

   ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean


Apex Reference Guide ChatterFeeds Class

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: `ConnectApi.FeedFilter`

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently, these feed elements have a User
or a Group parent record. However, other parent record types could be scoped to sites in the future. Feed elements that are
always visible in all sites are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have candidate answers associated with
them. This value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements that are questions that have candidate
answers that have been reviewed or published. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context user. Includes existing feed elements
when the context user joined the group. This value is valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedElementsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q,

  showInternalOnly, customFilter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestSearchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly, String

   customFilter, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

The ID of a case.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   cusotmFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q,`**

```
  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFilterFeed(String communityId, String

   subjectId, String keyPrefix, String q, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix,`**

```
  pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFilterFeed(String communityId, String

   subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, String q, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .


Apex Reference Guide ChatterFeeds Class

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

31.0

Signature

```
   public static Void setTestSearchFeedElementsInFilterFeed(String communityId, String

   subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String


Apex Reference Guide ChatterFeeds Class

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,
q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchStreams(communityId, q, result)`**

Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q)` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestSearchStreams(String communityId, String q,

   ConnectApi.ChatterStreamPage result)

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
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchStreams(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchStreams(communityId, q, sortParam, result)`**

Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q, sortParam)` method is called in a test context. Use the method with
the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestSearchStreams(String communityId, String q,

   ConnectApi.SortOrder sortParam, ConnectApi.ChatterStreamPage result)

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
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

```
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchStreams(communityId, q, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchStreams(communityId, q, pageParam, pageSize, result)`**

Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize)` method is called in a test context. Use
the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestSearchStreams(String communityId, String q, Integer pageParam,

   Integer pageSize, ConnectApi.ChatterStreamPage result)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchStreams(communityId, q, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, result)`**

Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam)` method is called in
a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestSearchStreams(String communityId, String q, Integer pageParam,

   Integer pageSize, ConnectApi.SortOrder sortParam, ConnectApi.ChatterStreamPage result)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

```
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchStreams(communityId, q, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam,`**

```
  globalScope, result)

```

Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching

```
   ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)
```

method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

41.0

Signature

```
   public static Void setTestSearchStreams(String communityId, String q, Integer pageParam,

   Integer pageSize, ConnectApi.SortOrder sortParam, Boolean globalScope,

   ConnectApi.ChatterStreamPage result)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

```
   sortParam
```

Type: `ConnectApi.SortOrder`

Specifies the sort order. Values are:

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).


Apex Reference Guide ChatterFeeds Class

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This sort order is valid only for Chatter feed
streams.

If not specified, default value is `Ascending` .

```
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

```
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.

Return Value

Type: Void

#### Retired ChatterFeeds Methods

These methods for `ChatterFeeds` are retired.

IN THIS SECTION:

deleteFeedItem(communityId, feedItemId)
Delete a feed item.

getCommentsForFeedItem(communityId, feedItemId)
Get comments for a feed item.

getCommentsForFeedItem(communityId, feedItemId, pageParam, pageSize)
Get a page of comments for a feed item.

getFeedItem(communityId, feedItemId)
Get a feed item.

getFeedItemBatch(communityId, feedItemIds)
Get a list of feed items.

getFeedItemsFromFeed(communityId, feedType)
Get feed items from the `Company`, `Home`, and `Moderation` feeds.

getFeedItemsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)
Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds.

getFeedItemsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam)
Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds. Each feed item contains no more than the
specified number of comments.

getFeedItemsFromFeed(communityId, feedType, subjectId)
Get feed items from a feed for a user or record.

getFeedItemsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam)
Get a page of sorted feed items from a feed for a user or record.


Apex Reference Guide ChatterFeeds Class

getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam)
Get a page of sorted feed items from a feed for a user or record. Each feed item includes no more than the specified number of
comments.

getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly)
Get a page of sorted feed items from a record feed for a user or record. Each feed item includes no more than the specified number
of comments. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix)
Get feed items from a feed filtered by a key prefix for a user.

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam)
Get a page of sorted feed items from a feed filtered by a key prefix for a user.

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam)
Get a page of sorted feed items from a feed filtered by a key prefix for a user. Each feed item contains no more than the specified
number of comments.

getFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
updatedSince)
Get a page of feed items from a feed filtered by a key prefix for a user. Include only feed items that have been updated since the
time specified in the _`updatedSince`_ parameter.

getFeedItemsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince)
Get a page of feed items from the `Company`, `Home`, and `Moderation` feeds. Include only feed items that have been updated
since the time specified in the _`updatedSince`_ parameter. Each feed item contains no more than the specified number of
comments.

getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince)
Get a page of feed items from the `Files`, `Groups`, `News`, `People`, and `Record` feeds. Include only feed items that have
been updated since the time specified in the _`updatedSince`_ parameter. Each feed item contains no more than the specified
number of comments.

getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince,
showInternalOnly)
Get a page of feed items from a record feed. Include only feed items that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.

getFeedPoll(communityId, feedItemId)
Get the poll associated with a feed item.

getLikesForFeedItem(communityId, feedItemId)
Get likes for a feed item.

getLikesForFeedItem(communityId, feedItemId, pageParam, pageSize)
Get a page of likes for a feed item.

likeFeedItem(communityId, feedItemId)
Like a feed item for the context user.

postComment(communityId, feedItemId, text)
Post a plain-text comment to a feed item.

postComment(communityId, feedItemId, comment, feedItemFileUpload)
Post a rich-text comment to a feed item. Use this method to include mentions and to attach a file to a comment.


Apex Reference Guide ChatterFeeds Class

postFeedElement(communityId, feedElement, feedElementFileUpload)
Post a rich-text feed element. Include mentions and hashtag topics, attach a file to a feed element, and associate action link groups
with a feed element. You can also use this method to share a feed element and add a comment.

postFeedItem(communityId, feedType, subjectId, text)
Post a plain-text feed item.

postFeedItem(communityId, feedType, subjectId, feedItemInput, feedItemFileUpload)
Post a rich-text feed item to a feed. Use this method to include mentions and hashtag topics and to attach a file to a feed item. You
can also use this method to share a feed item and add a comment.

searchFeedItems(communityId, q)
Get the feed items that match the search criteria.

searchFeedItems(communityId, q, sortParam)
Get the sorted feed items that match the search criteria.

searchFeedItems(communityId, q, pageParam, pageSize)
Get a page of feed items that match the search criteria.

searchFeedItems(communityId, q, pageParam, pageSize, sortParam)
Get a page of sorted feed items that match the search criteria.

searchFeedItems(communityId, q, recentCommentCount, pageParam, pageSize, sortParam)
Get a page of sorted feed items that match the search criteria.

searchFeedItemsInFeed(communityId, feedType, q)
Get the feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria.

searchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)
Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria.

searchFeedItemsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)
Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria. Each feed
item includes no more than the specified number of comments.

searchFeedItemsInFeed(communityId, feedType, subjectId, q)
Get the feed items from a feed that match the search criteria.

searchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)
Get a page of sorted feed items from a feed for a user or record that match the search criteria.

searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q)
Get a page of sorted feed items from a feed that match the search criteria. Each feed item includes no more than the specified
number of comments.

searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly)
Get a page of sorted feed items from a feed for a user or record that match the search criteria. Each feed item includes no more than
the specified number of comments. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q)
Get the feed items that match the search criteria from a feed filtered by a key prefix for a user.

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)
Get a page of sorted feed items that match the search criteria from a feed filtered by a key prefix for a user.


Apex Reference Guide ChatterFeeds Class

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,
q)
Get a page of sorted feed items that match the search criteria from a feed filtered by a key prefix for a user. Each feed item includes
no more than the specified number of comments.

shareFeedElement(communityId, subjectId, feedElementType, originalFeedElementId)
Share the _`originalFeedElementId`_ as the context user.

shareFeedItem(communityId, feedType, subjectId, originalFeedItemId)
Share the _`originalFeedItemId`_ to the feed specified by the _`feedType`_ .

updateBookmark(communityId, feedItemId, isBookmarkedByCurrentUser)
Bookmark a feed item or remove a bookmark from a feed item.

voteOnFeedPoll(communityId, feedItemId, myChoiceId)
Vote or change your vote on a feed poll.

setTestGetFeedItemsFromFeed(communityId, feedType, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam,
pageSize, sortParam, updatedSince, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the
`getFeedItemsFromFilterFeedUpdatedSince` method is called in a test context.

setTestGetFeedItemsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
ConnectApi.FeedItemPage, results)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)
Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestSearchFeedItems(communityId, q, result)
Register a test feed item page to be returned when `searchFeedItems(communityId, q)` is called during a test.

setTestSearchFeedItems(communityId, q, sortParam, result)
Register a test feed item page to be returned when `searchFeedItems(String, String,`
`ConnectApi.FeedSortOrder)` is called during a test.

setTestSearchFeedItems(communityId, q, pageParam, pageSize, result)
Register a test feed item page to be returned when `searchFeedItems(String, String, String, Integer)` is
called during a test.

setTestSearchFeedItems(communityId, q, pageParam, pageSize, sortParam, result)
Register a test feed item page to be returned when `searchFeedItems(String, String, String, Integer,`
`ConnectApi.FeedSortOrder)` is called during a test.

setTestSearchFeedItems(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)
Register a test feed item page to be returned when `searchFeedItems(communityId, q, recentCommentCount,`
`pageParam, pageSize, sortParam)` is called during a test.

setTestSearchFeedItemsInFeed(communityId, feedType, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedItemsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q, showInternalOnly, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, recentCommentCount, density, pageParam,
pageSize, sortParam, q, result)
Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

##### **`deleteFeedItem(communityId, feedItemId)`**

Delete a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use deleteFeedElement(communityId, feedElementId).


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static Void deleteFeedItem(String communityId, String feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: Void

##### **`getCommentsForFeedItem(communityId, feedItemId)`**

Get comments for a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use getCommentsForFeedElement(communityId, feedElementId).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedItem(String communityId, String

   feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.CommentPage`

##### **`getCommentsForFeedItem(communityId, feedItemId, pageParam, pageSize)`**

Get a page of comments for a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedItem(String communityId, String

   feedItemId, String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

##### **`getFeedItem(communityId, feedItemId)`**

Get a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElement(communityId, feedElementId).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItem getFeedItem(String communityId, String feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.FeedItem`

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

##### **`getFeedItemBatch(communityId, feedItemIds)`**

Get a list of feed items.

API Version

31.0–31.0


Apex Reference Guide ChatterFeeds Class

Important: In version 32.0 and later, use getFeedElementBatch(communityId, feedElementIds).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getFeedItemBatch(String communityId, List<String>

   feedItemIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemIds
```

Type: List<String>

A list of up to 500 feed item IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.FeedItem` object and errors for feed
items that didn’t load.

Example

```
   // Create a list of feed items.

   ConnectApi.FeedItemPage feedItemPage = ConnectApi.ChatterFeeds.getFeedItemsFromFeed(null,

    ConnectApi.FeedType.Company);

   System.debug(feedItemPage);

   // Create a list of feed item IDs.

   List<String> feedItemIds = new List<String>();

   for (ConnectApi.FeedItem aFeedItem : feedItemPage.items){

      feedItemIds.add(aFeedItem.id);

   }

   // Get info about the feed items in the list.

   ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterFeeds.getFeedItemBatch(null,

   feedItemIds);

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print the header for each feed item.

        ConnectApi.FeedItem aFeedItem;

        if(batchResult.getResult() instanceof ConnectApi.FeedItem) {

          aFeedItem = (ConnectApi.FeedItem) batchResult.getResult();

```


Apex Reference Guide ChatterFeeds Class

```
        }

        System.debug('SUCCESS');

        System.debug(aFeedItem.header.text);

      }

      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

##### **`getFeedItemsFromFeed(communityId, feedType)`**

```

Get feed items from the `Company`, `Home`, and `Moderation` feeds.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)`**

Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam)

```

Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds. Each feed item contains no more than the
specified number of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,
pageParam, pageSize, sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFeeds Class

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFeed(communityId, feedType, subjectId)`**

Get feed items from a feed for a user or record.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, subjectId).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFeed(communityId, feedType, subjectId, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed items from a feed for a user or record.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize,
sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam)

```

Get a page of sorted feed items from a feed for a user or record. Each feed item includes no more than the specified number of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.


Apex Reference Guide ChatterFeeds Class

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, showInternalOnly)

```

Get a page of sorted feed items from a record feed for a user or record. Each feed item includes no more than the specified number of
comments. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.


Apex Reference Guide ChatterFeeds Class

API Version

30.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, sortParam, showInternalOnly).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix)`**

Get feed items from a feed filtered by a key prefix for a user.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix).


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFilterFeed(String communityId,

   String subjectId, String keyPrefix)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam)

```

Get a page of sorted feed items from a feed filtered by a key prefix for a user.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize,
sortParam).


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFilterFeed(String communityId,

   String subjectId, String keyPrefix, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam)

```

Get a page of sorted feed items from a feed filtered by a key prefix for a user. Each feed item contains no more than the specified number
of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount,
elementsPerBundle, density, pageParam, pageSize, sortParam).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFilterFeed(String communityId,

   String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity

   density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.


Apex Reference Guide ChatterFeeds Class

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince)

```

Get a page of feed items from a feed filtered by a key prefix for a user. Include only feed items that have been updated since the time
specified in the _`updatedSince`_ parameter.

API Version

30.0–31.0

Important: In version 32.0 and later, use getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix,
recentCommentCount, elementsPerBundle, density, pageParam, pageSize, updatedSince).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsFromFilterFeedUpdatedSince(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

Opaque token containing information about the last modified date of the feed. Do not construct this token. To retrieve this token,
call `getFeedItemsFromFilterFeed` and take the value from the `updatesToken` property of the
`ConnectApi.FeedItemPage` response body.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

This method returns only feed items that have been updated since the time specified in the _`updatedSince`_ argument. A feed item
is considered to be updated if it was created since the last feed request, or if `sort=LastModifiedDateDesc` and a comment
was added to the feed item since the last feed request. Adding likes and topics doesn’t update a feed item.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam,
pageSize, sortParam, updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsUpdatedSince(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, updatedSince)

```

Get a page of feed items from the `Company`, `Home`, and `Moderation` feeds. Include only feed items that have been updated since
the time specified in the _`updatedSince`_ parameter. Each feed item contains no more than the specified number of comments.

API Version

30.0–31.0

Important: In version 32.0 and later, use getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density,
pageParam, pageSize, updatedSince).

Available to Guest Users

31.0 only


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

This method returns only feed items that have been updated since the time specified in the _`updatedSince`_ argument. A feed item
is considered to be updated if it was created since the last feed request, or if `sort=LastModifiedDateDesc` and a comment
was added to the feed item since the last feed request. Adding likes and topics doesn’t update a feed item.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets the feed items in the company feed and grabs the `updatesToken` property from the returned object. It then
##### passes the value of updatesToken to the getFeedItemsUpdatedSince method to get the feed items updated since the

first call:

```
   // Get the feed items in the company feed and return the updatesToken

   String communityId = null;

   // Get the feed and extract the update token

   ConnectApi.FeedItemPage page = ConnectApi.ChatterFeeds.getFeedItemsFromFeed(communityId,

   ConnectApi.FeedType.Company);

   // page.updatesToken is opaque and has a value like '2:1384549034000'

   // Get the feed items that changed since the provided updatesToken

   ConnectApi.FeedItemPage feedItems= ConnectApi.ChatterFeeds.getFeedItemsUpdatedSince

     (communityId, ConnectApi.FeedType.Company, 1, ConnectApi.FeedDensity.AllUpdates, null,

   1, page.updatesToken);

```

SEE ALSO:

setTestGetFeedItemsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
ConnectApi.FeedItemPage, results)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince)

```

Get a page of feed items from the `Files`, `Groups`, `News`, `People`, and `Record` feeds. Include only feed items that have been
updated since the time specified in the _`updatedSince`_ parameter. Each feed item contains no more than the specified number of
comments.

API Version

30.0–31.0

Important: In version 32.0 and later, use getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, updatedSince).

Available to Guest Users

31.0 only


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`

**•** `Groups`

**•** `News`

**•** `People`

**•** `Record`

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

This method returns only feed items that have been updated since the time specified in the _`updatedSince`_ argument. A feed item
is considered to be updated if it was created since the last feed request, or if `sort=LastModifiedDateDesc` and a comment
was added to the feed item since the last feed request. Adding likes and topics doesn’t update a feed item.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets the feed items in the news feed and grabs the `updatesToken` property from the returned object. It then passes
##### the value of updatesToken to the getFeedItemsUpdatedSince method to get the feed items updated since the first call:

```
   // Get the feed items in the news feed and return the updatesToken

   String communityId = null;

   String subjectId = 'me';

   // Get the feed and extract the update token

   ConnectApi.FeedItemPage page = ConnectApi.ChatterFeeds.getFeedItemsFromFeed(communityId,

   ConnectApi.FeedType.News, subjectId);

   // page.updatesToken is opaque and has a value like '2:1384549034000'

   // Get the feed items that changed since the provided updatesToken

   ConnectApi.FeedItemPage feedItems= ConnectApi.ChatterFeeds.getFeedItemsUpdatedSince

    (communityId, ConnectApi.FeedType.News, subjectId, 1, ConnectApi.FeedDensity.AllUpdates,

    null, 1, page.updatesToken);

```

SEE ALSO:

setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, showInternalOnly)

```

Get a page of feed items from a record feed. Include only feed items that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.


Apex Reference Guide ChatterFeeds Class

API Version

30.0–31.0

Important: In version 32.0 and later, use getFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, updatedSince, showInternalOnly).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage getFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String


Apex Reference Guide ChatterFeeds Class

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

This method returns only feed items that have been updated since the time specified in the _`updatedSince`_ argument. A feed item
is considered to be updated if it was created since the last feed request, or if `sort=LastModifiedDateDesc` and a comment
was added to the feed item since the last feed request. Adding likes and topics doesn’t update a feed item.

If _`showInternalOnly`_ is `true` and digital experiences is enabled, feed items from Experience Cloud sites are included. Otherwise,
only feed items from the internal site are included.

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets the feed items in the news feed and grabs the `updatesToken` property from the returned object. It then passes
the value of `updatesToken` to the `getFeedItemsUpdatedSince` method to get the feed items updated since the first call:

```
   // Get the feed items in the news feed and return the updatesToken

   String communityId = null;

   String subjectId = 'me';

   // Get the feed and extract the update token

   ConnectApi.FeedItemPage page = ConnectApi.ChatterFeeds.getFeedItemsFromFeed(communityId,

   ConnectApi.FeedType.News, subjectId);

   // page.updatesToken is opaque and has a value like '2:1384549034000'

   // Get the feed items that changed since the provided updatesToken

   ConnectApi.FeedItemPage feedItems= ConnectApi.ChatterFeeds.getFeedItemsUpdatedSince

```


Apex Reference Guide ChatterFeeds Class

```
    (communityId, ConnectApi.FeedType.News, subjectId, 1, ConnectApi.FeedDensity.AllUpdates,

    null, 1, page.updatesToken, true);

```

SEE ALSO:

setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedPoll(communityId, feedItemId)`**

Get the poll associated with a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use getFeedElementPoll(communityId, feedElementId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedPoll getFeedPoll(String communityId, String feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.FeedPoll`

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

##### **`getLikesForFeedItem(communityId, feedItemId)`**

Get likes for a feed item.


Apex Reference Guide ChatterFeeds Class

API Version

28.0–31.0

Important: In version 32.0 and later, use getLikesForFeedElement(communityId, feedElementId).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedItem(String communityId, String

   feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.ChatterLikePage`

##### **`getLikesForFeedItem(communityId, feedItemId, pageParam, pageSize)`**

Get a page of likes for a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use getLikesForFeedElement(communityId, feedElementId, pageParam, pageSize).

Available to Guest Users

31.0 only

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedItem(String communityId, String

   feedItemId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

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

Type: `ConnectApi.ChatterLikePage`

##### **`likeFeedItem(communityId, feedItemId)`**

Like a feed item for the context user.

API Version

28.0–31.0

Important: In version 32.0 and later, use likeFeedElement(communityId, feedElementId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike likeFeedItem(String communityId, String feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.ChatterLike`

If the context user already liked the feed item, this method is a non-operation and returns the existing like.

##### **`postComment(communityId, feedItemId, text)`**

Post a plain-text comment to a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use postCommentToFeedElement(communityId, feedElementId, text).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment postComment(String communityId, String feedItemId,

   String text)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   text
```

Type: String

The text of the comment. Mentions are downgraded to plain text. To include a mention that links to a user, call
`postComment(communityId, feedItemId, comment, feedItemFileUpload)` and pass the mention in a
`ConnectApi.CommentInput` object.

Return Value

Type: `ConnectApi.Comment`


Apex Reference Guide ChatterFeeds Class

Usage

If hashtags or links are detected in _`text`_, they’re included in the comment as hashtag and link segments. Mentions aren’t detected in
_`text`_ and aren’t separated out of the text.

Feed items and comments can contain up to 10,000 characters.

##### **`postComment(communityId, feedItemId, comment, feedItemFileUpload)`**

Post a rich-text comment to a feed item. Use this method to include mentions and to attach a file to a comment.

API Version

28.0–31.0

Important: In version 32.0 and later, use postCommentToFeedElement(communityId, feedElementId, comment,
feedElementFileUpload).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment postComment(String communityId, String feedItemId,

   ConnectApi.CommentInput comment, ConnectApi.BinaryInput feedItemFileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   comment
```

Type: `ConnectApi.CommentInput`

In the `CommentInput` object, specify rich text, including @mentions. Optionally, in the `CommentInput.attachment`
property, specify an existing file or a new file

```
   feedItemFileUpload
```

Type: `ConnectApi.BinaryInput`

If you specify a `NewFileAttachmentInput` object in the `CommentInput.attachment` property, specify the new
binary file to attach in this argument. Otherwise, do not specify a value.

Return Value

Type: `ConnectApi.Comment`


Apex Reference Guide ChatterFeeds Class

Usage

Feed items and comments can contain up to 10,000 characters.

Sample: Posting a Comment with a New File Attachment

To post a comment and upload and attach a new file to the comment, create a `ConnectApi.CommentInput` object and a
`ConnectApi.BinaryInput` object to pass to the `ConnectApi.ChatterFeeds.postComment` method.

```
   String communityId = null;

   String feedItemId = '0D5D0000000Kcd1';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Comment Text Body';

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageInput.messageSegments.add(textSegment);

   input.body = messageInput;

   ConnectApi.NewFileAttachmentInput attachmentInput = new ConnectApi.NewFileAttachmentInput();

   attachmentInput.description = 'The description of the file';

   attachmentInput.title = 'contentFile.txt';

   input.attachment = attachmentInput;

   String fileContents = 'This is the content of the file.';

   Blob fileBlob = Blob.valueOf(fileContents);

   ConnectApi.BinaryInput binaryInput = new ConnectApi.BinaryInput(fileBlob, 'text/plain',

   'contentFile.txt');

   ConnectApi.Comment commentRep = ConnectApi.ChatterFeeds.postComment(communityId, feedItemId,

    input, binaryInput);

##### **`postFeedElement(communityId, feedElement, feedElementFileUpload)`**

```

Post a rich-text feed element. Include mentions and hashtag topics, attach a file to a feed element, and associate action link groups with
a feed element. You can also use this method to share a feed element and add a comment.

API Version

31.0–35.0

Important: In version 36.0 and later, this method is no longer available because you can’t create a feed post and upload a binary
file in the same call. Upload files to Salesforce first, and then use `postFeedElement(communityId, feedElement)`
to create the feed post and attach the files.

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement postFeedElement(String communityId,

   ConnectApi.FeedElementInput feedElement, ConnectApi.BinaryInput feedElementFileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Specify rich text, including mentions. Optionally, specify a link, a poll, an existing file, or a new file.

```
   feedElementFileUpload
```

Type: `ConnectApi.BinaryInput`

Specify the new binary file to attach to the post only if you also specify a `NewFileAttachmentInput` object in the
_`feedElement`_ parameter. Otherwise, pass `null` .

Return Value

Type: `ConnectApi.FeedElement`

Example for Posting a Feed Element with a New (Binary) File

```
   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = 'me';

   ConnectApi.ContentCapabilityInput contentInput = new ConnectApi.ContentCapabilityInput();

   contentInput.title = 'Title';

   ConnectApi.FeedElementCapabilitiesInput capabilities = new

   ConnectApi.FeedElementCapabilitiesInput();

   capabilities.content = contentInput;

   input.capabilities = capabilities;

   String text = 'These are the contents of the new file.';

   Blob myBlob = Blob.valueOf(text);

   ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

   'fileName');

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), input, binInput);

##### **`postFeedItem(communityId, feedType, subjectId, text)`**

```

Post a plain-text feed item.

API Version

28.0–31.0


Apex Reference Guide ChatterFeeds Class

Important: In version 32.0 and later, use postFeedElement(communityId, subjectId, feedElementType, text).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItem postFeedItem(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String text)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of the following:

**•** `News`

**•** `Record`

**•** `UserProfile`

Use `Record` to post to a group.

```
   subjectId
```

Type: String

The value depends on the _`feedType`_ :

**•** `News` —ID of the context user or the keyword `me` .

**•** `Record` —ID of any record with a feed, including groups.

**•** `UserProfile` —ID of any user.

```
   text
```

Type: String

Text of the feed item. Mentions are downgraded to plain text. To include a mention that links to the user, call the

```
    postFeedItem(communityId, feedType, subjectId, feedItemInput, feedItemFileUpload)
```

method and pass the mention in a `ConnectApi.FeedItemInput` object.

Return Value

Type: `ConnectApi.FeedItem`

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.


Apex Reference Guide ChatterFeeds Class

Usage

Feed items and comments can contain up to 10,000 characters.

Posts to `ConnectApi.FeedType.UserProfile` in API versions 23.0 and 24.0 created user status updates, not feed items. For
posts to the User Profile Feed in those API versions, the character limit is 1,000 characters.

##### **`postFeedItem(communityId, feedType, subjectId, feedItemInput,`**

```
  feedItemFileUpload)

```

Post a rich-text feed item to a feed. Use this method to include mentions and hashtag topics and to attach a file to a feed item. You can
also use this method to share a feed item and add a comment.

API Version

28.0–31.0

Important: In version 32.0 and later, use postFeedElement(communityId, feedElement, feedElementFileUpload).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItem postFeedItem(String communityId, ConnectApi.FeedType

   feedType, String subjectId, ConnectApi.FeedItemInput feedItemInput,

   ConnectApi.BinaryInput feedItemFileUpload)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of the following:

**•** `News`

**•** `Record`

**•** `UserProfile`

To post a feed item to a group, use `Record` and use a group ID as the _`subjectId`_ .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   feedItemInput
```

Type: `ConnectApi.FeedItemInput`


Apex Reference Guide ChatterFeeds Class

In the `FeedItemInput` object, specify rich text. Optionally, in the `FeedItemInput.attachment` property, specify a link,
a poll, an existing file, or a new file.

```
   feedItemFileUpload
```

Type: `ConnectApi.BinaryInput`

If you specify a `NewFileAttachmentInput` object in the `FeedItemInput.attachment` property, specify the new
binary file to attach in this argument. Otherwise, do not specify a value.

Return Value

Type: `ConnectApi.FeedItem`

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

Usage

Feed items and comments can contain up to 10,000 characters.Posts to `ConnectApi.FeedType.UserProfile` in API versions
23.0 and 24.0 created user status updates, not feed items. For posts to the User Profile Feed in those API versions, the character limit is
1,000 characters.

Example for Sharing a Feed Item and Adding a Comment

To share a feed item and add a comment, create a `ConnectApi.FeedItemInput` object containing the comment and the feed
item to share. Then pass the object to `ConnectApi.ChatterFeeds.postFeeditem` in the _`feedItemInput`_ argument.
The message segments in the message body input are used as the comment.

```
   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.originalFeedItemId = '0D5D0000000JuAG';

   ConnectApi.MessageBodyInput body = new ConnectApi.MessageBodyInput();

   List<ConnectApi.MessageSegmentInput> segmentList = new

   List<ConnectApi.MessageSegmentInput>();

   ConnectApi.TextSegmentInput textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'I hope you enjoy this post I found in another group.';

   segmentList.add((ConnectApi.MessageSegmentInput)textSegment);

   body.messageSegments = segmentList;

   input.body = body;

   ConnectApi.ChatterFeeds.postFeedItem(null, ConnectApi.FeedType.UserProfile, 'me', input,

   null);

```

Example for Posting a Mention to a User Profile Feed

To post to a user profile feed and include an @mention, call the `ConnectApi.ChatterFeeds.postFeedItem` method.

```
   String communityId = null;

   ConnectApi.FeedType feedType = ConnectApi.FeedType.UserProfile;

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.MentionSegmentInput mentionSegment = new ConnectApi.MentionSegmentInput();

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hey there ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment.id = '005D0000001LLO1';

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '. How are you?';

   messageInput.messageSegments.add(textSegment);

   input.body = messageInput;

   ConnectApi.FeedItem feedItemRep = ConnectApi.ChatterFeeds.postFeedItem(communityId, feedType,

    'me', input, null);

##### **`searchFeedItems(communityId, q)`**

```

Get the feed items that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElements(communityId, q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItems(String communityId, String q)

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItems(communityId, q, sortParam)`**

Get the sorted feed items that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElements(communityId, q, sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItems(String communityId, String q,

   ConnectApi.FeedSortOrder sortParam)

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
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItems(communityId, q, pageParam, pageSize)`**

Get a page of feed items that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElements(communityId, q, pageParam, pageSize).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItems(String communityId, String q,

   String pageParam, Integer pageSize)

```


Apex Reference Guide ChatterFeeds Class

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItems(communityId, q, pageParam, pageSize, sortParam)`**

Get a page of sorted feed items that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElements(communityId, q, pageParam, pageSize, sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItems(String communityId, String q,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItems(communityId, q, recentCommentCount, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed items that match the search criteria.

API Version

29.0–31.0

Important: In version 32.0 and later, use searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize,
sortParam).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItems(String communityId, String q,

   Integer recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam)

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
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.


Apex Reference Guide ChatterFeeds Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFeed(communityId, feedType, q)`**

Get the feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, q).


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam,`**

```
  q)

```

Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria.

API Version

28.0–31.0


Apex Reference Guide ChatterFeeds Class

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam,
q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.


Apex Reference Guide ChatterFeeds Class

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed items from the `Company`, `Home`, and `Moderation` feeds that match the search criteria. Each feed item
includes no more than the specified number of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density,
pageParam, pageSize, sortParam, q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFeed(communityId, feedType, subjectId, q)`**

Get the feed items from a feed that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, subjectId, q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If feed type is `UserProfile`, _`subjectId`_
can be any user ID. If _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   q
```

Type: String


Apex Reference Guide ChatterFeeds Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize,`**

```
  sortParam, q)

```

Get a page of sorted feed items from a feed for a user or record that match the search criteria.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize,
sortParam, q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`


Apex Reference Guide ChatterFeeds Class

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Order of feed items in the feed.

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Search term. Searches keywords in the user or group name. A minimum of one character is required. This parameter doesn’t support
wildcards. This parameter is required.

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed items from a feed that match the search criteria. Each feed item includes no more than the specified number
of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, sortParam, q).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.


Apex Reference Guide ChatterFeeds Class

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly)

```

Get a page of sorted feed items from a feed for a user or record that match the search criteria. Each feed item includes no more than the
specified number of comments. Specify whether to return feed items posted by internal (non-Experience Cloud site) users only.

API Version

30.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,
density, pageParam, pageSize, sortParam, q, showInternalOnly).

Available to Guest Users

31.0 only

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Value must be `ConnectApi.FeedType.Record` .

```
   subjectId
```

Type: String

Any record ID, including a group ID.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.


Apex Reference Guide ChatterFeeds Class

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q)`**

Get the feed items that match the search criteria from a feed filtered by a key prefix for a user.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFilterFeed(String communityId,

   String subjectId, String keyPrefix, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam, q)

```

Get a page of sorted feed items that match the search criteria from a feed filtered by a key prefix for a user.

API Version

28.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize,
sortParam, q).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFilterFeed(String communityId,

   String subjectId, String keyPrefix, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed items that match the search criteria from a feed filtered by a key prefix for a user. Each feed item includes no
more than the specified number of comments.

API Version

29.0–31.0

Important: In version 32.0 and later, use searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount,
density, pageParam, pageSize, sortParam, q).


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItemPage searchFeedItemsInFilterFeed(String communityId,

   String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity

   density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String

   q)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, recentCommentCount, density, pageParam,
pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`shareFeedElement(communityId, subjectId, feedElementType,`**

```
  originalFeedElementId)

```

Share the _`originalFeedElementId`_ as the context user.

API Version

31.0–38.0

Important: In version 39.0 and later, use `postFeedElement(communityId, feedElement)` or

`updateFeedElement(communityId, feedElementId, feedElement)` with the
`ConnectApi.FeedEntityShareCapabilityInput` to share a feed entity with a feed element.

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement shareFeedElement(String communityId, String

   subjectId, ConnectApi.FeedElementType feedElementType, String originalFeedElementId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

The ID of the user or group with whom to share the feed element.

```
   feedElementType
```

Type: `ConnectApi.FeedElementType`

Values are:

**•** `Bundle` —A container of feed elements. A bundle also has a body made up of message segments that can always be gracefully
degraded to text-only values.

**•** `FeedItem` —A feed item has a single parent and is scoped to oneExperience Cloud site or across all Experience Cloud sites. A
feed item can have capabilities such as bookmarks, canvas, content, comment, link, poll. Feed items have a body made up of
message segments that can always be gracefully degraded to text-only values.

**•** `Recommendation` —A recommendation is a feed element with a recommendations capability. A recommendation suggests
records to follow, groups to join, or applications that are helpful to the context user.

```
   originalFeedElementId
```

Type: String

The ID of the feed element to share.

Return Value

Type: `ConnectApi.FeedElement`

Example

```
   ConnectApi.ChatterFeeds.shareFeedElement(null, '0F9RR0000004CPw',

   ConnectApi.FeedElementType.FeedItem, '0D5RR0000004Gxc');

##### **`shareFeedItem(communityId, feedType, subjectId, originalFeedItemId)`**

```

Share the _`originalFeedItemId`_ to the feed specified by the _`feedType`_ .

API Version

28.0–31.0

Important:

**•** In version 32.0–38.0, use `shareFeedElement(communityId, subjectId, feedElementType,`
`originalFeedElementId)` .


Apex Reference Guide ChatterFeeds Class

**•** In version 39.0 and later, use `postFeedElement(communityId, feedElement)` or

`updateFeedElement(communityId, feedElementId, feedElement)` with the
`ConnectApi.FeedEntityShareCapabilityInput` .

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItem shareFeedItem(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String originalFeedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of the following:

**•** `News`

**•** `Record`

**•** `UserProfile`

To share a feed item with a group, use `Record` and use a group ID as the _`subjectId`_ .

```
   subjectId
```

Type: String

The value depends on the value of _`feedType`_ :

**•** `News`     - _`subjectId`_ must be the ID of the context user or the keyword `me` .

**•** `Record`     - _`subjectId`_ can be a group ID or the ID of the context user (or `me` ).

**•** `UserProfile`     - _`subjectId`_ can be any user ID.

```
   originalFeedItemId
```

Type: String

The ID of the feed item to share.

Return Value

Type: `ConnectApi.FeedItem`


Apex Reference Guide ChatterFeeds Class

Example

To share a feed item with a group, pass in the Experience Cloud site ID (or `null` ), the feed type `Record`, the group ID, and the ID of
the feed item to share.

```
   ConnectApi.ChatterFeeds.shareFeedItem(null, ConnectApi.FeedType.Record, '0F9D00000000izf',

    '0D5D0000000JuAG');

##### **`updateBookmark(communityId, feedItemId, isBookmarkedByCurrentUser)`**

```

Bookmark a feed item or remove a bookmark from a feed item.

API Version

28.0–31.0

Important: In version 32.0 and later, use updateFeedElementBookmarks(communityId, feedElementId, bookmarks) or
updateFeedElementBookmarks(communityId, feedElementId, isBookmarkedByCurrentUser).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedItem updateBookmark(String communityId, String feedItemId,

   Boolean isBookmarkedByCurrentUser)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   isBookmarkedByCurrentUser
```

Type: Boolean

—Specifying `true` adds the feed item to the list of bookmarks for the context user. Specify `false` to remove a bookmark.

Return Value

Type: `ConnectApi.FeedItem`

##### **`voteOnFeedPoll(communityId, feedItemId, myChoiceId)`**

Vote or change your vote on a feed poll.


Apex Reference Guide ChatterFeeds Class

API Version

28.0–31.0

Important: In version 32.0 and later, use voteOnFeedElementPoll(communityId, feedElementId, myChoiceId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedPoll voteOnFeedPoll(String communityId, String feedItemId,

   String myChoiceId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID of the feed item that is associated with the poll.

```
   myChoiceId
```

Type: String

ID of the item in the poll you’re voting for.

Return Value

Type: `ConnectApi.FeedPoll`

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, subjectId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, showInternalOnly,

  result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsFromFeed` is called with matching
parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

30.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, Boolean

   showInternalOnly, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.


Apex Reference Guide ChatterFeeds Class

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

28.0–31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedItemsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching `getFeedItemsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestGetFeedItemsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.


Apex Reference Guide ChatterFeeds Class

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId,`**

```
  keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,

  updatedSince, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the `getFeedItemsFromFilterFeedUpdatedSince`
method is called in a test context.

API Version

30.0–31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedItemsFromFilterFeedUpdatedSince(String communityId,

   String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity

   density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String

   updatedSince, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   updatedSince
```

Type: String

Opaque token containing information about the last modified date of the feed. Do not construct this token. To retrieve this token,
call `getFeedItemsFromFilterFeed` and take the value from the `updatesToken` property of the
`ConnectApi.FeedItemPage` response body.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, ConnectApi.FeedItemPage, results)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

30.0–31.0

Signature

```
   public static Void setTestGetFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedItemPage results)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`


Apex Reference Guide ChatterFeeds Class

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

30.0–31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`

**•** `Groups`

**•** `News`

**•** `People`

**•** `Record`

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String


Apex Reference Guide ChatterFeeds Class

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedItemsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince,

  showInternalOnly, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when `getFeedItemsUpdatedSince` is called with matching
parameters in a test context. Use the method with the same parameters or the code throws an exception.

API Version

30.0–31.0

Signature

```
   public static Void setTestGetFeedItemsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize, String updatedSince,

   Boolean showInternalOnly, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

One of these values:

**•** `Files`

**•** `Groups`

**•** `News`

**•** `People`

**•** `Record`


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

If _`feedType`_ is `ConnectApi.Record`, _`subjectId`_ can be any record ID, including a group ID. Otherwise, it must be the
context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   updatedSince
```

Type: String

An opaque token containing information about the last modified date of the feed. Do not construct this token. Retrieve this token
from the `updatesToken` property of the `ConnectApi.FeedItemPage` response body.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedItemsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, updatedSince,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedItems(communityId, q, result)`**

Register a test feed item page to be returned when `searchFeedItems(communityId, q)` is called during a test.

API Version

28.0–31.0

Signature

```
   public static Void searchFeedItems(String communityId, String q, ConnectApi.FeedItemPage

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
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItems(communityId, q, sortParam, result)`**

Register a test feed item page to be returned when `searchFeedItems(String, String,`
`ConnectApi.FeedSortOrder)` is called during a test.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItems(String communityId, String q,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)

```


Apex Reference Guide ChatterFeeds Class

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
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

The feed item test page.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItems(communityId, q, pageParam, pageSize, result)`**

Register a test feed item page to be returned when `searchFeedItems(String, String, String, Integer)` is called
during a test.

API Version

28.0–31.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestSearchFeedItems(String communityId, String q, String pageParam,

   Integer pageSize, ConnectApi.FeedItemPage result)

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   result
```

Type: `ConnectApi.FeedItemPage`

The test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItems(communityId, q, pageParam, pageSize, sortParam, result)`**

Register a test feed item page to be returned when `searchFeedItems(String, String, String, Integer,`
`ConnectApi.FeedSortOrder)` is called during a test.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItems(String communityId, String q, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)

```


Apex Reference Guide ChatterFeeds Class

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

The test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedItems(communityId, q, recentCommentCount, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a test feed item page to be returned when `searchFeedItems(communityId, q, recentCommentCount,`
`pageParam, pageSize, sortParam)` is called during a test.

API Version

29.0–31.0

Signature

```
   public static Void setTestSearchFeedItems(String communityId, String q, Integer

   recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedItemPage result)

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
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFeeds Class

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   result
```

Type: `ConnectApi.FeedItemPage`

The test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q, recentCommentCount, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, q, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, q, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String

   q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, q, result)`**

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, String q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedItemPage result)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ChatterFeeds Class

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q,

  showInternalOnly, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFeed` method is called in a test context. Use the method with the same parameters or you
receive an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   Boolean showInternalOnly, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessages`, `Filter`,
`Landing`, and `Streams` .


Apex Reference Guide ChatterFeeds Class

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   showInternalOnly
```

Type: Boolean


Apex Reference Guide ChatterFeeds Class

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q,`**

```
  result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFilterFeed(String communityId, String

   subjectId, String keyPrefix, String q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   q
```

Type: String


Apex Reference Guide ChatterFeeds Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Specify the test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId,`**

```
  keyPrefix, pageParam, pageSize, sortParam, q, result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

28.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFilterFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String keyPrefix, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String


Apex Reference Guide ChatterFeeds Class

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Specify the test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId,`**

```
  keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam, q,

  result)

```

Register a `ConnectApi.FeedItemPage` object to be returned when the matching
`ConnectApi.searchFeedItemsInFilterFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

29.0–31.0

Signature

```
   public static Void setTestSearchFeedItemsInFilterFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String keyPrefix, Integer

   recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedType
```

Type: `ConnectApi.FeedType`

Type of feed. Valid values include every `ConnectApi.FeedType` except `Company`, `DirectMessageModeration`,
`DirectMessages`, `Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   keyPrefix
```

Type: String

A key prefix that specifies record type. A key prefix is the first three characters in the object ID, which specifies the object type. For
example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed item. The default value is 3.

```
   density
```

Type: `ConnectApi.FeedDensity`

Specify the amount of content in a feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also displays
custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and groups the user is a member of. Also
displays custom recommendations, but hides some system-generated updates from records.


### Apex Reference Guide ChatterGroups Class

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Number of feed items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.FeedSortOrder`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

Sorts the returned feed by the most recently created feed item, or by the most recently modified feed item. If you pass in `null`,
the default value `CreatedDateDesc` is used.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Specify the test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,
q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ChatterGroups Class

Information about groups, such as the group’s members, photo, and the groups the specified user is a member of. Add members to a
group, remove members, and change the group photo.


Apex Reference Guide ChatterGroups Class

Namespace

ConnectApi

#### ChatterGroups Methods These methods are for ChatterGroups . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

addMember(communityId, groupId, userId)
Add a user to a group as a standard member.

addMemberWithRole(communityId, groupId, userId, role)
Add a user with a role to a group.

addRecord(communityId, groupId, recordId)
Associate a record with a group.

createGroup(communityId, groupInput)
Create a group.

deleteBannerPhoto(communityId, groupId)
Delete the group banner photo.

deleteGroup(communityId, groupId)
Delete a group.

deleteMember(communityId, membershipId)
Remove a member from a group.

deletePhoto(communityId, groupId)
Delete the group photo.

getAnnouncements(communityId, groupId)
Get the first page of announcements in a group.

getAnnouncements(communityId, groupId, pageParam, pageSize)
Get a page of announcements in a group.

getBannerPhoto(communityId, groupId)
Get the group banner photo.

getGroup(communityId, groupId)
Get information about a group.

getGroupBatch(communityId, groupIds)
Get information about a list of groups.

getGroupMembershipRequest(communityId, requestId)
Get information about a request to join a private group.

getGroupMembershipRequests(communityId, groupId)
Get information about every request to join a private group.


Apex Reference Guide ChatterGroups Class

getGroupMembershipRequests(communityId, groupId, status)
Get information about every request to join a private group that has a specified status.

getGroups(communityId)
Get the first page of groups.

getGroups(communityId, pageParam, pageSize)
Get a page of groups.

getGroups(communityId, pageParam, pageSize, archiveStatus)
Get a page of groups with an archive status.

getMember(communityId, membershipId)
Get information about a group member.

getMembers(communityId, groupId)
Get the first page of information about the members of a group.

getMembers(communityId, groupId, pageParam, pageSize)
Get a page of information about the members of a group.

getMembershipBatch(communityId, membershipIds)
Get information about a list of group memberships.

getMyChatterSettings(communityId, groupId)
Get the context user’s Chatter settings for a group.

getPhoto(communityId, groupId)
Get the photo for a group.

getRecord(communityId, groupRecordId)
Get a record associated with a group.

getRecords(communityId, groupId)
Get the first page of records associated with a group.

getRecords(communityId, groupId, pageParam, pageSize)
Get a page of records associated with a group.

inviteUsers(groupId, invite)
Invite internal and external users to join a group.

postAnnouncement(communityId, groupId, announcement)
Post an announcement to a group.

removeRecord(communityId, groupRecordId)
Remove the association of a record with a group.

requestGroupMembership(communityId, groupId)
Request membership in a private group.

searchGroups(communityId, q)
Get the first page of groups that match the search criteria.

searchGroups(communityId, q, pageParam, pageSize)
Get a page of groups that match the search criteria.

searchGroups(communityId, q, archiveStatus, pageParam, pageSize)
Get a page of groups with the archive status that match the search criteria.


Apex Reference Guide ChatterGroups Class

setBannerPhoto(communityId, groupId, fileId, versionNumber)
Set an uploaded file as the group banner photo.

setBannerPhoto(communityId, groupId, fileUpload)
Set a file that hasn’t been uploaded as the group banner photo.

setBannerPhotoWithAttributes(communityId, groupId, bannerPhoto)
Set and crop an uploaded file as the group banner photo.

setBannerPhotoWithAttributes(communityId, groupId, bannerPhoto, fileUpload)
Set and crop a file that hasn’t been uploaded as the group banner photo.

setPhoto(communityId, groupId, fileId, versionNumber)
Set an uploaded file as the group photo.

setPhoto(communityId, groupId, fileUpload)
Set a file that hasn’t been uploaded as the group photo.

setPhotoWithAttributes(communityId, groupId, photo)
Set and crop an uploaded file as the group photo.

setPhotoWithAttributes(communityId, groupId, photo, fileUpload)
Set and crop a file that hasn’t been uploaded as the group photo.

updateGroup(communityId, groupId, groupInput)
Update the settings of a group.

updateGroupMember(communityId, membershipId, role)
Update the role of a group member.

updateMyChatterSettings(communityId, groupId, emailFrequency)
Update the context user’s email frequency for a group.

updateRequestStatus(communityId, requestId, status)
Update a request to join a private group.

updateRequestStatus(communityId, requestId, status, responseMessage)
Update a request to join a private group and optionally provide a message when the request is denied.

##### **`addMember(communityId, groupId, userId)`**

Add a user to a group as a standard member.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMember addMember(String communityId, String groupId,

   String userId)

```


Apex Reference Guide ChatterGroups Class

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
   userId
```

Type: String

ID for a user.

Return Value

Type: `ConnectApi.GroupMember`

Usage

To execute this method, the context user must be the group owner or moderator.

##### **`addMemberWithRole(communityId, groupId, userId, role)`**

Add a user with a role to a group.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMember addMemberWithRole(String communityId, String

   groupId, String userId, ConnectApi.GroupMembershipType role)

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
   userId
```

Type: String


Apex Reference Guide ChatterGroups Class

ID for a user.

```
   role
```

Type: `ConnectApi.GroupMembershipType`

The group membership type. One of these values:

**•** `GroupManager`

**•** `StandardMember`

Return Value

Type: `ConnectApi.GroupMember`

Usage

To execute this method, the context user must be the group owner or moderator.

##### **`addRecord(communityId, groupId, recordId)`**

Associate a record with a group.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupRecord addRecord(String communityId, String groupId,

   String recordId)

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

ID of the group with which to associate the record.

```
   recordId
```

Type: String

ID of the record to associate with the group.

Return Value

Type: `ConnectApi.GroupRecord`


Apex Reference Guide ChatterGroups Class

##### **`createGroup(communityId, groupInput)`**

Create a group.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupDetail createGroup(String, communityId,

   ConnectApi.ChatterGroupInput groupInput)

```

Parameters

```
   communityId
```

Type: String,

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupInput
```

Type: `ConnectApi.ChatterGroupInput`

The properties of the group.

Return Value

Type: `ConnectApi.ChatterGroupDetail`

##### **`deleteBannerPhoto(communityId, groupId)`**

Delete the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static Void deleteBannerPhoto(String communityId, String groupId)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterGroups Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupId
```

Type: String

ID of the group.

Return Value

Type: Void

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

##### **`deleteGroup(communityId, groupId)`**

Delete a group.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static Void deleteGroup(String communityId, String groupId)

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

Type: Void

##### **`deleteMember(communityId, membershipId)`**

Remove a member from a group.

API Version

28.0


Apex Reference Guide ChatterGroups Class

Requires Chatter

Yes

Signature

```
   public static Void deleteMember(String communityId, String membershipId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   membershipId
```

Type: String

ID for a membership.

Return Value

Type: Void

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

##### **`deletePhoto(communityId, groupId)`**

Delete the group photo.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deletePhoto(String communityId, String groupId)

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


Apex Reference Guide ChatterGroups Class

Return Value

Type: Void

Usage

This method is only successful when the context user is the group manager or owner, or has Modify All Data permission.

##### **`getAnnouncements(communityId, groupId)`**

Get the first page of announcements in a group.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.AnnouncementPage getAnnouncements(String communityId, String

   groupId)

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

Type: `ConnectApi.AnnouncementPage`

Usage

To post an announcement, get information about an announcement, update the expiration date of an announcement, or delete an
announcement, use the methods of the `ConnectApi.Announcements` class.

##### **`getAnnouncements(communityId, groupId, pageParam, pageSize)`**

Get a page of announcements in a group.

API Version

31.0


Apex Reference Guide ChatterGroups Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.AnnouncementPage getAnnouncements(String communityId, String

   groupId, Integer pageParam, Integer pageSize)

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

Type: `ConnectApi.AnnouncementPage`

Usage

To post an announcement, get information about an announcement, update the expiration date of an announcement, or delete an
announcement, use the methods of the `ConnectApi.Announcements` class.

##### **`getBannerPhoto(communityId, groupId)`**

Get the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto getBannerPhoto(String communityId, String groupId)

```


Apex Reference Guide ChatterGroups Class

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

The ID of the group.

Return Value

Type: `ConnectApi.BannerPhoto`

##### **`getGroup(communityId, groupId)`**

Get information about a group.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupDetail getGroup(String communityId, String groupId)

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

Type: `ConnectApi.ChatterGroupDetail`

##### **`getGroupBatch(communityId, groupIds)`**

Get information about a list of groups.


Apex Reference Guide ChatterGroups Class

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getGroupBatch(String communityId, List<String>

   groupIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupIds
```

Type: List<String>

A list of up to 500 group IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.ChatterGroup` object and errors
embedded in the results for groups that didn’t load.

Example

```
   // Create a list of groups.

   ConnectApi.ChatterGroupPage groupPage = ConnectApi.ChatterGroups.getGroups(null);

   // Create a list of group IDs.

   List<String> groupIds = new List<String>();

   for (ConnectApi.ChatterGroup aGroup : groupPage.groups){

      groupIds.add(aGroup.id);

   }

   // Get info about all the groups in the list.

   ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterGroups.getGroupBatch(null,

   groupIds);

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print the number of members in each group.

        ConnectApi.ChatterGroup aGroup;

        if(batchResult.getResult() instanceof ConnectApi.ChatterGroup) {

          aGroup = (ConnectApi.ChatterGroup) batchResult.getResult();

        }

```


Apex Reference Guide ChatterGroups Class

```
        System.debug('SUCCESS');

        System.debug(aGroup.memberCount);

      }

      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

```

SEE ALSO:

getMembershipBatch(communityId, membershipIds)

##### **`getGroupMembershipRequest(communityId, requestId)`**

Get information about a request to join a private group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequest getGroupMembershipRequest(String

   communityId, String requestId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   requestId
```

Type: String

The ID of a request to join a private group.

Return Value

Type: `ConnectApi.GroupMembershipRequest`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.


Apex Reference Guide ChatterGroups Class

##### **`getGroupMembershipRequests(communityId, groupId)`**

Get information about every request to join a private group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequests getGroupMembershipRequests(String

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

Type: `ConnectApi.GroupMembershipRequests`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

##### **`getGroupMembershipRequests(communityId, groupId, status)`**

Get information about every request to join a private group that has a specified status.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequests getGroupMembershipRequests(String

   communityId, String groupId, ConnectApi.GroupMembershipRequestStatus status)

```


Apex Reference Guide ChatterGroups Class

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
   status
```

Type: `ConnectApi.GroupMembershipRequestStatus`

_`status`_ —Status of a request to join a private group.

**•** `Accepted`

**•** `Declined`

**•** `Pending`

Return Value

Type: `ConnectApi.GroupMembershipRequests`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

##### **`getGroups(communityId)`**

Get the first page of groups.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage getGroups(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterGroups Class

Return Value

Type: `ConnectApi.ChatterGroupPage`

##### **`getGroups(communityId, pageParam, pageSize)`**

Get a page of groups.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage getGroups(String communityId, Integer

   pageParam, Integer pageSize)

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

Type: `ConnectApi.ChatterGroupPage`

##### **`getGroups(communityId, pageParam, pageSize, archiveStatus)`**

Get a page of groups with an archive status.

API Version

29.0


Apex Reference Guide ChatterGroups Class

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage getGroups(String communityId, Integer

   pageParam, Integer pageSize, ConnectApi.GroupArchiveStatus archiveStatus)

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
   archiveStatus
```

Type: `ConnectApi.GroupArchiveStatus`

Archive status of groups.

**•** `All` —All groups, including groups that are archived and groups that aren’t archived.

**•** `Archived` —Groups that are archived.

**•** `NotArchived` —Groups that aren’t archived.

If you pass in `null`, the default value is `All` .

Return Value

Type: `ConnectApi.ChatterGroupPage`

##### **`getMember(communityId, membershipId)`**

Get information about a group member.

API Version

28.0

Requires Chatter

Yes


Apex Reference Guide ChatterGroups Class

Signature

```
   public static ConnectApi.GroupMember getMember(String communityId, String membershipId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   membershipId
```

Type: String

ID for a membership.

Return Value

Type: `ConnectApi.GroupMember`

##### **`getMembers(communityId, groupId)`**

Get the first page of information about the members of a group.

API Version

28.0

Available to Guest Users

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMemberPage getMembers(String communityId, String groupId)

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

Type: `ConnectApi.GroupMemberPage`


Apex Reference Guide ChatterGroups Class

##### **`getMembers(communityId, groupId, pageParam, pageSize)`**

Get a page of information about the members of a group.

API Version

28.0

Available to Guest Users

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMemberPage getMembers(String communityId, String groupId,

   Integer pageParam, Integer pageSize)

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

Type: `ConnectApi.GroupMemberPage`

##### **`getMembershipBatch(communityId, membershipIds)`**

Get information about a list of group memberships.

API Version

31.0


Apex Reference Guide ChatterGroups Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getMembershipBatch(String communityId,

   List<String> membershipIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   membershipIds
```

Type: List<String>

A list of up to 500 group membership IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.GroupMember` object and errors
embedded in the results for group memberships that didn’t load.

Example

```
   // Get members of a group.

   ConnectApi.GroupMemberPage membersPage = ConnectApi.ChatterGroups.getMembers(null,

   '0F9D00000000oOT');

   // Create a list of membership IDs.

   List<String> membersList = new List<String>();

   for (ConnectApi.GroupMember groupMember : membersPage.members){

      membersList.add(groupMember.id);

   }

   // Get info about all group memberships in the list.

   ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterGroups.getMembershipBatch(null,

    membersList);

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print the first name of each member.

        ConnectApi.GroupMember groupMember;

        if(batchResult.getResult() instanceof ConnectApi.GroupMember) {

           groupMember = (ConnectApi.GroupMember) batchResult.getResult();

        }

        System.debug('SUCCESS');

        System.debug(groupMember.user.firstName);

      }

```


Apex Reference Guide ChatterGroups Class

```
      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

```

SEE ALSO:

getGroupBatch(communityId, groupIds)

##### **`getMyChatterSettings(communityId, groupId)`**

Get the context user’s Chatter settings for a group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupChatterSettings getMyChatterSettings(String communityId,

   String groupId)

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

Type: `ConnectApi.GroupChatterSettings`

##### **`getPhoto(communityId, groupId)`**

Get the photo for a group.

API Version

28.0


Apex Reference Guide ChatterGroups Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo getPhoto(String communityId, String groupId)

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

Type: `ConnectApi.Photo`

##### **`getRecord(communityId, groupRecordId)`**

Get a record associated with a group.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupRecord getRecord(String communityId, String groupRecordId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupRecordId
```

Type: String

ID of the group record.

Return Value

Type: `ConnectApi.GroupRecord`


Apex Reference Guide ChatterGroups Class

##### **`getRecords(communityId, groupId)`**

Get the first page of records associated with a group.

API Version

33.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupRecordPage getRecords(String communityId, String groupId)

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

Type: `ConnectApi.GroupRecordPage`

##### **`getRecords(communityId, groupId, pageParam, pageSize)`**

Get a page of records associated with a group.

API Version

33.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupRecordPage getRecords(String communityId, String groupId,

   Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterGroups Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupId
```

Type: String

ID for a group.

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

Type: `ConnectApi.GroupRecordPage`

##### **`inviteUsers(groupId, invite)`**

Invite internal and external users to join a group.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Invitations inviteUsers(String groupId, ConnectApi.InviteInput

   invite)

```

Parameters

```
   groupId
```

Type: String

ID of the group.

##### _`invite`_

Type: `ConnectApi.InviteInput`

A `ConnectApi.InviteInput` body.

Return Value

Type: `ConnectApi.Invitations`


Apex Reference Guide ChatterGroups Class

##### **`postAnnouncement(communityId, groupId, announcement)`**

Post an announcement to a group.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Announcement postAnnouncement(String communityId, String

   groupId, ConnectApi.AnnouncementInput announcement)

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
   announcement
```

Type: `ConnectApi.AnnouncementInput`

A `ConnectApi.AnnouncementInput` object.

Return Value

Type: `ConnectApi.Announcement`

Usage

Use an announcement to highlight information. Users can discuss, like, and post comments on announcements. Deleting the feed post
deletes the announcement.

To post an announcement, get information about an announcement, update the expiration date of an announcement, or delete an
announcement, use the methods of the `ConnectApi.Announcements` class.

##### **`removeRecord(communityId, groupRecordId)`**

Remove the association of a record with a group.

API Version

34.0


Apex Reference Guide ChatterGroups Class

Requires Chatter

Yes

Signature

```
   public static Void removeRecord(String communityId, String groupRecordId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupRecordId
```

Type: String

ID of the group record.

Return Value

Type: Void

##### **`requestGroupMembership(communityId, groupId)`**

Request membership in a private group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequest requestGroupMembership(String

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


Apex Reference Guide ChatterGroups Class

Return Value

Type: `ConnectApi.GroupMembershipRequest`

Sample: Requesting to Join a Private Group

This sample code calls `ConnectApi.ChatterGroups.requestGroupMembership` to request to join a private group.

```
   String communityId = null;

   ID groupId = '0F9x00000000hAZ';

   ConnectApi.GroupMembershipRequest membershipRequest =

   ConnectApi.ChatterGroups.requestGroupMembership(communityId, groupId);

##### **`searchGroups(communityId, q)`**

```

Get the first page of groups that match the search criteria.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage searchGroups(String communityId, String q)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

Return Value

Type: `ConnectApi.ChatterGroupPage`


Apex Reference Guide ChatterGroups Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchGroups(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchGroups(communityId, q, pageParam, pageSize)`**

Get a page of groups that match the search criteria.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage searchGroups(String communityId, String q,

   Integer pageParam, Integer pageSize)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

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


Apex Reference Guide ChatterGroups Class

Return Value

Type: `ConnectApi.ChatterGroupPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchGroups(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchGroups(communityId, q, archiveStatus, pageParam, pageSize)`**

Get a page of groups with the archive status that match the search criteria.

API Version

29.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterGroupPage searchGroups(String communityId, String q,

   ConnectApi.GroupArchiveStatus archiveStatus, Integer pageParam, Integer pageSize)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

```
   archiveStatus
```

Type: `ConnectApi.GroupArchiveStatus`

Archive status of groups.

**•** `All` —All groups, including groups that are archived and groups that aren’t archived.

**•** `Archived` —Groups that are archived.


Apex Reference Guide ChatterGroups Class

**•** `NotArchived` —Groups that aren’t archived.

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

Type: `ConnectApi.ChatterGroupPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchGroups(communityId, q, archiveStatus, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setBannerPhoto(communityId, groupId, fileId, versionNumber)`**

Set an uploaded file as the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String communityId, String groupId,

   String fileId, Integer versionNumber)

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

The ID of the group.


Apex Reference Guide ChatterGroups Class

```
   fileId
```

Type: String

The ID of the already uploaded file. The key prefix must be 069, and the image must be smaller than 8 MB.

```
   versionNumber
```

Type: Integer

Version number of the existing file. Specify either an existing version number or, to get the latest version, specify `null` .

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhoto(communityId, groupId, fileUpload)`**

Set a file that hasn’t been uploaded as the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String communityId, String groupId,

   ConnectApi.BinaryInput fileUpload)

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

The ID of the group.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.


Apex Reference Guide ChatterGroups Class

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhotoWithAttributes(communityId, groupId, bannerPhoto)`**

Set and crop an uploaded file as the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String communityId,

   String groupId, ConnectApi.BannerPhotoInput bannerPhoto)

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

The ID of the group.

```
   bannerPhoto
```

Type: `ConnectApi.BannerPhotoInput`

A `ConnectApi.BannerPhotoInput` object that specifies the ID and version of the file, and how to crop the file.

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.


Apex Reference Guide ChatterGroups Class

##### **`setBannerPhotoWithAttributes(communityId, groupId, bannerPhoto, fileUpload)`**

Set and crop a file that hasn’t been uploaded as the group banner photo.

API Version

36.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String communityId,

   String groupId, ConnectApi.BannerPhotoInput bannerPhoto, ConnectApi.BinaryInput

   fileUpload)

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

The ID of the group.

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

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

##### **`setPhoto(communityId, groupId, fileId, versionNumber)`**

Set an uploaded file as the group photo.


Apex Reference Guide ChatterGroups Class

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhoto(String communityId, String groupId, String

   fileId, Integer versionNumber)

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
   fileId
```

Type: String

ID of a file already uploaded. The key prefix must be 069, and the file must be an image that is smaller than 2 GB.

```
   versionNumber
```

Type: Integer

Version number of the existing file. Specify either an existing version number or, to get the latest version, specify `null` .

Return Value

Type: `ConnectApi.Photo`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

Sample: Updating a Group Photo with an Existing File

When a group is created, it doesn’t have a group photo. You can set an existing photo that has already been uploaded to Salesforce as
the group photo. The key prefix must be 069 and the file size must be less than 2 GB.

```
   String communityId = null;

   ID groupId = '0F9x00000000hAK';

   ID fileId = '069x00000001Ion';

   // Set photo

   ConnectApi.Photo photo = ConnectApi.ChatterGroups.setPhoto(communityId, groupId, fileId,

   null);

```


Apex Reference Guide ChatterGroups Class

##### **`setPhoto(communityId, groupId, fileUpload)`**

Set a file that hasn’t been uploaded as the group photo.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhoto(String communityId, String groupId,

   ConnectApi.BinaryInput fileUpload)

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
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

Sample: Uploading a New File and Using It as a Group Photo

When a group is created, it doesn’t have a group photo. You can upload a photo and set it as the group photo.

```
   String communityId = null;

   ID groupId = '0F9x00000000hAP';

   ID photoId = '069x00000001Ioo';

   // Set photo

   List<ContentVersion> groupPhoto = [Select c.VersionData From ContentVersion c where

   ContentDocumentId=:photoId];

   ConnectApi.BinaryInput binary = new ConnectApi.BinaryInput(groupPhoto.get(0).VersionData,

```


Apex Reference Guide ChatterGroups Class

```
    'image/png', 'image.png');

   ConnectApi.Photo photo = ConnectApi.ChatterGroups.setPhoto(communityId, groupId, binary);

##### **`setPhotoWithAttributes(communityId, groupId, photo)`**

```

Set and crop an uploaded file as the group photo.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String communityId, String groupId,

   ConnectApi.PhotoInput photo)

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
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object that specifies the ID and version of the file, and how to crop the file.

Return Value

Type: `ConnectApi.Photo`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(communityId, groupId, photo, fileUpload)`**

Set and crop a file that hasn’t been uploaded as the group photo.


Apex Reference Guide ChatterGroups Class

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String communityId, String groupId,

   ConnectApi.PhotoInput photo, ConnectApi.BinaryInput fileUpload)

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
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object that specifies how to crop the file specified in _`fileUpload`_ .

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Photos are processed asynchronously and might not be visible right away.

##### **`updateGroup(communityId, groupId, groupInput)`**

Update the settings of a group.

API Version

28.0

Requires Chatter

Yes


Apex Reference Guide ChatterGroups Class

Signature

```
   public static ConnectApi.ChatterGroup updateGroup(String communityId, String groupId,

   ConnectApi.ChatterGroupInput groupInput)

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
   groupInput
```

Type: `ConnectApi.ChatterGroupInput`

A `ConnectApi.ChatterGroupInput` object.

Return Value

Type: `ConnectApi.ChatterGroup`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission. Use this method
to update any settings in the `ConnectApi.ChatterGroupInput` class. These settings include the group title and text in the
“Information” section, whether the group is public or private, and whether the group is archived.

Example

This example archives a group.

```
   String groupId = '0F9D00000000qSz';

   String communityId = null;

   ConnectApi.ChatterGroupInput groupInput = new ConnectApi.ChatterGroupInput();

   groupInput.isArchived = true;

   ConnectApi.ChatterGroups.updateGroup(communityId, groupId, groupInput);

##### **`updateGroupMember(communityId, membershipId, role)`**

```

Update the role of a group member.

API Version

29.0

Requires Chatter

Yes


Apex Reference Guide ChatterGroups Class

Signature

```
   public static ConnectApi.ChatterGroup updateGroupMember(String communityId, String

   membershipId, ConnectApi.GroupMembershipType role)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   membershipId
```

Type: String

ID for a membership.

```
   role
```

Type: `ConnectApi.GroupMembershipType`

The group membership type. One of these values:

**•** `GroupManager`

**•** `StandardMember`

Return Value

Type: `ConnectApi.ChatterGroup`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

##### **`updateMyChatterSettings(communityId, groupId, emailFrequency)`**

Update the context user’s email frequency for a group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupChatterSettings updateMyChatterSettings(String communityId,

   String groupId, ConnectApi.GroupEmailFrequency emailFrequency)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterGroups Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   groupId
```

Type: String

ID for a group.

```
   emailFrequency
```

Type: `ConnectApi.GroupEmailFrequency`

Frequency with which a user receives email.

**•** `EachPost`

**•** `DailyDigest`

**•** `WeeklyDigest`

**•** `Never`

**•** `UseDefault`

The value `UseDefault` uses the value set in a call to `updateChatterSettings(communityId, userId,`
`defaultGroupEmailFrequency)` .

Return Value

Type: `ConnectApi.GroupChatterSettings`

##### **`updateRequestStatus(communityId, requestId, status)`**

Update a request to join a private group.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequest updateRequestStatus(String communityId,

   String requestId, ConnectApi.GroupMembershipRequestStatus status)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   requestId
```

Type: String

ID for a request to join a private group.

```
   status
```

Type: `ConnectApi.GroupMembershipRequestStatus`


Apex Reference Guide ChatterGroups Class

Status of the request:

**•** `Accepted`

**•** `Declined`

The `Pending` value of the enum is not valid in this method.

Return Value

Type: `ConnectApi.GroupMembershipRequest`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

Sample: Accepting or Declining a Request to Join a Private Group

This sample code calls `ConnectApi.ChatterGroups.updateRequestStatus` and passes it the membership request ID
and an `ConnectApi.GroupMembershipRequestStatus.Accepted` status. You can also pass
`ConnectApi.GroupMembershipRequestStatus.Declined` .

```
   String communityId = null;

   ID groupId = '0F9x00000000hAZ';

   String requestId = '0I5x000000001snCAA';

   ConnectApi.GroupMembershipRequest membershipRequestRep =

   ConnectApi.ChatterGroups.updateRequestStatus(communityId, requestId,

   ConnectApi.GroupMembershipRequestStatus.Accepted);

##### **`updateRequestStatus(communityId, requestId, status, responseMessage)`**

```

Update a request to join a private group and optionally provide a message when the request is denied.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.GroupMembershipRequest updateRequestStatus(String communityId,

   String requestId, ConnectApi.GroupMembershipRequestStatus status, String responseMessage)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterGroups Class

```
   requestId
```

Type: String

ID for a request to join a private group.

```
   status
```

Type: `ConnectApi.GroupMembershipRequestStatus`

Status of the request:

**•** `Accepted`

**•** `Declined`

The `Pending` value of the enum is not valid in this method.

```
   responseMessage
```

Type: String

Provide a message to the user if their membership request is declined. The value of this property is used only when the value of the
`status` property is `Declined` .

The maximum length is 756 characters.

Return Value

Type: `ConnectApi.GroupMembershipRequest`

Usage

This method is successful only when the context user is the group manager or owner, or has Modify All Data permission.

#### ChatterGroups Test Methods These test methods are for ChatterGroups . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchGroups(communityId, q, result)`**

Register a `ConnectApi.ChatterGroupPage` object to be returned when the matching `ConnectApi.searchGroups`
method is called in a test context. Use the test method with the same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestSearchGroups(String communityId, String q,

   ConnectApi.ChatterGroupPage result)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterGroups Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

```
   result
```

Type: `ConnectApi.ChatterGroupPage`

Test `ConnectApi.ChatterGroupPage` object.

Return Value

Type: Void

SEE ALSO:

searchGroups(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchGroups(communityId, q, pageParam, pageSize, result)`**

Register a `ConnectApi.ChatterGroupPage` object to be returned when the matching `ConnectApi.searchGroups`
method is called in a test context. Use the test method with the same parameters or you receive an exception.

API Version

28.0

Signature

```
   public static Void setTestSearchGroups(String communityId, String q, Integer pageParam,

   Integer pageSize, ConnectApi.ChatterGroupPage result)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterGroups Class

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   result
```

Type: `ConnectApi.ChatterGroupPage`

Test `ConnectApi.ChatterGroupPage` object.

Return Value

Type: Void

SEE ALSO:

searchGroups(communityId, q, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchGroups(communityId, q, archiveStatus, pageParam, pageSize,`**

```
  result)

```

Register a `ConnectApi.ChatterGroupPage` object to be returned when the matching `ConnectApi.searchGroups`
method is called in a test context. Use the test method with the same parameters or you receive an exception.

API Version

29.0

Signature

```
   public static Void setTestSearchGroups(String communityId, String q,

   ConnectApi.GroupArchiveStatus, archiveStatus, Integer pageParam, Integer pageSize,

   ConnectApi.ChatterGroupPage result)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

```
   archiveStatus
```

Type: `ConnectApi.GroupArchiveStatus`

Archive status of groups.

**•** `All` —All groups, including groups that are archived and groups that aren’t archived.

**•** `Archived` —Groups that are archived.

**•** `NotArchived` —Groups that aren’t archived.


### Apex Reference Guide ChatterMessages Class

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

Type: `ConnectApi.ChatterGroupPage`

Test `ConnectApi.ChatterGroupPage` object.

Return Value

Type: Void

SEE ALSO:

searchGroups(communityId, q, archiveStatus, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ChatterMessages Class

Get, send, search, and reply to private messages. You can also get and search private conversations, mark conversations as read, and get
a count of unread private messages.

Namespace

ConnectApi

Usage

Private messages and direct messages are different features. Direct messages are newer and offer a richer feature set for private
communication in Experience Cloud sites. Direct messages are a capability within Chatter feeds. To work with direct messages, use the
ChatterFeeds Class.

#### ChatterMessages Methods

### These methods are for ChatterMessages . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

getConversation(conversationId)
Get a conversation.

getConversation(conversationId, pageParam, pageSize)
Get a page of a conversation.


Apex Reference Guide ChatterMessages Class

getConversation(communityId, conversationId)
Get a conversation from an Experience Cloud site.

getConversation(communityId, conversationId, pageParam, pageSize)
Get a page of a conversation from an Experience Cloud site.

getConversations()
Get the most recent conversations.

getConversations(pageParam, pageSize)
Get a page of conversations.

getConversations(communityId)
Get the most recent conversations from an Experience Cloud site.

getConversations(communityId, pageParam, pageSize)
Get a page of conversations from an Experience Cloud site.

getMessage(messageId)
Get a message.

getMessage(communityId, messageId)
Get a message from an Experience Cloud site.

getMessages()
Get the most recent messages.

getMessages(pageParam, pageSize)
Get a page of messages.

getMessages(communityId)
Get the most recent messages from an Experience Cloud site.

getMessages(communityId, pageParam, pageSize)
Get a page of messages from an Experience Cloud site.

getUnreadCount()
Get the number of conversations that are marked unread.

getUnreadCount(communityId)
Get the number of conversations that are marked unread in an Experience Cloud site.

markConversationRead(conversationId, read)
Mark a conversation as read or unread.

markConversationRead(communityId, conversationID, read)
Mark a conversation as read or unread in an Experience Cloud site.

replyToMessage(text, inReplyTo)
Reply to a message.

replyToMessage(communityId, text, inReplyTo)
Reply to a message in an Experience Cloud site.

searchConversation(conversationId, q)
Get a conversation that matches the search criteria.

searchConversation(conversationId, pageParam, pageSize, q)
Get a conversation with a page of messages that match the search criteria.


Apex Reference Guide ChatterMessages Class

searchConversation(communityId, conversationId, q)
Get a conversation with messages that match the search criteria in an Experience Cloud site.

searchConversation(communityId, conversationId, pageParam, pageSize, q)
Get a conversation with a page of messages that match the search criteria in an Experience Cloud site.

searchConversations(q)
Get conversations in which member names and messages match the search criteria.

searchConversations(pageParam, pageSize, q)
Get a page of conversations in which member names and messages match the search criteria.

searchConversations(communityId, q)
Get conversations in which member names and messages match the search criteria in an Experience Cloud site.

searchConversations(communityId, pageParam, pageSize, q)
Get a page of conversations in which member names and messages match the search criteria in an Experience Cloud site.

searchMessages(q)
Get messages that match the search criteria.

searchMessages(pageParam, pageSize, q)
Get a page of messages that match the search criteria.

searchMessages(communityId, q)
Get messages that match the search criteria in an Experience Cloud site.

searchMessages(communityId, pageParam, pageSize, q)
Get a page of messages that match the search criteria in an Experience Cloud site.

sendMessage(text, recipients)
Send a message to a list of recipients.

sendMessage(communityId, text, recipients)
Send a message to a list of recipients in an Experience Cloud site.

##### **`getConversation(conversationId)`**

Get a conversation.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation getConversation(String conversationId)

```

Parameters

```
   conversationId
```

Type: String


Apex Reference Guide ChatterMessages Class

ID for the conversation.

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`getConversation(conversationId, pageParam, pageSize)`**

Get a page of a conversation.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation getConversation(String conversationId,

   String pageParam, Integer pageSize)

```

Parameters

```
   conversationId
```

Type: String

ID for the conversation.

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

Type: `ConnectApi.ChatterConversation`

##### **`getConversation(communityId, conversationId)`**

Get a conversation from an Experience Cloud site.

API Version

30.0


Apex Reference Guide ChatterMessages Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation getConversation(String communityId, String

   conversationId)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   conversationId
```

Type: String

ID for the conversation.

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`getConversation(communityId, conversationId, pageParam, pageSize)`**

Get a page of a conversation from an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation getConversation(String communityId, String

   conversationId, String pageParam, String pageSize)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   conversationId
```

Type: String

ID for the conversation.

```
   pageParam
```

Type:String


Apex Reference Guide ChatterMessages Class

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`getConversations()`**

Get the most recent conversations.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage getConversations()

```

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`getConversations(pageParam, pageSize)`**

Get a page of conversations.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage getConversations(String pageParam,

   Integer pageSize)

```


Apex Reference Guide ChatterMessages Class

Parameters

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

Type: `ConnectApi.ChatterConversationPage`

##### **`getConversations(communityId)`**

Get the most recent conversations from an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage getConversations(String communityId)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`getConversations(communityId, pageParam, pageSize)`**

Get a page of conversations from an Experience Cloud site.

API Version

30.0


Apex Reference Guide ChatterMessages Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage getConversations(String communityId,

   String pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   pageParam
```

Type:String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`getMessage(messageId)`**

Get a message.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage getMessage(String messageId)

```

Parameters

```
   messageId
```

Type: String

ID for the message.


Apex Reference Guide ChatterMessages Class

Return Value

Type: `ConnectApi.ChatterMessage`

##### **`getMessage(communityId, messageId)`**

Get a message from an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage getMessage(String communityId, String messageId)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   messageId
```

Type: String

ID for the message.

Return Value

Type: `ConnectApi.ChatterMessage`

##### **`getMessages()`**

Get the most recent messages.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage getMessages()

```


Apex Reference Guide ChatterMessages Class

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`getMessages(pageParam, pageSize)`**

Get a page of messages.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage getMessages(String pageParam, Integer

   pageSize)

```

Parameters

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

Type: `ConnectApi.ChatterMessagePage`

##### **`getMessages(communityId)`**

Get the most recent messages from an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage getMessages(String communityId)

```


Apex Reference Guide ChatterMessages Class

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`getMessages(communityId, pageParam, pageSize)`**

Get a page of messages from an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage getMessages(String communityId, String

   pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

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

Type: `ConnectApi.ChatterMessagePage`

##### **`getUnreadCount()`**

Get the number of conversations that are marked unread.


Apex Reference Guide ChatterMessages Class

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UnreadConversationCount getUnreadCount()

```

Return Value

Type: `ConnectApi.UnreadConversationCount`

If there are fewer than 50 unread conversations, `ConnectApi.UreadConversationCount` returns the exact number of unread
conversations and the `hasMore` property is `false` . If there are more than 50 unread conversations,
`ConnectApi.UreadConversationCount` returns 50 unread conversations and the `hasMore` property is `true` .

Example

```
   ConnectApi.UnreadConversationCount unread = ConnectApi.ChatterMessages.getUnreadCount();

##### **`getUnreadCount(communityId)`**

```

Get the number of conversations that are marked unread in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UnreadConversationCount getUnreadCount(String communityId)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.UnreadConversationCount`


Apex Reference Guide ChatterMessages Class

If there are fewer than 50 unread conversations, `ConnectApi.UreadConversationCount` returns the exact number of unread
conversations and the `hasMore` property is `false` . If there are more than 50 unread conversations,
`ConnectApi.UreadConversationCount` returns 50 unread conversations and the `hasMore` property is `true` .

##### **`markConversationRead(conversationId, read)`**

Mark a conversation as read or unread.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationSummary markConversationRead(String

   conversationId, Boolean read)

```

Parameters

```
   conversationId
```

Type: String

ID for the conversation.

```
   read
```

Type: Boolean

Specify whether the conversation is read ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.ChatterConversationSummary`

##### **`markConversationRead(communityId, conversationID, read)`**

Mark a conversation as read or unread in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationSummary markConversationRead(String

   communityId, String conversationID, Boolean read)

```


Apex Reference Guide ChatterMessages Class

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   conversationId
```

Type: String

ID for the conversation.

```
   read
```

Type: Boolean

Specify whether the conversation is read ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.ChatterConversationSummary`

##### **`replyToMessage(text, inReplyTo)`**

Reply to a message.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage replyToMessage(String text, String inReplyTo)

```

Parameters

```
   text
```

Type: String

Text of the message. Can’t be empty or over 10,000 characters.

```
   inReplyTo
```

Type: String

ID of the message that is being responded to.

Return Value

Type: `ConnectApi.ChatterMessage`

##### **`replyToMessage(communityId, text, inReplyTo)`**

Reply to a message in an Experience Cloud site.


Apex Reference Guide ChatterMessages Class

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage replyToMessage(String communityId, String text,

   String inReplyTo)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

Text of the message. Can’t be empty or over 10,000 characters.

```
   inReplyTo
```

Type: String

ID of the message that is being responded to.

Return Value

Type: `ConnectApi.ChatterMessage`

##### **`searchConversation(conversationId, q)`**

Get a conversation that matches the search criteria.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation searchConversation(String conversationId,

   String q)

```


Apex Reference Guide ChatterMessages Class

Parameters

```
   conversationId
```

Type: String

ID for the conversation.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`searchConversation(conversationId, pageParam, pageSize, q)`**

Get a conversation with a page of messages that match the search criteria.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation searchConversation(String conversationId,

   String pageParam, Integer pageSize, String q)

```

Parameters

```
   conversationId
```

Type: String

ID for the conversation.

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide ChatterMessages Class

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`searchConversation(communityId, conversationId, q)`**

Get a conversation with messages that match the search criteria in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversation searchConversation(String communityId,

   String conversationId, String q)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   conversationId
```

Type: String

ID for the conversation.

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`searchConversation(communityId, conversationId, pageParam, pageSize, q)`**

Get a conversation with a page of messages that match the search criteria in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes


Apex Reference Guide ChatterMessages Class

Signature

```
   public static ConnectApi.ChatterConversation searchConversation(String communityId,

   String conversationId, String pageParam, Integer pageSize, String q)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   conversationId
```

Type: String

ID for the conversation.

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversation`

##### **`searchConversations(q)`**

Get conversations in which member names and messages match the search criteria.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage searchConversations(String q)

```


Apex Reference Guide ChatterMessages Class

Parameters

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`searchConversations(pageParam, pageSize, q)`**

Get a page of conversations in which member names and messages match the search criteria.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage searchConversations(String pageParam,

   Integer pageSize, String q)

```

Parameters

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`searchConversations(communityId, q)`**

Get conversations in which member names and messages match the search criteria in an Experience Cloud site.


Apex Reference Guide ChatterMessages Class

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage searchConversations(String communityId,

   String q)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`searchConversations(communityId, pageParam, pageSize, q)`**

Get a page of conversations in which member names and messages match the search criteria in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterConversationPage searchConversations(String communityId,

   String pageParam, Integer pageSize, String q)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterMessages Class

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterConversationPage`

##### **`searchMessages(q)`**

Get messages that match the search criteria.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage searchMessages(String q)

```

Parameters

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`searchMessages(pageParam, pageSize, q)`**

Get a page of messages that match the search criteria.


Apex Reference Guide ChatterMessages Class

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage searchMessages(String pageParam, Integer

   pageSize, String q)

```

Parameters

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`searchMessages(communityId, q)`**

Get messages that match the search criteria in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage searchMessages(String communityId, String

   q)

```


Apex Reference Guide ChatterMessages Class

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`searchMessages(communityId, pageParam, pageSize, q)`**

Get a page of messages that match the search criteria in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessagePage searchMessages(String communityId, String

   pageParam, Integer pageSize, String q)

```

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

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

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide ChatterMessages Class

Return Value

Type: `ConnectApi.ChatterMessagePage`

##### **`sendMessage(text, recipients)`**

Send a message to a list of recipients.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage sendMessage(String text, String recipients)

```

Parameters

```
   text
```

Type: String

Text of the message. Can’t be empty or over 10,000 characters.

```
   recipients
```

Type: String

Up to nine comma-separated IDs of the users receiving the message.

Return Value

Type: `ConnectApi.ChatterMessage`

##### **`sendMessage(communityId, text, recipients)`**

Send a message to a list of recipients in an Experience Cloud site.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterMessage sendMessage(String communityId, String text,

   String recipients)

```


### Apex Reference Guide ChatterUsers Class

Parameters

```
   communityId
```

Type:String

ID for an Experience Cloud site, `internal`, or `null` .

```
   text
```

Type: String

Text of the message. Can’t be empty or over 10,000 characters.

```
   recipients
```

Type: String

Up to nine comma-separated IDs of users to receive the message.

Return Value

Type: `ConnectApi.ChatterMessage`

### ChatterUsers Class

Access information about users, such as activity, followers, subscriptions, files, and groups.

Namespace

ConnectApi

#### ChatterUsers Methods

### These methods are for ChatterUsers . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

exportUserActivities(communityId, userId)
Export Chatter-related user activity, such as bookmarks, topic endorsements, and votes.

follow(communityId, userId, subjectId)
Follow a user or record.

getChatterSettings(communityId, userId)
Get the default Chatter settings for a user.

getFollowers(communityId, userId)
Get the first page of followers for a user.

getFollowers(communityId, userId, pageParam, pageSize)
Get a page of followers for a user.

getFollowings(communityId, userId)
Get the first page of users and records that a user follows.

getFollowings(communityId, userId, pageParam)
Get a page of users and records that a user follows.


Apex Reference Guide ChatterUsers Class

getFollowings(communityId, userId, pageParam, pageSize)
Get a page with the specified number of users and records that a user follows.

getFollowings(communityId, userId, filterType)
Get the first page of records, filtered by key prefix, that a user follows.

getFollowings(communityId, userId, filterType, pageParam)
Get a page of records, filtered by key prefix, that a user follows.

getFollowings(communityId, userId, filterType, pageParam, pageSize)
Get a page with the specified number of records, filtered by key prefix, that a user follows.

getReputation(communityId, userId)
Get a user’s reputation.

getUser(communityId, userId)
Get information about a user.

getUserBatch(communityId, userIds)
Get information about a list of users.

getUserGroups(communityId, userId)
Get a user’s groups.

getUserGroups(communityId, userId, pageParam, pageSize)
Get a page of a user’s groups.

getUsers(communityId)
Get the first page of users.

getUsers(communityId, pageParam, pageSize)
Get a page of users.

purgeUserActivities(communityId, userId)
Start a job to purge Chatter-related user activity, such as bookmarks, topic endorsements, and votes.

searchUserGroupDetails(communityId, userId, q)
Get the user’s groups that match the search criteria.

searchUserGroupDetails(communityId, userId, q, pageParam, pageSize)
Get a page of a user’s groups that match the search criteria.

searchUsers(communityId, q)
Get the first page of users that match the search criteria.

searchUsers(communityId, q, pageParam, pageSize)
Get a page of users that match the search criteria.

searchUsers(communityId, q, searchContextId, pageParam, pageSize)
Get a page of users that match the search criteria.

updateChatterSettings(communityId, userId, defaultGroupEmailFrequency)
Update the default Chatter settings for a user.

updateUser(communityId, userId, userInput)
Update the About Me section for a user.


Apex Reference Guide ChatterUsers Class

##### **`exportUserActivities(communityId, userId)`**

Export Chatter-related user activity, such as bookmarks, topic endorsements, and votes.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserActivitiesJob exportUserActivities(String communityId,

   String userId)

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

Type: `ConnectApi.UserActivitiesJob`

Usage

The following activities can be exported.

**•** `Bookmark` —User bookmarked a post.

**•** `ChatterActivity` —Total counts of posts and comments made and likes and comments received for a user.

**•** `ChatterLike` —User liked a post or comment.

**•** `Comment` —User commented on a post.

**•** `CompanyVerify` —User verified comment.

**•** `DownVote` —User downvoted a post or comment.

**•** `FeedEntityRead` —User read a post.

**•** `FeedRead` —User read a feed.

**•** `Mute` —User muted a post.

**•** `Post` —User made a post.

**•** `TopicEndorsement` —User endorsed another user on a topic or received endorsement on a topic.

**•** `UpVote` —User upvoted a post or comment.


Apex Reference Guide ChatterUsers Class

##### **`follow(communityId, userId, subjectId)`**

Follow a user or record.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Subscription follow(String communityId, String userId, String

   subjectId)

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
   subjectId
```

Type: String

ID of the user or record to follow.

Return Value

Type: `ConnectApi.Subscription`

Example

```
   ChatterUsers.ConnectApi.Subscription subscriptionToRecord =

   ConnectApi.ChatterUsers.follow(null, 'me', '001RR000002G4Y0');

```

Usage

[This method creates an EntitySubscription record, which requires certain permissions. See the Usage section of the EntitySubscription](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_entitysubscription.htm)
object for more information.

SEE ALSO:

[Unfollow a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_unfollow_record.htm)


Apex Reference Guide ChatterUsers Class

##### **`getChatterSettings(communityId, userId)`**

Get the default Chatter settings for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserChatterSettings getChatterSettings(String communityId,

   String userId)

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

Type: `ConnectApi.UserChatterSettings`

##### **`getFollowers(communityId, userId)`**

Get the first page of followers for a user.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowerPage getFollowers(String communityId, String userId)

```


Apex Reference Guide ChatterUsers Class

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

Type: `ConnectApi.FollowerPage`

##### **`getFollowers(communityId, userId, pageParam, pageSize)`**

Get a page of followers for a user.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowerPage getFollowers(String communityId, String userId,

   Integer pageParam, Integer pageSize)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterUsers Class

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.FollowerPage`

##### **`getFollowings(communityId, userId)`**

Get the first page of users and records that a user follows.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId)

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

Type: `ConnectApi.FollowingPage`

##### **`getFollowings(communityId, userId, pageParam)`**

Get a page of users and records that a user follows.

API Version

28.0

Available to Guest Users

32.0


Apex Reference Guide ChatterUsers Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId,

   Integer pageParam)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

Return Value

Type: `ConnectApi.FollowingPage`

##### **`getFollowings(communityId, userId, pageParam, pageSize)`**

Get a page with the specified number of users and records that a user follows.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId,

   Integer pageParam, Integer pageSize)

```


Apex Reference Guide ChatterUsers Class

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

Type: `ConnectApi.FollowingPage`

##### **`getFollowings(communityId, userId, filterType)`**

Get the first page of records, filtered by key prefix, that a user follows.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId,

   String filterType)

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


Apex Reference Guide ChatterUsers Class

ID for a user.

```
   filterType
```

Type: String

Specifies the key prefix to filter the type of objects returned. A key prefix is the first three characters of the object ID, which specifies
the object type. For example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

Return Value

Type: `ConnectApi.FollowingPage`

##### **`getFollowings(communityId, userId, filterType, pageParam)`**

Get a page of records, filtered by key prefix, that a user follows.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId,

   String filterType, Integer pageParam)

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
   filterType
```

Type: String

Specifies the key prefix to filter the type of objects returned. A key prefix is the first three characters of the object ID, which specifies
the object type. For example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.


Apex Reference Guide ChatterUsers Class

Return Value

Type: `ConnectApi.FollowingPage`

##### **`getFollowings(communityId, userId, filterType, pageParam, pageSize)`**

Get a page with the specified number of records, filtered by key prefix, that a user follows.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FollowingPage getFollowings(String communityId, String userId,

   String filterType, Integer pageParam, Integer pageSize)

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
   filterType
```

Type: String

Specifies the key prefix to filter the type of objects returned. A key prefix is the first three characters of the object ID, which specifies
the object type. For example, User objects have a prefix of 005 and Group objects have a prefix of 0F9.

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

Type: `ConnectApi.FollowingPage`


Apex Reference Guide ChatterUsers Class

##### **`getReputation(communityId, userId)`**

Get a user’s reputation.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Reputation getReputation(String communityId, String userId)

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

Type: `ConnectApi.Reputation`

##### **`getUser(communityId, userId)`**

Get information about a user.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes


Apex Reference Guide ChatterUsers Class

Signature

```
   public static ConnectApi.UserSummary getUser(String communityId, String userId)

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

Type: `ConnectApi.UserDetail`

Usage

If the user is external, the properties that the `ConnectApi.UserDetail` output class shares with the
`ConnectApi.UserSummary` output class can have non-null values. Other properties are always `null` .

##### **`getUserBatch(communityId, userIds)`**

Get information about a list of users.

API Version

31.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getUserBatch(String communityId, List<String>

   userIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterUsers Class

```
   userIds
```

Type: List<String>

A list of up to 500 user IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.User` object and errors for users that
didn’t load.

Example

```
   // Get users in an organization.

   ConnectApi.UserPage userPage = ConnectApi.ChatterUsers.getUsers(null);

   // Create a list of user IDs.

   List<String> userList = new List<String>();

   for (ConnectApi.User user : userPage.users){

      userList.add(user.id);

   }

   // Get info about all users in the list.

   ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterUsers.getUserBatch(null, userList);

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

        // Operation was successful.

        // Print each user's username.

        ConnectApi.UserDetail user;

        if(batchResult.getResult() instanceof ConnectApi.UserDetail) {

           user = (ConnectApi.UserDetail) batchResult.getResult();

        }

        System.debug('SUCCESS');

        System.debug(user.username);

      }

      else {

        // Operation failed. Print errors.

        System.debug('FAILURE');

        System.debug(batchResult.getErrorMessage());

      }

   }

##### **`getUserGroups(communityId, userId)`**

```

Get a user’s groups.

API Version

45.0


Apex Reference Guide ChatterUsers Class

Available to Guest Users

45.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupDetailPage getUserGroups(String communityId, String

   userId)

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

Type: `ConnectApi.UserGroupDetailPage`

##### **`getUserGroups(communityId, userId, pageParam, pageSize)`**

Get a page of a user’s groups.

API Version

45.0

Available to Guest Users

45.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupDetailPage getUserGroups(String communityId, String

   userId, Integer pageParam, Integer pageSize)

```


Apex Reference Guide ChatterUsers Class

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

Type: `ConnectApi.UserGroupDetailPage`

##### **`getUsers(communityId)`**

Get the first page of users.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserPage getUsers(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.UserPage`


Apex Reference Guide ChatterUsers Class

##### **`getUsers(communityId, pageParam, pageSize)`**

Get a page of users.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserPage getUsers(String communityId, Integer pageParam,

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

Type: `ConnectApi.UserPage`

##### **`purgeUserActivities(communityId, userId)`**

Start a job to purge Chatter-related user activity, such as bookmarks, topic endorsements, and votes.

API Version

42.0

Requires Chatter

Yes


Apex Reference Guide ChatterUsers Class

Signature

```
   public static ConnectApi.UserActivitiesJob purgeUserActivities(String communityId,

   String userId)

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

Type: `ConnectApi.UserActivitiesJob`

Usage

The following activities can be purged with this method.

**•** `Bookmark` —User bookmarked a post.

**•** `ChatterActivity` —Total counts of posts and comments made and likes and comments received for a user.

**•** `ChatterLike` —User liked a post or comment.

**•** `CompanyVerify` —User verified comment.

**•** `DownVote` —User downvoted a post or comment.

**•** `FeedEntityRead` —User read a post.

**•** `FeedRead` —User read a feed.

**•** `Mute` —User muted a post.

**•** `TopicEndorsement` —User endorsed another user on a topic or received endorsement on a topic.

**•** `UpVote` —User upvoted a post or comment.

To delete a user’s posts and comments, use these methods, respectively.

**•** `deleteFeedElement(communityId, feedElementId)`

**•** `deleteComment(communityId, commentId)`

##### **`searchUserGroupDetails(communityId, userId, q)`**

Get the user’s groups that match the search criteria.

API Version

45.0

Available to Guest Users

45.0


Apex Reference Guide ChatterUsers Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupDetailPage searchUserGroupDetails(String communityId,

   String userId, String q)

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
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.UserGroupDetailPage`

##### **`searchUserGroupDetails(communityId, userId, q, pageParam, pageSize)`**

Get a page of a user’s groups that match the search criteria.

API Version

45.0

Available to Guest Users

45.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupDetailPage searchUserGroupDetails(String communityId,

   String userId, String q, Integer pageParam, Integer pageSize)

```


Apex Reference Guide ChatterUsers Class

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
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

Type: `ConnectApi.UserGroupDetailPage`

##### **`searchUsers(communityId, q)`**

Get the first page of users that match the search criteria.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserPage searchUsers(String communityId, String q)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterUsers Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.UserPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchUsers(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchUsers(communityId, q, pageParam, pageSize)`**

Get a page of users that match the search criteria.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserPage searchUsers(String communityId, String q, Integer

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


Apex Reference Guide ChatterUsers Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

Type: `ConnectApi.UserPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchUsers(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchUsers(communityId, q, searchContextId, pageParam, pageSize)`**

Get a page of users that match the search criteria.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserPage searchUsers(String communityId, String q, String

   searchContextId, Integer pageParam, Integer pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterUsers Class

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   searchContextId
```

Type: String

A feed item ID that filters search results for feed @mentions. More useful results are listed first. When you specify this argument, you
cannot query more than 500 results and you cannot use wildcards in the search term.

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

Type: `ConnectApi.UserPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchUsers(communityId, q, searchContextId, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`updateChatterSettings(communityId, userId, defaultGroupEmailFrequency)`**

Update the default Chatter settings for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserChatterSettings updateChatterSettings(String communityId,

   String userId, ConnectApi.GroupEmailFrequency defaultGroupEmailFrequency)

```


Apex Reference Guide ChatterUsers Class

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
   defaultGroupEmailFrequency
```

Type: `ConnectApi.GroupEmailFrequency`

Frequency with which a user receives email. Values are:

**•** `EachPost`

**•** `DailyDigest`

**•** `WeeklyDigest`

**•** `Never`

**•** `UseDefault`

Don’t pass the value `UseDefault` for the _`defaultGroupEmailFrequency`_ parameter because calling
`updateChatterSettings` sets the default value.

Return Value

Type: `ConnectApi.UserChatterSettings`

##### **`updateUser(communityId, userId, userInput)`**

Update the About Me section for a user.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserDetail updateUser(String communityId, String userId,

   ConnectApi.UserInput userInput)

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


Apex Reference Guide ChatterUsers Class

ID for the context user or the keyword `me` .

```
   userInput
```

Type: `ConnectApi.UserInput`

Specifies the updated information.

Return Value

Type: `ConnectApi.UserDetail`

#### ChatterUsers Test Methods These test methods are for ChatterUsers . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

IN THIS SECTION:

##### setTestSearchUsers(communityId, q, result)

Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is
called in a test context. Use the method with the same parameters or you receive an exception.

setTestSearchUsers(communityId, q, pageParam, pageSize, result)
Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is
called in a test context. Use the method with the same parameters or you receive an exception.

setTestSearchUsers(communityId, q, searchContextId, pageParam, pageSize, result)
Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is
called in a test context. Use the method with the same parameters or you receive an exception.

##### **`setTestSearchUsers(communityId, q, result)`**

Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is called
in a test context. Use the method with the same parameters or you receive an exception.

API Version

28.0

Signature

```
   public static Void setTestSearchUsers(String communityId, String q, ConnectApi.UserPage

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


Apex Reference Guide ChatterUsers Class

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.UserPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchUsers(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchUsers(communityId, q, pageParam, pageSize, result)`**

Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is called
in a test context. Use the method with the same parameters or you receive an exception.

API Version

28.0

Signature

```
   public static Void setTestSearchUsers(String communityId, String q, Integer pageParam,

   Integer pageSize, ConnectApi.UserPage result)

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

Type: `ConnectApi.UserPage`


Apex Reference Guide ChatterUsers Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchUsers(communityId, q, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchUsers(communityId, q, searchContextId, pageParam, pageSize,`**

```
  result)

```

Register a `ConnectApi.UserPage` object to be returned when the matching `ConnectApi.searchUsers` method is called
in a test context. Use the method with the same parameters or you receive an exception.

API Version

28.0

Signature

```
   public static Void setTestSearchUsers(String communityId, String q, String

   searchContextId, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)

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
   searchContextId
```

Type: String

A feed item ID that filters search results for feed @mentions. More useful results are listed first. When you specify this argument, you
cannot query more than 500 results and you cannot use wildcards in the search term.

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


Apex Reference Guide ChatterUsers Class

```
   result
```

Type: `ConnectApi.UserPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchUsers(communityId, q, searchContextId, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### Retired ChatterUsers Methods

These methods for `ChatterUsers` are retired.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

##### deletePhoto(communityId, userId)

Delete a user’s photo.

getGroups(communityId, userId)
Get the groups that a user is a member of.

getGroups(communityId, userId, pageParam, pageSize)
Get a page of groups that a user is a member of.

getPhoto(communityId, userId)
Get a user’s photo.

searchUserGroups(communityId, userId, q)
Get the user’s groups that match the search criteria.

searchUserGroups(communityId, userId, q, pageParam, pageSize)
Get a page of a user’s groups that match the search criteria.

setPhoto(communityId, userId, fileId, versionNumber)
Set an uploaded file as a user’s photo.

setPhoto(communityId, userId, fileUpload)
Set a file that hasn’t been uploaded as the user’s photo.

setPhotoWithAttributes(communityId, userId, photo)
Set and crop an uploaded file as a user’s photo.

setPhotoWithAttributes(communityId, userId, photo, fileUpload)
Set and crop a file that hasn’t been uploaded as a user’s photo.

##### **`deletePhoto(communityId, userId)`**

Delete a user’s photo.


Apex Reference Guide ChatterUsers Class

API Version

28.0–34.0

Important: In version 35.0 and later, use `ConnectApi.UserProfiles.deletePhoto(communityId, userId)`

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

##### **`getGroups(communityId, userId)`**

Get the groups that a user is a member of.

API Version

28.0–44.0

Important: In version 45.0 and later, use `getUserGroups(communityId, userId)` .

Available to Guest Users

32.0–44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupPage getGroups(String communityId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterUsers Class

```
   userId
```

Type: String

ID for a user.

Return Value

Type: `ConnectApi.UserGroupPage`

##### **`getGroups(communityId, userId, pageParam, pageSize)`**

Get a page of groups that a user is a member of.

API Version

28.0–44.0

Important: In version 45.0 and later, use `getUserGroups(communityId, userId, pageParam, pageSize)` .

Available to Guest Users

32.0–44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupPage getGroups(String communityId, String userId,

   Integer pageParam, Integer pageSize)

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
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterUsers Class

Return Value

Type: `ConnectApi.UserGroupPage`

##### **`getPhoto(communityId, userId)`**

Get a user’s photo.

API Version

28.0–34.0

Important: In version 35.0 and later, use `ConnectApi.UserProfiles.getPhoto(communityId, userId)` .

Available to Guest Users

32.0

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

##### **`searchUserGroups(communityId, userId, q)`**

Get the user’s groups that match the search criteria.

API Version

30.0–44.0

Important: In version 45.0 and later, use `searchUserGroupDetails(communityId, userId, q)` .


Apex Reference Guide ChatterUsers Class

Available to Guest Users

32.0–44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UserGroupPage searchUserGroups(String communityId, String

   userId, String q)

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
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.UserGroupPage`

##### **`searchUserGroups(communityId, userId, q, pageParam, pageSize)`**

Get a page of a user’s groups that match the search criteria.

API Version

30.0–44.0

Important: In version 45.0 and later, use `searchUserGroupDetails(communityId, userId, q, pageParam,`
`pageSize)` .

Available to Guest Users

32.0–44.0

Requires Chatter

Yes


Apex Reference Guide ChatterUsers Class

Signature

```
   public static ConnectApi.UserGroupPage searchUserGroups(String communityId, String

   userId, String q, Integer pageParam, Integer pageSize)

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
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

Type: `ConnectApi.UserGroupPage`

##### **`setPhoto(communityId, userId, fileId, versionNumber)`**

Set an uploaded file as a user’s photo.

API Version

28.0–34.0

Important: In version 35.0 and later, use `ConnectApi.UserProfiles.setPhoto(communityId, userId,`

```
     fileId, versionNumber)

```

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Photo setPhoto(String communityId, String userId, String

   fileId, Integer versionNumber)

```


Apex Reference Guide ChatterUsers Class

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

ID of a file already uploaded. The file must be an image, and be smaller than 2 GB.

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

Set a file that hasn’t been uploaded as the user’s photo.

API Version

28.0–34.0

Important: In version 35.0 and later, use `ConnectApi.UserProfiles.setPhoto(communityId, userId,`

```
     fileUpload)

```

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


Apex Reference Guide ChatterUsers Class

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

API Version

29.0–34.0

Important: In version 35.0 and later, use

```
     ConnectApi.UserProfiles.setPhotoWithAttributes(communityId, userId, photo)

```

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


Apex Reference Guide ChatterUsers Class

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(communityId, userId, photo, fileUpload)`**

Set and crop a file that hasn’t been uploaded as a user’s photo.

API Version

29.0–34.0

Important: In version 35.0 and later, use

```
     ConnectApi.UserProfiles.setPhotoWithAttributes(communityId, userId, photo,

     fileUpload)

```

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


### Apex Reference Guide Clm Class

Usage

Photos are processed asynchronously and might not be visible right away.

### Clm Class

Create and update Contract Lifecycle Management (CLM) contracts using object ID.

Namespace

ConnectApi

#### Clm Methods

### These methods are for Clm . All methods are static.

IN THIS SECTION:

##### createContract(contractInputPayload)

Create contracts using the object ID.

updateContract(contractInputPayload)
Update contracts using the object ID.

##### **`createContract(contractInputPayload)`**

Create contracts using the object ID.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContractOutputRepresentation

   createContract(ConnectApi.ContractInputRepresentation contractInputPayload)

```

Parameters

```
   contractInputPayload
```

Type: `ConnectApi.ContractInputRepresentation on page 2027`

Input payload to create contract.

Return Value

Type: `ConnectApi.ContractOutputRepresentation on page 2281`


### Apex Reference Guide CommerceBuyerExperience Class

##### **`updateContract(contractInputPayload)`**

Update contracts using the object ID.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContractOutputRepresentation

   updateContract(ConnectApi.ContractInputRepresentation contractInputPayload)

```

Parameters

```
   contractInputPayload
```

Type: `ConnectApi.ContractInputRepresentation on page 2027`

Input payload to update contract.

Return Value

Type: `ConnectApi.ContractOutputRepresentation on page 2281`

### CommerceBuyerExperience Class

Create, delete, or get commerce addresses. Get order delivery group, order item, order shipments, shipment items, and order summaries.
Get adjustments for order items and order summaries.

Namespace

ConnectApi

#### CommerceBuyerExperience Methods

### These methods are for CommerceBuyerExperience . All methods are static.

IN THIS SECTION:

addOrderToCart(webstoreId, orderSummaryId, orderToCartInput)
Add an order to a cart using a webstore order summary.

addOrderToCart(webstoreId, orderSummaryId, orderToCartInput, effectiveAccountId)
Add an order to a cart for a specific account using a webstore order summary.

calculateAdjustmentAggregates(webstoreId, orderSummaryIds)
Submit a job to calculate adjustment aggregates for a list of order summary IDs.


Apex Reference Guide CommerceBuyerExperience Class

createCommerceAccountAddress(webstoreId, accountId, addressInput)
Create a Commerce account address for a webstore account.

deleteCommerceAccountAddress(webstoreId, accountId, addressId)
Delete a Commerce account address for a webstore.

getCommerceAccountAddress(webstoreId, accountId)
Get a Commerce account address for a webstore.

getCommerceAccountAddress(webstoreId, accountId, defaultOnly)
Get Commerce account addresses for a webstore and account.

getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType, fields, pageToken, pageSize, sortOrder)
Get Commerce account addresses for a webstore and account.

getCommerceAccountAddress(webstoreId, accountId, addressType, excludeUnsupportedCountries)
Get Commerce account addresses for a webstore and account.

getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType, excludeUnsupportedCountries)
Get Commerce account addresses for a webstore and account.

getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType, excludeUnsupportedCountries, fields, pageToken,
pageSize, sortOrder)
Get Commerce account addresses for a webstore and account.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId)
Get order delivery group summaries.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, pageSize)
Get order delivery group summaries.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, pageParam)
Get a page of order delivery group summaries.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, fields)
Get order delivery group summaries with specific fields.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, pageParam, fields)
Get a page of order delivery group summaries with specific fields.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, fields, pageSize)
Get order delivery group summaries with specific fields.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, fields, sortParam)
Get a sorted list of order delivery group summaries with specific fields.

getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId, fields, pageSize, sortParam)
Get a sorted list of order delivery group summaries with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId)
Get order item summaries.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, pageSize)
Get order item summaries.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId)
Get order item summaries for a delivery group summary.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, pageSize)
Get order item summaries for a delivery group summary.


Apex Reference Guide CommerceBuyerExperience Class

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, pageParam)
Get a page of order item summaries for a delivery group summary.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields)
Get order item summaries for a delivery group summary with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields, pageSize)
Get order item summaries for a delivery group summary with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields, pageParam)
Get a page of order item summaries for a delivery group summary with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields, sortParam)
Get a sorted list of order item summaries for a delivery group summary with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields, pageSize, sortParam)
Get a sorted page of order item summaries for a delivery group summary with specific fields.

getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId, orderDeliveryGroupSummaryId, fields, pageParam,
pageSize, sortParam, includeAdjustmentDetails)
Get a sorted page of order item summaries for a delivery group summary with specific fields and include adjustment details.

getOrderItemSummaryAdjustments(webstoreId, orderSummaryId, orderItemSummaryAdjustmentCollectionInput)
Get adjustments for order items.

getOrderItemSummaryAdjustments(webstoreId, orderSummaryId, orderItemSummaryAdjustmentCollectionInput, effectiveAccountId)
Get adjustments for order items.

getOrderShipmentItems(webstoreId, shipmentId)
Get order shipment items.

getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId)
Get order shipment items.

getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields)
Get order shipment items with specific fields.

getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields, pageToken, pageSize)
Get a page of order shipment items with specific fields.

getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields, pageToken, pageSize, sortOrder)
Get a sorted page of order shipment items.

getOrderShipments(webstoreId, orderSummaryId)
Get order shipments.

getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId)
Get order shipments.

getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields)
Get order shipments with specific fields.

getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields, pageSize, pageToken)
Get a page of order shipments with specific fields.

getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields, pageSize, pageToken, sortOrder)
Get a sorted page of order shipments with specific fields.

getOrderSummaries(webstoreId)
Get order summaries.


Apex Reference Guide CommerceBuyerExperience Class

getOrderSummaries(webstoreId, effectiveAccountId)
Get order summaries.

getOrderSummaries(webstoreId, effectiveAccountId, fields)
Get order summaries with specific fields.

getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken)
Get a page of order summaries with specific fields.

getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken, sortOrder)
Get a sorted page of order summaries with specific fields.

getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken, sortOrder, earliestDate, latestDate)
Get a sorted page of order summaries with specific fields within a specific date range.

getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken, sortOrder, earliestDate, latestDate, ownerScoped)
Get a sorted page of order summaries with specific fields within a specific date range and scoped to orders owned by the context
user.

getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken, sortOrder, earliestDate, latestDate, ownerScoped,
includeAdjustmentDetails)
Get a sorted page of order summaries with specific fields within a specific date range and scoped to orders owned by the context
user.

getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId)
Get an order summary.

getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId, fields)
Get an order summary with fields.

getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId, fields, includeAdjustmentDetails)
Get an order summary with fields and include adjustment details.

getOrderSummaryAdjustments(webstoreId, orderSummaryId)
Get adjustments for an order summary.

getOrderSummaryAdjustments(webstoreId, orderSummaryId, effectiveAccountId)
Get adjustments for an order summary.

lookupOrderSummary(webstoreId, effectiveAccountId, fields, excludeLineItems, excludeDeliveryGroups, excludeAdjustmentAggregates,
excludeAdjustments, deliveryGroupId, orderSummaryLookupInput) (Developer Preview)
Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID, requested fields,
line items, delivery groups, adjustments aggregates, and adjustments.

lookupOrderSummary(webstoreId, effectiveAccountId, fields, orderSummaryLookupInput) (Developer Preview)
Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID and requested
fields.

lookupOrderSummary(webstoreId, effectiveAccountId, orderSummaryLookupInput) (Developer Preview)
Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID.

updateCommerceAccountAddress(webstoreId, accountId, addressId, addressInput)
Update a Commerce account address for a webstore.

##### **`addOrderToCart(webstoreId, orderSummaryId, orderToCartInput)`**

Add an order to a cart using a webstore order summary.


Apex Reference Guide CommerceBuyerExperience Class

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderToCartResult addOrderToCart(String webstoreId, String

   orderSummaryId, ConnectApi.OrderToCartInput orderToCartInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderToCartInput
```

Type: `ConnectApi.OrderToCartInput`

Input value indicating which cart the order should be added to.

Return Value

Type: `ConnectApi.OrderToCartResult`

##### **`addOrderToCart(webstoreId, orderSummaryId, orderToCartInput,`**

```
  effectiveAccountId)

```

Add an order to a cart for a specific account using a webstore order summary.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderToCartResult addOrderToCart(String webstoreId, String

   orderSummaryId, ConnectApi.OrderToCartInput orderToCartInput, String effectiveAccountId)

```


Apex Reference Guide CommerceBuyerExperience Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderToCartInput
```

Type: `ConnectApi.OrderToCartInput`

Input value indicating which cart the order should be added to.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.OrderToCartResult`

##### **`calculateAdjustmentAggregates(webstoreId, orderSummaryIds)`**

Submit a job to calculate adjustment aggregates for a list of order summary IDs.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryAdjustmentAggregatesAsyncOutput

   calculateAdjustmentAggregates(String webstoreId,

   ConnectApi.OrderSummaryAdjustmentAggregatesAsyncInput orderSummaryIds)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryIds
```

Type: `ConnectApi.OrderSummaryAdjustmentAggregatesAsyncInput`

A `ConnectApi.OrderSummaryAdjustmentAggregatesAsyncInput` class with a list of order summary IDs.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryAdjustmentAggregatesAsyncOutput`

##### **`createCommerceAccountAddress(webstoreId, accountId, addressInput)`**

Create a Commerce account address for a webstore account.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressOutput createCommerceAccountAddress(String

   webstoreId, String accountId, ConnectApi.commerceAddressInput addressInput)

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

ID of the account.

```
   addressInput
```

Type: `ConnectApi.commerceAddressInput`

Information about the address you want to create.

Return Value

Type: `ConnectApi.CommerceAddressOutput`

##### **`deleteCommerceAccountAddress(webstoreId, accountId, addressId)`**

Delete a Commerce account address for a webstore.

API Version

54.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static Void deleteCommerceAccountAddress(String webstoreId, String accountId,

   String addressId)

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

ID of the account.

```
   addressId
```

Type: String

ID of the address.

Return Value

Type: Void

##### **`getCommerceAccountAddress(webstoreId, accountId)`**

Get a Commerce account address for a webstore.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

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

ID of the account.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getCommerceAccountAddress(webstoreId, accountId, defaultOnly)`**

Get Commerce account addresses for a webstore and account.

You can get the default address by itself, or you can get all of the addresses for the account.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

   webstoreId, String accountId, Boolean defaultOnly)

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

ID of the account.

```
   defaultOnly
```

Type: Boolean

Indicate if you only want the default address ( `true` ) or all addresses for the account ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType,`**

```
  fields, pageToken, pageSize, sortOrder)

```

Get Commerce account addresses for a webstore and account.

API Version

54.0


Apex Reference Guide CommerceBuyerExperience Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

   webstoreId, String accountId, Boolean defaultOnly, List<String> addressType, List<String>

   fields, String pageToken, Integer pageSize, ConnectApi.CommerceAddressSort sortOrder)

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

ID of the account.

```
   defaultOnly
```

Type: Boolean

Indicate if you want only the default address ( `true` ) or all addresses for the account ( `false` ). The default value is `false` .

```
   addressType
```

Type: List<String>

Type of address, for example, `Billing` or `Shipping` .

```
   fields
```

Type: List<String>

A list of custom fields for the address.

```
   pageToken
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortOrder
```

Type: `ConnectApi.CommerceAddressSort`

Sort order for Commerce addresses.

**•** `CreatedDateAsc` —Sort in ascending order of created date.

**•** `CreatedDateDesc` —Sort in descending order of created date.

**•** `NameAsc` —Sort in ascending order of name.

**•** `NameDesc` —Sort in descending order of name.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getCommerceAccountAddress(webstoreId, accountId, addressType,`**

```
  excludeUnsupportedCountries)

```

Get Commerce account addresses for a webstore and account.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

   webstoreId, String accountId, List<String> addressType, Boolean

   excludeUnsupportedCountries)

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

ID of the account.

```
   addressType
```

Type: List<String>

Type of address, for example, `Billing` or `Shipping` .

```
   excludeUnsupportedCountries
```

Type: Boolean

Indicate if you want to retrieve all addresses ( `false` ) or only addresses of type Shipping that are in countries included in the store’s
shipToCountries list ( `true` ). The default value is `false` .

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType,`**

```
  excludeUnsupportedCountries)

```

Get Commerce account addresses for a webstore and account.


Apex Reference Guide CommerceBuyerExperience Class

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

   webstoreId, String accountId, Boolean defaultOnly, List<String> addressType, Boolean

   excludeUnsupportedCountries)

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

ID of the account.

```
   defaultOnly
```

Type: Boolean

Indicate if you want only the default address ( `true` ) or all addresses for the account ( `false` ). The default value is `false` .

```
   addressType
```

Type: List<String>

Type of address, for example, `Billing` or `Shipping` .

```
   excludeUnsupportedCountries
```

Type: Boolean

Indicate if you want to retrieve all addresses ( `false` ) or only addresses of type Shipping that are in countries included in the store’s
shipToCountries list ( `true` ). The default value is `false` .

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getCommerceAccountAddress(webstoreId, accountId, defaultOnly, addressType,`**

```
  excludeUnsupportedCountries, fields, pageToken, pageSize, sortOrder)

```

Get Commerce account addresses for a webstore and account.

API Version

57.0


Apex Reference Guide CommerceBuyerExperience Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressCollection getCommerceAccountAddress(String

   webstoreId, String accountId, Boolean defaultOnly, List<String> addressType, Boolean

   excludeUnsupportedCountries, List<String> fields, String pageToken, Integer pageSize,

   ConnectApi.CommerceAddressSort sortOrder)

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

ID of the account.

```
   defaultOnly
```

Type: Boolean

Indicate if you want only the default address ( `true` ) or all addresses for the account ( `false` ). The default value is `false` .

```
   addressType
```

Type: List<String>

Type of address, for example, `Billing` or `Shipping` .

```
   excludeUnsupportedCountries
```

Type: Boolean

Indicate if you want to retrieve all addresses ( `false` ) or only addresses of type Shipping that are in countries included in the store’s
shipToCountries list ( `true` ). The default value is `false` .

```
   fields
```

Type: List<String>

A list of custom fields for the address.

```
   pageToken
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortOrder
```

Type: `ConnectApi.CommerceAddressSort`

Sort order for Commerce addresses. Values are:

**•** `CreatedDateAsc` —Sort in ascending order of created date.

**•** `CreatedDateDesc` —Sort in descending order of created date.


Apex Reference Guide CommerceBuyerExperience Class

**•** `NameAsc` —Sort in ascending order of name.

**•** `NameDesc` —Sort in descending order of name.

Return Value

Type: `ConnectApi.CommerceAddressCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId)`**

Get order delivery group summaries.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  pageSize)

```

Get order delivery group summaries.


Apex Reference Guide CommerceBuyerExperience Class

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  pageParam)

```

Get a page of order delivery group summaries.

API Version

51.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, String pageParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  fields)

```

Get order delivery group summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, List<String> fields)

```


Apex Reference Guide CommerceBuyerExperience Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   fields
```

Type: List<String>

List of up to 15 order delivery group summary or order delivery method fields to display in the UI in each item row. For example,
`fields=OrderDeliveryGroupSummary.DeliveryAddress, OrderDeliveryMethod.Name` .

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  pageParam, fields)

```

Get a page of order delivery group summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, String pageParam, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceBuyerExperience Class

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   fields
```

Type: List<String>

List of up to 15 order delivery group summary or order delivery method fields to display in the UI in each item row. For example,
`fields=OrderDeliveryGroupSummary.DeliveryAddress, OrderDeliveryMethod.Name` .

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  fields, pageSize)

```

Get order delivery group summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, List<String> fields, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.


Apex Reference Guide CommerceBuyerExperience Class

```
   fields
```

Type: List<String>

List of up to 15 order delivery group summary or order delivery method fields to display in the UI in each item row. For example,
`fields=OrderDeliveryGroupSummary.DeliveryAddress, OrderDeliveryMethod.Name` .

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  fields, sortParam)

```

Get a sorted list of order delivery group summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, List<String> fields, ConnectApi.OrderDeliveryGroupSummarySort sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   fields
```

Type: List<String>

List of up to 15 order delivery group summary or order delivery method fields to display in the UI in each item row. For example,
`fields=OrderDeliveryGroupSummary.DeliveryAddress, OrderDeliveryMethod.Name` .


Apex Reference Guide CommerceBuyerExperience Class

```
   sortParam
```

Type: `ConnectApi.OrderDeliveryGroupSummarySort`

Sort order for order delivery group summaries. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If `null`, `IdAsc` is the default sort order.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderDeliveryGroupSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  fields, pageSize, sortParam)

```

Get a sorted list of order delivery group summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderDeliveryGroupSummaryCollection

   getOrderDeliveryGroupSummaries(String webstoreId, String effectiveAccountId, String

   orderSummaryId, List<String> fields, Integer pageSize,

   ConnectApi.OrderDeliveryGroupSummarySort sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   fields
```

Type: List<String>

List of up to 15 order delivery group summary or order delivery method fields to display in the UI in each item row. For example,
`fields=OrderDeliveryGroupSummary.DeliveryAddress, OrderDeliveryMethod.Name` .


Apex Reference Guide CommerceBuyerExperience Class

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.OrderDeliveryGroupSummarySort`

Sort order for order delivery group summaries. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If `null`, `IdAsc` is the default sort order.

Return Value

Type: `ConnectApi.OrderDeliveryGroupSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId)`**

Get order item summaries.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`


Apex Reference Guide CommerceBuyerExperience Class

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  pageSize)

```

Get order item summaries.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId)

```

Get order item summaries for a delivery group summary.

API Version

51.0


Apex Reference Guide CommerceBuyerExperience Class

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, pageSize)

```

Get order item summaries for a delivery group summary.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, Integer pageSize)

```


Apex Reference Guide CommerceBuyerExperience Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, pageParam)

```

Get a page of order item summaries for a delivery group summary.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, String pageParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceBuyerExperience Class

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields)

```

Get order item summaries for a delivery group summary with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceBuyerExperience Class

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields, pageSize)

```

Get order item summaries for a delivery group summary with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String


Apex Reference Guide CommerceBuyerExperience Class

ID of the order delivery group summary.

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields, pageParam)

```

Get a page of order item summaries for a delivery group summary with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields, String pageParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.


Apex Reference Guide CommerceBuyerExperience Class

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields, sortParam)

```

Get a sorted list of order item summaries for a delivery group summary with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields, ConnectApi.OrderItemSummarySort

   sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.


Apex Reference Guide CommerceBuyerExperience Class

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

```
   sortParam
```

Type: `ConnectApi.OrderItemSummarySort`

Sort order for order item summaries. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If `null`, `IdAsc` is the default sort order.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields, pageSize, sortParam)

```

Get a sorted page of order item summaries for a delivery group summary with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields, Integer pageSize,

   ConnectApi.OrderItemSummarySort sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.


Apex Reference Guide CommerceBuyerExperience Class

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.OrderItemSummarySort`

Sort order for order item summaries. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If `null`, `IdAsc` is the default sort order.

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaries(webstoreId, effectiveAccountId, orderSummaryId,`**

```
  orderDeliveryGroupSummaryId, fields, pageParam, pageSize, sortParam,

  includeAdjustmentDetails)

```

Get a sorted page of order item summaries for a delivery group summary with specific fields and include adjustment details.

API Version

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryCollection getOrderItemSummaries(String

   webstoreId, String effectiveAccountId, String orderSummaryId, String

   orderDeliveryGroupSummaryId, List<String> fields, String pageParam, Integer pageSize,

   ConnectApi.OrderItemSummarySort sortParam, Boolean includeAdjustmentDetails)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceBuyerExperience Class

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderDeliveryGroupSummaryId
```

Type: String

ID of the order delivery group summary.

```
   fields
```

Type: List<String>

List of up to 15 order item summary or product fields to display in the UI in each item row.

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

```
   sortParam
```

Type: `ConnectApi.OrderItemSummarySort`

Sort order for order item summaries. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If `null`, `IdAsc` is the default sort order.

```
   includeAdjustmentDetails
```

Type: Boolean

Specifies whether to return adjustment details ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.OrderItemSummaryCollection`

##### **`getOrderItemSummaryAdjustments(webstoreId, orderSummaryId,`**

```
  orderItemSummaryAdjustmentCollectionInput)

```

Get adjustments for order items.

API Version

53.0


Apex Reference Guide CommerceBuyerExperience Class

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryAdjustmentCollection

   getOrderItemSummaryAdjustments(String webstoreId, String orderSummaryId,

   ConnectApi.OrderItemSummaryAdjustmentCollectionInput

   orderItemSummaryAdjustmentCollectionInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderItemSummaryAdjustmentCollectionInput
```

Type: `ConnectApi.OrderItemSummaryAdjustmentCollectionInput`

Collection of order item summaries to get adjustments for.

Return Value

Type: `ConnectApi.OrderItemSummaryAdjustmentCollection`

##### **`getOrderItemSummaryAdjustments(webstoreId, orderSummaryId,`**

```
  orderItemSummaryAdjustmentCollectionInput, effectiveAccountId)

```

Get adjustments for order items.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderItemSummaryAdjustmentCollection

   getOrderItemSummaryAdjustments(String webstoreId, String orderSummaryId,

   ConnectApi.OrderItemSummaryAdjustmentCollectionInput

   orderItemSummaryAdjustmentCollectionInput, String effectiveAccountId)

```


Apex Reference Guide CommerceBuyerExperience Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   orderItemSummaryAdjustmentCollectionInput
```

Type: `ConnectApi.OrderItemSummaryAdjustmentCollectionInput`

Collection of order item summaries to get adjustments for.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.OrderItemSummaryAdjustmentCollection`

##### **`getOrderShipmentItems(webstoreId, shipmentId)`**

Get order shipment items.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentItemCollection getOrderShipmentItems(String

   webstoreId, String shipmentId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   shipmentId
```

Type: String

ID of the shipment.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderShipmentItemCollection`

##### **`getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId)`**

Get order shipment items.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentItemCollection getOrderShipmentItems(String

   webstoreId, String shipmentId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   shipmentId
```

Type: String

ID of the shipment.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.OrderShipmentItemCollection`

##### **`getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields)`**

Get order shipment items with specific fields.

API Version

52.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderShipmentItemCollection getOrderShipmentItems(String

   webstoreId, String shipmentId, String effectiveAccountId, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   shipmentId
```

Type: String

ID of the shipment.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment items, order item summary, and product fields to display in the UI in each item row.

Return Value

Type: `ConnectApi.OrderShipmentItemCollection`

##### **`getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields,`**

```
  pageToken, pageSize)

```

Get a page of order shipment items with specific fields.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentItemCollection getOrderShipmentItems(String

   webstoreId, String shipmentId, String effectiveAccountId, List<String> fields, String

   pageToken, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceBuyerExperience Class

```
   shipmentId
```

Type: String

ID of the shipment.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment items, order item summary, and product fields to display in the UI in each item row.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.OrderShipmentItemCollection`

##### **`getOrderShipmentItems(webstoreId, shipmentId, effectiveAccountId, fields,`**

```
  pageToken, pageSize, sortOrder)

```

Get a sorted page of order shipment items.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentItemCollection getOrderShipmentItems(String

   webstoreId, String shipmentId, String effectiveAccountId, List<String> fields, String

   pageToken, Integer pageSize, ConnectApi.OrderShipmentItemSort sortOrder)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   shipmentId
```

Type: String


Apex Reference Guide CommerceBuyerExperience Class

ID of the shipment.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment items, order item summary, and product fields to display in the UI in each item row.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortOrder
```

Type: `ConnectApi.OrderShipmentItemSort`

Sort order for order shipment items. Values are:

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

If unspecified, defaults to `IdAsc` .

Return Value

Type: `ConnectApi.OrderShipmentItemCollection`

##### **`getOrderShipments(webstoreId, orderSummaryId)`**

Get order shipments.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentCollection getOrderShipments(String webstoreId,

   String orderSummaryId)

```

Parameters

```
   webstoreId
```

Type: String


Apex Reference Guide CommerceBuyerExperience Class

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

Return Value

Type: `ConnectApi.OrderShipmentCollection`

##### **`getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId)`**

Get order shipments.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentCollection getOrderShipments(String webstoreId,

   String orderSummaryId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.OrderShipmentCollection`

##### **`getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields)`**

Get order shipments with specific fields.


Apex Reference Guide CommerceBuyerExperience Class

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderShipmentCollection getOrderShipments(String webstoreId,

   String orderSummaryId, String effectiveAccountId, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment and order delivery method fields to display in the UI in each item row.

Return Value

Type: `ConnectApi.OrderShipmentCollection`

##### **`getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields,`**

```
  pageSize, pageToken)

```

Get a page of order shipments with specific fields.

API Version

52.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderShipmentCollection getOrderShipments(String webstoreId,

   String orderSummaryId, String effectiveAccountId, List<String> fields, Integer pageSize,

   String pageToken)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment and order delivery method fields to display in the UI in each item row.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

Return Value

Type: `ConnectApi.OrderShipmentCollection`

##### **`getOrderShipments(webstoreId, orderSummaryId, effectiveAccountId, fields,`**

```
  pageSize, pageToken, sortOrder)

```

Get a sorted page of order shipments with specific fields.

API Version

52.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderShipmentCollection getOrderShipments(String webstoreId,

   String orderSummaryId, String effectiveAccountId, List<String> fields, Integer pageSize,

   String pageToken, ConnectApi.OrderShipmentSort sortOrder)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 15 additional shipment and order delivery method fields to display in the UI in each item row.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   sortOrder
```

Type: `ConnectApi.OrderShipmentSort`

Sort order for order shipments. Values are:

**•** `ExpectedDeliveryDateAsc` —Sorts by the oldest expected delivery date.

**•** `ExpectedDeliveryDateDesc` —Sorts by the most recent expected delivery date.

**•** `ShipmentNumberAsc` —Sorts by shipment number in ascending order (0–9).

**•** `ShipmentNumberDesc` —Sorts by shipment number in descending order (9–0).

If unspecified, defaults to `ShipmentNumberAsc` .

If you’re sorting by expected delivery date, make sure the expected delivery date is populated on your shipment records. A `null`
value isn’t supported and results in an error.

Return Value

Type: `ConnectApi.OrderShipmentCollection`

##### **`getOrderSummaries(webstoreId)`**

Get order summaries.


Apex Reference Guide CommerceBuyerExperience Class

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummaries(webstoreId, effectiveAccountId)`**

Get order summaries.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields)`**

Get order summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`


Apex Reference Guide CommerceBuyerExperience Class

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken)`**

Get a page of order summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields, Integer pageSize, String

   pageToken)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken,`**

```
  sortOrder)

```

Get a sorted page of order summaries with specific fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields, Integer pageSize, String

   pageToken, ConnectApi.OrderSummarySortOrder sortOrder)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide CommerceBuyerExperience Class

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   sortOrder
```

Type: `ConnectApi.OrderSummarySortOrder`

Sort order for order summaries. Values are:

**•** `CreatedDateAsc` —Sorts by the oldest created date.

**•** `CreatedDateDesc` —Sorts by the most recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest ordered date.

**•** `OrderedDateDesc` —Sorts by the most recent ordered date.

If unspecified, defaults to `OrderedDateDesc` .

If you’re sorting by ordered date, make sure the ordered date is populated on your order summary records. A `null` value isn’t
supported and results in an error.

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken,`**

```
  sortOrder, earliestDate, latestDate)

```

Get a sorted page of order summaries with specific fields within a specific date range.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields, Integer pageSize, String

   pageToken, ConnectApi.OrderSummarySortOrder sortOrder, String earliestDate, String

   latestDate)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceBuyerExperience Class

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   sortOrder
```

Type: `ConnectApi.OrderSummarySortOrder`

Sort order for order summaries. Values are:

**•** `CreatedDateAsc` —Sorts by the oldest created date.

**•** `CreatedDateDesc` —Sorts by the most recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest ordered date.

**•** `OrderedDateDesc` —Sorts by the most recent ordered date.

If unspecified, defaults to `OrderedDateDesc` .

If you’re sorting by ordered date, make sure the ordered date is populated on your order summary records. A `null` value isn’t
supported and results in an error.

```
   earliestDate
```

Type: String

Oldest created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any orders
on and after this date..

```
   latestDate
```

Type: String

Most recent created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any
orders before this date.

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`


Apex Reference Guide CommerceBuyerExperience Class

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken,`**

```
  sortOrder, earliestDate, latestDate, ownerScoped)

```

Get a sorted page of order summaries with specific fields within a specific date range and scoped to orders owned by the context user.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields, Integer pageSize, String

   pageToken, ConnectApi.OrderSummarySortOrder sortOrder, String earliestDate, String

   latestDate, Boolean ownerScoped)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.


Apex Reference Guide CommerceBuyerExperience Class

```
   sortOrder
```

Type: `ConnectApi.OrderSummarySortOrder`

Sort order for order summaries. Values are:

**•** `CreatedDateAsc` —Sorts by the oldest created date.

**•** `CreatedDateDesc` —Sorts by the most recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest ordered date.

**•** `OrderedDateDesc` —Sorts by the most recent ordered date.

If unspecified, defaults to `OrderedDateDesc` .

If you’re sorting by ordered date, make sure the ordered date is populated on your order summary records. A `null` value isn’t
supported and results in an error.

```
   earliestDate
```

Type: String

Oldest created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any orders
on and after this date..

```
   latestDate
```

Type: String

Most recent created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any
orders before this date.

```
   ownerScoped
```

Type: Boolean

Specifies whether the results are scoped to orders owned by the context user ( `true` ) or to orders owned by and shared with the
context user ( `false` ). If unspecified, defaults to `true` .

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummaries(webstoreId, effectiveAccountId, fields, pageSize, pageToken,`**

```
  sortOrder, earliestDate, latestDate, ownerScoped, includeAdjustmentDetails)

```

Get a sorted page of order summaries with specific fields within a specific date range and scoped to orders owned by the context user.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryCollectionRepresentation getOrderSummaries(String

   webstoreId, String effectiveAccountId, List<String> fields, Integer pageSize, String

```


Apex Reference Guide CommerceBuyerExperience Class

```
   pageToken, ConnectApi.OrderSummarySortOrder sortOrder, String earliestDate, String

   latestDate, Boolean ownerScoped, Boolean includeAdjustmentDetails)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   sortOrder
```

Type: `ConnectApi.OrderSummarySortOrder`

Sort order for order summaries. Values are:

**•** `CreatedDateAsc` —Sorts by the oldest created date.

**•** `CreatedDateDesc` —Sorts by the most recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest ordered date.

**•** `OrderedDateDesc` —Sorts by the most recent ordered date.

If unspecified, defaults to `OrderedDateDesc` .

If you’re sorting by ordered date, make sure the ordered date is populated on your order summary records. A `null` value isn’t
supported and results in an error.

```
   earliestDate
```

Type: String


Apex Reference Guide CommerceBuyerExperience Class

Oldest created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any orders
on and after this date..

```
   latestDate
```

Type: String

Most recent created or ordered date, depending on the `sortOrder` value, for order summaries to return. Results include any
orders before this date.

```
   ownerScoped
```

Type: Boolean

Specifies whether the results are scoped to orders owned by the context user ( `true` ) or to orders owned by and shared with the
context user ( `false` ). If unspecified, defaults to `true` .

```
   includeAdjustmentDetails
```

Type: Boolean

Specifies whether to fetch price adjustment details based on their type ( `true` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.OrderSummaryCollectionRepresentation`

##### **`getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId)`**

Get an order summary.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryRepresentation getOrderSummary(String webstoreId,

   String orderSummaryId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryRepresentation`

##### **`getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId, fields)`**

Get an order summary with fields.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryRepresentation getOrderSummary(String webstoreId,

   String orderSummaryId, String effectiveAccountId, List<String> fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryRepresentation`

##### **`getOrderSummary(webstoreId, orderSummaryId, effectiveAccountId, fields,`**

```
   includeAdjustmentDetails)

```

Get an order summary with fields and include adjustment details.

API Version

55.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryRepresentation getOrderSummary(String webstoreId,

   String orderSummaryId, String effectiveAccountId, List<String> fields, Boolean

   includeAdjustmentDetails)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   fields
```

Type: List<String>

List of up to 35 additional order summary fields to display in the UI in each item row.

These order summary fields are returned regardless of fields specified.

**•** `createdDate`

**•** `orderSummaryId`

**•** `orderNumber`

**•** `orderedDate`

**•** `ownerId`

**•** `status`

**•** `totalAmount`


Apex Reference Guide CommerceBuyerExperience Class

```
   includeAdjustmentDetails
```

Type: Boolean

Specifies whether to return adjustment details ( `true` ) or not ( `false` ). If unspecified, the default value is `false` .

Return Value

Type: `ConnectApi.OrderSummaryRepresentation`

##### **`getOrderSummaryAdjustments(webstoreId, orderSummaryId)`**

Get adjustments for an order summary.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryAdjustmentCollection

   getOrderSummaryAdjustments(String webstoreId, String orderSummaryId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

Return Value

Type: `ConnectApi.OrderSummaryAdjustmentCollection`

##### **`getOrderSummaryAdjustments(webstoreId, orderSummaryId, effectiveAccountId)`**

Get adjustments for an order summary.

API Version

53.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderSummaryAdjustmentCollection

   getOrderSummaryAdjustments(String webstoreId, String orderSummaryId, String

   effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   orderSummaryId
```

Type: String

ID of the order summary.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.OrderSummaryAdjustmentCollection`

##### **`lookupOrderSummary(webstoreId, effectiveAccountId, fields, excludeLineItems,`**

```
  excludeDeliveryGroups, excludeAdjustmentAggregates, excludeAdjustments,
```

**`deliveryGroupId, orderSummaryLookupInput)`** (Developer Preview)

Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID, requested fields, line
items, delivery groups, adjustments aggregates, and adjustments.

Note: This API is available as a developer preview. It isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or
tools.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No


Apex Reference Guide CommerceBuyerExperience Class

Signature

```
   public static ConnectApi.OrderSummaryLookupOutput lookupOrderSummary(String webstoreId,

   String effectiveAccountId, List<String> fields, Boolean excludeLineItems, Boolean

   excludeDeliveryGroups, Boolean excludeAdjustmentAggregates, Boolean excludeAdjustments,

   String deliveryGroupId, ConnectApi.OrderSummaryLookupInput orderSummaryLookupInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If unspecified, defaults to the account ID for the context user or, for guest users, the
guest buyer profile ID of the current store.

```
   fields
```

Type: List<String>

List of specific fields, including custom fields, to return in the response along with default fields. For example,
`OrderSummary.TotalAmount`, `OrderItemSummary.Quantity`, `Product2.Description`,
`OrderDeliveryGroupSummary.GrandTotalAmount`, `OrderDeliveryMethod.Carrier` .

```
   excludeLineItems
```

Type: Boolean

Specifies whether to exclude line items from the response. If unspecified, the default value is `false` .

```
   excludeDeliveryGroups
```

Type: Boolean

Specifies whether to exclude delivery groups from the response. If unspecified, the default value is `false` .

```
   excludeAdjustmentAggregates
```

Type: Boolean

Specifies whether to exclude adjustment aggregates associated with an order summary. Adjustment aggregates include fields
detailing promotional amounts by price, tax, and total. Aggregates are calculated asynchronously and results returned to the order
summary. If unspecified, the default value is `false` .

```
   excludeAdjustments
```

Type: Boolean

Specifies whether to exclude adjustments associated with an order summary. Adjustments include promotional discounts. If
unspecified, the default value is `false` .

```
   deliveryGroupId
```

Type: String

ID of the delivery group associated with the order summary.

```
   orderSummaryLookupInput
```

Type: `ConnectApi.OrderSummaryLookupInput`

Order summary lookup input representation.


Apex Reference Guide CommerceBuyerExperience Class

Return Value

Type: `ConnectApi.OrderSummaryLookupOutput`

##### **`lookupOrderSummary(webstoreId, effectiveAccountId, fields,`**

**`orderSummaryLookupInput)`** (Developer Preview)

Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID and requested fields.

Note: This API is available as a developer preview. It isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or
tools.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryLookupOutput lookupOrderSummary(String webstoreId,

   String effectiveAccountId, List<String> fields, ConnectApi.OrderSummaryLookupInput

   orderSummaryLookupInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If unspecified, defaults to the account ID for the context user or, for guest users, the
guest buyer profile ID of the current store.

```
   fields
```

Type: List<String>

List of specific fields, including custom fields, to return in the response along with default fields. For example,
`OrderSummary.TotalAmount`, `OrderItemSummary.Quantity`, `Product2.Description`,
`OrderDeliveryGroupSummary.GrandTotalAmount`, `OrderDeliveryMethod.Carrier` .

```
   orderSummaryLookupInput
```

Type: `ConnectApi.OrderSummaryLookupInput`


Apex Reference Guide CommerceBuyerExperience Class

Order summary lookup input representation.

Return Value

Type: `ConnectApi.OrderSummaryLookupOutput`

##### **`lookupOrderSummary(webstoreId, effectiveAccountId, orderSummaryLookupInput)`**

(Developer Preview)

Look up details about an order summary for a guest shopper or a registered buyer using the effective account ID.

Note: This API is available as a developer preview. It isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or
tools.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.OrderSummaryLookupOutput lookupOrderSummary(String webstoreId,

   String effectiveAccountId, ConnectApi.OrderSummaryLookupInput orderSummaryLookupInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If unspecified, defaults to the account ID for the context user or, for guest users, the
guest buyer profile ID of the current store.

```
   orderSummaryLookupInput
```

Type: `ConnectApi.OrderSummaryLookupInput`

Order summary lookup input representation.

Return Value

Type: `ConnectApi.OrderSummaryLookupOutput`


### Apex Reference Guide CommerceCart Class

##### **`updateCommerceAccountAddress(webstoreId, accountId, addressId, addressInput)`**

Update a Commerce account address for a webstore.

API Version

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceAddressOutput updateCommerceAccountAddress(String

   webstoreId, String accountId, String addressId, ConnectApi.commerceAddressInput

   addressInput)

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

ID of the account.

```
   addressId
```

Type: String

ID of the address.

```
   addressInput
```

Type: `ConnectApi.commerceAddressInput`

Information about the address fields you want to update.

Return Value

Type: `ConnectApi.CommerceAddressOutput`

### CommerceCart Class

Get, create, update, calculate, and delete carts. Get cart items, add items to carts, update and delete cart items.

Namespace

ConnectApi


Apex Reference Guide CommerceCart Class

#### CommerceCart Methods These methods are for CommerceCart . All methods are static.

IN THIS SECTION:

addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput, currencyIsoCode)
Add an item to a cart of a specific currency.

addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput, currencyIsoCode, includeCartData)
Add an item to a cart of a specific currency.

addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems)
Add a batch of up to 100 items to a cart.

addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems, currencyIsoCode)
Add a batch of up to 100 items to a cart of a specific currency.

addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput)
Add an item to a cart.

applyCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponInput)
Apply a coupon to a cart.

applyCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponInput, currencyIsoCode)
Apply a coupon to a cart.

copyCartToWishlist(webstoreId, effectiveAccountId, activeCartOrId, cartToWishlistInput)
Copy the products from a cart to a wishlist.

calculateCart(webstoreId, activeCartOrId, effectiveAccountId)
Calculate a cart.

calculateCart(webstoreId, activeCartOrId, effectiveAccountId, calculateCartInput)
Calculate a cart.

createCart(webstoreId, cart)
Create a cart.

cloneCart(webstoreId, activeCartOrId, targetEffectiveAccountId, targetType)
Clones an existing cart to create a secondary, read-only cart to support Pay Now functionality. Sets the guest cart status to
`PendingDelete` in a B2B store.

deleteCart(webstoreId, effectiveAccountId, activeCartOrId)
Delete a cart. Sets the guest cart status to `PendingDelete` in a B2B store or `Closed` in a D2C store.

deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId)
Delete a coupon from a cart.

deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId, currencyIsoCode)
Delete a coupon from a cart.

deleteCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId)
Delete an item from a cart.

deleteInventoryReservation(webstoreId, activeCartOrId, effectiveAccountId) (Pilot)
Delete an inventory reservation.


Apex Reference Guide CommerceCart Class

evaluateShipping(webstoreId, activeCartOrId, effectiveAccountId, cartEvaluateShippingInput)
Evaluate shipping costs for a cart.

evaluateTaxes(webstoreId, activeCartOrId, effectiveAccountId, cartEvaluateTaxInput)
Evaluate taxes for a cart.

getCartCoupons(webstoreId, effectiveAccountId, activeCartOrId)
Get coupons for a cart.

getCartCoupons(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Get coupons for a cart.

getCartItemPromotion(webstoreId, effectiveAccountId, activeCartOrId, cartItemPromotionCollectionInput)
Get promotions for a cart item.

getCartItemPromotion(webstoreId, effectiveAccountId, activeCartOrId, cartItemPromotionCollectionInput, currencyIsoCode)
Get a promotion for a cart item.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId)
Get items in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam)
Get a page of items in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam, sortParam)
Get a sorted page of items in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam, pageSize)
Get a specified size page of items in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam, pageSize, sortParam)
Get a specified size, sorted page of items in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields, pageParam, pageSize, sortParam)
Get a specified size, sorted page of items filtered by product fields in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields, pageParam, pageSize, sortParam, currencyIsoCode)
Get a specified size, sorted page of items filtered by product fields in a cart.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields, pageParam, pageSize, sortParam, currencyIsoCode,
includePromotions, includeCoupons)
Get a sorted page of items in a cart, including coupons and promotions.

getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields, pageParam, pageSize, sortParam, currencyIsoCode,
includePromotions, includeCoupons, pageNumber)
Get a specific, sorted page of items in a cart, including coupons and promotions.

getCartPromotions(webstoreId, effectiveAccountId, activeCartOrId)
Get promotions for a cart.

getCartPromotions(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Get promotions for a cart in a specific currency.

getCartSummary(webstoreId, effectiveAccountId, activeCartOrId)
Get a cart.

getCartSummary(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Get a cart in a specific currency.


Apex Reference Guide CommerceCart Class

getOrCreateActiveCartSummary(webstoreId, effectiveAccountId, activeCartOrId)
Get a cart or create an active cart if one doesn’t exist.

getOrCreateActiveCartSummary(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Get a cart in a specific currency, or create an active cart if one doesn’t exist.

getProductCartItem(webstoreId, effectiveAccountId, activeCartOrId, productId, currencyIsoCode)
Get cart items of a specific product.

getProductCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageSize, pageNumber, currencyIsoCode)
Get the items in a cart, sorted by product ID.

makeCartPrimary(webstoreId, activeCartOrId, effectiveAccountId)
Make a secondary cart a primary cart.

preserveGuestCart(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Preserve cart contents when a guest logs in as an authenticated customer. Sets the guest cart status to `PendingDelete` in a
B2B store or `Closed` in a D2C store.

setCartMessagesVisibility(webstoreId, activeCartOrId, effectiveAccountId, messageVisibility)
Set the visibility for cart messages.

updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId, cartItem)
Update an item in a cart.

updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId, cartItem, currencyIsoCode)
Update an item in a cart of a specific currency.

updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId, cartItem, currencyIsoCode, includeCartData)
Update an item in a cart of a specific currency.

upsertInventoryReservation(webstoreId, activeCartOrId, effectiveAccountId, cartInventoryReservationInput) (Pilot)
Create or update an inventory reservation.

##### **`addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput,`**

```
   currencyIsoCode)

```

Add an item to a cart of a specific currency.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartItem addItemToCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, ConnectApi.CartItemInput cartItemInput,

   String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String Use active only for B2B Aura stores; all other stores must use current.

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemInput
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing an item to add to the cart.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput,`**

```
  currencyIsoCode, includeCartData)

```

Add an item to a cart of a specific currency.

API Version

64.0

Available to Guest Users

51.0


Apex Reference Guide CommerceCart Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItem addItemToCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, ConnectApi.CartItemInput cartItemInput,

   String currencyIsoCode, Boolean includeCartData)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemInput
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing an item to add to the cart.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

```
   includeCartData
```

Type: Boolean

Specifies whether to return a collection of cart items in the response ( `true` ) or not ( `false` ). If unspecified, the default value is
`false` . This parameter is supported for D2C stores with Faster Add-to-Cart disabled. The cart must also have fewer than 25 items.

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems)`**

Add a batch of up to 100 items to a cart.


Apex Reference Guide CommerceCart Class

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BatchResult[] addItemsToCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, List<ConnectApi.BatchInput> cartItems)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   cartItems
```

Type: List< `ConnectApi.BatchInput`       

The list can contain up to 100 `ConnectApi.BatchInput` objects. In the `ConnectApi.BatchInput` constructor, the
input object must be `ConnectApi.CartItemInput` .

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.CartItem` object.

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.


Apex Reference Guide CommerceCart Class

##### **`addItemsToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItems,`**

```
  currencyIsoCode)

```

Add a batch of up to 100 items to a cart of a specific currency.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BatchResult[] addItemsToCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, List<ConnectApi.BatchInput> cartItems, String

   currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartItems
```

Type: List< `ConnectApi.BatchInput`       

The list can contain up to 100 `ConnectApi.BatchInput` objects. In the `ConnectApi.BatchInput` constructor, the
input object must be `ConnectApi.CartItemInput` .

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.CartItem` object.


Apex Reference Guide CommerceCart Class

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addItemToCart(webstoreId, effectiveAccountId, activeCartOrId, cartItemInput)`**

Add an item to a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItem addItemToCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, ConnectApi.CartItemInput cartItemInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   cartItemInput
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing an item to add to the cart.


Apex Reference Guide CommerceCart Class

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`applyCartCoupon(webstoreId, effectiveAccountId, activeCartOrId,`**

```
   cartCouponInput)

```

Apply a coupon to a cart.

API Version

54.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartCouponCollection applyCartCoupon(String webstoreId, String

   effectiveAccountId, String activeCartOrId, ConnectApi.cartCouponInput cartCouponInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartCouponInput
```

Type: `ConnectApi.cartCouponInput`

Coupon code for the coupon.


Apex Reference Guide CommerceCart Class

Return Value

Type: `ConnectApi.CartCouponCollection`

##### **`applyCartCoupon(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  cartCouponInput, currencyIsoCode)

```

Apply a coupon to a cart.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartCouponCollection applyCartCoupon(String webstoreId, String

   effectiveAccountId, String activeCartOrId, ConnectApi.cartCouponInput cartCouponInput,

   String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   cartCouponInput
```

Type: `ConnectApi.cartCouponInput`

Coupon code for the coupon.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.


Apex Reference Guide CommerceCart Class

Return Value

Type: `ConnectApi.CartCouponCollection`

##### **`copyCartToWishlist(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  cartToWishlistInput)

```

Copy the products from a cart to a wishlist.

API Version

50.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartToWishlistResult copyCartToWishlist(String webstoreId,

   String effectiveAccountId, String activeCartOrId, ConnectApi.CartToWishlistInput

   cartToWishlistInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartToWishlistInput
```

Type: `ConnectApi.CartToWishlistInput`

A `ConnectApi.CartToWishlistInput` object indicating the wishlist to copy products to.

Return Value

Type: `ConnectApi.CartToWishlistResult`


Apex Reference Guide CommerceCart Class

##### **`calculateCart(webstoreId, activeCartOrId, effectiveAccountId)`**

Calculate a cart.

API Version

62.0

Available to Guest Users

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CalculateCartResult calculateCart(String webstoreId, String

   activeCartOrId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

Return Value

Type: `ConnectApi.CalculateCartResult`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`calculateCart(webstoreId, activeCartOrId, effectiveAccountId,`**

```
  calculateCartInput)

```

Calculate a cart.


Apex Reference Guide CommerceCart Class

API Version

63.0

Available to Guest Users

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CalculateCartResult calculateCart(String webstoreId, String

   activeCartOrId, String effectiveAccountId, ConnectApi.CalculateCartInput

   calculateCartInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   calculateCartInput
```

Type: `ConnectApi.CalculateCartInput`

A `ConnectApi.CalculateCartInput` object representing any custom fields for the cart.

Return Value

Type: `ConnectApi.CalculateCartResult`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`createCart(webstoreId, cart)`**

Create a cart.


Apex Reference Guide CommerceCart Class

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartSummary createCart(String webstoreId, ConnectApi.CartInput

   cart)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   cart
```

Type: `ConnectApi.CartInput`

A `ConnectApi.CartInput` object representing a cart.

Return Value

Type: `ConnectApi.CartSummary`

Usage

Buyers with read access to carts can create and delete carts.

##### **`cloneCart(webstoreId, activeCartOrId, targetEffectiveAccountId, targetType)`**

Clones an existing cart to create a secondary, read-only cart to support Pay Now functionality. Sets the guest cart status to
`PendingDelete` in a B2B store.

API Version

60.0

Available to Guest Users

60.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartSummary cloneCart(String webstoreId, String activeCartOrId,

   String targetEffectiveAccountId, String targetType)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   targetEffectiveAccountId
```

Type: String

Effective Account ID associated with the cloned cart.

```
   targetType
```

Type: String

Type of the cloned cart. Value is `PayNowReadOnly` .

Return Value

Type: `ConnectApi.CartSummary on page 2222`

Usage

[The cloneCart method is valid only for the Pay Now feature. See Salesforce Pay Now for Embedded Payment Solutions.](https://help.salesforce.com/s/articleView?language=en_US&id=sf.pay_now_intro_prereqs.htm)

##### **`deleteCart(webstoreId, effectiveAccountId, activeCartOrId)`**

Delete a cart. Sets the guest cart status to `PendingDelete` in a B2B store or `Closed` in a D2C store.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static Void deleteCart(String webstoreId, String effectiveAccountId, String

   activeCartOrId)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

Return Value

Type: Void

Usage

Buyers with read access to carts can create and delete carts.

##### **`deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId)`**

Delete a coupon from a cart.

API Version

54.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static Void deleteCartCoupon(String webstoreId, String effectiveAccountId, String

   activeCartOrId, String cartCouponId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String


Apex Reference Guide CommerceCart Class

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartCouponId
```

Type: String

ID of the cart coupon.

Return Value

Type: Void

##### **`deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId,`**

```
  currencyIsoCode)

```

Delete a coupon from a cart.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static Void deleteCartCoupon(String webstoreId, String effectiveAccountId, String

   activeCartOrId, String cartCouponId, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.


Apex Reference Guide CommerceCart Class

```
   cartCouponId
```

Type: String

ID of the cart coupon.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: Void

##### **`deleteCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId)`**

Delete an item from a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static Void deleteCartItem(String webstoreId, String effectiveAccountId, String

   activeCartOrId, String cartItemId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   cartItemId
```

Type: String


Apex Reference Guide CommerceCart Class

ID of the cart item.

Return Value

Type: Void

Usage

Buyers with read access to carts can add, update, and delete items in carts.

##### **`deleteInventoryReservation(webstoreId, activeCartOrId, effectiveAccountId)`**

(Pilot)

Delete an inventory reservation.

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on
the basis of generally available products and features. This feature is made available on an AS IS basis and use of this feature is at
your sole risk.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static Void deleteInventoryReservation(String webstoreId, String activeCartOrId,

   String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String


Apex Reference Guide CommerceCart Class

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

Return Value

Type: Void

##### **`evaluateShipping(webstoreId, activeCartOrId, effectiveAccountId,`**

```
  cartEvaluateShippingInput)

```

Evaluate shipping costs for a cart.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CalculateCartResult evaluateShipping(String webstoreId, String

   activeCartOrId, String effectiveAccountId, ConnectApi.CartEvaluateShippingInput

   cartEvaluateShippingInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   cartEvaluateShippingInput
```

Type: `ConnectApi.CartEvaluateShippingInput`

A `ConnectApi.CartEvaluateShippingInput` object representing a shipping address and any custom fields.

Return Value

Type: `ConnectApi.CalculateCartResult`


Apex Reference Guide CommerceCart Class

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`evaluateTaxes(webstoreId, activeCartOrId, effectiveAccountId,`**

```
  cartEvaluateTaxInput)

```

Evaluate taxes for a cart.

API Version

63.0

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CalculateCartResult evaluateTaxes(String webstoreId, String

   activeCartOrId, String effectiveAccountId, ConnectApi.CartEvaluateTaxInput

   cartEvaluateTaxInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   cartEvaluateTaxInput
```

Type: `ConnectApi.CartEvaluateTaxInput`

A `ConnectApi.CartEvaluateTaxInput` object representing a shipping address and any custom fields.

Return Value

Type: `ConnectApi.CalculateCartResult`


Apex Reference Guide CommerceCart Class

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getCartCoupons(webstoreId, effectiveAccountId, activeCartOrId)`**

Get coupons for a cart.

API Version

54.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartCouponCollection getCartCoupons(String webstoreId, String

   effectiveAccountId, String activeCartOrId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

Return Value

Type: `ConnectApi.CartCouponCollection`

##### **`getCartCoupons(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Get coupons for a cart.


Apex Reference Guide CommerceCart Class

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartCouponCollection getCartCoupons(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

Return Value

Type: `ConnectApi.CartCouponCollection`

##### **`getCartItemPromotion(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  cartItemPromotionCollectionInput)

```

Get promotions for a cart item.

API Version

52.0

Available to Guest Users

57.0


Apex Reference Guide CommerceCart Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemPromotionCollectionOutputRepresentation

   getCartItemPromotion(String webstoreId, String effectiveAccountId, String activeCartOrId,

   ConnectApi.CartItemPromotionCollectionInputRepresentation

   cartItemPromotionCollectionInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemPromotionCollectionInput
```

Type: `ConnectApi.CartItemPromotionCollectionInputRepresentation`

Promotions for a cart item.

Return Value

Type: `ConnectApi.CartItemPromotionCollectionOutputRepresentation`

##### **`getCartItemPromotion(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  cartItemPromotionCollectionInput, currencyIsoCode)

```

Get a promotion for a cart item.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartItemPromotionCollectionOutputRepresentation

   getCartItemPromotion(String webstoreId, String effectiveAccountId, String activeCartOrId,

   ConnectApi.CartItemPromotionCollectionInputRepresentation

   cartItemPromotionCollectionInput, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemPromotionCollectionInput
```

Type: `ConnectApi.CartItemPromotionCollectionInputRepresentation`

Promotions for a cart item.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartItemPromotionCollectionOutputRepresentation`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId)`**

Get items in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam)`**

Get a page of items in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceCart Class

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam,`**

```
  sortParam)

```

Get a sorted page of items in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam, ConnectApi.CartItemSortOrder

   sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.


Apex Reference Guide CommerceCart Class

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   sortParam
```

Type: `ConnectApi.CartItemSortOrder`

Sort order for items in a cart. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `NameAsc` —Sorts by name in ascending alphabetical order (A–Z).

**•** `NameDesc` —Sorts by name in descending alphabetical order (Z–A).

**•** `SalesPriceAsc` —Sorts from lowest to highest negotiated price.

**•** `SalesPriceDesc` —Sorts from highest to lowest negotiated price.

If `null`, the default is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam,`**

```
  pageSize)

```

Get a specified size page of items in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam, Integer pageSize)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

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

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageParam,`**

```
  pageSize, sortParam)

```

Get a specified size, sorted page of items in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam, Integer pageSize,

   ConnectApi.CartItemSortOrder sortParam)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

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

```
   sortParam
```

Type: `ConnectApi.CartItemSortOrder`

Sort order for items in a cart. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `NameAsc` —Sorts by name in ascending alphabetical order (A–Z).

**•** `NameDesc` —Sorts by name in descending alphabetical order (Z–A).

**•** `SalesPriceAsc` —Sorts from lowest to highest negotiated price.

**•** `SalesPriceDesc` —Sorts from highest to lowest negotiated price.

If `null`, the default is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields,`**

```
  pageParam, pageSize, sortParam)

```

Get a specified size, sorted page of items filtered by product fields in a cart.

API Version

49.0


Apex Reference Guide CommerceCart Class

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.CartItemSortOrder sortParam)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   productFields
```

Type: String

Comma-separated list of up to 15 product fields. Results include fields that you have access to. Some product fields (such as
`productName` and `sku` ) are returned even when not included in the _`productFields`_ parameter.

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

```
   sortParam
```

Type: `ConnectApi.CartItemSortOrder`

Sort order for items in a cart. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `NameAsc` —Sorts by name in ascending alphabetical order (A–Z).

**•** `NameDesc` —Sorts by name in descending alphabetical order (Z–A).


Apex Reference Guide CommerceCart Class

**•** `SalesPriceAsc` —Sorts from lowest to highest negotiated price.

**•** `SalesPriceDesc` —Sorts from highest to lowest negotiated price.

If `null`, the default is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields,`**

```
  pageParam, pageSize, sortParam, currencyIsoCode)

```

Get a specified size, sorted page of items filtered by product fields in a cart.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.CartItemSortOrder sortParam, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   productFields
```

Type: String

Comma-separated list of up to 15 product fields. Results include fields that you have access to. Some product fields (such as
`productName` and `sku` ) are returned even when not included in the _`productFields`_ parameter.


Apex Reference Guide CommerceCart Class

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

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields,`**

```
  pageParam, pageSize, sortParam, currencyIsoCode, includePromotions,

  includeCoupons)

```

Get a sorted page of items in a cart, including coupons and promotions.

API Version

59.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.CartItemSortOrder sortParam, String currencyIsoCode,

   Boolean includePromotions, Boolean includeCoupons)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String


Apex Reference Guide CommerceCart Class

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   productFields
```

Type: String

Comma-separated list of up to 15 product fields. Results include fields that you have access to. Some product fields (such as
`productName` and `sku` ) are returned even when not included in the _`productFields`_ parameter.

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

```
   includePromotions
```

Type: Boolean

Indicates whether to include coupons ( `True` ) or not ( `False` )

```
   includeCoupons
```

Type: Boolean

Indicates whether to include promotions ( `True` ) or not ( `False` ).

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields,`**

```
  pageParam, pageSize, sortParam, currencyIsoCode, includePromotions,

  includeCoupons, pageNumber)

```

Get a specific, sorted page of items in a cart, including coupons and promotions.

API Version

60.0

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.CartItemSortOrder sortParam, String currencyIsoCode,

   Boolean includePromotions, Boolean includeCoupons, Integer pageNumber)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   productFields
```

Type: String

Comma-separated list of up to 15 product fields. Results include fields that you have access to. Some product fields (such as
`productName` and `sku` ) are returned even when not included in the _`productFields`_ parameter.

```
   pageParam
```

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

Description

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortParam
```

Type: `ConnectApi.CartItemSortOrder`

Sort order for items in a cart. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `NameAsc` —Sorts by name in ascending alphabetical order (A–Z).

**•** `NameDesc` —Sorts by name in descending alphabetical order (Z–A).

**•** `SalesPriceAsc` —Sorts from lowest to highest negotiated price.

**•** `SalesPriceDesc` —Sorts from highest to lowest negotiated price.

If `null`, the default is `CreatedDateDesc` .

```
   includePromotions
```

Type: Boolean

Indicates whether to include coupons ( `True` ) or not ( `False` )


Apex Reference Guide CommerceCart Class

```
   includeCoupons
```

Type: Boolean

Indicates whether to include promotions ( `True` ) or not ( `False` ).

```
   pageNumber
```

Type: Integer

Specifies the requested page number.

Return Value

Type: `ConnectApi.CartItemCollection`

##### **`getCartPromotions(webstoreId, effectiveAccountId, activeCartOrId)`**

Get promotions for a cart.

API Version

53.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartPromotionCollection getCartPromotions(String webstoreId,

   String effectiveAccountId, String activeCartOrId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.


Apex Reference Guide CommerceCart Class

Return Value

Type: `ConnectApi.CartPromotionCollection`

##### **`getCartPromotions(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Get promotions for a cart in a specific currency.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartPromotionCollection getCartPromotions(String webstoreId,

   String effectiveAccountId, String activeCartOrId, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartPromotionCollection`


Apex Reference Guide CommerceCart Class

##### **`getCartSummary(webstoreId, effectiveAccountId, activeCartOrId)`**

Get a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartSummary getCartSummary(String webstoreId, String

   effectiveAccountId, String activeCartOrId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . If you specify `active` and there isn’t an active cart, you get an error.

Return Value

Type: `ConnectApi.CartSummary`

##### **`getCartSummary(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Get a cart in a specific currency.

API Version

57.0


Apex Reference Guide CommerceCart Class

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartSummary getCartSummary(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartSummary`

##### **`getOrCreateActiveCartSummary(webstoreId, effectiveAccountId, activeCartOrId)`**

Get a cart or create an active cart if one doesn’t exist.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide CommerceCart Class

Signature

```
   public static ConnectApi.CartSummary getOrCreateActiveCartSummary(String webstoreId,

   String effectiveAccountId, String activeCartOrId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . If you specify `active` and there isn’t an active cart, one is created.

Return Value

Type: `ConnectApi.CartSummary`

Usage

Buyers with read access to carts can create and delete carts.

##### **`getOrCreateActiveCartSummary(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Get a cart in a specific currency, or create an active cart if one doesn’t exist.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartSummary getOrCreateActiveCartSummary(String webstoreId,

   String effectiveAccountId, String activeCartOrId, String currencyIsoCode)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartSummary`

Usage

Buyers with read access to carts can create and delete carts.

##### **`getProductCartItem(webstoreId, effectiveAccountId, activeCartOrId, productId,`**

```
  currencyIsoCode)

```

Get cart items of a specific product.

API Version

60.0

Available to Guest Users

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCartItem getProductCartItem(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productId, String currencyIsoCode)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the web store.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

```
   webstoreId
```

Type: String

ID of the product.

Return Value

Type: `ConnectApi.ProductCartItem on page 2476`

##### **`getProductCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageSize,`**

```
  pageNumber, currencyIsoCode)

```

Get the items in a cart, sorted by product ID.

API Version

60.0

Available to Guest Users

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCartItemCollection getProductCartItems(String webstoreId,

   String effectiveAccountId, String activeCartOrId, Integer pageSize, Integer pageNumber,

   String currencyIsoCode)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   pageNumber
```

Type: Integer

Specifies the requested page number.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 25.

```
   webstoreId
```

Type: String

ID of the web store.

Return Value

Type: `ConnectApi.ProductCartItemCollection on page 2476`

##### **`makeCartPrimary(webstoreId, activeCartOrId, effectiveAccountId)`**

Make a secondary cart a primary cart.

API Version

53.0

Available to Guest Users

56.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommerceActionResult makeCartPrimary(String webstoreId, String

   activeCartOrId, String effectiveAccountId)

```


Apex Reference Guide CommerceCart Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

Return Value

Type: `ConnectApi.CommerceActionResult`

##### **`preserveGuestCart(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Preserve cart contents when a guest logs in as an authenticated customer. Sets the guest cart status to `PendingDelete` in a B2B
store or `Closed` in a D2C store.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PreserveCart preserveGuestCart(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If null, the default value is determined from context.

```
   activeCartOrId
```

Type: String


Apex Reference Guide CommerceCart Class

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

Return Value

Type: `ConnectApi.PreserveCart` on page 2469

##### **`setCartMessagesVisibility(webstoreId, activeCartOrId, effectiveAccountId,`**

```
  messageVisibility)

```

Set the visibility for cart messages.

API Version

50.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartMessagesVisibilityResult setCartMessagesVisibility(String

   webstoreId, String activeCartOrId, String effectiveAccountId,

   ConnectApi.CartMessagesVisibilityInput messageVisibility)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   messageVisibility
```

Type: `ConnectApi.CartMessagesVisibilityInput`


Apex Reference Guide CommerceCart Class

A `ConnectApi.CartMessagesVisibilityInput` object specifying the visibility setting.

Return Value

Type: `ConnectApi.CartMessagesVisibilityResult`

##### **`updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId,`**

```
  cartItem)

```

Update an item in a cart.

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItem updateCartItem(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String cartItemId, ConnectApi.CartItemInput

   cartItem)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` .

```
   cartItemId
```

Type: String

ID of the cart item.

```
   cartItem
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing a cart item to update.


Apex Reference Guide CommerceCart Class

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId,`**

```
  cartItem, currencyIsoCode)

```

Update an item in a cart of a specific currency.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItem updateCartItem(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String cartItemId, ConnectApi.CartItemInput

   cartItem, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemId
```

Type: String

ID of the cart item.


Apex Reference Guide CommerceCart Class

```
   cartItem
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing a cart item to update.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`updateCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId,`**

```
  cartItem, currencyIsoCode, includeCartData)

```

Update an item in a cart of a specific currency.

API Version

64.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItem updateCartItem(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String cartItemId, ConnectApi.CartItemInput

   cartItem, String currencyIsoCode, Boolean includeCartData)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.


Apex Reference Guide CommerceCart Class

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   cartItemId
```

Type: String

ID of the cart item.

```
   cartItem
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing a cart item to update.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

```
   currencyIsoCode
```

Type: String

Description

```
   includeCartData
```

Type: Boolean

Specifies whether to return a collection of cart items in the response ( `true` ) or not ( `false` ). If unspecified, the default value is
`false` . This parameter is supported for D2C stores with Faster Add-to-Cart disabled. The cart must also have fewer than 25 items.

Return Value

Type: `ConnectApi.CartItem`

Usage

Buyers with read access to carts can add, update, and delete items in carts.

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`upsertInventoryReservation(webstoreId, activeCartOrId, effectiveAccountId,`**

**`cartInventoryReservationInput)`** (Pilot)

Create or update an inventory reservation.

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on
the basis of generally available products and features. This feature is made available on an AS IS basis and use of this feature is at
your sole risk.

API Version

58.0


### Apex Reference Guide CommerceCatalog Class

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartInventoryReservationOutputRepresentation

   upsertInventoryReservation(String webstoreId, String activeCartOrId, String

   effectiveAccountId, ConnectApi.CartInventoryReservationInputRepresentation

   cartInventoryReservationInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   activeCartOrId
```

Type: String

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   cartInventoryReservationInput
```

Type: `ConnectApi.CartInventoryReservationInputRepresentation`

A `ConnectApi.CartInventoryReservationInputRepresentation` input class indicating the reservation duration.

Return Value

Type: `ConnectApi.CartInventoryReservationOutputRepresentation`

### CommerceCatalog Class

Get products, product categories, and product category paths.

Namespace

ConnectApi

#### CommerceCatalog Methods

### These methods are for CommerceCatalog . All methods are static.


Apex Reference Guide CommerceCatalog Class

IN THIS SECTION:

getCategoryMenuItems(webstoreId, includeImageUrl, addHomeMenuItem, publishStatus, effectiveAccountId, maxLevels, maxItems)
Retrieve product category menu items for the given parent item and store.

getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields, mediaGroups, excludeMedia, excludeEntitlementDetails,
excludePrimaryProductCategory)
Get a product.

getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields, mediaGroups, excludeMedia, excludeEntitlementDetails,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo)
Get a product with variation and attribute information.

getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields, mediaGroups, excludeMedia, excludeEntitlementDetails,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule)
Get a product with quantity rule information.

getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields, mediaGroups, excludeMedia, excludeEntitlementDetails,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule, excludeProductSellingModels)
Get detailed information for a product, optionally including information about its product selling models.

getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups, excludeFields, excludeMedia,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule, excludeProductSellingModels)
Get detailed information for a product without its entitlement information.

getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups, excludeFields, excludeMedia,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule, excludeProductSellingModels,
noCache)
Get detailed information for a product without its entitlement information.

getProductCategory(webstoreId, productCategoryId, effectiveAccountId, fields, excludeFields, mediaGroups, excludeMedia)
Get a product category.

getProductCategoryChildren(webstoreId, effectiveAccountId, parentProductCategoryId, fields, excludeFields, mediaGroups,
excludeMedia)
Get product categories.

getProductCategoryPath(webstoreId, productCategoryId, effectiveAccountId)
Get the product category path from the root category to the current category.

getProductChildCollection(webstoreId, productId, effectiveAccountId, fields, mediaGroups, excludeFields, excludeMedia,
excludeAttributeSetInfo, excludeQuantityRule, pageToken, pageSize)
Get a collection of child products related to a parent product.

getProductChildCollection(webstoreId, productId, effectiveAccountId, fields, mediaGroups, excludeFields, excludeMedia,
excludeAttributeSetInfo, excludeQuantityRule, includeProductSellingModels, includeRequiredChildrenOnly,
excludeDynamicAttributeInfo, pageToken, pageSize, noCache)
Get a collection of child products related to a parent product.

getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia, excludePrices)
Get fields, prices, and default images for a list of products.

getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia)
Get fields and default images for a list of products.


Apex Reference Guide CommerceCatalog Class

getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia, includeQuantityRule, includeProductSellingModels,
includeAttributeSetInfo, includeGroupByAttributeVariationInfo)
Get fields and default images for a list of products.

getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia, includeQuantityRule, includeProductSellingModels,
includeAttributeSetInfo, includeGroupByAttributeVariationInfo, noCache)
Get fields and default images for a list of products.

##### **`getCategoryMenuItems(webstoreId, includeImageUrl, addHomeMenuItem,`**

```
  publishStatus, effectiveAccountId, maxLevels, maxItems)

```

Retrieve product category menu items for the given parent item and store.

API Version

64.0

Available to Guest Users

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.NavigationMenuItemCollection getCategoryMenuItems(String

   webstoreId, Boolean includeImageUrl, Boolean addHomeMenuItem, String publishStatus,

   String effectiveAccountId, Integer maxLevels, Integer maxItems)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   addHomeMenuItem
```

Type: Boolean

Indicates if a home menu item should be included. The default value is false.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   includeImageUrl
```

Type: Boolean

Indicates if the image URL should be included for root items.


Apex Reference Guide CommerceCatalog Class

```
   maxItems
```

Type: Integer

Maximum number of category items to be retrieved.

```
   maxLevels
```

Type: Integer

Maximum number of hierarchical levels to be retrieved.

```
   publishStatus
```

Type: String

Publish status of the storefront.

Return Value

Type: ConnectApi.NavigationMenuItemCollection on page 2423

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields,`**

```
  mediaGroups, excludeMedia, excludeEntitlementDetails,

  excludePrimaryProductCategory)

```

Get a product.

API Version

49.0

Supported in API versions 49.0 to 63.0.

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, Boolean excludeFields, List<String>

   mediaGroups, Boolean excludeMedia, Boolean excludeEntitlementDetails, Boolean

   excludePrimaryProductCategory)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String


Apex Reference Guide CommerceCatalog Class

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeEntitlementDetails
```

Type: Boolean

Specifies whether the entitlement details of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields,`**

```
  mediaGroups, excludeMedia, excludeEntitlementDetails,

  excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo)

```

Get a product with variation and attribute information.


Apex Reference Guide CommerceCatalog Class

API Version

50.0

Supported in API versions 50.0 to 63.0.

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, Boolean excludeFields, List<String>

   mediaGroups, Boolean excludeMedia, Boolean excludeEntitlementDetails, Boolean

   excludePrimaryProductCategory, Boolean excludeVariationInfo, Boolean

   excludeAttributeSetInfo)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.


Apex Reference Guide CommerceCatalog Class

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeEntitlementDetails
```

Type: Boolean

Specifies whether the entitlement details of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeVariationInfo
```

Type: Boolean

Specifies whether the variation information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields,`**

```
  mediaGroups, excludeMedia, excludeEntitlementDetails,

  excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo,

  excludeQuantityRule)

```

Get a product with quantity rule information.

API Version

52.0

Supported in API versions 52.0 to 63.0.

Available to Guest Users

52.0

Requires Chatter

No


Apex Reference Guide CommerceCatalog Class

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, Boolean excludeFields, List<String>

   mediaGroups, Boolean excludeMedia, Boolean excludeEntitlementDetails, Boolean

   excludePrimaryProductCategory, Boolean excludeVariationInfo, Boolean

   excludeAttributeSetInfo, Boolean excludeQuantityRule)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeEntitlementDetails
```

Type: Boolean

Specifies whether the entitlement details of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .


Apex Reference Guide CommerceCatalog Class

```
   excludeVariationInfo
```

Type: Boolean

Specifies whether the variation information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields,`**

```
  mediaGroups, excludeMedia, excludeEntitlementDetails,

  excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo,

  excludeQuantityRule, excludeProductSellingModels)

```

Get detailed information for a product, optionally including information about its product selling models.

API Version

56.0

Supported in API versions 56.0 to 63.0.

Available to Guest Users

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, Boolean excludeFields, List<String>

   mediaGroups, Boolean excludeMedia, Boolean excludeEntitlementDetails, Boolean

   excludePrimaryProductCategory, Boolean excludeVariationInfo, Boolean

   excludeAttributeSetInfo, Boolean excludeQuantityRule, Boolean

   excludeProductSellingModels)

```


Apex Reference Guide CommerceCatalog Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeEntitlementDetails
```

Type: Boolean

Specifies whether the entitlement details of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeVariationInfo
```

Type: Boolean

Specifies whether the variation information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .


Apex Reference Guide CommerceCatalog Class

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeProductSellingModels
```

Type: Boolean

Specifies whether product selling models are returned or not. The behavior of this parameter depends on whether you turn on the
CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit the parameter),
product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling models are not
returned. If the permission is off, product selling models are not returned, regardless of whether you omit the parameter or provide
a value.

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups,`**

```
  excludeFields, excludeMedia, excludePrimaryProductCategory,

  excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule,

  excludeProductSellingModels)

```

Get detailed information for a product without its entitlement information.

API Version

57.0

Supported in API versions 57.0 to 64.0.

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, List<String> mediaGroups, Boolean

   excludeFields, Boolean excludeMedia, Boolean excludePrimaryProductCategory, Boolean

   excludeVariationInfo, Boolean excludeAttributeSetInfo, Boolean excludeQuantityRule,

   Boolean excludeProductSellingModels)

```


Apex Reference Guide CommerceCatalog Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeVariationInfo
```

Type: Boolean

Specifies whether the variation information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .


Apex Reference Guide CommerceCatalog Class

```
   excludeProductSellingModels
```

Type: Boolean

Specifies whether product selling models are returned or not. The behavior of this parameter depends on whether you turn on the
CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit the parameter),
product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling models are not
returned. If the permission is off, product selling models are not returned, regardless of whether you omit the parameter or provide
a value.

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups,`**

```
  excludeFields, excludeMedia, excludePrimaryProductCategory,

  excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule,

  excludeProductSellingModels, noCache)

```

Get detailed information for a product without its entitlement information.

API Version

64.0

Available to Guest Users

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, List<String> mediaGroups, Boolean

   excludeFields, Boolean excludeMedia, Boolean excludePrimaryProductCategory, Boolean

   excludeVariationInfo, Boolean excludeAttributeSetInfo, Boolean excludeQuantityRule,

   Boolean excludeProductSellingModels, String noCache)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceCatalog Class

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludePrimaryProductCategory
```

Type: Boolean

Specifies whether the primary category path of the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeVariationInfo
```

Type: Boolean

Specifies whether the variation information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeProductSellingModels
```

Type: Boolean

Specifies whether product selling models are returned or not. The behavior of this parameter depends on whether you turn on the
CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit the parameter),
product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling models are not


Apex Reference Guide CommerceCatalog Class

returned. If the permission is off, product selling models are not returned, regardless of whether you omit the parameter or provide
a value.

```
   noCache
```

Type: String

Specifies whether to ignore cached data and return the latest response ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProductCategory(webstoreId, productCategoryId, effectiveAccountId, fields,`**

```
  excludeFields, mediaGroups, excludeMedia)

```

Get a product category.

API Version

49.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCategoryDetail getProductCategory(String webstoreId,

   String productCategoryId, String effectiveAccountId, List<String> fields, Boolean

   excludeFields, List<String> mediaGroups, Boolean excludeMedia)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productCategoryId
```

Type: String

ID of the product category.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.


Apex Reference Guide CommerceCatalog Class

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

Return Value

Type: `ConnectApi.ProductCategoryDetail`

##### **`getProductCategoryChildren(webstoreId, effectiveAccountId,`**

```
  parentProductCategoryId, fields, excludeFields, mediaGroups, excludeMedia)

```

Get product categories.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCategoryDetailCollection

   getProductCategoryChildren(String webstoreId, String effectiveAccountId, String

   parentProductCategoryId, List<String> fields, Boolean excludeFields, List<String>

   mediaGroups, Boolean excludeMedia)

```


Apex Reference Guide CommerceCatalog Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   parentProductCategoryId
```

Type: String

ID of the product category for which you want to get all the children product categories. If `null`, returns all the top-level product
categories for the store.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is unspecified, all fields are returned. There is no limit to the number of fields you can specify. The number of fields and
number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records.

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

Return Value

Type: `ConnectApi.ProductCategoryDetailCollection`

##### **`getProductCategoryPath(webstoreId, productCategoryId, effectiveAccountId)`**

Get the product category path from the root category to the current category.

API Version

49.0


Apex Reference Guide CommerceCatalog Class

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCategoryPath getProductCategoryPath(String webstoreId,

   String productCategoryId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productCategoryId
```

Type: String

ID of the product category.

```
   effectiveAccountId
```

Type: String

If `null`, the default value is determined from context.ID of the buyer account or guest buyer profile for which the request is made.
If unspecified, the default value is determined from context. This field is available in API version 65.0 and later.

Return Value

Type: `ConnectApi.ProductCategoryPath`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`getProductChildCollection(webstoreId, productId, effectiveAccountId, fields,`**

```
  mediaGroups, excludeFields, excludeMedia, excludeAttributeSetInfo,

  excludeQuantityRule, pageToken, pageSize)

```

Get a collection of child products related to a parent product.

API Version

57.0

Available to Guest Users

57.0


Apex Reference Guide CommerceCatalog Class

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductChildCollection getProductChildCollection(String

   webstoreId, String productId, String effectiveAccountId, List<String> fields,

   List<String> mediaGroups, Boolean excludeFields, Boolean excludeMedia, Boolean

   excludeAttributeSetInfo, Boolean excludeQuantityRule, String pageToken, Integer pageSize)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is empty or unspecified, all fields are returned. There’s no limit to the number of fields you can specify. The number of fields
and number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records. Possible values:

**•** `Attachment`

**•** `productDetailImage`

**•** `productListImage`

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

For product bundles, only the `producListImage` is returned.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeMedia
```

Type: Boolean


Apex Reference Guide CommerceCatalog Class

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 20.

Return Value

Type: `ConnectApi.ProductChildCollection`

##### **`getProductChildCollection(webstoreId, productId, effectiveAccountId, fields,`**

```
  mediaGroups, excludeFields, excludeMedia, excludeAttributeSetInfo,

  excludeQuantityRule, includeProductSellingModels, includeRequiredChildrenOnly,

  excludeDynamicAttributeInfo, pageToken, pageSize, noCache)

```

Get a collection of child products related to a parent product.

API Version

66.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductChildCollection getProductChildCollection(String

   webstoreId, String productId, String effectiveAccountId, List<String> fields,

   List<String> mediaGroups, Boolean excludeFields, Boolean excludeMedia, Boolean

   excludeAttributeSetInfo, Boolean excludeQuantityRule, Boolean

   includeProductSellingModels, Boolean includeRequiredChildrenOnly, Boolean

   excludeDynamicAttributeInfo, String pageToken, Integer pageSize, String noCache)

```


Apex Reference Guide CommerceCatalog Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   fields
```

Type: List<String>

Comma-separated list of field names.

If this list is empty or unspecified, all fields are returned. There’s no limit to the number of fields you can specify. The number of fields
and number of characters in the field name may affect the URL size limit. If `excludeFields` and `fields` are specified, the
`excludeFields` parameter takes precedence.

```
   mediaGroups
```

Type: List<String>

Comma-separated list of developer names of media group records. Possible values:

**•** `Attachment`

**•** `productDetailImage`

**•** `productListImage`

If this list is empty or unspecified, all media groups are returned. If `excludeMedia` and `mediaGroups` are specified, the
`excludeMedia` parameter takes precedence.

For product bundles, only the `producListImage` is returned.

```
   excludeFields
```

Type: Boolean

Specifies whether the fields are returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   excludeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   excludeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   includeProductSellingModels
```

Type: Boolean


Apex Reference Guide CommerceCatalog Class

Specifies whether product selling models are returned or not. The behavior of this parameter depends on whether you turn on the
CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit the parameter),
product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling models are not
returned. If the permission is off, product selling models are not returned, regardless of whether you omit the parameter or provide
a value.

```
   includeRequiredChildrenOnly
```

Type: Boolean

Specifies whether to include only the required children for the product ( `true` ) or not ( `false` ). If unspecified, defaults to `true` .

```
   excludeDynamicAttributeInfo
```

Type: Boolean

Specifies whether to exclue the dynamic attribute information for the product ( `true` ) or not ( `false` ). If unspecified, defaults to
`true` .

```
   pageToken
```

Type: String

Specifies the base64 encoded page token. Page tokens are returned as part of the response. If unspecified, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 20.

```
   noCache
```

Type: String

Specifies whether to ignore cached data and return the latest response ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.ProductChildCollection`

##### **`getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia,`**

```
   excludePrices)

```

Get fields, prices, and default images for a list of products.

API Version

54.0

Supported in API versions 54.0 to 63.0.

Available to Guest Users

54.0

Requires Chatter

No


Apex Reference Guide CommerceCatalog Class

Signature

```
   public static ConnectApi.ProductOverviewCollection getProducts(String webstoreId, String

   effectiveAccountId, List<String> ids, List<String> skus, List<String> fields, Boolean

   excludeMedia, Boolean excludePrices)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   ids
```

Type: List<String>

List of product IDs. Specify either a list of up to 20 product IDs or SKUs, but not both.

```
   skus
```

Type: List<String>

List of SKUs. Specify either a list of up to 20 SKUs or product IDs, but not both.

```
   fields
```

Type: List<String>

Comma-separated list of field names to return for each product. If the list is empty or not specified, all fields are returned. You can
specify any number of fields.

```
   excludeMedia
```

Type: Boolean

Specifies whether default images are returned for the products ( `false` ) or not ( `true` ). The default is `false` .

```
   excludePrices
```

Type: Boolean

Specifies whether prices are returned for the products ( `false` ) or not ( `true` ). The default is `false` .

Note: In version 58.0 and later, prices aren’t returned for products regardless of this parameter. To get pricing information for
products in version 58.0 and later, use the CommerceStorePricing Class.

Return Value

Type: `ConnectApi.ProductOverviewCollection`

##### **`getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia)`**

Get fields and default images for a list of products.

API Version

58.0


Apex Reference Guide CommerceCatalog Class

Supported in API versions 58.0 to 62.0.

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductOverviewCollection getProducts(String webstoreId, String

   effectiveAccountId, List<String> ids, List<String> skus, List<String> fields, Boolean

   excludeMedia)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   ids
```

Type: List<String>

List of product IDs. Specify either a list of up to 20 product IDs or SKUs, but not both.

```
   skus
```

Type: List<String>

List of SKUs. Specify either a list of up to 20 SKUs or product IDs, but not both.

```
   fields
```

Type: List<String>

Comma-separated list of field names to return for each product. If the list is empty or not specified, all fields are returned. You can
specify any number of fields.

```
   excludeMedia
```

Type: Boolean

Specifies whether default images are returnedSpecifies whether the media groups and default images of the product are returned
( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.ProductOverviewCollection`


Apex Reference Guide CommerceCatalog Class

##### **`getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia,`**

```
  includeQuantityRule, includeProductSellingModels, includeAttributeSetInfo,

  includeGroupByAttributeVariationInfo)

```

Get fields and default images for a list of products.

API Version

63.0

Supported in API versions 63.0 to 64.0.

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductOverviewCollection getProducts(String webstoreId, String

   effectiveAccountId, List<String> ids, List<String> skus, List<String> fields, Boolean

   excludeMedia, Boolean includeQuantityRule, Boolean includeProductSellingModels, Boolean

   includeAttributeSetInfo, Boolean includeGroupByAttributeVariationInfo)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   ids
```

Type: List<String>

List of product IDs. Specify either a list of up to 20 product IDs or SKUs, but not both.

```
   skus
```

Type: List<String>

List of skus. Specify either a list of up to 20 SKUs or product IDs, but not both.

```
   fields
```

Type: List<String>

Comma-separated list of field names to return for each product. If the list is empty or not specified, all fields are returned. You can
specify any number of fields.

```
   excludeMedia
```

Type: Boolean


Apex Reference Guide CommerceCatalog Class

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   includeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   includeProductSellingModels
```

Type: Boolean

Specifies whether product selling models are returned ( `true` ) or not ( `false` ). The behavior of this parameter depends on whether
you turn on the CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit
the parameter), product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling
models are not returned. If the permission is off, product selling models are not returned, regardless of whether you omit the
parameter or provide a value.

```
   includeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

```
   includeGroupByAttributeVariationInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

Return Value

Type: `ConnectApi.ProductOverviewCollection`

##### **`getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia,`**

```
  includeQuantityRule, includeProductSellingModels, includeAttributeSetInfo,

  includeGroupByAttributeVariationInfo, noCache)

```

Get fields and default images for a list of products.

API Version

64.0

Available to Guest Users

64.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductOverviewCollection getProducts(String webstoreId, String

   effectiveAccountId, List<String> ids, List<String> skus, List<String> fields, Boolean

   excludeMedia, Boolean includeQuantityRule, Boolean includeProductSellingModels, Boolean

   includeAttributeSetInfo, Boolean includeGroupByAttributeVariationInfo, String noCache)

```


Apex Reference Guide CommerceCatalog Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made.

```
   ids
```

Type: List<String>

List of product IDs. Specify either a list of up to 20 product IDs or SKUs, but not both.

```
   skus
```

Type: List<String>

List of skus. Specify either a list of up to 20 SKUs or product IDs, but not both.

```
   fields
```

Type: List<String>

Comma-separated list of field names to return for each product. If the list is empty or not specified, all fields are returned. You can
specify any number of fields.

```
   excludeMedia
```

Type: Boolean

Specifies whether the media groups and default images of the product are returned ( `false` ) or not ( `true` ). If unspecified, defaults
to `false` .

```
   includeQuantityRule
```

Type: Boolean

Specifies whether the quantity rule information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to `false` .

```
   includeProductSellingModels
```

Type: Boolean

Specifies whether product selling models are returned ( `true` ) or not ( `false` ). The behavior of this parameter depends on whether
you turn on the CommerceSubscription permission. If the permission is on, and if you set the parameter to `false` (or if you omit
the parameter), product selling models are returned. If the permission is on, and if you set the parameter to `true`, product selling
models are not returned. If the permission is off, product selling models are not returned, regardless of whether you omit the
parameter or provide a value.

```
   includeAttributeSetInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

```
   includeGroupByAttributeVariationInfo
```

Type: Boolean

Specifies whether the attribute set information for the product is returned ( `true` ) or not ( `false` ). If unspecified, defaults to `false` .

```
   noCache
```

Type: String

Specifies whether to ignore cached data and return the latest response ( `true` ) or not ( `false` ).


### Apex Reference Guide CommerceCatalogManagement Class

Return Value

Type: `ConnectApi.ProductOverviewCollection`

### CommerceCatalogManagement Class

Create or update a composite product. Create a variation product.

Namespace

ConnectApi

#### CommerceCatalogManagement Methods

### These methods are for CommerceCatalogManagement . All methods are static.

##### **`compositeCommerceProductCreate(webstoreId,`**

```
  compositeCommerceProductInputRepresentation)

```

Create a composite product.

API Version

61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CompositeCommerceProductOutputRepresentation

   compositeCommerceProductCreate(String webstoreId,

   ConnectApi.CompositeCommerceProductInputRepresentation

   compositeCommerceProductInputRepresentation)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   compositeCommerceProductInputRepresentation
```

Type: `ConnectApi.CompositeCommerceProductInputRepresentation`

Details used to create the composite product.

Return Value

Type: `ConnectApi.CompositeCommerceProductOutputRepresentation`


Apex Reference Guide CommerceCatalogManagement Class

##### **`compositeCommerceProductUpdate(webstoreId, productId,`**

```
  compositeCommerceProductInputRepresentation)

```

Update a composite product.

API Version

61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CompositeCommerceProductOutputRepresentation

   compositeCommerceProductUpdate(String webstoreId, String productId,

   ConnectApi.CompositeCommerceProductInputRepresentation

   compositeCommerceProductInputRepresentation)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the composite product.

```
   compositeCommerceProductInputRepresentation
```

Type: `ConnectApi.CompositeCommerceProductInputRepresentation`

Details used to update the composite product.

Return Value

Type: `ConnectApi.CompositeCommerceProductOutputRepresentation`

##### **`compositeCommerceVariationCreate(webstoreId,`**

```
  compositeCommerceVariationInputRepresentation)

```

Create a variation product.

API Version

62.0

Requires Chatter

No


### Apex Reference Guide CommercePromotions Class

Signature

```
   public static ConnectApi.CompositeCommerceVariationOutputRepresentation

   compositeCommerceVariationCreate(String webstoreId,

   ConnectApi.CompositeCommerceVariationInputRepresentation

   compositeCommerceVariationInputRepresentation)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   compositeCommerceVariationInputRepresentation
```

Type: `ConnectApi.CompositeCommerceVariationInputRepresentation`

Details used to create the variation product.

Return Value

Type: `ConnectApi.CompositeCommerceVariationOutputRepresentation`

### CommercePromotions Class

Evaluate promotions for Commerce orders. Get coupon code redemption usage.

Namespace

ConnectApi

#### CommercePromotions Methods

### These methods are for CommercePromotions . All methods are static. Note: Don’t write an Apex test that calls these CommercePromotions APIs within the context of a guest.

IN THIS SECTION:

decreaseRedemption(couponCodeRedemption)
Get coupon code redemption usage to revert a previously redeemed coupon code.

evaluate(salesTransaction)
Determine which promotions the customer is eligible for based on the store and buyer group, and compute the applicable price
adjustments based on the coupons and the items in the cart. This API evaluates only the first 50 active manual promotions and first
50 active automatic promotions, based on priority. This API computes and returns applicable price adjustments, but it does not apply
those adjustments to the webcart record. If you want to enable promotions based on shipping, contact Salesforce Customer Support.

increaseRedemption(couponCodeRedemption)
Get coupon code redemption addition (increase) usage.


Apex Reference Guide CommercePromotions Class

##### **`decreaseRedemption(couponCodeRedemption)`**

Get coupon code redemption usage to revert a previously redeemed coupon code.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CouponCodeRedemptionCollection

   decreaseRedemption(ConnectApi.CouponCodeRedemptionInput couponCodeRedemption)

```

Parameters

```
   couponCodeRedemption
```

Type: `ConnectApi.CouponCodeRedemptionInput on page 2028`

Tracks each coupon code redemption.

Return Value

Type: `ConnectApi.CouponCodeRedemptionCollection on page 2282`

##### **`evaluate(salesTransaction)`**

Determine which promotions the customer is eligible for based on the store and buyer group, and compute the applicable price
adjustments based on the coupons and the items in the cart. This API evaluates only the first 50 active manual promotions and first 50
active automatic promotions, based on priority. This API computes and returns applicable price adjustments, but it does not apply those
adjustments to the webcart record. If you want to enable promotions based on shipping, contact Salesforce Customer Support.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No


### Apex Reference Guide CommerceSearch Class

Signature

```
   global static ConnectApi.PromotionEvaluation evaluate(ConnectApi.PromotionEvaluateInput

   salesTransaction)

```

Parameters

```
   salesTransaction
```

Type: `ConnectApi.PromotionEvaluateInput`

Find promotions that the customer is eligible for and compute their discounts.

Return Value

Type: `ConnectApi.PromotionEvaluation`

##### **`increaseRedemption(couponCodeRedemption)`**

Get coupon code redemption addition (increase) usage.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CouponCodeRedemptionCollection

   increaseRedemption(ConnectApi.CouponCodeRedemptionInput couponCodeRedemption)

```

Parameters

```
   couponCodeRedemption
```

Type: `ConnectApi.CouponCodeRedemptionInput on page 2028`

Tracks each coupon code redemption.

Return Value

Type: `ConnectApi.CouponCodeRedemptionCollection on page 2282`

### CommerceSearch Class

Get sort rules for the live search index. Get product search suggestions. Search products.


Apex Reference Guide CommerceSearch Class

Namespace

ConnectApi

#### CommerceSearch Methods These methods are for CommerceSearch . All methods are static.

IN THIS SECTION:

##### getSortRules(webstoreId)

Get sort rules for the live index.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults)
Get suggestions for product searches.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults, includeSuggestedProducts, maxSuggestedProducts)
Get suggestions for product searches.

searchProducts(webstoreId, effectiveAccountId, productSearchInput)
Search products.

##### **`getSortRules(webstoreId)`**

Get sort rules for the live index.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SortRulesCollection getSortRules(String webstoreId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

Return Value

Type: `ConnectApi.SortRulesCollection`


Apex Reference Guide CommerceSearch Class

##### **`getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults)`**

Get suggestions for product searches.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchSuggestionsResults getSuggestions(String

   webstoreId, String effectiveAccountId, String searchTerm, Integer maxResults)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   searchTerm
```

Type: String

Search term with up to 100 characters. If specified, the service returns autocomplete suggestions from the user’s recent searches. If
unspecified, the service returns suggestions from the user’s recent searches.

```
   maxResults
```

Type: Integer

Maximum number of suggestions. Values are from 1 through 10. If unspecified, defaults to 10.

Return Value

Type: `ConnectApi.ProductSearchSuggestionsResults`

##### **`getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults,`**

```
  includeSuggestedProducts, maxSuggestedProducts)

```

Get suggestions for product searches.


Apex Reference Guide CommerceSearch Class

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchSuggestionsResults getSuggestions(String

   webstoreId, String effectiveAccountId, String searchTerm, Integer maxResults, Boolean

   includeSuggestedProducts, Integer maxSuggestedProducts)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   searchTerm
```

Type: String

Search term with up to 100 characters. If specified, the service returns autocomplete suggestions from the user’s recent searches. If
unspecified, the service returns suggestions from the user’s recent searches.

```
   maxResults
```

Type: Integer

Maximum number of suggestions. Values are from 1 through 10. If unspecified, defaults to 10.

```
   includeSuggestedProducts
```

Type: Boolean

Specifies whether a search term returns product suggestions ( `true` ) or not ( `false` ). If unspecified, defaults to `false` . If `true`,
the service returns the suggested product IDs.

```
   maxSuggestedProducts
```

Type: String

Maximum number of product suggestions. Values are from 1 through 10. If unspecified, defaults to 6.

Return Value

Type: `ConnectApi.ProductSearchSuggestionsResults`


### Apex Reference Guide CommerceSearchConnectFamily Class

##### **`searchProducts(webstoreId, effectiveAccountId, productSearchInput)`**

Search products.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchResults searchProducts(String webstoreId, String

   effectiveAccountId, ConnectApi.ProductSearchInput productSearchInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   productSearchInput
```

Type: `ConnectApi.ProductSearchInput`

A `ConnectApi.ProductSearchInput` body with either a category ID or search terms.

Return Value

Type: `ConnectApi.ProductSearchResults`

Usage

Searching products respects buyer View Product entitlements and only users entitled to view product data can access this resource.

### CommerceSearchConnectFamily Class

Search products by search term or category in a webstore.

Namespace

ConnectApi


Apex Reference Guide CommerceSearchConnectFamily Class

#### CommerceSearchConnectFamily Methods These methods are for CommerceSearchConnectFamily . All methods are static.

IN THIS SECTION:

##### searchProducts(webstoreId, searchTerm, categoryId, sortRuleId, grouping, fields, refinements, pageParam, pageSize, effectiveAccountId,

includeQuantityRule)
Search products by search term or category in a webstore.

##### **`searchProducts(webstoreId, searchTerm, categoryId, sortRuleId, grouping,`**

```
  fields, refinements, pageParam, pageSize, effectiveAccountId,

  includeQuantityRule)

```

Search products by search term or category in a webstore.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceProductSearchResults searchProducts(String webstoreId,

   String searchTerm, String categoryId, String sortRuleId, String grouping, List<String>

   fields, String refinements, Integer pageParam, Integer pageSize, String

   effectiveAccountId, Boolean includeQuantityRule)

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

List of up to 32 space-separated search terms.

```
   categoryId
```

Type: String

Category ID returns results for products in this category or its subcategories.

```
   sortRuleId
```

Type: String


### Apex Reference Guide CommerceSearchSettings Class

ID of the sort rule that specifies the order of products in the search results. If unspecified, the default sort type is relevancy.

```
   grouping
```

Type: String

Grouping option for search results. If unspecified, the default is the value specified in **Search**       - **Results Display Settings**       - **Results**
**Grouping** .

```
   fields
```

Type: List<String>

Product fields to return in search results. Search results include fields you have access to.

```
   refinements
```

Type: String

List up to nine refinements (facets) for search results. Buyers or shoppers can select up to 20 values for each refinement. The
`refinements` parameter is encoded as a Base64 string from the JSON representation of ConnectApi.DistinctValueRefinementInput
.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 200. If unspecified, defaults to 20.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   includeQuantityRule
```

Type: Boolean

Specifies whether to include purchase quantity rule information for products in search results ( `true` ) or not ( `false` ). If unspecified,
defaults to `false` .

Return Value

Type: `ConnectApi.CommerceProductSearchResults`

Usage

Searching products respects buyer View Product entitlements and only users entitled to view product data can access this resource.

### CommerceSearchSettings Class

Get indexes. Get index logs. Create an index of a product catalog.

Namespace

ConnectApi


Apex Reference Guide CommerceSearchSettings Class

#### CommerceSearchSettings Methods These methods are for CommerceSearchSettings . All methods are static.

IN THIS SECTION:

##### createCommerceSearchIndex(webstoreId, indexBuildType)

Create an index of a product catalog.

getCommerceSearchIndex(webstoreId, indexId)
Get a Commerce search index.

getCommerceSearchIndexes(webstoreId)
Get Commerce search indexes.

getCommerceSearchIndexLogs(webstoreId)
Get Commerce search index logs.

##### **`createCommerceSearchIndex(webstoreId, indexBuildType)`**

Create an index of a product catalog.

API Version

57.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommerceSearchIndex createCommerceSearchIndex(String webstoreId,

   String indexBuildType)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   indexBuildType
```

Type: `ConnectApi.CommerceSearchIndexBuildType`

Build type of the index. Values are:

**•** `Full`

**•** `Incremental`

Return Value

Type: `ConnectApi.CommerceSearchIndex`


Apex Reference Guide CommerceSearchSettings Class

Usage

This method creates a live index that replaces the current live index. Any indexes that are in progress are removed when you manually
create an index with this method.

##### **`getCommerceSearchIndex(webstoreId, indexId)`**

Get a Commerce search index.

API Version

52.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommerceSearchIndex getSingleCommerceSearchIndex(String

   webstoreId, String indexId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   indexId
```

Type: String

ID of the index.

Return Value

Type: `ConnectApi.CommerceSearchIndex`

##### **`getCommerceSearchIndexes(webstoreId)`**

Get Commerce search indexes.

API Version

52.0

Requires Chatter

Yes


### Apex Reference Guide CommerceStorePricing Class

Signature

```
   public static ConnectApi.CommerceSearchIndexCollection getCommerceSearchIndexes(String

   webstoreId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

Return Value

Type: `ConnectApi.CommerceSearchIndexCollection`

##### **`getCommerceSearchIndexLogs(webstoreId)`**

Get Commerce search index logs.

API Version

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceSearchIndexLogCollection

   getCommerceSearchIndexLogs(String webstoreId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

Return Value

Type: `ConnectApi.CommerceSearchIndexLogCollection`

### CommerceStorePricing Class

Get product prices.

Namespace

ConnectApi


Apex Reference Guide CommerceStorePricing Class

#### CommerceStorePricing Methods These methods are for CommerceStorePricing . All methods are static.

IN THIS SECTION:

##### getProductPrice(webstoreId, productId, effectiveAccountId)

Get the list and buyer price for a product.

getProductPrice(webstoreId, productId, effectiveAccountId, productSellingModelIds)
Get a product’s list and buyer price for specified product selling models.

getProductPrices(webstoreId, effectiveAccountId, productIds)
Get the prices for multiple products using multiple product IDs.

getProductPrices(webstoreId, effectiveAccountId, productIds, currencyIsoCode)
Get the prices for multiple products using multiple product IDs and a currency ISO code.

getProductPrices(webstoreId, effectiveAccountId, pricingInput)
Get the prices for multiple products.

getProductPrices(webstoreId, effectiveAccountId, pricingInput, currencyIsoCode)
Get the prices for multiple products using a currency ISO code.

##### **`getProductPrice(webstoreId, productId, effectiveAccountId)`**

Get the list and buyer price for a product.

API Version

49.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductPrice getProductPrice(String webstoreId, String

   productId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String


Apex Reference Guide CommerceStorePricing Class

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made.

Return Value

Type: `ConnectApi.ProductPrice`

Usage

This method respects buyer entitlements and only users entitled to view product and price data can access it.

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.

##### **`getProductPrice(webstoreId, productId, effectiveAccountId,`**

```
  productSellingModelIds)

```

Get a product’s list and buyer price for specified product selling models.

API Version

56.0

Available to Guest Users

56.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductPrice getProductPrice(String webstoreId, String

   productId, String effectiveAccountId, List<String> productSellingModelIds)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   productId
```

Type: String

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made.


Apex Reference Guide CommerceStorePricing Class

```
   productSellingModelIds
```

Type: List<String>

List of product selling model IDs for the product.

Return Value

Type: `ConnectApi.ProductPrice`

##### **`getProductPrices(webstoreId, effectiveAccountId, productIds)`**

Get the prices for multiple products using multiple product IDs.

API Version

54.0

Available to Guest Users

54.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PricingResult getProductPrices(String webstoreId, String

   effectiveAccountId, List<String> productIds)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   productIds
```

Type: List<String>

List of product IDs for which you want to get prices.

Return Value

Type: `ConnectApi.PricingResult`

Usage

This method respects buyer entitlements and only users entitled to view product and price data can access it.


Apex Reference Guide CommerceStorePricing Class

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.

##### **`getProductPrices(webstoreId, effectiveAccountId, productIds, currencyIsoCode)`**

Get the prices for multiple products using multiple product IDs and a currency ISO code.

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PricingResult getProductPrices(String webstoreId, String

   effectiveAccountId, List<String> productIds, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   productIds
```

Type: List<String>

List of product IDs for which you want to get prices.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the products.

Return Value

Type: `ConnectApi.PricingResult`

Usage

This method respects buyer entitlements and only users entitled to view product and price data can access it.

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.


Apex Reference Guide CommerceStorePricing Class

##### **`getProductPrices(webstoreId, effectiveAccountId, pricingInput)`**

Get the prices for multiple products.

API Version

49.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PricingResult getProductPrices(String webstoreId, String

   effectiveAccountId, ConnectApi.PricingInput pricingInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   pricingInput
```

Type: `ConnectApi.PricingInput`

A `ConnectApi.PricingInput` body with the list of line items to price.

Return Value

Type: `ConnectApi.PricingResult`

Usage

This method respects buyer entitlements and only users entitled to view product and price data can access it.

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.

##### **`getProductPrices(webstoreId, effectiveAccountId, pricingInput,`**

```
  currencyIsoCode)

```

Get the prices for multiple products using a currency ISO code.


### Apex Reference Guide CommerceWishlist Class

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PricingResult getProductPrices(String webstoreId, String

   effectiveAccountId, ConnectApi.PricingInput pricingInput, String currencyIsoCode)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made. If `null`, the default value is determined from context.

```
   pricingInput
```

Type: `ConnectApi.PricingInput`

A `ConnectApi.PricingInput` body with the list of line items to price.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the products.

Return Value

Type: `ConnectApi.PricingResult`

Usage

This method respects buyer entitlements and only users entitled to view product and price data can access it.

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.

### CommerceWishlist Class

Get, create, update, and delete wishlists. Add wishlists to carts. Get wishlist items, add items to wishlists, and delete wishlist items.


Apex Reference Guide CommerceWishlist Class

Namespace

ConnectApi

#### CommerceWishlist Methods These methods are for CommerceWishlist . All methods are static.

IN THIS SECTION:

addItemToWishlist(webstoreId, wishlistId, wishlistItemInput)
Add an item to a wishlist for the context user.

addItemToWishlist(webstoreId, effectiveAccountId, wishlistId, wishlistItemInput)
Add an item to a wishlist.

addWishlistToCart(webstoreId, wishlistId)
Add a wishlist to the active cart for the context user.

addWishlistToCart(webstoreId, wishlistId, effectiveAccountId)
Add a wishlist to the active cart.

addWishlistToCartWithCartId(webstoreId, wishlistId, cartId)
Add a wishlist to a cart.

addWishlistToCartWithCartId(webstoreId, wishlistId, cartId, effectiveAccountId)
Add a wishlist to a cart.

createWishlist(webstoreId, wishlistInput)
Create a wishlist for the context user.

createWishlist(webstoreId, effectiveAccountId, wishlistInput)
Create a wishlist.

deleteWishlist(webstoreId, wishlistId)
Delete a wishlist for the context user.

deleteWishlist(webstoreId, effectiveAccountId, wishlistId)
Delete a wishlist.

getWishlist(webstoreId, effectiveAccountId, wishlistId, productFields, sortItemsBy)
Get a wishlist with product fields sorted by items.

getWishlist(webstoreId, effectiveAccountId, wishlistId, productFields, pageSize, sortItemsBy)
Get a wishlist with product fields sorted by items with a specified number of items per page.

getWishlistItems(webstoreId, effectiveAccountId, wishlistId, productFields, pageParam, sortItemsBy)
Get a page of sorted wishlist items with product fields.

getWishlistItems(webstoreId, effectiveAccountId, wishlistId, productFields, pageParam, pageSize, sortItemsBy)
Get a page of specified size of sorted wishlist items with product fields.

getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList)
Get wishlist summaries.

getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList, productFields, sortItemsBy)
Get wishlist summaries with product fields sorted by items.


Apex Reference Guide CommerceWishlist Class

getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList, productFields, pageSize, sortItemsBy)
Get wishlist summaries with product fields sorted by items with a specified number of items per page.

removeWishlistItem(webstoreId, effectiveAccountId, wishlistId, wishlistItemId)
Remove an item from a wishlist.

updateWishlist(webstoreId, wishlistId, wishlistUpdateInput)
Update the name of a wishlist for the context user.

updateWishlist(webstoreId, effectiveAccountId, wishlistId, wishlistUpdateInput)
Update the name of a wishlist.

##### **`addItemToWishlist(webstoreId, wishlistId, wishlistItemInput)`**

Add an item to a wishlist for the context user.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistItem addItemToWishlist(String webstoreId, String

   wishlistId, ConnectApi.WishlistItemInput wishlistItemInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   wishlistItemInput
```

Type: `ConnectApi.WishlistItemInput`

A `ConnectApi.WishlistItemInput` body with the item to add to the wishlist.

Return Value

Type: `ConnectApi.WishlistItem`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.


Apex Reference Guide CommerceWishlist Class

##### **`addItemToWishlist(webstoreId, effectiveAccountId, wishlistId,`**

```
  wishlistItemInput)

```

Add an item to a wishlist.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistItem addItemToWishlist(String webstoreId, String

   effectiveAccountId, String wishlistId, ConnectApi.WishlistItemInput wishlistItemInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   wishlistItemInput
```

Type: `ConnectApi.WishlistItemInput`

A `ConnectApi.WishlistItemInput` body with the item to add to the wishlist.

Return Value

Type: `ConnectApi.WishlistItem`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addWishlistToCart(webstoreId, wishlistId)`**

Add a wishlist to the active cart for the context user.

API Version

49.0


Apex Reference Guide CommerceWishlist Class

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistToCartResult addWishlistToCart(String webstoreId,

   String wishlistId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

Return Value

Type: `ConnectApi.WishlistToCartResult`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addWishlistToCart(webstoreId, wishlistId, effectiveAccountId)`**

Add a wishlist to the active cart.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistToCartResult addWishlistToCart(String webstoreId,

   String wishlistId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceWishlist Class

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.WishlistToCartResult`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addWishlistToCartWithCartId(webstoreId, wishlistId, cartId)`**

Add a wishlist to a cart.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistToCartResult addWishlistToCartWithCartId(String

   webstoreId, String wishlistId, String cartId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   cartId
```

Type: String

ID of the cart. If `null`, wishlist items are added to the active cart.

Return Value

Type: `ConnectApi.WishlistToCartResult`


Apex Reference Guide CommerceWishlist Class

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`addWishlistToCartWithCartId(webstoreId, wishlistId, cartId,`**

```
  effectiveAccountId)

```

Add a wishlist to a cart.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistToCartResult addWishlistToCartWithCartId(String

   webstoreId, String wishlistId, String cartId, String effectiveAccountId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   cartId
```

Type: String

ID of the cart. If `null`, wishlist items are added to the active cart.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

Return Value

Type: `ConnectApi.WishlistToCartResult`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.

##### **`createWishlist(webstoreId, wishlistInput)`**

Create a wishlist for the context user.


Apex Reference Guide CommerceWishlist Class

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Wishlist createWishlist(String webstoreId,

   ConnectApi.WishlistInput wishlistInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistInput
```

Type: `ConnectApi.WishlistInput`

A `ConnectApi.WishlistInput` body that includes the wishlist name and items.

Return Value

Type: `ConnectApi.Wishlist`

##### **`createWishlist(webstoreId, effectiveAccountId, wishlistInput)`**

Create a wishlist.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Wishlist createWishlist(String webstoreId, String

   effectiveAccountId, ConnectApi.WishlistInput wishlistInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceWishlist Class

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistInput
```

Type: `ConnectApi.WishlistInput`

A `ConnectApi.WishlistInput` body that includes the wishlist name and items.

Return Value

Type: `ConnectApi.Wishlist`

##### **`deleteWishlist(webstoreId, wishlistId)`**

Delete a wishlist for the context user.

API Version

49.0

Requires Chatter

No

Signature

```
   public static Void deleteWishlist(String webstoreId, String wishlistId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

Return Value

Type: Void

##### **`deleteWishlist(webstoreId, effectiveAccountId, wishlistId)`**

Delete a wishlist.

API Version

51.0


Apex Reference Guide CommerceWishlist Class

Requires Chatter

No

Signature

```
   public static Void deleteWishlist(String webstoreId, String effectiveAccountId, String

   wishlistId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

Return Value

Type: Void

##### **`getWishlist(webstoreId, effectiveAccountId, wishlistId, productFields,`**

```
  sortItemsBy)

```

Get a wishlist with product fields sorted by items.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Wishlist getWishlist(String webstoreId, String

   effectiveAccountId, String wishlistId, String productFields,

   ConnectApi.WishlistItemSortOrder sortItemsBy)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceWishlist Class

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.Wishlist`

##### **`getWishlist(webstoreId, effectiveAccountId, wishlistId, productFields,`**

```
  pageSize, sortItemsBy)

```

Get a wishlist with product fields sorted by items with a specified number of items per page.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Wishlist getWishlist(String webstoreId, String

   effectiveAccountId, String wishlistId, String productFields, Integer pageSize,

   ConnectApi.WishlistItemSortOrder sortItemsBy)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.


Apex Reference Guide CommerceWishlist Class

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.Wishlist`

##### **`getWishlistItems(webstoreId, effectiveAccountId, wishlistId, productFields,`**

```
  pageParam, sortItemsBy)

```

Get a page of sorted wishlist items with product fields.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistItemCollection getWishlistItems(String webstoreId,

   String effectiveAccountId, String wishlistId, String productFields, String pageParam,

   ConnectApi.WishlistItemSortOrder sortItemsBy)

```


Apex Reference Guide CommerceWishlist Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

```
   pageParam
```

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.WishlistItemCollection`

##### **`getWishlistItems(webstoreId, effectiveAccountId, wishlistId, productFields,`**

```
  pageParam, pageSize, sortItemsBy)

```

Get a page of specified size of sorted wishlist items with product fields.

API Version

51.0

Requires Chatter

No


Apex Reference Guide CommerceWishlist Class

Signature

```
   public static ConnectApi.WishlistItemCollection getWishlistItems(String webstoreId,

   String effectiveAccountId, String wishlistId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.WishlistItemSortOrder sortItemsBy)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

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

Specifies the number of items per page. Valid values are from 1 through 200. If you pass in `null`, the default size is 25.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

Return Value

Type: `ConnectApi.WishlistItemCollection`

##### **`getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList)`**

Get wishlist summaries.


Apex Reference Guide CommerceWishlist Class

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistsSummary getWishlistSummaries(String webstoreId, String

   effectiveAccountId, Boolean includeDisplayedList)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   includeDisplayedList
```

Type: Boolean

Specifies whether to include the displayed list ( `true` ) or not ( `false` ). If `null`, defaults to `false` .

Return Value

Type: `ConnectApi.WishlistsSummary`

##### **`getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList,`**

```
  productFields, sortItemsBy)

```

Get wishlist summaries with product fields sorted by items.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistsSummary getWishlistSummaries(String webstoreId, String

   effectiveAccountId, Boolean includeDisplayedList, String productFields,

   ConnectApi.WishlistItemSortOrder sortItemsBy)

```


Apex Reference Guide CommerceWishlist Class

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   includeDisplayedList
```

Type: Boolean

Specifies whether to include the displayed list ( `true` ) or not ( `false` ).

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

If _`includeDisplayedList`_ is `false`, _`productFields`_ is ignored.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

If _`includeDisplayedList`_ is `false`, _`sortItemsBy`_ is ignored.

Return Value

Type: `ConnectApi.WishlistsSummary`

##### **`getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList,`**

```
  productFields, pageSize, sortItemsBy)

```

Get wishlist summaries with product fields sorted by items with a specified number of items per page.

API Version

51.0

Requires Chatter

No


Apex Reference Guide CommerceWishlist Class

Signature

```
   public static ConnectApi.WishlistsSummary getWishlistSummaries(String webstoreId, String

   effectiveAccountId, Boolean includeDisplayedList, Integer pageSize, String productFields,

   pageSize, ConnectApi.WishlistItemSortOrder sortItemsBy)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   includeDisplayedList
```

Type: Boolean

Specifies whether to include the displayed list ( `true` ) or not ( `false` ).

```
   productFields
```

Type: String

Comma-separated list of custom product fields. Fields aren’t case-sensitive. For example, `ProductCode` and `productcode`
return the same results.

If _`includeDisplayedList`_ is `false`, _`productFields`_ is ignored.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   sortItemsBy
```

Type: `ConnectApi.WishlistItemSortOrder`

Sort order for wishlist items. Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

The default sort order is `CreatedDateDesc` .

If _`includeDisplayedList`_ is `false`, _`sortItemsBy`_ is ignored.

Return Value

Type: `ConnectApi.WishlistsSummary`

##### **`removeWishlistItem(webstoreId, effectiveAccountId, wishlistId, wishlistItemId)`**

Remove an item from a wishlist.

API Version

49.0


Apex Reference Guide CommerceWishlist Class

Requires Chatter

No

Signature

```
   public static Void removeWishlistItem(String webstoreId, String effectiveAccountId,

   String wishlistId, String wishlistItemId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   wishlistItemId
```

Type: String

ID of the wishlist item to remove.

Return Value

Type: Void

##### **`updateWishlist(webstoreId, wishlistId, wishlistUpdateInput)`**

Update the name of a wishlist for the context user.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistSummary updateWishlist(String webstoreId, String

   wishlistId, ConnectApi.WishlistUpdateInput wishlistUpdateInput)

```

Parameters

```
   webstoreId
```

Type: String


Apex Reference Guide CommerceWishlist Class

ID of the webstore.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   wishlistUpdateInput
```

Type: `ConnectApi.WishlistUpdateInput`

A `ConnectApi.WishlistUpdateInput` body with the wishlist name to update.

Return Value

Type: `ConnectApi.WishlistSummary`

##### **`updateWishlist(webstoreId, effectiveAccountId, wishlistId,`**

```
  wishlistUpdateInput)

```

Update the name of a wishlist.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.WishlistSummary updateWishlist(String webstoreId, String

   effectiveAccountId, String wishlistId, ConnectApi.WishlistUpdateInput

   wishlistUpdateInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   wishlistUpdateInput
```

Type: `ConnectApi.WishlistUpdateInput`

A `ConnectApi.WishlistUpdateInput` body with the wishlist name to update.


### Apex Reference Guide Communities Class

Return Value

Type: `ConnectApi.WishlistSummary`

### Communities Class

Get information about Experience Cloud sites in your org.

Namespace

ConnectApi

#### Communities Methods

### These methods are for Communities . All methods are static.

IN THIS SECTION:

##### getCommunities()

Get a list of Experience Cloud sites that the context user has access to.

##### getCommunities(communityStatus)

Get a list of Experience Cloud sites with the specified status that the context user has access to.

getCommunity(communityId)
Get information about an Experience Cloud site.

##### **`getCommunities()`**

Get a list of Experience Cloud sites that the context user has access to.

API Version

28.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommunityPage getCommunities()

```

Return Value

Type: `ConnectApi.CommunityPage`

##### **`getCommunities(communityStatus)`**

Get a list of Experience Cloud sites with the specified status that the context user has access to.


Apex Reference Guide Communities Class

API Version

28.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommunityPage getCommunities(ConnectApi.CommunityStatus

   communityStatus)

```

Parameters

```
   communityStatus
```

Type: `ConnectApi.CommunityStatus`

_`communityStatus`_ —Status of the Experience Cloud site. Values are:

**•** `Live`

**•** `Inactive`

**•** `UnderConstruction`

Return Value

Type: `ConnectApi.CommunityPage`

##### **`getCommunity(communityId)`**

Get information about an Experience Cloud site.

API Version

28.0

Available to Guest Users

35.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Community getCommunity(String communityId)

```

Parameters

```
   communityId
```

Type: String


### Apex Reference Guide CommunityModeration Class

ID of an Experience Cloud site. You can’t specify `null` or `internal` .

Return Value

Type: `ConnectApi.Community`

### CommunityModeration Class

Get information about flagged feed items and comments in an Experience Cloud site. Add and remove flags from comments and feed
items.

Namespace

ConnectApi

#### CommunityModeration Methods

### These methods are for CommunityModeration . All methods are static.

All methods in this class require Chatter and are subject to the per user, per namespace, per hour rate limit.

IN THIS SECTION:

addFlagToComment(communityId, commentId)
Add a moderation flag to a comment.

addFlagToComment(communityId, commentId, visibility)
Add a moderation flag of the specified visibility to a comment.

addFlagToComment(communityId, commentId, type)
Add a moderation flag of the specified type to a comment.

addFlagToComment(communityId, commentId, note)
Add a moderation flag with a note to a comment.

addFlagToComment(communityId, commentId, type, note)
Add a moderation flag of the specified type with a note to a comment.

addFlagToComment(communityId, commentId, type, visibility)
Add a moderation flag of the specified type and visibility to a comment.

addFlagToComment(communityId, commentId, visibility, note)
Add a moderation flag of the specified visibility with a note to a comment.

addFlagToComment(communityId, commentId, type, visibility, note)
Add a moderation flag of the specified type and visibility with a note to a comment.

addFlagToFeedElement(communityId, feedElementId)
Add a moderation flag to a feed element.

addFlagToFeedElement(communityId, feedElementId, visibility)
Add a moderation flag of the specified visibility to a feed element.

addFlagToFeedElement(communityId, feedElementId, type)
Add a moderation flag of the specified type to a feed element.


Apex Reference Guide CommunityModeration Class

addFlagToFeedElement(communityId, feedElementId, note)
Add a moderation flag with a note to a feed element.

addFlagToFeedElement(communityId, feedElementId, type, note)
Add a moderation flag of the specified type with a note to a feed element.

addFlagToFeedElement(communityId, feedElementId, type, visibility)
Add a moderation flag of the specified type and visibility to a feed element.

addFlagToFeedElement(communityId, feedElementId, visibility, note)
Add a moderation flag of the specified visibility with a note to a feed element.

addFlagToFeedElement(communityId, feedElementId, type, visibility, note)
Add a moderation flag of the specified type and visibility with a note to a feed element.

getFlagsOnComment(communityId, commentId)
Get the moderation flags on a comment.

getFlagsOnComment(communityId, commentId, visibility)
Get the moderation flags with specified visibility on a comment.

getFlagsOnComment(communityId, commentId, pageSize, pageParam)
Get a page of moderation flags on a comment.

getFlagsOnComment(communityId, commentId, visibility, pageSize, pageParam)
Get a page of moderation flags with specified visibility on a comment.

getFlagsOnFeedElement(communityId, feedElementId)
Get the moderation flags on a feed element.

getFlagsOnFeedElement(communityId, feedElementId, visibility)
Get the moderation flags with specified visibility on a feed element.

getFlagsOnFeedElement(communityId, feedElementId, pageParam, pageSize)
Get a page of moderation flags on a feed element.

getFlagsOnFeedElement(communityId, feedElementId, visibility, pageSize, pageParam)
Get a page of moderation flags with specified visibility on a feed element.

removeFlagFromComment(communityId, commentId, userId)
Remove a moderation flag from a comment.

removeFlagFromFeedElement(communityId, feedElementId, userId)
Remove a moderation flag from a feed element.

##### **`addFlagToComment(communityId, commentId)`**

Add a moderation flag to a comment.

API Version

29.0

Requires Chatter

Yes


Apex Reference Guide CommunityModeration Class

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, visibility)`**

Add a moderation flag of the specified visibility to a comment.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagVisibility visibility)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`


Apex Reference Guide CommunityModeration Class

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, type)`**

Add a moderation flag of the specified type to a comment.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagType type)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .


Apex Reference Guide CommunityModeration Class

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, note)`**

Add a moderation flag with a note to a comment.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, String note)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, type, note)`**

Add a moderation flag of the specified type with a note to a comment.


Apex Reference Guide CommunityModeration Class

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagType type, String note)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, type, visibility)`**

Add a moderation flag of the specified type and visibility to a comment.

API Version

38.0


Apex Reference Guide CommunityModeration Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagType type, ConnectApi.CommunityFlagVisibility

   visibility)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, visibility, note)`**

Add a moderation flag of the specified visibility with a note to a comment.

API Version

38.0


Apex Reference Guide CommunityModeration Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagVisibility visibility, String note)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToComment(communityId, commentId, type, visibility, note)`**

Add a moderation flag of the specified type and visibility with a note to a comment.

API Version

38.0

Requires Chatter

Yes


Apex Reference Guide CommunityModeration Class

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagType type, ConnectApi.CommunityFlagVisibility

   visibility, String note)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a comment, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId)`**

Add a moderation flag to a feed element.

API Version

31.0


Apex Reference Guide CommunityModeration Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId)

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

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId, visibility)`**

Add a moderation flag of the specified visibility to a feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagVisibility visibility)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide CommunityModeration Class

```
   feedElementId
```

Type: String

ID of the feed element.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. One of these values:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId, type)`**

Add a moderation flag of the specified type to a feed element.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagType type)

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
   type
```

Type: `ConnectApi.CommunityFlagType`


Apex Reference Guide CommunityModeration Class

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

Return Value

Type: `ConnectApi.ModerationCapability`

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId, note)`**

Add a moderation flag with a note to a feed element.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, String note)

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
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationCapability`


Apex Reference Guide CommunityModeration Class

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId, type, note)`**

Add a moderation flag of the specified type with a note to a feed element.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagType type, String note)

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
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationCapability`

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.


Apex Reference Guide CommunityModeration Class

##### **`addFlagToFeedElement(communityId, feedElementId, type, visibility)`**

Add a moderation flag of the specified type and visibility to a feed element.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagType type,

   ConnectApi.CommunityFlagVisibility visibility)

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
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. One of these values:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationCapability`

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.


Apex Reference Guide CommunityModeration Class

##### **`addFlagToFeedElement(communityId, feedElementId, visibility, note)`**

Add a moderation flag of the specified visibility with a note to a feed element.

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagVisibility visibility, String note)

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
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. One of these values:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationCapability`

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedElement(communityId, feedElementId, type, visibility, note)`**

Add a moderation flag of the specified type and visibility with a note to a feed element.


Apex Reference Guide CommunityModeration Class

API Version

38.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability addFlagToFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagType type,

   ConnectApi.CommunityFlagVisibility visibility, String note)

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
   type
```

Type: `ConnectApi.CommunityFlagType`

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

If a type isn’t specified, it defaults to `FlagAsInappropriate` .

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. One of these values:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   note
```

Type: String

A note of up to 4,000 characters about the flag.

Return Value

Type: `ConnectApi.ModerationCapability`

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.


Apex Reference Guide CommunityModeration Class

##### **`getFlagsOnComment(communityId, commentId)`**

Get the moderation flags on a comment.

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnComment(String communityId, String

   commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnComment(communityId, commentId, visibility)`**

Get the moderation flags with specified visibility on a comment.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnComment(String communityId, String

   commentId, ConnectApi.CommunityFlagVisibility visibility)

```


Apex Reference Guide CommunityModeration Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnComment(communityId, commentId, pageSize, pageParam)`**

Get a page of moderation flags on a comment.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnComment(String communityId, String

   commentId, Integer pageSize, String pageParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String


Apex Reference Guide CommunityModeration Class

ID for a comment.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 0.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnComment(communityId, commentId, visibility, pageSize, pageParam)`**

Get a page of moderation flags with specified visibility on a comment.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnComment(String communityId, String

   commentId, ConnectApi.CommunityFlagVisibility visibility, Integer pageSize, String

   pageParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.


Apex Reference Guide CommunityModeration Class

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 0.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnFeedElement(communityId, feedElementId)`**

Get the moderation flags on a feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability getFlagsOnFeedElement(String communityId,

   String feedElementId)

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

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide CommunityModeration Class

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnFeedElement(communityId, feedElementId, visibility)`**

Get the moderation flags with specified visibility on a feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability getFlagsOnFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagVisibility visibility)

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
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. One of these values:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of moderation flags on a feed element.


Apex Reference Guide CommunityModeration Class

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability getFlagsOnFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize)

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
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 0.

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnFeedElement(communityId, feedElementId, visibility, pageSize,`**

```
  pageParam)

```

Get a page of moderation flags with specified visibility on a feed element.

API Version

40.0


Apex Reference Guide CommunityModeration Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationCapability getFlagsOnFeedElement(String communityId,

   String feedElementId, ConnectApi.CommunityFlagVisibility visibility, Integer pageSize,

   String pageParam)

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
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 0.

```
   pageParam
```

Type: String

Page token to use to view the page. Page tokens are returned as part of the response class, for example, `currentPageToken`
or `nextPageToken` . If you pass in `null`, the first page is returned.

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`removeFlagFromComment(communityId, commentId, userId)`**

Remove a moderation flag from a comment.


Apex Reference Guide CommunityModeration Class

API Version

29.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags removeFlagFromComment(String communityId,

   String commentId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentId
```

Type: String

ID for a comment.

```
   userId
```

Type: String

ID of the context user for whom the flag is removed. Specify `null` to remove the flag for all users.

Return Value

Type: Void

Usage

To remove a moderation flag, the context user must have added the flag or must have the Moderate Experiences Feeds permission.

##### **`removeFlagFromFeedElement(communityId, feedElementId, userId)`**

Remove a moderation flag from a feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static void removeFlagFromFeedElement(String communityId, String feedElementId,

   String userId)

```


Apex Reference Guide CommunityModeration Class

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
   userId
```

Type: String

ID of the context user for whom the flag is removed. Specify `null` to remove the flag for all users.

Return Value

Type: `ConnectApi.ModerationCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

To remove a moderation flag, the context user must have added the flag or must have the Moderate Experiences Feeds permission.

#### Retired CommunityModeration Methods

These methods for `CommunityModeration` are retired.

IN THIS SECTION:

##### addFlagToFeedItem(communityId, feedItemId)

Add a moderation flag to a feed item.

addFlagToFeedItem(communityId, feedItemId, visibility)
Add a moderation flag with specified visibility to a feed item.

getFlagsOnFeedItem(communityId, feedItemId)
Get the moderation flags on a feed item.

getFlagsOnFeedItem(communityId, feedItemId, visibility)
Get the moderation flags with specified visibility on a feed item.

removeFlagsOnFeedItem(communityId, feedItemId, userId)
Remove a moderation flag from a feed item.

##### **`addFlagToFeedItem(communityId, feedItemId)`**

Add a moderation flag to a feed item.

API Version

29.0–31.0


Apex Reference Guide CommunityModeration Class

Important: In version 32.0 and later, use addFlagToFeedElement(communityId, feedElementId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToFeedItem(String communityId, String

   feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a feed item, Allow members to flag content must be selected for an Experience Cloud site.

##### **`addFlagToFeedItem(communityId, feedItemId, visibility)`**

Add a moderation flag with specified visibility to a feed item.

API Version

30.0–31.0

Important: In version 32.0 and later, use addFlagToFeedElement(communityId, feedElementId, visibility).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags addFlagToFeedItem(String communityId, String

   feedItemId, ConnectApi.CommunityFlagVisibility visibility)

```


Apex Reference Guide CommunityModeration Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To add a flag to a feed item, Allow members to flag content must be selected for an Experience Cloud site.

##### **`getFlagsOnFeedItem(communityId, feedItemId)`**

Get the moderation flags on a feed item.

API Version

29.0–31.0

Important: In version 32.0 and later, use getFlagsOnFeedElement(communityId, feedElementId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnFeedItem(String communityId, String

   feedItemId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide CommunityModeration Class

```
   feedItemId
```

Type: String

ID for a feed item.

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`getFlagsOnFeedItem(communityId, feedItemId, visibility)`**

Get the moderation flags with specified visibility on a feed item.

API Version

30.0–31.0

Important: In version 32.0 and later, use getFlagsOnFeedElement(communityId, feedElementId, visibility).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags getFlagsOnFeedItem(String communityId, String

   feedItemId, ConnectApi.CommunityFlagVisibility visibility)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   visibility
```

Type: `ConnectApi.CommunityFlagVisibility`

Visibility behavior of a flag for various user types. Values are:

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with moderation permissions on the flagged
element or item.


Apex Reference Guide CommunityModeration Class

Return Value

Type: `ConnectApi.ModerationFlags`

Usage

To get moderation flags, the context user must have the Moderate Experiences Feeds permission.

##### **`removeFlagsOnFeedItem(communityId, feedItemId, userId)`**

Remove a moderation flag from a feed item.

API Version

29.0–31.0

Important: In version 32.0 and later, use removeFlagFromFeedElement(communityId, feedElementId, userId).

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ModerationFlags removeFlagsOnFeedItem(String communityId,

   String feedItemId, String userId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedItemId
```

Type: String

ID for a feed item.

```
   userId
```

Type: String

ID of the context user for whom the flag is removed. Specify `null` to remove the flag for all users.

Return Value

Type: Void

Usage

To remove a moderation flag, the context user must have added the flag or must have the Moderate Experiences Feeds permission.


### Apex Reference Guide ContentHub Class ContentHub Class

Access Files Connect repositories and their files and folders.

Namespace

ConnectApi

#### ContentHub Methods

### These methods are for ContentHub . All methods are static. Use ContentHub methods to work with Files Connect repositories.

IN THIS SECTION:

addRepositoryItem(repositoryId, repositoryFolderId, file)
Add a repository item.

addRepositoryItem(communityId, repositoryId, repositoryFolderId, file)
Add a repository item in an Experience Cloud site.

addRepositoryItem(repositoryId, repositoryFolderId, file, fileData)
Add a repository item, including the binary file.

addRepositoryItem(communityId, repositoryId, repositoryFolderId, file, fileData)
Add a repository item, including the binary file, in an Experience Cloud site.

getAllowedItemTypes(repositoryId, repositoryFolderId)
Get the item types that the context user is allowed to create in the repository folder.

getAllowedItemTypes(repositoryId, repositoryFolderId, filter)
Get the item types, filtered by type, that the context user is allowed to create in the repository folder.

getAllowedItemTypes(communityId, repositoryId, repositoryFolderId)
Get the item types that the context user is allowed to create in the repository folder in an Experience Cloud site.

getAllowedItemTypes(communityId, repositoryId, repositoryFolderId, filter)
Get the item types, filtered by type, that the context user is allowed to create in the repository folder in an Experience Cloud site.

getFilePreview(repositoryId, repositoryFileId, formatType)
Get a repository file preview.

getFilePreview(repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber)
Get a page or page range of a repository file preview.

getFilePreview(communityId, repositoryId, repositoryFileId, formatType)
Get a repository file preview in an Experience Cloud site.

getFilePreview(communityId, repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber)
Get a page or page range of a repository file preview in an Experience Cloud site.

getItemType(repositoryId, repositoryItemTypeId)
Get information about an item type associated with a repository.

getItemType(communityId, repositoryId, repositoryItemTypeId)
Get information about an item type associated with a repository in an Experience Cloud site.


Apex Reference Guide ContentHub Class

getPreviews(repositoryId, repositoryFileId)
Get information about a repository file’s supported previews.

getPreviews(communityId, repositoryId, repositoryFileId)
Get information about a repository file’s supported previews in an Experience Cloud site.

getRepositories()
Get a list of repositories.

getRepositories(communityId)
Get a list of repositories in an Experience Cloud site.

getRepositories(pageParam, pageSize)
Get a page of repositories.

getRepositories(communityId, pageParam, pageSize)
Get a page of repositories in an Experience Cloud site.

getRepository(repositoryId)
Get a repository.

getRepository(communityId, repositoryId)
Get a repository in an Experience Cloud site.

getRepositoryFile(repositoryId, repositoryFileId)
Get a repository file.

getRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)
Get a repository file with or without permissions information.

getRepositoryFile(communityId, repositoryId, repositoryFileId)
Get a repository file in an Experience Cloud site.

getRepositoryFile(communityId, repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)
Get a repository file with or without permissions information in an Experience Cloud site.

getRepositoryFolder(repositoryId, repositoryFolderId)
Get a repository folder.

getRepositoryFolder(communityId, repositoryId, repositoryFolderId)
Get a repository folder in an Experience Cloud site.

getRepositoryFolderItems(repositoryId, repositoryFolderId)
Get repository folder items.

getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId)
Get repository folder items in an Experience Cloud site.

getRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam, pageSize)
Get a page of repository folder items.

getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId, pageParam, pageSize)
Get a page of repository folder items in an Experience Cloud site.

updateRepositoryFile(repositoryId, repositoryFileId, file)
Update the name of a repository file.

updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)
Update the content of a repository file.


Apex Reference Guide ContentHub Class

updateRepositoryFile(communityId, repositoryId, repositoryFileId, file)
Update the name of a repository file in an Experience Cloud site.

updateRepositoryFile(communityId, repositoryId, repositoryFileId, file, fileData)
Update the content of a repository file in an Experience Cloud site.

##### **`addRepositoryItem(repositoryId, repositoryFolderId, file)`**

Add a repository item.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItem addRepositoryItem(String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubItemInput file)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

Return Value

Type: `ConnectApi.RepositoryFolderItem`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.


Apex Reference Guide ContentHub Class

Example

This example creates a file without binary content (metadata only) in a Google Drive repository folder. After the file is created, we show
the file’s ID, name, description, external URL, and download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.ContentHubItemInput newItem = new ConnectApi.ContentHubItemInput();

   newItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

   for creation/update

   newItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   final ConnectApi.ContentHubFieldValueInput fieldValueInput = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInput.name = 'name';

   fieldValueInput.value = 'new folder item name.txt';

   newItem.fields.add(fieldValueInput);

   //Metadata: description field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputDesc = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputDesc.name = 'description';

   fieldValueInputDesc.value = 'It does describe it';

   newItem.fields.add(fieldValueInputDesc);

   final ConnectApi.RepositoryFolderItem newFolderItem =

   ConnectApi.ContentHub.addRepositoryItem(gDriveRepositoryId, gDriveFolderId, newItem);

   final ConnectApi.RepositoryFileSummary newFile = newFolderItem.file;

   System.debug(String.format('New file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

   \'\'{2}\'\' \n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   newFile.id, newFile.name, newFile.description, newFile.externalDocumentUrl,

   newFile.downloadUrl}));

```

SEE ALSO:

setTestAddRepositoryItem(repositoryId, repositoryFolderId, file, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`addRepositoryItem(communityId, repositoryId, repositoryFolderId, file)`**

Add a repository item in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.RepositoryFolderItem addRepositoryItem(String communityId,

   String repositoryId, String repositoryFolderId, ConnectApi.ContentHubItemInput file)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

Return Value

Type: `ConnectApi.RepositoryFolderItem`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestAddRepositoryItem(communityId, repositoryId, repositoryFolderId, file, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`addRepositoryItem(repositoryId, repositoryFolderId, file, fileData)`**

Add a repository item, including the binary file.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.RepositoryFolderItem addRepositoryItem(String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput

   fileData)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

Return Value

Type: `ConnectApi.RepositoryFolderItem`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example creates a file with binary content and metadata in a Google Drive repository folder. After the file is created, we show the
file’s ID, name, description, external URL, and download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.ContentHubItemInput newItem = new ConnectApi.ContentHubItemInput();

   newItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

   for creation/update

   newItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   Final String newFileName = 'new folder item name.txt';

   final ConnectApi.ContentHubFieldValueInput fieldValueInput = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInput.name = 'name';

   fieldValueInput.value = newFileName;

   newItem.fields.add(fieldValueInput);

```


Apex Reference Guide ContentHub Class

```
   //Metadata: description field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputDesc = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputDesc.name = 'description';

   fieldValueInputDesc.value = 'It does describe it';

   newItem.fields.add(fieldValueInputDesc);

   //Binary content

   final Blob newFileBlob = Blob.valueOf('awesome content for brand new file');

   final String newFileMimeType = 'text/plain';

   final ConnectApi.BinaryInput fileBinaryInput = new ConnectApi.BinaryInput(newFileBlob,

   newFileMimeType, newFileName);

   final ConnectApi.RepositoryFolderItem newFolderItem =

   ConnectApi.ContentHub.addRepositoryItem(gDriveRepositoryId, gDriveFolderId, newItem,

   fileBinaryInput);

   final ConnectApi.RepositoryFileSummary newFile = newFolderItem.file;

   System.debug(String.format('New file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

   \'\'{2}\'\' \n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   newFile.id, newFile.name, newFile.description, newFile.externalDocumentUrl,

   newFile.downloadUrl}));

```

SEE ALSO:

setTestAddRepositoryItem(repositoryId, repositoryFolderId, file, fileData, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`addRepositoryItem(communityId, repositoryId, repositoryFolderId, file,`**

```
  fileData)

```

Add a repository item, including the binary file, in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItem addRepositoryItem(String communityId,

   String repositoryId, String repositoryFolderId, ConnectApi.ContentHubItemInput file,

   ConnectApi.BinaryInput fileData)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ContentHub Class

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

Return Value

Type: `ConnectApi.RepositoryFolderItem`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestAddRepositoryItem(communityId, repositoryId, repositoryFolderId, file, fileData, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getAllowedItemTypes(repositoryId, repositoryFolderId)`**

Get the item types that the context user is allowed to create in the repository folder.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubAllowedItemTypeCollection getAllowedItemTypes(String

   repositoryId, String repositoryFolderId)

```


Apex Reference Guide ContentHub Class

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetAllowedItemTypes(repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getAllowedItemTypes(repositoryId, repositoryFolderId, filter)`**

Get the item types, filtered by type, that the context user is allowed to create in the repository folder.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubAllowedItemTypeCollection getAllowedItemTypes(String

   repositoryId, String repositoryFolderId, ConnectApi.ConnectContentHubItemType filter)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.


Apex Reference Guide ContentHub Class

```
   filter
```

Type: `ConnectApi.ContentHubItemType`

Item types. Values are:

**•** `Any` —Includes files and folders.

**•** `FilesOnly` —Includes files only.

**•** `FoldersOnly` —Includes folders only.

Return Value

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example calls `getAllowedItemTypes(repositoryId, repositoryFolderId,`
`ConnectApi.ContentHubItemType.FilesOnly)` to get the first `ConnectApi.ContentHubItemTypeSummary.id`
of a file. The context user can create allowed files in a repository folder in the external system.

```
   final ConnectApi.ContentHubAllowedItemTypeCollection allowedItemTypesColl =

   ConnectApi.ContentHub.getAllowedItemTypes(repositoryId, repositoryFolderId,

   ConnectApi.ContentHubItemType.FilesOnly);

   final List<ConnectApi.ContentHubItemTypeSummary> allowedItemTypes =

   allowedItemTypesColl.allowedItemTypes;

   string allowedFileItemTypeId = null;

   if(allowedItemTypes.size() > 0){

     ConnectApi.ContentHubItemTypeSummary allowedItemTypeSummary = allowedItemTypes.get(0);

     allowedFileItemTypeId = allowedItemTypeSummary.id;

   }

```

SEE ALSO:

setTestGetAllowedItemTypes(repositoryId, repositoryFolderId, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getAllowedItemTypes(communityId, repositoryId, repositoryFolderId)`**

Get the item types that the context user is allowed to create in the repository folder in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.ContentHubAllowedItemTypeCollection getAllowedItemTypes(String

   communityId, String repositoryId, String repositoryFolderId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetAllowedItemTypes(communityId, repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getAllowedItemTypes(communityId, repositoryId, repositoryFolderId, filter)`**

Get the item types, filtered by type, that the context user is allowed to create in the repository folder in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubAllowedItemTypeCollection getAllowedItemTypes(String

   communityId, String repositoryId, String repositoryFolderId,

   ConnectApi.ConnectContentHubItemType filter)

```


Apex Reference Guide ContentHub Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   filter
```

Type: `ConnectApi.ContentHubItemType`

Item types. Values are:

**•** `Any` —Includes files and folders.

**•** `FilesOnly` —Includes files only.

**•** `FoldersOnly` —Includes folders only.

Return Value

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetAllowedItemTypes(communityId, repositoryId, repositoryFolderId, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFilePreview(repositoryId, repositoryFileId, formatType)`**

Get a repository file preview.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FilePreview getFilePreview(String repositoryId, String

   repositoryFileId, ConnectApi.FilePreviewFormat formatType)

```


Apex Reference Guide ContentHub Class

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

Return Value

Type: `ConnectApi.FilePreview`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example calls `getFilePreview(repositoryId, repositoryFileId,`
`ConnectApi.FilePreviewFormat.Thumbnail)` to get the thumbnail format preview along with its respective URL and
number of thumbnail renditions. For each thumbnail format, we show every rendition URL available.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'document:1-zcA1BaeoQbo2_yNFiHCcK6QJTPmOke-kHFC4TYg3rk';final ConnectApi.FilePreview

   filePreview =

   ConnectApi.ContentHub.getFilePreview(gDriveRepositoryId, gDriveFileId,

   ConnectApi.FilePreviewFormat.Thumbnail);System.debug(String.format('Preview - URL:

   \'\'{0}\'\', format: \'\'{1}\'\', nbr of

   renditions for this format: {2}', new String[]{ filePreview.url,

   filePreview.format.name(),String.valueOf(filePreview.previewUrls.size())}));for(ConnectApi.FilePreviewUrl

    filePreviewUrl : filePreview.previewUrls){

```


Apex Reference Guide ContentHub Class

```
     System.debug('-----> Rendition URL: ' + filePreviewUrl.previewUrl);

   }

```

SEE ALSO:

setTestGetFilePreview(repositoryId, repositoryFileId, formatType, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFilePreview(repositoryId, repositoryFileId, formatType, startPageNumber,`**

```
  endPageNumber)

```

Get a page or page range of a repository file preview.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FilePreview getFilePreview(String repositoryId, String

   repositoryFileId, ConnectApi.FilePreviewFormat formatType, Integer startPageNumber,

   Integer endPageNumber)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.


Apex Reference Guide ContentHub Class

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   startPageNumber
```

Type: Integer

The starting page number in the range of file preview URLs.

```
   endPageNumber
```

Type: Integer

The ending page number in the range of file preview URLs.

Return Value

Type: `ConnectApi.FilePreview`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFilePreview(repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFilePreview(communityId, repositoryId, repositoryFileId, formatType)`**

Get a repository file preview in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FilePreview getFilePreview(String communityId, String

   repositoryId, String repositoryFileId, ConnectApi.FilePreviewFormat formatType)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String


Apex Reference Guide ContentHub Class

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

Return Value

Type: `ConnectApi.FilePreview`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFilePreview(communityId, repositoryId, repositoryFileId, formatType, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFilePreview(communityId, repositoryId, repositoryFileId, formatType,`**

```
  startPageNumber, endPageNumber)

```

Get a page or page range of a repository file preview in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.FilePreview getFilePreview(String communityId, String

   repositoryId, String repositoryFileId, ConnectApi.FilePreviewFormat formatType, Integer

   startPageNumber, Integer endPageNumber)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   startPageNumber
```

Type: Integer

The starting page number in the range of file preview URLs.

```
   endPageNumber
```

Type: Integer

The ending page number in the range of file preview URLs.

Return Value

Type: `ConnectApi.FilePreview`


Apex Reference Guide ContentHub Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFilePreview(communityId, repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getItemType(repositoryId, repositoryItemTypeId)`**

Get information about an item type associated with a repository.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubItemTypeDetail getItemType(String repositoryId,

   String repositoryItemTypeId)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryItemTypeId
```

Type: String

The ID of the repository item type.

Return Value

Type: `ConnectApi.ContentHubItemTypeDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetItemType(repositoryId, repositoryItemTypeId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`getItemType(communityId, repositoryId, repositoryItemTypeId)`**

Get information about an item type associated with a repository in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubItemTypeDetail getItemType(String communityId, String

   repositoryId, String repositoryItemTypeId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryItemTypeId
```

Type: String

The ID of the repository item type.

Return Value

Type: `ConnectApi.ContentHubItemTypeDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetItemType(communityId, repositoryId, repositoryItemTypeId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getPreviews(repositoryId, repositoryFileId)`**

Get information about a repository file’s supported previews.


Apex Reference Guide ContentHub Class

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FilePreviewCollection getPreviews(String repositoryId, String

   repositoryFileId)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

Return Value

Type: `ConnectApi.FilePreviewCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets all supported preview formats and their respective URLs and number of renditions. For each supported preview format,
we show every rendition URL available.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'document:1-zcA1BaeoQbo2_yNFiHCcK6QJTPmOke-kHFC4TYg3rk';

   final ConnectApi.FilePreviewCollection previewsCollection =

   ConnectApi.ContentHub.getPreviews(gDriveRepositoryId, gDriveFileId);

   for(ConnectApi.FilePreview filePreview : previewsCollection.previews){

     System.debug(String.format('Preview - URL: \'\'{0}\'\', format: \'\'{1}\'\', nbr of

   renditions for this format: {2}', new String[]{ filePreview.url,

   filePreview.format.name(),String.valueOf(filePreview.previewUrls.size())}));

     for(ConnectApi.FilePreviewUrl filePreviewUrl : filePreview.previewUrls){

       System.debug('-----> Rendition URL: ' + filePreviewUrl.previewUrl);

```


Apex Reference Guide ContentHub Class

```
       }

   }

```

SEE ALSO:

setTestGetPreviews(repositoryId, repositoryFileId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getPreviews(communityId, repositoryId, repositoryFileId)`**

Get information about a repository file’s supported previews in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FilePreviewCollection getPreviews(String communityId, String

   repositoryId, String repositoryFileId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

Return Value

Type: `ConnectApi.FilePreviewCollection`


Apex Reference Guide ContentHub Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetPreviews(communityId, repositoryId, repositoryFileId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositories()`**

Get a list of repositories.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubRepositoryCollection getRepositories()

```

Return Value

Type: `ConnectApi.ContentHubRepositoryCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets all repositories and gets the first SharePoint online repository found.

```
   final string sharePointOnlineProviderType ='ContentHubSharepointOffice365';

   final ConnectApi.ContentHubRepositoryCollection repositoryCollection =

   ConnectApi.ContentHub.getRepositories();

   ConnectApi.ContentHubRepository sharePointOnlineRepository = null;

   for(ConnectApi.ContentHubRepository repository : repositoryCollection.repositories){

     if(sharePointOnlineProviderType.equalsIgnoreCase(repository.providerType.type)){

       sharePointOnlineRepository = repository;

       break;

```


Apex Reference Guide ContentHub Class

```
     }

   }

```

SEE ALSO:

setTestGetRepositories(result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositories(communityId)`**

Get a list of repositories in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubRepositoryCollection getRepositories(String

   communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ContentHubRepositoryCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositories(communityId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositories(pageParam, pageSize)`**

Get a page of repositories.


Apex Reference Guide ContentHub Class

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubRepositoryCollection getRepositories(Integer

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

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

Return Value

Type: `ConnectApi.ContentHubRepositoryCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositories(pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositories(communityId, pageParam, pageSize)`**

Get a page of repositories in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.ContentHubRepositoryCollection getRepositories(String

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

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

Return Value

Type: `ConnectApi.ContentHubRepositoryCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositories(communityId, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepository(repositoryId)`**

Get a repository.

API Version

369.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubRepository getRepository(String repositoryId)

```


Apex Reference Guide ContentHub Class

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

Return Value

Type: `ConnectApi.ContentHubRepository`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

```
   final string repositoryId = '0XCxx0000000123GAA';

   final ConnectApi.ContentHubRepository repository =

   ConnectApi.ContentHub.getRepository(repositoryId);

```

SEE ALSO:

setTestGetRepository(repositoryId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepository(communityId, repositoryId)`**

Get a repository in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ContentHubRepository getRepository(String communityId, String

   repositoryId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String


Apex Reference Guide ContentHub Class

The ID of the repository.

Return Value

Type: `ConnectApi.ContentHubRepository`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepository(communityId, repositoryId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFile(repositoryId, repositoryFileId)`**

Get a repository file.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail getRepositoryFile(String repositoryId,

   String repositoryFileId)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.


Apex Reference Guide ContentHub Class

Example

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'file:0B0lTys1KmM3sTmxKNjVJbWZja00';

   final ConnectApi.RepositoryFileDetail file =

   ConnectApi.ContentHub.getRepositoryFile(gDriveRepositoryId, gDriveFileId);

   System.debug(String.format('File - name: \'\'{0}\'\', size: {1}, external URL: \'\'{2}\'\',

    download URL: \'\'{3}\'\'',

     new String[]{ file.name, String.valueOf(file.contentSize), file.externalDocumentUrl,

   file.downloadUrl}));

```

SEE ALSO:

setTestGetRepositoryFile(repositoryId, repositoryFileId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFile(repositoryId, repositoryFileId,`**

```
  includeExternalFilePermissionsInfo)

```

Get a repository file with or without permissions information.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail getRepositoryFile(String repositoryId,

   String repositoryFileId, Boolean includeExternalFilePermissionsInfo)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   includeExternalFilePermissionsInfo
```

Type: Boolean

Specifies whether to include permission information, such as whether the file is shared and what are the available permission types.

Managing external file permissions is supported for Google Drive, SharePoint Online, and OneDrive for Business.


Apex Reference Guide ContentHub Class

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'file:0B0lTys1KmM3sTmxKNjVJbWZja00';

   final ConnectApi.RepositoryFileDetail file =

   ConnectApi.ContentHub.getRepositoryFile(gDriveRepositoryId, gDriveFileId, true);

   System.debug(String.format('File - name: \'\'{0}\'\', size: {1}, external URL: \'\'{2}\'\',

    download URL: \'\'{3}\'\'', new String[]{ file.name, String.valueOf(file.contentSize),

   file.externalDocumentUrl, file.downloadUrl}));

   final ConnectApi.ExternalFilePermissionInformation externalFilePermInfo =

   file.externalFilePermissionInformation;

   //permission types

   final List<ConnectApi.ContentHubPermissionType> permissionTypes =

   externalFilePermInfo.externalFilePermissionTypes;

   for(ConnectApi.ContentHubPermissionType permissionType : permissionTypes){

     System.debug(String.format('Permission type - id: \'\'{0}\'\', label: \'\'{1}\'\'', new

    String[]{ permissionType.id, permissionType.label}));

   }

   //permission groups

   final List<ConnectApi.RepositoryGroupSummary> groups =

   externalFilePermInfo.repositoryPublicGroups;

   for(ConnectApi.RepositoryGroupSummary ggroup : groups){

     System.debug(String.format('Group - id: \'\'{0}\'\', name: \'\'{1}\'\', type:

   \'\'{2}\'\'', new String[]{ ggroup.id, ggroup.name, ggroup.type.name()}));

   }

```

SEE ALSO:

setTestGetRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFile(communityId, repositoryId, repositoryFileId)`**

Get a repository file in an Experience Cloud site.

API Version

39.0


Apex Reference Guide ContentHub Class

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail getRepositoryFile(String communityId,

   String repositoryId, String repositoryFileId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFile(communityId, repositoryId, repositoryFileId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFile(communityId, repositoryId, repositoryFileId,`**

```
  includeExternalFilePermissionsInfo)

```

Get a repository file with or without permissions information in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.RepositoryFileDetail getRepositoryFile(String communityId,

   String repositoryId, String repositoryFileId, Boolean includeExternalFilePermissionsInfo)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   includeExternalFilePermissionsInfo
```

Type: Boolean

Specifies whether to include permission information, such as whether the file is shared and what are the available permission types.

Managing external file permissions is supported for Google Drive, SharePoint Online, and OneDrive for Business.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFile(communityId, repositoryId, repositoryFileId, includeExternalFilePermissionsInfo, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolder(repositoryId, repositoryFolderId)`**

Get a repository folder.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.RepositoryFolderDetail getRepositoryFolder(String repositoryId,

   String repositoryFolderId)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.RepositoryFolderDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.RepositoryFolderDetail folder =

   ConnectApi.ContentHub.getRepositoryFolder(gDriveRepositoryId, gDriveFolderId);

   System.debug(String.format('Folder - name: \'\'{0}\'\', description: \'\'{1}\'\', external

    URL: \'\'{2}\'\', folder items URL: \'\'{3}\'\'',

     new String[]{ folder.name, folder.description, folder.externalFolderUrl,

   folder.folderItemsUrl}));

```

SEE ALSO:

setTestGetRepositoryFolder(repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolder(communityId, repositoryId, repositoryFolderId)`**

Get a repository folder in an Experience Cloud site.

API Version

39.0

Requires Chatter

No


Apex Reference Guide ContentHub Class

Signature

```
   public static ConnectApi.RepositoryFolderDetail getRepositoryFolder(String communityId,

   String repositoryId, String repositoryFolderId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.RepositoryFolderDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFolder(communityId, repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolderItems(repositoryId, repositoryFolderId)`**

Get repository folder items.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItemsCollection getRepositoryFolderItems(String

   repositoryId, String repositoryFolderId)

```


Apex Reference Guide ContentHub Class

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.RepositoryFolderItemsCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets the collection of items in a repository folder. For files, we show the file’s name, size, external URL, and download URL.
For folders, we show the folder’s name, description, and external URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.RepositoryFolderItemsCollection folderItemsColl =

   ConnectApi.ContentHub.getRepositoryFolderItems(gDriveRepositoryId,gDriveFolderId);

   final List<ConnectApi.RepositoryFolderItem> folderItems = folderItemsColl.items;

   System.debug('Number of items in repository folder: ' + folderItems.size());

   for(ConnectApi.RepositoryFolderItem item : folderItems){

     ConnectApi.RepositoryFileSummary fileSummary = item.file;

     if(fileSummary != null){

       System.debug(String.format('File item - name: \'\'{0}\'\', size: {1}, external URL:

    \'\'{2}\'\', download URL: \'\'{3}\'\'', new String[]{ fileSummary.name,

   String.valueOf(fileSummary.contentSize), fileSummary.externalDocumentUrl,

   fileSummary.downloadUrl}));

       }else{

         ConnectApi.RepositoryFolderSummary folderSummary = item.folder;

         System.debug(String.format('Folder item - name: \'\'{0}\'\', description:

   \'\'{1}\'\'', new String[]{ folderSummary.name, folderSummary.description}));

       }

   }

```

SEE ALSO:

setTestGetRepositoryFolderItems(repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId)`**

Get repository folder items in an Experience Cloud site.


Apex Reference Guide ContentHub Class

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItemsCollection getRepositoryFolderItems(String

   communityId, String repositoryId, String repositoryFolderId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

Return Value

Type: `ConnectApi.RepositoryFolderItemsCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFolderItems(communityId, repositoryId, repositoryFolderId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam,`**

```
  pageSize)

```

Get a page of repository folder items.

API Version

39.0


Apex Reference Guide ContentHub Class

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItemsCollection getRepositoryFolderItems(String

   repositoryId, String repositoryFolderId, Integer pageParam, Integer pageSize)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

Return Value

Type: `ConnectApi.RepositoryFolderItemsCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId,`**

```
  pageParam, pageSize)

```

Get a page of repository folder items in an Experience Cloud site.

API Version

39.0


Apex Reference Guide ContentHub Class

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFolderItemsCollection getRepositoryFolderItems(String

   communityId, String repositoryId, String repositoryFolderId, Integer pageParam, Integer

   pageSize)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

Return Value

Type: `ConnectApi.RepositoryFolderItemsCollection`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetRepositoryFolderItems(communityId, repositoryId, repositoryFolderId, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`updateRepositoryFile(repositoryId, repositoryFileId, file)`**

Update the name of a repository file.


Apex Reference Guide ContentHub Class

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail updateRepositoryFile(String repositoryId,

   String repositoryFileId, ConnectApi.ContentHubItemInput file)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

When updating the metadata of a repository file, only the name field can be updated.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example updates the name of a file in a Google Drive repository. After the file is updated, we show the file’s ID, name, description,
external URL, download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs', gDriveFileId =

   'document:1q9OatVpcyYBK-JWzp_PhR75ulQghwFP15zhkamKrRcQ';

   final ConnectApi.ContentHubItemInput updatedItem = new ConnectApi.ContentHubItemInput();

   updatedItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

    for creation/update

   updatedItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

```


Apex Reference Guide ContentHub Class

```
   final ConnectApi.ContentHubFieldValueInput fieldValueInputName = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputName.name = 'name';

   fieldValueInputName.value = 'updated file name.txt';

   updatedItem.fields.add(fieldValueInputName);

   final ConnectApi.RepositoryFileDetail updatedFile =

   ConnectApi.ContentHub.updateRepositoryFile(gDriveRepositoryId, gDriveFileId, updatedItem);

   System.debug(String.format('Updated file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

    \'\'{2}\'\',\n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   updatedFile.id, updatedFile.name, updatedFile.description, updatedFile.externalDocumentUrl,

    updatedFile.downloadUrl}));

```

SEE ALSO:

setTestUpdateRepositoryFile(communityId, repositoryId, repositoryFileId, file, fileData, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)`**

Update the content of a repository file.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail updateRepositoryFile(String repositoryId,

   String repositoryFileId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput

   fileData)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

When updating the metadata of a repository file, only the name field can be updated.


Apex Reference Guide ContentHub Class

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example updates the content and name of a file in a Google Drive repository. After the file is updated, we show the file’s ID, name,
description, external URL, and download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs', gDriveFileId =

   'document:1q9OatVpcyYBK-JWzp_PhR75ulQghwFP15zhkamKrRcQ';

   final ConnectApi.ContentHubItemInput updatedItem = new ConnectApi.ContentHubItemInput();

   updatedItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

    for creation/update

   updatedItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputName = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputName.name = 'name';

   fieldValueInputName.value = 'updated file name.txt';

   updatedItem.fields.add(fieldValueInputName);

   //Binary content

   final Blob updatedFileBlob = Blob.valueOf('even more awesome content for updated file');

   final String updatedFileMimeType = 'text/plain';

   final ConnectApi.BinaryInput fileBinaryInput = new ConnectApi.BinaryInput(updatedFileBlob,

    updatedFileMimeType, updatedFileName);

   final ConnectApi.RepositoryFileDetail updatedFile =

   ConnectApi.ContentHub.updateRepositoryFile(gDriveRepositoryId, gDriveFileId, updatedItem);

   System.debug(String.format('Updated file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

    \'\'{2}\'\',\n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   updatedFile.id, updatedFile.name, updatedFile.description, updatedFile.externalDocumentUrl,

    updatedFile.downloadUrl}));

```

SEE ALSO:

setTestUpdateRepositoryFile(repositoryId, repositoryFileId, file, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`updateRepositoryFile(communityId, repositoryId, repositoryFileId, file)`**

Update the name of a repository file in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail updateRepositoryFile(String communityId,

   String repositoryId, String repositoryFileId, ConnectApi.ContentHubItemInput file)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

When updating the metadata of a repository file, only the name field can be updated.

Return Value

Type: `ConnectApi.RepositoryFileDetail`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestUpdateRepositoryFile(repositoryId, repositoryFileId, file, fileData, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`updateRepositoryFile(communityId, repositoryId, repositoryFileId, file,`**

```
  fileData)

```

Update the content of a repository file in an Experience Cloud site.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RepositoryFileDetail updateRepositoryFile(String communityId,

   String repositoryId, String repositoryFileId, ConnectApi.ContentHubItemInput file,

   ConnectApi.BinaryInput fileData)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

When updating the metadata of a repository file, only the name field can be updated.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

Return Value

Type: `ConnectApi.RepositoryFileDetail`


Apex Reference Guide ContentHub Class

Usage

##### To test code that uses this method, use the matching set test method (prefix the method name with setTest ). Use the set test method

with the same parameters or the code throws an exception.

SEE ALSO:

setTestUpdateRepositoryFile(communityId, repositoryId, repositoryFileId, file, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### ContentHub Test Methods These test methods are for ContentHub . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAddRepositoryItem(repositoryId, repositoryFolderId, file, result)`**

Register a `ConnectApi.RepositoryFolderItem` object to be returned when the matching
`addRepositoryItem(repositoryId, repositoryFolderId, file)` method is called in a test context. Use the
method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestAddRepositoryItem(String repositoryId, String

   repositoryFolderId, ConnectApi.ContentHubItemInput file, ConnectApi.RepositoryFolderItem

   result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   result
```

Type: `ConnectApi.RepositoryFolderItem`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

addRepositoryItem(repositoryId, repositoryFolderId, file)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAddRepositoryItem(communityId, repositoryId, repositoryFolderId, file,`**

```
  result)

```

Register a `ConnectApi.RepositoryFolderItem` object to be returned when the matching
`addRepositoryItem(communityId, repositoryId, repositoryFolderId, file)` method is called in a
test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestAddRepositoryItem(String communityId, String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubItemInput file,

   ConnectApi.RepositoryFolderItem result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   result
```

Type: `ConnectApi.RepositoryFolderItem`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

addRepositoryItem(communityId, repositoryId, repositoryFolderId, file)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAddRepositoryItem(repositoryId, repositoryFolderId, file, fileData,`**

```
  result)

```

Register a `ConnectApi.RepositoryFolderItem` object to be returned when the matching
`addRepositoryItem(repositoryId, repositoryFolderId, file, fileData)` method is called in a test
context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestAddRepositoryItem(String repositoryId, String

   repositoryFolderId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput fileData,

   ConnectApi.RepositoryFolderItem result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

```
   result
```

Type: `ConnectApi.RepositoryFolderItem`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

addRepositoryItem(repositoryId, repositoryFolderId, file, fileData)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestAddRepositoryItem(communityId, repositoryId, repositoryFolderId, file,`**

```
  fileData, result)

```

Register a `ConnectApi.RepositoryFolderItem` object to be returned when the matching
`addRepositoryItem(communityId, repositoryId, repositoryFolderId, file, fileData)` method
is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestAddRepositoryItem(String communityId, String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput

   fileData, ConnectApi.RepositoryFolderItem result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

```
   result
```

Type: `ConnectApi.RepositoryFolderItem`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

addRepositoryItem(communityId, repositoryId, repositoryFolderId, file, fileData)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetAllowedItemTypes(repositoryId, repositoryFolderId, result)`**

Register a `ConnectApi.ContentHubAllowedItemTypeCollection` object to be returned when the matching
`getAllowedItemTypes(repositoryId, repositoryFolderId)` method is called in a test context. Use the method
with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetAllowedItemTypes(String repositoryId, String

   repositoryFolderId, ConnectApi.ContentHubAllowedItemTypeCollection result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getAllowedItemTypes(repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`setTestGetAllowedItemTypes(repositoryId, repositoryFolderId, filter, result)`**

Register a `ConnectApi.ContentHubAllowedItemTypeCollection` object to be returned when the matching
`getAllowedItemTypes(repositoryId, repositoryFolderId, filter)` method is called in a test context. Use
the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetAllowedItemTypes(String repositoryId, String

   repositoryFolderId, ConnectApi.ContentHubItemType filter,

   ConnectApi.ContentHubAllowedItemTypeCollection result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   filter
```

Type: `ConnectApi.ContentHubItemType`

Item types. Values are:

**•** `Any` —Includes files and folders.

**•** `FilesOnly` —Includes files only.

**•** `FoldersOnly` —Includes folders only.

```
   result
```

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getAllowedItemTypes(repositoryId, repositoryFolderId, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`setTestGetAllowedItemTypes(communityId, repositoryId, repositoryFolderId,`**

```
  result)

```

Register a `ConnectApi.ContentHubAllowedItemTypeCollection` object to be returned when the matching
`getAllowedItemTypes(communityId, repositoryId, repositoryFolderId)` method is called in a test
context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetAllowedItemTypes(String communityId, String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubAllowedItemTypeCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getAllowedItemTypes(communityId, repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetAllowedItemTypes(communityId, repositoryId, repositoryFolderId,`**

```
  filter, result)

```

Register a `ConnectApi.ContentHubAllowedItemTypeCollection` object to be returned when the matching
`getAllowedItemTypes(communityId, repositoryId, repositoryFolderId, filter)` method is called
in a test context. Use the method with the same parameters or you receive an exception.


Apex Reference Guide ContentHub Class

API Version

40.0

Signature

```
   public static Void setTestGetAllowedItemTypes(String communityId, String repositoryId,

   String repositoryFolderId, ConnectApi.ContentHubItemType filter,

   ConnectApi.ContentHubAllowedItemTypeCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   filter
```

Type: `ConnectApi.ContentHubItemType`

Item types. Values are:

**•** `Any` —Includes files and folders.

**•** `FilesOnly` —Includes files only.

**•** `FoldersOnly` —Includes folders only.

```
   result
```

Type: `ConnectApi.ContentHubAllowedItemTypeCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getAllowedItemTypes(communityId, repositoryId, repositoryFolderId, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFilePreview(repositoryId, repositoryFileId, formatType, result)`**

Register a `ConnectApi.FilePreview` object to be returned when the matching `getFilePreview(repositoryId,`
`repositoryFileId, formatType)` method is called in a test context. Use the method with the same parameters or you
receive an exception.


Apex Reference Guide ContentHub Class

API Version

40.0

Signature

```
   public static Void setTestGetFilePreview(String repositoryId, String repositoryFileId,

   ConnectApi.FilePreviewFormat formatType, ConnectApi.FilePreview result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   result
```

Type: `ConnectApi.FilePreview`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFilePreview(repositoryId, repositoryFileId, formatType)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`setTestGetFilePreview(repositoryId, repositoryFileId, formatType,`**

```
  startPageNumber, endPageNumber, result)

```

Register a `ConnectApi.FilePreview` object to be returned when the matching `getFilePreview(repositoryId,`
`repositoryFileId, formatType, startPageNumber, endPageNumber)` method is called in a test context. Use
the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFilePreview(String repositoryId, String repositoryFileId,

   ConnectApi.FilePreviewFormat formatType, Integer startPageNumber, Integer endPageNumber,

   ConnectApi.FilePreview result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   startPageNumber
```

Type: Integer

The starting page number in the range of file preview URLs.

```
   endPageNumber
```

Type: Integer


Apex Reference Guide ContentHub Class

The ending page number in the range of file preview URLs.

```
   result
```

Type: `ConnectApi.FilePreview`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFilePreview(repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFilePreview(communityId, repositoryId, repositoryFileId, formatType,`**

```
  result)

```

Register a `ConnectApi.FilePreview` object to be returned when the matching `getFilePreview(communityId,`
`repositoryId, repositoryFileId, formatType)` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFilePreview(String communityId, String repositoryId, String

   repositoryFileId, ConnectApi.FilePreviewFormat formatType, ConnectApi.FilePreview

   result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.


Apex Reference Guide ContentHub Class

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   result
```

Type: `ConnectApi.FilePreview`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFilePreview(communityId, repositoryId, repositoryFileId, formatType)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFilePreview(communityId, repositoryId, repositoryFileId, formatType,`**

```
  startPageNumber, endPageNumber, result)

```

Register a `ConnectApi.FilePreview` object to be returned when the matching `getFilePreview(communityId,`
`repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber)` method is called
in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFilePreview(String communityId, String repositoryId, String

   repositoryFileId, ConnectApi.FilePreviewFormat formatType, Integer startPageNumber,

   Integer endPageNumber, ConnectApi.FilePreview result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ContentHub Class

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   formatType
```

Type: `ConnectApi.FilePreviewFormat`

Specifies the format of the file preview. Values are:

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

PDF previews are available for files of type DOC, DOCX, PPT, PPTX, TEXT, XLS, and XLSX. SVG files are generated on demand.

If you’re concerned that feature-rich SVG previews don’t work in your org, choose alternative file previews. To use JPG file previews,
enter _`general`_ in the Quick Find box in Setup. Select General Settings, and then select **Display alternative file previews** .

```
   startPageNumber
```

Type: Integer

The starting page number in the range of file preview URLs.

```
   endPageNumber
```

Type: Integer

The ending page number in the range of file preview URLs.

```
   result
```

Type: `ConnectApi.FilePreview`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFilePreview(communityId, repositoryId, repositoryFileId, formatType, startPageNumber, endPageNumber)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`setTestGetItemType(repositoryId, repositoryItemTypeId, result)`**

Register a `ConnectApi.ContentHubItemTypeDetail` object to be returned when the matching
`getItemType(repositoryId, repositoryItemTypeId)` method is called in a test context. Use the method with the
same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetItemType(String repositoryId, String repositoryItemTypeId,

   ConnectApi.ContentHubItemTypeDetail result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryItemTypeId
```

Type: String

The ID of the repository item type.

```
   result
```

Type: `ConnectApi.ContentHubItemTypeDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getItemType(repositoryId, repositoryItemTypeId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetItemType(communityId, repositoryId, repositoryItemTypeId, result)`**

Register a `ConnectApi.ContentHubItemTypeDetail` object to be returned when the matching
`getItemType(communityId, repositoryId, repositoryItemTypeId)` method is called in a test context. Use
the method with the same parameters or you receive an exception.

API Version

40.0


Apex Reference Guide ContentHub Class

Signature

```
   public static Void setTestGetItemType(String communityId, String repositoryId, String

   repositoryItemTypeId, ConnectApi.ContentHubItemTypeDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryItemTypeId
```

Type: String

The ID of the repository item type.

```
   result
```

Type: `ConnectApi.ContentHubItemTypeDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getItemType(communityId, repositoryId, repositoryItemTypeId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetPreviews(repositoryId, repositoryFileId, result)`**

Register a `ConnectApi.FilePreviewCollection` object to be returned when the matching
`getPreviews(repositoryId, repositoryFileId)` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetPreviews(String repositoryId, String repositoryFileId,

   ConnectApi.FilePreviewCollection result)

```

Parameters

```
   repositoryId
```

Type: String


Apex Reference Guide ContentHub Class

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   result
```

Type: `ConnectApi.FilePreviewCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getPreviews(repositoryId, repositoryFileId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetPreviews(communityId, repositoryId, repositoryFileId, result)`**

Register a `ConnectApi.FilePreviewCollection` object to be returned when the matching
`getPreviews(communityId, repositoryId, repositoryFileId)` method is called in a test context. Use the
method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetPreviews(String communityId, String repositoryId, String

   repositoryFileId, ConnectApi.FilePreviewCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   result
```

Type: `ConnectApi.FilePreviewCollection`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

getPreviews(communityId, repositoryId, repositoryFileId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositories(result)`**

Register a `ConnectApi.ContentHubRepositoryCollection` object to be returned when the matching
`getRepositories()` method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositories(ConnectApi.ContentHubRepositoryCollection

   result)

```

Parameters

```
   result
```

Type: `ConnectApi.ContentHubRepositoryCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositories()

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositories(communityId, result)`**

Register a `getRepositories(communityId)` object to be returned when the matching
`ConnectApi.ContentHubRepositoryCollection` method is called in a test context. Use the method with the same
parameters or you receive an exception.

API Version

40.0


Apex Reference Guide ContentHub Class

Signature

```
   public static Void setTestGetRepositories(String communityId,

   ConnectApi.ContentHubRepositoryCollection result)

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

Type: `ConnectApi.ContentHubRepositoryCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositories(communityId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositories(pageParam, pageSize, result)`**

Register a `ConnectApi.ContentHubRepositoryCollection` object to be returned when the matching
`getRepositories(pageParam, pageSize)` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositories(Integer pageParam, Integer pageSize,

   ConnectApi.ContentHubRepositoryCollection result)

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

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

```
   result
```

Type: `ConnectApi.ContentHubRepositoryCollection`


Apex Reference Guide ContentHub Class

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositories(pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositories(communityId, pageParam, pageSize, result)`**

Register a `ConnectApi.ContentHubRepositoryCollection` object to be returned when the matching
`getRepositories(communityId, pageParam, pageSize)` method is called in a test context. Use the method with
the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositories(String communityId, Integer pageParam, Integer

   pageSize, ConnectApi.ContentHubRepositoryCollection result)

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

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

```
   result
```

Type: `ConnectApi.ContentHubRepositoryCollection`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

getRepositories(communityId, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepository(repositoryId, result)`**

Register a `ConnectApi.ContentHubRepository` object to be returned when the matching
`getRepository(repositoryId)` method is called in a test context. Use the method with the same parameters or you receive
an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepository(String repositoryId,

   ConnectApi.ContentHubRepository result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   result
```

Type: `ConnectApi.ContentHubRepository`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepository(repositoryId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepository(communityId, repositoryId, result)`**

Register a `ConnectApi.ContentHubRepository` object to be returned when the matching
`getRepository(communityId, repositoryId)` method is called in a test context. Use the method with the same
parameters or you receive an exception.


Apex Reference Guide ContentHub Class

API Version

40.0

Signature

```
   public static Void setTestGetRepository(String communityId, String repositoryId,

   ConnectApi.ContentHubRepository result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   result
```

Type: `ConnectApi.ContentHubRepository`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepository(communityId, repositoryId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFile(repositoryId, repositoryFileId, result)`**

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`getRepositoryFile(repositoryId, repositoryFileId)` method is called in a test context. Use the method with
the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFile(String repositoryId, String repositoryFileId,

   ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   repositoryId
```

Type: String


Apex Reference Guide ContentHub Class

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFile(repositoryId, repositoryFileId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFile(repositoryId, repositoryFileId,`**

```
  includeExternalFilePermissionsInfo, result)

```

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching

```
   getRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)
```

method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFile(String repositoryId, String repositoryFileId,

   Boolean includeExternalFilePermissionsInfo, ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   includeExternalFilePermissionsInfo
```

Type: Boolean

Specifies whether to include permission information, such as whether the file is shared and what are the available permission types.

Managing external file permissions is supported for Google Drive, SharePoint Online, and OneDrive for Business.


Apex Reference Guide ContentHub Class

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFile(communityId, repositoryId, repositoryFileId, result)`**

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`getRepositoryFile(communityId, repositoryId, repositoryFileId)` method is called in a test context.
Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFile(String communityId, String repositoryId,

   String repositoryFileId, ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

getRepositoryFile(communityId, repositoryId, repositoryFileId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFile(communityId, repositoryId, repositoryFileId,`**

```
  includeExternalFilePermissionsInfo, result)

```

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching

```
   getRepositoryFile(communityId, repositoryId, repositoryFileId,
```

`includeExternalFilePermissionsInfo)` method is called in a test context. Use the method with the same parameters
or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFile(String communityId, String repositoryId,

   String repositoryFileId, Boolean includeExternalFilePermissionsInfo,

   ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   includeExternalFilePermissionsInfo
```

Type: Boolean

Specifies whether to include permission information, such as whether the file is shared and what are the available permission types.

Managing external file permissions is supported for Google Drive, SharePoint Online, and OneDrive for Business.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.


Apex Reference Guide ContentHub Class

Return Value

Type: Void

SEE ALSO:

getRepositoryFile(communityId, repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFolder(repositoryId, repositoryFolderId, result)`**

Register a `ConnectApi.RepositoryFolderDetail` object to be returned when the matching
`getRepositoryFolder(repositoryId, repositoryFolderId)` method is called in a test context. Use the method
with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolder(String repositoryId, String

   repositoryFolderId, ConnectApi.RepositoryFolderDetail result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.RepositoryFolderDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolder(repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ContentHub Class

##### **`setTestGetRepositoryFolder(communityId, repositoryId, repositoryFolderId,`**

```
  result)

```

Register a `ConnectApi.RepositoryFolderDetail` object to be returned when the matching
`getRepositoryFolder(communityId, repositoryId, repositoryFolderId)` method is called in a test
context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolder(String communityId, String repositoryId,

   String repositoryFolderId, ConnectApi.RepositoryFolderDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.RepositoryFolderDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolder(communityId, repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFolderItems(repositoryId, repositoryFolderId, result)`**

Register a `ConnectApi.RepositoryFolderItemsCollection` object to be returned when the matching
`getRepositoryFolderItems(repositoryId, repositoryFolderId)` method is called in a test context. Use the
method with the same parameters or you receive an exception.


Apex Reference Guide ContentHub Class

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolderItems(String repositoryId, String

   repositoryFolderId, ConnectApi.RepositoryFolderItemsCollection result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.RepositoryFolderItemsCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolderItems(repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFolderItems(communityId, repositoryId, repositoryFolderId,`**

```
  result)

```

Register a `ConnectApi.RepositoryFolderItemsCollection` object to be returned when the matching
`getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId)` method is called in a
test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolderItems(String communityId, String

   repositoryId, String repositoryFolderId, ConnectApi.RepositoryFolderItemsCollection

   result)

```


Apex Reference Guide ContentHub Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   result
```

Type: `ConnectApi.RepositoryFolderItemsCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam,`**

```
  pageSize, result)

```

Register a `ConnectApi.RepositoryFolderItemsCollection` object to be returned when the matching
`getRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam, pageSize)` method
is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolderItems(String repositoryId, String

   repositoryFolderId, Integer pageParam, Integer pageSize,

   ConnectApi.RepositoryFolderItemsCollection result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.


Apex Reference Guide ContentHub Class

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

```
   result
```

Type: `ConnectApi.RepositoryFolderItemsCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolderItems(repositoryId, repositoryFolderId, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetRepositoryFolderItems(communityId, repositoryId, repositoryFolderId,`**

```
  pageParam, pageSize, result)

```

Register a `ConnectApi.RepositoryFolderItemsCollection` object to be returned when the matching

```
   getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId, pageParam,
```

`pageSize)` method is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestGetRepositoryFolderItems(String communityId, String

   repositoryId, String repositoryFolderId, Integer pageParam, Integer pageSize,

   ConnectApi.RepositoryFolderItemsCollection result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String


Apex Reference Guide ContentHub Class

The ID of the repository.

```
   repositoryFolderId
```

Type: String

The ID of the repository folder.

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default page size is 25.

```
   result
```

Type: `ConnectApi.RepositoryFolderItemsCollection`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getRepositoryFolderItems(communityId, repositoryId, repositoryFolderId, pageParam, pageSize)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestUpdateRepositoryFile(communityId, repositoryId, repositoryFileId,`**

```
  file, fileData, result)

```

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`updateRepositoryFile(communityId, repositoryId, repositoryFileId, file, fileData)` method
is called in a test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestUpdateRepositoryFile(String communityId, String repositoryId,

   String repositoryFileId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput

   fileData, ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ContentHub Class

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

updateRepositoryFile(repositoryId, repositoryFileId, file)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestUpdateRepositoryFile(repositoryId, repositoryFileId, file, result)`**

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`updateRepositoryFile(repositoryId, repositoryFileId, file)` method is called in a test context. Use the
method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestUpdateRepositoryFile(String repositoryId, String

   repositoryFileId, ConnectApi.ContentHubItemInput file, ConnectApi.RepositoryFileDetail

   result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.


Apex Reference Guide ContentHub Class

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestUpdateRepositoryFile(repositoryId, repositoryFileId, file, fileData,`**

```
  result)

```

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)` method is called in a test
context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestUpdateRepositoryFile(String repositoryId, String

   repositoryFileId, ConnectApi.ContentHubItemInput file, ConnectApi.BinaryInput fileData,

   ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.

```
   file
```

Type: `ConnectApi.ContentHubItemInput`


Apex Reference Guide ContentHub Class

The item type ID and fields of the item type.

```
   fileData
```

Type: `ConnectApi.BinaryInput`

The binary file.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

updateRepositoryFile(communityId, repositoryId, repositoryFileId, file)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestUpdateRepositoryFile(communityId, repositoryId, repositoryFileId,`**

```
  file, result)

```

Register a `ConnectApi.RepositoryFileDetail` object to be returned when the matching
`updateRepositoryFile(communityId, repositoryId, repositoryFileId, file)` method is called in a
test context. Use the method with the same parameters or you receive an exception.

API Version

40.0

Signature

```
   public static Void setTestUpdateRepositoryFile(String communityId, String repositoryId,

   String repositoryFileId, ConnectApi.ContentHubItemInput file,

   ConnectApi.RepositoryFileDetail result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   repositoryId
```

Type: String

The ID of the repository.

```
   repositoryFileId
```

Type: String

The ID of the repository file.


### Apex Reference Guide ConversationApplicationDefinition Class

```
   file
```

Type: `ConnectApi.ContentHubItemInput`

The item type ID and fields of the item type.

```
   result
```

Type: `ConnectApi.RepositoryFileDetail`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

updateRepositoryFile(communityId, repositoryId, repositoryFileId, file, fileData)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ConversationApplicationDefinition Class

Access information about a conversation application definition.

Namespace

ConnectApi

#### ConversationApplicationDefinition Methods

### These methods are for ConversationApplicationDefinition . All methods are static.

IN THIS SECTION:

##### getConversationApplicationDefinition(integrationName)

Get information about an integration’s conversation application definition and the associated bot.

##### **`getConversationApplicationDefinition(integrationName)`**

Get information about an integration’s conversation application definition and the associated bot.

API Version

54.0

Requires Chatter

No


### Apex Reference Guide Datacloud Class

Signature

```
   public static ConnectApi.ConversationApplicationDefinitionDetailRespresentation

   getConversationApplicationDefinition(String integrationName)

```

Parameters

```
   integrationName
```

Type: String

Name of the conversation application.

Return Value

Type: `ConnectApi.ConversationApplicationDefinitionDetailRespresentation`

Usage

To access this method, enable the bot feature, and the user must be an admin or have the Manage Bots or Manage Bots Training Data
user permissions.

### Datacloud Class

Purchase Data.com contact or company records, and retrieve purchase information.

Namespace

ConnectApi

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

IN THIS SECTION:

#### Datacloud Methods
### These methods are for Datacloud . All methods are static.

#### Datacloud Methods

### These methods are for Datacloud . All methods are static.

IN THIS SECTION:

getCompaniesFromOrder(orderId, pageSize, page)
Get a list of purchased company records for an order.

getCompany(companyId)
Get a company record.


Apex Reference Guide Datacloud Class

getContact(contactId)
Get a contact.

getContactsFromOrder(orderId, page, pageSize)
Get a list of purchased contacts for an order.

getOrder(orderId)
Get an order.

getUsage(userId)
Get purchase usage information for a user.

postOrder(orderInput)
Purchase records that are listed in an input file.

##### **`getCompaniesFromOrder(orderId, pageSize, page)`**

Get a list of purchased company records for an order.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudCompanies getCompaniesFromOrder(String orderId, String

   pageSize, String page)

```

Parameters

```
   orderId
```

Type: String

ID of an order.

```
   page
```

Type: Integer

Number of the page that you want returned.

```
   pageSize
```

Type: Integer

Number of companies to show on a page. The default _`pageSize`_ is 25.

Return Value

Type: `ConnectApi.DatacloudCompanies`


Apex Reference Guide Datacloud Class

##### **`getCompany(companyId)`**

Get a company record.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudCompany getCompany(String companyId)

```

Parameters

```
   companyId
```

Type: String

ID of a company in the Data.com database.

Return Value

Type: `ConnectApi.DatacloudCompany`

##### **`getContact(contactId)`**

Get a contact.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudContact getContact(String contactId)

```

Parameters

```
   contactId
```

Type: String

ID of a contact in the Data.com database.

Return Value

Type: `ConnectApi.DatacloudContact`


Apex Reference Guide Datacloud Class

##### **`getContactsFromOrder(orderId, page, pageSize)`**

Get a list of purchased contacts for an order.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudContacts getContactsFromOrder(String orderId, String

   page, String pageSize)

```

Parameters

```
   orderId
```

Type: String

ID of an order.

```
   page
```

Type: Integer

Number of the page that you want returned.

```
   pageSize
```

Type: Integer

Number of contacts to show on a page. The default _`pageSize`_ is 25.

Return Value

Type: `ConnectApi.DatacloudContacts`

##### **`getOrder(orderId)`**

Get an order.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudOrder getOrder(String orderId)

```


Apex Reference Guide Datacloud Class

Parameters

```
   orderId
```

Type: String

ID of an order.

Return Value

Type: `ConnectApi.DatacloudOrder`

##### **`getUsage(userId)`**

Get purchase usage information for a user.

API Version

32.0

Requires Chatter

No

Signature

```
   public static ConnectApi.DatacloudPurchaseUsage getUsage(String userId)

```

Parameters

```
   userId
```

Type: String

ID of a user.

Return Value

Type: `ConnectApi.DatacloudPurchaseUsage`

##### **`postOrder(orderInput)`**

Purchase records that are listed in an input file.

API Version

32.0

Requires Chatter

No


### Apex Reference Guide EinsteinLLM Class

Signature

```
   public static ConnectApi.DatacloudOrder postOrder(ConnectApi.DatacloudOrderInput

   orderInput)

```

Parameters

```
   orderInput
```

Type: `ConnectApi.DatacloudOrderInput`

A list that contains IDs for the contacts or companies that you want to see.

Return Value

Type: `ConnectApi.DatacloudOrder`

Example

```
   ConnectApi.DatacloudOrderInput inputOrder=new ConnectApi.DatacloudOrderInput();

   List<String> ids=new List<String>();

   ids.add('1234');

   inputOrder.companyIds=ids;

   ConnectApi.DatacloudOrder datacloudOrderRep = ConnectApi.Datacloud.postOrder(inputOrder);

### EinsteinLLM Class

```

Get a list of prompt templates and generate LLM responses for prompt templates.

Namespace

ConnectApi

#### EinsteinLLM Methods

### These methods are for EinsteinLLM . All methods are static.

IN THIS SECTION:

generateMessagesForPromptTemplate(promptTemplateDevName, promptTemplateGenerationsInput)
Generates a response using the specified prompt template and input parameters.

getPromptTemplates(query, sortBy, offset, pageLimit, fields, type, relatedEntity, isActive)
Get a list of prompt templates using the specified filters.

```
  generateMessagesForPromptTemplate(promptTemplateDevName, promptTemplate

  GenerationsInput)

```

Generates a response using the specified prompt template and input parameters.


Apex Reference Guide EinsteinLLM Class

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.EinsteinPromptTemplateGenerationsRepresentation

   generateMessagesForPromptTemplate(String promptTemplateDevName,

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptTemplateGenerationsInput)

```

Parameters

```
   promptTemplateDevName
```

Type: String

Developer name or ID of a prompt template record.

```
   promptTemplateGenerationsInput
```

Type: `ConnectApi.EinsteinPromptTemplateGenerationsInput`

Input for generating a response using the specified prompt template.

Return Value

Type: `ConnectApi.EinsteinPromptTemplateGenerationsRepresentation`

Example

In this example, call `generateMessagesForPromptTemplate(promptTemplateDevName,`
`promptTemplateGenerationsInput)` [to resolve a Sales Email prompt template. For more examples, see Resolve a Prompt](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_resolve_prompt_template.htm)
[Template.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_examples_resolve_prompt_template.htm)

```
   // Create input

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptGenerationsInput = new

   ConnectApi.EinsteinPromptTemplateGenerationsInput();

   promptGenerationsInput.isPreview = false;

   // Build input map

   Map<String,ConnectApi.WrappedValue> valueMap = new Map<String,ConnectApi.WrappedValue>();

   Map<String, String> recipientEntityRecordIdMap = new Map<String, String>();

   recipientEntityRecordIdMap.put('id', '00Qxx000002ToPvEAK');

   Map<String, String> senderEntityRecordIdMap = new Map<String, String>();

   senderEntityRecordIdMap.put('id', '005xx000001XiWLAA0');

   ConnectApi.WrappedValue recipientEntityWrappedValue = new ConnectApi.WrappedValue();

   recipientEntityWrappedValue.value = recipientEntityRecordIdMap;

   ConnectApi.WrappedValue senderEntityWrappedValue = new ConnectApi.WrappedValue();

   senderEntityWrappedValue.value = senderEntityRecordIdMap;

```


Apex Reference Guide EinsteinLLM Class

```
   valueMap.put('Input:Account', recipientEntityWrappedValue);

   valueMap.put('Input:Recipient', recipientEntityWrappedValue);

   valueMap.put('Input:Sender', senderEntityWrappedValue);

   promptGenerationsInput.inputParams = valueMap;

   // Set additional configuration values

   promptGenerationsInput.additionalConfig = new ConnectApi.EinsteinLlmAdditionalConfigInput();

   promptGenerationsInput.additionalConfig.applicationName =

   'PromptTemplateGenerationsInvocable';

   // Call the service

   ConnectApi.EinsteinPromptTemplateGenerationsRepresentation generationsOutput =

   ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate('0hfxx0000000KTNAA2',

   promptGenerationsInput);

   // Consume response

   System.debug('Prompt Testing: ' + generationsOutput.prompt);

##### **`getPromptTemplates(query, sortBy, offset, pageLimit, fields, type,`**

  relatedEntity, isActive)

```

Get a list of prompt templates using the specified filters.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.EinsteinPromptRecordCollectionOutputRepresentation

   getPromptTemplates(String query, String sortBy, Integer offset, Integer pageLimit,

   List<String> fields, String type, String relatedEntity, Boolean isActive)

```

Parameters

```
   query
```

Type: String

User-entered search string. If `null`, all prompt template records are returned.

```
   sortBy
```

Type: String

Field to sort the returned prompt template records by, such as `createdDate` . If `null`, records are returned in the order they’re
retrieved.

```
   offset
```

Type: Integer


Apex Reference Guide EinsteinLLM Class

Used for pagination. Number of rows to skip between returned prompt template records. The default value is `0` .

```
   pageLimit
```

Type: Integer

Used for pagination. Maximum number of prompt template records returned per page. The default value is `50` .

```
   fields
```

Type: List<String>

Comma-separated list of prompt template record fields to return, such as `createdDate` . If `null`, all fields are returned.

```
   type
```

Type: String

Prompt template type to filter records by, such as `einstein_gpt__salesEmail` . If `null`, records of all types are returned.

```
   relatedEntity
```

Type: String

Related entity to filter records by, such as `Contact` . If `null`, all records with all related entities are returned.

```
   isActive
```

Type: Boolean

Specifies whether to return active prompt templates only. The default is `false` .

Return Value

Type: `ConnectApi.EinsteinPromptRecordCollectionOutputRepresentation`

Usage

To get a list of prompt templates, you must have Einstein Generative AI enabled and the Execute Prompt Templates user permission.

Example

```
   ConnectApi.EinsteinPromptRecordCollectionOutputRepresentation promptTemplateList =

   ConnectApi.EinsteinLLM.getPromptTemplates('Summarize', 'CreatedDate', 0, 5, null,

   'einstein_gpt__flex', null, true);

   // Get information from the prompt templates in the list

      if (promptTemplateList != null && promptTemplateList.promptRecords != null) {

      for (ConnectApi.EinsteinPromptRecordRepresentation promptTemplate :

   promptTemplateList.promptRecords) {

        System.debug('Prompt Template ID: ' + promptTemplate.id);

        for (String fieldName : promptTemplate.fields.keySet()) {

           System.debug('Field Name: ' + fieldName + ', Value: ' +

   promptTemplate.fields.get(fieldName).value);

        }

      }

   } else {

      System.debug('No prompt templates found.');

   }

```


### Apex Reference Guide EmailMergeFieldService Class EmailMergeFieldService Class

Extract a list of merge fields for an object. A merge field is a field you can put in an email template, mail merge template, custom link,
or formula to incorporate values from a record.

Namespace

ConnectApi

#### EmailMergeFieldService Methods

### These methods are for EmailMergeFieldService . All methods are static.

IN THIS SECTION:

##### getMergeFields(objectApiNames)

Extract the merge fields for a specific object.

##### **`getMergeFields(objectApiNames)`**

Extract the merge fields for a specific object.

API Version

39.0

Requires Chatter

No

Signature

```
   public static ConnectApi.EmailMergeFieldInfo getMergeFields(List<String> objectApiNames)

```

Parameters

```
   objectApiNames
```

Type: List<String>

The API names for the objects being referenced.

Return Value

Type: `ConnectApi.EmailMergeFieldInfo`

### EmployeeProfiles Class

Get, set and crop, and delete employee banner photos and photos.


Apex Reference Guide EmployeeProfiles Class

Namespace

ConnectApi

#### EmployeeProfiles Methods These methods are for EmployeeProfiles . All methods are static.

IN THIS SECTION:

##### deleteBannerPhoto(employeeId)

Delete an employee’s banner photo.

deletePhoto(employeeId)
Delete an employee’s photo.

getBannerPhoto(employeeId)
Get an employee’s banner photo.

getPhoto(employeeId)
Get an employee’s photo.

setBannerPhoto(employeeId, fileId, versionNumber)
Set an uploaded file as an employee’s banner photo.

setBannerPhoto(employeeId, fileUpload)
Set a file that hasn’t been uploaded as an employee’s banner photo.

setBannerPhotoWithAttributes(employeeId, bannerPhoto)
Set and crop an uploaded file as an employee’s banner photo.

setBannerPhotoWithAttributes(employeeId, bannerPhoto, fileUpload)
Set and crop a file that hasn’t been uploaded as an employee’s banner photo.

setPhoto(employeeId, fileId, versionNumber)
Set an uploaded file as an employee’s photo.

setPhoto(employeeId, fileUpload)
Set a file that hasn’t been uploaded as an employee’s photo.

setPhotoWithAttributes(employeeId, photo)
Set and crop an uploaded file as an employee’s photo.

setPhotoWithAttributes(employeeId, photo, fileUpload)
Set and crop a file that hasn’t been uploaded as an employee’s photo.

##### **`deleteBannerPhoto(employeeId)`**

Delete an employee’s banner photo.

API Version

51.0


Apex Reference Guide EmployeeProfiles Class

Requires Chatter

No

Signature

```
   public static Void deleteBannerPhoto(String employeeId)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

Return Value

Type: Void

##### **`deletePhoto(employeeId)`**

Delete an employee’s photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static Void deletePhoto(String employeeId)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

Return Value

Type: Void

##### **`getBannerPhoto(employeeId)`**

Get an employee’s banner photo.

API Version

51.0


Apex Reference Guide EmployeeProfiles Class

Requires Chatter

No

Signature

```
   public static ConnectApi.BannerPhoto getBannerPhoto(String employeeId)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

Return Value

Type: `ConnectApi.BannerPhoto`

##### **`getPhoto(employeeId)`**

Get an employee’s photo.

API Version

51.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Photo getPhoto(String employeeId)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

Return Value

Type: `ConnectApi.Photo`

##### **`setBannerPhoto(employeeId, fileId, versionNumber)`**

Set an uploaded file as an employee’s banner photo.


Apex Reference Guide EmployeeProfiles Class

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String employeeId, String fileId,

   Integer versionNumber)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   fileId
```

Type: String

ID of the uploaded file to use as the employee banner photo. The file must be an image and be smaller than 2 GB.

```
   versionNumber
```

Type: Integer

Version number of the file. Specify an existing version number or, to get the latest version, specify `null` .

Return Value

Type: `ConnectApi.BannerPhoto`

##### **`setBannerPhoto(employeeId, fileUpload)`**

Set a file that hasn’t been uploaded as an employee’s banner photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhoto(String employeeId,

   ConnectApi.BinaryInput fileUpload)

```


Apex Reference Guide EmployeeProfiles Class

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.BannerPhoto`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhotoWithAttributes(employeeId, bannerPhoto)`**

Set and crop an uploaded file as an employee’s banner photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String employeeId,

   ConnectApi.BannerPhotoInput bannerPhoto)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   bannerPhoto
```

Type: `ConnectApi.BannerPhotoInput`

A `ConnectApi.BannerPhotoInput` object that specifies the ID and version of the file, and how to crop the file.

Return Value

Type: `ConnectApi.BannerPhoto`


Apex Reference Guide EmployeeProfiles Class

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setBannerPhotoWithAttributes(employeeId, bannerPhoto, fileUpload)`**

Set and crop a file that hasn’t been uploaded as an employee’s banner photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BannerPhoto setBannerPhotoWithAttributes(String employeeId,

   ConnectApi.BannerPhotoInput bannerPhoto, ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

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

##### **`setPhoto(employeeId, fileId, versionNumber)`**

Set an uploaded file as an employee’s photo.

API Version

51.0


Apex Reference Guide EmployeeProfiles Class

Requires Chatter

No

Signature

```
   public static ConnectApi.Photo setPhoto(String employeeId, String fileId, Integer

   versionNumber)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   fileId
```

Type: String

ID of the uploaded file to use as the employee photo. The file must be an image and be smaller than 2 GB.

```
   versionNumber
```

Type: Integer

Version number of the file. Specify an existing version number or, to get the latest version, specify `null` .

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhoto(employeeId, fileUpload)`**

Set a file that hasn’t been uploaded as an employee’s photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Photo setPhoto(String employeeId, ConnectApi.BinaryInput

   fileUpload)

```


Apex Reference Guide EmployeeProfiles Class

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   fileUpload
```

Type: `ConnectApi.BinaryInput`

File to use as the photo. The content type must be usable as an image.

Return Value

Type: `ConnectApi.Photo`

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(employeeId, photo)`**

Set and crop an uploaded file as an employee’s photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String employeeId,

   ConnectApi.PhotoInput photo)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

```
   photo
```

Type: `ConnectApi.PhotoInput`

A `ConnectApi.PhotoInput` object specifying the file ID, version number, and cropping parameters.

Return Value

Type: `ConnectApi.Photo`


### Apex Reference Guide Exchanges Class

Usage

Photos are processed asynchronously and might not be visible right away.

##### **`setPhotoWithAttributes(employeeId, photo, fileUpload)`**

Set and crop a file that hasn’t been uploaded as an employee’s photo.

API Version

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.Photo setPhotoWithAttributes(String employeeId,

   ConnectApi.PhotoInput photo, ConnectApi.BinaryInput fileUpload)

```

Parameters

```
   employeeId
```

Type: String

ID of the employee.

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

### Exchanges Class

Preview and submit cart to exchange orders.

Namespace

ConnectApi


Apex Reference Guide Exchanges Class

#### Exchanges Methods These methods are for Exchanges . All methods are static.

IN THIS SECTION:

##### previewCartToExchangeOrder(previewCartToExchangeOrderInput)

Retrieves a preview of an exchange order, taking into account the order summary balance and the difference between the return
order and the cart that represents the exchange order.

##### submitCartToExchangeOrder(submitCartToExchangeOrderInput)

Creates an exchange order summary, based on the return order and the cart used for exchanges. The new exchange order summary
is attached to the original order summary (created before any exchanges occurred). You can also provide optional payment information
and optional information about order summary sequences, which affect the newly created exchange order summary.

##### **`previewCartToExchangeOrder(previewCartToExchangeOrderInput)`**

Retrieves a preview of an exchange order, taking into account the order summary balance and the difference between the return order
and the cart that represents the exchange order.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.PreviewCartToExchangeOrderOutputRepresentation

   previewCartToExchangeOrder(ConnectApi.PreviewCartToExchangeOrderInputRepresentation

   previewCartToExchangeOrderInput)

```

Parameters

```
   previewCartToExchangeOrderInput
```

Type: `ConnectApi.PreviewCartToExchangeOrderInputRepresentation on page 2101`

Information required to preview a cart to exchange order.

Return Value

Type: `ConnectApi.PreviewCartToExchangeOrderOutputRepresentation on page 2469`

##### **`submitCartToExchangeOrder(submitCartToExchangeOrderInput)`**

Creates an exchange order summary, based on the return order and the cart used for exchanges. The new exchange order summary is
attached to the original order summary (created before any exchanges occurred). You can also provide optional payment information
and optional information about order summary sequences, which affect the newly created exchange order summary.


### Apex Reference Guide ExtendedCommerceDelivery Class

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.SubmitCartToExchangeOrderOutputRepresentation

   submitCartToExchangeOrder(ConnectApi.SubmitCartToExchangeOrderInputRepresentation

   submitCartToExchangeOrderInput)

```

Parameters

```
   submitCartToExchangeOrderInput
```

Type: `ConnectApi.SubmitCartToExchangeOrderInputRepresentation on page 2112`

Information required to submit a cart to exchange order.

Return Value

Type: `ConnectApi.SubmitCartToExchangeOrderOutputRepresentation on page 2541`

### ExtendedCommerceDelivery Class

Access information about delivery estimation.

Namespace

ConnectApi

#### ExtendedCommerceDelivery Methods

### This method is for ExtendedCommerceDelivery . It is static.

IN THIS SECTION:

##### estimateDeliveryDate(estimateDeliveryDateInput, externalReference)

Forecast an expected delivery date and time based on delivery estimation settings and the selected shipping carrier method. Provide
information on when a package is expected to be shipped and delivered.

##### **`estimateDeliveryDate(estimateDeliveryDateInput, externalReference)`**

Forecast an expected delivery date and time based on delivery estimation settings and the selected shipping carrier method. Provide
information on when a package is expected to be shipped and delivered.

API Version

63.0


### Apex Reference Guide ExternalEmailServices Class

Available to Guest Users

63.0

Requires Chatter

No

Signature

```
   public static ConnectApi.EstimateDeliveryDateOutputRepresentation

   estimateDeliveryDate(ConnectApi.EstimateDeliveryDateInputRepresentation

   estimateDeliveryDateInput, String externalReference)

```

Parameters

```
   estimateDeliveryDateInput
```

Type: Datetime

ConnectApi.EstimateDeliveryDateInputRepresentation on page 2043

Estimated delivery date.

```
   externalReference
```

Type: String

Delivery estimation setup external reference ID.

Return Value

Type: ConnectApi.EstimateDeliveryDateOutputRepresentation on page 2313

### ExternalEmailServices Class

Access information about integration with external email services, such as sending email within Salesforce through an external email
account.

Namespace

ConnectApi

#### ExternalEmailServices Methods

### These methods are for ExternalEmailService . All methods are static.

IN THIS SECTION:

##### getUserOauthInfo(landingPage)

Get information about whether an external email service has been authorized to send email on behalf of a user.

##### **`getUserOauthInfo(landingPage)`**

Get information about whether an external email service has been authorized to send email on behalf of a user.


### Apex Reference Guide ExternalManagedAccount Class

API Version

37.0

Requires Chatter

No

Signature

```
   public static getUserOauthInfo(String landingPage)

```

Parameters

```
   landingPage
```

Type: String

The landing page that the user starts on when they are finished with the OAuth authorization process.

Return Value

Type: `ConnectApi.UserOauthInfo`

SEE ALSO:

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

### ExternalManagedAccount Class

Get externally managed accounts.

Namespace

ConnectApi

#### ExternalManagedAccount Methods

### These methods are for ExternalManagedAccount . All methods are static.

IN THIS SECTION:

getCommunitiesExternalManagedAccounts(communityId)
Get externally managed accounts available to the context user across all Experience Cloud sites.

getCommunitiesExternalManagedAccounts(communityId, includeMyAccount)
Get externally managed accounts available to the context user, including the context user’s account, across all Experience Cloud
sites.

getExternalManagedAccounts(webstoreId)
Get externally managed accounts for a store.

getExternalManagedAccounts(webstoreId, includeMyAccount)
Get externally managed accounts, including the context user’s account, for a store.


Apex Reference Guide ExternalManagedAccount Class

##### **`getCommunitiesExternalManagedAccounts(communityId)`**

Get externally managed accounts available to the context user across all Experience Cloud sites.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalManagedAccountCollectionOutput

   getCommunitiesExternalManagedAccounts(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Note: Regardless of the ID specified, this method returns externally managed accounts available to the context user across
all Experience Cloud sites.

Return Value

Type: `ConnectApi.ExternalManagedAccountCollectionOutput`

##### **`getCommunitiesExternalManagedAccounts(communityId, includeMyAccount)`**

Get externally managed accounts available to the context user, including the context user’s account, across all Experience Cloud sites.

API Version

53.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalManagedAccountCollectionOutput

   getCommunitiesExternalManagedAccounts(String communityId, Boolean includeMyAccount)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ExternalManagedAccount Class

ID for an Experience Cloud site, `internal`, or `null` .

Note: Regardless of the ID specified, this method returns externally managed accounts available to the context user across
all Experience Cloud sites.

```
   includeMyAccount
```

Type: Boolean

Specifies whether to return the context user’s account ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ExternalManagedAccountCollectionOutput`

##### **`getExternalManagedAccounts(webstoreId)`**

Get externally managed accounts for a store.

API Version

49.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ExternalManagedAccountCollectionOutput

   getExternalManagedAccounts(String webstoreId)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

Return Value

Type: `ConnectApi.ExternalManagedAccountCollectionOutput`

##### **`getExternalManagedAccounts(webstoreId, includeMyAccount)`**

Get externally managed accounts, including the context user’s account, for a store.

API Version

53.0

Requires Chatter

No


### Apex Reference Guide FieldService Class

Signature

```
   public static ConnectApi.ExternalManagedAccountCollectionOutput

   getExternalManagedAccounts(String webstoreId, Boolean includeMyAccount)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   includeMyAccount
```

Type: Boolean

Specifies whether to return the context user’s account ( `true` ) or not ( `false` ). The default value is `false` .

Return Value

Type: `ConnectApi.ExternalManagedAccountCollectionOutput`

### FieldService Class

Preview and create shifts from a pattern.

Namespace

ConnectApi

#### FieldService Methods

### These methods are for FieldService . All methods are static.

IN THIS SECTION:

##### createShiftsFromPattern(shiftsFromPatternInput, shiftPatternId)

Create up to 2,000 shifts from a pattern.

previewShiftsFromPattern(shiftsFromPatternInput, shiftPatternId)
Preview up to 2,000 shifts from a pattern.

##### **`createShiftsFromPattern(shiftsFromPatternInput, shiftPatternId)`**

Create up to 2,000 shifts from a pattern.

API Version

51.0

Requires Chatter

Yes


Apex Reference Guide FieldService Class

Signature

```
   public static ConnectApi.ShiftsFromPattern

   createShiftsFromPattern(ConnectApi.ShiftsFromPatternInput shiftsFromPatternInput, String

   shiftPatternId)

```

Parameters

```
   shiftsFromPatternInput
```

Type: `ConnectApi.ShiftsFromPatternInput`

A `ConnectApi.ShiftsFromPatternInput` object providing the pattern.

```
   shiftPatternId
```

Type: String

ID of the shift pattern.

Return Value

Type: `ConnectApi.ShiftsFromPattern`

##### **`previewShiftsFromPattern(shiftsFromPatternInput, shiftPatternId)`**

Preview up to 2,000 shifts from a pattern.

API Version

51.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ShiftsFromPattern

   previewShiftsFromPattern(ConnectApi.ShiftsFromPatternInput shiftsFromPatternInput,

   String shiftPatternId)

```

Parameters

```
   shiftsFromPatternInput
```

Type: `ConnectApi.ShiftsFromPatternInput`

A `ConnectApi.ShiftsFromPatternInput` object providing the pattern.

```
   shiftPatternId
```

Type: String

ID of the shift pattern.

Return Value

Type: `ConnectApi.ShiftsFromPattern`


### Apex Reference Guide FlowApprovalProcesses Class FlowApprovalProcesses Class

Get the status and available actions for flow approval processes.

Namespace

ConnectApi

#### FlowApprovalProcesses Methods

### These methods are for FlowApprovalProcesses . All methods are static.

IN THIS SECTION:

##### getFlowApprovalProcessWithStatus(relatedRecordId, processNames)

Get the status and available actions for flow approval processes.

##### **`getFlowApprovalProcessWithStatus(relatedRecordId, processNames)`**

Get the status and available actions for flow approval processes.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FlowApprovalProcessCollection

   getFlowApprovalProcessWithStatus(String relatedRecordId, List<String> processNames)

```

Parameters

```
   relatedRecordId
```

Type: String

The ID of the related record associated with the approval submission.

```
   processNames
```

Type: List<String>

A list of flow approval process names.

Return Value

Type: `ConnectApi.FlowApprovalProcessCollection`


### Apex Reference Guide FulfillmentOrder Class FulfillmentOrder Class

Fulfill orders in Order Management.

Namespace

ConnectApi

#### FulfillmentOrder Methods

### These methods are for FulfillmentOrder . All methods are static.

IN THIS SECTION:

##### cancelFulfillmentOrderLineItems(fulfillmentOrderId, cancelFulfillmentOrderLineItemsInput)

Cancel FulfillmentOrderLineItems from a FulfillmentOrder. This action doesn’t cancel the associated OrderItemSummaries, so reallocate
the canceled quantities to a new FulfillmentOrder.

createFulfillmentOrders(fulfillmentOrderInput)
Create one or more FulfillmentOrders and FulfillmentOrderLineItems for an OrderDeliveryGroupSummary, which defines a delivery
method and recipient for an OrderSummary. You specify the OrderItemSummaries to allocate, which can be fulfilled from different
locations. Specifying multiple fulfillment groups creates one FulfillmentOrder for each location. For each OrderItemSummary, a
FulfillmentOrderLineItem is created and assigned to the corresponding FulfillmentOrder.

createInvoice(fulfillmentOrderId, invoiceInput)
Create an invoice for a FulfillmentOrder that doesn’t have one.

createMultipleFulfillmentOrder(multipleFulfillmentOrderInput)
