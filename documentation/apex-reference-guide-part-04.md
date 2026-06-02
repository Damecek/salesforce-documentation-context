Get a page of top unanswered questions for the context user in an Experience Cloud site.

getTopUnansweredQuestions(communityId, filter, pageSize) (Pilot)
Get a page of filtered top unanswered questions for the context user in an Experience Cloud site.

getVotesForComment(communityId, commentId, vote)
Get the first page of users who upvoted or downvoted a comment.


Apex Reference Guide ChatterFeeds Class

getVotesForComment(communityId, commentId, vote, pageParam, pageSize)
Get a page of users who upvoted or downvoted a comment.

getVotesForFeedElement(communityId, feedElementId, vote)
Get the first page of users who upvoted or downvoted a feed element.

getVotesForFeedElement(communityId, feedElementId, vote, pageParam, pageSize)
Get a page of users who upvoted or downvoted a feed element.

isCommentEditableByMe(communityId, commentId)
Discover whether the context user can edit a comment.

isFeedElementEditableByMe(communityId, feedElementId)
Discover whether the context user can edit a feed element.

isModified(communityId, feedType, subjectId, since)
Discover whether a news feed has been updated or changed. Use this method to poll a news feed for updates.

likeComment(communityId, commentId)
Like a comment for the context user.

likeFeedElement(communityId, feedElementId)
Like a feed element.

postCommentToFeedElement(communityId, feedElementId, text)
Post a plain-text comment to a feed element.

postCommentToFeedElement(communityId, feedElementId, comment, feedElementFileUpload)
Post a rich-text comment to a feed element. Use this method to include mentions and to attach a file.

postFeedElement(communityId, subjectId, feedElementType, text)
Post a plain-text feed element.

postFeedElement(communityId, feedElement)
Post a rich-text feed element. Include mentions and hashtag topics, attach already uploaded files to a feed element, and associate
action link groups with a feed element. You can also use this method to share a feed element and add a comment.

postFeedElementBatch(communityId, feedElements)
Post a list of feed elements.

publishDraftFeedElement(communityId, feedElementId, feedElement)
Publish a draft feed element.

searchFeedElements(communityId, q)
Get the first page of feed elements that match the search criteria.

searchFeedElements(communityId, q, sortParam)
Get the first page of sorted feed elements that match the search criteria.

searchFeedElements(communityId, q, threadedCommentsCollapsed)
Get the feed elements and comments that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize)
Get a page of feed elements that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize, sortParam)
Get a page of sorted feed elements that match the search criteria.

searchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed)
Get a page of feed elements with comments in a threaded style that match the search criteria.


Apex Reference Guide ChatterFeeds Class

searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam)
Get a page of sorted feed elements that match the search criteria. Each feed element includes no more than the specified number
of comments.

searchFeedElementsInFeed(communityId, feedType, q)
Get the feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` feeds that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria. Each feed element includes no more than the specified number of
comments.

searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q, filter)
Get a page of sorted and filtered feed elements from the `Home` feed that match the search criteria. Each feed element includes no
more than the specified number of comments.

searchFeedElementsInFeed(communityId, feedType, subjectId, q)
Search up to 5,000 of the most recent feed elements in a feed for a subject ID that match the search string. Feed elements are
returned in order of most recent activity.

searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from a feed for a record or user that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
q)
Get a page of sorted feed elements from a feed that match the search criteria. Each feed element includes no more than the specified
number of comments.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter)
Get a page of sorted and filtered feed elements from a `UserProfile` feed that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
customFilter)
Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly)
Get a page of sorted feed elements from a feed for a record or user that match the search criteria. Each feed element includes no
more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, filter)
Get a page of sorted and filtered feed elements from a feed for a record or user that match the search criteria. Each feed element
includes no more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience
Cloud site) users only.

searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam, q,
showInternalOnly, customFilter)
Get a page of sorted and filtered feed elements from a case feed that match the search criteria.


Apex Reference Guide ChatterFeeds Class

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)
Get the feed elements from a feed filtered by a key prefix that match the search criteria.

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q)
Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria.

searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize, sortParam,
q)
Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria. Each feed element includes no
more than the specified number of comments.

searchStreams(communityId, q)
Search the Chatter feed streams for the context user.

searchStreams(communityId, q, sortParam)
Search and sort the Chatter feed streams for the context user.

searchStreams(communityId, q, pageParam, pageSize)
Search the Chatter feed streams for the context user and return a page of results.

searchStreams(communityId, q, pageParam, pageSize, sortParam)
Search the Chatter feed streams for the context user and return a sorted page of results.

searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)
Search the Chatter feed streams from all Experience Cloud sites for the context user and return a sorted page of results.

setCommentIsVerified(communityId, commentId, isVerified)
Mark a comment as verified or unverified.

setCommentIsVerifiedByAnonymized(communityId, commentId, isVerified, isVerifiedByAnonymized)
Mark a comment as verified by an anonymous user.

setCommentVote(communityId, commentId, upDownVote)
Upvote or downvote a comment.

setFeedCommentStatus(communityId, commentId, status)
Set the status of a comment.

setFeedElementIsClosed(communityId, feedElementId, isClosed)
Set a feed element to closed.

setFeedElementVote(communityId, feedElementId, upDownVote)
Upvote or downvote a feed element.

setFeedEntityStatus(communityId, feedElementId, status)
Set the status of a feed post.

setIsMutedByMe(communityId, feedElementId, isMutedByMe)
Mute or unmute a feed element.

setIsReadByMe(communityId, feedElementId, readBy)
Mark a feed element as read for the context user using an input class.

setIsReadByMe(communityId, feedElementId, isReadByMe)
Mark a feed element as read for the context user.

updateComment(communityId, commentId, comment)
Edit a comment.


Apex Reference Guide ChatterFeeds Class

updateDirectMessage(communityId, feedElementId, directMessage)
Update the members of a direct message.

updateFeedElement(communityId, feedElementId, feedElement)
Edit a feed element.

updateFeedElementBookmarks(communityId, feedElementId, bookmarks)
Bookmark a feed element or remove a bookmark from a feed element using an input class.

updateFeedElementBookmarks(communityId, feedElementId, isBookmarkedByCurrentUser)
Bookmark a feed element or remove a bookmark from a feed element.

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, readBy)
Mark multiple feed elements as read by the context user at the same time using an input class.

updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, isReadByMe)
Mark multiple feed elements as read by the context user at the same time.

updateLikeForComment(communityId, commentId, isLikedByCurrentUser)
Like or unlike a comment.

updateLikeForFeedElement(communityId, feedElementId, isLikedByCurrentUser)
Like or unlike a feed element.

updatePinnedFeedElements(communityId, feedType, subjectId, pin)
Pin or unpin feed elements to a group or topic feed.

updateStream(communityId, streamId, streamInput)
Update a Chatter feed stream.

voteOnFeedElementPoll(communityId, feedElementId, myChoiceId)
Vote on a poll or change your vote on a poll.

##### **`createStream(communityId, streamInput)`**

Create a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream createStream(String communityId,

   ConnectApi.ChatterStreamInput streamInput)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   streamInput
```

Type: `ConnectApi.ChatterStreamInput`

A `ConnectApi.ChatterStreamInput` body.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`deleteComment(communityId, commentId)`**

Delete a comment.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deleteComment(String communityId, String commentId)

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

Type: Void

##### **`deleteFeedElement(communityId, feedElementId)`**

Delete a feed element.

API Version

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static deleteFeedElement(String communityId, String feedElementId)

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

Type: Void

##### **`deleteLike(communityId, likeId)`**

Delete a like on a comment or post.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static Void deleteLike(String communityId, String likeId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   likeId
```

Type: String

ID for a like.

Return Value

Type: Void

##### **`deleteStream(communityId, streamId)`**

Delete a Chatter feed stream.


Apex Reference Guide ChatterFeeds Class

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static Void deleteStream(String communityId, String streamId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

Return Value

Type: Void

##### **`getComment(communityId, commentId)`**

Get a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment getComment(String communityId, String commentId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   commentId
```

Type: String

ID for a comment.

Return Value

Type: `ConnectApi.Comment`

##### **`getCommentBatch(communityId, commentIds)`**

Get a list of comments.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getCommentBatch(String communityId, List<String>

   commentIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   commentIds
```

Type: List<String>

A list of up to 100 comment IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.Comment` object and errors for comments
that didn’t load.

##### **`getCommentInContext(communityId, commentId, pageSize)`**

Get a threaded comment in the context of its parent comments and post.

API Version

44.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getCommentInContext(String communityId, String

   commentId, Integer pageSize)

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

ID of the comment.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you don’t specify a value, the default size is 25.

Return Value

Type: `ConnectApi.FeedElement`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId)`**

Get comments for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

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

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId,`**

```
  threadedCommentsCollapsed)

```

Get comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, Boolean threadedCommentsCollapsed)

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


Apex Reference Guide ChatterFeeds Class

ID of the feed element.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of comments for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

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

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize,`**

```
  threadedCommentsCollapsed)

```

Get a page of comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Boolean

   threadedCommentsCollapsed)

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

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId,`**

```
  threadedCommentsCollapsed, sortParam)

```

Get sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, Boolean threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder

   sortParam)

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.


Apex Reference Guide ChatterFeeds Class

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, pageParam, pageSize,`**

```
  threadedCommentsCollapsed, sortParam)

```

Get a page of sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getCommentsForFeedElement(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Boolean

   threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder sortParam)

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

Specifies the number of comments per page. Valid values are from 1 through 100. If you pass `null`, the default size is 25.

```
   threadedCommentsCollapsed
