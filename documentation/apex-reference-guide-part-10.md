`adjustmentValue` String Price value of the adjustment. 57.0

`baseAmount` String Total amount of the adjustment. 57.0

`cartId` String ID of the cart. 57.0

`id` String ID of the cart adjustment group. 57.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`priceAdjustment` String ID of the related promotion. 57.0

```
   CauseId

```

`priority` Integer Where in the sequence of adjustments this 57.0
adjustment was applied.

SEE ALSO:

#### ConnectApi.PromotionCart

ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionCartDeliveryMethodAdjustment

Adjustment for a cart delivery method in a promotion.

**Property Name** **Type** **Description** **Available Version**

`adjustmentType` String Type of price adjustment. Valid values are: 60.0

**•** `AdjustmentAmount` —The adjustment is a
fixed amount.

**•** `AdjustmentPercentage` —The adjustment
is a percentage.

`adjustmentValue` String Price value of the adjustment. 60.0

`baseAmount` String Price value of the adjustment. 60.0

`priceAdjustment` String ID of the related promotion. 60.0

```
   CauseId

```

`priority` Integer Where in the sequence of adjustments this 60.0
adjustment was applied.

#### ConnectApi.PromotionCartItem

A cart item and its adjustments.

**Property Name** **Type** **Description** **Available Version**

`cartDelivery` String ID of the associated cart delivery group. 57.0

```
   GroupId

```

`cartId` String ID of the associated cart. 57.0

#### cartItemPrice <List ConnectApi.PromotionCartItemPriceAdjustment > List of price adjustments applied to the cart item. 57.0

```
   Adjustments

```

`id` String ID of the cart item. 57.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`itemDescription` String Description of the cart item. 57.0

`itemName` String Name of the cart item. 57.0

`listPrice` String Unit list price of the cart item. 57.0

`product2Id` String ID of the product. 57.0

`quantity` String Quantity of the cart item. 57.0

`salesPrice` String Unit sales price of the cart item. 57.0

`sku` String Stock keeping unit of the cart item. 57.0

`totalAdjustment` String Total adjustment amount for the cart item. 57.0

```
   BaseAmount

```

`totalLine` String Total amount for the cart item, based on sales price 57.0
`BaseAmount` and quantity, not including adjustments.

`totalList` String Total amount for the cart item, based on list price 57.0
`BaseAmount` and quantity, not including adjustments.

`totalNetAmount` String Total amount for the cart item, based on list price 57.0
and quantity, including adjustments.

#### type ConnectApi. Type of item in a cart. Values are: 57.0

```
             CartItemType
```

**•** `DeliveryCharge`

**•** `Product`

SEE ALSO:

#### ConnectApi.PromotionCart

ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionCartItemPriceAdjustment

Price adjustments applied to a cart item.

**Property Name** **Type** **Description** **Available Version**

#### ConnectApi. Scope of the price adjustment amount. Values are: 57.0

```
AdjustmentAmount
```

**•** `Total` —The adjustment scope is the total price.
```
Scope

```

#### adjustmentAmount ConnectApi. Scope of the price adjustment amount. Values are:

```
Scope AdjustmentAmount
```

**•** `Total` —The adjustment scope is the total price.

**•** `Unit` —The adjustment scope is the unit price.

**•** `UnproratedTotal` —The adjustment scope
is the unprorated total price.

`adjustmentBasis` String ID of the associated coupon, if applicable. 57.0

```
Reference

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`adjustment` String Description of the adjustment. 57.0

```
   Description

#### adjustmentTarget ConnectApi. Level of the promotion target. Values are: 57.0

   Type CartPromotionType
```

**•** `Cart` —The target is cart-level.

**•** `Item` —The target is item-level.

#### adjustmentType ConnectApi. How the price adjustment amount is calculated. 57.0

`AdjustmentType` Values are:

**•** `AdjustmentAmount` —The adjustment is a
fixed amount.

**•** `AdjustmentPercentage` —The adjustment
is a percentage.

`adjustmentValue` String Value of the price adjustment. 57.0

`baseAmount` String Total adjustment amount. 57.0

`cartAdjustment` String ID of the associated cart adjustment group. 57.0

```
   GroupId

```

`cartItemId` String ID of the associated cart item. 57.0

`id` String ID of the cart item price adjustment. 57.0

`priceAdjustment` String ID of the associated promotion. 57.0

```
   CauseId

```

`priority` Integer Where in the sequence of adjustments this 57.0
adjustment was applied.

SEE ALSO:

ConnectApi.PromotionCartItem

ConnectApi.PromotionCart

ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionCoupon

A coupon used in a promotion.

**Property Name** **Type** **Description** **Available Version**

`couponCode` String Coupon code. 57.0

`couponErrorCode` String Error code returned if the coupon is invalid. 57.0

`id` String ID of the coupon. 57.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isValidCoupon` Boolean Indicates whether the coupon is valid ( `true` ) or 57.0
invalid ( `false` ).

SEE ALSO:

#### ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionEvaluation

Results of a promotion evaluation.

**Property Name** **Type** **Description** **Available Version**

#### cart ConnectApi. Cart and its items. 57.0

```
             PromotionCart

#### coupons List< ConnectApi. Collection of coupon codes to enable promotions. A 57.0
```

`PromotionCoupon`            - customer can apply a maximum of two coupons.

SEE ALSO:

evaluate(salesTransaction)

#### ConnectApi.PurchaseQuantityRule

Rule that restricts the quantity of a product that can be purchased.

**Property Name** **Type** **Description** **Available Version**

`increment` String Increment value of the quantity that can be 52.0
purchased.

`maximum` String Maximum quantity that can be purchased. 52.0

`minimum` String Minimum quantity that can be purchased. 52.0

SEE ALSO:

ConnectApi.CartItemProduct

ConnectApi.ProductDetail

ConnectApi.ProductSummary

#### ConnectApi.QueryInfo

Query execution information.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`queryId` String

Unique identifier assigned to a search query to enable 65.0
tracking usage and analysis of user interactions with
search results.

```
sobjects

```

Map<String, Query execution information for the object. 64.0

#### `ConnectApi.`

`ObjectQueryInfo` 

#### status ConnectApi. Status on the object search such as error messages 64.0

`SearchStatus` and warnings.

#### ConnectApi.QuestionAndAnswersCapability

If a feed element has this capability, it has a question and comments on the feed element are answers to the question.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### bestAnswer ConnectApi. Comment selected as the best answer for the 32.0

`Comment` question.

#### bestAnswer ConnectApi. User who selected the best answer for the question. 32.0

```
SelectedBy UserSummary

```

`canCurrentUser` Boolean Indicates whether the context user can select or 32.0
`SelectOrRemove` remove a best answer ( `true` ) or not ( `false` ).

```
BestAnswer

```

`candidateAnswers` `ConnectApi.CandidateAnswersStatus` Status of candidate answers for the question. 41.0

#### escalatedCase ConnectApi. If a question post is escalated, this is the case to which 33.0

`Reference` it was escalated.

`questionTitle` String Title for the question. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.QuestionAndAnswersSuggestions

Question and answers suggestions.

**Property Name** **Type** **Description** **Available Version**

`articles` `List<ConnectApi.` List of articles. 32.0

```
           ArticleItem>

```

`questions` `List<ConnectApi.` List of questions. 32.0

```
           FeedElement>

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.QueryPath

Represents a query path.

**Property Name** **Type** **Description** **Available Version**

`fieldLabel` String Label of the field. 60.0

`fieldName` String Name of the field. 60.0

`objectLabel` String Label of the object. 60.0

`objectName` String Name of the object. 60.0

#### ConnectApi.QueryPathConfig

Represents a query path configuration.

**Property Name** **Type** **Description** **Available Version**

#### queryPath List< ConnectApi.QueryPath > Query path. 60.0 ConnectApi.QueryPathConfigList

Represents a list of query path configurations.

**Property Name** **Type** **Description** **Available Version**

#### queryPathConfig List< ConnectApi.QueryPathConfig > List of query path configurations. 60.0 ConnectApi.QuerySqlOutput

Represents the SQL query output.

**Property Name** **Type** **Description** **Available Version**

`dataRows` `ConnectApi.QuerySqlRowRepresentation` Data associated with the SQL. 62.0

`metadata` `ConnectApi.QuerySqlMetadataItem` Metadata associated with the SQL. 62.0

`returnedRows` Long Number of rows returned by the query. 62.0

`status` `ConnectApi.QuerySqlStatus` Metadata related to the status of an SQL query. 62.0

SEE ALSO:

querySql(input)

querySql(input, dataspace)

querySql(input, workloadName, dataspace)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.QuerySqlMetadataItem

Represents the metadata associated with an SQL query output.

**Property Name** **Type** **Description** **Available Version**

#### innerElement ConnectApi.QuerySqlMetadataItem Description of array fields. 62.0

`name` String Name of the field. 62.0

`nullable` Boolean Indicates if the field is nullable ( `true` ) or not 62.0
( `false` ).

`precision` Integer Precision for numeric fields. 62.0

`scale` Integer Scale for numeric fields. 62.0

`type` `TypeEnum` Type of the SQL parameter. 62.0

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

#### ConnectApi.QuerySqlPageOutput

Represents the rows output for an SQL query.

**Property Name** **Type** **Description** **Available Version**

`dataRows` `ConnectApi.QuerySqlRowRepresentation` Data associated with the SQL. 62.0

#### metadata ConnectApi.QuerySqlMetadataItem Metadata associated with the SQL. 62.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`returnedRows` Long Number of rows returned by the query. 62.0

SEE ALSO:

querySqlRows(queryId, offset, rowLimit)

querySqlRows(queryId, offset, rowLimit, omitSchema)

querySqlRows(queryId, offset, rowLimit, dataspace)

querySqlRows(queryId, offset, rowLimit, omitSchema, dataspace)

querySqlRows(queryId, offset, rowLimit, workloadName, dataspace)

querySqlRows(queryId, offset, rowLimit, omitSchema, workloadName, dataspace)

#### ConnectApi.QuerySqlRow

Represents data associated with the an SQL query output.

**Property Name** **Type** **Description** **Available Version**

`row` List< `Object`   - List of column values. 62.0

#### ConnectApi.QuerySqlStatus

Represents the status of an SQL query.

**Property Name** **Type** **Description** **Available Version**

`chunkCount` Long Number of chunks available for extraction. 62.0

`completionStatus` `QuerySqlStatusEnum` Completion status of the query. 62.0

**•** `Finished`

**•** `ResultsProduced`

**•** `Running`

**•** `Unspecified`

`expirationTime` String Time when the query expires. You can't make 62.0
requests to an expired query.

`progress` Double A number between 0 and 1 that indicates the current 62.0
progress of query.

**•** `0` : The query execution has not started.

**•** `1` : The query execution is complete and the
results are available for you to retrieve.

`queryId` String ID of the query for which status information is 62.0
returned.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`rowCount` Long Number of rows available for extraction. 62.0

SEE ALSO:

querySqlStatus(queryId)

querySqlStatus(queryId, waitTimeMs)

querySqlStatus(queryId, dataspace)

querySqlStatus(queryId, dataspace, waitTimeMs)

querySqlStatus(queryId, workloadName, dataspace)

querySqlStatus(queryId, workloadName, dataspace, waitTimeMs)

#### ConnectApi.QuoteError

Error representation.

**Property Name** **Type** **Description** **Available Version**

`code` String The error code. 66.0

`message` String Details of the error, if available. 66.0

#### ConnectApi.RangeFacetDisplayMetadataRepresentation

Display metadata representation for a range facet.

**Property Name** **Type** **Description** **Available Version**

`currencyInfo` Map<String, String> Map of currency information display metadata for 64.0
the range facet.

#### ConnectApi.RangeSearchFacet

Range facet with minimum and maximum values in product search results.

**Property Name** **Type** **Description** **Available Version**

`attributeType` String Type of search attribute for the refinement. Values 64.0
are:

**•** `Custom`

**•** `Standard`

**•** `PricebookEntry`

#### displayMetadata ConnectApi.RangeFacetDisplayMetadataRepresentation Metadata required for rendering the range facet. 64.0

on page 2552


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`displayName` String Display name of the facet. 64.0

`displayRank` String Display rank of the facet. Valid values are from 1 64.0
through 50.

`displayType` String Display type of the facet. Value is: 64.0

**•** `Range`

`facetType` String Type of the facet. Value is: 64.0

**•** `Range`

`max` String Maximum value of the facet found in the search 64.0
result.

`min` String Minimum value of the facet found in the search result. 64.0

`nameOrId` String Developer name of the attribute for the refinement. 64.0

#### ConnectApi.RankAverageDistanceOutputRepresentation

The results of calculating the average distances from sets of inventory locations to an order recipient.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`distanceUnit` String The specified unit of distance (miles or kilometers). 51.0

```
results

