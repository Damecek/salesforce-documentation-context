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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFeed(communityId, feedType, subjectId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.ChatterStreamPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchStreams(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItems(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedItemPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedItemsInFilterFeed(communityId, feedType, subjectId, keyPrefix, recentCommentCount, density, pageParam,
pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItems(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Specify the test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedItemPage`

Specify the test feed item page.

Return Value

Type: Void

SEE ALSO:

searchFeedItemsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
specified as `null` .

Return Value

Type: `ConnectApi.ChatterGroupPage`


Apex Reference Guide ChatterGroups Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchGroups(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Specifies the string to search. The search string must contain at least two characters, not including wildcards. See Wildcards. Can be](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)
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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)


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

[This method creates an EntitySubscription record, which requires certain permissions. See the Usage section of the EntitySubscription](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_entitysubscription.htm)
object for more information.

SEE ALSO:

[Unfollow a Record](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_unfollow_record.htm)


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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.UserPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchUsers(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.UserPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchUsers(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

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

Type: `ConnectApi.ContractInputRepresentation on page 2065`

Input payload to create contract.

Return Value

Type: `ConnectApi.ContractOutputRepresentation on page 2325`


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

Type: `ConnectApi.ContractInputRepresentation on page 2065`

Input payload to update contract.

Return Value

Type: `ConnectApi.ContractOutputRepresentation on page 2325`

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