```

Type: Boolean


Apex Reference Guide ChatterFeeds Class

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentPage`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, sortParam)`**

Get sorted comments for a feed element.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, ConnectApi.FeedCommentSortOrder sortParam)

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
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`


Apex Reference Guide ChatterFeeds Class

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.CommentsCapability`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getCommentsForFeedElement(communityId, feedElementId, sortParam,`**

```
  threadedCommentsCollapsed)

```

Get sorted comments in a threaded style for a feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getCommentsForFeedElement(String communityId,

   String feedElementId, ConnectApi.FeedCommentSortOrder sortParam, Boolean

   threadedCommentsCollapsed)

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
   sortParam
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments. Values are:

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentsCapability`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getExtensions(communityId, pageParam, pageSize)`**

Get extensions.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ExtensionDefinitions getExtensions(String communityId, String

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

Type: String

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. The default size is 15.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ExtensionDefinitions`

##### **`getFeed(communityId, feedType)`**

Get a feed.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType)

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

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, sortParam)`**

Get a sorted feed.

API Version

28.0

Available to Guest Users

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

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

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, subjectId)`**

Get a feed for a record or user.

API Version

28.0

Available to Guest Users

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

   String subjectId)

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

Return Value

Type: `ConnectApi.Feed`

##### **`getFeed(communityId, feedType, subjectId, sortParam)`**

Get a sorted feed for a record or user.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeed(String communityId, ConnectApi.FeedType feedType,

   String subjectId, ConnectApi.FeedSortOrder sortParam)

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

Return Value

Type: `ConnectApi.Feed`

##### **`getFeedDirectory(String)`**

Get a list of all feeds available to the context user.

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedDirectory getFeedDirectory(String communityId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.FeedDirectory`

##### **`getFeedElement(communityId, feedElementId)`**

Get a feed element.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId)

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

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, commentSort)`**

Get a feed element with sorted comments.


Apex Reference Guide ChatterFeeds Class

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedCommentSortOrder commentSort)

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
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

The default value is `CreatedDateLatestAsc` .

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, threadedCommentsCollapsed)`**

Get a feed element and its comments in a threaded style.

API Version

44.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Boolean threadedCommentsCollapsed)

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, threadedCommentsCollapsed,`**

```
  commentSort)

```

Get a feed element and its sorted comments in a threaded style.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Boolean threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder

   commentSort)

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle)

```

Get a feed element with the specified number of elements per bundle including no more than the specified number of comments per
feed element.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle)

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
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, threadedCommentsCollapsed)

```

Get a feed element with its comments in a threaded style with the specified number of elements per bundle and comments per feed
element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle, Boolean

   threadedCommentsCollapsed)

```


Apex Reference Guide ChatterFeeds Class

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, threadedCommentsCollapsed, commentSort)

```

Get a feed element with its sorted comments in a threaded style with the specified number of elements per bundle and comments per
feed element.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle, Boolean

   threadedCommentsCollapsed, ConnectApi.FeedCommentSortOrder commentSort)

```


Apex Reference Guide ChatterFeeds Class

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

```
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElement(communityId, feedElementId, recentCommentCount,`**

```
  elementsPerBundle, commentSort)

```

Get a feed element with the specified number of elements per bundle including no more than the specified number of sorted comments
per feed element.

API Version

41.0

Available to Guest Users

41.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement getFeedElement(String communityId, String

   feedElementId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedCommentSortOrder commentSort)

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
   commentSort
```

Type: `ConnectApi.FeedCommentSortOrder`

Order of comments.

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

The default value is `CreatedDateLatestAsc` .

Sorting in descending order isn’t supported.

Return Value

Type: `ConnectApi.FeedElement`

##### **`getFeedElementBatch(communityId, feedElementIds)`**

Get a list of feed elements.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] getFeedElementBatch(String communityId,

   List<String> feedElementIds)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

A list of up to 500 feed element IDs.

Return Value

Type: `ConnectApi.BatchResult` []

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.FeedElement` object and errors for
feed elements that didn’t load.

##### **`getFeedElementPoll(communityId, feedElementId)`**

Get the poll associated with a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PollCapability getFeedElementPoll(String communityId, String

   feedElementId)

```


Apex Reference Guide ChatterFeeds Class

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

Type: `ConnectApi.PollCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Note: Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

##### **`getFeedElementsFromBundle(communityId, feedElementId)`**

Get feed elements from a bundle.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromBundle(String communityId,

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

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromBundle(communityId, feedElementId, pageParam, pageSize,`**

```
  elementsPerBundle, recentCommentCount)

```

Get a page of feed elements from a bundle. Specify the number of elements per bundle and include no more than the specified number
of comments per feed element.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromBundle(String communityId,

   String feedElementId, String pageParam, Integer pageSize, Integer elementsPerBundle,

   Integer recentCommentCount)

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

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

```
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFeed(communityId, feedType)`**

Get feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)`**

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` feeds.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` feeds. Each feed element contains no more than the specified number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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


Apex Reference Guide ChatterFeeds Class

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

If _`feedType`_ is `DirectMessages`, _`sortParam`_ must be `LastModifiedDateDesc` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, filter)

```

Get a page of sorted and filtered feed elements from the `Home` feed. Each feed element contains no more than the specified number
of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter)

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

The type of feed. The only valid value is `Home` .

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


Apex Reference Guide ChatterFeeds Class

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

Get a page of filtered and sorted feed elements with comments in a threaded style from the `Home` feed. Each feed element contains
no more than the specified number of comments.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, Boolean threadedCommentsCollapsed)

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

The type of feed. The only valid value is `Home` .


Apex Reference Guide ChatterFeeds Class

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

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

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
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId)`**

Get feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`, `Filter`, `Home`,
`Isolated`, `Landing`, `Moderation`, and `PendingReview` for a user or record.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_
must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_
can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the alias `me` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example for Getting the Context User’s News Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.News, 'me');

```

Example for Getting Another User’s Profile Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, '005R0000000HwMA');

```


Apex Reference Guide ChatterFeeds Class

Example for Getting Another User’s Record Feed

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.Record, '005R0000000HwMA');

```

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` .

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize,

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

The number of feed elements per page.

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam)

```

Get a page of sorted feed elements from any feed other than `Company`, `DirectMessageModeration`, `DirectMessages`,
`Filter`, `Home`, `Isolated`, `Landing`, `Moderation`, and `PendingReview` . Each feed element includes no more than the
specified number of comments.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, showInternalOnly)

```

Get a page of sorted feed elements from a record feed. Each feed element includes no more than the specified number of comments.
Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

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


Apex Reference Guide ChatterFeeds Class

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter)

```

Get a page of sorted and filtered feed elements from the `UserProfile` feed.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter)

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
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` or `ConnectApi.FeedFilter.AuthoredBy` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

Example

This example gets only community-specific feed elements.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, 'me', 3, ConnectApi.FeedDensity.FewerUpdates, null, null,

    ConnectApi.FeedSortOrder.LastModifiedDateDesc, ConnectApi.FeedFilter.CommunityScoped );

```

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

Get a page of feed elements with comments in a threaded style from the `UserProfile` feed.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter, Boolean

   threadedCommentsCollapsed)

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
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` or `ConnectApi.FeedFilter.AuthoredBy` .

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, customFilter)

```

Get a page of sorted and filtered feed elements from the case feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String customFilter)

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
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly)

```

Get a page of sorted feed elements from a record feed. Specify the number of elements per bundle and include no more than the
specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

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


Apex Reference Guide ChatterFeeds Class

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  filter)

```

Get a page of sorted and filtered feed elements from a record feed. Specify the number of elements per bundle and include no more
than the specified number of comments per feed element. Specify whether to return feed elements posted by internal (non-Experience
Cloud site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter)

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  filter, threadedCommentsCollapsed)

```

Get a page of sorted and filtered feed elements with comments in a threaded style for a record feed. Specify the number of elements
per bundle and include no more than the specified number of comments per feed element. Specify whether to return feed elements
posted by internal (non-Experience Cloud site) users only.


Apex Reference Guide ChatterFeeds Class

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, Boolean threadedCommentsCollapsed)

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


Apex Reference Guide ChatterFeeds Class

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
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


Apex Reference Guide ChatterFeeds Class

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  customFilter)

```

Get a page of sorted and filtered feed elements from a case feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter)

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

Maximum number of comments to return with each feed item. The default value is 3.

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

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

  customFilter, threadedCommentsCollapsed)

```

Get a page of filtered and sorted feed elements with comments in a threaded style from a case feed.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

   Boolean threadedCommentsCollapsed)

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

Maximum number of comments to return with each feed item. The default value is 3.

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

If you pass in `null`, the default value `CreatedDateDesc` is used.

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)`**

Get feed elements from a feed filtered by a key prefix for a user.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix)

```


Apex Reference Guide ChatterFeeds Class

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

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam)

```

Get a page of sorted feed elements from a feed filtered by a key prefix for a user.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```


Apex Reference Guide ChatterFeeds Class

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

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam)

```

Get a page of sorted feed elements from a feed filtered by a key prefix for a user. Each feed element contains no more than the specified
number of comments.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeed(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince)

```

Get a page of feed elements from a feed filtered by a key prefix for a user. Include only feed elements that have been updated since the
time specified in the _`updatedSince`_ parameter.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsFromFilterFeedUpdatedSince(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince)

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


Apex Reference Guide ChatterFeeds Class

```
   updatedSince
```

Type: String

Opaque token defining the modification timestamp of the feed and the sort order.

The _`updatedSince`_ parameter doesn’t return feed elements that are created in the same second as the call.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince)

```

Get a page of feed elements from the `Company`, `DirectMessageModeration`, `Home`, and `Moderation` feeds. Include only
feed elements that have been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains no
more than the specified number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince)

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

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, and `Moderation` .

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, filter)