```

#### List< ConnectApi. The results of the shipping distance calculations. 51.0

```
AverageDistanceResult
```

`OutputRepresentation` 

#### ConnectApi.ReadBy

Information about who read the feed element and when.

**Property Name** **Type** **Description** **Available Version**

`lastReadDateByUser` Datetime When the user last read the feed element in ISO 8601 40.0
format.

#### user ConnectApi. Information about the user who read the feed 40.0

`UserSummary` element.

SEE ALSO:

#### ConnectApi.ReadByPage


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ReadByCapability

If a feed element has this capability, the context user can mark it as read.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isReadByMe` Boolean Specifies whether the feed element has been read 40.0
( `true` ) or not ( `false` ) by the context user.

`lastReadDateByMe` Datetime

Last date when the feed element was marked read 40.0
for the context user in ISO 8601 format. Otherwise,
`null` .

#### page ConnectApi. First page of information about who read the feed 40.0

`ReadByPage` element and when.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.ReadByPage

A collection of information about who read the feed element and when.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page. 40.0

`currentPageUrl` String Connect REST API URL identifying the current page. 40.0
The default is 25 items per page.

#### items List< ConnectApi. Collection of read-by information, including users 40.0

`ReadBy`          - and when they last read the feed element.

`nextPageToken` String Token identifying the next page, or `null` if there 40.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 40.0
`null` if there isn’t a next page.

`previousPageToken` String Reserved for future use. 40.0

`previousPageUrl` String Reserved for future use. 40.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`total` Integer Total number of users who read the feed element. 40.0

Note: This count appears in the UI under feed
posts in private and unlisted Chatter groups
as the “seen by” number, for example, “Seen
by 48.”

SEE ALSO:

ConnectApi.ReadByCapability

#### ConnectApi.RecRepresentation

Recommended action.

**Property Name** **Type** **Description** **Available Version**

`acceptanceLabel` String Text indicating user acceptance of the recommended 59.0
action.

```
actionInfo

```

`ConnectApi.ActionInfo` Name and parameters required for processing and 60.0
`OutputRepresentation` displaying the recommended action.
on page 2206

`businessObjectiveId` String 18-character business objective ID associated with 59.0
the recommended action.

`channelId` String Associated channel ID for the recommended action. 61.0

`createdDate` Datetime Creation date of the recommended action. 61.0

`description` String Description of the recommended action. 59.0

`domain` String Domain category of the recommended action (e.g., 59.0
"Product").

`externalName` String External identifier used for recommended action 60.0
tracking.

`externalState` String JSON string containing data required for executing 60.0
the recommended action.

`grouping` String Free-form categorization field to keep track of 62.0
additional groupings of the recommended actions.

`iconName` String SLDS icon name representing the recommended 60.0
action domain.

`id` String ID of the recommended action. 59.0

`imageId` String Content asset file ID for the recommended action 60.0
display image.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`lastModifiedDate` Datetime Date that the recommended action was last modified. 61.0

`name` String Display name of the recommended action. 59.0

```
output

```

`ConnectApi.ActionInfo` Stores the last executed snapshot of the 61.0
`OutputRepresentation` recommended action.
on page 2206

`rejectionLabel` String Text indicating user rejection of the recommended 59.0
action.

`score` Integer Impact score of the recommended action (value 60.0
between 0-100).

`secondaryState` String Optional state field for additional filtering of 62.0
recommended action states.

`state` String Primary state of the recommended action (e.g., 59.0
"ACTIVE", "INACTIVE", "ACCEPTED", "NOT_EXPIRING").

`tertiaryState` String Optional state field for additional filtering of 62.0
recommended action states.

#### ConnectApi.Recommendation

A Next Best Action recommendation object.

**Property Name** **Type** **Description** **Available Version**

`acceptanceLabel` String Text indicating user acceptance of the 45.0
recommendation.

`actionReference` String Reference to the action to perform, for example, 45.0
launching a flow.

`description` String Description of the recommendation. 45.0

`externalId` String

External ID of the recommendation. This ID doesn’t 46.0
need to be a Salesforce 18-character ID. For example,
it can be a product number from an external system.

`id` String ID of the recommendation. 45.0

#### image ConnectApi. Image to display. 45.0

```
          FileAsset

```

`name` String Name of the recommendation. 45.0

`rejectionLabel` String Text indicating user rejection of the recommendation. 45.0

`url` String URL to the recommendation. 45.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.RecencyCriteria

Represents recency criteria of the object data for a data graph.

**Property Name** **Type** **Description** **Available Version**

`fieldName` String API name of the field to which recency criteria is 59.0
applied.

`value` String Value of the recency criteria. 59.0

`valueType` String Type of value for the recency criteria. Valid values are 59.0
`time` and `record` .

`valueUnit` String

Unit of measure for the recency criteria. For a value 59.0
of type `time`, the valid value is `DAY` . For a value of
type `record`, the valid value is `RECORD` .

#### ConnectApi.RecommendationsOutputRepresentation

List of recommended actions.

**Property Name** **Type** **Description** **Available Version**

```
recommendations

```

#### List< ConnectApi.Rec List of recommended actions. 59.0

`Representation` on
page 2555>

#### ConnectApi.RecommendationAudience

A custom recommendation audience.

**Property Name** **Type** **Description** **Available Version**

`criteria` `ConnectApi.AudienceCriteria` The criteria for the custom recommendation audience 36.0
type.

`id` String 18-character ID of the custom recommendation 35.0
audience.

`memberCount` Integer 35.0 only
Important: This property is available only in
version 35.0. In version 36.0 and later, this
property is available in
ConnectApi.CustomListAudienceCriteria.

Number of members in the custom recommendation
audience.

#### members ConnectApi. 35.0 only

Important: This property is available only in
```
           UserReferencePage
```
version 35.0. In version 36.0 and later, this


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

property is available in
ConnectApi.CustomListAudienceCriteria.

Members of the custom recommendation audience.

`modifiedBy` `ConnectApi.User` User who last modified the custom recommendation 36.0
audience.

`modifiedDate` Datetime ISO 8601 format date string, for example, 36.0
2011-02-25T18:24:31.000Z.

`name` String Name of the custom recommendation audience. 35.0

`url` String URL to the custom recommendation audience. 35.0

SEE ALSO:

#### ConnectApi.RecommendationAudiencePage ConnectApi.RecommendationAudiencePage

A list of custom recommendation audiences.

**Property Name** **Type** **Description** **Available Version**

`audienceCount` Integer The total number of custom recommendation 35.0
audiences.

`currentPageUrl` String URL to the current page. 35.0

`nextPageUrl` String URL to the next page. 35.0

`previousPageUrl` String URL to the previous page. 35.0

```
recommendation

Audiences

```

#### List< ConnectApi. A list of custom recommendation audiences. 35.0

```
Recommendation
```

`Audience` 

#### ConnectApi.RecommendationCollection

A list of Chatter, custom, and static recommendations.

**Property Name** **Type** **Description** **Available Version**

```
recommendations

```

`List<ConnectApi.` Collection of Chatter, custom, and static 33.0
`Abstract` recommendations.

```
Recommendation>

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.RecommendationDefinition

Represents a custom recommendation definition.

**Property Name** **Type** **Description** **Available Version**

`actionUrl` String The URL for acting on this custom recommendation. 35.0

`actionUrlName` String The text label for the action URL in the user interface. 35.0

`explanation` String Explanation of the custom recommendation 35.0
definition.

`id` String 18-character ID of the custom recommendation 35.0
definition.

`name` String Name of the custom recommendation definition. 35.0
The name is displayed in Setup.

`photo` `ConnectApi.Photo` Photo of the custom recommendation definition. 35.0

`title` String Title of the custom recommendation definition. 35.0

`url` String URL to the Connect REST API resource for the custom 35.0
recommendation definition.

SEE ALSO:

#### ConnectApi.RecommendationDefinitionPage

ConnectApi.ScheduledRecommendation

#### ConnectApi.RecommendationDefinitionPage

A list of custom recommendation definitions.

**Property Name** **Type** **Description** **Available Version**

```
recommendation

Definitions

```

#### List< ConnectApi. A list of custom recommendation definitions. 35.0

```
Recommendation
```

`Definition` 

`url` String URL to the Connect REST API resource for the 35.0
recommendation definition collection.

#### ConnectApi.RecommendationExplanation

Explanation for a Chatter recommendation.

Subclass of ConnectApi.AbstractRecommendationExplanation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`detailsUrl` String URL to explanation details or `null` if the Chatter 32.0
recommendation doesn’t have a detailed explanation.

SEE ALSO:

ConnectApi.AbstractRecommendation

#### ConnectApi.RecommendationReaction

A reaction to a recommendation produced by a recommendation strategy

**Property Name** **Type** **Description** **Available Version**

`aiModel` String Reserved for future use. 47.0

`contextRecord` `ConnectApi.Reference` Reference to the context record. 45.0

#### createdBy ConnectApi. Reference to the reaction creator. 45.0

```
             Reference

```

`createdDate` Datetime Reaction creation date. 45.0

`externalId` String External target ID of the recommendation reacted 46.0
on. This ID doesn’t need to be a Salesforce

18-character ID. For example, it can be a product
number from an external system.

`id` String Reaction record ID. 45.0

#### onBehalfOf ConnectApi. Reference to the user or record that is indirectly 45.0

`Reference` reacting to the recommendation.

```
reactionType

```

#### ConnectApi. Type of reaction to a recommendation. Values are: 45.0

```
RecommendationReaction
```

**•** `Accepted`
```
Type
```

**•** `Rejected`

`recommendation` String Reserved for future use. 46.0

```
Mode

```

`recommendation` Double Reserved for future use. 46.0

```
Score

#### strategy ConnectApi. Strategy that recommended the target record. 45.0

          RecordSnapshot

#### targetAction ConnectApi. Target action that is recommended. 45.0

          RecordSnapshot

#### targetRecord ConnectApi. Reference to the target record. 45.0

          Reference

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`url` String URL to the recommendation reaction. 45.0

SEE ALSO:

#### ConnectApi.RecommendationReactions ConnectApi.RecommendationReactions

