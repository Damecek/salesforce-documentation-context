TaxAddress

Response

```

#### ConnectApi.TaxAddressResponse

Location code of an address.

**Property Name** **Type** **Description** **Available Version**

`locationCode` String Location code of an address. 55.0

#### ConnectApi.TaxAmountDetailsResponse

Information about tax amount values on the line item.

**Property Name** **Type** **Description** **Available Version**

`exemptAmount` Double Amount of the line item exempt from tax application. 55.0

`taxAmount` Double Tax amount for the line item. 55.0

`totalAmount` Double Total amount of the line item. 55.0

`totalAmountWithTax` Double The line item's total amount with tax. 55.0

#### ConnectApi.TaxDetailsResponse

Tax details for each line item in a tax line item output.

**Property Name** **Type** **Description** **Available Version**

`exemptAmount` Double Amount of the line item that is exempt from taxation. 55.0

`exemptReason` String The reason that any tax exemption applied to the 55.0
line item.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
imposition

jurisdiction

```

#### ConnectApi. The business justification for applying tax to a line 55.0

`TaxImposition` item.

```
Response

#### ConnectApi. Business address used to calculate the tax rate for the 55.0
```

`TaxJurisdiction` line item.

```
Response

```

`rate` Double Tax rate for the line item. 55.0

`tax` Double Total amount of tax on the line item. 55.0

`taxId` String ID for the type of tax applied to the line item. 55.0

`taxableAmount` Double Amount of line item that can be taxed. 55.0

#### ConnectApi.TaxEngineLogResponse

Shows the results of the tax calculation request to the tax engine.

**Property Name** **Type** **Description** **Available Version**

`createdDate` Datetime The date that the gateway log was created. 55.0

`id` String ID of the tax engine log record. 55.0

`resultCode` String

Result code sent from the external tax engine. Review 55.0
the tax engine provider's documentation for more
information about the code.

#### ConnectApi.TaxImpositionResponse

Tax imposition output representation.

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the tax imposition. 55.0

`type` String Type of the tax imposition. 55.0

#### ConnectApi.TaxJurisdictionResponse

Represents the address or jurisdiction of the primary business used for calculating tax.

**Property Name** **Type** **Description** **Available Version**

`country` String Country of the tax jurisdiction address. 55.0

`id` String ID of the tax jurisdiction address. 55.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`level` String Level of the tax jurisdiction address. 55.0

`name` String Name of the tax jurisdiction address. 55.0

`region` String Region of the tax jurisdiction address. 55.0

`stateAssignedNo` String State-assigned number of the tax jurisdiction address. 55.0

#### ConnectApi.TaxTransactionResponse

Tax transaction output representation

This class is abstract.

Superclass of ConnectApi.CalculateTaxResponse.

**Property Name** **Type** **Description** **Available Version**

```
addresses

amountDetails

```

#### ConnectApi. The Ship From, Ship To, and Sold To addresses used 55.0

`TaxAddresses` during tax calculation.

```
Response

#### ConnectApi. Information about tax amount values on the line item. 55.0

TaxAmount

DetailsResponse

```

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 55.0
the payment group record.

`description` String Information about whether the tax transaction failed 55.0
or was successful.

`documentCode` String Document code. 55.0

`effectiveDate` Datetime The date that tax is applied to the taxed entity. 55.0

```
lineItems

```

#### List< ConnectApi. A list of line items on which tax was calculated. 55.0

```
LineItem
```

`Response` 

`referenceDocumentCode` String The original document code. Used in case of 55.0
subsequent transactions such as credit tax.

`referenceEntityId` String ID of the reference entity used during tax calculation. 55.0

`taxTransactionId` String ID of the tax transaction. 55.0

`transactionDate` Datetime The date that the tax transaction occurred. 55.0

#### ConnectApi.TextClassificationsBulkResultsOutputRepresentation

Text classification to get results for multiple text classification request IDs.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### resultsList <List ConnectApi.TextClassificationsResultWithIdOutputRepresentation > List of results for passed request IDs. 59.0 ConnectApi.TextClassificationsOutputRepresentation

HTTP headers containing URLs associating text strings and classifications.

**Property Name** **Type** **Description** **Available Version**

`httpHeaders` List<ConnectApi.H **t** pHeaderOutputRepresentation> HTTP headers for text classifications output. Each **59.0**
header provides a URL you can use to get the result

of the classification. The URL takes a list of text strings
and classifiers that each text string can be classified
in.

#### ConnectApi.TextClassificationsResultOutputRepresentation

Text classifications result.

**Property Name** **Type** **Description** **Available Version**

`classifications` List<ConnectApi.ClassfcationsOutputRepresentation **i**   - List of classifications that each text string was given **59.0**
after analysis.

`classificationsId` String Response ID to receive feedback for classification. **59.0**

#### ConnectApi.TextClassificationsResultWithIdOutputRepresentation

Classified text with status and text classification request IDs.

**Property Name** **Type** **Description** **Available Version**

`id` String Request ID for text classifications. **59.0**

`result` ConnectApi.TextClassfcationsResultOutputRepresentation **i** Result for text classifications. **59.0**

`status` String Request status for text classification. **59.0**

#### ConnectApi.TextSegment

Text segment.

Subclass of ConnectApi.MessageSegment.

No additional properties.

#### ConnectApi.ThemeInfo

Theme information related to an object.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`color` String Color that represents the object. 63.0

`iconUrl` String Icon that represents the object. 63.0

SEE ALSO:

ConnectApi.ObjectMetadata

#### ConnectApi.TimeZone

User's time zone as selected in the user’s personal settings in Salesforce. This value doesn’t reflect a device's current location.

**Name** **Type** **Description** **Available Version**

`gmtOffset` Double Signed offset, in hours, from GMT. 30.0

`name` String Display name of this time zone. 30.0

SEE ALSO:

ConnectApi.UserSettings

#### ConnectApi.Topic

Topic.

**Name** **Type** **Description** **Available Version**

`createdDate` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z. 29.0

`description` String Description of the topic. 29.0

`id` String 18-character ID. 29.0

#### images ConnectApi. Images associated with the topic. 32.0

```
            TopicImages

```

`isBeingDeleted` Boolean

`true` if the topic is currently being deleted; `false` otherwise. 33.0

After the topic is deleted, when attempting to retrieve the topic, the
output is NOT_FOUND.

`name` String Name of the topic. 29.0

`nonLocalized` String Non-localized name of the topic. 36.0

```
Name

```

`talkingAbout` Integer

Number of people talking about this topic over the last two months, 29.0
based on factors such as topic additions and comments on posts
with the topic.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`url` String URL to the topic detail page. 29.0

SEE ALSO:

ConnectApi.ManagedTopic

ConnectApi.TopicPage

#### ConnectApi.TopicEndorsement

assignTopic(communityId, recordId, topicId)

assignTopicByName(communityId, recordId, topicName)

getTopic(communityId, topicId)

updateTopic(communityId, topicId, topic)

createTopic(communityId, name, description)

mergeTopics(communityId, topicId, idsToMerge)

#### ConnectApi.TopicEndorsementCollection

ConnectApi.TopicSuggestion

ConnectApi.TopicsCapability

#### ConnectApi.TopicEndorsement

Represents one user endorsing another user for a single topic.

**Name** **Type** **Description** **Available**
**Version**

`endorsee` `ConnectApi.User` User being endorsed. 30.0

```
            Summary

```

`endorsementId` String 18-character ID of the endorsement record. 30.0

`endorser` `ConnectApi.User` User performing the endorsement. 30.0

```
            Summary

#### topic ConnectApi.Topic Topic the user is being endorsed for. 30.0

```

`url` String URL to the resource for the endorsement record. 30.0

#### ConnectApi.TopicEndorsementCollection

Collection of topic endorsement response bodies.

**Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 30.0

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 30.0
there isn’t a next page.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`previousPageUrl` String Connect REST API URL identifying the previous page, or `null` 30.0
if there isn’t a previous page.

`topicEndorsements` `List<ConnectApi.` List of topic endorsements. 30.0

```
            Topic>

#### ConnectApi.TopicEndorsementSummary

```

Topic endorsement summary.

Subclass of ConnectApi.UserActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`endorsementId` `ID` ID of the topic endorsement. 42.0

#### ConnectApi.TopicImages

Images associated with a topic.

**Property Name** **Type** **Description** **Available Version**

`coverImageUrl` String

`featuredImageUrl` String

SEE ALSO:

#### ConnectApi.Topic ConnectApi.TopicPage

Page of topics.

URL to a topic’s cover image, which appears on the 32.0
topic page. Both topics and managed topics can have
cover images.

URL to a managed topic’s featured image, which 32.0
appears wherever you feature it, for example, on your
Experience Cloud site home page.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 29.0

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 29.0
if there isn’t a next page.

`topics` `List<ConnectApi.` List of topics. 29.0

```
         Topic>

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.TopicsCapability

If a feed element has this capability, the context user can add topics to it. Topics help users organize and discover conversations.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`canAssignTopics` Boolean `true` if a topic can be assigned to the feed element, 32.0
`false` otherwise.

#### items List< ConnectApi. A collection of topics associated with this feed 32.0

`Topic`            - element.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.TopicSuggestion

Topic suggestion.

**Name** **Type** **Description** **Available**
**Version**

#### existingTopic ConnectApi.Topic Topic that already exists or null for a new topic 29.0

`name` String Topic name 29.0

SEE ALSO:

#### ConnectApi.TopicSuggestionPage ConnectApi.TopicSuggestionPage

Page of topic suggestions.

**Name** **Type** **Description** **Available**
**Version**

`TopicSuggestions` `List<ConnectApi.` List of topic suggestions. 29.0

```
               TopicSuggestion>

#### ConnectApi.TopicSummary

```

Summary of a topic.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the topic. 47.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the topic. 47.0

SEE ALSO:

ConnectApi.ManagedContentAssociations

#### ConnectApi.TrackedChangeBundleCapability

If a feed element has this capability, it has a group of other feed elements aggregated into one feed element called a _bundle_ . This type
of bundle aggregates feed tracked changes.

Subclass of ConnectApi.BundleCapability.

**Property Name** **Type** **Description** **Available Version**

#### changes List< ConnectApi. Collection of feed tracked changes. 31.0

`TrackedChangeItem`              

ConnectApi.TrackedChangeItem

Tracked change item.

**Name** **Type** **Description** **Available**
**Version**

`fieldName` String The name of the field that was updated. 28.0

`newValue` String The new value of the field or `null` if the field length is long. 28.0

`oldValue` String The old value of the field or `null` if the field length is long. 28.0

SEE ALSO:

#### ConnectApi.TrackedChangesCapability ConnectApi.TrackedChangeBundleCapability ConnectApi.TrackedChangesCapability

If a feed element has this capability, it contains all changes to a record for a single tracked change event.

Subclass of ConnectApi.FeedElementCapability.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### changes List< ConnectApi. Collection of feed tracked changes. 32.0

`TrackedChangeItem`              

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.TypeAndFilter

Represents the type and filter output.

**Property Name** **Type** **Description** **Available Version**

`filter` `ConnectApi.BaseComparison` Filter. 60.0

`type` String Type. 60.0

#### ConnectApi.UnauthenticatedUser

Unauthenticated user.

Subclass of ConnectApi.Actor.

No additional properties.

Instances of this class are used as the actor for feed items and comments posted by Chatter customers.

#### ConnectApi.UnreadConversationCount

Unread count for a conversation.

**Name** **Type** **Description** **Available**
**Version**

`hasMore` Boolean Specifies if there are more than 50 unread 29.0
messages ( `true` ) or not ( `false` ).

`unreadCount` Integer The total number of unread messages. 29.0

#### ConnectApi.UpDownVoteCapability

If a feed post or comment has this capability, users can upvote or downvote it.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`downVoteCount` Long Number of downvotes. 41.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### myVote ConnectApi. Specifies the context user’s vote. Values are: 41.0

```
             UpDownVoteValue
```

**•** `Down`

**•** `None`

**•** `Up`

`upVoteCount` Long Number of upvotes. 41.0

SEE ALSO:

ConnectApi.CommentCapabilities

ConnectApi.FeedElementCapabilities

#### ConnectApi.UpVoteSummary

Summary of an upvote.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.User

User.

This class is abstract.

Subclass of ConnectApi.ActionWithId.

Superclass of:

#### • ConnectApi.UserDetail • ConnectApi.UserSummary

**Name** **Type** **Description** **Available Version**

`additional` String If one exists, an extra label for the user, for example, 30.0
`Label` “Customer,” “Partner,” or “Acme Corporation.”

`communityNickname` String User’s nickname in the site. 32.0

`companyName` String

`displayName` String

Name of the company. 28.0

If your Experience Cloud site allows access without
logging in, the value is `null` for guest users.

User’s name that is displayed in the site. If nicknames 32.0
are enabled, the nickname is displayed. If nicknames
aren’t enabled, the full name is displayed.

`firstName` String User's first name. In version 39.0 and later, if nicknames 28.0
are enabled, `firstName` is `null` .


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`isChatterGuest` Boolean `true` if user is a Chatter customer; `false` otherwise. 28.0

`isInThisCommunity` Boolean `true` if user is in the same site as the context user; 28.0
`false` otherwise.

`lastName` String User's last name. In version 39.0 and later, if nicknames 28.0
are enabled, `lastName` is `null` .

`outOfOffice` `ConnectApi.OutOfOffice` If one exists, extra out-of-office message for the user. 40.0

`photo` `ConnectApi.Photo` Information about the user's photos. 28.0

`reputation` `ConnectApi.Reputation` Reputation of the user. 32.0

`stamps` List< `ConnectApi.Stamp` 

`title` String

Collection of the user’s stamps. 39.0–43.0

In version 44.0 and later, use SOQL to get a user’s
stamps.

User’s title. 28.0

If your Experience Cloud site allows access without
logging in, the value is `null` for guest users.

`userType` `ConnectApi.UserType` Type of user. 28.0
Enum

**•** `ChatterGuest` —User is an external user in a
private group.

**•** `ChatterOnly` —User is a Chatter Free
customer.

**•** `Guest` —User is unauthenticated.

**•** `Internal` —User is a standard org member.

**•** `Portal` —User is an external user in an
Experience Cloud site.

**•** `System` —User is Chatter Expert or a system user.

**•** `Undefined` —User is a user type that is a
custom object.

SEE ALSO:

ConnectApi.RecommendationAudience

#### ConnectApi.UserActivitiesJob

User activities job.

**Property Name** **Type** **Description** **Available Version**

`jobToken` String Token that identifies the user activities job. 42.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`jobType` String Type of user activities job. Value is `export` or 42.0
`purge` .

`message` String

SEE ALSO:

exportUserActivities(communityId, userId)

purgeUserActivities(communityId, userId)

#### ConnectApi.UserActivityCollection

User activity collection.

Message describing the status and expected outcome 42.0
of the job.

When the job completes, you receive an email with
information about the Salesforce file that contains
#### ConnectApi.UserActivityCollection .

**Property Name** **Type** **Description** **Available Version**

`activityType` String Type of user activity. Values are: 42.0

**•** `Bookmark` —User bookmarked a post.

**•** `ChatterActivity` —Total counts of posts
and comments made and likes and comments
received for a user.

**•** `ChatterLike` —User liked a post or comment.

**•** `Comment` —User commented on a post.

**•** `CompanyVerify` —User verified comment.

**•** `DownVote` —User downvoted a post or
comment.

**•** `FeedEntityRead` —User read a post.

**•** `FeedRead` —User read a feed.

**•** `Mute` —User muted a post.

**•** `Post` —User made a post.

**•** `TopicEndorsement` —User endorsed
another user on a topic or received endorsement
on a topic.

**•** `UpVote` —User upvoted a post or comment.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
userActivities

```

SEE ALSO:

#### List< ConnectApi. Collection of user activities. 42.0

```
UserActivity
```

`Summary` 

ConnectApi.UserActivitiesJob

#### ConnectApi.UserActivitySummary

User activity summary.

This class is abstract.

Superclass of:

**•** ConnectApi.CommentSummary

**•** ConnectApi.FeedPostSummary

**•** ConnectApi.FeedReadSummary

**•** ConnectApi.TopicEndorsementSummary

**•** ConnectApi.UserFeedEntityActivitySummary

**Property Name** **Type** **Description** **Available Version**

`activityDate` Datetime Date of the user activity. 42.0

`activityType` String Type of user activity. Values are: 42.0

**•** `Bookmark` —User bookmarked a post.

**•** `ChatterActivity` —Total counts of posts
and comments made and likes and comments
received for a user.

**•** `ChatterLike` —User liked a post or comment.

**•** `Comment` —User commented on a post.

**•** `CompanyVerify` —User verified comment.

**•** `DownVote` —User downvoted a post or
comment.

**•** `FeedEntityRead` —User read a post.

**•** `FeedRead` —User read a feed.

**•** `Mute` —User muted a post.

**•** `Post` —User made a post.

**•** `TopicEndorsement` —User endorsed
another user on a topic or received endorsement
on a topic.

**•** `UpVote` —User upvoted a post or comment.

`activityUrl` String URL to the user activity. 42.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### community ConnectApi. Experience Cloud site in which the user performed 42.0

`CommunitySummary` the activity.

SEE ALSO:

ConnectApi.UserActivityCollection

#### ConnectApi.UserCapabilities

Capabilities associated with a user profile.

**Name** **Type** **Description** **Available**
**Version**

`canChat` Boolean Specifies if the context user can use Chatter Messenger with the 29.0
subject user ( `true` ) or not ( `false` )

`canDirectMessage` Boolean Specifies if the context user can direct message the subject user 29.0
( `true` ) or not ( `false` )

`canEdit` Boolean Specifies if the context user can edit the subject user’s account 29.0
( `true` ) or not ( `false` )

`canFollow` Boolean Specifies if the context user can follow the subject user’s feed ( `true` ) 29.0
or not ( `false` )

`canViewFeed` Boolean Specifies if the context user can view the feed of the subject user 29.0
( `true` ) or not ( `false` )

`canViewFullProfile` Boolean Specifies if the context user can view the full profile of the subject 29.0
user ( `true` ) or only the limited profile ( `false` )

`isModerator` Boolean Specifies if the subject user is a Chatter moderator or admin ( `true` ) 29.0
or not ( `false` )

SEE ALSO:

ConnectApi.UserProfile

#### ConnectApi.UserChatterSettings

User’s global Chatter settings.

**Name** **Type** **Description** **Available**
**Version**

`defaultGroup` `ConnectApi.GroupEmail` The default frequency with which a user receives email 28.0
`EmailFrequency` `Frequency` Enum from a group when they join it.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.UserDetail

Details about a user in an org.

Subclass of ConnectApi.User.

If the context user doesn’t have permission to see a property, its value is set to `null` .

**Name** **Type** **Description** **Available**
**Version**

`aboutMe` String Text from user's profile. 28.0

`address` `ConnectApi.Address` User’s address. 28.0

`bannerPhoto` `ConnectApi.BannerPhoto` User’s banner photo. 36.0

`chatterActivity` `ConnectApi.Chatter` Chatter activity statistics. 28.0

```
            Activity

```

`chatterInfluence` `ConnectApi.Global` User’s influence rank. 28.0

```
            Influence

```

`email` String User's email address. 28.0

`followersCount` Integer Number of users following this user. 28.0

`followingCounts` `ConnectApi.Following` Information about items the user is following. 28.0

```
            Counts

```

`groupCount` Integer Number of groups user is following. 28.0

`hasChatter` Boolean `true` if user has access to Chatter; `false` otherwise. 31.0

`isActive` Boolean `true` if user is active; `false` otherwise. 28.0

`managerId` String 18-character ID of the user’s manager. 28.0

`managerName` String Locale-based concatenation of manager's first and last 28.0
names.

`phoneNumbers` `List<ConnectApi.Phone` Collection of user's phone numbers. 28.0

```
            Number>

```

`thanksReceived` Integer The number of times the user has been thanked. 29.0

`username` String Username of the user, such as 28.0
_`Admin@mycompany.com`_ .

SEE ALSO:

ConnectApi.UserPage

ConnectApi.UserProfile

#### ConnectApi.UserFeedEntityActivitySummary

User feed entity activity summary.


Apex Reference Guide ConnectApi Output Classes

This class is abstract.

Subclass of ConnectApi.UserActivitySummary.

Superclass of:

**•** ConnectApi.BookmarkSummary

**•** ConnectApi.ChatterActivitySummary

**•** ConnectApi.CompanyVerifySummary

**•** ConnectApi.DownVoteSummary

**•** ConnectApi.FeedEntityReadSummary

**•** ConnectApi.LikeSummary

**•** ConnectApi.MuteSummary

**•** ConnectApi.UpVoteSummary

**Property Name** **Type** **Description** **Available Version**

`feedEntityId` String ID of the feed entity. 42.0

#### ConnectApi.UserGroupDetailPage

A page of groups that a user is a member of.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page. 45.0

#### groups List< ConnectApi. Collection of groups that the user is a member of. 45.0

`ChatterGroupDetail`              

`nextPageUrl` String URL to the next page, or `null` if there is no next 45.0
page.

`previousPageUrl` String URL to the previous page, or `null` if there is no 45.0
previous page.

`total` Integer Total number of groups that the user is a member 45.0
of.

#### ConnectApi.UserGroupPage

A paginated list of groups the context user is a member of.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

```
groups

```

`List<ConnectApi.` List of groups. 28.0

```
ChatterGroup

Summary>

```


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 28.0
if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 28.0
`null` if there isn’t a previous page.

`total` Integer Total number of groups across all pages. 28.0

#### ConnectApi.UserMission

Mission details for a user.

Subclass of ConnectApi.AbstractUserMissionActivity.

**Property Name** **Type** **Description** **Available Version**

`missionName` String Name of the mission. 46.0

`missionThreshold` Integer Threshold of the mission. When a user reaches this 46.0
activity count, the mission is achieved.

#### ConnectApi.UserMissionActivitiesJob

User mission activities job.

**Property Name** **Type** **Description** **Available Version**

`jobToken` String Token that identifies the mission user activities job. 45.0

`jobType` String Type of user activities job, either `export` or 45.0
`purge` .

`message` String

#### ConnectApi.UserMissionActivity

User activity associated with missions.

Subclass of ConnectApi.AbstractUserMissionActivity.

No additional properties.

Message describing the status and expected outcome 45.0
of the job.

When the job completes, you receive an email with
information about the Salesforce file that contains
#### ConnectApi.UserMissionActivityCollection .


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.UserMissionActivityCollection

List of mission activities for a user.

**Property Name** **Type** **Description** **Available Version**

#### community ConnectApi. Experience Cloud site in which the user performed 45.0

`CommunitySummary` activities.

`userId` String ID of the user. 45.0

```
userMission

Activities

```

#### List< ConnectApi. List of mission activities performed by the user. 45.0

```
AbstractUser
```

`MissionActivity` 

`userName` String Name of the user. 45.0

SEE ALSO:

ConnectApi.UserMissionActivitiesJob

#### ConnectApi.UserMissionActivityStatus

Status of mission activity for a user.

**Property Name** **Type** **Description** **Available Version**

`message` String Success or error message. 45.0

`status` String Status of mission activity for a user. 45.0

#### ConnectApi.UserOauthInfo

User OAuth information.

**Name** **Type** **Description** **Available Version**

`availableExternal` `Connect.Oauth` The available OAuth service provider. 37.0

```
EmailService ProviderInfo

```

`isAuthenticated` Boolean Specifies whether the user is authenticated ( `true` ) or not ( `false` ). 37.0

#### ConnectApi.UserPage

Page of users.

**Name** **Type** **Description** **Available**
**Version**

`currentPageToken` Integer Token identifying the current page. 28.0

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`nextPageToken` Integer Token identifying the next page, or `null` if there isn’t a next 28.0
page.

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 28.0
there isn’t a next page.

`previousPageToken` Integer Token identifying the previous page, or `null` if there isn’t 28.0
a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 28.0
`null` if there isn’t a previous page.

`users` `List<ConnectApi.User` List of user detail information. If the context user doesn’t have 28.0
`Detail>` permission to see a property, the property is set to `null` .

#### ConnectApi.UserProfile

Details necessary to render a view of a user profile.

**Name** **Type** **Description** **Available**
**Version**

`capabilities` `ConnectApi.UserCapabilities` The context user’s capabilities specific to the 29.0
subject user’s profile.

`id` String The ID of the user attached to the profile. 29.0

`tabs` `List<ConnectApi.UserProfileTab>` The tabs visible to the context user specific to the 29.0
subject user’s profile.

`url` String The URL of the user’s profile. 29.0

`userDetail` `ConnectApi.UserDetail` The details about the user attached to the profile. 29.0

#### ConnectApi.UserProfileTab

Information about a profile tab.

**Name** **Type** **Descriptio** **Available**
**Version**

`id` String The tab’s unique identifier or 18–character ID 29.0

`isDefault` Boolean Specifies if the tab appears first when clicking the 29.0
user profile ( `true` ) or not ( `false` )

#### tabType ConnectApi.UserProfile Specifies the type of tab 29.0

`TabType` Enum

**•** `CustomVisualForce` —Tab that displays
data from a Visualforce page.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Descriptio** **Available**
**Version**

**•** `CustomWeb` —Tab that displays data from
any external web-based application or web
page.

**•** `Element` —Tab that displays generic
content inline.

**•** `Feed` —Tab that displays the Chatter feed.

**•** `Overview` —Tab that displays user details.

`tabUrl` String The current tab’s content URL (for non built-in 29.0
tab types)

SEE ALSO:

ConnectApi.UserProfile

#### ConnectApi.UserReferencePage

A list of user references.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page. 35.0

`nextPageUrl` String URL to the next page. 35.0

`previousPageUrl` String URL to the previous page. 35.0

`userCount` Integer Number of users in the collection. 35.0

#### users List< ConnectApi. A collection of user references. 35.0

`Reference`            

SEE ALSO:

ConnectApi.CustomListAudienceCriteria

#### ConnectApi.UserSettings

Settings specific to a user.

**Property** **Type** **Description** **Available**
**Version**

`approvalPosts` Boolean User can approve workflows from Chatter posts. 28.0

`canAccess` Boolean User can access personal stream feeds. 40.0

```
   PersonalStreams

```


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

`canFollow` Boolean User can follow users and records. 28.0

`canModify` Boolean User has Modify all Data permission. 28.0

```
   AllData

```

`canOwnGroups` Boolean User can own groups. 28.0

`canViewAllData` Boolean User has View all Data permission. 28.0

`canViewAllGroups` Boolean User has View all Groups permission. 28.0

`canViewAllUsers` Boolean User has View all Users permission. 28.0

`canViewCommunity` Boolean User can see the site switcher menu. 34.0

```
   Switcher

```

`canViewFull` Boolean User can see other user’s Chatter profile. 28.0

```
   UserProfile

```

`canViewPublicFiles` Boolean User can see all files that are public. 28.0

`currencySymbol` String Currency symbol to use for displaying currency values. Applicable only when 28.0
the `ConnectApi.Features.multiCurrency` property is `false` .

`externalUser` Boolean User is a Chatter customer. 28.0

`fileSyncLimit` Integer Maximum number of files user can sync. 32.0

`fileSync` Integer Maximum storage for synced files, in megabytes (MB). 29.0

```
   StorageLimit

```

`folderSync` Integer Maximum number of folders user can sync. 32.0

```
   Limit

```

`hasAccessTo` Boolean User is a member of the internal org. 28.0

```
   InternalOrg

```

`hasChatter` Boolean User has access to Chatter. 31.0

`hasFileSync` Boolean User has Sync Files permission. 28.0

`hasFieldService` Boolean User has Field Service GPS tracking enabled. 41.0

```
   LocationTracking

```

`hasFieldService` Boolean User has access to the Field Service mobile app. 41.0

```
   MobileAccess

```

`hasFileSync` Boolean Administrator for the user’s org allows file sync clients to update automatically. 34.0

```
   ManagedClient

   AutoUpdate

```

`hasRestData` Boolean User has access to REST API. 29.0

```
   ApiAccess

```


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

#### timeZone ConnectApi. The user's time zone as selected in the user’s personal settings in Salesforce. 30.0

`TimeZone` This value does not reflect a device's current location.

`userDefault` String The ISO code for the default currency. Applicable only when the 28.0
`CurrencyIsoCode` `ConnectApi.Features.multiCurrency` property is `true` .

`userId` String 18-character ID of the user. 28.0

`userLocale` String Locale of user. 28.0

SEE ALSO:

ConnectApi.OrganizationSettings

#### ConnectApi.UserSummary

User summary.

Subclass of ConnectApi.User.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`isActive` Boolean `true` if user is active; `false` otherwise. 28.0

SEE ALSO:

ConnectApi.ChatterConversation

ConnectApi.ChatterConversationSummary

ConnectApi.ChatterGroup

ConnectApi.ChatterLike

ConnectApi.DashboardComponentSnapshot

ConnectApi.DirectMessageMemberPage

ConnectApi.GroupMembershipRequest

ConnectApi.GroupMember

ConnectApi.FeedFavorite

ConnectApi.OriginCapability

ConnectApi.PlatformAction

ConnectApi.DirectMessageMemberPage

ConnectApi.DirectMessageMemberActivity

ConnectApi.ChatterMessage

ConnectApi.Comment

ConnectApi.File

ConnectApi.MentionSegment

ConnectApi.QuestionAndAnswersCapability

ConnectApi.SocialPostCapability

ConnectApi.TopicEndorsement

#### ConnectApi.VerifiedCapability

If a comment has this capability, users with permission can mark it as verified or unverified.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isVerifiableByMe` Boolean

Specifies whether the context user has permission 41.0
to mark comments as verified or unverified ( `true` )
or not ( `false` ).

`isVerified` Boolean Specifies whether the comment is marked as verified 41.0
( `true` ) or not ( `false` ).

`isVerifiedBy` Boolean Specifies whether the comment is marked as verified 43.0
`Anonymized` by an anonymous user ( `true` ) or not ( `false` ). If
the comment has never been marked as verified or


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

unverified, `null` . Also `null` if the context user
doesn’t have permission to mark comments as
verified or unverified.

`lastVerifiedByUser` `ConnectApi.UserSummary` User who last marked the comment as verified or 41.0
unverified, otherwise `null` . Also `null` if the

context user doesn’t have permission to mark
comments as verified or unverified.

`lastVerifiedDate` Datetime Date when the comment was last marked as verified 41.0
or unverified, otherwise `null` . Also `null` if the

context user doesn’t have permission to mark
comments as verified or unverified.

SEE ALSO:

ConnectApi.CommentCapabilities

#### ConnectApi.Vote

An upvote or downvote on a feed element or comment.

**Property Name** **Type** **Description** **Available Version**

#### type ConnectApi. Type of vote for a feed element or comment. 42.0

```
             UpDownVoteValue
```

**•** `Down`

**•** `Up`

#### user ConnectApi. User who voted on the feed element or comment. 42.0

```
             UserSummary

#### votedItem ConnectApi. Reference to the feed element or comment that was 42.0
```

`Reference` voted on.

SEE ALSO:

#### ConnectApi.VotePage ConnectApi.VotePage

A page of upvotes or downvotes on a feed element or comment.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` Integer Token identifying the current page. 42.0

`currentPageUrl` String Connect REST API URL identifying the current page. 42.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### items List< ConnectApi.

`Vote`         

Collection of users and their upvotes or downvotes. 42.0

Upvotes include likes and upvotes. For example, if a
post receives five likes and three upvotes, the number

of upvotes is eight. For this reason, the collection of
users and their upvotes also includes users who liked
the post or comment. If a user both liked and upvoted
a post, they appear only once in the collection.

`nextPageToken` Integer Token identifying the next page, or `null` if there 42.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 42.0
`null` if there isn’t a next page.

`previousPageToken` Integer Token identifying the previous page, or `null` if 42.0
there isn’t a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 42.0
or `null` if there isn’t a previous page.

`total` Long

#### ConnectApi.WebStoreMetaConfig

Details of a webstore Meta configuration.

Total number of upvotes or downvotes for the feed 42.0
element or comment.

The number of upvotes includes the number of likes
and upvotes. For example, if a post receives five likes

and three upvotes, the total number of upvotes is
eight. If a user both liked and upvoted a post, we
count that as two upvotes.

**Property Name** **Type** **Description** **Available Version**

`adAccountExtKey` String External key for Meta Ad Account. 64.0

`businessManagerExtKey` String External key for Meta Business Manager. 64.0

`catalogExtKey` String External key for Meta Catalog. 64.0

`commerceMerchantSettingsExtKey` String External key for Meta Commerce Merchant Settings. 64.0

`id` String ID of the Webstore Meta Config entity. 64.0

`pageExtKey` String External key for Meta Page. 64.0

`profileExtKey` String External key for Meta Instagram Profile. 64.0

`trackerExtKey` String External key for Meta Pixel. 64.0

`webStoreId` String ID of the webstore. 64.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.WebStoreMetaConfigurations

List of webstore Meta configurations.

**Property Name** **Type** **Description** **Available Version**

#### configurations List< ConnectApi.WebStoreMetaConfig > List of webstore Meta configurations. 64.0

`status` `ConnectApi.SocialStatusRepresentation` Status specifying whether retrieval of webstore Meta 64.0
configurations was success.

#### ConnectApi.Wishlist

Wishlist, including summary and items.

**Property Name** **Type** **Description** **Available Version**

```
page

```

#### ConnectApi. Page of wishlist items. 49.0

```
WishlistItem

Collection

```

#### summary ConnectApi. Summary of the wishlist. 49.0

```
           WishlistSummary

```

SEE ALSO:

#### ConnectApi.WishlistsSummary ConnectApi.WishlistItem

Item in a wishlist.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 49.0
the product.

#### error ConnectApi. Error information. 49.0

```
           ErrorResponse

```

`listPrice` Double List price of the wishlist item. 49.0

#### productSummary ConnectApi. Product summary for the wishlist item. 49.0

```
           CartItemProduct

```

`salesPrice` Double Sales price of the wishlist item. 49.0

`wishlistItemId` String ID of the wishlist item. 49.0

SEE ALSO:

#### ConnectApi.WishlistItemCollection


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.WishlistItemCollection

Collection of wishlist items.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 49.0
the product.

`currentPageToken` String Token identifying the current page. 49.0

`currentPageUrl` String Connect REST API URL identifying the current page. 49.0

`hasErrors` Boolean Specifies whether at least one of the results contains 49.0
an error ( `true` ) or not ( `false` ).

#### items List< ConnectApi. Collection of wishlist items. 49.0

`WishlistItem`            

`nextPageToken` String Token identifying the next page, or `null` if there 49.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 49.0
`null` if there isn’t a next page.

`previousPageToken` String Token identifying the previous page, or `null` if 49.0
there isn’t a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 49.0
or `null` if there isn’t a previous page.

SEE ALSO:

#### ConnectApi.Wishlist ConnectApi.WishlistsSummary

List of wishlist summaries and the displayed list for the context user.

**Property Name** **Type** **Description** **Available Version**

#### displayedList ConnectApi. Oldest wishlist displayed for the context user. 49.0

```
             Wishlist

#### summaries List< ConnectApi. Summary of wishlists belonging to the context user. 49.0
```

`WishlistSummary`            

`wishlistCount` Integer Total number of wishlists belonging to the context 49.0
user.

#### ConnectApi.WishlistSummary

Summary of a wishlist.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`createdDate` Datetime Created date for the wishlist in ISO 8601 format, for 49.0
example, 2011-02-25T18:24:31.000Z.

`id` String ID of the wishlist. 49.0

`modifiedDate` Datetime Last modified date of the wishlist in ISO 8601 format, 49.0
for example, 2011-02-25T18:24:31.000Z.

`name` String Name of the wishlist. 49.0

`wishlistProductCount` Integer Unique product count in the wishlist. 49.0

SEE ALSO:

#### ConnectApi.Wishlist

ConnectApi.WishlistsSummary

#### ConnectApi.WishlistToCartResult

Result of adding a wishlist to a cart.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the cart to which the products were added. 49.0

#### failedWishlist List< ConnectApi. Wishlist items that weren’t successfully added to the 49.0

`ToCartItems` `CartItemResult`   - cart.

`productsFailed` Integer Total number of products that weren’t added to the 49.0
`Count` cart.

`productsRequested` Integer Total number of products requested to add to the 49.0
`Count` cart.

`productsSucceeded` Integer Total number of products that were successfully 49.0
`Count` added to the cart.

#### succeededWishlist List< ConnectApi. Wishlist items that were successfully added to the 49.0

`ToCartItems` `CartItemResult`   - cart.

#### ConnectApi.WorkStepPicklistValueAttribute

Work step picklist value attributes.

Subclass of ConnectApi.AbstractPicklistValueAttributes

[To use work step status picklist value attributes, you must have Field Service enabled in your org.](https://developer.salesforce.com/docs/atlas.en-us.260.0.field_service_dev.meta/field_service_dev/fsl_dev_set_up.htm)

**Property Name** **Type** **Description** **Available Version**

`sortOrder` Integer Order in which the work step statuses are displayed 66.0
in the status category’s picklist.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`statusCode` String Status category of the work step. 66.0

[For more information, see the WorkStepStatus object documentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_workstepstatus.htm)

#### ConnectApi.WrappedMapObject

Map of a parameter name and value.

**Property Name** **Type** **Description** **Available Version**

`wrappedMap` Map<String, Object> Map of parameter name and value. 60.0

#### ConnectApi.Zone

Information about a Chatter Answers zone.

**Name** **Type** **Description** **Available**
**Version**

`description` String The description of the zone. 29.0

`id` String The zone ID. 29.0

`isActive` Boolean Indicates whether or not the zone is active. 29.0

`isChatterAnswers` Boolean Indicates whether or not the zone is available for 29.0
Chatter Answers.

`name` String Name of the zone. 29.0

`url` String The URL of the zone. 30.0

#### visibility ConnectApi.ZoneShowIn Zone visibility type. 29.0

**•** `Community` —Available in an Experience
Cloud site.

**•** `Internal` —Available internally only.

**•** `Portal` —Available in a portal.

`visibilityId` String

SEE ALSO:

#### ConnectApi.ZonePage

If the zone is available in a site, this property 29.0
contains the ID of the site. If the zone is available
to all sites, this property contains the value `All` .


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ZonePage

Page of zones.

**Name** **Type** **Description** **Available**
**Version**

`zones` `List<ConnectApi.Zone>` A list of one or more zones. 29.0

`currentPageUrl` String Connect REST API URL identifying the current 29.0
page.

`nextPageUrl` String Connect REST API URL identifying the next page, 29.0
or `null` if there isn’t a next page.

#### ConnectApi.ZoneSearchPage

Page of zone search results.

**Name** **Type** **Description** **Available**
**Version**

`currentPageToken` String Token identifying the current page. 29.0

`currentPageUrl` String Connect REST API URL identifying the current 29.0
page.

`items` `List<ConnectApi.ZoneSearchResult`   - List of search results. 29.0

`nextPageToken` String Token identifying the next page, or `null` if there 29.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, 29.0
or `null` if there isn’t a next page.

#### ConnectApi.ZoneSearchResult

Information about a specific zone search result.

**Name** **Type** **Description** **Available**
**Version**

`hasBestAnswer` Boolean Indicates if the search result has a best answer. 29.0

`id` String ID of the search result. The search result can be a 29.0
question or an article.

`title` String Title of the search result. 29.0

#### type ConnectApi.ZoneSearch Specifies the zone search result type. 29.0

`ResultType` Enum

**•** `Article` —Search results contain only
articles.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

**•** `Question` —Search results contain only
questions.

`voteCount` String Number of votes given to the search result. 29.0

SEE ALSO:

ConnectApi.ZoneSearchPage

#### Retired ConnectApi Output Classes

These `ConnectApi` output classes are retired.

IN THIS SECTION:

ConnectApi.ApprovalAttachment
Attach an approval to a feed item.

ConnectApi.BasicTemplateAttachment
Attachments in feed items with type `BasicTemplate` .

ConnectApi.CanvasTemplateAttachment
Attachments in feed items with type `CanvasPost` .

ConnectApi.CaseComment
Attachments in feed items with type `CaseCommentPost` .

ConnectApi.ContentAttachment
Attachments in feed items with the type `ContentPost` .

ConnectApi.DashboardComponentAttachment
Attachments in feed items with type `DashboardSnapshot` .

ConnectApi.DatacloudCompany
Information about a Data.com company.

ConnectApi.DatacloudCompanies
Lists all companies that were purchased in a specific order, page URLs, and the number of companies in the order.

ConnectApi.DatacloudContact
Information about a Data.com contact.

ConnectApi.DatacloudContacts
Lists all contacts that were purchased in the specific order, page URLs, and the number of contacts in the order.

ConnectApi.DatacloudOrder
Represents a Datacloud order.

ConnectApi.DatacloudPurchaseUsage
Information about Data.com point usage for monthly and list pool users.

ConnectApi.EmailMessage
Email message from a case.


Apex Reference Guide ConnectApi Output Classes

ConnectApi.FeedItemAttachment
Feed item attachment.

ConnectApi.FeedItemPage
A paged collection of `ConnectApi.FeedItem` objects.

ConnectApi.FeedItemTopicPage
Feed item topic page.

ConnectApi.FeedPoll
Attachment of `ConnectApi.FeedItem` objects where the `type` property is `PollPost` .

ConnectApi.LinkAttachment
Link attached to a feed item.

ConnectApi.NonEntityRecommendation
A recommendation for a non-Salesforce entity, such as an application.

ConnectApi.RecordSnapshotAttachment
Fields of a record at the point in time when the record was created.

ConnectApi.SocialAccount
A social account on a social network.

ConnectApi.SocialAccountRelationship
Follow relationship between a managed social account and a social persona.

ConnectApi.SocialPostCapability
If a feed element has this capability, it can interact with a social post on a social network.

ConnectApi.SocialPostIntents
Intents available for a social post.

ConnectApi.SocialPostMassApprovalOutput
Approval or rejection of a large number of social posts.

ConnectApi.SocialPostStatus
The status of a social post.

ConnectApi.TrackedChangeAttachment
Tracked change attachment to a feed item.

##### ConnectApi.ApprovalAttachment

Attach an approval to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.ApprovalCapability is used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available Version**

`id` String A work item ID. 28.0–31.0

`postTemplateFields` `List` Collection of approval post template fields 28.0–31.0

```
            <ConnectApi.

            ApprovalPost

            TemplateField>

```


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`process` String An approval step ID. 30.0–31.0

```
   InstanceStepId

```

```
status

```

##### ConnectApi. Status of a workflow process. 28.0–31.0

```
WorkflowProcess
```

**•** `Approved`

`Status` Enum

**•** `Approved`

**•** `Fault`

**•** `Held`

**•** `NoResponse`

**•** `Pending`

**•** `Reassigned`

**•** `Rejected`

**•** `Removed`

**•** `Started`

##### ConnectApi.BasicTemplateAttachment

Attachments in feed items with type `BasicTemplate` .

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.EnhancedLinkCapability is
used.

Subclass of ConnectApi.FeedItemAttachment.

**Property** **Type** **Description** **Available**
**Version**

`description` String An optional description with a 500 character limit. 28.0–31.0

`icon` `ConnectApi.Icon` An optional icon. 28.0–31.0

`linkRecordId` String If `linkURL` refers to a Salesforce record, `linkRecordId` 28.0–31.0
contains the ID of the record.

`linkUrl` String

An optional URL to a detail page if there is more content that 28.0–31.0
can’t be displayed inline. Do not specify `linkUrl` unless you
specify a `title` .

`title` String An optional title to the detail page. If `linkUrl` is specified, the 28.0–31.0
title links to `linkUrl` .

##### ConnectApi.CanvasTemplateAttachment

Attachments in feed items with type `CanvasPost` .

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.CanvasCapability is used.

Subclass of ConnectApi.FeedItemAttachment.


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available Version**

`description` String Optional. Description of the canvas app. The maximum length of this 29.0–31.0
field is 500 characters.

`developerName` String Specifies the developer name (API name) of the canvas app. 29.0–31.0

`height` String Optional. The height of the canvas app in pixels. Default height is 200 29.0–31.0
pixels.

`icon` `ConnectApi.Icon` The canvas app icon. 29.0–31.0

`namespacePrefix` String Optional. The namespace prefix of the Developer Edition organization 29.0–31.0
in which the canvas app was created.

`parameters` String

Optional. Parameters passed to the canvas app in JSON format. Example: 29.0–31.0

```
{'isUpdated'='true'}

```

`thumbnailUrl` String Optional. A URL to a thumbnail image for the canvas app. Maximum 29.0–31.0
dimensions are 120x120 pixels.

`title` String Specifies the title of the link used to call the canvas app. 29.0–31.0

##### ConnectApi.CaseComment

Attachments in feed items with type `CaseCommentPost` .

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.CaseCommentCapability is
used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available**
**Version**

```
actorType

createdBy

```

##### ConnectApi. Type of user who made the comment. 28.0–31.0

```
CaseActorType
```

**•** `Customer` —if a Chatter customer made the comment

Enum

##### ConnectApi. Comment’s creator 28.0–31.0

```
User

Summary

```

**•** `Customer` —if a Chatter customer made the comment

**•** `CustomerService` —if a service representative made the
comment

`createdDate` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z 28.0–31.0

`id` String Comment’s 18–character ID 28.0–31.0

`published` Boolean Specifies whether the comment has been published 28.0–31.0

`text` String Comment’s text 28.0–31.0


Apex Reference Guide ConnectApi Output Classes

##### ConnectApi.ContentAttachment

Attachments in feed items with the type `ContentPost` .

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.ContentCapability is used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available Version**

`checkSum` String MD5 checksum for the file. 28.0–31.0

`contentUrl` String URL for link files and Google Docs; otherwise the value is `null` . 31.0–31.0

`description` String Description of the attachment. 28.0–31.0

`downloadUrl` String File’s URL. This value is `null` if the content is a link or a Google Doc. 28.0–31.0

`fileExtension` String File’s extension. 28.0–31.0

`fileSize` String Size of the file in bytes. If size cannot be determined, returns 28.0–31.0
`unknown` .

`fileType` String Type of file. 28.0–31.0

`hasImagePreview` Boolean `true` if the file has a preview image available, otherwise, `false` . 28.0–29.0

`hasPdfPreview` Boolean `true` if the file has a PDF preview available, otherwise, `false` . 28.0–31.0

`id` String Content’s 18-character ID. 28.0–31.0

`isInMyFileSync` Boolean `true` if the file is synced with Salesforce Files Sync; `false` otherwise. 28.0–31.0

Note: Salesforce Files Sync was retired on May 25, 2018.

`mimeType` String File’s MIME type. 28.0–31.0

`renditionUrl` String URL to the file’s rendition resource. 28.0–31.0

`renditionUrl` String URL to the 240 x 180 rendition resource for the file.For shared files, 30.0–31.0
`240By180` renditions process asynchronously after upload. For private files,
renditions process when the first file preview is requested, and aren’t
available immediately after the file is uploaded.

`renditionUrl` String URL to the 720 x 480 rendition resource for the file.For shared files, 30.0–31.0
`720By480` renditions process asynchronously after upload. For private files,
renditions process when the first file preview is requested, and aren’t
available immediately after the file is uploaded.

`textPreview` String Text preview of the file if available; `null` otherwise. 30.0–31.0

`thumb120By90` String Specifies the rendering status of the 120 x 90 preview image of the 30.0–31.0
`RenditionStatus` file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

**•** `Na` —Rendering is not available for this image.

`thumb240By180` String Specifies the rendering status of the 240 x 180 preview image of the 30.0–31.0
`RenditionStatus` file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`thumb720By480` String Specifies the rendering status of the 720 x 480 preview image of the 30.0–31.0
`RenditionStatus` file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`title` String Title of the file. 28.0–31.0

`versionId` String 18-character ID for this version of the content. 28.0–31.0

##### ConnectApi.DashboardComponentAttachment

Attachments in feed items with type `DashboardSnapshot` .

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later,
ConnectApi.DashboardComponentSnapshotCapability is used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available Version**

`componentId` String Component’s 18–character ID. 28.0–31.0

`componentName` String Name of the component. If no name is saved with the component, 28.0–31.0
returns the localized string, “Untitled Component.”.

`dashboardBodyText` String

Text displayed next to the actor in the body of a feed item. This is used 28.0–31.0
instead of the default body text. If no text is specified, and there is no
default body text, returns null.

`dashboardId` String Dashboard’s 18–character ID. 28.0–31.0

`dashboardName` String Name of the dashboard. 28.0–31.0

`fullSizeImageUrl` String URL of the full-sized dashboard image. 28.0–31.0

`lastRefreshDate` Datetime ISO8601 date string, for example, 2011-02-25T18:24:31.000Z, 28.0–31.0
specifying when this dashboard was last refreshed.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`lastRefreshDate` String The text of the last refresh date to be displayed, such as, “Last refreshed 28.0–31.0
`DisplayText` on October 31, 2011.”

```
runningUser

```

##### ConnectApi. The user running the dashboard. 28.0–31.0

```
User

Summary

```

`thumbnailUrl` String URL of the thumbnail-sized dashboard image. 28.0–31.0

##### ConnectApi.DatacloudCompany

Information about a Data.com company.

All company information is visible for companies that you purchased and own. If you haven’t purchased a company, some of the fields
are hidden. Hidden fields are fully or partially hidden by asterisks “***.”

**Property Name** **Type** **Description** **Available Version**

`activeContacts` Integer The number of active Data.com contacts who 32.0
work in the company.

`address` ConnectApi.Address

`annualRevenue` Double

The postal address for the company. This is 32.0
typically a physical address that can include the
city, state, street, and postal code.

The amount of money that the company makes 32.0
in one year. Annual revenue is measured in US
dollars.

`companyId` String A unique numerical identifier for the company. 32.0
This is the Data.com identifier for a company.

`description` String

`dunsNumber` String

`industry` String

`isInactive` Boolean

A brief synopsis of the company that provides 32.0
a general overview of the company and what it
does.

A randomly generated nine-digit number that’s 32.0
assigned by Dun & Bradstreet (D&B) to identify
unique business establishments.

A description of the type of industry such as 32.0
“Telecommunications,” “Agriculture,” or
“Electronics.”

Indicates whether this company is active (true) 32.0
or not (false). Inactive companies have
out-of-date information in Data.com.

`isOwned` Boolean 32.0

**•** True: You or your organization owns this
company.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** False: Neither you nor your organization
owns this company.

`naicsCode` String North American Industry Classification System 32.0
(NAICS) codes were created to provide more

details about a business’s service orientation.
The code descriptions are focused on what a
business does.

`naicsDescription` String A description of the NAICS classification. 32.0

`name` String The name of the company. 32.0

`numberOf` Integer The number of employees who are working for 32.0
`Employees` the company.

`ownership` String 32.0
The type of ownership of the company:

**•** Public

**•** Private

**•** Government

**•** Other

`phoneNumbers` ConnectApi.PhoneNumber

`sic` String

32.0
The list of telephone numbers for the company,
including the type. Here are some possible types
of telephone numbers.

**•** Mobile

**•** Work

**•** Fax

Standard Industrial Codes (SIC) is a numbering 32.0
convention that indicates what type of service
a business provides. It’s a four-digit value.

`sicDescription` String A description of the SIC classification. 32.0

`site` String

Company’s site. For example, HQ, Single 32.0
Location, or Branch.

An organization status of the company.

**•** Branch: a secondary location to a
headquarter location.

**•** Headquarter: the parent company has
branches or subsidiaries.

**•** Single Location: a single business with no
subsidiaries or branches.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`tickerSymbol` String The symbol that uniquely identifies companies 32.0
that are traded on public stock exchanges.

`tradeStyle` String A legal name under which a company conducts 32.0
business.

`updatedDate` Datetime The date of the most recent change to this 32.0
company’s information.

`website` String The standard URL for the company’s home page. 32.0

`yearStarted` String The year when the company was founded. 32.0

##### ConnectApi.DatacloudCompanies

Lists all companies that were purchased in a specific order, page URLs, and the number of companies in the order.

**Property Name** **Type** **Description** **Available**
**Version**

`companies` ConnectApi.DatacloudCompany A detailed list of companies that were 32.0
part of a single order.

`currentPageUrl` String The URL for the current page of a list of 32.0
companies.

`nextPageUrl` String

Connect REST API URL identifying the 32.0
next page, or `null` if there isn’t a next
page.

`previousPageUrl` String The URL to the previous page of 32.0
companies that were viewed before the

current page. If this value is `null`,
there’s no previous page.

`total` Integer The number of companies in the order. 32.0
You can calculate the number of pages

to display by dividing this number by
your page size. The default page size is
25.

##### ConnectApi.DatacloudContact

Information about a Data.com contact.

All contact information is visible for contacts that you purchased. If you have not purchased a contact, some of the fields will be hidden.
Hidden fields are fully or partially hidden by asterisks “***.”

**Property Name** **Type** **Description** **Available Version**

`address` ConnectApi.Address The contact’s business address. 32.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`companyId` String

A unique numerical identifier for the company where 32.0
the contact works. This is the Data.com identifier for
a company.

`companyName` String The company name where the contact works. 32.0

`contactId` String A unique numerical identifier for the contact. This is 32.0
the Data.com identifier for a contact.

`department` String The department in the company where the contact 32.0
works. Here are some possible departments.

**•** Engineering

**•** IT

**•** Marketing

**•** Sales

`email` String The most current business email address for the 32.0
contact.

`firstName` String The first name of the contact. 32.0

`isInactive` Boolean

Whether this contact is active (true) or not (false). 32.0
Inactive contacts have out-of-date information in
Data.com.

`isOwned` Boolean Whether this contact is owned (true) or not (false). 32.0

`lastName` String The last name of the contact. 32.0

`level` String A human resource label that designates a person’s 32.0
level in the company. Here are some possible levels.

**•** C-Level

**•** Director

**•** Manager

**•** Staff

`phoneNumbers` ConnectApi.PhoneNumber Telephone numbers for the contact, which can 32.0
include direct-dial business telephone numbers,

mobile telephone numbers, and business
headquarters telephone numbers. The type of
telephone number is also indicated.

`title` String The title of the contact, such as CEO or Vice President. 32.0

`updatedDate` Datetime The date of the most recent change to this contact’s 32.0
information.

SEE ALSO:

ConnectApi.DatacloudContacts


Apex Reference Guide ConnectApi Output Classes

##### ConnectApi.DatacloudContacts

Lists all contacts that were purchased in the specific order, page URLs, and the number of contacts in the order.

**Property Name** **Type** **Description** **Available Version**

`contacts` A detailed list of purchased contacts. 32.0
##### List< ConnectApi.DatacloudContact >

`currentPageUrl` String URL to the current page of contacts. 32.0

`nextPageUrl` String Connect REST API URL identifying the next page, or 32.0
`null` if there isn’t a next page.

`previousPageUrl` String URL to the previous page of contacts. This value is 32.0
null if there is no previous page.

`total` Integer

##### ConnectApi.DatacloudOrder

Represents a Datacloud order.

Number of contacts that are associated with this 32.0
order. Can be greater than the number of contacts
that are shown on a single page.

**Property Name** **Type** **Description** **Available Version**

`entityUrl` String URL to a list of contacts or companies that were 32.0
purchased with this order.

`id` String Unique number that’s used to track your order 32.0
information.

`purchaseCount` Integer Number of contacts or companies that were 32.0
purchased for this order.

`purchaseDate` Datetime Purchase date for this order. 32.0

`url` String GET request URL for this order. 32.0

##### ConnectApi.DatacloudPurchaseUsage

Information about Data.com point usage for monthly and list pool users.

**Property Name** **Type** **Description** **Available Version**

`listpoolCreditsAvailable` Integer The points or credits that are available in a 32.0
pool of credits for your organization. This

pool of credits can be used by any List Pool
User in your organization.

`listpoolCreditsUsed` Integer

The points or credits that have been used 32.0
from a pool of credits that are used by List
Pool Users to purchase records.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`monthlyCreditsAvailable` Integer

The total credits that are assigned to a 32.0
Monthly User. Unused credits expire at the
end of each month.

`monthlyCreditsUsed` Integer The credits that are used by a Monthly User 32.0
for the current month.

##### ConnectApi.EmailMessage

Email message from a case.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.EmailMessageCapability is
used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available**
**Version**

```
direction

```

##### ConnectApi.Email The direction of the email message. 29.0–31.0

```
MessageDirection
```

**•** `Inbound` —An inbound message (sent by a customer).

Enum

**•** `Inbound` —An inbound message (sent by a customer).

**•** `Outbound` —An outbound message (sent to a customer
by a support agent).

`emailMessageId` String The ID of the email message. 29.0–31.0

`subject` String The subject of the email message. 29.0–31.0

`textBody` String The body of the email message. 29.0–31.0

`toAddresses` `List<ConnectApi.EmailAddress>` A list of email addresses to send the message to. 29.0–31.0

##### ConnectApi.FeedItemAttachment

Feed item attachment.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.FeedElementCapability is used.

This class is abstract.

Subclasses:

**•** ConnectApi.ApprovalAttachment

**•** ConnectApi.BasicTemplateAttachment

**•** ConnectApi.CanvasTemplateAttachment

**•** Connectapi.EmailMessage

**•** ConnectApi.CaseComment

**•** ConnectApi.ContentAttachment

**•** ConnectApi.DashboardComponentAttachment


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.FeedPoll

**•** ConnectApi.LinkAttachment

**•** ConnectApi.RecordSnapshotAttachment

**•** ConnectApi.TrackedChangeAttachment

Message segments in a feed item are typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as
`ConnectApi.FeedItemCapability` . Record fields are typed as `ConnectApi.AbstractRecordField` . These classes
are all abstract and have several concrete subclasses. At runtime you can use `instanceof` to check the concrete types of these objects
and then safely proceed with the corresponding downcast. When you downcast, you must have a default case that handles unknown
subclasses.

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

##### ConnectApi.FeedItemPage A paged collection of ConnectApi.FeedItem objects.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.FeedElementPage is used.

**Name** **Type** **Description** **Available**
**Version**

`currentPageToken` String Token identifying the current page. 28.0–31.0

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0–31.0

`isModifiedToken` String

Opaque polling token to use in the _`since`_ parameter of the 28.0–31.0
`ChatterFeeds.isModified` method. The token
describes when the feed was last modified.

Important: This feature is available through a Feed
Polling pilot program. This pilot program is closed and
not accepting new participants.

`isModifiedUrl` String Connect REST API URL with a _`since`_ request parameter 28.0–31.0
that contains an opaque token that describes when the feed

was last modified. Returns `null` if the feed isn’t a news
feed. Use this URL to poll a news feed for updates.

Important: This feature is available through a Feed
Polling pilot program. This pilot program is closed and
not accepting new participants.

`items` `List<ConnectApi.FeedItem>` List of feed items 28.0–31.0

`nextPageToken` String Token identifying the next page, or `null` if there isn’t a next 28.0–31.0
page.

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 28.0–31.0
if there isn’t a next page.

`updatesToken` String Token to use in an `updatedSince` parameter, or `null` 30.0–31.0
if not available.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`updatesUrl` String A Connect REST API resource with a query string containing 30.0–31.0
the value of the `updatesToken` property. The resource

returns the feed items that have been updated since the last
request. Use the URL as it is—do not modify it. Property is
`null` if not available.

##### ConnectApi.FeedItemTopicPage

Feed item topic page.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.TopicsCapability is used.

**Name** **Type** **Description** **Available**
**Version**

`canAssignTopics` Boolean `true` if a topic can be assigned to the feed item, `false` 28.0–31.0
otherwise.

`topics` `List<ConnectApi.` List of topics. 28.0–31.0

```
            Topic>

##### ConnectApi.FeedPoll Attachment of ConnectApi.FeedItem objects where the type property is PollPost .

```

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.PollCapability is used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available Version**

```
choices

```

`List<ConnectApi.` List of choices for poll. 28.0–31.0

```
FeedPoll

Choice>

```

`myChoiceId` String ID of the poll choice that the context user has voted for in this poll. 28.0–31.0
Returns `null` if the context user hasn’t voted.

`totalVoteCount` Integer Total number of votes cast on the feed poll item. 28.0–31.0

##### ConnectApi.LinkAttachment

Link attached to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.LinkCapability is used.

Subclass of ConnectApi.FeedItemAttachment.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`title` String Title given to the link if available, otherwise, `null` . 28.0–31.0

`url` String The link URL. 28.0–31.0

##### ConnectApi.NonEntityRecommendation

A recommendation for a non-Salesforce entity, such as an application.

Subclass of ConnectApi.AbstractRecommendation.

##### Important: ConnectApi.NonEntityRecommendation isn’t used in version 34.0 and later. In version 34.0 and later,

ConnectApi.EntityRecommendation is used for all recommendations.

**Property Name** **Type** **Description** **Available Version**

`displayLabel` String Localized label of the non-entity object. 32.0

`motif` `ConnectApi.Motif` Motif for the non-entity object. 32.0

##### ConnectApi.RecordSnapshotAttachment

Fields of a record at the point in time when the record was created.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.RecordSnapshotCapability is
used.

Subclass of ConnectApi.FeedItemAttachment.

**Name** **Type** **Description** **Available**
**Version**

##### recordView ConnectApi. The representation of the record. 29.0–31.0

```
            RecordView

##### ConnectApi.SocialAccount

```

A social account on a social network.

**Property Name** **Type** **Description** **Available Version**

`externalSocial` String ID of the external social account, if available. 38.0

```
   AccountId

```

`handle` String Social handle, screen name, or alias that identifies 36.0
this account.

`name` String Name of the account as defined by the account's 36.0
owner.

`profileUrl` String URL to the account's profile. 36.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`socialPersonaId` String ID of the social persona account, if the external social 39.0
account ID isn’t available.

SEE ALSO:

##### ConnectApi.SocialPostCapability ConnectApi.SocialAccountRelationship

Follow relationship between a managed social account and a social persona.

**Property Name** **Type** **Description** **Available Version**

`isFollowed` Boolean Specifies whether the social account is followed by 46.0
the social persona.

`isFollowing` Boolean Specifies whether the social account is following the 46.0
social persona.

`socialAccountId` String ID of the social account. 46.0

`socialPersonaId` String ID of the social persona. 46.0

##### ConnectApi.SocialPostCapability

If a feed element has this capability, it can interact with a social post on a social network.

Subclass of ConnectApi.FeedElementCapabilities.

**Property Name** **Type** **Description** **Available Version**

##### author ConnectApi.SocialAccount Social account that authored the social post. 36.0

`content` String Content body of the social post. 36.0

`deletedBy` `ConnectApi.UserSummary` User who deleted the social post. 38.0

`hiddenBy` `ConnectApi.UserSummary` User who hid the social post. 41.0

`icon` `ConnectApi.Icon` Icon of the social network. 36.0

`id` String ID associated with the social post Salesforce record. 36.0

`isOutbound` Boolean If `true`, the social post originated from the 36.0
Salesforce application.

`likedBy` String External social account who liked the social post. 40.0

```
messageType

```

##### ConnectApi. Message type of the social post. Values are: 38.0

```
SocialPost
```

**•** `Comment`
```
MessageType

```

**•** `Comment`

**•** `Direct`

**•** `Post`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `PrivateMessage`

**•** `Reply`

**•** `Retweet`

**•** `Tweet`

`name` String Title or heading of the social post. 36.0

`postUrl` String External URL to the social post on the social network. 36.0

```
provider

```

`ConnectApi.` Social network that this social post belongs to. Values 36.0
`SocialNetwork` are:

```
Provider
```

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

`recipient` `ConnectApi.SocialAccount` Social account that is the recipient of the social post. 36.0

`recipientId` String ID of the recipient of the social post. 38.0

`reviewScale` Double Review scale of the social post. 40.0

`reviewScore` Double Review score of the social post. 40.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

##### status ConnectApi.SocialPostStatus Status of the social post. 36.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

##### ConnectApi.SocialPostIntents

Intents available for a social post.

**Property Name** **Type** **Description** **Available Version**

##### approvalIntent ConnectApi. Approval intent for the social post. 45.0

```
             ApprovalIntent

##### deleteIntent ConnectApi. Delete intents for the social post. 45.0

             DeleteIntents

##### followIntent ConnectApi. Follow intents for the social persona. 45.0

             FollowIntents

```

```
hideIntent

```

##### ConnectApi. Hide intent for the social post. 45.0

```
HideSocial

PostIntent

```

##### likeIntent ConnectApi. Like intents for the social post. 45.0

```
           LikeIntents

##### replyIntent ConnectApi. Reply intents for the social post. 45.0

           ReplyIntents

##### ConnectApi.SocialPostMassApprovalOutput

```

Approval or rejection of a large number of social posts.

**Property Name** **Type** **Description** **Available Version**

`isApproved` Boolean Specifies whether the social posts were approved 46.0
( `true` ) or rejected ( `false` ) for publishing.

##### ConnectApi.SocialPostStatus

The status of a social post.

**Property Name** **Type** **Description** **Available Version**

`message` String Status message. 36.0


### Apex Reference Guide ConnectApi Enums

**Property Name** **Type** **Description** **Available Version**

##### type ConnectApi. Status type. Values are: 36.0

```
             SocialPostStatusType
```

**•** `ApprovalPending`

**•** `ApprovalRecalled`

**•** `ApprovalRejected`

**•** `Deleted`

**•** `Failed`

**•** `Hidden`

**•** `Pending`

**•** `Sent`

**•** `Unknown`

SEE ALSO:

ConnectApi.SocialPostCapability

##### ConnectApi.TrackedChangeAttachment

Tracked change attachment to a feed item.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.TrackedChangesCapability is
used.

**Name** **Type** **Description** **Available**
**Version**

`changes` `List<ConnectApi.` A list of tracked changes. 28.0–31.0

```
            TrackedChangeItem>

##### ConnectApi Enums Enums specific to the ConnectApi namespace. ConnectApi enums inherit all properties and methods of Apex enums.

```

Enums are not versioned. Enum values are returned in all API versions. Clients must handle values they don't understand gracefully.

**Enum** **Description**

`ConnectApi.ActionLink` Number of times an action link can be executed.

```
   ExecutionsAllowed
```

**•** `Once` —An action link can be executed only one time across all users.

**•** `OncePerUser` —An action link can be executed only one time for each user.

**•** `Unlimited` —An action link can be executed an unlimited number of times by each user.
If the action link’s `actionType` is `Api` or `ApiAsync`, you can’t use this value.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of action link.

```
   ActionLinkType
```

**•** `Api` —The action link calls a synchronous API at the action URL. Salesforce sets the status
to `SuccessfulStatus` or `FailedStatus` based on the HTTP status code returned
by your server.

**•** `ApiAsync` —The action link calls an asynchronous API at the action URL. The action remains
in a `PendingStatus` state until a third party makes a request to
`/connect/action-links/` _**`actionLinkId`**_ to set the status to
`SuccessfulStatus` or `FailedStatus` when the asynchronous operation is
complete.

**•** `Download` —The action link downloads a file from the action URL.

**•** `Ui` —The action link takes the user to a web page at the action URL.

`ConnectApi.ActivationPlatformCreationType` Creation type of the external platform.

**•** `Json`

**•** `Manual`

`ConnectApi.` Customer file source of the activation platform.

```
   ActivationPlatformCustomerFileSource
```
**•** `First_And_Third_Party`

**•** `First_Party`

**•** `Third_Party`

`ConnectApi.ActivationPlatformPrivacyType` Privacy type of the external platform.

**•** `NotApplicable`

**•** `ServiceProvider`

**•** `ThirdParty`

**•** `UpdateFailed`

`ConnectApi.ActivationPlatformStatus` Status of the external platform.

**•** `Active`

**•** `Error`

**•** `Inactive`

**•** `Processing`

`ConnectApi.ActivationPlatformType` Platform type of the external platform.

**•** `Advertising`

**•** `Analytics`

**•** `Marketing`

**•** `Publishing`

**•** `Technology`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.ActivationStatus` Status of the activation.

**•** `Active`

**•** `Processing`

**•** `Error`

**•** `Inactive`

`ConnectApi.ActivationTargetStatusEnum` Status of the activation target.

**•** `Active`

**•** `Processing`

**•** `Error`

**•** `Inactive`

`ConnectApi.` Type of sharing operation.

```
   ActivitySharingType
```

**•** `Everyone` —The activity is shared with everyone.

**•** `MyGroups` —The activity is shared only with a selection of the context user’s groups.

**•** `OnlyMe` —The activity is private.

`ConnectApi.ActivityType` Type of activity.

**•** `All`

**•** `Event`

**•** `Task`

`ConnectApi.AccountHolderType` Bank account holder type.

**•** `Business`

**•** `Individual`

`ConnectApi.AccountType` Bank account type.

**•** `Business`

**•** `Savings`

`ConnectApi.` Scope of the price adjustment amount.

```
   AdjustmentAmountScope
```

**•** `Total` —The adjustment scope is the total price.

**•** `Unit` —The adjustment scope is the unit price.

**•** `UnproratedTotal` —The adjustment scope is the unprorated total price.

`ConnectApi.` How the price adjustment amount is calculated.

```
   AdjustmentType
```

**•** `AdjustmentAmount` —The adjustment is a fixed amount.

**•** `AdjustmentPercentage` —The adjustment is a percentage.

`ConnectApi.Application` Application that initiated the payment request.

**•** `RLM`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of operation to perform on articles and topics.

```
   ArticleTopicJobType
```

**•** `AssignTopicsToArticle` —Assign topics to articles in a data category.

**•** `UnassignTopicsFromArticle` —Unassign topics from articles in a data category.

`ConnectApi.AsyncOperationStatus` Asynchronous processing status of the cart, if asynchronous processing is enabled for the store.

**•** `Completed`

**•** `Errored`

**•** `Processing`

`ConnectApi.` Operator used in the personalization audience criterion.

```
   AudienceCriteriaOperator
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

`ConnectApi.` Type of personalization audience criterion.

```
   AudienceCriteriaType
```

**•** `Audience` —Criterion based on audience.

**•** `Default` —Audience has no criteria.

**•** `Domain` —Criterion based on domain.

**•** `FieldBased` —Criterion based on object fields.

**•** `GeoLocation` —Criterion based on location.

**•** `Permission` —Criterion based on standard or custom permissions.

**•** `Profile` —Criterion based on profile.

`ConnectApi.AudienceDMODeltaType` Delta type of the activation.

**•** `A` —ADDED

**•** `D` —DELETED

**•** `E` —EXISTING

**•** `U` —UPDATED

`ConnectApi.BankType` Bank type.

**•** `ACH` —Automated Clearing House transaction

**•** `BACS` —Bankers' Automated Clearing Services transaction

**•** `BECS` —Bulk Electronic Clearing System transaction


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `SepaDebit` —Single Euro Payments Area transaction

`ConnectApi.BannerStyle` Decorates a feed item with a color and set of icons.

**•** `Announcement` —An announcement displays in a designated location in the Salesforce
UI until 11:59 p.m. on its expiration date, unless it’s deleted or replaced by another
announcement.

`ConnectApi.BillingFrequency` Billing frequency for a subscription.

**•** `Annual`

**•** `Monthly`

`ConnectApi.BotVersion` Activation status of the bot version.

```
   ActivationStatus
```

**•** `Active`

**•** `Inactive`

`ConnectApi.BundleType` Type of bundle.

**•** `GenericBundle` —A bundle that contains no additional information and is just a
collection of feed elements.

**•** `TrackedChanges` —A bundle that represents a collection of feed-tracked changes. The
bundle includes summary information about the feed-tracked changes that make up the
bundle.

`ConnectApi.` Definition type of the calculated insight.

```
CalculatedInsight
```

**•** `CALCULATED_METRIC`
```
DefinitionTypeEnum
```

**•** `CALCULATED_METRIC`

**•** `CALCULATED_METRIC`

`ConnectApi.` Type of tax calculation.

```
CalculateTaxType
```

**•** `Actual` —Calculated tax represents the final taxed amount for the transaction.

**•** `Estimated` —Calculated tax represents only an estimated value before the transaction
is finalized.

`ConnectApi.CalloutStatus` Indicates whether a named credential is enabled for callout.

**•** `Disabled`

**•** `Enabled`

`ConnectApi.CardCategory` Indicates a credit card or debit card.

**•** `CreditCard`

**•** `DebitCard`

`ConnectApi.CardType` Credit card issuer.

**•** `AmericanExpress`

**•** `DinersClub`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `JCB`

**•** `Maestro`

**•** `MasterCard`

**•** `Visa`

`ConnectApi.` Sort order for items in a cart.

```
   CartItemSortOrder
```

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `NameAsc` —Sorts by name in ascending alphabetical order (A–Z).

**•** `NameDesc` —Sorts by name in descending alphabetical order (Z–A).

**•** `SalesPriceAsc` —Sorts from lowest to highest negotiated price.

**•** `SalesPriceDesc` —Sorts from highest to lowest negotiated price.

`ConnectApi.` Subtype of item in a cart.

```
   CartItemSubType
```

**•** `Bonus` —A bonus product.

**•** `Gift` —A gift product.

`ConnectApi.CartItemType` Type of item in a cart.

**•** `DeliveryCharge`

**•** `Product`

`ConnectApi.` Severity of cart message.

```
   CartMessageSeverity
```

**•** `Error`

**•** `Info`

**•** `Warning`

`ConnectApi.` Level of the promotion target.

```
   CartPromotionType
```

**•** `Cart` —The target is cart-level.

**•** `Item` —The target is item-level.

`ConnectApi.CartStatus` Status of the cart.

**•** `Active—` Cart is created and available for modifications, like adding or removing products
or promotions.

**•** `Checkout—` Cart is in checkout. If the customer modifies the cart, the current checkout
session is canceled.

**•** `Closed—` Checkout is complete and an order was created. The cart cannot be modified.

**•** `PendingClosed—` Cart is marked to be closed, but the request isn't completed yet. The
cart can’t be modified. This value is available in API version 57.0 and later.

**•** `PendingDelete—` Cart is marked for delete, but the request isn't completed yet. The cart
can’t be modified.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Processing—` Cart is processing. For example, taxes are being calculated. The cart can’t
be modified.

`ConnectApi.CartTaxType` Tax type of the cart.

**•** `Automatic` —Automatic taxation policy.

**•** `Gross` —Gross taxation policy.

**•** `Net` —Net taxation policy.

`ConnectApi.CartType` Type of cart.

**•** `Cart` —Cart created by a customer.

**•** `PayNowReadOnly` —Clone of a Template cart that the customer can check out with
using the Pay Now feature.

**•** `Template` —Cart created by an internal user.

`ConnectApi.` Type of user who made the comment.

```
   CaseActorType
```

**•** `Customer` —if a Chatter customer made the comment

**•** `CustomerService` —if a service representative made the comment

`ConnectApi.CaseComment` Event type of a comment in Case Feed.

```
   EventType
```

**•** `NewInternal` —A case comment that has newly been marked Internal Only.

**•** `NewPublished` —A newly published case comment.

**•** `NewPublishedByCustomer` —A case comment by a customer that was newly
published.

**•** `PublishExisting` —An existing case comment that was republished.

**•** `PublishExistingByCustomer` —An existing case comment by a customer that
was republished.

**•** `UnpublishExistingByCustomer` —An existing case comment by a customer that
was unpublished.

**•** `UnpublishExsiting` —An existing case comment that was unpublished.

Note: Unfortunately, this typo is in the code, not the documentation. Use this spelling
in your code.

`ConnectApi.` Source object for an identity resolution ruleset.

```
CdpIdentityResolution
```

**•** `Account`
```
ConfigurationType

```

**•** `Account`

**•** `Individual`

`ConnectApi.` Match method for a match rule criterion.

```
CdpIdentityResolution
```

**•** `Exact` —Exact match.
```
MatchMethodType

```

**•** `Exact` —Exact match.

**•** `ExactNormalized` —Exact normalized match.

**•** `Fuzzy` —Fuzzy match with medium precision.

**•** `FuzzyHigh` —Fuzzy match with high precision.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `FuzzyLow` —Fuzzy match with low precision.

`ConnectApi.` Default reconciliation rule applied to fields in the object the reconciliation rule applies to.

```
CdpIdentityResolution
```

**•** `LastUpdated`
```
ReconciliationRuleType

```

**•** `LastUpdated`

**•** `MostFrequent`

**•** `SourceSequence`

`ConnectApi.` Result of an identity resolution ruleset job run.
`CdpIdentityResolution` **•**
```
RunNowResultCode

```

**•** `ExceededMaximumNumberOfSuccessfulRunsAllowedIn24Hours`

**•** `IdentityResolutionJobIsAlreadyRunning`

**•** `NoPendingChangesJobRunSkipped`

**•** `SuccessfullySubmittedIdentityResolutionJobRunRequest`

`ConnectApi.` Type of the model prediction.

```
CdpMlModelPredictionTypeEnum
```
**•** `BinaryClassification` -Binary classification.

**•** `Generic` -Generic/unknown.

**•** `MulticlassClassification` -Multiclass classification.

**•** `Regression` -Regression.

`ConnectApi.` Status of the prediction aggregate function.

```
CdpMlPredictAggregateFunctionStatusEnum
```
**•** `Error`

**•** `Success`

`ConnectApi.` Type of the prediction aggregate function.

```
CdpMlPredictAggregateFunctionTypeEnum
```
**•** `Average`

**•** `Median`

**•** `Sum`

`ConnectApi.` Status of the prediction.

```
CdpMlPredictStatusEnum
```

**•** `Error`

**•** `Success`

`ConnectApi.` Type of input data for the prediction.

```
CdpMlPredictTypeEnum
```

**•** `RawData` -Raw data.

**•** `RecordOverrides` -Record IDs with user-provided overrides.

**•** `Records` -Record IDs.

`ConnectApi.CommentType` Type of comment.

**•** `ContentComment` —Comment holds a content capability.

**•** `TextComment` —Comment contains only text.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Sort order for Commerce addresses.

```
   CommerceAddressSort
```

**•** `CreatedDateAsc` —Sort in ascending order of created date.

**•** `CreatedDateDesc` —Sort in descending order of created date.

**•** `NameAsc` —Sort in ascending order of name.

**•** `NameDesc` —Sort in descending order of name.

`ConnectApi.` Search attribute type.

```
CommerceSearch
```

**•** `Custom`
```
AttributeType

```

**•** `Custom`

**•** `PricebookEntry`

**•** `ProductAttribute`

**•** `ProductCategory`

**•** `Product2`

**•** `Standard`

`ConnectApi.` Display type of the facet.

```
CommerceSearchFacet
```

**•** `CategoryTree`
```
DisplayType

```

**•** `CategoryTree`

**•** `DatePicker`

**•** `MultiSelect`

**•** `SingleSelect`

`ConnectApi.` Search facet type.

```
CommerceSearchFacetType
```
**•** `DistinctValue`

**•** `Range`

`ConnectApi.` Grouping option for search results.

```
CommerceSearch
```

**•** `BestMatch` —Search results are grouped by the best-match product of the variation

`GroupingOption` group.

**•** `NoGrouping` —Search results aren’t grouped.

**•** `VariationParent` —Search results are grouped by the variation parent.

`ConnectApi.` Build type of the index.

```
CommerceSearch
```

**•** `Full`
```
IndexBuildType

```

**•** `Full`

**•** `Incremental`

`ConnectApi.` Creation type of the index.

```
CommerceSearch
```

**•** `Manual`
```
IndexCreationType

```

**•** `Manual`

**•** `Scheduled`

`ConnectApi.` Status of the index.

```
CommerceSearch
```

**•** `Completed`
```
IndexStatus

```

**•** `Completed`

**•** `Failed`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `InProgress`

`ConnectApi.` Usage of the index.

```
CommerceSearch
```

**•** `Live`
```
IndexUsage

```

**•** `Live`

**•** `OutOfUse`

`ConnectApi.` Direction of the sort rule.

```
CommerceSearch
```

**•** `Ascending`
```
SortRuleDirection

```

**•** `Ascending` —Sorts in ascending alphanumeric order (A–Z, 0–9).

**•** `Default` —When no direction is defined, sorts by relevance.

**•** `Descending` —Sorts in descending alphanumeric order (Z–A, 9–0).

`ConnectApi.` Label suffix of the sort rule.

```
CommerceSearchSortRule
```

**•** `Ascen`
```
LabelSuffix

```

**•** `Ascen` —Label suffix for 'Asc'

**•** `Ascending` —Label suffix for 'Ascending'

**•** `Az` —Label suffix for 'A-Z'

**•** `Descen` —Label suffix for 'Desc'

**•** `Descending` —Label suffix for 'Descending'

**•** `FewMany` —Label suffix for 'Few-Many'

**•** `HeavyLight` —Label suffix for 'Heavy-Light'

**•** `HighLow` —Label suffix for 'High-Low'

**•** `HighestLowest` —Label suffix for 'Highest-Lowest'

**•** `LightHeavy` —Label suffix for 'Light-Heavy'

**•** `LowHigh` —Label suffix for 'Low-High'

**•** `LowestHighest` —Label suffix for 'Lowest-Highest'

**•** `ManyFew` —Label suffix for 'Many-Few'

**•** `NewOld` —Label suffix for 'New-Old'

**•** `Newest` —Label suffix for 'Newest'

**•** `NewestOldest` —Label suffix for 'Newest-Oldest'

**•** `NineZero` —Label suffix for '9-0'

**•** `OldNew` —Label suffix for 'Old-New'

**•** `Oldest` —Label suffix for 'Oldest'

**•** `OldestNewest` —Label suffix for 'Oldest-Newest'

**•** `PriceDecreasing` —Label suffix for '$$-$'

**•** `PriceIncreasing` —Label suffix for '$-$$'

**•** `ThickThin` —Label suffix for 'Thick-Thin'

**•** `ThinThick` —Label suffix for 'Thin-Thick'

**•** `Za` —Label suffix for 'Z-A'

**•** `ZeroNine` —Label suffix for '0-9'


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of sort rule.
`CommerceSearch` **•**
```
SortRuleType

```

**•** `ProductAttributeBased` —Sorts by product attribute fields.

**•** `ProductBased` —Sorts by product field data.

**•** `Relevancy` —Sorts by product and catalog term frequency.

**•** `SortByPricebook` —Sorts by product prices defined in the specified pricebook (version
55.0 and later).

`ConnectApi.` Type of the top product to return for each product group in search results.

```
CommerceSearchTop
```

**•** `VariationParent`
```
ProductType

```

`ConnectApi.CommunityFlag` Reason a post, comment, or file is flagged.

```
ReasonType
```

**•** `FlaggedByRule` —Moderation rule flagged the item.

**•** `FlaggedBySystem` —Einstein flagged the item.

**•** `FlaggedByUserAsInappropriate` —User flagged the item as inappropriate.

**•** `FlaggedByUserAsSpam` —User flagged the item as spam.

`ConnectApi.` Type of moderation flag.

```
CommunityFlagType
```

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

`ConnectApi.` Visibility behavior of a flag for various user types.

```
CommunityFlagVisibility
```
**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the
flagged element or item.

**•** `SelfAndModerators` —The flag is visible to the creator of the flag and to users with
moderation permissions on the flagged element or item.

`ConnectApi.` Status of the Experience Cloud site.

```
CommunityStatus
```

**•** `Live`

**•** `Inactive`

**•** `UnderConstruction`

`ConnectApi.CompressionFormatEnum` Compression format for the output file.

**•** `Bzip2`

**•** `Gzip`

**•** `None` -No compression

`ConnectApi.ConnectInsightUnitEnum` Unit for an insight.

**•** `Count`

**•** `Currency`

**•** `Dollar`

**•** `Number`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Percent`

`ConnectApi.ContactPointType` Type of contact point.

**•** `Email`

**•** `Maid`

**•** `Ott`

**•** `Phone`

**•** `Push`

**•** `Subscriber_Key_Email`

**•** `Subscriber_Key_Phone`

**•** `WhatsApp`

`ConnectApi.ContactPointPref` Type of contact point.

**•** `ContactPointPrefAny`

**•** `ContactPointPrefBusiness`

**•** `ContactPointPrefPersonal`

**•** `ContactPointPrefPrimary`

`ConnectApi.ContentHub` Authentication protocol used for the repository.

```
   AuthenticationProtocol
```

**•** `NoAuthentication` —Repository doesn’t require authentication.

**•** `Oauth` —Repository uses OAuth authentication protocol.

**•** `Password` —Repository uses user name and password authentication protocol.

`ConnectApi.ContentHub` Type of directory entry.

```
   DirectoryEntryType
```

**•** `GroupEntry`

**•** `UserEntry`

`ConnectApi.ContentHub` Sharing status for the external file.

```
   ExternalItemSharingType
```
**•** `DomainSharing` —File is shared with the domain.

**•** `PrivateSharing` —File is private or shared only with individuals.

**•** `PublicSharing` —File is publicly shared.

`ConnectApi.ContentHub` Type of group.

```
   GroupType
```

**•** `Everybody` —Group is public to everybody.

**•** `EverybodyInDomain` —Group is public to everybody in the same domain.

**•** `Unknown` —Group type is unknown.

`ConnectApi.ContentHub` Item types.

```
   ItemType
```

**•** `Any` —Includes files and folders.

**•** `FilesOnly` —Includes files only.

**•** `FoldersOnly` —Includes folders only.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.ContentHub` Support for content streaming.

```
   StreamSupport
```

**•** `ContentStreamAllowed`

**•** `ContentStreamNotAllowed`

**•** `ContentStreamRequired`

`ConnectApi.ContentHub` Data type of the value of the field.

```
   VariableType
```

**•** `BooleanType`

**•** `DateTimeType`

**•** `DecimalType`

**•** `HtmlType`

**•** `IdType`

**•** `IntegerType`

**•** `StringType`

**•** `UriType`

**•** `XmlType`

`ConnectApi.Conversation` Conversation application integration types.

```
Application
```

**•** `Api`
```
IntegrationType

```

**•** `Api`

**•** `Slack`

`ConnectApi.` Action to take when creating the credential.

```
CreateCredentialAction
```

**•** `Refresh`

`ConnectApi.` Authentication protocol of the external credential.

```
CredentialAuthentication
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

`ConnectApi.` Authentication protocol variant of the external credential.

```
CredentialAuthentication
```

**•** `AwsSv4_STS`
```
ProtocolVariant

```

**•** `AwsSv4_STS` —AWS Signature Version 4 with Security Token Service.

**•** `ClientCredentialsClientSecret` —OAuth 2.0 Client Credentials client secret.
Client secrets are sent in the callout’s request body.

**•** `ClientCredentialsClientSecretBasic` —OAuth 2.0 Client Credentials client
secret. Client secrets are sent in the callout’s authorization header, as with Basic authentication.

**•** `ClientCredentialsJwtAssertion` —OAuth 2.0 Client Credentials JSON Web
Token assertion.

**•** `JwtBearer` —OAuth 2.0 JSON Web Token bearer flow.

**•** `NoAuthentication` —No authentication.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `RolesAnywhere` —AWS Signature Version 4 with Identity and Access Management
(IAM) Roles Anywhere.

`ConnectApi.` Status of the credential authentication.

```
CredentialAuthentication
```

**•** `Configured`
```
Status

```

**•** `Configured` —Credential has all required credentials for at least one principal.

**•** `NotConfigured` —Credential isn’t configured.

**•** `Unknown` —Credential status can’t be determined because the authentication protocol is
custom.

`ConnectApi.` Type of credential principal.

```
CredentialPrincipalType
```
**•** `AwsStsPrincipal`

**•** `NamedPrincipal`

**•** `PerUserPrincipal`

`ConnectApi.` Display metadata type of the currency info.

```
CurrencyInfoDisplayTypeEnum
```
**•** `IsoCode` —ISO code of the currency.

`ConnectApi.DaoObjectFieldTypeQueryEnum` Type of the calculated insight field.

**•** `Dimension`

**•** `Measure`

**•** `ObjectTypeUnspecified`

`ConnectApi.` Data category operator.

```
DataCategoryOperator
```

**•** `Above` —Queries the data category and all of its parent categories.

**•** `AboveOrBelow` —Queries the data category, all of its parent categories, and all of its
subcategories.

**•** `At` —Queries the data category.

**•** `Below` —Queries the data category and all of its subcategories.

`ConnectApi.DataConnectorTypeEnum` Data connector type of the activation target.

**•** `AmazonS3`

**•** `AzureBlob`

**•** `DataCloud`

**•** `GoogleCloudStorage`

**•** `SalesforceMarketingCloud`

**•** `Sftp`

`ConnectApi.DataExportAttributeSource` Activation attribute source.

**•** `Direct`

**•** `Related`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.DataExportAttributeType` Type of activation attribute.

**•** `Computed_Dimension`

**•** `Computed_Measure`

**•** `Model`

**•** `Model_Related`

**•** `Non_Aggregatable_Computed_Measure`

`ConnectApi.DataExportRefreshMode` Refresh type of the activation.

**•** `Full_Refresh`

**•** `Incremental`

`ConnectApi.` Last publish status of the activation.

```
   DataExportRunStatus
```

**•** `Error`

**•** `Partner_Error`

**•** `Partner_Processing`

**•** `Publishing`

**•** `Queued`

**•** `Segment_Error`

**•** `Skipped`

**•** `Success`

`ConnectApi.DataGraphObjectType` Data type of an object for a data graph.

**•** `Adg`

**•** `AdgActivationAudience`

**•** `AdgExternal`

**•** `Bridge`

**•** `Calculated`

**•** `CalculatedRealTime`

**•** `CalculatedStreaming`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `MlPrediction`

**•** `ObjectTypeUnspecified`

**•** `Package`

**•** `SegmentMembership`

**•** `Standard`

**•** `System`

**•** `Transform`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.DataGraphStatus` Status of the data graph.

**•** `Error`

**•** `Inprogress`

**•** `Published`

**•** `Ready`

**•** `StatusUnspecified`

**•** `Unrecognized`

`ConnectApi.` Type of user.

```
   DatacloudUserType
```

**•** `Monthly` —A user type that’s assigned monthly point limits for purchasing Data.com
records. Only the assigned user can use monthly points. Points expire at the end of the
month. Monthly is the default setting for `DatacloudUserType` .

**•** `Listpool` —A user type that allows users to draw from a pool of points to purchase
Data.com records.

`ConnectApi.` Status of the import.

```
DatacloudImport
```

**•** `Success`
```
StatusTypeEnum

```

**•** `Success` —Indicates that selected records were added to the org’s CRM.

**•** `Duplicate` —Marks a record that is already in the org’s CRM. The API determines whether
an org allows the addition of duplicate records in its CRM.

**•** `Error` —Indicates that the selected records weren’t added to the org’s CRM.

`ConnectApi.DataSpaceStatusEnum` Status of the data space.

**•** `Active` —The data space is active.

**•** `Error` —The data space has an error.

**•** `Processing` —The data space is being processed.

`ConnectApi.DigestPeriod` Time period that’s included in a Chatter email digest.

**•** `DailyDigest` —The email includes up to the 50 latest posts from the previous day.

**•** `WeeklyDigest` —The email includes up to the 50 latest posts from the previous week.

`ConnectApi.EgressFileNameTypeEnum` Type of egress file name.

**•** `Custom`

**•** `Predetermined`

`ConnectApi.EmailMessage` Automation type of the email message.

```
AutomationType
```

**•** `aiAssisted` —The email message was created with the assistance of AI.

**•** `aiAutomated` —The email message was created automatically by AI.

`ConnectApi.EmailMessage` Direction of an email message on a case.

```
Direction
```

**•** `Inbound` —An inbound message (sent by a customer).

**•** `Outbound` —An outbound message (sent to a customer by a support agent).


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.EmailMessage` Size of a case’s email message HTML body.

```
   Size
```

**•** `Large`                  - `UseLargeHtmlBody` permission is set, HTML body exceeds 131K characters,
and HTML email display is enabled.

**•** `Normal` —Email message doesn’t meet the `Large` criteria.

`ConnectApi.EmailMessage` Status of an email message on a case.

```
   Status
```

**•** `DraftStatus`

**•** `ForwardedStatus`

**•** `NewStatus`

**•** `ReadStatus`

**•** `RepliedStatus`

**•** `SentStatus`

`ConnectApi.` Information type of the extension.

```
   ExtensionInformationType
```
**•** `Lightning`

`ConnectApi.` Parameter type for an external auth identity provider.

```
ExternalAuthIdentity
```

**•** `AuthorizeRequestQueryParameter`
```
ProviderParamType

```

**•** `AuthorizeRequestQueryParameter`

**•** `IdentityProviderOptions`

**•** `ManagedByComponent`

**•** `ManagedByFeature`

**•** `RefreshRequestBodyParameter`

**•** `RefreshRequestHttpHeader`

**•** `RefreshRequestQueryParameter`

**•** `TokenRequestBodyParameter`

**•** `TokenRequestHttpHeader`

**•** `TokenRequestQueryParameter`

`ConnectApi.` Parameter type of the external credential.

```
ExternalCredential
```

**•** `AdditionalRefreshStatusCode`
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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Access type of the external credential principal.

```
ExternalCredential
```

**•** `PermissionSet`
```
PrincipalAccessType

```

**•** `PermissionSet`

**•** `PermissionSetGroup`

**•** `Profile`

`ConnectApi.` Order of comments.

```
FeedCommentSortOrder
```

**•** `CreatedDateLatestAsc` —Sorts by most recently created comments in ascending
order.

**•** `CreatedDateOldestAsc` —Sorts by oldest comments in ascending order.

**•** `Relevance` —Sorts by most relevant content.

`ConnectApi.FeedDensity` Density of the feed.

**•** `AllUpdates` —Displays all updates from people and records the user follows and groups
the user is a member of. Also displays custom recommendations.

**•** `FewerUpdates` —Displays all updates from people and records the user follows and
groups the user is a member of. Also displays custom recommendations, but hides some
system-generated updates from records.

```
ConnectApi.

FeedElementCapability

Type

```

Capabilities of a feed element in API versions 31.0 and later. If a capability exists on a feed element,
the capability is available, even if the value doesn’t exist or is `null` . If the capability doesn’t
exist, it isn’t available.

**•** `AssociatedActions` —The feed element includes information about actions associated
with it.

**•** `Approval` —The feed element includes information about an approval.

**•** `Banner` —The body of the feed element has an icon and border.

**•** `Bookmarks` —The context user can bookmark the feed element. Bookmarked feed elements
are visible in the bookmarks feed.

**•** `Bundle` —The feed element has a group of other feed elements that display as a bundle
in the feed. The bundle type determines the additional data associated with the bundle.

**•** `CallCollaboration` —The feed element has a recording comment.

**•** `Canvas` —The feed element renders a canvas app.

**•** `CaseComment` —The feed element has a case comment in the case feed.

**•** `ChatterLikes` —The context user can like the feed element.

**•** `Close` —The feed element can’t be edited, commented on, or deleted. If the feed element
is a poll, it can’t be voted on.

**•** `Comments` —The context user can add comments to the feed element.

**•** `Content` —The feed element has a file.

**•** `DashboardComponentSnapshot` —The feed element has a dashboard component
snapshot.

**•** `DirectMessage` —The feed element is a direct message.

**•** `Edit` —Users who have permission can edit the feed element.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `EmailMessage` —The feed element has an email message from a case.

**•** `EnhancedLink` —The feed element has a link that can contain supplemental information
like an icon, a title, and a description.

**•** `Extensions` —The feed element has one or more extension attachments.

**•** `FeedEntityShare` —The feed element has a feed entity shared with it.

**•** `Files` —The feed element has one or more file attachments.

**•** `Interactions` —The feed element has information about user interactions.

**•** `Link` —The feed element has a URL.

**•** `MediaReferences` —The feed element has one or more media references.

**•** `Moderation` —Users in an Experience Cloud site can flag the feed element for moderation.

**•** `Mute` —The context user can mute the feed element.

**•** `Origin` —A feed action created the feed element.

**•** `Pin` —Users who have permission can pin the feed element.

**•** `Poll` —The feed element has poll voting.

**•** `QuestionAndAnswers` —The feed element has a question, and users can add answers
to the feed element instead of comments. Users can also select the best answer.

**•** `ReadBy` —The context user can mark the feed element as read.

**•** `Recommendations` —The feed element has a recommendation.

**•** `Record` —The comment has a record attachment.

**•** `RecordSnapshot` —The feed element has all the snapshot fields of a record for a single
create record event.

**•** `SocialPost` —The feed element can interact with a social post on a social network.

**•** `Status` —The feed element has a status that determines its visibility.

**•** `Topics` —The context user can add topics to the feed element.

**•** `TrackedChanges` —The feed element has all changes to a record for a single tracked
change event.

**•** `UpDownVote` —Users can upvote or downvote the feed element.

**•** `Verified` —Users who have permission can mark a comment as verified or unverified.

`ConnectApi.FeedElement` Feed elements are the top-level objects that a feed contains. The feed element type describes
`Type` the characteristics of that feed element.

**•** `Bundle` —A container of feed elements. A bundle also has a body made up of message
segments that can always be gracefully degraded to text-only values.

**•** `FeedItem` —A feed item has a single parent and is scoped to oneExperience Cloud site
or across all Experience Cloud sites. A feed item can have capabilities such as bookmarks,
canvas, content, comment, link, poll. Feed items have a body made up of message segments
that can always be gracefully degraded to text-only values.

**•** `Recommendation` —A recommendation is a feed element with a recommendations
capability. A recommendation suggests records to follow, groups to join, or applications
that are helpful to the context user.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.FeedEntity` Status of the feed post or comment.

```
   Status
```

**•** `Draft` —The feed post isn’t published but is visible to the author and users with Modify
All Data or View All Data permission. Comments can’t be drafts.

**•** `Isolated` —The feed post or comment is isolated, and only admins can see it.

**•** `PendingReview` —The feed post or comment isn’t approved yet and therefore isn’t
published or visible.

**•** `Published` —The feed post or comment is approved and visible.

`ConnectApi.FeedFavorite` Origin of the feed favorite.

```
   Type
```

**•** `ListView`

**•** `Search`

**•** `Topic`

`ConnectApi.FeedFilter` Filter value for a feed.

**•** `AllQuestions` —Feed elements that are questions.

**•** `AuthoredBy` —Feed elements authored by the user profile owner. This value is valid only
for the `UserProfile` feed.

**•** `CommunityScoped` —Feed elements that are scoped to Experience Cloud sites. Currently,
these feed elements have a User or a Group parent record. However, other parent record
types could be scoped to sites in the future. Feed elements that are always visible in all sites
are filtered out. This value is valid only for the `UserProfile` feed.

**•** `QuestionsWithCandidateAnswers` —Feed elements that are questions that have
candidate answers associated with them. This value is valid only for users with the Access
Einstein-Generated Answers permission.

**•** `QuestionsWithCandidateAnswersReviewedPublished` —Feed elements
that are questions that have candidate answers that have been reviewed or published. This
value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `Read` —Feed elements that are older than 30 days or are marked as read for the context
user. Includes existing feed elements when the context user joined the group. This value is
valid only for the `Record` feed of a group.

**•** `SolvedQuestions` —Feed elements that are questions and that have a best answer.

**•** `UnansweredQuestions` —Feed elements that are questions and that don’t have any
answers.

**•** `UnansweredQuestionsWithCandidateAnswers` —Feed elements that are
questions that don’t have answers but have candidate answers associated with them. This
value is valid only for users with the Access Einstein-Generated Answers permission.

**•** `Unread` —Feed elements that are created in the past 30 days and aren’t marked as read
for the context user. This value is valid only for the `Record` feed of a group.

**•** `UnsolvedQuestions` —Feed elements that are questions and that don’t have a best
answer.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.FeedItem` Attachment type for feed item output objects.

```
   AttachmentType
```

**•** `Approval` —A feed item requiring approval.

**•** `BasicTemplate` —A feed item with a generic rendering of an image, link, and title.

**•** `Canvas` —A feed item that contains the metadata to render a link to a canvas app.

**•** `CaseComment` —A feed item created from a comment to a case record.

**•** `CaseComment` —A feed item created from a comment to a case record.

**•** `Content` —A feed item with a file attached.

**•** `DashboardComponent` —A feed item with a dashboard attached.

**•** `EmailMessage` —An email attached to a case record in Case Feed.

**•** `Link` —A feed item with a URL attached.

**•** `Poll` —A feed item with a poll attached.

**•** `Question` —A feed item with a question attached.

**•** `RecordSnapshot` —The feed item attachment contains a view of a record at a single
`ConnectApi.FeedItemType.CreateRecordEvent` .

**•** `TrackedChange` —All changes to a record for a single
`ConnectApi.FeedItemType.TrackedChange` event.

`ConnectApi.FeedItemType` Type of feed item.

**•** `ActivityEvent` —Feed item generated in Case Feed when an event or task associated
with a parent record with a feed enabled is created or updated.

**•** `AdvancedTextPost` —A feed item with advanced text formatting, such as a group
announcement post.

**•** `ApprovalPost` —Feed item with an approval capability. Approvers can act on the feed
item parent.

**•** `AttachArticleEvent` —Feed item generated when an article is attached to a case in
Case Feed.

**•** `BasicTemplateFeedItem` —Feed item with an enhanced link capability.

**•** `CallLogPost` —Feed item generated when a call log is saved to a case in Case Feed.

**•** `CanvasPost` —Feed item generated by a canvas app in the publisher or from Connect
REST API or Connect in Apex. The post itself is a link to a canvas app.

**•** `CaseCommentPost` —Feed item generated when a case comment is saved in Case Feed.

**•** `ChangeStatusPost` —Feed item generated when the status of a case is changed in
Case Feed.

**•** `ChatTranscriptionPost` —Feed item generated in Case Feed when a Live Agent
chat transcript is saved to a case.

**•** `CollaborationGroupCreated` —Feed item generated when a new public group
is created. Contains a link to the new group.

**•** `CollaborationGroupUnarchived` —Deprecated. Feed item generated when an
archived group is activated.

**•** `ContentPost` —Feed item with a content capability.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `CreateRecordEvent` —Feed item that describes a record created in the publisher.

**•** `DashboardComponentAlert` —Feed item with a dashboard alert.

**•** `DashboardComponentSnapshot` —Feed item with a dashboard component snapshot
capability.

**•** `EmailMessageEvent` —Feed item generated when an email is sent from a case in Case
Feed.

**•** `FacebookPost` —Deprecated. Feed item generated when a Facebook post is created
from a case in Case Feed.

**•** `LinkPost` —Feed item with a link capability.

**•** `MilestoneEvent` —Feed item generated when a case milestone is either completed
or reaches a violation status. Contains a link to the case milestone.

**•** `PollPost` —Feed item with a poll capability. Viewers of the feed item are allowed to vote
on the options in the poll.

**•** `ProfileSkillPost` —Feed item generated when a skill is added to a user’s profile.

**•** `QuestionPost` —Feed item generated when a question is asked.

As of API version 33.0, a feed item of this type can have a content capability and a link
capability.

**•** `ReplyPost` —Feed item generated by a Chatter Answers reply.

**•** `RypplePost` —Feed item generated when a user posts thanks.

**•** `SocialPost` —Feed item generated when a social post is created from a case in Case
Feed.

**•** `TextPost` —Feed item containing text only.

**•** `TrackedChange` —Feed item created when one or more fields on a record have been
changed.

**•** `UserStatus` —Deprecated. A user's post to their own profile.

`ConnectApi.FeedItem` Type of users who can see a feed item.

```
   VisibilityType
```

**•** `AllUsers` —Visibility is not limited to internal users.

**•** `InternalUsers` —Visibility is limited to internal users.

`ConnectApi.` Order of feed items in the feed.

```
   FeedSortOrder
```

**•** `CreatedDateAsc` —Sorts by oldest creation date. This sort order is available only for
`DirectMessageModeration`, `Draft`, `Isolated`, `Moderation`, and
`PendingReview` feeds.

**•** `CreatedDateDesc` —Sorts by most recent creation date.

**•** `LastModifiedDateDesc` —Sorts by most recent activity.

**•** `MostViewed` —Sorts by most viewed content. This sort order is available only for `Home`
feeds when the `ConnectApi.FeedFilter` is `UnansweredQuestions` .

**•** `Relevance` —Sorts by most relevant content. This sort order is available only for
`Company`, `Home`, and `Topics` feeds.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.FeedType` Type of feed.

**•** `Bookmarks` —Contains all feed items saved as bookmarks by the context user.

**•** `Company` —Contains all feed items except feed items of type `TrackedChange` . To see
the feed item, the user must have sharing access to its parent.

**•** `DirectMessageModeration` —Contains all direct messages that are flagged for
moderation. The Direct Message Moderation feed is available only to users with Moderate
Experiences Chatter Messages permissions.

**•** `DirectMessages` —Contains all feed items of the context user’s direct messages.

**•** `Draft` —Contains all the feed items that the context user drafted.

**•** `Files` —Contains all feed items that contain files posted by people or groups that the
context user follows.

**•** `Filter` —Contains the news feed filtered to contain feed items whose parent is a specified
object type.

**•** `Groups` —Contains all feed items from all groups the context user either owns or is a
member of.

**•** `Home` —Contains all feed items associated with any managed topic in an Experience Cloud
site.

**•** `Isolated` —Contains all the feed items and comments that are isolated.

**•** `Landing` —Contains all feed items that best drive user engagement when the feed is
requested. Allows clients to avoid an empty feed when there aren’t many personalized feed
items.

**•** `Moderation` —Contains all feed items that are flagged for moderation, except direct
messages. The moderation feed is available only to users with Moderate Experiences Feeds
permissions.

**•** `Mute` —Contains all feed items that the context user muted.

**•** `News` —Contains all updates for people the context user follows, groups the user is a member
of, and files and records the user is following. Contains all updates for records whose parent
is the context user.

**•** `PendingReview` —Contains all feed items and comments that are pending review.

**•** `People` —Contains all feed items posted by all people the context user follows.

**•** `Record` —Contains all feed items whose parent is a specified record, which could be a
group, user, object, file, or any other standard or custom object. When the record is a group,
the feed also contains feed items that mention the group. When the record is a user, the
feed contains only feed items on that user. You can get another user’s record feed.

**•** `Streams` —Contains all feed items for any combination of up to 25 feed-enabled entities
that the context user subscribes to in a stream. Examples of feed-enabled entities include
people, groups, and records,

**•** `To` —Contains all feed items with mentions of the context user. Contains feed items the
context user commented on and feed items created by the context user that are commented
on.

**•** `Topics` —Contains all feed items that include the specified topic.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `UserProfile` —Contains feed items created when a user changes records that can be
tracked in a feed. Contains feed items whose parent is the user and feed items that @mention
the user. This feed is different than the news feed, which returns more feed items, including
group updates. You can get another user’s user profile feed.

`ConnectApi.FieldChange` Value type of a field change.

```
   ValueType
```

**•** `NewValue` —A new value

**•** `OldValue` —An old value

`ConnectApi.FieldType` Field type.

**•** `Address`

**•** `AnyType`

**•** `Base64`

**•** `Boolean`

**•** `Combobox`

**•** `ComplexValue`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `Email`

**•** `EncryptedString`

**•** `ExtensionEntityLookup`

**•** `ExternalLookup`

**•** `FloatArray`

**•** `Id`

**•** `ImageUrl`

**•** `IndirectLookup`

**•** `Integer`

**•** `Json`

**•** `Location`

**•** `Long`

**•** `MultiPicklist`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Picklist`

**•** `PlainTextArea`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Reference`

**•** `RichTextArea`

**•** `Sobject`

**•** `String`

**•** `SwitchablePersonName`

**•** `TextArea`

**•** `Time`

**•** `Url`

`ConnectApi.FileDelimiterEnum` Field delimiter for the output file.

**•** `BrokenPipe`

**•** `Caret`

**•** `Colon`

**•** `Comma`

**•** `Hash`

**•** `Pipe`

**•** `Semicolon`

**•** `Slash`

**•** `Tab`

**•** `Tilde`

**•** `Underscore`

`ConnectApi.` Format of the file preview.

```
   FilePreviewFormat
```

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.

**•** `ThumbnailBig` —Preview format is 720 x 480 PNG.

**•** `ThumbnailTiny` —Preview format is 120 x 90 PNG.

**•** `Video` —Preview format is MP4.

`ConnectApi.` Availability status of the file preview.

```
   FilePreviewStatus
```

**•** `Available` —Preview is available.

**•** `InProgress` —Preview is being processed.

**•** `NotAvailable` —Preview is unavailable.

**•** `NotScheduled` —Generation of the preview isn’t scheduled yet.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Publish status of the file.

```
   FilePublishStatus
```

**•** `PendingAccess` —File is pending publishing.

**•** `PrivateAccess` —File is private.

**•** `PublicAccess` —File is public.

`ConnectApi.` Sharing option of the file.

```
   FileSharingOption
```

**•** `Allowed` —Resharing of the file is allowed.

**•** `Restricted` —Resharing of the file is restricted.

`ConnectApi.` Sharing privacy of a file.

```
   FileSharingPrivacy
```

**•** `None` —File is visible to anyone with record access.

**•** `PrivateOnRecords` —File is private on records.

`ConnectApi.` Sharing role of the file.

```
   FileSharingType
```

**•** `Admin` —Owner permission, but doesn’t own the file.

**•** `Collaborator` —Viewer permission, and can edit, change permissions, and upload a
new version of a file.

**•** `Owner` —Collaborator permission, and can make a file private, and delete a file.

**•** `Viewer` —Can view, download, and share a file.

**•** `WorkspaceManaged` —Permission controlled by the library.

`ConnectApi.FilterConjunction` Conjunction for the activation attribute filter expression.

**•** `FilterConjunctionAnd`

**•** `FilterConjunctionOr`

`ConnectApi.` Filter operator.

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

`ConnectApi.FilterOperatorDataType` Type of attribute.

**•** `FilterOperatorDataTypeBoolean`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `FilterOperatorDataTypeDate`

**•** `FilterOperatorDataTypeDateOnly`

**•** `FilterOperatorDataTypeExactlyRelativeDate`

**•** `FilterOperatorDataTypeNumber`

**•** `FilterOperatorDataTypeRelateToNowDate`

**•** `FilterOperatorDataTypeText`

`ConnectApi.FilterSortOrder` The sort order for filtering.

**•** `FilterSortOrderAsc`

**•** `FilterSortOrderDesc`

`ConnectApi.FolderItem` Type of item in a folder.

```
   Type
```

**•** `file`

**•** `folder`

`ConnectApi.FormFieldType` Type of marketing integration form field.

**•** `Boolean`

**•** `Date`

**•** `EmailAddress`

**•** `Number`

**•** `Text`

`ConnectApi.` Formula filter type for the personalization audience.

```
   FormulaFilterType
```

**•** `AllCriteriaMatch` —All audience criteria are true (AND operation).

**•** `AnyCriterionMatches` —Any audience criterion is true (OR operation).

**•** `CustomLogicMatches` —Audience criteria match the custom formula (for example,
(1 AND 2) OR 3).

`ConnectApi.` Definition category of the business objective, or goal.

```
   GoalDefinitionCategoryEnum
```
**•** `Webstore`

`ConnectApi.GroupArchive` Archive status of groups.

```
   Status
```

**•** `All` —All groups, including groups that are archived and groups that aren’t archived.

**•** `Archived` —Groups that are archived.

**•** `NotArchived` —Groups that aren’t archived.

`ConnectApi.GroupEmail` Frequency with which a user receives email.

```
   Frequency
```

**•** `EachPost`

**•** `DailyDigest`

**•** `WeeklyDigest`

**•** `Never`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `UseDefault`

`ConnectApi.` Type of membership the user has with the group.

```
   GroupMembershipType
```

**•** `GroupOwner`

**•** `GroupManager`

**•** `NotAMember`

**•** `NotAMemberPrivateRequested`

**•** `StandardMember`

`ConnectApi.` Status of a request to join a private group.

```
GroupMembership
```

**•** `Accepted`
```
RequestStatus
```

**•** `Declined`

**•** `Pending`

`ConnectApi.GroupViral` Status of an invitation to join a group.

```
InvitationsStatus
```

**•** `ActedUponUser` —The user was added to the group. An email was sent asking the user
to visit the group.

**•** `Invited` —An email was sent asking the user to sign up for the org.

**•** `MaxedOutUsers` —The group has the maximum allowed members.

**•** `MultipleError` —The user wasn’t invited due to multiple errors.

**•** `NoActionNeededUser` —The user is already a member of the group.

**•** `NotVisibleToExternalInviter` —The user is not accessible to the user sending
the invitation.

**•** `Unhandled` —The user couldn’t be added to the group for an unknown reason.

`ConnectApi.` Group visibility type.

```
GroupVisibilityType
```

**•** `PrivateAccess` —Only members of the group can see posts to this group.

**•** `PublicAccess` —All users within the Experience Cloud site can see posts to this group.

**•** `Unlisted` —Reserved for future use.

`ConnectApi.HttpRequest` HTTP method.

```
Method
```

**•** `HttpDelete` —Returns HTTP 204 on success. Response body or output class is empty.

**•** `HttpGet` —Returns HTTP 200 on success.

**•** `HttpHead` —Returns HTTP 200 on success. Response body or output class is empty.

**•** `HttpPatch` —Returns HTTP 200 on success or HTTP 204 if the response body or output
class is empty.

**•** `HttpPost` —Returns HTTP 201 on success or HTTP 204 if the response body or output
class is empty. Exceptions are the batch posting resources and methods, which return HTTP
200 on success.

**•** `HttpPut` —Return HTTP 200 on success or HTTP 204 if the response body or output class
is empty.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Authentication flow to get tokens to call protected APIs.

```
   IdentityProviderAuthFlow
```
**•** `AuthorizationCode`

`ConnectApi.` Authentication protocol required to access the external system.

```
   IdentityProviderAuthProtocol
```
**•** `OAuth`

`ConnectApi.` Client authentication method that describes how credentials are sent to the authorization server.

```
   IdentityProviderClientAuth
```
**•** `ClientSecretBasic`

**•** `ClientSecretPost`

`ConnectApi.` Source of the link metadata.

```
   LinkMetadataSource
```

**•** `None` —Link metadata wasn’t retrieved.

**•** `Sfdc` —Salesforce is the source.

`ConnectApi.` Type of link that the metadata represents.

```
   LinkMetadataType
```

**•** `Error` —Link metadata couldn’t be retrieved.

**•** `Link` —Represents a link.

**•** `None` —Link metadata wasn’t retrieved because the link isn’t an allowed domain.

**•** `Photo` —Represents a photo.

**•** `Rich` —Represents rich content, typically HTML content.

**•** `Unknown` —Link metadata was retrieved, but the type is unknown.

**•** `Video` —Represents a video.

`ConnectApi.` Type of maintenance.

```
   MaintenanceType
```

**•** `Downtime` —Downtime maintenance.

**•** `GenerallyAvailable` —Generally available mode.

**•** `MaintenanceAndAvailable` —Maintenance with available mode.

**•** `MaintenanceWithDowntime` —Scheduled maintenance with downtime.

**•** `ReadOnly` —Maintenance with read-only mode.

`ConnectApi.` Type of managed content channel.

```
ManagedContent
```

**•** `CloudToCloud`
```
ChannelType

```

**•** `CloudToCloud` —Cloud-to-Cloud integrated channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a connected app.

**•** `PublicUnauthenticated` —Public channel. All published content is publicly available.

**•** `UserPermission` —Channel backed by a system permission. All published content is
available only to users with the permission.

`ConnectApi.` Status of the managed content clone.

```
ManagedContent
```

**•** `PartialSuccess`
```
CloneStatus

```

**•** `PartialSuccess`

**•** `Success`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of managed content media.

```
   ManagedContentMediaType
```
**•** `Document`

**•** `Image`

`ConnectApi.` Type of managed content node.

```
   ManagedContentNodeType
```

**•** `Date`

**•** `DateTime`

**•** `Media`

**•** `MediaSource`

**•** `MultilineText`

**•** `NameField`

**•** `RichText`

**•** `Text`

**•** `Url`

`ConnectApi.` Type of managed content provider.

```
   ManagedContent
```

**•** `DigitalAssetManager`
```
   ProviderType

```

`ConnectApi.` Operation to perform on the channel and managed content space.

```
ManagedContent
```

**•** `Add` —Add a channel to a managed content space.
```
SpaceChannelOperation

```

**•** `Add` —Add a channel to a managed content space.

**•** `Remove` —Remove a channel from a managed content space.

`ConnectApi.` Status of the add or remove operation for a channel and managed content space.

```
ManagedContent
```

**•** `Added` —Channel was added to the managed content space.
```
SpaceChannelStatus

```

**•** `Added` —Channel was added to the managed content space.

**•** `Failed` —Add or remove operation failed.

**•** `Pending` —Add or remove operation is pending.

**•** `Removed` —Channel was removed from the managed content space.

`ConnectApi.` Type of managed content space.

```
ManagedContentSpaceType
```
**•** `Content`

**•** `Marketing`

`ConnectApi.` Status of the managed content variant.

```
ManagedContent
```

**•** `Draft` —Content isn’t published.
```
VariantStatus

```

**•** `Draft` —Content isn’t published.

**•** `Published` —Content is published and available for use in your live sites.

**•** `Revised` —Content that’s published and edited. Publish this content to make the changes
available for use in your live sites.

`ConnectApi.ManagedTopic` Type of managed topic.

```
Type
```

**•** `Content` —Topics that are associated with native content.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Featured` —Topics that are featured, for example, on the Experience Cloud site home
page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a navigational menu in the Experience Cloud
site.

`ConnectApi.MarkupType` Type of rich text markup.

**•** `Bold` —Bold tag.

**•** `Code` —Code tag.

**•** `Hyperlink` —Hyperlink anchor tag.

**•** `Italic` —Italic tag.

**•** `ListItem` —List item tag.

**•** `OrderedList` —Ordered list tag.

**•** `Paragraph` —Paragraph tag.

**•** `Strikethrough` —Strikethrough tag.

**•** `Underline` —Underline tag.

**•** `UnorderedList` —Unordered list tag.

`ConnectApi.` Status of sharing a managed content space folder.

```
   MCSFolderShareStatus
```

**•** `PendingShare`

**•** `PendingUnshare`

**•** `Shared`

`ConnectApi.` Type of mention completion.

```
   MentionCompletionType
```

**•** `All` —All mention completions, regardless of the type of record to which the mention
refers.

**•** `Group` —Mention completions for groups.

**•** `User` —Mention completions for users.

`ConnectApi.` Type of validation error for a proposed mention, if any.

```
   MentionValidationStatus
```
**•** `Disallowed` —The proposed mention is invalid and is rejected because the context user
is trying to mention something that is not allowed. For example, a user who is not a member
of a private group is trying to mention the private group.

**•** `Inaccessible` —The proposed mention is allowed, but the user or record being
mentioned isn’t notified. They don't have access to the parent record that’s being discussed.

**•** `Ok` —There is no validation error for this proposed mention.

`ConnectApi.` Type of message segment, such as text, link, field change name, or field change value.

```
   MessageSegmentType
```

**•** `EntityLink`

**•** `FieldChange`

**•** `FieldChangeName`

**•** `FieldChangeValue`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Hashtag`

**•** `InlineImage`

**•** `Link`

**•** `MarkupBegin`

**•** `MarkupEnd`

**•** `Mention`

**•** `MoreChanges`

**•** `ResourceLink`

**•** `Text`

`ConnectApi.` Type of named credential parameter.
`NamedCredential` **•**
```
ParameterType

```

**•** `AllowedManagedPackageNamespaces`

**•** `ClientCertificate`

**•** `ConnectionStatus`

`ConnectApi.` Type of named credential.

```
NamedCredentialType
```

**•** `PrivateEndpoint`

**•** `SecuredEndpoint`

`ConnectApi.` Event, URL type, or modal navigation menu item.

```
NavigationMenuItem
```

**•** `Event` —Event-based navigation.
```
ActionType
```

Note: `Event` is internal only and can’t be used in custom components.

**•** `ExternalLink` —URL outside of your Experience Cloud site.

**•** `InternalLink` —Relative URL inside your Experience Cloud site.

**•** `Modal` —Modal, such as Account Switcher.

`ConnectApi.` Target for the navigation menu item.

```
NavigationMenuItem
```

**•** `CurrentWindow`
```
OpenTarget

```

**•** `CurrentWindow` —Navigation menu item opens in the current window.

**•** `NewWindow` —Navigation menu item opens in a new window.

`ConnectApi.` Type of navigation menu item.

```
NavigationMenuItemType
```

**•** `DataSourceDriven` —Menu items dynamically added from a data source.

**•** `Event` —Event, such as logging in, logging out, or switching accounts.

**•** `ExternalLink` —URL outside of your site.

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `SalesforceObject` —Objects such as accounts, cases, contacts, and custom objects.

**•** `SystemLink` —System link, such as a link to Builder, Workspaces, or Setup.

`ConnectApi.` Type of action.

```
   NBAActionType
```

**•** `Flow` —Automated process tool with multiple subtypes.

`ConnectApi.NBAFlowType` Type of recommended flow.

**•** `AutoLaunchedFlow` —Autolaunched flow that runs in the background.

**•** `Flow` —Screen flow that accepts user inputs.

`ConnectApi.` Type of target.

```
   NBATargetType
```

**•** `Recommendation`

`ConnectApi.` Operation to carry out on the file.

```
   OperationType
```

**•** `Add` —Adds the file to the feed element.

**•** `Remove` —Removes the file from the feed element.

`ConnectApi.` Status of the orchestration instance.

```
   OrchestrationInstanceStatus
```
**•** `Canceled`

**•** `Completed`

**•** `Discontinued`

**•** `Error`

**•** `InProgress`

**•** `NotStarted`

**•** `Suspended`

`ConnectApi.` Type of orchestration step.

```
   OrchestrationStepType
```

**•** `AsynchronousBackgroundStep`

**•** `ApprovalStep`

**•** `BackgroundStep`

**•** `InteractiveStep`

**•** `ManagedContentRoleInteractiveStep`

**•** `ManagedContentVariantAutoPublishBackgroundStep`

**•** `ManagedContentVariantAutoUnpublishBackgroundStep`

**•** `ManagedContentVariantSetLockBackgroundStep`

**•** `ManagedContentVariantSetReadyBackgroundStep`

**•** `MuleSoftStep`

`ConnectApi.` Status of the orchestration work item.

```
   OrchestrationWorkItemStatus
```
**•** `Assigned`

**•** `Completed`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Sort order for order delivery group summaries.

```
OrderDeliveryGroup
```

**•** `IdAsc`
```
SummarySort

```

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

`ConnectApi.` Sort order for order item summaries.

```
OrderItemSummarySort
```

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

`ConnectApi.OrderNulls` Null value order.

**•** `Firsts` —Null values are sorted first.

**•** `Lasts` —Null values are sorted last.

`ConnectApi.` Sort order for order shipment items.

```
OrderShipmentItemSort
```

**•** `IdAsc` —Sorts by ID in ascending alphanumeric order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending alphanumeric order (Z–A, 9–0).

`ConnectApi.` Sort order for order shipments.

```
OrderShipmentSort
```

**•** `ExpectedDeliveryDateAsc` —Sorts by the oldest expected delivery date.

**•** `ExpectedDeliveryDateDesc` —Sorts by the most recent expected delivery date.

**•** `ShipmentNumberAsc` —Sorts by shipment number in ascending order (0–9).

**•** `ShipmentNumberDesc` —Sorts by shipment number in descending order (9–0).

`ConnectApi.OrderSummary` Order summary adjustment aggregate job status.

```
AdjustmentAggregates
```

**•** `Failed`
```
Status

```

**•** `Failed` —The adjustment aggregate data job for the order summary failed.

**•** `InProgress` —The adjustment aggregate data job for the order summary is in progress.

**•** `NotInitiated` —The adjustment aggregate data job for the order summary is not
initiated.

**•** `Submitted` —The adjustment aggregate data job for the order summary is submitted.

`ConnectApi.OrderSummary` Type of price adjustment in promotions.

```
AdjustmentTargetType
```

**•** `SplitLine` —Price adjustment on an order item.

**•** `Header` —Price adjustment on the entire order.

`ConnectApi.OrderSummary` Sort order for order summaries.

```
SortOrder
```

**•** `CreatedDateAsc` —Sorts by the oldest created date.

**•** `CreatedDateDesc` —Sorts by the most recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest ordered date.

**•** `OrderedDateDesc` —Sorts by the most recent ordered date.

`ConnectApi.` Indicates the type of picklist attribute value.

```
PicklistAttributes
```

**•** `CaseStatus`
```
ValueType

```


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `LeadStatus`

**•** `OpportunityStage`

**•** `Standard`

**•** `WorkStepStatus`

`ConnectApi.PeriodType` Time period used for forecasting.

**•** `Month`

**•** `Quarter`

**•** `Week`

**•** `Year`

`ConnectApi.` Location of an action link group on an associated feed element.

```
PlatformAction
```

**•** `Primary`
```
GroupCategory

```

**•** `Primary` —The action link group is displayed in the body of the feed element.

**•** `Overflow` —The action link group is displayed in the overflow menu of the feed element.

`ConnectApi.` Status of the action.

```
PlatformActionStatus
```

**•** `FailedStatus` —The action link execution failed.

**•** `NewStatus` —The action link is ready to be executed. Available for `Download` and `Ui`
action links only.

**•** `PendingStatus` —The action link is executing. Choosing this value triggers the API call
for `Api` and `ApiAsync` action links.

**•** `SuccessfulStatus` —The action link executed successfully.

`ConnectApi.` Type of platform action.

```
PlatformActionType
```

**•** `ActionLink` —An indicator on a feed element that targets an API, a web page, or a file,
represented by a button in the Salesforce UI.

**•** `CustomButton` —When clicked, opens a URL or a Visualforce page in a window or
executes JavaScript.

**•** `ProductivityAction` —Productivity actions are predefined and attached to a limited
set of objects. Productivity actions include Send Email, Call, Map, View Website, and Read
News. Except for the Call action, you can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit, or Delete.

`ConnectApi.PreDeterminedFileNameEnum` Predetermined name of the output file. Either `customFilename` or
`predeterminedFilename` must be present.

**•** `Activation`

**•** `Segment`

**•** `SegmentActivation`

`ConnectApi.` Type of price adjustment for the tier.

```
PriceAdjustmentTierType
```
**•** `AmountBasedAdjustment` —Price is adjusted by a specified amount.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `PercentageBasedAdjustment` —Price is adjusted by a specified percentage.

`ConnectApi.` Unit of time used to define a pricing term.

```
   PricingTermUnit
```

**•** `Months` —Product is priced on a monthly basis.

**•** `Annual` —Product is priced on an annual basis.

`ConnectApi.` View type for product attributes.

```
   ProductAttributeViewType
```
**•** `ColorSwatch`

**•** `Dropdown`

**•** `Pill`

`ConnectApi.ProductClass` Class of product.

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

`ConnectApi.` Type of product media.

```
   ProductMediaType
```

**•** `Document`

**•** `Image`

**•** `Video`

`ConnectApi.` Usage type of a product media item within a media group.

```
   ProductMediaUsageType
```

**•** `Attachment` —Product media group with product documents as attachments.

**•** `Banner` —Product category media group with banner images of the product.

**•** `Listing` —Product media group with listing images of the product.

**•** `Standard` —Product media group with standard images and videos of the product.

**•** `Tile` —Product category media group with tile images of the product.

`ConnectApi.` Publish refresh schedule.

```
   PublishSchedule
```

**•** `One` —Refreshes every hour. Used to rapidly publish UI and DBT-based segments.

**•** `Four` —Refreshes every four hours. Used to rapidly publish UI and DBT-based segments.

**•** `Twelve` —Refreshes every twelve hours.

**•** `TwentyFour` —Refreshes every twenty-four hours.

`ConnectApi.` Publish status of a personalization audience, target, or navigation menu item.

```
   PublishStatus
```

**•** `Draft`

**•** `Live`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Swatch display metadata type.

```
   SwatchDisplayTypeEnum
```

**•** `Color` —Color of the swatch.

`ConnectApi.QuerySqlStatusEnum` Completion status of the query.

**•** `Finished`

**•** `ResultsProduced`

**•** `Running`

**•** `Unspecified`

`ConnectApi.` Action to take on a recommendation.

```
   RecommendationActionType
```
**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.

**•** `view` —View a file, group, article, record, user, custom, or static recommendation.

`ConnectApi.` Custom recommendation audience criteria type.

```
RecommendationAudience
```

**•** `CustomList`
```
CriteriaType

```

**•** `CustomList` —A custom list of users makes up the audience.

**•** `MaxDaysInCommunity` —New members make up the audience.

`ConnectApi.` Operation to carry out on the custom recommendation audience members.

```
RecommendationAudience
```

**•** `Add` —Adds specified members to the audience.
```
MemberOperationType

```

**•** `Add` —Adds specified members to the audience.

**•** `Remove` —Removes specified members from the audience.

`ConnectApi.` A way to tie custom recommendations together. For example, display recommendations in
`RecommendationChannel` specific places in the UI or show recommendations based on time of day or geographic locations.

**•** `CustomChannel1` —Custom recommendation channel. Not used by default. Work with
your community manager to define custom channels. For example, community managers
can use Experience Builder to determine where recommendations appear.

**•** `CustomChannel2` —Custom recommendation channel. Not used by default. Work with
your community manager to define custom channels.

**•** `CustomChannel3` —Custom recommendation channel. Not used by default. Work with
your community manager to define custom channels.

**•** `CustomChannel4` —Custom recommendation channel. Not used by default. Work with
your community manager to define custom channels.

**•** `CustomChannel5` —Custom recommendation channel. Not used by default. Work with
your community manager to define custom channels.

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by
default on the Home and Question Detail pages of Customer Service and Partner Central
Experience Builder templates. They also appear in the feed in the Salesforce mobile web
and anywhere community managers add recommendations using Experience Builder.

`ConnectApi.` Reason for a Chatter recommendation.

```
RecommendationExplanationType
```
**•** `ArticleHasRelatedContent` —Articles with related content to a context article.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `ArticleViewedTogether` —Articles often viewed together with the article that the
context user just viewed.

**•** `ArticleViewedTogetherWithViewers` —Articles often viewed together with
other records that the context user views.

**•** `Custom` —Custom recommendations.

**•** `FilePopular` —Files with many followers or views.

**•** `FileViewedTogether` —Files often viewed at the same time as other files that the
context user views.

**•** `FollowedTogetherWithFollowees` —Users often followed together with other
records that the context user follows.

**•** `GroupMembersFollowed` —Groups with members that the context user follows.

**•** `GroupNew` —Recently created groups.

**•** `GroupPopular` —Groups with many active members.

**•** `ItemViewedTogether` —Records often viewed at the same time as other records that
the context user views.

**•** `PopularApp` —Applications that are popular.

**•** `RecordOwned` —Records that the context user owns.

**•** `RecordParentOfFollowed` —Parent records of records that the context user follows.

**•** `RecordViewed` —Records that the context user recently viewed.

**•** `TopicFollowedTogether` —Topics often followed together with the record that the
context user just followed.

**•** `TopicFollowedTogetherWithFollowees` —Topics often followed together with
other records that the context user follows.

**•** `TopicPopularFollowed` —Topics with many followers.

**•** `TopicPopularLiked` —Topics on posts that have many likes.

**•** `UserDirectReport` —Users who report to the context user.

**•** `UserFollowedTogether` —Users often followed together with the record that the
context user followed .

**•** `UserFollowsSameUsers` —Users who follow the same users as the context user.

**•** `UserManager` —The context user’s manager.

**•** `UserNew` —Recently created users.

**•** `UserPeer` —Users who report to the same manager as the context user.

**•** `UserPopular` —Users with many followers.

**•** `UserViewingSameRecords` —Users who view the same records as the context user.

`ConnectApi.` Type of reaction to a recommendation.

```
   RecommendationReactionType
```
**•** `Accepted`

**•** `Rejected`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of record being recommended.

```
   RecommendationType
```

**•** `apps`

**•** `articles`

**•** `files`

**•** `groups`

**•** `records`

**•** `topics`

**•** `users`

`ConnectApi.` Type of object being recommended.

```
   RecommendedObjectType
```

**•** `Today` —Static recommendations that don’t have an ID, for example, the Today app
recommendation.

`ConnectApi.` Order in which fields are rendered in a grid.

```
   RecordColumnOrder
```

**•** `LeftRight` —Fields are rendered from left to right.

**•** `TopDown` —Fields are rendered from the top down.

`ConnectApi.` Data type of a record field.

```
   RecordFieldType
```

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

`ConnectApi.` Type of related feed post.

```
   RelatedFeedPostType
```

**•** `Answered` —Related questions that have at least one answer.

**•** `BestAnswer` —Related questions that have a best answer.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Generic` —All types of related questions, including answered, with a best answer, and
unanswered.

**•** `Unanswered` —Related questions that don’t have answers.

`ConnectApi.RelationshipCardinality` Cardinality of the relationship of a field for object data of the data graph.

**•** `CardinalityUnspecified`

**•** `ManyToOne`

**•** `OneToMany`

**•** `OneToOne`

`ConnectApi.` Saved payment method status.

```
   SavedPaymentMethodStatus
```
**•** `AlreadyExists`

**•** `Created`

**•** `Updated`

`ConnectApi.SearchBoostBuryRuleAction` Action of the boost and bury rule.

**•** `Boost` —Boost rule. Increases search result rankings for targeted products.

**•** `Bury` —Bury rule. Decreases search result rankings for targeted products.

`ConnectApi.SearchBoostBuryRuleOperation` Operation for the conditions of the target expression in the boost and bury rule.

**•** `AllOf` —All-of operation.

**•** `AnyOf` —Any-of operation.

`ConnectApi.SearchOrder` Order direction.

**•** `Ascending`

**•** `Descending`

`ConnectApi.SegmentType` Type of segment.

**•** `Dbt` —Data build tool

`ConnectApi.` Type of product selling model.

```
   SellingModelType
```

**•** `Evergreen` —A subscription without an end date. An evergreen subscription continues
until the shopper affirmatively cancels it.

**•** `OneTime` —A product that isn’t sold as a subscription.

**•** `TermDefined` —A subscription with a defined end date. The subscription continues for
a specified time period. When the term ends, the subscription ends.

`ConnectApi.` Type of site search result item.

```
   SitesPageType
```

**•** `ContentPage`

**•** `SitePage`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Social network provider.

```
   SocialNetworkProvider
```

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

`ConnectApi.SocialPost` Message type of the social post.

```
   MessageType
```

**•** `Comment`

**•** `Direct`

**•** `Post`

**•** `PrivateMessage`

**•** `Reply`

**•** `Retweet`

**•** `Tweet`

`ConnectApi.` State of the social post.

```
   SocialPostStatusType
```

**•** `ApprovalPending`

**•** `ApprovalRecalled`

**•** `ApprovalRejected`

**•** `Deleted`

**•** `Failed`


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Hidden`

**•** `Pending`

**•** `Sent`

**•** `Unknown`

`ConnectApi.SortOrder` Order for sorting.

**•** `Ascending` —Items are in ascending alphabetical order (A-Z).

**•** `Descending` —Items are in descending alphabetical order (Z-A).

**•** `MostRecentlyViewed` —Items are in descending chronological order by view. This
sort order is valid only for Chatter feed streams.

`ConnectApi.` Three-letter code that identifies the type of electronic payment transaction being processed
`StandardEntryClassCode` within the Automated Clearing House (ACH) network.

**•** `CCD` —Corporate Credit or Debit

**•** `PPD` —Prearranged Payment and Deposit

**•** `TEL` —Telephone-Initiated Entry

**•** `WEB` —Internet Initiated/Mobile

`ConnectApi.` Status of a survey invitation email.

```
   SurveyEmailStatusEnum
```

**•** `Failed` —The survey invitation email wasn't sent.

**•** `Queued` —The survey invitation email is queued for sending.

`ConnectApi.SvcApptModeEnum` Mode of the service appointment.

**•** `Group`                  - Service appointment mode is Group.

**•** `Regular`                  - Default mode of service appointment.

`ConnectApi.TargetType` Target type of a promotion discount.

**•** `Shipping` —Promotion discounts shipping amount.

**•** `Transaction` —Promotion discounts total transaction amount.

`ConnectApi.SwatchDisplayTypeEnum` Display metadata type of the swatch.

**•** `Color` —Color of the swatch.

`ConnectApi.` Status of a tax transaction.

```
   TaxTransactionStatus
```

**•** `Committed` —Tax has been committed to the transaction.

**•** `Uncommitted` —Tax hasn’t been committed to the transaction.

`ConnectApi.` Type of tax transaction.

```
   TaxTransactionType
```

**•** `Credit` —Transaction is a credit transaction.

**•** `Debit` —Transaction is a debit transaction.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Void` —Reserved for internal use in case of input. In case of output, this value specifies that
the tax engine has voided the document that's mentioned as the
`referenceDocumentCode` property value.

`ConnectApi.TopicSort` Order returned by the sort.

**•** `popularDesc` —Sorts topics by popularity with the most popular first. This value is the
default.

**•** `alphaAsc` —Sorts topics alphabetically.

`ConnectApi.TypeEnum` Type of the SQL parameter.

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

`ConnectApi.` Type of vote for a feed element or comment.

```
   UpDownVoteValue
```

**•** `Down`

**•** `None`

**•** `Up`

`ConnectApi.UserActivityType` Type of user activity.

**•** `Bookmark` —User bookmarked a post.

**•** `ChatterActivity` —Total counts of posts and comments made and likes and comments
received for a user.

**•** `ChatterLike` —User liked a post or comment.

**•** `Comment` —User commented on a post.

**•** `CompanyVerify` —User verified comment.

**•** `DownVote` —User downvoted a post or comment.


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `FeedEntityRead` —User read a post.

**•** `FeedRead` —User read a feed.

**•** `Mute` —User muted a post.

**•** `Post` —User made a post.

**•** `TopicEndorsement` —User endorsed another user on a topic or received endorsement
on a topic.

**•** `UpVote` —User upvoted a post or comment.

`ConnectApi.UserMission` Type of mission activity for a user.

```
   ActivityType
```

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

`ConnectApi.UserProfile` Type of user profile tab.

```
   TabType
```

**•** `CustomVisualForce` —Tab that displays data from a Visualforce page.

**•** `CustomWeb` —Tab that displays data from any external web-based application or web
page.

**•** `Element` —Tab that displays generic content inline.

**•** `Feed` —Tab that displays the Chatter feed.

**•** `Overview` —Tab that displays user details.

`ConnectApi.UserType` Type of user.

**•** `ChatterGuest` —User is an external user in a private group.

**•** `ChatterOnly` —User is a Chatter Free customer.

**•** `Guest` —User is unauthenticated.

**•** `Internal` —User is a standard org member.

**•** `Portal` —User is an external user in an Experience Cloud site.

**•** `System` —User is Chatter Expert or a system user.

**•** `Undefined` —User is a user type that is a custom object.

`ConnectApi.WishlistItem` Sort order for wishlist items.

```
   SortOrder
```

**•** `CreatedDateAsc` —Sorts by oldest creation date.

**•** `CreatedDateDesc` —Sorts by most recent creation date.


### Apex Reference Guide ConnectApi Exceptions

**Enum** **Description**

`ConnectApi.` Status of a workflow process.

```
   WorkflowProcessStatus
```

**•** `Approved`

**•** `Fault`

**•** `Held`

**•** `NoResponse`

**•** `Pending`

**•** `Reassigned`

**•** `Rejected`

**•** `Removed`

**•** `Started`

`ConnectApi.ZoneSearch` Zone search result type.

```
   ResultType
```

**•** `Article` —Search results contain only articles.

**•** `Question` —Search results contain only questions.

`ConnectApi.ZoneShowIn` Zone search result location.

**•** `Community` —Available in an Experience Cloud site.

**•** `Internal` —Available internally only.

**•** `Portal` —Available in a portal.

### ConnectApi Exceptions The ConnectApi namespace contains exception classes.

All exceptions classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3784.

### The ConnectApi namespace contains these exceptions:

**Exception** **Description**

```
ConnectApi.ConnectApiException

```

Any logic error in the way your application is utilizing
### ConnectApi code. This is equivalent to receiving a 400 error

from Connect REST API.

`ConnectApi.NotFoundException` Any issues with the specified resource being found. This is
equivalent to receiving a 404 error from Connect REST API.

`ConnectApi.RateLimitException` When you exceed the rate limit. This is equivalent to receiving a
503 Service Unavailable error from Connect REST API.

### ConnectApi Utilities The ConnectApi namespace contains a utility class.


### Apex Reference Guide ConnectApi Release Notes

**Utility** **Description**

```
ConnectApi.ConnectUtilities.unwrapApexWrapper()

```

Example

Unwraps obfuscated, Apex-wrapped objects into known types
such as `Map<String, Object>` . Example from Apex Debug
log: `core.connect.apex.ApexMapWrapper@7270879d`

This example calls `getManagedContentForSite(siteId, contentKeyOrId, showAbsoluteUrl)` to get a custom
content type with an image reference and uses the `ConnectApi.ConnectUtilities.unwrapApexWrapper()` utility.

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

### ConnectApi Release Notes

```

Use the Salesforce Release Notes to learn about the most recent updates and changes to the ConnectApi namespace in Apex.

[For updates and changes that impact Apex, including ConnectApi, see the Apex Release Notes.](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm&language=en_US)

[For new and changed ConnectApi classes and enums, see ConnectApi (Connect in Apex): New and Changed Classes and Enums in the](https://help.salesforce.com/s/articleView?id=release-notes.rn_connect_in_apex.htm&language=en_US)
Salesforce Release Notes.


## Apex Reference Guide Context Namespace Context Namespace The Context namespace provides classes and methods to manage the sharing and consumption of business application data by

using Context Service.

## The Context namespace includes the IndustriesContext class. Database Namespace The Database namespace provides classes used with DML operations. The following are the classes in the Database namespace.

IN THIS SECTION:

Batchable Interface
The class that implements this interface can be executed as a batch Apex job.

BatchableContext Interface
Represents the parameter type of a batch job method and contains the batch job ID. This interface is implemented internally by
Apex.

Cursor Class
Contains methods to fetch records and to get the number of cursor rows returned from a SOQL query.

CursorFetchResult Class
This class encapsulates the result of a `PaginationCursor.fetchPage()` call. It contains methods that get the rows for
the current page, the start index of the next page, and the number of deleted rows skipped during the fetch operation. It also contains
a method that indicates whether the pagination cursor has fetched all available rows in the result set.

DeletedRecord Class
Contains information about a deleted record.

DeleteResult Class
Represents the result of a delete DML operation returned by the `Database.delete` method.

DMLOptions Class
Enables you to set options related to DML operations.

DmlOptions.AssignmentRuleHeader Class
Enables setting assignment rule options.

DMLOptions.DuplicateRuleHeader Class
Determines options for using duplicate rules to detect duplicate records. Duplicate rules are part of the Duplicate Management
feature.

DmlOptions.EmailHeader Class
Enables setting email options.

DuplicateError Class
Contains information about an error that occurred when an attempt was made to save a duplicate record. Use if your organization
has set up duplicate rules, which are part of the Duplicate Management feature.

EmptyRecycleBinResult Class
The result of the emptyRecycleBin DML operation returned by the `Database.emptyRecycleBin` method.


### Apex Reference Guide Batchable Interface

Error Class
Represents information about an error that occurred during a DML operation when using a Database method.

GetDeletedResult Class
Contains the deleted records retrieved for a specific sObject type and time window.

GetUpdatedResult Class
Contains the result for the `Database.getUpdated` method call.

LeadConvert Class
Contains information used for lead conversion.

LeadConvertResult Class
The result of a lead conversion.

MergeResult Class
Contains the result of a merge Database method operation.

PaginationCursor Class
This class represents a pagination cursor that can traverse a SOQL query result set. It contains methods that fetch rows by page. It
also contains a method that returns the total number of rows in the result set.

QueryLocator Class
Represents the record set returned by `Database.getQueryLocator` and used with Batch Apex.

QueryLocatorIterator Class
Represents an iterator over a query locator record set.

SaveResult Class
The result of an insert or update DML operation returned by a Database method.

UndeleteResult Class
The result of an undelete DML operation returned by the `Database.undelete` method.

UpsertResult Class
The result of an upsert DML operation returned by the `Database.upsert` method.

### Batchable Interface

The class that implements this interface can be executed as a batch Apex job.

Namespace

Database

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)_ : Using Batch

#### Batchable Methods

### The following are methods for Batchable .


Apex Reference Guide Batchable Interface

IN THIS SECTION:

##### execute(jobId, recordList)

Gets invoked when the batch job executes and operates on one batch of records. Contains or calls the main execution logic for the
batch job.

##### finish(jobId)

Gets invoked when the batch job finishes. Place any clean up code in this method.

start(jobId)
Gets invoked when the batch job starts. Returns the record set as an iterable that will be batched for execution.

start(jobId)
Gets invoked when the batch job starts. Returns the record set as a QueryLocator object that will be batched for execution.

##### execute(jobId, recordList)

Gets invoked when the batch job executes and operates on one batch of records. Contains or calls the main execution logic for the batch
job.

Signature

```
   public Void execute(Database.BatchableContext jobId, List<sObject> recordList)

```

Parameters

```
   jobId
```

Type: Database.BatchableContext

Contains the job ID.

```
   recordList
```

Type: List<sObject>

Contains the batch of records to process.

Return Value

Type: Void

##### finish(jobId)

Gets invoked when the batch job finishes. Place any clean up code in this method.

Signature

```
   public Void finish(Database.BatchableContext jobId)

```

Parameters

```
   jobId
```

Type: Database.BatchableContext

Contains the job ID.


### Apex Reference Guide BatchableContext Interface

Return Value

Type: Void

##### start(jobId)

Gets invoked when the batch job starts. Returns the record set as an iterable that will be batched for execution.

Signature

```
   public System.Iterable start(Database.BatchableContext jobId)

```

Parameters

```
   jobId
```

Type: Database.BatchableContext

Contains the job ID.

Return Value

Type: System.Iterable

##### start(jobId)

Gets invoked when the batch job starts. Returns the record set as a QueryLocator object that will be batched for execution.

Signature

```
   public Database.QueryLocator start(Database.BatchableContext jobId)

```

Parameters

```
   jobId
```

Type: Database.BatchableContext

Contains the job ID.

Return Value

Type: Database.QueryLocator

### BatchableContext Interface

Represents the parameter type of a batch job method and contains the batch job ID. This interface is implemented internally by Apex.


### Apex Reference Guide Cursor Class

Namespace

Database

SEE ALSO:

Batchable Interface

#### BatchableContext Methods The following are methods for BatchableContext .

IN THIS SECTION:

##### getChildJobId()

Returns the ID of the current batch job chunk that is being processed.

##### getJobId()

Returns the batch job ID.

##### getChildJobId()

Returns the ID of the current batch job chunk that is being processed.

Signature

```
   public Id getChildJobId()

```

Return Value

Type: ID

##### getJobId()

Returns the batch job ID.

Signature

```
   public Id getJobId()

```

Return Value

Type: ID

### Cursor Class

Contains methods to fetch records and to get the number of cursor rows returned from a SOQL query.

Namespace

Database


Apex Reference Guide Cursor Class

Usage

A cursor is created when a SOQL query is executed on a `Database.getCursor()` or a `Database.getCursorWithBinds()`
call. When the SOQL query is invoked, the corresponding rows are returned from the cursor. The maximum number of rows per cursor
is 50 million, regardless of the operation being synchronous or asynchronous.

Example

```
   public with sharing class QueryChunkingQueueable implements Queueable {

      private Database.Cursor locator;

      private Integer position;

      public QueryChunkingQueueable() {

        locator = Database.getCursor(

           'SELECT Id FROM Contact WHERE LastActivityDate = LAST_N_DAYS:400',

           AccessLevel.USER_MODE);

        position = 0;

      }

      public void execute(QueueableContext ctx) {

        Integer remainingRows = locator.getNumRecords() - position;

        if (remainingRows == 0) {

           return; // Nothing to do

        }

        // Take the minimum of batch size and remaining rows to avoid over-fetching

        Integer fetchSize = Math.min(200, remainingRows);

        List<Contact> scope = locator.fetch(position, 200);

        position += scope.size();

        // do something, like archive or delete the scope list records

        if (position < locator.getNumRecords()) {

           // process the next chunk

           System.enqueueJob(this);

        }

      }

   }

```

IN THIS SECTION:

#### Cursor Methods Cursor Methods The following are methods for Cursor .

IN THIS SECTION:

fetch(position, count)
Fetches cursor rows that correspond to the offset position and the specified record count. The maximum number of rows per cursor
is 50 million, regardless of the operation being synchronous or asynchronous. Calling the `Cursor.fetch()` method counts
against the SOQL query limit, and the rows fetched count against the SOQL query row limit.


### Apex Reference Guide CursorFetchResult Class

##### getNumRecords()

Gets the number of rows returned in an Apex cursor from a `Cursor.fetch(position, count)` operation.

##### **`fetch(position, count)`**

Fetches cursor rows that correspond to the offset position and the specified record count. The maximum number of rows per cursor is
50 million, regardless of the operation being synchronous or asynchronous. Calling the `Cursor.fetch()` method counts against
the SOQL query limit, and the rows fetched count against the SOQL query row limit.

Signature

```
   public static List<SObject> fetch(Integer position, Integer count)

```

Parameters

```
   position
```

Type: Integer

The offset position from which records are fetched.

```
   count
```

Type: Integer

The number of sObjects to fetch from the cursor, up to a maximum of 2,000.

Return Value

Type: List on page 3891<sObject>

The list of sObjects from the SOQL query, starting from the specified position.

##### **`getNumRecords()`**

Gets the number of rows returned in an Apex cursor from a `Cursor.fetch(position, count)` operation.

Signature

```
   public static Integer getNumRecords()

```

Return Value

Type: Integer

### CursorFetchResult Class

This class encapsulates the result of a `PaginationCursor.fetchPage()` call. It contains methods that get the rows for the
current page, the start index of the next page, and the number of deleted rows skipped during the fetch operation. It also contains a
method that indicates whether the pagination cursor has fetched all available rows in the result set.

Namespace

Database


Apex Reference Guide CursorFetchResult Class

IN THIS SECTION:

#### CursorFetchResult Methods CursorFetchResult Methods The following are methods for CursorFetchResult .

IN THIS SECTION:

##### getNextIndex()

Gets the start index required to fetch the next page of results. Use this value as the _`start`_ parameter in the call to
`PaginationCursor.fetchPage(start, pageSize)` to fetch the next page of results.

##### getNumDeletedRecords()

Gets the number of deleted rows that were skipped during the fetch operation.

##### getRecords()

Gets the list of records that comprise the rows on the current page.

isDone()
Returns `true` if the pagination cursor has reached either the page size passed to `PaginationCursor.fetchPage(start,`
`pageSize)` or the end of the result set. Otherwise returns `false` .

##### **`getNextIndex()`**

Gets the start index required to fetch the next page of results. Use this value as the _`start`_ parameter in the call to
`PaginationCursor.fetchPage(start, pageSize)` to fetch the next page of results.

Signature

```
   public Integer getNextIndex()

```

Return Value

Type: Integer

##### **`getNumDeletedRecords()`**

Gets the number of deleted rows that were skipped during the fetch operation.

Signature

```
   public Integer getNumDeletedRecords()

```

Return Value

Type: Integer

##### **`getRecords()`**

Gets the list of records that comprise the rows on the current page.


### Apex Reference Guide DeletedRecord Class

Signature

```
   public List<SObject> getRecords()

```

Return Value

Type: List on page 3891<sObject>

The list of sObjects from the SOQL query for the current page.

##### **`isDone()`**

Returns `true` if the pagination cursor has reached either the page size passed to `PaginationCursor.fetchPage(start,`
`pageSize)` or the end of the result set. Otherwise returns `false` .

Signature

```
   public Boolean isDone()

```

Return Value

Type: Boolean

SEE ALSO:

getPaginationCursor(query, accessLevel)

PaginationCursor Class

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cursors.htm)_ : Apex Cursors

### DeletedRecord Class

Contains information about a deleted record.

Namespace

Database

Usage

The `getDeletedRecords` method of the `Database.GetDeletedResult` class returns a list of
`Database.DeletedRecord` objects. Use the methods in the `Database.DeletedRecord` class to retrieve details about
each deleted record.

#### DeletedRecord Methods

### The following are methods for DeletedRecord . All are instance methods.


### Apex Reference Guide DeleteResult Class

IN THIS SECTION:

##### getDeletedDate()

Returns the deleted date of this record.

##### getId()

Returns the ID of a record deleted within the time window specified in the `Database.getDeleted` method.

##### getDeletedDate()

Returns the deleted date of this record.

Signature

```
   public Date getDeletedDate()

```

Return Value

Type: Date

##### getId()

Returns the ID of a record deleted within the time window specified in the `Database.getDeleted` method.

Signature

```
   public Id getId()

```

Return Value

Type: ID

### DeleteResult Class

Represents the result of a delete DML operation returned by the `Database.delete` method.

Namespace

Database

Usage

An array of `Database.DeleteResult` objects is returned with the `delete` database method. Each element in the DeleteResult
array corresponds to the sObject array passed as the _`sObject[]`_ parameter in the `delete` Database method; that is, the first
element in the DeleteResult array matches the first element passed in the sObject array, the second element corresponds with the second
element, and so on. If only one sObject is passed in, the DeleteResult array contains a single element.


Apex Reference Guide DeleteResult Class

Example

The following example shows how to obtain and iterate through the returned `Database.DeleteResult` objects. It deletes some
queried accounts using `Database.delete` with a false second parameter to allow partial processing of records on failure. Next, it
iterates through the results to determine whether the operation was successful or not for each record. It writes the ID of every record
that was processed successfully to the debug log, or error messages and fields of the failed records.

```
   // Query the accounts to delete

   Account[] accts = [SELECT Id from Account WHERE Name LIKE 'Acme%'];

   // Delete the accounts

   Database.DeleteResult[] drList = Database.delete(accts, false);

   // Iterate through each returned result

   for(Database.DeleteResult dr : drList) {

      if (dr.isSuccess()) {

        // Operation was successful, so get the ID of the record that was processed

        System.debug('Successfully deleted account with ID: ' + dr.getId());

      }

      else {

        // Operation failed, so get all errors

        for(Database.Error err : dr.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Account fields that affected this error: ' + err.getFields());

        }

      }

   }

#### DeleteResult Methods The following are methods for DeleteResult . All are instance methods.

```

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error
occurred, returns an empty set.

getId()
Returns the ID of the sObject you were trying to delete.

isSuccess()
A Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error occurred,
returns an empty set.

Signature

```
   public Database.Error[] getErrors()

```


### Apex Reference Guide DMLOptions Class

Return Value

Type: Database.Error[]

##### getId()

Returns the ID of the sObject you were trying to delete.

Signature

```
   public ID getId()

```

Return Value

Type: ID

##### isSuccess()

A Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### DMLOptions Class

Enables you to set options related to DML operations.

Namespace

Database

Usage

`Database.DMLOptions` is only available for Apex saved against API versions 15.0 and higher. DMLOptions settings take effect
only for record operations performed using Apex DML and not through the Salesforce user interface. The DMLOptions class has three
child options.

**DML Child Options**

DmlOptions.AssignmentRuleHeader—Enables setting assignment rule options.

DmlOptions.DuplicateRuleHeader—Determines options for using duplicate rules to detect duplicate records. Duplicate rules are
part of the Duplicate Management feature.


Apex Reference Guide DMLOptions Class

DmlOptions.EmailHeader—Enables setting email options.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_insert_3)_ : Database.insert()

_Apex Reference Guide_ [: SObject.setOptions()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_sobject.htm#apex_System_SObject_setOptions)

#### DmlOptions Properties The following are properties for DmlOptions .

IN THIS SECTION:

##### allowFieldTruncation

Specifies the truncation behavior of large strings.

##### assignmentRuleHeader

Specifies the assignment rule to be used when creating a case or lead.

emailHeader
Specifies additional information regarding the automatic email that gets sent when an events occurs.

localeOptions
Specifies the language of any labels that are returned by Apex.

optAllOrNone
Specifies whether the operation allows for partial success.

##### allowFieldTruncation

Specifies the truncation behavior of large strings.

Signature

```
   public Boolean allowFieldTruncation {get; set;}

```

Property Value

Type: Boolean

Usage

In Apex saved against API versions previous to 15.0, if you specify a value for a string and that value is too large, the value is truncated.
For API version 15.0 and later, if a value is specified that is too large, the operation fails and an error message is returned. The
##### allowFieldTruncation property allows you to specify that the previous behavior, truncation, be used instead of the new

behavior in Apex saved against API versions 15.0 and later.

##### assignmentRuleHeader

Specifies the assignment rule to be used when creating a case or lead.


Apex Reference Guide DMLOptions Class

Signature

```
   public Database.DmlOptions.Assignmentruleheader assignmentRuleHeader {get; set;}

```

Property Value

Type: Database.DMLOptions.AssignmentRuleHeader

Usage

DMLOption.AssignmentRuleHeader.useDefaultRule affects only the default assignment rule and does not disable other existing assignment
rules on the object.

Note: The Database.DMLOptions object supports assignment rules for cases and leads, but not for accounts.

##### emailHeader

Specifies additional information regarding the automatic email that gets sent when an events occurs.

Signature

```
   public Database.DmlOptions.EmailHeader emailHeader {get; set;}

```

Property Value

Type: Database.DMLOptions.EmailHeader

Usage

The Salesforce user interface allows you to specify whether or not to send an email when the following events occur.

**•** Creation of a new case or task

**•** Conversion of a case email to a contact

**•** New user email notification

**•** Lead queue email notification

**•** Password reset

##### In Apex saved against API version 15.0 or later, the Database.DMLOptions emailHeader property enables you to specify additional

information regarding the email that gets sent when one of the events occurs because of the code's execution.

##### localeOptions

Specifies the language of any labels that are returned by Apex.

Signature

```
   public Database.DmlOptions.LocaleOptions localeOptions {get; set;}

```

Property Value

Type: Database.DMLOptions.LocaleOptions


### Apex Reference Guide DmlOptions.AssignmentRuleHeader Class

Usage

The value must be a valid user locale (language and country), such as de_DE or en_GB. The value is a String, 2-5 characters long. The
first two characters are always an ISO language code, for example 'fr' or 'en.' If the value is further qualified by a country, then the string
also has an underscore (_) and another ISO country code, for example 'US' or 'UK'. For example, the string for the United States is 'en_US',
and the string for French Canadian is 'fr_CA'.

##### optAllOrNone

Specifies whether the operation allows for partial success.

Signature

```
   public Boolean optAllOrNone {get; set;}

```

Property Value

Type: Boolean

Usage

##### If optAllOrNone is set to true, all changes are rolled back if any record causes errors. The default for this property is false and successfully processed records are committed while records with errors aren't. If optAllOrNone is set to false and a record fails,

the remainder of the DML operation can still succeed. You must iterate through the returned results to identify which records succeeded
or failed.

This property is available in Apex saved against Salesforce API version 20.0 and later.

### DmlOptions.AssignmentRuleHeader Class

Enables setting assignment rule options.

Namespace

Database

Example

The following example uses the `useDefaultRule` option:

```
   Database.DMLOptions dmo = new Database.DMLOptions();

   dmo.assignmentRuleHeader.useDefaultRule= true;

   Lead l = new Lead(company='ABC', lastname='Smith');

   l.setOptions(dmo);

   insert l;

```

The following example uses the `assignmentRuleID` option:

```
   Database.DMLOptions dmo = new Database.DMLOptions();

   dmo.assignmentRuleHeader.assignmentRuleId= '01QD0000000EqAn';

```


Apex Reference Guide DmlOptions.AssignmentRuleHeader Class

```
   Lead l = new Lead(company='ABC', lastname='Smith');

   l.setOptions(dmo);

   insert l;

#### DmlOptions.AssignmentRuleHeader Properties The following are properties for DmlOptions.AssignmentRuleHeader .

```

IN THIS SECTION:

##### assignmentRuleID

Specifies the ID of a specific assignment rule to run for the case or lead. The assignment rule can be active or inactive.

##### useDefaultRule

If specified as `true` for a case or lead, the system uses the default (active) assignment rule for the case or lead. If specified, do not
specify an `assignmentRuleId` .

##### assignmentRuleID

Specifies the ID of a specific assignment rule to run for the case or lead. The assignment rule can be active or inactive.

Signature

```
   public Id assignmentRuleID {get; set;}

```

Property Value

Type: ID

Usage

##### The ID can be retrieved by querying the AssignmentRule sObject. If specified, do not specify useDefaultRule .

If the value is not in the correct ID format (15-character or 18-character Salesforce ID), the call fails and an exception is returned.

##### useDefaultRule

If specified as `true` for a case or lead, the system uses the default (active) assignment rule for the case or lead. If specified, do not specify
an `assignmentRuleId` .

Signature

```
   public Boolean useDefaultRule {get; set;}

```

Property Value

Type: Boolean


### Apex Reference Guide DMLOptions.DuplicateRuleHeader Class

Usage

If there are no assignment rules in the organization, in API version 29.0 and earlier, creating a case or lead with `useDefaultRule`
set to `true` results in the case or lead being assigned to the predefined default owner. In API version 30.0 and later, the case or lead is
unassigned and doesn't get assigned to the default owner.

### DMLOptions.DuplicateRuleHeader Class

Determines options for using duplicate rules to detect duplicate records. Duplicate rules are part of the Duplicate Management feature.

Namespace

Database

Example

The following example shows how to save an account record that’s been identified as a duplicate. To learn how to iterate through
duplicate errors, see DuplicateError Class

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.DuplicateRuleHeader.allowSave = true;

   dml.DuplicateRuleHeader.runAsCurrentUser = true;

   Account duplicateAccount = new Account(Name='dupe');

   Database.SaveResult sr = Database.insert(duplicateAccount, dml);

   if (sr.isSuccess()) {

    System.debug('Duplicate account has been inserted in Salesforce!');

   }

```

IN THIS SECTION:

#### DMLOptions.DuplicateRuleHeader Properties DMLOptions.DuplicateRuleHeader Properties

### The following are properties for DMLOptions.DuplicateRuleHeader .

IN THIS SECTION:

##### allowSave

For a duplicate rule, when the Alert option is enabled, bypass alerts and save duplicate records by setting this property to `true` .
Prevent duplicate records from being saved by setting this property to `false` .

runAsCurrentUser
Make sure that sharing rules for the current user are enforced when duplicate rules run by setting this property to `true` . Use the
sharing rules specified in the class for the request by setting this property to `false` . If no sharing rules are specified, Apex code
runs in system context and sharing rules for the current user are not enforced.

##### allowSave

For a duplicate rule, when the Alert option is enabled, bypass alerts and save duplicate records by setting this property to `true` . Prevent
duplicate records from being saved by setting this property to `false` .


Apex Reference Guide DMLOptions.DuplicateRuleHeader Class

Signature

```
   public Boolean allowSave {get; set;}

```

Property Value

Type: Boolean

Example

This example shows how to save an account record that’s been identified as a duplicate.
`dml.DuplicateRuleHeader.allowSave = true` means the user should be allowed to save the duplicate. To learn how
to iterate through duplicate errors, see DuplicateError Class.

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.DuplicateRuleHeader.allowSave = true;

   dml.DuplicateRuleHeader.runAsCurrentUser = true;

   Account duplicateAccount = new Account(Name='dupe');

   Database.SaveResult sr = Database.insert(duplicateAccount, dml);

   if (sr.isSuccess()) {

    System.debug('Duplicate account has been inserted in Salesforce!');

   }

##### runAsCurrentUser

```

Make sure that sharing rules for the current user are enforced when duplicate rules run by setting this property to `true` . Use the sharing
rules specified in the class for the request by setting this property to `false` . If no sharing rules are specified, Apex code runs in system
context and sharing rules for the current user are not enforced.

Signature

```
   public Boolean runAsCurrentUser {get; set;}

```

Property Value

Type: Boolean

Usage

If specified as `true`, duplicate rules run for the current user, which ensures users can’t view duplicate records that aren’t available to
them.

##### Use runAsCurrentUser = true to detect duplicates when converting leads to contacts. Typically, lead conversion Apex code

runs in a system context and does not enforce sharing rules for the current user.

Example

This example shows how to set options so that duplicate rules run for the current user when saving a new account.

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.DuplicateRuleHeader.allowSave = true;

   dml.DuplicateRuleHeader.runAsCurrentUser = true;

   Account duplicateAccount = new Account(Name='dupe');

```


### Apex Reference Guide DmlOptions.EmailHeader Class

```
   Database.SaveResult sr = Database.insert(duplicateAccount, dml);

   if (sr.isSuccess()) {

    System.debug('Duplicate account has been inserted in Salesforce!');

   }

### DmlOptions.EmailHeader Class

```

Enables setting email options.

Namespace

Database

Usage

Even though auto-sent emails can be triggered by actions in the Salesforce user interface, the DMLOptions settings for `emailHeader`
take effect only for DML operations carried out in Apex code.

Example

In the following example, the `triggerAutoResponseEmail` option is specified:

```
   Account a = new Account(name='Acme Plumbing');

      insert a;

      Contact c = new Contact(email='jplumber@salesforce.com',

   firstname='Joe',lastname='Plumber', accountid=a.id);

      insert c;

      Database.DMLOptions dlo = new Database.DMLOptions();

      dlo.EmailHeader.triggerAutoResponseEmail = true;

      Case ca = new Case(subject='Plumbing Problems', contactid=c.id);

      database.insert(ca, dlo);

```

Suppose that you use an after-insert or after-update trigger to change ownership of leads, contacts, or opportunities. If you use the API
to change record ownership, or if a Lightning Experience user changes a record’s owner, no email notification is sent. To send email
notifications to a record’s new owner, set the `triggerUserEmail` property to `true` .

#### DmlOptions.EmailHeader Properties

### The following are properties for DmlOptions.EmailHeader .


Apex Reference Guide DmlOptions.EmailHeader Class

IN THIS SECTION:

##### triggerAutoResponseEmail

Indicates whether to trigger auto-response rules ( `true` ) or not ( `false` ), for leads and cases.

##### triggerOtherEmail

Indicates whether to trigger email outside the organization ( `true` ) or not ( `false` ).

triggerUserEmail
Indicates whether to trigger email that is sent to users in the organization ( `true` ) or not ( `false` ).

##### triggerAutoResponseEmail

Indicates whether to trigger auto-response rules ( `true` ) or not ( `false` ), for leads and cases.

Signature

```
   public Boolean triggerAutoResponseEmail {get; set;}

```

Property Value

Type: Boolean

Usage

This email can be automatically triggered by a number of events, for example creating a case or resetting a user password. If this value
is set to `true`, when a case is created, if there is an email address for the contact specified in `ContactID`, the email is sent to that
address. If not, the email is sent to the address specified in `SuppliedEmail`

##### triggerOtherEmail

Indicates whether to trigger email outside the organization ( `true` ) or not ( `false` ).

Signature

```
   public Boolean triggerOtherEmail {get; set;}

```

Property Value

Type: Boolean

Usage

This email can be automatically triggered by creating, editing, or deleting a contact for a case.

Note: Email sent through Apex because of a group event includes additional behaviors. A _group event_ is an event for which
`IsGroupEvent` is true. The `EventAttendee` object tracks the users, leads, or contacts that are invited to a group event.
Note the following behaviors for group event email sent through Apex:

##### • Sending a group event invitation to a lead or contact respects the triggerOtherEmail option • Email sent when updating or deleting a group event also respects the triggerUserEmail and triggerOtherEmail

options, as appropriate


### Apex Reference Guide DuplicateError Class

##### triggerUserEmail

Indicates whether to trigger email that is sent to users in the organization ( `true` ) or not ( `false` ).

Signature

```
   public Boolean triggerUserEmail {get; set;}

```

Property Value

Type: Boolean

Usage

This email can be automatically triggered by a number of events; resetting a password, creating a new user, or creating or modifying a
task.

##### Note: Adding comments to a case in Apex doesn’t trigger email to users in the organization even if triggerUserEmail is

set to `true` .

Note: Email sent through Apex because of a group event includes additional behaviors. A _group event_ is an event for which
`IsGroupEvent` is true. The EventAttendee object tracks the users, leads, or contacts that are invited to a group event. Note
the following behaviors for group event email sent through Apex:

##### • Sending a group event invitation to a user respects the triggerUserEmail option • Email sent when updating or deleting a group event also respects the triggerUserEmail and triggerOtherEmail

options, as appropriate

### DuplicateError Class

Contains information about an error that occurred when an attempt was made to save a duplicate record. Use if your organization has
set up duplicate rules, which are part of the Duplicate Management feature.

Namespace

Database

Example

When you try to save a record that’s identified as a duplicate record by a duplicate rule, you’ll receive a duplicate error. If the duplicate
rule contains the Allow action, an attempt will be made to bypass the error.

```
   // Try to save a duplicate account

   Account duplicateAccount = new Account(Name='Acme', BillingCity='San Francisco');

   Database.SaveResult sr = Database.insert(duplicateAccount, false);

   if (!sr.isSuccess()) {

    // Insertion failed due to duplicate detected

    for(Database.Error duplicateError : sr.getErrors()){

     Datacloud.DuplicateResult duplicateResult =

              ((Database.DuplicateError)duplicateError).getDuplicateResult();

     System.debug('Duplicate records have been detected by ' +

```


Apex Reference Guide DuplicateError Class

```
              duplicateResult.getDuplicateRule());

     System.debug(duplicateResult.getErrorMessage());

    }

    // If the duplicate rule is an alert rule, we can try to bypass it

    Database.DMLOptions dml = new Database.DMLOptions();

    dml.DuplicateRuleHeader.AllowSave = true;

    Database.SaveResult sr2 = Database.insert(duplicateAccount, dml);

    if (sr2.isSuccess()) {

     System.debug('Duplicate account has been inserted in Salesforce!');

    }

   }

```

IN THIS SECTION:

#### DuplicateError Methods

SEE ALSO:

SaveResult Class

DuplicateResult Class

Error Class

#### DuplicateError Methods The following are methods for DuplicateError .

IN THIS SECTION:

##### getDuplicateResult()

Returns the details of a duplicate rule and duplicate records found by the duplicate rule.

getFields()
Returns an array of one or more field names. Identifies which fields in the object, if any, affected the error condition.

getMessage()
Returns the error message text.

getStatusCode()
Returns a code that characterizes the error.

##### getDuplicateResult()

Returns the details of a duplicate rule and duplicate records found by the duplicate rule.

Signature

```
   public Datacloud.DuplicateResult getDuplicateResult()

```

Return Value

Type: Datacloud.DuplicateResult


### Apex Reference Guide EmptyRecycleBinResult Class

Example

This example shows the code used to get the possible duplicates and related match information after saving a new contact. This code
is part of a custom application that implements duplicate management when users add a contact. See DuplicateResult Class on page
2695 to check out the entire sample applicaton.

```
   Datacloud.DuplicateResult duplicateResult =

                    duplicateError.getDuplicateResult();

##### getFields()

```

Returns an array of one or more field names. Identifies which fields in the object, if any, affected the error condition.

Signature

```
   public List<String> getFields()

```

Return Value

Type: List<String>

##### getMessage()

Returns the error message text.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### getStatusCode()

Returns a code that characterizes the error.

Signature

```
   public StatusCode getStatusCode()

```

Return Value

[Type: StatusCode](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

### EmptyRecycleBinResult Class

The result of the emptyRecycleBin DML operation returned by the `Database.emptyRecycleBin` method.


Apex Reference Guide EmptyRecycleBinResult Class

Namespace

Database

Usage

A list of `Database.EmptyRecycleBinResult` objects is returned by the `Database.emptyRecycleBin` method. Each
object in the list corresponds to either a record ID or an sObject passed as the parameter in the `Database.emptyRecycleBin`
method. The first index in the EmptyRecycleBinResult list matches the first record or sObject specified in the list, the second with the
second, and so on.

#### EmptyRecycleBinResult Methods The following are methods for EmptyRecycleBinResult . All are instance methods.

IN THIS SECTION:

##### getErrors()

If an error occurred during the delete for this record or sObject, returns a list of one or more Database.Error objects. If no errors
occurred, the returned list is empty.

##### getId()

Returns the ID of the record or sObject you attempted to delete.

isSuccess()
Returns `true` if the record or sObject was successfully removed from the Recycle Bin; otherwise `false` .

##### getErrors()

If an error occurred during the delete for this record or sObject, returns a list of one or more Database.Error objects. If no errors occurred,
the returned list is empty.

Signature

```
   public Database.Errors[] getErrors()

```

Return Value

Type: Database.Errors []

##### getId()

Returns the ID of the record or sObject you attempted to delete.

Signature

```
   public ID getId()

```

Return Value

Type: ID


### Apex Reference Guide Error Class

##### isSuccess()

Returns `true` if the record or sObject was successfully removed from the Recycle Bin; otherwise `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### Error Class

Represents information about an error that occurred during a DML operation when using a Database method.

Namespace

Database

Usage

### Error class is part of SaveResult, which is generated when a user attempts to save a Salesforce record.

SEE ALSO:

SaveResult Class

DuplicateError Class

#### Error Methods

### The following are methods for Error . All are instance methods.

IN THIS SECTION:

##### getFields()

Returns an array of one or more field names. Identifies which fields in the object, if any, affected the error condition.

getMessage()
Returns the error message text.

getStatusCode()
Returns a code that characterizes the error.

##### getFields()

Returns an array of one or more field names. Identifies which fields in the object, if any, affected the error condition.

Signature

```
   public String[] getFields()

```


### Apex Reference Guide GetDeletedResult Class

Return Value

Type: String[]

##### getMessage()

Returns the error message text.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### getStatusCode()

Returns a code that characterizes the error.

Signature

```
   public StatusCode getStatusCode()

```

Return Value

Type: StatusCode

Usage

The full list of status codes is available in the WSDL file for your organization (see _Downloading Salesforce WSDLs and Client Authentication_
_Certificates_ in the Salesforce online help.)

### GetDeletedResult Class

Contains the deleted records retrieved for a specific sObject type and time window.

Namespace

Database

Usage

The `Database.getDeleted` method returns the deleted record information as a `Database.GetDeletedResult` object.

#### GetDeletedResult Methods

### The following are methods for GetDeletedResult . All are instance methods.


Apex Reference Guide GetDeletedResult Class

IN THIS SECTION:

##### getDeletedRecords()

Returns a list of deleted records for the time window specified in the `Database.getDeleted` method call.

##### getEarliestDateAvailable()

Returns the date in Coordinated Universal Time (UTC) of the earliest physically deleted object for the sObject type specified in
`Database.getDeleted` .

##### getLatestDateCovered()

Returns the date in Coordinated Universal Time (UTC) of the last date covered in the `Database.getDeleted` call.

##### getDeletedRecords()

Returns a list of deleted records for the time window specified in the `Database.getDeleted` method call.

Signature

```
   public List<Database.DeletedRecord> getDeletedRecords()

```

Return Value

Type: List<Database.DeletedRecord>

##### getEarliestDateAvailable()

Returns the date in Coordinated Universal Time (UTC) of the earliest physically deleted object for the sObject type specified in
`Database.getDeleted` .

Signature

```
   public Date getEarliestDateAvailable()

```

Return Value

Type: Date

##### getLatestDateCovered()

Returns the date in Coordinated Universal Time (UTC) of the last date covered in the `Database.getDeleted` call.

Signature

```
   public Date getLatestDateCovered()

```

Return Value

Type: Date


### Apex Reference Guide GetUpdatedResult Class

Usage

If there is a value, it is less than or equal to the _`endDate`_ argument of `Database.getDeleted` . A value here indicates that, for
safety, you should use this value for the _`startDate`_ of your next call to capture the changes that started after this date but didn’t
complete before _`endDate`_ and were, therefore, not returned in the previous call.

### GetUpdatedResult Class

Contains the result for the `Database.getUpdated` method call.

Namespace

Database

Usage

Use the methods in this class to obtain detailed information about the updated records returned by `Database.getUpdated` for
a specific time window.

#### GetUpdatedResult Methods

### The following are methods for GetUpdatedResult . All are instance methods.

IN THIS SECTION:

##### getIds()

Returns the IDs of records updated within the time window specified in the `Database.getUpdated` method.

##### getLatestDateCovered()

Returns the date in Coordinated Universal Time (UTC) of the last date covered in the `Database.getUpdated` call.

##### getIds()

Returns the IDs of records updated within the time window specified in the `Database.getUpdated` method.

Signature

```
   public List<Id> getIds()

```

Return Value

Type: List<ID>

##### getLatestDateCovered()

Returns the date in Coordinated Universal Time (UTC) of the last date covered in the `Database.getUpdated` call.

Signature

```
   public Date getLatestDateCovered()

```


### Apex Reference Guide LeadConvert Class

Return Value

Type: Date

### LeadConvert Class

Contains information used for lead conversion.

Namespace

Database

Usage

The `convertLead` Database method converts a lead into an account and contact or an account and person account, as well as
(optionally) an opportunity. The `convertLead` takes an instance of the `Database.LeadConvert` class as a parameter. Create
an instance of this class and set the information required for conversion, such as setting the lead, and destination account and contact.

### Note: The Database.convertLead() method can take one LeadConvert object or a list of LeadConvert objects.

Example

This example shows how to use the `Database.convertLead` method to convert a lead. It inserts a new lead, creates a
### LeadConvert object, sets its status to converted, then passes it to the Database.convertLead method. Finally, it verifies

that the conversion was successful.

```
   Lead myLead = new Lead(LastName = 'Fry', Company='Fry And Sons');

   insert myLead;

   Database.LeadConvert lc = new Database.LeadConvert();

   lc.setLeadId(myLead.id);

   LeadStatus convertStatus = [SELECT Id, ApiName FROM LeadStatus WHERE IsConverted=true LIMIT

    1];

   lc.setConvertedStatus(convertStatus.ApiName);

   Database.LeadConvertResult lcr = Database.convertLead(lc);

   System.assert(lcr.isSuccess());

```

IN THIS SECTION:

#### LeadConvert Constructors

LeadConvert Methods

#### LeadConvert Constructors

### The following are constructors for LeadConvert .


Apex Reference Guide LeadConvert Class

IN THIS SECTION:

##### LeadConvert()

Creates a new instance of the `Database.LeadConvert` class.

##### LeadConvert()

Creates a new instance of the `Database.LeadConvert` class.

Signature

```
   public LeadConvert()

#### LeadConvert Methods

##### The following are methods for LeadConvert . All are instance methods.

```

IN THIS SECTION:

getAccountId()
Gets the ID of the account into which the lead will be merged.

getAccountRecord()
This method is for internal use only.

getBypassAccountDedupeCheck()
This method is for internal use only.

getBypassContactDedupeCheck()
This method is for internal use only.

getContactId()
Gets the ID of the contact into which the lead will be merged.

getContactRecord()
This method is for internal use only.

getConvertedStatus()
Gets the lead status value for a converted lead.

getLeadID()
Gets the ID of the lead to convert.

getOpportunityId()
Gets the ID of the existing opportunity that will be related to the resulting contact.

getOpportunityName()
Gets the name of the opportunity to create.

getOpportunityRecord()
This method is for internal use only.

getOwnerID()
Gets the ID of the person to own any newly created account, contact, and opportunity.

getRelatedPersonAccountId()
Gets the ID of the existing person account into which the lead will be converted.


Apex Reference Guide LeadConvert Class

getRelatedPersonAccountRecord()
Gets the entity record of the new person account into which the lead will be converted.

isDoNotCreateOpportunity()
Indicates whether an Opportunity is created during lead conversion ( `false`, the default) or not ( `true` ).

isOverWriteLeadSource()
Indicates whether the `LeadSource` field on the target Contact object is overwritten with the contents of the `LeadSource`
field in the source Lead object ( `true` ), or not ( `false`, the default).

isSendNotificationEmail()
Indicates whether a notification email is sent to the owner specified by `setOwnerId` ( `true` ) or not ( `false`, the default).

setAccountId(accountId)
Sets the ID of the account into which the lead is merged. This value is required only when updating an existing account, including
person accounts.

setAccountRecord(accountRecord)
This method is for internal use only.

setBypassAccountDedupeCheck(bypassAccountDedupeCheck)
This method is for internal use only.

setBypassContactDedupeCheck(bypassContactDedupeCheck)
This method is for internal use only.

setContactId(contactId)
Sets the ID of the contact into which the lead will be merged (this contact must be associated with the account specified with
`setAccountId`, and `setAccountId` must be specified). This value is required only when updating an existing contact.

setContactRecord(contactRecord)
This method is for internal use only.

setConvertedStatus(status)
Sets the lead status value for a converted lead. This field is required.

setDoNotCreateOpportunity(createOpportunity)
Specifies whether to create an opportunity during lead conversion. The default value is `false` : opportunities are created by default.
Set this flag to `true` only if you do not want to create an opportunity from the lead.

setLeadId(leadId)
Sets the ID of the lead to convert. This field is required.

setOpportunityId(opportunityId)
Sets the ID of the opportunity into which the lead is merged. This value is required only when updating an existing opportunity.

setOpportunityName(opportunityName)
Sets the name of the opportunity to create. If no name is specified, this value defaults to the company name of the lead.

setOpportunityRecord(opportunityRecord)
This method is for internal use only.

setOverwriteLeadSource(overwriteLeadSource)
Specifies whether to overwrite the `LeadSource` field on the target contact object with the contents of the `LeadSource` field
in the source lead object. The default value is `false`, to not overwrite the field. If you specify this as `true`, you must also specify
`setContactId` for the target contact.


Apex Reference Guide LeadConvert Class

setOwnerId(ownerId)
Specifies the ID of the person to own any newly created account, contact, and opportunity. If the application does not specify this
value, the owner of the new object will be the owner of the lead.

setRelatedPersonAccountId(relatedPersonAccountId)
Sets the ID of the existing person account into which to convert the lead. This value is required only when updating an existing
person account.

setSendNotificationEmail(sendEmail)
Specifies whether to send a notification email to the owner specified by `setOwnerId` . The default value is `false`, that is, to not
send email.

##### getAccountId()

Gets the ID of the account into which the lead will be merged.

Signature

```
   public ID getAccountId()

```

Return Value

Type: ID

##### **`getAccountRecord()`**

This method is for internal use only.

##### **`getBypassAccountDedupeCheck()`**

This method is for internal use only.

##### **`getBypassContactDedupeCheck()`**

This method is for internal use only.

##### getContactId()

Gets the ID of the contact into which the lead will be merged.

Signature

```
   public ID getContactId()

```

Return Value

Type: ID

##### **`getContactRecord()`**

This method is for internal use only.


Apex Reference Guide LeadConvert Class

##### getConvertedStatus()

Gets the lead status value for a converted lead.

Signature

```
   public String getConvertedStatus()

```

Return Value

Type: String

##### getLeadID()

Gets the ID of the lead to convert.

Signature

```
   public ID getLeadID()

```

Return Value

Type: ID

##### getOpportunityId()

Gets the ID of the existing opportunity that will be related to the resulting contact.

Signature

```
   public ID getOpportunityId()

```

Return Value

Type: ID

##### getOpportunityName()

Gets the name of the opportunity to create.

Signature

```
   public String getOpportunityName()

```

Return Value

Type: String

##### **`getOpportunityRecord()`**

This method is for internal use only.


Apex Reference Guide LeadConvert Class

##### getOwnerID()

Gets the ID of the person to own any newly created account, contact, and opportunity.

Signature

```
   public ID getOwnerID()

```

Return Value

Type: ID

##### getRelatedPersonAccountId()

Gets the ID of the existing person account into which the lead will be converted.

Signature

```
   public ID getRelatedPersonAccountId()

```

Return Value

Type: ID

##### getRelatedPersonAccountRecord()

Gets the entity record of the new person account into which the lead will be converted.

Signature

```
   public ID getRelatedPersonAccountRecord()

```

Return Value

Type: ID

##### isDoNotCreateOpportunity()

Indicates whether an Opportunity is created during lead conversion ( `false`, the default) or not ( `true` ).

Signature

```
   public Boolean isDoNotCreateOpportunity()

```

Return Value

Type: Boolean


Apex Reference Guide LeadConvert Class

##### isOverWriteLeadSource()

Indicates whether the `LeadSource` field on the target Contact object is overwritten with the contents of the `LeadSource` field
in the source Lead object ( `true` ), or not ( `false`, the default).

Signature

```
   public Boolean isOverWriteLeadSource()

```

Return Value

Type: Boolean

##### isSendNotificationEmail()

Indicates whether a notification email is sent to the owner specified by `setOwnerId` ( `true` ) or not ( `false`, the default).

Signature

```
   public Boolean isSendNotificationEmail()

```

Return Value

Type: Boolean

##### setAccountId(accountId)

Sets the ID of the account into which the lead is merged. This value is required only when updating an existing account, including person
accounts.

Signature

```
   public Void setAccountId(ID accountId)

```

Parameters

```
   accountId
```

Type: ID

Return Value

Type: Void

##### **`setAccountRecord(accountRecord)`**

This method is for internal use only.

##### **`setBypassAccountDedupeCheck(bypassAccountDedupeCheck)`**

This method is for internal use only.


Apex Reference Guide LeadConvert Class

##### **`setBypassContactDedupeCheck(bypassContactDedupeCheck)`**

This method is for internal use only.

##### setContactId(contactId)

Sets the ID of the contact into which the lead will be merged (this contact must be associated with the account specified with
`setAccountId`, and `setAccountId` must be specified). This value is required only when updating an existing contact.

Signature

```
   public Void setContactId(ID contactId)

```

Parameters

```
   contactId
```

Type: ID

Return Value

Type: Void

Usage

##### If setContactId is specified, then the application creates a new contact that is implicitly associated with the account. The contact

name and other existing data are not overwritten (unless `setOverwriteLeadSource` is set to true, in which case only the
`LeadSource` field is overwritten).

##### Important: If you are converting a lead into a person account, do not specify setContactId or an error will result. Specify

only `setAccountId` of the person account.

##### **`setContactRecord(contactRecord)`**

This method is for internal use only.

##### setConvertedStatus(status)

Sets the lead status value for a converted lead. This field is required.

Signature

```
   public Void setConvertedStatus(String status)

```

Parameters

```
   status
```

Type: String

Return Value

Type: Void


Apex Reference Guide LeadConvert Class

##### setDoNotCreateOpportunity(createOpportunity)

Specifies whether to create an opportunity during lead conversion. The default value is `false` : opportunities are created by default.
Set this flag to `true` only if you do not want to create an opportunity from the lead.

Signature

```
   public Void setDoNotCreateOpportunity(Boolean createOpportunity)

```

Parameters

```
   createOpportunity
```

Type: Boolean

Return Value

Type: Void

##### setLeadId(leadId)

Sets the ID of the lead to convert. This field is required.

Signature

```
   public Void setLeadId(ID leadId)

```

Parameters

```
   leadId
```

Type: ID

Return Value

Type: Void

##### setOpportunityId(opportunityId)

Sets the ID of the opportunity into which the lead is merged. This value is required only when updating an existing opportunity.

Signature

```
   public Void setOpportunityId(ID opportunityId)

```

Parameters

```
   opportunityId
```

Type: ID

Return Value

Type: Void


Apex Reference Guide LeadConvert Class

##### setOpportunityName(opportunityName)

Sets the name of the opportunity to create. If no name is specified, this value defaults to the company name of the lead.

Signature

```
   public Void setOpportunityName(String opportunityName)

```

Parameters

```
   opportunityName
```

Type: String

Return Value

Type: Void

Usage

The maximum length of this field is 80 characters.

If `setDoNotCreateOpportunity` is true, no Opportunity is created and this field must be left blank; otherwise, an error is
returned.

##### **`setOpportunityRecord(opportunityRecord)`**

This method is for internal use only.

##### setOverwriteLeadSource(overwriteLeadSource)

Specifies whether to overwrite the `LeadSource` field on the target contact object with the contents of the `LeadSource` field in
the source lead object. The default value is `false`, to not overwrite the field. If you specify this as `true`, you must also specify
`setContactId` for the target contact.

Signature

```
   public Void setOverwriteLeadSource(Boolean overwriteLeadSource)

```

Parameters

```
   overwriteLeadSource
```

Type: Boolean

Return Value

Type: Void

##### setOwnerId(ownerId)

Specifies the ID of the person to own any newly created account, contact, and opportunity. If the application does not specify this value,
the owner of the new object will be the owner of the lead.


Apex Reference Guide LeadConvert Class

Signature

```
   public Void setOwnerId(ID ownerId)

```

Parameters

```
   ownerId
```

Type: ID

Return Value

Type: Void

Usage

This method is not applicable when merging with existing objects—if `setOwnerId` is specified, the `ownerId` field is not overwritten
in an existing account or contact.

##### setRelatedPersonAccountId(relatedPersonAccountId)

Sets the ID of the existing person account into which to convert the lead. This value is required only when updating an existing person
account.

Signature

```
   public Void setRelatedPersonAccountId(ID relatedPersonAccountId)

```

Parameters

```
   relatedPersonAccountId
```

Type: ID

Return Value

Type: Void

##### setSendNotificationEmail(sendEmail)

Specifies whether to send a notification email to the owner specified by `setOwnerId` . The default value is `false`, that is, to not
send email.

Signature

```
   public Void setSendNotificationEmail(Boolean sendEmail)

```

Parameters

```
   sendEmail
```

Type: Boolean


### Apex Reference Guide LeadConvertResult Class

Return Value

Type: Void

### LeadConvertResult Class

The result of a lead conversion.

Namespace

Database

Usage

An array of LeadConvertResult objects is returned with the `convertLead` Database method. Each element in the LeadConvertResult
array corresponds to the sObject array passed as the _`SObject[]`_ parameter in the `convertLead` Database method, that is, the
first element in the LeadConvertResult array matches the first element passed in the SObject array, the second element corresponds to
the second element, and so on. If only one sObject is passed in, the LeadConvertResult array contains a single element.

#### LeadConvertResult Methods

### The following are methods for LeadConvertResult . All are instance methods.

IN THIS SECTION:

##### getAccountId()

The ID of the new account (if a new account was specified) or the ID of the account specified when `convertLead` was invoked.

getContactId()
The ID of the new contact (if a new contact was specified) or the ID of the contact specified when `convertLead` was invoked.

getErrors()
If an error occurred, an array of one or more database error objects providing the error code and description.

getLeadId()
The ID of the converted lead.

getOpportunityId()
The ID of the new opportunity, if one was created when `convertLead` was invoked.

getRelatedPersonAccountId()
The ID of the new or existing person account specified when `convertLead` was invoked.

isSuccess()
A Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise

##### getAccountId()

The ID of the new account (if a new account was specified) or the ID of the account specified when `convertLead` was invoked.

Signature

```
   public ID getAccountId()

```


Apex Reference Guide LeadConvertResult Class

Return Value

Type: ID

##### getContactId()

The ID of the new contact (if a new contact was specified) or the ID of the contact specified when `convertLead` was invoked.

Signature

```
   public ID getContactId()

```

Return Value

Type: ID

##### getErrors()

If an error occurred, an array of one or more database error objects providing the error code and description.

Signature

```
   public Database.Error[] getErrors()

```

Return Value

Type: Database.Error[]

##### getLeadId()

The ID of the converted lead.

Signature

```
   public ID getLeadId()

```

Return Value

Type: ID

##### getOpportunityId()

The ID of the new opportunity, if one was created when `convertLead` was invoked.

Signature

```
   public ID getOpportunityId()

```

Return Value

Type: ID


### Apex Reference Guide MergeResult Class

##### getRelatedPersonAccountId()

The ID of the new or existing person account specified when `convertLead` was invoked.

Signature

```
   public ID getRelatedPersonAccountId()

```

Return Value

Type: ID

##### isSuccess()

A Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### MergeResult Class

Contains the result of a merge Database method operation.

Namespace

Database

Usage

The `Database.merge` method returns a `Database.MergeResult` object for each merged record.

#### MergeResult Methods

### The following are methods for MergeResult . All are instance methods.

IN THIS SECTION:

getErrors()
Returns a list of `Database.Error` objects representing the errors encountered, if any, during a merge operation using the
`Database.merge` method. If no error occurred, returns null.

getId()
Returns the ID of the master record into which other records were merged.

getMergedRecordIds()
Returns the IDs of the records merged into the master record.


Apex Reference Guide MergeResult Class

##### getUpdatedRelatedIds()

Returns the IDs of all related records that were reparented as a result of the merge that are viewable by the user sending the merge
call.

isSuccess()
Indicates whether the merge was successful ( `true` ) or not ( `false` ).

##### getErrors()

Returns a list of `Database.Error` objects representing the errors encountered, if any, during a merge operation using the
`Database.merge` method. If no error occurred, returns null.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getId()

Returns the ID of the master record into which other records were merged.

Signature

```
   public Id getId()

```

Return Value

Type: ID

##### getMergedRecordIds()

Returns the IDs of the records merged into the master record.

Signature

```
   public List<String> getMergedRecordIds()

```

Return Value

Type: List<String>

##### getUpdatedRelatedIds()

Returns the IDs of all related records that were reparented as a result of the merge that are viewable by the user sending the merge call.

Signature

```
   public List<String> getUpdatedRelatedIds()

```


### Apex Reference Guide PaginationCursor Class

Return Value

Type: List<String>

##### isSuccess()

Indicates whether the merge was successful ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### PaginationCursor Class

This class represents a pagination cursor that can traverse a SOQL query result set. It contains methods that fetch rows by page. It also
contains a method that returns the total number of rows in the result set.

Namespace

Database

Usage

A pagination cursor is created when a SOQL query is executed on a `Database.getPaginationCursor()` on page 3651 or a
`Database.getPaginationCursorWithBinds()` on page 3652 call. When the SOQL query is invoked, the corresponding
rows are returned from the pagination cursor.

Use a pagination cursor for traversing human-viewable data, such as a list of records in a UI. The maximum number of rows per pagination
cursor is 100,000, regardless of whether the operation is synchronous or asynchronous.

[For a comparison between pagination cursors and standard cursors, see Apex Cursors in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cursors.htm) _Apex Developer Guide_ .

[For Apex pagination cursor limits, see Execution Governors and Limits in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm) _Apex Developer Guide_ .

IN THIS SECTION:

#### PaginationCursor Methods PaginationCursor Methods

### The following are methods for PaginationCursor .

IN THIS SECTION:

fetchDeleted(start, pageSize)
Fetches the number of deleted rows within the specified range. The method counts only rows deleted after the creation of the
pagination cursor. Calling the `PaginationCursor.fetchDeleted()` method counts against the SOQL query limit, and
the rows fetched count against the SOQL query row limit.


Apex Reference Guide PaginationCursor Class

##### fetchPage(start, pageSize)

Fetches a page of rows from the result set. By default, the method skips rows deleted after the creation of the pagination cursor. The
method also returns information used to fetch the next page. Calling the `PaginationCursor.fetchPage()` method
counts against the SOQL query limit, and the rows fetched count against the SOQL query row limit.

getNumRecords()
Gets the total number of rows in the SOQL query result set.

##### **`fetchDeleted(start, pageSize)`**

Fetches the number of deleted rows within the specified range. The method counts only rows deleted after the creation of the pagination
cursor. Calling the `PaginationCursor.fetchDeleted()` method counts against the SOQL query limit, and the rows fetched
count against the SOQL query row limit.

Signature

```
   public Integer fetchDeleted(Integer start, Integer pageSize)

```

Parameters

```
   start
```

Type: Integer

The zero-based index from which to begin checking for deleted rows.

```
   pageSize
```

Type: Integer

The number of rows to check, beginning at the _`start`_ index.

Return Value

Type: Integer

##### **`fetchPage(start, pageSize)`**

Fetches a page of rows from the result set. By default, the method skips rows deleted after the creation of the pagination cursor. The
method also returns information used to fetch the next page. Calling the `PaginationCursor.fetchPage()` method counts
against the SOQL query limit, and the rows fetched count against the SOQL query row limit.

Signature

```
   public Database.CursorFetchResult fetchPage(Integer start, Integer pageSize)

```

Parameters

```
   start
```

Type: Integer

The zero-based index from which to begin fetching rows.

```
   pageSize
```

Type: Integer


### Apex Reference Guide QueryLocator Class

The maximum number of rows to include on the current page.

Return Value

Type: Database.CursorFetchResult on page 2646

Contains the rows for the current page and the information used to fetch the next page.

##### **`getNumRecords()`**

Gets the total number of rows in the SOQL query result set.

Signature

```
   public Integer getNumRecords()

```

Return Value

Type: Integer

SEE ALSO:

getPaginationCursor(query, accessLevel)

CursorFetchResult Class

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_cursors.htm)_ : Apex Cursors

### QueryLocator Class

Represents the record set returned by `Database.getQueryLocator` and used with Batch Apex.

Namespace

Database

#### QueryLocator Methods

### The following are methods for QueryLocator . All are instance methods.

IN THIS SECTION:

##### getQuery()

Returns the query used to instantiate the `Database.QueryLocator` object. This is useful when testing the `start` method.

iterator()
Returns a new instance of a query locator iterator.

##### getQuery()

Returns the query used to instantiate the `Database.QueryLocator` object. This is useful when testing the `start` method.


### Apex Reference Guide QueryLocatorIterator Class

Signature

```
   public String getQuery()

```

Return Value

[Type: String](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_string.htm)

Usage

You can’t use the `[FOR UPDATE](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_locking_statements.htm)` keywords with a getQueryLocator query to lock a set of records. The set of records in the batch is
determined when the `start` method is run.

Example

```
   System.assertEquals(QLReturnedFromStart.

   getQuery(),

   Database.getQueryLocator([SELECT Id

     FROM Account]).getQuery() );

##### iterator()

```

Returns a new instance of a query locator iterator.

Signature

```
   public Database.QueryLocatorIterator iterator()

```

Return Value

Type: Database.QueryLocatorIterator

Usage

Warning: To iterate over a query locator, save the iterator instance that this method returns in a variable and then use this variable
##### to iterate over the collection. Calling iterator every time you want to perform an iteration can result in incorrect behavior

because each call returns a new iterator instance.

For an example, see QueryLocatorIterator Class.

### QueryLocatorIterator Class

Represents an iterator over a query locator record set.

Namespace

Database


Apex Reference Guide QueryLocatorIterator Class

Example

##### This sample shows how to obtain an iterator for a query locator, which contains five accounts. This sample calls hasNext and next

to get each record in the collection.

```
   // Get a query locator

   Database.QueryLocator q = Database.getQueryLocator(

      [SELECT Name FROM Account LIMIT 5]);

   // Get an iterator

   Database.QueryLocatorIterator it = q.iterator();

   // Iterate over the records

   while (it.hasNext())

   {

      Account a = (Account)it.next();

      System.debug(a);

   }

#### QueryLocatorIterator Methods The following are methods for QueryLocatorIterator . All are instance methods.

```

IN THIS SECTION:

##### hasNext()

Returns `true` if there are one or more records remaining in the collection; otherwise, returns `false` .

##### next()

Advances the iterator to the next sObject record and returns the sObject.

##### hasNext()

Returns `true` if there are one or more records remaining in the collection; otherwise, returns `false` .

Signature

```
   public Boolean hasNext()

```

Return Value

Type: Boolean

##### next()

Advances the iterator to the next sObject record and returns the sObject.

Signature

```
   public sObject next()

```


### Apex Reference Guide SaveResult Class

Return Value

Type: sObject

Usage

Because the return value is the generic sObject type, you must cast it if using a more specific type. For example:

```
   Account a = (Account)myIterator.next();

```

Example

```
   Account a = (Account)myIterator.next();

### SaveResult Class

```

The result of an insert or update DML operation returned by a Database method.

Namespace

Database

Usage

An array of SaveResult objects is returned with the `insert` and `update` database methods. Each element in the SaveResult array
corresponds to the sObject array passed as the _`sObject[]`_ parameter in the Database method, that is, the first element in the
SaveResult array matches the first element passed in the sObject array, the second element corresponds with the second element, and
so on. If only one sObject is passed in, the SaveResult array contains a single element.

A SaveResult object is generated when a new or existing Salesforce record is saved.

Example

The following example shows how to obtain and iterate through the returned `Database.SaveResult` objects. It inserts two
accounts using `Database.insert` with a false second parameter to allow partial processing of records on failure. One of the
accounts is missing the Name required field, which causes a failure. Next, it iterates through the results to determine whether the
operation was successful or not for each record. It writes the ID of every record that was processed successfully to the debug log, or error
messages and fields of the failed records. This example generates one successful operation and one failure.

```
   // Create two accounts, one of which is missing a required field

   Account[] accts = new List<Account>{

      new Account(Name='Account1'),

      new Account()};

   Database.SaveResult[] srList = Database.insert(accts, false);

   // Iterate through each returned result

   for (Database.SaveResult sr : srList) {

      if (sr.isSuccess()) {

        // Operation was successful, so get the ID of the record that was processed

        System.debug('Successfully inserted account. Account ID: ' + sr.getId());

      }

```


Apex Reference Guide SaveResult Class

```
      else {

        // Operation failed, so get all errors

        for(Database.Error err : sr.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Account fields that affected this error: ' + err.getFields());

        }

      }

   }

```

SEE ALSO:

Error Class

DuplicateError Class

#### SaveResult Methods The following are methods for SaveResult . All are instance methods.

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error
occurred, returns an empty set.

##### getId()

Returns the ID of the sObject you were trying to insert or update.

isSuccess()
Returns a Boolean that is set to `true` if the DML operation was successful for this object, `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error occurred,
returns an empty set.

Signature

```
   public Database.Error[] getErrors()

```

Return Value

Type: Database.Error[]

##### getId()

Returns the ID of the sObject you were trying to insert or update.

Signature

```
   public ID getId()

```


### Apex Reference Guide UndeleteResult Class

Return Value

Type: ID

Versioned Behavior Changes

In API version 53.0 and later, the method returns the sObject ID. However, if record locking fails during the update operation, the method
returns a null value.

In API version 52.0 and earlier, the method returned a null value if the record wasn’t updated successfully.

##### isSuccess()

Returns a Boolean that is set to `true` if the DML operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

Example

This example shows the code used to process duplicate records, which are detected when there is an unsuccessful save due to an error.
This code is part of a custom application that implements duplicate management when users add a contact. See DuplicateResult Class
on page 2695 to check out the entire sample applicaton.

```
   if (!saveResult.isSuccess()) { ... }

### UndeleteResult Class

```

The result of an undelete DML operation returned by the `Database.undelete` method.

Namespace

Database

Usage

An array of Database.UndeleteResult objects is returned with the `undelete` database method. Each element in the UndeleteResult
array corresponds to the sObject array passed as the _`sObject[]`_ parameter in the `undelete` Database method; that is, the first
element in the UndeleteResult array matches the first element passed in the sObject array, the second element corresponds with the
second element, and so on. If only one sObject is passed in, the UndeleteResults array contains a single element.

#### UndeleteResult Methods

### The following are methods for UndeleteResult . All are instance methods.


Apex Reference Guide UndeleteResult Class

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error
occurred, returns null.

##### getId()

Returns the ID of the sObject you were trying to undelete.

##### isSuccess()

Returns a Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error occurred,
returns null.

Signature

```
   public Database.Error[] getErrors()

```

Return Value

Type: Database.Error[]

##### getId()

Returns the ID of the sObject you were trying to undelete.

Signature

```
   public ID getId()

```

Return Value

Type: ID

Usage

If this field contains a value, the object was successfully undeleted. If this field is empty, the operation was not successful for that object.

##### isSuccess()

Returns a Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean


### Apex Reference Guide UpsertResult Class UpsertResult Class

The result of an upsert DML operation returned by the `Database.upsert` method.

Namespace

Database

Usage

An array of Database.UpsertResult objects is returned with the `upsert` database method. Each element in the UpsertResult array
corresponds to the sObject array passed as the _`sObject[]`_ parameter in the `upsert` Database method; that is, the first element
in the UpsertResult array matches the first element passed in the sObject array, the second element corresponds with the second element,
and so on. If only one sObject is passed in, the UpsertResults array contains a single element.

#### UpsertResult Methods

### The following are methods for UpsertResult . All are instance methods.

IN THIS SECTION:

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error
occurred, returns an empty set.

##### getId()

Returns the ID of the sObject you were trying to update or insert.

isCreated()
A Boolean value that is set to `true` if the record was created, `false` if the record was updated.

isSuccess()
Returns a Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

##### getErrors()

If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error occurred,
returns an empty set.

Signature

```
   public Database.Error[] getErrors()

```

Return Value

Type: Database.Error []

##### getId()

Returns the ID of the sObject you were trying to update or insert.


## Apex Reference Guide Datacloud Namespace

Signature

```
   public ID getId()

```

Return Value

Type: ID

Versioned Behavior Changes

In API version 53.0 and later, the method returns the sObject ID. However, if record locking fails during the update operation, the method
returns a null value.

In API version 52.0 and earlier, the method returned a null value if the record wasn’t updated successfully.

##### isCreated()

A Boolean value that is set to `true` if the record was created, `false` if the record was updated.

Signature

```
   public Boolean isCreated()

```

Return Value

Type: Boolean

##### isSuccess()

Returns a Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

## Datacloud Namespace The Datacloud namespace provides classes and methods for retrieving information about duplicate rules. Duplicate rules let you

control whether and when users can save duplicate records within Salesforce.

## The Datacloud namespace is related to the Duplicate Management feature. For more information, see Manage Duplicate Records in Salesforce Help and Duplicate Management in Trailhead. The Datacloud namespace isn’t related to the Salesforce Data Cloud

[product. See Data Cloud.](https://www.salesforce.com/products/data/)

## The following are the classes in the Datacloud namespace.


### Apex Reference Guide AdditionalInformationMap Class

IN THIS SECTION:

### AdditionalInformationMap Class

Represents other information, if any, about matched records.

DuplicateResult Class
Represents the details of a duplicate rule that detected duplicate records and information about those duplicate records.

FieldDiff Class
Represents the name of a matching rule field and how the values of the field compare for the duplicate and its matching record.

FindDuplicates Class
Performs rule-based searches for duplicate records. The input is an array of sObjects. Each sObject represents a record you want to
find duplicates of. The output identifies the detected duplicates for each input sObject based on active duplicate rules for the given
object.

FindDuplicatesByIds Class
Performs rule-based searches for duplicate records. The input is an array of IDs. Each ID specifies records to search for duplicates
among. The duplicates are detected based on the active duplicate rules applicable to the object type corresponding to the input
IDs.

FindDuplicatesResult Class
Output for rule-based searches for duplicate records. `FindDuplicatesResult` contains results of detecting duplicates using
instances of `FindDuplicates` or `FindDuplicatesByIds` classes.

MatchRecord Class
Represents a duplicate record detected by a matching rule.

MatchResult Class
Represents the duplicate results for a matching rule.

### AdditionalInformationMap Class

Represents other information, if any, about matched records.

Namespace

Datacloud

IN THIS SECTION:

#### AdditionalInformationMap Methods AdditionalInformationMap Methods

### The following are methods for AdditionalInformationMap .

IN THIS SECTION:

getName()
Returns the element name.

getValue()
Returns the value of the element.


### Apex Reference Guide DuplicateResult Class

##### getName()

Returns the element name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getValue()

Returns the value of the element.

Signature

```
   public String getValue()

```

Return Value

Type: String

### DuplicateResult Class

Represents the details of a duplicate rule that detected duplicate records and information about those duplicate records.

Namespace

Datacloud

Usage

### The DuplicateResult class and its methods are available to organizations that use duplicate rules. DuplicateResult is contained within DuplicateError, which is part of SaveResult . SaveResult is generated when

a user attempts to save a record in Salesforce.

Example

This example shows a custom application that lets users add a contact. When a contact is saved, an alert displays if there are duplicate
records.

The sample application consists of a Visualforce page and an Apex controller. The Visualforce page is listed first so that you can see how
the page makes use of the Apex controller. Save the Apex class first before saving the Visualforce page.

```
   <apex:page controller="ContactDedupeController">

      <apex:form >

        <apex:pageBlock title="Duplicate Records" rendered="{!hasDuplicateResult}">

           <apex:pageMessages />

           <apex:pageBlockTable value="{!duplicateRecords}" var="item">

```


Apex Reference Guide DuplicateResult Class

```
             <apex:column >

               <apex:facet name="header">Name</apex:facet>

              <apex:outputLink value="/{!item['Id']}">{!item['Name']}</apex:outputLink>

             </apex:column>

             <apex:column >

               <apex:facet name="header">Owner</apex:facet>

               <apex:outputField value="{!item['OwnerId']}"/>

             </apex:column>

             <apex:column >

               <apex:facet name="header">Last Modified Date</apex:facet>

               <apex:outputField value="{!item['LastModifiedDate']}"/>

             </apex:column>

           </apex:pageBlockTable>

        </apex:pageBlock>

        <apex:pageBlock title="Contact" mode="edit">

           <apex:pageBlockButtons >

             <apex:commandButton value="Save" action="{!save}"/>

           </apex:pageBlockButtons>

           <apex:pageBlockSection >

             <apex:inputField value="{!Contact.FirstName}"/>

             <apex:inputField value="{!Contact.LastName}"/>

             <apex:inputField value="{!Contact.Email}"/>

             <apex:inputField value="{!Contact.Phone}"/>

             <apex:inputField value="{!Contact.AccountId}"/>

           </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

This sample is the Apex controller for the page. This controller contains the action method for the Save button. The `save` method
inserts the new contact. If errors are returned, this method iterates through each error, checks if it’s a duplicate error, adds the error
message to the page, and returns information about the duplicate records to be displayed on the page.

```
   public class ContactDedupeController {

      // Initialize a variable to hold the contact record you're processing

      private final Contact contact;

      // Initialize a list to hold any duplicate records

      private List<sObject> duplicateRecords;

      // Define variable that’s true if there are duplicate records

      public boolean hasDuplicateResult{get;set;}

      // Define the constructor

      public ContactDedupeController() {

        // Define the values for the contact you’re processing based on its ID

        Id id = ApexPages.currentPage().getParameters().get('id');

        this.contact = (id == null) ? new Contact() :

           [SELECT Id, FirstName, LastName, Email, Phone, AccountId

           FROM Contact WHERE Id = :id];

```


Apex Reference Guide DuplicateResult Class

```
        // Initialize empty list of potential duplicate records

        this.duplicateRecords = new List<sObject>();

        this.hasDuplicateResult = false;

      }

      // Return contact and its values to the Visualforce page for display

      public Contact getContact() {

        return this.contact;

      }

      // Return duplicate records to the Visualforce page for display

      public List<sObject> getDuplicateRecords() {

        return this.duplicateRecords;

      }

      // Process the saved record and handle any duplicates

      public PageReference save() {

        // Optionally, set DML options here, use “DML” instead of “false”

        // in the insert()

        // Database.DMLOptions dml = new Database.DMLOptions();

        // dml.DuplicateRuleHeader.allowSave = true;

        // dml.DuplicateRuleHeader.runAsCurrentUser = true;

        Database.SaveResult saveResult = Database.insert(contact, false);

        if (!saveResult.isSuccess()) {

           for (Database.Error error : saveResult.getErrors()) {

             // If there are duplicates, an error occurs

             // Process only duplicates and not other errors

             // (e.g., validation errors)

             if (error instanceof Database.DuplicateError) {

               // Handle the duplicate error by first casting it as a

               // DuplicateError class

               // This lets you use methods of that class

               // (e.g., getDuplicateResult())

               Database.DuplicateError duplicateError =

                    (Database.DuplicateError)error;

               Datacloud.DuplicateResult duplicateResult =

                    duplicateError.getDuplicateResult();

               // Display duplicate error message as defined in the duplicate rule

               ApexPages.Message errorMessage = new ApexPages.Message(

                    ApexPages.Severity.ERROR, 'Duplicate Error: ' +

                    duplicateResult.getErrorMessage());

               ApexPages.addMessage(errorMessage);

               // Get duplicate records

               this.duplicateRecords = new List<sObject>();

               // Return only match results of matching rules that

               // find duplicate records

               Datacloud.MatchResult[] matchResults =

                    duplicateResult.getMatchResults();

```


Apex Reference Guide DuplicateResult Class

```
               // Just grab first match result (which contains the

               // duplicate record found and other match info)

               Datacloud.MatchResult matchResult = matchResults[0];

               Datacloud.MatchRecord[] matchRecords = matchResult.getMatchRecords();

               // Add matched record to the duplicate records variable

               for (Datacloud.MatchRecord matchRecord : matchRecords) {

                  System.debug('MatchRecord: ' + matchRecord.getRecord());

                  this.duplicateRecords.add(matchRecord.getRecord());

               }

               this.hasDuplicateResult = !this.duplicateRecords.isEmpty();

             }

           }

           //If there’s a duplicate record, stay on the page

           return null;

        }

        // After save, navigate to the view page:

        return (new ApexPages.StandardController(contact)).view();

      }

   }

```

IN THIS SECTION:

#### DuplicateResult Methods

SEE ALSO:

SaveResult Class

DuplicateError Class

#### DuplicateResult Methods The following are methods for DuplicateResult .

IN THIS SECTION:

getDuplicateRule()
Returns the developer name of the executed duplicate rule that returned duplicate records.

getErrorMessage()
Returns the error message configured by the administrator to warn users they may be creating duplicate records. This message is
associated with a duplicate rule.

getMatchResults()
Returns the duplicate records and match information.


Apex Reference Guide DuplicateResult Class

isAllowSave()
Indicates whether the duplicate rule will allow a record that’s identified as a duplicate to be saved. Set to `true` if duplicate rule
should allow save; otherwise, `false` .

##### getDuplicateRule()

Returns the developer name of the executed duplicate rule that returned duplicate records.

Signature

```
   public String getDuplicateRule()

```

Return Value

Type: String

##### getErrorMessage()

Returns the error message configured by the administrator to warn users they may be creating duplicate records. This message is
associated with a duplicate rule.

Signature

```
   public String getErrorMessage()

```

Return Value

Type: String

Example

This example shows the code used to display the error message when duplicates are found while saving a new contact. This code is part
of a custom application that lets users add a contact. When a contact is saved, an alert displays if there are duplicate records. Review
DuplicateResult Class on page 2695 to check out the entire sample applicaton.

```
   ApexPages.Message errorMessage = new ApexPages.Message(

                    ApexPages.Severity.ERROR, 'Duplicate Error: ' +

                    duplicateResult.getErrorMessage());

               ApexPages.addMessage(errorMessage);

##### getMatchResults()

```

Returns the duplicate records and match information.

Signature

```
   public List<Datacloud.MatchResult> getMatchResults()

```

Return Value

Type: List<Datacloud.MatchResult>


### Apex Reference Guide FieldDiff Class

Example

This example shows the code used to return duplicate record and match information and assign it to the `matchResults` variable.
This code is part of a custom application that implements duplicate management when users add a contact. See DuplicateResult Class
on page 2695 to check out the entire sample applicaton.

```
   Datacloud.MatchResult[] matchResults =

                    duplicateResult.getMatchResults();

##### isAllowSave()

```

Indicates whether the duplicate rule will allow a record that’s identified as a duplicate to be saved. Set to `true` if duplicate rule should
allow save; otherwise, `false` .

Signature

```
   public Boolean isAllowSave()

```

Return Value

Type: Boolean

### FieldDiff Class

Represents the name of a matching rule field and how the values of the field compare for the duplicate and its matching record.

Namespace

Datacloud

IN THIS SECTION:

#### FieldDiff Methods FieldDiff Methods

### The following are methods for FieldDiff .

IN THIS SECTION:

##### getDifference()

Returns how the field values compare for the duplicate and its matching record.

getName()
Returns the name of a field on a matching rule that detected duplicates.

##### getDifference()

Returns how the field values compare for the duplicate and its matching record.


### Apex Reference Guide FindDuplicates Class

Signature

```
   public String getDifference()

```

Return Value

Type: String

Possible values include:

**•** `SAME` : Indicates the field values match exactly.

**•** `DIFFERENT` : Indicates that the field values do not match.

**•** `NULL` : Indicates that the field values are a match because both values are blank.

##### getName()

Returns the name of a field on a matching rule that detected duplicates.

Signature

```
   public String getName()

```

Return Value

Type: String

### FindDuplicates Class

Performs rule-based searches for duplicate records. The input is an array of sObjects. Each sObject represents a record you want to find
duplicates of. The output identifies the detected duplicates for each input sObject based on active duplicate rules for the given object.

Namespace

Datacloud

IN THIS SECTION:

#### FindDuplicates Methods FindDuplicates Methods

### The following are methods for FindDuplicates .

IN THIS SECTION:

##### findDuplicates(sObjects)

Identifies duplicates for sObjects provided and returns a list of `FindDuplicatesResult` objects.

##### findDuplicates(sObjects)

Identifies duplicates for sObjects provided and returns a list of `FindDuplicatesResult` objects.


Apex Reference Guide FindDuplicates Class

Usage

Use `FindDuplicates` to apply active duplicate rules associated with an object to records represented by input sObjects.

`FindDuplicates` uses the duplicate rules for the object that has the same type as the input sObjects.

This method doesn’t return custom fields by default. This method identifies duplicate records according to activated standard and custom
matching rules. Standard matching rules don’t include custom fields in their matching criteria. You can configure custom matching rules
[that do include custom fields for matching criteria, and then assign the custom matching rule to a duplicate rule. However, configuring](https://help.salesforce.com/s/articleView?id=sales.duplicate_rules_map_of_reference.htm&type=5&language=en_US)
these rules isn’t a part of the Datacloud API.

**Input**

**•** All sObjects in the input array must be of the same object type, and that type must correspond to an object type that supports
duplicate rules.

**•** The input array is limited to 50 elements. If you exceed this limit, an exception is thrown with the following message:

```
      Configuration error: The number of records to check is greater than the permitted

      batch size.

```

**Output**

**•** The output of `FindDuplicates` is an array of objects with the same number of elements as the input array, and in the same
order. The output objects encapsulate record IDs for duplicate records. The output objects also contain values from the duplicate
records.

**•** Each element contains an array of `DuplicateResult` on page 2695 objects, which each represent a duplicate rule that
`FindDuplicates` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2711 objects,
which each represent a matching rule that the duplicate rule applied. If `FindDuplicates` doesn’t find any duplicates for
that matching rule, then the `MatchResult.getMatchRecords()` on page 2712 array is empty. Otherwise, the
`MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2709 elements, which each represent a
duplicate record.

**•** If no duplicate rule is active for the object type in the input array, a `System.HandledException` exception is thrown
with this message: `No active duplicate rules are defined for the {ObjectName} object`
`type` .

Example

```
   //Create the sObject to check for duplicates.

   Account acct = new Account();

   acct.Name = 'Test Account 123';

   acct.BillingStreet = '123 Test Street';

   acct.BillingCity = 'San Francisco';

   acct.BillingState = 'CA';

   acct.BillingCountry = 'US';

   List<Account> acctList = new List<Account>();

   acctList.add(acct);

   // Call the findDuplicates method, which returns one FindDuplicatesResult for each sObject

    in the input list.

   List<Datacloud.FindDuplicatesResult> results =

   Datacloud.FindDuplicates.findDuplicates(acctList);

   //Get the result for the first record (index 0).

   Datacloud.FindDuplicatesResult acctResult = results[0];

```


Apex Reference Guide FindDuplicates Class

```
   // Check that findDuplicates() was successfully executed for this account.

   if (!acctResult.isSuccess()) {

     List<Database.Error> errs = acctResult.getErrors();

     for (Database.Error err : errs) {

       System.debug(err.getMessage());

     }

   } else {

     Boolean duplicatesFound = false;

     Boolean matchError = false;

     // Iterate through the duplicate rules that were evaluated.

     for (Datacloud.DuplicateResult dupResult : acctResult.getDuplicateResults()) {

      // Iterate through the matching rules that were evaluated for each duplicate rule.

      for (Datacloud.MatchResult matchResult : dupResult.getMatchResults()) {

       // Check that getMatchResults() was successfully executed for this matching rule.

       if (!matchResult.isSuccess()) {

        List<Database.Error> errs = matchResult.getErrors();

        for (Database.Error err : errs) {

         System.debug(err.getMessage());

        }

        matchError = true;

       } else {

        // Check if duplicates are found according to the matching rule.

        if (!matchResult.getMatchRecords().isEmpty()) {

         System.debug('Duplicate record(s) found with matching rule: ' +

   matchResult.getRule());

         duplicatesFound = true;

         // Get information about the duplicates.

         for (Datacloud.MatchRecord matchRecord : matchResult.getMatchRecords()) {

           System.debug('Duplicate record: ' + matchRecord.getRecord());

         }

        }

       }

      }

     }

     // Insert the record only if no duplicates were found and no errors occurred.

     if (!duplicatesFound && !matchError) {

      insert(acct);

      System.debug('Account inserted.');

     }

   }

```

Signature

```
   public static List<Datacloud.FindDuplicatesResult> findDuplicates(List<SObject> sObjects)

```

Parameters

```
   sObjects
```

Type: List<SObject>


### Apex Reference Guide FindDuplicatesByIds Class

An array of sObjects for which you want to find duplicates.

Return Value

Type: List<FindDuplicatesResult>

### FindDuplicatesByIds Class

Performs rule-based searches for duplicate records. The input is an array of IDs. Each ID specifies records to search for duplicates among.
The duplicates are detected based on the active duplicate rules applicable to the object type corresponding to the input IDs.

Namespace

Datacloud

IN THIS SECTION:

#### FindDuplicatesByIds Methods FindDuplicatesByIds Methods

### The following are methods for FindDuplicatesByIds .

IN THIS SECTION:

##### findDuplicatesByIds(ids)

Identifies duplicates of record IDs provided and returns a list of `FindDuplicatesResult` objects.

##### **`findDuplicatesByIds(ids)`**

Identifies duplicates of record IDs provided and returns a list of `FindDuplicatesResult` objects.

Usage

### FindDuplicatesByIds uses the duplicate rules for the object that has the same type as the input record IDs. For example, if the record ID represents an Account, FindDuplicatesByIds uses the duplicate rules associated with the Account object. FindDuplicatesByIds identifies duplicate records according to activated standard and custom matching rules. Standard matching

[rules don’t include custom fields in their matching criteria. You can configure custom matching rules that do include custom fields for](https://help.salesforce.com/s/articleView?id=sales.matching_rules_standard_rules.htm&language=en_US&type=5)
[matching criteria, and then assign the custom matching rule to a duplicate rule. However, configuring these rules isn’t a part of the](https://help.salesforce.com/s/articleView?id=sales.duplicate_rules_map_of_reference.htm&type=5&language=en_US)
Datacloud API.

**Input**

**•** All record IDs in the input array must be of the same object type, and that type must correspond to an object type that supports
duplicate rules.

**•** The input array is limited to 50 elements. If you exceed this limit, an exception is thrown with the following message:

```
      Configuration error: The number of records to check is greater than the permitted

      batch size.

```


Apex Reference Guide FindDuplicatesByIds Class

**Output**

**•** The output of `FindDuplicatesByIds` is an array of objects with the same number of elements as the input array, and in
the same order. The output objects encapsulate record IDs for duplicate records. The output objects also contain values from
the duplicate records.

**•** Each element contains an array of `DuplicateResult` on page 2695 objects, which each represent a duplicate rule that
`FindDuplicatesByIds` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2711
objects, which each represent a matching rule that the duplicate rule applied. If `FindDuplicatesByIds` doesn’t find any
duplicates for that matching rule, then the `MatchResult.getMatchRecords()` on page 2712 array is empty. Otherwise,
the `MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2709 objects, which each represent
a duplicate record.

**•** If no duplicate rule is active for the object type of the record IDs in the input array, a `System.HandledException`
exception is thrown with this message: `No active duplicate rules are defined for the {ObjectName}`
`object type` .

Example

```
   // Create list of existing record IDs to check for duplicates

   List<Id> idList = new List<Id>();

   idList.add(' EXISTING_ID '); // Replace placeholder with an existing 18-digit record ID

   // Call the FindDuplicatesByIds method, which returns one FindDuplicatesResult for each

   ID in the input list.

   List<Datacloud.FindDuplicatesResult> results =

   Datacloud.FindDuplicatesByIds.findDuplicatesByIds(idList);

   //Get the result for the first record ID (index 0).

   Datacloud.FindDuplicatesResult idResult = results[0];

   // Check that findDuplicates() was successfully executed for this record

   if (!idResult.isSuccess()) {

     List<Database.Error> errs = idResult.getErrors();

     for (Database.Error err : errs) {

       System.debug(err.getMessage());

     }

   } else {

     Boolean duplicatesFound = false;

     Boolean matchError = false;

     // Iterate through the duplicate rules that were evaluated.

     for (Datacloud.DuplicateResult dupResult : idResult.getDuplicateResults()) {

      // Iterate through the matching rules that were evaluated for each duplicate rule

      for (Datacloud.MatchResult matchResult : dupResult.getMatchResults()) {

       // Check that getMatchResults() was successfully executed for this matching rule

       if (!matchResult.isSuccess()) {

        List<Database.Error> errs = matchResult.getErrors();

        for (Database.Error err : errs) {

         System.debug(err.getMessage());

        }

        matchError = true;

       } else {

```


### Apex Reference Guide FindDuplicatesResult Class

```
        // Check if duplicates are found according to the matching rule

        if (!matchResult.getMatchRecords().isEmpty()) {

         System.debug('Duplicate record(s) found with matching rule: ' +

   matchResult.getRule());

         duplicatesFound = true;

         // Get information about the duplicates

         for (Datacloud.MatchRecord matchRecord : matchResult.getMatchRecords()) {

           System.debug('Duplicate record: ' + matchRecord.getRecord());

         }

        }

       }

      }

     }

     // If no duplicates were found and no errors occurred for first record ID

     if (!duplicatesFound && !matchError) {

      System.debug('No duplicates found for record ID: ' + idList[0]);

     }

   }

```

Signature

```
   public static List<Datacloud.FindDuplicatesResult> findDuplicatesByIds(List<Id> ids)

```

Parameters

```
   ids
```

Type: ListID>

A list of IDs for which you want to find duplicates.

Return Value

Type: List<FindDuplicatesResult>

### FindDuplicatesResult Class Output for rule-based searches for duplicate records. FindDuplicatesResult contains results of detecting duplicates using instances of FindDuplicates or FindDuplicatesByIds classes.

Namespace

Datacloud

IN THIS SECTION:

FindDuplicatesResult Properties

FindDuplicatesResult Methods


Apex Reference Guide FindDuplicatesResult Class

#### FindDuplicatesResult Properties The following are properties for FindDuplicatesResult .

IN THIS SECTION:

##### duplicateresults

A list of `DuplicateResult` objects representing the results of calling `FindDuplicates.findDuplicates(sObjects)`
or `FindDuplicatesByIds.findDuplicatesByIds(ids)` . Elements in the list correspond to sObjects or IDs in the
input list.

##### errors

A list of `Database.Error` objects holding errors resulting from calling
`FindDuplicates.findDuplicates(sObjects)` or `FindDuplicatesByIds.findDuplicatesByIds(ids)` .

##### success

Boolean signifying whether the call to `FindDuplicates.findDuplicates(sObjects)` or
`FindDuplicatesByIds.findDuplicatesByIds(ids)` was successful.

##### duplicateresults

A list of `DuplicateResult` objects representing the results of calling `FindDuplicates.findDuplicates(sObjects)`
or `FindDuplicatesByIds.findDuplicatesByIds(ids)` . Elements in the list correspond to sObjects or IDs in the input
list.

Signature

```
   public List<Datacloud.DuplicateResult> duplicateresults

```

Property Value

Type: List<DuplicateResult>

##### errors

A list of `Database.Error` objects holding errors resulting from calling `FindDuplicates.findDuplicates(sObjects)`
or `FindDuplicatesByIds.findDuplicatesByIds(ids)` .

Signature

```
   public List<Database.Error> errors {get; set;}

```

Property Value

Type: List<Database.Error>

##### success

Boolean signifying whether the call to `FindDuplicates.findDuplicates(sObjects)` or
`FindDuplicatesByIds.findDuplicatesByIds(ids)` was successful.


Apex Reference Guide FindDuplicatesResult Class

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### FindDuplicatesResult Methods The following are methods for FindDuplicatesResult .

IN THIS SECTION:

##### getDuplicateResults()

Returns a list of `DuplicateResult` objects representing the results of calling
`FindDuplicates.findDuplicates(sObjects)` or `FindDuplicatesByIds.findDuplicatesByIds(ids)` .
Elements in the list correspond to sObjects or IDs in the input list.

getErrors()
Returns a list of `DatabaseError` objects containing errors resulting from calling
`FindDuplicates.findDuplicates(sObjects)` or `FindDuplicatesByIds.findDuplicatesByIds(ids)`,
if errors were encountered.

isSuccess()
Returns a Boolean signifying whether the call to `FindDuplicates.findDuplicates(sObjects)` or
`FindDuplicatesByIds.findDuplicatesByIds(ids)` was successful.

##### getDuplicateResults()

Returns a list of `DuplicateResult` objects representing the results of calling
`FindDuplicates.findDuplicates(sObjects)` or `FindDuplicatesByIds.findDuplicatesByIds(ids)` .
Elements in the list correspond to sObjects or IDs in the input list.

Example

```
   Account acct = new Account(name='Salesforce');

   List<Account> acctList = new List<Account>();

   acctList.add(acct);

   Datacloud.FindDuplicatesResult[] results = Datacloud.FindDuplicates.findDuplicates(acctList);

   for (Datacloud.FindDuplicatesResult findDupeResult : results) {

     for (Datacloud.DuplicateResult dupeResult : findDupeResult.getDuplicateResults()) {

      for (Datacloud.MatchResult matchResult : dupeResult.getMatchResults()) {

       for (Datacloud.MatchRecord matchRecord : matchResult.getMatchRecords()) {

         System.debug('Duplicate Record: ' + matchRecord.getRecord());

       }

      }

     }

   }

```


### Apex Reference Guide MatchRecord Class

Signature

```
   public List<Datacloud.DuplicateResult> getDuplicateResults()

```

Return Value

Type: List<DuplicateResult>

##### getErrors()

Returns a list of `DatabaseError` objects containing errors resulting from calling
`FindDuplicates.findDuplicates(sObjects)` or `FindDuplicatesByIds.findDuplicatesByIds(ids)`,
if errors were encountered.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### isSuccess()

Returns a Boolean signifying whether the call to `FindDuplicates.findDuplicates(sObjects)` or
`FindDuplicatesByIds.findDuplicatesByIds(ids)` was successful.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### MatchRecord Class

Represents a duplicate record detected by a matching rule.

Namespace

Datacloud

IN THIS SECTION:

#### MatchRecord Methods MatchRecord Methods

### The following are methods for MatchRecord .


Apex Reference Guide MatchRecord Class

IN THIS SECTION:

##### getAdditionalInformation()

Returns other information about a matched record. For example, a `matchGrade` represents the quality of the data for the D&B
fields in the matched record.

##### getFieldDiffs()

Returns all matching rule fields and how each field value compares for the duplicate and its matching record.

##### getMatchConfidence()

Returns the ranking of how similar a matched record’s data is to the data in your request. Must be equal to or greater than the value
of the `minMatchConfidence` specified in your request. Returns -1 if unused.

getRecord()
Returns the fields and field values for the duplicate.

##### getAdditionalInformation()

Returns other information about a matched record. For example, a `matchGrade` represents the quality of the data for the D&B fields
in the matched record.

Signature

```
   public List<Datacloud.AdditionalInformationMap> getAdditionalInformation()

```

Return Value

Type: List<Datacloud.AdditionalInformationMap>

##### getFieldDiffs()

Returns all matching rule fields and how each field value compares for the duplicate and its matching record.

Signature

```
   public List<Datacloud.FieldDiff> getFieldDiffs()

```

Return Value

Type: List<Datacloud.FieldDiff>

##### getMatchConfidence()

Returns the ranking of how similar a matched record’s data is to the data in your request. Must be equal to or greater than the value of
the `minMatchConfidence` specified in your request. Returns -1 if unused.

Signature

```
   public Double getMatchConfidence()

```

Return Value

Type: Double


### Apex Reference Guide MatchResult Class

##### getRecord()

Returns the fields and field values for the duplicate.

Signature

```
   public SObject getRecord()

```

Return Value

Type: SObject

### MatchResult Class

Represents the duplicate results for a matching rule.

Namespace

Datacloud

IN THIS SECTION:

#### MatchResult Methods MatchResult Methods

### The following are methods for MatchResult .

IN THIS SECTION:

getEntityType()
Returns the entity type of the matching rule.

getErrors()
Returns errors that occurred during matching for the matching rule.

getMatchEngine()
Returns the match engine for the matching rule.

getMatchRecords()
Returns information about the duplicates for the matching rule.

getRule()
Returns the developer name of the matching rule.

getSize()
Returns the number of duplicates detected by the matching rule.

isSuccess()
Returns `false` if there’s an error with the matching rule, and `true` if the matching rule successfully ran.


Apex Reference Guide MatchResult Class

##### getEntityType()

Returns the entity type of the matching rule.

Signature

```
   public String getEntityType()

```

Return Value

Type: String

##### getErrors()

Returns errors that occurred during matching for the matching rule.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getMatchEngine()

Returns the match engine for the matching rule.

Signature

```
   public String getMatchEngine()

```

Return Value

Type: String

##### getMatchRecords()

Returns information about the duplicates for the matching rule.

Signature

```
   public List<Datacloud.MatchRecord> getMatchRecords()

```

Return Value

Type: List<Datacloud.MatchRecord>

##### getRule()

Returns the developer name of the matching rule.


## Apex Reference Guide DataRetrieval Namespace

Signature

```
   public String getRule()

```

Return Value

Type: String

##### getSize()

Returns the number of duplicates detected by the matching rule.

Signature

```
   public Integer getSize()

```

Return Value

Type: Integer

##### isSuccess()

Returns `false` if there’s an error with the matching rule, and `true` if the matching rule successfully ran.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

## DataRetrieval Namespace The DataRetrieval namespace provides classes and methods to record details of customer-agent engagements, as well as transcripts

of their conversations.

## The following are the classes in the DataRetrieval namespace.

[Engagement Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Engagement.htm)

[Engagements Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Engagements.htm)

[EngagementRecordDetails Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_EngagementRecordDetails.htm)

[EngagementRecordDetailsList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_EngagementRecordDetailsList.htm)

[FieldDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_FieldDetailsRepresentation.htm)

[ObjectDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_ObjectDetailsRepresentation.htm)

[RecordDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordDetailsRepresentation.htm)

[RecordTranscripts Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordTranscripts.htm)

[RecordTranscriptsList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordTranscriptsList.htm)


## Apex Reference Guide DataSource Namespace

[Transcript Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Transcript.htm)

## DataSource Namespace The DataSource namespace provides the classes for the Apex Connector Framework. Use the Apex Connector Framework to develop

a custom adapter for Salesforce Connect. Then connect your Salesforce organization to any data anywhere via the Salesforce Connect
custom adapter.

## The following are the classes in the DataSource namespace.

IN THIS SECTION:

AsyncDeleteCallback Class
A callback class that the `Database.deleteAsync` method references. Salesforce calls this class after the remote
`deleteAsync` operation is completed. This class provides the compensating transaction in the completion context of the delete
operation. Extend this class to define the actions to execute after the remote delete operation finishes execution.

AsyncSaveCallback Class
A callback class that the `Database.insertAsync` or `Database.updateAsync` method references. Salesforce calls this
class after the remote operation is completed. This class provides the compensating transaction in the completion context of the
insert or update operation. Extend this class to define the actions to execute after the remote insert or update operation finishes
execution.

AuthenticationCapability Enum
Specifies the types of authentication that can be used to access the external system.

AuthenticationProtocol Enum
Determines what type of credentials are used to authenticate to the external system.

Capability Enum
Declares which functional operations the external system supports. Also specifies required endpoint settings for the external data
source definition.

Column Class
Describes a column on a `DataSource.Table` . This class extends the `DataSourceUtil` class and inherits its methods.

ColumnSelection Class
Identifies the list of columns to return during a query or search.

Connection Class
Extend this class to enable your Salesforce org to sync the external system’s schema and to handle queries, searches, and write
operations (upsert and delete) of the external data. This class extends the `DataSourceUtil` class and inherits its methods.

ConnectionParams Class
Contains the credentials for authenticating to the external system.

DataSourceUtil Class
Parent class for the `DataSource.Provider`, `DataSource.Connection`, `DataSource.Table`, and
`DataSource.Column` classes.

DataType Enum
Specifies the data types that are supported by the Apex Connector Framework.


Apex Reference Guide DataSource Namespace

DeleteContext Class
An instance of `DeleteContext` is passed to the `deleteRows()` method on your `Database.Connection` class. The
class provides context information about the delete request to the implementor of `deleteRows()` .

DeleteResult Class
Represents the result of a delete operation on an sObject record. The result is returned by the `DataSource.deleteRows`
method of the `DataSource.Connection` class.

Filter Class
Represents a `WHERE` clause in a SOSL or SOQL query.

FilterType Enum
Referenced by the `type` property on a `DataSource.Filter` .

IdentityType Enum
Determines which set of credentials is used to authenticate to the external system.

Order Class
Contains details about how to sort the rows in the result set. Equivalent to an `ORDER BY` statement in a SOQL query.

OrderDirection Enum
Specifies the direction for sorting rows based on column values.

Provider Class
Extend this base class to create a custom adapter for Salesforce Connect. The class informs Salesforce of the functional and
authentication capabilities that are supported by or required to connect to the external system. This class extends the
`DataSourceUtil` class and inherits its methods.

QueryAggregation Enum
Specifies how to aggregate a column in a query.

QueryContext Class
An instance of `QueryContext` is provided to the `query` method on your `DataSource.Connection` class. The instance
corresponds to a SOQL request.

QueryUtils Class
Contains helper methods to locally filter, sort, and apply limit and offset clauses to data rows. This helper class is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

ReadContext Class
Abstract base class for the `QueryContext` and `SearchContext` classes.

SearchContext Class
An instance of `SearchContext` is provided to the search method on your `DataSource.Connection` class. The instance
corresponds to a search or SOSL request.

SearchUtils Class
Helper class for implementing search on a custom adapter for Salesforce Connect.

Table Class
Describes a table on an external system that the Salesforce Connect custom adapter connects to. This class extends the
`DataSourceUtil` class and inherits its methods.

TableResult Class
Contains the results of a search or query.


### Apex Reference Guide AsyncDeleteCallback Class

TableSelection Class
Contains a breakdown of the SOQL or SOSL query. Its properties represent the FROM, ORDER BY, SELECT, and WHERE clauses in the
query.

UpsertContext Class
An instance of `UpsertContext` is passed to the `upsertRows()` method on your `Datasource.Connection` class.
This class provides context information about the upsert request to the implementor of `upsertRows()` .

UpsertResult Class
Represents the result of an upsert operation on an external object record. The result is returned by the `upsertRows` method of
the `DataSource.Connection` class.

DataSource Exceptions
The `DataSource` namespace contains exception classes.

### AsyncDeleteCallback Class

A callback class that the `Database.deleteAsync` method references. Salesforce calls this class after the remote `deleteAsync`
operation is completed. This class provides the compensating transaction in the completion context of the delete operation. Extend this
class to define the actions to execute after the remote delete operation finishes execution.

Namespace

DataSource

IN THIS SECTION:

#### AsyncDeleteCallback Methods AsyncDeleteCallback Methods

### The following are methods for AsyncDeleteCallback .

IN THIS SECTION:

##### processDelete(deleteResult)

Override this method to define actions that Salesforce executes after a remote `Database.deleteAsync` operation is completed.
For example, based on the results of the remote operation, you can update custom object data or other data that's stored in the
Salesforce org..

##### processDelete(deleteResult)

Override this method to define actions that Salesforce executes after a remote `Database.deleteAsync` operation is completed.
For example, based on the results of the remote operation, you can update custom object data or other data that's stored in the Salesforce
org..

Signature

```
   public void processDelete(Database.DeleteResult deleteResult)

```


### Apex Reference Guide AsyncSaveCallback Class

Parameters

```
   deleteResult
```

Type: Database.DeleteResult

The result of the asynchronous delete operation.

Return Value

Type: void

### AsyncSaveCallback Class

A callback class that the `Database.insertAsync` or `Database.updateAsync` method references. Salesforce calls this
class after the remote operation is completed. This class provides the compensating transaction in the completion context of the insert
or update operation. Extend this class to define the actions to execute after the remote insert or update operation finishes execution.

Namespace

DataSource

IN THIS SECTION:

#### AsyncSaveCallback Methods AsyncSaveCallback Methods

### The following are methods for AsyncSaveCallback .

IN THIS SECTION:

##### processSave(saveResult)

Override this method to define actions that Salesforce executes after the remote `Database.insertAsync` or
`Database.updateAsync` operation is completed. For example, based on the results of the remote operation, you can update
custom object data or other data that's stored in the Salesforce org.

##### processSave(saveResult)

Override this method to define actions that Salesforce executes after the remote `Database.insertAsync` or
`Database.updateAsync` operation is completed. For example, based on the results of the remote operation, you can update
custom object data or other data that's stored in the Salesforce org.

Signature

```
   public void processSave(Database.SaveResult saveResult)

```

Parameters

```
   saveResult
```

Type: Database.SaveResult


### Apex Reference Guide AuthenticationCapability Enum

The result of the asynchronous insert or update operation.

Return Value

Type: void

### AuthenticationCapability Enum

Specifies the types of authentication that can be used to access the external system.

Usage

The `DataSource.Provider` class returns `DataSource.AuthenticationCapability` enum values. The returned
values determine which authentication settings are available on the external data source definition in Salesforce.

If you set up callouts in your `DataSource.Connection` class, you can specify the callout endpoints as named credentials instead
of URLs. If you do so for all callouts, return `ANONYMOUS` as the sole entry in the list of data source authentication capabilities. That way,
the external data source definition doesn’t require authentication settings. Salesforce manages all authentication for Apex callouts that
specify a named credential as the callout endpoint so that your code doesn’t have to.

Enum Values

The following are the values of the `DataSource.AuthenticationCapability` enum.

**Value** **Description**

`ANONYMOUS` No credentials are required to authenticate to the external system.

`BASIC` A username and password can be used to authenticate to the external system.

`CERTIFICATE` A security certificate can be supplied when establishing each connection to the
external system.

`OAUTH` OAuth can be used to authenticate to the external system.

### AuthenticationProtocol Enum

Determines what type of credentials are used to authenticate to the external system.

Enum Values

The following are the values of the `DataSource.AuthenticationProtocol` enum.

**Value** **Description**

`NONE` No credentials are used to authenticate to the external system.

`OAUTH` OAuth 2.0 is used to authenticate to the external system.

`PASSWORD` A username and password are used to authenticate to the external system.


### Apex Reference Guide Capability Enum Capability Enum

Declares which functional operations the external system supports. Also specifies required endpoint settings for the external data source
definition.

Usage

The `DataSource.Provider` class returns `DataSource.Capability` enum values, which:

**•** Specify the functional capabilities of the external system.

**•** Determine which endpoint settings are available on the external data source definition in Salesforce.

Enum Values

The following are the values of the `DataSource.Capability` enum.

**Value** **Description**

`MULTI_PICKLIST` The external system supports multi-picklist fields.

`PICKLIST` The external system supports picklist fields.

`QUERY_PAGINATION_SERVER_DRIVEN` With server-driven paging, the external system determines the page sizes and batch
boundaries. The external system’s paging settings can optimize the external system’s

performance and improve the load times for external objects in your org. Also, the
external data set can change while your users or the Lightning Platform are paging
through the result set. Typically, server-driven paging adjusts batch boundaries to
accommodate changing data sets more effectively than client-driven paging.

If you enable server-driven paging on an external data source, Salesforce ignores
the requested page sizes, including the default `queryMore()` batch size of 500
rows. The pages returned by the external system determine the batches, but each
page can’t exceed 2,000 rows. Also, the Apex code must generate a query token
and use it to determine and fetch the next batch of results.

```
QUERY_TOTAL_SIZE

```

The external system can provide the total number of rows that meet the query
criteria, even when requested to return a smaller batch size. This capability enables
you to simplify how you paginate results by using `queryMore()` .

`REQUIRE_ENDPOINT` Requires the administrator to specify the endpoint in the URL field in the external
data source definition.

`REQUIRE_HTTPS` Requires the endpoint URL to use secure HTTP. If `REQUIRE_ENDPOINT` isn’t
declared, `REQUIRE_HTTPS` is ignored.

`ROW_CREATE` Allows creating of external data.

`ROW_DELETE` Allows deleting external data.

`ROW_QUERY` Allows API and SOQL queries of the external data. Also allows reports on the external
objects.

`ROW_UPDATE` Allows updating external data.


### Apex Reference Guide Column Class

**Value** **Description**

```
SEARCH

```

SEE ALSO:

Allows SOSL and Salesforce searches of the external data.

When the custom adapter declares the `SEARCH` capability, you can control which
external objects are searchable by selecting or deselecting **Allow Search** on each

external object. However, syncing always overwrites the external object’s search
status to match the search status of the external data source.

Only text, text area, and long text area fields on external objects can be searched.
If an external object has no searchable fields, searches on that object return no
records.

_Salesforce Help:_ [Validate and Sync an External Data Source](https://help.salesforce.com/apex/HTViewHelpDoc?id=ext_data_sync_database.htm&language=en_US)

### Column Class

Describes a column on a `DataSource.Table` . This class extends the `DataSourceUtil` class and inherits its methods.

Namespace

DataSource

Usage

A list of column metadata is provided by the `DataSource.Connection` class when the `sync()` method is invoked. Each column
can become a field on an external object.

The metadata is stored in Salesforce. Updating the Apex code to return new or updated values for the column metadata doesn’t
automatically update the stored metadata in Salesforce.

IN THIS SECTION:

#### Column Properties

Column Methods

#### Column Properties

### The following are properties for Column .

IN THIS SECTION:

decimalPlaces
If the data type is numeric, the number of decimal places to the right of the decimal point.

description
Description of what the column represents.


Apex Reference Guide Column Class

filterable
Whether a result set can be filtered based on the values of the column.

isPicklistAlphabeticallySorted
Returns `true` if the picklist is sorted alphabetically, `false` otherwise.

isPicklistRestricted
Returns `true` if the picklist is restricted, `false` otherwise.

label
User-friendly name for the column that appears in the Salesforce user interface.

length
If the column is a string data type, the number of characters in the column. If the column is a numeric data type, the total number
of digits on both sides of the decimal point, but excluding the decimal point.

name
Name of the column in the external system.

picklistValues
If the data type is a picklist, the picklist values.

referenceTargetField
API name of the custom field on the parent object whose values are compared against this column’s values. Matching values identify
related records in an indirect lookup relationship. Applies only when the column’s data type is `INDIRECT_LOOKUP_TYPE` . For
other data types, this value is ignored.

referenceTo
API name of the parent object in the relationship that’s represented by this column. Applies only when the column’s data type is
`LOOKUP_TYPE`, `EXTERNAL_LOOKUP_TYPE`, or `INDIRECT_LOOKUP_TYPE` . For other data types, this value is ignored.

sortable
Whether a result set can be sorted based on the values of the column via an `ORDER BY` clause.

type
Data type of the column.

##### decimalPlaces

If the data type is numeric, the number of decimal places to the right of the decimal point.

Signature

```
   public Integer decimalPlaces {get; set;}

```

Property Value

Type: Integer

##### description

Description of what the column represents.


Apex Reference Guide Column Class

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

##### filterable

Whether a result set can be filtered based on the values of the column.

Signature

```
   public Boolean filterable {get; set;}

```

Property Value

Type: Boolean

##### **`isPicklistAlphabeticallySorted`**

Returns `true` if the picklist is sorted alphabetically, `false` otherwise.

Signature

```
   public Boolean isPicklistAlphabeticallySorted {get; set;}

```

Property Value

Type: Boolean

##### **`isPicklistRestricted`**

Returns `true` if the picklist is restricted, `false` otherwise.

Signature

```
   public Boolean isPicklistRestricted {get; set;}

```

Property Value

Type: Boolean

##### label

User-friendly name for the column that appears in the Salesforce user interface.

Signature

```
   public String label {get; set;}

```


Apex Reference Guide Column Class

Property Value

Type: String

##### length

If the column is a string data type, the number of characters in the column. If the column is a numeric data type, the total number of
digits on both sides of the decimal point, but excluding the decimal point.

Signature

```
   public Integer length {get; set;}

```

Property Value

Type: Integer

##### name

Name of the column in the external system.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`picklistValues`**

If the data type is a picklist, the picklist values.

Signature

```
   public List<Map<String,String>> picklistValues {get; set;}

```

Property Value

Type: List<Map<String,String>>

##### referenceTargetField

API name of the custom field on the parent object whose values are compared against this column’s values. Matching values identify
related records in an indirect lookup relationship. Applies only when the column’s data type is `INDIRECT_LOOKUP_TYPE` . For other
data types, this value is ignored.

Signature

```
   public String referenceTargetField {get; set;}

```


Apex Reference Guide Column Class

Property Value

Type: String

##### referenceTo

API name of the parent object in the relationship that’s represented by this column. Applies only when the column’s data type is
`LOOKUP_TYPE`, `EXTERNAL_LOOKUP_TYPE`, or `INDIRECT_LOOKUP_TYPE` . For other data types, this value is ignored.

Signature

```
   public String referenceTo {get; set;}

```

Property Value

Type: String

##### sortable

Whether a result set can be sorted based on the values of the column via an `ORDER BY` clause.

Signature

```
   public Boolean sortable {get; set;}

```

Property Value

Type: Boolean

##### type

Data type of the column.

Signature

```
   public DataSource.DataType type {get; set;}

```

Property Value

Type: DataSource.DataType

#### Column Methods The following are methods for Column .

IN THIS SECTION:

boolean(name)
Returns a new column of data type `BOOLEAN_TYPE` .

currency(name, length, decimalPlaces)
Returns a new column of data type `CURRENCY_TYPE` .


Apex Reference Guide Column Class

date(name)
Returns a new column of data type `DATE_TYPE` .

datetime(name)
Returns a new column of data type `DATETIME_TYPE` .

email(name)
Returns a new column of data type `EMAIL_TYPE` .

externalLookup(name, domain)
Returns a new column of data type `EXTERNAL_LOOKUP_TYPE` .

get(name, label, description, isSortable, isFilterable, type, length, decimalPlaces, referenceTo, referenceTargetField, picklistValuesObj,
isPicklistAlphabeticallySorted, isPicklistRestricted)
Returns a new column with the 13 specified `Column` property values.

get(name, label, description, isSortable, isFilterable, type, length, decimalPlaces, referenceTo, referenceTargetField)
Returns a new column with the ten specified `Column` property values.

get(name, label, description, isSortable, isFilterable, type, length, decimalPlaces)
Returns a new column with the eight specified `Column` property values.

get(name, label, description, isSortable, isFilterable, type, length)
Returns a new column with the seven specified `Column` property values.

indirectLookup(name, domain, targetField)
Returns a new column of data type `INDIRECT_LOOKUP_TYPE` .

integer(name, length)
Returns a new numeric column with no decimal places using the specified name and length.

lookup(name, domain)
Returns a new column of data type `LOOKUP_TYPE` .

multipicklist(name, picklistValues, isPicklistAlphabeticallySorted, isPicklistRestricted)
Returns a new column of data type `PICKLIST_MULTISELECT_TYPE` with the specified name and picklist values. You can
also specify whether the picklist is sorted alphabetically or if the picklist is restricted.

multipicklist(name, picklistValues)
Returns a new column of data type `PICKLIST_MULTISELECT_TYPE` with the specified name and picklist values.

number(name, length, decimalPlaces)
Returns a new column of data type `NUMBER_TYPE` .

percent(name, length, decimalPlaces)
Returns a new column of data type `PERCENT_TYPE` .

phone(name)
Returns a new column of data type `PHONE_TYPE` .

picklist(name, picklistValues, isPicklistAlphabeticallySorted, isPicklistRestricted)
Returns a new column of data type `PICKLIST_TYPE` with the specified name and picklist values. You can also specify whether
the picklist is sorted alphabetically or if the picklist is restricted.

picklist(name, picklistValues)
Returns a new column of data type `PICKLIST_TYPE` with the specified name and picklist values.


Apex Reference Guide Column Class

text(name, label, length)
Returns a new column of data type `STRING_SHORT_TYPE` or `STRING_LONG_TYPE`, with the specified name, label, and
length.

text(name, length)
Returns a new column of data type `STRING_SHORT_TYPE` or `STRING_LONG_TYPE`, with the specified name and length.

text(name)
Returns a new column of data type `STRING_SHORT_TYPE` with the specified name and the length of 255 characters.

textarea(name)
Returns a new column of data type `STRING_LONG_TYPE` with the specified name and the length of 32,000 characters.

time(name)
Returns a new column of data type `Time` with the specified name.

url(name, length)
Returns a new column of data type `URL_TYPE` with the specified name and length.

url(name)
Returns a new column of data type `URL_TYPE` with the specified name and the length of 1,000 characters.

##### boolean(name)

Returns a new column of data type `BOOLEAN_TYPE` .

Signature

```
   public static DataSource.Column boolean(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### **`currency(name, length, decimalPlaces)`**

Returns a new column of data type `CURRENCY_TYPE` .

Signature

```
   public static DataSource.Column currency(String name, Integer length, Integer

   decimalPlaces)

```

Parameters

```
   name
```

Type: String


Apex Reference Guide Column Class

Name of the column.

```
   length
```

Type: Integer

Number of characters allowed in the column.

```
   decimalPlaces
```

Type: Integer

Number of decimal places to the right of the decimal point.

Return Value

Type: DataSource.Column

##### **`date(name)`**

Returns a new column of data type `DATE_TYPE` .

Signature

```
   public static DataSource.Column date(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### **`datetime(name)`**

Returns a new column of data type `DATETIME_TYPE` .

Signature

```
   public static DataSource.Column datetime(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column


Apex Reference Guide Column Class

##### **`email(name)`**

Returns a new column of data type `EMAIL_TYPE` .

Signature

```
   public static DataSource.Column email(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### externalLookup(name, domain)

Returns a new column of data type `EXTERNAL_LOOKUP_TYPE` .

Signature

```
   public static DataSource.Column externalLookup(String name, String domain)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   domain
```

Type: String

API name of the parent object in the external lookup relationship.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true


Apex Reference Guide Column Class

**Property** **Value**

type DataSource.DataType.EXTERNAL_LOOKUP_TYPE

length 255

decimalPlaces 0

referenceTo _`domain`_

referenceTargetField null

##### **`get(name, label, description, isSortable, isFilterable, type, length,`**

```
  decimalPlaces, referenceTo, referenceTargetField, picklistValuesObj,

  isPicklistAlphabeticallySorted, isPicklistRestricted)

```

Returns a new column with the 13 specified `Column` property values.

Signature

```
   public static DataSource.Column get(String name, String label, String description,

   Boolean isSortable, Boolean isFilterable, DataSource.DataType type, Integer length,

   Integer decimalPlaces, String referenceTo, String referenceTargetField, Object

   picklistValuesObj, Boolean isPicklistAlphabeticallySorted, Boolean isPicklistRestricted)

```

Parameters

See Column Properties on page 2720 for information about each parameter.

```
   name
```

Type: String

```
   label
```

Type: String

```
   description
```

Type: String

```
   isSortable
```

Type: Boolean

```
   isFilterable
```

Type: Boolean

```
   type
```

Type: DataSource.DataType

```
   length
```

Type: Integer

```
   decimalPlaces
```

Type: Integer

```
   referenceTo
```

Type: String


Apex Reference Guide Column Class

```
   referenceTargetField
```

Type: String

```
   picklistValuesObj
```

Type: Object

```
   isPicklistAlphabeticallySorted
```

Type: Boolean

```
   isPicklistRestricted
```

Type: Boolean

Return Value

Type: DataSource.Column

##### get(name, label, description, isSortable, isFilterable, type, length, decimalPlaces, referenceTo,

referenceTargetField)

Returns a new column with the ten specified `Column` property values.

Signature

```
   public static DataSource.Column get(String name, String label, String description,

   Boolean isSortable, Boolean isFilterable, DataSource.DataType type, Integer length,

   Integer decimalPlaces, String referenceTo, String referenceTargetField)

```

Parameters

See Column Properties on page 2720 for information about each parameter.

```
   name
```

Type: String

```
   label
```

Type: String

```
   description
```

Type: String

```
   isSortable
```

Type: Boolean

```
   isFilterable
```

Type: Boolean

```
   type
```

Type: DataSource.DataType

```
   length
```

Type: Integer

```
   decimalPlaces
```

Type: Integer

```
   referenceTo
```

Type: String


Apex Reference Guide Column Class

```
   referenceTargetField
```

Type: String

Return Value

Type: DataSource.Column

##### get(name, label, description, isSortable, isFilterable, type, length, decimalPlaces)

Returns a new column with the eight specified `Column` property values.

Signature

```
   public static DataSource.Column get(String name, String label, String description,

   Boolean isSortable, Boolean isFilterable, DataSource.DataType type, Integer length,

   Integer decimalPlaces)

```

Parameters

See Column Properties on page 2720 for information about each parameter.

```
   name
```

Type: String

```
   label
```

Type: String

```
   description
```

Type: String

```
   isSortable
```

Type: Boolean

```
   isFilterable
```

Type: Boolean

```
   type
```

Type: DataSource.DataType

```
   length
```

Type: Integer

```
   decimalPlaces
```

Type: Integer

Return Value

Type: DataSource.Column

##### get(name, label, description, isSortable, isFilterable, type, length)

Returns a new column with the seven specified `Column` property values.


Apex Reference Guide Column Class

Signature

```
   public static DataSource.Column get(String name, String label, String description,

   Boolean isSortable, Boolean isFilterable, DataSource.DataType type, Integer length)

```

Parameters

See Column Properties on page 2720 for information about each parameter.

```
   name
```

Type: String

```
   label
```

Type: String

```
   description
```

Type: String

```
   isSortable
```

Type: Boolean

```
   isFilterable
```

Type: Boolean

```
   type
```

Type: DataSource.DataType

```
   length
```

Type: Integer

Return Value

Type: DataSource.Column

##### indirectLookup(name, domain, targetField)

Returns a new column of data type `INDIRECT_LOOKUP_TYPE` .

Signature

```
   public static DataSource.Column indirectLookup(String name, String domain, String

   targetField)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   domain
```

Type: String

API name of the parent object in the indirect lookup relationship.

```
   targetField
```

Type: String


Apex Reference Guide Column Class

API name of the custom field on the parent object whose values are compared against this column’s values. Matching values identify
related records in an indirect lookup relationship.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.INDIRECT_LOOKUP_TYPE

length 255

decimalPlaces 0

referenceTo _`domain`_

referenceTargetField _`targetField`_

##### integer(name, length)

Returns a new numeric column with no decimal places using the specified name and length.

Signature

```
   public static DataSource.Column integer(String name, Integer length)

```

Parameters

```
   name
```

Type: String

The column name.

```
   length
```

Type: Integer

The column length.

Return Value

Type: DataSource.Column


Apex Reference Guide Column Class

##### lookup(name, domain)

Returns a new column of data type `LOOKUP_TYPE` .

Signature

```
   public static DataSource.Column lookup(String name, String domain)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   domain
```

Type: String

API name of the parent object in the lookup relationship.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.LOOKUP_TYPE

length 255

decimalPlaces 0

referenceTo _`domain`_

referenceTargetField null

##### **`multipicklist(name, picklistValues, isPicklistAlphabeticallySorted,`**

```
  isPicklistRestricted)

```

Returns a new column of data type `PICKLIST_MULTISELECT_TYPE` with the specified name and picklist values. You can also
specify whether the picklist is sorted alphabetically or if the picklist is restricted.


Apex Reference Guide Column Class

Signature

```
   public static DataSource.Column multipicklist(String name, List<Map<String,String>>

   picklistValues, Boolean isPicklistAlphabeticallySorted, Boolean isPicklistRestricted)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   picklistValues
```

Type: List<Map<String,String>>

```
   isPicklistAlphabeticallySorted
```

Indicates whether the picklist is sorted alphabetically.

```
   isPicklistRestricted
```

Type: Boolean

Indicates whether the picklist is restricted.

Return Value

Type: DataSource.Column

##### **`multipicklist(name, picklistValues)`**

Returns a new column of data type `PICKLIST_MULTISELECT_TYPE` with the specified name and picklist values.

Signature

```
   public static DataSource.Column multipicklist(String name, List<Map<String,String>>

   picklistValues)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   picklistValues
```

Type: List<Map<String,String>>

List of picklist values.

Return Value

Type: DataSource.Column

##### number(name, length, decimalPlaces)

Returns a new column of data type `NUMBER_TYPE` .


Apex Reference Guide Column Class

Signature

```
   public static DataSource.Column number(String name, Integer length, Integer

   decimalPlaces)

```

Parameters

See Column Properties on page 2720 for information about each parameter.

```
   name
```

Type: String

```
   length
```

Type: Integer

```
   decimalPlaces
```

Type: Integer

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.NUMBER_TYPE

length _`length`_

decimalPlaces _`decimalPlaces`_

##### **`percent(name, length, decimalPlaces)`**

Returns a new column of data type `PERCENT_TYPE` .

Signature

```
   public static DataSource.Column percent(String name, Integer length, Integer

   decimalPlaces)

```

Parameters

```
   name
```

Type: String

Name of the column.


Apex Reference Guide Column Class

```
   length
```

Type: Integer

Number of characters allowed in the column.

```
   decimalPlaces
```

Type: Integer

Number of decimal places to the right of the decimal point.

Return Value

Type: DataSource.Column

##### **`phone(name)`**

Returns a new column of data type `PHONE_TYPE` .

Signature

```
   public static DataSource.Column phone(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### **`picklist(name, picklistValues, isPicklistAlphabeticallySorted,`**

```
  isPicklistRestricted)

```

Returns a new column of data type `PICKLIST_TYPE` with the specified name and picklist values. You can also specify whether the
picklist is sorted alphabetically or if the picklist is restricted.

Signature

```
   public static DataSource.Column picklist(String name, List<Map<String,String>>

   picklistValues, Boolean isPicklistAlphabeticallySorted, Boolean isPicklistRestricted)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   picklistValues
```

Type: List<Map<String,String>>


Apex Reference Guide Column Class

List of picklist values.

```
   isPicklistAlphabeticallySorted
```

Indicates whether the picklist is sorted alphabetically.

```
   isPicklistRestricted
```

Type: Boolean

Indicates whether the picklist is restricted.

Return Value

Type: DataSource.Column

##### **`picklist(name, picklistValues)`**

Returns a new column of data type `PICKLIST_TYPE` with the specified name and picklist values.

Signature

```
   public static DataSource.Column picklist(String name, List<Map<String,String>>

   picklistValues)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   picklistValues
```

Type: List<Map<String,String>>

List of picklist values.

Return Value

Type: DataSource.Column

##### text(name, label, length)

Returns a new column of data type `STRING_SHORT_TYPE` or `STRING_LONG_TYPE`, with the specified name, label, and length.

Signature

```
   public static DataSource.Column text(String name, String label, Integer length)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   label
```

Type: String


Apex Reference Guide Column Class

User-friendly name for the column that appears in the Salesforce user interface.

```
   length
```

Type: Integer

Number of characters allowed in the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`label`_

description _`label`_

isSortable true

isFilterable true

type

DataSource.DataType.STRING_SHORT_TYPE if _`length`_ is 255 or less

DataSource.DataType.STRING_LONG_TYPE if _`length`_ is greater than 255

length _`length`_

decimalPlaces 0

##### text(name, length)

Returns a new column of data type `STRING_SHORT_TYPE` or `STRING_LONG_TYPE`, with the specified name and length.

Signature

```
public static DataSource.Column text(String name, Integer length)

```

Parameters

```
name
```

Type: String

Name of the column.

```
length
```

Type: Integer

Number of characters allowed in the column.

Return Value

Type: DataSource.Column

The returned column has these property values.


Apex Reference Guide Column Class

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type

DataSource.DataType.STRING_SHORT_TYPE if _`length`_ is 255 or
less

DataSource.DataType.STRING_LONG_TYPE if _`length`_ is greater
than 255

length _`length`_

decimalPlaces 0

##### text(name)

Returns a new column of data type `STRING_SHORT_TYPE` with the specified name and the length of 255 characters.

Signature

```
public static DataSource.Column text(String name)

```

Parameters

```
name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.STRING_SHORT_TYPE


Apex Reference Guide Column Class

**Property** **Value**

length 255

decimalPlaces 0

##### textarea(name)

Returns a new column of data type `STRING_LONG_TYPE` with the specified name and the length of 32,000 characters.

Signature

```
   public static DataSource.Column textarea(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.STRING_LONG_TYPE

length 32000

decimalPlaces 0

##### **`time(name)`**

Returns a new column of data type `Time` with the specified name.

Signature

```
   public static DataSource.Column time(String name)

```


Apex Reference Guide Column Class

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### url(name, length)

Returns a new column of data type `URL_TYPE` with the specified name and length.

Signature

```
   public static DataSource.Column url(String name, Integer length)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   length
```

Type: Integer

Number of characters allowed in the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.URL_TYPE

length _`length`_

decimalPlaces 0


### Apex Reference Guide ColumnSelection Class

##### url(name)

Returns a new column of data type `URL_TYPE` with the specified name and the length of 1,000 characters.

Signature

```
   public static DataSource.Column url(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.URL_TYPE

length 1000

decimalPlaces 0

### ColumnSelection Class

Identifies the list of columns to return during a query or search.

Namespace

DataSource Namespace

Usage

This class is associated with the `SELECT` clause for a SOQL query, or the `RETURNING` clause for a SOSL query.

IN THIS SECTION:

ColumnSelection Properties


Apex Reference Guide ColumnSelection Class

#### ColumnSelection Properties The following are properties for ColumnSelection .

IN THIS SECTION:

##### aggregation

How to aggregate the column’s data.

##### columnName

Name of the selected column.

##### tableName

Name of the column’s table.

##### aggregation

How to aggregate the column’s data.

Signature

```
   public DataSource.QueryAggregation aggregation {get; set;}

```

Property Value

Type: DataSource.QueryAggregation

##### columnName

Name of the selected column.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### tableName

Name of the column’s table.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String


### Apex Reference Guide Connection Class Connection Class

Extend this class to enable your Salesforce org to sync the external system’s schema and to handle queries, searches, and write operations
(upsert and delete) of the external data. This class extends the `DataSourceUtil` class and inherits its methods.

Namespace

DataSource

Usage

Your `DataSource.Connection` and `DataSource.Provider` classes compose a custom adapter for Salesforce Connect.

Changing the `sync` method on the `DataSource.Connection` class doesn’t automatically resync any external objects.

Example

```
   global class SampleDataSourceConnection extends DataSource.Connection {

      global SampleDataSourceConnection(DataSource.ConnectionParams connectionParams) {

      }

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables = new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('Name', 255));

        columns.add(DataSource.Column.text('ExternalId', 255));

        columns.add(DataSource.Column.url('DisplayUrl'));

        tables.add(DataSource.Table.get('Sample', 'Title', columns));

        return tables;

      }

      override global DataSource.TableResult query(DataSource.QueryContext c) {

        return DataSource.TableResult.get(c, DataSource.QueryUtils.process(c, getRows()));

      }

      override global List<DataSource.TableResult> search(DataSource.SearchContext c) {

        List<DataSource.TableResult> results = new List<DataSource.TableResult>();

        for (DataSource.TableSelection tableSelection : c.tableSelections) {

           results.add(DataSource.TableResult.get(tableSelection, getRows()));

        }

        return results;

      }

      // Helper method to get record values from the external system for the Sample table.

      private List<Map<String, Object>> getRows () {

       // Get row field values for the Sample table from the external system via a callout.

        HttpResponse response = makeGetCallout();

        // Parse the JSON response and populate the rows.

        Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

```


Apex Reference Guide Connection Class

```
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

            // First, deserialize it.

            Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

                 response.getBody());

            if (response.getStatusCode() == 200){

              results.add(DataSource.UpsertResult.success(

                   String.valueOf(m.get('id'))));

            }

            else {

              results.add(DataSource.UpsertResult.failure(

```


Apex Reference Guide Connection Class

```
                       String.valueOf(m.get('id')),

                'The callout resulted in an error: ' +

                response.getStatusCode()));

            }

          }

          return results;

        }

        return null;

      }

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

      // Helper methods

      // Make a GET callout

      private static HttpResponse makeGetCallout() {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

      // Populate a row based on values from the external system.

      private Map<String,Object> foundRow(Map<String,Object> foundRow) {

        Map<String,Object> row = new Map<String,Object>();

        row.put('ExternalId', string.valueOf(foundRow.get('Id')));

        row.put('DisplayUrl', string.valueOf(foundRow.get('DisplayUrl')));

        row.put('Name', string.valueOf(foundRow.get('Name')));

        return row;

      }

      // Make a POST callout

      private static HttpResponse makePostCallout(String jsonBody) {

         HttpResponse response;

         // Make callout

         // ...

```


Apex Reference Guide Connection Class

```
         return response;

      }

      // Make a PUT callout

      private static HttpResponse makePutCallout(String jsonBody, String externalID) {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

      // Make a DELETE callout

      private static HttpResponse makeDeleteCallout(String externalID) {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

   }

```

IN THIS SECTION:

#### Connection Methods Connection Methods The following are methods for Connection .

IN THIS SECTION:

##### deleteRows(deleteContext)

Invoked when external object records are deleted via the Salesforce user interface, APIs, or Apex.

query(queryContext)
Invoked by a SOQL query of an external object. A SOQL query is generated and executed when a user visits an external object’s list
view or record detail page in Salesforce. Returns the results of the query.

search(searchContext)
Invoked by a SOSL query of an external object or when a user performs a Salesforce global search that also searches external objects.
Returns the results of the query.

sync()
Invoked when an administrator clicks **Validate and Sync** on the external data source detail page. Returns a list of tables that describe
the external system’s schema.

upsertRows(upsertContext)
Invoked when external object records are created or updated via the Salesforce user interface, APIs, or Apex.

##### deleteRows(deleteContext)

Invoked when external object records are deleted via the Salesforce user interface, APIs, or Apex.


Apex Reference Guide Connection Class

Signature

```
   public List<DataSource.DeleteResult> deleteRows(DataSource.DeleteContext deleteContext)

```

Parameters

```
   deleteContext
```

Type: DataSource.DeleteContext

Contains context information about the delete request.

Return Value

Type: List<DataSource.DeleteResult>

The results of the delete operation.

##### query(queryContext)

Invoked by a SOQL query of an external object. A SOQL query is generated and executed when a user visits an external object’s list view
or record detail page in Salesforce. Returns the results of the query.

Signature

```
   public DataSource.TableResult query(DataSource.QueryContext queryContext)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

Return Value

Type: DataSource.TableResult

##### search(searchContext)

Invoked by a SOSL query of an external object or when a user performs a Salesforce global search that also searches external objects.
Returns the results of the query.

Signature

```
   public List<DataSource.TableResult> search(DataSource.SearchContext searchContext)

```

Parameters

```
   searchContext
```

Type: DataSource.SearchContext

Represents the query to run against an external data table.


### Apex Reference Guide ConnectionParams Class

Return Value

Type: List<DataSource.TableResult>

##### sync()

Invoked when an administrator clicks **Validate and Sync** on the external data source detail page. Returns a list of tables that describe
the external system’s schema.

Signature

```
   public List<DataSource.Table> sync()

```

Return Value

Type: List<DataSource.Table>

Each returned table can be used to create an external object in Salesforce. On the Validate External Data Source page, the administrator
views the list of returned tables and selects which tables to sync. When the administrator clicks **Sync**, an external object is created for
each selected table. Each column within the selected tables also becomes a field in the external object.

##### upsertRows(upsertContext)

Invoked when external object records are created or updated via the Salesforce user interface, APIs, or Apex.

Signature

```
   public List<DataSource.UpsertResult> upsertRows(DataSource.UpsertContext upsertContext)

```

Parameters

```
   upsertContext
```

Type: DataSource.UpsertContext

Contains context information about the upsert request.

Return Value

Type: List<DataSource.UpsertResult>

The results of the upsert operation.

### ConnectionParams Class

Contains the credentials for authenticating to the external system.

Namespace

DataSource


Apex Reference Guide ConnectionParams Class

Usage

If your extension of the `[DataSource.Provider](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_Provider.htm)` class returns `[DataSource.AuthenticationCapability](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_enum_DataSource_AuthenticationCapability.htm)` values that
indicate support for authentication, the `[DataSource.Connection](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_Connection.htm)` class is instantiated with a
`[DataSource.ConnectionParams](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_ConnectionParams.htm)` instance in the constructor.

The authentication credentials in the `DataSource.ConnectionParams` instance depend on the `Identity Type` field of
the external data source definition in Salesforce.

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

The values in this class can appear in debug logs and can be accessed by users who have the “Author Apex” permission. If you require
better security, we recommend that you specify named credentials instead of URLs as your Apex callout endpoints. Salesforce manages
all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to.

IN THIS SECTION:

#### ConnectionParams Properties ConnectionParams Properties The following are properties for ConnectionParams .

IN THIS SECTION:

certificateName
The name of the certificate for establishing each connection to the external system.

endpoint
The URL of the external system.

oauthToken
The OAuth token that’s issued by the external system.

password
The password for authenticating to the external system.

principalType
An instance of DataSource.IdentityType, which determines which set of credentials to use to access the external system.

protocol
The type of protocol that’s used to authenticate to the external system.

repository
Reserved for future use.

username
The username for authenticating to the external system.


Apex Reference Guide ConnectionParams Class

##### certificateName

The name of the certificate for establishing each connection to the external system.

Signature

```
   public String certificateName {get; set;}

```

Property Value

Type: String

The value comes from the external data source definition in Salesforce.

##### endpoint

The URL of the external system.

Signature

```
   public String endpoint {get; set;}

```

Property Value

Type: String

The value comes from the external data source definition in Salesforce.

##### oauthToken

The OAuth token that’s issued by the external system.

Signature

```
   public String oauthToken {get; set;}

```

Property Value

Type: String

##### password

The password for authenticating to the external system.

Signature

```
   public String password {get; set;}

```

Property Value

Type: String

The value depends on the `Identity Type` field of the external data source definition in Salesforce.


Apex Reference Guide ConnectionParams Class

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

##### principalType

An instance of DataSource.IdentityType, which determines which set of credentials to use to access the external system.

Signature

```
   public DataSource.IdentityType principalType {get; set;}

```

Property Value

Type: DataSource.IdentityType

##### protocol

The type of protocol that’s used to authenticate to the external system.

Signature

```
   public DataSource.AuthenticationProtocol protocol {get; set;}

```

Property Value

Type: DataSource.AuthenticationProtocol

##### repository

Reserved for future use.

Signature

```
   public String repository {get; set;}

```

Property Value

Type: String

Reserved for future use.

##### username

The username for authenticating to the external system.


### Apex Reference Guide DataSourceUtil Class

Signature

```
   public String username {get; set;}

```

Property Value

Type: String

The value depends on the `Identity Type` field of the external data source definition in Salesforce.

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

### DataSourceUtil Class

Parent class for the `DataSource.Provider`, `DataSource.Connection`, `DataSource.Table`, and
`DataSource.Column` classes.

Namespace

### DataSource

IN THIS SECTION:

#### DataSourceUtil Methods DataSourceUtil Methods

### The following are methods for DataSourceUtil .

IN THIS SECTION:

##### logWarning(message)

Logs the error message in the debug log.

throwException(message)
Throws a `DataSourceException` and displays the provided message to the user.

##### logWarning(message)

Logs the error message in the debug log.

Signature

```
   public void logWarning(String message)

```


### Apex Reference Guide DataType Enum

Parameters

```
   message
```

Type: String

The error message.

Return Value

Type: void

##### throwException(message)

Throws a `DataSourceException` and displays the provided message to the user.

Signature

```
   public void throwException(String message)

```

Parameters

```
   message
```

Type: String

Error message to display to the user.

Return Value

Type: void

### DataType Enum

Specifies the data types that are supported by the Apex Connector Framework.

Usage

The `DataSource.DataType` enum is referenced by the `type` property on the `DataSource.Column` class.

Enum Values

The following are the values of the `DataSource.DataType` enum.

**Value** **Description**

`BOOLEAN_TYPE` Boolean

`CURRENCY_TYPE` Currency

`DATE_TYPE` Date

`DATETIME_TYPE` Date/Time

`EMAIL_TYPE` Email


### Apex Reference Guide DeleteContext Class

**Value** **Description**

`EXTERNAL_LOOKUP_TYPE` External lookup relationship

`INDIRECT_LOOKUP_TYPE` Indirect lookup relationship

`LOOKUP_TYPE` Lookup relationship

`NUMBER_TYPE` Number

`PERCENT_TYPE` Percent

`PHONE_TYPE` Phone

`PICKLIST_MULTISELECT_TYPE` Multi-select picklist

`PICKLIST_TYPE` Picklist

`STRING_LONG_TYPE` Long text area

`STRING_SHORT_TYPE` Text area

`TIME_TYPE` Time

`URL_TYPE` URL

### DeleteContext Class An instance of DeleteContext is passed to the deleteRows() method on your Database.Connection class. The class

provides context information about the delete request to the implementor of `deleteRows()` .

Namespace

DataSource

Usage

The Apex Connector Framework creates context for operations. Context is comprised of parameters about the operations, which other
### methods can use. An instance of the DeleteContext class packages these parameters into an object that can be used when a

`deleteRows()` operation is initiated.

IN THIS SECTION:

#### DeleteContext Properties DeleteContext Properties

### The following are properties for DeleteContext .

IN THIS SECTION:

externalIds
The external IDs of the rows representing external object records to delete.


### Apex Reference Guide DeleteResult Class

##### tableSelected

The name of the table to delete rows from.

##### externalIds

The external IDs of the rows representing external object records to delete.

Signature

```
   public List<String> externalIds {get; set;}

```

Property Value

Type: List<String>

##### tableSelected

The name of the table to delete rows from.

Signature

```
   public String tableSelected {get; set;}

```

Property Value

Type: String

### DeleteResult Class

Represents the result of a delete operation on an sObject record. The result is returned by the `DataSource.deleteRows` method
of the `DataSource.Connection` class.

Namespace

DataSource

Usage

A delete operation on external object records generates an array of objects of type `DataSource.DeleteResult` . Its methods
create result records that indicate whether the delete operation succeeded or failed.

IN THIS SECTION:

#### DeleteResult Properties

DeleteResult Methods

#### DeleteResult Properties

### The following are properties for DeleteResult .


Apex Reference Guide DeleteResult Class

IN THIS SECTION:

##### errorMessage

The error message that’s generated by a failed delete operation. Recorded with a result of type `DataSource.DeleteResult` .

##### externalId

The unique identifier of a row that represents an external object record to delete.

##### success

Indicates whether a delete operation succeeded or failed.

##### errorMessage

The error message that’s generated by a failed delete operation. Recorded with a result of type `DataSource.DeleteResult` .

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### externalId

The unique identifier of a row that represents an external object record to delete.

Signature

```
   public String externalId {get; set;}

```

Property Value

Type: String

##### success

Indicates whether a delete operation succeeded or failed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeleteResult Methods The following are methods for DeleteResult .


Apex Reference Guide DeleteResult Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `DeleteResult` by determining the equality of external objects in a list. This method is
##### dynamic and is based on the equals method in Java. failure(externalId, errorMessage)

Creates a delete result indicating the failure of a delete request for a given external ID.

hashCode()
Maintains the integrity of lists of type `DeleteResult` by determining the uniqueness of the external object records in a list.

success(externalId)
Creates a delete result indicating the successful completion of a delete request for a given external ID.

##### equals(obj)

Maintains the integrity of lists of type `DeleteResult` by determining the equality of external objects in a list. This method is dynamic
##### and is based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

##### For information about the equals method, see Using Custom Types in Map Keys and Sets.

Return Value

Type: Boolean

##### failure(externalId, errorMessage)

Creates a delete result indicating the failure of a delete request for a given external ID.

Signature

```
   public static DataSource.DeleteResult failure(String externalId, String errorMessage)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the sObject record to delete.

```
   errorMessage
```

Type: String

The reason the delete operation failed.


### Apex Reference Guide Filter Class

Return Value

Type: DataSource.DeleteResult

Status result of the delete operation.

##### hashCode()

Maintains the integrity of lists of type `DeleteResult` by determining the uniqueness of the external object records in a list.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### success(externalId)

Creates a delete result indicating the successful completion of a delete request for a given external ID.

Signature

```
   public static DataSource.DeleteResult success(String externalId)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the sObject record to delete.

Return Value

Type: DataSource.DeleteResult

Status result of the delete operation for the sObject with the given external ID.

### Filter Class

Represents a `WHERE` clause in a SOSL or SOQL query.

Namespace

DataSource

Usage

Compound types require child filters. Specifically, the `subfilters` property can’t be null if the `type` property is `NOT_`, `AND_`, or
`OR_` .


Apex Reference Guide Filter Class

IN THIS SECTION:

#### Filter Properties Filter Properties The following are properties for Filter .

IN THIS SECTION:

##### columnName

Name of the column that’s being evaluated in a simple comparative type of filter.

##### columnValue

Value that the filter compares records against in a simple comparative type of filter.

##### subfilters

List of subfilters for compound filter types, such as `NOT_`, `AND_`, and `OR_` .

tableName
Name of the table whose column is being evaluated in a simple comparative type of filter.

type
Type of filter operation that limits the returned data.

##### columnName

Name of the column that’s being evaluated in a simple comparative type of filter.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### columnValue

Value that the filter compares records against in a simple comparative type of filter.

Signature

```
   public Object columnValue {get; set;}

```

Property Value

Type: Object

##### subfilters

List of subfilters for compound filter types, such as `NOT_`, `AND_`, and `OR_` .


### Apex Reference Guide FilterType Enum

Signature

```
   public List<DataSource.Filter> subfilters {get; set;}

```

Property Value

Type: List<DataSource.Filter>

##### tableName

Name of the table whose column is being evaluated in a simple comparative type of filter.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

##### type

Type of filter operation that limits the returned data.

Signature

```
   public DataSource.FilterType type {get; set;}

```

Property Value

Type: DataSource.FilterType

### FilterType Enum

##### Referenced by the type property on a DataSource.Filter .

Usage

Determines how to limit the returned data.

Enum Values

The following are the values of the `DataSource.FilterType` enum.

**Value** **Description**

`AND_` This compound filter type returns all rows that match all the subfilters.

`CONTAINS` Simple comparative filter type.

`ENDS_WITH` Simple comparative filter type.


### Apex Reference Guide IdentityType Enum

**Value** **Description**

`EQUALS` Simple comparative filter type.

`GREATER_THAN` Simple comparative filter type.

`GREATER_THAN_OR_EQUAL_TO` Simple comparative filter type.

`LESS_THAN` Simple comparative filter type.

`LESS_THAN_OR_EQUAL_TO` Simple comparative filter type.

`LIKE_` Simple comparative filter type.

`NOT_` This compound filter type returns the rows that don’t match the subfilter.

`NOT_EQUALS` Simple comparative filter type.

`OR_` This compound filter type returns all rows that match any of the subfilters.

`STARTS_WITH` Simple comparative filter type.

### IdentityType Enum

Determines which set of credentials is used to authenticate to the external system.

Usage

The relevant credentials are passed to your `DataSource.Connection` class.

Enum Values

The following are the values of the `DataSource.IdentityType` enum.

**Value** **Description**

`ANONYMOUS` No credentials are used to authenticate to the external system.

```
NAMED_USER

PER_USER

### Order Class

```

The credentials in the external data source definition are used to authenticate to
the external system, regardless of which user is accessing the external data from
your organization.

For queries and searches, the credentials are specific to the current user who invokes
the query or search. The credentials come from the user’s authentication settings
for the external system.

For administrative connections, such as syncing the external system’s schema, the
credentials come from the external data source definition.

Contains details about how to sort the rows in the result set. Equivalent to an `ORDER BY` statement in a SOQL query.


Apex Reference Guide Order Class

Namespace

DataSource

Usage

Used in the `order` property on the `DataSource.TableSelection` class.

IN THIS SECTION:

#### Order Properties

Order Methods

#### Order Properties The following are properties for Order .

IN THIS SECTION:

##### columnName

Name of the column whose values are used to sort the rows in the result set.

##### direction

Direction for sorting rows based on column values.

tableName
Name of the table whose column values are used to sort the rows in the result set.

##### columnName

Name of the column whose values are used to sort the rows in the result set.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### direction

Direction for sorting rows based on column values.

Signature

```
   public DataSource.OrderDirection direction {get; set;}

```

Property Value

Type: DataSource.OrderDirection


Apex Reference Guide Order Class

##### tableName

Name of the table whose column values are used to sort the rows in the result set.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

#### Order Methods The following are methods for Order .

IN THIS SECTION:

##### get(tableName, columnName, direction)

Creates an instance of the DataSource.Order class.

##### get(tableName, columnName, direction)

Creates an instance of the DataSource.Order class.

Signature

```
   public static DataSource.Order get(String tableName, String columnName,

   DataSource.OrderDirection direction)

```

Parameters

##### _`tableName`_

Type: String

Name of the table whose column values are used to sort the rows in the result set.

```
   columnName
```

Type: String

Name of the column whose values are used to sort the rows in the result set.

```
   direction
```

Type: DataSource.OrderDirection

Direction for sorting rows based on column values.

Return Value

Type: DataSource.Order


### Apex Reference Guide OrderDirection Enum OrderDirection Enum

Specifies the direction for sorting rows based on column values.

Usage

Used by the direction property on the DataSource.Order class.

Enum Values

The following are the values of the `DataSource.OrderDirection` enum.

**Value** **Description**

`ASCENDING` Sort rows in ascending order (A–Z).

`DESCENDING` Sort rows in descending order (Z–A).

### Provider Class

Extend this base class to create a custom adapter for Salesforce Connect. The class informs Salesforce of the functional and authentication
capabilities that are supported by or required to connect to the external system. This class extends the `DataSourceUtil` class and
inherits its methods.

Namespace

DataSource

Usage

Create an Apex class that extends `DataSource.Provider` to specify the following.

**•** The types of authentication that can be used to access the external system

**•** The features that are supported for the connection to the external system

**•** The Apex class that extends `DataSource.Connection` to sync the external system’s schema and to handle the queries and
searches of the external data

The values that are returned by the `DataSource.Provider` class determine which settings are available in the external data
source definition in Salesforce. To access the external data source definition from Setup, enter _`External Data Sources`_ in the
`Quick Find` box, then select **External Data Sources** .

IN THIS SECTION:

#### Provider Methods Provider Methods

### The following are methods for Provider .


Apex Reference Guide Provider Class

IN THIS SECTION:

##### getAuthenticationCapabilities()

Returns the types of authentication that can be used to access the external system.

##### getCapabilities()

Returns the functional operations and endpoint settings that the external system supports.

##### getConnection(connectionParams)

Returns a connection that points to an instance of the external data source.

##### getAuthenticationCapabilities()

Returns the types of authentication that can be used to access the external system.

When you call this method, be sure the list of the external system’s authentication capabilities always contains the same values. The
returned authentication types should never change based on runtime conditions, user context, dynamic queries, or any other conditions.
Returning different authentication types for an external system can lead to errors that are difficult to troubleshoot.

For example, if your external system supports OAuth and Anonymous authentication, always return these types every time this method
is called. Don’t query the database, make callouts, or use conditional logic that varies the results of this method.

Signature

```
   public List<DataSource.AuthenticationCapability> getAuthenticationCapabilities()

```

Return Value

Type: List<DataSource.AuthenticationCapability>

##### getCapabilities()

Returns the functional operations and endpoint settings that the external system supports.

When you call this method, be sure the list of the external system’s capabilities always contains the same values. The returned capabilities
should never change based on runtime conditions, user context, dynamic queries, or any other conditions. Returning different capabilities
for an external system can lead to errors that are difficult to troubleshoot.

For example, if your external system supports the `ROW_QUERY` and `SEARCH` operations, always return these capabilities every time
this method is called. Don’t query the database, make callouts, or use conditional logic that varies the results of this method.

Signature

```
   public List<DataSource.Capability> getCapabilities()

```

Return Value

Type: List<DataSource.Capability>

##### getConnection(connectionParams)

Returns a connection that points to an instance of the external data source.


### Apex Reference Guide QueryAggregation Enum

Signature

```
   public DataSource.Connection getConnection(DataSource.ConnectionParams connectionParams)

```

Parameters

```
   connectionParams
```

Type: DataSource.ConnectionParams

Credentials for authenticating to the external system.

Return Value

Type: DataSource.Connection

### QueryAggregation Enum

Specifies how to aggregate a column in a query.

Usage

Used by the aggregation property on the DataSource.ColumnSelection class.

Enum Values

The following are the values of the `DataSource.QueryAggregation` enum.

**Value** **Description**

`AVG` Reserved for future use.

`COUNT` Returns the number of rows that meet the query criteria.

`MAX` Reserved for future use.

`MIN` Reserved for future use.

`NONE` No aggregation.

`SUM` Reserved for future use.

### QueryContext Class An instance of QueryContext is provided to the query method on your DataSource.Connection class. The instance

corresponds to a SOQL request.

Namespace

DataSource


Apex Reference Guide QueryContext Class

IN THIS SECTION:

#### QueryContext Properties QueryContext Methods QueryContext Properties The following are properties for QueryContext .

IN THIS SECTION:

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results.

##### tableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results.

Signature

```
   public String queryMoreToken {get; set;}

```

Property Value

Type: String

##### tableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

Signature

```
   public DataSource.TableSelection tableSelection {get; set;}

```

Property Value

Type: DataSource.TableSelection

#### QueryContext Methods The following are methods for QueryContext .

IN THIS SECTION:

get(metadata, offset, maxResults, tableSelection)
#### Creates an instance of the QueryContext class.


### Apex Reference Guide QueryUtils Class

##### get(metadata, offset, maxResults, tableSelection)

Creates an instance of the `QueryContext` class.

Signature

```
   public static DataSource.QueryContext get(List<DataSource.Table> metadata, Integer

   offset, Integer maxResults, DataSource.TableSelection tableSelection)

```

Parameters

```
   metadata
```

Type: List<DataSource.Table>

List of table metadata that describes the external system’s tables to query.

```
   offset
```

Type: Integer

Used for client-driven paging. Specifies the starting row offset into the query’s result set.

```
   maxResults
```

Type: Integer

Used for client-driven paging. Specifies the maximum number of rows to return in each batch.

```
   tableSelection
```

Type: DataSource.TableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

Return Value

Type: `DataSource.QueryContext`

### QueryUtils Class

Contains helper methods to locally filter, sort, and apply limit and offset clauses to data rows. This helper class is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

Namespace

DataSource

Usage

The `DataSource.QueryUtils` class and its helper methods can process query results locally within your Salesforce org. This class
is provided for your convenience to simplify the development of your Salesforce Connect custom adapter for initial tests. However, the
`DataSource.QueryUtils` class and its methods aren’t supported for use in production environments that use callouts to retrieve
data from external systems. Complete the filtering and sorting on the external system before sending the query results to Salesforce.
When possible, use server-driven paging or another technique to have the external system determine the appropriate data subsets
according to the limit and offset clauses in the query.


Apex Reference Guide QueryUtils Class

IN THIS SECTION:

#### QueryUtils Methods QueryUtils Methods The following are methods for QueryUtils .

IN THIS SECTION:

##### applyLimitAndOffset(queryContext, rows)

Returns a subset of data rows after locally applying limit and offset clauses from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

filter(queryContext, rows)
Returns a subset of data rows after locally ordering and applying filters from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

process(queryContext, rows)
Returns data rows after locally filtering, sorting, ordering, and applying limit and offset clauses from the query. This helper method
is provided for your convenience during early development and tests, but it isn’t supported for use in production environments.

sort(queryContext, rows)
Returns data rows after locally sorting and applying the order from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

##### applyLimitAndOffset(queryContext, rows)

Returns a subset of data rows after locally applying limit and offset clauses from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,Object>> applyLimitAndOffset(DataSource.QueryContext

   queryContext, List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>


Apex Reference Guide QueryUtils Class

##### filter(queryContext, rows)

Returns a subset of data rows after locally ordering and applying filters from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,object>> filter(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

queryContext

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>

##### process(queryContext, rows)

Returns data rows after locally filtering, sorting, ordering, and applying limit and offset clauses from the query. This helper method is
provided for your convenience during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,object>> process(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>


### Apex Reference Guide ReadContext Class

##### sort(queryContext, rows)

Returns data rows after locally sorting and applying the order from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,ject>> sort(DataSource.QueryContext queryContext,

   List<Map<String,object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>

### ReadContext Class

Abstract base class for the `QueryContext` and `SearchContext` classes.

Namespace

DataSource

IN THIS SECTION:

#### ReadContext Properties ReadContext Properties

### The following are properties for ReadContext .

IN THIS SECTION:

maxResults
Maximum number of rows that the query can return.

metadata
Describes the external system’s tables to query.

offset
The starting row offset into the query’s result set. Used for client-driven paging.


### Apex Reference Guide SearchContext Class

##### maxResults

Maximum number of rows that the query can return.

Signature

```
   public Integer maxResults {get; set;}

```

Property Value

Type: Integer

##### metadata

Describes the external system’s tables to query.

Signature

```
   public List<DataSource.Table> metadata {get; set;}

```

Property Value

Type: List<DataSource.Table>

##### offset

The starting row offset into the query’s result set. Used for client-driven paging.

Signature

```
   public Integer offset {get; set;}

```

Property Value

Type: Integer

### SearchContext Class An instance of SearchContext is provided to the search method on your DataSource.Connection class. The instance

corresponds to a search or SOSL request.

Namespace

DataSource

IN THIS SECTION:

SearchContext Constructors

SearchContext Properties


Apex Reference Guide SearchContext Class

#### SearchContext Constructors The following are constructors for SearchContext .

IN THIS SECTION:

##### SearchContext(metadata, offset, maxResults, tableSelections, searchPhrase)
#### Creates an instance of the SearchContext class with the specified parameter values.

##### SearchContext()
#### Creates an instance of the SearchContext class.

##### SearchContext(metadata, offset, maxResults, tableSelections, searchPhrase)

#### Creates an instance of the SearchContext class with the specified parameter values.

Signature

```
   public SearchContext(List<DataSource.Table> metadata, Integer offset, Integer maxResults,

   List<DataSource.TableSelection> tableSelections, String searchPhrase)

```

Parameters

```
   metadata
```

Type: List<DataSource.Table>

List of table metadata that describes the external system’s tables to query.

```
   offset
```

Type: Integer

Specifies the starting row offset into the query’s result set.

```
   maxResults
```

Type: Integer

Specifies the maximum number of rows to return in each batch.

```
   tableSelections
```

Type: List<DataSource.TableSelection>

List of queries and their details. The details represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in each SOQL or SOSL
query.

```
   searchPhrase
```

Type: String

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

##### SearchContext()

#### Creates an instance of the SearchContext class.

Signature

```
   public SearchContext()

```


### Apex Reference Guide SearchUtils Class

#### SearchContext Properties The following are properties for SearchContext .

IN THIS SECTION:

##### searchPhrase

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

##### tableSelections

List of queries and their details. The details represent the FROM, ORDER BY, SELECT, and WHERE clauses in each SOQL or SOSL query.

##### searchPhrase

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

Signature

```
   public String searchPhrase {get; set;}

```

Property Value

Type: String

##### tableSelections

List of queries and their details. The details represent the FROM, ORDER BY, SELECT, and WHERE clauses in each SOQL or SOSL query.

Signature

```
   public List<DataSource.TableSelection> tableSelections {get; set;}

```

Property Value

Type: List<DataSource.TableSelection>

### SearchUtils Class

Helper class for implementing search on a custom adapter for Salesforce Connect.

Namespace

DataSource

Usage

We recommend that you develop your own search implementation that can search columns in addition to the designated name field.

IN THIS SECTION:

SearchUtils Methods


### Apex Reference Guide Table Class

#### SearchUtils Methods The following are methods for SearchUtils .

IN THIS SECTION:

##### searchByName(searchDetails, connection)

Queries all the tables and returns each row whose designated name field contains the search phrase.

##### searchByName(searchDetails, connection)

Queries all the tables and returns each row whose designated name field contains the search phrase.

Signature

```
   public static List<DataSource.TableResult> searchByName(DataSource.SearchContext

   searchDetails, DataSource.Connection connection)

```

Parameters

```
   searchDetails
```

Type: DataSource.SearchContext

The `SearchContext` class that specifies which data to search and what to search for.

```
   connection
```

Type: DataSource.Connection

The `DataSource.Connection` class that connects to the external system.

Return Value

Type: List<DataSource.TableResult>

### Table Class

Describes a table on an external system that the Salesforce Connect custom adapter connects to. This class extends the
`DataSourceUtil` class and inherits its methods.

Namespace

DataSource

Usage

A list of table metadata is provided by the `DataSource.Connection` class when the `sync()` method is invoked. Each table
can become an external object in Salesforce.

The metadata is stored in Salesforce. Updating the Apex code to return new or updated values for the table metadata doesn’t automatically
update the stored metadata in Salesforce.


Apex Reference Guide Table Class

IN THIS SECTION:

#### Table Properties

Table Methods

#### Table Properties The following are properties for Table .

IN THIS SECTION:

##### columns

List of table columns.

##### description

Description of what the table represents.

labelPlural
Plural form of the user-friendly name for the table. The `labelPlural` becomes the object’s plural label in the Salesforce user
interface.

labelSingular
Singular form of the user-friendly name for the table. The `labelSingular` becomes the object label in the Salesforce user
interface. We recommend that you make object labels unique across all standard, custom, and external objects in the org.

name
Name of the table on the external system.

nameColumn
Name of the table column that becomes the name field of the external object when the administrator syncs the table.

##### columns

List of table columns.

Signature

```
   public List<DataSource.Column> columns {get; set;}

```

Property Value

Type: List<DataSource.Column>

##### description

Description of what the table represents.

Signature

```
   public String description {get; set;}

```


Apex Reference Guide Table Class

Property Value

Type: String

##### labelPlural Plural form of the user-friendly name for the table. The labelPlural becomes the object’s plural label in the Salesforce user interface.

Signature

```
   public String labelPlural {get; set;}

   DataSource.Table, labelPlural

```

Property Value

Type: String

##### labelSingular Singular form of the user-friendly name for the table. The labelSingular becomes the object label in the Salesforce user interface.

We recommend that you make object labels unique across all standard, custom, and external objects in the org.

Signature

```
   public String labelSingular {get; set;}

```

Property Value

Type: String

##### name

Name of the table on the external system.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### nameColumn

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

Signature

```
   public String nameColumn {get; set;}

```


Apex Reference Guide Table Class

Property Value

Type: String

#### Table Methods The following are methods for Table .

IN THIS SECTION:

##### get(name, labelSingular, labelPlural, description, nameColumn, columns)

Returns the table metadata with the specified parameter values.

get(name, nameColumn, columns)
Returns the table metadata with the specified parameter values, using the name for the labels and description.

##### get(name, labelSingular, labelPlural, description, nameColumn, columns)

Returns the table metadata with the specified parameter values.

Signature

```
   public static DataSource.Table get(String name, String labelSingular, String labelPlural,

   String description, String nameColumn, List<DataSource.Column> columns)

```

Parameters

```
   name
```

Type: String

Name of the external table.

```
   labelSingular
```

Type: String

Singular form of the user-friendly name for the table. The `labelSingular` becomes the object label in the Salesforce user
interface.

```
   labelPlural
```

Type: String

Plural form of the user-friendly name for the table. The `labelPlural` becomes the object’s plural label in the Salesforce user
interface.

```
   description
```

Type: String

Description of the external table.

```
   nameColumn
```

Type: String

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

```
   columns
```

Type: List<DataSource.Column>

List of table columns.


### Apex Reference Guide TableResult Class

Return Value

Type: DataSource.Table

##### get(name, nameColumn, columns)

Returns the table metadata with the specified parameter values, using the name for the labels and description.

Signature

```
   public static DataSource.Table get(String name, String nameColumn,

   List<DataSource.Column> columns)

   DataSource.Table, get, [String, String, List<DataSource.Column>], DataSource.Table

```

Parameters

```
   name
```

Type: String

Name of the external table.

```
   nameColumn
```

Type: String

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

```
   columns
```

Type: List<DataSource.Column>

List of table columns.

Return Value

Type: DataSource.Table

The returned table metadata has these property values.

**Property** **Value**

name _`name`_

labelSingular _`name`_

labelPlural _`name`_

description _`name`_

nameColumn _`nameColumn`_

columns _`columns`_

### TableResult Class

Contains the results of a search or query.


Apex Reference Guide TableResult Class

Namespace

DataSource

IN THIS SECTION:

#### TableResult Properties

TableResult Methods

#### TableResult Properties The following are properties for TableResult .

IN THIS SECTION:

##### errorMessage errorMessage queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results. This token is passed back
##### to the Apex data source on subsequent queries in the queryMoreToken property on the QueryContext .

rows
Rows of data.

success
Whether the search or query was successful.

tableName
Name of the table that was queried.

totalSize
The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

##### errorMessage errorMessage

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results. This token is passed back to
##### the Apex data source on subsequent queries in the queryMoreToken property on the QueryContext .


Apex Reference Guide TableResult Class

Signature

```
   public String queryMoreToken {get; set;}

```

Property Value

Type: String

##### rows

Rows of data.

Signature

```
   public List<Map<String,Object>> rows {get; set;}

```

Property Value

Type: List<Map<String, Object>>

##### success

Whether the search or query was successful.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

##### tableName

Name of the table that was queried.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

##### totalSize

The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

Signature

```
   public Integer totalSize {get; set;}

```


Apex Reference Guide TableResult Class

Property Value

Type: Integer

#### TableResult Methods The following are methods for TableResult .

IN THIS SECTION:

##### error(errorMessage)

Returns failed search or query results with the provided error message.

get(success, errorMessage, tableName, rows, totalSize)
#### Returns a subset of data rows in a TableResult with the provided property values and the number of rows in the table.

get(success, errorMessage, tableName, rows)
#### Returns a subset of data rows in a TableResult with the provided property values.

get(queryContext, rows)
#### Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a TableResult .

get(tableSelection, rows)
#### Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a TableResult .

##### error(errorMessage)

Returns failed search or query results with the provided error message.

Signature

```
   public static DataSource.TableResult error(String errorMessage)

```

Parameters

```
   errorMessage
```

Type: String

errorMessage

Return Value

Type: DataSource.TableResult

#### The returned TableResult has these property values.

**Property** **Value**

success false

errorMessage _`errorMessage`_

tableName null

rows null


Apex Reference Guide TableResult Class

**Property** **Value**

rows.size() 0

##### get(success, errorMessage, tableName, rows, totalSize)

Returns a subset of data rows in a `TableResult` with the provided property values and the number of rows in the table.

Signature

```
   public static DataSource.TableResult get(Boolean success, String errorMessage, String

   tableName, List<Map<String,Object>> rows, Integer totalSize)

```

Parameters

```
   success
```

Type: Boolean

Whether the search or query was successful.

```
   errorMessage
```

Type: String

errorMessage

```
   tableName
```

Type: String

Name of the table that was queried.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

```
   totalSize
```

Type: Integer

The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

Return Value

Type: DataSource.TableResult

##### get(success, errorMessage, tableName, rows)

Returns a subset of data rows in a `TableResult` with the provided property values.

Signature

```
   public static DataSource.TableResult get(Boolean success, String errorMessage, String

   tableName, List<Map<String,Object>> rows)

```


Apex Reference Guide TableResult Class

Parameters

```
   success
```

Type: Boolean

Whether the search or query was successful.

```
   errorMessage
```

Type: String

errorMessage

```
   tableName
```

Type: String

Name of the table that was queried.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

##### get(queryContext, rows)

Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a `TableResult` .

Signature

```
   public static DataSource.TableResult get(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

##### get(tableSelection, rows)

Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a `TableResult` .


### Apex Reference Guide TableSelection Class

Signature

```
   public static DataSource.TableResult get(DataSource.TableSelection tableSelection,

   List<Map<String,Object>> rows)

```

Parameters

```
   tableSelection
```

Type: DataSource.TableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

### TableSelection Class

Contains a breakdown of the SOQL or SOSL query. Its properties represent the FROM, ORDER BY, SELECT, and WHERE clauses in the
query.

Namespace

DataSource

IN THIS SECTION:

#### TableSelection Properties TableSelection Properties

### The following are properties for TableSelection .

IN THIS SECTION:

columnsSelected
List of columns to query. Corresponds to the `SELECT` clause in a SOQL or SOSL query.

filter
Identifies the query filter, which can be a compound filter that has a list of subfilters. The filter corresponds to the `WHERE` clause in
a SOQL or SOSL query.

order
Identifies the order for sorting the query results. Corresponds to the `ORDER BY` clause in a SOQL or SOSL query.

tableSelected
Name of the table to query. Corresponds to the `FROM` clause in a SOQL or SOSL query.


Apex Reference Guide TableSelection Class

##### columnsSelected

List of columns to query. Corresponds to the `SELECT` clause in a SOQL or SOSL query.

Signature

```
   public List<DataSource.ColumnSelection> columnsSelected {get; set;}

```

Property Value

Type: List<DataSource.ColumnSelection>

##### filter

Identifies the query filter, which can be a compound filter that has a list of subfilters. The filter corresponds to the `WHERE` clause in a
SOQL or SOSL query.

Signature

```
   public DataSource.Filter filter {get; set;}

```

Property Value

Type: DataSource.Filter

##### order

Identifies the order for sorting the query results. Corresponds to the `ORDER BY` clause in a SOQL or SOSL query.

Signature

```
   public List<DataSource.Order> order {get; set;}

```

Property Value

Type: List<DataSource.Order>

##### tableSelected

Name of the table to query. Corresponds to the `FROM` clause in a SOQL or SOSL query.

Signature

```
   public String tableSelected {get; set;}

```

Property Value

Type: String


### Apex Reference Guide UpsertContext Class UpsertContext Class An instance of UpsertContext is passed to the upsertRows() method on your Datasource.Connection class. This

class provides context information about the upsert request to the implementor of `upsertRows()` .

Namespace

DataSource

Usage

The Apex Connector Framework creates the contet for operations. Context is comprised of parameters about the operations, which
### other methods can use. An instance of the UpsertContext class packages these parameters into an object that can be used when

an `upsertRows()` operation is initiated.

IN THIS SECTION:

#### UpsertContext Properties UpsertContext Properties

### The following are properties for UpsertContext .

IN THIS SECTION:

##### rows

List of rows corresponding to the external object records to upsert.

##### tableSelected

The name of the table to upsert rows in.

##### rows

List of rows corresponding to the external object records to upsert.

Signature

```
   public List<Map<String,ANY>> rows {get; set;}

```

Property Value

Type: List<Map<String,Object>>

##### tableSelected

The name of the table to upsert rows in.

Signature

```
   public String tableSelected {get; set;}

```


### Apex Reference Guide UpsertResult Class

Property Value

Type: String

### UpsertResult Class

Represents the result of an upsert operation on an external object record. The result is returned by the `upsertRows` method of the
`DataSource.Connection` class.

Namespace

DataSource

Usage

An upsert operation on external object records generates an array of objects of type `DataSource.UpsertResult` . Its methods
create result records that indicate whether the upsert operation succeeded or failed.

IN THIS SECTION:

#### UpsertResult Properties

UpsertResult Methods

#### UpsertResult Properties

### The following are properties for UpsertResult .

IN THIS SECTION:

##### errorMessage

The error message that’s generated by a failed upsert operation.

externalId
The unique identifier of a row that represents an external object record to upsert.

success
Indicates whether a delete operation succeeded or failed.

##### errorMessage

The error message that’s generated by a failed upsert operation.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String


Apex Reference Guide UpsertResult Class

##### externalId

The unique identifier of a row that represents an external object record to upsert.

Signature

```
   public String externalId {get; set;}

```

Property Value

Type: String

##### success

Indicates whether a delete operation succeeded or failed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### UpsertResult Methods The following are methods for UpsertResult .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type UpsertResult by determining the equality of external object records in a list. This method
##### is dynamic and is based on the equals method in Java.

failure(externalId, errorMessage)
Creates an upsert result that indicates the failure of a delete request for a given external ID.

hashCode()
#### Maintains the integrity of lists of type UpsertResult by determining the uniqueness of the external object records in a list.

##### success(externalId)

Creates a delete result that indicates the successful completion of an upsert request for a given external ID.

##### equals(obj)

#### Maintains the integrity of lists of type UpsertResult by determining the equality of external object records in a list. This method is
##### dynamic and is based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```


Apex Reference Guide UpsertResult Class

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### failure(externalId, errorMessage)

Creates an upsert result that indicates the failure of a delete request for a given external ID.

Signature

```
   public static DataSource.UpsertResult failure(String externalId, String errorMessage)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the external object record to upsert.

```
   errorMessage
```

Type: String

The reason the upsert operation failed.

Return Value

Type: DataSource.UpsertResult

Status result for the upsert operation.

##### hashCode()

Maintains the integrity of lists of type `UpsertResult` by determining the uniqueness of the external object records in a list.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### success(externalId)

Creates a delete result that indicates the successful completion of an upsert request for a given external ID.


### Apex Reference Guide DataSource Exceptions

Signature

```
   public static DataSource.UpsertResult success(String externalId)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the external object record to upsert.

Return Value

Type: DataSource.UpsertResult

Status result of the upsert operation for the external object record with the given external ID.

### DataSource Exceptions The DataSource namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The DataSource namespace contains these exceptions.

**Exception** **Description** **Methods**

To get the error message and write it
to debug log, use the `String`

`getMessage()` .

To get the error message and write it
to debug log, use the `String`

`getMessage()` .

```
DataSource.DataSourceException

DataSource.OAuthTokenExpiredException

## DataWeave Namespace

```

Throw this exception to indicate that an
error occurred while communicating with
an external data source.

Throw this exception to indicate that an
OAuth token has expired. The system then
attempts to refresh the token
automatically and restart the query, search,
or sync operation.

The DataWeave namespace provides classes and methods to support the invocation of DataWeave scripts from Apex.

DataWeave is the MuleSoft expression language for accessing, parsing, and transforming data that travels through a Mule application.
[For detailed information, see DataWeave Language.](https://docs.mulesoft.com/mule-runtime/4.3/dataweave)

## These are the classes in the DataWeave namespace.

IN THIS SECTION:

Result Class
Contains methods to retrieve data that was transformed using Script class methods.


### Apex Reference Guide Result Class

Script Class
Contains the `createScript()` method to load DataWeave scripts and the `execute()` method to obtain script output in
a `DataWeave.Result` object.

SEE ALSO:

[DataWeave in Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/DataWeaveInApex.htm)

### Result Class

Contains methods to retrieve data that was transformed using Script class methods.

Namespace

DataWeave

Example

See Script Class for an example to run a DataWeave script from Apex and retrieve the resulting script output.

IN THIS SECTION:

#### Result Methods Result Methods

### The following are methods for Result .

IN THIS SECTION:

##### getValue()

Returns the result of a DataWeave script execution as an object.

getValueAsString()
Returns the result of a DataWeave script execution as a string value.

##### **`getValue()`**

Returns the result of a DataWeave script execution as an object.

Signature

```
   public Object getValue()

```

Return Value

Type: Object


### Apex Reference Guide Script Class

##### **`getValueAsString()`**

Returns the result of a DataWeave script execution as a string value.

Signature

```
   public String getValueAsString()

```

Return Value

Type: String

### Script Class

Contains the `createScript()` method to load DataWeave scripts and the `execute()` method to obtain script output in a
`DataWeave.Result` object.

Namespace

DataWeave

This example runs a DataWeave script from Apex and retrieves the resulting script output. First deploy the script to the org as
`ContactsToJson.dwl` .

```
   %dw 2.0

   input records application/java

   output application/json

   --
   {

     users: records map(record) -> {

      firstName: record.FirstName,

      lastName: record.LastName

     }

```

Then, execute the script from Apex.

```
   List<Contact> data = [SELECT FirstName, LastName FROM Contact WHERE LastName LIMIT 5];

   Map<String, Object> args = new Map<String, Object>{ 'records' => data };

   DataWeave.Script script = DataWeave.Script.createScript('ContactsToJson');

   DataWeave.Result result = script.execute(args);

   string jsonOutput = result.getValueAsString();

```

IN THIS SECTION:

#### Script Methods Script Methods

### The following are methods for Script .


Apex Reference Guide Script Class

IN THIS SECTION:

##### createScript(scriptName)

Loads a DataWeave 2.0 script from the `.dwl` metadata file that is deployed in an org. The script can then be run using the
`Script.execute` method.

##### createScript(namespace, scriptName)

Loads a DataWeave 2.0 script from a specified namespace. The script can then be run using the `Script.execute` method.

execute(parameters)
Executes the DataWeave script that is loaded using the `createScript()` method and returns the script output.

toString()
Returns the name of the script.

##### **`createScript(scriptName)`**

Loads a DataWeave 2.0 script from the `.dwl` metadata file that is deployed in an org. The script can then be run using the
`Script.execute` method.

Signature

```
   public static createScript(String scriptName)

```

Parameters

```
   scriptName
```

Type: String

The name of the deployed metadata `.dwl` script (not including the file extension).

Return Value

Type: DataWeave.Script

DataWeave script that is used as a parameter in the `Script.execute()` method.

##### **`createScript(namespace, scriptName)`**

Loads a DataWeave 2.0 script from a specified namespace. The script can then be run using the `Script.execute` method.

Signature

```
   public static dataweave.Script createScript(String namespace, String scriptName)

```

Parameters

```
   namespace
```

Type: String

The namespace name for the deployed script. If the namespace name is null, the caller namespace is used. If the namespace name
is empty, the org namespace is used.

```
   scriptName
```

Type: String


## Apex Reference Guide Dom Namespace

The name of the deployed metadata `.dwl` script (not including the file extension).

Return Value

Type: DataWeave.Script

DataWeave script that is used as a parameter in the `Script.execute()` method.

##### **`execute(parameters)`**

Executes the DataWeave script that is loaded using the `createScript()` method and returns the script output.

Signature

```
   public execute(Map<String,Object> parameters)

```

Parameters

```
   parameters
```

Type: Map<String,Object>

Input to the DataWeave script. The keys correspond to the input directive names defined in the DataWeave header.

[See Input Directive and DataWeave Header.](https://docs.mulesoft.com/dataweave/1.2/dataweave-language-introduction#input-directive)

Return Value

Type: DataWeave.Result

The `DataWeave.Result` object contains the script output.

##### **`toString()`**

Returns the name of the script.

Signature

```
   public String toString()

```

Return Value

Type: String

## Dom Namespace The Dom namespace provides classes and methods for parsing and creating XML content. The following are the classes in the Dom namespace.

IN THIS SECTION:

Document Class
Use the `Document` class to process XML content. You can parse nested XML content that’s up to 50 nodes deep.


### Apex Reference Guide Document Class

XmlNode Class
Use the `XmlNode` class to work with a node in an XML document.

XmlNodeType Enum
Specifies the node type in an XML document.

### Document Class Use the Document class to process XML content. You can parse nested XML content that’s up to 50 nodes deep.

Namespace

Dom

Usage

One common application is to use it to create the body of a request for HttpRequest or to parse a response accessed by HttpResponse.

IN THIS SECTION:

#### Document Constructors Document Methods

SEE ALSO:

[Reading and Writing XML Using the DOM](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_dom.htm)

#### Document Constructors

### The following are constructors for Document .

IN THIS SECTION:

##### Document()

Creates a new instance of the `Dom.Document` class.

##### Document()

Creates a new instance of the `Dom.Document` class.

Signature

```
   public Document()

#### Document Methods

### The following are methods for Document . All are instance methods.

```


Apex Reference Guide Document Class

IN THIS SECTION:

##### createRootElement(name, namespace, prefix)

Creates the top-level root element for a document.

##### getRootElement()

Returns the top-level root element node in the document. If this method returns `null`, the root element has not been created yet.

load(xml)
Parse the XML representation of the document specified in the _`xml`_ argument and load it into a document.

toXmlString()
Returns the XML representation of the document as a String.

##### createRootElement(name, namespace, prefix)

Creates the top-level root element for a document.

Signature

```
   public Dom.XmlNode createRootElement(String name, String namespace, String prefix)

```

Parameters

```
   name
```

Type: String

```
   namespace
```

Type: String

```
   prefix
```

Type: String

Return Value

Type: Dom.XmlNode

Usage

[For more information about namespaces, see Reading and Writing XML Using the DOM.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_dom.htm)

Calling this method more than once on a document generates an error as a document can have only one root element.

##### getRootElement()

Returns the top-level root element node in the document. If this method returns `null`, the root element has not been created yet.

Signature

```
   public Dom.XmlNode getRootElement()

```

Return Value

Type: Dom.XmlNode


### Apex Reference Guide XmlNode Class

##### load(xml)

Parse the XML representation of the document specified in the _`xml`_ argument and load it into a document.

Signature

```
   public Void load(String xml)

```

Parameters

```
   xml
```

Type: String

Return Value

Type: Void

Example

```
   Dom.Document doc = new Dom.Document();

   doc.load(xml);

##### toXmlString()

```

Returns the XML representation of the document as a String.

Signature

```
   public String toXmlString()

```

Return Value

Type: String

### XmlNode Class Use the XmlNode class to work with a node in an XML document.

Namespace

Dom

#### XmlNode Methods

### The following are methods for XmlNode . All are instance methods.

IN THIS SECTION:

addChildElement(name, namespace, prefix)
Creates a child element node for this node.


Apex Reference Guide XmlNode Class

addCommentNode(text)
Creates a child comment node for this node.

addTextNode(text)
Creates a child text node for this node.

getAttribute(key, keyNamespace)
Returns _`namespacePrefix:attributeValue`_ for the given key and key namespace.

getAttributeCount()
Returns the number of attributes for this node.

getAttributeKeyAt(index)
Returns the attribute key for the given index. Index values start at 0.

getAttributeKeyNsAt(index)
Returns the attribute key namespace for the given index.

getAttributeValue(key, keyNamespace)
Returns the attribute value for the given key and key namespace.

getAttributeValueNs(key, keyNamespace)
Returns the attribute value namespace for the given key and key namespace.

getChildElement(name, namespace)
Returns the child element node for the node with the given name and namespace.

getChildElements()
Returns the child element nodes for this node. This doesn't include child text or comment nodes.

getChildren()
Returns the child nodes for this node. This includes all node types.

getName()
Returns the element name.

getNamespace()
Returns the namespace of the element.

getNamespaceFor(prefix)
Returns the namespace of the element for the given prefix.

getNodeType()
Returns the node type.

getParent()
Returns the parent of this element.

getPrefixFor(namespace)
Returns the prefix of the given namespace.

getText()
Returns the text for this node.

insertBefore(newChild, refChild)
Inserts a new child node before the specified node.

removeAttribute(key, keyNamespace)
Removes the attribute with the given key and key namespace. Returns `true` if successful, `false` otherwise.


Apex Reference Guide XmlNode Class

removeChild(childNode)
Removes the given child node.

setAttribute(key, value)
Sets the key attribute value.

setAttributeNs(key, value, keyNamespace, valueNamespace)
Sets the key attribute value.

setNamespace(prefix, namespace)
Sets the namespace for the given prefix.

##### addChildElement(name, namespace, prefix)

Creates a child element node for this node.

Signature

```
   public Dom.XmlNode addChildElement(String name, String namespace, String prefix)

```

Parameters

```
   name
```

Type: String

The _`name`_ argument can't have a `null` value.

```
   namespace
```

Type: String

```
   prefix
```

Type: String

Return Value

Type: Dom.XmlNode

Usage

**•** If the _`namespace`_ argument has a non- `null` value and the _`prefix`_ argument is `null`, the namespace is set as the default
namespace.

**•** If the _`prefix`_ argument is `null`, Salesforce automatically assigns a prefix for the element. The format of the automatic prefix is
`ns` _**`i`**_, where _`i`_ is a number.If the _`prefix`_ argument is `''`, the namespace is set as the default namespace.

##### addCommentNode(text)

Creates a child comment node for this node.

Signature

```
   public Dom.XmlNode addCommentNode(String text)

```


Apex Reference Guide XmlNode Class

Parameters

```
   text
```

Type: String

The _`text`_ argument can't have a `null` value.

Return Value

Type: Dom.XmlNode

##### addTextNode(text)

Creates a child text node for this node.

Signature

```
   public Dom.XmlNode addTextNode(String text)

```

Parameters

```
   text
```

Type: String

The _`text`_ argument can't have a `null` value.

Return Value

Type: Dom.XmlNode

##### getAttribute(key, keyNamespace)

Returns _`namespacePrefix:attributeValue`_ for the given key and key namespace.

Signature

```
   public String getAttribute(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

Example

For example, for the `<xyz a:b="c:d" />` element:


Apex Reference Guide XmlNode Class

##### • getAttribute returns c:d

**•** `getAttributeValue` returns `d`

##### getAttributeCount()

Returns the number of attributes for this node.

Signature

```
   public Integer getAttributeCount()

```

Return Value

Type: Integer

##### getAttributeKeyAt(index)

Returns the attribute key for the given index. Index values start at 0.

Signature

```
   public String getAttributeKeyAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

##### getAttributeKeyNsAt(index)

Returns the attribute key namespace for the given index.

Signature

```
   public String getAttributeKeyNsAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String


Apex Reference Guide XmlNode Class

##### getAttributeValue(key, keyNamespace)

Returns the attribute value for the given key and key namespace.

Signature

```
   public String getAttributeValue(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

Example

For example, for the `<xyz a:b="c:d" />` element:

##### • getAttribute returns c:d • getAttributeValue returns d getAttributeValueNs(key, keyNamespace)

Returns the attribute value namespace for the given key and key namespace.

Signature

```
   public String getAttributeValueNs(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

##### getChildElement(name, namespace)

Returns the child element node for the node with the given name and namespace.


Apex Reference Guide XmlNode Class

Signature

```
   public Dom.XmlNode getChildElement(String name, String namespace)

```

Parameters

```
   name
```

Type: String

```
   namespace
```

Type: String

Return Value

Type: Dom.XmlNode

##### getChildElements()

Returns the child element nodes for this node. This doesn't include child text or comment nodes.

Signature

```
   public Dom.XmlNode[] getChildElements()

```

Return Value

Type: Dom.XmlNode[]

##### getChildren()

Returns the child nodes for this node. This includes all node types.

Signature

```
   public Dom.XmlNode[] getChildren()

```

Return Value

Type: Dom.XmlNode[]

##### getName()

Returns the element name.

Signature

```
   public String getName()

```

Return Value

Type: String


Apex Reference Guide XmlNode Class

##### getNamespace()

Returns the namespace of the element.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

##### getNamespaceFor(prefix)

Returns the namespace of the element for the given prefix.

Signature

```
   public String getNamespaceFor(String prefix)

```

Parameters

```
   prefix
```

Type: String

Return Value

Type: String

##### getNodeType()

Returns the node type.

Signature

```
   public Dom.XmlNodeType getNodeType()

```

Return Value

Type: Dom.XmlNodeType

Uses `XmlNodeType` enum to return _`COMMENT`_, _`ELEMENT`_, or _`TEXT`_ as the node type.

##### getParent()

Returns the parent of this element.

Signature

```
   public Dom.XmlNode getParent()

```


Apex Reference Guide XmlNode Class

Return Value

Type: Dom.XmlNode

##### getPrefixFor(namespace)

Returns the prefix of the given namespace.

Signature

```
   public String getPrefixFor(String namespace)

```

Parameters

```
   namespace
```

Type: String

The _`namespace`_ argument can't have a `null` value.

Return Value

Type: String

##### getText()

Returns the text for this node.

Signature

```
   public String getText()

```

Return Value

Type: String

##### insertBefore(newChild, refChild)

Inserts a new child node before the specified node.

Signature

```
   public Dom.XmlNode insertBefore(Dom.XmlNode newChild, Dom.XmlNode refChild)

```

Parameters

```
   newChild
```

Type: Dom.XmlNode

The node to insert.

```
   refChild
```

Type: Dom.XmlNode

The node before the new node.


Apex Reference Guide XmlNode Class

Return Value

Type: Dom.XmlNode

Usage

**•** If _`refChild`_ is `null`, _`newChild`_ is inserted at the end of the list.

**•** If _`refChild`_ doesn't exist, an exception is thrown.

##### removeAttribute(key, keyNamespace)

Removes the attribute with the given key and key namespace. Returns `true` if successful, `false` otherwise.

Signature

```
   public Boolean removeAttribute(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: Boolean

##### removeChild(childNode)

Removes the given child node.

Signature

```
   public Boolean removeChild(Dom.XmlNode childNode)

```

Parameters

```
   childNode
```

Type: Dom.XmlNode

Return Value

Type: Boolean

##### setAttribute(key, value)

Sets the key attribute value.


Apex Reference Guide XmlNode Class

Signature

```
   public Void setAttribute(String key, String value)

```

Parameters

```
   key
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void

##### setAttributeNs(key, value, keyNamespace, valueNamespace)

Sets the key attribute value.

Signature

```
   public Void setAttributeNs(String key, String value, String keyNamespace, String

   valueNamespace)

```

Parameters

```
   key
```

Type: String

```
   value
```

Type: String

```
   keyNamespace
```

Type: String

```
   valueNamespace
```

Type: String

Return Value

Type: Void

##### setNamespace(prefix, namespace)

Sets the namespace for the given prefix.

Signature

```
   public Void setNamespace(String prefix, String namespace)

```


### Apex Reference Guide XmlNodeType Enum

Parameters

```
   prefix
```

Type: String

```
   namespace
```

Type: String

Return Value

Type: Void

### XmlNodeType Enum

Specifies the node type in an XML document.

Usage

### Use XMLNodeType enum with the getNodeType() method in the XmlNode class.

Enum Values

The following are the values of the `Dom.XMLNodeType` enum.

**Value** **Description**

`COMMENT` Dom node of type comment.

`ELEMENT` Dom node of type element.

`TEXT` Dom node of type text.

## embeddedai Namespace The embeddedai namespace provides classes and methods to manage and represent records and data in Apex to support embedded

AI features.

## These are the classes in the embeddedai namespace.

IN THIS SECTION:

### ApexMap Class

Create, clone, and convert string based key-value pairs to a JSON string format.

RecordApexRepresentation Class
Contains properties and a method to create a serializable representation of a record and its associated data for AI service integration
and data processing.

### ApexMap Class

Create, clone, and convert string based key-value pairs to a JSON string format.


Apex Reference Guide ApexMap Class

Namespace

embeddedai

IN THIS SECTION:

#### ApexMap Constructors

Learn more about the constructors available with the ApexMap class.

ApexMap Properties

ApexMap Methods
Create a copy of the ApexMap object and convert key-value pairs to string format.

#### ApexMap Constructors

Learn more about the constructors available with the ApexMap class.

#### The ApexMap class includes these constructors.

IN THIS SECTION:

##### ApexMap(key, value)

Initializes a new instance of the ApexMap class by assigning the specified key and value. This constructor creates a single key–value
entry that can be included in an embedded AI Apex map for passing contextual data to embedded AI logic.

ApexMap()
Initializes the ApexMap class.

##### **`ApexMap(key, value)`**

Initializes a new instance of the ApexMap class by assigning the specified key and value. This constructor creates a single key–value
entry that can be included in an embedded AI Apex map for passing contextual data to embedded AI logic.

Signature

```
   public ApexMap(String key, String value)

```

Parameters

```
   key
```

Type: String

The unique identifier for an entry in the embedded AI Apex map. This key references and retrieves the associated value during
embedded AI processing.

```
   value
```

Type: String

The data associated with the specified key in the embedded AI Apex map. This value stores the contextual information consumed
by embedded AI logic.


Apex Reference Guide ApexMap Class

##### **`ApexMap()`**

Initializes the ApexMap class.

Signature

```
   public ApexMap()

#### ApexMap Properties

##### These are the properties for ApexMap .

```

IN THIS SECTION:

##### key

Represents key of the key-value pair. This property is used to store the unique ID or name of the data.

##### value

Represents value of the key-value pair. This property is used to store the data associated with the key.

##### **`key`**

Represents key of the key-value pair. This property is used to store the unique ID or name of the data.

Signature

```
   public String key {get; set;}

   embeddedai.ApexMap, key

```

Property Value

Type: String

##### **`value`**

Represents value of the key-value pair. This property is used to store the data associated with the key.

Signature

```
   public String value {get; set;}

   embeddedai.ApexMap, value

```

Property Value

Type: String

#### ApexMap Methods

Create a copy of the ApexMap object and convert key-value pairs to string format.


### Apex Reference Guide RecordApexRepresentation Class

These are the methods for `ApexMap` .

IN THIS SECTION:

##### toString()

Returns a string representation of the `ApexMap` object.

##### **`toString()`**

Returns a string representation of the `ApexMap` object.

Signature

```
   public String toString()

   embeddedai.ApexMap, toString, [], String

```

Return Value

Type: String

### RecordApexRepresentation Class

Contains properties and a method to create a serializable representation of a record and its associated data for AI service integration and
data processing.

Namespace

embeddedai

IN THIS SECTION:

#### RecordApexRepresentation Constructors

Learn more about the constructors available with the RecordApexRepresentation class.

RecordApexRepresentation Properties

RecordApexRepresentation Methods
Create detailed, hierarchical record objects and convert them to a custom JSON string for structured AI input.

#### RecordApexRepresentation Constructors

Learn more about the constructors available with the RecordApexRepresentation class.

### The RecordApexRepresentation class includes these constructors.

IN THIS SECTION:

RecordApexRepresentation(objectType, recordData, relatedRecordData)
Initializes a new instance of the RecordApexRepresentation class with the specified object type, primary record data, and related
record data. This constructor represents a structured record and its relationships for consumption by embedded AI logic.


Apex Reference Guide RecordApexRepresentation Class

##### RecordApexRepresentation()

Initializes the RecordApexRepresentation class.

##### **`RecordApexRepresentation(objectType, recordData, relatedRecordData)`**

Initializes a new instance of the RecordApexRepresentation class with the specified object type, primary record data, and related record
data. This constructor represents a structured record and its relationships for consumption by embedded AI logic.

Signature

```
   public RecordApexRepresentation(String objectType, List<embeddedai.ApexMap> recordData,

   List<embeddedai.RecordApexRepresentation> relatedRecordData)

```

Parameters

```
   objectType
```

Type: String

The object type represented by this record (for example, Account, Case, or a custom object). This value defines the context in which
the record data is interpreted by embedded AI processing.

```
   recordData
```

Type: List<embeddedai.ApexMap on page 2811>

The field-level data for the primary record as a collection of key–value pairs. Each ApexMap entry corresponds to a field name and
its associated value used to construct the record context.

```
   relatedRecordData
```

Type: List<embeddedai.RecordApexRepresentation on page 2814>

Related records associated with the primary record. Each entry represents a related object and its data, enabling hierarchical or
relational record context to be passed to embedded AI logic.

##### **`RecordApexRepresentation()`**

Initializes the RecordApexRepresentation class.

Signature

```
   public RecordApexRepresentation()

#### RecordApexRepresentation Properties

##### The following are properties for RecordApexRepresentation .

```

IN THIS SECTION:

objectType
Stores the type of the object.

recordData
Stores a list of objects, where each object holds a key-value pair.


Apex Reference Guide RecordApexRepresentation Class

##### relatedRecordData

Stores a list that contains a child or related records associated with the record data.

##### **`objectType`**

Stores the type of the object.

Signature

```
   public String objectType {get; set;}

   embeddedai.RecordApexRepresentation, objectType

```

Property Value

Type: String

##### **`recordData`**

Stores a list of objects, where each object holds a key-value pair.

Signature

```
   public List<embeddedai.ApexMap> recordData {get; set;}

   embeddedai.RecordApexRepresentation, recordData

```

Property Value

Type: List<embeddedai.ApexMap>

##### **`relatedRecordData`**

Stores a list that contains a child or related records associated with the record data.

Signature

```
   public List<embeddedai.RecordApexRepresentation> relatedRecordData {get; set;}

   embeddedai.RecordApexRepresentation, relatedRecordData

```

Property Value

Type: List<embeddedai.RecordApexRepresentation>

#### RecordApexRepresentation Methods

Create detailed, hierarchical record objects and convert them to a custom JSON string for structured AI input.

#### The following are methods for RecordApexRepresentation .


## Apex Reference Guide EventBus Namespace

IN THIS SECTION:

##### toRecordApexRep(jsonString)

Converts a JSON-formatted string into a RecordApexRepresentation instance. This method parses the provided JSON and constructs
a structured record representation that can be used by embedded AI logic.

##### toString()

Returns a structured JSON string representation of the `RecordApexRepresentation` object and its nested related records.

##### **`toRecordApexRep(jsonString)`**

Converts a JSON-formatted string into a RecordApexRepresentation instance. This method parses the provided JSON and constructs a
structured record representation that can be used by embedded AI logic.

Signature

```
   public static embeddedai.RecordApexRepresentation toRecordApexRep(String jsonString)

```

Parameters

```
   jsonString
```

Type: String

The JSON-formatted string containing record data and related record information to be converted into a RecordApexRepresentation
object.

Return Value

Type: embeddedai.RecordApexRepresentation

Returns a RecordApexRepresentation instance populated with the data parsed from the provided JSON string.

##### **`toString()`**

Returns a structured JSON string representation of the `RecordApexRepresentation` object and its nested related records.

Signature

```
   public String toString()

   embeddedai.RecordApexRepresentation, toString, [], String

```

Return Value

Type: String

## EventBus Namespace The EventBus namespace provides classes and methods for platform events and Change Data Capture events. The following are the classes in the EventBus namespace.


### Apex Reference Guide ChangeEventHeader Class

IN THIS SECTION:

### ChangeEventHeader Class

Contains header fields of Change Data Capture events.

EventPublishFailureCallback Interface
Implement this interface to track platform event messages that failed to publish. The `onFailure()` method in this interface is
called when the final result of the asynchronous publish operation becomes available.

EventPublishSuccessCallback Interface
Implement this interface to track platform event messages that were published successfully. The `onSuccess()` method in this
interface is called when the final result of the asynchronous publish operation becomes available.

FailureResult Interface
Contains the result of an Apex publish callback when the event publishing failed. This interface is used as a parameter in the
`onFailure` method of the `EventPublishFailureCallback` interface.

SuccessResult Interface
Contains the result of an Apex publish callback when the event publishing succeeded. This interface is used as a parameter in the
`onSuccess` method of the `EventPublishSuccessCallback` interface.

TestBroker Class
Contains methods that simulate the successful delivery or failed publishing of platform event or change event messages in an Apex
test.

TriggerContext Class
Provides information about the platform event or change event trigger that’s currently executing, such as how many times the
trigger was retried due to the `EventBus.RetryableException` . Also, provides a method to resume trigger executions.

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

### ChangeEventHeader Class

Contains header fields of Change Data Capture events.

Namespace

EventBus

IN THIS SECTION:

#### ChangeEventHeader Properties

SEE ALSO:

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_intro.htm)_

#### ChangeEventHeader Properties

### The following are properties for ChangeEventHeader .


Apex Reference Guide ChangeEventHeader Class

IN THIS SECTION:

##### changedfields

A list of the fields that were changed in an update operation, including the `LastModifiedDate` system field. This field is empty
for other operations, including record creation. This property is available in Apex saved using API version 47.0 or later.

changeorigin
Only populated for changes done by API apps or from Lightning Experience; empty otherwise. The Salesforce API and the API client
ID that initiated the change, if set by the client. Use this field to detect whether your app initiated the change to not process the
change again and potentially avoid a deep cycle of changes.

changetype
The operation that caused the change.

commitnumber
The system change number (SCN) of a committed transaction, which increases sequentially. This field is provided for diagnostic
purposes. The field value is not guaranteed to be unique in Salesforce—it is unique only in a single database instance. If your
Salesforce org migrates to another database instance, the commit number might not be unique or sequential.

committimestamp
The date and time when the change occurred, represented as the number of milliseconds since January 1, 1970 00:00:00 GMT.

commituser
The ID of the user that ran the change operation.

difffields
Contains the names of fields whose values are sent as a unified diff because they contain large text values.

entityname
The API name of the standard or custom object that the change pertains to. For example, Account or MyObject__c.

nulledfields
Contains the names of fields whose values were changed to null in an update operation. Use this field in Apex change event messages
to determine if a field was changed to null in an update and isn’t an unchanged field.

recordids
One or more record IDs for the changed records. Typically, this field contains one record ID. If in one transaction the same change
occurred in multiple records of the same object type during one second, Salesforce merges the change notifications. In this case,
Salesforce sends one change event for all affected records and the `recordIds` field contains the IDs for all records that have the
same change.

sequencenumber
The sequence of the change within a transaction. The sequence number starts from 1.

transactionkey
A string that uniquely identifies each Salesforce transaction. You can use this key to identify and group all changes that were made
in the same transaction.

##### changedfields

A list of the fields that were changed in an update operation, including the `LastModifiedDate` system field. This field is empty
for other operations, including record creation. This property is available in Apex saved using API version 47.0 or later.

Signature

```
   public List<String> changedfields {get; set;}

```


Apex Reference Guide ChangeEventHeader Class

Property Value

Type: List<String>

##### changeorigin

Only populated for changes done by API apps or from Lightning Experience; empty otherwise. The Salesforce API and the API client ID
that initiated the change, if set by the client. Use this field to detect whether your app initiated the change to not process the change
again and potentially avoid a deep cycle of changes.

Signature

```
   public String changeorigin {get; set;}

```

Property Value

Type: String

The format of the `changeOrigin` field value is:

```
   com/salesforce/api/<API_Name>/<API_Version>;client=<Client_ID>

```

**•** `<API_Name>` is the name of the Salesforce API used to make the data change. It can take one of these values: soap, rest, bulkapi,
xmlrpc, oldsoap, toolingsoap, toolingrest, apex, apexdebuggerrest.

**•** `<API_Version>` is the version of the API call that made the change and is in the format _`XX.X`_ .

**•** `<Client_ID>` is a string that contains the client ID of the app that initiated the change. If the client ID is not set in the API call,
`client=<Client_ID>` is not appended to the `changeOrigin` field.

**Example:**

```
   com/salesforce/api/soap/49.0;client=Astro

```

The client ID is set in the Call Options header of an API call. For an example on how to set the Call Options header, see:

**•** [REST API: Sforce-Call-Options Header. (Bulk API also uses the Sforce-Call-Options header. )](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/headers_calloptions.htm)

**•** [SOAP API: CallOptions Header. (Apex API also uses the CallOptions element.)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_header_calloptions.htm)

##### changetype

The operation that caused the change.

Signature

```
   public String changetype {get; set;}

```

Property Value

Type: String

Can be one of the following values:

**•** CREATE

**•** UPDATE

**•** DELETE


Apex Reference Guide ChangeEventHeader Class

**•** UNDELETE

**•** SNAPSHOT (reserved for future use)

For gap events, the change type starts with the GAP_ prefix.

**•** GAP_CREATE

**•** GAP_UPDATE

**•** GAP_DELETE

**•** GAP_UNDELETE

For overflow events, the change type is GAP_OVERFLOW.

##### commitnumber

The system change number (SCN) of a committed transaction, which increases sequentially. This field is provided for diagnostic purposes.
The field value is not guaranteed to be unique in Salesforce—it is unique only in a single database instance. If your Salesforce org migrates
to another database instance, the commit number might not be unique or sequential.

Signature

```
   public Long commitnumber {get; set;}

```

Property Value

Type: Long

##### committimestamp

The date and time when the change occurred, represented as the number of milliseconds since January 1, 1970 00:00:00 GMT.

Signature

```
   public Long committimestamp {get; set;}

```

Property Value

Type: Long

##### commituser

The ID of the user that ran the change operation.

Signature

```
   public String commituser {get; set;}

```

Property Value

Type: String


Apex Reference Guide ChangeEventHeader Class

##### difffields

Contains the names of fields whose values are sent as a unified diff because they contain large text values.

Signature

```
   public List<String> difffields {get; set;}

```

Property Value

Type: List<String>

SEE ALSO:

_Change Data Capture Developer Guide_ [: Sending Data Differences for Fields of Updated Records](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_data_diff.htm)

##### entityname

The API name of the standard or custom object that the change pertains to. For example, Account or MyObject__c.

Signature

```
   public String entityname {get; set;}

```

Property Value

Type: String

##### nulledfields

Contains the names of fields whose values were changed to null in an update operation. Use this field in Apex change event messages
to determine if a field was changed to null in an update and isn’t an unchanged field.

Signature

```
   public List<String> nulledfields {get; set;}

```

Property Value

Type: List<String>

##### recordids

One or more record IDs for the changed records. Typically, this field contains one record ID. If in one transaction the same change occurred
in multiple records of the same object type during one second, Salesforce merges the change notifications. In this case, Salesforce sends
one change event for all affected records and the `recordIds` field contains the IDs for all records that have the same change.

Signature

```
   public List<String> recordids {get; set;}

```


### Apex Reference Guide EventPublishFailureCallback Interface

Property Value

Type: List<String>

Examples of operations with same changes are:

**•** Update of fieldA to valueA in Account records.

**•** Deletion of Account records.

**•** Renaming or replacing a picklist value that results in updating the field value in all affected records.

The `recordIds` field can contain a wildcard value when a change event message is generated for custom field type conversions that
cause data loss. In this case, the `recordIds` value is the three-character prefix of the object, followed by the wildcard character `*` .
For example, for accounts, the value is `001*` .

##### sequencenumber

The sequence of the change within a transaction. The sequence number starts from 1.

Signature

```
   public Integer sequencenumber {get; set;}

```

Property Value

Type: Integer

A lead conversion is an example of a transaction that can have multiple changes. A lead conversion results in the following sequence
of changes, all within the same transaction.

**1.** Create an account

**2.** Create a contact

**3.** Create an opportunity

**4.** Update a lead

##### transactionkey

A string that uniquely identifies each Salesforce transaction. You can use this key to identify and group all changes that were made in
the same transaction.

Signature

```
   public String transactionkey {get; set;}

```

Property Value

Type: String

### EventPublishFailureCallback Interface

Implement this interface to track platform event messages that failed to publish. The `onFailure()` method in this interface is called
when the final result of the asynchronous publish operation becomes available.


Apex Reference Guide EventPublishFailureCallback Interface

Namespace

EventBus

Usage

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
_Developer Guide_ .

IN THIS SECTION:

#### EventPublishFailureCallback Methods EventPublishFailureCallback Example Implementation EventPublishFailureCallback Methods The following are methods for EventPublishFailureCallback .

IN THIS SECTION:

##### onFailure(result)

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform
event message failed.

##### **`onFailure(result)`**

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform event
message failed.

Signature

```
   public void onFailure(eventbus.FailureResult result)

```

Parameters

```
   result
```

Type: EventBus.FailureResult

The final result of `EventBus.publish` .

Return Value

Type: void

#### EventPublishFailureCallback Example Implementation

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .


### Apex Reference Guide EventPublishSuccessCallback Interface EventPublishSuccessCallback Interface

Implement this interface to track platform event messages that were published successfully. The `onSuccess()` method in this
interface is called when the final result of the asynchronous publish operation becomes available.

Namespace

EventBus

Usage

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
_Developer Guide_ .

IN THIS SECTION:

#### EventPublishSuccessCallback Methods

EventPublishSuccessCallback Example Implementation

#### EventPublishSuccessCallback Methods

### The following are methods for EventPublishSuccessCallback .

IN THIS SECTION:

##### onSuccess(result)

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform
event message succeeded.

##### **`onSuccess(result)`**

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform event
message succeeded.

Signature

```
   public void onSuccess(eventbus.SuccessResult result)

```

Parameters

```
   result
```

Type: EventBus.SuccessResult

The final result of `EventBus.publish` .

Return Value

Type: void


### Apex Reference Guide FailureResult Interface

#### EventPublishSuccessCallback Example Implementation

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

### FailureResult Interface

Contains the result of an Apex publish callback when the event publishing failed. This interface is used as a parameter in the `onFailure`
method of the `EventPublishFailureCallback` interface.

Namespace

EventBus

IN THIS SECTION:

#### FailureResult Methods FailureResult Methods

### The following are methods for FailureResult .

IN THIS SECTION:

##### getEventUuids()

Returns a list of `EventUuid` field values of each platform event that is included in
`EventBus.EventPublishFailureCallback` .

##### **`getEventUuids()`**

Returns a list of `EventUuid` field values of each platform event that is included in
`EventBus.EventPublishFailureCallback` .

Signature

```
   public List<String> getEventUuids()

```

Return Value

Type: List<String>

### SuccessResult Interface

Contains the result of an Apex publish callback when the event publishing succeeded. This interface is used as a parameter in the
#### onSuccess method of the EventPublishSuccessCallback interface.

Namespace

EventBus


### Apex Reference Guide TestBroker Class

IN THIS SECTION:

#### SuccessResult Methods SuccessResult Methods The following are methods for SuccessResult .

IN THIS SECTION:

##### getEventUuids()

Returns a list of `EventUuid` field values of each platform event that is included in the
`EventBus.EventPublishSuccessCallback` .

##### **`getEventUuids()`**

Returns a list of `EventUuid` field values of each platform event that is included in the
`EventBus.EventPublishSuccessCallback` .

Signature

```
   public List<String> getEventUuids()

```

Return Value

Type: List<String>

### TestBroker Class

Contains methods that simulate the successful delivery or failed publishing of platform event or change event messages in an Apex test.

Namespace

EventBus

IN THIS SECTION:

#### TestBroker Methods TestBroker Methods

### The following are methods for TestBroker .

IN THIS SECTION:

deliver()
Delivers platform event messages to the test event bus. Use this method to deliver test event messages multiple times and verify
that event subscribers have processed the test events each step of the way.


Apex Reference Guide TestBroker Class

##### fail()

Causes the publishing of platform event messages to fail in the test event bus. Use this method to test Apex publish callbacks.

##### deliver()

Delivers platform event messages to the test event bus. Use this method to deliver test event messages multiple times and verify that
event subscribers have processed the test events each step of the way.

Signature

```
   public void deliver()

```

Return Value

Type: void

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

   // Perform validation

   // ...

   Test.stopTest();

```

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

##### **`fail()`**

Causes the publishing of platform event messages to fail in the test event bus. Use this method to test Apex publish callbacks.

Signature

```
   public void fail()

```

Return Value

Type: void

Usage

```
   // Create test events

   // ...

   // Publish test events with EventBus.publish()

```


### Apex Reference Guide TriggerContext Class

```
   // ...

   // Fail publishing of test events

   Test.getEventBus().fail();

   // Perform validation

   // ...

```

For more information, see <link>Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks<link/> in the
_Platform Events Developer Guide_ .

### TriggerContext Class

Provides information about the platform event or change event trigger that’s currently executing, such as how many times the trigger
was retried due to the `EventBus.RetryableException` . Also, provides a method to resume trigger executions.

Namespace

EventBus

IN THIS SECTION:

#### TriggerContext Properties

TriggerContext Methods

#### TriggerContext Properties

### The following are properties for TriggerContext .

IN THIS SECTION:

##### lastError

Read-only. The error message that the last thrown `EventBus.RetryableException` contains.

retries
Read-only. The number of times the trigger was retried due to throwing the `EventBus.RetryableException` .

##### lastError

Read-only. The error message that the last thrown `EventBus.RetryableException` contains.

Signature

```
   public String lastError {get;}

```

Property Value

Type: String


Apex Reference Guide TriggerContext Class

Usage

The error message that this property returns is the message that was passed in when creating the
`EventBus.RetryableException` exception, as follows.

```
   throw new EventBus.RetryableException(

           'Condition is not met, so retrying the trigger again.');

##### retries

```

Read-only. The number of times the trigger was retried due to throwing the `EventBus.RetryableException` .

Signature

```
   public Integer retries {get;}

```

Property Value

Type: Integer

#### TriggerContext Methods The following are methods for TriggerContext .

IN THIS SECTION:

##### currentContext()

Returns an instance of the `EventBus.TriggerContext` class containing information about the currently executing trigger.

getResumeCheckpoint()
Returns the replay ID that was set by `setResumeCheckpoint()` . The returned value is the replay ID of the event message
after which trigger processing resumes in a new trigger invocation.

setResumeCheckpoint(resumeReplayId)
Sets a checkpoint in the event stream where the platform event trigger resumes execution in a new invocation. Use this method to
recover from limit and uncaught exceptions, or to control the number of events processed in one trigger execution. When calling
this method, pass in the replay ID of the last successfully processed event message. When the trigger stops execution before all
events in `Trigger.New` are processed, either because of an uncaught exception or intentionally, the trigger is invoked again.
The new execution starts with the event message in the stream after the one with the checkpointed Replay ID.

##### currentContext()

Returns an instance of the `EventBus.TriggerContext` class containing information about the currently executing trigger.

Signature

```
   public static eventbus.TriggerContext currentContext()

```

Return Value

Type: EventBus.TriggerContext

Information about the currently executing trigger.


Apex Reference Guide TriggerContext Class

##### getResumeCheckpoint()

Returns the replay ID that was set by `setResumeCheckpoint()` . The returned value is the replay ID of the event message after
which trigger processing resumes in a new trigger invocation.

Signature

```
   public String getResumeCheckpoint()

```

Return Value

Type: String

##### setResumeCheckpoint(resumeReplayId)

Sets a checkpoint in the event stream where the platform event trigger resumes execution in a new invocation. Use this method to
recover from limit and uncaught exceptions, or to control the number of events processed in one trigger execution. When calling this
method, pass in the replay ID of the last successfully processed event message. When the trigger stops execution before all events in
`Trigger.New` are processed, either because of an uncaught exception or intentionally, the trigger is invoked again. The new execution
starts with the event message in the stream after the one with the checkpointed Replay ID.

Signature

```
   public void setResumeCheckpoint(String resumeReplayId)

```

Parameters

```
   resumeReplayId
```

Type: String

The replay ID of the last successfully processed platform event message, after which to resume processing in a new trigger execution
context.

Return Value

Type: void

Usage

The method throws an `EventBus.InvalidReplayIdException` if the supplied Replay ID is not valid—the replay ID is not
in the current trigger batch of events, in the `Trigger.new` list.

Example

This snippet shows how to call the method and pass in the replayId property of an event instance.

```
   EventBus.TriggerContext.currentContext().setResumeCheckpoint(event.replayId);

```


## Apex Reference Guide ExternalService Namespace ExternalService Namespace The ExternalService namespace provides dynamically generated Apex service interfaces and Apex classes for complex object

data types.

## The ExternalService namespace doesn't define a fixed set of classes. The namespace reflects OpenAPI-compatible external

service registrations with active operations for type-safe outbound calls. The object schema, in the API specification that is associated
with the registered external service, maps to Apex types.

SEE ALSO:

_Salesforce Help:_ [Invoke External Service Callouts Using Apex](https://help.salesforce.com/s/articleView?id=platform.external_services_apex_invoking.htm&type=5&language=en_US)

## Flow Namespace The Flow namespace provides a class for advanced access to flows from Apex such as from Visualforce controllers and asynchronous

Apex.

## The following is the class in the Flow namespace.

IN THIS SECTION:

### Interview Class

The `Flow.Interview` class provides advanced controller access to flows and the ability to start a flow.

### Interview Class

The `Flow.Interview` class provides advanced controller access to flows and the ability to start a flow.

Namespace

## Flow

Usage

[SOQL and DML limits apply during flow execution. See Per-Transaction Flow Limits in Salesforce Help.](https://help.salesforce.com/articleView?id=flow_considerations_limit_transaction.htm&language=en_US)

To create an Interview object, you have two options.

Note: We recommend only using `createInterview()` if you must reuse your method or class. Using
`createInterview()` has these drawbacks.

**•** If you package a class that uses `createInterview()`, you have to add the associated flow manually.

**•** If you delete a flow, Salesforce doesn't check if it's referenced with `createInterview()` .

**•** Create the object directly in your class by using:

**–** No namespace: `Flow.Interview.` _**`flowName`**_

**–** Namespace: `Flow.Interview.` _**`namespace`**_ `.` _**`flowName`**_

**•** Create the object dynamically by using `createInterview()`


Apex Reference Guide Interview Class

To enforce sharing rules, run the flow or Apex on API version 62.0 or later. The Apex class must be declared using the `with sharing`
keyword. The flow runs more securely in the default context when an Apex class that’s declared using the `with sharing` keyword
launches an autolaunched flow. The flow enforces the sharing rules of the user that executes the Apex class. Data access is restricted to
the sharing rules of the user that executed the Apex class. For example, a query can return fewer rows than it did in system context
without sharing. An operation can fail because the user doesn’t have the correct permissions.

Examples: Starting Flow Interviews

[These examples are all sample controllers that start an interview for the flow from the Build a Discount Calculator project on Trailhead.](https://trailhead.salesforce.com/projects/flow_calculate)
Each shows a different permutation, based on:

**•** Whether the interview is created statically, with `Flow.Interview.` _**`myFlow`**_, or dynamically, with `createInterview()` .

**•** Whether the flow is managed or local.

Interview Created Statically for a Local Flow

```
   {

     Map<String, Object> inputs = new Map<String, Object>();

     inputs.put('AccountID', myAccount);

     inputs.put('OpportunityID', myOppty);

     Flow.Interview.Calculate_discounts myFlow =

      new Flow.Interview.Calculate_discounts(inputs);

     myFlow.start();

   }

```

Interview Created Dynamically for a Local Flow

```
   public void callFlow(String flowName, Map <String, Object> inputs) {

     Flow.Interview myFlow = Flow.Interview.createInterview(flowName, inputs);

     myFlow.start();

   }

```

Interview Created Statically for a Managed Flow

```
   {

     Map<String, Object> inputs = new Map<String, Object>();

     inputs.put('AccountID', myAccount);

     inputs.put('OpportunityID', myOppty);

     Flow.Interview.myNamespace.Calculate_discounts myFlow =

      new Flow.Interview.myNamespace.Calculate_discounts(inputs);

     myFlow.start();

   }

```

Interview Created Dynamically for a Managed Flow

```
   public void callFlow(String namespace, String flowName, Map <String, Object> inputs) {

     Flow.Interview myFlow = Flow.Interview.createInterview(namespace, flowName, inputs);

     myFlow.start();

   }

```


Apex Reference Guide Interview Class

Example: Getting Variable Values

This sample uses the `getVariableValue` method to obtain breadcrumb (navigation) information from a flow. If that flow contains
subflow elements, and each of the referenced flows also contains a _`vaBreadCrumb`_ variable, you can provide users with breadcrumbs
regardless of which flow the interview is running.

```
   public class SampleController {

     //Instance of the flow

     public Flow.Interview.Flow_Template_Gallery myFlow {get; set;}

     public String getBreadCrumb() {

       String aBreadCrumb;

       if (myFlow==null) { return 'Home';}

       else aBreadCrumb = (String) myFlow.getVariableValue('vaBreadCrumb');

       return(aBreadCrumb==null ? 'Home': aBreadCrumb);

     }

   }

```

SEE ALSO:

_Tooling API Objects_ [: FlowTestCoverage](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_flowtestcoverage.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_qs_test.htm)_ : Add a Test Class

_Salesforce Help_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

_Apex Developer Guide_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

#### Interview Methods The following are instance methods for Interview .

##### **`createInterview(namespace, flowName, inputVariables)`**

Creates an interview for a namespaced flow.

Signature

```
   public static Flow.Interview createInterview(String namespace, String flowName,

   Map<String,ANY> inputVariables)

```

Parameters

```
   namespace
```

Type: String

The flow’s namespace.

```
   flowName
```

Type: String

The flow’s API name.


Apex Reference Guide Interview Class

```
   inputVariables
```

Type: Map<String,Object>

Initial values for the flow’s input variables.

Return Value

Type: Flow.Interview

Usage

Use this method to dynamically create a Flow.Interview object for the `start()` method.

How you get output variable values from an interview depends on the type of the Apex variable where you're storing the interview.

**•** If the variable is cast to a specific flow, you can use _myFlow.myVar_ to access a variable, where _myVar_ is the name of the variable.

```
     system.debug('My Output Variable: ' + myFlow.varName);

```

**•** If the variable is of type Flow.Interview but not cast to a specific flow, you must use getVariableValue() to access the flow's variables.

```
     system.debug('My Output Variable: ' + myFlow.getVariableValue('varName'));

```

If the flow doesn't exist in the current org, a TypeException is thrown.

##### **`createInterview(flowName, inputVariables)`**

Creates an interview for a flow.

Signature

```
   public static Flow.Interview createInterview(String flowName, Map<String,Object>

   inputVariables)

```

Parameters

```
   flowName
```

Type: String

The flow’s API name.

```
   inputVariables
```

Type: Map<String,Object>

Initial values for the flow’s input variables.

Return Value

Type: Flow.Interview

Usage

Use this method to dynamically create a Flow.Interview object for the `start()` method.

How you get output variable values from an interview depends on the type of the Apex variable where you're storing the interview.


Apex Reference Guide Interview Class

**•** If the variable is cast to a specific flow, you can use _myFlow.myVar_ to access a variable, where _myVar_ is the name of the variable.

```
     system.debug('My Output Variable: ' + myFlow.varName);

```

**•** If the variable is of type Flow.Interview but not cast to a specific flow, you must use getVariableValue() to access the flow's variables.

```
     system.debug('My Output Variable: ' + myFlow.getVariableValue('varName'));

```

If the flow doesn't exist in the current org, a TypeException is thrown.

##### **`getVariableValue(variableName)`**

Returns the value of the specified flow variable. The flow variable can be in the flow embedded in the Visualforce page, or in a separate
flow that is called by a subflow element.

Signature

```
   public Object getVariableValue(String variableName)

```

Parameters

```
   variableName
```

Type: String

Specifies the unique name of the flow variable.

Return Value

Type: Object

Usage

The returned variable value comes from whichever flow the interview is running. If the specified variable can't be found in that flow, the
method returns `null` .

This method checks for the existence of the variable at run time only, not at compile time.

##### **`start()`**

Starts an instance (interview) for an autolaunched or user provisioning flow.

Signature

```
   public Void start()

```

Return Value

Type: Void

Usage

This method can be used only with flows that have one of these types.

**•** Autolaunched Flow


## Apex Reference Guide Flowtesting Namespace

**•** User Provisioning Flow

[For details, see “Flow Types” in Salesforce Help.](https://help.salesforce.com/articleView?id=flow_concepts_type.htm&language=en_US)

When a flow user invokes an autolaunched flow, the active flow version runs. If there’s no active version, the latest version runs. When
a flow admin invokes a flow, the latest version always runs.

## Flowtesting Namespace

The `flowtesting` namespace provides dynamically generated Apex classes for flow tests that are created in Flow Builder.

The `flowtesting` namespace doesn't define a fixed set of classes. The namespace reflects flows and flow tests that are created in
Flow Builder. You can run flow tests with the Salesforce CLI command _`sf flow run test`_ . For more details about the command,
use the Salesforce CLI _`–help flag`_ .

SEE ALSO:

_[Salesforce CLI Setup Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)_ Before You Begin

## flowuiruntime Namespace

The classes and methods in this namespace are reserved for internal use only or future use.

## The following are the classes in the flowuiruntime namespace.

IN THIS SECTION:

### ComplexObjectFieldDetails Class

The methods and properties in this class are for internal use only.

### PropertyTypeDetails Class

The methods and properties in this class are for internal use only.

ToastLink Class
The methods and properties in this class are reserved for future use.

### ComplexObjectFieldDetails Class

The methods and properties in this class are for internal use only.

Namespace

## flowuiruntime

### PropertyTypeDetails Class

The methods and properties in this class are for internal use only.

Namespace

## flowuiruntime


### Apex Reference Guide ToastLink Class ToastLink Class

The methods and properties in this class are reserved for future use.

Namespace

flowuiruntime

## FormulaEval Namespace

The FormulaEval namespace provides classes and methods to evaluate dynamic formulas for SObjects and Apex objects. Use the methods
to avoid unnecessary DML statements to recalculate formula field values or evaluate dynamic formula expressions.

When using a formula against an SObject or Apex object as the context object, the class methods or properties referenced by the formula
must be global.

```
   Account myAcc = new Account(Name='123');

        FormulaEval.FormulaInstance ff = Formula.builder()

          .withType(Schema.Account.class)

          .withReturnType(FormulaEval.FormulaReturnType.STRING)

          .withFormula('name & " (" & website & ")"')

          .build();

   //Use the list of field names returned by the getReferenced method to generate dynamic

   soql

        String fieldNameList = String.join(ff.getReferencedFields(),',');

        String queryStr = 'select ' + fieldNameList + ' from Account LIMIT 1'; //select

   name, website from Account

        Account s = Database.query(queryStr);

        system.debug(ff.evaluate(s));

```

[For usage notes, see Formula Evaluation in Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_formulaeval.htm)

## The following are the classes and enums in the FormulaEval namespace.

IN THIS SECTION:

### FormulaBuilder Class

Contains methods to build and validate user-defined formulas.

FormulaGlobal Enum
Specifies a global variable that references data in your organization in the `withGlobalVariables(formulaGlobals)`
method.

FormulaInstance Class
Contains a method to evaluate the formula instance.

FormulaReturnType Enum
Specifies the return type for the `withReturnType(returnType)` method.

### FormulaBuilder Class

Contains methods to build and validate user-defined formulas.


Apex Reference Guide FormulaBuilder Class

Namespace

FormulaEval

Usage

The context type that corresponds to the Apex class used in the builder `withType()` method must be a global, user-defined Apex
class. Any fields or properties that the formula references must also be global.

IN THIS SECTION:

#### FormulaBuilder Methods FormulaBuilder Methods The following are methods for FormulaBuilder .

IN THIS SECTION:

##### build()
#### Validates and returns the formula instance created using the FormulaBuilder methods.

parseAsTemplate(templateMode)
##### Optional. Indicates whether a formula expression created with the build() method is evaluated in template mode. In template

mode, values are interpolated into a string by using merge field syntax rather than by concatenating strings with the `&` operator.
Merge fields use the syntax `{!Object_Name.Field_Name}`, where names are preceded by an exclamation mark and enclosed
in curly braces.

treatNumericNullAsZero(isNumericNullZero)
##### Optional. Indicates whether a null for a numeric data type is treated as zero while evaluating the formula with the build() method.

withFormula(formulaText)
##### Required. Sets the formula expression that the build() method uses to create the formula instance.

withGlobalVariables(formulaGlobals)
##### Optional. Sets the list of global variables that can be referenced in the formula expression created with the build() method.

withReturnType(returnType)
##### Required. Sets the formula output data type for the formula instance created with the build() method.

withType(contextType)
##### Sets the Apex type that corresponds to the Apex class used with the build() method.

withType(contextType)
##### Sets the Apex type that corresponds to the Apex class used with the build() method to SObject type. **`build()`**

#### Validates and returns the formula instance created using the FormulaBuilder methods.

Signature

```
   public FormulaEval.FormulaInstance build()

```


Apex Reference Guide FormulaBuilder Class

Return Value

Type: FormulaEval.FormulaInstance

Returns an instance of the `FormulaInstance` object. If the formula validation such as field references, functions, or syntax, fails,
the method throws a `FormulaValidationException` exception.

##### **`parseAsTemplate(templateMode)`**

Optional. Indicates whether a formula expression created with the `build()` method is evaluated in template mode. In template
mode, values are interpolated into a string by using merge field syntax rather than by concatenating strings with the `&` operator. Merge
fields use the syntax `{!Object_Name.Field_Name}`, where names are preceded by an exclamation mark and enclosed in curly
braces.

Signature

```
   public formulaeval.FormulaBuilder parseAsTemplate(Boolean templateMode)

```

Parameters

```
   templateMode
```

Type: Boolean

If `true`, the formula expression is evaluated in template mode. The default value is `false` .

Return Value

Type: FormulaEval.FormulaBuilder

Usage

In template mode, the `FormulaEval.FormulaReturnType` value that’s set with `withReturnType()` must be `STRING` .

Template mode supports the same global variables, formula expressions, and context types as non-template mode, as long as they are
correctly set using the FormulaBuilder methods.

Example

In this example, `true` is passed to `parseAsTemplate()` . The formula expression is evaluated in template mode, so the values of
the `name` and `website` fields on the Account record are interpolated into the string using merge field syntax. The output is equal
to the expression `'name & " (" & website & ")"'` .

```
   FormulaEval.FormulaInstance ff = Formula.builder()

      .withType(Schema.Account.class)

      .withReturnType(FormulaEval.FormulaReturnType.STRING)

      .withFormula('{!name} ({!website})')

      .parseAsTemplate(true)

      .build();

##### **`treatNumericNullAsZero(isNumericNullZero)`**

```

Optional. Indicates whether a null for a numeric data type is treated as zero while evaluating the formula with the `build()` method.


Apex Reference Guide FormulaBuilder Class

Signature

```
   public FormulaEval.FormulaBuilder treatNumericNullAsZero(Boolean isNumericNullZero)

```

Parameters

```
   isNumericNullZero
```

Type: Boolean

If `true`, null for numeric is treated as zero. The default value is `false` .

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withFormula(formulaText)`**

Required. Sets the formula expression that the `build()` method uses to create the formula instance.

Signature

```
   public FormulaEval.FormulaBuilder withFormula(String formulaText)

```

Parameters

```
   formulaText
```

Type: String

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withGlobalVariables(formulaGlobals)`**

Optional. Sets the list of global variables that can be referenced in the formula expression created with the `build()` method.

Signature

```
   public FormulaEval.FormulaBuilder withGlobalVariables(List<formulaeval.FormulaGlobal>

   formulaGlobals)

```

Parameters

```
   formulaGlobals
```

Type: List<FormulaEval.FormulaGlobal>

Uses values from the `FormulaGlobal` enum.

Return Value

Type: FormulaEval.FormulaBuilder


Apex Reference Guide FormulaBuilder Class

##### **`withReturnType(returnType)`**

Required. Sets the formula output data type for the formula instance created with the `build()` method.

Signature

```
   public FormulaEval.FormulaBuilder withReturnType(formulaeval.FormulaReturnType

   returnType)

```

Parameters

```
   returnType
```

Type: FormulaEval.FormulaReturnType

Uses values from the `FormulaReturnType` enum.

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withType(contextType)`**

Sets the Apex type that corresponds to the Apex class used with the `build()` method.

Signature

```
   public formulaeval.FormulaBuilder withType(System.Type contextType)

```

Parameters

```
   contextType
```

Type: System.Type

An instance of the Apex class type.

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withType(contextType)`**

Sets the Apex type that corresponds to the Apex class used with the `build()` method to SObject type.

Signature

```
   public formulaeval.FormulaBuilder withType(Schema.SObjectType contextSObjectType)

```

Parameters

```
   contextSObjectType
```

Type: Schema.SObjectType

An instance of the SObject type.


### Apex Reference Guide FormulaGlobal Enum

Return Value

Type: FormulaEval.FormulaBuilder

Example

This example uses an SObject type as an input in the `withType()` method to build and evaluate a formula.

```
   FormulaEval.FormulaInstance ff = Formula.builder()

      .withReturnType(FormulaEval.FormulaReturnType.Boolean)

      .withType(Account.SObjectType)

      .withFormula('ISBLANK(Site)')

      .build();

   Boolean siteIsBlank = (Boolean)ff.evaluate(new Account(Site='Test'));

   Assert.isFalse(siteIsBlank);

### FormulaGlobal Enum

```

Specifies a global variable that references data in your organization in the `withGlobalVariables(formulaGlobals)`
method.

Enum Values

The following are the values of the `FormulaEval.FormulaGlobal` enum.

**Value** **Description**

`CUSTOMMETADATA` A custom metadata record.

`LABEL` A global variable to use when referencing a custom label.

`ORGANIZATION` A global variable to use when referencing information about your company profile,
such as organization’s city, fax, ID, or other details.

`PERMISSION` A global variable to use when referencing information about the current user’s
custom permission access.

`PROFILE` A global variable to use when referencing information about the current user’s
profile, such as license type or name.

`SETUP` A global variable to use when referencing a custom setting of type `hierarchy` .

```
SYSTEM

```

A global variable that exposes _`OriginDateTime`_ and represents the literal value
of 1900-01-01 00:00:00. Use this global variable when performing date/time offset
calculations, or to assign a literal value to a date/time field.

`USER` A global variable to use when referencing information about the current user, such
as alias, title, and ID.

`USERROLE` A global variable to use when referencing information about the current user’s role,
such as role name, description, and ID.


### Apex Reference Guide FormulaInstance Class FormulaInstance Class

Contains a method to evaluate the formula instance.

Namespace

FormulaEval

Example

```
   global class MotorYacht {

     global Integer lengthInYards;

     global Integer numOfGuestCabins;

     global String name;

     global Account owner;

   }

   MotorYacht aBoat = new MotorYacht();

   aBoat.lengthInYards = 52;

   aBoat.numOfGuestCabins = 4;

   aBoat.name = 'RV Foo';

   FormulaEval.FormulaInstance isItSuper = Formula.builder()

                    .withReturnType(FormulaEval.FormulaReturnType.STRING)

                    .withType(MotorYacht.class)

                    .withFormula('IF(lengthInYards < 100, "Not Super", "Super")')

                    .build();

   isItSuper.evaluate(aBoat); //=> "Not Super"

   aBoat.owner = new Account(Name='Acme Watercraft', Site='New York');

   FormulaEval.FormulaInstance ownerDetails = Formula.builder()

                    .withReturnType(FormulaEval.FormulaReturnType.STRING)

                    .withType(MotorYacht.class)

                    .withFormula('owner.Name & " (" & owner.Site & ")"')

                    .build();

   ownerDetails.evaluate(aBoat); //=> "Acme Watercraft (New York)"

```

Usage

The context type in the `withType` method must be a global, user-defined Apex class. Any fields or properties that the formula
references must also be global.

IN THIS SECTION:

#### FormulaInstance Methods FormulaInstance Methods

### The following are methods for FormulaInstance .


Apex Reference Guide FormulaInstance Class

IN THIS SECTION:

##### evaluate(contextObject)

Calculates the formula expression and returns the formula output.

##### getReferencedFields()

Returns a set of strings that denote the field names referenced in a formula.

##### **`evaluate(contextObject)`**

Calculates the formula expression and returns the formula output.

Signature

```
   public Object evaluate(Object contextObject)

```

Parameters

```
   contextObject
```

Type: Object

An instance of the Apex class as generated with the `FormulaBuilder.builder()` method.

Return Value

Type: Object

Apex type that corresponds to the Apex class as configured by the `withType()` method in the `FormulaBuilder` class.

##### **`getReferencedFields()`**

Returns a set of strings that denote the field names referenced in a formula.

Signature

```
   public Set<String> getReferencedFields()

```

Return Value

Type: Set<String>

Usage

A formula is built and evaluated in the context of the current namespace of the subscriber org. If you package a formula that references
fields, the fields must be fully qualified with the namespace name.

Example

```
   FormulaEval.FormulaInstance ff = Formula.builder()

                       .withType(Schema.Account.class)

                       .withReturnType(FormulaEval.FormulaReturnType.STRING)

                       .withFormula('name & website')

                       .build();

```


### Apex Reference Guide FormulaReturnType Enum

```
   // Returns the field names 'name', and 'website' required to process the formula

   Set<String> fieldNames = ff.getReferencedFields();

   // Use the list of field names to generate dynamic soql

   String queryStr = 'select ' + string.join(fieldNames, ', ') + ' from Account limit 1';

   List<sObject> accounts = Database.query(queryStr);

   string formulaOutput = (string)ff.evaluate(accounts[0]);

   System.debug(formulaOutput);

### FormulaReturnType Enum

```

Specifies the return type for the `withReturnType(returnType)` method.

Enum Values

The following are the values of the `FormulaEval.FormulaReturnType` enum.

**Value** **Description**

`BOOLEAN` A value that can only be assigned `true`, `false`, or `null` .

`DATE` A value that indicates a particular day.

`DATETIME` A value that indicates a particular day and time, such as a timestamp.

`DECIMAL` A number that includes a decimal point. Decimal is an arbitrary precision number.

`DOUBLE` A 64-bit number that includes a decimal point.

`ID` Any valid 18-character Lightning Platform record identifier.

`INTEGER` A 32-bit number that doesn’t include a decimal point.

`LONG` A 64-bit number that doesn’t include a decimal point.

`STRING` Any set of characters surrounded by single quotes.

`TIME` A value that indicates a particular time.

## fsccashflow Namespace The fsccashflow namespace provides classes used in the FSCCashFlow Flexcards and its child Flexcards. The fsccashflow namespace has these classes.

IN THIS SECTION:

FSCCashFlowUtil Class
Use the callable FSCCashFlowUtil class to manage and validate data for party income and expense entities by passing in the action
and the corresponding arguments. This class provides utility methods used in FSCCashFlow Flexcard and its child Flexcards.


### Apex Reference Guide FSCCashFlowUtil Class FSCCashFlowUtil Class

Use the callable FSCCashFlowUtil class to manage and validate data for party income and expense entities by passing in the action and
the corresponding arguments. This class provides utility methods used in FSCCashFlow Flexcard and its child Flexcards.

Namespace

fsccashflow Namespace

Usage

The Financial Goals FlexCards use Integration Procedures that call the FSCHouseholdService class. These FlexCards display information
about Financial Goals.

IN THIS SECTION:

#### FSCCashFlowUtil Methods FSCCashFlowUtil Methods

### The FSCCashFlowUtil has these methods.

IN THIS SECTION:

GetPartyIncomeFrequencyLabel
Returns the picklist values for the party income frequency field on the party income entity.

GetPartyIncomeTypeLabel
Returns the picklist values for the party income type field on the party income entity.

GetPartyIncomeStatusLabel
Returns the picklist values for the party income status field on the party income entity.

CalculateIncomeExpenseSummary
Calculates the monthly income, total income, average monthly income, monthly expense, total expense, average monthly expense
from a list of income and expenses provided.

GetPartyExpenseFrequencyLabel
Returns the picklist values for the party expense frequency field on the party expense entity.

GetPartyExpenseTypeLabel
Returns the picklist values for the party expense type field on the party expense entity.

GetPartyExpenseStatusLabel
Returns the picklist values for the party expense status field on the party expense entity.

PerformIncomeValidation
Performs validations on Party Income records. Ensure that the start date is not earlier than the end date.

PerformExpenseValidation
Performs validations on Party Income records.


Apex Reference Guide FSCCashFlowUtil Class

GetDurationDateRange
Returns the start and end date given a duration.For example, if you input the number 3 on the date 10/29/2024, it will return a start
date of 7/1/2024 and an end date of 10/1/2024.

HandleUpsertError
Helper method that constructs the error response for upsert of a partyIncome or partyExpense record.

CheckReadAccess
Checks for read access on the partyIncome and partyExpense entities.

CheckCrudOnIncome
Checks create, update and delete access on partyIncome entity.

CheckCrudOnExpense
Checks create, update and delete access on partyExpense entity.

##### **`GetPartyIncomeFrequencyLabel`**

Returns the picklist values for the party income frequency field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income frequency.

##### **`GetPartyIncomeTypeLabel`**

Returns the picklist values for the party income type field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income type.

##### **`GetPartyIncomeStatusLabel`**

Returns the picklist values for the party income status field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income status.


Apex Reference Guide FSCCashFlowUtil Class

##### **`CalculateIncomeExpenseSummary`**

Calculates the monthly income, total income, average monthly income, monthly expense, total expense, average monthly expense from
a list of income and expenses provided.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns income and expense details.

Examples

Input and output JSON example of the actions are as follows.

Input format:

```
     [

       {

          "Duration": "12",

          "PartyExpenseList": [

            {

               "Name": "PE-0000000004",

               "UsageType": "CashFlow",

               "RecurrenceInterval": "Monthly",

               "Type": "Child Care",

               "Id": "2n3SG000007dkzpYAA",

               "TotalAmount": 999.99,

               "PartyId": "001SG000004TCczYAG",

               "Status": "Active",

               "StartDate": "2024-01-29T08:00:00.000Z"

            }

          ],

          "PartyIncomeList": [

            {

               "Name": "PI-0000000003",

               "UsageType": "CashFlow",

               "IncomeFrequency": "Monthly",

               "IncomeType": "Salary",

               "Id": "2m3SG000007dkzpYAA",

               "IncomeAmount": 999.99,

               "PartyId": "001SG000004TCczYAG",

               "IncomeStatus": "Active",

               "StartDate": "2024-01-29T08:00:00.000Z"

            }

          ]

       }

     ]

```

Output format:

```
     [

       {

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "MonthlyIncome": {

            "Nov 2023": 0,

            "Aug 2024": 999.99,

            "Oct 2023": 0,

            "Jan 2024": 96.7732258064516,

            "Mar 2024": 999.99,

            "Jul 2024": 999.99,

            "Apr 2024": 999.99,

            "Dec 2023": 0,

            "Jun 2024": 999.99,

            "Sep 2024": 999.99,

            "Feb 2024": 999.99,

            "May 2024": 999.99

          },

          "MonthlyExpense": {

            "Nov 2023": 0,

            "Aug 2024": 999.99,

            "Oct 2023": 0,

            "Jan 2024": 96.7732258064516,

            "Mar 2024": 999.99,

            "Jul 2024": 999.99,

            "Apr 2024": 999.99,

            "Dec 2023": 0,

            "Jun 2024": 999.99,

            "Sep 2024": 999.99,

            "Feb 2024": 999.99,

            "May 2024": 999.99

          },

          "AvgMonthlyExpense": 674.72,

          "TotalIncome": 8096.69,

          "TotalSurplus": 0,

          "AvgMonthlyIncome": 674.72,

          "AvgMonthlySurplus": 0,

          "TotalExpense": 8096.69

       }

     ]

##### **`GetPartyExpenseFrequencyLabel`**

```

Returns the picklist values for the party expense frequency field on the party expense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense frequency.

##### **`GetPartyExpenseTypeLabel`**

Returns the picklist values for the party expense type field on the party expense entity.


Apex Reference Guide FSCCashFlowUtil Class

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense type.

##### **`GetPartyExpenseStatusLabel`**

Returns the picklist values for the party expense status field on the party expense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense status.

##### **`PerformIncomeValidation`**

Performs validations on Party Income records. Ensure that the start date is not earlier than the end date.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income type.

Examples

Input and output JSON example of the actions are as follows.

Input format:

```
     [

       {

          "IncomeFrequency": "Weekly",

          "IncomeFrequencyLabelObject": {

            "value": "Weekly",

            "label": "Weekly"

          },

          "MemberOptionsList": [

            {

               "value": "001OG00000xx6gAYAQ",

               "label": "Okee PA"

            },

            {

               "value": "id2",

               "label": "Name2"

```


Apex Reference Guide FSCCashFlowUtil Class

```
            }

          ],

          "IsHousehold": true,

          "IncomeAmount": 100,

          "IncomeStatusOptions": [

            {

               "value": "Active",

               "label": "Active"

            },

            {

               "value": "Inactive",

               "label": "Inactive"

            }

          ],

          "PartyId": "001OG00000xx6gAYAQ",

          "IncomeStatus": "Active",

          "Party": {

            "Name": "Okee PA",

            "Id": "001OG00000xx6gAYAQ"

          },

          "IncomeTypeOptions": [

            {

               "value": "Salary",

               "label": "Salary"

            },

            {

               "value": "Commission",

               "label": "Commission"

            },

            {

               "value": "Fees",

               "label": "Fees"

            },

            {

               "value": "Rent",

               "label": "Rent"

            }

          ],

          "StartDate": "2024-02-02T00:00:00.000Z",

          "Name": "PI-0000000009",

          "FrequencyOptions": [

            {

               "value": "Weekly",

               "label": "Weekly"

            },

            {

               "value": "Monthly",

               "label": "Monthly"

            },

            {

               "value": "Yearly",

               "label": "Yearly"

            }

          ],

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "UsageType": "CashFlow",

          "IncomeId": "2m3OG000000009xxAQ",

          "IsPersonAccount": false,

          "IncomeTypeLabelObject": {

            "value": "Salary",

            "label": "Salary"

          }

       }

     ]

```

Output format:

```
     [

       {

          "dateErrorMessage": null,

          "IncomeFrequency": "Weekly",

          "IncomeFrequencyLabelObject": {

            "value": "Weekly",

            "label": "Weekly"

          },

          "MemberOptionsList": [

            {

               "value": "001OG000003f6gAYAQ",

               "label": "Okee PA"

            },

            {

               "value": "id2",

               "label": "Name2"

            }

          ],

          "requiredFieldErrorMessage": "Required fields:Type",

          "IsHousehold": true,

          "IncomeAmount": 100,

          "PartyId": "001OG000003f6gAYAQ",

          "IncomeStatusOptions": [

            {

               "value": "Active",

               "label": "Active"

            },

            {

               "value": "Inactive",

               "label": "Inactive"

            }

          ],

          "Party": {

            "Name": "Okee PA",

            "Id": "001OG000003f6gAYAQ"

          },

          "IncomeStatus": "Active",

          "hasUpsertError": false,

          "IncomeTypeOptions": [

            {

               "value": "Salary",

               "label": "Salary"

            },

```


Apex Reference Guide FSCCashFlowUtil Class

```
            {

               "value": "Commission",

               "label": "Commission"

            },

            {

               "value": "Fees",

               "label": "Fees"

            },

            {

               "value": "Rent",

               "label": "Rent"

            }

          ],

          "StartDate": "2024-02-02T00:00:00.000Z",

          "Name": "PI-0000000009",

          "FrequencyOptions": [

            {

               "value": "Weekly",

               "label": "Weekly"

            },

            {

               "value": "Monthly",

               "label": "Monthly"

            },

            {

               "value": "Yearly",

               "label": "Yearly"

            }

          ],

          "UsageType": "CashFlow",

          "IncomeId": "2m3OG000000009IYAQ",

          "IsPersonAccount": false,

          "IncomeTypeLabelObject": {

            "value": "Salary",

            "label": "Salary"

          }

       }

     ]

##### **`PerformExpenseValidation`**

```

Performs validations on Party Income records.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income frequency.


Apex Reference Guide FSCCashFlowUtil Class

Examples

Output JSON example of the actions are as follows.

Output format:

```
     {

       "Required fields": "Expense Type, Member, Amount, Start Date, Frequency"

     }

##### **`GetDurationDateRange`**

```

Returns the start and end date given a duration.For example, if you input the number 3 on the date 10/29/2024, it will return a start date
of 7/1/2024 and an end date of 10/1/2024.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns the start and end date for a specified duration.

Examples

Output JSON example of the actions are as follows.

Output format:

```
     {

           "DurationStartDate": "2024-02-02T00:00:00.000Z",

           "DurationEndDate": "2024-05-02T00:00:00.000Z"

          }

##### **`HandleUpsertError`**

```

Helper method that constructs the error response for upsert of a partyIncome or partyExpense record.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of errors encountered while upserting the record in the database.

Examples

Input and output JSON example of the action are as follows.

Input format:

```
     [

       {

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "Name": "PI-0000000003",

          "UsageType": "CashFlow",

          "IncomeFrequency": "Monthly",

          "IncomeType": "Salary",

          "Id": "2m3SG000007dkxxYAA",

          "IncomeAmount": 999.99,

          "PartyId": "001SG000004TCxxYAG",

          "IncomeStatus": "Active",

          "StartDate": "2024-01-29T08:00:00.000Z"

       }

     ]

```

Output format:

```
     [ { "UpsertError“: "Invalid Id“ } ]

##### **`CheckReadAccess`**

```

Checks for read access on the partyIncome and partyExpense entities.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether read access is granted or not.

Examples

Output JSON example of the action are as follows.

Output format:

```
     { "isAccessible" : "true" }

##### **`CheckCrudOnIncome`**

```

Checks create, update and delete access on partyIncome entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether create, update and delete access on the partyIncome entity is given.

Examples

Output JSON example of the action are as follows.


## Apex Reference Guide Functions Namespace

Output format:

```
     { "isCreatable" : "true", "isUpdateable" : "true", "isDeletable": "true" }

##### **`CheckCrudOnExpense`**

```

Checks create, update and delete access on partyExpense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether create, update and delete access on the partyExpense entity is given.

Examples

Output JSON example of the action are as follows.

Output format:

```
     { "isCreatable" : "true", "isUpdateable" : "true", "isDeletable": "true" }

## Functions Namespace

```

The Functions namespace provides classes and methods used to invoke and manage Salesforce Functions.

Salesforce Functions is your code, run on demand, in the Salesforce Functions trusted elastic compute cloud. Upload your complex
business logic code, written using your preferred languages and frameworks, and Salesforce Functions takes care of everything else
necessary to invoke your code in a secure, multi-tenant aware, and self-scaling environment. For more details on Salesforce Functions,
[see Salesforce Functions.](https://developer.salesforce.com/docs/platform/functions/guide)

The following are the classes in the `functions` namespace.

IN THIS SECTION:

Function Class
Use the Function class to access deployed Salesforce Functions, and invoke them synchronously or asynchronously.

FunctionCallback Interface
Represents the callback Salesforce calls when an asynchronous, queued Function invocation has completed.

FunctionErrorType Enum
Represents the error type of FunctionInvocationError.

FunctionInvocation Interface
Use FunctionInvocation to get the status and results of a synchronous or asynchronous Function invocation.

FunctionInvocationError Interface
Use FunctionInvocationError to get detailed error information about a failed Function invocation.

FunctionInvocationStatus Enum
Represents the status of a Function invocation.


### Apex Reference Guide Function Class

FunctionInvokeMock Interface
Use the `FunctionInvokeMock` interface to mock Salesforce Functions responses during testing.

MockFunctionInvocationFactory Class
Use the `MockFunctionInvocationFactory` methods to generate appropriate mock responses for testing Salesforce
Functions.

### Function Class

Use the Function class to access deployed Salesforce Functions, and invoke them synchronously or asynchronously.

Namespace

functions

Usage

The Function class represents an instance of a deployed Function you can invoke from your org. You can invoke Functions synchronously,
or asynchronously using asynchronous Apex.

If your Function takes longer than 2 minutes to return, the request times out. To avoid timing out, consider using asynchronous invocation.
Invoking a Function asynchronously doesn’t count against asynchronous Apex limits, such as Apex Queueable limits.

Before synchronously invoking a Function, commit any pending data operations in Apex, otherwise you get a CalloutException. For
asynchronous invocations, the queued invocation doesn’t happen if the Apex transaction isn’t committed. Any data operations that
happen in the Function itself aren’t considered part of the Apex transaction.

Functions can’t be invoked in an Apex test. A “Function invocations from Apex tests are not supported” CalloutException is thrown if
Apex determines that a Function is being invoked during a test. If you must run tests against code that invokes Functions, mock your
Function invocations during the tests. See FunctionInvocation Example Implementation for an example of a mocked FunctionInvocation
that you can use in testing.

Example

The following example synchronously invokes a deployed “accountfunction” Function:

```
   functions.Function accountFunction = functions.Function.get('MyProject.accountfunction');

   functions.FunctionInvocation invocation = accountFunction.invoke('{ "accountName" : "Acct",

    "contactName" : "MyContact", "opportunityName" : "Oppty" }');

   String jsonResponse = invocation.getResponse();

```

The following example asynchronously invokes a deployed “AccountFunction” Function, using the provided callback:

```
   functions.Function accountFunction = functions.Function.get('MyProject.accountfunction');

   accountFunction.invoke('{ "accountName" : "Acct", "contactName" : "MyContact",

   "opportunityName" : "Oppty" }', new MyCallback());

   public class MyCallback

     implements functions.FunctionCallback {

      public void handleResponse(functions.FunctionInvocation result) {

       // Handle result of function invocation

       // ...

```


Apex Reference Guide Function Class

```
      }

   }

```

IN THIS SECTION:

#### Function Methods Function Methods The following are methods for Function .

IN THIS SECTION:

##### get(functionName)

Returns the Function instance for the named Function and Project. The Function must be properly deployed and have appropriate
permissions to work with the org running your Apex code.

get(namespace, functionName)
Returns the Function instance for the named Function, Project, and Namespace. The Function must be properly deployed and have
appropriate permissions to work with the org running your Apex code.

invoke(payload, callback)
Invokes the Function asynchronously.

invoke(payload)
Invokes the Function synchronously.

##### get(functionName)

Returns the Function instance for the named Function and Project. The Function must be properly deployed and have appropriate
permissions to work with the org running your Apex code.

Signature

```
   public static functions.Function get(String functionName)

```

Parameters

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
#### “ project name . function name ”. For example, to retrieve the generatepdf Function in the Onboarding Function

Project, use `Onboarding.generatepdf` . The Function and Project must be deployed to a compute environment connected
to the org.

Return Value

Type: functions.Function

Returns a Function instance that you can invoke.


Apex Reference Guide Function Class

Usage

The `Function.get()` method can throw the following exceptions:

**•** `InvalidParameterValueException`   - The _`functionName`_ parameter doesn’t have the correct _`project`_
_`name`_ . _`function name`_ format.

**•** `NoDataFoundException`   - The project or Function name provided in the _`functionName`_ parameter couldn’t be found.
Make sure the project and Function name are spelled correctly and that the project and Function have been properly deployed.

##### get(namespace, functionName)

Returns the Function instance for the named Function, Project, and Namespace. The Function must be properly deployed and have
appropriate permissions to work with the org running your Apex code.

Signature

```
   public static functions.Function get(String namespace, String functionName)

```

Parameters

```
   namespace
```

Type: String

The name of the Namespace that both the Salesforce Function and the Functions Project are part of. The org the Function is in must
be `global` to access across namespaces. Default value is the same org where the method is being called.

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
“ _`project name`_ . _`function name`_ ”. For example, to retrieve the `generatepdf` Function in the `Onboarding` Function
Project, use `Onboarding.generatepdf` . The Function and Project must be deployed to a compute environment connected
to the org.

Return Value

Type: functions.Function

Returns a Function instance that you can invoke.

Usage

The `Function.get()` method can throw the following exceptions:

**•** `InvalidParameterValueException`   - The _`functionName`_ parameter doesn’t have the correct _`project`_
_`name`_ . _`function name`_ format.

**•** `NoDataFoundException`   - The project or Function name provided in the _`functionName`_ parameter couldn’t be found.
Make sure the project and Function name are spelled correctly and that the project and Function have been properly deployed.

**•** `RuntimeException`   - The function is `public` yet references a function across namespaces. Make sure to retrieve references
across namespaces only in a `global` org.

##### invoke(payload, callback)

Invokes the Function asynchronously.


Apex Reference Guide Function Class

Signature

```
   public functions.FunctionInvocation invoke(String payload, functions.FunctionCallback

   callback)

```

Parameters

```
   payload
```

Type: String

The payload data that gets passed to the Function. Specify your payload data in a JSON-format string.

```
   callback
```

Type: functions.FunctionCallback

A FunctionCallback implementation that gets called when your Function is invoked asynchronously.

Return Value

Type: functions.FunctionInvocation

Returns a FunctionInvocation that contains information about the results of the invocation, such as the Function response, or error
results.

Usage

The `Function.invoke(payload, callback)` method can throw the following exceptions:

**•** `CalloutException`   - One of the following conditions causes this exception to be thrown:

**–** [Salesforce Functions isn’t enabled on the current org. For more details on enabling Functions, see Configure Orgs for Functions](https://developer.salesforce.com/docs/platform/functions/guide/config-org#enable-functions-on-dev-hub-orgs)
in the Functions Developer Guide.

**–** The Function is being invoked in an Apex test. Functions can’t be invoked in tests.

**–** The “Functions” permission set is missing or has incorrect permissions for `FunctionInvocationRequest` . For more
details on the correct permissions for `FunctionInvocationRequest` [see Function Permissions in the Functions Developer](https://developer.salesforce.com/docs/platform/functions/guide/permissions)
Guide.

**–** The provided payload isn’t valid JSON.

**–** The Function hasn’t completed deployment to a compute environment or invocation request returns a 404 HTTP error.

**•** `InvalidParameterValueException`   - The _`callback`_ parameter is null or references a class that doesn’t implement
`functions.FunctionCallback` .

**•** `NoDataFoundException`   - A reference for the Function couldn’t be found in the current org. Make sure the project and
Function have been properly deployed.

##### invoke(payload)

Invokes the Function synchronously.

Signature

```
   public functions.FunctionInvocation invoke(String payload)

```


### Apex Reference Guide FunctionCallback Interface

Parameters

```
   payload
```

Type: String

The payload data that gets passed to the Function. Specify your payload data in a JSON-format string.

Return Value

Type: functions.FunctionInvocation

Returns a FunctionInvocation that contains information about the results of the invocation, such as the Function response, or error
results.

Usage

The `Function.invoke(payload)` method can throw the following exceptions:

**•** `CalloutException`   - One of the following conditions causes this exception to be thrown:

**–** [Salesforce Functions isn’t enabled on the current org. For more details on enabling Functions, see Configure Orgs for Functions](https://developer.salesforce.com/docs/platform/functions/guide/config-org#enable-functions-on-dev-hub-orgs)
in the Functions Developer Guide.

**–** The Function is being invoked in an Apex test. Functions can’t be invoked in tests.

**–** The provided payload isn’t valid JSON.

**–** There are pending DML operations.

**–** The Function is being synchronously invoked from an Apex trigger.

**–** The Function hasn’t completed deployment to a compute environment or invocation request returns a 404 HTTP error.

**–** The Function request returns a 5xx HTTP error.

**–** The Function invocation has exceeded the time limit for synchronous invocations. For details on the time limit and work-arounds,
[see Limits in the Functions Developer Guide.](https://developer.salesforce.com/docs/platform/functions/guide/limits#apex-limits-and-functions)

**•** `NoDataFoundException`   - A reference for the Function couldn’t be found in the current org. Make sure the project and
Function have been properly deployed.

### FunctionCallback Interface

Represents the callback Salesforce calls when an asynchronous, queued Function invocation has completed.

Namespace

functions

Usage

When invoking Functions asynchronously via `Function.invoke(payload, callback)`, you provide your own class that
implements FunctionCallback.

IN THIS SECTION:

FunctionCallback Methods

FunctionCallback Example Implementation


### Apex Reference Guide FunctionErrorType Enum

#### FunctionCallback Methods The following are methods for FunctionCallback .

IN THIS SECTION:

##### handleResponse(var1)

Called when an asynchronous Function invocation has completed.

##### handleResponse(var1)

Called when an asynchronous Function invocation has completed.

Signature

```
   public void handleResponse(functions.FunctionInvocation var1)

```

Parameters

```
   var1
```

Type: functions.FunctionInvocation

The result parameter contains JSON response information and error information.

Return Value

Type: void

#### FunctionCallback Example Implementation

This is an example implementation of the `functions.FunctionCallback` interface.

```
   public class MyCallback

     implements functions.FunctionCallback {

      public void handleResponse(functions.FunctionInvocation result) {

       // Handle result of function invocation

       String jsonResponse = result.getResponse();

       System.debug('Got response ' + jsonResponse);

       JSONParser parser = JSON.createParser(jsonResponse);

       // Process JSON using your own data class...

      }

   }

```

The following example uses this implementation when invoking a Function asynchronously:

```
   myFunction.invoke('{ "accountName" : "Acct", "contactName" : "MyContact", "opportunityName"

    : "Oppty" }', new MyCallback());

### FunctionErrorType Enum

```

Represents the error type of FunctionInvocationError.


### Apex Reference Guide FunctionInvocation Interface

Enum Values

These are the values of the `functions.FunctionErrorType` enum.

**Value** **Description**

```
FUNCTION_EXCEPTION

```

A known exception resulting from the Function logic itself. Examples include an
exception thrown from the Function code, or an exception thrown from a library
or framework the Function uses.

`RUNTIME_EXCEPTION` A known exception resulting from the Salesforce Functions runtime. For example,
a malformed payload passed to the Function when invoked results in this error type.

`UNEXPECTED_FUNCTION_EXCEPTION` An unknown exception. For example, a network or system-level issue within the
Salesforce Functions infrastructure results in this error type.

### FunctionInvocation Interface

Use FunctionInvocation to get the status and results of a synchronous or asynchronous Function invocation.

Namespace

functions

Usage

The results of a Function invocation are passed back via FunctionInvocation. Use this instance to determine if the invocation was successful,
and any results from the Function invocation.

You can also implement your own FunctionInvocation interface if you run Apex tests with your Function invocation code. Your test code
can create and use your own FunctionInvocation instance in place of using the results from a call to `Function.invoke()` .

IN THIS SECTION:

#### FunctionInvocation Methods

FunctionInvocation Example Implementation

#### FunctionInvocation Methods

### The following are methods for FunctionInvocation .

IN THIS SECTION:

getError()
Returns error information for a Function invocation.

getInvocationId()
Returns the invocation ID of the Function invocation.

getResponse()
Returns the response string of the Function invocation.


Apex Reference Guide FunctionInvocation Interface

##### getStatus()

Returns the status of the Function invocation.

##### getError()

Returns error information for a Function invocation.

Signature

```
   public functions.FunctionInvocationError getError()

```

Return Value

Type: functions.FunctionInvocationError

Contains a `FunctionInvocationError` instance that you can use to get information about any invocation errors. If the Function
was invoked successfully, the returned instance is null.

##### getInvocationId()

Returns the invocation ID of the Function invocation.

Signature

```
   public String getInvocationId()

```

Return Value

Type: String

This ID is available after a call to either the synchronous or asynchronous `Function.invoke()` methods. For asynchronous
invocations, this ID can be used to check the status of the queued invocation.

##### getResponse()

Returns the response string of the Function invocation.

Signature

```
   public String getResponse()

```

Return Value

Type: String

The response string is the raw request JSON response, which can be parsed using the JSONParser Class.

##### getStatus()

Returns the status of the Function invocation.


### Apex Reference Guide FunctionInvocationError Interface

Signature

```
   public functions.FunctionInvocationStatus getStatus()

```

Return Value

Type: functions.FunctionInvocationStatus

The result of the invocation, such as `FunctionInvocationStatus.SUCCESS` or `FunctionInvocationStatus.ERROR` .

#### FunctionInvocation Example Implementation

This is an example implementation of the `functions.FunctionInvocation` interface.

```
   public class MyFunctionInvocationError

     implements functions.FunctionInvocationError {

      public String getMessage() {

       return 'Mock error message for testing';

      }

      public functions.FunctionErrorType getType() {

       return functions.FunctionErrorType.FUNCTION_EXCEPTION;

      }

   }

   public class MyFunctionInvocation

     implements functions.FunctionInvocation {

      public functions.FunctionInvocationStatus getStatus() {

       return functions.FunctionInvocationStatus.ERROR;

      }

      public String getResponse() {

       return 'Mock response for testing';

      }

      public String getInvocationId() {

       return 'MOCKTESTID';

      }

      public functions.FunctionInvocationError getError() {

       functions.FunctionInvocationError testError = new MyFunctionInvocationError();

       return testError;

      }

   }

```

The following example tests the implementation:

```
   functions.FunctionInvocation testInvocation = new MyFunctionInvocation();

   if (testInvocation.getStatus() == functions.FunctionInvocationStatus.ERROR) {

      System.debug('Error: ' + (testInvocation.getError() != null ?

   testInvocation.getError().getMessage() : 'UNKNOWN'));

      return;

   }

### FunctionInvocationError Interface

```

Use FunctionInvocationError to get detailed error information about a failed Function invocation.


Apex Reference Guide FunctionInvocationError Interface

Namespace

functions

Usage

FunctionInvocationError contains various error information such as the error message at the time of the error.

IN THIS SECTION:

#### FunctionInvocationError Methods

FunctionInvocationError Example Implementation

#### FunctionInvocationError Methods The following are methods for FunctionInvocationError .

IN THIS SECTION:

##### getMessage()

Returns the error message from a Function invocation error.

##### getType()

Returns the error type for FunctionInvocationError.

##### getMessage()

Returns the error message from a Function invocation error.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### **`getType()`**

Returns the error type for FunctionInvocationError.

Signature

```
   public functions.FunctionErrorType getType()

```

Return Value

Type: functions.FunctionErrorType


### Apex Reference Guide FunctionInvocationStatus Enum

#### FunctionInvocationError Example Implementation

This is an example implementation of the `functions.FunctionInvocationError` interface.

```
   public class MyFunctionInvocationError

     implements functions.FunctionInvocationError {

       public String getMessage() {

         return 'Mock error message for testing';

       }

       public functions.FunctionErrorType getType() {

         return functions.FunctionErrorType.FUNCTION_EXCEPTION;

       }

   }

```

This example tests the implementation.

```
   functions.FunctionInvocationError testError = new MyFunctionInvocationError();

   System.debug('Error: ' + testError.getMessage() + ' Type: ' + testError.getType());

### FunctionInvocationStatus Enum

```

Represents the status of a Function invocation.

Enum Values

The following are the values of the `functions.FunctionInvocationStatus` enum.

**Value** **Description**

`ERROR` The invocation failed. Check the FunctionInvocation and FunctionInvocationError
returned by the invoke call to debug the issue.

`PENDING` The invocation is pending. If the Function is being invoked asynchronously, the
invocation is still in the asynch queue.

```
SUCCESS

```

The invocation succeeded. Use `FunctionInvocation.getResponse()`
with the FunctionInvocation instance returned by the invoke call to get any response
returned by the Function.

### FunctionInvokeMock Interface Use the FunctionInvokeMock interface to mock Salesforce Functions responses during testing.

Namespace

functions

Usage

To mock Salesforce Functions testing, implement an appropriate mock response in the `respond(functionName,payload)`
### method of the FunctionInvokeMock interface. During mock testing of a Salesforce Functions, Apex runtime sends the response


Apex Reference Guide FunctionInvokeMock Interface

specified in the `respond()` method, rather than invoking the function itself. Appropriate success and error messages can be configured
with the `createSuccessResponse(invocationId,message)` and
`createErrorResponse(invocationId,functionsErrorType,errorMsg)` methods in
`Functions.MockFunctionInvocationFactory` .

IN THIS SECTION:

#### FunctionInvokeMock Methods

FunctionInvokeMock Example Implementation

#### FunctionInvokeMock Methods The following are methods for FunctionInvokeMock .

IN THIS SECTION:

##### respond(functionName, payload)

The mock response implemented in the `Functions.FunctionInvokeMock` interface. The response is sent by Apex runtime
when the `Test.setMock()` method is called.

##### **`respond(functionName, payload)`**

The mock response implemented in the `Functions.FunctionInvokeMock` interface. The response is sent by Apex runtime
when the `Test.setMock()` method is called.

Signature

```
   public functions.FunctionInvocation respond(String functionName, String payload)

```

Parameters

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
“ _`project name`_ . _`function name`_ ”.

```
   payload
```

Type: String

The JSON-format payload data that is passed to the Function.

Return Value

Type: FunctionInvocation Interface

The result of the mock call to Salesforce Functions. Appropriate responses can be generated by using the
`createSuccessResponse()` and `createErrorResponse()` methods in the
`Functions.MockFunctionInvocationFactory` class.


Apex Reference Guide FunctionInvokeMock Interface

#### FunctionInvokeMock Example Implementation

This is sample implementation of the `functions.FunctionInvokeMock` interface.

```
   @isTest

   public class FunctionsInvokeMockImpl implements functions.FunctionInvokeMock {

      public functions.FunctionInvocation respond(String functionName, String payload) {

        // return mock success response

        String invocationId = '000000000000000';

        String response = 'mockResponse';

       return functions.MockFunctionInvocationFactory.createSuccessResponse(invocationId,

    response);

      }

   }

```

This example shows the minimal setup required for testing synchronous and asynchronous functions and is simplified to include both
function invocations and the `FunctionCallback` class.

```
   @isTest

   public class FunctionTest {

      @isTest

      static void testSyncFunctionCall() {

           // Set mock class to respond to function invocations

        Test.setMock( functions.FunctionInvokeMock.class, new FunctionsInvokeMockInner());

          functions.Function mockedFunction = functions.Function.get('example.function');

           Test.startTest();

           // Synchronous function call

           functions.FunctionInvocation invokeResult = mockedFunction.invoke('{}');

           Test.stopTest();

           // Verify that the received response contains expected mock values

           System.assertEquals(functions.FunctionInvocationStatus.SUCCESS,

   invokeResult.getStatus());

           System.assertEquals('mockResponse', invokeResult.getResponse());

           System.assertEquals('000000000000000', invokeResult.getInvocationId());

        }

        @isTest

        static void testAsyncFunctionCall() {

           // Set mock class to respond to function invocations

           Test.setMock( functions.FunctionInvokeMock.class, new

   FunctionsInvokeMockInner());

          functions.Function mockedFunction = functions.Function.get('example.function2');

           Test.startTest();

           //Asynchronous function invocation with callback

           mockedFunction.invoke('{}', new DemoCallback());

```


### Apex Reference Guide MockFunctionInvocationFactory Class

```
           Test.stopTest();

           // Include assertions here about the expected callback processing

        }

         public class DemoCallback implements functions.FunctionCallback {

           public void handleResponse(functions.FunctionInvocation invokeResult) {

             // Handle result of function invocation

             // The callback is included in the example here for convenience

             // It would normally be defined in the classes being tested

             // Verify that the received response contains expected mock values

             System.assertEquals(invokeResult.getStatus(),

   functions.FunctionInvocationStatus.ERROR);

             functions.FunctionInvocationError resultError = invokeResult.getError();

           System.assertEquals('bang', invokeResult.getError().getMessage());

           System.assertEquals('000000000000000', invokeResult.getInvocationId());

           }

        }

        public class FunctionsInvokeMockInner implements functions.FunctionInvokeMock {

          public functions.FunctionInvocation respond(String functionName, String payload)

    {

             // return mock success response

             String invocationId = '000000000000000';

             if(functionName == 'example.function2') {

               return functions.MockFunctionInvocationFactory.createErrorResponse(

                  invocationId,

                  functions.FunctionErrorType.FUNCTION_EXCEPTION,

                  'bang');

             }

             String response = 'mockResponse';

             return

   functions.MockFunctionInvocationFactory.createSuccessResponse(invocationId, response);

           }

        }

      }

### MockFunctionInvocationFactory Class Use the MockFunctionInvocationFactory methods to generate appropriate mock responses for testing Salesforce Functions.

```

Namespace

functions


Apex Reference Guide MockFunctionInvocationFactory Class

Usage

To mock Salesforce Functions testing, implement an appropriate mock response in the `respond(functionName,payload)`
method of the `FunctionInvokeMock` interface. During mock testing of a Salesforce Functions, the Apex runtime sends the response
specified in the `respond()` method, rather than invoking the function itself. Appropriate success and error messages can be configured
with the `createSuccessResponse(invocationId,message)` and
`createErrorResponse(invocationId,functionsErrorType,errorMsg)` methods.

See FunctionInvokeMock Example Implementation.

IN THIS SECTION:

#### MockFunctionInvocationFactory Methods MockFunctionInvocationFactory Methods The following are methods for MockFunctionInvocationFactory .

IN THIS SECTION:

##### createErrorResponse(invocationId, functionsErrorType, errMsg)

Generate a response for an error condition during mock testing of Salesforce Functions.

createSuccessResponse(invocationId, response)
Generate a response for a successful mock test of Salesforce Functions.

##### **`createErrorResponse(invocationId, functionsErrorType, errMsg)`**

Generate a response for an error condition during mock testing of Salesforce Functions.

Signature

```
   public static functions.FunctionInvocation createErrorResponse(String invocationId,

   functions.FunctionErrorType functionsErrorType, String errMsg)

```

Parameters

```
   invocationId
```

Type: String

The ID associated with a call to either the synchronous or asynchronous `Function.invoke()` method.

```
   functionsErrorType
```

Type: FunctionErrorType Enum

The error type of `FunctionInvocationError` .

```
   errMsg
```

Type: String

The error message.

Return Value

Type: FunctionInvocation Interface


## Apex Reference Guide ise_bots_apex Namespace

##### **`createSuccessResponse(invocationId, response)`**

Generate a response for a successful mock test of Salesforce Functions.

Signature

```
   public static functions.FunctionInvocation createSuccessResponse(String invocationId,

   String response)

```

Parameters

```
   invocationId
```

Type: String

The ID associated with a call to either the synchronous or asynchronous `Function.invoke()` method.

```
   response
```

Type: String

The message indicating success.

Return Value

Type: FunctionInvocation Interface

## ise_bots_apex Namespace

The ise_bots_apex namespace provides classes and properties to facilitate dynamic content generation and data handling for menu-driven
bot interactions. Create and manage dynamic menu items that adapt to user inputs, context, and underlying object data.

## The ise_bots_apex namespace includes these classes.

IN THIS SECTION:

### DynamicMenuItem Class

Contains properties to define and hold the details for a single dynamic menu item Each item contains information related to an
object, such as identifiers, labels, summaries, and sorting logic. It enables bots to present context-aware and user-relevant choices
dynamically during conversations. .

### DynamicMenuItem Class

Contains properties to define and hold the details for a single dynamic menu item Each item contains information related to an object,
such as identifiers, labels, summaries, and sorting logic. It enables bots to present context-aware and user-relevant choices dynamically
during conversations. .

Namespace

ise_bots_apex on page 2873


Apex Reference Guide DynamicMenuItem Class

IN THIS SECTION:

#### DynamicMenuItem Properties

Learn more about the properties available with the DynamicMenuItem class.

#### DynamicMenuItem Properties

Learn more about the properties available with the DynamicMenuItem class.

#### The DynamicMenuItem class includes these properties.

IN THIS SECTION:

##### EntityId

API name representing the ID field of the related Salesforce object.

##### EntityIdValue

The ID value retrieved at run time for the associated object.

EntityName
API name or label of the object being referenced, for example Case, Contact, or a custom object such as Service__c.

EntityNameValue
The name of the specific object instance.

Label
The label used to define how the item must be displayed in the bot menu.

LabelValue
The value of the label displayed to the user for the menu item at run time.

SummaryTextWithFormula
A formula or a string of text that defines the structure of the summary text displayed for the item. This formula is used to construct
a dynamic summary for the user after they make a selection.

SummaryTextWithFormulaValue
The summary string based on the formula and object data.

sortByDate
The API name of a date or date/time field on the object that's used to sort the dynamic menu items.

sortByDateValue
The DateTime value used at run time to sort the menu items chronologically.

##### **`EntityId`**

API name representing the ID field of the related Salesforce object.

Signature

```
   public String EntityId {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityId

```


Apex Reference Guide DynamicMenuItem Class

Property Value

Type: String

##### **`EntityIdValue`**

The ID value retrieved at run time for the associated object.

Signature

```
   public String EntityIdValue {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityIdValue

```

Property Value

Type: String

##### **`EntityName`**

API name or label of the object being referenced, for example Case, Contact, or a custom object such as Service__c.

Signature

```
   public String EntityName {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityName

```

Property Value

Type: String

##### **`EntityNameValue`**

The name of the specific object instance.

Signature

```
   public String EntityNameValue {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityNameValue

```

Property Value

Type: String

##### **`Label`**

The label used to define how the item must be displayed in the bot menu.


Apex Reference Guide DynamicMenuItem Class

Signature

```
   public String Label {get; set;}

   ise_bots_apex.DynamicMenuItem, Label

```

Property Value

Type: String

##### **`LabelValue`**

The value of the label displayed to the user for the menu item at run time.

Signature

```
   public String LabelValue {get; set;}

   ise_bots_apex.DynamicMenuItem, LabelValue

```

Property Value

Type: String

##### **`SummaryTextWithFormula`**

A formula or a string of text that defines the structure of the summary text displayed for the item. This formula is used to construct a
dynamic summary for the user after they make a selection.

Signature

```
   public String SummaryTextWithFormula {get; set;}

   ise_bots_apex.DynamicMenuItem, SummaryTextWithFormula

```

Property Value

Type: String

##### **`SummaryTextWithFormulaValue`**

The summary string based on the formula and object data.

Signature

```
   public String SummaryTextWithFormulaValue {get; set;}

   ise_bots_apex.DynamicMenuItem, SummaryTextWithFormulaValue

```

Property Value

Type: String


## Apex Reference Guide industriesNlpSvc

##### **`sortByDate`**

The API name of a date or date/time field on the object that's used to sort the dynamic menu items.

Signature

```
   public Date sortByDate {get; set;}

   ise_bots_apex.DynamicMenuItem, sortByDate

```

Property Value

Type: Date

##### **`sortByDateValue`**

The DateTime value used at run time to sort the menu items chronologically.

Signature

```
   public Date sortByDateValue {get; set;}

   ise_bots_apex.DynamicMenuItem, sortByDateValue

```

Property Value

Type: Date

## industriesNlpSvc

Stores the objects used in Industries Einstein Natural Language Processing (NLP) services.

The industriesNlpSvc namespace contains these classes that are the outputs for the transformNlpActionResult Invocable action.

### • NlpResponse — Stores the NLP Summarization result performed for an NLP Operation involving summarization use cases such

as SurveyLongSummarization and SurveyShortSummarization.

**•** _`NlpSummarizationResult`_   - Provides the summary obtained as result of NLP Operation.

IN THIS SECTION:

### NlpResponse Class

Stores the result for an NLP Operation. NLP operation can be SurveyLongSummarization and SurveyShortSummarization.

NlpSummarizationResult Class
Provides the summary obtained as result of NLP Operation.

### NlpResponse Class

Stores the result for an NLP Operation. NLP operation can be SurveyLongSummarization and SurveyShortSummarization.


### Apex Reference Guide NlpSummarizationResult Class

Namespace

industriesNlpSvc

IN THIS SECTION:

#### NlpResponse Properties NlpResponse Properties The following are properties for NlpResponse .

IN THIS SECTION:

##### summarizationResult

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

##### errors

Represents the property to store errors that occurred as a result of the NLP Operation.

##### **`summarizationResult`**

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

Signature

```
   public industriesNlpSvc.NlpSummarizationResult summarizationResult {get; set;}

```

Property Value

Type: List<industriesNlpSvc.NlpSummarizationResult on page 2878>

##### **`errors`**

Represents the property to store errors that occurred as a result of the NLP Operation.

Signature

```
   public List<String> errors {get; set;}

```

Property Value

Type: List<String>

### NlpSummarizationResult Class

Provides the summary obtained as result of NLP Operation.


## Apex Reference Guide IndustriesDigitalLending Namespace

Namespace

industriesNlpSvc

IN THIS SECTION:

#### NlpSummarizationResult Properties NlpSummarizationResult Properties The following are properties for NlpSummarizationResult :

IN THIS SECTION:

##### summary

Represents the field that captures the summary obtained as result of NLP Operation.

##### **`summary`**

Represents the field that captures the summary obtained as result of NLP Operation.

Signature

```
   public String summary {get; set;}

```

Property Value

Type: List<String>

## IndustriesDigitalLending Namespace

The `industriesDigitalLending` namespace provides classes used in the Digital Lending OmniScripts and Integration Procedures.

The industriesDigitalLending namespace contains these classes:

**•** _`DigitalLendingIntakeRecordsWrapper`_   - Use the callable DigitalLendingIntakeRecordsWrapper class to call utility
methods from OmniScripts used in Digital Lending application intake process.

**•** _`DigitalLendingPostIntakeRecordsWrapper`_   - Use the callable DigitalLendingPostIntakeRecordsWrapper class to
call utility methods from integration procedures used in Digital Lending post intake in FlexCards.

**•** _`DigitalLendingProductsApi`_   - Use the callable DigitalLendingProductsApi class to call utility methods from integration
procedures used in Digital Lending FlexCards.

**•** _`DigitalLendingUtils`_   - Use the callable DigitalLendingUtils class to call utility methods from integration procedures used
in Digital Lending PostIntake FlexCards.

**•** _`PricingExecutionWrapper`_   - Use the callable PricingExecutionWrapper class to call utility methods from integration
procedures used in Digital Lending FlexCards.

[See industriesDigitalLending namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_namespace_industriesDigitalLending.htm)


## Apex Reference Guide Invocable Namespace Invocable Namespace The Invocable namespace provides classes for calling invocable actions from Apex. These classes are in the Invocable namespace.

IN THIS SECTION:

### Action Class

Contains methods to create, update, and retrieve information about invocable actions.

Action.Error Class
Contains methods to retrieve errors returned by invocable actions.

Action.Result Class
Contains methods to retrieve results from invocable actions called from Apex code.

### Action Class

Contains methods to create, update, and retrieve information about invocable actions.

Namespace

## Invocable

IN THIS SECTION:

#### Action Methods

SEE ALSO:

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_Salesforce Help_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

#### Action Methods

### These methods are for Action .

IN THIS SECTION:

addInvocation()
Creates an empty invocation in preparation for calling an invocable action. After you create the invocation, you can add parameters
to the invocation.

clearInvocations()
Clears the existing invocations from the action.

clone()
Creates a copy of the `Invocable.Action` .

createCustomAction(type, namespace, name, version)
Creates a wrapper for the specified version of a custom invocable action in a specified package namespace.


Apex Reference Guide Action Class

createCustomAction(type, namespace, name)
Creates a wrapper for a custom invocable action in a specified package namespace.

createCustomAction(type, name)
Creates a wrapper for a custom invocable action.

createStandardAction(type, version)
Creates a wrapper for a standard invocable action.

createStandardAction(type)
Creates a wrapper for a standard invocable action.

getName()
Gets the name of an invocable action.

getNamespace()
Gets the namespace of a custom invocable action.

getType()
Gets the type of an invocable action.

invoke()
Invokes an invocable action from Apex code.

isStandard()
Determines whether an invocable action is a standard invocable action.

setInvocationParameter(parameterName, parameterValue)
Sets a value for an invocable action parameter.

setInvocations(invocations)
Initializes the invocations for an action from a pre-existing list of invocations.

##### **`addInvocation()`**

Creates an empty invocation in preparation for calling an invocable action. After you create the invocation, you can add parameters to
the invocation.

Signature

```
   public Invocable.Action addInvocation()

```

Return Value

Type: Invocable.Action on page 2880

##### **`clearInvocations()`**

Clears the existing invocations from the action.

Signature

```
   public Invocable.Action clearInvocations()

```


Apex Reference Guide Action Class

Return Value

Type: Invocable.Action on page 2880

##### **`clone()`**

Creates a copy of the `Invocable.Action` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### **`createCustomAction(type, namespace, name, version)`**

Creates a wrapper for the specified version of a custom invocable action in a specified package namespace.

Signature

```
   public static Invocable.Action createCustomAction(String type, String namespace, String

   name)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

```
   namespace
```

Type: String

Namespace where the invocable action is located.

```
   name
```

Type: String

Name for the custom invocable action.

```
   version
```

Type: String

Version of the invocable action.

Return Value

Type: Invocable.Action

##### **`createCustomAction(type, namespace, name)`**

Creates a wrapper for a custom invocable action in a specified package namespace.


Apex Reference Guide Action Class

Signature

```
   public static Invocable.Action createCustomAction(String type, String namespace, String

   name)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

```
   namespace
```

Type: String

Namespace where the invocable action is located.

```
   name
```

Type: String

Name for the custom invocable action.

Return Value

Type: Invocable.Action

##### **`createCustomAction(type, name)`**

Creates a wrapper for a custom invocable action.

Signature

```
   public static Invocable.Action createCustomAction(String type, String name)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

```
   name
```

Type: String

Name for the custom invocable action.

Return Value

Type: Invocable.Action

##### **`createStandardAction(type, version)`**

Creates a wrapper for a standard invocable action.


Apex Reference Guide Action Class

Signature

```
   public static Invocable.Action createStandardAction(String type)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

```
   version
```

Type: String

Version of the invocable action.

Return Value

Type: Invocable.Action

##### **`createStandardAction(type)`**

Creates a wrapper for a standard invocable action.

Signature

```
   public static Invocable.Action createStandardAction(String type)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

Return Value

Type: Invocable.Action

##### **`getName()`**

Gets the name of an invocable action.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the invocable action.


Apex Reference Guide Action Class

##### **`getNamespace()`**

Gets the namespace of a custom invocable action.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Namespace of the custom invocable action.

##### **`getType()`**

Gets the type of an invocable action.

Signature

```
   public String getType()

```

Return Value

Type: String

Type of invocable action.

##### **`invoke()`**

Invokes an invocable action from Apex code.

Signature

```
   public List<Invocable.Action.Result> invoke()

```

Return Value

Type: List<Invocable.Action.Result>

##### **`isStandard()`**

Determines whether an invocable action is a standard invocable action.

Signature

```
   public Boolean isStandard()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action is a standard invocable action.


### Apex Reference Guide Action.Error Class

##### **`setInvocationParameter(parameterName, parameterValue)`**

Sets a value for an invocable action parameter.

Signature

```
   public Invocable.Action setInvocationParameter(String parameterName, Object

   parameterValue)

```

Parameters

```
   parameterName
```

Type: String

Name of the invocable action parameter to set.

```
   parameterValue
```

Type: Object

Value to set the invocable action parameter to.

Return Value

Type: Invocable.Action on page 2880

##### **`setInvocations(invocations)`**

Initializes the invocations for an action from a pre-existing list of invocations.

Signature

```
   public Invocable.Action setInvocations(List<Map<String,ANY>> invocations)

```

Parameters

```
   invocations
```

Type: List on page 3891<Map on page 3911<String on page 4124,ANY>>

List of invocations for the invocable action.

Return Value

Type: Invocable.Action on page 2880

### Action.Error Class

Contains methods to retrieve errors returned by invocable actions.

Namespace

Invocable


Apex Reference Guide Action.Error Class

IN THIS SECTION:

#### Action.Error Methods Action.Error Methods These methods are for Action.Error .

IN THIS SECTION:

##### clone()

Creates a copy of the `Invocable.Action.Error` .

##### getCode()

Gets the error code returned by an invocable action.

##### getMessage()

Gets the error message returned by an invocable action.

##### **`clone()`**

Creates a copy of the `Invocable.Action.Error` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### **`getCode()`**

Gets the error code returned by an invocable action.

Signature

```
   public String getCode()

```

Return Value

Type: String

##### **`getMessage()`**

Gets the error message returned by an invocable action.

Signature

```
   public String getMessage()

```


### Apex Reference Guide Action.Result Class

Return Value

Type: String

### Action.Result Class

Contains methods to retrieve results from invocable actions called from Apex code.

Namespace

Invocable

IN THIS SECTION:

#### Action.Result Methods Action.Result Methods

### The methods are for Action.Result .

IN THIS SECTION:

##### clone()

Creates a copy of the `Invocable.Action.Result` .

getAction()
Gets the invocable action that was invoked and caused a result to be returned.

getErrors()
Gets a list of errors that were returned by an invocable action.

getInvocationParameters()
Gets a list of the parameter values set for an invocable action. This method returns a list that contains the input parameter values
for each invocation of an action. Each map in the list contains a key for the name of each input parameter.

getOutputParameters()
Gets a list of the parameter values returned by an invocable action. This method returns a list that contains the result for each
invocation of an action. Each map in the list contains a key for the name of each output parameter.

isSuccess()
Determines if an invocable action ran without errors.

##### **`clone()`**

Creates a copy of the `Invocable.Action.Result` .

Signature

```
   public Object clone()

```

Return Value

Type: Object


Apex Reference Guide Action.Result Class

##### **`getAction()`**

Gets the invocable action that was invoked and caused a result to be returned.

Signature

```
   public Invocable.Action getAction()

```

Return Value

Type: Invocable.Action on page 2880

##### **`getErrors()`**

Gets a list of errors that were returned by an invocable action.

Signature

```
   public List on page 4124<Invocable.Action.Error on page 2886> getErrors()

```

Return Value

Type: List on page 4124<Invocable.Action.Error on page 2886>

##### **`getInvocationParameters()`**

Gets a list of the parameter values set for an invocable action. This method returns a list that contains the input parameter values for
each invocation of an action. Each map in the list contains a key for the name of each input parameter.

Signature

```
   public Map<String,Object> getInvocationParameters()

```

Return Value

Type: Map on page 3911<String on page 4124,Object>

##### **`getOutputParameters()`**

Gets a list of the parameter values returned by an invocable action. This method returns a list that contains the result for each invocation
of an action. Each map in the list contains a key for the name of each output parameter.

Signature

```
   public Map<String,Object> getOutputParameters()

```

Return Value

Type: Map on page 3911<String on page 4124,Object>


## Apex Reference Guide InvoiceWriteOff Namespace

##### **`isSuccess()`**

Determines if an invocable action ran without errors.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action ran successfully.

## InvoiceWriteOff Namespace The InvoiceWriteOff namespace provides classes to create credit memos with the total charge amount on the invoice as the

write-off amount.

## The InvoiceWriteOff namespace includes these classes.

**•** [WriteOffInvoiceInputList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm)

**•** [WriteOffInvoiceInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm)

**•** [WriteOffInvoiceResponseList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm)

**•** [WriteOffInvoiceResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm)

**•** [WriteOffInvoiceResponseError Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm)

## IsvPartners Namespace The IsvPartners namespace provides a class associated with Salesforce ISV partner use cases, such as optimizing code, providing

great customer trial experiences, and driving feature adoption.

## These are the classes in the IsvPartners namespace.

IN THIS SECTION:

### AppAnalytics Class

Contains methods to help with AppExchange App Analytics use cases, such as minimizing subscriber attrition and obtaining product
insights.

### AppAnalytics Class

Contains methods to help with AppExchange App Analytics use cases, such as minimizing subscriber attrition and obtaining product
insights.

Namespace

## IsvPartners


Apex Reference Guide AppAnalytics Class

Usage

#### Use AppAnalytics and its methods to log App Analytics custom interactions.

Example

```
   public void submitClicked() {

        Id jobId = System.enqueueJob(new MyQueueable(colorValue));

        IsvPartners.AppAnalytics.logCustomInteraction(

           MyPageInteractions.SUBMIT_CLICKED, jobId);

```

IN THIS SECTION:

#### AppAnalytics Methods AppAnalytics Methods These are methods for AppAnalytics .

IN THIS SECTION:

##### logCustomInteraction(interactionLabel, interactionId)

Logs the custom interaction using a label that you provide as an enum value and an interaction ID.

logCustomInteraction(interactionLabel, interactionUuid)
Logs the custom interaction using a label that you provide as an enum value and an interaction ID that you provide as an Apex UUID.

logCustomInteraction(interactionLabel)
Logs the custom interaction using a label that you provide as an enum value.

##### **`logCustomInteraction(interactionLabel, interactionId)`**

Logs the custom interaction using a label that you provide as an enum value and an interaction ID.

Signature

```
   public static void logCustomInteraction(Object interactionLabel, Id interactionId)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

```
   interactionId
```

Type: Id

An Apex ID that is associated with the custom interaction. The `interactionId` that you provide is hashed and tokenized before
it’s included in AppExchange App Analytics package usage logs.


Apex Reference Guide AppAnalytics Class

Return Value

Type: Void

##### **`logCustomInteraction(interactionLabel, interactionUuid)`**

Logs the custom interaction using a label that you provide as an enum value and an interaction ID that you provide as an Apex UUID.

Signature

```
   public static void logCustomInteraction(Object interactionLabel, System.UUID

   interactionUuid)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

```
   interactionUuid
```

Type: System.UUID

An Apex UUID that is associated with the custom interaction. The `interactionId` that you provide is hashed and tokenized
before being included in AppExchange App Analytics package usage logs.

Return Value

Type: Void

##### **`logCustomInteraction(interactionLabel)`**

Logs the custom interaction using a label that you provide as an enum value.

Signature

```
   public static void logCustomInteraction(Object interactionLabel)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

Return Value

Type: Void


## Apex Reference Guide KbManagement Namespace KbManagement Namespace The KbManagement namespace provides a class for managing knowledge articles. The following is the class in the KbManagement namespace.

IN THIS SECTION:

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.

Namespace

## KbManagement

Usage

Use the methods in the `KbManagement.PublishingService` class to manage the following parts of the lifecycle of an article
and its translations:

### • Publishing

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

#### PublishingService Methods

### The following are methods for PublishingService . All methods are static.

IN THIS SECTION:

archiveOnlineArticle(articleId, scheduledDate)
Archives an online version of an article. If the specified scheduledDate is null, the article is archived immediately. Otherwise, it archives
the article on the scheduled date.


Apex Reference Guide PublishingService Class

assignDraftArticleTask(articleId, assigneeId, instructions, dueDate, sendEmailNotification)
Assigns a review task related to a draft article.

assignDraftTranslationTask(articleVersionId, assigneeId, instructions, dueDate, sendEmailNotification)
Assigns a review task related to a draft translation.

cancelScheduledArchivingOfArticle(articleId)
Cancels the scheduled archiving of an online article.

cancelScheduledPublicationOfArticle(articleId)
Cancels the scheduled publication of a draft article.

completeTranslation(articleVersionId)
Puts a translation in a completed state that is ready to publish.

deleteArchivedArticle(articleId)
Deletes an archived article.

deleteArchivedArticleVersion(articleId, versionNumber)
Deletes a specific archived version of a published article.

deleteDraftArticle(articleId)
Deletes a draft article.

deleteDraftTranslation(articleVersionId)
Deletes a draft translation.

editArchivedArticle(articleId)
Creates a draft article from the archived primary version and returns the new draft primary version ID of the article.

editOnlineArticle(articleId, unpublish)
Creates a draft article from the online version and returns the new draft primary version ID of the article. Also, unpublishes the online
article, if _`unpublish`_ is set to `true` .

editPublishedTranslation(articleId, language, unpublish)
Creates a draft version of the online translation for a specific language and returns the new draft primary version ID of the article.
Also, unpublishes the article, if set to `true` .

publishArticle(articleId, flagAsNew)
Publishes an article. If _`flagAsNew`_ is set to `true`, the article is published as a major version.

restoreOldVersion(articleId, versionNumber)
Creates a draft article from an existing online article based on the specified archived version of the article and returns the article
version ID.

scheduleForPublication(articleId, scheduledDate)
Schedules the article for publication as a major version. If the specified date is null, the article is published immediately.

setTranslationToIncomplete(articleVersionId)
Sets a draft translation that is ready for publication back to “in progress” status.

submitForTranslation(articleId, language, assigneeId, dueDate)
Submits an article for translation to the specified language. Also assigns the specified user and due date to the submittal and returns
new ID of the draft translation.


Apex Reference Guide PublishingService Class

##### archiveOnlineArticle(articleId, scheduledDate)

Archives an online version of an article. If the specified scheduledDate is null, the article is archived immediately. Otherwise, it archives
the article on the scheduled date.

Signature

```
   public static Void archiveOnlineArticle(String articleId, Datetime scheduledDate)

```

Parameters

```
   articleId
```

Type: String

```
   scheduledDate
```

Type: Datetime

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Datetime scheduledDate = Datetime.newInstanceGmt(2012, 12,1,13,30,0);

   KbManagement.PublishingService.archiveOnlineArticle(articleId, scheduledDate);

##### assignDraftArticleTask(articleId, assigneeId, instructions, dueDate, sendEmailNotification)

```

Assigns a review task related to a draft article.

Signature

```
   public static Void assignDraftArticleTask(String articleId, String assigneeId, String

   instructions, Datetime dueDate, Boolean sendEmailNotification)

```

Parameters

```
   articleId
```

Type: String

```
   assigneeId
```

Type: String

```
   instructions
```

Type: String

```
   dueDate
```

Type: Datetime

```
   sendEmailNotification
```

Type: Boolean


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   String assigneeId = '';

   String instructions = 'Please review this draft.';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12, 1);

   KbManagement.PublishingService.assignDraftArticleTask(articleId, assigneeId, instructions,

    dueDate, true);

##### assignDraftTranslationTask(articleVersionId, assigneeId, instructions, dueDate, sendEmailNotification)

```

Assigns a review task related to a draft translation.

Signature

```
   public static Void assignDraftTranslationTask(String articleVersionId, String assigneeId,

   String instructions, Datetime dueDate, Boolean sendEmailNotification)

```

Parameters

```
   articleVersionId
```

Type: String

```
   assigneeId
```

Type: String

```
   instructions
```

Type: String

```
   dueDate
```

Type: Datetime

```
   sendEmailNotification
```

Type: Boolean

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   String assigneeId = ' Insert assignee ID ';

   String instructions = 'Please review this draft.';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12, 1);

   KbManagement.PublishingService.assignDraftTranslationTask(articleId, assigneeId,

   instructions, dueDate, true);

```


Apex Reference Guide PublishingService Class

##### cancelScheduledArchivingOfArticle(articleId)

Cancels the scheduled archiving of an online article.

Signature

```
   public static Void cancelScheduledArchivingOfArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.cancelScheduledArchivingOfArticle (articleId);

##### cancelScheduledPublicationOfArticle(articleId)

```

Cancels the scheduled publication of a draft article.

Signature

```
   public static Void cancelScheduledPublicationOfArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.cancelScheduledPublicationOfArticle (articleId);

##### completeTranslation(articleVersionId)

```

Puts a translation in a completed state that is ready to publish.

Signature

```
   public static Void completeTranslation(String articleVersionId)

```


Apex Reference Guide PublishingService Class

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.completeTranslation(articleVersionId);

##### deleteArchivedArticle(articleId)

```

Deletes an archived article.

Signature

```
   public static Void deleteArchivedArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.deleteArchivedArticle(articleId);

##### deleteArchivedArticleVersion(articleId, versionNumber)

```

Deletes a specific archived version of a published article.

Signature

```
   public static Void deleteArchivedArticleVersion(String articleId, Integer versionNumber)

```

Parameters

```
   articleId
```

Type: String

```
   versionNumber
```

Type: Integer


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Integer versionNumber = 1;

   KbManagement.PublishingService.deleteArchivedArticleVersion(articleId, versionNumber);

##### deleteDraftArticle(articleId)

```

Deletes a draft article.

Signature

```
   public static Void deleteDraftArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.deleteDraftArticle(articleId);

##### deleteDraftTranslation(articleVersionId)

```

Deletes a draft translation.

Signature

```
   public static Void deleteDraftTranslation(String articleVersionId)

```

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void


Apex Reference Guide PublishingService Class

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.deleteDraftTranslation (articleVersionId);

##### editArchivedArticle(articleId)

```

Creates a draft article from the archived primary version and returns the new draft primary version ID of the article.

Signature

```
   public static String editArchivedArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.editArchivedArticle(articleId);

##### editOnlineArticle(articleId, unpublish)

```

Creates a draft article from the online version and returns the new draft primary version ID of the article. Also, unpublishes the online
article, if _`unpublish`_ is set to `true` .

Signature

```
   public static String editOnlineArticle(String articleId, Boolean unpublish)

```

Parameters

```
   articleId
```

Type: String

```
   unpublish
```

Type: Boolean

Return Value

Type: String


Apex Reference Guide PublishingService Class

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.editOnlineArticle (articleId, true);

##### editPublishedTranslation(articleId, language, unpublish)

```

Creates a draft version of the online translation for a specific language and returns the new draft primary version ID of the article. Also,
unpublishes the article, if set to `true` .

Signature

```
   public static String editPublishedTranslation(String articleId, String language, Boolean

   unpublish)

```

Parameters

```
   articleId
```

Type: String

```
   language
```

Type: String

```
   unpublish
```

Type: Boolean

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String language = 'fr';

   String id = KbManagement.PublishingService.editPublishedTranslation(articleId, language,

   true);

##### publishArticle(articleId, flagAsNew)

```

Publishes an article. If _`flagAsNew`_ is set to `true`, the article is published as a major version.

Signature

```
   public static Void publishArticle(String articleId, Boolean flagAsNew)

```

Parameters

```
   articleId
```

Type: String

```
   flagAsNew
```

Type: Boolean


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.publishArticle(articleId, true);

##### restoreOldVersion(articleId, versionNumber)

```

Creates a draft article from an existing online article based on the specified archived version of the article and returns the article version
ID.

Signature

```
   public static String restoreOldVersion(String articleId, Integer versionNumber)

```

Parameters

```
   articleId
```

Type: String

```
   versionNumber
```

Type: Integer

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.restoreOldVersion (articleId, 1);

##### scheduleForPublication(articleId, scheduledDate)

```

Schedules the article for publication as a major version. If the specified date is null, the article is published immediately.

Signature

```
   public static Void scheduleForPublication(String articleId, Datetime scheduledDate)

```

Parameters

```
   articleId
```

Type: String

```
   scheduledDate
```

Type: Datetime


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Datetime scheduledDate = Datetime.newInstanceGmt(2012, 12,1,13,30,0);

   KbManagement.PublishingService.scheduleForPublication(articleId, scheduledDate);

##### setTranslationToIncomplete(articleVersionId)

```

Sets a draft translation that is ready for publication back to “in progress” status.

Signature

```
   public static Void setTranslationToIncomplete(String articleVersionId)

```

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.setTranslationToIncomplete(articleVersionId);

##### submitForTranslation(articleId, language, assigneeId, dueDate)

```

Submits an article for translation to the specified language. Also assigns the specified user and due date to the submittal and returns
new ID of the draft translation.

Signature

```
   public static String submitForTranslation(String articleId, String language, String

   assigneeId, Datetime dueDate)

```

Parameters

```
   articleId
```

Type: String

```
   language
```

Type: String

```
   assigneeId
```

Type: String


## Apex Reference Guide LxScheduler Namespace

```
   dueDate
```

Type: Datetime

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String language = 'fr';

   String assigneeId = ' Insert assignee ID ';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12,1);

   String id = KbManagement.PublishingService.submitForTranslation(articleId, language,

   assigneeId, dueDate);

## LxScheduler Namespace The LxScheduler namespace provides an interface and classes for integrating Salesforce Scheduler with external calendars. The following are the classes and the interface in the LxScheduler namespace.

```

IN THIS SECTION:

GetAppointmentCandidatesInput Class
Contains information about the available service resources (appointment candidates) based on work type group and service territories.

GetAppointmentCandidatesInputBuilder Class
Contains methods to build an instance of the `lxscheduler.GetAppointmentCandidatesInput` class.

GetAppointmentSlotsInput Class
Contains information about the available appointment time slots for a resource based on given work type group and territories.

GetAppointmentSlotsInputBuilder Class
Contains methods to build an instance of the `lxscheduler.GetAppointmentSlotsInput` class.

SchedulerResources Class
Contains methods that holds the business logic to get resources availability.

SkillRequirement Class
Contains information about the set of skills that are required to complete a particular task for a work type.

SkillRequirementBuilder Class
Contains methods to build an instance of the `lxscheduler.SkillRequirement` class.

WorkType Class
Contains information about the type of work to be performed.

WorkTypeBuilder Class
Contains methods to build an instance of the `lxscheduler.WorkType` class.

ServiceResourceScheduleHandler Interface
Allows an implementing class to check external calendar events to find already booked time slots for the requested service resources.
This interface is part of Salesforce Scheduler.


### Apex Reference Guide GetAppointmentCandidatesInput Class

ServiceAppointmentRequestInfo Class
Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface. This class is implemented internally
by Apex.

ServiceResourceInfo Class
Contains information about a service resource.

ServiceResourceSchedule Class
Use this class to pass results from your implemented Apex class to the ServiceResourceScheduleHandler interface methods.

UnavailableTimeslot Class
Use this class to pass the unavailable time slots to the lxscheduler.ServiceResourceSchedule class. Timezones that differ across
operating hours are handled and results are always returned in UTC.

SEE ALSO:

[Apex Interface Implementation Limitations and Error Codes](https://help.salesforce.com/s/articleView?id=platform.ls_ext_cal_integration_troubleshooting.htm&type=5&language=en_US)

### GetAppointmentCandidatesInput Class

Contains information about the available service resources (appointment candidates) based on work type group and service territories.

Set up Salesforce Scheduler before making requests. This setup includes creating or configuring Service Resources, Service Territory
[Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Set Up Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&type=5&language=en_US)
for more information.

The appointment time slots are determined based on multiple factors, such as field values, scheduled appointments, absences, Scheduler
[Settings, and Scheduling Policies to determine available time slots. See How Salesforce Scheduler Determines Available Time Slots for](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
more information.

The following factors are considered for returning start time and end time of resources.

**Resource Availability**
Determined using service territory member, service territory, work type, and account operating hours fields.

**Resource Unavailability**
Determined by resource absences, existing appointments that the resource is assigned to. The resource must be marked as a required
resource for the appointment with a status that isn’t in closed, canceled, or completed.

**Appointment Start Time Interval in the Scheduling Policy**
Appointment start time interval field in the Scheduling Policy is used to determine when the appointment can start. This interval
can be 5, 10, 15, 20, 30, or 60. By default, it’s set to 15.

**Work Type Duration**
The end time is calculated as start time + duration of the work type.

Note: If asset scheduling is enabled, the response also includes asset-based candidates.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentCandidatesInput Class

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the
GetAppointmentCandidatesInputBuilder.build() method.

This example shows how to get a list of available appointment candidates based on `workTypeGroupId` :

```
   //Build input for GetAppointmentCandidates API

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkTypeGroupId('0VSRM0000000ABc4AM')

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

   .setEndTime(System.now().addDays(5).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

      .setAccountId('001RM0000053iQgYAI')

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows how to get a list of available appointment candidates based on `workType` :

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

      .setId('08qRM0000000G9RYAU')

      .build();

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkType(workType)

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

   .setEndTime(System.now().addDays(5).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

      .setAccountId('001RM0000053iQgYAI')

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows how to get a list of available candidate appointments based on `durationInMinutes` and without the
`workTypeGroupId` or `workType` fields:

Important: If you're using shifts, you must specify the `workTypeGroupId` or `workType` field.

```
   //Build SkillRequirement

     lxscheduler.SkillRequirement skillReq = new lxscheduler.SkillRequirementBuilder()

      .setSkillId('0C5RM0000004EZS0A2')

      .setSkillLevel(90)

      .build();

```


### Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

      .setDurationInMinutes(15)

      .setBlockTimeBeforeAppointmentInMinutes(5)

      .setBlockTimeAfterAppointmentInMinutes(5)

      .setTimeFrameStartInMinutes(10080)

      .setTimeFrameEndInMinutes(40320)

      .setOperatingHoursId('0OHRM0000000FmG4AU')

      .setSkillRequirements(new List<lxscheduler.SkillRequirement>{skillReq})

      .build();

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkType(workType)

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows a sample response of a list of available candidates:

```
   [

     {

       "startTime": "2021-02-16T16:15:00.000+0000",

       "endTime": "2021-02-16T16:16:00.000+0000",

       "resources": [

         "0Hnxx0000004C9BCAU"

       ],

       "territoryId": "0Hhxx0000004C92CAE"

     },

     {

       "startTime": "2021-02-16T16:30:00.000+0000",

       "endTime": "2021-02-16T16:31:00.000+0000",

       "resources": [

        "0Hnxx0000004C9BCAU"

       ],

       "territoryId": "0Hhxx0000004C92CAE"

     },

   ]

### GetAppointmentCandidatesInputBuilder Class

```

Contains methods to build an instance of the `lxscheduler.GetAppointmentCandidatesInput` class.

### A Builder object is obtained by invoking one of the GetAppointmentCandidatesInputBuilder methods defined by the GetAppointmentCandidatesInput class.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

IN THIS SECTION:

#### GetAppointmentCandidatesInputBuilder Methods GetAppointmentCandidatesInputBuilder Methods The following are methods for GetAppointmentCandidatesInputBuilder .

IN THIS SECTION:

##### build()

Returns an instance of the `lxscheduler.GetAppointmentCandidatesInput` object.

setAccountId(accountId)
Sets the ID of the associated account for which you want to create the appointments.

setAllowConcurrent(allowConcurrent)
Allows the scheduling of concurrent appointments.

setApiVersion(apiVersion)
Sets the API version of the business logic for the `getAppointmentCandidates` method.

setCorrelationId(correlationId)
Sets the correlation ID.

setEndTime(endTime)
Sets the scheduling end time.

setEngagementChannelTypeIds(engagementChannelTypeIds)
Sets an engagement channel type.

setFilterByResources(filterByResources)
Enables filtering resources using a comma-separated list of service resource IDs.

setResourceLimitApptDistribution(resourceLimitApptDistribution)
Sets the number of service resources to show during appointment scheduling.

setSchedulingPolicyId(schedulingPolicyId)
Sets the ID of the AppointmentSchedulingPolicy object.

setStartTime(startTime)
Sets the scheduling start time to the specified time.

setTerritoryIds(territoryIds)
Sets the service territory IDs.

setWorkType(workType)
Sets the type of work to be performed.

setWorkTypeGroupId(workTypeGroupId)
Sets the ID of the work type group.

##### **`build()`**

Returns an instance of the `lxscheduler.GetAppointmentCandidatesInput` object.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentCandidatesInput build()

```

Return Value

Type: lxscheduler.GetAppointmentCandidatesInput

##### **`setAccountId(accountId)`**

Sets the ID of the associated account for which you want to create the appointments.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setAccountId(String accountId)

```

Parameters

```
   accountId
```

Type: String

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setAllowConcurrent(allowConcurrent)`**

Allows the scheduling of concurrent appointments.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setAllowConcurrent(Boolean

   allowConcurrent)

```

Parameters

```
   allowConcurrent
```

Type: Boolean

If true, allows scheduling of concurrent appointments in a time slot. The default is false.

Available in API version 47.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setApiVersion(apiVersion)`**

Sets the API version of the business logic for the `getAppointmentCandidates` method.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setApiVersion(Double apiVersion)

```

Parameters

```
   apiVersion
```

Type: Double

Usage

The specified parameter must use the correct API version. For example, if API version is set to 45.0 and _`filterByResources`_ is set
(which is available in API version 51.0 and later), then this field is ignored. If no API version or incorrect API version is passed in the request
body, by default the latest version is used.

Note: The API is available since version 45.0.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setCorrelationId(correlationId)`**

Sets the correlation ID.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setCorrelationId(String

   correlationId)

```

Parameters

```
   correlationId
```

Type: String

ID to pass custom information to the `ServiceResourceScheduleHandler` Apex interface. For example, you can use the
correlation ID to identify the app, website, or any other external system that calls this Apex interface implementation. If you don’t
pass a custom value, a randomly generated identifier is passed. Available in API version 53.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setEndTime(endTime)`**

Sets the scheduling end time.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setEndTime(String endTime)

```


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Parameters

```
   endTime
```

Type: String

The latest time that a time slot can end (inclusive).

Note: If end time is not specified, it defaults to 31 days.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setEngagementChannelTypeIds(engagementChannelTypeIds)`**

Sets an engagement channel type.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder

   setEngagementChannelTypeIds(List<String> engagementChannelTypeIds)

```

Parameters

```
   engagementChannelTypeIds
```

Type: List<String>

The ID of the engagement channel type record. The availability of service resources is filtered based on the engagement channel
type selected. This field is available in API version 56.0 and later.

Note: This field supports only one engagement channel type ID.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

Usage

You can use engagement channel types only in these cases:

**•** The **Schedule Appointments Using Engagement Channels** setting is enabled in Salesforce Scheduler Settings in your Salesforce
org.

**•** [Shifts are defined in the scheduling policy. For more information on setting up shifts in scheduling policy, see Define Shift Rules in](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)
[Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating-hours rules in the scheduling policy.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

##### **`setFilterByResources(filterByResources)`**

Enables filtering resources using a comma-separated list of service resource IDs.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setFilterByResources(List<String>

   filterByResources)

```

Parameters

```
   filterByResources
```

Type: List<String>

Gets only eligible resources that are both in the list and in the selected service territory sorted by the order in which the resource
IDs are passed. This field is available in API version 51.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setResourceLimitApptDistribution(resourceLimitApptDistribution)`**

Sets the number of service resources to show during appointment scheduling.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder

   setResourceLimitApptDistribution(Integer resourceLimitApptDistribution)

```

Parameters

```
   resourceLimitApptDistribution
```

Type: Integer

Specify the maximum number of service resources that you want to show during appointment scheduling when appointment
distribution is enabled. Available in API version 53.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setSchedulingPolicyId(schedulingPolicyId)`**

Sets the ID of the AppointmentSchedulingPolicy object.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setSchedulingPolicyId(String

   schedulingPolicyId)

```


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Parameters

```
   schedulingPolicyId
```

Type: String

The ID of the `AppointmentSchedulingPolicy` object. If no scheduling policy is passed in the request body, the default
configurations are used.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setStartTime(startTime)`**

Sets the scheduling start time to the specified time.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setStartTime(String startTime)

```

Parameters

```
   startTime
```

Type: String

The earliest time that a time slot can begin (inclusive). You can also use a time from the past.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setTerritoryIds(territoryIds)`**

Sets the service territory IDs.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setTerritoryIds(List<String>

   territoryIds)

```

Parameters

```
   territoryIds
```

Type: List<String>

List of service territory IDs, where the work that is being requested is performed. This is a required field.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setWorkType(workType)`**

Sets the type of work to be performed.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setWorkType(lxscheduler.WorkType

   workType)

```

Parameters

```
   workType
```

Type: lxscheduler.WorkType

This method takes input as an instance of the `lxscheduler.WorkType` class. Build the instance of the input class using the
`lxscheduler.WorkTypeBuilder` class.

Required if _`workTypeGroupId`_ is not given. If id of the _`workType`_ is given, the rest of _`workType`_ fields are optional.

Usage

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setWorkTypeGroupId(workTypeGroupId)`**

Sets the ID of the work type group.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setWorkTypeGroupId(String

   workTypeGroupId)

```

Parameters

```
   workTypeGroupId
```

Type: String

The ID of the work type group containing the work types that are being performed. Required if _`workType`_ is not given. If _`workType`_
is given, then you must provide either _`id`_ or _`durationInMinutes`_, but not both.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder


### Apex Reference Guide GetAppointmentSlotsInput Class GetAppointmentSlotsInput Class

Contains information about the available appointment time slots for a resource based on given work type group and territories.

The appointment time slots are determined based on your Salesforce Scheduler data model configurations. Here are some prerequisites
that you can consider while setting up data.

**•** Set up Salesforce Scheduler before making your requests. The setup includes creating or configuring Service Resources, Service
[Territory Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Manage](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)
[Business Information in Salesforce Scheduler for more information.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)

**•** Configure a work type mapped for each territory in the request body via Service Territory Work Type. Map the same work type to
the work type group, via work type group member.

The following factors affect how time slots are calculated and returned.

**•** Timezones that differ across operating hours are handled and results are always returned in UTC.

**•** The resource must be marked as a required resource on the assigned resource object.

**•** The resource is considered unavailable If the status categories of the resource assigned to service appointments are other than
`Canceled`, `Cannot Complete`, and `Completed` .

**•** Resource Absences of all types are considered unavailable from start to end.

**•** The following fields of Work Type records, if configured, are used to fine-tune time slot requirements. For more information, see
[Create Work Types in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_create_work_types.htm&language=en_US)

**Parameter** **Description**

`Timeframe Start` Time slots sooner than `current time +` _**`Timeframe Start`**_ aren’t
returned.

`Timeframe End` Time slots later than `current time +` _**`Timeframe End`**_ aren’t returned.

`Block Time Before Appointment` The time period before the appointment is considered as unavailable.

`Block Time After Appointment` The time period after the appointment is considered as unavailable.

```
Operating Hours

```

The overlap of all operating hours from the account, work type, service territory, and
service territory member are considered while determining time slots. For more
[information, see Set Up Operating Hours in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up_oh.htm&type=5&language=en_US)

**•** Only the time slots within the period of 31 days from the start date are returned.

**•** Salesforce Scheduler uses multiple factors, such as field values, scheduled appointments, absences, Scheduler Settings, and Scheduling
[Policies to determine available time slots, including the earliest and latest appointment slots. See How Does Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
[Determine Available Time Slots.](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)

Note: If asset scheduling is enabled, you can provide an asset-based service resource in `requiredResourceIds` to
retrieve available timeslots for the asset resource.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentSlotsInput Class

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the GetAppointmentSlotsInputBuilder.build()
method.

This example shows how to get a list of available time slots based on `workTypeGroupId` :

```
   //Build input for GetAppointmentSlots API

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkTypeGroupId('0VSxx0000004C92GAE')

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setEndTime(System.now().addDays(1).format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setAccountId('001xx000003GYK0AAO')

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

       .setSchedulingPolicyId('0Vrxx0000004CAe')

       .setApiVersion(Double.valueOf('48.0'))

       .build();

   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows how to get a list of available time slots based on `workType` :

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

       .setId('08qxx0000004C92AAE')

       .build();

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkType(workType)

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setEndTime(System.now().addDays(1).format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setAccountId('001xx000003GYK0AAO')

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

       .setSchedulingPolicyId('0Vrxx0000004CAe')

       .setApiVersion(Double.valueOf('48.0'))

       .build();

   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows how to get a list of available time slots based on `durationInMinutes` and without `workTypeGroupId`
or `workType` fields:

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

       .setDurationInMinutes(60)

       .build();

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkType(workType)

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

```


### Apex Reference Guide GetAppointmentSlotsInputBuilder Class

```
       .setApiVersion(Double.valueOf('48.0'))

       .build();

     String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows a sample response of a list of available time slots:

```
   [

     {

      "territoryId": "0Hhxx0000004C92CAE",

      "startTime": "2021-02-10T16:00:00.000+0000",

      "endTime": "2021-02-10T16:15:00.000+0000",

      "remainingAppointments": 1

     },

     {

      "territoryId": "0Hhxx0000004C92CAE",

      "startTime": "2021-02-10T16:15:00.000+0000",

      "endTime": "2021-02-10T16:30:00.000+0000",

      "remainingAppointments": 1

     },

   ]

### GetAppointmentSlotsInputBuilder Class

```

Contains methods to build an instance of the `lxscheduler.GetAppointmentSlotsInput` class.

### A Builder object is obtained by invoking one of the GetAppointmentSlotsInputBuilder methods defined by the GetAppointmentSlotsInput class.

Namespace

LxScheduler

IN THIS SECTION:

#### GetAppointmentSlotsInputBuilder Methods GetAppointmentSlotsInputBuilder Methods

### The following are methods for GetAppointmentSlotsInputBuilder .

IN THIS SECTION:

build()
Returns an instance of the `lxscheduler.GetAppointmentSlotsInput` object.

setAccountId(accountId)
Sets the ID of the associated account for which you want to create appointments.

setAllowConcurrentScheduling(allowConcurrentScheduling)
Allows the scheduling of concurrent appointments.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

setApiVersion(apiVersion)
Sets the API version of the business logic for the `getAppointmentSlots` method.

setCorrelationId(correlationId)
Sets the correlation ID.

setEndTime(endTime)
Sets the scheduling end time.

setEngagementChannelTypeIds(engagementChannelTypeIds)
Sets an engagement channel type.

setPrimaryResourceId(primaryResourceId)
Sets the ID of the primary resource.

setRequiredResourceIds(requiredResourceIds)
Sets the resource IDs.

setSchedulingPolicyId(schedulingPolicyId)
Sets the ID of the `AppointmentSchedulingPolicy` object.

setStartTime(startTime)
Sets the scheduling start time.

setTerritoryIds(territoryIds)
Sets the IDs of service territories.

setWorkType(workType)
Sets the type of work to be performed.

setWorkTypeGroupId(workTypeGroupId)
Sets the ID of the work type group.

##### **`build()`**

Returns an instance of the `lxscheduler.GetAppointmentSlotsInput` object.

Signature

```
   public lxscheduler.GetAppointmentSlotsInput build()

```

Return Value

Type: lxscheduler.GetAppointmentSlotsInput

##### **`setAccountId(accountId)`**

Sets the ID of the associated account for which you want to create appointments.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setAccountId(String accountId)

```


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Parameters

```
   accountId
```

Type: String

The ID of the associated account.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setAllowConcurrentScheduling(allowConcurrentScheduling)`**

Allows the scheduling of concurrent appointments.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setAllowConcurrentScheduling(Boolean

   allowConcurrentScheduling)

```

Parameters

```
   allowConcurrentScheduling
```

Type: Boolean

If true, allows scheduling of concurrent appointments in a time slot. If false, concurrent appointments are not allowed. The default
is false. Available in API version 47.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setApiVersion(apiVersion)`**

Sets the API version of the business logic for the `getAppointmentSlots` method.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setApiVersion(Double apiVersion)

```

Parameters

```
   apiVersion
```

Type: Double

Usage

The specified parameter must use the correct API version. For example, if API version is set to 45.0 and _`primaryResourceId`_ is set
(which is available in API version 48.0 and later), then this field is ignored. If no API version or incorrect API version is passed in the request
body, by default the latest version is used.

Note: The API is available since version 45.0.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setCorrelationId(correlationId)`**

Sets the correlation ID.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setCorrelationId(String correlationId)

```

Parameters

```
   correlationId
```

Type: String

ID to pass custom information to the `ServiceResourceScheduleHandler` Apex interface. For example, you can use the
correlation ID to identify the app, website, or any other external system that calls this Apex interface implementation. If you don’t
pass a custom value, a randomly generated identifier is passed. Available in API version 53.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setEndTime(endTime)`**

Sets the scheduling end time.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setEndTime(String endTime)

```

Parameters

```
   endTime
```

Type: String

The latest time that a time slot can end (inclusive). If end time is not specified, it defaults to 31 days.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setEngagementChannelTypeIds(engagementChannelTypeIds)`**

Sets an engagement channel type.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder

   setEngagementChannelTypeIds(List<String> engagementChannelTypeIds)

```

Parameters

```
   engagementChannelTypeIds
```

Type: List<String>

The ID of the engagement channel type record. The availability of time slots is filtered based on the engagement channel type
selected. This field is available in API version 56.0 and later.

Note: This field supports only one engagement channel type ID.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

Usage

You can use engagement channel types only in these cases:

**•** The **Schedule Appointments Using Engagement Channels** setting is enabled in Salesforce Scheduler Settings in your Salesforce
org.

**•** [Shifts are defined in the scheduling policy. For more information on setting up shifts in scheduling policy, see Define Shift Rules in](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)
[Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating-hours rules in the scheduling policy.

##### **`setPrimaryResourceId(primaryResourceId)`**

Sets the ID of the primary resource.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setPrimaryResourceId(String

   primaryResourceId)

```

Parameters

```
   primaryResourceId
```

Type: String

The ID of the primary resource in multi-resource scheduling. Required only when multi-resource scheduling is enabled. Available in
API version 48.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

##### **`setRequiredResourceIds(requiredResourceIds)`**

Sets the resource IDs.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setRequiredResourceIds(List<String>

   requiredResourceIds)

```

Parameters

```
   requiredResourceIds
```

Type: List<String>

List of resource IDs that must be available during the time slot. This is a required field.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setSchedulingPolicyId(schedulingPolicyId)`**

Sets the ID of the `AppointmentSchedulingPolicy` object.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setSchedulingPolicyId(String

   schedulingPolicyId)

```

Parameters

```
   schedulingPolicyId
```

Type: String

If no scheduling policy is passed in the request body, the default configurations are used.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setStartTime(startTime)`**

Sets the scheduling start time.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setStartTime(String startTime)

```

Parameters

```
   startTime
```

Type: String


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

The earliest time that a time slot can begin (inclusive). Defaults to the current time of the request, if empty.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setTerritoryIds(territoryIds)`**

Sets the IDs of service territories.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setTerritoryIds(List<String>

   territoryIds)

```

Parameters

```
   territoryIds
```

Type: List<String>

List of IDs of service territories, where the work that is being requested is performed. This is a required field.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setWorkType(workType)`**

Sets the type of work to be performed.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setWorkType(lxscheduler.WorkType

   workType)

```

Parameters

```
   workType
```

Type: lxscheduler.WorkType

This method takes input as an instance of the `lxscheduler.WorkType` class. Build the instance of the input class using the
`lxscheduler.WorkTypeBuilder` class.

Required if _`workTypeGroupId`_ is not given.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder


### Apex Reference Guide SchedulerResources Class

##### **`setWorkTypeGroupId(workTypeGroupId)`**

Sets the ID of the work type group.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setWorkTypeGroupId(String

   workTypeGroupId)

```

Parameters

```
   workTypeGroupId
```

Type: String

The ID of the work type group containing the work types that are being performed.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

### SchedulerResources Class

Contains methods that holds the business logic to get resources availability.

Namespace

LxScheduler

Implementation Considerations

### Apex implementation of the methods in the SchedulerResources class should adhere to Apex Governor Limits. It includes

synchronous heap size limit, synchronous CPU time limit, and synchronous concurrent transactions for long running transactions. To
avoid governor limits, you must tune the input by reducing the time frame, limiting number of service resources, or limiting number or
territories at a time. This will reduce the overall transaction time and response size of the implementation. For more information on
[standard Apex Governer Limits, see Salesforce Developer Limits and Allocations Quick Reference.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm)

Example

To get list of available service resources (appointment candidates):

```
   String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

To get a list of available appointment time slots for a resource:

```
   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

IN THIS SECTION:

SchedulerResources Methods


Apex Reference Guide SchedulerResources Class

#### SchedulerResources Methods The following are methods for SchedulerResources .

IN THIS SECTION:

##### getAppointmentCandidates(getAppointmentCandidatesInput)

Returns a list of service resources based on work type group or work type and service territories.

getAppointmentSlots(getAppointmentSlotsInput)
Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

setAppointmentCandidatesMock(expectedResponse)
##### Sets a mock object when running tests for the getAppointmentCandidates method.

setAppointmentSlotsMock(expectedResponse)
Sets a mock object when running tests for the `getAppointmentSlots` method.

##### **`getAppointmentCandidates(getAppointmentCandidatesInput)`**

Returns a list of service resources based on work type group or work type and service territories.

Set up Salesforce Scheduler before making requests. This setup includes creating or configuring Service Resources, Service Territory
[Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Set Up Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&type=5&language=en_US)
for more information.

The appointment time slots are determined based on multiple factors, such as field values, scheduled appointments, absences, Scheduler
[Settings, and Scheduling Policies to determine available time slots. See How Salesforce Scheduler Determines Available Time Slots for](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
more information.

The following factors are considered for returning start time and end time of resources.

**Resource Availability**
Determined using service territory member, service territory, work type, and account operating hours fields.

**Resource Unavailability**
Determined by resource absences, existing appointments that the resource is assigned to. The resource must be marked as a required
resource for the appointment with a status that isn’t in closed, canceled, or completed.

**Appointment Start Time Interval in the Scheduling Policy**
Appointment start time interval field in the Scheduling Policy is used to determine when the appointment can start. This interval
can be 5, 10, 15, 20, 30, or 60. By default, it’s set to 15.

**Work Type Duration**
The end time is calculated as start time + duration of the work type.

Note: If asset scheduling is enabled, the response also includes asset-based candidates.

Signature

```
   public static String getAppointmentCandidates(lxscheduler.GetAppointmentCandidatesInput

   getAppointmentCandidatesInput)

```


Apex Reference Guide SchedulerResources Class

Parameters

```
   getAppointmentCandidatesInput
```

Type: lxscheduler.GetAppointmentCandidatesInput

This method takes input as an instance of the `lxscheduler.GetAppointmentCandidatesInput` class. Build the
instance of the input class using the `lxscheduler.GetAppointmentCandidatesInputBuilder` class.

Return Value

Type: String

##### **`getAppointmentSlots(getAppointmentSlotsInput)`**

Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

The appointment time slots are determined based on your Salesforce Scheduler data model configurations. Here are some prerequisites
that you can consider while setting up data.

**•** Set up Salesforce Scheduler before making your requests. The setup includes creating or configuring Service Resources, Service
[Territory Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Manage](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)
[Business Information in Salesforce Scheduler for more information.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)

**•** Configure a work type mapped for each territory in the request body via Service Territory Work Type. Map the same work type to
the work type group, via work type group member.

The following factors affect how time slots are calculated and returned.

**•** Timezones that differ across operating hours are handled and results are always returned in UTC.

**•** The resource must be marked as a required resource on the assigned resource object.

**•** The resource is considered unavailable If the status categories of the resource assigned to service appointments are other than
`Canceled`, `Cannot Complete`, and `Completed` .

**•** Resource Absences of all types are considered unavailable from start to end.

**•** The following fields of Work Type records, if configured, are used to fine-tune time slot requirements. For more information, see
[Create Work Types in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_create_work_types.htm&language=en_US)

**Parameter** **Description**

`Timeframe Start` Time slots sooner than `current time +` _**`Timeframe Start`**_ aren’t
returned.

`Timeframe End` Time slots later than `current time +` _**`Timeframe End`**_ aren’t returned.

`Block Time Before Appointment` The time period before the appointment is considered as unavailable.

`Block Time After Appointment` The time period after the appointment is considered as unavailable.

```
Operating Hours

```

The overlap of all operating hours from the account, work type, service territory, and
service territory member are considered while determining time slots. For more
[information, see Set Up Operating Hours in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up_oh.htm&type=5&language=en_US)

**•** Only the time slots within the period of 31 days from the start date are returned.


Apex Reference Guide SchedulerResources Class

**•** Salesforce Scheduler uses multiple factors, such as field values, scheduled appointments, absences, Scheduler Settings, and Scheduling
[Policies to determine available time slots, including the earliest and latest appointment slots. See How Does Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
[Determine Available Time Slots.](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)

Note: If asset scheduling is enabled, you can provide an asset-based service resource in `requiredResourceIds` to
retrieve available timeslots for the asset resource.

Signature

```
   public static String getAppointmentSlots(lxscheduler.GetAppointmentSlotsInput

   getAppointmentSlotsInput)

```

Parameters

```
   getAppointmentSlotsInput
```

Type: lxscheduler.GetAppointmentSlotsInput

This method takes input as an instance of the `lxscheduler.GetAppointmentSlotsInput` class. Build the instance of
the input class using the `lxscheduler.GetAppointmentSlotsInputBuilder` class.

Return Value

Type: String

##### **`setAppointmentCandidatesMock(expectedResponse)`**

Sets a mock object when running tests for the `getAppointmentCandidates` method.

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   public static void setAppointmentCandidatesMock(String expectedResponse)

```

Parameters

```
   expectedResponse
```

Type: String

Return Value

Type: void

This example shows a sample implementation of the `GetAppointmentCandidates` class:

```
   public class AppointmentCandidateService {

     //Instance members for parsing

     public String startTime;

     public String endTime;

     public List<String> resources;

     public String territoryId;

     public static List<AppointmentCandidateService> getAppointmentCandidates(){

```


Apex Reference Guide SchedulerResources Class

```
       //Build input for GetAppointmentCandidates API

       lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

         .setWorkTypeGroupId('0VSRM0000000AGT4A2')

         .setTerritoryIds(new List<String>{'0HhRM0000000G8W0AU'})

        .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/Los_Angeles'))

   .setEndTime(System.now().addDays(2).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/Los_Angeles'))

         .setSchedulingPolicyId('0VrRM00000000D0')

         .setApiVersion(Double.valueOf('50.0'))

         .build();

       List<AppointmentCandidateService> vList =

   parse(lxscheduler.SchedulerResources.getAppointmentCandidates(input));

       return vList;

     }

     private static List<AppointmentCandidateService> parse(String json) {

       return (List<AppointmentCandidateService>) System.JSON.deserialize(json,

   List<AppointmentCandidateService>.class);

     }

   }

```

This example shows how to set a sample mock using the `setAppointmentCandidatesMock` method:

```
   @isTest

   private class GetAppointmentCandidatesTest {

     static testMethod void getAppCandidatesTest() {

       String expectedResponse = '[' +

                         ' {' +

                        ' \"startTime\": \"2021-03-18T16:00:00.000+0000\",'

    +

                         ' \"endTime\": \"2021-03-18T17:00:00.000+0000\",'

   +

                         ' \"resources\": [' +

                         ' \"0HnRM0000000Fxv0AE\"' +

                         ' ],' +

                         ' \"territoryId\": \"0HhRM0000000G8W0AU\"' +

                         ' },' +

                         ' {' +

                        ' \"startTime\": \"2021-03-18T19:00:00.000+0000\",'

    +

                         ' \"endTime\": \"2021-03-18T20:00:00.000+0000\",'

   +

                         ' \"resources\": [' +

                         ' \"0HnRM0000000Fxv0AE\"' +

                         ' ],' +

                         ' \"territoryId\": \"0HhRM0000000G8W0AU\"' +

                         ' }' +

                         ']';

       lxscheduler.SchedulerResources.setAppointmentCandidatesMock(expectedResponse);

       Test.startTest();

         List<AppointmentCandidateService> candidateList =

```


### Apex Reference Guide SkillRequirement Class

```
   AppointmentCandidateService.getAppointmentCandidates();

         System.assertEquals(2, candidateList.size(), 'Should return only 2 records!');

       Test.stopTest();

     }

   }

##### **`setAppointmentSlotsMock(expectedResponse)`**

```

Sets a mock object when running tests for the `getAppointmentSlots` method.

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   public static void setAppointmentSlotsMock(String expectedResponse)

```

Parameters

```
   expectedResponse
```

Type: String

Return Value

Type: void

### SkillRequirement Class

Contains information about the set of skills that are required to complete a particular task for a work type.

Namespace

LxScheduler

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the SkillRequirementBuilder.build() method.

### SkillRequirementBuilder Class

Contains methods to build an instance of the `lxscheduler.SkillRequirement` class.

### A Builder object is obtained by invoking one of the SkillRequirementBuilder methods defined by the SkillRequirement

class.

Namespace

LxScheduler


Apex Reference Guide SkillRequirementBuilder Class

IN THIS SECTION:

#### SkillRequirementBuilder Methods SkillRequirementBuilder Methods The following are methods for SkillRequirementBuilder .

IN THIS SECTION:

##### build()

Returns an instance of the `lxscheduler.SkillRequirement` object.

##### setSkillId(skillId)

Sets the skill that is required to complete a particular task for a work type. This is a required field.

##### setSkillLevel(skillLevel)

Sets the level of the skill that is required to complete a particular task for a work type

##### **`build()`**

Returns an instance of the `lxscheduler.SkillRequirement` object.

Signature

```
   public lxscheduler.SkillRequirement build()

```

Return Value

Type: lxscheduler.SkillRequirement

##### **`setSkillId(skillId)`**

Sets the skill that is required to complete a particular task for a work type. This is a required field.

Signature

```
   public lxscheduler.SkillRequirementBuilder setSkillId(String skillId)

```

Parameters

```
   skillId
```

Type: String

Return Value

Type: lxscheduler.SkillRequirementBuilder

##### **`setSkillLevel(skillLevel)`**

Sets the level of the skill that is required to complete a particular task for a work type


### Apex Reference Guide WorkType Class

Signature

```
   public lxscheduler.SkillRequirementBuilder setSkillLevel(Double skillLevel)

```

Parameters

```
   skillLevel
```

Type: Double

The skill levels can range from zero to 99.99. Depending on your business needs, you might want the skill level to reflect years of
experience, certification levels, or license classes.

Return Value

Type: lxscheduler.SkillRequirementBuilder

### WorkType Class

Contains information about the type of work to be performed.

Namespace

LxScheduler

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the WorkTypeBuilder.build() method.

### WorkTypeBuilder Class

Contains methods to build an instance of the `lxscheduler.WorkType` class.

### A Builder object is obtained by invoking one of the WorkTypeBuilder methods defined by the WorkType class.

Namespace

LxScheduler

IN THIS SECTION:

#### WorkTypeBuilder Methods WorkTypeBuilder Methods

### The following are methods for WorkTypeBuilder .

IN THIS SECTION:

build()
Returns an instance of the `lxscheduler.WorkType` object.


Apex Reference Guide WorkTypeBuilder Class

##### setBlockTimeAfterAppointmentInMinutes(blockTimeAfterAppointmentInMinutes)

Sets the time period, in minutes.

setBlockTimeBeforeAppointmentInMinutes(blockTimeBeforeAppointmentInMinutes)
Sets the time period, in minutes.

setDurationInMinutes(durationInMinutes)
Sets the event length.

setId(id)
Sets the ID of the work type to the specified ID.

setOperatingHoursId(operatingHoursId)
Sets the overlap of operating hours.

setSkillRequirements(skillRequirements)
Sets the skills that are required to complete a particular task for a work type.

setTimeFrameEndInMinutes(timeFrameEndInMinutes)
Sets the end of the timeframe.

setTimeFrameStartInMinutes(timeFrameStartInMinutes)
Sets the beginning of the timeframe.

##### **`build()`**

Returns an instance of the `lxscheduler.WorkType` object.

Signature

```
   public lxscheduler.WorkType build()

```

Return Value

Type: lxscheduler.WorkType

##### **`setBlockTimeAfterAppointmentInMinutes(blockTimeAfterAppointmentInMinutes)`**

Sets the time period, in minutes.

Signature

```
   public lxscheduler.WorkTypeBuilder setBlockTimeAfterAppointmentInMinutes(Integer

   blockTimeAfterAppointmentInMinutes)

```

Parameters

```
   blockTimeAfterAppointmentInMinutes
```

Type: Integer

The time period after the appointment is considered unavailable.


Apex Reference Guide WorkTypeBuilder Class

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setBlockTimeBeforeAppointmentInMinutes(blockTimeBeforeAppointmentInMinutes)`**

Sets the time period, in minutes.

Signature

```
   public lxscheduler.WorkTypeBuilder setBlockTimeBeforeAppointmentInMinutes(Integer

   blockTimeBeforeAppointmentInMinutes)

```

Parameters

```
   blockTimeBeforeAppointmentInMinutes
```

Type: Integer

The time period before the appointment is considered as unavailable.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setDurationInMinutes(durationInMinutes)`**

Sets the event length.

Signature

```
   public lxscheduler.WorkTypeBuilder setDurationInMinutes(Integer durationInMinutes)

```

Parameters

```
   durationInMinutes
```

Type: Integer

Contains the event length, in minutes. Required if _`id`_ is not given.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setId(id)`**

Sets the ID of the work type to the specified ID.

Signature

```
   public lxscheduler.WorkTypeBuilder setId(String id)

```


Apex Reference Guide WorkTypeBuilder Class

Parameters

```
   id
```

Type: String

The ID of the work type. Required if you're using shifts or if _`durationInMinutes`_ is not given.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setOperatingHoursId(operatingHoursId)`**

Sets the overlap of operating hours.

Signature

```
   public lxscheduler.WorkTypeBuilder setOperatingHoursId(String operatingHoursId)

```

Parameters

```
   operatingHoursId
```

Type: String

The overlap of all operating hours from the account, work type, service territory, and service territory member are considered while
determining time slots.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setSkillRequirements(skillRequirements)`**

Sets the skills that are required to complete a particular task for a work type.

Signature

```
   public lxscheduler.WorkTypeBuilder

   setSkillRequirements(List<lxscheduler.SkillRequirement> skillRequirements)

```

Parameters

```
   skillRequirements
```

Type: List<lxscheduler.SkillRequirement>

This method takes input as an instance of the `lxscheduler.SkillRequirement` class. Build the instance of the input class
using the `lxscheduler.SkillRequirementBuilder` class.

Return Value

Type: lxscheduler.WorkTypeBuilder


### Apex Reference Guide ServiceResourceScheduleHandler Interface

##### **`setTimeFrameEndInMinutes(timeFrameEndInMinutes)`**

Sets the end of the timeframe.

Signature

```
   public lxscheduler.WorkTypeBuilder setTimeFrameEndInMinutes(Integer

   timeFrameEndInMinutes)

```

Parameters

```
   timeFrameEndInMinutes
```

Type: Integer

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setTimeFrameStartInMinutes(timeFrameStartInMinutes)`**

Sets the beginning of the timeframe.

Signature

```
   public lxscheduler.WorkTypeBuilder setTimeFrameStartInMinutes(Integer

   timeFrameStartInMinutes)

```

Parameters

```
   timeFrameStartInMinutes
```

Type: Integer

Return Value

Type: lxscheduler.WorkTypeBuilder

### ServiceResourceScheduleHandler Interface

Allows an implementing class to check external calendar events to find already booked time slots for the requested service resources.
This interface is part of Salesforce Scheduler.

Namespace

LxScheduler

Usage

The `lxscheduler.ServiceResourceScheduleHandler` interface is called by Salesforce Scheduler APIs.


Apex Reference Guide ServiceResourceScheduleHandler Interface

To implement this interface, you must first declare a class with the `implements` keyword as follows:

```
   public class ServiceResourceScheduleHandlerImpl implements

   LxScheduler.ServiceResourceScheduleHandler{}

```

Next, your class must provide an implementation for the following method:

```
   public static List<LxScheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(LxScheduler.ServiceAppointmentRequestInfo requestInfo){

       //Your code here

   }

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

#### ServiceResourceScheduleHandler Methods

ServiceResourceScheduleHandler Example Implementation

#### ServiceResourceScheduleHandler Methods The following are methods for ServiceResourceScheduleHandler .

IN THIS SECTION:

##### getUnavailableTimeslots(var1)

Passes the required information to get unavailable time slots from an external system. The implementation of this method returns
the `lxscheduler.ServiceResourceSchedule` class.

##### getUnavailableTimeslots(var1)

Passes the required information to get unavailable time slots from an external system. The implementation of this method returns the
`lxscheduler.ServiceResourceSchedule` class.

Signature

```
   public List<lxscheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(lxscheduler.ServiceAppointmentRequestInfo var1)

```

Parameters

```
   var1
```

Type: lxscheduler.ServiceAppointmentRequestInfo

Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface.

Return Value

Type: List<lxscheduler.ServiceResourceSchedule>


Apex Reference Guide ServiceResourceScheduleHandler Interface

#### ServiceResourceScheduleHandler Example Implementation

This is an example implementation of the `lxscheduler.ServiceResourceScheduleHandler` interface.

```
   /**

    * Implement interface lxscheduler.ServiceResourceScheduleHandler

    * This class is called when fetching service resources and time slots through Salesforce

    Scheduler API.*/

     Public class ServiceResourceScheduleHandlerImpl implements

   lxscheduler.ServiceResourceScheduleHandler{

      // The main interface method.

      public static List<lxscheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(lxscheduler.ServiceAppointmentRequestInfo requestInfo){

        //Request info values.

        List<lxscheduler.ServiceResourceInfo>

   serviceResources=requestInfo.getServiceResources();

        DateTime startDate=requestInfo.getStartDate();

        DateTime endDate=requestInfo.getEndDate();

        List<lxscheduler.ServiceResourceSchedule> resourceUnavailability = new

   List<lxscheduler.ServiceResourceSchedule>();

        Set<lxscheduler.UnavailableTimeslot> unavailabilityIntervals = new

   Set<lxscheduler.UnavailableTimeslot>();

        //This is a dummy response. Implement your own business logic to connect to your

   internal or external systems.

        for (Integer i = 0; i < 5; i++) {

           //Set the unavailability intervals of a service resource.

           unavailabilityIntervals.add(new

   lxscheduler.UnavailableTimeslot(startDate.addMinutes(15*i),startDate.addMinutes(15*(i+1))));

        }

        for (lxscheduler.ServiceResourceInfo ServiceResource:serviceResources) {

           //Set the unavailability of Service resource.

        resourceUnavailability.add(new

   lxscheduler.ServiceResourceSchedule(serviceResource.getServiceResourceId(),unavailabilityIntervals));

        }

        return resourceUnavailability;

      }

   }

```

This example shows how to set a sample test mock using the `lxscheduler.ServiceResourceScheduleHandler` interface.

```
   @isTest

   private class ServiceResourceScheduleHandlerImplTest {

     static testMethod void getUnavailableTimeslotsTest() {

       //Initializing the test execution with mock values. Change it according to the

```


### Apex Reference Guide ServiceAppointmentRequestInfo Class

```
   implementation.

       //In case of non-test execution, the lxscheduler.ServiceAppointmentRequestInfo

   instance will automatically initialize.

       //Mock values for lxscheduler.ServiceResourceInfo

       String userId = '005D2000000I1N6IAK';

       String userName = 'someuser@example.com';

       String email = 'someuser@example.com';

       String serviceResourceId = '0HnD20000004C9bKAE';

       List<String> territoryIds = new List<String>();

       String resourceType = 'T';

       lxscheduler.ServiceResourceInfo serviceResInfo = new

   lxscheduler.ServiceResourceInfo(userId, userName, email,

                                    serviceResourceId, territoryIds,

   resourceType);

       //Mock values for lxscheduler.ServiceAppointmentRequestInfo

       DateTime startDate = System.now();

       DateTime endDate = System.now();

       List<lxscheduler.ServiceResourceInfo> serviceResources = new

   List<lxscheduler.ServiceResourceInfo>();

       serviceResources.add(serviceResInfo);

       String schedulingPolicyId = '0VrD20000004C9S';

       String workTypeGroupId = '0VSD20000004C93OAE';

       String accountId = '001D2000002pkXwIAI';

       String primaryResourceId = '0HnD20000004C9bKAE';

       String workTypeId = '08qD20000004C9XIAU';

       String correlationId = 'SOME_ID';

       lxscheduler.ServiceAppointmentRequestInfo mockRequestInfo = new

   lxscheduler.ServiceAppointmentRequestInfo(startDate, endDate, serviceResources,

                                           schedulingPolicyId,

   workTypeGroupId, accountId,

                                           primaryResourceId,

   workTypeId, correlationId);

       ServiceResourceScheduleHandlerImpl.getUnavailableTimeslots(mockRequestInfo);

     }

   }

### ServiceAppointmentRequestInfo Class

```

Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface. This class is implemented internally
by Apex.

Namespace

LxScheduler

IN THIS SECTION:

ServiceAppointmentRequestInfo Constructors


Apex Reference Guide ServiceAppointmentRequestInfo Class

ServiceAppointmentRequestInfo Methods

#### ServiceAppointmentRequestInfo Constructors The following are constructors for ServiceAppointmentRequestInfo .

IN THIS SECTION:

##### ServiceAppointmentRequestInfo(startDate, endDate, ServiceResources, SchedulingPolicyId, workTypeGroupId, accountId,

primaryResourceId, workTypeId, correlationId)
Creates a new instance of the `lxscheduler.ServiceAppointmentRequestInfo` class using the specified start date,
end date, service resources, scheduling policy, work type group, accound ID, primary resource, work type, and correlation.

##### **`ServiceAppointmentRequestInfo(startDate, endDate, ServiceResources,`**

```
  SchedulingPolicyId, workTypeGroupId, accountId, primaryResourceId, workTypeId,

  correlationId)

```

Creates a new instance of the `lxscheduler.ServiceAppointmentRequestInfo` class using the specified start date, end
date, service resources, scheduling policy, work type group, accound ID, primary resource, work type, and correlation.

Signature

```
   public ServiceAppointmentRequestInfo(Datetime startDate, Datetime endDate,

   List<lxscheduler.ServiceResourceInfo> ServiceResources, String SchedulingPolicyId,

   String workTypeGroupId, String accountId, String primaryResourceId, String workTypeId,

   String correlationId)

```

Parameters

```
   startDate
```

Type: Datetime

The start date and time for which unavailable time slots are requested.

```
   endDate
```

Type: Datetime

The end date and time for which unavailable time slots are requested.

```
   ServiceResources
```

Type: List<lxscheduler.ServiceResourceInfo>

The list of requested service resources for the unavailable time slots.

```
   SchedulingPolicyId
```

Type: String

The ID of the scheduling policy .

```
   workTypeGroupId
```

Type: String

The work type group ID.

```
   accountId
```

Type: String


Apex Reference Guide ServiceAppointmentRequestInfo Class

The account ID of an existing user.

```
   primaryResourceId
```

Type: String

The ID of the primary service resource.

```
   workTypeId
```

Type: String

The work type ID.

```
   correlationId
```

Type: String

A unique identifier for a service appointment request.

#### ServiceAppointmentRequestInfo Methods The following are methods for ServiceAppointmentRequestInfo .

IN THIS SECTION:

##### getAccountId()

Returns the account ID of the customer if the API request contains one.

getCorrelationId()
Returns a unique identifier for a request.

getEndDate()
Returns the end date and time for which unavailable time slots are requested.

getPrimaryResourceId()
Returns the ID of the primary service resource.

getSchedulingPolicyId()
Returns the ID of the scheduling policy that the API request contains.

getServiceResources()
Returns the list of requested service resources for the unavailable time slots.

getStartDate()
Returns the start date and time for which unavailable time slots are requested.

getWorkTypeGroupId()
Returns the work type group ID if the API request contains one.

getWorkTypeId()
Returns the work type ID if the API request contains one.

##### getAccountId()

Returns the account ID of the customer if the API request contains one.

Signature

```
   public String getAccountId()

```


Apex Reference Guide ServiceAppointmentRequestInfo Class

Return Value

Type: String

##### getCorrelationId()

Returns a unique identifier for a request.

Signature

```
   public String getCorrelationId()

```

Return Value

Type: String

##### getEndDate()

Returns the end date and time for which unavailable time slots are requested.

Signature

```
   public Datetime getEndDate()

```

Return Value

Type: Datetime

##### getPrimaryResourceId()

Returns the ID of the primary service resource.

Signature

```
   public String getPrimaryResourceId()

```

Return Value

Type: String

##### getSchedulingPolicyId()

Returns the ID of the scheduling policy that the API request contains.

Signature

```
   public String getSchedulingPolicyId()

```

Return Value

Type: String


### Apex Reference Guide ServiceResourceInfo Class

##### getServiceResources()

Returns the list of requested service resources for the unavailable time slots.

Signature

```
   public List<lxscheduler.ServiceResourceInfo> getServiceResources()

```

Return Value

Type: List<lxscheduler.ServiceResourceInfo>

##### getStartDate()

Returns the start date and time for which unavailable time slots are requested.

Signature

```
   public Datetime getStartDate()

```

Return Value

Type: Datetime

##### getWorkTypeGroupId()

Returns the work type group ID if the API request contains one.

Signature

```
   public String getWorkTypeGroupId()

```

Return Value

Type: String

##### getWorkTypeId()

Returns the work type ID if the API request contains one.

Signature

```
   public String getWorkTypeId()

```

Return Value

Type: String

### ServiceResourceInfo Class

Contains information about a service resource.


Apex Reference Guide ServiceResourceInfo Class

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceInfo Constructors

ServiceResourceInfo Methods

#### ServiceResourceInfo Constructors The following are constructors for ServiceResourceInfo .

IN THIS SECTION:

##### ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds, resourceType)

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.

##### **`ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds,`**

```
  resourceType)

```

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.

Signature

```
   public ServiceResourceInfo(String userId, String userName, String email, String

   serviceResourceId, List<String> territoryIds, String resourceType)

```

Parameters

```
   userId
```

Type: String

The user ID of the service resource.

```
   userName
```

Type: String

The user name of the service resource.

```
   email
```

Type: String

The email ID of the service resource.

```
   serviceResourceId
```

Type: String

The ID of the service resource.

```
   territoryIds
```

Type: List<String>

A list of requested service territories for the service resource.


Apex Reference Guide ServiceResourceInfo Class

```
   resourceType
```

Type: String

The type of the service resource such as Technician or Asset.

#### ServiceResourceInfo Methods The following are methods for ServiceResourceInfo .

IN THIS SECTION:

##### getEmail()

Returns the email ID of the service resource.

##### getResourceType()

Returns the type of the service resource such as Technician or Asset.

getServiceResourceId()
Returns the ID of the service resource.

getTerritoryIds()
Returns a list of requested service territories for the service resource.

getUserId()
Returns the user ID of the service resource.

getUserName()
Returns the user name of the service resource.

##### getEmail()

Returns the email ID of the service resource.

Signature

```
   public String getEmail()

```

Return Value

Type: String

##### getResourceType()

Returns the type of the service resource such as Technician or Asset.

Signature

```
   public String getResourceType()

```

Return Value

Type: String


### Apex Reference Guide ServiceResourceSchedule Class

##### getServiceResourceId()

Returns the ID of the service resource.

Signature

```
   public String getServiceResourceId()

```

Return Value

Type: String

##### getTerritoryIds()

Returns a list of requested service territories for the service resource.

Signature

```
   public List<String> getTerritoryIds()

```

Return Value

Type: List<String>

##### getUserId()

Returns the user ID of the service resource.

Signature

```
   public String getUserId()

```

Return Value

Type: String

##### getUserName()

Returns the user name of the service resource.

Signature

```
   public String getUserName()

```

Return Value

Type: String

### ServiceResourceSchedule Class

Use this class to pass results from your implemented Apex class to the ServiceResourceScheduleHandler interface methods.


Apex Reference Guide ServiceResourceSchedule Class

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceSchedule Constructors ServiceResourceSchedule Properties ServiceResourceSchedule Constructors The following are constructors for ServiceResourceSchedule .

IN THIS SECTION:

##### ServiceResourceSchedule(serviceResourceId, unavailableTimeslots)

Creates a new instance of lxscheduler.ServiceResourceSchedule class.

##### ServiceResourceSchedule(serviceResourceId, unavailableTimeslots)

Creates a new instance of lxscheduler.ServiceResourceSchedule class.

Signature

```
   public ServiceResourceSchedule(String serviceResourceId,

   Set<lxscheduler.UnavailableTimeslot> unavailableTimeslots)

```

Parameters

```
   serviceResourceId
```

Type: String

Record ID of the service resource.

```
   unavailableTimeslots
```

Type: Set<lxscheduler.UnavailableTimeslot>

An instance of lxscheduler.UnavailableTimeslot class.

#### ServiceResourceSchedule Properties The following are properties for ServiceResourceSchedule .

IN THIS SECTION:

serviceResourceId
Record ID of the service resource.

unavailableTimeslots
An instance of lxscheduler.UnavailableTimeslot class.


### Apex Reference Guide UnavailableTimeslot Class

##### serviceResourceId

Record ID of the service resource.

Signature

```
   public String serviceResourceId {get; set;}

```

Property Value

Type: String

##### unavailableTimeslots

An instance of lxscheduler.UnavailableTimeslot class.

Signature

```
   public Set<lxscheduler.UnavailableTimeslot> unavailableTimeslots {get; set;}

```

Property Value

Type: Set<lxscheduler.UnavailableTimeslot>

### UnavailableTimeslot Class

Use this class to pass the unavailable time slots to the lxscheduler.ServiceResourceSchedule class. Timezones that differ across operating
hours are handled and results are always returned in UTC.

Namespace

LxScheduler

IN THIS SECTION:

#### UnavailableTimeslot Constructors

UnavailableTimeslot Properties

#### UnavailableTimeslot Constructors

### The following are constructors for UnavailableTimeslot .

IN THIS SECTION:

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.


Apex Reference Guide UnavailableTimeslot Class

Signature

```
   public UnavailableTimeslot(Datetime timeMin, Datetime timeMax)

```

Parameters

##### _`timeMin`_

Type: Datetime

Start time of an unavailable time slot.

##### _`timeMax`_

Type: Datetime

End time of an unavailable time slot.

#### UnavailableTimeslot Properties The following are properties for UnavailableTimeslot .

IN THIS SECTION:

##### timeMax

End time of an unavailable time slot.

##### timeMin

Start time of an unavailable time slot.

##### timeMax

End time of an unavailable time slot.

Signature

```
   public Datetime timeMax {get; set;}

```

Property Value

Type: Datetime

##### timeMin

Start time of an unavailable time slot.

Signature

```
   public Datetime timeMin {get; set;}

```

Property Value

Type: Datetime


## Apex Reference Guide Messaging Namespace Messaging Namespace The Messaging namespace provides classes and methods for Salesforce outbound and inbound email functionality. The following are the classes in the Messaging namespace.

IN THIS SECTION:

AttachmentRetrievalOption Enum
Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

Email Class (Base Email Methods)
Contains base email methods common to both single and mass email.

EmailFileAttachment Class
EmailFileAttachment is used in SingleEmailMessage to specify attachments passed in as part of the request, as opposed to existing
documents in Salesforce.

InboundEmail Class
Represents an inbound email object.

InboundEmail.AuthenticationResult Class
Contains the authentication type and response for inbound emails.

InboundEmail.AuthenticationResultField Class
Contains field data from the authentication result response for inbound emails.

InboundEmail.BinaryAttachment Class
An InboundEmail object stores binary attachments in an InboundEmail.BinaryAttachment object.

InboundEmail.TextAttachment Class
An InboundEmail object stores text attachments in an InboundEmail.TextAttachment object.

InboundEmailResult Class
The InboundEmailResult object is used to return the result of the email service. If this object is null, the result is assumed to be
successful.

InboundEnvelope Class
The InboundEnvelope object stores the envelope information associated with the inbound email, and has the following fields.

MassEmailMessage Class
Contains methods for sending mass email.

InboundEmail.Header Class
An InboundEmail object stores RFC 2822 email header information in an InboundEmail.Header object with the following properties.

PushNotification Class

`PushNotification` is used to configure push notifications and send them from an Apex trigger.

PushNotificationPayload Class
Contains methods to create the notification message payload for an Apple device.

CustomNotification Class

`CustomNotification` is used to create, configure, and send custom notifications from Apex code.

RenderEmailTemplateBodyResult Class
Contains the results for rendering email templates.


### Apex Reference Guide AttachmentRetrievalOption Enum

RenderEmailTemplateError Class
Represents an error that the `RenderEmailTemplateBodyResult` object can contain.

SendEmailError Class
Represents an error that the SendEmailResult object may contain.

SendEmailResult Class
Contains the result of sending an email message.

SingleEmailMessage Class
Contains methods for sending single email messages.

### AttachmentRetrievalOption Enum

Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

Use these enum values with the renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption) method.

Enum Values

The following are the values of the `Messaging.AttachmentRetrievalOption` enum.

**Value** **Description**

`METADATA_ONLY` Includes only the file name, content type, and the object ID in the
`fileAttachments` property of `Messaging.SingleEmailMessage` .

Note: When the template is rendered from a Visualforce template (and not
from a static file attached to the template), the object ID is not available.

```
METADATA_WITH_BODY

```

Includes the attachment content, in addition to the file name, content type, and
the object ID in the `fileAttachments` property of
`Messaging.SingleEmailMessage` .

`NONE` Doesn’t include any attachments in `Messaging.SingleEmailMessage` .

### Email Class (Base Email Methods)

Contains base email methods common to both single and mass email.


Apex Reference Guide Email Class (Base Email Methods)

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

If templates are not being used, all email content must be in plain text, HTML, or both.Visualforce email templates cannot be used for
mass email.

#### Email Methods The following are methods for Email . All are instance methods.

IN THIS SECTION:

##### setBccSender(bcc)

Indicates whether the email sender receives a copy of the email that is sent. For a mass mail, the sender is only copied on the first
email sent.

setReplyTo(replyAddress)
Optional. The email address that receives the message when a recipient replies.

setTemplateID(templateId)
The ID of the template to be merged to create this email. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

setSaveAsActivity(saveAsActivity)
Optional. The default value is `true`, meaning the email is saved as an activity. This argument only applies if the recipient list is based
on `targetObjectId` or `targetObjectIds` . If HTML email tracking is enabled for the organization, you will be able to track
open rates.

setSenderDisplayName(displayName)
Optional. The name that appears on the From line of the email. This cannot be set if the object associated with a
`setOrgWideEmailAddressId` for a SingleEmailMessage has defined its `DisplayName` field.

setUseSignature(useSignature)
Indicates whether the email includes an email signature if the user has one configured. The default is `true`, meaning if the user
has a signature it is included in the email unless you specify `false` .

##### setBccSender(bcc)

Indicates whether the email sender receives a copy of the email that is sent. For a mass mail, the sender is only copied on the first email
sent.

Signature

```
   public Void setBccSender(Boolean bcc)

```


Apex Reference Guide Email Class (Base Email Methods)

Parameters

```
   bcc
```

Type: Boolean

Return Value

Type: Void

Usage

Note: If the BCC compliance option is set at the organization level, the user cannot add BCC addresses on standard messages.
The following error code is returned: `BCC_NOT_ALLOWED_IF_BCC_ COMPLIANCE_ENABLED` . Contact your Salesforce
representative for information on BCC compliance.

##### setReplyTo(replyAddress)

Optional. The email address that receives the message when a recipient replies.

Signature

```
   public Void setReplyTo(String replyAddress)

```

Parameters

```
   replyAddress
```

Type: String

Return Value

Type: Void

##### setTemplateID(templateId)

The ID of the template to be merged to create this email. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

Signature

```
   public Void setTemplateID(ID templateId)

```

Parameters

```
   templateId
```

Type: ID

Return Value

Type: Void


Apex Reference Guide Email Class (Base Email Methods)

Usage

Note: `setHtmlBody` and `setPlainTextBody` apply only to single email methods, not to mass email methods.

##### setSaveAsActivity(saveAsActivity)

Optional. The default value is `true`, meaning the email is saved as an activity. This argument only applies if the recipient list is based
on `targetObjectId` or `targetObjectIds` . If HTML email tracking is enabled for the organization, you will be able to track
open rates.

Signature

```
   public Void setSaveAsActivity(Boolean saveAsActivity)

```

Parameters

```
   saveAsActivity
```

Type: Boolean

Return Value

Type: Void

##### setSenderDisplayName(displayName)

Optional. The name that appears on the From line of the email. This cannot be set if the object associated with a
`setOrgWideEmailAddressId` for a SingleEmailMessage has defined its `DisplayName` field.

Signature

```
   public Void setSenderDisplayName(String displayName)

```

Parameters

```
   displayName
```

Type: String

Return Value

Type: Void

##### setUseSignature(useSignature)

Indicates whether the email includes an email signature if the user has one configured. The default is `true`, meaning if the user has a
signature it is included in the email unless you specify `false` .

Signature

```
   public Void setUseSignature(Boolean useSignature)

```


### Apex Reference Guide EmailFileAttachment Class

Parameters

```
   useSignature
```

Type: Boolean

Return Value

Type: Void

### EmailFileAttachment Class

EmailFileAttachment is used in SingleEmailMessage to specify attachments passed in as part of the request, as opposed to existing
documents in Salesforce.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

IN THIS SECTION:

#### EmailFileAttachment Constructors EmailFileAttachment Properties EmailFileAttachment Constructors

### The following are constructors for EmailFileAttachment .

IN THIS SECTION:

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

Signature

```
   public EmailFileAttachment()

#### EmailFileAttachment Properties

### The following are properties for EmailFileAttachment .

```


Apex Reference Guide EmailFileAttachment Class

IN THIS SECTION:

##### body

Gets or sets the attachment itself.

##### contenttype

Gets or sets the attachment's Content-Type.

##### filename

Gets or sets the name of the file to attach.

id
Read-Only. Gets the attachment ID.

inline
Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).

##### body

Gets or sets the attachment itself.

Signature

```
   public Blob body {get; set;}

```

Property Value

Type: Blob

##### contenttype

Gets or sets the attachment's Content-Type.

Signature

```
   public String contenttype {get; set;}

```

Property Value

Type: String

##### filename

Gets or sets the name of the file to attach.

Signature

```
   public String filename {get; set;}

```

Property Value

Type: String


### Apex Reference Guide InboundEmail Class

##### id

Read-Only. Gets the attachment ID.

Signature

```
   public Id id {get;}

```

Property Value

Type: Id

##### inline

Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).

Signature

```
   public Boolean inline {get; set;}

```

Property Value

Type: Boolean

### InboundEmail Class

Represents an inbound email object.

Namespace

Messaging

IN THIS SECTION:

#### InboundEmail Constructors

InboundEmail Properties

#### InboundEmail Constructors

### The following are constructors for InboundEmail .

IN THIS SECTION:

##### InboundEmail()

Creates a new instance of the `Messaging.InboundEmail` class.

##### InboundEmail()

Creates a new instance of the `Messaging.InboundEmail` class.


Apex Reference Guide InboundEmail Class

Signature

```
   public InboundEmail()

#### InboundEmail Properties The following are properties for InboundEmail .

```

IN THIS SECTION:

authenticationResults
A list of authentication results received with the email, if any.

binaryAttachments
A list of binary attachments received with the email, if any.

ccAddresses
A list of carbon copy (CC) addresses, if any.

fromAddress
The email address that appears in the From field.

fromName
The name that appears in the From field, if any.

headers
A list of the RFC 2822 headers in the email.

htmlBody
The HTML version of the email, if specified by the sender.

htmlBodyIsTruncated
Indicates whether the HTML body text is truncated ( `true` ) or not ( `false` .)

inReplyTo
The In-Reply-To field of the incoming email. Identifies the email or emails to which this one is a reply (parent emails). Contains the
parent email or emails' message-IDs.

messageId
The Message-ID—the incoming email's unique identifier.

plainTextBody
The plain text version of the email, if specified by the sender.

plainTextBodyIsTruncated
Indicates whether the plain body text is truncated ( `true` ) or not ( `false` .)

references
The References field of the incoming email. Identifies an email thread. Contains a list of the parent emails' References and message
IDs, and possibly the In-Reply-To fields.

replyTo
The email address that appears in the reply-to header.

subject
The subject line of the email, if any.


Apex Reference Guide InboundEmail Class

textAttachments
A list of text attachments received with the email, if any.

toAddresses
The email address that appears in the `To` field.

##### **`authenticationResults`**

A list of authentication results received with the email, if any.

Signature

```
   public InboundEmail.AuthenticationResult[] authenticationResults {get; set;}

```

Property Value

Type: InboundEmail.AuthenticationResult[]

Usage

Examples of authentication results include `dkim`, `dmarc`, and `spf` .

##### binaryAttachments

A list of binary attachments received with the email, if any.

Signature

```
   public InboundEmail.BinaryAttachment[] binaryAttachments {get; set;}

```

Property Value

Type: InboundEmail.BinaryAttachment[]

Usage

Examples of binary attachments include image, audio, application, and video files.

##### ccAddresses

A list of carbon copy (CC) addresses, if any.

Signature

```
   public String[] ccAddresses {get; set;}

```

Property Value

Type: String[]


Apex Reference Guide InboundEmail Class

##### fromAddress

The email address that appears in the From field.

Signature

```
   public String fromAddress {get; set;}

```

Property Value

Type: String

##### fromName

The name that appears in the From field, if any.

Signature

```
   public String fromName {get; set;}

```

Property Value

Type: String

##### headers

A list of the RFC 2822 headers in the email.

Signature

```
   public InboundEmail.Header[] headers {get; set;}

```

Property Value

Type: InboundEmail.Header[]

Usage

The list of the RFC 2822 headers includes:

**•** Recieved from

**•** Custom headers

**•** Message-ID

**•** Date

##### htmlBody

The HTML version of the email, if specified by the sender.


Apex Reference Guide InboundEmail Class

Signature

```
   public String htmlBody {get; set;}

```

Property Value

Type: String

##### htmlBodyIsTruncated

Indicates whether the HTML body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean htmlBodyIsTruncated {get; set;}

```

Property Value

Type: Boolean

##### inReplyTo

The In-Reply-To field of the incoming email. Identifies the email or emails to which this one is a reply (parent emails). Contains the parent
email or emails' message-IDs.

Signature

```
   public String inReplyTo {get; set;}

```

Property Value

Type: String

##### messageId

The Message-ID—the incoming email's unique identifier.

Signature

```
   public String messageId {get; set;}

```

Property Value

Type: String

##### plainTextBody

The plain text version of the email, if specified by the sender.


Apex Reference Guide InboundEmail Class

Signature

```
   public String plainTextBody {get; set;}

```

Property Value

Type: String

##### plainTextBodyIsTruncated

Indicates whether the plain body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean plainTextBodyIsTruncated {get; set;}

```

Property Value

Type: Boolean

##### references

The References field of the incoming email. Identifies an email thread. Contains a list of the parent emails' References and message IDs,
and possibly the In-Reply-To fields.

Signature

```
   public String[] references {get; set;}

```

Property Value

Type: String[]

##### replyTo

The email address that appears in the reply-to header.

Signature

```
   public String replyTo {get; set;}

```

Property Value

Type: String

Usage

If there is no reply-to header, this field is identical to the `fromAddress` field.


### Apex Reference Guide InboundEmail.AuthenticationResult Class

##### subject

The subject line of the email, if any.

Signature

```
   public String subject {get; set;}

```

Property Value

Type: String

##### textAttachments

A list of text attachments received with the email, if any.

Signature

```
   public InboundEmail.TextAttachment[] textAttachments {get; set;}

```

Property Value

Type: InboundEmail.TextAttachment[]

Usage

The text attachments can be any of the following:

##### • Attachments with a Multipurpose Internet Mail Extension (MIME) type of text

**•** Attachments with a MIME type of `application/octet-stream` and a file name that ends with either a `.vcf` or `.vcs`
extension. These are saved as `text/x-vcard` and `text/calendar` MIME types, respectively.

##### toAddresses

The email address that appears in the `To` field.

Signature

```
   public String[] toAddresses {get; set;}

```

Property Value

Type: String[]

### InboundEmail.AuthenticationResult Class

Contains the authentication type and response for inbound emails.

Namespace

Messaging


Apex Reference Guide InboundEmail.AuthenticationResult Class

IN THIS SECTION:

#### InboundEmail.AuthenticationResult Constructors InboundEmail.AuthenticationResult Properties InboundEmail.AuthenticationResult Constructors The following are constructors for InboundEmail.AuthenticationResult .

IN THIS SECTION:

##### InboundEmail.AuthenticationResult()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResult` class.

##### InboundEmail.AuthenticationResult()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResult` class.

Signature

```
   public InboundEmail.AuthenticationResult()

#### InboundEmail.AuthenticationResult Properties The following are properties for InboundEmail.AuthenticationResult .

```

IN THIS SECTION:

##### authenticationResultFields

Additional information in authentication result headers. Examples include: `name: smtp.mailfrom` and `value:`
`example.com` .

method
The authentication method used for the security check. Possible values include `dkim`, `dmarc`, or `spf` .

result
The result of the authentication check. When the email service is configured to verify the legitimacy of the sending server before
processing a message, possible values include `pass` or `fail` . Otherwise, the value returned is `none` .

##### **`authenticationResultFields`**

Additional information in authentication result headers. Examples include: `name: smtp.mailfrom` and `value: example.com` .

Signature

```
   public InboundEmail.AuthenticationResultField[] authenticationResultFields {get; set;}

```

Property Value

Type: InboundEmail.AuthenticationResultField[]


### Apex Reference Guide InboundEmail.AuthenticationResultField Class

##### **`method`**

The authentication method used for the security check. Possible values include `dkim`, `dmarc`, or `spf` .

Signature

```
   public String method {get; set;}

```

Property Value

Type: String

##### **`result`**

The result of the authentication check. When the email service is configured to verify the legitimacy of the sending server before processing
a message, possible values include `pass` or `fail` . Otherwise, the value returned is `none` .

Signature

```
   public String result {get; set;}

```

Property Value

Type: String

### InboundEmail.AuthenticationResultField Class

Contains field data from the authentication result response for inbound emails.

Namespace

Messaging

IN THIS SECTION:

#### InboundEmail.AuthenticationResultField Constructors

InboundEmail.AuthenticationResultField Properties

#### InboundEmail.AuthenticationResultField Constructors

### The following are constructors for InboundEmail.AuthenticationResultField .

IN THIS SECTION:

##### InboundEmail.AuthenticationResultField()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResultField` class.

##### InboundEmail.AuthenticationResultField()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResultField` class.


### Apex Reference Guide InboundEmail.BinaryAttachment Class

Signature

```
   public InboundEmail.AuthenticationResultField()

#### InboundEmail.AuthenticationResultField Properties The following are properties for InboundEmail.AuthenticationResultField .

```

IN THIS SECTION:

##### name

The authentication result field name. For example: `smtp.mailfrom` .

##### value

The authentication result field value. For example: `example.com` .

##### **`name`**

The authentication result field name. For example: `smtp.mailfrom` .

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`value`**

The authentication result field value. For example: `example.com` .

Signature

```
   public String value {get; set;}

```

Property Value

Type: String

### InboundEmail.BinaryAttachment Class

An InboundEmail object stores binary attachments in an InboundEmail.BinaryAttachment object.

Namespace

Messaging


Apex Reference Guide InboundEmail.BinaryAttachment Class

Usage

Examples of binary attachments include image, audio, application, and video files.

IN THIS SECTION:

#### InboundEmail.BinaryAttachment Constructors InboundEmail.BinaryAttachment Properties InboundEmail.BinaryAttachment Constructors The following are constructors for InboundEmail.BinaryAttachment .

IN THIS SECTION:

##### InboundEmail.BinaryAttachment()

Creates a new instance of the `Messaging.InboundEmail.BinaryAttachment` class.

##### InboundEmail.BinaryAttachment()

Creates a new instance of the `Messaging.InboundEmail.BinaryAttachment` class.

Signature

```
   public InboundEmail.BinaryAttachment()

#### InboundEmail.BinaryAttachment Properties The following are properties for InboundEmail.BinaryAttachment .

```

IN THIS SECTION:

##### body

The body of the attachment.

fileName
The name of the attached file.

headers
Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

mimeTypeSubType
The primary and sub MIME-type.

##### body

The body of the attachment.


### Apex Reference Guide InboundEmail.TextAttachment Class

Signature

```
   public Blob body {get; set;}

```

Property Value

Type: Blob

##### fileName

The name of the attached file.

Signature

```
   public String fileName {get; set;}

```

Property Value

Type: String

##### headers

Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

Signature

```
   public List<Messaging.InboundEmail.Header> headers {get; set;}

```

Property Value

Type: List<Messaging.InboundEmail.Header>

##### mimeTypeSubType

The primary and sub MIME-type.

Signature

```
   public String mimeTypeSubType {get; set;}

```

Property Value

Type: String

### InboundEmail.TextAttachment Class

An InboundEmail object stores text attachments in an InboundEmail.TextAttachment object.


Apex Reference Guide InboundEmail.TextAttachment Class

Namespace

Messaging

Usage

The text attachments can be any of the following:

**•** Attachments with a Multipurpose Internet Mail Extension (MIME) type of `text`

**•** Attachments with a MIME type of `application/octet-stream` and a file name that ends with either a `.vcf` or `.vcs`
extension. These are saved as `text/x-vcard` and `text/calendar` MIME types, respectively.

IN THIS SECTION:

#### InboundEmail.TextAttachment Constructors InboundEmail.TextAttachment Properties InboundEmail.TextAttachment Constructors The following are constructors for InboundEmail.TextAttachment .

IN THIS SECTION:

##### InboundEmail.TextAttachment()

Creates a new instance of the `Messaging.InboundEmail.TextAttachment` class.

##### InboundEmail.TextAttachment()

Creates a new instance of the `Messaging.InboundEmail.TextAttachment` class.

Signature

```
   public InboundEmail.TextAttachment()

#### InboundEmail.TextAttachment Properties The following are properties for InboundEmail.TextAttachment .

```

IN THIS SECTION:

body
The body of the attachment.

bodyIsTruncated
Indicates whether the attachment body text is truncated ( `true` ) or not ( `false` .)

charset
The original character set of the body field. The body is re-encoded as UTF-8 as input to the Apex method.

fileName
The name of the attached file.


Apex Reference Guide InboundEmail.TextAttachment Class

headers
Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

mimeTypeSubType
The primary and sub MIME-type.

##### body

The body of the attachment.

Signature

```
   public String body {get; set;}

```

Property Value

Type: String

##### bodyIsTruncated

Indicates whether the attachment body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean bodyIsTruncated {get; set;}

```

Property Value

Type: Boolean

##### charset

The original character set of the body field. The body is re-encoded as UTF-8 as input to the Apex method.

Signature

```
   public String charset {get; set;}

```

Property Value

Type: String

##### fileName

The name of the attached file.

Signature

```
   public String fileName {get; set;}

```


### Apex Reference Guide InboundEmailResult Class

Property Value

Type: String

##### headers

Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

Signature

```
   public List<Messaging.InboundEmail.Header> headers {get; set;}

```

Property Value

Type: List<Messaging.InboundEmail.Header>

##### mimeTypeSubType

The primary and sub MIME-type.

Signature

```
   public String mimeTypeSubType {get; set;}

```

Property Value

Type: String

### InboundEmailResult Class

The InboundEmailResult object is used to return the result of the email service. If this object is null, the result is assumed to be successful.

Namespace

Messaging

#### InboundEmailResult Properties

### The following are properties for InboundEmailResult .

IN THIS SECTION:

message
A message that Salesforce returns in the body of a reply email. This field can be populated with text irrespective of the value returned
by the `Success` field.

success
A value that indicates whether the email was successfully processed.


### Apex Reference Guide InboundEnvelope Class

##### message

A message that Salesforce returns in the body of a reply email. This field can be populated with text irrespective of the value returned
by the `Success` field.

Signature

```
   public String message {get; set;}

```

Property Value

Type: String

##### success

A value that indicates whether the email was successfully processed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

Usage

If `false`, Salesforce rejects the inbound email and sends a reply email to the original sender containing the message specified in the
`Message` field.

### InboundEnvelope Class

The InboundEnvelope object stores the envelope information associated with the inbound email, and has the following fields.

Namespace

Messaging

#### InboundEnvelope Properties

### The following are properties for InboundEnvelope .

IN THIS SECTION:

fromAddress
The name that appears in the `From` field of the envelope, if any.

toAddress
The name that appears in the `To` field of the envelope, if any.


### Apex Reference Guide MassEmailMessage Class

##### fromAddress

The name that appears in the `From` field of the envelope, if any.

Signature

```
   public String fromAddress {get; set;}

```

Property Value

Type: String

##### toAddress

The name that appears in the `To` field of the envelope, if any.

Signature

```
   public String toAddress {get; set;}

```

Property Value

Type: String

### MassEmailMessage Class

Contains methods for sending mass email.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

MassEmailMessage extends Email and inherits all of its methods. All base email ( `Email` class) methods are also available to the
### MassEmailMessage objects.

IN THIS SECTION:

MassEmailMessage Constructors

MassEmailMessage Methods

SEE ALSO:

Email Class (Base Email Methods)


Apex Reference Guide MassEmailMessage Class

#### MassEmailMessage Constructors The following are constructors for MassEmailMessage .

IN THIS SECTION:

##### MassEmailMessage()

Creates a new instance of the `Messaging.MassEmailMessage` class.

##### MassEmailMessage()

Creates a new instance of the `Messaging.MassEmailMessage` class.

Signature

```
   public MassEmailMessage()

#### MassEmailMessage Methods The following are methods for MassEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the MassEmailMessage objects. These methods are described in Email Class (Base Email Methods).

```

IN THIS SECTION:

##### setDescription(description)

The description of the email.

setTargetObjectIds(targetObjectIds)
A list of IDs of the contacts, leads, or users to which the email will be sent. The IDs you specify set the context and ensure that merge
fields in the template contain the correct data. The objects must be of the same type (all contacts, all leads, or all users).

setWhatIds(whatIds)
Optional. If you specify a list of contacts for the `targetObjectIds` field, you can specify a list of `whatIds` as well. This helps
to further ensure that merge fields in the template contain the correct data.

##### setDescription(description)

The description of the email.

Signature

```
   public Void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: Void


Apex Reference Guide MassEmailMessage Class

##### setTargetObjectIds(targetObjectIds)

A list of IDs of the contacts, leads, or users to which the email will be sent. The IDs you specify set the context and ensure that merge
fields in the template contain the correct data. The objects must be of the same type (all contacts, all leads, or all users).

Signature

```
   public Void setTargetObjectIds(ID[] targetObjectIds)

```

Parameters

```
   targetObjectIds
```

Type: ID[]

Return Value

Type: Void

Usage

You can list multiple IDs per email. If you specify a value for the `targetObjectIds` field, optionally specify a `whatId` as well to
set the email context to a user, contact, or lead. This ensures that merge fields in the template contain the correct data. Each ID counts
against the sending organization's daily mass email limit.

Do not specify the IDs of records that have the `Email Opt Out` option selected.

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setWhatIds(whatIds)

Optional. If you specify a list of contacts for the `targetObjectIds` field, you can specify a list of `whatIds` as well. This helps to
further ensure that merge fields in the template contain the correct data.

Signature

```
   public Void setWhatIds(ID[] whatIds)

```

Parameters

```
   whatIds
```

Type: ID[]

Return Value

Type: Void


### Apex Reference Guide InboundEmail.Header Class

Usage

The values must be one of the following types:

**•** Contract

**•** Case

**•** Opportunity

**•** Product

Note: If you specify `whatIds`, specify one for each `targetObjectId` ; otherwise, you will receive an `INVALID_ID_FIELD`
error.

### InboundEmail.Header Class

An InboundEmail object stores RFC 2822 email header information in an InboundEmail.Header object with the following properties.

Namespace

Messaging

#### InboundEmail.Header Properties

### The following are properties for InboundEmail.Header .

IN THIS SECTION:

##### name

The name of the header parameter, such as `Date` or `Message-ID` .

##### value

The value of the header.

##### name

The name of the header parameter, such as `Date` or `Message-ID` .

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### value

The value of the header.

Signature

```
   public String value {get; set;}

```


### Apex Reference Guide PushNotification Class

Property Value

Type: String

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound_what_is.htm)_ : Apex Email Service

_Apex Developer Guide_ [: Using the InboundEmail Object](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound_using.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound.htm)_ : Inbound Email

_[Internet Engineering Task Force (IETF) Data Tracker](https://datatracker.ietf.org/doc/html/rfc2822#section-3.6)_ : RFC 2822 Section 3.6

### PushNotification Class PushNotification is used to configure push notifications and send them from an Apex trigger.

Namespace

Messaging

Example

This sample Apex trigger sends push notifications to the external client app named _`Test_App`_, which corresponds to a mobile app
on iOS mobile clients. The trigger fires after cases have been updated and sends the push notification to two users: the case owner and
the user who last modified the case.

```
   trigger caseAlert on Case (after update) {

      for(Case cs : Trigger.New)

      {

        // Instantiating a notification

        Messaging.PushNotification msg =

           new Messaging.PushNotification();

        // Assembling the necessary payload parameters for Apple.

        // Apple params are:

        // (<alert text>,<alert sound>,<badge count>,

        // <free-form data>)

        // This example doesn't use badge count or free-form data.

        // The number of notifications that haven't been acted

        // upon by the intended recipient is best calculated

        // at the time of the push. This timing helps

        // ensure accuracy across multiple target devices.

        Map<String, Object> payload =

           Messaging.PushNotificationPayload.apple(

             'Case ' + cs.CaseNumber + ' status changed to: '

             + cs.Status, '', null, null);

        // Adding the assembled payload to the notification

        msg.setPayload(payload);

        // Getting recipient users

        String userId1 = cs.OwnerId;

```


Apex Reference Guide PushNotification Class

```
        String userId2 = cs.LastModifiedById;

        // Adding recipient users to list

        Set<String> users = new Set<String>();

        users.add(userId1);

        users.add(userId2);

        // Sending the notification to the specified app and users.

        // Here we specify the API name of the external client app.

        msg.send('Test_App', users);

      }

   }

```

IN THIS SECTION:

#### PushNotification Constructors

PushNotification Methods

#### PushNotification Constructors The following are the constructors for PushNotification .

IN THIS SECTION:

##### PushNotification()

Creates a new instance of the `Messaging.PushNotification` class.

##### PushNotification(payload)

Creates a new instance of the `Messaging.PushNotification` class using the specified payload parameters as key-value
pairs. When you use this constructor, you don’t need to call `setPayload` to set the payload.

##### PushNotification()

Creates a new instance of the `Messaging.PushNotification` class.

Signature

```
   public PushNotification()

##### PushNotification(payload)

```

Creates a new instance of the `Messaging.PushNotification` class using the specified payload parameters as key-value pairs.
When you use this constructor, you don’t need to call `setPayload` to set the payload.

Signature

```
   public PushNotification(Map<String,Object> payload )

```


Apex Reference Guide PushNotification Class

Parameters

```
   payload
```

Type:Map<String, Object>

The payload, expressed as a map of key-value pairs.

#### PushNotification Methods The following are the methods for PushNotification . All are global methods.

IN THIS SECTION:

##### send(application, users)

Sends a push notification message to the specified users.

##### setPayload(payload)

Sets the payload of the push notification message.

setTtl(ttl)
Reserved for future use.

##### send(application, users)

Sends a push notification message to the specified users.

Signature

```
   public void send(String application, Set<String> users)

```

Parameters

```
   application
```

Type: String

The connected app API name. This corresponds to the mobile client app the notification should be sent to.

```
   users
```

Type: Set

A set of user IDs that correspond to the users the notification should be sent to.

Example

See the Push Notification Example.

##### setPayload(payload)

Sets the payload of the push notification message.

Signature

```
   public void setPayload(Map<String,Object> payload)

```


### Apex Reference Guide PushNotificationPayload Class

Parameters

```
   payload
```

Type: Map<String, Object>

The payload, expressed as a map of key-value pairs.

Payload parameters can be different for each mobile OS vendor. For more information on Apple’s payload parameters, search for
[“Apple Push Notification Service” at https://developer.apple.com/library/mac/documentation/.](https://developer.apple.com/library/mac/documentation)

To create the payload for an Apple device, see the PushNotificationPayload Class.

Example

See the Push Notification Example.

##### setTtl(ttl)

Reserved for future use.

Signature

```
   public void setTtl(Integer ttl)

```

Parameters

```
   ttl
```

Type: Integer

Reserved for future use.

### PushNotificationPayload Class

Contains methods to create the notification message payload for an Apple device.

Namespace

Messaging

Usage

Apple has specific requirements for the notification payload. and this class has helper methods to create the payload. For more information
[on Apple’s payload parameters, search for “Apple Push Notification Service” at https://developer.apple.com/library/mac/documentation/.](https://developer.apple.com/library/mac/documentation/)

Example

See the Push Notification Example.

IN THIS SECTION:

PushNotificationPayload Methods


Apex Reference Guide PushNotificationPayload Class

#### PushNotificationPayload Methods The following are the methods for PushNotificationPayload . All are global static methods.

IN THIS SECTION:

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

apple(alertBody, actionLocKey, locKey, locArgs, launchImage, sound, badgeCount, userData)
Helper method that creates a valid Apple payload from the specified arguments.

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

Signature

```
   public static Map<String,Object> apple(String alert, String sound, Integer badgeCount,

   Map<String,Object> userData)

```

Parameters

```
   alert
```

Type: String

Notification message to be sent to the mobile client.

```
   sound
```

Type: String

Name of a sound file to be played as an alert. This sound file should be in the mobile application bundle.

```
   badgeCount
```

Type: Integer

Number to display as the badge of the application icon.

```
   userData
```

Type: Map<String, Object>

Map of key-value pairs that contains any additional data used to provide context for the notification. For example, it can contain IDs
of the records that caused the notification to be sent. The mobile client app can use these IDs to display these records.

Return Value

Type:Map<String, Object>

Returns a formatted payload that includes all of the specified arguments.

Usage

To generate a valid payload, you must provide a value for at least one of the following parameters: `alert`, `sound`, `badgeCount` .


Apex Reference Guide PushNotificationPayload Class

Example

See the Push Notification Example.

##### apple(alertBody, actionLocKey, locKey, locArgs, launchImage, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

Signature

```
   public static Map<String,Object> apple(String alertBody, String actionLocKey, String

   locKey, String[] locArgs, String launchImage, String sound, Integer badgeCount,

   Map<String,Object> userData)

```

Parameters

```
   alertBody
```

Type: String

Text of the alert message.

```
   actionLocKey
```

Type: String

If a value is specified for the _`actionLocKey`_ argument, an alert with two buttons is displayed. The value is a key to get a localized
string in a `Localizable.strings` file to use for the right button’s title.

```
   locKey
```

Type: String

Key to an alert-message string in a `Localizable.strings` file for the current localization.

```
   locArgs
```

Type: List<String>

Variable string values to appear in place of the format specifiers in _`locKey`_ .

```
   launchImage
```

Type: String

File name of an image file in the application bundle.

```
   sound
```

Type: String

Name of a sound file to be played as an alert. This sound file should be in the mobile application bundle.

```
   badgeCount
```

Type: Integer

Number to display as the badge of the application icon.

```
   userData
```

Type: Map<String, Object>

Map of key-value pairs that contains any additional data used to provide context for the notification. For example, it can contain IDs
of the records that caused the notification to be sent. The mobile client app can use these IDs to display these records.


### Apex Reference Guide CustomNotification Class

Return Value

Type: Map<String, Object>

Returns a formatted payload that includes all of the specified arguments.

Usage

To generate a valid payload, you must provide a value for at least one of the following parameters: `alert`, `sound`, `badgeCount` .

### CustomNotification Class CustomNotification is used to create, configure, and send custom notifications from Apex code.

Namespace

Messaging

Usage

### CustomNotification allows two approaches to creating and configuring a custom notification.

**•** Create an instance with the default constructor, and then set notification attributes using the various setter methods.

**•** Create an instance and configure notification parameters at the same time using the parameterized constructor.

Once the custom notification is configured, call `send()` to send the notification.

**Notification Target**

The _notification target_ is used by the receiving client application to navigate to an appropriate record or page when a user responds to
a notification. For example, when a user is notified that a record was updated, responding to the notification can open the relevant
record.

You must specify a target for a notification. The target can be specified using either the `targetID` or the `targetPageRef` attribute.
Neither attribute is required, but if both are omitted, `send()` throws an exception. If there’s no natural target for a notification, set the
`targetID` to a dummy value, such as _`000000000000000AAA`_ . A dummy value prevents the exception, and also prevents
automatic navigation when responding to the notification in the client app.

You can set both `targetID` and `targetPageRef` in the same notification. The client app that receives the notification determines
which target, if any, to use when responding to the notification.

Important: Before Winter ’21 you could set only a target record ( `targetID` ) for a notification. Most client applications expect
to find a `targetID` in the notification payload. If you can’t update a client app to handle notifications that include only a
`targetPageRef`, set the `targetID` to a dummy value.

**Execution Context and Notification Permissions**

### By default Apex code executes in system mode, and doesn’t require user permissions to send notifications with CustomNotification .

However, if your Apex code runs in a user context—for example, by executing anonymous Apex in the Developer Console—the Send
Custom Notifications user permission is checked, and `send()` fails if you don’t have the required permission.


Apex Reference Guide CustomNotification Class

Example

This example Apex class provides a static method for sending a custom notification to a recipient list. Call this method from a trigger,
flow, or wherever you want to send a custom notification from Apex.

```
   public without sharing class CustomNotificationFromApex {

      public static void notifyUsers(Set<String> recipientsIds, String targetId) {

        // Get the Id for our custom notification type

        CustomNotificationType notificationType =

           [SELECT Id, DeveloperName

           FROM CustomNotificationType

           WHERE DeveloperName='Custom_Notification'];

        // Create a new custom notification

        Messaging.CustomNotification notification = new Messaging.CustomNotification();

        // Set the contents for the notification

        notification.setTitle('Apex Custom Notification');

        notification.setBody('The notifications are coming from INSIDE the Apex!');

        // Set the notification type and target

        notification.setNotificationTypeId(notificationType.Id);

        notification.setTargetId(targetId);

        // Actually send the notification

        try {

           notification.send(recipientsIds);

        }

        catch (Exception e) {

           System.debug('Problem sending notification: ' + e.getMessage());

        }

      }

   }

```

Note: This example uses a custom notification type with the `DeveloperName` (API name) _`Custom_Notification`_ .
[You can create a custom notification type using Notification Builder in Setup or Tooling API. Then, use your notification type’s](https://help.salesforce.com/s/articleView?id=platform.notif_builder.htm&language=en_US)
`DeveloperName` (API name) in the query to find the ID of the notification type.

`CustomNotification.send()` can throw an exception, which is handled minimally in this example. Add more substantial
error handling to code you plan to use in production.

IN THIS SECTION:

CustomNotification Constructors

CustomNotification Methods

SEE ALSO:

_Salesforce Help_ [: Send Custom Notifications](https://help.salesforce.com/articleView?id=notif_builder_custom.htm&language=en_US)

_Actions Developer Guide_ [: Custom Notification Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_action.meta/api_action/actions_obj_custom_notification.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customnotificationtype.htm)_ : CustomNotificationType


Apex Reference Guide CustomNotification Class

#### CustomNotification Constructors The following are constructors for CustomNotification .

IN THIS SECTION:

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

##### CustomNotification(typeId, sender, title, body, targetId, targetPageRef)

Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this
constructor, you don’t need to call the various setter methods to define the custom notification attributes.

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

Signature

```
   public CustomNotification()

##### CustomNotification(typeId, sender, title, body, targetId, targetPageRef)

```

Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this constructor,
you don’t need to call the various setter methods to define the custom notification attributes.

Signature

```
   public CustomNotification(String typeId, String sender, String title, String body,

   String targetId, String targetPageRef)

```

Parameters

```
   typeId
```

Type: String

The ID of the Custom Notification Type being used for the notification.

```
   sender
```

Type: String

The User ID of the sender of the notification.

```
   title
```

Type: String

The title of the notification. Maximum characters: 250.

```
   body
```

Type: String

The body of the notification. Maximum characters: 750.

```
   targetId
```

Type: String

The Record ID for the target record of the notification.


Apex Reference Guide CustomNotification Class

You must specify either a `targetID` or a `targetPageRef` . See Custom Notification Usage.

```
   targetPageRef
```

Type: String

The `PageReference` [for the navigation target of the notification. To see how to specify the target using JSON, see pageReference](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_navigation_page_definitions.htm)
[Types.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_navigation_page_definitions.htm)

You must specify either a `targetID` or a `targetPageRe` . See Custom Notification Usage.

Usage

A client may see a truncated notification title or body depending on the delivery channel or app, and how the Connect API notification
parameters are configured. For more information on the `trimMessages` [query parameter, see Notification .](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_notifications_list.htm)

#### CustomNotification Methods The following are methods for CustomNotification .

IN THIS SECTION:

##### send(users)

Sends a custom notification to the specified users.

setNotificationTypeId(id)
Sets the type of the custom notification.

setTitle(title)
Sets the title of the custom notification.

setBody(body)
Sets the body of the custom notification.

setSenderId(id)
Sets the sender of the custom notification.

setTargetId(targetId)
Sets the target record of the custom notification.

setTargetPageRef(pageRef)
Sets the target page of the custom notification.

##### send(users)

Sends a custom notification to the specified users.

Signature

```
   public void send(Set<String> users)

```

Parameters

```
   users
```

Type: Set<String>


Apex Reference Guide CustomNotification Class

Required. A set of recipient IDs. Each recipient ID corresponds to a recipient or recipient type that the notification should be sent to.
Valid recipient or recipient type values are:

**•** `UserId`     - The notification is sent to this user, if this user is active.

**•** `AccountId`     - The notification is sent to all active users who are members of this account’s Account Team.

Note: This recipient type is valid if account teams are enabled for your org.

**•** `OpportunityId`     - The notification is sent to all active users who are members of this opportunity’s Opportunity Team.

Note: This recipient type is valid if team selling is enabled for your org.

**•** `GroupId`     - The notification is sent to all active users who are members of this group.

**•** `QueueId`     - The notification is sent to all active users who are members of this queue.

Values can be combined in a set, up to the maximum of 500 values.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setNotificationTypeId(id)

Sets the type of the custom notification.

Signature

```
   public void setNotificationTypeId(String id)

```

Parameters

```
   id
```

Type: String

The ID of the Custom Notification Type being used for the notification.

A notification type is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTitle(title)

Sets the title of the custom notification.


Apex Reference Guide CustomNotification Class

Signature

```
   public void setTitle(String title)

```

Parameters

```
   title
```

Type: String

The title of the notification, as it will be seen by recipients. Maximum characters: 250.

A title is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setBody(body)

Sets the body of the custom notification.

Signature

```
   public void setBody(String body)

```

Parameters

```
   body
```

Type: String

The body of the notification, as it will be seen by recipients. Maximum characters: 750.

A body is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setSenderId(id)

Sets the sender of the custom notification.

Signature

```
   public void setSenderId(String id)

```


Apex Reference Guide CustomNotification Class

Parameters

```
   id
```

Type: String

The User ID of the sender of the notification.

Setting a sender is optional. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTargetId(targetId)

Sets the target record of the custom notification.

Signature

```
   public void setTargetId(String targetId)

```

Parameters

```
   targetId
```

Type: String

The Record ID for the target record of the notification.

Either a `targetID` or a `targetPageRef` is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTargetPageRef(pageRef)

Sets the target page of the custom notification.

Signature

```
   public void setTargetPageRef(String pageRef)

```

Parameters

```
   pageRef
```

Type: String


### Apex Reference Guide RenderEmailTemplateBodyResult Class

The `PageReference` for the navigation target of the notification.

Either a `targetID` or a `targetPageRef` is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

### RenderEmailTemplateBodyResult Class

Contains the results for rendering email templates.

Namespace

Messaging

IN THIS SECTION:

#### RenderEmailTemplateBodyResult Methods RenderEmailTemplateBodyResult Methods

### The following are methods for RenderEmailTemplateBodyResult .

IN THIS SECTION:

##### getErrors()

If an error occurred during the `renderEmailTemplate` method, a `RenderEmailTemplateError` object is returned.

getMergedBody()
Returns the rendered body text with merge field references replaced with the corresponding record data.

getSuccess()
Indicates whether the operation was successful.

##### getErrors()

If an error occurred during the `renderEmailTemplate` method, a `RenderEmailTemplateError` object is returned.

Signature

```
   public List<Messaging.RenderEmailTemplateError> getErrors()

```

Return Value

Type: List<Messaging.RenderEmailTemplateError>


### Apex Reference Guide RenderEmailTemplateError Class

##### getMergedBody()

Returns the rendered body text with merge field references replaced with the corresponding record data.

Signature

```
   public String getMergedBody()

```

Return Value

Type: String

##### getSuccess()

Indicates whether the operation was successful.

Signature

```
   public Boolean getSuccess()

```

Return Value

Type: Boolean

### RenderEmailTemplateError Class

Represents an error that the `RenderEmailTemplateBodyResult` object can contain.

Namespace

Messaging

IN THIS SECTION:

#### RenderEmailTemplateError Methods RenderEmailTemplateError Methods

### The following are methods for RenderEmailTemplateError .

IN THIS SECTION:

getFieldName()
Returns the name of the merge field in the error.

getMessage()
Returns a message describing the error.

getOffset()
Returns the offset within the supplied body text where the error was discovered. If the offset cannot be determined, -1 is returned.


Apex Reference Guide RenderEmailTemplateError Class

##### getStatusCode()

Returns a Salesforce API status code.

##### getFieldName()

Returns the name of the merge field in the error.

Signature

```
   public String getFieldName()

```

Return Value

Type: String

##### getMessage()

Returns a message describing the error.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### getOffset()

Returns the offset within the supplied body text where the error was discovered. If the offset cannot be determined, -1 is returned.

Signature

```
   public Integer getOffset()

```

Return Value

Type: Integer

##### getStatusCode()

Returns a Salesforce API status code.

Signature

```
   public System.StatusCode getStatusCode()

```

Return Value

Type: System.StatusCode


### Apex Reference Guide SendEmailError Class SendEmailError Class

Represents an error that the SendEmailResult object may contain.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

#### SendEmailError Methods

### The following are methods for SendEmailError . All are instance methods.

IN THIS SECTION:

##### getFields()

A list of one or more field names. Identifies which fields in the object, if any, affected the error condition.

##### getMessage()

The text of the error message.

getStatusCode()
Returns a code that characterizes the error.

getTargetObjectId()
The ID of the target record for which the error occurred.

##### getFields()

A list of one or more field names. Identifies which fields in the object, if any, affected the error condition.

Signature

```
   public String[] getFields()

```

Return Value

Type: String[]

##### getMessage()

The text of the error message.

Signature

```
   public String getMessage()

```


### Apex Reference Guide SendEmailResult Class

Return Value

Type: String

##### getStatusCode()

Returns a code that characterizes the error.

Signature

```
   public System.StatusCode getStatusCode()

```

Return Value

Type: System.StatusCode

Usage

The full list of status codes is available in the WSDL file for your organization. For more information about accessing the WSDL file for
your organization, see _Downloading Salesforce WSDLs and Client Authentication Certificates_ in the Salesforce online help.

##### getTargetObjectId()

The ID of the target record for which the error occurred.

Signature

```
   public String getTargetObjectId()

```

Return Value

Type: String

### SendEmailResult Class

Contains the result of sending an email message.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

#### SendEmailResult Methods

### The following are methods for SendEmailResult . All are instance methods.


### Apex Reference Guide SingleEmailMessage Class

IN THIS SECTION:

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

##### isSuccess() Indicates whether the email was successfully submitted for delivery ( true ) or not ( false ). Even if isSuccess is true, it does

not mean the intended recipients received the email, as there could have been a problem with the email address or it could have
bounced or been blocked by a spam blocker.

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

Signature

```
   public SendEmailError[] getErrors()

```

Return Value

Type: Messaging.SendEmailError[]

##### isSuccess() Indicates whether the email was successfully submitted for delivery ( true ) or not ( false ). Even if isSuccess is true, it does not

mean the intended recipients received the email, as there could have been a problem with the email address or it could have bounced
or been blocked by a spam blocker.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### SingleEmailMessage Class

Contains methods for sending single email messages.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)


Apex Reference Guide SingleEmailMessage Class

SingleEmailMessage extends Email and inherits all of its methods. All base email ( `Email` class) methods are also available to the
#### SingleEmailMessage objects. Emails sent via SingleEmailMessage count against the sending organization's daily single email

limit.

Email properties are readable and writable. Each property has corresponding setter and getter methods. For example, the
`toAddresses()` property is equivalent to the `setToAddresses()` and `getToAddresses()` methods. Only the setter
methods are documented. However, the `getTemplateName()` method doesn’t have an equivalent setter method; use
`setTemplateId()` to specify a template name.

IN THIS SECTION:

#### SingleEmailMessage Constructors SingleEmailMessage Methods

SEE ALSO:

Email Class (Base Email Methods)

#### SingleEmailMessage Constructors The following are constructors for SingleEmailMessage .

IN THIS SECTION:

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

Signature

```
   public SingleEmailMessage()

#### SingleEmailMessage Methods The following are methods for SingleEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the SingleEmailMessage objects. These methods are described in Email Class (Base Email Methods).

```

IN THIS SECTION:

getOneClickPost()
Optional. Returns a boolean value based on the value set by the `setOneClickPost` method. Default is `false` .

getTemplateName()
The name of the template used to create the email.


Apex Reference Guide SingleEmailMessage Class

setBccAddresses(bccAddresses)
Optional. A list of blind carbon copy (BCC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The
maximum size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per
email is 150. All recipients in these three fields count against the limit for email sent using Apex or the API.

setCcAddresses(ccAddresses)
Optional. A list of carbon copy (CC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum
size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150.
All recipients in these three fields count against the limit for email sent using Apex or the API.

setCharset(characterSet)
Optional. The character set for the email. If this value is null, the user's default value is used.

setDocumentAttachments(documentIds)
**(Deprecated. Use** `setEntityAttachments()` **instead.)** Optional. A list containing the ID of each document object you
want to attach to the email.

setEntityAttachments(ids)
[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

setFileAttachments(fileNames)
Optional. A list containing the file names of the binary and text files you want to attach to the email.

setHtmlBody(htmlBody)
Optional. The HTML version of the email, specified by the sender. The value is encoded according to the specification associated
with the organization. Specify a value for `setTemplateId`, `setHtmlBody`, or `setPlainTextBody` . Or, you can define
both `setHtmlBody` and `setPlainTextBody` .

setInReplyTo(parentMessageIds)
Sets the optional In-Reply-To field of the outgoing email. This field identifies the email or emails to which this email is a reply (parent
emails).

setOneClickPost(oneClickPost)
Optional. If set to true, a List-Unsubscribe-Post header is added to an email with List-Unsubscribe=One-Click. Use this method to
support unsubscribe functionality in email sent via Salesforce. You can provide additional instructions on how to send unsubscribe
requests by using the header. This includes specifying the HTTP method and content type to use and provides a secure way to add
more info to unsubscribe requests. Default is `false` .

setOptOutPolicy(emailOptOutPolicy)
Optional. If you added recipients by ID instead of email address and the `Email Opt Out` option is set, this method determines
the behavior of the `sendEmail()` call. If you add recipients by their email addresses, the opt-out settings for those recipients
aren’t checked and those recipients always receive the email.

setPlainTextBody(plainTextBody)
Optional. The text version of the email, specified by the sender. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

setOrgWideEmailAddressId(emailAddressId)
Optional. The ID of the organization-wide email address associated with the outgoing email. If you’re using Apex to send emails
from the guest user, set the sender to the verified org-wide email address or the emails are blocked. The object's `DisplayName`
field cannot be set if the `setSenderDisplayName` field is already set.

setReferences(references)
Optional. The References field of the outgoing email. Identifies an email thread. Contains the parent emails' References and message
IDs, and possibly the In-Reply-To fields.


Apex Reference Guide SingleEmailMessage Class

setSubject(subject)
Optional. The email subject line. If you are using an email template, the subject line of the template overrides this value.

setTargetObjectId(targetObjectId)
Required if using a template, optional otherwise. The ID of the contact, lead, or user to which the email will be sent. The ID you
specify sets the context and ensures that merge fields in the template contain the correct data.

setTemplateId(templateId)
Required if using a template, optional otherwise. The ID of the template used to create the email.

setToAddresses(toAddresses)
Optional. A list of email addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum size for
this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All
recipients in these three fields count against the limit for email sent using Apex or the API.

setTreatBodiesAsTemplate(treatAsTemplate)
Optional. If set to `true`, the subject, plain text, and HTML text bodies of the email are treated as template data. The merge fields
are resolved using the `renderEmailTemplate` method. Default is `false` .

setTreatTargetObjectAsRecipient(treatAsRecipient)
Optional. If set to `true`, the `targetObjectId` (a contact, lead, or user) is the recipient of the email. If set to `false`, the
`targetObjectId` is supplied as the `WhoId` field for template rendering but isn’t a recipient of the email. The default is `true` .

setUnsubscribeComment(unsubscribeComment)
Optional. Sets a comment in the List-Unsubscribe email header. This comment is ignored by email clients and systems that parse
the header. The comments contain human-readable notes or context for developers, administrators, or other stakeholders managing
the email system.

setUnsubscribeUrls(UnsubscribeUrls)
Optional. Sets a `mailto` URI and HTTP URL of a mechanism for unsubscribing a recipient from an email list. A list of all unsubscribe
URLs passed through `setUnsubscribeUrls` is added to the `List-Unsubscribe` header. A minimum of one URL is
required to use this method.

setWhatId(whatId)
If you specify a contact for the `targetObjectId` field, you can specify an optional `whatId` as well. This helps to further ensure
that merge fields in the template contain the correct data.

##### **`getOneClickPost()`**

Optional. Returns a boolean value based on the value set by the `setOneClickPost` method. Default is `false` .

Signature

```
   public Boolean getOneClickPost()

```

Parameters

Type: Boolean

Return Value

Type: Boolean


Apex Reference Guide SingleEmailMessage Class

Usage

Invoke the `setOneClickPost` method before using `getOneClickPost` . The value of `getOneClickPost` will be false if
the `setOneClickPost` method is set to true only after invoking the `setUnsubscribeUrls` method.

##### getTemplateName()

The name of the template used to create the email.

Signature

```
   public STRING getTemplateName()

```

Return Value

Type: String

Usage

##### There is no equivalent setter method for getTemplateName() . If the email didn’t use a template, getTemplateName() returns nothing. If you use setTemplateId(), and then call getTemplateName(), the template name associated to the

template ID is returned.

##### setBccAddresses(bccAddresses)

Optional. A list of blind carbon copy (BCC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The
maximum size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email
is 150. All recipients in these three fields count against the limit for email sent using Apex or the API.

Signature

```
   public Void setBccAddresses(String[] bccAddresses)

```

Parameters

```
   bccAddresses
```

Type: String[]

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`


Apex Reference Guide SingleEmailMessage Class

If the BCC compliance option is set at the organization level, the user cannot add BCC addresses on standard messages. The following