```

Get a page of filtered feed elements from the `Home` feed. Include only feed elements that have been updated since the time specified
in the _`updatedSince`_ parameter. Each feed element contains no more than the specified number of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, String updatedSince, ConnectApi.FeedFilter filter)

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


Apex Reference Guide ChatterFeeds Class

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

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are questions that don’t have answers but
have candidate answers associated with them. This value is valid only for users with the Access Einstein-Generated Answers
permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read for the context user. This value is valid
only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince)

```

Get a page of feed elements from the `Files`, `Groups`, `News`, `People`, and `Record` feeds. Include only feed elements that have
been updated since the time specified in the _`updatedSince`_ parameter. Each feed element contains no more than the specified
number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

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


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, updatedSince,

  showInternalOnly)

```

Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify whether to return feed elements posted by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

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

Maximum number of comments to return with each feed element. The default value is 3.

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, filter)

```

Get a page of filtered feed elements from a `UserProfile` feed. Include only feed elements that have been updated since the time
specified in the _`updatedSince`_ parameter.

API Version

35.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedFilter filter)

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


Apex Reference Guide ChatterFeeds Class

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
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, customFilter)

```

Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

```


Apex Reference Guide ChatterFeeds Class

```
   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, String customFilter)

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

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly)

```

Get a page of feed elements from a record feed. Include only feed elements that have been updated since the time specified in the
_`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed elements posted
by internal (non-Experience Cloud site) users only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly)

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


Apex Reference Guide ChatterFeeds Class

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

```
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, filter)

```

Get a page of filtered feed elements from a record feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter. Specify the maximum number of feed elements in a bundle and whether to return feed elements
posted by internal (non-Experience Cloud site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, ConnectApi.FeedFilter filter)

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


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedElementsUpdatedSince(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  updatedSince, showInternalOnly, customFilter)

```

Get a page of filtered feed elements from a case feed. Include only feed elements that have been updated since the time specified in
the _`updatedSince`_ parameter.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage getFeedElementsUpdatedSince(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, Integer

   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, Boolean showInternalOnly, String customFilter)

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
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getFeedWithFeedElements(communityId, feedType, pageSize)`**

Get information about a feed and a page of feed elements from the feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeedWithFeedElements(String communityId,

   ConnectApi.FeedType feedType, Integer pageSize)

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

The type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Landing`, `Moderation`, and `PendingReview` . `Landing` is valid only when _`communityId`_ is `internal` .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in 0, feed elements aren’t returned
with the feed.

Return Value

Type: `ConnectApi.Feed`

##### **`getFeedWithFeedElements(communityId, feedType, pageSize, recentCommentCount)`**

Get a page of information about the feed and the feed elements with the specified number of comments per feed element from the
feed.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFeedWithFeedElements(String communityId,

   ConnectApi.FeedType feedType, Integer pageSize, Integer recentCommentCount)

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

The type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Landing`, `Moderation`, and `PendingReview` . `Landing` is valid only when _`communityId`_ is `internal` .

```
   pageSize
```

Type: Integer


Apex Reference Guide ChatterFeeds Class

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in 0, feed elements aren’t returned
with the feed.

```
   recentCommentCount
```

Type: Integer

Maximum number of comments to return with each feed element. The default value is 3.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeed(communityId, subjectId, keyPrefix)`**

Get a feed filtered by a key prefix for a user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFilterFeed(String communityId, String subjectId, String

   keyPrefix)

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

A _key prefix_ is the first three characters of a record ID, which specifies the object type.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeed(communityId, subjectId, keyPrefix, sortParam)`**

Get a sorted feed filtered by a key prefix for a user.


Apex Reference Guide ChatterFeeds Class

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Feed getFilterFeed(String communityId, String subjectId, String

   keyPrefix, ConnectApi.FeedType sortParam)

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
   sortParam
```

Type: `ConnectApi.FeedType`

Values are:

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for `DirectMessageModeration`,
`Draft`, `Isolated`, `Moderation`, and `PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.Feed`

##### **`getFilterFeedDirectory(communityId, subjectId)`**

Get a feed directory of filter feeds available to the context user.


Apex Reference Guide ChatterFeeds Class

API Version

30.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedDirectory getFilterFeedDirectory(String communityId, String

   subjectId)

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

Return Value

Type: `ConnectApi.FeedDirectory`

This feed directory contains a list of filter feeds, which are the news feed filtered to include feed items whose parent is a specific entity
type.

Usage

Call this method to return a directory containing a list of `ConnectApi.FeedDirectoryItem` objects. Each object contains a
key prefix associated with an entity type the context user is following. A _key prefix_ is the first three characters of a record ID, which specifies
the object type.

Use key prefixes to filter the news feed so that it contains only feed items whose parent is the entity type associated with the key prefix.
For example, get all the feed items whose parent is an Account. To get the feed items, pass a key prefix to the
`ConnectApi.getFeedItemsFromFilterFeed` method.

The information about filter feeds never contains the key prefixes for users ( `005` ) or groups ( `0F9` ), but all users can use those key prefixes
as filters.

The `ConnectApi.FeedDirectory.favorites` property is always empty when returned by a call to
`getFilterFeedDirectory` because you can’t filter a news feed by favorites.

Example

This example calls `getFilterFeedDirectory` and loops through the returned `FeedDirectoryItem` objects to find the
key prefixes the context user can use to filter their news feed. It then copies each `keyPrefix` value to a list. Finally, it passes one of


Apex Reference Guide ChatterFeeds Class

the key prefixes from the list to the `getFeedItemsFromFilterFeed` method. The returned feed items include every feed item
from the news feed whose parent is the entity type specified by the passed key prefix.

```
   String communityId = null;

   String subjectId = 'me';

   // Create a list to populate with key prefixes.

   List<String> keyPrefixList = new List<String>();

   // Prepopulate with User and Group record types

   // which are available to all users.

   keyPrefixList.add('005');

   keyPrefixList.add('0F9');

   System.debug(keyPrefixList);

   // Get the key prefixes available to the context user.

   ConnectApi.FeedDirectory myFeedDirectory =

     ConnectApi.ChatterFeeds.getFilterFeedDirectory(null, 'me');

   // Loop through the returned feeds list.

   for (ConnectApi.FeedDirectoryItem i : myFeedDirectory.feeds) {

     // Grab each key prefix and add it to the list.

     keyPrefixList.add(i.keyPrefix);

   }

   System.debug(keyPrefixList);

   // Use a key prefix from the list to filter the feed items in the news feed.

   ConnectApi.FeedItemPage myFeedItemPage =

     ConnectApi.ChatterFeeds.getFeedItemsFromFilterFeed(communityId, subjectId,

   keyPrefixList[0]);

   System.debug(myFeedItemPage);

##### **`getLike(communityId, likeId)`**

```

Get a like on a post or comment.

API Version

28.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike getLike(String communityId, String likeId)

```


Apex Reference Guide ChatterFeeds Class

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   likeId
```

Type: String

ID for a like.

Return Value

Type: `ConnectApi.ChatterLike`

##### **`getLikesForComment(communityId, commentId)`**

Get likes for a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForComment(String communityId, String

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

Type: `ConnectApi.ChatterLikePage`


Apex Reference Guide ChatterFeeds Class

##### **`getLikesForComment(communityId, commentId, pageParam, pageSize)`**

Get a page of likes for a comment.

API Version

28.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForComment(String communityId, String

   commentId, Integer pageParam, Integer pageSize)

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

##### **`getLikesForFeedElement(communityId, feedElementId)`**

Get likes for a feed element.

API Version

32.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedElement(String communityId,

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

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getLikesForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of likes for a feed element.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage getLikesForFeedElement(String communityId,

   String feedElementId, Integer pageParam, Integer pageSize)

```


Apex Reference Guide ChatterFeeds Class

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

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getLinkMetadata(communityId, urls)`**

Get link metadata for URLs.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

No

Signature

```
   public static ConnectApi.LinkMetadataCollection getLinkMetadata(String communityId,

   String urls)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

```
   urls
```

Type: String

Comma-separated list of URL-encoded URLs.

Return Value

Type: `ConnectApi.LinkMetadataCollection`

##### **`getPinnedFeedElementsFromFeed(communityId, feedType, subjectId)`**

Get pinned feed elements from a group or topic feed.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PinnedFeedElements getPinnedFeedElementsFromFeed(String

   communityId, ConnectApi.FeedType feedType, String subjectId)

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

The type of feed. Valid values are `Record` and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ must be a group ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID.

Return Value

Type: `ConnectApi.PinnedFeedElements`

If the feed doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

Usage

In the UI, pinned feed elements don’t show all auxiliary information, such as comments, likes, interaction counts, or read by information.
As a result, the `ConnectApi.PinnedFeedElements` output class doesn’t include all the information for these capabilities.

##### **`getReadByForFeedElement(communityId, feedElementId)`**

Get information about who read a feed element and when.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ReadByPage getReadByForFeedElement(String communityId, String

   feedElementId)

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

Type: `ConnectApi.ReadByPage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getReadByForFeedElement(communityId, feedElementId, pageParam, pageSize)`**

Get a page of information about who read a feed element and when.

API Version

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ReadByPage getReadByForFeedElement(String communityId, String

   feedElementId, Integer pageParam, Integer pageSize)

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

Specifies the page token to use to view a page of information. Page tokens are returned as part of the response class, such as
`currentPageToken` or `nextPageToken` . If you pass in `null`, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.ReadByPage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getRelatedPosts(communityId, feedElementId, filter, maxResults)`**

Get posts related to the context feed element.

API Version

37.0

Available to Guest Users

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.RelatedFeedPosts getRelatedPosts(String communityId, String

   feedElementId, ConnectApi.RelatedFeedPostType filter, Integer maxResults)

```


Apex Reference Guide ChatterFeeds Class

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

Specifies the type of related post. Values are:

**•** `Answered` —Related questions that have at least one answer.

**•** `BestAnswer` —Related questions that have a best answer.

**•** `Generic` —All types of related questions, including answered, with a best answer, and unanswered.

**•** `Unanswered` —Related questions that don’t have answers.

`Generic` is the default value.

```
   maxResults
```

Type: Integer

The maximum number of results to return. You can return up to 25 results; 5 is the default.

Return Value

Type: `ConnectApi.RelatedFeedPosts`

In version 37.0 and later, related feed posts are questions.

Each related feed post has a score indicating how closely it’s related to the context feed post. We return related feed posts sorted by
score, with the highest score first.

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`getStream(communityId, streamId)`**

Get information about a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ChatterStream getStream(String communityId, String streamId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`getStream(communityId, streamId, globalScope)`**

Get information about a Chatter feed stream, regardless of Experience Cloud site.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream getStream(String communityId, String streamId,

   Boolean globalScope)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

```
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

Tip: If you know the _`communityId`_ for the stream, we recommend setting _`globalScope`_ to `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterStream`

##### **`getStreams(communityId)`**

Get the Chatter feed streams for the context user.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, sortParam)`**

Get and sort the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId,

   ConnectApi.SortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String


Apex Reference Guide ChatterFeeds Class

ID for an Experience Cloud site, `internal`, or `null` .

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

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, pageParam, pageSize)`**

Get a page of Chatter feed streams for the context user.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

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

Specifies the number of items per page. Valid values are from 1 to 250. The default size is 25.

Return Value

Type: `ConnectApi.ChatterStreamPage`


Apex Reference Guide ChatterFeeds Class

##### **`getStreams(communityId, pageParam, pageSize, sortParam)`**

Get a sorted page of Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

   pageParam, Integer pageSize, ConnectApi.SortOrder sortParam)

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

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getStreams(communityId, pageParam, pageSize, sortParam, globalScope)`**

Get a sorted page of Chatter feed streams from all Enterprise Cloud sites for the context user.


Apex Reference Guide ChatterFeeds Class

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage getStreams(String communityId, Integer

   pageParam, Integer pageSize, ConnectApi.SortOrder sortParam, Boolean globalScope)

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
   globalScope
```