A list of recommendation reactions.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page of reactions in the collection. 45.0

`nextPageUrl` String URL to the next page of reactions in the collection. 45.0

```
reactions

```

#### List< ConnectApi. Collection of recommendation reactions. 45.0

```
Recommendation
```

`Reaction` 

#### ConnectApi.RecommendationsCapability

If a feed element has this capability, it has a recommendation.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

```
items

```

SEE ALSO:

#### List< ConnectApi. A list of recommendations. 32.0

```
Abstract
```

`Recommendation` 

ConnectApi.FeedElementCapabilities

#### ConnectApi.RecommendedObject

A recommended object, such as a custom or static recommendation.

Subclass of ConnectApi.Actor

**Property Name** **Type** **Description** **Available Version**

`idOrEnum` String ID of a recommendation definition for a custom 34.0
recommendation or the enum value `Today` for

static recommendations that don’t have an ID
(version 35.0 and later).


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`motif` `ConnectApi.Motif` Motif of the recommended object. 34.0

#### ConnectApi.RecordCapability

If a comment has this capability, it has a record attachment.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`recordId` String ID of the record. 42.0

`url` String URL to the record. 42.0

#### ConnectApi.RecordField

Generic record field containing a label and text value.

Subclass of ConnectApi.LabeledRecordField.

No additional properties.

SEE ALSO:

ConnectApi.CompoundRecordField

ConnectApi.OrderItemSummary

ConnectApi.OrderItemSummaryProduct

ConnectApi.OrderDeliveryGroupSummary

ConnectApi.OrderSummaryRepresentation

#### ConnectApi.RecordFieldValue

Field value.

**Property Name** **Type** **Description** **Available Version**

`displayValue` String Field display value. 63.0

`highlight` String Represents field highlighting in the results. 63.0

`value` Object Field raw value. 63.0

SEE ALSO:

ConnectApi.SearchResult

#### ConnectApi.RecordSnapshot

A record snapshot in a recommendation reaction.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the record. 45.0

`nameAtSnapshot` String Name of the record when the ID was recorded. 45.0

SEE ALSO:

ConnectApi.RecommendationReaction

#### ConnectApi.RecordSnapshotCapability

If a feed element has this capability, it contains all the snapshotted fields of a record for a single create record event.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### recordView ConnectApi. A record representation that includes metadata and 32.0

`RecordView` data so you can display the record easily.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.RecordSummary

Record summary.

Subclass of ConnectApi.AbstractRecordView.

**Property Name** **Type** **Description** **Available Version**

`entityLabel` `ConnectApi.EntityLabel` Label of the record’s entity. 40.0

SEE ALSO:

ConnectApi.EmailAddress

ConnectApi.EmailAttachment

ConnectApi.ReferenceRecordField

ConnectApi.ReferenceWithDateRecordField

#### ConnectApi.RecordSummaryList

Summary information about a list of records in the organization including custom objects.

**Name** **Type** **Description** **Available**
**Version**

`records` `List<ConnectApi.ActorWithId>` A list of records. 30.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`url` String The URL to this list of records. 30.0

#### ConnectApi.RecordView

A view of any record in the org, including a custom object record. This object is used if a specialized object, such as User or ChatterGroup,
isn’t available for the record type.

Subclass of ConnectApi.AbstractRecordView.

**Name** **Type** **Description** **Available**
**Version**

`sections` `List<ConnectApi.` List of record view sections. 29.0

```
            RecordViewSection>

```

SEE ALSO:

ConnectApi.RecordSnapshotCapability

#### ConnectApi.RecordViewSection

Section of record fields and values on a record detail.

**Name** **Type** **Description** **Available**
**Version**

`columnCount` Integer Number of columns to use to lay out the fields in a record 29.0
section.

```
columnOrder

fields

```

#### ConnectApi. Order of the fields to use in the fields property to lay out 29.0

`RecordColumnOrder` the fields in a record section.
Enum

**•** `LeftRight` —Fields are rendered from left to right.

**•** `TopDown` —Fields are rendered from the top down.

#### ConnectApi. Fields and values for the record contained in this section. 29.0

```
Abstract

RecordField

```

`heading` String Localized label to display when rendering this section of fields. 29.0

`isCollapsible` Boolean Indicates whether the section can be collapsed to hide all the 29.0
fields ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.RecordView


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.RecordsetFilterCriteria

Recordset filter criteria and the filtered records.

**Property Name** **Type** **Description** **Available Version**

`criteriaId` String Recordset filter criteria ID. 53.0

`recordIds` List<String> List of filtered record IDs. 53.0

SEE ALSO:

#### ConnectApi.RecordsetFilterCriteriaCollection ConnectApi.RecordsetFilterCriteriaCollection

List of the recordset filters and records.

**Property Name** **Type** **Description** **Available Version**

#### recordsetFilters List< ConnectApi. Collection of recordset filter criteria IDs and filtered 53.0

`RecordsetFilterCriteria`                  - record IDs.

SEE ALSO:

evaluateRecordsetFilterCriteria(recordsetFilterCriteriaInput)

#### ConnectApi.Reference

Reference to a record.

**Name** **Type** **Description** **Available Version**

`id` String The ID of the record being referenced, which could be an 18-character 28.0
ID or some other string identifier.

`url` String The URL to the resource endpoint. 28.0

#### ConnectApi.ReferenceRecordField

Record field with a label and text value.

Subclass of ConnectApi.LabeledRecordField.

**Name** **Type** **Description** **Available Version**

#### reference ConnectApi. Object referenced by the record field. 29.0

```
            RecordSummary

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ReferencedRefundResponse

Refund comprehensive output.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error response representation for the refund. 50.0

```
             ErrorResponse

#### gatewayResponse ConnectApi. Gateway response received for the processed refund 50.0
```

`RefundGatewayResponse` request.

#### paymentGatewayLogs List< ConnectApi. Gateway log collection representation for the refund. 50.0

`GatewayLogResponse`              
#### paymentGroup ConnectApi. Payment group associated with the refund. 50.0

```
             PaymentGroupResponse

#### refund ConnectApi. Refund response representation. 50.0

             RefundResponse

#### ConnectApi.ReferenceWithDateRecordField

```

Record field containing a referenced object that acted at a specific time, for example, “Created By...”.

Subclass of ConnectApi.LabeledRecordField.

**Name** **Type** **Description** **Available Version**

`dateValue` Datetime Time at which the referenced object acted. 29.0

#### reference ConnectApi. Object referenced by the record field. 29.0

```
            RecordSummary

#### ConnectApi.RefundGatewayResponse

```

Refund gateway response.

Subclass of ConnectApi.AbstractGatewayResponse.

No additional properties.

#### ConnectApi.RefundInstructionsHintOutputRepresentation

Instructions showing the sequence in which credits and refunds were issued to the customer.

**Property Name** **Type** **Description** **Available Version**

`paymentCreditSequence` <List `ConnectApi.PaymentCreditSequenceItemOutputRepresentation` The representation of individual payment credit 65.0

           - items. Each item represents a specific payment

method and the amount of credit to be applied to
it.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### refundSequence <List ConnectApi.RefundSequenceItemOutputRepresentation > The order payment summary ID and value of the 65.0

processed refund items.

#### ConnectApi.RefundResponse

Refund output.

**Property Name** **Type** **Description** **Available Version**

`accountId` String ID of the account related to the refund record. 50.0

`amount` Double Total amount of the refund transaction performed in 50.0
the payment request.

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 50.0
the payment group record.

`effectiveDate` Datetime Date that the refund becomes effective. 50.0

`id` String ID of the refund record. 50.0

`refundNumber` String Number of the refund record that was created as a 50.0
result of the request processing.

`requestDate` Datetime Date when the refund occurred. 50.0

`status` String

Indicates the results of processing the refund 50.0
transaction in the gateway. Can be DRAFT,
PROCESSED or CANCELLED.

#### ConnectApi.RefundSequenceItemOutputRepresentation

The order payment summary ID and amount of the processed refund items.

**Property Name** **Type** **Description** **Available Version**

`amount` Double The amount that was refunded. 65.0

`orderPaymentSummaryId` String The order payment summary’s ID. 65.0

#### ConnectApi.RegisterGuestBuyerOutputRepresentation

Indicates success or failure of a register guest buyer action.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. Any errors that were returned. 48.0

`ErrorResponse`          


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`success` Boolean Indicates whether the transaction was successful. 48.0

#### ConnectApi.RelatedFeedPost

This class is abstract.

Subclass of ConnectApi.ActorWithId.

Superclass of: ConnectApi.RelatedQuestion.

**Property Name** **Type** **Description** **Available Version**

`score` Double Score of the related feed post that indicates how 37.0
closely related it is to the context feed post.

`title` String Title of the related feed post. 37.0

SEE ALSO:

#### ConnectApi.RelatedFeedPosts ConnectApi.RelatedFeedPosts

A collection of related feed posts.

**Property Name** **Type** **Description** **Available Version**

#### relatedFeedPosts List< ConnectApi. Collection of related feed posts. 37.0

`RelatedFeedPost`            
#### ConnectApi.RelatedQuestion

A related question.

Subclass of ConnectApi.RelatedFeedPost.

**Property Name** **Type** **Description** **Available Version**

`hasBestAnswer` Boolean Indicates whether the question has a best answer. 37.0

`interactions` `ConnectApi.InteractionsCapability` The number of individual views, likes, and comments 38.0
on a question.

#### ConnectApi.ReleaseHeldFOCapacityOutputRepresentation

Response to a request to confirm held fulfillment order capacity at one or more locations. Can correspond to one action call.

Subclass of ConnectApi.BaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
releaseHeldFO

CapacityResponses

```

#### List< ConnectApi. List of responses to the requests to confirm held 55.0

`ReleaseHeldFO` fulfillment order capacity at one or more locations.

```
CapacityResponse
```

`OutputRepresentation` 

#### ConnectApi.ReleaseHeldFOCapacityResponseOutputRepresentation

Response to a request to release held fulfillment order capacity at one or more locations.

**Property Name** **Type** **Description** **Available Version**

```
capacityResponses

```

#### List< ConnectApi. List of responses to the requests to release held 55.0

`CapacityResponse` fulfillment order capacity at individual locations.
`OutputRepresentation` 

#### ConnectApi.ReplyIntent

Reply intent for a social post.

**Property Name** **Type** **Description** **Available Version**

`managedSocialAccount` `ConnectApi.ManagedSocialAccount` Managed social account that replies to the social 45.0
post.

SEE ALSO:

#### ConnectApi.ReplyIntents ConnectApi.ReplyIntents

List of reply intents for a social post.

**Property Name** **Type** **Description** **Available Version**

#### replies List< ConnectApi.ReplyIntent > List of reply intents for the social post. 45.0

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.RepositoryFileDetail

A detailed description of a repository file.

Subclass of ConnectApi.AbstractRepositoryFile.

No additional properties.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.RepositoryFileSummary

A summary of a repository file.

Subclass of ConnectApi.AbstractRepositoryFile.

No additional properties.

SEE ALSO:

#### ConnectApi.RepositoryFolderItem ConnectApi.RepositoryFolderDetail

A detailed description of a repository folder.

Subclass of ConnectApi.AbstractRepositoryFolder.

No additional properties.

#### ConnectApi.RepositoryFolderItem

A folder item.

**Property Name** **Type** **Description** **Available Version**

```
file

folder

```

#### ConnectApi. If the folder item is a file, the file summary. If the folder 39.0

`Repository` item is a folder, `null` .