Type: Boolean

Specifies whether to get streams from all the context user’s Experience Cloud sites, regardless of the _`communityId`_ value.

Tip: If you know the _`communityId`_ for the streams, we recommend setting _`globalScope`_ to `false` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

##### **`getSupportedEmojis()`**

Get supported emojis for the org.


Apex Reference Guide ChatterFeeds Class

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.SupportedEmojis getSupportedEmojis()

```

Return Value

Type: `ConnectApi.SupportedEmojis`

Usage

To get the list, emojis must be enabled in your org.

##### **`getThreadsForFeedComment(communityId, commentId)`**

Get threaded comments for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getThreadsForFeedComment(String communityId, String

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

ID of the comment.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.CommentPage`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### **`getThreadsForFeedComment(communityId, commentId, pageParam, pageSize)`**

Get a page of threaded comments for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentPage getThreadsForFeedComment(String communityId, String

   commentId, String pageParam, Integer pageSize)

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

ID of the comment.

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

Type: `ConnectApi.CommentPage`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

##### **`getThreadsForFeedComment(communityId, commentId, threadedCommentsCollapsed)`**

Access the comments capability for a comment.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.CommentsCapability getThreadsForFeedComment(String communityId,

   String commentId, Boolean threadedCommentsCollapsed)

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

ID of the comment.

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.CommentsCapability`

If the comment doesn’t support the `comments` capability, the return value is `ConnectApi.NotFoundException` .

##### getTopUnansweredQuestions(communityId) (Pilot)

Get top unanswered questions for the context user in aExperience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId)

```

Parameters

```
   communityId
```

Type: String

ID of the Experience Cloud site.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, filter) (Pilot)

Get filtered top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   ConnectApi.TopUnansweredQuestionsFilterType filter)

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, filter, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, pageSize) (Pilot)

Get a page of top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   Integer pageSize)

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


Apex Reference Guide ChatterFeeds Class

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, pageSize, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### getTopUnansweredQuestions(communityId, filter, pageSize) (Pilot)

Get a page of filtered top unanswered questions for the context user in an Experience Cloud site.

Note: We provided top-five unanswered questions to selected customers through a pilot program that required agreement to
specific terms and conditions. This pilot program is closed and not accepting new participants.

API Version

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage getTopUnansweredQuestions(String communityId,

   ConnectApi.FeedFilter filter, Integer pageSize)

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
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 0 through 10. If you pass in `null`, the default size is 5.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestGetTopUnansweredQuestions(communityId, filter, pageSize, result) (Pilot)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`getVotesForComment(communityId, commentId, vote)`**

Get the first page of users who upvoted or downvoted a comment.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForComment(String communityId, String

   commentId, ConnectApi.UpDownVoteValue vote)

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

ID of the comment.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`


Apex Reference Guide ChatterFeeds Class

You can’t specify `None` .

Return Value

Type: `ConnectApi.VotePage`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForComment(communityId, commentId, vote, pageParam, pageSize)`**

Get a page of users who upvoted or downvoted a comment.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForComment(String communityId, String

   commentId, ConnectApi.UpDownVoteValue vote, Integer pageParam, Integer pageSize)

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

ID of the comment.

```
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.


Apex Reference Guide ChatterFeeds Class

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

Return Value

Type: `ConnectApi.VotePage`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForFeedElement(communityId, feedElementId, vote)`**

Get the first page of users who upvoted or downvoted a feed element.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForFeedElement(String communityId, String

   feedElementId, ConnectApi.UpDownVoteValue vote)

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
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VotePage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`getVotesForFeedElement(communityId, feedElementId, vote, pageParam, pageSize)`**

Get a page of users who upvoted or downvoted a feed element.

API Version

42.0

Available to Guest Users

42.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VotePage getVotesForFeedElement(String communityId, String

   feedElementId, ConnectApi.UpDownVoteValue vote, Integer pageParam, Integer pageSize)

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
   vote
```

Type: `ConnectApi.UpDownVoteValue`

Specifies the value of the vote for the feed element. Values are:

**•** `Down`

**•** `Up`

You can’t specify `None` .

```
   pageParam
```

Type: Integer

Number of the page you want returned. Starts at 0. If you pass in `null` or 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VotePage`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`isCommentEditableByMe(communityId, commentId)`**

Discover whether the context user can edit a comment.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedEntityIsEditable isCommentEditableByMe(String communityId,

   String commentId)

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

ID of the comment.

Return Value

Type: `ConnectApi.FeedEntityIsEditable`

If the comment doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

SEE ALSO:

[Edit a Comment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_comment.htm)

##### **`isFeedElementEditableByMe(communityId, feedElementId)`**

Discover whether the context user can edit a feed element.

API Version

34.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedEntityIsEditable isFeedElementEditableByMe(String

   communityId, String feedElementId)

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

ID of the feed element. Feed items are the only type of feed element that can be edited.

Return Value

Type: `ConnectApi.FeedEntityIsEditable`

If the feed element doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

SEE ALSO:

[Edit a Feed Element](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_feed_element.htm)

[Edit a Question Title and Post](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_edit_question_title_post.htm)

##### **`isModified(communityId, feedType, subjectId, since)`**

Discover whether a news feed has been updated or changed. Use this method to poll a news feed for updates.

Important: This feature is available through a Feed Polling pilot program. This pilot program is closed and not accepting new
participants.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedModifiedInfo isModified(String communityId,

   ConnectApi.FeedType feedType, String subjectId, String since)

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

Specifies the type of feed. The only supported type is `News`

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   since
```

Type: String

An opaque token containing information about the last modified date of the feed. Retrieve this token from the
`FeedElementPage.isModifiedToken` property.

Return Value

Type: `ConnectApi.FeedModifiedInfo`

##### **`likeComment(communityId, commentId)`**

Like a comment for the context user.

API Version

28.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike likeComment(String communityId, String commentId)

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterLike`

If the context user has already liked the comment, this method is a non-operation and returns the existing like.

##### **`likeFeedElement(communityId, feedElementId)`**

Like a feed element.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLike likeFeedElement(String communityId, String

   feedElementId)

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

Type: `ConnectApi.ChatterLike`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

##### **`postCommentToFeedElement(communityId, feedElementId, text)`**

```

Post a plain-text comment to a feed element.

API Version

32.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment postCommentToFeedElement(String communityId, String

   feedElementId, String text)

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
   text
```

Type: String

Text of the comment. A comment can contain up to 10,000 characters.

Return Value

Type: `ConnectApi.Comment`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.Comment comment = ConnectApi.ChatterFeeds.postCommentToFeedElement(null,

   '0D5D0000000KuGh', 'I agree with the proposal.' );

##### **`postCommentToFeedElement(communityId, feedElementId, comment,`**

  feedElementFileUpload)

```

Post a rich-text comment to a feed element. Use this method to include mentions and to attach a file.

API Version

32.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.Comment postCommentToFeedElement(String communityId, String

   feedElementId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput

   feedElementFileUpload)

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
   comment
```

Type: `ConnectApi.CommentInput`

The comment body, including text and mentions, and capabilities, such as information about an attached file. A comment can
contain up to 10,000 characters.

```
   feedElementFileUpload
```

Type: `ConnectApi.BinaryInput`

A new binary file to attach to the comment, or `null` . If you specify a binary file, specify the title and description of the file in the
_`comment`_ parameter.

Return Value

Type: `ConnectApi.Comment`

If the feed element doesn’t support the `Comments` capability, the return value is `ConnectApi.NotFoundException` .

Example for Posting a Comment with Mentions

[You can post comments with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or use](https://github.com/forcedotcom/ConnectApiHelper)
this method example.

```
   String communityId = null;

   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Does anyone in this group have an idea? ';

   messageBodyInput.messageSegments.add(textSegmentInput);

   mentionSegmentInput.id = '005D00000000oOT';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

```


Apex Reference Guide ChatterFeeds Class

```
   commentInput.body = messageBodyInput;

   ConnectApi.Comment commentRep = ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId,

    feedElementId, commentInput, null);

```

Example for Posting a Comment with an Existing File

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'I attached this file from Salesforce Files.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.contentDocumentId = '069D00000001rNJ';

   commentInput.capabilities = commentCapabilitiesInput;

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, null);

```

Example for Posting a Comment with a New File

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Enjoy this new file.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.title = 'Title';

   commentInput.capabilities = commentCapabilitiesInput;

   String text = 'These are the contents of the new file.';

   Blob myBlob = Blob.valueOf(text);

   ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

   'fileName');

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, binInput);

```

Example for Posting a Rich-Text Comment with an Inline Image

[You can post rich-text comments with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to write](https://github.com/forcedotcom/ConnectApiHelper)
a single line of code, or use this method example. In this example, the image file is existing content that has already been uploaded to
Salesforce.

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String imageId = '069R00000000IgQ';

   String mentionedUserId = '005R0000000DiMz';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

```


Apex Reference Guide ChatterFeeds Class

```
   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

```

Example for Posting a Rich-Text Comment with a Code Block

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

##### **`postFeedElement(communityId, subjectId, feedElementType, text)`**

```

Post a plain-text feed element.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement postFeedElement(String communityId, String

   subjectId, ConnectApi.FeedElementType feedElementType, String text)

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

The ID of the parent this feed element is being posted to. This value can be the ID of a user, group, or record, or the string `me` to
indicate the context user.

```
   feedElementType
```

Type: `ConnectApi.FeedElementType`

The only possible value is `FeedItem` .

```
   text
```

Type: String

The text of the feed element. A feed element can contain up to 10,000 characters.

Return Value

Type: `ConnectApi.FeedElement`

Example

```
   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), '0F9d0000000TreH',

   ConnectApi.FeedElementType.FeedItem, 'On vacation this week.');

##### **`postFeedElement(communityId, feedElement)`**

```

Post a rich-text feed element. Include mentions and hashtag topics, attach already uploaded files to a feed element, and associate action
link groups with a feed element. You can also use this method to share a feed element and add a comment.

API Version

36.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElement postFeedElement(String communityId,

   ConnectApi.FeedElementInput feedElement)

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

Specify rich text, including mentions. Optionally, specify a link, a poll, or up to 10 existing files.

Return Value

Type: `ConnectApi.FeedElement`

Example for Posting a Feed Element with a Mention

[You can post feed elements with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or](https://github.com/forcedotcom/ConnectApiHelper)
use this method example.

```
   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   mentionSegmentInput.id = '005RR000000Dme9';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

   textSegmentInput.text = 'Could you take a look?';

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   feedItemInput.feedElementType = ConnectApi.FeedElementType.FeedItem;

   feedItemInput.subjectId = '0F9RR0000004CPw';

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Posting a Feed Element with Existing Content

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Would you please review these docs?';

```


Apex Reference Guide ChatterFeeds Class

```
   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a files capability to hold the file(s).

   List<String> fileIds = new List<String>();

   fileIds.add('069xx00000000QO');

   fileIds.add('069xx00000000QT');

   fileIds.add('069xx00000000Qn');

   fileIds.add('069xx00000000Qi');

   fileIds.add('069xx00000000Qd');

   ConnectApi.FilesCapabilityInput filesInput = new ConnectApi.FilesCapabilityInput();

   filesInput.items = new List<ConnectApi.FileIdInput>();

   for (String fileId : fileIds) {

      ConnectApi.FileIdInput idInput = new ConnectApi.FileIdInput();

      idInput.id = fileId;

      filesInput.items.add(idInput);

   }

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.files = filesInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Posting a Rich-Text Feed Element with an Inline Image

[You can post rich-text feed elements with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to](https://github.com/forcedotcom/ConnectApiHelper)
write a single line of code, or use this method example. In this example, the image file is existing content that has already been uploaded
to Salesforce. The post also includes text and a mention.

```
   String communityId = null;

   String imageId = '069D00000001INA';

   String mentionedUserId = '005D0000001QNpr';

   String targetUserOrGroupOrRecordId = '005D0000001Gif0';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

Example for Posting a Rich-Text Feed Element with a Code Block

```
   String communityId = null;

   String targetUserOrGroupOrRecordId = 'me';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

```


Apex Reference Guide ChatterFeeds Class

```
   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

Example for Sharing a Feed Element (in Version 39.0 and Later)

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Look at this post I'm sharing.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   ConnectApi.FeedEntityShareCapabilityInput shareInput = new

   ConnectApi.FeedEntityShareCapabilityInput();

   shareInput.feedEntityId = '0D5R0000000SEbc';

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.feedEntityShare = shareInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Example for Sending a Direct Message

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Thanks for attending my presentation test run this morning. Send

    me any feedback.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a direct message capability to hold the member(s) and the

    subject.

```


Apex Reference Guide ChatterFeeds Class

```
   List<String> memberIds = new List<String>();

   memberIds.add('005B00000016OUQ');

   memberIds.add('005B0000001rIN6');

   ConnectApi.DirectMessageCapabilityInput dmInput = new

   ConnectApi.DirectMessageCapabilityInput();

   dmInput.subject = 'Thank you!';

   dmInput.membersToAdd = memberIds;

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.directMessage = dmInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

##### **`postFeedElementBatch(communityId, feedElements)`**

```

Post a list of feed elements.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] postFeedElementBatch(String communityId,

   List<ConnectApi.BatchInput> feedElements)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElements
```

Type: List< `ConnectApi.BatchInput`       

The list can contain up to 500 `ConnectApi.BatchInput` objects. In the `ConnectApi.BatchInput` constructor, the
input object must be a concrete instance of the abstract `ConnectApi.FeedElementInput` class.

Return Value

Type: `ConnectApi.BatchResult` []


Apex Reference Guide ChatterFeeds Class

The `ConnectApi.BatchResult.getResult()` method returns a `ConnectApi.FeedElement` object.

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

Usage

Use this method to post a list of feed elements efficiently. Create a list containing up to 500 objects and insert them all for the cost of
one DML statement.

In version 36.0 and later, you can attach only one already uploaded file to each post. The `ConnectApi.BatchInput` has three
constructors, but the `postFeedElementBatch` method supports only `ConnectApi.BatchInput(Object input)`
in version 35.0 and later. This constructor doesn’t support a binary input.

In version 32.0–35.0, this method supports both `ConnectApi.BatchInput(Object input)` and
`ConnectApi.BatchInput(Object input, ConnectApi.BinaryInput binary)` constructors. The
`ConnectApi.BatchInput(Object input, ConnectApi.BinaryInput binary)` constructor allows for a single
binary input.

In each constructor, the input object must be an instance of `ConnectApi.FeedElementInput` .

Example

This trigger bulk posts to the feeds of newly inserted accounts.

```
   trigger postFeedItemToAccount on Account (after insert) {

      Account[] accounts = Trigger.new;

      // Bulk post to the account feeds.

      List<ConnectApi.BatchInput> batchInputs = new List<ConnectApi.BatchInput>();

      for (Account a : accounts) {

        ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

        input.subjectId = a.id;

        ConnectApi.MessageBodyInput body = new ConnectApi.MessageBodyInput();

        body.messageSegments = new List<ConnectApi.MessageSegmentInput>();

        ConnectApi.TextSegmentInput textSegment = new ConnectApi.TextSegmentInput();

        textSegment.text = 'Let\'s win the ' + a.name + ' account.';

        body.messageSegments.add(textSegment);

        input.body = body;

        ConnectApi.BatchInput batchInput = new ConnectApi.BatchInput(input);

        batchInputs.add(batchInput);

      }

      ConnectApi.ChatterFeeds.postFeedElementBatch(Network.getNetworkId(), batchInputs);

   }

```


Apex Reference Guide ChatterFeeds Class

##### **`publishDraftFeedElement(communityId, feedElementId, feedElement)`**

Publish a draft feed element.

API Version

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement publishDraftFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedElementInput feedElement)

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

ID of the feed element to publish.

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Use this optional parameter to edit your draft before publishing.

Return Value

Type: `ConnectApi.FeedElement`

The published feed element has a new ID.

##### **`searchFeedElements(communityId, q)`**

Get the first page of feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q)

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, sortParam)`**

Get the first page of sorted feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, ConnectApi.FeedSortOrder sortParam)

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

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, threadedCommentsCollapsed)`**

Get the feed elements and comments that match the search criteria.

API Version

44.0

Available to Guest Users

44.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, Boolean threadedCommentsCollapsed)

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize)`**

Get a page of feed elements that match the search criteria.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize)

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize, sortParam)`**

Get a page of sorted feed elements that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)

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

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, pageParam, pageSize,`**

```
  threadedCommentsCollapsed)

```

Get a page of feed elements with comments in a threaded style that match the search criteria.

API Version

44.0

Available to Guest Users

44.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, String pageParam, Integer pageSize, Boolean threadedCommentsCollapsed)

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


Apex Reference Guide ChatterFeeds Class

```
   threadedCommentsCollapsed
```