```
FileSummary

#### ConnectApi. If the folder item is a folder, the folder summary. If 39.0
```

`Repository` the folder item is a file, `null` .

```
FolderSummary

```

#### type ConnectApi. Type of item in a folder. Values are: 39.0

```
          FolderItemType
```

**•** `file`

**•** `folder`

SEE ALSO:

#### ConnectApi.RepositoryFolderItemsCollection ConnectApi.RepositoryFolderItemsCollection

A collection of repository folder items.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page of items. 39.0

```
items

```

#### List< ConnectApi. Collection of items in a repository folder. 39.0

```
Repository
```

`FolderItem` 


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`nextPageUrl` String URL to the next page of items, or `null` if there isn’t 39.0
a next page.

`previousPageUrl` String URL to the previous page of items, or `null` if there 39.0
isn’t a previous page.

#### ConnectApi.RepositoryFolderSummary

A summary of a repository folder.

Subclass of ConnectApi.AbstractRepositoryFolder.

No additional properties.

SEE ALSO:

ConnectApi.RepositoryFolderItem

#### ConnectApi.RepositoryGroupSummary

A group summary.

Subclass of ConnectApi.AbstractDirectoryEntrySummary.

**Property Name** **Type** **Description** **Available Version**

```
groupType

```

#### ConnectApi. Type of group. Values are: 39.0

```
ContentHub
```

**•** `Everybody` —Group is public to everybody.
```
GroupType

```

**•** `Everybody` —Group is public to everybody.

**•** `EverybodyInDomain` —Group is public to
everybody in the same domain.

**•** `Unknown` —Group type is unknown.

`name` String Name of the group. 39.0

SEE ALSO:

ConnectApi.ExternalFilePermissionInformation

#### ConnectApi.RepositoryUserSummary

A user summary.

Subclass of ConnectApi.AbstractDirectoryEntrySummary.

**Property Name** **Type** **Description** **Available Version**

`firstName` String First name of the user. 39.0

`lastName` String Last name of the user. 39.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.Reputation

Reputation for a user.

**Property Name** **Type** **Description** **Available Version**

#### reputationLevel ConnectApi. User’s reputation level. 32.0

```
             ReputationLevel

```

`reputationPoints` Double User's reputation points, which can be earned by 32.0
performing different activities.

`url` String Connect REST API URL to the reputation. 32.0

SEE ALSO:

ConnectApi.User

#### ConnectApi.ReputationLevel

Reputation level for a user.

**Property Name** **Type** **Description** **Available Version**

`levelImageUrl` String URL to the reputation level image. 32.0

`levelName` String Name of the reputation level. 32.0

`levelNumber` Integer

SEE ALSO:

#### ConnectApi.Reputation ConnectApi.RequestHeader

An HTTP request header name and value pair.

Reputation level number, which is the numerical rank 32.0
of the level, with the lowest level at 1. Administrators
define the reputation level point ranges.

**Property Name** **Type** **Description** **Available Version**

`name` String The name of the request header. 33.0

`value` String The value of the request header. 33.0

SEE ALSO:

ConnectApi.ActionLinkDefinition


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ResourceLinkSegment

Resource link segment.

**Name** **Type** **Description** **Available Version**

`url` String URL to a resource not otherwise identified by an ID field, for example, 28.0
a link to a list of users.

#### ConnectApi.ReturnItemsOutputRepresentation

Output of Return Items. Includes the ID of the generated change order for items and delivery charges being returned, as well as the ID
of the generated change order for any charged return fees. Also includes information about any ReturnOrderLineItems that were created
to represent remaining return quantities.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`changeOrderId` String ID of the change order created by processing the 52.0
ReturnOrderLineItems representing returned items

and delivery charges. Use this change order to create
a credit memo.

`feeChangeOrderId` String

`RefundInstructionsHint` String

ID of the change order created by processing the 56.0
ReturnOrderLineItems representing return fees. Use
this change order to create an invoice.

Stores a JSON representation of the payment credit 65.0
and refund sequences for ensure credit and ensure
refund.

#### returnLineItem List< ConnectApi. List of properties representing any remaining 52.0

`Splits` `ReturnOrderItem` quantities from partial returns processed by this call.
`SplitLine` It includes order items, delivery charges, and return
`OutputRepresentation`             - fees. Each element of the list includes the ID of a split
ReturnOrderLineItem and the ID of the partially
processed ReturnOrderLineItem whose remaining
quantity it holds.

SEE ALSO:

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderItemSplitLineOutputRepresentation

After a change order is created for a ReturnOrderLineItem, that ReturnOrderLineItem is read-only. If the Return Items API is used to return
a partial quantity, it creates a new “split” ReturnOrderLineItem to hold the remaining quantity to be returned. In that case, it returns this
output property, which contains the IDs of the original and split ReturnOrderLineItems.

Subclass of ConnectApi.BaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`newReturnOrderItemId` String ID of the new ReturnOrderLineItem that holds the 52.0
remaining return quantity.

`original` String ID of the original ReturnOrderLineItem. 52.0

```
   ReturnOrderItemId

```

SEE ALSO:

ConnectApi.ReturnItemsOutputRepresentation

returnItems(returnOrderId, returnItemsInput)

#### ConnectApi.ReturnOrderOutputRepresentation

ID of the created ReturnOrder.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`returnOrderId` String ID of the created ReturnOrder. 50.0

SEE ALSO:

createReturnOrder(returnOrderInput)

#### ConnectApi.RouteLocationOutputRepresentation

A fulfillment location within a route, including the products fulfilled from that location.

**Property Name** **Type** **Description** **Available Version**

`errors` List< `ConnectApi.ErrorResponse`   - Any errors that were returned. 67.0

`location` String The location's ID. 67.0

`products` <List `ConnectApi.RouteProductOutputRepresentation`   - Products fulfilled from this location. 67.0

`success` Boolean Indicates whether the request succeeded. 67.0

#### ConnectApi.RouteOutputRepresentation

A single possible fulfillment route, including its aggregated score and the locations that make up the route.

**Property Name** **Type** **Description** **Available Version**

`errors` List< `ConnectApi.ErrorResponse`   - Any errors that were returned. 67.0

#### locations <List ConnectApi.RouteLocationOutputRepresentation > The fulfillment locations that make up this route. 67.0

`success` Boolean Indicates whether the request succeeded. 67.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalScore` Double The aggregated score for this route. 67.0

#### ConnectApi.RouteProductOutputRepresentation

A product allocated to a fulfillment location within a route, including its allocated quantity and score.

**Property Name** **Type** **Description** **Available Version**

`errors` List< `ConnectApi.ErrorResponse`   - Any errors that were returned. 67.0

`product` String The product's SKU. 67.0

`quantity` Integer The product quantity allocated to this location. 67.0

`success` Boolean Indicates whether the request succeeded. 67.0

`unitScore` Double The score for this product at this location. 67.0

#### ConnectApi.SaleGatewayResponse

Sale gateway response.

Subclass of ConnectApi.AbstractGatewayResponse.

No additional properties.

#### ConnectApi.SaleResponse

Payment sale response.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error representation for the payment sale. 54.0

```
             ErrorResponse

#### gatewayResponse ConnectApi. Information from the payment gateway following 54.0
```

`SaleGatewayResponse` the sale request.

#### payment ConnectApi. Information about the payment used in the sale 54.0

`PaymentResponse` request.

#### paymentGateway List< ConnectApi. Collection of responses from the gateway following 54.0

`Logs` `GatewayLogResponse`   - the sale request.

#### paymentGroup ConnectApi. Payment group used in the sale request. 54.0

```
             PaymentGroupResponse

#### paymentMethod ConnectApi. Payment method used in the sale request. 54.0

             PaymentMethodResponse

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ScheduledRecommendation

Represents a scheduled custom recommendation.

**Property Name** **Type** **Description** **Available Version**

```
channel

```

#### ConnectApi. A way to tie custom recommendations together. For 36.0

`Recommendation` example, display recommendations in specific places
`Channel` in the UI or show recommendations based on time

of day or geographic locations. Values are:

**•** `CustomChannel1` —Custom
recommendation channel. Not used by default.
Work with your community manager to define
custom channels. For example, community
managers can use Experience Builder to
determine where recommendations appear.

**•** `CustomChannel2` —Custom
recommendation channel. Not used by default.
Work with your community manager to define
custom channels.

**•** `CustomChannel3` —Custom
recommendation channel. Not used by default.
Work with your community manager to define
custom channels.

**•** `CustomChannel4` —Custom
recommendation channel. Not used by default.
Work with your community manager to define
custom channels.

**•** `CustomChannel5` —Custom
recommendation channel. Not used by default.
Work with your community manager to define
custom channels.

**•** `DefaultChannel` —Default
recommendation channel. Recommendations
appear by default on the Home and Question
Detail pages of Customer Service and Partner
Central Experience Builder templates. They also
appear in the feed in the Salesforce mobile web
and anywhere community managers add
recommendations using Experience Builder.

`enabled` Boolean Indicates whether scheduling is enabled. If `true`, 35.0
the custom recommendation is enabled and appears

in Experience Cloud sites. If `false`, custom
recommendations in feeds in Salesforce mobile web
aren’t removed, but no new custom
recommendations appear. In Customer Service and


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

Partner Central sites, disabled custom
recommendations no longer appear.

`id` String 18-character ID of the scheduled custom 35.0
recommendation.

`rank` Integer The rank determining the order of this scheduled 35.0
custom recommendation.

`recommendation` String ID of the audience for the scheduled custom 35.0
`AudienceId` recommendation.

```
recommendation

Definition

Representation

```

#### ConnectApi. Custom recommendation definition that this 35.0

`Recommendation` scheduled recommendation schedules.

```
Definition

```

`url` String URL to the Connect REST API resource for the 35.0
scheduled custom recommendation.

SEE ALSO:

#### ConnectApi.ScheduledRecommendationPage ConnectApi.ScheduledRecommendationPage

A list of scheduled custom recommendations.

**Property Name** **Type** **Description** **Available Version**

```
scheduled

Recommendations

```

#### List< ConnectApi. A list of scheduled custom recommendations. 35.0

```
Scheduled
```

`Recommendation` 

`url` String URL to the Connect REST API resource for the 35.0
scheduled custom recommendation collection.

#### ConnectApi.Scope

Scope information for a target.

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the scope for the target. 48.0–49.0

`value` String Value of the scope for the target. 48.0–49.0

SEE ALSO:

ConnectApi.Target


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ScopedSearchResults

Keyword search results for an object.

**Property Name** **Type** **Description** **Available Version**

#### metadata ConnectApi. All search metadata associated with the object. 63.0

```
             ObjectMetadata

#### objectQueryInfo ConnectApi. Query execution information for the object. 64.0

             ObjectQueryInfo

```

`queryId` String

Unique identifier assigned to a search query to enable 65.0
tracking usage and analysis of user interactions with
search results.

#### results List< ConnectApi. Record results for the keyword search. 64.0

`SearchResult`          
#### searchObject ConnectApi. Record results for the keyword search. In version 64.0 63.0 only

`SearchObject` and later, use `results` for record results.

SEE ALSO:

find(objectApiName, request)

#### ConnectApi.SearchAnswer

Results of searching objects using a natural language query.

**Property Name** **Type** **Description** **Available Version**

`content` String AI generated response. 63.0

`llmGenerationId` String LLM generation ID used to track any feedback on the 63.0
conversation.

```
metadata

```

Map<String, All search related metadata associated with the 63.0
#### ConnectApi. objects found in the results.