Type: Boolean

Specifies whether to return threaded comments in a collapsed style ( `true` ) or not ( `false` ). If you pass in `null`, the default is

`false` .

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize,`**

```
  sortParam)

```

Get a page of sorted feed elements that match the search criteria. Each feed element includes no more than the specified number of
comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElements(String communityId, String

   q, Integer recentCommentCount, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, q)`**

Get the feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` feeds that match the search criteria.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

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

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`, and
`PendingReview` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchFeedElementsInFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, q)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

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


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from the `Company`, `DirectMessageModeration`, `Home`, `Isolated`, `Moderation`,
and `PendingReview` feeds that match the search criteria. Each feed element includes no more than the specified number of
comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, recentCommentCount, density,`**

```
  pageParam, pageSize, sortParam, q, filter)

```

Get a page of sorted and filtered feed elements from the `Home` feed that match the search criteria. Each feed element includes no more
than the specified number of comments.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q,

   ConnectApi.FeedFilter filter)

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

The type of feed. The only valid value is `Home` .


Apex Reference Guide ChatterFeeds Class

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

When the _`sortParam`_ is `MostViewed`, you must pass in `null` for the _`pageParam`_ .

```
   pageSize
```

Type: Integer

Specifies the number of feed elements per page. Valid values are from 1 through 100. If you pass in `null`, the default size is 25.

When the _`sortParam`_ is `MostViewed`, the _`pageSize`_ must be a value from 1 to 25.

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

Specifies the feed filters.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only for the `UserProfile` feed.


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, q)`**

Search up to 5,000 of the most recent feed elements in a feed for a subject ID that match the search string. Feed elements are returned
in order of most recent activity.

API Version

31.0

Available to Guest Users

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

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
`Landing`, `Streams`, and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ can be any record ID, including a group ID. If _`feedType`_ is `UserProfile`,
_`subjectId`_ can be any user ID. If the _`feedType`_ is any other value, _`subjectId`_ must be the ID of the context user or the
alias `me` .

```
   q
```

Type: String

Required and can’t be `null` . Specifies the string to search. The search string must contain at least two characters, not including
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed for a record or user that match the search criteria.


Apex Reference Guide ChatterFeeds Class

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

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


Apex Reference Guide ChatterFeeds Class

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed that match the search criteria. Each feed element includes no more than the specified
number of comments.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q)

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, filter)

```

Get a page of sorted and filtered feed elements from a `UserProfile` feed that match the search criteria.

API Version

35.0

Available to Guest Users

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedFilter filter)

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

One or more keywords to search for in the feed elements visible to the context user. The search string can contain wildcards and
[must contain at least two characters that aren’t wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, customFilter)

```

Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

API Version

40.0

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, String customFilter)

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
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly)

```

Get a page of sorted feed elements from a feed for a record or user that match the search criteria. Each feed element includes no more
than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud site) users
only.

API Version

31.0

Available to Guest Users

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

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


Apex Reference Guide ChatterFeeds Class

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

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly, filter)

```

Get a page of sorted and filtered feed elements from a feed for a record or user that match the search criteria. Each feed element includes
no more than the specified number of comments. Specify whether to return feed elements posted by internal (non-Experience Cloud
site) users only.

API Version

32.0

Available to Guest Users

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly,

   ConnectApi.FeedFilter filter)

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


Apex Reference Guide ChatterFeeds Class

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

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

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

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, filter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, q, showInternalOnly, customFilter)

```

Get a page of sorted and filtered feed elements from a case feed that match the search criteria.

API Version

40.0


Apex Reference Guide ChatterFeeds Class

Available to Guest Users

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFeed(String communityId,

   ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, String q, Boolean showInternalOnly, String

   customFilter)

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed elements from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   filter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, customFilter, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q)`**

Get the feed elements from a feed filtered by a key prefix that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, String q)

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

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam,`**

```
  pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria.

API Version

31.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize,

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElementPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, q)

```

Get a page of sorted feed elements from a feed filtered by a key prefix that match the search criteria. Each feed element includes no
more than the specified number of comments.

API Version

31.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElementPage searchFeedElementsInFilterFeed(String

   communityId, String subjectId, String keyPrefix, Integer recentCommentCount,

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

Return Value

Type: `ConnectApi.FeedElementPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchStreams(communityId, q)`**

Search the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q)

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

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, sortParam)`**

Search and sort the Chatter feed streams for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   ConnectApi.SortOrder sortParam)

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

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, pageParam, pageSize)`**

Search the Chatter feed streams for the context user and return a page of results.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

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

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, pageParam, pageSize, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`searchStreams(communityId, q, pageParam, pageSize, sortParam)`**

Search the Chatter feed streams for the context user and return a sorted page of results.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   Integer pageParam, Integer pageSize, ConnectApi.SortOrder sortParam)

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

Return Value

Type: `ConnectApi.ChatterStreamPage`


Apex Reference Guide ChatterFeeds Class

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

SEE ALSO:

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, result)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)`**

Search the Chatter feed streams from all Experience Cloud sites for the context user and return a sorted page of results.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStreamPage searchStreams(String communityId, String q,

   Integer pageParam, Integer pageSize, ConnectApi.SortOrder sortParam, Boolean globalScope)

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

Tip: If you know the _`communityId`_ for the streams, we recommend setting _`globalScope`_ to `false` .

Return Value

Type: `ConnectApi.ChatterStreamPage`

Usage

To test code that uses this method, use the matching set test method (prefix the method name with `setTest` ). Use the set test method
with the same parameters or the code throws an exception.

##### **`setCommentIsVerified(communityId, commentId, isVerified)`**

Mark a comment as verified or unverified.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VerifiedCapability setCommentIsVerified(String communityId,

   String commentId, Boolean isVerified)

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

ID of the comment on a question post. Only one comment on a question post can be marked as verified.

```
   isVerified
```

Type: Boolean

Specifies whether to mark the comment as verified ( `true` ) or unverified ( `false` ).

Only verified comments can be marked as unverified, and only unverified comments can be marked as verified.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VerifiedCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setCommentIsVerifiedByAnonymized(communityId, commentId, isVerified,`**

```
  isVerifiedByAnonymized)

```

Mark a comment as verified by an anonymous user.

API Version

43.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.VerifiedCapability setCommentIsVerifiedByAnonymized(String

   communityId, String commentId, Boolean isVerified, Boolean isVerifiedByAnonymized)

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

ID of the comment on a question post. Only one comment on a question post can be marked as verified.

```
   isVerified
```

Type: Boolean

Specifies whether to mark the comment as verified ( `true` ) or unverified ( `false` ).

Only verified comments can be marked as unverified, and only unverified comments can be marked as verified.

```
   isVerifiedByAnonymized
```

Type: Boolean

Specifies whether to mark the comment as verified by an anonymous user ( `true` ).

If a user previously verified a comment and then requested the activity to be deleted, use `isVerifiedByAnonymized` to
maintain the verification and anonymize the value of `lastVerifiedByUser` .

You can’t set `isVerified` and `isVerifiedByAnonymized` to `true` at the same time. `isVerifiedByAnonymized`
can be set to `true` only if `isVerified` is already set to `true` .

You can’t set `isVerifiedByAnonymized` to `false` . After `isVerifiedByAnonymized` is set to `true`, it can be
undone only when another user marks the comment as unverified and then reverifies the comment.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.VerifiedCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setCommentVote(communityId, commentId, upDownVote)`**

Upvote or downvote a comment.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UpDownVoteCapability setCommentVote(String communityId, String

   commentId, ConnectApi.UpDownVoteCapabilityInput upDownVote)

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

ID of the comment.

```
   upDownVote
```

Type: `ConnectApi.UpDownVoteCapabilityInput`

A `ConnectApi.UpDownVoteCapabilityInput` object that includes your vote.

Return Value

Type: `ConnectApi.UpDownVoteCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedCommentStatus(communityId, commentId, status)`**

Set the status of a comment.

API Version

38.0


Apex Reference Guide ChatterFeeds Class

Requires Chatter

Yes

Signature

```
   public static ConnectApi.StatusCapability setFeedCommentStatus(String communityId,

   String commentId, ConnectApi.StatusCapabilityInput status)

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

ID of the comment.

```
   status
```

Type: `ConnectApi.StatusCapabilityInput`

A `ConnectApi.StatusCapabilityInput` object that includes the status you want to set.

Return Value

Type: `ConnectApi.StatusCapability`

If the comment doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

Only users with the Can Approve Feed Post and Comment permission can set the status of a feed post or comment.

##### **`setFeedElementIsClosed(communityId, feedElementId, isClosed)`**

Set a feed element to closed.

Users can’t edit (specifically the feed item body or title), comment on, or delete a closed feed element. If the closed feed element is a
poll, users can’t vote on it. Users can’t edit (specifically the comment body) or delete a comment on a closed feed element or select or
remove it as best answer.

Admins and moderators can edit and delete closed feed elements and comments on closed feed elements. Admins and moderators
can select or remove the best answer status on comments on closed feed elements.

API Version

43.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.CloseCapability setFeedElementIsClosed(String communityId,

   String feedElementId, Boolean isClosed)

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
   isClosed
```

Type: Boolean

Specifies whether to set the feed element to closed ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.CloseCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedElementVote(communityId, feedElementId, upDownVote)`**

Upvote or downvote a feed element.

API Version

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.UpDownVoteCapability setFeedElementVote(String communityId,

   String feedElementId, ConnectApi.UpDownVoteCapabilityInput upDownVote)

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


Apex Reference Guide ChatterFeeds Class

```
   upDownVote