`ObjectMetadata` 

#### searchObjects List< ConnectApi. Record results for the natural language search. 63.0

`SearchObject`          

SEE ALSO:

answer(q, objectApiName)

answer(q, objectApiName, displayFields)

answer(q)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.SearchCategory

Search category.

**Property Name** **Type** **Description** **Available Version**

#### category ConnectApi. Information about the category. 52.0

```
             ProductCategoryData

#### children List< ConnectApi. First-level child categories of the category searched 52.0
```

`SearchCategory`            - with non-empty search results.

`productCount` Long Number of products in the search results that belong 52.0
to the category.

SEE ALSO:

ConnectApi.ProductSearchResults

#### ConnectApi.SearchFacet

Search facet.

This class is abstract and is a superclass of ConnectApi.DistinctValueSearchFacet.

**Property Name** **Type** **Description** **Available Version**

```
attributeType

```

#### ConnectApi. Search attribute type. Values are: 52.0

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

`displayName` String Display name of the facet. 52.0

`displayRank` Integer Display rank of the facet. Valid values are from 1 52.0
through 50.

```
displayType

facetType

```

#### ConnectApi. Display type of the facet. Values are: 52.0

```
CommerceSearchFacet
```

**•** `CategoryTree`
```
DisplayType

```

#### ConnectApi. Search facet type. Value is: 52.0

```
CommerceSearch
```

**•** `DistinctValue`
```
FacetType

```

**•** `CategoryTree`

**•** `DatePicker`

**•** `MultiSelect`

**•** `SingleSelect`

**•** `DistinctValue`

**•** `Range`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`nameOrId` String Developer name of the attribute. In version 52.0 and 52.0
later, the ID of the attribute isn’t supported.

SEE ALSO:

ConnectApi.ProductSearchResults

#### ConnectApi.SearchObject

Record results for the keyword search.

**Property Name** **Type** **Description** **Available Version**

`displayFields` List<String> Fields to display from the response. 63.0

`objectApiName` String Object API name. 63.0

```
orderBy

```

#### List< ConnectApi. Applied order for object search. 63.0

```
SearchApplied
```

`OrderBy` 

#### pageInfo ConnectApi. Page position information for the object search. 63.0-64.0

```
          PageInfo

#### searchResults List< ConnectApi. Search results from the query. 63.0
```

`SearchResult`         

```
spellCorrectionInfo

```

#### ConnectApi. Spell correction information for the object search. 63.0

```
SpellCorrection

Info

```

#### status ConnectApi. Provides status on the object search such as error 63.0

`SearchStatus` messages and warnings.

SEE ALSO:

#### ConnectApi.SearchResultGroups

ConnectApi.SearchAnswer

ConnectApi.ScopedSearchResults

#### ConnectApi.SearchResult

Results from searching an object using keywords.

**Property Name** **Type** **Description** **Available Version**

`apiName` String Object API name. 64.0

#### chunks List< ConnectApi. Content chunks for the search result. 63.0

```
           Chunk

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
fields

```

Map<String, Field values by field API 63.0

#### `ConnectApi.`

`RecordFieldValue` 

`id` String ID of the record. 63.0

#### matchInfo ConnectApi. Search information related to the search result. 63.0

```
           MatchInfo

```

`sourceUrl` String Source URL from where the record originated. 64.0

SEE ALSO:

#### ConnectApi.SearchResultGroup

ConnectApi.ScopedSearchResults

ConnectApi.SearchObject

#### ConnectApi.SearchResultGroup

Search result group.

**Property Name** **Type** **Description** **Available Version**

`objectApiName` String Object API name. 64.0

```
results

```

SEE ALSO:

#### List< ConnectApi. List of search results. 64.0

`SearchResult` on
page 2580>

#### ConnectApi.SearchResultGroups ConnectApi.SearchResultGroups

Results of searching objects using keywords.

**Property Name** **Type** **Description** **Available Version**

```
metadata

```

Map<String, All related metadata associated with the objects 63.0
#### ConnectApi. found in the results.

`ObjectMetadata` 

#### queryInfo ConnectApi. Search query execution information. 64.0

```
          QueryInfo

#### resultGroups ConnectApi. Record results from a keyword search. 64.0

          SearchResultGroup

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### searchObjects List< ConnectApi.

`SearchObject`          

SEE ALSO:

findAndGroup(q)

findAndGroup(q, configurationName)

findAndGroup(q, configurationName, highlights)

#### ConnectApi.SearchStatus

Provides status on the object search.

Record results for the keyword search grouped by 63.0 only
object. In version 64.0 and later, use
`resultGroups` for record results.

**Property Name** **Type** **Description** **Available Version**

`code` String Search status code. 63.0

`message` String Search status message. 63.0

SEE ALSO:

ConnectApi.QueryInfo

ConnectApi.ObjectQueryInfo

ConnectApi.SearchObject

#### ConnectApi.SearchSuggestion

Search suggestion.

**Property Name** **Type** **Description** **Available Version**

`value` String Search suggestion. 52.0

SEE ALSO:

ConnectApi.ProductSearchSuggestionsResults

#### ConnectApi.ServiceAppointmentOutput

Output of the create service appointment request.

**Property Name** **Type** **Description** **Available Version**

`result` `ConnectApi.ServiceAppointmentResult` Result of the create or update service appointment 53.0
request.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ServiceAppointmentResult

Contains result of the service appointment.

**Property Name** **Type** **Description** **Available Version**

`assignedResourceIds` List<String> The IDs of the assigned resources. 53.0

`parentRecordId` String The ID of the parent record. 53.0

`serviceAppointmentId` String The ID of the service appointment record. 53.0

#### ConnectApi.ShiftsFromPattern

Shifts created from a pattern.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Total count of created shifts. 51.0

#### error ConnectApi.Shifts Error details for shifts from a pattern. 53.0

```
             FromPatternError

```

`isSuccess` Boolean Indicates if the request is successful ( `true` ) or not 53.0
( `false` ).

`recordIds` List<String> Collection of created shift IDs. 51.0

#### ConnectApi.ShiftsFromPatternError

Shifts from pattern error response.

**Property Name** **Type** **Description** **Available Version**

`code` String Error code. 53.0

`invalidService` String ID of invalid service resource. 53.0

```
   ResourceId

```

`message` String Error message. 53.0

#### ConnectApi.SiteSearchItem

Site search result item.

**Property Name** **Type** **Description** **Available Version**

`contentReference` String

Content reference field, which is the route developer 54.0
name for a site page or a content key for a content
detail page.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`contentType` String Developer name of the content type of the site search 54.0
`DeveloperName` result item.

`highlightedSnippet` String Text snippet that contains the query term. 54.0

`id` String ID of the site search result item. 54.0

#### pageType ConnectApi. Type of site search result item. Values are: 54.0

```
             SitesPageType
```

**•** `ContentPage`

**•** `SitePage`

`title` String Title of the site search result item. 54.0

SEE ALSO:

#### ConnectApi.SiteSearchResult ConnectApi.SiteSearchResult

Site search result.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token for the current page of search results. 54.0

`currentPageUrl` String URL to the current page of search results. 54.0

#### items List< ConnectApi. Collection of search result items. 54.0

`SiteSearchItem`            

`language` String Language of the search results. 54.0

`nextPageToken` String Token for the next page of search results. 54.0

`nextPageUrl` String URL to the next page of search results, or `null` if 54.0
there isn’t a next page.

`pageSize` Integer Number of items per page in search results. 54.0

`previousPageToken` String Token for the previous page of search results. 54.0

`previousPageUrl` String URL to the previous page of search results, or `null` 54.0
if there isn’t a previous page.

`totalItems` Integer Total number of items in the search results across all 54.0
pages.

#### ConnectApi.SocialStatusRepresentation

Status response for Webstore Meta Config entity creation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`error` `ConnectApi.ErrorResponse` Detailed error message if the operation was 64.0
unsuccessful.

`isSuccess` Boolean Specifies whether the operation was successful 64.0
( `true` ) or not ( `false` ).

#### ConnectApi.SortRule

Sort rule.

**Property Name** **Type** **Description** **Available Version**

```
direction

```

#### ConnectApi. Direction of the sort rule. Values are: 52.0

```
CommerceSearch
```

**•** `Ascending` —Sorts in ascending alphanumeric

`SortRuleDirection` order (A–Z, 0–9).

**•** `Default` —When no direction is defined, sorts
by relevance.

**•** `Descending` —Sorts in descending
alphanumeric order (Z–A, 9–0).

`label` String Label of the sort rule. 52.0

```
labelSuffix

```

#### ConnectApi. Label suffix of the sort rule.Values are: 54.0

```
CommerceSearch
```

**•** `Ascen` —Label suffix for 'Asc'
```
SortRuleLabelSuffix

```

**•** `Ascen` —Label suffix for 'Asc'

**•** `Ascending` —Label suffix for 'Ascending'

**•** `Az` —Label suffix for 'A-Z'

**•** `Descen` —Label suffix for 'Desc'

**•** `Descending` —Label suffix for 'Descending'

**•** `FewMany` —Label suffix for 'Few-Many'

**•** `HeavyLight` —Label suffix for 'Heavy-Light'

**•** `HighLow` —Label suffix for 'High-Low'

**•** `HighestLowest` —Label suffix for
'Highest-Lowest'

**•** `LightHeavy` —Label suffix for 'Light-Heavy'

**•** `LowHigh` —Label suffix for 'Low-High'

**•** `LowestHighest` —Label suffix for
'Lowest-Highest'

**•** `ManyFew` —Label suffix for 'Many-Few'

**•** `NewOld` —Label suffix for 'New-Old'

**•** `Newest` —Label suffix for 'Newest'

**•** `NewestOldest` —Label suffix for
'Newest-Oldest'

**•** `NineZero` —Label suffix for '9-0'


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `OldNew` —Label suffix for 'Old-New'

**•** `Oldest` —Label suffix for 'Oldest'

**•** `OldestNewest` —Label suffix for
'Oldest-Newest'

**•** `PriceDecreasing` —Label suffix for '$$-$'

**•** `PriceIncreasing` —Label suffix for '$-$$'

**•** `ThickThin` —Label suffix for 'Thick-Thin'

**•** `ThinThick` —Label suffix for 'Thin-Thick'

**•** `Za` —Label suffix for 'Z-A'

**•** `ZeroNine` —Label suffix for '0-9'

`nameOrId` String Name of the sort rule field or, if the sort rule is based 52.0
on a custom field, ID.

`sortOrder` Integer

Sort order for the rule. A lower number has higher 54.0
precedence. The first sort option is called when no
other option is selected.

`sortRuleId` String ID of the sort rule. 52.0

```
type