```

Type: `ConnectApi.UpDownVoteCapabilityInput`

A `ConnectApi.UpDownVoteCapabilityInput` object that includes your vote.

Return Value

Type: `ConnectApi.UpDownVoteCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setFeedEntityStatus(communityId, feedElementId, status)`**

Set the status of a feed post.

API Version

37.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.StatusCapability setFeedEntityStatus(String communityId, String

   feedElementId, ConnectApi.StatusCapabilityInput status)

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
   status
```

Type: `ConnectApi.StatusCapabilityInput`

A `ConnectApi.StatusCapabilityInput` object that includes the status you want to set.

Return Value

Type: `ConnectApi.StatusCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Usage

Only users with the Can Approve Feed Post and Comment permission can set the status of a feed post or comment.


Apex Reference Guide ChatterFeeds Class

##### **`setIsMutedByMe(communityId, feedElementId, isMutedByMe)`**

Mute or unmute a feed element.

API Version

35.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.MuteCapability setIsMutedByMe(String communityId, String

   feedElementId, Boolean isMutedByMe)

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
   isMutedByMe
```

Type: Boolean

Indicates whether the feed element is muted for the context user. Default value is `false` .

Return Value

Type: `ConnectApi.MuteCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setIsReadByMe(communityId, feedElementId, readBy)`**

Mark a feed element as read for the context user using an input class.

API Version

40.0

Requires Chatter

Yes


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static ConnectApi.ReadByCapability setIsReadByMe(String communityId, String

   feedElementId, ConnectApi.ReadByCapabilityInput readBy)

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

ID of the feed element to mark as read.

```
   readBy
```

Type: `ConnectApi.ReadByCapabilityInput`

A `ConnectApi.ReadByCapabilityInput` body indicating to mark the feed elements as read.

Return Value

Type: `ConnectApi.ReadByCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`setIsReadByMe(communityId, feedElementId, isReadByMe)`**

Mark a feed element as read for the context user.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ReadByCapability setIsReadByMe(String communityId, String

   feedElementId, Boolean isReadByMe)

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

ID of the feed element to mark as read.


Apex Reference Guide ChatterFeeds Class

```
   isReadByMe
```

Type: Boolean

Specifies to mark the feed element as read ( `true` ) for the context user.

Return Value

Type: `ConnectApi.ReadByCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateComment(communityId, commentId, comment)`**

Edit a comment.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.Comment updateComment(String communityId, String commentId,

   ConnectApi.CommentInput comment)

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

ID of the comment to be edited.

```
   comment
```

Type: `ConnectApi.CommentInput`

Information about the comment to be edited.

Return Value

Type: `ConnectApi.Comment`

If the comment doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   String commentId;

   String communityId = Network.getNetworkId();

```


Apex Reference Guide ChatterFeeds Class

```
   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.CommentPage commentPage =

   ConnectApi.ChatterFeeds.getCommentsForFeedElement(communityId, feedElementId);

   if (commentPage.items.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   commentId = commentPage.items[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isCommentEditableByMe(communityId, commentId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited comment.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      commentInput.body = messageBodyInput;

      ConnectApi.Comment editedComment = ConnectApi.ChatterFeeds.updateComment(communityId,

    commentId, commentInput);

   }

##### **`updateDirectMessage(communityId, feedElementId, directMessage)`**

```

Update the members of a direct message.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.DirectMessageCapability updateDirectMessage(String communityId,

   String feedElementId, ConnectApi.DirectMessageCapabilityInput directMessage)

```


Apex Reference Guide ChatterFeeds Class

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
   directMessage
```

Type: `ConnectApi.DirectMessageCapabilityInput`

A `ConnectApi.DirectMessageCapabilityInput` body that includes the members to add and remove.

Return Value

Type: `ConnectApi.DirectMessageCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateFeedElement(communityId, feedElementId, feedElement)`**

Edit a feed element.

API Version

34.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.FeedElement updateFeedElement(String communityId, String

   feedElementId, ConnectApi.FeedElementInput feedElement)

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

ID of the feed element to be edited. Feed items are the only type of feed element that can be edited.

```
   feedElement
```

Type: `ConnectApi.FeedElementInput`

Information about the feed item to be edited.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.FeedElement`

If the feed element doesn’t support the `edit` capability, the return value is `ConnectApi.NotFoundException` .

Example for Editing a Feed Post

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited post.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

```

Example for Editing a Question Title and Post

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

```


Apex Reference Guide ChatterFeeds Class

```
   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

      ConnectApi.QuestionAndAnswersCapabilityInput questionAndAnswersCapabilityInput = new

   ConnectApi.QuestionAndAnswersCapabilityInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited question.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      feedItemInput.capabilities = feedElementCapabilitiesInput;

      feedElementCapabilitiesInput.questionAndAnswers = questionAndAnswersCapabilityInput;

      questionAndAnswersCapabilityInput.questionTitle = 'Where is my edited question?';

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

##### **`updateFeedElementBookmarks(communityId, feedElementId, bookmarks)`**

```

Bookmark a feed element or remove a bookmark from a feed element using an input class.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BookmarksCapability updateFeedElementBookmarks(String

   communityId, String feedElementId, ConnectApi.BookmarksCapabilityInput bookmarks)

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


Apex Reference Guide ChatterFeeds Class

```
   bookmarks
```

Type: `ConnectApi.BookmarksCapabilityInput`

Information about a bookmark.

Return Value

Type: ConnectApi.BookmarksCapability

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateFeedElementBookmarks(communityId, feedElementId,`**

```
  isBookmarkedByCurrentUser)

```

Bookmark a feed element or remove a bookmark from a feed element.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BookmarksCapability updateFeedElementBookmarks(String

   communityId, String feedElementId, Boolean isBookmarkedByCurrentUser)

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
   isBookmarkedByCurrentUser
```

Type: Boolean

Specify whether to bookmark the feed element ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.BookmarksCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

Example

```
   ConnectApi.BookmarksCapability bookmark =

   ConnectApi.ChatterFeeds.updateFeedElementBookmarks(null, '0D5D0000000KuGh', true);

##### **`updateFeedElementReadByCapabilityBatch(communityId, feedElementIds, readBy)`**

```

Mark multiple feed elements as read by the context user at the same time using an input class.

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] updateFeedElementReadByCapabilityBatch(String

   communityId, List<String> feedElementIds, ConnectApi.ReadByCapabilityInput readBy)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

Up to 500 feed element IDs to mark as read.

```
   readBy
```

Type: `ConnectApi.ReadByCapabilityInput`

A `ConnectApi.ReadByCapabilityInput` body indicating to mark the feed elements as read.

Return Value

Type: `ConnectApi.BatchResult` []

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

The returned objects correspond to each of the input objects and are returned in the same order as the input objects.

The method call fails only if an error occurs that affects the entire operation (such as a parsing failure). If an individual object causes an
error, the error is embedded within the `ConnectApi.BatchResult` list.

##### **`updateFeedElementReadByCapabilityBatch(communityId, feedElementIds,`**

```
  isReadByMe)

```

Mark multiple feed elements as read by the context user at the same time.


Apex Reference Guide ChatterFeeds Class

API Version

40.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.BatchResult[] updateFeedElementReadByCapabilityBatch(String

   communityId, List<String> feedElementIds, Boolean isReadByMe)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   feedElementIds
```

Type: List<String>

Up to 500 feed element IDs to mark as read.

```
   isReadByMe
```

Type: Boolean

Specifies to mark the feed element as read ( `true` ) for the context user.

Return Value

Type: `ConnectApi.BatchResult` []

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

##### **`updateLikeForComment(communityId, commentId, isLikedByCurrentUser)`**

Like or unlike a comment.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage updateLikeForComment(String communityId, String

   commentId, Boolean isLikedByCurrentUser)

```


Apex Reference Guide ChatterFeeds Class

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

ID of the comment.

```
   isLikedByCurrentUser
```

Type: Boolean

Specifies if the context user likes ( `true` ) or unlikes ( `false` ) the comment.

Return Value

Type: `ConnectApi.ChatterLikePage`

##### **`updateLikeForFeedElement(communityId, feedElementId, isLikedByCurrentUser)`**

Like or unlike a feed element.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterLikePage updateLikeForFeedElement(String communityId,

   String feedElementId, Boolean isLikedByCurrentUser)

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
   isLikedByCurrentUser
```

Type: Boolean

Specifies if the context user likes ( `true` ) or unlikes ( `false` ) the feed element.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: `ConnectApi.ChatterLikePage`

If the feed element doesn’t support the `ChatterLikes` capability, the return value is `ConnectApi.NotFoundException` .

##### **`updatePinnedFeedElements(communityId, feedType, subjectId, pin)`**

Pin or unpin feed elements to a group or topic feed.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PinCapability updatePinnedFeedElements(String communityId,

   ConnectApi.FeedType feedType, String subjectId, ConnectApi.PinCapabilityInput pin)

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

The type of feed. Valid values are `Record` and `Topics` .

```
   subjectId
```

Type: String

If _`feedType`_ is `Record`, _`subjectId`_ must be a group ID. If _`feedType`_ is `Topics`, _`subjectId`_ must be a topic ID.

```
   pin
```

Type: `ConnectApi.PinCapabilityInput`

A `ConnectApi.PinCapabilityInput` object indicating the feed element to pin or unpin.

Return Value

Type: `ConnectApi.PinCapability`

If the feed doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .


Apex Reference Guide ChatterFeeds Class

##### **`updateStream(communityId, streamId, streamInput)`**

Update a Chatter feed stream.

API Version

39.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.ChatterStream updateStream(String communityId, String streamId,

   ConnectApi.ChatterStreamInput streamInput)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .

```
   streamId
```

Type: String

ID of the Chatter feed stream.

```
   streamInput
```

Type: `ConnectApi.ChatterStreamInput`