```

SEE ALSO:

#### ConnectApi. Type of sort rule. Values are: 52.0

```
CommerceSearch
```

**•** `ProductAttributeBased` —Sorts by

`SortRuleType` product attribute fields.

**•** `ProductBased` —Sorts by product field data.

**•** `Relevancy` —Sorts by product and catalog
term frequency.

**•** `SortByPricebook` —Sorts by product prices
defined in the specified pricebook (version 55.0
and later).

#### ConnectApi.SortRulesCollection ConnectApi.SortRulesCollection

Collection of sort rules.

**Property Name** **Type** **Description** **Available Version**

#### sortRules List< ConnectApi. Collection of sort rules. 52.0

`SortRule`          


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.SpellCorrectionInfo

Spell correction information for object search.

**Property Name** **Type** **Description** **Available Version**

`correctedQuery` String Specifies corrected query. 63.0

`hasNonCorrected` Boolean Specifies whether some non-corrected results were 63.0
`Results` returned ( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.ObjectQueryInfo

ConnectApi.SearchObject

#### ConnectApi.Stamp

A user stamp.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the stamp. 39.0–43.0

`id` String ID of the stamp. 39.0–43.0

`imageUrl` String Image URL of the stamp. 39.0–43.0

`label` String Label of the stamp. 39.0–43.0

SEE ALSO:

ConnectApi.User

#### ConnectApi.StaticData

Represents the static data output.

**Property Name** **Type** **Description** **Available Version**

`value` String Column value of the static data. 60.0

#### ConnectApi.StaticDataConfig

Represents the static attributes configuration output.

**Property Name** **Type** **Description** **Available Version**

#### staticDataList List< ConnectApi.StaticData > List of activation static attributes. 60.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.StatusCapability

If a feed post or comment has this capability, it has a status that determines its visibility.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### feedEntityStatus ConnectApi. Status of the feed post or comment. Values are: 37.0

```
             FeedEntityStatus
```

**•** `Draft` —The feed post isn’t published but is
visible to the author and users with Modify All
Data or View All Data permission. Comments
can’t be drafts.

**•** `Isolated` —The feed post or comment is
isolated, and only admins can see it.

**•** `PendingReview` —The feed post or comment
isn’t approved yet and therefore isn’t published
or visible.

**•** `Published` —The feed post or comment is
approved and visible.

`isApprovableByMe` Boolean Specifies whether the context user can change the 37.0
status of the feed post or comment.

SEE ALSO:

ConnectApi.CommentCapabilities

ConnectApi.FeedElementCapabilities

#### ConnectApi.StrategyTrace

Messages and trace nodes for a recommendation strategy execution.

**Property Name** **Type** **Description** **Available Version**

`messages` List<String> Messages and errors from the strategy execution. 45.0

#### nodes List< ConnectApi. Nodes of the strategy execution used for debugging. 45.0

`StrategyTraceNode`              

SEE ALSO:

ConnectApi.NBARecommendations

#### ConnectApi.StrategyTraceNode

A trace node for a recommendation strategy execution.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`inputCount` Integer Number of items put into the node. 45.0

`messages` List<String> Messages that occurred during node execution. 45.0

`nodeName` String Name of the node. 45.0

`nodeTime` Long Time spent processing inside the node. 45.0

`nodeType` String Type of node. 45.0

`outputCount` Integer Number of items returned from the node. 45.0

`outputs` List<String> Recommendations that are returned from the node. 45.0

`totalTime` Long Total time spent processing. 45.0

SEE ALSO:

ConnectApi.StrategyTrace

#### ConnectApi.SubmitCancelOutputRepresentation

ID of the change order created for a cancel action, and a set of its financial values.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. Financial values resulting from the cancel. 48.0

```
ChangeItem

OutputRepresentation

```

`changeOrderId` String

`feeChangeOrderId` String

ID of the change order created for the canceled order 48.0
items and shipping charges. Use this change order
to create a credit memo.

ID of the change order created by canceling order 57.0
items with associated cancel fees. Use this change
order to create an invoice.

#### ConnectApi.SubmitCartToExchangeOrderOutputRepresentation

Exhange order summary resulting from a submit cart to exchange order action.

**Property Name** **Type** **Description** **Available Version**

`balanceStateExchangeWebCart` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the exchange web cart. Big, 61.0

```
           on page 2235

```

`balanceStateOriginalOrderSummary` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the original order Big, 61.0
`on page 2235` summary.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`balanceStateReturnOrder` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the return order. Big, 61.0

```
              on page 2235

```

`changeBalances` `ConnectApi.ChangeItemOutputRepresentation` Change order financial values for a preview order Big, 60.0
`on page 2289` action.

#### errors List< ConnectApi. Any errors that were returned. Big, 60.0

`ErrorResponse`            

`exchangeOrderSummaryId` String Exchange order summary ID. Big, 60.0

`orderSummaryId` String ID of the order summary. Big, 60.0

`success` Boolean Indicates whether the transaction was successful. Big, 60.0

#### ConnectApi.SubmitChangeOrderSummaryOutputRepresentation

ID of the change order created for a submit change order summary action, and a set of its financial values.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. The financial values for the change Order Summary 66.0

`ChangeItem` action.

```
OutputRepresentation

```

`orderSummaryId` String The ID of the OrderSummary. 66.0

`preFulfillmentChangeOrderId` String The pre fulfillment change order ID that holds the 66.0
financial changes applicable to the modified order.

When the change is non-financial, this value is always
null. Use this change order to create a credit memo.

#### ConnectApi.SubmitReturnOutputRepresentation

ID of the change order created for a return action, and a set of its financial values.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. Financial values resulting from the return. 48.0

```
ChangeItem

OutputRepresentation

```

`changeOrderId` String

ID of the change order created for the returned order 48.0
items and shipping charges. Use this change order
to create a credit memo.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`feeChangeOrderId` String

#### ConnectApi.Subscription

Subscription.

ID of the change order created by returning order 57.0
items with associated return fees. Use this change
order to create an invoice.

**Name** **Type** **Description** **Available Version**

`community` `ConnectApi.Reference` Information about the Experience Cloud site in 28.0
which the subscription exists.

`id` String Subscription’s 18–character ID. 28.0

`subject` `ConnectApi.Actor` Information about the parent, that is, the thing 28.0
or person being followed.

`subscriber` `ConnectApi.Actor` Information about the subscriber, that is, the 28.0
person following this item.

`url` String Connect REST API URL to this specific 28.0
subscription.

SEE ALSO:

ConnectApi.FollowerPage

ConnectApi.FollowingPage

#### ConnectApi.SubscriptionTermRule

Subscription term rules.

**Property Name** **Type** **Description** **Available Version**

`increment` Integer Number of pricing term units that can be used to 59.0
increase the subscription term.

`maximum` Integer Maximum number of pricing term units per 59.0
subscription term.

`minimum` Integer Minimum number of pricing term units per 59.0
subscription term.

#### ConnectApi.SupportedEmojis

A collection of supported emoji.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`supportedEmojis` `ConnectApi.EmojiCollection` A collection of supported emoji. 39.0

#### ConnectApi.SurveyInvitationEmailOutput

Survey invitation email.

**Property Name** **Type** **Description** **Available Version**

`errorCode` Integer Error code for the failed call. 50.0

`errorMessage` String Details explaining why the call failed. 50.0

```
status

```

#### ConnectApi. Status of a survey invitation email. Values are: 50.0

```
SurveyEmailStatus
```

**•** `Failed` —The survey invitation email wasn't

`Enum` sent.

**•** `Queued` —The survey invitation email is queued
for sending.

#### ConnectApi.Target

Personalization target information.

**Property Name** **Type** **Description** **Available Version**

#### audience ConnectApi. Audience assigned to the target. 48.0

```
           AudienceTarget

#### formulaScope ConnectApi. Formula scope of the target. 50.0

           FormulaScope

```

`groupName` String Group name of the target. Groups bundle related 48.0
target and audience pairs.

`id` String ID of the target. 48.0

`priority` Integer

Priority of the target. Within a group, priority 48.0
determines which target is returned if the user
matches more than one audience.

#### publishStatus ConnectApi. Publish status of the target. Values are: 48.0

```
          PublishStatus
```

**•** `Draft`

#### scope List< ConnectApi.

`Scope`         

**•** `Live`

List of scopes for the target. 48.0–49.0

In version 50.0 and later, the `formulaScope`
property returns this information.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`targetType` String Type of target, indicating the nature of the data being 48.0
targeted.

`targetValue` String Value of the target. 48.0

`url` String URL to the target. 48.0

SEE ALSO:

#### ConnectApi.TargetCollection ConnectApi.TargetCollection

List of personalization targets.

**Property Name** **Type** **Description** **Available Version**

#### targets List< ConnectApi. List of personalization targets. 48.0

`Target`            
#### ConnectApi.TaxAddressesResponse

The Ship From, Ship To, and Sold To addresses used during tax calculation.

**Property Name** **Type** **Description** **Available Version**

```
shipFrom

shipTo

soldTo

```

#### ConnectApi. The Ship From address used in tax calculation. 55.0

```
TaxAddress

Response

#### ConnectApi. The Ship To address used in tax calculation. 55.0

TaxAddress

Response

#### ConnectApi. The Sold To address used in tax calculation. 55.0

TaxAddress

Response

```

#### ConnectApi.TaxAddressResponse

Location code of an address.

**Property Name** **Type** **Description** **Available Version**

`locationCode` String Location code of an address. 55.0


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`classifications` List<ConnectApi.ClassfcationsOutputRepresentation **i** - List of classifications that each text string was given **59.0**
after analysis.

`classificationsId` String Response ID to receive feedback for classification. **59.0**

#### ConnectApi.TextClassificationsResultWithIdOutputRepresentation

Classified text with status and text classification request IDs.


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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

URL to a topic’s cover image, which appears on the 32.0
topic page. Both topics and managed topics can have
cover images.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`featuredImageUrl` String

SEE ALSO:

#### ConnectApi.Topic ConnectApi.TopicPage

Page of topics.

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

#### ConnectApi.TopicsCapability

```

If a feed element has this capability, the context user can add topics to it. Topics help users organize and discover conversations.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`canAssignTopics` Boolean `true` if a topic can be assigned to the feed element, 32.0
`false` otherwise.

#### items List< ConnectApi. A collection of topics associated with this feed 32.0

`Topic`          - element.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.TopicSuggestion

Topic suggestion.

**Name** **Type** **Description** **Available**
**Version**

#### existingTopic ConnectApi.Topic Topic that already exists or null for a new topic 29.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`fieldName` String The name of the field that was updated. 28.0

`newValue` String The new value of the field or `null` if the field length is long. 28.0

`oldValue` String The old value of the field or `null` if the field length is long. 28.0

SEE ALSO:

#### ConnectApi.TrackedChangesCapability

ConnectApi.TrackedChangeBundleCapability

#### ConnectApi.TrackedChangesCapability

If a feed element has this capability, it contains all changes to a record for a single tracked change event.

Subclass of ConnectApi.FeedElementCapability.

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


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.UpdateQuoteOutput

Representation of the quote update response.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`errors` List< `[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)`   - Detailed error message if the update quote operation 67.0
was unsuccessful.

SEE ALSO:

updateQuote(webstoreId, quoteId, updateQuoteInput)

ConnectApi.updateQuoteInput

updateQuote(webstoreId, quoteId, updateQuoteInput)

ConnectApi.updateQuoteInput

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

`isChatterGuest` Boolean `true` if user is a Chatter customer; `false` otherwise. 28.0

`isInThisCommunity` Boolean `true` if user is in the same site as the context user; 28.0
`false` otherwise.

`lastName` String User's last name. In version 39.0 and later, if nicknames 28.0
are enabled, `lastName` is `null` .

`outOfOffice` `ConnectApi.OutOfOffice` If one exists, extra out-of-office message for the user. 40.0

`photo` `ConnectApi.Photo` Information about the user's photos. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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

`jobType` String Type of user activities job. Value is `export` or 42.0
`purge` .


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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

#### community ConnectApi. Experience Cloud site in which the user performed 42.0

`CommunitySummary` the activity.

SEE ALSO:

ConnectApi.UserActivityCollection


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.UserDetail

Details about a user in an org.

Subclass of ConnectApi.User.