A `ConnectApi.ChatterStreamInput` object.

Return Value

Type: `ConnectApi.ChatterStream`

##### **`voteOnFeedElementPoll(communityId, feedElementId, myChoiceId)`**

Vote on a poll or change your vote on a poll.

API Version

32.0

Requires Chatter

Yes

Signature

```
   public static ConnectApi.PollCapability voteOnFeedElementPoll(String communityId, String

   feedElementId, String myChoiceId)

```


Apex Reference Guide ChatterFeeds Class

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
   myChoiceId
```

Type: String

ID of the poll item you’re voting for. The key prefix for poll items is 09A.

Return Value

Type: `ConnectApi.PollCapability`

If the feed element doesn’t support this capability, the return value is `ConnectApi.NotFoundException` .

Example

```
   ConnectApi.PollCapability poll = ConnectApi.ChatterFeeds.voteOnFeedElementPoll(null,

   '0D5D0000000XZaUKAW', '09AD000000000TKMAY');

#### ChatterFeeds Test Methods These test methods are for ChatterFeeds . All methods are static.

```

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

IN THIS SECTION:

setTestGetFeedElementsFromFeed(communityId, feedType, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, filter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, result)
a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElementsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the
`getFeedElementsFromFilterFeedUpdatedSince` method is called in a test context.

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount, density, pageParam, pageSize, updatedSince,
filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
updatedSince, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetFeedElementsUpdatedSince(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density,
pageParam, pageSize, updatedSince, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsUpdatedSince` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestGetRelatedPosts(communityId, feedElementId, filter, maxResults, result)
Register a `ConnectApi.RelatedFeedPosts` object to be returned when the matching
`ConnectApi.getRelatedPosts(communityId, feedElementId, filter, maxResults)` method is
called in a test context. Use the method with the same parameters or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, filter, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, pageSize, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestGetTopUnansweredQuestions(communityId, filter, pageSize, result) (Pilot)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getTopUnansweredQuestions` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElements(communityId, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, pageParam, pageSize, threadedCommentsCollapsed, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElements(communityId, q, recentCommentCount, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElements` method is called in a test context. Use the method with the same parameters or you
receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, q,
filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when `searchFeedElementsInFeed` is called
with matching parameters in a test context. Use the method with the same parameters or the code throws an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, filter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize,
sortParam, q, showInternalOnly, customFilter, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFeed` method is called in a test context. Use the method with the same parameters
or you receive an exception.

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.


Apex Reference Guide ChatterFeeds Class

setTestSearchFeedElementsInFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, density, pageParam, pageSize,
sortParam, q, result)
Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.searchFeedElementsInFilterFeed` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchStreams(communityId, q, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q)` method is called in a test context. Use the method with the same
parameters or you receive an exception.

setTestSearchStreams(communityId, q, sortParam, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStream(communityId, q, sortParam)` method is called in a test context. Use the method
with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize)` method is called in a test context.
Use the method with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching
`ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam)` method is called
in a test context. Use the method with the same parameters or you receive an exception.

setTestSearchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope, result)
Register a `ConnectApi.ChatterStreamPage` object to be returned when the matching

```
    ConnectApi.searchStreams(communityId, q, pageParam, pageSize, sortParam, globalScope)
```

method is called in a test context. Use the method with the same parameters or you receive an exception.

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, ConnectApi.FeedElementPage result)

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

Type of feed. Valid values are `Company`, `DirectMessageModeration`, `DirectMessages`, `Home`, `Isolated`,
`Moderation`, and `PendingReview` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, pageParam, pageSize,`**

```
  sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

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

The only valid value for this parameter is `Company` .

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
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

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
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter,

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


Apex Reference Guide ChatterFeeds Class

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


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam,

   Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedFilter filter,

   Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

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

The type of feed. The only valid value is `Home` .

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


Apex Reference Guide ChatterFeeds Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density, pageParam, pageSize, sortParam, filter,
threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, result)`**

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, ConnectApi.FeedElementPage result)

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

The feed type.

```
   subjectId
```

Type: String

ID of the context user or the alias `me` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId, pageParam,`**

```
  pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedElementPage result)

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
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedElementPage result)

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
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, showInternalOnly,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, Boolean

   showInternalOnly, ConnectApi.FeedElementPage result)

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the method with the same parameters or the code throws an exception.


Apex Reference Guide ChatterFeeds Class

API Version

35.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home` feeds when the
`ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for `Company`, `Home`, and `Topics` feeds.

If you pass in `null`, the default value `CreatedDateDesc` is used.

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

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, filter,

  threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam,

   ConnectApi.FeedFilter filter, Boolean threadedCommentsCollapsed,

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
   filter
```

Type: `ConnectApi.FeedFilter`


Apex Reference Guide ChatterFeeds Class

Value must be `ConnectApi.FeedFilter.CommunityScoped` . Filters the feed to include only feed elements that are
scoped to Experience Cloud sites. Feed elements that are always visible in all sites are filtered out. Currently, feed elements scoped
to sites have a User or a Group parent record. However, other parent record types could be scoped to sites in the future.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
filter, threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, density, pageParam, pageSize, sortParam, customFilter,

  result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

40.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density,

   String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String

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


Apex Reference Guide ChatterFeeds Class

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
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, density, pageParam, pageSize, sortParam,
customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedElementPage

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
   elementsPerBundle
```

Type: Integer

Maximum number of feed elements to include in a bundle. The value must be an integer between 0 and 10. The default value is 3.


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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, filter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

32.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
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


Apex Reference Guide ChatterFeeds Class

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best answer.

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, filter, threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, ConnectApi.FeedFilter

   filter, Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

Maximum number of comments to return with each feed item. The default value is 3.

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
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


Apex Reference Guide ChatterFeeds Class

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

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, filter, threadedCommentsCollapsed)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, customFilter, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when `getFeedElementsFromFeed` is called with
matching parameters in a test context. Use the get feed method with the same parameters or the code throws an exception.

API Version

40.0


Apex Reference Guide ChatterFeeds Class

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

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

Maximum number of comments to return with each feed item. The default value is 3.

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

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

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFeed(communityId, feedType, subjectId,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching
`ConnectApi.getFeedElementsFromFeed` method is called in a test context. Use the method with the same parameters or
you receive an exception.

API Version

44.0

Signature

```
   public static Void setTestGetFeedElementsFromFeed(String communityId, ConnectApi.FeedType

   feedType, String subjectId, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

```


Apex Reference Guide ChatterFeeds Class

```
   ConnectApi.FeedSortOrder sortParam, Boolean showInternalOnly, String customFilter,

   Boolean threadedCommentsCollapsed, ConnectApi.FeedElementPage result)

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

Maximum number of comments to return with each feed item. The default value is 3.

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
   showInternalOnly
```

Type: Boolean

Specifies whether to show only feed items from internal (non-Experience Cloud site) users ( `true` ), or not ( `false` ). The default
value is `false` .

```
   customFilter
```

Type: String

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam, showInternalOnly, customFilter, threadedCommentsCollapsed)

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  result)

```

a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElementsFromFilterFeed`
method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, ConnectApi.FeedElementPage result)

```


Apex Reference Guide ChatterFeeds Class

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

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  pageParam, pageSize, sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder

   sortParam, ConnectApi.FeedElementPage result)

```

Parameters

```
   communityId
```

Type: String

ID for an Experience Cloud site, `internal`, or `null` .


Apex Reference Guide ChatterFeeds Class

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

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam, pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


Apex Reference Guide ChatterFeeds Class

##### **`setTestGetFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix,`**

```
  recentCommentCount, elementsPerBundle, density, pageParam, pageSize,

  sortParam, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the matching `getFeedElements`
`FromFilterFeed` method is called in a test context. Use the method with the same parameters or the code throws an exception.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeed(String communityId, String

   subjectId, String keyPrefix, Integer recentCommentCount, Integer elementsPerBundle,

   ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedElementPage result)

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


Apex Reference Guide ChatterFeeds Class

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

getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle, density, pageParam,
pageSize, sortParam)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId,`**

```
  keyPrefix, recentCommentCount, elementsPerBundle, density, pageParam,

  pageSize, updatedSince, result)

```

Register a `ConnectApi.FeedElementPage` object to be returned when the
`getFeedElementsFromFilterFeedUpdatedSince` method is called in a test context.

API Version

31.0

Signature

```
   public static Void setTestGetFeedElementsFromFilterFeedUpdatedSince(String communityId,

   String subjectId, String keyPrefix, Integer recentCommentCount, Integer

```


Apex Reference Guide ChatterFeeds Class

```
   elementsPerBundle, ConnectApi.FeedDensity density, String pageParam, Integer pageSize,

   String updatedSince, ConnectApi.FeedElementPage result)

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
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.


Apex Reference Guide ChatterFeeds Class

Return Value

Type: Void

SEE ALSO:

getFeedElementsFromFilterFeedUpdatedSince(communityId, subjectId, keyPrefix, recentCommentCount, elementsPerBundle,
density, pageParam, pageSize, updatedSince)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestGetFeedElementsUpdatedSince(communityId, feedType, recentCommentCount,`**

```
  density, pageParam, pageSize, updatedSince, result)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

[Custom filter that applies only to the case feed. See customFeedFilter in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customfeedfilter.htm) _Metadata API Developer Guide_ for supported values.

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
[wildcards. See Wildcards.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/intro_wildcards.htm)

```
   result
```

Type: `ConnectApi.FeedElementPage`

Object containing test data.

Return Value

Type: Void

SEE ALSO:

searchFeedElements(communityId, q)

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

##### **`setTestSearchFeedElements(communityId, q, threadedCommentsCollapsed, result)`**