If the context user doesn’t have permission to see a property, its value is set to `null` .

**Name** **Type** **Description** **Available**
**Version**

`aboutMe` String Text from user's profile. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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

This class is abstract.

Subclass of ConnectApi.UserActivitySummary.

Superclass of:

**•** ConnectApi.BookmarkSummary

**•** ConnectApi.ChatterActivitySummary

**•** ConnectApi.CompanyVerifySummary


Apex Reference Guide ConnectApi Output Classes

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

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 28.0
if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 28.0
`null` if there isn’t a previous page.

`total` Integer Total number of groups across all pages. 28.0


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`nextPageToken` Integer Token identifying the next page, or `null` if there isn’t a next 28.0
page.

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 28.0
there isn’t a next page.

`previousPageToken` Integer Token identifying the previous page, or `null` if there isn’t 28.0
a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 28.0
`null` if there isn’t a previous page.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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

**•** `CustomWeb` —Tab that displays data from
any external web-based application or web
page.

**•** `Element` —Tab that displays generic
content inline.

**•** `Feed` —Tab that displays the Chatter feed.

**•** `Overview` —Tab that displays user details.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Descriptio** **Available**
**Version**

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

`canFollow` Boolean User can follow users and records. 28.0

`canModify` Boolean User has Modify all Data permission. 28.0

```
   AllData

```

`canOwnGroups` Boolean User can own groups. 28.0

`canViewAllData` Boolean User has View all Data permission. 28.0

`canViewAllGroups` Boolean User has View all Groups permission. 28.0


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

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

`timeZone` `ConnectApi.` The user's time zone as selected in the user’s personal settings in Salesforce. 30.0
`TimeZone` This value does not reflect a device's current location.

`userDefault` String The ISO code for the default currency. Applicable only when the 28.0
`CurrencyIsoCode` `ConnectApi.Features.multiCurrency` property is `true` .

`userId` String 18-character ID of the user. 28.0


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

`userLocale` String Locale of user. 28.0

SEE ALSO:

ConnectApi.OrganizationSettings

#### ConnectApi.UserSummary

User summary.

Subclass of ConnectApi.User.

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


Apex Reference Guide ConnectApi Output Classes

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

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### votedItem ConnectApi. Reference to the feed element or comment that was 42.0

`Reference` voted on.

SEE ALSO:

#### ConnectApi.VotePage ConnectApi.VotePage

A page of upvotes or downvotes on a feed element or comment.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` Integer Token identifying the current page. 42.0

`currentPageUrl` String Connect REST API URL identifying the current page. 42.0

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.WishlistItemCollection ConnectApi.WishlistItemCollection

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

#### ConnectApi.Wishlist


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.WishlistsSummary

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

**Property Name** **Type** **Description** **Available Version**

`createdDate` Datetime Created date for the wishlist in ISO 8601 format, for 49.0
example, 2011-02-25T18:24:31.000Z.

`id` String ID of the wishlist. 49.0

`modifiedDate` Datetime Last modified date of the wishlist in ISO 8601 format, 49.0
for example, 2011-02-25T18:24:31.000Z.

`name` String Name of the wishlist. 49.0

`wishlistProductCount` Integer Unique product count in the wishlist. 49.0

SEE ALSO:

#### ConnectApi.Wishlist ConnectApi.WishlistsSummary ConnectApi.WishlistToCartResult

Result of adding a wishlist to a cart.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the cart to which the products were added. 49.0

#### failedWishlist List< ConnectApi. Wishlist items that weren’t successfully added to the 49.0

`ToCartItems` `CartItemResult`   - cart.

`productsFailed` Integer Total number of products that weren’t added to the 49.0
`Count` cart.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`productsRequested` Integer Total number of products requested to add to the 49.0
`Count` cart.

`productsSucceeded` Integer Total number of products that were successfully 49.0
`Count` added to the cart.

#### succeededWishlist List< ConnectApi. Wishlist items that were successfully added to the 49.0

`ToCartItems` `CartItemResult`   - cart.

#### ConnectApi.WorkStepPicklistValueAttribute

Work step picklist value attributes.

Subclass of ConnectApi.AbstractPicklistValueAttributes

[To use work step status picklist value attributes, you must have Field Service enabled in your org.](https://developer.salesforce.com/docs/atlas.en-us.262.0.field_service_dev.meta/field_service_dev/fsl_dev_set_up.htm)

**Property Name** **Type** **Description** **Available Version**

`sortOrder` Integer Order in which the work step statuses are displayed 66.0
in the status category’s picklist.

`statusCode` String Status category of the work step. 66.0

[For more information, see the WorkStepStatus object documentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_workstepstatus.htm)

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`name` String Name of the zone. 29.0

`url` String The URL of the zone. 30.0

`visibility` `ConnectApi.ZoneShowIn` Zone visibility type. 29.0

**•** `Community` —Available in an Experience
Cloud site.

**•** `Internal` —Available internally only.

**•** `Portal` —Available in a portal.

`visibilityId` String

SEE ALSO:

#### ConnectApi.ZonePage ConnectApi.ZonePage

Page of zones.

If the zone is available in a site, this property 29.0
contains the ID of the site. If the zone is available
to all sites, this property contains the value `All` .

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

`items` `List<ConnectApi.ZoneSearchResult` - List of search results. 29.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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

**•** `Question` —Search results contain only
questions.

`voteCount` String Number of votes given to the search result. 29.0

SEE ALSO:

ConnectApi.ZoneSearchPage

#### Retired ConnectApi Output Classes These ConnectApi output classes are retired.

IN THIS SECTION:

ConnectApi.ApprovalAttachment
Attach an approval to a feed item.

ConnectApi.BasicTemplateAttachment
Attachments in feed items with type `BasicTemplate` .

ConnectApi.CanvasTemplateAttachment
Attachments in feed items with type `CanvasPost` .

ConnectApi.CaseComment
Attachments in feed items with type `CaseCommentPost` .


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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

The postal address for the company. This is 32.0
typically a physical address that can include the
city, state, street, and postal code.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`annualRevenue` Double

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available**
**Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

##### ConnectApi.DatacloudContacts ConnectApi.DatacloudContacts

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

Number of contacts that are associated with this 32.0
order. Can be greater than the number of contacts
that are shown on a single page.


Apex Reference Guide ConnectApi Output Classes

##### ConnectApi.DatacloudOrder

Represents a Datacloud order.

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

`monthlyCreditsAvailable` Integer

The points or credits that have been used 32.0
from a pool of credits that are used by List
Pool Users to purchase records.

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

```
direction

```

`ConnectApi.Email` The direction of the email message. 29.0–31.0

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


Apex Reference Guide ConnectApi Output Classes

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

`updatesUrl` String A Connect REST API resource with a query string containing 30.0–31.0
the value of the `updatesToken` property. The resource

returns the feed items that have been updated since the last
request. Use the URL as it is—do not modify it. Property is
`null` if not available.

##### ConnectApi.FeedItemTopicPage

Feed item topic page.

Important: This class isn’t available in version 32.0 and later. In version 32.0 and later, ConnectApi.TopicsCapability is used.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`canAssignTopics` Boolean `true` if a topic can be assigned to the feed item, `false` 28.0–31.0
otherwise.

`topics` `List<ConnectApi.` List of topics. 28.0–31.0

```
            Topic>

##### ConnectApi.FeedPoll

```

Attachment of `ConnectApi.FeedItem` objects where the `type` property is `PollPost` .

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

**Name** **Type** **Description** **Available Version**

`title` String Title given to the link if available, otherwise, `null` . 28.0–31.0

`url` String The link URL. 28.0–31.0

##### ConnectApi.NonEntityRecommendation

A recommendation for a non-Salesforce entity, such as an application.

Subclass of ConnectApi.AbstractRecommendation.

##### Important: ConnectApi.NonEntityRecommendation isn’t used in version 34.0 and later. In version 34.0 and later,

ConnectApi.EntityRecommendation is used for all recommendations.


Apex Reference Guide ConnectApi Output Classes

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

`socialPersonaId` String ID of the social persona account, if the external social 39.0
account ID isn’t available.

SEE ALSO:

ConnectApi.SocialPostCapability

##### ConnectApi.SocialAccountRelationship

Follow relationship between a managed social account and a social persona.


Apex Reference Guide ConnectApi Output Classes

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

`author` `ConnectApi.SocialAccount` Social account that authored the social post. 36.0

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

**•** `PrivateMessage`

**•** `Reply`

**•** `Retweet`

**•** `Tweet`

`name` String Title or heading of the social post. 36.0

`postUrl` String External URL to the social post on the social network. 36.0

```
provider

```

##### ConnectApi. Social network that this social post belongs to. Values 36.0

`SocialNetwork` are:

```
Provider
```

**•** `Facebook`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`status` `ConnectApi.SocialPostStatus` Status of the social post. 36.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

##### ConnectApi.SocialPostIntents

Intents available for a social post.

**Property Name** **Type** **Description** **Available Version**

##### approvalIntent ConnectApi. Approval intent for the social post. 45.0

```
             ApprovalIntent

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

##### deleteIntent ConnectApi. Delete intents for the social post. 45.0

```
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

**•** `SfHttpRequestExtensionName`

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

**•** `ClientCredentials`

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

**•** `ServiceAgreement` —Service agreement maintenance.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Revised` —Content that’s published and edited. Publish this content to make the changes
available for use in your live sites.

`ConnectApi.ManagedTopic` Type of managed topic.

```
   Type
```

**•** `Content` —Topics that are associated with native content.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of message segment, such as text, link, field change name, or field change value.

```
   MessageSegmentType
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

`ConnectApi.` Type of named credential parameter.
`NamedCredential` **•**
```
ParameterType

```

**•** `AllowedManagedPackageNamespaces`

**•** `ClientCertificate`

**•** `ConnectionStatus`

**•** `SfHttpRequestExtensionName`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `ExternalLink` —URL outside of your site.

**•** `GlobalAction` —Lets users create records that aren’t related to other records.

**•** `InternalLink` —Relative URL inside your site.

**•** `MenuLabel` —Menu label.

**•** `Modal` —Modal, such as Account Switcher.

**•** `NavigationalTopic` —Dropdown list with links to the navigational topics in your site.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `ManagedContentVariantSetLockBackgroundStep`

**•** `ManagedContentVariantSetReadyBackgroundStep`

**•** `MuleSoftStep`

`ConnectApi.` Status of the orchestration work item.

```
   OrchestrationWorkItemStatus
```
**•** `Assigned`

**•** `Completed`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Twelve` —Refreshes every twelve hours.

**•** `TwentyFour` —Refreshes every twenty-four hours.

`ConnectApi.` Publish status of a personalization audience, target, or navigation menu item.

```
   PublishStatus
```

**•** `Draft`

**•** `Live`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `DefaultChannel` —Default recommendation channel. Recommendations appear by
default on the Home and Question Detail pages of Customer Service and Partner Central
Experience Builder templates. They also appear in the feed in the Salesforce mobile web
and anywhere community managers add recommendations using Experience Builder.

`ConnectApi.` Reason for a Chatter recommendation.

```
   RecommendationExplanationType
```
**•** `ArticleHasRelatedContent` —Articles with related content to a context article.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of reaction to a recommendation.

```
   RecommendationReactionType
```
**•** `Accepted`

**•** `Rejected`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

`ConnectApi.` Type of related feed post.

```
   RelatedFeedPostType
```

**•** `Answered` —Related questions that have at least one answer.

**•** `BestAnswer` —Related questions that have a best answer.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `SitePage`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Deleted`

**•** `Failed`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `Debit` —Transaction is a debit transaction.

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

**•** `DownVote` —User downvoted a post or comment.

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


### Apex Reference Guide ConnectApi Exceptions

**Enum** **Description**

**•** `CreatedDateDesc` —Sorts by most recent creation date.

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
Exceptions on page 3882.

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


### Apex Reference Guide ConnectApi Utilities ConnectApi Utilities The ConnectApi namespace contains a utility class.

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)_ : Using Batch

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


Apex Reference Guide Cursor Class

IN THIS SECTION:

##### fetch(position, count)

Fetches cursor rows that correspond to the offset position and the specified record count. The maximum number of rows per cursor
is 50 million, regardless of whether the operation is synchronous or asynchronous. Calling the `Cursor.fetch()` method counts
against the SOQL query limit, and the rows fetched count against the SOQL query row limit. You can make a maximum of 100
`Cursor.fetch()` calls per transaction.

##### getNumRecords()

Gets the number of rows returned in an Apex cursor from a `Cursor.fetch(position, count)` operation.

##### **`fetch(position, count)`**

Fetches cursor rows that correspond to the offset position and the specified record count. The maximum number of rows per cursor is
50 million, regardless of whether the operation is synchronous or asynchronous. Calling the `Cursor.fetch()` method counts
against the SOQL query limit, and the rows fetched count against the SOQL query row limit. You can make a maximum of 100
`Cursor.fetch()` calls per transaction.

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

Type: List on page 3992<sObject>

The list of sObjects from the SOQL query, starting from the specified position.

##### **`getNumRecords()`**

Gets the number of rows returned in an Apex cursor from a `Cursor.fetch(position, count)` operation.

Signature

```
   public static Integer getNumRecords()

```

Return Value

Type: Integer


### Apex Reference Guide CursorFetchResult Class CursorFetchResult Class

This class encapsulates the result of a `PaginationCursor.fetchPage()` call. It contains methods that get the rows for the
current page, the start index of the next page, and the number of deleted rows skipped during the fetch operation. It also contains a
method that indicates whether the pagination cursor has fetched all available rows in the result set.

Namespace

Database

IN THIS SECTION:

#### CursorFetchResult Methods CursorFetchResult Methods

### The following are methods for CursorFetchResult .

IN THIS SECTION:

##### getNextIndex()

Gets the start index required to fetch the next page of results. Use this value as the _`start`_ parameter in the call to
`PaginationCursor.fetchPage(start, pageSize)` to fetch the next page of results.

##### getNumDeletedRecords()

Gets the number of deleted rows that were skipped during the fetch operation.

getRecords()
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


### Apex Reference Guide DeletedRecord Class

Signature

```
   public Integer getNumDeletedRecords()

```

Return Value

Type: Integer

##### **`getRecords()`**

Gets the list of records that comprise the rows on the current page.

Signature

```
   public List<SObject> getRecords()

```

Return Value

Type: List on page 3992<sObject>

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cursors.htm)_ : Apex Cursors

### DeletedRecord Class

Contains information about a deleted record.

Namespace

Database


### Apex Reference Guide DeleteResult Class

Usage

The `getDeletedRecords` method of the `Database.GetDeletedResult` class returns a list of
`Database.DeletedRecord` objects. Use the methods in the `Database.DeletedRecord` class to retrieve details about
each deleted record.

#### DeletedRecord Methods The following are methods for DeletedRecord . All are instance methods.

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


Apex Reference Guide DeleteResult Class

Usage

An array of `Database.DeleteResult` objects is returned with the `delete` database method. Each element in the DeleteResult
array corresponds to the sObject array passed as the _`sObject[]`_ parameter in the `delete` Database method; that is, the first
element in the DeleteResult array matches the first element passed in the sObject array, the second element corresponds with the second
element, and so on. If only one sObject is passed in, the DeleteResult array contains a single element.

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

getErrors()
If an error occurred, returns an array of one or more database error objects providing the error code and description. If no error
occurred, returns an empty set.

getId()
Returns the ID of the sObject you were trying to delete.

isSuccess()
A Boolean value that is set to `true` if the DML operation was successful for this object, `false` otherwise.


### Apex Reference Guide DMLOptions Class

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


Apex Reference Guide DMLOptions Class

**DML Child Options**

DmlOptions.AssignmentRuleHeader—Enables setting assignment rule options.

DmlOptions.DuplicateRuleHeader—Determines options for using duplicate rules to detect duplicate records. Duplicate rules are
part of the Duplicate Management feature.

DmlOptions.EmailHeader—Enables setting email options.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_insert_3)_ : Database.insert()

_Apex Reference Guide_ [: SObject.setOptions()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject.htm#apex_System_SObject_setOptions)

#### DmlOptions Properties The following are properties for DmlOptions .

IN THIS SECTION:

##### allowFieldTruncation

Specifies the truncation behavior of large strings.

assignmentRuleHeader
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


Apex Reference Guide DMLOptions Class

##### assignmentRuleHeader

Specifies the assignment rule to be used when creating a case or lead.

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


### Apex Reference Guide DmlOptions.AssignmentRuleHeader Class

Property Value

Type: Database.DMLOptions.LocaleOptions

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


Apex Reference Guide DmlOptions.AssignmentRuleHeader Class

##### The following example uses the assignmentRuleID option:

```
   Database.DMLOptions dmo = new Database.DMLOptions();

   dmo.assignmentRuleHeader.assignmentRuleId= '01QD0000000EqAn';

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
Determine whether sharing rules for the current user are enforced when duplicate rules run ( `true` ) or not ( `false` ). If no sharing
rules are specified, Apex code runs in user mode and sharing rules for the current user are enforced.

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

Determine whether sharing rules for the current user are enforced when duplicate rules run ( `true` ) or not ( `false` ). If no sharing rules
are specified, Apex code runs in user mode and sharing rules for the current user are enforced.

Signature

```
   public Boolean runAsCurrentUser {get; set;}

```

Property Value

Type: Boolean

Usage

If specified as `true`, duplicate rules run for the current user, which ensures users can’t view duplicate records that aren’t available to
them.

##### Use runAsCurrentUser = true to detect duplicates when converting leads to contacts.

Example

This example shows how to set options so that duplicate rules run for the current user when saving a new account.

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.DuplicateRuleHeader.allowSave = true;

   dml.DuplicateRuleHeader.runAsCurrentUser = true;

   Account duplicateAccount = new Account(Name='dupe');

   Database.SaveResult sr = Database.insert(duplicateAccount, dml);

   if (sr.isSuccess()) {

```


### Apex Reference Guide DmlOptions.EmailHeader Class

```
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

IN THIS SECTION:

triggerAutoResponseEmail
Indicates whether to trigger auto-response rules ( `true` ) or not ( `false` ), for leads and cases.


Apex Reference Guide DmlOptions.EmailHeader Class

##### triggerOtherEmail

Indicates whether to trigger email outside the organization ( `true` ) or not ( `false` ).

##### triggerUserEmail

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

##### triggerUserEmail

Indicates whether to trigger email that is sent to users in the organization ( `true` ) or not ( `false` ).


### Apex Reference Guide DuplicateError Class

Signature

```
   public Boolean triggerUserEmail {get; set;}

```

Property Value

Type: Boolean

Usage

This email can be automatically triggered by a number of events; resetting a password, creating a new user, or creating or modifying a
task.

Note: Adding comments to a case in Apex doesn’t trigger email to users in the organization even if `triggerUserEmail` is
set to `true` .

Note: Email sent through Apex because of a group event includes additional behaviors. A _group event_ is an event for which
`IsGroupEvent` is true. The EventAttendee object tracks the users, leads, or contacts that are invited to a group event. Note
the following behaviors for group event email sent through Apex:

**•** Sending a group event invitation to a user respects the `triggerUserEmail` option

**•** Email sent when updating or deleting a group event also respects the `triggerUserEmail` and `triggerOtherEmail`
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

              duplicateResult.getDuplicateRule());

     System.debug(duplicateResult.getErrorMessage());

    }

```


Apex Reference Guide DuplicateError Class

```
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
2744 to check out the entire sample applicaton.

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

[Type: StatusCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

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

A pagination cursor is created when a SOQL query is executed on a `Database.getPaginationCursor()` on page 3745 or a
`Database.getPaginationCursorWithBinds()` on page 3745 call. When the SOQL query is invoked, the corresponding
rows are returned from the pagination cursor.

Use a pagination cursor for traversing human-viewable data, such as a list of records in a UI. The maximum number of rows per pagination
cursor is 100,000, regardless of whether the operation is synchronous or asynchronous.

[For a comparison between pagination cursors and standard cursors, see Apex Cursors in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cursors.htm) _Apex Developer Guide_ .

[For Apex pagination cursor limits, see Execution Governors and Limits in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm) _Apex Developer Guide_ .

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

Type: Database.CursorFetchResult on page 2696

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cursors.htm)_ : Apex Cursors

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

[Type: String](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm)

Usage

You can’t use the `[FOR UPDATE](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_locking_statements.htm)` keywords with a getQueryLocator query to lock a set of records. The set of records in the batch is
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
on page 2744 to check out the entire sample applicaton.

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
DuplicateResult Class on page 2744 to check out the entire sample applicaton.

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
on page 2744 to check out the entire sample applicaton.

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

**•** Each element contains an array of `DuplicateResult` on page 2744 objects, which each represent a duplicate rule that
`FindDuplicates` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2760 objects,
which each represent a matching rule that the duplicate rule applied. If `FindDuplicates` doesn’t find any duplicates for
that matching rule, then the `MatchResult.getMatchRecords()` on page 2761 array is empty. Otherwise, the
`MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2758 elements, which each represent a
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

**•** Each element contains an array of `DuplicateResult` on page 2744 objects, which each represent a duplicate rule that
`FindDuplicatesByIds` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2760
objects, which each represent a matching rule that the duplicate rule applied. If `FindDuplicatesByIds` doesn’t find any
duplicates for that matching rule, then the `MatchResult.getMatchRecords()` on page 2761 array is empty. Otherwise,
the `MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2758 objects, which each represent
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

[Engagement Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Engagement.htm)

[Engagements Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Engagements.htm)

[EngagementRecordDetails Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_EngagementRecordDetails.htm)

[EngagementRecordDetailsList Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_EngagementRecordDetailsList.htm)

[FieldDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_FieldDetailsRepresentation.htm)

[ObjectDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_ObjectDetailsRepresentation.htm)

[RecordDetailsRepresentation Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordDetailsRepresentation.htm)

[RecordTranscripts Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordTranscripts.htm)

[RecordTranscriptsList Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_RecordTranscriptsList.htm)


## Apex Reference Guide DataSource Namespace

[Transcript Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_class_DataRetrieval_Transcript.htm)

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

See Column Properties on page 2769 for information about each parameter.

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

See Column Properties on page 2769 for information about each parameter.

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

See Column Properties on page 2769 for information about each parameter.

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

See Column Properties on page 2769 for information about each parameter.

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

See Column Properties on page 2769 for information about each parameter.

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

If your extension of the `[DataSource.Provider](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_class_DataSource_Provider.htm)` class returns `[DataSource.AuthenticationCapability](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_enum_DataSource_AuthenticationCapability.htm)` values that
indicate support for authentication, the `[DataSource.Connection](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_class_DataSource_Connection.htm)` class is instantiated with a
`[DataSource.ConnectionParams](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_class_DataSource_ConnectionParams.htm)` instance in the constructor.

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

