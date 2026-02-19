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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**Property Name** **Type** **Description** **Available Version**

`batchSize` Integer Batch size 60.0

`data` List< `ConnectApi.ActivationData` - List of Audience DMO records. 60.0

`offset` Integer Start offset of the next batch. 60.0

SEE ALSO:

getActivationData(activationId)


Apex Reference Guide ConnectApi Output Classes

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

`targetType` String Type of target, indicating the nature of the data being 48.0
targeted.

`targetValue` String Value of the target. 48.0

`url` String URL to the target. 48.0

SEE ALSO:

#### ConnectApi.Audience


Apex Reference Guide ConnectApi Output Classes

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

paymentGateway

Logs

paymentGroup

paymentMethod

```

#### ConnectApi. Payment authorization representation. 51.0

```
Payment

AuthorizationResponse

#### List< ConnectApi. Gateway log list representation for the payment 51.0
```

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.BaseComparison

```

Represents the abstract class for a base comparison output.

**Property Name** **Type** **Description** **Available Version**

`filters` List< `ConnectApi.TypeAndFilter`   - List of logical comparison filters. 60.0

`operator` String operator 60.0

#### ConnectApi.BaseInvoiceOutputRepresentation

Base Order Management Invoice output class.

This class is abstract.

Subclass of ConnectApi.BaseOutputRepresentation.

Superclass of ConnectApi.ChangeOrdersInvoiceOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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

Example

#### The following example shows how to obtain and iterate through the returned ConnectApi.BatchResult objects. The code

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

#### `ConnectApi.BatchResult[] batchResults = ConnectApi.ChatterGroups.getGroupBatch(null,`

   myList);

   // Iterate through each returned result.

   for (ConnectApi.BatchResult batchResult : batchResults) {

      if (batchResult.isSuccess()) {

```


Apex Reference Guide ConnectApi Output Classes

```
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

getError()
If an error occurred, returns a `ConnectApi.ConnectApiException` object providing the error code and description.

getErrorMessage()
Returns a String that contains an error message.


Apex Reference Guide ConnectApi Output Classes

###### getErrorTypeName()

Returns a String that contains the name of the error type.

getResult()
Returns an object that contains the results of the batch operation. The object is typed according to the batch method. For example,
if you call `getMembershipBatch()`, a successful call to BatchResult `getResult()` returns a
`ConnectApi.GroupMembership` object.

isSuccess()
Returns a Boolean that is set to `true` if the batch operation was successful for this object, `false` otherwise.

###### getError()

If an error occurred, returns a `ConnectApi.ConnectApiException` object providing the error code and description.

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


Apex Reference Guide ConnectApi Output Classes

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

###### isSuccess()

Returns a Boolean that is set to `true` if the batch operation was successful for this object, `false` otherwise.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

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

`page 2205`            


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

#### ConnectApi.BundleCapability

If a feed element has this capability, it has a container of feed elements called a _bundle_ .

This class is abstract.

Subclass of ConnectApi.FeedElementCapability.

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


Apex Reference Guide ConnectApi Output Classes

Subclass of ConnectApi.CommerceResultRepresentationBase

**Property Name** **Type** **Description** **Available Version**

`data` ConnectApi.CartSummary A cart summary with calculated cart values. 62.0

#### ConnectApi.CalculateTaxResponse

Shows the results of a tax calculation request.

Subclass of ConnectApi.TaxTransactionResponse.

**Property Name** **Type** **Description** **Available Version**

#### adapterError ConnectApi. Adapter error. 55.0

```
             ErrorResponse

```

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`commentEndTime` Integer End time of the comment on the media player, in 51.0
seconds.

`commentStartTime` Integer Start time of the comment on the media player, in 51.0
seconds.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.CancelAllOrderItemsAsyncOutputRepresentation

ID of the asynchronous background operation.

Subclass of ConnectApi.BaseAsyncOutputRepresentation on page 2184.

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`developerName` String The API name (developer name) of the client app. 32.0

`height` String The height of the canvas app in pixels. 32.0

`icon` `ConnectApi.Icon` The icon for the canvas app. 32.0

`namespacePrefix` String A unique namespace prefix for the canvas app. 32.0

`parameters` String JSON parameters passed to the canvas app. 32.0

`thumbnailUrl` String A thumbnail URL to a preview image. The maximum 32.0
thumbnail size is 120 pixels by 120 pixels.

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.CardPaymentMethodOutput

```

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**Property Name** **Type** **Description** **Available Version**

#### coupons List< ConnectApi.CartCoupon > List of coupons associated with a cart. 54.0 ConnectApi.PromotionCartDeliveryGroupMethod

Cart delivery group method for a promotion.

**Property Name** **Type** **Description** **Available Version**

#### cartDelivery List< ConnectApi. List of cart delivery method adjustments. 60.0

```
   MethodAdjustments PromotionCart

             DeliveryMethod

             Adjustment on
```

`page 2483`            

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`cartDeliveryGroupId` String ID of the cart delivery group. 60.0

#### cartDelivery List< ConnectApi. List of methods for the delivery group. 60.0

```
   GroupMethods PromotionCart

             DeliveryGroupMethod
```

`on page 2200`            

`id` String ID of the cart. 60.0

#### ConnectApi.CartInventoryItemReservationOutputRepresentation (Pilot)

Inventory item reservation.

Note: This feature is not generally available and is being piloted with certain Customers subject to additional terms and conditions.
It is not part of your purchased Services. This feature is subject to change, may be discontinued with no notice at any time in
Salesforce’s sole discretion, and Salesforce may never make this feature generally available. Make your purchase decisions only on
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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Currency ISO code of the cart. 57.0

#### cartData ConnectApi. Collection of items in the cart. 64.0

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

#### productClass ConnectApi. Class of product. Values are: 62.0

```
          ProductClass
```

**•** `Bundle`

**•** `Set`

**•** `Simple`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

Unit price, including tier level discounts, for the item. 50.0
This value is informational only and isn’t used in
pricing calculations.

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

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CartItemBasicResult

Represents the result of a cart request.

**Property Name** **Type** **Description** **Available Version**

#### cartItem ConnectApi.CartItemBasic Item in a cart. 60.0

```
             on page 2203

```

`message` String Error message when the request is not successful. 60.0

`status` String Status of the request. 60.0

#### ConnectApi.CartItemCollection

A collection of items in a cart.

**Property Name** **Type** **Description** **Available Version**

`approaching` List<String> List of approaching discounts for the cart items. 64.0

```
   Discounts

#### cartCoupons ConnectApi. Collection of coupons in the cart. 59.0

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.CartItemProduct

```

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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

`CartMessage`          - list of messages related to the cart item. In

`ConnectApi.CartSummary`, each message
can be related to the cart or to another cart-related
entity.

`relatedEntityId` String In `ConnectApi.CartItemResult`, the ID of 49.0
the related cart item. In

`ConnectApi.CartSummary`, each message
can be related to the cart or to another cart-related
entity.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalLineItems` Integer In `ConnectApi.CartItemResult`, either 50.0
`WithErrors` `null` if the cart item has no errors or `1` if the cart
item has errors. In `ConnectApi.CartSummary`,
the total number of product line items that contain
errors.

SEE ALSO:

ConnectApi.AbstractCartItem

#### ConnectApi.CartMessagesVisibilityResult

Result of setting the visibility for cart messages.

**Property Name** **Type** **Description** **Available Version**

`visibility` Boolean Specifies whether cart messages are set to visible 50.0
( `true` ) or not ( `false` ).

#### ConnectApi.CartProductAttribute

Product attribute for a cart item.

**Property Name** **Type** **Description** **Available Version**

`label` String Label or display name of the attribute. 50.0

`sequence` Integer Sequence of the attribute within the attribute set. 50.0

`value` String Display value of the attribute. 50.0

SEE ALSO:

ConnectApi.CartItemProduct

#### ConnectApi.CartPromotionCollection

All the promotions associated with the cart.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the cart. 53.0

#### cartStatus ConnectApi. Status of the cart. Values are: 53.0

```
             CartStatus
```

**•** `Active—` Cart is created and available for
modifications, like adding or removing products
or promotions.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`currencyIsoCode` String Currency ISO code of the cart. 53.0

```
promotions

```

#### List< ConnectApi. Collection of promotions. 53.0

```
CartPromotion
```

`List` 

#### ConnectApi.CartPromotionList

A list of promotions for a cart.

**Property Name** **Type** **Description** **Available Version**

```
promotions

```

#### List< ConnectApi. Promotions associated with a cart. 54.0

```
CartPromotion
```

`OutputRepresentation` 

#### ConnectApi.CartPromotionOutputRepresentation

A promotion associated with a cart.

**Property Name** **Type** **Description** **Available Version**

`adjustmentAmount` String Adjustment amount out of the promotion. 53.0

`couponCode` String

Coupon code for a promotion. A coupon code is 54.0
available only for manual promotions, not for
automatic promotions.

`currencyIsoCode` String Currency ISO code associated with the cart. 57.0

`displayName` String Localized display name of the promotion. 52.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`promotionId` String ID of the promotion. 53.0

```
targetType

```

#### ConnectApi. Promotion target type. Values are: 53.0

```
CartPromotion
```

**•** `Cart` —Promotion targets a cart.
```
Type

```

**•** `Cart` —Promotion targets a cart.

**•** `Item` —Promotion targets an item in a cart.

`termsAndConditions` String Localized terms and conditions for the promotion. 53.0

#### ConnectApi.CartSummary

A cart summary.

**Property Name** **Type** **Description** **Available Version**

`accountId` String ID of the account for the cart. 49.0

`asyncOperation` String Asynchronous processing status of the cart, if 59.0
`Status` asynchronous processing is enabled for the store.
This property returns `Completed` in Apex, because
Apex operations always run synchronously.

`cartId` String ID of the cart. 49.0

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 49.0
the cart.

`customFields` List< `SObject` - Array of sObjects and viewable custom fields for the 61.0
[sObjects. Field-level security rules from the shopper](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)

[profile are applied to the custom fields. The rules are](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
applied for registered shoppers and for the guest
shopper profile. If no custom fields were specified,
returns an empty collection.

`firstPymtGrand` String

```
TotalAmount

```

First payment amount for subscription products, plus 60.0
the total payment amount for non-subscription
products. Includes taxes.

`firstPymt` String The total amount on the first payment of the cart. 63.0

```
TotalAmount

```

`firstPymt` String The total list price on the first payment of the cart. 63.0

```
TotalListPrice

```

`firstPymtTotal` String

```
TaxAmount

```

Tax amount on the first payment for any subscription 60.0
products, plus the total tax amount on
non-subscription products.

`grandTotalAmount` String Grand total amount including shipping and tax for 49.0
items in the cart, in the currency of the cart.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`hasGift` Boolean Specifies whether the cart contains a gift ( `true` ) or 64.0
not ( `false` ).

`isSecondary` Boolean Specifies whether the cart is secondary ( `true` ) or 53.0
not ( `false` ).

`name` String Name of the cart. 49.0

`ownerId` String ID of the owner of the cart. 49.0

`ownerOrderId` String ID of the owner of the order. 58.0

`purchaseOrder` String Purchase order for the cart. 50.0

```
   Number

```

`status` `ConnectApi.` Status of the cart. Values are: 49.0

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

`taxType` String Tax type of the cart. 55.0

**•** `Automatic` —Automatic taxation policy.

**•** `Gross` —Gross taxation policy.

**•** `Net` —Net taxation policy.

`totalAmount` String

```
WithItem

Adjustment

```

Total amount, including both tier and item level 61.0
discounts but excluding cart level discounts, for all
items in the cart.

`totalCartLevel` String Total cart level discount amount for the cart. 61.0

```
AdjustmentAmount

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalChargeAmount` String

Total amount for shipping and other charges in the 49.0
currency of the cart. Includes adjustments from
shipping promotions.

`totalListPrice` String Total list price for all cart items plus shipping 49.0
adjustments.

`totalProduct` String Total amount including discounts, but excluding 49.0
`Amount` shipping and tax, for product items in the cart.

`totalProductAmount` String Total product amount, including promotions. 52.0

```
AfterAdjustments

```

`totalProduct` String

```
Count

```

Total count of items in the cart. This field may not be 49.0
[accurate when faster add-to-cart is turned on and](https://help.salesforce.com/s/articleView?id=commerce.comm_faster_add_to_cart.htm&type=5&language=en_US)
quantity rules are enabled for products in the cart.

`totalProduct` Integer Total count of line items, of the type Product, in the 60.0
`LineItemCount` cart.

`totalProduct` String Total list price for all products in the cart without any 59.0
`ListAmount` adjustments.

`totalPromotional` String Total promotional adjustment amount for items in 52.0
`AdjustmentAmount` the cart.

`totalSubProduct` String Total quantity of all cart items with the selling model 60.0
`Count` type Evergreen or Term-Defined.

`totalTaxAmount` String Total tax amount for the cart, including tax on 49.0
shipping, if applicable.

`type` `ConnectApi.` Type of cart. Values are: 49.0

```
          CartType
```

**•** `Cart` —Cart created by a customer.

**•** `PayNowReadOnly` —Clone of a Template cart
that the customer can check out with using the
Pay Now feature.

**•** `Template` —Cart created by an internal user.

`uniqueProduct` Integer

```
Count

```

Total count of unique items, or SKUs, in the cart. This 49.0
[field is supported when faster add-to-cart is turned](https://help.salesforce.com/s/articleView?id=commerce.comm_faster_add_to_cart.htm&type=5&language=en_US)
off.

`webstoreId` String ID of the webstore of the cart. 49.0

SEE ALSO:

ConnectApi.CartItemCollection


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CartToWishlistResult

Result of copying products from a cart to a wishlist.

**Property Name** **Type** **Description** **Available Version**

`productsAddedCount` Integer Number of products copied from the cart to the 50.0
wishlist.

`wishlistId` String ID of the wishlist that cart products were copied to. 50.0

#### ConnectApi.CaseCommentCapability

If a feed element has this capability, it has a case comment on the case feed.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### actorType ConnectApi. Specifies the type of user who made the comment. 32.0

```
             CaseActorType

```

`createdBy` `ConnectApi.Actor` Information about the user who created the 32.0
comment.

`createdDate` Datetime ISO 8601 date string, for example, 32.0
2011-02-25T18:24:31.000Z.

```
eventType

```

#### ConnectApi. Specifies an event type for a comment in the case 32.0

`CaseComment` feed.

```
EventType

```

`id` String 18-character ID of case comment. 32.0

`published` Boolean Specifies whether the comment has been published. 32.0

`text` String Text of the case comment. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.CaseStatusPicklistValueAttributes

Case status picklist value attributes.

Subclass of ConnectApi.AbstractPicklistValueAttributes

**Property Name** **Type** **Description** **Available Version**

`closed` Boolean Specifies whether the case has a status of closed 66.0
( `true` ) or not ( `false` ).


Apex Reference Guide ConnectApi Output Classes

[For more information, see the CaseStatus object documentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_casestatus.htm)

#### ConnectApi.CdpActionResponse

Customer Data Platform action response.

This class is abstract.

Superclass of:

**•** ConnectApi.CdpCalculatedInsightStandardActionResponseRepresentation

**•** ConnectApi.CdpSegmentActionOutput in API version 59.0 and later.

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. List of errors that resulted from the action. 57.0

`CdpErrorResponse`             

`success` Boolean Indicates whether the call was successful ( `true` ) or 57.0
not ( `false` ).

#### ConnectApi.CdpAssetReference

Model asset reference used as part of the prediction request.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the asset. 58.0

`name` String Name of the asset. 58.0

`namespace` String Namespace of the asset. 58.0

#### ConnectApi.CdpCalculatedInsightDataSource

Calculated insight data source.

**Property Name** **Type** **Description** **Available Version**

`sourceApiName` String Data source API name. 57.0

`type` String Data source type. 57.0

SEE ALSO:

#### ConnectApi.CdpCalculatedInsightDimension

ConnectApi.CdpCalculatedInsightMeasure

#### ConnectApi.CdpCalculatedInsightDimension

Calculated insight dimension.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the dimension. 57.0

`creationType` String Creation type of the dimension. 57.0

```
dataSource

```

#### ConnectApi. Data source of the dimension. 57.0

```
CdpCalculated

InsightDataSource

```

`dataType` String Data type of the dimension. 57.0

`dateGranularity` String Date granularity of the dimension. 57.0

`displayName` String Display name of the dimension. 57.0

`fieldRole` String Field role of the dimension. 57.0

`formula` String Formula of the dimension. 57.0

SEE ALSO:

#### ConnectApi.CdpCalculatedInsightOutput ConnectApi.CdpCalculatedInsightMeasure

Calculated insight measure.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the measure. 57.0

`creationType` String Creation type of the measure. 57.0

```
dataSource

```

#### ConnectApi. Data source of the measure. 57.0

```
CdpCalculated

InsightDataSource

```

`dataType` String Data type of the measure. 57.0

`displayName` String Display name of the measure. 57.0

`fieldAggregationType` String Field aggregation type of the measure. 57.0

`fieldRole` String Field role of the measure. 57.0

`formula` String Formula of the measure. 57.0

SEE ALSO:

#### ConnectApi.CdpCalculatedInsightOutput ConnectApi.CdpCalculatedInsightOutput

Calculated insight.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the calculated insight. 57.0

`calculatedInsight` String Status of the calculated insight. 57.0

```
   Status

```

`creationType` String Creation type of the calculated insight. 57.0

`dataSpace` String Data space of the calculated insight. 57.0

`definitionStatus` String Definition status of the calculated insight. 57.0

`definitionType` String Definition type of the calculated insight. 57.0

`description` String Description of the calculated insight. 57.0

```
dimensions

```

#### List< ConnectApi. Dimensions of the calculated insight. 57.0

```
CdpCalculated
```

`InsightDimension` 

`displayName` String Display name of the calculated insight. 57.0

`expression` String Expression of the calculated insight. 57.0

`isEnabled` Boolean Specifies whether the calculated insight is enabled 57.0
( `true` ) or not ( `false` ).

`lastCalcInsight` String Last calculated insight status date and time. 57.0

```
StatusDateTime

```

`lastCalcInsight` String Last calculated insight status error code. 57.0

```
StatusErrorCode

```

`lastRunDateTime` String Last run date and time of the calculated insight. 57.0

`lastRunStatus` String Last run status of the calculated insight. 57.0

`lastRunStatus` String Last run status date and time of the calculated insight. 57.0

```
DateTime

```

`lastRunStatus` String Last run status error code of the calculated insight. 57.0

```
ErrorCode

```

```
measures

```

SEE ALSO:

#### List< ConnectApi. Measures of the calculated insight. 57.0

```
CdpCalculated
```

`InsightMeasure` 

#### ConnectApi.CdpCalculatedInsightPageData ConnectApi.CdpCalculatedInsightPage

Collection of calculated insights.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
collection

```

#### ConnectApi. Collection of calculated insights. 57.0

```
CdpCalculated

InsightPageData

```

#### ConnectApi.CdpCalculatedInsightPageData

Calculated insight collection data.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Number of results returned in the page. 57.0

`currentPageToken` String Token identifying the current page. 57.0

`currentPageUrl` String Connect REST API URL identifying the current page. 57.0

```
items

```

#### List< ConnectApi. List of calculated insights. 57.0

```
CdpCalculated
```

`InsightOutput` 

`nextPageToken` String Token identifying the next page, or `null` if there 57.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 57.0
`null` if there isn’t a next page.

`previousPageToken` String Token identifying the previous page, or `null` if 57.0
there isn’t a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 57.0
or `null` if there isn’t a previous page.

`total` Integer Total row count of calculated insights. 57.0

SEE ALSO:

#### ConnectApi.CdpCalculatedInsightPage ConnectApi.CdpCalculatedInsightStandardActionResponseRepresentation

Response of the calculated insight run action.

Subclass of ConnectApi.CdpActionResponse.

No additional properties.

#### ConnectApi.CdpDgMetadata

Represents metadata from one or more data graphs.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`dataGraphMetadata` <List `ConnectApi.CdpQueryDataGraphMetadata`    - List of metadata from data graphs. 59.0

SEE ALSO:

getDataGraphMetadata()

getDataGraphMetadata(dataGraphEntityName)

getDataGraphMetadata(dataGraphEntityName, dataspace)

#### ConnectApi.CdpErrorResponse

Error response.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code. 57.0

`message` String Message stating the reason for the error, if any. 57.0

SEE ALSO:

ConnectApi.CdpActionResponse

#### ConnectApi.CdpIdentityResolutionMatchCriterionOutput

Identity resolution ruleset's match rule criterion.

**Property Name** **Type** **Description** **Available Version**

`caseSensitiveMatch` Boolean

Specifies whether the criterion match is case sensitive 58.0
( `true` ) or not ( `false` ). Available only when
[matching is based on the party identifier.](https://help.salesforce.com/s/articleView?id=data.c360_a_match_rules.htm&type=5&language=en_US)

`entityName` String API name of the Data Model Object the match rule 57.0
applies to.

`fieldName` String Name of the field the criterion applies to. 57.0

```
matchMethodType

```

#### ConnectApi. Match method for a match rule criterion. Values are: 57.0

```
CdpIdentityResolution
```

**•** `Exact` —Exact match.
```
MatchMethodType

```

**•** `Exact` —Exact match.

**•** `ExactNormalized` —Exact normalized
match.

**•** `Fuzzy` —Fuzzy match with medium precision.

**•** `FuzzyHigh` —Fuzzy match with high precision.

**•** `FuzzyLow` —Fuzzy match with low precision.

#### partyIdentification ConnectApi. Party Identifier information. 57.0

```
Info CdpIdentityResolution

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
             MatchCriterionParty

             IdentificationInfoOutput

```

`shouldMatchOnBlank` Boolean Specifies whether blank fields can be used for 57.0
matching ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.CdpIdentityResolutionMatchRuleOutput ConnectApi.CdpIdentityResolutionMatchCriterionPartyIdentificationInfoOutput

Information when party identification is used in an identity resolution ruleset's match rule criterion.

**Property Name** **Type** **Description** **Available Version**

`partyName` String Party identification name. 57.0

`partyType` String Party identification type. 57.0

SEE ALSO:

ConnectApi.CdpIdentityResolutionMatchCriterionOutput

#### ConnectApi.CdpIdentityResolutionMatchRuleOutput

Identity resolution ruleset’s match rule.

**Property Name** **Type** **Description** **Available Version**

```
criteria

```

#### List< ConnectApi. Object and field the match rule applies to and the 57.0

`CdpIdentityResolution` match method applied.
`MatchCriterionOutput` 

`label` String User friendly name for the identity resolution match 57.0
rule.

SEE ALSO:

#### ConnectApi.CdpIdentityResolutionOutput ConnectApi.CdpIdentityResolutionOutput

Identity resolution ruleset.

**Property Name** **Type** **Description** **Available Version**

`anonymousUnified` Long Count of anonymous unified profiles created by 57.0
`Profiles` running the identity resolution ruleset.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
configurationType

```

`ConnectApi.` Source object for an identity resolution ruleset. Values 57.0
`CdpIdentityResolution` are:

```
ConfigurationType
```

**•** `Account`

**•** `Individual`

`consolidationRate` Double Consolidation rate resulting from the run of an 57.0
identity resolution ruleset.

`dataSpaceName` String Data space used as source data for an identity 57.0
resolution ruleset.

`description` String Description of the identity resolution ruleset. 57.0

`doesRun` Boolean

```
Automatically

```

Specifies whether automatic job run scheduling is 57.0
enabled for the ruleset ( `true` ) or not ( `false` ). If
unspecified, defaults to `false` .

`id` String Identity resolution ruleset's ID. This is not the identity 57.0
resolution's extended ruleset ID ( `rulesetId` ).

`knownUnified` Long Count of known unified profiles created by running 57.0
`Profiles` the identity resolution ruleset.

`label` String User friendly name of the identity resolution ruleset. 57.0

`lastJobCompleted` Datetime Date and time the last job completed. 57.0

`lastJobStatus` String Last job's status. Possible values are: 57.0

**•** `SUCCESS`

**•** `IN_PROGRESS`

**•** `FAIL`

**•** `SCHEDULED`

**•** `SKIPPED`

```
matchRules

```

List< `ConnectApi.` List of match rules. 57.0

```
CdpIdentityResolution
```

`MatchRuleOutput` 

`matchedSource` Long Count of matched source profiles identified by 57.0
`Profiles` running the identity resolution ruleset.

`objectApiName` String Object name of the identity resolution ruleset. 57.0

```
reconciliationRules

```

List< `ConnectApi.` List of reconciliation rules. 57.0

```
CdpIdentityResolution
```

`ReconciliationRuleOutput` 

`rulesetId` String

Extension ID of a ruleset. The ruleset ID must be 57.0
unique and no longer than 4 characters. This ID is not
the identifying ID for the ruleset.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`rulesetStatus` String Status of a ruleset job. Possible values are: 57.0

**•** `NEW`

**•** `PUBLISHING`

**•** `PUBLISHED`

**•** `ERROR`

**•** `DELETING`

**•** `DELETE_FAILED`

`sourceProfiles` Long Count of source profiles that were processed by a 57.0
ruleset job.

`totalUnifiedProfiles` Long Count of unified profiles created by running the 57.0
identity resolution ruleset.

SEE ALSO:

ConnectApi.CdpIdentityResolutionsOutput

#### ConnectApi.CdpIdentityResolutionReconciliationFieldRuleOutput

Identity resolution ruleset's reconciliation rule for a field.

**Property Name** **Type** **Description** **Available Version**

`fieldName` String The field that this reconciliation rule applies to. 57.0

```
ruleType

```

#### ConnectApi. Default reconciliation rule applied to fields in the 57.0

`CdpIdentityResolution` object the reconciliation rule applies to. Values are:

```
ReconciliationRuleType
```

**•** `LastUpdated`

**•** `MostFrequent`

**•** `SourceSequence`

`shouldIgnore` Boolean Specifies whether to ignore an empty value ( `true` ) 57.0
`EmptyValue` or not ( `false` ).

```
sources

```

SEE ALSO:

#### List< ConnectApi. If ruleType is SourceSequence, a prioritized 57.0

`CdpIdentityResolution` list of data sources.
`ReconciliationSourceOutput` 

#### ConnectApi.CdpIdentityResolutionReconciliationRuleOutput ConnectApi.CdpIdentityResolutionReconciliationRuleOutput

Identity resolution ruleset’s reconciliation rule for an object.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`entityName` String API name of the Data Model Object the reconciliation 57.0
rule applies to.

```
fields

```

#### List< ConnectApi. Field-specific reconciliation rules that override this 57.0

`CdpIdentityResolution` default rule for the specified field.

```
ReconciliationField
```

`RuleOutput` 

`linkDmoName` String API name of the unified link object created by the 57.0
identity resolution process.

```
ruleType

```

#### ConnectApi. Default reconciliation rule applied to fields in the 57.0

`CdpIdentityResolution` object the reconciliation rule applies to. Values are:

```
ReconciliationRuleType
```

**•** `LastUpdated`

**•** `MostFrequent`

**•** `SourceSequence`

`shouldIgnore` Boolean Specifies whether to ignore an empty value ( `true` ) 57.0
`EmptyValue` or not ( `false` ).

```
sources

```

#### List< ConnectApi. If ruleType is SourceSequence, a list of data 57.0

`CdpIdentityResolution` sources in priority order.
`ReconciliationSourceOutput` 

`unifiedDmoName` String API name of the unified data model object created 57.0
by the identity resolution process.

SEE ALSO:

ConnectApi.CdpIdentityResolutionOutput

#### ConnectApi.CdpIdentityResolutionReconciliationSourceOutput

Source for an identity resolution default reconciliation rule or field-specific rule using the `SourceSequence` match method.

**Property Name** **Type** **Description** **Available Version**

`name` String

SEE ALSO:

If the `ruleType` for a reconciliation rule is 57.0
`SourceSequence`, API name of a source Data
Lake Object.

ConnectApi.CdpIdentityResolutionReconciliationRuleOutput

ConnectApi.CdpIdentityResolutionReconciliationFieldRuleOutput


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CdpIdentityResolutionRunNowOutput

Identity resolution ruleset run now output.

**Property Name** **Type** **Description** **Available Version**

```
resultCode

```

#### ConnectApi. Result of an identity resolution ruleset job run. Values 57.0

`CdpIdentityResolution` are:

```
RunNowResultCode
```

**•** `ExceededMaximumNumberOf`

```
            SuccessfulRunsAllowedIn24Hours

```

**•** `IdentityResolutionJobIsAlready`

```
            Running

```

**•** `NoPendingChangesJobRunSkipped`

**•** `SuccessfullySubmittedIdentity`

```
            ResolutionJobRunRequest

```

#### ConnectApi.CdpIdentityResolutionsOutput

Identity resolution rulesets.

**Property Name** **Type** **Description** **Available Version**

```
identityResolutions

```

#### List< ConnectApi. List of identity resolution rulesets. 57.0

```
CdpIdentity
```

`ResolutionOutput` 

#### ConnectApi.CdpMlAggregatePredictCondition

CDP machine-learning aggregate prediction contribution.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Count of rows included in the aggregate condition. 59.0

#### ConnectApi.CdpMlAggregatePrediction

Represents a CDP machine-learning aggregate prediction.

**Property Name** **Type** **Description** **Available Version**

#### factors <List ConnectApi.CdpMlAggregatePredictCondition > Top factors associated with this aggregate prediction. 59.0 prescriptions <List ConnectApi.CdpMlAggregatePredictCondition > Prescriptions associated with this aggregate 59.0

prediction.

`status` `CdpMlPredictAggregateFunctionStatusEnum` Status of the prediction aggregate function. 59.0

**•** `Error`

**•** `Success`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`type` `CdpMlPredictAggregateFunctionTypeEnum` Type of the prediction aggregate function. 59.0

**•** `Average`

**•** `Median`

**•** `Sum`

`value` Double Value of the aggregate prediction. 59.0

#### ConnectApi.CdpMlPredictResult

Represents a CDP machine-learning prediction result.

**Property Name** **Type** **Description** **Available Version**

`aggregatePredictions` <List `ConnectApi.CdpMlAggregatePrediction`    - List of aggregate results. 59.0

`model` `ConnectApi.CdpAssetReference` Model asset reference used as part of the prediction 59.0
request.

`predictionType` `CdpMlModelPredictionTypeEnum` Type of the model prediction. 59.0

**•** `BinaryClassification` -Binary
classification.

**•** `Generic` -Generic/unknown.

**•** `MulticlassClassification` -Multiclass
classification.

**•** `Regression` -Regression.

`predictions` List< `ConnectApi.CdpMlPredictionBase`   - A list of prediction results. 59.0

#### settings ConnectApi.CdpMlPredictSettings Settings used for the prediction. 59.0

SEE ALSO:

predict(predict)

#### ConnectApi.CdpMlPredictSettings

Prediction settings.

**Property Name** **Type** **Description** **Available Version**

`aggregateFunctions` List< `String`    - List of aggregate functions. 59.0

`maxPrescriptions` Integer

Maximum number of recommendations. The default 59.0
value is `-1` (unlimited) and the allowed range is `-1`
through `200` .


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`maxTopFactors` Integer Maximum number of top factors. The default value 59.0
is `0` and the allowed range is `0` through `3` .

`prescriptionImpactPercentage` Integer Impact percentage of prescriptions. The default value 59.0
is `0` and the range of values is `0` through `100` .

#### ConnectApi.CdpMlPredictionBase

Prediction result.

**Property Name** **Type** **Description** **Available Version**

`status` `CdpMlPredictStatusEnum` Status of the prediction. 59.0

**•** `Error`

**•** `Success`

#### ConnectApi.CdpMlPredictionContributionBase

Base representation for a Prediction Contribution

**Property Name** **Type** **Description** **Available Version**

`fields` <List `ConnectApi.CdpMlPredictionContributionField`   - List of field and values that have the same 59.0
contribution value

`value` Double Contribution value 59.0

#### ConnectApi.CdpQueryDataOutput

Query data output.

**Property Name** **Type** **Description** **Available Version**

`data` List<Object> Result data set. 54.0

SEE ALSO:

universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId, sourceRecordId)

universalIdLookupBySourceId(entityName, dataSourceId, dataSourceObjectId, sourceRecordId, dataspace)

#### ConnectApi.CdpQueryDataGraphMetadata

Represents metadata for a data graph.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`dataspaceName` String Name of the data space in which the data graph 59.0
metadata resides.

`description` String Description of the data graph metadata. 59.0

`developerName` String Developer name of the data graph metadata. 59.0

`dgObject` `ConnectApi.DataGraphObjectData` Metadata for the data object of the data graph. 59.0

`extendedProperties` `Object` Extended properties of the data graph metadata. 59.0

`idDmoName` String API name of the Data Model Object (DMO) that 59.0
contains the ID table for the data graph.

`idsDmo` `ConnectApi.DataGraphIdsDmo` Data about the DMO that contains the ID table for 61.0
the data graph.

`primaryObjectName` String Name of the primary object for the data graph. 59.0

`primaryObjectType` `DataGraphObjectTypeEnum` Data type of the primary object for the data graph. 59.0

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

`status` `DataGraphStatusEnum` Status of the data graph. 59.0

**•** `Error`

**•** `Inprogress`

**•** `Published`

**•** `Ready`

**•** `StatusUnspecified`

**•** `Unrecognized`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`valuesDmo` `ConnectApi.DataGraphValuesDmo` Data about the Data Model Object (DMO) that 61.0
contains the JSON records for the data graph.

`valuesDmoName` String API name of the DMO that contains the JSON records 59.0
for the data graph.

`version` String Version of the data graph metadata. 59.0

#### ConnectApi.CdpQueryMetadataItem

Metadata item.

**Property Name** **Type** **Description** **Available Version**

`placeInOrder` Integer Attribute place order in the result. 55.0

`type` String Metadata type for column. 55.0

`typeCode` Integer Metadata type code. 55.0

SEE ALSO:

#### ConnectApi.CdpQueryOutputV2 ConnectApi.CdpQueryMetadataOutput

Query metadata result.

**Property Name** **Type** **Description** **Available Version**

`metadata` List<Object> Metadata set. 52.0

SEE ALSO:

getAllMetadata()

getAllMetadata(entityType, entityCategory, entityName)

getAllMetadata(entityType, entityCategory, entityName, dataspace)

getInsightsMetadata()

getInsightsMetadata(ciName)

getInsightsMetadata(ciName, dataspace)

getProfileMetadata()

getProfileMetadata(dataModelName)

getProfileMetadata(dataModelName, dataspace)

#### ConnectApi.CdpQueryOutput

Query result.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`data` List<Object> Result data set. 52.0

`done` Boolean Specifies whether the query is done ( `true` ) or not 52.0
( `false` ).

`endTime` String Query end time. 52.0

`metadata` Map<String, Object> Result metadata set. 52.0

`queryId` String Query ID. 52.0

`rowCount` Integer Number of rows in the result data set. 52.0

`startTime` String Query start time. 52.0

SEE ALSO:

getDataGraphData(dataGraphEntityName, id)

getDataGraphData(dataGraphEntityName, id, dataspace)

getDataGraphData(dataGraphEntityName, id, live)

getDataGraphData(dataGraphEntityName, id, dataspace, live)

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys)

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace)

getDataGraphDataWithLookupKeys(dataGraphEntityName, lookupKeys, dataspace, noCache)

queryANSISql(input)

queryANSISql(input, batchSize, offset, orderby)

queryANSISql(input, batchSize, offset, orderby, dataspace)

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset)

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset, timeGranularity)

queryCalculatedInsights(ciName, dimensions, measures, orderby, filters, batchSize, offset, timeGranularity, dataspace)

queryProfileApi(dataModelName, filters, fields, batchSize, offset, orderby)

queryProfileApi(dataModelName, id, searchKey, filters, fields, batchSize, offset, orderby)

queryProfileApi(dataModelName, id, childDataModelName, searchKey, filters, fields, batchSize, offset, orderby)

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby)

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby, timeGranularity)

queryProfileApi(dataModelName, id, ciName, searchKey, dimensions, measures, filters, fields, batchSize, offset, orderby, timeGranularity,
dataspace)

#### ConnectApi.CdpQueryOutputV2

Query output for the V2 API.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
data

```

#### List< ConnectApi. Result data set. 54.0

`CdpQueryV2Row` - (in
version 55.0 and later)

List<Object> (version
54.0 only)

`done` Boolean Specifies whether the query is done ( `true` ) or not 54.0
( `false` ).

`endTime` String Query end time. 54.0

`metadata` Map<String, Result metadata set. 54.0

#### `ConnectApi.`

```
          CdpQuery
```

`MetadataItem`         (version 55.0 and later)

Map<String, Object>
(version 54.0 only)

`nextBatchId` String

Next batch ID. 54.0

Use this property as the _`nextBatchId`_ parameter
in the

```
nextBatchAnsiSqlV2(nextBatchId)
```

method to get the next batch of data.

`queryId` String Query ID. 54.0

`rowCount` Integer Number of rows in the result data set. 54.0

`startTime` String Query start time. 54.0

SEE ALSO:

queryAnsiSqlV2(input)

queryAnsiSqlV2(input, dataspace)

nextBatchAnsiSqlV2(nextBatchId)

nextBatchAnsiSqlV2(nextBatchId, dataspace)

#### ConnectApi.CdpQueryV2Row

Row in the query output for the V2 API.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`rowData` List<Object> Row values. 55.0

SEE ALSO:

ConnectApi.CdpQueryOutputV2

#### ConnectApi.CdpSegmentActionOutput

Segment action.

Subclass of ConnectApi.CdpActionResponse in API version 59.0 and later.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code associated with the action, if any. 57.0

`errorMessage` String Error message associated with the action, if any. 57.0

`jobId` String Job ID for the publish job. 56.0

`partitionId` String ID of the partition. 56.0

`publishStatus` String Publish status of the segment. 57.0

`segmentApiName` String API name of the segment. 59.0

`segmentId` String ID of the segment. 56.0

#### ConnectApi.CdpSegmentContainerOutput

Segment container.

**Property Name** **Type** **Description** **Available Version**

`batchSize` Integer Number of items returned. 56.0

`offset` Integer Number of rows skipped before returning results. 56.0

`orderByExpression` String Expression indicating how results are ordered. 56.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### segments List< ConnectApi. List of segments. 55.0

`CdpSegmentOutput`             

SEE ALSO:

getSegment(segmentApiName)

getSegmentById(segmentId)

getSegments()

getSegmentsPaginated(batchSize, offset, orderBy)

getSegmentsPaginated(batchSize, offset, orderBy, dataspace)

getSegmentsFilteredPaginated(batchSize, offset, orderBy, filters)

getSegmentsFilteredPaginated(batchSize, offset, orderBy, dataspace, filters)

#### ConnectApi.CdpSegmentDbtModel

Segment dbt model.

**Property Name** **Type** **Description** **Available Version**

`name` String Dbt model name. 55.0

`sql` String Dbt model SQL. 55.0

SEE ALSO:

#### ConnectApi.CdpSegmentDbtPipeline ConnectApi.CdpSegmentDbtPipeline

Segment dbt pipeline.

**Property Name** **Type** **Description** **Available Version**

```
models

```

SEE ALSO:

#### List< ConnectApi. Dbt models. 55.0

```
CdpSegment
```

`DbtModel` 

ConnectApi.CdpSegmentOutput

#### ConnectApi.CdpSegmentMemberOutput

Data 360 segment member output.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
data

```

#### List< ConnectApi. Result data set. 58.0

```
CdpSegment
```

`MemberRowOutput` 

`endTime` Datetime Query end time. 58.0

`filter` String Filter information for the query. 58.0

`limit` Integer Batch size information. 58.0

`nextPageUrl` String URL for the next page. 58.0

`offSet` Integer Offset information. 58.0

`orderBy` String Order by information. 58.0

`rowCount` Integer Total row count. 58.0

`startTime` Datetime Query start time. 58.0

`totalCount` Integer Total count of records. 58.0

#### ConnectApi.CdpSegmentMemberRowOutput

Data 360 segment member row output.

**Property Name** **Type** **Description** **Available Version**

`deltaType` String Delta type, for example, `new`, `existing`, or 58.0
`removed` .

`id` String Segment member ID. 58.0

`kqId` String Fully qualified key ID. 58.0

`snapshotType` String Type of snapshot, for example, `full` or 58.0
`incremental` .

`timestamp` String Timestamp. 58.0

`versionStamp` String Version timestamp. 58.0

SEE ALSO:

ConnectApi.CdpSegmentMemberOutput

#### ConnectApi.CdpSegmentMembershipTableOutput

Data 360 segment membership table.

**Property Name** **Type** **Description** **Available Version**

`historyTable` String Segment membership history table. 58.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`latestTable` String Segment membership latest table. 58.0

`profileTable` String Segment membership profile table. 58.0

SEE ALSO:

#### ConnectApi.CdpSegmentOutput ConnectApi.CdpSegmentOutput

Segment.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the segment. 56.0

`dataSpace` String Data space of the segment. 57.0

`description` String Segment description. 55.0

`developerName` String Segment developer name. 55.0

`displayName` String Segment display name. 57.0

`excludeCriteria` String Segment exclude criteria. 57.0

`includeCriteria` String Segment include criteria. 57.0

```
includeDbt

```

#### ConnectApi. Segment dbt pipeline. 55.0

```
CdpSegment

DbtPipeline

```

`lookalikeCriteria` Reserved for future use. 56.0

`marketSegment` String ID of the market segment definition. 55.0

```
DefinitionId

```

`marketSegmentId` String ID of the market segment. 56.0

`nextPublish` String Date and time of the next segment publish. 57.0

```
DateTime

```

`publishInterval` String Segment publish interval. 55.0

`publishSchedule` String Publish schedule end date. 55.0

```
EndDate

```

`publishSchedule` String Publish schedule start date time. 55.0

```
StartDateTime

```

`publishStatus` String Segment publish status. 55.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
segmentMembership

Dmo

```

#### ConnectApi. Segment membership tables. 58.0

```
CdpSegmentMembership

TableOutput

```

`segmentMembership` String Name of the segment membership table. 56.0

```
Table

```

`segmentOnApiName` String API name of the SegmentOn entity. 56.0

`segmentOnId` String ID of the DMO segment. 55.0

`segmentStatus` String Segment status. 55.0

`segmentType` String Type of segment. 56.0

SEE ALSO:

ConnectApi.CdpSegmentContainerOutput

#### ConnectApi.ChangeItemOutputRepresentation

The financial changes resulting from a change to one or more OrderItemSummaries. Most of the values represent the deltas of the values
on the associated OrderSummary. The sign of each value is the opposite of the corresponding value on a change order record. For
example, a discount is a positive value here and a negative value on a change order record.

**Property Name** **Type** **Description** **Available Version**

`grandTotalAmount` Double Change to the GrandTotalAmount field. 48.0

`totalAdjDelivery` Double Change to the TotalAdjDeliveryAmtWithTax field. 49.0

```
AmtWithTax

```

`totalAdjDist` Double Change to the TotalAdjDistAmountWithTax field. 49.0

```
AmountWithTax

```

`totalAdjProduct` Double Change to the TotalAdjProductAmtWithTax field. 49.0

```
AmtWithTax

```

`totalAdjusted` Double Change to the TotalAdjustedDeliveryAmount field. 48.0

```
DeliveryAmount

```

`totalAdjusted` Double Change to the TotalAdjustedDeliveryTaxAmount field. 48.0

```
DeliveryTaxAmount

```

`totalAdjusted` Double Change to the TotalAdjustedProductAmount field. 48.0

```
ProductAmount

```

`totalAdjusted` Double Change to the TotalAdjustedProductTaxAmount field. 48.0

```
ProductTaxAmount

```

`totalAdjustment` Double Change to the TotalAdjustmentDistributedAmount 48.0
`DistributedAmount` field.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalAdjustment` Double Change to the 48.0
`DistributedTaxAmount` TotalAdjustmentDistributedTaxAmount field.

`totalAmount` Double Change to the TotalAmount field. 48.0

`totalExcess` Double Amount of excess funds available on the 48.0
`FundsAmount` OrderPaymentSummaries related to the
OrderSummary. It is equal to the captured amount
that is owed as a refund but is not associated with
an invoice or credit memo. Excess funds normally
occur when order items are canceled before
fulfillment but after payment has been captured. This
situation is not common in the US, where funds are
normally authorized but not captured until the
fulfillment process begins. This value includes all
current excess funds related to the OrderSummary,
not only the funds related to the current change.

`totalFeeAmount` Double Total amount of the fees charged for the change. 57.0

`totalFeeTaxAmount` Double Total amount of tax on the fees charged for the 57.0
change.

`totalRefundable` Double Total amount available to be refunded. It is the sum 48.0
`Amount` of the excess funds and any outstanding change
order grand total amounts that apply to
post-fulfillment changes. This value includes all
current refundable amounts related to the
OrderSummary, not only the amount related to the
current change.

`totalRequired` Double The required funds associated with added order 54.0
`FundsAmount` items.

`totalTaxAmount` Double Change to the TotalTaxAmount field. 48.0

SEE ALSO:

ConnectApi.PreviewCancelOutputRepresentation

ConnectApi.PreviewReturnOutputRepresentation

ConnectApi.SubmitCancelOutputRepresentation

ConnectApi.SubmitReturnOutputRepresentation

#### ConnectApi.ChangeOrdersInvoiceOutputRepresentation

List of IDs of invoices created for change orders.

Subclass of ConnectApi.BaseInvoiceOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

No additional properties.

SEE ALSO:

createMultipleInvoices(invoicesInput)

ConnectApi.CreateMultipleInvoicesFromChangeOrdersOutputRepresentation

#### ConnectApi.ChatterActivity

Chatter activity.

**Name** **Type** **Description** **Available**
**Version**

`commentCount` Integer Total number of comments in the org or site made by the user. 28.0

`commentReceived` Integer Total number of comments in the org or site received by the user. 28.0

```
   Count

```

`likeReceived` Integer Total number of likes and upvotes (in version 45.0 and later) on posts 28.0
`Count` and comments in the org or site received by the user.

`postCount` Integer Total number of posts in the org or site made by the user. 28.0

SEE ALSO:

ConnectApi.UserDetail

#### ConnectApi.ChatterActivitySummary

Summary of Chatter activity.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`commentCount` Integer Total number of comments in the org or site made 42.0
by the user.

`commentReceived` Integer Total number of comments in the org or site received 42.0
`Count` by the user.

`likeReceived` Integer

```
Count

```

Total number of likes and upvotes (in version 45.0 42.0
and later) on posts and comments in the org or site
received by the user.

`postCount` Integer Total number of posts in the org or site made by the 42.0
user.

#### ConnectApi.ChatterConversation

Chatter conversation.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`conversationId` String ID for the conversation. 29.0

`conversationUrl` String Connect REST API URL identifying the conversation. 29.0

`members` `List<ConnectApi.` List of users in the conversation. 29.0

```
            UserSummary>

```

```
messages

```

#### ConnectApi. Content of the conversation. 29.0

```
Chatter

MessagePage

```

`read` Boolean Specifies if the conversation is read ( `true` ) or not read 29.0
( `false` ).

#### ConnectApi.ChatterConversationPage

Chatter conversation page.

**Name** **Type** **Description** **Available**
**Version**

`conversations` `List<ConnectApi.Chatter` List of conversations on the page. 29.0

```
         ConversationSummary>

```

`currentPageToken` String Token identifying the current page. 29.0

`currentPageUrl` String Connect REST API URL identifying the current page. 29.0

`nextPageToken` String Token identifying the next page, or `null` if there isn’t 29.0
a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 29.0
`null` if there isn’t a next page.

#### ConnectApi.ChatterConversationSummary

Chatter conversation summary.

**Name** **Type** **Description** **Available**
**Version**

`id` String ID for the conversation summary. 29.0

`latestMessage` `ConnectApi.ChatterMessage` Contents of the latest message. 29.0

`members` `List<ConnectApi.UserSummary>` List of members in the conversation. 29.0

`read` Boolean Specifies if the conversation is read ( `true` ) or not read 29.0
( `false` ).


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`url` String Connect REST API URL to the conversation summary. 29.0

SEE ALSO:

ConnectApi.ChatterConversationPage

#### ConnectApi.ChatterGroup

Chatter group.

This class is abstract.

Subclass of ConnectApi.ActorWithId.

Superclass of:

#### • ConnectApi.ChatterGroupDetail • ConnectApi.ChatterGroupSummary

**Name** **Type** **Description** **Available**
**Version**

`additional` String An extra label for the group, for example, “Archived,” “Private,” or “Private With 30.0
`Label` Customers.” If there isn’t an extra label, the value is `null` .

#### `announcement ConnectApi.`

```
         Announcement

```

The current announcement for this group. An announcement displays in a 31.0
designated location in the Salesforce UI until 11:59 p.m. on its expiration date,
unless it’s deleted or replaced by another announcement.

`bannerPhoto` `ConnectApi.BannerPhoto` The banner photo for the group. 36.0

`canHave` Boolean `true` if this group allows Chatter guests. 28.0

```
ChatterGuests

#### community ConnectApi. Information about the Experience Cloud site the group is in. 28.0

         Reference

```

`description` String Group’s description. 28.0

`emailTo` String

```
ChatterAddress

```

Group’s email address for posting to this group by email. 30.0

Returns `null` if Chatter emails and posting to Chatter by email aren’t both
enabled in your organization.

`isArchived` Boolean Specifies whether the group is archived ( `true` ) or not ( `false` ). 29.0

`isAuto` Boolean Specifies whether automatic archiving is disabled for the group ( `true` ) or 29.0
`ArchiveDisabled` not ( `false` ).

`isBroadcast` Boolean Specifies whether the group is a broadcast group ( `true` ) or not ( `false` ). 36.0
In a broadcast group, only group owners and managers can post to the group.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`lastFeedElement` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z, of the most 31.0
`PostDate` recent feed element posted to the group.

`lastFeedItem` Datetime

```
PostDate

```

ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z, of the most 28.0–30.0
recent feed item posted to the group.

Use `lastFeedElementPosted` .

`memberCount` Integer Total number of group members. 28.0

#### myRole ConnectApi. Type of membership the user has with the group. 28.0

```
         GroupMembershipType
```

**•** `GroupOwner`

**•** `GroupManager`

**•** `NotAMember`

**•** `NotAMemberPrivateRequested`

**•** `StandardMember`

#### mySubscription ConnectApi. If the context user is a member of this group, contains information about that 28.0

`Reference` subscription; otherwise, returns `null` .

`name` String Name of the group. 28.0

#### owner ConnectApi. Information about the owner of the group. 28.0

```
         UserSummary

```

`photo` `ConnectApi.Photo` Information about the group photo. 28.0

```
visibility

```

`Connectapi.` Group visibility type. Valid values are: 28.0

```
GroupVisibility
```

**•** `PrivateAccess` —Only members of the group can see posts to this

`Type` group.

**•** `PublicAccess` —All users within the Experience Cloud site can see
posts to this group.

**•** `Unlisted` —Reserved for future use.

#### ConnectApi.ChatterGroupDetail

Chatter group details.

Subclass of ConnectApi.ChatterGroup.

**Name** **Type** **Description** **Available**
**Version**

`fileCount` Integer The number of files posted to the group. 28.0

```
information

```

#### ConnectApi. Describes the Information section of the group. If the group is private, this 28.0

`Group` section is visible only to members. If the context user is not a member of

```
Information

```


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

the group or does not have Modify All Data or View All Data permission,
this value is `null` .

`pending` Integer The number of requests to join a group that are in a pending state. 29.0

```
   Requests

```

SEE ALSO:

#### ConnectApi.ChatterGroupPage

ConnectApi.UserGroupDetailPage

#### ConnectApi.ChatterGroupPage

Page of groups.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

`groups` `List<ConnectApi.` List of group details. 28.0

```
            Chatter

            Group

            Detail>

```

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if there isn’t a 28.0
next page.

`previous` String Connect REST API URL identifying the previous page, or `null` if there isn’t 28.0
`PageUrl` a previous page.

#### ConnectApi.ChatterGroupSummary

Chatter group summary.

Subclass of ConnectApi.ChatterGroup.

**Name** **Type** **Description** **Available**
**Version**

`fileCount` Integer The number of files posted to the group. 28.0

SEE ALSO:

#### ConnectApi.ChatterGroupSummaryPage

ConnectApi.UserGroupPage


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ChatterGroupSummaryPage

Page of group summaries.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 29.0

```
groups

```

`List<ConnectApi.` List of group summary objects. 29.0

```
ChatterGroup

Summary>

```

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 29.0
there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or `null` 29.0
if there isn’t a previous page.

#### ConnectApi.ChatterLike

Chatter like information.

**Name** **Type** **Description** **Available**
**Version**

`id` String Like’s 18-character ID 28.0

#### likedItem ConnectApi. A reference to the liked comment or feed element. 28.0

```
         Reference

```

`url` String Like’s Connect REST API URL 28.0

`user` `ConnectApi.User` Like’s creator 28.0

```
         Summary

```

SEE ALSO:

#### ConnectApi.ChatterLikePage ConnectApi.ChatterLikePage

Page of Chatter likes.

**Name** **Type** **Description** **Available**
**Version**

`currentPageToken` Integer Token identifying the current page. 28.0

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

`items` `List<ConnectApi.` List of likes. 32.0

```
         ChatterLike>

```


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`likes` `List<ConnectApi.` List of likes. 28.0–31.0

```
            ChatterLike>
```

Important: As of API version 32.0, use the `items`
property.

`nextPageToken` Integer Token identifying the next page, or `null` if there isn’t a next 28.0
page.

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if there 28.0
isn’t a next page.

`previousPageToken` Integer Token identifying the previous page, or `null` if there isn’t a 28.0
previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or `null` if 28.0
there isn’t a previous page.

`total` Integer Total number of likes across all pages. 28.0

SEE ALSO:

#### ConnectApi.ChatterLikesCapability

ConnectApi.Comment

#### ConnectApi.ChatterLikesCapability

If a feed element has this capability, the context user can like it. Exposes information about existing likes.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isLikedBy` Boolean Indicates whether the feed element is liked by the 32.0
`CurrentUser` context user ( `true` ) or not ( `false` ).

#### page ConnectApi. Likes information for this feed element. 32.0

```
             ChatterLikePage

#### likesMessage ConnectApi. A message body that describes who likes the feed 32.0
```

`MessageBody` element.

#### `myLike ConnectApi.`

```
           Reference

```

SEE ALSO:

ConnectApi.FeedElementCapabilities

If the context user has liked the feed element, this 32.0
property is a reference to the specific like, `null`
otherwise.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ChatterMessage

Chatter message.

**Name** **Type** **Description** **Available**
**Version**

`body` `ConnectApi.MessageBody` Contents of the message. 29.0

`conversationId` String ID for the conversation. 29.0

`conversationUrl` String Connect REST API URL identifying the conversation. 29.0

`id` String ID of the message. 29.0

`recipients` `List<ConnectApi.UserSummary>` List of the recipients of the message. 29.0

`sender` `ConnectApi.UserSummary` Sender of the message. 29.0

```
sendingCommunity ConnectApi.Reference

```

Information about the Experience Cloud site from 32.0
which the message was sent.

Returns `null` for the default site or if digital
experiences isn’t enabled.

`sentDate` Datetime The date and time the message was sent. 29.0

`url` String Connect REST API URL identifying the current page 29.0
of the conversation.

SEE ALSO:

ConnectApi.ChatterConversationSummary

#### ConnectApi.ChatterMessagePage ConnectApi.ChatterMessagePage

Chatter message page.

**Name** **Type** **Description** **Available**
**Version**

`currentPageToken` String Token identifying the current page. 29.0

`currentPageUrl` String Connect REST API URL identifying the current page. 29.0

`messages` `List<ConnectApi.ChatterMessage>` Messages on the current page. 29.0

`nextPageToken` String Token identifying the next page, or `null` if there 29.0
isn’t a next page.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`nextPageUrl` String Connect REST API URL identifying the next page, or 29.0
`null` if there isn’t a next page.

SEE ALSO:

ConnectApi.ChatterConversation

#### ConnectApi.ChatterStream

A Chatter feed stream.

**Property Name** **Type** **Description** **Available Version**

`community` `ConnectApi.CommunitySummary` Experience Cloud site where the stream is. 41.0

`createdDate` Datetime Date the stream was created. 39.0

`description` String Description of the stream. 39.0

`id` String 18-character ID of the stream. 39.0

`name` String Name of the stream. 39.0

`subscriptions` List< `ConnectApi.FeedEnabledEntity`   - List of entities whose feeds are included in the stream. 39.0

`url` String URL to the stream. 39.0

SEE ALSO:

#### ConnectApi.ChatterStreamPage ConnectApi.ChatterStreamPage

A collection of Chatter feed streams.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page of streams. 39.0

#### items List< ConnectApi. List of streams. 39.0

`ChatterStream`            

`nextPageUrl` String

URL to the next page of streams. 39.0

In version 39.0, all streams are included in
`currentPageUrl` and `nextPageUrl` is
`null` .

`total` Integer Total number of streams in the collection. 39.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.Chunk

Content chunk for the search result.

**Property Name** **Type** **Description** **Available Version**

`text` String Text extract relevant to the search query. 63.0

#### ConnectApi.ClientInfo

Client information.

**Name** **Type** **Description** **Available**
**Version**

`applicationName` String Name of the connected app used for authentication. 28.0

`applicationUrl` String Value from the `Info URL` field of the connected app used for 28.0
authentication.

SEE ALSO:

ConnectApi.Comment

ConnectApi.FeedItem

#### ConnectApi.CloseCapability

If a feed element has this capability, users with permission can close it.

Users can’t edit (specifically the feed item body or title), comment on, or delete a closed feed element. If the closed feed element is a
poll, users can’t vote on it. Users can’t edit (specifically the comment body) or delete a comment on a closed feed element or select or
remove it as best answer.

Admins and moderators can edit and delete closed feed elements and comments on closed feed elements. Admins and moderators
can select or remove the best answer status on comments on closed feed elements.

**Property Name** **Type** **Description** **Available Version**

`canContextUser` Boolean

```
UpdateIsClosed

```

Specifies whether the context user has permission 43.0
to set the feed element to closed ( `true` ) or not
( `false` ).

`isClosed` Boolean Specifies whether the feed element is closed ( `true` ) 43.0
or not ( `false` ).

SEE ALSO:

ConnectApi.FeedElementCapabilities


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.Comment

A comment.

**Name** **Type** **Description** **Available**
**Version**

```
attachment ConnectApi.FeedItem

         Attachment

```

If the comment contains an attachment, property value is 28.0–31.0
`ContentAttachment` . If the comment does not contain
an attachment, it is `null` .

Important: As of version 32.0, use the
`capabilities` property.

`body` `ConnectApi.FeedBody` Body of the comment. 28.0

#### capabilities ConnectApi. Capabilities associated with the comment, such as any file 32.0

`CommentCapabilities` attachments.

#### clientInfo ConnectApi. Information about the connected app used to authenticate 28.0

`ClientInfo` the connection.

`createdDate` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z. 28.0

#### feedElement ConnectApi. Feed element on which the comment is posted.

```
         Reference

#### feedItem ConnectApi. Feed item on which the comment is posted. 28.0–31.0

         Reference
```

Important: As of version 32.0, use the
`feedElement` property.

`id` String Comment’s 18–character ID. 28.0

`isDelete` Boolean

```
Restricted

likes ConnectApi.Chatter

         LikePage

likesMessage ConnectApi.Message

         Body

#### `moderation ConnectApi.`

Flags ModerationFlags

#### `myLike ConnectApi.`

         Reference

```

If this property is `true`, the context user can’t delete the 28.0
comment. If this property is `false`, the context user might
be able to delete the comment.

The first page of likes for the comment. 28.0

This property has no information for comments on direct
messages.

A message body that describes who likes the comment. 28.0

This property is `null` for comments on direct messages.

Information about the moderation flags on a comment. If 29.0

```
ConnectApi.Features.communityModeration
```

is `false`, this property is `null` .

If the context user liked the comment, this property is a 28.0
reference to the specific like, `null` otherwise.

This property is `null` for comments on direct messages.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

#### parent ConnectApi. Information about the parent feed-item for this comment. 28.0

```
            Reference

```

`relativeCreatedDate` String The created date formatted as a relative, localized string, for 28.0
example, “17m ago” or “Yesterday.”

`threadLevel` Integer Level of nesting for a comment. 0 indicates a standard 44.0
comment with a parent post. 1 indicates a threaded

comment with a parent comment and a parent post. 2
indicates a threaded comment with two parent comments
and a parent post. The UI is limited to these three levels.

`threadParentId` String ID of the parent comment for a threaded comment. 44.0

#### type ConnectApi. Type of comment. 28.0

```
            CommentType
```

**•** `ContentComment` —Comment holds a content
capability.

**•** `TextComment` —Comment contains only text.

`url` String Connect REST API URL to this comment. 28.0

`user` `ConnectApi.User` Information about the comment author. 28.0

```
            Summary

```

SEE ALSO:

ConnectApi.CommentPage

ConnectApi.QuestionAndAnswersCapability

#### ConnectApi.CommentCapabilities

A set of capabilities on a comment.

**Property Name** **Type** **Description** **Available Version**

`comments` `ConnectApi.CommentsCapability` If a comment has this capability, it has threaded 44.0
comments.

```
content ConnectApi.ContentCapability

```

If a comment has this capability, it has a file 32.0
attachment.

Most `ConnectApi.ContentCapability`
properties are null if the content has been deleted

from the feed element or if the access has changed
to private.

`edit` `ConnectApi.EditCapability` If a comment has this capability, users who have 34.0
permission can edit it.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`feedEntityShare` `ConnectApi.FeedEntityShareCapability` If a comment has this capability, a feed entity is 42.0
shared with it.

`record` `ConnectApi.RecordCapability` If a comment has this capability, it has a record 42.0
attachment.

`status` `ConnectApi.StatusCapability` If a comment has this capability, it has a status that 38.0
determines its visibility.

`upDownVote` `ConnectApi.UpDownVoteCapability` If a comment has this capability, users can upvote or 41.0
downvote it.

`verified` `ConnectApi.VerifiedCapability` If a comment has this capability, users with 41.0
permission can mark it as verified or unverified.

SEE ALSO:

#### ConnectApi.Comment ConnectApi.CommentPage

A page of comments.

**Name** **Type** **Description** **Available**
**Version**

#### comments List< ConnectApi. Collection of comments. 28.0–31.0

`Comment`           
Important: As of version 32.0, use the `items` property.

`currentPageToken` String Token identifying the current page. 28.0

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

#### items List< ConnectApi. Collection of comments for this feed element. 32.0

`Comment`           

`nextPageToken` String

`nextPageUrl` String

Token identifying the next page, or `null` if there isn’t a next page. 28.0

If you want to read more of the comments in search results, all the
comments in the thread are refreshed, not just the ones that match the

search term. Avoid using `nextPageToken` until the comments are
refreshed.

Connect REST API URL identifying the next page, or `null` if there isn’t 28.0
a next page.

If you want to read more of the comments in search results, all the
comments in the thread are refreshed, not just the ones that match the

search term. Avoid using `nextPageUrl` until the comments are
refreshed.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`previousPageToken` String Token identifying the previous page, or `null` if there isn’t a previous 44.0
page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or `null` if there 44.0
isn’t a previous page.

`total` Integer Total number of published comments for the parent feed element. 28.0

SEE ALSO:

#### ConnectApi.CommentsCapability ConnectApi.CommentSummary

Summary of the comment.

Subclass of ConnectApi.UserActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`commentId` String ID of the comment. 42.0

#### ConnectApi.CommentsCapability

If a feed element or comment has this capability, the context user can add a comment to it.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

```
page ConnectApi.CommentPage

```

SEE ALSO:

ConnectApi.FeedElementCapabilities

The comments information for this feed element or 32.0
comment.

Threaded comments are supported in version 44.0
and later.

#### ConnectApi.CommerceActionResult

Result of executing a commerce action.

**Property Name** **Type** **Description** **Available Version**

`isSuccess` Boolean Specifies whether the action is a success ( `true` ) or 53.0
not ( `false` ).


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`message` String Action result message. 53.0

#### ConnectApi.CommerceAddressCollection

A collection of Commerce addresses.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Count of addresses. 54.0

`currentPageToken` String Token to the current page of addresses. 54.0

`currentPageUrl` String URL to the current page of addresses. 54.0

#### items <List ConnectApi.CommerceAddressOutput > Address Details 54.0

`nextPageToken` String Token to the next page of addresses. 54.0

`nextPageUrl` String URL to the next page of addresses. 54.0

`pageSize` Integer Page size for addresses. 54.0

`previousPageToken` String Token to previous page of addresses. 54.0

`previousPageUrl` String URL to the previous page of addresses. 54.0

`sortOrder` `ConnectApi.CommerceAddressSort` Sort order for Commerce addresses. 54.0

**•** `CreatedDateAsc` —Sort in ascending order
of created date.

**•** `CreatedDateDesc` —Sort in descending
order of created date.

**•** `NameAsc` —Sort in ascending order of name.

**•** `NameDesc` —Sort in descending order of name.

#### ConnectApi.CommerceAddressOutput

Address for a Commerce account.

**Property Name** **Type** **Description** **Available Version**

`addressId` String ID of the address. 54.0

`addressType` String Type of address (for example, “Shipping” or “Billing”). 54.0

`city` String The address city. 54.0

`companyName` String The address company name. 57.0

`country` String The address country. 54.0

`countryCode` String Two-character country code. 54.0–58.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`fields` Map<String, Record A list of custom address fields, if any. 54.0
Field>

`firstName` String The address first name. 57.0

`isDefault` Boolean

Indicates whether a contact’s address is the preferred 54.0
method of communication ( `true` ) or not ( `false` ).
The default value is `false` .

`lastName` String The address last name. 57.0

`middleName` String The address middle name. 57.0

`name` String Name of the contact. 54.0

`phoneNumber` String The address phone number. 57.0

`postalCode` String Zip code or postal code for the address. 54.0

`region` String The address state. 54.0

`regionCode` String The address state code. 54.0–58.0

`street` String The address street. 54.0

#### ConnectApi.CommerceProductSearchResults

Product search results information.

**Property Name** **Type** **Description** **Available Version**

#### categories ConnectApi. Categories from the search results. 52.0

```
           SearchCategory

```

`correlationId` String Reserved for future use. 55.0

#### facets List< ConnectApi. Facets from the search results. 52.0

`SearchFacet`          

`locale` String Locale of the search results. 52.0

#### productsPage ConnectApi. Page of products from the search results. 52.0

```
           ProductSummaryPage

#### ConnectApi.CommerceProductSellingModel

```

Product selling model information.

**Property Name** **Type** **Description** **Available Version**

`isSubscriptionProduct` Boolean Indicates whether the product selling model is a 59.0
subscription product or not.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.CommerceProductSummary

Summary of a product in product search results.

**Property Name** **Type** **Description** **Available Version**

#### defaultImage ConnectApi. Default image of the product. 55.0

```
             ProductMedia

```

```
fields

```

Map<String, Map of fields belonging to the product. 55.0

#### `ConnectApi.`

`FieldValue` 

`id` String ID of the product. 55.0

`name` String Name of the product. 55.0

```
prices

```

#### ConnectApi. Prices of the product. 55.0

```
PricingResult

LineItem

```

#### productClass ConnectApi. Class of product. Values are: 55.0

```
          ProductClass
```

**•** `Bundle`

```
productSelling

ModelInformation

```

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

#### ConnectApi. Product selling model information. 59.0

```
CommerceProduct

SellingModel

```

`productVariation` ConnectApi.ProductVariationInfo Product variation attributes, metadata, and mappings 63.0
`Info` on page 2481 of attribute combinations to variation product IDs.
This field isn't available in stores with displayable
fields enabled.

```
purchaseQuantityRule

```

#### ConnectApi. If one exists, purchase quantity rule for the product. 58.0

```
PurchaseQuantity

Rule

```

`urlName` String SEO-friendly URL name for the product. 59.0

```
variationAttributeSet

```

#### ConnectApi. Variation attribute set that’s associated with the 55.0

`ProductAttribute` product.

```
SetSummary

```

#### ConnectApi.CommerceProductSummaryPage

Collection of product summary representations in product search results.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`pageSize` Integer Number of products per page in search results. 55.0

`products` <List `ConnectApi.CommerceProductSummary`   - Collection of product summaries. 55.0

`total` Long Number of products in search results across all pages. 55.0

#### ConnectApi.CommerceResultRepresentationBase

Base cart calculate output class.

This class is abstract.

Superclass of:

**•** ConnectApi.CalculateCartResult

**Property Name** **Type** **Description** **Available Version**

`message` String Message related to the request. 62.0

`status` String Asynchronous processing status of the cart, if 62.0
asynchronous processing is enabled for the store.

This property returns `Completed` in Apex, because
Apex operations always run synchronously.

#### ConnectApi.CommerceSearchIndex

Index information.

**Property Name** **Type** **Description** **Available Version**

`completionDate` Datetime Completion date and time of the index. 52.0

`createdDate` Datetime Creation date of the index. 52.0

```
creationType

```

#### ConnectApi. Creation type of the index. Values are: 52.0

```
CommerceSearch
```

**•** `Manual`
```
IndexCreationType

```

**•** `Manual`

**•** `Scheduled`

`id` String ID of the index. 52.0

```
indexBuildType

indexStatus

```

#### ConnectApi. Build type of the index. Values are: 57.0

```
CommerceSearch
```

**•** `Full`
```
IndexBuildType

```

#### ConnectApi. Status of the index. Values are: 52.0

```
CommerceSearch
```

**•** `Completed`
```
IndexStatus

```

**•** `Full`

**•** `Incremental`

**•** `Completed`

**•** `Failed`

**•** `InProgress`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
indexUsage

```

#### ConnectApi. Usage of the index. Values are: 52.0

```
CommerceSearch
```

**•** `Live`
```
IndexUsage

```

**•** `Live`

**•** `OutOfUse`

`isIncrementable` Boolean Specifies whether the index allows incremental 57.0
indexing ( `true` ) or not ( `false` ).

`lastCatalogSnapshotTime` Datetime Catalog snapshot time of the index. 57.0

`message` String Detailed message for the index status. 52.0

SEE ALSO:

#### ConnectApi.CommerceSearchIndexCollection ConnectApi.CommerceSearchIndexCollection

Collection of indexes.

**Property Name** **Type** **Description** **Available Version**

List of up to two indexes. Returns the completed, live 52.0
index and either the in-progress, out-of-use index or
the most-recently-failed, out-of-use index.

```
indexes

```

#### List< ConnectApi.

```
CommerceSearch
```

`Index` 

#### ConnectApi.CommerceSearchIndexLog

Search index log information.

**Property Name** **Type** **Description** **Available Version**

`catalog` Datetime Catalog snapshot time of the index build. 57.0

```
SnapshotTime

```

`completionDate` Datetime Completion date of the index build. 57.0

`createdById` String ID of the user who initiated the index build. 57.0

```
indexBuildStatus

indexBuildType

```

#### ConnectApi. Status of the index. Values are: 57.0

```
CommerceSearch
```

**•** `Completed`
```
IndexStatus

```

#### ConnectApi. Build type of the index. Values are: 57.0

```
CommerceSearch
```

**•** `Full`
```
IndexBuildType

```

**•** `Completed`

**•** `Failed`

**•** `InProgress`

**•** `Full`

**•** `Incremental`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`indexId` String ID of the index build. 57.0

`message` String Detailed message for the index build status. 57.0

`numberOfProducts` Integer Number of new or changed products in the index 57.0
build.

#### ConnectApi.CommerceSearchIndexLogCollection

Collection of search index logs for a webstore.

**Property Name** **Type** **Description** **Available Version**

```
indexLogs

```

#### List< ConnectApi. List of up to 100 index logs sorted by most recent 57.0

`CommerceSearch` catalog snapshot time of the index.
`IndexLog` 

#### ConnectApi.Community

Experience Cloud site.

**Name** **Type** **Description** **Available**
**Version**

`allowChatter` Boolean Specifies if guest users can access public groups without logging in. 31.0

```
AccessWithoutLogin

```

`allowMembers` Boolean Specifies if members can flag content. 30.0

```
ToFlag

```

`builderBased` Boolean

```
SnaEnabled

```

Specifies whether the Service Not Available page is an auto-generated 52.0
Experience Builder-based page ( `true` ) or a static resource page that’s
set in **Workspaces** - **Administration** - **Pages** ( `false` ).

`builderUrl` String Experience Builder URL for the site. 56.0

`contentSpaceId` String ID of the managed content space associated with the enhanced site. 62.0

`description` String Site description. 28.0

`guestMember` Boolean Specifies whether guest members can see other members ( `true` ) or not 47.0
`VisibilityEnabled` ( `false` ).

`id` String Site ID. 28.0

`imageOptimization` Boolean

```
CDNEnabled

```

Specifies whether images are optimized for guest users on all devices for 56.0
sites using Salesforce's CDN for Digital Experiences ( `true` ) or not
( `false` ).

`invitationsEnabled` Boolean Specifies whether users can invite other external users. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`knowledgeable` Boolean Specifies whether knowledgeable people and endorsements are available 30.0
`Enabled` for topics ( `true` ), or not ( `false` ).

`loginUrl` String Login URL for the site. 36.0

`memberVisibility` Boolean Specifies whether members can see other members ( `true` ) or not 45.0
`Enabled` ( `false` ).

`name` String Site name. 28.0

`nicknameDisplay` Boolean Specifies whether nicknames are displayed. 32.0

```
   Enabled

```

`privateMessages` Boolean Specifies whether members can send and receive private messages to 30.0
`Enabled` and from other members ( `true` ) or not ( `false` ).

`reputationEnabled` Boolean Specifies whether reputation is calculated and displayed for members. 31.0

`sendWelcomeEmail` Boolean Specifies whether emails are sent to all new users when they join. 28.0

`siteAsContainer` Boolean Specifies whether the site is an Experience Builder site ( `true` ) or a 41.0
`Enabled` Salesforce Tabs + Visualforce site ( `false` ).

`siteUrl` String URL for the site, which is your Experience Cloud sites domain plus a URL 30.0
prefix. For example, _`MyDomainName`_ `.my.site.com/customers` .

```
status

```

#### ConnectApi. Status of the Experience Cloud site. 28.0

```
CommunityStatus
```

**•** `Live`

Enum

**•** `Live`

**•** `Inactive`

**•** `UnderConstruction`

`templateName` String Name of the Experience Builder template. 46.0

`url` String Connect REST API URL to the site. 28.0

`urlPathPrefix` String

SEE ALSO:

#### ConnectApi.CommunityPage

Site-specific URL prefix. For example, in the site URL 28.0
_`MyDomainName`_ `.my.site.com/customers`, `customers` is
the `UrlPathPrefix` .

#### ConnectApi.CommunityPage

Page of Experience Cloud sites.

**Name** **Type** **Description** **Available Version**

`communities` `List<ConnectApi.` List of Experience Cloud sites the context user has access 28.0
`Community>` to.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`total` Integer Total number of Experience Cloud sites. 28.0

#### ConnectApi.CommunitySummary

Summary of an Experience Cloud site.

**Property Name** **Type** **Description** **Available Version**

`id` String 18-character ID of the site. 41.0

`name` String Localized name of the site. 41.0

SEE ALSO:

ConnectApi.UserActivitySummary

#### ConnectApi.CompanyVerifySummary

Company verify summary.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.ComplexSegment

Complex segments of field changes.

This class is abstract.

Subclass of ConnectApi.MessageSegment.

Superclass of ConnectApi.FieldChangeSegment.

**Name** **Type** **Description** **Available Version**

`segments` `List<ConnectApi.` List of message segments. 28.0

```
            MessageSegment>

#### ConnectApi.CompositeCommerceProductOutputRepresentation

```

Details of a composite product.

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. List of any errors that were returned, including the 61.0

`ErrorResponse`            - error code and error message.

`productId` String ID of the product record created. 61.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`success` Boolean Indicates whether the product was successfully 61.0
created ( `true` ) or not ( `false` ).

#### ConnectApi.CompositeCommerceVariationOutputRepresentation

Details of composite product variations.

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. List of any errors that were returned, including the 62.0

`ErrorResponse`            - error code and error message.

`productIds` List<String> IDs of the created product variations. 62.0

`success` Boolean Indicates whether the product variations were 62.0
successfully created ( `true` ) or not ( `false` ).

#### ConnectApi.CompoundRecordField

Record field that is a composite of subfields.

Subclass of ConnectApi.LabeledRecordField.

**Name** **Type** **Description** **Available Version**

```
fields

```

`List<ConnectApi.` Collection of subfields that make up the compound field. 29.0

```
Abstract

RecordField>

```

#### ConnectApi.ConfirmHeldFOCapacityOutputRepresentation

Response to a request to confirm held fulfillment order capacity at one or more locations. Can correspond to one action call.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
confirmHeldFO

CapacityResponses

```

#### List< ConnectApi. List of responses to the requests to confirm held 55.0

`ConfirmHeldFO` fulfillment order capacity at one or more locations.

```
CapacityResponse
```

`OutputRepresentation` 

#### ConnectApi.ConfirmHeldFOCapacityResponseOutputRepresentation

Response to a request to confirm held fulfillment order capacity at one or more locations.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
capacityResponses

```

#### List< ConnectApi. List of responses to the requests to confirm held 55.0

`CapacityResponse` fulfillment order capacity at individual locations.
`OutputRepresentation` 

#### ConnectApi.ConnectionDbSchemaCollection

Represents a collection of database schemas.

**Property Name** **Type** **Description** **Available Version**

`databaseSchemas` List<String> List of database schemas. 63.0

SEE ALSO:

getDatabaseSchemas(connectionId, getDatabaseSchemasInput)

#### ConnectApi.ContactPointConfig

Represents an activation contact point configuration output.

**Property Name** **Type** **Description** **Available Version**

`activationContactPointFieldConfig` `ConnectApi.ActivationContactPointsFieldConfig` Contact point field configurations. 60.0

`activationContactPointSourcesConfig` `ConnectApi.ActivationContactPointsSourceConfig` Contact point source configurations. 60.0

`contactPointFilterExpression` `ConnectApi.ContactPointFilterExpression` Contact point filter expression. 60.0

`contactPointPath` String Contact point path. 60.0

`contactPointType` `ContactPointTypeRepresentationEnum` Type of contact point. 60.0

**•** `Email`

**•** `Maid`

**•** `Ott`

**•** `Phone`

**•** `Push`

**•** `Subscriber_Key_Email`

**•** `Subscriber_Key_Phone`

**•** `WhatsApp`

`entityId` String ID of the entity. 60.0

`entityName` String Name of the entity. 60.0

#### queryPathConfigList List< ConnectApi. List of query path configurations. 60.0

`QueryPathConfigList`            


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ContactPointFilterExpression

Represents an activation contact point filter expression output.

**Property Name** **Type** **Description** **Available Version**

`contactPointDmoFilters` List< `ConnectApi.DmoFilter`    - List of contact point DMO filter expressions. 60.0

#### ConnectApi.ContactPointsConfig

Represents the activation contact points configuration output.

**Property Name** **Type** **Description** **Available Version**

`contactPoints` List< `ConnectApi.ContactPointConfig`   - Activation contact points. 60.0

#### ConnectApi.Content

A file attached to a feed item.

**Property Name** **Type** **Description** **Available Version**

`checksum` String MD5 checksum for the file. 36.0

`contentUrl` String URL of the content for links. 36.0

`description` String Description of the attachment. 36.0

`downloadUrl` String URL to the content. 36.0

`fileExtension` String Extension of the file. 36.0

`fileSize` String Size of the file in bytes. If size can’t be determined, 36.0
returns `unknown` .

`fileType` String Type of file, such as PDF. 36.0

`hasPdfPreview` Boolean `true` if the file has a PDF preview available; `false` 36.0
otherwise.

`id` String 18-character ID of the content. 36.0

#### imageDetails ConnectApi.ContentImageFileDetails Image details, or null if the file isn’t an image. 40.0

`isInMyFileSync` Boolean `true` if the file is synced with Salesforce Files Sync. 36.0

Note: Salesforce Files Sync was retired on
May 25, 2018.

`mimeType` String MIME type of the file. 36.0

`renditionUrl` String URL to the rendition resource for the file. For shared 36.0
files, renditions process asynchronously after upload.

For private files, renditions process when the first file


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

preview is requested, and aren’t available
immediately after the file is uploaded.

`renditionUrl` String URL to the 240 x 180 pixel rendition resource for the 36.0
`240By180` file. For shared files, renditions process
asynchronously after upload. For private files,
renditions process when the first file preview is
requested, and aren’t available immediately after the
file is uploaded.

`renditionUrl` String URL to the 720 x 480 pixel rendition resource for the 36.0
`720By480` file. For shared files, renditions process
asynchronously after upload. For private files,
renditions process when the first file preview is
requested, and aren’t available immediately after the
file is uploaded.

`sharingOption` `ConnectApi.` Sharing option of the file. Values are: 36.0

```
             FileSharingOption
```

**•** `Allowed` —Resharing of the file is allowed.

**•** `Restricted` —Resharing of the file is
restricted.

`textPreview` String Text preview of the file if available; `null` otherwise. 36.0

`thumb120By90` String Specifies the rendering status of the 120 x 90 preview 36.0
`RenditionStatus` image of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`thumb240By180` String Specifies the rendering status of the 240 x 180 36.0
`RenditionStatus` preview image of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`thumb720By480` String Specifies the rendering status of the 720 x 480 36.0
`RenditionStatus` preview image of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`title` String Title of the file. 36.0

`versionId` String Version ID of the file. 36.0

SEE ALSO:

ConnectApi.FilesCapability

#### ConnectApi.ContentCapability

If a comment has this capability, it has a file attachment.

Subclass of ConnectApi.FeedElementCapability.

For files attached to a feed post (instead of a comment) in version 36.0 and later, use `ConnectApi.FilesCapability` .

If content is deleted from a feed element after it’s posted or if the access to the content is changed to private, the
#### ConnectApi.ContentCapability exists, however most of its properties are null.

**Property Name** **Type** **Description** **Available Version**

`checksum` String MD5 checksum for the file. 32.0

`contentUrl` String URL of the content for links and Google docs. 32.0

`description` String Description of the attachment. 32.0

`downloadUrl` String URL to the content. 32.0

`fileExtension` String Extension of the file. 32.0

`fileSize` String Size of the file in bytes. If size cannot be determined, 32.0
returns `Unknown` .

`fileType` String Type of file. 32.0

`hasPdfPreview` Boolean `true` if the file has a PDF preview available, `false` 32.0
otherwise.

`id` String 18-character ID of the content. 32.0

`isInMyFileSync` Boolean `true` if the file is synced with Salesforce Files Sync; 32.0
`false` otherwise.

Note: Salesforce Files Sync was retired on
May 25, 2018.

`mimeType` String MIME type of the file. 32.0

`renditionUrl` String URL to the rendition resource for the file. Renditions 32.0
are processed asynchronously and may not be

available immediately after the file has been
uploaded.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`renditionUrl240By180` String URL to the 240x180 size rendition resource for the 32.0
file. Renditions are processed asynchronously and

may not be available immediately after the file has
been uploaded.

`renditionUrl720By480` String URL to the 720x480 size rendition resource for the 32.0
file. Renditions are processed asynchronously and

may not be available immediately after the file has
been uploaded.

#### sharingOption ConnectApi. Sharing option of the file. Values are: 35.0

```
             FileSharingOption
```

**•** `Allowed` —Resharing of the file is allowed.

**•** `Restricted` —Resharing of the file is
restricted.

`textPreview` String Text preview of the file if available, `null` otherwise. 32.0
The maximum number of characters is 200.

`thumb120By90` String

```
RenditionStatus

```

`thumb240By180` String

```
RenditionStatus

```

`thumb720By480` String

```
RenditionStatus

```

The status of the rendering of the 120x90 pixel sized 32.0
preview image of the file. Should be either
Processing, Failed, Success, or Na if unavailable.

The status of the rendering of the 240x180 pixel sized 32.0
preview image of the file. Should be either
Processing, Failed, Success, or Na if unavailable.

The status of the rendering of the 720x480 pixel sized 32.0
preview image of the file. Should be either
Processing, Failed, Success, or Na if unavailable.

`title` String Title of the file. 32.0

`versionId` String Version ID of the file. 32.0

SEE ALSO:

ConnectApi.CommentCapabilities

#### ConnectApi.ContentHubAllowedItemTypeCollection

The item types that the context user is allowed to create in a repository folder.

**Property Name** **Type** **Description** **Available Version**

```
allowedItemTypes

```

#### List< ConnectApi. A collection of item types that the context user is 39.0

`ContentHub` allowed to create in a repository folder.
`ItemTypeSummary` 


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ContentHubFieldDefinition

A field definition.

**Property Name** **Type** **Description** **Available Version**

`displayName` String Label or caption of this field. 39.0

`isMandatory` Boolean Specifies whether this field is mandatory for the item 39.0
type.

`maxLength` Integer Maximum length of the value of this field. 39.0

`name` String Name of the field. 39.0

```
type

```

SEE ALSO:

#### ConnectApi. Data type of the value of the field. Values are: 39.0

```
ContentHub
```

**•** `BooleanType`
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

#### ConnectApi.ContentHubItemTypeDetail ConnectApi.ContentHubItemTypeDetail

The details of an item type associated with a repository folder.

Subclass of ConnectApi.AbstractContentHubItemType.

**Property Name** **Type** **Description** **Available Version**

```
fields

```

#### List< ConnectApi. A list of fields that the context user is allowed to set 39.0

`ContentHub` in the metadata of this item type.
`FieldDefinition` 

#### ConnectApi.ContentHubItemTypeSummary

The summary of an item type associated with a repository folder.

Subclass of ConnectApi.AbstractContentHubItemType.


Apex Reference Guide ConnectApi Output Classes

No additional properties.

SEE ALSO:

ConnectApi.ContentHubAllowedItemTypeCollection

#### ConnectApi.ContentHubPermissionType

A permission type.

**Property Name** **Type** **Description** **Available Version**

`id` String Internal ID of the permission type in the repository. 39.0

`label` String Label as returned by the repository. 39.0

SEE ALSO:

ConnectApi.ExternalFilePermissionInformation

#### ConnectApi.ContentHubProviderType

The type of repository.

**Property Name** **Type** **Description** **Available Version**

`label` String Localized label of the provider type. 39.0

`type` String Provider type. One of these values: 39.0

**•** `ContentHubBox`

**•** `ContentHubGDrive`

**•** `ContentHubSharepoint`

**•** `ContentHubSharepointOffice365`

**•** `ContentHubSharepointOneDrive`

**•** `SimpleUrl`

SEE ALSO:

#### ConnectApi.ContentHubRepository ConnectApi.ContentHubRepository

A repository.

Subclass of ConnectApi.ActorWithId.

**Property Name** **Type** **Description** **Available Version**

#### authentication ConnectApi.ContentHubRepositoryAuthentication Repository authentication information. 40.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
features

```

#### ConnectApi. Repository features. 39.0

```
ContentHub

RepositoryFeatures

```

`label` String Repository label. 39.0

`name` String Repository name. 39.0

```
providerType

```

#### ConnectApi. Repository provider type. 39.0

```
ContentHub

ProviderType

```

`rootFolderItemsUrl` String URL to the list of items in the repository root folder. 39.0

SEE ALSO:

ConnectApi.ContentHubRepositoryCollection

#### ConnectApi.ContentHubRepositoryAuthentication

Authentication information for a repository.

**Property Name** **Type** **Description** **Available Version**

`authFlowUrl` String 40.0
Depends on the `authProtocol` .

**•** `NoAuthentication`                     - `null` .

**•** `Oauth` —URL to start the OAuth flow.

**•** `Password` —URL to the authentication settings
for external systems.

```
authProtocol

```

#### ConnectApi. Authentication protocol used for the repository. 40.0

ContentHubAuthentication Values are:
Protocol

**•** `NoAuthentication` —Repository doesn’t
require authentication.

**•** `Oauth` —Repository uses OAuth authentication
protocol.

**•** `Password` —Repository uses user name and
password authentication protocol.

`userHas` Boolean Specifies whether the user has credentials or the 40.0
`AuthSettings` administrator configured the external data source to
use the same set of credentials for every user ( `true` ).
Otherwise, `false` .

SEE ALSO:

#### ConnectApi.ContentHubRepository


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ContentHubRepositoryCollection

A collection of repositories.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page of repositories. 39.0

`nextPageUrl` String URL to the next page of repositories, or `null` if there 39.0
isn’t a next page.

`previousPageUrl` String URL to the previous page of repositories, or `null` 39.0
if there isn’t a previous page.

```
repositories

```

#### List< ConnectApi. Collection of repositories. 39.0

```
ContentHub
```

`Repository` 

#### ConnectApi.ContentHubRepositoryFeatures

The features of a repository.

**Property Name** **Type** **Description** **Available Version**

`canBrowse` Boolean Specifies whether the repository’s folder hierarchy 39.0
can be browsed ( `true` ) or not ( `false` ).

`canSearch` Boolean Specifies whether the repository can be searched 39.0
( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.ContentHubRepository ConnectApi.ContentImageFileDetails

Image file details.

**Property Name** **Type** **Description** **Available Version**

`height` Integer Image’s height in pixels. 40.0

`imageFormat` String Image’s format. 40.0

`orientation` String Image’s EXIF orientation value, if present. 40.0

`width` Integer Image’s width in pixels. 40.0

SEE ALSO:

ConnectApi.InlineImageSegment


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ContractOutputRepresentation

Contract list.

**Property Name** **Type** **Description** **Available Version**

`data` List< `String`   - Record IDs of the contacts. 56.0

#### ConnectApi.ConversationApplicationDefinitionDetailRespresentation

Information about the conversation application definition.

**Property Name** **Type** **Description** **Available Version**

`botInfo` `ConnectApi.BotInfo` Basic information of the bot associated with this 54.0
`Representation` conversation application.

`errorMessage` String Error message for the failed get operation. 54.0

```
integration

Application

```

#### ConnectApi. Conversation application integration types. 54.0

`Conversation` Values are:

```
Application
```

**•** `Api`
```
IntegrationType

```

**•** `Api`

**•** `Slack`

`integrationName` String Name of the conversation application. 54.0

`isSuccess` Boolean Success indicator of the get operation. 54.0

`runtimeUrl` String Base URL of the bot runtime API. 54.0

#### ConnectApi.CouponCodeRedemptionCollection

Collection of coupon code redemption results.

**Property Name** **Type** **Description** **Available Version**

#### couponCode List< ConnectApi.Coupon List of coupon code redemption results. 58.0

`RedemptionResults` `CodeRedemptionResult` 
#### ConnectApi.CouponCodeRedemptionResult

Coupon code redemption result.

**Property Name** **Type** **Description** **Available Version**

`availableRedemptions` Integer Number of coupon code redemptions available. 58.0

`couponCode` String Coupon code. 58.0

`errorMsg` String Error message when coupon code redemption isn’t 58.0
successful.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isSuccess` Boolean

Specifies whether increasing or decreasing the 58.0
coupon code redemption is successful ( `true` ) or
not ( `false` ).

`redemptionLimit` Integer Number of coupon code redemptions allowed. 58.0

#### ConnectApi.CreateCreditMemoOutputRepresentation

ID of a created Credit Memo.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`creditMemoId` String ID of the created Credit Memo. 48.0

#### ConnectApi.CreateMultipleInvoicesFromChangeOrdersOutputRepresentation

List of lists of invoices created from change orders for fees.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

List of IDs of invoices created from change orders for 56.0
fees. Include these invoice IDs when calling Ensure
Refunds for the return that the fees applied to.

```
invoices

```

SEE ALSO:

#### List< ConnectApi.

```
ChangeOrdersInvoice
```

`OutputRepresentation` 

createMultipleInvoices(invoicesInput)

#### ConnectApi.CreateOrderPaymentSummaryOutputRepresentation

ID of the created Order Payment Summary.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`orderPayment` String ID of the Order Payment Summary. 48.0

```
SummaryId

#### ConnectApi.CreateSocialNamedCredential

```

Result of a creating a named credential for a social external channel.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`authUrl` String Authentication URL. 64.0

`externalCredentialDeveloperName` String Developer name of the external credential. 64.0

`namedCredentialDeveloperName` String Developer name of the named credential. 64.0

`status` `ConnectApi.SocialStatusRepresentation` Status response specifiying whether the Webstore 64.0
Meta Config entity was successfully created.

#### ConnectApi.CreateWebStoreMetaConfiguration

Response for a Webstore Meta Config creation request.

**Property Name** **Type** **Description** **Available Version**

`status` `ConnectApi.SocialStatusRepresentation` Specifies whether the Webstore Meta Config entity 64.0
was successfully created ( `true` ) or not ( `false` ).

`webStoreMetaConfig` `ConnectApi.WebStoreMetaConfig` Details of a webstore Meta configuration. 64.0

#### ConnectApi.Credential

Credential.

**Property Name** **Type** **Description** **Available Version**

```
authentication

Protocol

authentication

ProtocolVariant

```

#### ConnectApi. Authentication protocol of the external credential. 56.0

`CredentialAuthentication` Values are:

```
Protocol
```

**•** `AwsSv4`

**•** `Basic`

**•** `Custom`

**•** `Jwt`

**•** `OAuth`

#### ConnectApi. Authentication protocol variant of the external 57.0

`CredentialAuthentication` credential. Values are:

```
ProtocolVariant
```

**•** `AwsSv4_STS` —AWS Signature Version 4 with
Security Token Service.

**•** `ClientCredentialsClientSecret` —OAuth
2.0 Client Credentials client secret. Client secrets
are sent in the callout’s request body.

**•** `ClientCredentialsClientSecretBasic` —OAuth
2.0 Client Credentials client secret. Client secrets
are sent in the callout’s authorization header, as
with Basic authentication.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ClientCredentialsJwtAssertion` —OAuth
2.0 Client Credentials JSON Web Token assertion.

**•** `JwtBearer` —OAuth 2.0 JSON Web Token
bearer flow.

**•** `NoAuthentication` —No authentication.

**•** `RolesAnywhere` —AWS Signature Version 4
with Identity and Access Management (IAM)
Roles Anywhere.

#### authentication ConnectApi. Status of the credential authentication. Values are: 56.0

```
   Status CredentialAuthentication
```

**•** `Configured` —Credential has all required

`Status` credentials for at least one principal.

**•** `NotConfigured` —Credential isn’t
configured.

**•** `Unknown` —Credential status can’t be
determined because the authentication protocol
is custom.

```
credentials

```

Map<String, Map of protocol-specific credentials. 56.0

#### `ConnectApi.`

`CredentialValue` 

`externalCredential` String Fully qualified developer name of the external 56.0
credential.

`principalName` String Name of the external credential named principal. 56.0

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: 56.0

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

#### ConnectApi.CredentialCustomHeader

Credential custom header.

**Property Name** **Type** **Description** **Available Version**

`headerName` String Header name. 57.0

`headerValue` String Header value that can contain formulas. 57.0

`id` String ID of the customer header parameter. 58.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`sequenceNumber` Integer Sequence number of the header. The sequence 57.0
number determines the order of the header.

SEE ALSO:

ConnectApi.ExternalCredential

ConnectApi.NamedCredential

#### ConnectApi.CredentialValue

Credential value.

**Property Name** **Type** **Description** **Available Version**

`encrypted` Boolean Specifies whether the credential value is encrypted 56.0
( `true` ) or not ( `false` ).

`revision` Integer Revision number of a short-lived credential. 58.0

`value` String Value of the credential. 56.0

SEE ALSO:

#### ConnectApi.Credential ConnectApi.CurrencyRecordField

Record field containing a currency value.

Subclass of ConnectApi.LabeledRecordField.

#### ConnectApi.CustomListAudienceCriteria

Criteria for the custom list type of custom recommendation audience.

Subclass of ConnectApi.AudienceCriteria.

**Property Name** **Type** **Description** **Available Version**

`memberCount` Integer Total number of members in the custom 36.0
recommendation audience.

`members` `ConnectApi.UserReferencePage` Members of the custom recommendation audience. 36.0

#### ConnectApi.DashboardComponentSnapshot

Represents both dashboard component snapshots and alerts you receive when a dashboard component value crosses a threshold.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`componentId` String 18-character ID of the dashboard component. 32.0

`componentName` String The dashboard component name. 32.0

`dashboardBodyText` String

Display this text next to the actor in the feed 32.0
element.Use this text in place of the default body
text.

`dashboardId` String 18-character ID of the dashboard. 32.0

`dashboardName` String The name of the dashboard. 32.0

`fullSizeImageUrl` String The source URL to retrieve the full-size image of a 32.0
snapshot. Access this URL with OAuth credentials.

`lastRefreshDate` Datetime ISO 8601 date specifying when this dashboard 32.0
component was last refreshed.

`lastRefresh` String Display text for the last refresh date, for example, “Last 32.0
`DateDisplayText` Refreshed on October 31, 2013.”

#### runningUser ConnectApi. The running user of the dashboard at the time the 32.0

`UserSummary` snapshot was posted. This value may be `null` . Each

dashboard has a running user, whose security settings
determine which data to display in a dashboard.

`thumbnailUrl` String The source URL to retrieve the thumbnail image of a 32.0
snapshot. Access this URL with OAuth credentials.

SEE ALSO:

#### ConnectApi.DashboardComponentSnapshotCapability

ConnectApi.DatacloudCompanies

#### ConnectApi.DashboardComponentSnapshotCapability

If a feed element has this capability, it has a dashboard component snapshot. A snapshot is a static image of a dashboard component
at a specific point in time.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### dashboardComponent ConnectApi.DashboardComponentSnapshot The dashboard component snapshot. 32.0

```
Snapshot

```

SEE ALSO:

ConnectApi.FeedElementCapabilities


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.DataCategoryMetadata

Data category metadata for the object.

**Property Name** **Type** **Description** **Available Version**

`groupName` String Group name of the data category. 63.0

`label` String Label of the data category. 63.0

`values` Map<String, Map of values for the current data category. 63.0

#### `ConnectApi.`

```
             DataCategory
```

`ValueMetadata`            

SEE ALSO:

ConnectApi.ObjectMetadata

#### ConnectApi.DataCategoryValueMetadata

Data category values for the object's data category.

**Property Name** **Type** **Description** **Available Version**

`label` String Label of the data category group. 63.0

`valueName` String Name of the data category group. 63.0

SEE ALSO:

ConnectApi.ObjectMetadata

#### ConnectApi.DataConnector

Details about the data connector for an activation target.

**Property Name** **Type** **Description** **Available Version**

`outputFormat` String Output format for the activation target. 60.0

#### ConnectApi.DataGraphField

Represents a field of a data graph.

**Property Name** **Type** **Description** **Available Version**

`ciFieldType` `DaoObjectFieldTypeQueryEnum` Type of the calculated insight field. 59.0

**•** `Dimension`

**•** `Measure`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ObjectTypeUnspecified`

`dataGraphFieldDevName` String Developer name of the field. 61.0

`dataType` String Data type of the field. 59.0

`developerName` String Developer name of the data graph. 59.0

`isProjected` String Indicates whether the field needs to be projected in 59.0
output JSON ( `true` ) or not ( `false` ).

`keyCol` String Indicates whether the field is a primary key ( `true` ) 59.0
or not ( `false` ).

`keyQualifierName` String Qualifier name of the key for the field. 59.0

`length` String Length of the field. 59.0

`lookupCol` String Lookup column for the field. 59.0

`usageTag` String Indicates whether the field represents a key qualifier 59.0
field ( `KEY_QUALIFIER` ) or not ( `NONE` ).

#### ConnectApi.DataGraphIdsDmo

Represents data about the Data Model Object (DMO) that contains the ID table for the data graph.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Developer name of the DMO. 61.0

#### fields List< ConnectApi.DataGraphIdsDmoField > List of fields for the DMO. 59.0 ConnectApi.DataGraphIdsDmoField

Represents the fields of the Data Model Object (DMO) that contains the ID table for the data graph.

**Property Name** **Type** **Description** **Available Version**

`capabilities` List< `Integer`   - List of capabilities for the DMO field. 61.0

`dataType` String Data type of the DMO field. 61.0

`developerName` String Developer name of the DMO field. 61.0

#### ConnectApi.DataGraphObjectData

Represents object metadata for a data graph.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`dataGraphSourceDevName` String Developer name of the source data graph for the 61.0
data object.

`developerName` String Developer name of the data object for the data graph. 59.0

`fields` List< `ConnectApi.DataGraphField`   - List of fields for the data object of the data graph. 59.0

`filterCriteria` String Filter criteria for the data object of the data graph. 59.0

`memberDmoName` String Name of the member Data Model Object (DMO) for 59.0
the data graph.

#### paths <List ConnectApi.DataGraphRelationship > List of data path relationships for the object data of 59.0

the data graph.

`recencyCriteria` List< `ConnectApi.RecencyCriteria`   - List of recency criteria for the object data of the data 59.0
graph.

`relatedObjects` List< `ConnectApi.DataGraphObjectData`   - Recursive list of related data objects for the data 59.0
graph.

`type` `DataGraphObjectTypeEnum` Data type of the data object for the data graph. 59.0

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

#### ConnectApi.DataGraphRelationship

Represents the relationship of a field of the object data for the data graph.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`cardinality` `RelationshipCardinality` Cardinality of the relationship of a field for object data 59.0
of the data graph.

**•** `CardinalityUnspecified`

**•** `ManyToOne`

**•** `OneToMany`

**•** `OneToOne`

`fieldName` String Field name of the object data for the data graph. 59.0

`parentFieldName` String Parent field name of the object data for the data 59.0
graph.

#### ConnectApi.DataGraphValuesDmo

Represents data about the Data Model Object (DMO) that contains the JSON records for the data graph.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Developer name of the DMO. 61.0

#### fields <List ConnectApi.DataGraphValuesDmoField > List of fields for the DMO. 59.0 ConnectApi.DataGraphValuesDmoField

Represents the fields of the Data Model Object (DMO) that contains the JSON records for the data graph.

**Property Name** **Type** **Description** **Available Version**

`capabilities` List< `Integer`   - List of capabilities for the DMO field. 61.0

`dataType` String Data type of the DMO field. 61.0

`developerName` String Developer name of the DMO field. 61.0

#### ConnectApi.DataSpaceCollectionRepresentation

Represents a collection of all data spaces that a user is assigned to.

**Property Name** **Type** **Description** **Available Version**

`dataSpaces` <List `ConnectApi.DataSpaceInfoRepresentation`   - List of all data spaces. 62.0

SEE ALSO:

getAllDataSpaces(batchSize, offset, orderBy)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.DataSpaceInfoRepresentation

Represents a data space.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the data space. 62.0

`prefix` String Prefix of the data space. 62.0

`status` `DataSpaceStatusEnum` Status of the data space. 62.0

**•** `Active` —The data space is active.

**•** `Error` —The data space has an error.

**•** `Processing` —The data space is being
processed.

SEE ALSO:

getDataSpace(idOrName)

#### ConnectApi.DataStreamActionResponseOutput

Represents an action on a data stream.

**Property Name** **Type** **Description** **Available Version**

`jobId` String Job Id of the data stream. 62.0

SEE ALSO:

runDataStream(recordIdOrDeveloperName, interactive)

#### ConnectApi.DateEstimationOutputRepresentation

Date estimation for product delivery.

**Property Name** **Type** **Description** **Available Version**

`max` String Maximum estimated date for delivery. 63.0

`min` String Minimum estimated date for delivery. 63.0

`type` String Estimation type. 63.0

#### ConnectApi.DateRecordField

Record field containing a date.

Subclass of ConnectApi.LabeledRecordField.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`dateValue` Datetime

#### ConnectApi.DeleteIntent

Delete intent for a social post.

Date that a machine can read. 29.0

Ignore the trailing `00:00:00.000Z` characters.

**Property Name** **Type** **Description** **Available Version**

#### managedSocialAccount ConnectApi. Managed social account that deletes the social post. 45.0

```
           ManagedSocialAccount

```

SEE ALSO:

#### ConnectApi.DeleteIntents ConnectApi.DeleteIntents

List of delete intents for a social post.

**Property Name** **Type** **Description** **Available Version**

#### deletes List< ConnectApi. List of delete intents for the social post. 45.0

`DeleteIntent`          

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.DeleteSocialPostIntent

Delete intent for the social post.

**Property Name** **Type** **Description** **Available Version**

`socialAccountId` String ID of the social account that deletes the social post. 46.0

`socialPostId` String ID of the social post to delete. 46.0

#### ConnectApi.DeliveryEstimateOutputRepresentation

Delivery estimation information for products.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi.DeliveryEstimationE r orOutputRepresentation Any error that was returned, including the error code 63.0

on page 2280 and error message.

`location` String Location external reference. 63.0

`productDeliverEstimations` ListConnectApi.ProductDeliverEstimationOutputRepresentation List of product delivery estimations. 63.0
on page 2468

`shippingCarrierMethodExternalReference` String Shipping carrier method external reference. 63.0

#### ConnectApi.DeliveryEstimationErrorOutputRepresentation

Delivery estimation error.

**Property Name** **Type** **Description** **Available Version**

`code` String Error code. 63.0

`message` String Error message, if any. 63.0

#### ConnectApi.DigestJob

Represents a successfully enqueued API digest job request.

**Property Name** **Type** **Description** **Available Version**

#### period ConnectApi. Time period that’s included in a Chatter email digest. 37.0

`DigestPeriod` Values are:

**•** `DailyDigest` —The email includes up to the
50 latest posts from the previous day.

**•** `WeeklyDigest` —The email includes up to
the 50 latest posts from the previous week.

#### ConnectApi.DirectMessageCapability

If a feed element has this capability, it’s a direct message.

**Property Name** **Type** **Description** **Available Version**

`memberChanges` `ConnectApi.DirectMessageMemberActivityPage` Member activities of the direct message, with the 40.0
most recent activity first.

```
members

```

#### ConnectApi. Members included in the direct message. 39.0

```
DirectMessage

MemberPage

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
originalMembers

```

#### ConnectApi. Original members of the direct message. 40.0

```
DirectMessage

MemberPage

```

`subject` String Subject of the direct message. 39.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.DirectMessageMemberActivity

Direct message member activity.

**Property Name** **Type** **Description** **Available Version**

`activityDate` Datetime Direct message member activity date. 40.0

#### actor ConnectApi. User who changed the direct message membership. 40.0

```
           UserSummary

```

```
membersAdded

membersRemoved

```

SEE ALSO:

#### ConnectApi. Members added to the direct message as part of the 40.0

`DirectMessage` activity.

```
MemberPage

#### ConnectApi. Members removed from the direct message as part 40.0
```

`DirectMessage` of the activity.

```
MemberPage

```

#### ConnectApi.DirectMessageMemberActivityPage ConnectApi.DirectMessageMemberActivityPage

A page of direct message member activities.

**Property Name** **Type** **Description** **Available Version**

```
activities

```

#### List< ConnectApi. Collection of direct message member activities. 40.0

```
DirectMessage
```

`MemberActivity` 

`currentPageToken` String Token identifying the current page. 40.0

`currentPageUrl` String Connect REST API URL identifying the current page. 40.0

`nextPageToken` String Token identifying the next page, or `null` if there 40.0
isn’t a next page.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`nextPageUrl` String Connect REST API URL identifying the next page, or 40.0
`null` if there isn’t a next page.

SEE ALSO:

ConnectApi.DirectMessageCapability

#### ConnectApi.DirectMessageMemberPage

A collection of direct message members.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Page token to access the current page of direct 39.0
message members.

`currentPageUrl` String URL to the current page of direct message members. 39.0

`nextPageToken` String Page token to access the next page of direct message 39.0
members.

`nextPageUrl` String URL to the next page of direct message members. 39.0

#### users List< ConnectApi. Collection of direct message members. 39.0

`UserSummary`            

SEE ALSO:

ConnectApi.DirectMessageCapability

ConnectApi.DirectMessageCapability

ConnectApi.DirectMessageMemberActivity

#### ConnectApi.DistanceCalculationOutputRepresentation

Shipping distance data for a set of inventory locations.

**Property Name** **Type** **Description** **Available Version**

`averageDistance` Double The average distance from the locations to the order 51.0
recipient.

```
locations

```

#### List< ConnectApi. The list of locations and their distances to the order 51.0

`LocationOutput` recipient.
`Representation` 

`rank` Integer This result’s rank among all results by average 51.0
distance to the order recipient.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.DistinctFacetValue

Distinct facet value.

This class is a subclass of ConnectApi.FacetValue.

**Property Name** **Type** **Description** **Available Version**

```
displayMetadata

```

#### ConnectApi.DistinctFacetValue Map of metadata required for rendering the facet 64.0

`DisplayMetadata` value.
`Representation` on
page 2283

`displayName` String Display name of the facet value. 52.0

`nameOrId` String Developer name of the attribute. 52.0

`productCount` Long Number of products in the search result that match 52.0
the facet value.

SEE ALSO:

#### ConnectApi.DistinctValueSearchFacet ConnectApi.DistinctFacetValueDisplayMetadataRepresentation

Display metadata representation for a distinct facet value.

**Property Name** **Type** **Description** **Available Version**

`swatch` Map<String, String> Map of swatch display metadata for the distinct facet 64.0
value.

#### ConnectApi.DistinctValueSearchFacet

Facet with distinct values in product search results.

This class is a subclass of ConnectApi.SearchFacet.

**Property Name** **Type** **Description** **Available Version**

#### values List< ConnectApi. Values of the facet found in the search result. Sorted 52.0

`DistinctFacetValue`           - by display name in alphabetical order.

#### ConnectApi.DistributePickedQuantitiesOutputRepresentation

Output representation of where the quantities were distributed in orders and any remaining quantity

**Property Name** **Type** **Description** **Available Version**

`fullyDistributed` <List `ConnectApi.OrderQuantitiesOutputRepresentation` - Orders that have all quantities distributed. 58.0

```
OrdersList

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`notDistributed` <List `ConnectApi.OrderQuantitiesOutputRepresentation`   - Orders that have no quantities available after 58.0
`OrdersList` distribution.

`partially` <List `ConnectApi.OrderQuantitiesOutputRepresentation`   - Orders that have partially distributed quantities after 58.0
`Distributed` distribution.

```
   OrdersList

```

`quantities` <List `ConnectApi.ItemQuantityOutputRepresentation`   - Quantities remaining after the distribution. 58.0

```
   RemainingList

#### ConnectApi.DmoFilter

```

Represents a DMO filter output.

**Property Name** **Type** **Description** **Available Version**

`entityFilter` `ConnectApi.BaseComparison` Filter for the entity. 60.0

`entityFilterType` String Type of DMO filter. 60.0

`entityName` String Entity name of the DMO filter. 60.0

#### filterLimit ConnectApi.DmoFilterLimit Limit for the DMO filter. 60.0

`inheritedFilter` `ConnectApi.BaseComparison` Inherited filter. 60.0

`inheritedFilterType` String Type of inherited filter. 60.0

#### pathFromActivateOnToContainer List< ConnectApi. Path from the activation to the container. 60.0

`QueryPathConfigList`               
#### pathFromContainerToEntity List< ConnectApi. Path from the container to the entity. 60.0

`QueryPathConfigList`               
#### ConnectApi.DmoFilterLimit

Represents a DMO filter limit output.

**Property Name** **Type** **Description** **Available Version**

`attributeName` String Name of the attribute for the DMO filter limit. 60.0

`maxNumberOfValues` Integer Max number of values for the DMO filter limit. 60.0

`order` `FilterSortOrderEnum` The sort order for filtering. 60.0

**•** `FilterSortOrderAsc`

**•** `FilterSortOrderDesc`


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.DmoFilterConfig

Represents a DMO filter configuration output.

**Property Name** **Type** **Description** **Available Version**

#### filters List< ConnectApi.DmoFilter > List of activation DMO filters. 60.0 ConnectApi.DownVoteSummary

Summary of a downvote.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.EditCapability

If a feed element or comment has this capability, users who have permission can edit it.

**Property Name** **Type** **Description** **Available Version**

`isEditRestricted` Boolean Specifies whether editing this feed element or 34.0
comment is restricted. If `true`, the context user can’t

edit this feed element or comment. If `false`, the
context user may or may not have permission to edit
this feed element or comment. To determine if the
context user can edit a feed element or comment,
use the

```
                        isFeedElementEditableByMe(communityId,
```

`feedElementId)` or

```
                        isCommentEditableByMe(communityId,
```

`commentId)` method.

`isEditable` String The URL to check if the context user is able to edit 34.0
`ByMeUrl` this feed element or comment.

`lastEditedBy` `ConnectApi.Actor` Who last edited this feed element or comment. 34.0

`lastEditedDate` Datetime The most recent edit date of this feed element or 34.0
comment.

`latestRevision` Integer The most recent revision of this feed element or 34.0
comment.

`relativeLast` String Relative last edited date, for example, “2h ago.” 34.0

```
   EditedDate

```

SEE ALSO:

ConnectApi.CommentCapabilities

ConnectApi.FeedElementCapabilities


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.EgressPropertiesRepresentation

Represents the details for egress properties of the activation target.

**Property Name** **Type** **Description** **Available Version**

`childFolder` String Path of the child folder. 60.0

`customFilename` String

Custom name of the output file. Either 60.0
`customFilename` or
`predeterminedFilename` must be present.

`fileNameType` `EgressFileNameTypeEnum` Type of egress file name. 60.0

**•** `Custom`

**•** `Predetermined`

`filenameDateSuffixFormat` String Date suffix format for the output file name. 60.0

`isSubfolderCreationEnabled` Boolean Indicates whether subfolder creation is enabled 60.0
( `true` ) or not ( `false` ).

`outputCompressionFormat` `CompressionFormatEnum` Compression format for the output file. 60.0

**•** `Bzip2`

**•** `Gzip`

**•** `None` -No compression

`outputDelimiter` `FileDelimiterEnum` Field delimiter for the output file. 60.0

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

`outputFormat` String Output format of the activation target. 60.0

`outputMaxFileSizeMegaBytes` Long Maximum size of the output file in megabytes. 60.0

`outputMaxRecordsPerFile` Long Maximum number of records in the output file. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
predeterminedFilename PreDeterminedFileNameEnum

```

Predetermined name of the output file. Either 60.0
`customFilename` or
`predeterminedFilename` must be present.

**•** `Activation`

**•** `Segment`

**•** `SegmentActivation`

#### ConnectApi.EinsteinLlmGenAiSourceReference

Source from a data provider.

**Property Name** **Type** **Description** **Available Version**

```
contents

metadata

```

#### List< ConnectApi. List of values from the source that are used for 62.0

`EinsteinLlmGeneration` grounding a generated response.

```
GenAiSource
```

`ContentInfo` 
#### List< ConnectApi. List of metadata for the source, such as URLs or record 62.0

`EinsteinLlmGeneration` IDs.

```
GenAiSource
```

`ReferenceInfo` 

#### ConnectApi.EinsteinLlmGenerationCitationOutput

Source information associated with a generated response.

**Property Name** **Type** **Description** **Available Version**

```
citedReferences

sourceReferences

```

#### List< ConnectApi. List of metadata for the sources that are cited in the 62.0

`EinsteinLlmGeneration` generated response.
`GenAiCitedReference` 
#### List< ConnectApi. List of sources from one or more data providers. 62.0

```
EinsteinLlmGenAi
```

`SourceReference` 

ConnectApi.EinsteinLlmGenerationContentQualityOutput

Quality information about the generated response.

**Property Name** **Type** **Description** **Available Version**

`isToxicityDetected` Boolean Specifies whether the generated response contains 61.0
toxic language `(true)` or not `(false)` .


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.EinsteinLlmGenerationGenAiCitedReference

Metadata from an input source that is cited in a generated response.

**Property Name** **Type** **Description** **Available Version**

`link` String URL for the source that is cited in a generated 62.0
response.

`sourceObject` String API name of the source record that is cited in a 62.0
`ApiName` generated response.

`sourceObject` String ID of the source record that is cited in a generated 62.0
`RecordId` response.

#### ConnectApi.EinsteinLlmGenerationGenAiSourceContentInfo

Values from a source that is cited in a generated response.

**Property Name** **Type** **Description** **Available Version**

`content` String Text from the source that is cited in the generated 62.0
response.

`fieldName` String API name of the field that is cited in the generated 62.0
response, such as `Opportunity.Amount` .

`objectName` String API name of the object that is cited in the generated 62.0
response, such as `Opportunity` .

#### ConnectApi.EinsteinLlmGenerationGenAiSourceReferenceInfo

Metadata from a source from a data provider.

**Property Name** **Type** **Description** **Available Version**

`link` String URL for the source from the data provider. 62.0

`sourceObject` String API name of the source record. 62.0

```
   ApiName

```

`sourceObject` String ID of the source record. 62.0

```
   RecordId

```

ConnectApi.EinsteinLLMGenerationItemOutput

Generated response from the LLM provider.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
contentQuality

Representation

```

#### ConnectApi. Specifies whether the generated response contains 61.0

`EinsteinLlm` toxic language `(true)` or not `(false)` .

```
Generations

ContentQuality

```

`parameters` String Parameter values for the LLM provider. 60.0

`responseId` String ID of the generated response. 60.0

```
safetyScore

Representation

```

#### ConnectApi. Safety score information related to the generated 60.0

`EinsteinLlm` response.

```
Generation

SafetyScore

Output

```

`text` String Text of generated response. 60.0

ConnectApi.EinsteinLlmGenerationSafetyScoreOutput

Safety score information related to the LLM response.

**Property Name** **Type** **Description** **Available Version**

`hateScore` Double A higher value means the generated response is more 60.0
likely to contain text that expresses, incites, or

promotes hatred, violence, or severe harm towards
the targeted group. Minimum value of `0.0` .
Maximum value of `1.0` .

`physicalScore` Double A higher value means the generated response is more 60.0
likely to contain text with unsafe advice that may

harm the user or others physically, or text that
promotes, encourages, or depicts acts of self-harm.
Minimum value of `0.0` . Maximum value of `1.0` .

`profanityScore` Double A higher value means the generated response is more 60.0
likely to contain swear words, curse words, or

obscene or profane language. Minimum value of
`0.0` . Maximum value of `1.0` .

`safetyScore` Double Overall safety score based on the `hateScore`, 60.0
`physicalScore`, `profanityScore`,

`sexualScore`, `toxicityScore`, and
`violenceScore` . A higher value means the
generated response is more likely to be safe.
Minimum value of `0.0` . Maximum value of `1.0` .

`sexualScore` Double A higher value means the generated response is more 60.0
likely to contain text meant to arouse sexual


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

excitement or promote sexual services. Minimum
value of `0.0` . Maximum value of `1.0` .

`toxicityScore` Double A higher value means the generated response is more 60.0
likely to contain text that is rude, disrespectful, or

unreasonable. Minimum value of `0.0` . Maximum
value of `1.0` .

`violenceScore` Double A higher value means the generated response is more 60.0
likely to contain text that promotes or glorifies

violence or celebrates the suffering or humiliation of
others. Minimum value of `0.0` . Maximum value of
`1.0` .

#### ConnectApi.EinsteinPromptRecordCollectionOutputRepresentation

List of prompt template records.

**Property Name** **Type** **Description** **Available Version**

`hasMoreRecords` Boolean Specifies whether the query returned more prompt 62.0
template records `(true)` or not `(false)` .

```
promptRecords

```

#### List< ConnectApi. List of prompt template records returned. 62.0

```
EinsteinPrompt
```

`RecordRepresentation` 

`totalPromptRecords` Integer Number of prompt template records returned. 62.0

#### ConnectApi.EinsteinPromptRecordFieldRepresentation

Field values for a prompt template record field.

**Property Name** **Type** **Description** **Available Version**

`displayValue` String Visible value of a prompt template record field. 62.0

`value` Object Raw data value of a prompt template record field. 62.0

#### ConnectApi.EinsteinPromptRecordRepresentation

Prompt template record.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the prompt template record. 62.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
childRelationships

```

Map<String, Map of prompt template name and prompt template 62.0
#### ConnectApi. records that are versions of the prompt template.

```
EinsteinPrompt
```

`RecordRepresentation` 

`fields` Map<String, Map of field name and prompt template record fields. 62.0

#### `ConnectApi.`

```
          EinsteinPrompt

          RecordField
```

`Representation`         

`id` String ID of the prompt template record. 62.0

`isStandard` Boolean

Specifies whether the prompt template record is a 62.0
standard prompt template `(true)` or user-created
prompt template `(false)` .

#### ConnectApi.EinsteinPromptTemplateAttachment

Data for file attachments to prompts.

**Property Name** **Type** **Description** **Available Version**

`fileExtension` String Extension of the file attachment. 63.0

`id` String Content document ID of the file attachment. 63.0

`latestPublished` String Content version ID of the file attachment. 63.0

```
Version

```

`title` String Title of the file attachment. 63.0

ConnectApi.EinsteinPromptTemplateGenerationsError

Error response to a prompt template generation request.

**Property Name** **Type** **Description** **Available Version**

`errorMessage` String Message stating the reason for the error, if any. 60.0

`httpErrorCode` String HTTP status code, if any. 60.0

`localized` String Translated error message, if available. 60.0

```
ErrorMessage

```

`messageCode` String Message code associated with the error message, if 60.0
any.


Apex Reference Guide ConnectApi Output Classes

ConnectApi.EinsteinPromptTemplateGenerationsRepresentation

Generated response from the LLM provider and resolved prompt template text.

**Property Name** **Type** **Description** **Available Version**

```
citations

fileData

generationErrors

```

#### ConnectApi. Source information associated with the generated 62.0

`EinsteinLlmGeneration` responses.

```
CitationOutput

```

List<ConnectApi. File data of the input files used in generation. 63.0
EinsteinPrompt
TemplateAttachment>

#### List< ConnectApi. List of errors associated with the generated responses, 60.0

`EinsteinPrompt` if any.

```
Template
```

`GenerationsError` 

#### generations List< ConnectApi. List of generated responses from the LLM provider. 60.0

```
          EinsteinLlm

          GenerationItem
```

`Output`         

`isSummarized` Boolean Specifies whether the generated response contains 61.0
summarized text `(true)` or not `(false)` .

#### parameters ConnectApi. Map of parameters and values for the LLM provider 60.0

`WrappedMapObject` parameters.

`prompt` String Prompt template text with resolved inputs. 60.0

`promptTemplate` String Developer name or ID of the prompt template record. 60.0

```
DevName

```

`requestId` String ID of the generation request sent to the LLM provider. 60.0

```
requestMessages

responseMessages

slotsMasking

Information

```

#### List< ConnectApi. List of resolved prompt templates with masked data 61.0

`EinsteinPrompt` and masking information.

```
TemplateMask
```

`Content` 

#### List< ConnectApi. List of original and placeholder values of the masked 61.0

`EinsteinPrompt` data.
`TemplateMaskData` 

#### List< ConnectApi.

```
EinsteinPrompt

TemplateMask
```

`Content` 

List of generated responses with masked data and 61.0
masking information for the specified prompt
template.

ConnectApi.EinsteinPromptTemplateMaskContentRepresentation

Generated response with masked data and masking information for a prompt template.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`content` String Text of generated response or resolved prompt 61.0
template with masked data.

```
moderation

Settings

```

#### ConnectApi. Data masking settings for the specified prompt 61.0

`EinsteinPrompt` template.

```
TemplateMaskSettings

Representation

```

`role` String Role in the Salesforce role hierarchy of the user 61.0
executing the prompt template.

ConnectApi.EinsteinPromptTemplateMaskDataRepresentation

Information about masked data for a prompt template.

**Property Name** **Type** **Description** **Available Version**

`originalValue` String Original value of the masked data. 61.0

`placeHolder` String Placeholder value of the masked data. 61.0

`recognizers` List<String> Reserved for internal use. 61.0

ConnectApi.EinsteinPromptTemplateMaskSettingsRepresentation

Data masking settings for a prompt template.

**Property Name** **Type** **Description** **Available Version**

`enableModeration` Boolean Specifies whether data masking is enabled `(true)` 61.0
or not `(false)` .

#### ConnectApi.EmailAddress

Email address.

**Name** **Type** **Description** **Available Version**

`displayName` String The display name for the email address. 29.0

`emailAddress` String The email address. 29.0

`relatedRecord` `ConnectApi.RecordSummary` The summary of a related record, for example, a contact or user 36.0
summary.

SEE ALSO:

ConnectApi.EmailMessageCapability


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.EmailAttachment

An email attachment in an email message.

**Property Name** **Type** **Description** **Available Version**

#### attachment ConnectApi. Record summary of the attachment. 36.0

```
             RecordSummary

```

`contentType` String Type of attachment. 36.0

`fileName` String Name of the attachment. 36.0

SEE ALSO:

#### ConnectApi.EmailMessageCapability ConnectApi.EmailMergeFieldCollectionInfo

The merge fields for an object.

**Property Name** **Type** **Description** **Available Version**

`mergeFields` List<String> List of merge fields for a single object. 39.0

SEE ALSO:

#### ConnectApi.EmailMergeFieldInfo ConnectApi.EmailMergeFieldInfo

The map for objects and their merge fields.

**Property Name** **Type** **Description** **Available Version**

```
entityToMerge

FieldsMap

```

Map<String, Map for multiple objects and their merge field 39.0
#### ConnectApi. collections.

```
EmailMergeField
```

`CollectionInfo` 

#### ConnectApi.EmailMessageCapability

If a feed element has this capability, it has an email message from a case.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### attachments List< ConnectApi. Attachments in the email message. 36.0

`EmailAttachment`          


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`automationType` String Automation type of the email message. 63.0

**•** `aiAssisted` —The email message was
created with the assistance of AI.

**•** `aiAutomated` —The email message was
created automatically by AI.

`bccAddresses` List< `ConnectApi.` BCC addresses for the email message. 36.0
`EmailAddress`            

`body` String Body of the email message. 36.0

`ccAddresses` List< `ConnectApi.` CC addresses for the email message. 36.0
`EmailAddress`            

`direction` `ConnectApi.` Direction of the email message. Values are: 32.0

```
             EmailMessageDirection
```

**•** `Inbound` —An inbound message (sent by a
customer).

**•** `Outbound` —An outbound message (sent to a
customer by a support agent).

`emailMessageId` String ID of the email message. 32.0

`emailSize` `ConnectApi.` Size of a case’s email message HTML body. 66.0

```
             EmailMessageSize
```

**•** `Large`                       - `UseLargeHtmlBody` permission
is set, HTML body exceeds 131K characters, and
HTML email display is enabled.

**•** `Normal` —Email message doesn’t meet the
`Large` criteria.

`fromAddress` `ConnectApi.EmailAddress` From address for the email message. 36.0

`htmlExpand` Integer Start location of previous email thread. 47.0

```
   EmailThread

```

`isRichText` Boolean Indicates whether the body of the email message is 36.0
in rich text format.

`status` `ConnectApi.` Status of an email message on a case. Values are: 47.0

```
             EmailMessageStatus
```

**•** `DraftStatus`

**•** `ForwardedStatus`

**•** `NewStatus`

**•** `ReadStatus`

**•** `RepliedStatus`

**•** `SentStatus`

`subject` String Subject of the email message. 32.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`textBody` String Body of the email message. 32.0–35.0

Important: In version 36.0 and later, use the
`body` property.

#### toAddresses List< ConnectApi. To addresses of the email message. 32.0

`EmailAddress`            

`totalAttachments` Integer Total number of attachments in the email message. 38.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.Emoji

An emoji.

**Property Name** **Type** **Description** **Available Version**

`category` String Emoji category. 39.0

`shortcut` String Emoji shortcut. 39.0

`unicodeCharacter` String Emoji’s unicode character. 39.0

SEE ALSO:

#### ConnectApi.EmojiCollection ConnectApi.EmojiCollection

A collection of emoji.

**Property Name** **Type** **Description** **Available Version**

#### emojis List< ConnectApi.Emoji > A collection of emoji. 39.0

SEE ALSO:

ConnectApi.SupportedEmojis

#### ConnectApi.EnhancedLinkCapability

If a feed element has this capability, it has a link that may contain supplemental information like an icon, a title, and a description.

Subclass of ConnectApi.FeedElementCapability.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`description` String A description with a 500 character limit. 32.0

`icon` `ConnectApi.Icon` A icon. 32.0

`linkRecordId` String A ID associated with the link if the link URL refers to 32.0
a Salesforce record.

`linkUrl` String A link URL to a detail page if available content can’t 32.0
display inline.

`title` String A title to a detail page. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.EnsureFundsAsyncOutputRepresentation

ID of the asynchronous background operation. This output only includes the operation ID, regardless of whether a call is made to an
external payment gateway. It doesn’t include any errors from the operation.

Subclass of ConnectApi.BaseAsyncOutputRepresentation.

No additional properties.

SEE ALSO:

ensureFundsAsync(orderSummaryId, ensureFundsInput)

#### ConnectApi.EnsurePaymentCreditOutputRepresentation

A list of payment credits created from the credit memo with success status and error information. Shows all payment credits successfully
issued to the customer's payment methods and any errors encountered during processing.

**Property Name** **Type** **Description** **Available Version**

`paymentCredits` <List `ConnectApi.PaymentCreditOutputRepresentation`   - The list of payment credits that were created. 65.0

#### ConnectApi.EnsureRefundsAsyncOutputRepresentation

ID of the asynchronous background operation. This output only includes the operation ID, regardless of whether a call is made to an
external payment gateway. It doesn’t include any errors from the operation.

Subclass of ConnectApi.BaseAsyncOutputRepresentation.

No additional properties.

SEE ALSO:

ensureRefundsAsync(orderSummaryId, ensureRefundsInput)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.EntityLabel

An entity's label.

**Property Name** **Type** **Description** **Available Version**

`label` String Localized singular label of the entity. 40.0

`labelPlural` String Localized plural label of the entity. 40.0

SEE ALSO:

ConnectApi.RecordSummary

#### ConnectApi.EntityLinkSegment

Entity link segment.

Subclass of ConnectApi.MessageSegment.

**Name** **Type** **Description** **Available**
**Version**

```
motif ConnectApi.Motif

         Class

```

A set of small, medium, and large icons that indicate whether 28.0
the entity is a file, group, record, or user. The motif can also
contain the object’s base color.

#### reference ConnectApi. A reference to the link object if applicable, otherwise, null . 28.0

```
         Reference

#### ConnectApi.EntityRecommendation

```

A Chatter, custom, or static recommendation.

Subclass of ConnectApi.AbstractRecommendation.

**Property Name** **Type** **Description** **Available Version**

`actOnUrl` String

For user, file, group, topic, and record `entity` 32.0
types, use this Connect REST URL with a POST request
to take action on the recommendation.

For `ConnectApi.RecommendedObject`
`entity` types, such as custom recommendations,

use the `actionUrl` property of the
ConnectApi.PlatformAction to take action on the
recommendation.

```
action

```

#### ConnectApi. Specifies the action to take on a recommendation. 32.0

```
Recommendation
```

**•** `follow` —Follow a file, record, topic, or user.
```
ActionType

```

**•** `follow` —Follow a file, record, topic, or user.

**•** `join` —Join a group.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `view` —View a file, group, article, record, user,
custom, or static recommendation.

`entity` `ConnectApi.Actor` The entity with which the receiver is recommended 32.0
to take action.

#### ConnectApi.ErrorResponse

Base error response.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code. 48.0

`message` String More error detail, if available. 48.0

SEE ALSO:

ConnectApi.BaseOutputRepresentation

#### ConnectApi.EstimateDeliveryDateOutputRepresentation

Estimated delivery dates.

**Property Name** **Type** **Description** **Available Version**

`deliveryEstimates` ListConnectApi.DeliveryEstimateOutputRepresentation List of delivery estimations. 63.0
on page 2279

`estimatedDeliveryReference` String Unique code, reference, or identifier for the estimated 63.0
delivery used by external systems.

#### ConnectApi.Extension

An extension.

**Property Name** **Type** **Description** **Available Version**

`alternative` `ConnectApi.Alternative` Alternative representation of the extension. 40.0

```
   Representation

```

`attachmentId` String Attachment ID of the extension. 41.0

`extensionId` String ID of the extension. 40.0

`payload` String Payload associated with the extension. 40.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`payloadVersion` String Payload version that identifies the structure of the 40.0
payload associated with the extension.

SEE ALSO:

ConnectApi.ExtensionsCapability

#### ConnectApi.ExtensionDefinition

An extension's definition.

**Property Name** **Type** **Description** **Available Version**

`canAccess` Boolean Indicates whether users can access the extension 40.0
when it’s associated with a feed element.

`canCreate` Boolean Indicates whether users can create a feed element 40.0
with the extension in the org.

`createdDate` Datetime Date when the extension was created. 40.0

`description` String Description of the extension. 40.0

`iconUrl` String URL to the icon for the extension. 40.0

`id` String ID of the extension. 40.0

```
information

Collection

```

#### List< ConnectApi. Collection of extension information. 40.0

```
AbstractExtension
```

`Information` 

`isEnabled` Boolean Indicates whether the extension is enabled in the 40.0 only
`InCommunity` site.

`isEnabled` Boolean Indicates whether the extension is enabled in the 40.0 only
`InLightningPublisher` Lightning publisher.

`name` String Name of the extension. 40.0

`position` Integer Position in which the extension is displayed in the 41.0
publisher.

SEE ALSO:

#### ConnectApi.ExtensionDefinitions ConnectApi.ExtensionDefinitions

A collection of extension definitions.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page. 40.0

`currentPageUrl` String Connect REST API URL identifying the current page. 40.0

#### extension List< ConnectApi. Collection of extension definitions. 40.0

`Definitions` `ExtensionDefinition`   

`nextPageToken` String Token identifying the next page, or `null` if there 40.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 40.0
`null` if there isn’t a next page.

`total` Integer Total number of extensions returned. 40.0

#### ConnectApi.ExtensionsCapability

If a feed element has this capability, it has one or more extension attachments.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### items List< ConnectApi. List of extensions associated with the feed element. 40.0

`Extension`            

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.ExternalAuthIdentityProvider

External auth identity provider.

**Property Name** **Type** **Description** **Available Version**

```
authenticationFlow

authenticationProtocol

```

#### ConnectApi. Authentication flow to get tokens to call protected 62.0

`IdentityProvider` APIs. Values are:

```
AuthFlow
```

**•** `AuthorizationCode`

#### ConnectApi. Authentication protocol required to access the 62.0

`IdentityProvider` external system. Values are:

```
AuthProtocol
```

**•** `OAuth`

`authorizeUrl` String Authorization endpoint URL for the external system. 62.0

`callbackUrl` String

For the Authorization Code authentication flow, the 62.0
callback URL that's used by the external system after
authorization.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
clientAuthentication

```

```
ConnectApi.

IdentityProvider

ClientAuth

```

Client authentication method that describes how 63.0
credentials are sent to the authorization server. Values
are:

**•** `ClientSecretBasic`

**•** `ClientSecretPost`

`createdByNamespace` String Namespace of the package that created the external 62.0
auth identity provider.

`credentials` List< `ConnectApi.` List of the external auth identity provider credentials. 62.0

```
          ExternalAuth

          IdentityProvider
```

`Credential`         

`description` String Description of the external auth identity provider. 62.0

`fullName` String Full name of the external auth identity provider. The 62.0
full name can include a namespace prefix.

`id` String External auth identity provider ID. 62.0

`label` String External auth identity provider label. 62.0

`parameters` List< `ConnectApi.` List of custom request parameters. 63.0

```
          ExternalAuth

          IdentityProvider
```

`Parameter`         

`standardExternal` String Reference to a standard external auth identity 63.0
`IdentityProvider` provider.

`tokenUrl` String

Token endpoint URL to retrieve tokens from the 62.0
external system. Required for all OAuth 2.0
authentication flows.

`url` String Connect REST API URL for the external auth identity 62.0
provider.

`userInfoUrl` String User info URL to retrieve user profile information from 62.0
the external system.

SEE ALSO:

ConnectApi.ExternalAuthIdentityProviderList

createExternalAuthIdentityProvider(requestBody)

getExternalAuthIdentityProvider(fullName)

updateExternalAuthIdentityProvider(developerName, requestBody)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ExternalAuthIdentityProviderCredential

External auth identity provider credential.

**Property Name** **Type** **Description** **Available Version**

`credentialName` String Name of the external auth identity provider 62.0
credential.

`credentialValue` String Value of the external auth identity provider credential. 62.0

`encrypted` Boolean Indicates whether the external auth identity provider 62.0
credential is encrypted ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.ExternalAuthIdentityProviderCredentials ConnectApi.ExternalAuthIdentityProviderCredentials

List of an external auth identity provider's credentials.

**Property Name** **Type** **Description** **Available Version**

#### credentials <List ConnectApi.ExternalAuthIdentityProviderCredential List of external auth identity provider credentials. 62.0

on page 2303>

SEE ALSO:

getExternalAuthIdentityProviderCredentials(fullName)

createExternalAuthIdentityProviderCredentials(fullName, requestBody)

updateExternalAuthIdentityProviderCredentials(fullName, requestBody)

#### ConnectApi.ExternalAuthIdentityProviderList

List of external auth identity providers in the org.

**Property Name** **Type** **Description** **Available Version**

#### externalAuthIdentityProviders <List ConnectApi.ExternalAuthIdentityProvider List of external auth identity providers. 62.0

on page 2301>

SEE ALSO:

getExternalAuthIdentityProviders()

#### ConnectApi.ExternalAuthIdentityProviderParameter

External auth identity provider parameter.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`parameterName` String The name of the external auth identity provider 63.0
parameter.

```
parameterType

```

#### ConnectApi. Parameter type for an external auth identity provider. 63.0

`ExternalAuth` Values are:

```
IdentityProvider
```

**•** `AuthorizeRequestQueryParameter`
```
ParameterType

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

`parameterValue` String If `parameterType` describes a literal value then 63.0
the literal value is stored in this property.

`sequenceNumber` Integer Specifies the order of parameters to apply when an 63.0
external auth identity provider has more than one

parameter. Priority is from lower to higher numbers,
for example, `1` is the highest priority.

SEE ALSO:

ConnectApi.ExternalAuthIdentityProvider

#### ConnectApi.ExternalCredential

External credential, including the named credentials and principals associated with it and the type and status of each principal.

If you don’t have the View Setup and Configuration permission, some properties are empty or show limited information.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property Name** **Type** **Description** **Available Version**

```
authenticationProtocol

```

#### ConnectApi. Authentication protocol of the external credential. 56.0

`CredentialAuthentication` Values are:

```
Protocol
```

**•** `AwsSv4`

**•** `Basic`

**•** `Custom`

**•** `Jwt`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `OAuth`

```
authenticationProtocol

Variant

authenticationStatus

```

`ConnectApi.` Authentication protocol variant of the external 57.0
`CredentialAuthentication` credential. Values are:

```
ProtocolVariant
```

**•** `AwsSv4_STS` —AWS Signature Version 4 with
Security Token Service.

**•** `ClientCredentialsClientSecret` —OAuth
2.0 Client Credentials client secret. Client secrets
are sent in the callout’s request body.

**•** `ClientCredentialsClientSecretBasic` —OAuth
2.0 Client Credentials client secret. Client secrets
are sent in the callout’s authorization header, as
with Basic authentication.

**•** `ClientCredentialsJwtAssertion` —OAuth
2.0 Client Credentials JSON Web Token assertion.

**•** `JwtBearer` —OAuth 2.0 JSON Web Token
bearer flow.

**•** `NoAuthentication` —No authentication.

**•** `RolesAnywhere` —AWS Signature Version 4
with Identity and Access Management (IAM)
Roles Anywhere.

`ConnectApi.` Status of the credential authentication. Values are: 56.0

```
CredentialAuthentication
```

**•** `Configured` —Credential has all required

`Status` credentials for at least one principal.

**•** `NotConfigured` —Credential isn’t
configured.

**•** `Unknown` —Credential status can’t be
determined because the authentication protocol
is custom.

`createdByNamespace` String Namespace of the package that created the external 59.0
credential.

```
customHeaders

```

List< `ConnectApi.` List of custom headers. 57.0

```
CredentialCustom
```

`Header` 

`developerName` String Fully qualified developer name of the external 56.0
credential.

`id` String External credential ID. 58.0

`masterLabel` String External credential label. 56.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
parameters

principals

```

#### List< ConnectApi. List of parameters of the external credential. 57.0

```
ExternalCredential
```

`Parameter` 
#### List< ConnectApi. List of principals the credential has. 56.0

```
ExternalCredential
```

`Principal` 

#### relatedNamed List< ConnectApi. List of named credentials associated to the external 56.0

`Credentials` `NamedCredential` - credential.

`url` String Connect REST API URL for the external credential. 58.0

SEE ALSO:

#### ConnectApi.ExternalCredentialList

ConnectApi.NamedCredential

#### ConnectApi.ExternalCredentialList

List of external credentials.

**Property Name** **Type** **Description** **Available Version**

#### external List< ConnectApi. List of external credentials. 56.0

`Credentials` `ExternalCredential` 
#### ConnectApi.ExternalCredentialParameter

External credential parameter.

**Property Name** **Type** **Description** **Available Version**

`id` String Parameter ID. 58.0

`parameterDescription` String Parameter description. 58.0

`parameterName` String Parameter name. If the `parameterType` is 57.0
`AuthParameter`, valid values are:

**•** `AwsAccountId` —Valid for AwsSv4.

**•** `AwsProfileArn` —Valid for AwsSv4 with
RolesAnywhere.

**•** `AwsRegion` —Valid for AwsSv4.

**•** `AwsService` —Valid for AwsSv4.

**•** `AwsStsDuration` —Valid for AwsSv4 with
STS or RolesAnywhere.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `AwsStsExternalId` —Valid for AwsSv4 with
STS.

**•** `AwsTrustAnchorArn` —Valid for AwsSv4
with RolesAnywhere.

**•** `Scope` —Valid for OAuth.

Other parameter types can be any value.

```
parameterType

```

#### ConnectApi. Parameter type of the external credential. Values are: 57.0

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

`parameterValue` String Parameter value. If the `parameterType` is 57.0
`JwtBodyClaim` or `JwtHeaderClaim`, the

parameter value can contain formulas. If the
`parameterType` is `AuthProvider` or
`SigningCertificate`, the parameter value is
the fully qualified entity name of the corresponding
entity.

SEE ALSO:

#### ConnectApi.ExternalCredential ConnectApi.ExternalCredentialPrincipal

External credential principal.

If you don’t have the View Setup and Configuration permission, some properties are empty or show limited information.

**Property Name** **Type** **Description** **Available Version**

```
authenticationStatus

```

#### ConnectApi. Status of the credential authentication. Values are: 56.0

```
CredentialAuthentication
```

**•** `Configured` —Credential has all required

`Status` credentials for at least one principal.

**•** `NotConfigured` —Credential isn’t
configured.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Unknown` —Credential status can’t be
determined because the authentication protocol
is custom.

`id` String ID of the external credential principal. 58.0

```
parameters

principalAccess

```

#### List< ConnectApi. List of external credential parameters. 58.0

```
ExternalCredential
```

`Parameter` 
#### List< ConnectApi. List of access entities associated with the external 58.0

`ExternalCredential` credential principal.
`PrincipalAccess` 

`principalName` String Name of the external credential named principal. 56.0

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: 56.0

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

`sequenceNumber` Integer Sequence number of the external credential principal. 58.0

SEE ALSO:

#### ConnectApi.ExternalCredential ConnectApi.ExternalCredentialPrincipalAccess

External credential principal access.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Developer name of the associated access entity. 58.0

`id` String ID of the associated access entity. 58.0

```
type

```

SEE ALSO:

#### ConnectApi. Access type of the external credential principal. Values 58.0

`ExternalCredential` are:

```
PrincipalAccessType
```

**•** `PermissionSet`

**•** `PermissionSetGroup`

**•** `Profile`

#### ConnectApi.ExternalCredentialPrincipal


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ExternalFilePermissionInformation

External file permission information.

**Property Name** **Type** **Description** **Available Version**

#### external List< ConnectApi. Available permission types for the parent folder of 39.0

`FilePermission` `ContentHub` the external file, or `null` for non-external files or
`Types` `PermissionType`   - when

```
                        includeExternalFilePermissionsInfo
```

is `false` .

`external` Boolean `true` if the retrieval of external file information failed 39.0
`FilePermissions` or if

```
   Failure includeExternalFilePermissionsInfo
```

is `false` ; `false` otherwise.

`external` String

```
FilePermissions

InfoFailureReason

```

Explanation of the failure if a failure occurred and 39.0

```
includeExternalFilePermissionsInfo
```

is `true` ; `null` otherwise.

#### external ConnectApi. Sharing status for the external file. Values are: 39.0

```
FileSharing ContentHub
```

**•** `DomainSharing` —File is shared with the

`Status` `ExternalItem` domain.
```
          SharingType
```

**•** `PrivateSharing` —File is private or shared
only with individuals.

**•** `PublicSharing` —File is publicly shared.

Value is `null` for non-external files or when

```
                     includeExternalFilePermissionsInfo
```

is `false` .

#### repository List< ConnectApi. Available public groups in the external repository or 39.0

`PublicGroups` `RepositoryGroupSummary` - `null` for non-external files or when

```
                     includeExternalFilePermissionsInfo
```

is `false` .

SEE ALSO:

ConnectApi.AbstractRepositoryFile

#### ConnectApi.ExternalManagedAccountAddressOutput

Default shipping address for an externally managed account.

**Property Name** **Type** **Description** **Available Version**

`city` String City of the external managed account record. 53.0

`country` String Country of the external managed account record. 53.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`geolocationAccuracy` String Geolocation accuracy of the external managed 53.0
account record.

`latitude` String Latitude of the external managed account record. 53.0

`longitude` String Longitude of the external managed account record. 53.0

`state` String State of the external managed account record. 53.0

`street` String Street of the external managed account record. 53.0

`zip` String Postal code of the external managed account record. 53.0

SEE ALSO:

#### ConnectApi.ExternalManagedAccountOutput ConnectApi.ExternalManagedAccountCollectionOutput

Collection of externally managed accounts.

**Property Name** **Type** **Description** **Available Version**

```
externalManaged

Accounts

```

#### List< ConnectApi. Collection of externally managed accounts. 49.0

```
ExternalManaged
```

`AccountOutput` 

`totalExternal` Integer Total number of externally managed accounts. 49.0

```
ManagedAccounts

#### ConnectApi.ExternalManagedAccountOutput

```

Externally managed account.

**Property Name** **Type** **Description** **Available Version**

`accountId` String ID of the account managed by another account. 49.0

`accountName` String Name of the external managed account record. 53.0

```
address

```

#### ConnectApi. Default shipping address of the external managed 53.0

`ExternalManagedAccount` account.

```
AddressOutput

```

`externalManaged` String ID of the external managed account record. 49.0

```
AccountId

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isMyAccount` Boolean Specifies whether the account is the context user’s 53.0
account ( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.ExternalManagedAccountCollectionOutput

#### ConnectApi.FacetValue

Facet value.

This class is abstract and is a superclass of ConnectApi.DistinctFacetValue.

**Property Name** **Type** **Description** **Available Version**

```
type

```

#### ConnectApi. Search facet type. Value is: 52.0

```
CommerceSearch
```

**•** `DistinctValue`
```
FacetType

```

**•** `DistinctValue`

**•** `Range`

#### ConnectApi.Features

Features available to the context user in the org.

**Property** **Type** **Description** **Available**
**Version**

`activityReminder` Boolean Reserved for future use. 37.0

```
Notifications

Enabled

```

`chatter` Boolean Specifies whether Chatter is enabled. 28.0

`chatterActivity` Boolean Specifies whether user details include information about Chatter activity. 28.0

`chatterAnswers` Boolean Specifies whether Chatter Answers is enabled. 29.0

Note: With the Spring ’18 release, Salesforce no longer supports
Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and
updates are scheduled to end. We recommend transitioning to
[Chatter Questions. For more information, see End of Support for](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)
[Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

`chatter` Boolean Specifies whether user details include global Chatter activity. 28.0

```
GlobalInfluence

```

`chatterGroup` Boolean Specifies whether Chatter groups can have records associated with them. 30.0

```
Records

```


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

`chatterGroup` Boolean Specifies whether Chatter records are implicitly shared among group 30.0
`RecordSharing` members when records are added to groups.

`chatter` Boolean Specifies whether Chatter messages are enabled. 28.0

```
   Messages

```

`chatterTopics` Boolean Specifies whether topics are enabled. 28.0

`communities` Boolean Specifies whether digital experiences is enabled. 31.0

```
   Enabled

```

`community` Boolean Specifies whether moderation is enabled. 29.0

```
   Moderation

```

`community` Boolean Specifies whether reputation is enabled. 32.0

```
   Reputation

```

`customFiscal` Boolean Specifies whether custom fiscal calendar is enabled. 63.0

```
   Calendar

   Enabled

```

`dashboard` Boolean Specifies whether the user can post dashboard component snapshots. 28.0

```
   Component

   Snapshots

```

`default` String ISO code of the default currency. Applicable only when 28.0
`Currency` `multiCurrency` is `false` .

```
   IsoCode

```

`defaultLocale` String Specifies the Default locale. 63.0

`einstein` Boolean Reserved for future use. 46.0

```
   VoiceEnabled

```

`einstein` Boolean Reserved for future use. 46.0

```
   VoiceInPilot

   Enabled

```

`einstein` Boolean Reserved for future use. 46.0

```
   VoiceLogging

   Enabled

```

`einstein` Integer Reserved for future use. 46.0

```
   VoiceProviderId

```

`favorites` Boolean Specifies whether favorites in Lightning are enabled. 41.0

```
   Enabled

```

`feedPolling` Boolean Reserved for future use. 28.0

`feedStream` Boolean Specifies whether Chatter feed streams are enabled. 39.0

```
   Enabled

```


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

`files` Boolean Specifies whether files can act as resources for Connect REST API. 28.0

`filesOnComments` Boolean Specifies whether files can be attached to comments. 28.0

`fiscalYear` Integer

```
StartMonth

```

Specifies the number that corresponds to the month that starts the fiscal 63.0
year for the org. For example, if the org's fiscal year starts in February, the
value is 2.

`forecasting3` Boolean Specifies whether aggregated forecasting is enabled for mobile clients. 38.0

```
Aggregated

Enabled

```

`forecasting` Boolean Specifies whether forecasting is enabled. 38.0

```
Enabled

```

`forecasting` Integer Range of the forecasting period. 38.0

```
PeriodRange

```

`forecasting` Integer Start index for the forecasting period. 38.0

```
PeriodStart

```

`forecasting` `ConnectApi.` Time period used for forecasting. Values are: 38.0

```
PeriodType PeriodType
```

**•** `Month`

**•** `Quarter`

**•** `Week`

**•** `Year`

`groupsCanFollow` Boolean Reserved for future use. 28.0–29.0

`ideas` Boolean Specifies whether Ideas is enabled. 29.0

`liveAgent` String Live Agent host name configured for the org. 41.0

```
HostName

```

`managedTopics` Boolean Specifies whether managed topics are enabled. 32.0

```
Enabled

```

`maxEntity` Integer Specifies the maximum number of feed-enabled entities that can be 39.0
`Subscriptions` subscribed to in a Chatter stream.

```
PerStream

```

`maxFiles` Integer Specifies the maximum number of files that can be added to a feed item. 36.0

```
PerFeedItem

```

`maxStreams` Integer Specifies the maximum number of Chatter streams that a user can have. 39.0

```
PerPerson

```

`mobile` Boolean Reserved for future use. 29.0

```
Notifications

Enabled

```


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

`multiCurrency` Boolean

Specifies whether the org uses multiple currencies ( `true` ) or not 28.0
( `false` ). When `false`, the `defaultCurrencyIsoCode`
indicates the ISO code of the default currency.

`offlineEdit` Boolean Specifies whether the offline object permissions are enabled for Salesforce 37.0
`Enabled` for Android and Salesforce for iOS mobile clients.

`publisherActions` Boolean Specifies whether actions in the publisher are enabled. 28.0

`storeData` Boolean Specifies whether the Salesforce for Android and Salesforce for iOS can 30.0
`OnDevices` use secure, persistent storage on mobile devices to cache data.

```
Enabled

```

`thanksAllowed` Boolean Reserved for future use. 28.0

`trendingTopics` Boolean Specifies whether trending topics are enabled. 28.0

`userNav` Boolean Specifies whether users can customize the navigation bar in Lightning. 41.0

```
ItemsEnabled

```

`usesStartDate` Boolean Specifies whether the calendar year when the fiscal year begins is referred 63.0
`AsFiscalYear` to as the year of the company's fiscal year. For example, if the fiscal year
`Name` begins in November 2025, but is referred to as fiscal year 2026, the value
is `false` .

`viralInvites` Boolean Specifies whether existing Chatter users can invite people in their 28.0
`Allowed` company to use Chatter.

`wave` Boolean Specifies whether CRM Analytics is enabled. 36.0

SEE ALSO:

getSettings()

ConnectApi.OrganizationSettings

#### ConnectApi.Feed

Chatter feed.

**Name** **Type** **Description** **Available**
**Version**

`feedElement` String Connect REST API URL to post feed elements to this subject. 31.0

```
PostUrl

#### feedElements ConnectApi.FeedElementPage Page of feed elements for the feed specified in 40.0
```

`redirectedFeedType` . Otherwise, `null` .

`feedElementsUrl` String Connect REST API URL to feed elements. 31.0

`feedItemsUrl` String Connect REST API URL to feed items. 28.0–31.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`isModifedUrl` String Connect REST API URL with a _`since`_ request parameter that contains 28.0
an opaque token that describes when the feed was last modified. Returns

`null` if the feed isn’t a news feed. Use this URL to poll a news feed for
updates.

Important: This feature is available through a Feed Polling pilot
program. This pilot program is closed and not accepting new
participants.

`pinnedFeed` String URL to pinned feed items. 41.0

```
   ElementsUrl

#### redirected ConnectApi. Filter for the feed specified in redirectedFeedType . Otherwise, 42.0
```

`FeedFilter` `FeedFilter` `null` .

```
redirected

FeedSort

```

#### ConnectApi. Sort order for the feed specified in redirectedFeedType . 42.0

`FeedSort` Otherwise, `null` .

```
Order

```

#### redirected ConnectApi. Specifies which feed is returned if pageSize is specified. Otherwise, 40.0

`FeedType` `FeedType` `null` .

`respectsMute` Boolean Indicates whether the feed respects the mute feature. If `true`, the feed 35.0
shows the ability to mute or unmute each element, depending on the

value of `isMutedByMe` ; `null` if the mute feature is disabled for the
organization.

#### ConnectApi.FeedBody

Feed body.

Subclass of ConnectApi.AbstractMessageBody.

No additional properties.

SEE ALSO:

ConnectApi.Comment

ConnectApi.FeedElement

ConnectApi.FeedEntitySummary

#### ConnectApi.FeedDirectory

Directory of feeds and favorites.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`favorites` `List<ConnectApi.Feed` A list of feed favorites 30.0

```
            Favorite>

```

`feeds` `List<ConnectApi.FeedDirectoryItem>` A list of feeds 30.0

#### ConnectApi.FeedDirectoryItem

Definition of a feed.

**Name** **Type** **Description** **Available**
**Version**

`feedElementsUrl` String Connect REST API resource URL for the feed elements.

`feedItemsUrl` String Connect REST API resource URL for the feed items of a specific feed. 30.0–31.0

```
feedType

```

#### ConnectApi The feed type. One of these values: 30.0

```
.FeedType
```

**•** `Bookmarks` —Contains all feed items saved as bookmarks by the

Enum

context user.

**•** `Company` —Contains all feed items except feed items of type
`TrackedChange` . To see the feed item, the user must have sharing
access to its parent.

**•** `DirectMessageModeration` —Contains all direct messages
that are flagged for moderation. The Direct Message Moderation
feed is available only to users with Moderate Experiences Chatter
Messages permissions.

**•** `DirectMessages` —Contains all feed items of the context user’s
direct messages.

**•** `Draft` —Contains all the feed items that the context user drafted.

**•** `Files` —Contains all feed items that contain files posted by people
or groups that the context user follows.

**•** `Filter` —Contains the news feed filtered to contain feed items
whose parent is a specified object type.

**•** `Groups` —Contains all feed items from all groups the context user
either owns or is a member of.

**•** `Home` —Contains all feed items associated with any managed topic
in an Experience Cloud site.

**•** `Isolated` —Contains all the feed items and comments that are
isolated.

**•** `Landing` —Contains all feed items that best drive user engagement
when the feed is requested. Allows clients to avoid an empty feed
when there aren’t many personalized feed items.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

**•** `Moderation` —Contains all feed items that are flagged for
moderation, except direct messages. The moderation feed is available
only to users with Moderate Experiences Feeds permissions.

**•** `Mute` —Contains all feed items that the context user muted.

**•** `News` —Contains all updates for people the context user follows,
groups the user is a member of, and files and records the user is
following. Contains all updates for records whose parent is the
context user.

**•** `PendingReview` —Contains all feed items and comments that
are pending review.

**•** `People` —Contains all feed items posted by all people the context
user follows.

**•** `Record` —Contains all feed items whose parent is a specified record,
which could be a group, user, object, file, or any other standard or
custom object. When the record is a group, the feed also contains
feed items that mention the group. When the record is a user, the
feed contains only feed items on that user. You can get another user’s
record feed.

**•** `Streams` —Contains all feed items for any combination of up to
25 feed-enabled entities that the context user subscribes to in a
stream. Examples of feed-enabled entities include people, groups,
and records,

**•** `To` —Contains all feed items with mentions of the context user.
Contains feed items the context user commented on and feed items
created by the context user that are commented on.

**•** `Topics` —Contains all feed items that include the specified topic.

**•** `UserProfile` —Contains feed items created when a user changes
records that can be tracked in a feed. Contains feed items whose
parent is the user and feed items that @mention the user. This feed
is different than the news feed, which returns more feed items,
including group updates. You can get another user’s user profile
feed.

`feedUrl` String Connect REST API resource URL for a specific feed 30.0

`keyPrefix` String

A _key prefix_ is the first three characters of a record ID, which specifies the 30.0
object type.

For filter feeds, this value is the key prefix associated with the object type
used to filter this feed. All feed items in this feed have a parent whose

object type matches this key prefix value. For non-filter feeds, this value
is `null` .


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`label` String Localized label of the feed 30.0

SEE ALSO:

ConnectApi.FeedDirectory

#### ConnectApi.FeedElement

Feed elements are the top-level items that a feed contains. Feeds are feed element containers.

This class is abstract.

Superclass of:

**•** ConnectApi.FeedItem

**•** ConnectApi.GenericFeedElement

**Property Name** **Type** **Description** **Available Version**

#### body ConnectApi. Information about the feed element. 22.0

```
             FeedBody
```

Important: Use the `header.text`
property as the default value for rendering
text because the `body.text` property can
be `null` .

```
capabilities

```

#### ConnectApi. A container for all capabilities that can be included 31.0

`FeedElement` with a feed element.

```
Capabilities

```

`createdDate` Datetime ISO 8601 format date string, for example, 31.0
2011-02-25T18:24:31.000Z.

#### feedElementType ConnectApi. Feed elements are the top-level objects that a feed 31.0

`FeedElementType` contains. The feed element type describes the

characteristics of that feed element. One of these
values:

**•** `Bundle` —A container of feed elements. A
bundle also has a body made up of message
segments that can always be gracefully degraded
to text-only values.

**•** `FeedItem` —A feed item has a single parent
and is scoped to oneExperience Cloud site or
across all Experience Cloud sites. A feed item can
have capabilities such as bookmarks, canvas,
content, comment, link, poll. Feed items have a
body made up of message segments that can
always be gracefully degraded to text-only values.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Recommendation` —A recommendation is a
feed element with a recommendations capability.
A recommendation suggests records to follow,
groups to join, or applications that are helpful to
the context user.

#### header ConnectApi. The header is the title of the post. This property 31.0

`MessageBody` contains renderable plain text for all the segments

of the message. If a client doesn’t know how to
render a feed element type, it should render this text.

`id` String 18-character ID of the feed element. 22.0

`modifiedDate` Datetime ISO 8601 format date string, for example, 31.0
2011-02-25T18:24:31.000Z.

#### parent ConnectApi. Feed element’s parent 28.0

```
             ActorWithId

```

`relativeCreated` String The created date formatted as a relative, localized 31.0
`Date` string, for example, “17m ago” or “Yesterday.”

`url` String Connect REST API URL to this feed element. 22.0

SEE ALSO:

ConnectApi.Announcement

ConnectApi.FeedElementPage

ConnectApi.PinnedFeedElements

ConnectApi.QuestionAndAnswersSuggestions

#### ConnectApi.FeedElementCapabilities

A container for all capabilities that can be included with a feed element.

**Property Name** **Type** **Description** **Available Version**

#### approval ConnectApi. If a feed element has this capability, it includes 32.0

`ApprovalCapability` information about an approval.

```
associated

Actions

```

#### ConnectApi. If a feed element has this capability, it has platform 33.0

`AssociatedActions` actions associated with it.

```
Capability

```

#### banner ConnectApi. If a feed element has this capability, it has a banner 31.0

`BannerCapability` motif and style.

#### bookmarks ConnectApi. If a feed element has this capability, the context user 31.0

`BookmarksCapability` can bookmark it.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`bundle` `ConnectApi.` If a feed element has this capability, it has a container 31.0
`BundleCapability` of feed elements called a _bundle_ .

```
callCollaboration

```

`ConnectApi.` If a feed element has this capability, it has a recording 51.0
`CallCollaboration` comment.

```
Capability

```

`canvas` `ConnectApi.` If a feed element has this capability, it renders a 32.0
`CanvasCapability` canvas app.

```
caseComment

chatterLikes

```

`ConnectApi.` If a feed element has this capability, it has a case 32.0
`CaseComment` comment on the case feed.

```
Capability

```

`ConnectApi.` If a feed element has this capability, the context user 31.0
`ChatterLikes` can like it. Exposes information about existing likes.

```
Capability

```

`close` `ConnectApi.` If a feed element has this capability, users with 43.0
`CloseCapability` permission can close it.

`comments` `ConnectApi.` If a feed element or comment has this capability, the 31.0
`CommentsCapability` context user can add a comment to it.

```
content ConnectApi.

          ContentCapability

```

If a comment has this capability, it has a file 32.0–35.0
attachment.

Most `ConnectApi.ContentCapability`
properties are null if the content has been deleted

from the feed element or if the access has changed
to private.

Important: In version 36.0 and later, use the
`files` property.

`dashboardComponent` `ConnectApi.` If a feed element has this capability, it has a 32.0
`Snapshot` `DashboardComponent` dashboard component snapshot. A snapshot is a

`SnapshotCapability` static image of a dashboard component at a specific

point in time.

```
directMessage

```

`ConnectApi.` If a feed element has this capability, it’s a direct 39.0
`DirectMessage` message.

```
Capability

```

`edit` `ConnectApi.` If a feed element has this capability, users who have 34.0
`EditCapability` permission can edit it.

```
emailMessage

```

`ConnectApi.` If a feed element has this capability, it has an email 32.0
`EmailMessage` message from a case.

```
Capability

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
enhancedLink

```

```
ConnectApi.

EnhancedLink

Capability

```

If a feed element has this capability, it has a link that 32.0
may contain supplemental information like an icon,
a title, and a description.

`extensions` `ConnectApi.` If a feed element has this capability, it has one or 40.0
`ExtensionsCapability` more extension attachments.

```
feedEntityShare

```

`ConnectApi.` If a feed element or comment has this capability, a 39.0
`FeedShare` feed entity is shared with it.

```
Capability

```

`files` `ConnectApi.` If a feed element has this capability, it has one or 36.0
`FilesCapability` more file attachments.

`interactions` `ConnectApi.` If a feed element has this capability, it has information 37.0
`InteractionsCapability` about user interactions.

`link` `ConnectApi.` If a feed element has this capability, it has a link. 32.0

```
          LinkCapability

```

`mediaReferences` `ConnectApi.MediaReferenceCapability` If a feed element has this capability, it has one or 41.0
more media references.

`moderation` `ConnectApi.` If a feed element has this capability, users in an 31.0
`ModerationCapability` Experience Cloud site can flag it for moderation.

`mute` `ConnectApi.` If a feed element has this capability, users can mute 35.0
`MuteCapability` it.

`origin` `ConnectApi.` If a feed element has this capability, it was created 33.0
`OriginCapability` by a feed action.

`pin` `ConnectApi.PinCapability` If a feed element has this capability, users who have 41.0
permission can pin it to a feed.

`poll` `ConnectApi.` If a feed element has this capability, it includes a poll. 31.0

```
          PollCapability

```

```
questionAndAnswers

```

```
ConnectApi.

QuestionAnd

AnswersCapability

```

If a feed element has this capability, it has a question 31.0
and comments on the feed element are answers to
the question.

`readBy` `ConnectApi.` If a feed element has this capability, the context user 40.0
`ReadByCapability` can mark it as read.

```
recommendations

recordSnaphot

```

`ConnectApi.` If a feed element has this capability, it has a 32.0
`Recommendations` recommendation.

```
Capability

```

```
ConnectApi.

RecordSnapshot

Capability

```

If a feed element has this capability, it contains all the 32.0
snapshotted fields of a record for a single create
record event.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
socialPost

```

#### ConnectApi. If a feed element has this capability, it can interact 36.0

`SocialPost` with a social post on a social network.

```
Capability

```

#### status ConnectApi. If a feed post or comment has this capability, it has 37.0

`StatusCapability` a status that determines its visibility.

#### `topics ConnectApi.`

```
          TopicsCapability

```

If a feed element has this capability, the context user 31.0
can add topics to it. Topics help users organize and
discover conversations.

```
trackedChanges

upDownVote

```

SEE ALSO:

#### ConnectApi. If a feed element has this capability, it contains all 32.0

`TrackedChanges` changes to a record for a single tracked change event.

```
Capability

#### ConnectApi. If a feed post or comment has this capability, users 41.0
```

`UpDownVote` can upvote or downvote it.

```
Capability

```

#### ConnectApi.FeedElement

ConnectApi.FeedItemSummary

#### ConnectApi.FeedElementCapability

A feed element capability, which defines the characteristics of a feed element.

In API version 30.0 and earlier, most feed items can have comments, likes, topics, and so on. In version 31.0 and later, every feed item
(and feed element) can have a unique set of _capabilities_ . If a capability property exists on a feed element, that capability is available, even
if the capability property doesn’t have a value. For example, if the `ChatterLikes` capability property exists on a feed element (with
or without a value), the context user can like that feed element. If the capability property doesn’t exist, it isn’t possible to like that feed
element. A capability can also contain associated data. For example, the `Moderation` capability contains data about moderation
flags.

This class is abstract.

This class is a superclass of:

**•** ConnectApi.AssociatedActionsCapability

**•** ConnectApi.ApprovalCapability

**•** ConnectApi.BannerCapability

**•** ConnectApi.BookmarksCapability

**•** ConnectApi.BundleCapability

**•** ConnectApi.CallCollaborationCapability

**•** ConnectApi.CanvasCapability

**•** ConnectApi.CaseCommentCapability

**•** ConnectApi.ChatterLikesCapability

**•** ConnectApi.CloseCapability


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.CommentsCapability

**•** ConnectApi.ContentCapability

**•** ConnectApi.DashboardComponentSnapshotCapability

**•** ConnectApi.DirectMessageCapability

**•** ConnectApi.EmailMessageCapability

**•** ConnectApi.EnhancedLinkCapability

**•** ConnectApi.ExtensionsCapability

**•** ConnectApi.FeedEntityShareCapability

**•** ConnectApi.FilesCapability

**•** ConnectApi.InteractionsCapability

**•** ConnectApi.LinkCapability

**•** ConnectApi.MediaReferenceCapability

**•** ConnectApi.ModerationCapability

**•** ConnectApi.MuteCapability

**•** ConnectApi.OriginCapability

**•** ConnectApi.PinCapability

**•** ConnectApi.PollCapability

**•** ConnectApi.QuestionAndAnswersCapability

**•** ConnectApi.ReadByCapability

**•** ConnectApi.RecommendationsCapability

**•** ConnectApi.RecordCapability

**•** ConnectApi.RecordSnapshotCapability

**•** ConnectApi.SocialPostCapability

**•** ConnectApi.StatusCapability

**•** ConnectApi.TopicsCapability

**•** ConnectApi.TrackedChangesCapability

**•** ConnectApi.UpDownVoteCapability

**•** ConnectApi.VerifiedCapability

This class doesn’t have any properties.

#### ConnectApi.FeedElementPage A paged collection of ConnectApi.FeedElement objects.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page. 31.0

`currentPageUrl` String Connect REST API URL identifying the current page. 31.0

#### elements List< ConnectApi. Collection of feed elements. 31.0

`FeedElement`            


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isModifiedToken` String Opaque polling token to use in the _`since`_ 31.0
parameter of the `ChatterFeeds.isModified`

method. The token describes when the feed was last
modified.

Important: This feature is available through
a Feed Polling pilot program. This pilot
program is closed and not accepting new
participants.

`isModifiedUrl` String Connect REST API URL with a _`since`_ request 31.0
parameter that contains an opaque token that

describes when the feed was last modified. Returns

`null` if the feed isn’t a news feed. Use this URL to
poll a news feed for updates.

Important: This feature is available through
a Feed Polling pilot program. This pilot
program is closed and not accepting new
participants.

`nextPageToken` String Token identifying the next page, or `null` if there 31.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 31.0
`null` if there isn’t a next page.

`updatesToken` String

A token to use in a request to the 31.0

```
ConnectApi.ChatterFeeds.getFeedElementsUpdatedSince
```

method.

`updatesUrl` String Connect REST API feed resource containing the feed 31.0
elements that have been updated since the feed was

refreshed. If the feed doesn’t support this feature, the
value is `null` .

SEE ALSO:

ConnectApi.BundleCapability

#### ConnectApi.Feed ConnectApi.FeedEnabledEntity

An entity that can have feeds associated with it.

**Property Name** **Type** **Description** **Available Version**

`id` String The 18-character ID of the record. 39.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`motif` `ConnectApi.Motif` Small, medium, and large icons indicating the 39.0
record's type.

`name` String The localized name of the record. 39.0

`type` String The type of the record. 39.0

`url` String URL to the record. 39.0

SEE ALSO:

ConnectApi.ChatterStream

#### ConnectApi.FeedEntityIsEditable

Indicates if the context user can edit a feed element or comment.

**Property Name** **Type** **Description** **Available Version**

`areAttachments` Boolean

```
EditableByMe

```

`true` if the context user can add and remove 36.0
attachments on the feed element or comment,

`false` otherwise.

`feedEntityUrl` String URL of the feed element or comment. 34.0

`isEditableByMe` Boolean `true` if the context user can edit the feed element 34.0
or comment, `false` otherwise.

#### ConnectApi.FeedEntityNotAvailableSummary

A summary when the feed entity isn’t available.

Subclass of ConnectApi.FeedEntitySummary.

No additional properties.

#### ConnectApi.FeedEntityReadSummary

Summary of the feed post or comment that was read.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.FeedEntityShareCapability

If a feed element or comment has this capability, a feed entity is shared with it.

Subclass of ConnectApi.FeedElementCapability.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
feedEntity

```

SEE ALSO:

#### ConnectApi. The summary of the feed entity that is shared with 39.0

`FeedEntity` the feed element or comment.

```
Summary

```

ConnectApi.FeedElementCapabilities

#### ConnectApi.FeedEntitySummary

The summary of a feed entity that is shared with a feed element.

This class is abstract.

Superclass of:

**•** ConnectApi.FeedItemSummary

**•** ConnectApi.FeedEntityNotAvailableSummary

**Property Name** **Type** **Description** **Available Version**

`actor` `ConnectApi.Actor` Entity that created the feed entity. 39.0

#### body ConnectApi. Information about the feed entity. 39.0

```
           FeedBody

```

`createdDate` Datetime

ISO 8601 date string, for example, 39.0
2011-02-25T18:24:31.000Z, when the entity was
created.

#### feedElementType ConnectApi. Type of feed entity. 39.0

```
          FeedElementType
```

**•** `Bundle` —A container of feed elements. A
bundle also has a body made up of message
segments that can always be gracefully degraded
to text-only values.

**•** `FeedItem` —A feed item has a single parent
and is scoped to oneExperience Cloud site or
across all Experience Cloud sites. A feed item can
have capabilities such as bookmarks, canvas,
content, comment, link, poll. Feed items have a
body made up of message segments that can
always be gracefully degraded to text-only values.

**•** `Recommendation` —A recommendation is a
feed element with a recommendations capability.
A recommendation suggests records to follow,
groups to join, or applications that are helpful to
the context user.

`id` String 18-character ID of the feed entity. 39.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isEntityAvailable` Boolean

Specifies whether the entity is available. If `false`, 39.0
either the user doesn’t have access to the entity or
the entity was deleted.

#### parent ConnectApi. Parent of the feed entity. 39.0

```
           ActorWithId

```

`relativeCreatedDate` String Relative created date, for example, “2h ago.” 39.0

`url` String URL to the feed entity. 39.0

SEE ALSO:

ConnectApi.FeedEntityShareCapability

#### ConnectApi.FeedFavorite

Feed favorite.

**Name** **Type** **Description** **Available Version**

`community` `ConnectApi.Reference` Information about the Experience Cloud site that 28.0
contains the favorite.

`createdBy` `ConnectApi.User` Favorite’s creator. 28.0

```
         Summary

```

`feedUrl` String Connect REST API URL identifying the feed item for 28.0
this favorite.

`id` String Favorite’s 18–character ID. 28.0

`lastViewDate` Datetime ISO 8601 date string, for example, 28.0
2011-02-25T18:24:31.000Z.

`name` String Favorite’s name. 28.0

`searchText` String If the favorite is from a search, contains the search text, 28.0
otherwise, an empty string.

`target` `ConnectApi.Reference` A reference to the topic if applicable, `null` otherwise. 28.0

#### type ConnectApi. An empty string or one of the following values: 28.0

`FeedFavoriteType` Enum

**•** `ListView`

**•** `Search`

**•** `Topic`

`url` String Connect REST API URL to this favorite. 28.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`user` `ConnectApi.User` Information about the user who saved this favorite. 28.0

```
            Summary

```

SEE ALSO:

ConnectApi.FeedDirectory

#### ConnectApi.FeedFavorites ConnectApi.FeedFavorites

Feed favorites.

**Name** **Type** **Description** **Available Version**

`favorites` `List<ConnectApi.Feed` Complete list of favorites. 28.0

```
            Favorite>

```

`total` Integer Total number of favorites. 28.0

#### ConnectApi.FeedItem

Feed item.

Subclass of ConnectApi.FeedElement Class as of version 31.0.

**Name** **Type** **Description** **Available**
**Version**

`actor` `ConnectApi.Actor` The entity that created the feed item. 28.0

#### attachment ConnectApi.FeedItem Information about the attachment. If there is no 28.0–31.0

`Attachment` attachment, returns `null` .

Important: As of version 32.0, use the
inherited `capabilities` property.

`canShare` Boolean

Indicates whether the feed item can be shared. 28.0–38.0

If a feed item has multiple file attachments and at least
one attachment has been deleted or is inaccessible,

the feed item can’t be shared. The `canShare` value
is incorrectly set to `true` in these cases.

Important: As of version 39.0, use the
`isSharable` property.

`clientInfo` `ConnectApi.ClientInfo` Information about the connected app used to 28.0
authenticate the connection.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`comments` `ConnectApi.CommentPage` First page of comments for this feed item. 28.0–31.0

Important: As of version 32.0, use the
inherited

```
                             capabilities.comments.page
```

property.

`event` Boolean `true` if feed item is created due to an event change, 22.0
`false` otherwise.

`hasVerified` Boolean `true` if the feed item has a verified comment, 41.0
`Comment` otherwise `false` .

`isBookmarked` Boolean `true` if the context user has bookmarked this feed 28.0–31.0
`ByCurrentUser` item, otherwise, `false` .

Important: As of version 32.0, use the
inherited

```
                             capabilities.bookmarks.isBookmarkedByCurrentUser
```

property.

`isDelete` Boolean If this property is `true` the comment cannot be 28.0
`Restricted` deleted by the context user. If it is `false`, it might
be possible for the context user to delete the
comment, but it is not guaranteed.

`isLikedBy` Boolean `true` if the context user has liked this feed item, 28.0–31.0
`CurrentUser` otherwise, `false` .

Important: As of version 32.0, use the
inherited

```
                             capabilities.chatterLikes.isLikedByCurrentUser
```

property.

`isSharable` Boolean Indicates whether the feed item can be shared. 39.0

`likes` `ConnectApi.ChatterLike` First page of likes for this feed item. 28.0–31.0

```
            Page
```

Important: As of version 32.0, use the
inherited

```
                             capabilities.chatterLikes.page
```

property.

`likesMessage` `ConnectApi.MessageBody` A message body the describes who likes the feed item. 28.0–31.0

Important: As of version 32.0, use the
inherited

```
                             capabilities.chatterLikes.likesMessage
```

property.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`moderationFlags` `ConnectApi.` Information about the moderation flags on a feed 29.0–30.0
`ModerationFlags` item. If

```
                           ConnectApi.Features.communityModeration
```

is `false`, this property is `null` .

Important: As of version 31.0, use the
inherited

```
                             capabilities.moderation.moderationFlags
```

property.

```
myLike ConnectApi.Reference

```

If the context user has liked the feed item, this 28.0–31.0
property is a reference to the specific like, otherwise,
`null` .

Important: As of version 32.0, use the
inherited

```
  capabilities.chatterLikes.myLike
```

property.

`originalFeedItem` `ConnectApi.Reference` A reference to the original feed item if this feed item 28.0
is a shared feed item, otherwise, `null` .

```
originalFeed ConnectApi.Actor

ItemActor

```

If this feed item is a shared feed item, returns 28.0
information about the original poster of the feed item,
otherwise, returns `null` .

`photoUrl` String URL of the photo associated with the feed item 28.0

`preamble` `ConnectApi.MessageBody` A collection of message segments, including the 28.0-30.0
unformatted text of the message that you can use as

the title of a feed item. Message segments include
name, link, and motif icon information for the actor
that created the feed item.

Important: For API versions 29.0 and 30.0,
use the

```
                          ConnectApi.FeedItem.preamble.text
```

property as the default case to render text. For
API versions 31.0 and later, use the

```
                          ConnectApi.FeedElement.header.text
```

property as the default case to render text.

`topics` `ConnectApi.FeedItemTopicPage` Topics for this feed item. 28.0–31.0

Important: As of version 31.0, use the
inherited

```
                          capabilities.topics.items
```

property.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`type` `ConnectApi.FeedItemType` Type of feed item. 28.0

Important: As of API version 32.0, use the
`capabilities` property to determine
what can be done with a feed item. See
[Working with Feeds and Feed Elements.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/connectapi_features_feeds_feed_elements.htm)

One of these values:

**•** `ActivityEvent` —Feed item generated in
Case Feed when an event or task associated with
a parent record with a feed enabled is created or
updated.

**•** `AdvancedTextPost` —A feed item with
advanced text formatting, such as a group
announcement post.

**•** `ApprovalPost` —Feed item with an approval
capability. Approvers can act on the feed item
parent.

**•** `AttachArticleEvent` —Feed item
generated when an article is attached to a case
in Case Feed.

**•** `BasicTemplateFeedItem` —Feed item
with an enhanced link capability.

**•** `CallLogPost` —Feed item generated when a
call log is saved to a case in Case Feed.

**•** `CanvasPost` —Feed item generated by a
canvas app in the publisher or from Connect REST
API or Connect in Apex. The post itself is a link to
a canvas app.

**•** `CaseCommentPost` —Feed item generated
when a case comment is saved in Case Feed.

**•** `ChangeStatusPost` —Feed item generated
when the status of a case is changed in Case Feed.

**•** `ChatTranscriptionPost` —Feed item
generated in Case Feed when a Live Agent chat
transcript is saved to a case.

**•** `CollaborationGroupCreated` —Feed
item generated when a new public group is
created. Contains a link to the new group.

**•** `CollaborationGroupUnarchived` —Deprecated.
Feed item generated when an archived group is
activated.

**•** `ContentPost` —Feed item with a content
capability.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

**•** `CreateRecordEvent` —Feed item that
describes a record created in the publisher.

**•** `DashboardComponentAlert` —Feed item
with a dashboard alert.

**•** `DashboardComponentSnapshot` —Feed
item with a dashboard component snapshot
capability.

**•** `EmailMessageEvent` —Feed item generated
when an email is sent from a case in Case Feed.

**•** `FacebookPost` —Deprecated. Feed item
generated when a Facebook post is created from
a case in Case Feed.

**•** `LinkPost` —Feed item with a link capability.

**•** `MilestoneEvent` —Feed item generated
when a case milestone is either completed or
reaches a violation status. Contains a link to the
case milestone.

**•** `PollPost` —Feed item with a poll capability.
Viewers of the feed item are allowed to vote on
the options in the poll.

**•** `ProfileSkillPost` —Feed item generated
when a skill is added to a user’s profile.

**•** `QuestionPost` —Feed item generated when
a question is asked.

As of API version 33.0, a feed item of this type can
have a content capability and a link capability.

**•** `ReplyPost` —Feed item generated by a Chatter
Answers reply.

**•** `RypplePost` —Feed item generated when a
user posts thanks.

**•** `SocialPost` —Feed item generated when a
social post is created from a case in Case Feed.

**•** `TextPost` —Feed item containing text only.

**•** `TrackedChange` —Feed item created when
one or more fields on a record have been
changed.

**•** `UserStatus` —Deprecated. A user's post to
their own profile.

`visibility` `ConnectApi.FeedItem` Type of users who can see a feed item. 28.0

```
            VisibilityType
```

**•** `AllUsers` —Visibility is not limited to internal
users.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

**•** `InternalUsers` —Visibility is limited to
internal users.

#### ConnectApi.FeedItemSummary

A feed item summary.

Subclass of ConnectApi.FeedEntitySummary.

**Property Name** **Type** **Description** **Available Version**

```
capabilities

```

#### ConnectApi. Container for all capabilities that can be included 39.0

`FeedElement` with a feed item.

```
Capabilities

```

#### header ConnectApi. Title of the post. This property contains renderable 39.0

`MessageBody` plain text for all the message segments. If a client

doesn’t know how to render a feed element type, it
should render this text.

`modifiedDate` Datetime

When the feed item was modified in the form of an 39.0
ISO 8601 date string, for example,
2011-02-25T18:24:31.000Z.

#### originalFeedItem ConnectApi. Reference to the original feed item if this feed item 39.0

`Reference` is a shared feed item; otherwise, `null` .

```
originalFeed ConnectApi.Actor

ItemActor

```

If this feed item is a shared feed item, information 39.0
about the original poster of the feed item; otherwise,

`null` .

`photoUrl` String URL of the photo associated with the feed item. 39.0

#### visibility ConnectApi. Specifies who can see a feed item. 39.0

```
           FeedItemVisibility
```

**•** `AllUsers` —Visibility is not limited to internal
users.

**•** `InternalUsers` —Visibility is limited to
internal users.

#### ConnectApi.FeedModifiedInfo

Feed modified information.

Important: This feature is available through a Feed Polling pilot program. This pilot program is closed and not accepting new
participants.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`isModified` Boolean

`isModifiedToken` String

`true` if the news feed has been modified since the last time it was 28.0
polled; `false` otherwise. Returns `null` if the feed is not a news
feed.

Opaque polling token to use in the _`since`_ parameter of the 28.0
`ChatterFeeds.isModified` method. The token describes when
the feed was last modified.

`nextPollUrl` String Connect REST API URL with a _`since`_ request parameter that contains 28.0
an opaque token that describes when the feed was last modified.

Returns `null` if the feed isn’t a news feed. Use this URL to poll a news
feed for updates.

#### ConnectApi.FeedPollChoice

Feed poll choice.

**Name** **Type** **Description** **Available Version**

`id` String Poll choice ID. 28.0

`position` Integer The location in the poll where this poll choice exists. The first poll 28.0
choice starts at 1.

`text` String Label text associated with the poll choice. 28.0

`voteCount` Integer Total number of votes for this poll choice. 28.0

`voteCountRatio` Double

SEE ALSO:

ConnectApi.PollCapability

The ratio of total number of votes for this poll choice to all votes cast 28.0
in the poll. Multiply the ratio by 100 to get the percentage of votes
cast for this poll choice.

#### ConnectApi.FeedPostSummary

Summary of the post.

Subclass of ConnectApi.UserActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`feedItemId` String ID of the post. 42.0

#### ConnectApi.FeedReadSummary

Summary of the feed that was read.


Apex Reference Guide ConnectApi Output Classes

Subclass of ConnectApi.UserActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`containerId` String ID of the parent of the feed. 42.0

`feedType` `ConnectApi.FeedType` Type of feed. 42.0

**•** `Bookmarks` —Contains all feed items saved as
bookmarks by the context user.

**•** `Company` —Contains all feed items except feed
items of type `TrackedChange` . To see the
feed item, the user must have sharing access to
its parent.

**•** `DirectMessageModeration` —Contains
all direct messages that are flagged for
moderation. The Direct Message Moderation feed
is available only to users with Moderate
Experiences Chatter Messages permissions.

**•** `DirectMessages` —Contains all feed items
of the context user’s direct messages.

**•** `Draft` —Contains all the feed items that the
context user drafted.

**•** `Files` —Contains all feed items that contain
files posted by people or groups that the context
user follows.

**•** `Filter` —Contains the news feed filtered to
contain feed items whose parent is a specified
object type.

**•** `Groups` —Contains all feed items from all
groups the context user either owns or is a
member of.

**•** `Home` —Contains all feed items associated with
any managed topic in an Experience Cloud site.

**•** `Isolated` —Contains all the feed items and
comments that are isolated.

**•** `Landing` —Contains all feed items that best
drive user engagement when the feed is
requested. Allows clients to avoid an empty feed
when there aren’t many personalized feed items.

**•** `Moderation` —Contains all feed items that
are flagged for moderation, except direct
messages. The moderation feed is available only
to users with Moderate Experiences Feeds
permissions.

**•** `Mute` —Contains all feed items that the context
user muted.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `News` —Contains all updates for people the
context user follows, groups the user is a member
of, and files and records the user is following.
Contains all updates for records whose parent is
the context user.

**•** `PendingReview` —Contains all feed items
and comments that are pending review.

**•** `People` —Contains all feed items posted by all
people the context user follows.

**•** `Record` —Contains all feed items whose parent
is a specified record, which could be a group,
user, object, file, or any other standard or custom
object. When the record is a group, the feed also
contains feed items that mention the group.
When the record is a user, the feed contains only
feed items on that user. You can get another
user’s record feed.

**•** `Streams` —Contains all feed items for any
combination of up to 25 feed-enabled entities
that the context user subscribes to in a stream.
Examples of feed-enabled entities include people,
groups, and records,

**•** `To` —Contains all feed items with mentions of
the context user. Contains feed items the context
user commented on and feed items created by
the context user that are commented on.

**•** `Topics` —Contains all feed items that include
the specified topic.

**•** `UserProfile` —Contains feed items created
when a user changes records that can be tracked
in a feed. Contains feed items whose parent is
the user and feed items that @mention the user.
This feed is different than the news feed, which
returns more feed items, including group
updates. You can get another user’s user profile
feed.

#### ConnectApi.FieldChangeNameSegment

Field change name segment.

Subclass of ConnectApi.MessageSegment.

No additional properties.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.FieldChangeSegment

Field change segment.

Subclass of ConnectApi.ComplexSegment.

No additional properties.

SEE ALSO:

ConnectApi.MoreChangesSegment

#### ConnectApi.FieldChangeValueSegment

Field change value segment.

Subclass of ConnectApi.MessageSegment.

**Name** **Type** **Description** **Available Version**

```
valueType

```

#### ConnectApi. Value type of a field change. 28.0

```
FieldChange
```

**•** `NewValue` —A new value
```
ValueType Enum
```

**•** `OldValue` —An old value

`url` String URL value if the field change is to a URL field (such as 28.0
a web address)

#### ConnectApi.FieldMetadata

Search metadata for the field of an object.

**Property Name** **Type** **Description** **Available Version**

`domain` String The object that the field is associated with. 63.0

`field` String Field path through the object. 63.0

`fieldApiName` String API name of the field. 63.0

#### fieldType ConnectApi. Field type. Values are: 63.0

```
           FieldType
```

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

**•** `Reference`

**•** `RichTextArea`

**•** `Sobject`

**•** `String`

**•** `SwitchablePersonName`

**•** `TextArea`

**•** `Time`

**•** `Url`

`filterable` Boolean Specifies whether the field is filterable ( `true` ) or not 63.0
( `false` ).

`highlightable` Boolean Specifies whether the field is highlightable ( `true` ) 63.0
or not ( `false` ).

`label` String Label of the field. 63.0

`sortable` Boolean Specifies whether the field is sortable ( `true` ) or not 63.0
( `false` ).

SEE ALSO:

ConnectApi.ObjectMetadata


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.FieldValue

Field's value in product search results.

**Property Name** **Type** **Description** **Available Version**

`value` String Value of the field. 52.0

SEE ALSO:

ConnectApi.ProductSummary

#### ConnectApi.File

File.

This class is abstract.

Subclass of ConnectApi.ActorWithId.

Superclass of ConnectApi.FileSummary.

**Name** **Type** **Description** **Available Version**

`checksum` String MD5 checksum for the file. 28.0

`content` Datetime ISO 8601 format date string, for example, 32.0
`ModifiedDate` 2011-02-25T18:24:31.000Z. File-specific modified date, which
is updated only for direct file operations, such as rename.
Modifications to the file from outside of Salesforce can update
this date.

`contentSize` Integer Size of the file in bytes. 28.0

`contentUrl` String If the file is a link, returns the URL, otherwise, the string `null` . 28.0

`createdDate` Datetime ISO 8601 date string when the file was created. 41.0

`description` String Description of the file. 28.0

`downloadUrl` String URL to the file, that can be used for downloading the file. 28.0

`fileExtension` String Extension of the file. 28.0

`fileType` String Type of file, such as PDF, PowerPoint. 28.0

`flashRendition` String Specifies if a flash preview version of the file has been 28.0
`Status` rendered.

Note: Flash renditions were retired on July 16, 2021.

`isFileAsset` Boolean Specifies whether the file is an asset. 46.0


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`isInMyFileSync` Boolean `true` if the file is synced with Salesforce Files Sync; `false` 28.0
otherwise.

Note: Salesforce Files Sync was retired on May 25,
2018.

`isMajorVersion` Boolean `true` if the file is a major version; `false` if the file is a 31.0
minor version. Major versions can’t be replaced.

`mimeType` String File’s MIME type. 28.0

```
moderationFlags ConnectApi.

         ModerationFlags

```

`modifiedDate` Datetime

Information about the moderation flags on a file. If 30.0

```
ConnectApi.Features.communityModeration
```

is `false`, this property is `null` .

ISO 8601 format date string, for example, 28.0
2011-02-25T18:24:31.000Z. Modifications to the file from
within Salesforce update this date.

`name` String Name of the file. 28.0

`origin` String Specifies the file source. Valid values are: 28.0

**•** `Chatter` —file came from Chatter

**•** `Content` —file came from content

`owner` `ConnectApi.User` File’s owner. 28.0

```
         Summary

```

`pdfRendition` String Specifies if a PDF preview version of the file has been 28.0
`Status` rendered.

`publishStatus` `ConnectApi.` Specifies the publish status of the file. 28.0

```
         FilePublishStatus
```

**•** `PendingAccess` —File is pending publishing.

**•** `PrivateAccess` —File is private.

**•** `PublicAccess` —File is public.

`renditionUrl` String URL to the rendition for the file. 28.0

`renditionUrl` String URL to the 240 x 180 rendition resource for the file.For shared 29.0
`240By180` files, renditions process asynchronously after upload. For
private files, renditions process when the first file preview is
requested, and aren’t available immediately after the file is
uploaded.

`renditionUrl` String URL to the 720 x 480 rendition resource for the file.For shared 29.0
`720By480` files, renditions process asynchronously after upload. For
private files, renditions process when the first file preview is
requested, and aren’t available immediately after the file is
uploaded.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`sharingOption` `ConnectApi.` Sharing option of the file. Values are: 35.0

```
            FileSharingOption
```

**•** `Allowed` —Resharing of the file is allowed.

**•** `Restricted` —Resharing of the file is restricted.

`sharingPrivacy` `ConnectApi.` Sharing privacy of a file. Values are: 41.0

```
            FileSharingPrivacy
```

**•** `None` —File is visible to anyone with record access.

**•** `PrivateOnRecords` —File is private on records.

`sharingRole` `ConnectApi.` Sharing role of the file. 28.0

```
            FileSharingType
```

**•** `Admin` —Owner permission, but doesn’t own the file.

**•** `Collaborator` —Viewer permission, and can edit,
change permissions, and upload a new version of a file.

**•** `Owner` —Collaborator permission, and can make a file
private, and delete a file.

**•** `Viewer` —Can view, download, and share a file.

**•** `WorkspaceManaged` —Permission controlled by the
library.

`systemModstamp` Datetime ISO 8601 date string indicating when a user or any automated 41.0
system process, such as a trigger, updated the file.

`textPreview` String Text preview of the file if available; `null` otherwise. 30.0

`thumb120By90` String Specifies the rendering status of the 120 x 90 preview image 28.0
`RenditionStatus` of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`thumb240By180` String Specifies the rendering status of the 240 x 180 preview image 28.0
`RenditionStatus` of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.

`thumb720By480` String Specifies the rendering status of the 720 x 480 preview image 28.0
`RenditionStatus` of the file. One of these values:

**•** `Processing` —Image is being rendered.

**•** `Failed` —Rendering process failed.

**•** `Success` —Rendering process was successful.

**•** `Na` —Rendering is not available for this image.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`title` String Title of the file. 28.0

`versionNumber` String File’s version number. 28.0

#### ConnectApi.FileAsset

An asset file.

**Property Name** **Type** **Description** **Available Version**

`baseAssetUrl` String Base download URL of the asset. 45.0

`baseUnauthenticated` String

```
AssetUrl

```

Base download URL of the asset for unauthenticated 45.0
users if `isVisibleByExternalUsers` is
`true`, otherwise `null` .

`id` String ID of the asset. 45.0

`isVisibleBy` Boolean Indicates whether unauthenticated users can see the 45.0
`ExternalUsers` asset file ( `true` ) or not ( `false` ).

`masterLabel` String Label of the asset. 45.0

`name` String Unique name of the asset. 45.0

`namespacePrefix` String Namespace prefix of the package containing the 45.0
asset.

`type` String Type of asset. 45.0

SEE ALSO:

ConnectApi.Recommendation

ConnectApi.NBANativeRecommendation

#### ConnectApi.FilePreview

A file preview.

**Property Name** **Type** **Description** **Available Version**

#### format ConnectApi. The format of the preview. Values are: 39.0

```
           FilePreviewFormat
```

**•** `Audio` —Preview format is MP3.

**•** `Jpg` —Preview format is JPG.

**•** `Pdf` —Preview format is PDF.

**•** `Svg` —Preview format is compressed SVG.

**•** `Thumbnail` —Preview format is 240 x 180 PNG.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `ThumbnailBig` —Preview format is 720 x 480
PNG.

**•** `ThumbnailTiny` —Preview format is 120 x
90 PNG.

**•** `Video` —Preview format is MP4.

`previewUrlCount` Integer The total number of preview URLs for this preview 39.0
format.

#### previewUrls List< ConnectApi. A list of file preview URLs. 39.0

`FilePreviewUrl`            
#### status ConnectApi. The availability status of the preview. Values are: 39.0

```
             FilePreviewStatus
```

**•** `Available` —Preview is available.

**•** `InProgress` —Preview is being processed.

**•** `NotAvailable` —Preview is unavailable.

**•** `NotScheduled` —Generation of the preview
isn’t scheduled yet.

`url` String The URL for the file preview. 39.0

SEE ALSO:

#### ConnectApi.FilePreviewCollection ConnectApi.FilePreviewCollection

A collection of file previews.

**Property Name** **Type** **Description** **Available Version**

`fileId` String ID of the file. 39.0

#### previews List< ConnectApi. Previews supported for the file. 39.0

`FilePreview`            

`url` String URL to the current page of file previews. 39.0

`versionNumber` String Version number of the file. 40.0

SEE ALSO:

ConnectApi.InlineImageSegment

#### ConnectApi.FilePreviewUrl

A URL to a file preview.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`pageNumber` Integer Preview page number starting from zero, or `null` 39.0
for PDF files.

`previewUrl` String File preview URL. 39.0

SEE ALSO:

ConnectApi.FilePreview

#### ConnectApi.FilesCapability

If a feed element has this capability, it has one or more file attachments.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`items` List< `ConnectApi.Content`   - Collection of files. 36.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.FileSummary

A file summary.

Subclass of ConnectApi.File.

No additional properties.

#### ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation

A list of inventory location combinations that can fulfill an order without exceeding the maximum number of shipments.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
targetLocations

```

SEE ALSO:

#### List< ConnectApi. Each element of the list is a set of inventory locations 51.0

`AvailableLocation` that together can fulfill the order being routed.
`OutputRepresentation` 

findRoutesWithFewestSplits(findRoutesWithFewestSplitsInputRepresentation)

#### ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation

A list of order fulfillment routes with inventory availability information.


Apex Reference Guide ConnectApi Output Classes

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
results

```

SEE ALSO:

#### List< ConnectApi. Each element of the list is the response for one 54.0

`FindRoutesWithFewest` element of the input list.

```
SplitsWithInventory
```

`OutputRepresentation` 

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

#### ConnectApi.FindRoutesWithFewestSplitsWithInventoryOutputRepresentation

Sets of inventory locations that can combine to fulfill an order, with availability data for those locations.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
inventory

targetLocations

```

SEE ALSO:

#### ConnectApi. Inventory availability data for the location groups and 54.0

`OCIGetInventoryAvailability` locations specified in the input.

```
OutputRepresentation

#### List< ConnectApi. Each entry in the list is a set of inventory locations 54.0
```

`AvailableLocation` that can combine to fulfill an order.
`OutputRepresentation` 

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation

#### ConnectApi.FlowApprovalProcess

Details about a flow approval process, its status, and available actions.

**Property Name** **Type** **Description** **Available Version**

`approvalProcess` String The name of the flow approval process. 66.0

```
Name

```

```
availableActions

```

#### List< ConnectApi. Available actions for the flow approval process. 66.0

```
FlowApproval
```

`ProcessAction` 


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isApproval` Boolean Specifies whether one or more approval submissions 66.0
`InProgress` are in progress ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.FlowApprovalProcessCollection ConnectApi.FlowApprovalProcessAction

Available actions for a flow approval process.

**Property Name** **Type** **Description** **Available Version**

`actionLabel` String The label of an available action. 66.0

`actionName` String The name of an available action. 66.0

`inProgressApproval` List<String> List of in-progress approval submission IDs. 66.0

```
   SubmissionIds

```

`url` String The URL of an available action. 66.0

SEE ALSO:

#### ConnectApi.FlowApprovalProcess ConnectApi.FlowApprovalProcessCollection

The results of requesting a flow approval status.

**Property Name** **Type** **Description** **Available Version**

```
flowApproval

Processes

```

#### List< ConnectApi. A list of flow approval processes retrieved with the 66.0

`FlowApproval` specified process names and related record ID.
`Process` 

`relatedRecordId` String The ID of the related record associated with the 66.0
approval submission.

SEE ALSO:

getFlowApprovalProcessWithStatus(relatedRecordId, processNames)

#### ConnectApi.FollowerPage

Page of followers.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

`followers` `List<ConnectApi.` List of subscriptions. 28.0

```
            Subscription>

```

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 28.0
if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 28.0
`null` if there isn’t a previous page.

`total` Integer Total number of followers across all pages. 28.0

#### ConnectApi.FollowingCounts

Following counts.

**Name** **Type** **Description** **Available Version**

`people` Integer Number of people user is following. 28.0

`records` Integer

Number of records user is following. 28.0

Topics are a type of record that can be followed as of version 29.0.

`total` Integer Total number of items user is following. 28.0

SEE ALSO:

ConnectApi.UserDetail

#### ConnectApi.FollowingPage

Page of following subscriptions.

**Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

`following` `List<ConnectApi.` List of subscriptions. 28.0

```
         Subscription>

```

`nextPageUrl` String Connect REST API URL identifying the next page, or 28.0
`null` if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 28.0
or `null` if there isn’t a previous page.

`total` Integer Total number of records being followed across all 28.0
pages.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.FollowIntents

A list of follow intents for a social persona.

**Property Name** **Type** **Description** **Available Version**

```
follows

```

SEE ALSO:

#### List< ConnectApi. List of follow intents for the social persona. 45.0

```
FollowSocial
```

`PersonaIntent` 

ConnectApi.SocialPostIntents

#### ConnectApi.FollowSocialPersonaIntent

Follow intent on a social persona.

**Property Name** **Type** **Description** **Available Version**

#### managedSocialAccount ConnectApi. Managed social account that follows the social 45.0

`ManagedSocialAccount` persona.

`socialPersonaId` String ID of the social persona to follow. 45.0

SEE ALSO:

#### ConnectApi.FollowIntents ConnectApi.Form

Marketing integration form.

**Property Name** **Type** **Description** **Available Version**

`dataExtensionId` String ID of the data extension associated with the 53.0
marketing integration form.

#### formFieldsList ConnectApi. List of form fields associated with the marketing 53.0

`FormFields` integration form.

`formId` String ID of the marketing integration form. 53.0

`formName` String Name of the marketing integration form. 53.0

#### ConnectApi.FormField

Marketing integration form field.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the marketing integration form field. 53.0

#### type ConnectApi. Type of marketing integration form field. Values are: 53.0

```
             FormFieldType
```

**•** `Boolean`

**•** `Date`

**•** `EmailAddress`

**•** `Number`

**•** `Text`

SEE ALSO:

#### ConnectApi.FormFields ConnectApi.FormFields

List of marketing integration form fields.

**Property Name** **Type** **Description** **Available Version**

#### formFields List< ConnectApi. List of form fields associated with the marketing 53.0

`FormField`            - integration form.

SEE ALSO:

#### ConnectApi.Form ConnectApi.FormSubmission

Marketing integration form submission.

**Property Name** **Type** **Description** **Available Version**

`formSubmissionId` String ID of the form submission, representing the 53.0
submission data that was saved.

#### ConnectApi.FormulaScope

Formula scope for a target.

**Property Name** **Type** **Description** **Available Version**

`contextValues` Map<String, String> Map of context values for the scope. 50.0–51.0

Note: In version 52.0 and later, use the
`contextValuesMap` property.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`contextValuesMap` Map<String, Object> Map of context values for the scope. 52.0

`fields` List<String> List of fields of the scope. 50.0

`formula` String Formula of the scope. 50.0

SEE ALSO:

ConnectApi.Target

#### ConnectApi.FulfillmentGroupOutputRepresentation

Information about one FulfillmentOrder from a request to create fulfillment orders from multiple OrderDeliveryGroupSummaries. If the
FulfillmentOrder was created, then its ID is returned. If it failed, then data from the input is returned so you can resubmit it.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`fulfilledFromLocationId` String (Creation failed) The input FulfilledFromLocationId. 50.0

`fulfillmentOrderId` String The FulfillmentOrderId from the successfully created 50.0
FulfillmentOrder.

`fulfillmentType` String (Creation failed) The input FulfillmentType. 50.0

`orderDeliveryGroup` String (Creation failed) The input 50.0
`SummaryId` OrderDeliveryGroupSummaryId.

```
orderItemSummaries

```

#### List< ConnectApi. (Creation failed) The input list of 50.0

`OrderItemSummary` OrderItemSummaries.
`OutputRepresentation` 

`orderSummaryId` String (Creation failed) The input OrderSummaryId. 50.0

`referenceId` String

The referenceId from the FulfillmentGroup input 50.0
representation. Use this value to troubleshoot a
failure.

#### ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation

Wraps the base output.

Subclass of ConnectApi.BaseOutputRepresentation.

No additional properties.

#### ConnectApi.FulfillmentOrderInvoiceOutputRepresentation

ID of the created invoice.

Subclass of ConnectApi.BaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`invoiceId` String ID of the created invoice. 48.0

#### ConnectApi.FulfillmentOrderOutputRepresentation

A list of IDs of the created FulfillmentOrders.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`fulfillment` List<String> A list of IDs of created Fulfillment Orders. 48.0

```
   OrderIds

#### ConnectApi.GatewayLogResponse

```

Gateway log output.

**Property Name** **Type** **Description** **Available Version**

`createdDate` Datetime Date when the gateway log was created. 50.0

`gatewayResultCode` String

Result codes that show the status of a transaction as 50.0
it is passed to the financial institution and then
returned to the client.

`id` String ID of the gateway log record. 50.0

`interactionStatus` String Gateway interaction status. It can be SUCCESS, 50.0
FAILED, or TIMEOUT.

#### ConnectApi.GenericBundleCapability

If a feed element has this capability, the feed element has a group of other feed elements condensed into one feed element. This group
is called a _bundle_ .

Subclass of ConnectApi.BundleCapability.

#### ConnectApi.GenericFeedElement

A concrete implementation of the abstract `ConnectApi.FeedElement` class.

Subclass of ConnectApi.FeedElement.

#### ConnectApi.GetFOCapacityValuesOutputRepresentation

Response to a request for fulfillment order capacity values for one or more locations.

Subclass of ConnectApi.BaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
locations

```

#### List< ConnectApi. List of fulfillment order capacity values for one or 55.0

`LocationCapacity` more locations.
`OutputRepresentation` 

#### ConnectApi.GlobalInfluence

Chatter influence.

**Name** **Type** **Description** **Available Version**

`percentile` String Percentile value for the user’s influence rank within the org or 28.0
Experience Cloud site.

`rank` Integer Number indicating the user’s influence rank, relative to all other 28.0
users within the org or Experience Cloud site.

SEE ALSO:

ConnectApi.UserDetail

#### ConnectApi.GroupChatterSettings

A user’s Chatter settings for a specific group.

**Name** **Type** **Description** **Available Version**

```
emailFrequency

```

#### ConnectApi. The frequency with which a group member receives 28.0

`GroupEmailFrequency` email from a group.

```
on page 2607

```

#### ConnectApi.GroupInformation

Describes the Information section of the group. If the group is private, this section is visible only to members.

**Name** **Type** **Description** **Available Version**

`text` String The text of the “Information” section of the group. 28.0

`title` String The title of the “Information” section of the group. 28.0

SEE ALSO:

ConnectApi.ChatterGroupDetail

#### ConnectApi.GroupMember

Member of a group.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`id` String User’s 18-character ID. 28.0

`lastFeed` Datetime The date and time at which the group member last 31.0
`AccessDate` accessed the group feed.

```
role

```

#### ConnectApi. Type of membership the user has with the group. 28.0

```
GroupMembership
```

**•** `GroupOwner`

`Type` Enum

**•** `GroupOwner`

**•** `GroupManager`

**•** `NotAMember`

**•** `NotAMemberPrivateRequested`

**•** `StandardMember`

`url` String Connect REST API URL to this membership. 28.0

`user` `ConnectApi.User` Information about the user who is subscribed to this 28.0
`Summary` group.

SEE ALSO:

#### ConnectApi.GroupMemberPage ConnectApi.GroupMemberPage

Page of group members.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 28.0

`members` `List<ConnectApi.` List of group members. 28.0
`GroupMember`        
#### myMembership ConnectApi. If the context user is a member of this group, returns 28.0

`Reference` information about that membership, otherwise, `null` .

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 28.0
there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or `null` 28.0
if there isn’t a previous page.

`totalMemberCount` Integer Total number of group members across all pages. 28.0

#### ConnectApi.GroupMembershipRequest

Request to become a group member.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`createdDate` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z. 28.0

`id` String ID for the group membership request object. 28.0

`lastUpdateDate` Datetime ISO 8601 date string, for example, 2011-02-25T18:24:31.000Z. 28.0

#### requestedGroup ConnectApi. Information about the group the context user is requesting 28.0

`Reference` to join.

`responseMessage` String

A message for the user if their membership request is 28.0
declined. The value of this property is used only when the
value of the `status` property is `Declined` .

The maximum length is 756 characters.

#### status ConnectApi. Status of a request to join a private group. Values are: 28.0

```
         GroupMembership
```

**•** `Accepted`
```
         RequestStatus
```

**•** `Declined`
Enum

**•** `Pending`

`url` String URL of the group membership request object. 28.0

`user` `ConnectApi.User` Information about the user requesting membership in a 28.0
`Summary` group.

SEE ALSO:

#### ConnectApi.GroupMembershipRequests ConnectApi.GroupMembershipRequests

Requests to become group members.

**Name** **Type** **Description** **Available Version**

`requests` `List<ConnectApi.Group` Information about group membership requests. 28.0

```
         MembershipRequest>

```

`total` Integer The total number of requests. 28.0

#### ConnectApi.GroupRecord

A record associated with a group.

**Property** **Type** **Description** **Available**
**Version**

`id` String Record’s 18-character ID. 33.0


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Available**
**Version**

#### record ConnectApi. Information about the record associated with the group. 33.0

```
            ActorWithId

```

`url` String Record URL. 33.0

SEE ALSO:

#### ConnectApi.GroupRecordPage ConnectApi.GroupRecordPage A paginated list of ConnectApi.GroupRecord objects.

**Property** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 33.0

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` if 33.0
there isn’t a next page.

`previous` String Connect REST API URL identifying the previous page, or `null` 33.0
`PageUrl` if there isn’t a previous page.

`records` `List<ConnectApi.` List of records on the current page. 33.0

```
            GroupRecord>

```

`totalRecord` Integer Total number of records associated with the group. 33.0

```
   Count

#### ConnectApi.HashtagSegment

```

Hashtag segment.

Subclass of ConnectApi.MessageSegment.

**Name** **Type** **Description** **Available Version**

`tag` String Text of the topic without the hash symbol (#). 28.0

`topicUrl` String

`url` String

Connect REST API Topics resource that searches for the topic: 28.0

```
/services/data/v66.0/chatter

/topics?exactMatch=true&q= topic

```

Connect REST API Feed Items resource URL that searches for the topic 28.0
in all feed items in an organization:

```
/services/data/v66.0/chatter/feed-items?q= topic

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.HideSocialPostIntent

Hide intent for a social post.

**Property Name** **Type** **Description** **Available Version**

`isHidden` Boolean Specifies whether the managed social account hid 45.0
the social post ( `true` ) or not ( `false` ).

#### managedSocialAccount ConnectApi. Managed social account that hides the social post. 45.0

```
             ManagedSocialAccount

```

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.HoldFOCapacityOutputRepresentation

Response to a request to hold fulfillment order capacity at one or more locations. Can correspond to one action call.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
holdFOCapacity

Responses

```

#### List< ConnectApi. List of responses to the requests to hold fulfillment 55.0

`HoldFOCapacity` order capacity at one or more locations.

```
ResponseOutput
```

`Representation` 

#### ConnectApi.HoldFOCapacityResponseOutputRepresentation

Response to a request to hold fulfillment order capacity at one or more locations.

**Property Name** **Type** **Description** **Available Version**

```
capacityResponses

```

#### List< ConnectApi. List of responses to the requests to hold fulfillment 55.0

`CapacityResponse` order capacity at individual locations.
`OutputRepresentation` 

#### ConnectApi.HttpHeaderOutputRepresentation

HTTP header with information about a text classification

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the HTTP header. 59.0

`value` String Value of the HTTP header. 59.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.Icon

Icon.

**Property** **Type** **Description** **Available**
**Version**

`height` Integer The height of the icon in pixels. 28.0

`width` Integer The width of the icon in pixels. 28.0

`url` String The URL of the icon. This URL is available to unauthenticated users. This 28.0
URL does not expire.

SEE ALSO:

ConnectApi.CanvasCapability

ConnectApi.EnhancedLinkCapability

ConnectApi.SocialPostCapability

#### ConnectApi.InlineImageSegment

An inline image in the feed body.

Subclass of ConnectApi.MessageSegment.

**Property Name** **Type** **Description** **Available Version**

`altText` String Alt text for the inline image. 35.0

`contentSize` Integer Size of the file in bytes. 35.0

`fileExtension` String Extension of the file, such as gif. 37.0

`thumbnails` `ConnectApi.File` Information about the available thumbnails for the 35.0
`PreviewCollection` image.

`url` String URL to the latest version of the inline image. 35.0

#### ConnectApi.InsightValuesOutputRepresentation

Insight value details for a business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

`contextId` String Salesforce record ID of the record that the insight is 62.0
based on.

`name` String Name of the Salesforce record that the insight is 62.0
based on.

`previousValue` Double Value of the insight for the previous timeframe based 62.0
on the key performance indicator.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`value` Double Value of the insight for the current timeframe based 62.0
on the key performance indicator.

#### ConnectApi.InsightsOutputRepresentation

Insight details for a business objective, or goal.

**Property Name** **Type** **Description** **Available Version**

`dashboardUrl` String URL to the dashboard where the insight can be 62.0
viewed.

`insightSummaryText` String

A localized, human-readable summary of the insight 62.0
value's performance, including the change from the
previous value.

`name` String Name of the insight. 62.0

```
values

```

#### List< ConnectApi. List of insight categories. 62.0

```
InsightsValues
```

`OutputRepresentation` 

#### ConnectApi.InteractionsCapability

If a feed element has this capability, it has information about user interactions.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`count` Long The number of individual views, likes, and comments 37.0
on a feed post.

Note: This count appears in the UI under the
feed post as the number of views, for example,
“5 views.”

SEE ALSO:

ConnectApi.FeedElementCapabilities

ConnectApi.RelatedQuestion

#### ConnectApi.Invitation

An invitation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`email` String Email address of the user. 39.0

```
status

```

#### ConnectApi. Specifies the status of an invitation to join a group. 39.0

`GroupViral` Values are:

```
InvitationsStatus
```

**•** `ActedUponUser` —The user was added to
the group. An email was sent asking the user to
visit the group.

**•** `Invited` —An email was sent asking the user
to sign up for the org.

**•** `MaxedOutUsers` —The group has the
maximum allowed members.

**•** `MultipleError` —The user wasn’t invited
due to multiple errors.

**•** `NoActionNeededUser` —The user is already
a member of the group.

**•** `NotVisibleToExternalInviter` —The
user is not accessible to the user sending the
invitation.

**•** `Unhandled` —The user couldn’t be added to
the group for an unknown reason.

`userId` String ID of the user. 39.0

SEE ALSO:

#### ConnectApi.Invitations ConnectApi.Invitations

A collection of invitations.

**Property Name** **Type** **Description** **Available Version**

#### invitations List< ConnectApi. Collection of invitations. 39.0

`Invitation`          
#### ConnectApi.ItemQuantityOutputRepresentation

The quantity for a specific item

**Property Name** **Type** **Description** **Available Version**

`externalItemId` String The identifier for the item with quantity 58.0

`quantity` Double Quantity requested for the item 58.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`quantityDistributed` Double Quantity that was distributed to this item 58.0

#### ConnectApi.KnowledgeArticleVersion

A knowledge article version.

**Property Name** **Type** **Description** **Available Version**

`articleType` String Type of the knowledge article. 36.0

`id` String ID of the knowledge article version. 36.0

`knowledgeArticleId` String ID of the corresponding knowledge article. 36.0

`lastPublishedDate` Datetime Last published date of the knowledge article. 36.0

`summary` String Summary of the knowledge article contents. 36.0

`title` String Title of the knowledge article. 36.0

`urlName` String URL name of the knowledge article. 36.0

SEE ALSO:

#### ConnectApi.KnowledgeArticleVersionCollection ConnectApi.KnowledgeArticleVersionCollection

A collection of knowledge article versions.

**Property Name** **Type** **Description** **Available Version**

#### items <List ConnectApi.KnowledgeArticleVersion > A collection of knowledge article versions. 36.0 ConnectApi.LabeledRecordField

Record field containing a label and a text value.

This class is abstract.

Subclass of ConnectApi.AbstractRecordField.

Superclass of:

**•** ConnectApi.CompoundRecordField

**•** ConnectApi.CurrencyRecordField

**•** ConnectApi.DateRecordField

**•** ConnectApi.PercentRecordField

**•** ConnectApi.PicklistRecordField

**•** ConnectApi.RecordField


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.ReferenceField

**•** ConnectApi.ReferenceWithDateRecordField

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

**Name** **Type** **Description** **Available Version**

`label` String Localized string describing the record field. 29.0

`text` String Text value of the record field. All record fields have a text value. To 29.0
ensure that all clients can consume new content, inspect the record

field’s `type` property. If it isn’t recognized, render the text value
as the default case.

#### ConnectApi.LeadStatusPicklistValueAttributes

Lead status picklist value attributes.

Subclass of ConnectApi.AbstractPicklistValueAttributes

**Property Name** **Type** **Description** **Available Version**

`converted` Boolean Specifies whether the lead has a status of converted 66.0
( `true` ) or not ( `false` ).

[For more information, see the LeadStatus object documentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_leadstatus.htm)

#### ConnectApi.LightningExtensionInformation

Lightning extension information.

Subclass of ConnectApi.AbstractExtensionInformation.

**Property Name** **Type** **Description** **Available Version**

`compositionComponent` String Component to use in compose state. 40.0

`headerTextLabel` String Label for the extension’s header. 40.0

`hoverTextLabel` String Label for hovering over the extension. 40.0

`renderComponent` String Component to use in render or preview state. 40.0

SEE ALSO:

ConnectApi.ExtensionDefinition

#### ConnectApi.LikeIntent

Like intent for a social post.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`isLiked` Boolean Specifies whether the managed social account liked 45.0
the social post ( `true` ) or not ( `false` ).

#### managedSocialAccount ConnectApi. Managed social account that likes the social post. 45.0

```
             ManagedSocialAccount

```

SEE ALSO:

#### ConnectApi.LikeIntents ConnectApi.LikeIntents

List of like intents for a social post.

**Property Name** **Type** **Description** **Available Version**

#### likes List< ConnectApi. List of like intents for the social post. 45.0

`LikeIntent`            

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.LikeSocialPostIntent

Like intent on a social post.

**Property Name** **Type** **Description** **Available Version**

`socialAccountId` String ID of the social account that likes the social post. 46.0

`socialPostId` String ID of the social post to like. 46.0

#### ConnectApi.LikeSummary

Summary of a like.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

**Property Name** **Type** **Description** **Available Version**

`likeId` String ID of the like. 42.0

#### ConnectApi.LineItemResponse

Response class that stores information about a list of one or more line items on which the tax engine has calculated tax.


Apex Reference Guide ConnectApi Output Classes

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

`effectiveDate` Datetime The date that the tax calculation takes effect. 55.0

`lineNumber` String System-generated number used to identify the tax 55.0
line.

`productCode` String Product code for the product related to the taxed 55.0
line item.

`quantity` Double Quantity of the taxed line item. 55.0

`taxCode` String Tax code for the taxed line item. 55.0

```
taxes

```

#### List< ConnectApi. Tax details for each line item in a tax line item output. 55.0

```
TaxDetails
```

`Response` 

#### ConnectApi.LinkCapability

If a feed element has this capability, it has a link.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`url` String Link URL. The URL can be to an external site. 32.0

`urlName` String Description of the link. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.LinkMetadata

Metadata for a link.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the link. 42.0

`frameSource` String HTML required to display the resource. 42.0

`height` Integer Height required to display the HTML. 42.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`originalUrl` String Original URL that was used to request the metadata. 42.0

`providerUrl` String URL of the provider that the information is retrieved 42.0
from.

#### source ConnectApi. Source of the link metadata. Values are: 42.0

```
             LinkMetadataSource
```

**•** `None` —Link metadata wasn’t retrieved.

**•** `Sfdc` —Salesforce is the source.

`thumbnailUrl` String Thumbnail of the resource. 42.0

`title` String Title of the link. 42.0

#### type ConnectApi. Type of link that the metadata represents. Values are: 42.0

```
             LinkMetadataType
```

**•** `Error` —Link metadata couldn’t be retrieved.

**•** `Link` —Represents a link.

**•** `None` —Link metadata wasn’t retrieved because
the link isn’t an allowed domain.

**•** `Photo` —Represents a photo.

**•** `Rich` —Represents rich content, typically HTML
content.

**•** `Unknown` —Link metadata was retrieved, but
the type is unknown.

**•** `Video` —Represents a video.

`url` String URL of the image to display, if one is available. 42.0

`width` Integer Width required to display the HTML. 42.0

SEE ALSO:

#### ConnectApi.LinkMetadataCollection ConnectApi.LinkMetadataCollection

Collection of link metadata.

**Property Name** **Type** **Description** **Available Version**

#### linkMetadataList List< ConnectApi. List of metadata for links. 42.0

`LinkMetadata`            
#### ConnectApi.LinkSegment

Link segment.

Subclass of ConnectApi.MessageSegment.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`url` String The link URL. 28.0

#### ConnectApi.LocationCapacityOutputRepresentation

Fulfillment order capacity values for a location.

**Property Name** **Type** **Description** **Available Version**

`assigned` Integer Value of the location’s Assigned Fulfillment Order 55.0
Count.

`capacity` Integer

Value of the location’s Fulfillment Order Capacity. 55.0
This property represents the location’s maximum
capacity.

#### error ConnectApi. Error returned by the request, if any. 55.0

```
           ErrorResponse

```

`heldCapacity` Integer Number of fulfillment orders that the location is 55.0
holding capacity for.

`locationId` String ID of the location. 55.0

#### ConnectApi.LocationOutputRepresentation

An inventory location’s distance to an order recipient.

**Property Name** **Type** **Description** **Available Version**

`distance` Double The distance from the location to the order recipient. 51.0

`locationIdentifier` String The location identifier. 51.0

#### ConnectApi.MaintenanceInfo

Information about the upcoming scheduled maintenance for the organization.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the maintenance. 34.0

`maintenanceTitle` String Title of the maintenance. 34.0

#### maintenanceType ConnectApi. Type of maintenance. Values are: 34.0

```
           MaintenanceType
```

**•** `Downtime` —Downtime maintenance.

**•** `GenerallyAvailable` —Generally available
mode.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `MaintenanceAndAvailable` —Maintenance
with available mode.

**•** `MaintenanceWithDowntime` —Scheduled
maintenance with downtime.

**•** `ReadOnly` —Maintenance with read-only
mode.

`message` Datetime Effective time when users start seeing the 34.0
`EffectiveTime` maintenance message.

`message` Datetime Expiration time of the maintenance message. 34.0

```
   ExpirationTime

```

`scheduledEnd` Datetime

```
Downtime

```

Scheduled end of downtime. `null` for 34.0
`GenerallyAvailable` and `ReadOnly`
maintenance types.

`scheduledEnd` Datetime Scheduled end of maintenance. `null` for 34.0
`MaintenanceTime` `Downtime` maintenance type.

`scheduledStart` Datetime

```
Downtime

```

Scheduled start of downtime. `null` for 34.0
`GenerallyAvailable` and `ReadOnly`
maintenance types.

`scheduledStart` Datetime Scheduled start time of maintenance. `null` for 34.0
`MaintenanceTime` `Downtime` maintenance type.

SEE ALSO:

ConnectApi.OrganizationSettings

#### ConnectApi.ManagedContentAssociations

Content topics associated with managed content.

**Property Name** **Type** **Description** **Available Version**

#### topics List< ConnectApi. A collection of topics associated with the managed 47.0

`TopicSummary`          - content.

SEE ALSO:

ConnectApi.ManagedContentVersion

#### ConnectApi.ManagedContentChannel

Managed content channel.

Subclass of ConnectApi.AbstractManagedContentChannelRepresentation in version 62.0 and later


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`cacheControlMaxAge` Long HTTP cache control max age response header for 55.0
content delivered from the channel.

`channelId` String ID of the managed content channel. 48.0–61.0

`channelName` String Name of the managed content channel. 48.0–61.0

```
channelType

```

`ConnectApi.` Type of managed content channel. Values are: 48.0–61.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

`domain` String ID or name of the domain assigned to the channel. 52.0–61.0

`domainId` String

ID of the domain assigned to the channel. 50.0–51.0

In version 52.0 and later, this information is returned
in the `domain` property.

`domainName` String Name of the domain assigned to the channel. 50.0–61.0

`id` String ID of the managed content channel. 62.0

`isChannelSearchable` Boolean Specifies whether the text contents of the channel 48.0–61.0
are searchable ( `true` ) or not ( `false` ).

`isDedicated` Boolean Specifies whether the channel has off-core dedicated 63.0
`ContentDelivery` content delivery enabled ( `true` ) or not ( `false` ).
Orgs hosted on Hyperforce use off-core dedicated
content delivery to deliver content in public channels
with high performance and low latency.

`isDomainLocked` Boolean Specifies whether the domain is locked and can’t be 50.0–61.0
changed ( `true` ) or not ( `false` ).

`isSearchable` Boolean Specifies whether the text contents of the channel 62.0
are searchable ( `true` ) or not ( `false` ).

`managedContent` `ConnectApi.` Domain associated with the channel. 62.0

```
ChannelDomain ManagedContent

          ChannelDomain

          Representation

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`mediaCacheControl` Long HTTP cache control max age response header for 57.0
`MaxAge` media delivered from the channel.

`name` String Name of the managed content channel. 62.0

`targetId` String ID of the target associated with the channel. 62.0

```
type

```

SEE ALSO:

#### ConnectApi. Type of managed content channel. Values are: 62.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

#### ConnectApi.ManagedContentChannelCollection

postManagedContentChannel(ManagedContentCreateInputParam)

getManagedContentChannel(channelId)

patchManagedContentChannel(channelId, ManagedContentChannelInput)

#### ConnectApi.ManagedContentChannelCollection

Collection of managed content channels.

**Property Name** **Type** **Description** **Available Version**

```
channels

```

#### List< ConnectApi. List of managed content channels. 48.0–61.0

```
ManagedContent
```

`Channel` 

`currentPageUrl` String Connect REST API URL identifying the current page. 48.0–61.0

`nextPageUrl` String Connect REST API URL identifying the next page, or 48.0–61.0
`null` if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 48.0–61.0
or `null` if there isn’t a previous page.

`totalChannels` Integer Total number of managed content channels. 48.0–61.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentChannelDetail

Managed content channel detail.

**Property Name** **Type** **Description** **Available Version**

`channelId` String ID of the managed content channel. 54.0–61.0

`channelName` String Name of the managed content channel. 54.0–61.0

```
channelType

```

#### ConnectApi. Type of managed content channel. Values are: 54.0–61.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

`domain` String Domain assigned to the managed content channel. 54.0–61.0

`domainName` String Name of the domain assigned to the managed 54.0–61.0
content channel.

`isChannelSearchable` Boolean Specifies whether the text of the channel's contents 54.0–61.0
is searchable ( `true` ) or not ( `false` ).

`isDomainLocked` Boolean Specifies whether the channel’s domain is locked and 54.0–61.0
can’t be changed ( `true` ) or not ( `false` ).

#### ConnectApi.ManagedContentChannelDomainRepresentation

Domain associated with a managed content channel.

**Property Name** **Type** **Description** **Available Version**

`isLocked` Boolean Specifies whether the domain is locked and can’t be 62.0
changed ( `true` ) or not ( `false` ).

`name` String Name of the domain assigned to the channel. 62.0

`value` String Value of the domain (name or ID) associated with the 62.0
channel.

SEE ALSO:

#### ConnectApi.ManagedContentChannel


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentChannelsRepresentation

Collection of managed content channels.

**Property Name** **Type** **Description** **Available Version**

#### channels List< ConnectApi. List of managed content channels. 62.0

```
             AbstractManaged

             ContentChannel
```

`Representation`            

`currentPageUrl` String Connect REST API URL identifying the current page. 62.0

`nextPageUrl` String Connect REST API URL identifying the next page, or 62.0
`null` if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 62.0
or `null` if there isn’t a previous page.

`totalChannels` Integer Total number of managed content channels. 62.0

SEE ALSO:

getManagedContentChannels(pageParam, pageSize, showDetails)

#### ConnectApi.ManagedContentChannelSummary

Managed content channel.

Subclass of ConnectApi.AbstractManagedContentChannelRepresentation in version 62.0 and later

**Property Name** **Type** **Description** **Available Version**

`domainUrl` String Domain URL of the channel. 55.0–61.0

`id` String ID of the managed content channel. 62.0

`name` String Name of the managed content channel. 54.0

`resourceUrl` String Resource URL to complete information of the 54.0–61.0
channel.

#### target ConnectApi. Target site associated with the channel. 54.0–61.0

```
             ManagedContent

             ChannelTarget

             Summary

```

```
type

```

#### ConnectApi. Type of managed content channel. Values are: 62.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

`url` String URL to the channel resource. 62.0

SEE ALSO:

ConnectApi.ManagedContentDeliveryDocument

ConnectApi.ManagedContentCollectionItems

ConnectApi.ManagedContentDeliveryDocumentCollection

#### ConnectApi.ManagedContentChannelTargetSummary

Target site associated with the channel.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the site associated with the channel. 54.0

SEE ALSO:

ConnectApi.ManagedContentChannelSummary

ConnectApi.ManagedContentDeliveryChannelSummaryRepresentation

#### ConnectApi.ManagedContentCloneStatus

Information about managed content's clone status.

**Property Name** **Type** **Description** **Available Version**

`label` String Localized label for the status. 61.0

```
status

```

SEE ALSO:

#### ConnectApi. Status of the managed content clone. Values are: 61.0

```
ManagedContent
```

**•** `PartialSuccess`
```
CloneStatus

```

**•** `PartialSuccess`

**•** `Success`

ConnectApi.ManagedContentDocumentClone


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentClonedVariants

Information about clone variants.

**Property Name** **Type** **Description** **Available Version**

`language` String Language of the translated clone variant. 61.0

`managedContent` String ID of the clone variant. 61.0

```
   VariantId

```

`resourceURL` String Resource URL of the clone variant. 61.0

SEE ALSO:

ConnectApi.ManagedContentDocumentClone

#### ConnectApi.ManagedContentCollectionItem

Managed content collection item.

**Property Name** **Type** **Description** **Available Version**

`body` Map<String, Object> Map of properties of the collection item with their 56.0
values.

#### contentType ConnectApi. Type of collection item. 56.0

```
             ManagedContent

             CollectionItem

             TypeSummary

```

`id` String ID of the collection item. 56.0

`name` String Name or title for collection item. 56.0

SEE ALSO:

#### ConnectApi.ManagedContentCollectionItems ConnectApi.ManagedContentCollectionItems

Managed content collection Items.

**Property Name** **Type** **Description** **Available Version**

```
channelInfo

```

#### ConnectApi. Information about the managed content channel. 56.0–61.0

```
ManagedContent

ChannelSummary

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
channelSummary

```

#### ConnectApi. Summary information about the managed content 62.0

`ManagedContent` delivery channel.

```
DeliveryChannel

SummaryRepresentation

```

`collectionKey` String Unique identifier for the collection. 56.0

```
collectionType

```

#### ConnectApi. Type of collection. 56.0

```
ManagedContent

TypeSummary

```

`currentPageUrl` String URL to the current page. 63.0

`id` String ID of the collection. 56.0

```
items

```

#### List< ConnectApi. List of collection Items. 56.0

```
ManagedContent
```

`CollectionItem` 

`language` String Language locale of the collection. 56.0

`nextPageUrl` String URL to the next page. 63.0

`previousPageUrl` String URL to the previous page. 63.0

`publishedDate` Datetime Most recent publish date of the collection. 56.0

`title` String Title of the collection. 56.0

`total` Integer Total number of items in the current collection detail 56.0
page.

`urlName` String URL name of the collection. 56.0

SEE ALSO:

getCollectionItemsForChannel(channelId, collectionKeyOrId, language)

getCollectionItemsForSite(siteId, collectionKeyOrId, language)

#### ConnectApi.ManagedContentCollectionItemTypeSummary

Summary of a collection item type.

**Property Name** **Type** **Description** **Available Version**

`fullyQualifiedName` String Fully qualified name of the collection item type. 56.0

`name` String Name of the collection item type. 56.0

SEE ALSO:

#### ConnectApi.ManagedContentCollectionItem


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentDateAndTimeNodeValue

Managed content node of date and time type.

Subclass of ConnectApi.ManagedContentNodeValue.

**Property Name** **Type** **Description** **Available Version**

`dateTimeValue` Datetime UTC date and time value of the managed content 48.0
node.

`timeZone` String Time zone in which the date and time is authored. 48.0

#### ConnectApi.ManagedContentDateNodeValue

Managed content node of date type.

Subclass of ConnectApi.ManagedContentNodeValue.

**Property Name** **Type** **Description** **Available Version**

`value` Datetime Date value of the managed content node. 48.0

#### ConnectApi.ManagedContentDeliveryChannelRepresentation

Managed content delivery channel.

**Property Name** **Type** **Description** **Available Version**

`domain` String Domain assigned to the managed content channel. 62.0

`domainName` String Name of the domain assigned to the managed 62.0
content channel.

`id` String ID of the managed content channel. 62.0

`isDedicated` Boolean Specifies whether the channel has off-core dedicated 63.0
`ContentDelivery` content delivery enabled ( `true` ) or not ( `false` ).
Orgs hosted on Hyperforce use off-core dedicated
content delivery to deliver content in public channels
with high performance and low latency.

`isDomainLocked` Boolean Specifies whether the channel’s domain is locked and 62.0
can’t be changed ( `true` ) or not ( `false` ).

`isSearchable` Boolean Specifies whether the text of the channel's contents 62.0
is searchable ( `true` ) or not ( `false` ).

`name` String Name of the managed content channel. 62.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
type

```

SEE ALSO:

#### ConnectApi. Type of managed content channel. Values are: 62.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

getManagedContentDeliveryChannel(channelId)

#### ConnectApi.ManagedContentDeliveryChannelsRepresentation

Collection of managed content delivery channels.

**Property Name** **Type** **Description** **Available Version**

#### channels List< ConnectApi. List of managed content delivery channels. 62.0

```
           ManagedContent

           DeliveryChannel
```

`SummaryRepresentation`             

`currentPageUrl` String Connect REST API URL identifying the current page. 62.0

`nextPageUrl` String Connect REST API URL identifying the next page, or 62.0
`null` if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 62.0
or `null` if there isn’t a previous page.

`totalChannels` Integer Total number of managed content delivery channels. 62.0

SEE ALSO:

getAllDeliveryChannels(pageParam, pageSize)

#### ConnectApi.ManagedContentDeliveryChannelSummaryRepresentation

Summary information of a managed content delivery channel.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`domainUrl` String Domain URL of the channel. 62.0

`id` String ID of the managed content delivery channel. 62.0

`name` String Name of the managed content channel. 62.0

`resourceUrl` String Resource URL to complete information of the 62.0
channel.

#### target ConnectApi. Target site associated with the channel. 62.0

```
             ManagedContent

             ChannelTarget

             Summary

```

```
type

```

SEE ALSO:

#### ConnectApi. Type of managed content channel. Values are: 62.0

```
ManagedContent
```

**•** `CloudToCloud` —Cloud-to-Cloud integrated

`ChannelType` channel.

**•** `Community` —Experience Cloud site channel.

**•** `ConnectedApp` —Channel served by a
connected app.

**•** `PublicUnauthenticated` —Public
channel. All published content is publicly
available.

**•** `UserPermission` —Channel backed by a
system permission. All published content is
available only to users with the permission.

#### ConnectApi.ManagedContentDeliveryDocumentCollection ConnectApi.ManagedContentDeliveryDocument

ConnectApi.ManagedContentCollectionItems

#### ConnectApi.ManagedContentDeliveryDocument

Managed content in delivery scope.

Subclass of ConnectApi.AbstractManagedContentDeliveryDocument in version 55.0 and later. Properties with an available version of
54.0 only are included in ConnectApi.AbstractManagedContentDeliveryDocument in version 55.0 and later.

**Property Name** **Type** **Description** **Available Version**

```
channelInfo

```

#### ConnectApi. Information about the managed content channel. 54.0–61.0

```
ManagedContent

ChannelSummary

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
channelSummary

```

#### ConnectApi. Summary information about the managed content 62.0

`ManagedContent` delivery channel.

```
DeliveryChannel

SummaryRepresentation

```

`contentBody` Map<String, Object> Map of properties of the managed content with their 54.0
values.

`contentKey` String Globally unique identifier (GUID) for the managed 54.0 only
content.

```
contentType

```

#### ConnectApi. Type of managed content. 54.0 only

```
ManagedContent

TypeSummary

```

`language` String Language locale of the managed content. 54.0 only

`managedContentId` String ID of the managed content. 54.0 only

`publishedDate` Datetime Most recent publish date of the managed content. 54.0 only

`references` Map<String, Map of references with `contentKey` as the key. 54.0

#### `ConnectApi.`

```
          AbstractManaged
```

`ContentReference`          

```
referencesList

```

#### List< ConnectApi. List of references. 54.0

```
AbstractManaged
```

`ContentReference` 

`title` String Title of the managed content. 54.0 only

`unauthenticatedUrl` String Public URL for the managed content. 54.0 only

`urlName` String URL name of the managed content. 54.0 only

SEE ALSO:

#### ConnectApi.ManagedContentDeliveryDocumentCollection ConnectApi.ManagedContentDeliveryDocumentCollection

Managed content delivery document collection.

**Property Name** **Type** **Description** **Available Version**

```
channelInfo

```

#### ConnectApi. Information about the managed content channel. 55.0–61.0

```
ManagedContent

ChannelSummary

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
channelSummary

```

#### ConnectApi. Summary information about the managed content 62.0

`ManagedContent` delivery channel.

```
DeliveryChannel

SummaryRepresentation

```

#### contents List< ConnectApi. List of managed content delivery documents. 55.0

```
          AbstractManaged

          ContentDelivery
```

`Document`         

`currentPageUrl` String URL to the current page of managed content records. 55.0

`nextPageUrl` String URL to the next page of managed content records. 55.0

`previousPageUrl` String URL to the previous page of managed content 55.0
records.

`references` Map<String, Map of references with `contentKey` as the key. 55.0

#### `ConnectApi.`

```
          AbstractManaged
```

`ContentReference`          

```
referencesList

```

#### List< ConnectApi. List of references. 55.0

```
AbstractManaged
```

`ContentReference` 

#### ConnectApi.ManagedContentDeliveryDocumentSummary

Managed content delivery document summary.

Subclass of ConnectApi.AbstractManagedContentDeliveryDocument.

No additional properties.

#### ConnectApi.ManagedContentDocument

Information about a piece of managed content in an authoring space.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the managed content. 61.0

`contentBody` Map<String, Object> Map of properties of the managed content with their 60.0
values.

`contentFqn` String Fully qualified name (FQN) of the managed content. 64.0

`contentKey` String Globally unique identifier (GUID) for the managed 60.0
content.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
contentSpace

contentType

```

`ConnectApi.` Content space of the managed content. 60.0

```
ManagedContent

SpaceSummary

```

`ConnectApi.` Type of managed content. 60.0

```
ManagedContent

TypeSummary

```

`contentVersion` Integer Content version of the managed content. 66.0

```
createdBy

```

`ConnectApi.` User who created the managed content. 60.0

```
ManagedContent

UserSummary

```

`createdDate` Datetime Date when the managed content was created. 60.0

`externalId` String External ID of the managed content. 60.0

```
folder

```

`ConnectApi.` Folder of the managed content. 60.0

```
ManagedContent

FolderSummary

```

`isPublished` Boolean Specifies whether the managed content variant is 60.0
published to a channel ( `true` ) or not ( `false` ).

`language` String Language locale of the managed content. 60.0

```
lastModifiedBy

```

`ConnectApi.` User who last modified the managed content. 60.0

```
ManagedContent

UserSummary

```

`lastModifiedDate` Datetime Date when the managed content was last modified. 60.0

`managedContentId` String ID of the managed content. 60.0

`managedContent` String Managed content variant ID. 60.0

```
VariantId

```

`managedContent` String Managed content version ID. 60.0

```
VersionId

```

`status` `ConnectApi.` Status of the managed content variant. 60.0

```
          ManagedContent

          VariantStatus

          Output

```

`title` String Title of the managed content. 60.0

`urlName` String URL name of the managed content. 60.0

`variantVersion` Integer Variant version of the managed content. 66.0

`versionNumber` String

Version number of the managed content. In version 60.0–65.0
66.0 and later, use `contentVersion` and
`variantVersion` for version information.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentDocumentClone

Managed content document clone.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the cloned content. 61.0

```
cloneStatus

```

#### ConnectApi. Status of the cloned content. 61.0

```
ManagedContent

CloneStatus

```

`contentKey` String Globally unique identifier (GUID) for the cloned 61.0
content.

`errorMessage` String Error message if the primary variant failed to clone. 61.0

```
failedVariants

folder

```

#### List< ConnectApi. Information about failed cloned variants if cloning 61.0

`ManagedContent` was partially successful.
`FailedVariants` 
#### ConnectApi. Folder of the cloned content. 61.0

```
ManagedContent

FolderSummary

```

`managedContentId` String ID of the cloned content in the authoring workspace. 61.0

`resourceURL` String Resource URL of the cloned content. 61.0

`sourceContentKey` String ID or content key of the source managed content in 61.0
`OrId` the authoring workspace.

`title` String Title of cloned content. 61.0

```
variants

```

SEE ALSO:

#### List< ConnectApi. List of cloned variants. 61.0

```
ManagedContent
```

`ClonedVariants` 

cloneManagedContentDocument(contentKeyOrId, ManagedContentCloneInputParam)

#### ConnectApi.ManagedContentFailedVariants

Information about failed cloned managed content variants if cloning was partially successful.

**Property Name** **Type** **Description** **Available Version**

`errorMessage` String Error message for the failure. 61.0

`language` String Language of the failed translated variant. 61.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`sourceManaged` String ID of the managed content variant that failed to 61.0
`ContentVariantId` clone.

SEE ALSO:

ConnectApi.ManagedContentDocumentClone

#### ConnectApi.ManagedContentFolderSummary

Information about the managed content folder.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the managed content folder in the authoring 60.0
space.

`resourceUrl` String Resource URL of the managed content folder. 60.0

SEE ALSO:

ConnectApi.ManagedContentDocument

ConnectApi.ManagedContentVariant

ConnectApi.ManagedContentDocumentClone

#### ConnectApi.ManagedContentMediaNodeValue

Managed content node of media type.

Subclass of ConnectApi.ManagedContentNodeValue.

**Property Name** **Type** **Description** **Available Version**

`altText` String Alternative text for the managed content node. 47.0

`altUrl` String

Alternative URL to the managed content node. 47.0–48.0

In version 49.0 and later, this information is returned
in the `thumbnailUrl` property.

`contentKey` String Content key of the managed content. 51.0

`fileName` String File name of the managed content node. 48.0

```
mediaType

```

#### ConnectApi. Type of managed content media. Value is Image . 47.0

```
ManagedContent

MediaType

```

`mimeType` String MIME type of the managed content node. 47.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`resourceUrl` String

Resource URL to the image. 48.0

In version 48.0, the resource URL is available if
referencing asset files and is `null` if referencing

media. In version 49.0 and later, the resource URL is
available if referencing asset files or media.

`thumbnailUrl` String URL to the thumbnail of the media. 49.0

`title` String Title of the managed content node. 47.0

`unauthenticatedUrl` String Unauthenticated URL to the image or `null` if the 48.0
image isn’t visible to external users.

`url` String URL to the image. 47.0

#### ConnectApi.ManagedContentMediaSourceNodeValue

Source of managed content media.

**Property Name** **Type** **Description** **Available Version**

`fileName` String File name of the media source. 49.0

`isExternal` Boolean Specifies whether the media source is referenced via 49.0
an external URL ( `true` ) or uploaded ( `false` ).

```
mediaType

```

#### ConnectApi. Type of managed content media. Values are: 49.0

```
ManagedContent
```

**•** `Document`
```
MediaType

```

**•** `Document`

**•** `Image`

`mimeType` String MIME type of the media source. 49.0

`referenceId` String Reference ID of the uploaded media source. 49.0

`resourceUrl` String Resource URL of the media source. 49.0

`unauthenticatedUrl` String

URL to the media source for unauthenticated users, 49.0
or `null` if the media source isn’t available to
external users.

`url` String URL to the media source for authenticated users. 49.0

#### ConnectApi.ManagedContentNodeType

Managed content node type.

**Property Name** **Type** **Description** **Available Version**

`label` String Label of the managed content node type. 47.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`name` String Developer name of the managed content node type. 47.0

```
nodeType

```

SEE ALSO:

#### ConnectApi. Type of managed content node. Values are: 47.0

```
ManagedContent
```

**•** `Date`
```
NodeTypeEnum

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

ConnectApi.ManagedContentType

#### ConnectApi.ManagedContentNodeValue

Managed content node.

This class is abstract.

Superclass of:

**•** ConnectApi.ManagedContentDateAndTimeNodeValue

**•** ConnectApi.ManagedContentDateNodeValue

**•** ConnectApi.ManagedContentMediaNodeValue

**•** ConnectApi.ManagedContentMediaSourceNodeValue

**•** ConnectApi.ManagedContentTextNodeValue


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
nodeType

```

SEE ALSO:

#### ConnectApi. Type of managed content node. Values are: 47.0

```
ManagedContent
```

**•** `Date`
```
NodeType

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

ConnectApi.ManagedContentVersion

#### ConnectApi.ManagedContentProvider

Information about a managed content provider.

**Property Name** **Type** **Description** **Available Version**

`componentDefinition` String Provider lightning component definition. 65.0

`icon` String Icon of the dropdown menu item. 65.0

`label` String Label of the dropdown menu item. 65.0

`providerId` String ID of the provider. 65.0

```
providerInstances

```

#### List< ConnectApi. Instances of the provider. 65.0

```
ManagedContent
```

`ProviderInstance` 

`providerLightning` String ID of the dropdown menu item. 65.0

```
ComponentId

```

```
type

```

SEE ALSO:

#### ConnectApi. Type of managed content provider. Values are: 65.0

```
ManagedContent
```

**•** `DigitalAssetManager`
```
ProviderType

```

#### ConnectApi.ManagedContentProviderCollection ConnectApi.ManagedContentProviderCollection

Collection of managed content providers.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`contentSpaceId` String ID of the managed content space, if provided. 66.0
Otherwise, `null` .

`currentPageUrl` String URL to the current page of managed content 65.0
providers.

`nextPageUrl` String URL to the next page of managed content providers. 65.0

```
providers

```

#### List< ConnectApi. Managed content providers. 65.0

```
ManagedContent
```

`Provider` 

`total` Integer Total number of managed content providers. 65.0

SEE ALSO:

getManagedContentProviders()

getManagedContentProvidersForSpace(contentSpaceId)

#### ConnectApi.ManagedContentProviderInstance

Information about a managed content provider instance.

**Property Name** **Type** **Description** **Available Version**

`instanceKey` String Provider instance key. 65.0

`isDefault` Boolean Specifies whether the instance is the default instance 65.0
( `true` ) or not ( `false` ).

`isEnabledForSpace` Boolean Specifies whether the provider instance is enabled 66.0
for the managed content space ( `true` ) or not

( `false` ). If there isn't a managed content space
context, defaults to `false` .

`name` String Name of the provider instance. 65.0

`providerInstanceId` String ID of the provider instance. 65.0

SEE ALSO:

#### ConnectApi.ManagedContentProvider

createManagedContentProvider(providerInstanceInput)

updateManagedContentProviderInstance(providerInstanceId, providerInstanceInput)

#### ConnectApi.ManagedContentPublishOutput

Information about a Publish action


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`deploymentId` String ID of the managed content deployment. 60.0

`description` String Publish description. 60.0

`publishDate` Datetime Publish date. 60.0

#### ConnectApi.ManagedContentReference

Managed content reference.

Subclass of ConnectApi.AbstractManagedContentReference.

**Property Name** **Type** **Description** **Available Version**

`contentBody` Map<String, Object> Map of properties of the managed content reference 54.0
with their values.

`title` String Title of the managed content reference. 54.0

SEE ALSO:

#### ConnectApi.ManagedContentReferenceSummary ConnectApi.ManagedContentReferenceSummary

Summary of the managed content reference.

Subclass of ConnectApi.AbstractManagedContentReference.

**Property Name** **Type** **Description** **Available Version**

`title` String Title of the managed content reference. 54.0

#### ConnectApi.ManagedContentSpace

Managed content space.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the managed content space. 61.0

`createdBy` String ID of the user who created the managed content 55.0
space.

`createdDate` Datetime Date when the managed content space was created. 55.0

`defaultLanguage` String Default language of the managed content space. 55.0

`description` String Description of the managed content space. 55.0

`fullyQualifiedName` String Fully qualified name of the managed content space. 63.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the managed content space. 55.0

`isEnhancedSpace` Boolean Specifies whether the space is enhanced ( `true` ) or 60.0
not ( `false` ).

`lastModifiedBy` String ID of the user who last modified the managed 55.0
content space.

`lastModifiedDate` Datetime Date when the managed content space was last 55.0
modified.

`name` String Name of the managed content space. 55.0

`rootFolderId` String ID of the root folder of the managed content space. 55.0

```
spaceType

```

SEE ALSO:

#### ConnectApi. Base type of the managed content space. 64.0

```
ManagedContent

SpaceBaseType

```

getManagedContentSpace(contentSpaceId)

patchManagedContentSpace(contentSpaceId, ManagedContentSpaceUpdateInput)

postManagedContentSpace(ManagedContentSpaceInput)

ConnectApi.ManagedContentSpaceCollectionRepresentation

#### ConnectApi.ManagedContentSpaceBaseType

Base type of the managed content space.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the base type of the managed content 64.0
space.

SEE ALSO:

#### ConnectApi.ManagedContentSpace ConnectApi.ManagedContentSpaceChannelRepresentation

Managed content space channel.

**Property Name** **Type** **Description** **Available Version**

```
channelSummary

```

#### ConnectApi. Information about the managed content space 62.0

`ManagedContent` channel.

```
ChannelSummary

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
createdBy

```

#### ConnectApi. Information about the user who created the managed 62.0

`ManagedContent` content space channel.

```
UserSummary

```

`createdDate` Datetime Date when the managed content space channel was 62.0
created.

```
status

```

SEE ALSO:

#### ConnectApi. Status of the add or remove operation for a channel 62.0

`ManagedContent` and managed content space.

```
SpaceChannel
```

**•** `Added` —Channel was added to the managed

`Status` on page 2610

content space.

**•** `Failed` —Add or remove operation failed.

**•** `Pending` —Add or remove operation is
pending.

**•** `Removed` —Channel was removed from the
managed content space.

#### ConnectApi.ManagedContentSpaceChannelsRepresentation ConnectApi.ManagedContentSpaceChannelsRepresentation

List of managed content space channels.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String URL to the current page of managed content space 62.0
channels.

`nextPageUrl` String URL to the next page of Mmanaged content space 62.0
channels.

`previousPageUrl` String URL to the previous page of managed content space 62.0
channels.

#### spaceChannels List< ConnectApi. List of managed content space channels. 62.0

```
           ManagedContent

           SpaceChannel
```

`Representation`          

`totalSpaceChannels` Integer Total count of managed content space channels 62.0
returned for the request.

SEE ALSO:

patchManagedContentSpaceChannels(contentSpaceId, spaceChannels)

getManagedContentSpaceChannels(contentSpaceId, pageParam, pageSize)


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedContentSpaceCollectionRepresentation

Collection of managed content spaces.

**Property Name** **Type** **Description** **Available Version**

```
spaces

```

SEE ALSO:

#### List< ConnectApi. Collection of managed content spaces corresponding 64.0

`ManagedContent` to the current page.
`Space` 

getManagedContentSpaces(pageParam, pageSize, nameFragment)

#### ConnectApi.ManagedContentSpaceSummary

Information about the managed content space.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the managed content space. 60.0

`resourceUrl` String Resource URL of the managed content space. 60.0

SEE ALSO:

ConnectApi.ManagedContentDocument

ConnectApi.ManagedContentVariant

#### ConnectApi.ManagedContentTextNodeValue

Managed content node of text type.

Subclass of ConnectApi.ManagedContentNodeValue.

**Property Name** **Type** **Description** **Available Version**

`value` String Text value of the managed content node. 47.0

#### ConnectApi.ManagedContentType

Managed content type.

**Property Name** **Type** **Description** **Available Version**

`label` String Label of the managed content type. 47.0

`name` String Developer name of the managed content type. 47.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`nodeTypes` Map<String, Map of node types for the managed content type. 47.0

#### `ConnectApi.`

```
             ManagedContent
```

`NodeType`            

SEE ALSO:

ConnectApi.ManagedContentVersionCollection

#### ConnectApi.ManagedContentTypeSummary

Managed content type.

**Property Name** **Type** **Description** **Available Version**

`fullyQualified` String Fully qualified name of the managed content type. 54.0

```
   Name

```

`name` String Reserved for future use. 55.0

SEE ALSO:

ConnectApi.ManagedContentDeliveryDocument

ConnectApi.ManagedContentCollectionItems

ConnectApi.ManagedContentDocument

ConnectApi.ManagedContentVariant

#### ConnectApi.ManagedContentUnpublishOutput

Managed content unpublish action.

**Property Name** **Type** **Description** **Available Version**

`deploymentId` String ID of the Managed content deployment. 60.0

`description` String Unpublish description. 60.0

`unpublishDate` Datetime Unpublish date. 60.0

#### ConnectApi.ManagedContentUserSummary

Information about the user who created or modified the content.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the user. 60.0

`name` String Reserved for future use. 60.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`resourceUrl` String Resource URL of the user. 60.0

SEE ALSO:

ConnectApi.ManagedContentDocument

#### ConnectApi.ManagedContentVariant ConnectApi.ManagedContentVariant

Managed content variant.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the managed content variant. 63.0

`contentBody` Map<String, Object> Map of properties of the managed content with their 60.0
values.

`contentFqn` String Fully qualified name (FQN) of the managed content. 64.0

`contentKey` String Globally unique identifier (GUID) for the managed 60.0
content.

```
contentSpace

contentType

createdBy

```

#### ConnectApi. Content space of the managed content. 60.0

```
ManagedContent

SpaceSummary

#### ConnectApi. Type of managed content. 60.0

ManagedContent

TypeSummary

#### ConnectApi. User who created the managed content variant. 60.0

ManagedContent

UserSummary

```

`createdDate` Datetime Date when the managed content variant was created. 60.0

`externalId` String External ID of the managed content. 60.0

```
folder

```

#### ConnectApi. Folder of the managed content. 60.0

```
ManagedContent

FolderSummary

```

`isPublished` Boolean Specifies whether the managed content variant is 60.0
published to a channel (true) or not (false).

`language` String Language locale of the managed content. 60.0

```
lastModifiedBy

```

#### ConnectApi. User who last modified the managed content variant. 60.0

```
ManagedContent

UserSummary

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`lastModifiedDate` Datetime Date when the managed content variant was last 60.0
modified.

`managedContentId` String ID of the managed content. 60.0

`managedContent` String ID of the managed content variant. 60.0

```
   VariantId

```

`managedContent` String Managed content version ID. 60.0

```
   VersionId

```

```
status

```

#### ConnectApi. Information about a managed content variant's status 60.0

`ManagedContent` in the authoring space.

```
VariantStatus

Output

```

`title` String Title of the managed content. 60.0

`urlName` String URL name of the managed content. 60.0

#### ConnectApi.ManagedContentVariantStatusOutput

Information about a managed content variant's status in the authoring space.

**Property Name** **Type** **Description** **Available Version**

`label` String Localized label for the status. 60.0

```
status

```

SEE ALSO:

#### ConnectApi. Status of the managed content variant. Values are: 60.0

```
ManagedContent
```

**•** `Draft` —Content isn’t published.
```
VariantStatus

```

**•** `Draft` —Content isn’t published.

**•** `Published` —Content is published and
available for use in your live sites.

**•** `Revised` —Content that’s published and
edited. Publish this content to make the changes
available for use in your live sites.

ConnectApi.ManagedContentDocument

#### ConnectApi.ManagedContentVariant ConnectApi.ManagedContentVersion

Managed content version.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
associations

```

#### ConnectApi. Content topics associated with the managed content. 47.0

```
ManagedContent

Associations

```

`contentKey` String Content key of the managed content. 51.0

`contentNodes` Map<String, Map of content nodes. 47.0

#### `ConnectApi.`

```
           ManagedContent
```

`NodeValue`          

`contentUrlName` String Content URL name of the managed content version. 48.0

`language` String Language of the managed content version. 48.0

`managedContentId` String ID of the managed content. 47.0

`publishedDate` Datetime Date when the managed content version was last 47.0
published.

`title` String Title of the managed content version. 47.0

`type` String Type of managed content version. 47.0

`typeLabel` String Type label of the managed content type. 47.0

`unauthenticatedUrl` String Unauthenticated delivery URL. 50.0

SEE ALSO:

#### ConnectApi.ManagedContentVersionCollection ConnectApi.ManagedContentVersionCollection

Collection of managed content versions.

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 47.0

```
items

managedContent

Types

```

#### List< ConnectApi. List of managed content versions. 47.0

```
ManagedContent
```

`Version` 

Map<String, Map of managed content types. 47.0

#### `ConnectApi.`

`ManagedContentType` 

`nextPageUrl` String Connect REST API URL identifying the next page, or 47.0
`null` if there isn’t a next page.

`total` Integer Total number of managed content versions. 47.0

`totalTypes` Integer Total number of managed content types. 47.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ManagedSocialAccount

Information describing a managed social account or fan page of a social network.

Subclass of ConnectApi.BaseManagedSocialAccount

No additional properties.

#### ConnectApi.ManagedSocialAccounts

A list of managed social accounts.

**Property Name** **Type** **Description** **Available Version**

#### managedSocial List< ConnectApi. List of managed social accounts. 44.0

`Accounts` `ManagedSocialAccount`   
#### ConnectApi.ManagedTopic

Represents a managed topic in an Experience Cloud site.

**Property Name** **Type** **Description** **Available Version**

#### children List< ConnectApi.

`ManagedTopic`         

Children managed topics of the managed topic; 35.0

`null` if the `depth` request parameter isn’t
specified or is _`1`_ .

`id` String ID of managed topic. 32.0

#### managedTopicType ConnectApi.Managed Type of managed topic. 32.0

```
           TopicType
```

**•** `Content` —Topics that are associated with
native content.

**•** `Featured` —Topics that are featured, for
example, on the Experience Cloud site home
page, but don’t provide overall navigation.

**•** `Navigational` —Topics that display in a
navigational menu in the Experience Cloud site.

`parent` `ConnectApi.Reference` Parent managed topic of the managed topic. 35.0

`topic` `ConnectApi.Topic` Information about the topic. 32.0

`url` String Connect REST API URL to the managed topic. 32.0

SEE ALSO:

#### ConnectApi.ManagedTopicCollection ConnectApi.ManagedTopicCollection

A collection of managed topics.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 32.0

`managedTopics` `List<ConnectApi.` List of managed topics. 32.0

```
             ManagedTopic>

```

`nextPageUrl` String Connect REST API URL identifying the next page, or 44.0
`null` if there isn’t a next page.

#### ConnectApi.MarkupBeginSegment

The beginning of rich text markup.

Subclass of ConnectApi.MessageSegment.

**Property Name** **Type** **Description** **Available Version**

`altText` String Alternative text for the segment, if available. 45.0

`htmlTag` String The HTML tag for this markup. 35.0

#### markupType ConnectApi. Type of rich text markup. 35.0

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

**•** `Strikethrough` —Strikethrough tag.

**•** `Underline` —Underline tag.

**•** `UnorderedList` —Unordered list tag.

`url` String URL to the segment, if available. 45.0

#### ConnectApi.MarkupEndSegment

The end of rich text markup.

Subclass of ConnectApi.MessageSegment.

**Property Name** **Type** **Description** **Available Version**

`htmlTag` String The HTML tag for this markup. 35.0

#### markupType ConnectApi. Type of rich text markup. 35.0

```
             MarkupType
```

**•** `Bold` —Bold tag.

**•** `Code` —Code tag.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Hyperlink` —Hyperlink anchor tag.

**•** `Italic` —Italic tag.

**•** `ListItem` —List item tag.

**•** `OrderedList` —Ordered list tag.

**•** `Paragraph` —Paragraph tag.

**•** `Strikethrough` —Strikethrough tag.

**•** `Underline` —Underline tag.

**•** `UnorderedList` —Unordered list tag.

#### ConnectApi.MatchInfo

Search information related to the search result.

**Property Name** **Type** **Description** **Available Version**

`isPromoted` Boolean Specifies whether search promotion affected the 63.0
result ( `true` ) or not ( `false` ).

`isSpellCorrected` Boolean Specifies whether spell correction affected the result 63.0
( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.SearchResult

#### ConnectApi.MCSFolderShare

Target that a managed content space folder is shared with.

**Property Name** **Type** **Description** **Available Version**

`canUserUnshare` Boolean Specifies whether the user has permission to unshare 63.0
with the target space ( `true` ) or not ( `false` ).

Content Manager or higher role in the target
workspace has permission to unshare.

```
shareStatus

```

#### ConnectApi. Status of sharing a managed content space folder. 63.0

`MCSFolderShare` Values are:

```
Status
```

**•** `PendingShare`

**•** `PendingUnshare`

**•** `Shared`

`targetId` String ID of the share target. 63.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`targetLabel` String Label of the share target. 63.0

SEE ALSO:

#### ConnectApi.MCSFolderShareCollection ConnectApi.MCSFolderShareCollection

Collection of targets that a managed content space folder is shared with.

**Property Name** **Type** **Description** **Available Version**

`folderId` String ID of the managed content space folder. 63.0

#### shares List< ConnectApi. List of targets that a managed content space folder 63.0

`MCSFolderShare`            - is shared with.

SEE ALSO:

patchMCSFolderShares(folderId, mcsFolderShareCollectionUpdateInput)

getMCSFolderShares(folderId)

#### ConnectApi.MCSFolderShareTarget

Target that a managed content space folder can be shared with.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the share target. 63.0

`label` String Label of the share target. 63.0

`resourceUrl` String Resource URL of the share target that provides target 63.0
details.

SEE ALSO:

#### ConnectApi.MCSFolderShareTargetCollection ConnectApi.MCSFolderShareTargetCollection

Collection of targets that a managed content space folder can be shared with.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
shareTargets

```

SEE ALSO:

#### List< ConnectApi. List of targets that a managed content space folder 63.0

`MCSFolderShare` can be shared with.
`Target` 

getMCSFolderShareTargets(folderId)

#### ConnectApi.MediaReference

A media reference.

**Property Name** **Type** **Description** **Available Version**

`mediaUrl` String URL to stream or download the media. 41.0

`thumbnailUrl` String If one exists, URL of the media’s thumbnail. 41.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.MediaReferenceCapability ConnectApi.MediaReferenceCapability

If a feed element has this capability, it has one or more media references.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

#### media List< ConnectApi. Collection of media references. 41.0

`MediaReference`          
#### ConnectApi.MentionCompletion

Information about a record that could be used to @mention a user or group.

**Name** **Type** **Description** **Available Version**

`additionalLabel` String If one exists, an additional label for the record represented by this 29.0
completion, for example, “(Customer)” or “(Acme Corporation)”.

`description` String A description of the record represented by this completion. 29.0

`name` String The name of the record represented by this completion. The name 29.0
is localized, if possible.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`outOfOffice` `ConnectApi.OutOfOffice` If the record represented by this completion is a user, an additional 40.0
out-of-office message, if one exists, for the user.

`photoUrl` String A URL to the photo or icon of the record represented by this 29.0
completion.

`recordId` String The ID of the record represented by this completion. 29.0

```
userType

```

SEE ALSO:

#### `ConnectApi.`

```
UserType
```

Enum

If the record represented by this completion is a user, this value is 30.0
the user type associated with that user; otherwise the value is `null` .

One of these values:

**•** `ChatterGuest` —User is an external user in a private group.

**•** `ChatterOnly` —User is a Chatter Free customer.

**•** `Guest` —User is unauthenticated.

**•** `Internal` —User is a standard org member.

**•** `Portal` —User is an external user in an Experience Cloud site.

**•** `System` —User is Chatter Expert or a system user.

**•** `Undefined` —User is a user type that is a custom object.

#### ConnectApi.MentionCompletionPage ConnectApi.MentionCompletionPage

Paginated list of Mention Completion response bodies.

**Name** **Type** **Description** **Available**
**Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 29.0

`mentionCompletions` `List<ConnectApi.` A list of mention completion proposals. Use these proposals 29.0
`MentionCompletion>` to build a feed post body.

`nextPageUrl` String Connect REST API URL identifying the next page, or `null` 29.0
if there isn’t a next page.

`previousPageUrl` String Connect REST API URL identifying the previous page, or 29.0
`null` if there isn’t a previous page.

#### ConnectApi.MentionSegment

Mention segment.

Subclass of ConnectApi.MessageSegment.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

`accessible` Boolean

Specifies whether the mentioned user or group can see 28.0
the post in which they are mentioned ( `true` ) or not
( `false` ).

`name` String Name of the mentioned user or group. 28.0

#### record ConnectApi. Information about the mentioned user or group. 29.0

```
         ActorWithId

```

`user` `ConnectApi.User` Information about the mentioned user.

```
         Summary
```

Important: In versions 29.0 and later, use the
`record` property.

#### ConnectApi.MentionValidation

Information about whether a proposed mention is valid for the context user.

28.0 only

In versions before
29.0, if the mention

is not a user, the
mention is in a

```
ConnectApi.TextSegment
```

object.

**Name** **Type** **Description** **Available Version**

`recordId` String The ID of the mentioned record. 29.0

```
validationStatus

```

SEE ALSO:

#### ConnectApi. Type of validation error for a proposed mention, if any. 29.0

```
MentionValidation
```

**•** `Disallowed` —The proposed mention is invalid

`Status` Enum

and is rejected because the context user is trying
to mention something that is not allowed. For
example, a user who is not a member of a private
group is trying to mention the private group.

**•** `Inaccessible` —The proposed mention is
allowed, but the user or record being mentioned
isn’t notified. They don't have access to the parent
record that’s being discussed.

**•** `Ok` —There is no validation error for this proposed
mention.

#### ConnectApi.MentionValidations ConnectApi.MentionValidations

Information about whether a set of mentions is valid for the context user.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`hasErrors` Boolean Indicates whether at least one of the proposed 29.0
mentions has an error ( `true` ), or not ( `false` ). For

example, context users can’t mention private groups
they don’t belong to. If such a group is included in
the list of mention validations, `hasErrors` is
`true` and the group has a `validationStatus`
of `Disallowed` in its mention validation.

`mentionValidations` `List<ConnectApi.` List of mention validation information in the same 29.0
`MentionValidation>` order as the provided record IDs.

#### ConnectApi.MessageBody

Message body.

Subclass of ConnectApi.AbstractMessageBody.

No additional properties.

SEE ALSO:

ConnectApi.ChatterLikesCapability

ConnectApi.ChatterMessage

ConnectApi.Comment

ConnectApi.FeedElement

ConnectApi.FeedItemSummary

#### ConnectApi.MessageSegment

Message segment.

This class is abstract.

Superclass of:

**•** ConnectApi.ComplexSegment

**•** ConnectApi.EntityLinkSegment

**•** ConnectApi.FieldChangeSegment

**•** ConnectApi.FieldChangeNameSegment

**•** ConnectApi.FieldChangeValueSegment

**•** ConnectApi.HashtagSegment

**•** ConnectApi.InlineImageSegment

**•** ConnectApi.LinkSegment

**•** ConnectApi.MarkupBeginSegment

**•** ConnectApi.MarkupEndSegment

**•** ConnectApi.MentionSegment

**•** ConnectApi.MoreChangesSegment


Apex Reference Guide ConnectApi Output Classes

**•** ConnectApi.ResourceLinkSegment

**•** ConnectApi.TextSegment

Message segments in a feed item are typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as
`ConnectApi.FeedItemCapability` . Record fields are typed as `ConnectApi.AbstractRecordField` . These classes
are all abstract and have several concrete subclasses. At runtime you can use `instanceof` to check the concrete types of these objects
and then safely proceed with the corresponding downcast. When you downcast, you must have a default case that handles unknown
subclasses.

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

**Name** **Type** **Description** **Available Version**

`text` String Text-only rendition of this segment. If a client encounters an 28.0
unknown message segment type, it can render this value.

```
type

```

SEE ALSO:

#### ConnectApi. The message segment type. One of these values: 28.0

```
MessageSegment
```

**•** `EntityLink`

`Type` Enum

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

ConnectApi.AbstractMessageBody

#### ConnectApi.ModerationCapability

If a feed element has this capability, users in an Experience Cloud site can flag it for moderation.

Subclass of ConnectApi.FeedElementCapability.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### `moderationFlags ConnectApi.`

```
           ModerationFlags

```

SEE ALSO:

ConnectApi.FeedElementCapabilities

The moderation flags for this feed element. 31.0
Moderators can view and take action on flagged
items.

#### ConnectApi.ModerationFlagItemDetail

Flag details on a feed item, comment, or file.

**Property Name** **Type** **Description** **Available Version**

`createdBy` String ID of the user who flagged the item. 40.0

`createdDate` Datetime Date when the item was flagged. 40.0

`id` String ID of the moderation flag. 40.0

#### moderationType ConnectApi. Type of moderation flag. Values are: 40.0

```
           CommunityFlagType
```

**•** `FlagAsInappropriate` —Flag for
inappropriate content.

**•** `FlagAsSpam` —Flag for spam.

`note` String Note from user who flagged the item. 40.0

```
visibility

```

SEE ALSO:

#### ConnectApi. Visibility behavior of a flag for various user types. 40.0

`CommunityFlag` Values are:

```
Visibility
```

**•** `ModeratorsOnly` —The flag is visible only
to users with moderation permissions on the
flagged element or item.

**•** `SelfAndModerators` —The flag is visible
to the creator of the flag and to users with
moderation permissions on the flagged element
or item.

#### ConnectApi.ModerationFlagsCollection ConnectApi.ModerationFlags

Information about the moderation flags on a feed item, comment, or file.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`flagCount` Integer Number of moderation flags on this feed item, comment, or file. If 29.0
the context user is not a moderator, the property is `null` .

```
flagCount

ByReason

```

#### Map< ConnectApi. Number of moderation flags categorized by reason. Values for 40.0

`CommunityFlag` `ConnectApi.CommunityFlagReasonType` are:
`ReasonType`,

**•** `FlaggedByRule` —Moderation rule flagged the item.

Integer>

**•** `FlaggedByRule` —Moderation rule flagged the item.

**•** `FlaggedBySystem` —Einstein flagged the item.

**•** `FlaggedByUserAsInappropriate` —User flagged the
item as inappropriate.

**•** `FlaggedByUserAsSpam` —User flagged the item as spam.

`flaggedByMe` Boolean `true` if the context user flagged the feed item, comment, or file 29.0
for moderation; `false` otherwise.

#### flags ConnectApi.ModerationFlagsCollection Collection of flags. 40.0

SEE ALSO:

ConnectApi.Comment

ConnectApi.File

ConnectApi.ModerationCapability

#### ConnectApi.ModerationFlagsCollection

A collection of flags on a feed item, comment, or file.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page. 40.0

`currentPageUrl` String Connect REST API URL identifying the current page. 40.0

```
flags

```

#### List< ConnectApi. List of flag details. 40.0

```
ModerationFlag
```

`ItemDetail` 

`nextPageToken` String Token identifying the next page, or `null` if there 40.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 40.0
`null` if there isn’t a next page.

`pageSize` Integer Number of items per page. 40.0

SEE ALSO:

#### ConnectApi.ModerationFlags


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.MoreChangesSegment

In feed items with a large number of tracked changes, the message is formatted as: “changed A, B, and made X more changes.” The
`MoreChangesSegment` contains the “X more changes.”

Subclass of ConnectApi.MessageSegment.

**Name** **Type** **Description** **Available Version**

```
moreChanges

```

`List<ConnectApi.` Complete list of tracked changes. 29.0

```
FieldChange

Segment>

```

`moreChangesCount` Integer Number of additional changes. 28.0

#### ConnectApi.Motif

The motif properties contain URLs for small, medium, and large icons that indicate the Salesforce record type. Common record types
are files, users, and groups, but all record types have a set of motif icons. Custom object records use their tab style icon. All icons are
available to unauthenticated users so that, for example, you can display the motif icons in an email. The motif can also contain the record
type’s base color.

The motif images are icons, not user uploaded images or photos. For example, every user has the same set of motif icons.

Custom object records use their tab style icon, for example, the following custom object uses the “boat” tab style:

```
  "motif": {

    "color: "8C004C",

    "largeIconUrl": "/img/icon/custom51_100/boat64.png",

    "mediumIconUrl": "/img/icon/custom51_100/boat32.png",

    "smallIconUrl": "/img/icon/custom51_100/boat16.png",

    "svgIconUrl": null

  },

```

Users use the following icons:

```
  "motif": {

    "color: "1797C0",

    "largeIconUrl": "/img/icon/profile64.png",

    "mediumIconUrl": "/img/icon/profile32.png",

    "smallIconUrl": "/img/icon/profile16.png",

    "svgIconUrl": null

  },

```

Groups use the following icons:

```
  "motif": {

    "color: "1797C0",

    "largeIconUrl": "/img/icon/groups64.png",

    "mediumIconUrl": "/img/icon/groups32.png",

    "smallIconUrl": "/img/icon/groups16.png",

    "svgIconUrl": null

  },

```


Apex Reference Guide ConnectApi Output Classes

Files use the following icons:

```
     "motif": {

       "color: "1797C0",

       "largeIconUrl": "/img/content/content64.png",

       "mediumIconUrl": "/img/content/content32.png",

       "smallIconUrl": "/img/icon/files16.png",

       "svgIconUrl": null

     },

```

Note: To view the icons in the previous examples, preface the URL with `https://` _`instance_name`_ . For example,
`https://` _`instance_name`_ `/img/icon/profile64.png` .

**Name** **Type** **Description** **Available**
**Version**

`color` String A hex value representing the base color of the record type, or `null` . 29.0

`largeIconUrl` String A large icon indicating the record type. 28.0

`mediumIconUrl` String A medium icon indicating the record type. 28.0

`smallIconUrl` String A small icon indicating the record type. 28.0

`svgIconUrl` String An icon in SVG format indicating the record type, or `null` if the icon 34.0
doesn’t exist.

#### ConnectApi.MultipleAsyncOutputRepresentation

IDs of the asynchronous background operations. This output only includes the operation IDs, regardless of whether calls are made to
an external payment gateway. It doesn’t include any errors from the operations.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
asyncOutputs

```

SEE ALSO:

#### List< ConnectApi. List of IDs of background operations. 56.0

```
AsyncOutput
```

`Representation` 

multipleEnsureFundsAsync(multipleEnsureFundsInput)

#### ConnectApi.MultipleFulfillmentOrderInvoicesOutputRepresentation

IDs of the created Invoices.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`invoiceIds` List<String> List of IDs of the created Invoices. 52.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.MultipleFulfillmentOrderOutputRepresentation

A list of responses for the individual FulfillmentOrder creation attempts from a request to create multiple fulfillment orders.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`invoicesMap` 50.0

```
fulfillmentOrders

```

#### List< ConnectApi. A list of response data for created and failed 50.0

`FulfillmentGroup` FulfillmentOrders.
`OutputRepresentation` 

#### ConnectApi.MuteCapability

If a feed element has this capability, users can mute it. Muted feed elements are visible in the muted feed, and invisible in all other feeds
that respect mute.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isMutedByMe` Boolean Indicates whether the context user muted the feed 35.0
element.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.MuteSummary

Summary of a mute.

Subclass of ConnectApi.UserFeedEntityActivitySummary.

No additional properties.

#### ConnectApi.NamedCredential

Named credential associated with an external credential.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property Name** **Type** **Description** **Available Version**

```
calloutOptions

```

#### ConnectApi. Callout options for the named credential. 58.0

```
NamedCredential

CalloutOptions

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### calloutStatus ConnectApi. Indicates whether a named credential is enabled for 59.0

`CalloutStatus` callout. Values are:

**•** `Disabled`

**•** `Enabled`

`calloutUrl` String URL of the named credential in a callout. 58.0

`createdByNamespace` String Namespace of the package that created the named 59.0
credential.

```
customHeaders

```

#### List< ConnectApi. Custom HTTP headers for the named credential. 58.0

```
CredentialCustom
```

`Header` 

`description` String Description of the named credential. 64.0

`developerName` String Fully qualified developer name of the named 56.0
credential.

#### externalCredentials List< ConnectApi. External credentials used by the named credential. 58.0

`ExternalCredential`           

`id` String Named credential ID. 58.0

`masterLabel` String Named credential label. 56.0

#### networkConnection ConnectApi. PrivateConnect outbound network connection for 58.0

`NetworkConnection` the named credential.

```
parameters

```

#### List< ConnectApi. Named credential parameters. 58.0

```
NamedCredential
```

`Parameter` 

#### type ConnectApi. Type of named credential. Values are: 58.0

```
          NamedCredentialType
```

**•** `PrivateEndpoint`

**•** `SecuredEndpoint`

`url` String Connect REST API URL of the named credential. 58.0

SEE ALSO:

ConnectApi.ExternalCredential

ConnectApi.NamedCredentialList

#### ConnectApi.NamedCredentialCalloutOptions

Named credential callout options.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`allowMergeFields` Boolean Specifies whether to allow merge fields in the HTTP 58.0
`InBody` body ( `true` ) or not ( `false` ).

`allowMergeFields` Boolean Specifies whether to allow merge fields in the HTTP 58.0
`InHeader` header ( `true` ) or not ( `false` ).

`generate` Boolean Specifies whether to generate an authorization 58.0
`AuthorizationHeader` header ( `true` ) or not ( `false` ).

SEE ALSO:

#### ConnectApi.NamedCredential ConnectApi.NamedCredentialList

List of named credentials.

**Property Name** **Type** **Description** **Available Version**

#### namedCredentials List< ConnectApi. List of named credentials. 58.0

`NamedCredential`            
#### ConnectApi.NamedCredentialParameter

Named credential parameter.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the parameter. 58.0

`parameterName` String Name of the parameter. 58.0

```
parameterType

```

#### ConnectApi. Type of named credential parameter. Values are: 58.0

```
NamedCredential
```

**•** `AllowedManagedPackageNamespaces`
```
ParameterType

```

**•** `AllowedManagedPackageNamespaces`

**•** `ClientCertificate`

**•** `ConnectionStatus`

`parameterValue` String Value of the parameter. 58.0

SEE ALSO:

#### ConnectApi.NamedCredential ConnectApi.NavigationMenuItem

Navigation menu item.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
actionType

```

#### ConnectApi. Event, URL type, or modal navigation menu item. 52.0

`NavigationMenuItem` Values are:

```
ActionType
```

**•** `Event` —Event-based navigation.

Note: `Event` is internal only and can’t
be used in custom components.

**•** `ExternalLink` —URL outside of your
Experience Cloud site.

**•** `InternalLink` —Relative URL inside your
Experience Cloud site.

**•** `Modal` —Modal, such as Account Switcher.

`actionValue` String For `Event` action type, the event fully qualified 52.0
name for the navigation menu item. For

`ExternalLink` and `InternalLink` action
types, the route URL for the navigation menu item.
For `Modal` action type, the component fully
qualified name for the navigation menu item.

`imageUrl` String URL to the image of the navigation menu item. 52.0

`label` String Label for the navigation menu item. 52.0

```
pageReference

```

#### `ConnectApi.`

```
NavigationMenuPage

Reference

```

Page reference for the navigation menu item. Page 59.0
reference is returned only for the Storefront
Categories data source.

#### subMenu List< ConnectApi. Submenu for the navigation menu item. 52.0

`NavigationMenuItem`           

```
target

```

SEE ALSO:

#### ConnectApi. Target for the navigation menu item. Values are: 52.0

```
NavigationMenuItem
```

**•** `CurrentWindow` —Navigation menu item

`OpenTarget` opens in the current window.

**•** `NewWindow` —Navigation menu item opens in
a new window.

#### ConnectApi.NavigationMenuItemCollection ConnectApi.NavigationMenuItemCollection

Collection of navigation menu items.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### menuItems List< ConnectApi. Collection of navigation menu items. 52.0

`NavigationMenuItem`              
#### ConnectApi.NavigationMenuPageReference

Navigation menu item page reference.

**Property Name** **Type** **Description** **Available Version**

`attributes` Map<String, String> Attributes for the navigation menu item page 59.0
reference.

`state` Map<String, String> State for the navigation menu item page reference. 59.0

`type` String Type for the navigation menu item page reference. 59.0

SEE ALSO:

ConnectApi.NavigationMenuItem

#### ConnectApi.NBAActionParameter

A parameter for an action.

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the parameter. 45.0

`type` String Type of the parameter. 45.0

`value` String Value of the parameter. 45.0

#### ConnectApi.NBAFlowAction

A recommended flow.

Subclass of ConnectApi.AbstractNBAAction.

**Property Name** **Type** **Description** **Available Version**

`flowLabel` String Label of the recommended flow. 47.0

#### flowType ConnectApi. Type of recommended flow. Values are: 47.0

```
             NBAFlowType
```

**•** `AutoLaunchedFlow` —Autolaunched flow
that runs in the background.

**•** `Flow` —Screen flow that accepts user inputs.

`id` String ID of the flow. 45.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`name` String Name of the flow. 45.0

#### ConnectApi.NBANativeRecommendation

A record the user is recommended to take action on.

Subclass of ConnectApi.AbstractNBATarget.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the recommendation. 45.0

`name` String Name of the recommendation. 45.0

`url` String URL to the recommendation. 45.0

#### ConnectApi.NBARecommendation

A recommendation returned by a recommendation strategy.

**Property Name** **Type** **Description** **Available Version**

`aiModel` String Reserved for future use. 47.0

`acceptanceLabel` String Text indicating user acceptance of the 45.0
recommendation.

`description` String Description of the recommendation. 45.0

`externalId` String

External ID of the recommendation. This ID doesn’t 46.0
need to be a Salesforce 18-character ID. For example,
it can be a product number from an external system.

`imageUrl` String URL to the asset file to display. 45.0

`recommendation` String Reserved for future use. 46.0

```
Mode

```

`recommendation` Double Reserved for future use. 46.0

```
Score

```

`rejectionLabel` String Text indicating user rejection of the recommendation. 45.0

#### target ConnectApi. Target to act on. 45.0

```
           AbstractNBATarget

#### targetAction ConnectApi. Action to recommend. 45.0

           AbstractNBAAction

```

SEE ALSO:

#### ConnectApi.NBARecommendations


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.NBARecommendations

Recommendations returned by a recommendation strategy.

**Property Name** **Type** **Description** **Available Version**

`debug` String Runtime debug information recorded during 45.0
recommendation strategy execution.

`errors` String Runtime errors that occurred during recommendation 45.0
strategy execution.

`executionId` String ID of the recommendation strategy execution. 45.0

`onBehalfOfId` String ID of the user or entity for which the 45.0
recommendation strategy was executed.

#### recommendations List< ConnectApi. List of recommendations returned by a 45.0

`NBARecommendation`              - recommendation strategy.

#### trace ConnectApi. Trace information for the recommendation strategy 45.0

`StrategyTrace` execution, if requested.

#### ConnectApi.NetworkConnection

External network connection.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property Name** **Type** **Description** **Available Version**

`developerName` String Name of the network connection. 58.0

`id` String ID of the network connection. 58.0

`masterLabel` String Label of the network connection. 58.0

`namespacePrefix` String Namespace prefix of the network connection. 58.0

SEE ALSO:

ConnectApi.NamedCredential

#### ConnectApi.NewUserAudienceCriteria

Criteria for the new members type of custom recommendation audience.

Subclass of ConnectApi.AudienceCriteria.

**Property Name** **Type** **Description** **Available Version**

`maxDaysInCommunity` Double The maximum number of days since a user became 36.0
a site member.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.OAuthCredentialAuthUrl

OAuth authentication URL for a credential.

**Property Name** **Type** **Description** **Available Version**

`authenticationUrl` String

Authentication URL for the user external credential. 56.0

Authentication URLs have encoded and escaped
special characters. Before using the URL, undo the
encoded and escaped characters.

`external` String Fully qualified developer name of the external 56.0
`Credential` credential.

`principalName` String Name of the external credential named principal. 56.0

```
principalType

```

#### ConnectApi. Type of credential principal. Values are: 56.0

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

#### ConnectApi.OauthProviderInfo

OAuth provider information.

**Name** **Type** **Description** **Available Version**

`authorizationUrl` String The URL used for authorization. 37.0

`name` String The name of the OAuth service provider. 37.0

SEE ALSO:

ConnectApi.UserOauthInfo

#### ConnectApi.ObjectMetadata

Search metadata related to the object.

**Property Name** **Type** **Description** **Available Version**

```
dataCategories

fields

```

Map<String, Metadata on each data category for the object. 63.0

#### `ConnectApi.`

`DataCategoryMetadata` 

Map<String, Metadata on each field of the object. 63.0

#### `ConnectApi.`

`FieldMetadata` 

`label` String Name of the object. 63.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`labelPlural` String Plural name of the object. 63.0

`objectApiName` String API name of the object 63.0

#### themeInfo ConnectApi. Theme related to the object. 63.0

```
             ThemeInfo

```

SEE ALSO:

ConnectApi.SearchResultGroups

ConnectApi.SearchAnswer

ConnectApi.ScopedSearchResults

#### ConnectApi.ObjectQueryInfo

Search query metadata related to the object.

**Property Name** **Type** **Description** **Available Version**

`displayFields` List<String> Fields to display from the response. 64.0

`hasMoreResults` Boolean

Specifies whether there are more records to fetch 64.0
matching the search query for the object ( `true` ) or
not ( `false` ).

`nameField` String Name field identifier of the object. 64.0

`numberOfMatches` Integer Number of results for the object matching the search 64.0
query.

```
orderBy

```

#### List< ConnectApi. Applied order for object search. 64.0

```
SearchApplied
```

`OrderBy` 

`source` String Source name for the object. 64.0

```
spellCorrectionInfo

```

#### ConnectApi. Spell correction information for the object search. 64.0

```
SpellCorrection

Info

```

#### status ConnectApi. Status on the object search such as error messages 64.0

`SearchStatus` and warnings.

SEE ALSO:

ConnectApi.QueryInfo

ConnectApi.ScopedSearchResults


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.OCIBaseOutputRepresentation

Base Omnichannel Inventory output class.

This class is abstract.

Superclass of:

**•** ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation

**•** ConnectApi.OCIPublishLocationStructureOutputRepresentation

**•** ConnectApi.OCIPublishLocationStructureStatusOutputRepresentation

**•** ConnectApi.OCIUploadInventoryAvailabilityOutputRepresentation

**•** ConnectApi.OCIUploadInventoryAvailabilityStatusOutputRepresentation

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. Any errors that were returned. 51.0

`ErrorResponse`            

`success` Boolean Indicates whether the request was successful. 51.0

#### ConnectApi.OCICreateReservationErrorOutputRepresentation

Error returned from an attempt to create an Omnichannel Inventory reservation.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String The error code. 51.0

`message` String Details of the error, if available. 51.0

#### ConnectApi.OCICreateReservationOutputRepresentation

Result of an Omnichannel Inventory reservation creation request.

**Property Name** **Type** **Description** **Available Version**

```
details

errors

```

#### List< ConnectApi. Details for each product in the reservation. 51.0

```
OCICreateReservation
```

`SingleOutputRepresentation` 
#### List< ConnectApi. Any errors returned by the reservation request. 51.0

```
OCICreateReservation
```

`ErrorOutputRepresentation` 

`expirationTime` String The time at which the reservation would expire. 51.0

`reservationTime` String The time when the reservation was recorded. 51.0

`success` Boolean Indicates whether the reservation was successfully 51.0
created.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.OCICreateReservationSingleOutputRepresentation

Details of an inventory reservation for one product.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String The error code, if any. 51.0

`locationGroupIdentifier` String Identifier of the location group where the inventory 51.0
is reserved.

`locationIdentifier` String Identifier of the location where the inventory is 51.0
reserved.

`quantity` Double The reserved quantity of the product. 51.0

`stockKeepingUnit` String The SKU of the reserved product. 51.0

#### ConnectApi.OCIFulfillReservationErrorOutputRepresentation

Response to a request to fulfill one inventory reservation.

**Property Name** **Type** **Description** **Available Version**

```
details

```

#### ConnectApi. Details of the fulfilled reservation, if successful. 51.0

```
OCIFulfillReservation

SingleOutputRepresentation

```

`errorCode` String Error code, if any. 51.0

`message` String Details of the error, if available. 51.0

#### ConnectApi.OCIFulfillReservationOutputRepresentation

Response to a request to fulfill one or more inventory reservations.

**Property Name** **Type** **Description** **Available Version**

```
errors

```

#### List< ConnectApi. Responses for the individual reservations in the 51.0

`OCIFulfillReservation` fulfillment request.
`ErrorOutputRepresentation` 

`success` Boolean Indicates whether the request was successful. 51.0

#### ConnectApi.OCIFulfillReservationSingleOutputRepresentation

Details of a single fulfilled reservation.

**Property Name** **Type** **Description** **Available Version**

`actionRequestId` String The UUID that identifies the original fulfill reservation 51.0
request.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`externalRefId` String The external reference ID of the location that fulfilled 51.0
the reservation.

`locationIdentifier` String The identifier of the location that fulfilled the 51.0
reservation.

`quantity` Double The fulfilled quantity. 51.0

`stockKeepingUnit` String The SKU of the fulfilled product. 51.0

#### ConnectApi.OCIFutureInventoryOutputRepresentation

An expected future inventory restock.

**Property Name** **Type** **Description** **Available Version**

`expectedDate` Datetime Date when the future inventory is expected. 51.0

`quantity` Double Quantity of the future inventory. 51.0

#### ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation

Response to a request for inventory availability data.

Subclass of ConnectApi.OCIBaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
locationGroups

locations

```

SEE ALSO:

#### List< ConnectApi. A list of inventory availability data for individual 51.0

`OCILocationGroup` location groups.
`AvailabilityOutputRepresentation` 
#### List< ConnectApi. A list of inventory availability data for individual 51.0

`OCILocationAvailability` locations.
`OutputRepresentation` 

getInventoryAvailability(inventoryAvailabilityInputRepresentation)

findRoutesWithFewestSplitsUsingOCI(findRoutesWithFewestSplitsUsingOCIInput)

ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation

#### ConnectApi.OCIInventoryRecordOutputRepresentation

Inventory availability data for a product.

**Property Name** **Type** **Description** **Available Version**

`availableToFulfill` Double The Available To Fulfill quantity. 51.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`availableToOrder` Double The Available To Order quantity. 51.0

`effectiveDate` Datetime The effective date of the inventory. Indicates if the 51.0
SKU exists in the inventory.

`exists` Boolean Indicates if the SKU exists in the inventory. 62.0

```
futures

```

#### List< ConnectApi. A list of any expected future inventory restocks. 51.0

```
OCIFutureInventory
```

`OutputRepresentation` 

`onHand` Double The On Hand quantity. 51.0

`reserved` Double The Reserved quantity. 51.0

`safetyStockCount` Double The Safety Stock Count. 51.0

`stockKeepingUnit` String The SKU of the product. 51.0

#### ConnectApi.OCILocationAvailabilityOutputRepresentation

A set of inventory availability data for one inventory location.

**Property Name** **Type** **Description** **Available Version**

```
inventoryRecords

```

#### List< ConnectApi. A list of availability data for individual products at this 51.0

`OCIInventoryRecord` location.
`OutputRepresentation` 

`locationIdentifier` String The identifier of the location. 51.0

#### ConnectApi.OCILocationGroupAvailabilityOutputRepresentation

A set of inventory availability data for one inventory location group.

**Property Name** **Type** **Description** **Available Version**

A list of availability data for individual products. The 51.0
data combines the quantities for all locations
belonging to this location group.

```
inventoryRecords

```

#### List< ConnectApi.

```
OCIInventoryRecord
```

`OutputRepresentation` 

`locationGroup` String The identifier of the location group. 51.0

```
Identifier

#### ConnectApi.OCIPublishLocationStructureOutputRepresentation

```

Response to a publish location structure request.

Subclass of ConnectApi.OCIBaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`uploadId` String Identifier of the publish job. Use this value to retrieve 51.0
the status of the job.

#### ConnectApi.OCIPublishLocationStructureStatusOutputRepresentation

Detailed status of a publish location structure job.

Subclass of ConnectApi.OCIBaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`endTimeUTC` String The UTC time when the job finished. (for example: 51.0
"2020-07-06T22:54:08.012Z")

`recordsProcessedCount` Integer The number of records processed by the job. 51.0

`recordsReadCount` Integer The number of records read by the job. 51.0

`recordsSkippedCount` Integer The number of records skipped by the job. 51.0

`startTimeUTC` String The UTC time when the job started. (for example: 51.0
"2020-07-06T22:53:06.788Z")

`status` String The status of the job. (e.g., "PENDING," "COMPLETED," 51.0
etc.).

`uploadId` String Identifier of the job. 51.0

`validationErrors` List< `String`   - List of any validation errors returned by the job. 51.0

`validationStatus` String The validation status of the job. 51.0

#### ConnectApi.OCIReleaseReservationErrorOutputRepresentation

Response to a request to release one inventory reservation.

**Property Name** **Type** **Description** **Available Version**

```
details

```

#### ConnectApi. Details of the released reservation, if successful. 51.0

```
OCIReleaseReservation

SingleOutputRepresentation

```

`errorCode` String Error code, if any. 51.0

`message` String Details of the error, if available. 51.0

#### ConnectApi.OCIReleaseReservationOutputRepresentation

Response to a request to release one or more inventory reservations.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
errors

```

#### List< ConnectApi. Responses for the individual reservations in the 51.0

`OCIReleaseReservation` release request.
`ErrorOutputRepresentation` 

`success` Boolean Indicates whether the request was successful. 51.0

#### ConnectApi.OCIReleaseReservationSingleOutputRepresentation

Details of a single released reservation.

**Property Name** **Type** **Description** **Available Version**

`actionRequestId` String The UUID that identifies the original release 51.0
reservation request.

`externalRefId` String The external reference ID of the location that released 51.0
the reservation.

`locationGroupIdentifier` String The identifier of the location group that released the 51.0
reservation.

`locationIdentifier` String The identifier of the location that released the 51.0
reservation.

`quantity` Double The released quantity. 51.0

`stockKeepingUnit` String The SKU of the released product. 51.0

#### ConnectApi.OCITransferReservationErrorOutputRepresentation

Response to a request to fulfill one inventory reservation.

**Property Name** **Type** **Description** **Available Version**

```
details

```

#### ConnectApi. Details of the transferred reservation, if successful. 51.0

```
OCITransferReservation

SingleOutputRepresentation

```

`errorCode` String Error code, if any. 51.0

`message` String Details of the error, if available. 51.0

#### ConnectApi.OCITransferReservationOutputRepresentation

Response to a request to transfer one or more inventory reservations.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
errors

```

#### List< ConnectApi. Responses for the individual reservations in the 51.0

`OCITransferReservation` transfer request.
`ErrorOutputRepresentation` 

`success` Boolean Indicates whether the request was successful. 51.0

#### ConnectApi.OCITransferReservationSingleOutputRepresentation

Details of a single transferred reservation.

**Property Name** **Type** **Description** **Available Version**

`actionRequestId` String The UUID that identifies the original transfer 51.0
reservation request.

`externalRefId` String The external reference ID of the location that received 51.0
the reservation.

`fromLocationGroupIdentifier` String The identifier of the location group that sent the 51.0
reservation.

`fromLocationIdentifier` String The identifier of the location that sent the reservation. 51.0

`ignoreAvailabilityCheck` Boolean Whether this call ignored availability data at the 52.0
location that received the reservation.

`quantity` Double The quantity of transferred inventory. 51.0

`stockKeepingUnit` String The SKU of the transferred product. 51.0

`toLocationGroupIdentifier` String The identifier of the location group that received the 51.0
reservation.

`toLocationIdentifier` String The identifier of the location that received the 51.0
reservation.

#### ConnectApi.OCIUpdateReservationErrorOutputRepresentation

Error output representation for the update inventory reservation.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String The error code. 61.0

`message` String Details of the error, if available. 61.0

#### ConnectApi.OCIUpdateReservationOutputRepresentation

Result of an Omnichannel Inventory update request for reserved inventory.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
details

errors

```

List Details for each product in the reservation. 61.0
#### ConnectApi.OCIUpdateReservationSingleOutputRepresentation

[]

List Any errors returned by the reservation update 61.0
ConnectApi.OCIUpdateReservationE **r** orOutputRepresentation request.

[]

`reservationTime` String The time when the reservation was updated. 61.0

`success` Boolean Indicates whether the reservation was successfully 61.0
updated.

#### ConnectApi.OCIUpdateReservationSingleOutputRepresentation

Details of an updated reservation for one product.

**Property Name** **Type** **Description** **Available Version**

`adjustment` Double The total reservation adjustment. 61.0

`errorCode` String The error code, if any. 61.0

`locationGroupIdentifier` String Identifier of the location group where the inventory 61.0
is reserved.

`locationIdentifier` String Identifier of the location where the inventory is 61.0
reserved.

`quantity` Double The total reservation quantity of the product. 61.0

`stockKeepingUnit` String The SKU of the updated product. 61.0

#### ConnectApi.OCIUploadInventoryAvailabilityOutputRepresentation

Response to an upload inventory availability job.

Subclass of ConnectApi.OCIBaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

`uploadId` String Identifier of the upload job. Use this value to retrieve 51.0
the status of the job.

#### ConnectApi.OCIUploadInventoryAvailabilityStatusOutputRepresentation

Detailed status of an upload inventory availability job.

Subclass of ConnectApi.OCIBaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`endTimeUTC` String The UTC time when the job finished. (for example: 51.0
"2020-07-06T22:54:08.012Z")

`recordsProcessedCount` Integer The number of records processed by the job. 51.0

`recordsReadCount` Integer The number of records read by the job. 51.0

`recordsSkippedCount` Integer The number of records skipped by the job. 51.0

`startTimeUTC` String The UTC time when the job started. (for example: 51.0
"2020-07-06T22:53:06.788Z")

`status` String The overall status of the inventory availability upload 51.0
(e.g. "PENDING", "COMPLETED").

`uploadId` String Identifier of the job. 51.0

`validationErrors` List< `String`   - List of any validation errors returned by the job. 51.0

`validationStatus` String The validation status of the job. 51.0

#### ConnectApi.OpportunityStagePicklistValueAttributes

Opportunity stage picklist value attributes.

Subclass of ConnectApi.AbstractPicklistValueAttributes

**Property Name** **Type** **Description** **Available Version**

`closed` Boolean

Specifies whether the opportunity has a stage of 66.0
closed ( `true` ) or not ( `false` ). Multiple opportunity
stage values can represent a closed opportunity.

`forecastCategoryName` String Default percentage estimate of the confidence in 66.0
closing an opportunity for this opportunity stage

value. Value is `null` if forecasting isn’t enabled for
the org.

`deafultProbability` Double

`won` Boolean

Default forecast category value for this opportunity 66.0
stage value. Value is `null` if forecasting isn’t
enabled for the org.

Specifies whether the opportunity has a stage of won 66.0
( `true` ) or not ( `false` ). Multiple opportunity stage
values can represent a won opportunity.

[For more information, see the OpportunityStage object documentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_opportunitystage.htm)

#### ConnectApi.OrchestrationInstance

Orchestration instance.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`flowDefinition` String Developer name of the flow definition. 54.0

```
   DeveloperName

```

`flowDefinitionId` String ID of the flow definition. 54.0

`flowDefinitionName` String Name of the flow definition. 54.0

`id` String ID of the orchestration instance. 54.0

`interviewId` String ID of the interview to resume. 54.0

```
stageInstances

status

```

SEE ALSO:

#### List< ConnectApi. Orchestration stage instances. 54.0

```
OrchestrationStage
```

`Instance` 

#### ConnectApi. Status of the orchestration instance. Values are: 54.0

```
Orchestration
```

**•** `Canceled`
```
Status

```

**•** `Canceled`

**•** `Completed`

**•** `Discontinued`

**•** `Error`

**•** `InProgress`

**•** `NotStarted`

**•** `Suspended`

#### ConnectApi.OrchestrationInstanceCollection

getOrchestrationInstanceCollection(relatedRecordId)

getOrchestrationInstanceCollection(relatedRecordId, relatedOrchestrationId)

#### ConnectApi.OrchestrationInstanceCollection

Collection of orchestration instances.

**Property Name** **Type** **Description** **Available Version**

#### instances List< ConnectApi. Collection of orchestration instances. 54.0

`OrchestrationInstance`             

SEE ALSO:

getOrchestrationInstance(instanceId)

#### ConnectApi.OrchestrationStageInstance

Orchestration stage instance.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`completionTime` String The duration of the stage in seconds. 63.0

`id` String ID of the orchestration stage instance. 54.0

`label` String Orchestration stage instance label. 54.0

`name` String Orchestration stage instance name. 54.0

```
status

stepInstances

```

SEE ALSO:

#### ConnectApi. Status of the orchestration instance. Values are: 54.0

```
Orchestration
```

**•** `Canceled`
```
Status

```

**•** `Canceled`

**•** `Completed`

**•** `Discontinued`

**•** `Error`

**•** `InProgress`

**•** `NotStarted`

**•** `Suspended`

#### List< ConnectApi. Orchestration stage instance steps. 54.0

```
OrchestrationStep
```

`Instance` 

ConnectApi.OrchestrationInstance

#### ConnectApi.OrchestrationStepInstance

Orchestration step instance.

**Property Name** **Type** **Description** **Available Version**

`assignedTo` String The ID of the user, group, or queue that's assigned 63.0
to a work item.

`assigneeType` String The assignee type associated with a work item. Valid 63.0
values are:

**•** Group

**•** Invalid

**•** Queue

**•** User

`comments` String

The string stored in an output variable with the API 63.0
name of Comments from a flow called by a
completed orchestration step.

`completedBy` String The user ID of the user who completed the work item. 63.0

`completionTime` String The duration of the step in seconds. 63.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`description` String The description associated with the orchestration 63.0
step.

`id` String ID of the orchestration step instance. 54.0

`label` String Orchestration step instance label. 54.0

`name` String Orchestration step instance name. 54.0

```
status

stepType

workItems

```

SEE ALSO:

#### ConnectApi. Status of the orchestration instance. Values are: 54.0

```
Orchestration
```

**•** `Canceled`
```
Status

```

**•** `Canceled`

**•** `Completed`

**•** `Discontinued`

**•** `Error`

**•** `InProgress`

**•** `NotStarted`

**•** `Suspended`

#### ConnectApi. Type of orchestration step. Values are: 54.0

```
Orchestration
```

**•** `AsynchronousBackgroundStep`
```
StepType

```

**•** `AsynchronousBackgroundStep`

**•** `ApprovalStep`

**•** `BackgroundStep`

**•** `InteractiveStep`

**•** `ManagedContentRoleInteractiveStep`

**•** `ManagedContentVariantAutoPublishBackgroundStep`

**•** `ManagedContentVariantAutoUnpublishBackgroundStep`

**•** `ManagedContentVariantSetLock`

```
            BackgroundStep

```

**•** `ManagedContentVariantSetReady`

```
            BackgroundStep

```

**•** `MuleSoftStep`

#### List< ConnectApi. Orchestration step instance work items. 54.0

```
Orchestration
```

`WorkItem` 

ConnectApi.OrchestrationStageInstance

#### ConnectApi.OrchestrationWorkItem

Orchestration work item.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`assigneeId` String ID of the assignee for the orchestration work item. 54.0

`createdDate` Datetime Date when the orchestration work item was created. 61.0

`description` String Description of the orchestration work item. 54.0

`flowType` String Flow type of the orchestration that created the 62.0
orchestration work item.

`id` String ID of the orchestration work item. 54.0

`label` String Label key for the orchestration work item. 54.0

`lastModifiedDate` Datetime Date when the work item was last modified. 61.0

`relatedRecordId` String ID of the record the orchestration work item is related 54.0
to.

`screenFlow` String Developer name of the screen flow to start when 54.0
`DeveloperName` assignees work on the orchestration work item.

`screenFlowId` String ID of the screen flow to start when assignees work 54.0
on the orchestration work item.

`screenFlowInputs` String Input parameters for the screen flow. 54.0

```
status

```

SEE ALSO:

#### ConnectApi. Status of the orchestration work item. Values are: 54.0

```
OrchestrationWork
```

**•** `Assigned`
```
ItemStatus

```

**•** `Assigned`

**•** `Completed`

ConnectApi.OrchestrationStepInstance

#### ConnectApi.OrderDeliveryGroupSummary

Order delivery group summary.

**Property Name** **Type** **Description** **Available Version**

`fields` Map<String, Map of fields from order delivery group summary and 51.0
`ConnectApi.RecordField`              - other related objects that were queried.

SEE ALSO:

#### ConnectApi.OrderDeliveryGroupSummaryCollection ConnectApi.OrderDeliveryGroupSummaryCollection

Collection of order delivery group summaries.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page of order delivery 51.0
group summaries.

`currentPageUrl` String URL to the current page of order delivery group 51.0
summaries.

`nextPageToken` String Token identifying the next page of order delivery 51.0
group summaries.

`nextPageUrl` String URL to the next page of order delivery group 51.0
summaries.

```
orderDeliveryGroups

```

#### List< ConnectApi. Collection of order delivery group summaries. 51.0

```
OrderDelivery
```

`GroupSummary` 

`previousPageToken` String Token identifying previous page of order delivery 51.0
group summaries.

`previousPageUrl` String URL to the previous page of order delivery group 51.0
summaries.

#### ConnectApi.OrderDeliveryGroupSummaryLookupOutput

Order delivery group summary lookup output.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 58.0
the order delivery group summary record.

#### deliveryMethod ConnectApi.OrderDeliveryMethodLookupOutput Delivery method associated with order the delivery 58.0

group summary.

```
fields

```

Map<String, Map of requested order delivery group summary 58.0

`ConnectApi.RecordField` ConnectApi.RecordField fields.
on page 2501>

`id` String ID of the order delivery group summary. 58.0

`lineItems` <List `ConnectApi.OrderSummaryLookupOutput` - Line items associated with the order delivery group 58.0
summary.

#### ConnectApi.OrderDeliveryMethodLookupOutput

Order delivery method lookup output.

**Property Name** **Type** **Description** **Available Version**

`fields` Map<String, Map of requested order delivery method fields. 58.0
`ConnectApi.RecordField`              


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the order delivery method. 58.0

#### ConnectApi.OrderItemSummary

Order item summary.

**Property Name** **Type** **Description** **Available Version**

```
adjustmentAggregates

fields

```

#### ConnectApi. Adjustment aggregates associated with an order item 55.0

`OrderItemSummary` summary.

```
AdjustmentAggregates

```

Map<String, Map of fields from order item summary and other 51.0
#### ConnectApi. related objects that were queried.

`RecordField` 

`orderItem` String ID of the order item summary. 51.0

```
SummaryId

```

`orderSummaryId` String ID of the order summary. 51.0

```
product

```

SEE ALSO:

#### ConnectApi. Associated product item information. 51.0

```
OrderItemSummary

Product

```

#### ConnectApi.OrderItemSummaryCollection ConnectApi.OrderItemSummaryAdjustmentAggregates

Adjustment aggregates associated with an order item summary.

**Property Name** **Type** **Description** **Available Version**

`available` Boolean Indicates whether adjustment aggregates are 55.0
available ( `true` ) or not ( `false` ).

```
status

```

#### ConnectApi. Order summary adjustment aggregate job status. 55.0

```
OrderSummaryAdjustment
```

**•** `Failed` —The adjustment aggregate data job

`AggregatesStatus` for the order summary failed.

**•** `InProgress` —The adjustment aggregate
data job for the order summary is in progress.

**•** `NotInitiated` —The adjustment aggregate
data job for the order summary is not initiated.

**•** `Submitted` —The adjustment aggregate data
job for the order summary is submitted.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalLine` String Total of all line item promotions applied to this 55.0
`PromotionAmount` specific product.

`totalPromotion` String Total of all order level promotions applied to this 55.0
`DistAmount` specific product.

#### ConnectApi.OrderItemSummaryAdjustmentCollection

Collection of adjustments for order item summaries.

**Property Name** **Type** **Description** **Available Version**

```
orderItemSummaries

```

Map<String, Order item summaries and their associated 53.0
#### ConnectApi. adjustments.

```
OrderItemSummary
```

`AdjustmentList` 

#### ConnectApi.OrderItemSummaryAdjustmentList

Representation for list of adjustments for an Order Item Summary.

**Property Name** **Type** **Description** **Available Version**

```
adjustments

```

SEE ALSO:

#### List< ConnectApi. Adjustments associated with an order item summary. 53.0

```
OrderSummary
```

`Adjustment` 

#### ConnectApi.OrderItemSummaryAdjustmentCollection ConnectApi.OrderItemSummaryCollection

Collection of order item summaries.

**Property Name** **Type** **Description** **Available Version**

`currentPageToken` String Token identifying the current page of items. 51.0

`currentPageUrl` String URL to the current page of items. 51.0

#### items List< ConnectApi. Collection of order item summaries. 51.0

`OrderItemSummary`          

`nextPageToken` String Token identifying the next page of items. 51.0

`nextPageUrl` String URL to the next page of items. 51.0

`previousPageToken` String Token identifying the previous page of items. 51.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`previousPageUrl` String URL to the previous page of items. 51.0

#### ConnectApi.OrderItemSummaryLookupOutput

Order item summary lookup output.

**Property Name** **Type** **Description** **Available Version**

`adjustmentAggregates` `ConnectApi.OrderItemSummaryAdjustmentAggregates` Adjustment aggregates for the order item summary. 58.0

`adjustments` <List `ConnectApi.OrderSummaryAdjustment`   - Adjustments associated with the order item 58.0
summary.

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 58.0
the order item summary record.

`fields` Map<String, Map of requested order item summary fields. 58.0
`ConnectApi.RecordField`                 

`id` String ID of the order item summary. 58.0

`product` `ConnectApi.OrderSummaryProductLookupOutput` Details of the product associated with order item 58.0
summary.

#### ConnectApi.OrderItemSummaryOutputRepresentation

Details of an OrderItemSummary from a failed FulfillmentOrder in a create multiple fulfillment orders request.

**Property Name** **Type** **Description** **Available Version**

#### errors List< ConnectApi. List of errors specific to the OrderItemSummary, if 50.0

`ErrorResponse`            - any.

`orderItemSummaryId` String ID of the OrderItemSummary. 50.0

`quantity` Double Quantity of the OrderItemSummary. 50.0

#### ConnectApi.OrderItemSummaryProduct

Product item mapped to the order item summary.

**Property Name** **Type** **Description** **Available Version**

`canViewProduct` Boolean Specifies whether the context user can view the 51.0
product ( `true` ) or not ( `false` ).

`errorCode` String Error code for the product with errors. 51.0

`errorMessage` String Error message for the product with errors. 51.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
fields

```

Map<String, Map of the product fields queried. 51.0

#### `ConnectApi.`

`RecordField` 

#### media ConnectApi. Associated product media. 51.0

```
          ProductMedia

```

```
productAttributes

```

#### ConnectApi. Summary of the product attributes. 51.0

```
ProductAttributeSet

Summary

```

`productId` String ID of the product. 51.0

SEE ALSO:

ConnectApi.OrderItemSummary

#### ConnectApi.OrderQuantitiesOutputRepresentation

Output groupings of items in an order

**Property Name** **Type** **Description** **Available Version**

`externalOrderId` String String representation of the grouping of SKUs. 58.0

`itemQuantities` <List `>ConnectApi.ItemQuantityOutputRepresentation` - List of items and quantities. 58.0

#### ConnectApi.OrderShipment

Order shipment.

**Property Name** **Type** **Description** **Available Version**

`expectedDeliveryDate` Datetime Expected delivery date for the shipment. 52.0

```
fields

```

Map<String, Map of requested fields. 52.0

#### `ConnectApi.`

`RecordField` 

`orderSummaryId` String ID of the order summary. 52.0

`shipmentId` String ID of the shipment. 52.0

`shipmentNumber` String Number of the shipment. 52.0

`status` String Status of the shipment. 52.0

SEE ALSO:

#### ConnectApi.OrderShipmentCollection


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.OrderShipmentCollection

Collection of order shipments.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Total number of records returned in the collection. 52.0

`currentPageToken` String Token identifying the current page of order 52.0
shipments.

`currentPageUrl` String URL to the current page of order shipments. 52.0

`nextPageToken` String Token identifying the next page of order shipments. 52.0

`nextPageUrl` String URL to the next page of order shipments. 52.0

`previousPageToken` String Token identifying the previous page of order 52.0
shipments.

`previousPageUrl` String URL to the previous page of order shipments. 52.0

#### shipments List< ConnectApi. Collection of order shipments. 52.0

`OrderShipment`            
#### sortOrder ConnectApi. Sort order for order shipments. Values are: 52.0

```
             OrderShipmentSort
```

**•** `ExpectedDeliveryDateAsc` —Sorts by
the oldest expected delivery date.

**•** `ExpectedDeliveryDateDesc` —Sorts by
the most recent expected delivery date.

**•** `ShipmentNumberAsc` —Sorts by shipment
number in ascending order (0–9).

**•** `ShipmentNumberDesc` —Sorts by shipment
number in descending order (9–0).

#### ConnectApi.OrderShipmentItem

Shipment item.

**Property Name** **Type** **Description** **Available Version**

```
fields

```

Map<String, Map of requested fields. 52.0

#### `ConnectApi.`

`RecordField` 

`orderItemSummaryId` String ID of the order item summary. 52.0

```
product

```

#### ConnectApi. Product mapped to an order item summary. 52.0

```
OrderItem

SummaryProduct

```

`productId` String ID of the product. 52.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`quantity` Double Quantity of the product. 52.0

`shipmentId` String ID of the shipment. 52.0

`shipmentItemId` String ID of the shipment item. 52.0

#### ConnectApi.OrderShipmentItemCollection

Collection of order shipment items.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Total number of records returned in a page. 52.0

`currentPageToken` String Token identifying the current page of order shipment 52.0
items.

`currentPageUrl` String URL to the current page of order shipment items. 52.0

#### items List< ConnectApi. Collection of order shipment items. 52.0

`OrderShipmentItem`              

`nextPageToken` String Token identifying the next page of order shipment 52.0
items.

`nextPageUrl` String URL to the next page of order shipment items. 52.0

`previousPageToken` String Token identifying the previous page of order 52.0
shipment items.

`previousPageUrl` String URL to the previous page of order shipment items. 52.0

```
sortOrder

```

#### ConnectApi. Sort order for order shipment items. Values are: 52.0

```
OrderShipment
```

**•** `IdAsc` —Sorts by ID in ascending alphanumeric

`ItemSort` order (A–Z, 0–9).

**•** `IdDesc` —Sorts by ID in descending
alphanumeric order (Z–A, 9–0).

#### ConnectApi.OrderSummaryAdjustment

Adjustment associated with an order summary.

**Property Name** **Type** **Description** **Available Version**

`amount` String Amount associated with the adjustment. 53.0

`basisReferenceDisplayName` String

Display name for secondary cause of the adjustment 54.0
(for example, Null or the CouponCode that’s
associated with a Coupon)


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 53.0
the adjustment.

`displayName` String Display name for the primary cause of the adjustment 53.0
(for example, Display name of the Promotion)

#### targetType ConnectApi. Type of price adjustment in promotions. Values are: 56.0

```
             OrderSummary
```

**•** `SplitLine` —Price adjustment on an order
`AdjustmentTarget` item.
```
             Type
```

**•** `Header` —Price adjustment on the entire order.

`type` String Type of adjustment (for example, Promotion, Other). 53.0

SEE ALSO:

ConnectApi.OrderSummaryAdjustmentCollection

ConnectApi.OrderItemSummaryAdjustmentList

#### ConnectApi.OrderSummaryAdjustmentAggregates

Adjustment aggregates associated with an order summary.

**Property Name** **Type** **Description** **Available Version**

`available` Boolean Indicates if adjustment aggregate values are available 55.0
( `true` ) or not ( `false` ).

```
status

```

#### ConnectApi. Order summary adjustment aggregate job status. 55.0

`OrderSummaryAdjustment` Values are:

```
AggregatesStatus
```

**•** `Failed` —The adjustment aggregate data job
for the order summary failed.

**•** `InProgress` —The adjustment aggregate
data job for the order summary is in progress.

**•** `NotInitiated` —The adjustment aggregate
data job for the order summary is not initiated.

**•** `Submitted` —The adjustment aggregate data
job for the order summary is submitted.

`totalDelivery` String Total distributed delivery promotion amounts 55.0
`PromotionDistAmount` associated with an order summary.

`totalDelivery` String Total delivery promotion line amounts associated 55.0
`PromotionLineAmount` with an order summary.

`totalDelivery` String Total delivery promotion amount associated with an 55.0
`Promotion` order summary.

```
TotalAmount

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalProduct` String Total distributed product promotion amounts 55.0
`PromotionDistAmount` associated with an order summary.

`totalProduct` String Total product promotion line amount associated with 55.0
`PromotionLineAmount` an order summary.

`totalProduct` String Total product promotion amount associated with an 55.0
`Promotion` order summary.

```
   TotalAmount

#### ConnectApi.OrderSummaryAdjustmentAggregatesAsyncOutput

```

Async adjustment aggregates output.

**Property Name** **Type** **Description** **Available Version**

`statusURL` String Status URL. 55.0

#### ConnectApi.OrderSummaryAdjustmentCollection

Collection of adjustments for an order summary.

**Property Name** **Type** **Description** **Available Version**

```
adjustments

```

#### List< ConnectApi. Collection of adjustments for an order summary. 53.0

```
OrderSummary
```

`Adjustment` 

#### ConnectApi.OrderSummaryCollectionRepresentation

Collection of order summaries.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Total count of order summaries returned on the 51.0
current page.

`currentPageToken` String Token identifying the current page. 51.0

`currentPageUrl` String Connect REST API URL identifying the current page. 51.0

`nextPageToken` String Token identifying the next page, or `null` if there 51.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 51.0
`null` if there isn’t a next page.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
orderSummaries

```

#### List< ConnectApi. Collection of order summaries. 51.0

```
OrderSummary
```

`Representation` 

`previousPageToken` String Token identifying the previous page, or `null` if 51.0
there isn’t a previous page.

`previousPageUrl` String Connect REST API URL identifying the previous page, 51.0
or `null` if there isn’t a previous page.

```
sortOrder

```

#### ConnectApi. Sort order for order summaries. Values are: 51.0

```
OrderSummary
```

**•** `CreatedDateAsc` —Sorts by the oldest

`SortOrder` created date.

**•** `CreatedDateDesc` —Sorts by the most
recent created date.

**•** `OrderedDateAsc` —Sorts by the oldest
ordered date.

**•** `OrderedDateDesc` —Sorts by the most
recent ordered date.

#### ConnectApi.OrderSummaryLookupOutput

Order summary lookup output.

**Property Name** **Type** **Description** **Available Version**

`adjustmentAggregates` `ConnectApi.OrderSummaryAdjustmentAggregates` Adjustment aggregates associated with the order 58.0
summary.

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 58.0
the order summary.

`deliveryGroups` <List `ConnectApi.OrderDeliveryGroupSummaryLookupOutput` - Delivery groups associated with the order summary. 58.0

`fields` Map<String, Map of requested order summary fields. 58.0
`ConnectApi.RecordField`              

`id` String ID of the order summary. 58.0

`orderNumber` String Reference number of the order summary. 58.0

`status` String Status associated with the order summary. 58.0

#### ConnectApi.OrderSummaryOutputRepresentation

ID of the created Order Summary.

Subclass of ConnectApi.BaseOutputRepresentation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`orderSummaryId` String ID of the Order Summary. 48.0

#### ConnectApi.OrderSummaryProductLookupOutput

Order summary product lookup output.

**Property Name** **Type** **Description** **Available Version**

`canViewProduct` Boolean Specifies whether the context user can view the 58.0
product (true) or not (false).

`errorCode` String Error code captured during product load. 58.0

`errorMessage` String Error message captured during product load. 58.0

`fields` Map<String, Map of requested product fields. 58.0
`ConnectApi.RecordField`                 

`id` String Id of the product 58.0

`media` `ConnectApi.ProductMedia` Associated product media. 58.0

`variationAttributes` Map<String, Variation attributes (color, size, and so on) associated 58.0
`ConnectApi.OrderSummaryProductAttribute`                             - with the product.

#### ConnectApi.OrderSummaryRepresentation

Order summary.

**Property Name** **Type** **Description** **Available Version**

```
adjustmentAggregates

```

#### ConnectApi. Adjustment aggregates associated with the order 55.0

`OrderSummary` summary.

```
AdjustmentAggregates

```

`createdDate` Datetime Created date of the order summary. 51.0

```
fields

```

Map< String, Map of requested order summary fields. 51.0

#### `ConnectApi.`

`RecordField` 

`orderNumber` String Order number of the order summary. 51.0

`orderSummaryId` String ID of the order summary. 51.0

`orderedDate` Datetime Ordered date of the order summary. 51.0

`ownerId` String ID of the owner of the order summary. 51.0

`status` String Status of the order summary. 51.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalAmount` String Total amount of the order summary. 51.0

SEE ALSO:

ConnectApi.OrderSummaryCollectionRepresentation

#### ConnectApi.OrderSummaryProductAttribute

Order summary product attribute representation.

**Property Name** **Type** **Description** **Available Version**

`label` String Label or display name of the attribute. 58.0

`sequence` Integer Sequence of the attribute set with regard to the 58.0
product.

`value` String Display value of the attribute. 58.0

#### ConnectApi.OrderToCartFailedProduct

Product that could not be added to the cart from an order, with error information.

**Property Name** **Type** **Description** **Available Version**

`errorCode` String Error code. 57.0

`errorMessage` String Error message about the cause of the failure. 57.0

`productId` String ID of the product. 57.0

`productName` String Name of the product. 57.0

`productSKU` String SKU of the product. 57.0

#### ConnectApi.OrderToCartResult

Result of action adding an order to a cart.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the cart. 57.0

`totalFailedProductCount` Integer Number of products that couldn't be successfully 57.0
added to the cart from the order.

`totalSucceededProductCount` Integer Number of products successfully added to the cart 57.0
from the order.

#### unaddedProducts <List ConnectApi.OrderToCartFailedProduct > List of products not successfully added to the cart. 57.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.OrganizationSettings

Org settings.

**Name** **Type** **Description** **Available**
**Version**

`accessTimeout` Integer Amount of time after which the system prompts users 28.0
who have been inactive to log out or continue working.

`features` `ConnectApi.Features` Information about features available in the org. 28.0

`maintenanceInfo` List< `ConnectApi.MaintenanceInfo`    - Information about a list of upcoming scheduled 34.0
maintenances for the org.

`name` String Org name. 28.0

`orgId` String 18-character ID for the org. 28.0

`userSettings` `ConnectApi.UserSettings` Information about the org permissions for the user. 28.0

#### ConnectApi.OriginCapability

If a feed element has this capability, it was created by a feed action.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`actor` ConnectApi.UserSummary The user who executed the feed action. 33.0

`originRecord` ConnectApi.Reference A reference to the feed element containing the feed 33.0
action.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.OutOfOffice

User's out-of-office message.

**Property Name** **Type** **Description** **Available Version**

`message` String Out-of-office message for the user. 40.0

SEE ALSO:

ConnectApi.User

ConnectApi.MentionCompletion


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.PageInfo

Page position information for the object search.

**Property Name** **Type** **Description** **Available Version**

`hasNextPage` Boolean Specifies whether the search has more results to 63.0
return ( `true` ) or not ( `false` ).

`offset` Integer Search page offset position. 63.0

`pageSize` Integer Number of results per page. 63.0

SEE ALSO:

ConnectApi.SearchObject

#### ConnectApi.PardotBusinessUnitContextItem

Pardot business unit context item.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property Name** **Type** **Description** **Available Version**

`id` String ID of the PardotTenant record. 55.0

`isCurrent` Boolean Specifies whether the business unit is selected as the 55.0
context user's current business unit context in the

business unit switcher of the Pardot Lightning app
( `true` ) or not ( `false` ).

`name` String Name of the Pardot business unit as it is specified in 55.0
the `MasterLabel` of the PardotTenant record.

SEE ALSO:

#### ConnectApi.PardotBusinessUnitContextOutput ConnectApi.PardotBusinessUnitContextOutput

Pardot business unit context.

**Property Name** **Type** **Description** **Available Version**

```
businessUnits

```

#### List< ConnectApi. List of the Pardot business unit context items that 55.0

`PardotBusiness` the context user has access to.
`UnitContextItem` 

`isSuccess` Boolean Indicates whether the requested resource was 55.0
successfully provided.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalBusinessUnits` Integer Indicates the total number of Pardot business units 55.0
that the context user has access to.

#### ConnectApi.PaymentAuthAdjustmentResponse

Authorization Adjustment output representation.

**Property Name** **Type** **Description** **Available Version**

`accountId` String ID of the account containing the payment 51.0
authorization being adjusted.

`amount` Double Amount of the payment authorization adjustment. 51.0

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 51.0
the payment authorization adjustment.

`effectiveDate` Datetime Date when the authorization adjustment becomes 51.0
effective.

`id` String ID of the PaymentAuthAdjustment record. 51.0

`paymentAuthAdjustmentNumber` String System-defined reference number. 51.0

`requestDate` Datetime Date when the authorization adjustment transaction 51.0
occurred.

`status` String Status of the payment authorization 51.0
adjustment.Possible values are:

**•** `Canceled` : The payment authorization reversal
has been canceled. The parent authorization has
returned to its pre-reversal balance.

**•** `Draft` : The payment authorization reversal can
be edited before applying it against the parent
authorization.

**•** `Processed` : The payment authorization
reversal has been finalized.

Users can change the status as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

#### ConnectApi.PaymentAuthorizationResponse

Payment authorization output representation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`accountId` String Salesforce account for the payment authorization. 51.0

`amount` Double Amount that the gateway authorized for the payment 51.0
transaction.

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 51.0
the payment group record.

`effectiveDate` Datetime Date that the authorization becomes effective. 51.0

`expirationDate` Datetime Date that the authorization expires. 51.0

`id` String ID of the payment authorization record. 51.0

`paymentAuthorizationNumber` String System-defined number for the payment 51.0
authorization record.

`requestDate` Datetime Date that the authorization occurred. 51.0

`status` String Status of the payment authorization as returned by 51.0
the gateway.

#### ConnectApi.PaymentGroupResponse

Payment group.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 50.0
the payment group record.

`id` String ID of the payment group record. 50.0

`sourceObjectId` String Source object ID of the payment group record. 50.0
Supports only OrderId.

#### ConnectApi.PaymentCreditOutputRepresentation

The payment credit ID, amount, and order payment summary ID for a newly created payment credit. Represents a single credit transaction
that was applied to a specific payment method with the generated credit ID for tracking.

**Property Name** **Type** **Description** **Available Version**

`amount` Double The amount in the payment credit. 65.0

`orderPaymentSummaryId` String The order payment summary’s ID. 65.0

`paymentCreditId` String The created payment credit’s ID. 65.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.PaymentCreditSequenceItemOutputRepresentation

The representation of individual payment credit items. Each item represents a specific payment method and the amount of credit to be
applied to it.

**Property Name** **Type** **Description** **Available Version**

`creditType` String The type of payment credit that is being issued. Must 65.0
be a valid value on the Credit Type picklist.

#### ConnectApi.PaymentMethodDetails

Details about the payment method.

**Property Name** **Type** **Description** **Available Version**

```
alternative

PaymentMethod

```

#### ConnectApi. Alternative Payment Method details. 56.0

AlternativePayment
MethodOutput

`cardPaymentMethod` ConnectApi.CardPayment Card Payment Method details. 56.0
MethodOutput

#### ConnectApi.PaymentMethodResponse

Payment method information response.

**Property Name** **Type** **Description** **Available Version**

`accountId` String Salesforce Payments account to which this payment 51.0
method is linked.

`id` String ID of the payment method. 51.0

#### paymentMethod ConnectApi. Details about the payment method.

`Details` PaymentMethodDetails

`status` String Status of the payment method. 51.0

#### ConnectApi.PaymentMethodTokenizationGatewayResponse

Payment method tokenization gateway response representation.

Subclass of ConnectApi.AbstractGatewayResponse.

**Property Name** **Type** **Description** **Available Version**

`gatewayToken` String The payment method token sent from the gateway. 52.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.PaymentMethodTokenizationResponse

Payment method tokenization output representation.

**Property Name** **Type** **Description** **Available Version**

#### `error ConnectApi.`

```
          ErrorResponse

```

Error representation for the payment method 52.0
tokenization process. Sent only if the tokenization
process encounters an error in the gateway.

```
gatewayResponse

```

#### ConnectApi. Response containing the tokenized payment method 52.0

`PaymentMethodTokenization` value from the payment gateway.

```
GatewayResponse

```

#### paymentGatewayLogs List< ConnectApi. Logs showing more details about the tokenization 52.0

`GatewayLogResponse`           - process that occurred in the gateway.

#### paymentMethod ConnectApi.PaymentMethod Object representation of the payment method object 52.0

`Response` that was tokenized.

#### ConnectApi.PaymentResponse

Payment output.

**Property Name** **Type** **Description** **Available Version**

`accountId` String ID of the account related the payment record. 50.0

`amount` Double Total amount of the payment transaction performed 50.0
in the payment request.

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 50.0
the payment output.

`effectiveDate` Datetime Date that the payment becomes effective. 50.0

`id` String ID of the payment record. 50.0

`paymentNumber` String Number of the payment record created as a result of 50.0
the request processing.

`requestDate` Datetime Date when the payment transaction occurred. 50.0

`status` String Status of the new payment record. Can be DRAFT, 50.0
PROCESSED or CANCELLED.

#### ConnectApi.PercentRecordField

Record field containing a percentage value.

Subclass of ConnectApi.LabeledRecordField.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`value` Double Value of the percentage. 29.0

#### ConnectApi.PhoneNumber

Phone number.

**Name** **Type** **Description** **Available Version**

`label` String A localized string indicating the phone type. 30.0

`phoneNumber` String Phone number. 28.0

`phoneType` String Phone type. Values are: 30.0

**•** `Fax`

**•** `Mobile`

**•** `Work`

These values are not localized.

`type` String 28.0–29.0
Note: This property is not available after version 29.0. Use
the `phoneType` property instead.

Values are:

**•** `Fax`

**•** `Mobile`

**•** `Work`

These values are not localized.

SEE ALSO:

ConnectApi.DatacloudCompany

ConnectApi.DatacloudContact

ConnectApi.UserDetail

#### ConnectApi.Photo

Profile photo.

**Name** **Type** **Description** **Available Version**

`fullEmailPhotoUrl` String A temporary URL to the large profile picture. The URL expires after 28.0
30 days and is available to unauthenticated users.


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

`largePhotoUrl` String

`mediumPhotoUrl` String

URL to the large profile picture. The default width is 200 pixels, and 28.0
the height is scaled so the original image proportions are
maintained.

If a user hasn’t uploaded a photo, this URL points to a default photo.
If the user hasn’t uploaded a photo and the request header included

_`X-Connect-Theme: Salesforce1`_, this URL points to a
default photo based on a theme that the admin selected for the
org.

URL to the medium profile picture. The default width is 160 pixels, 37.0
and the height is scaled so the original image proportions are
maintained.

If a user hasn’t uploaded a photo, this URL points to a default photo.
If the user hasn’t uploaded a photo and the request header included

_`X-Connect-Theme: Salesforce1`_, this URL points to a
default photo based on a theme that the admin selected for the
org.

`photoVersionId` String 18–character ID to that version of the photo 28.0

`smallPhotoUrl` String

URL to the small profile picture. The default size is 64x64 pixels. 28.0

If a user hasn’t uploaded a photo, this URL points to a default photo.
If the user hasn’t uploaded a photo and the request header included

_`X-Connect-Theme: Salesforce1`_, this URL points to a
default photo based on a theme that the admin selected for the
org.

`standardEmail` String A temporary URL to the small profile. The URL expires after 30 days 28.0
`PhotoUrl` and is available to unauthenticated users.

`url` String A resource that returns a Photo object: for example, 28.0
`/services/data/v66.0/chatter/users/005D0000001LL8OIAW/photo` .

SEE ALSO:

ConnectApi.ChatterGroup

ConnectApi.RecommendationDefinition

ConnectApi.User

#### ConnectApi.PicklistRecordField

Record field containing an enumerated value.

Subclass of ConnectApi.LabeledRecordField.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.PicklistValue

Picklist value.

**Property Name** **Type** **Description** **Available Version**

```
attributes

```

#### ConnectApi. Picklist value attributes. 66.0

```
AbstractPicklist

ValueAttributes

```

`label` String Displayable value of the picklist to use. 66.0

`validFor` List<Integer> If the picklist is a dependent picklist, the property 66.0
contains a list of the controlling value indexes for

which this value is valid. If the picklist is an
independent picklist, the list is empty.

`value` String Value of the picklist to use. 66.0

SEE ALSO:

#### ConnectApi.PicklistValues ConnectApi.PicklistValues

Picklist values for a field, scoped to a record type. If a picklist is dependent, this response includes the values of its immediate controlling
field and how they map to the picklist.

**Property Name** **Type** **Description** **Available Version**

`controllerValues` Map<String, Integer>

If the picklist is dependent, this property is a map of 66.0
its immediate controlling field’s picklist values to their
indexes.

**•** If the controlling field is a picklist, the string is the
picklist value and the integer is the value’s index.

**•** If the controlling field is a checkbox, the values
in the map are `"false": 0` and `"true":`
`1` .

If the picklist is independent, the map is empty.

#### defaultValue ConnectApi. Default value for the picklist, or null if there isn’t 66.0

`PicklistValue` one.

`url` String User Interface API resource that represents this 66.0
payload.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### values List< ConnectApi. List of values for this object, record type, field 66.0

`PicklistValue`            - combination.

SEE ALSO:

#### ConnectApi.PicklistValuesCollection ConnectApi.PicklistValuesCollection

Collection of picklist values for all the picklists of a record type.

**Property Name** **Type** **Description** **Available Version**

`picklistField` Map<String, ConnectApi. A map of field names to picklist values. The map 66.0
`Values` PicklistValues> contains all the picklist values for all the picklists of a
record type, including dependent picklists. If a field
isn’t a picklist, it isn’t represented in the map.

SEE ALSO:

getPicklistValuesByRecordType(objectApiName, recordTypeId)

#### ConnectApi.PinCapability

If a feed element has this capability, users who have permission can pin it to a feed.

Subclass of ConnectApi.FeedElementCapability.

**Property Name** **Type** **Description** **Available Version**

`isPinnableByMe` Boolean Specifies whether the context user can pin or unpin 41.0
the entity to the feed ( `true` ) or not ( `false` ).

`isPinned` Boolean Specifies whether the entity is pinned ( `true` ) or not 41.0
pinned ( `false` ) to the feed.

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.PinnedFeedElements

List of pinned feed elements for a feed.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### elements List< ConnectApi. List of pinned feed elements. 41.0

`FeedElement`            
Note: In the UI, pinned feed elements don’t
show all auxiliary information, such as
comments, likes, interaction counts, or read
by information. As a result, the

```
                          ConnectApi.PinnedFeedElements
```

output class doesn’t include all the
information for these capabilities.

#### ConnectApi.PlatformAction

A platform action instance with state information for the context user.

**Property Name** **Type** **Description** **Available Version**

`actionUrl` String For action links of `subtype Ui` or `Download`, 33.0
direct the user to download or visit the UI from this

link. Salesforce issues a Javascript redirect for the link
in this format:

```
                        /action-link-redirect/ communityId
```

`/` _**`actionLinkId`**_ `?_bearer=` _**`bearerToken`**_ .

For `Api` action links and for all platform actions, this
value is `null` and Salesforce handles the call.

`apiName` String The API name. The value may be `null` . 33.0

`confirmation` String If this action requires a confirmation and has a status 33.0
`Message` of `NewStatus`, this is a default localized message
that should be shown to an end user prior to invoking
the action. Otherwise, this is `null` .

`executingUser` `ConnectApi.UserSummary` The user who initiated execution of this platform 33.0
action.

`groupDefault` Boolean `true` if this platform action is the default or primary 33.0
platform action in the platform action group; `false`

otherwise. There can be only one default platform
action per platform action group.

`iconUrl` String The URL of the icon for the platform action. This value 33.0
may be `null` .

`id` String

The ID for the platform action. 33.0

If the `type` is `QuickAction` and the `subtype`
is `Create`, this value is `null` .

`label` String The localized label for this platform action. 33.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`modifiedDate` Datetime ISO 8601 format date string, for example, 33.0
2011-02-25T18:24:31.000Z.

`platformAction` `ConnectApi.Reference` A reference to the platform action group containing 33.0
`Group` this platform action.

```
status

```

`ConnectApi.` The execution status of the platform action. Values 33.0
`PlatformAction` are:

```
Status
```

**•** `FailedStatus` —The action link execution
failed.

**•** `NewStatus` —The action link is ready to be
executed. Available for `Download` and `Ui`
action links only.

**•** `PendingStatus` —The action link is
executing. Choosing this value triggers the API
call for `Api` and `ApiAsync` action links.

**•** `SuccessfulStatus` —The action link
executed successfully.

`subtype` String

The subtype of a platform action or `null` . 33.0

If the `type` property is `ActionLink`, possible
values are:

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

[Link resource in the Connect REST API](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)
[Developer Guidefor more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/)

#### type ConnectApi. The type of platform action. Values are: 33.0

```
             PlatformActionType
```

**•** `ActionLink` —An indicator on a feed element
that targets an API, a web page, or a file,
represented by a button in the Salesforce UI.

**•** `CustomButton` —When clicked, opens a URL
or a Visualforce page in a window or executes
JavaScript.

**•** `ProductivityAction` —Productivity
actions are predefined and attached to a limited
set of objects. Productivity actions include Send
Email, Call, Map, View Website, and Read News.
Except for the Call action, you can’t edit
productivity actions.

**•** `QuickAction` —A global or object-specific
action.

**•** `StandardButton` —A predefined Salesforce
button such as New, Edit, or Delete.

`url` String

SEE ALSO:

#### ConnectApi.PlatformActionGroup ConnectApi.PlatformActionGroup

The URL for this platform action. 33.0

If the `type` is `QuickAction` and the `subtype`
is `Create`, this value is `null` .

A platform action group instance with state appropriate for the context user.

#### Action link groups are one type of platform action group and are therefore represented as ConnectApi.PlatformActionGroup

output classes.

**Property Name** **Type** **Description** **Available Version**

```
category

```

#### ConnectApi. Indicates the priority and relative locations of platform 33.0

`PlatformAction` actions. Values are:

```
GroupCategory
```

**•** `Primary` —The action link group is displayed
in the body of the feed element.

**•** `Overflow` —The action link group is displayed
in the overflow menu of the feed element.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`id` String

The 18-character ID or an opaque string ID of the 33.0
platform action group.

If the `ConnectApi.PlatformAction type`
is `QuickAction` and the `subtype` is `Create`,
this value is `null` .

`modifiedDate` Datetime ISO 8601 date string, for example, 33.0
2014-02-25T18:24:31.000Z.

#### platformActions List< ConnectApi.

`PlatformAction`          

`url` String

SEE ALSO:

ConnectApi.AbstractRecommendation

ConnectApi.AssociatedActionsCapability

#### ConnectApi.PollCapability

If a feed element has this capability, it includes a poll.

Subclass of ConnectApi.FeedElementCapability.

The platform action instances for this group. 33.0

Within an action link group, action links are displayed
in the order listed in the `actionLinks` property

of the `ConnectApi.ActionLinkGroup`
`DefinitionInput` class. Within a feed item,
action link groups are displayed in the order specified
in the `actionLinkGroupIds` property of the

```
ConnectApi.AssociatedActions
```

`CapabilityInput` class.

The URL for this platform action group. 33.0

If the `ConnectApi.PlatformAction type`
is `QuickAction` and the `subtype` is `Create`,
this value is `null` .

**Property Name** **Type** **Description** **Available Version**

#### choices List< ConnectApi. Collection of poll choices that make up the poll. 32.0

`FeedPollChoice`         

`myChoiceId` String

18-character ID of the poll choice that the context 32.0
user has voted for in this poll. Returns `null` if the
context user has not voted.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`totalVoteCount` Integer Total number of votes cast on the feed poll element. 32.0

SEE ALSO:

ConnectApi.FeedElementCapabilities

#### ConnectApi.PostAuthGatewayResponse

Gateway response after confirmation that the merchant is ready to capture payment of an existing pre-authorized transaction.

Sublass of ConnectApi.AbstractGatewayResponse.

**Property Name** **Type** **Description** **Available Version**

`gateway` String Code used to authorize the payment that the 54.0
`AuthorizationCode` payment gateway is processing.

#### paymentMethod ConnectApi. Details about the payment method. 54.0

`Details` PaymentMethodDetails

#### ConnectApi.PostAuthorizationResponse

Gateway response following a post authorization request.

**Property Name** **Type** **Description** **Available Version**

#### `error ConnectApi.`

```
          ErrorResponse

```

Information about errors that occurred in the 54.0
payment gateway while evaluating the post
authorization request.

```
gatewayResponse

paymentAuthorization

```

#### ConnectApi. Payment gateway's response to the post 54.0

`PostAuth` authorization request.

```
GatewayResponse

#### ConnectApi. Payment gateway's response to the original payment 54.0
```

`Payment` authorization request.

```
AuthorizationResponse

```

#### paymentGateway List< ConnectApi. Stores information exchanged between the 54.0

`Logs` `GatewayLog` Salesforce payments platform and external payment

`Response`         - gateways. Gateway logs can also record payloads

from external payment entities.

```
paymentGroup

paymentMethod

```

#### `ConnectApi.`

```
PaymentGroup

Response

```

#### ConnectApi. Payment method used in the post authorization 54.0

`PaymentMethod` request.

```
Response

```


Payment group, consisting of one or more payments, 54.0
sent to the gateway for the post authorization
request.

Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### savedPayment ConnectApi. Saved payment method status. Valid values are: 61.0

```
   MethodStatus PostAuthSPMStatus
```

**•** `AlreadyExists`

**•** `Created`

**•** `Updated`

#### ConnectApi.PreserveCart

Represents a preserved cart.

**Property Name** **Type** **Description** **Available Version**

`cartId` String ID of the authenticated cart. 60.0

`currencyIsoCode` String Currency ISO code for the authenticated cart. 60.0

`failedCartItems` List< `ConnectApi.CartItem` List of products that weren’t successfully transferred 60.0
`BasicResult`            - from the guest cart to the authenticated cart.

`numberOfProducts` Integer Total number of products in the guest cart. 60.0

`numberOfProductsWithError` Integer

Total number of products that weren’t successfully 60.0
transferred from the guest cart to the authenticated
cart.

`numberOfProductsWithSuccess` Integer Total number of products successfully transferred 60.0
from the guest cart to the authenticated cart.

`succeededCartItems` List< `ConnectApi.CartItem` List of products successfully transferred from the 60.0
`BasicResult`          - guest cart to the authenticated cart.

#### ConnectApi.PreviewCancelOutputRepresentation

Expected financial values for a proposed cancel action.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. Expected financial values for the proposed cancel 48.0

`ChangeItem` action.

```
OutputRepresentation

```

`orderSummaryId` String ID of the OrderSummary. 48.0

#### ConnectApi.PreviewCartToExchangeOrderOutputRepresentation

Expected change order financial values for the preview cart to exchange order action.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`balanceStateExchangeWebCart` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the exchange web cart. Big, 61.0

```
              on page 2182

```

`balanceStateOriginalOrderSummary` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the original order Big, 61.0
`on page 2182` summary.

`balanceStateReturnOrder` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the return order. Big, 61.0

```
              on page 2182

```

`changeBalances` `ConnectApi.ChangeItemOutputRepresentation` Change order financial values for a preview order Big, 60.0
`on page 2234` action.

#### errors List< ConnectApi. Any errors that were returned. Big, 60.0

`ErrorResponse`            

`orderSummaryId` String ID of the order summary. Big, 60.0

`success` Boolean Indicates whether the transaction was successful. Big, 60.0

#### ConnectApi.PreviewReturnOutputRepresentation

Expected financial values for a proposed return action.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
changeBalances

```

#### ConnectApi. Expected financial values for the proposed return 48.0

`ChangeItem` action.

```
OutputRepresentation

```

`orderSummaryId` String ID of the OrderSummary. 48.0

#### ConnectApi.PriceAdjustmentSchedule

Price adjustment schedule.

**Property Name** **Type** **Description** **Available Version**

`adjustmentMethod` Reserved for future use. 59.0

`id` String ID of the price adjustment schedule. 49.0

```
priceAdjustment

Tiers

```

#### List< ConnectApi. List of price adjustment tiers. 49.0

```
PriceAdjustment
```

`Tier` 


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`scheduleType` Reserved for future use. 59.0

SEE ALSO:

ConnectApi.ProductPrice

#### ConnectApi.PriceAdjustmentTier

Price adjustment tier.

**Property Name** **Type** **Description** **Available Version**

```
adjustmentType

```

#### ConnectApi. Type of price adjustment for the tier. Values are: 49.0

```
PriceAdjustment
```

**•** `AmountBasedAdjustment` —Price is

`TierType` adjusted by a specified amount.

**•** `PercentageBasedAdjustment` —Price
is adjusted by a specified percentage.

`adjustmentValue` String Adjustment value of the tier. 49.0

`id` String ID of the price adjustment tier. 49.0

`lowerBound` String Lower limit of the tier. 49.0

`tierUnitPrice` String Unit price of the tier. 49.0

`upperBound` String Upper limit of the tier. 49.0

SEE ALSO:

ConnectApi.PriceAdjustmentSchedule

#### ConnectApi.PricingResult

Product pricing result.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 49.0
the product.

#### error ConnectApi. Error code and message. 49.0

```
           ErrorResponse

#### pricingLine List< ConnectApi. Pricing result line Items. 49.0
```

`ItemResults` `PricingResultLineItem` 

`success` Boolean Specifies whether the execution was successful 49.0
( `true` ) or not ( `false` ).


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.PricingResultLineItem

Pricing result line item.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error code and message. 49.0

```
             ErrorResponse

```

`listPrice` String List price for the product. 49.0

`lowestUnitPrice` String Lowest unit price for the product. 49.0

`pricebookEntryId` String ID of the pricebook entry. 49.0

`productId` String ID of the product to price. 49.0

`success` Boolean Specifies whether the execution was successful 49.0
( `true` ) or not ( `false` ).

`unitPrice` String Unit price for the product. 49.0

SEE ALSO:

#### ConnectApi.PricingResult

ConnectApi.ProductSummary

#### ConnectApi.ProductAttributeInfo

Product attribute information.

**Property Name** **Type** **Description** **Available Version**

`allowableValues` List<String>

Active attribute picklist values that can be used to 50.0
create variations. These values are determined by the
order of the picklist values in Object Manager.

`apiName` String API name of the attribute. 50.0

`availableValues` List<String> Attribute picklist values that are available for the 50.0
product in the store. These values are sorted by the

order of values in the `allowableValues`
property.

`fieldEnumOrId` String Field ID for custom fields or enumeration value for 50.0
standard fields.

`isGroupedBy` Boolean Indicates if product variations are grouped by a 64.0
specific attribute.

`label` String Label of the attribute. 50.0

`objectName` String Name of the object that contains the field. 50.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### options List< ConnectApi. List of product attribute value metadata. 63.0

```
             ProductAttribute

             ValueMetadata
```

`Representation`            

`sequence` Integer

Sequence value determined by the order of the 50.0
attributes under Commerce Setup for the attribute
set.

#### viewType ConnectApi. View type for product attributes. Values are: 63.0

```
          ProductAttributeViewType
```

**•** `ColorSwatch`

**•** `Dropdown`

**•** `Pill`

SEE ALSO:

ConnectApi.ProductDetail

#### ConnectApi.ProductAttributeSetInfo

ConnectApi.ProductVariationInfo

#### ConnectApi.ProductAttributeSelectionInfo

Product attribute.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the attribute. 50.0

`label` String Label of the attribute. 50.0

`sequence` Integer

Sequence value determined by the order of the 50.0
attributes under Commerce Setup for the attribute
set.

`value` String Display value of the attribute. 50.0

SEE ALSO:

ConnectApi.ProductAttributesToProductEntry

#### ConnectApi.ProductAttributeSet

Product attribute set data.

**Property Name** **Type** **Description** **Available Version**

`attributes` Map<String, String> Map of the attributes that are members of the 50.0
attribute set.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`developerName` String Name of the attribute set. 50.0

`id` String ID of the product attribute record that represents the 50.0
product attribute set.

#### ConnectApi.ProductAttributeSetInfo

Attribute set metadata.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**Property Name** **Type** **Description** **Available Version**

```
attributeInfo

```

Map<String, Map of the API name of the attribute field to the 50.0
#### ConnectApi. attribute metadata.

`ProductAttributeInfo` 

`description` String Description of the attribute set. 50.0

`developerName` String Developer name of the attribute set. 50.0

`id` String ID of the attribute set. 50.0

`masterLabel` String Label of the attribute set. 50.0

`sequence` Integer Sequence of the attribute set for the product. 50.0

SEE ALSO:

ConnectApi.ProductDetail

#### ConnectApi.ProductAttributeSetSummary

Summary of a product attribute set.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the attribute set. 51.0

```
attributes

```

#### List< ConnectApi. List of attributes in the attribute set. 51.0

```
ProductAttribute
```

`Summary` 

`label` String Display label of the attribute set. 51.0

SEE ALSO:

ConnectApi.OrderItemSummaryProduct

ConnectApi.ProductSummary


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ProductAttributeSummary

Summary of a product attribute.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the attribute. 51.0

`label` String Display label of the attribute. 51.0

`sequence` Integer Sequence of the attribute in the attribute set. 51.0

`value` String Display value of the attribute. 51.0

SEE ALSO:

ConnectApi.ProductAttributeSetSummary

#### ConnectApi.ProductAttributesToProductEntry

Mapping of an attribute value combination to a variation product ID.

**Property Name** **Type** **Description** **Available Version**

`canonicalKey` String

Attribute API values concatenated with an underscore 50.0
(_) based on the sequence number of the attributes
in the attribute set.

`productId` String Variation product ID for the selection of attributes. 50.0

```
selectedAttributes

```

#### List< ConnectApi. Ordered list of attribute values and metadata that 50.0

`ProductAttribute` can be used to form a key that maps to product ID.
`SelectionInfo` 

`urlName` String Variant URL name for the selection of attributes. 59.0

SEE ALSO:

ConnectApi.ProductVariationInfo

#### ConnectApi.ProductAttributeValueMetadataRepresentation

Metadata for a product attribute value.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API Name of the product attribute picklist value. For 63.0
example, `blue__c` .

`colorHexCode` String Hex code value of a color attribute. For example, 63.0
`#0000FF` .


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`label` String Label of the picklist value for a custom field product 63.0
attribute. For example, `Red` .

`variantAvailable` Boolean Specifies whether a variation product exists ( `true` ) 63.0
or not ( `false` ).

#### ConnectApi.ProductBundleChildOutput

Output representation of a product details bundle child.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the child product. 64.0

`name` String Child product name. 64.0

`productId` String ProductId of the child product. 64.0

`quantity` Double Quantity of the child product per bundle. 64.0

`stockKeepingUnit` String Stock Keeping Unit (SKU) of the child product. 64.0

#### ConnectApi.ProductCartItem

Cart items of a specific product type.

**Property Name** **Type** **Description** **Available Version**

```
cartItems

product

```

#### List< ConnectApi. Items in a cart. 60.0

`CartItemResult` on
page 2206>

#### ConnectApi. Product summary for a cart item. 60.0

```
CartItemProduct

on page 2205

```

#### ConnectApi.ProductCartItemCollection

Items in the cart, grouped by product type.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Number of cart items returned on the current page 60.0

`currentPage` Integer Current page of cart items. The value matches the 60.0
requested page number, unless the requested page

number exceeds the total number of pages. In this
scenario, the current page is the highest available
page number.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`hasErrors` Boolean Indicates whether at least one of the results contains 60.0
an error ( `True` ) or not ( `False` ).

```
products

```

#### List< ConnectApi. Products in the cart. 60.0

```
ProductCartItem
```

on page 2463>

`totalItemCount` Integer Total number of unique products in the cart. 60.0

`totalNumberOfPages` Integer Total number of pages for the given page size. 60.0

#### ConnectApi.ProductCategoryData

Product category.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the category. 49.0

`id` String ID of the category. 49.0

`name` String Name of the category. 49.0

`urlSlug` String SEO-friendly URL slug of the category. 59.0

SEE ALSO:

ConnectApi.ProductCategoryPath

ConnectApi.SearchCategory

#### ConnectApi.ProductCategoryDetail

Details of a product category.

**Property Name** **Type** **Description** **Available Version**

#### bannerImage ConnectApi. Banner image of the product category. 49.0

```
           ProductCategoryMedia

```

`fields` Map<String, String> List of fields for the product category. 49.0

`id` String ID of the product category. 49.0

```
mediaGroups

```

#### List< ConnectApi. List of media groups of the product category. 49.0

```
ProductCategory
```

`MediaGroup` 

#### tileImage ConnectApi. Tile image of the product category. 49.0

```
          ProductCategoryMedia

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`urlName` String SEO-friendly URL name of the product category. 59.0

SEE ALSO:

#### ConnectApi.ProductCategoryDetailCollection ConnectApi.ProductCategoryDetailCollection

Collection of product category details.

**Property Name** **Type** **Description** **Available Version**

```
productCategories

```

#### List< ConnectApi. List of product category details. 52.0

```
ProductCategory
```

`Detail` 

#### ConnectApi.ProductCategoryMedia

Media associated with a product category.

**Property Name** **Type** **Description** **Available Version**

`alternateText` String Alternative text for the product category media. 49.0

`contentVersionId` String ID of the latest published content version if the media 49.0
is stored as a ContentDocument. If the image is a

customer-provided external URL, the value is `null` .
Not supported in enhanced CMS workspaces.

`id` String ID of the product category image. 49.0

#### mediaType ConnectApi. Type of product media. Values are: 49.0

```
           ProductMediaType
```

**•** `Document`

**•** `Image`

**•** `Video`

`sortOrder` Integer Sort order of a media item inside a media group. 49.0

`thumbnailUrl` String URL of the thumbnail for product media. If a value 49.0
exists, it should be used for the thumbnail whether

the image is natively uploaded or hosted externally.
Not supported in enhanced CMS workspaces.

`title` String Title of the product category media. 49.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`url` String URL of the product category media. 49.0

SEE ALSO:

#### ConnectApi.ProductCategoryMediaGroup

ConnectApi.ProductCategoryDetail

#### ConnectApi.ProductCategoryMediaGroup

Media group associated with a product category.

**Property Name** **Type** **Description** **Available Version**

`developerName` String API name of the product category media group. 49.0

`id` String ID of the product category media group. 49.0

#### mediaItems List< ConnectApi. List of media items within a product category media 49.0

`ProductCategoryMedia`                - group.

`name` String Name of the product category media group. 49.0

```
usageType

```

#### ConnectApi. Usage type of a product media item within a media 49.0

`ProductMedia` group. Values are:

```
UsageType
```

**•** `Attachment` —Product media group with
product documents as attachments.

**•** `Banner` —Product category media group with
banner images of the product.

**•** `Listing` —Product media group with listing
images of the product.

**•** `Standard` —Product media group with
standard images and videos of the product.

**•** `Tile` —Product category media group with tile
images of the product.

#### ConnectApi.ProductCategoryPath

List of product categories in a path.

**Property Name** **Type** **Description** **Available Version**

#### path List< ConnectApi. List of product categories in a path. 49.0

`ProductCategoryData`            

SEE ALSO:

ConnectApi.ProductDetail


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ProductChild

Child product related to a parent product.

**Property Name** **Type** **Description** **Available Version**

`defaultQuantity` String Default quantity of child products to be ordered. 57.0

`isEntitled` Boolean Specifies whether the child product can be viewed 62.0
on the product detail page ( `true` ) or not ( `false` ).

#### productInfo ConnectApi. Product details of the child product. 57.0

```
             ProductDetail

#### ConnectApi.ProductChildCollection

```

Collection of child products related to a parent product.

**Property Name** **Type** **Description** **Available Version**

`count` Integer Number of child products returned on this page. 57.0

`currentPageToken` String Current page token, if any. 57.0

`currentPageUrl` String URL of the current page in the response. 57.0

#### items List< ConnectApi. List of child products related to the parent product. 57.0

`ProductChild`            - The child products are sorted by their configured

sequence values, in ascending order, with null values
sorted last. If there are no configured sequence
values, the child products are sorted by
`createdDate`, in ascending order.

`nextPageToken` String

Token for the next page, if any. A value is included in 57.0
the response only if a value is returned for
`nextPageUrl` .

`nextPageUrl` String URL of the next page, if any. 57.0

`previousPageToken` String

Token for the previous page, if any. A value is 57.0
included in the response only if a value is returned
for `previousPageUrl` .

`previousPageUrl` String URL of the previous page, if any. 57.0

#### productClass ConnectApi. Class of product. Values are: 62.0

```
          ProductClass
```

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`total` Integer Total number of child products in the collection. 57.0

#### ConnectApi.ProductDeliverEstimationOutputRepresentation

Delivery estimation information for each product.

**Property Name** **Type** **Description** **Available Version**

`estimatedDeliveryDate` DatetimeConnectApi.EstimateDeliveryDateOutputRepresentation Estimated delivery date. 63.0
on page 2299

`estimatedShipDate` Datetime Estimated shipping date. 63.0

`quantity` Double Product quantity. 63.0

`routingCalculationType` String Routing calculation type. 63.0

`stockKeepingUnit` String Product stock keeping unit (SKU). 63.0

#### ConnectApi.ProductDetail

Details of a product.

**Property Name** **Type** **Description** **Available Version**

```
attributeSetInfo

```

Map<String, Map of the attribute set developer name to its 50.0
#### ConnectApi. metadata.

```
ProductAttribute
```

`SetInfo` 

#### defaultImage ConnectApi. Default image of the product. 49.0

```
          ProductMedia

```

#### `entitlement ConnectApi.`

```
          ProductEntitlement

```

Entitlement details for the product. 49.0–56.0

To get pricing information for products in version 57
and later, use the CommerceStorePricing Class.

`fields` Map<String, String> List of fields for the product. 49.0

`id` String ID of the product. 49.0

#### mediaGroups List< ConnectApi. List of media groups of the product. 49.0

`ProductMediaGroup`          
#### primaryProduct ConnectApi. Primary category path of the product. 49.0

```
CategoryPath ProductCategoryPath

#### productClass ConnectApi. Class of product. Values are: 50.0

          ProductClass
```

**•** `Bundle`

**•** `Set`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

```
productSelling

Models

purchaseQuantity

Rule

```

#### List< ConnectApi. List of product selling models for the product. 56.0

```
ProductSelling
```

`Model` 
#### ConnectApi. If one exists, purchase quantity rule for the product. 52.0

```
PurchaseQuantity

Rule

```

`urlName` String SEO-friendly URL name for the product. 59.0

#### variationAttribute ConnectApi. Variation attribute set for the product. 50.0

```
Set ProductAttributeSet

```

#### `variationInfo ConnectApi.`

```
          ProductVariationInfo

```

Available and allowable values for variation attributes 50.0
and a map to resolve variation product IDs from
attribute value combinations.

`variationParentId` String ID of the variation parent. 50.0

#### ConnectApi.ProductDetailsOutputRepresentation

Details about a product.

Subclass of ConnectApi.BaseOutputRepresentation.

**Property Name** **Type** **Description** **Available Version**

```
attributes

```

List< `ConnectApi.ProductVariation` List of variation attributes that define variations of 55.0
`AttributeOutput` the product.
`Representation` 

`currencyIsoCode` String Currency ISO code. 55.0

For bundle products only: an array of the individual 64.0
products that are a part of the bundle. Only applicable
for B2B or D2C stores. />

```
childItems

```

List< `ConnectApi.ProductBundleChild`

```
AttributeOutput
```

`Representation` 

`description` String Description of the product. 55.0

`fields` Map<String, String> List of the product’s fields. 55.0

#### imageGroups List< ConnectApi. List of the product’s image groups. 55.0

```
          ProductImage

          GroupOutput
```

`Representation`         

`listPrice` Double List price. 55.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`name` String Name. 55.0

`productClass` String The product’s class. Possible values are: Bundle, 64.0
Simple, Variation, Variation Parent, or Set.

`productQuantityRule` Purchase Quantity Rule If one exists, purchase quantity rule for the product. 55.0

`productId` String Product ID. 55.0

`stockKeepingUnit` String Stock keeping unit. 55.0

`totalChildrenCount` Enum For bundles only: the total number of child products 64.0
in a bundle. Only applicable for B2B or D2C stores./>

`unitPrice` Double Unit price. 55.0

#### variants List< ConnectApi. List of variations of the product. 55.0

```
             ProductVariant

             Output
```

`Representation`            
#### ConnectApi.ProductEntitlement

Entitlements for a product.

**Property Name** **Type** **Description** **Available Version**

`canViewPrice` Boolean Specifies whether the product's price can be viewed 49.0
( `true` ) or not ( `false` ).

SEE ALSO:

ConnectApi.ProductDetail

#### ConnectApi.ProductExpandOutputRepresentation

Product expand information with return reasons.

**Property Name** **Type** **Description** **Available Version**

`returnReasons` List< `String`   - Return reasons for products. 59.0

#### ConnectApi.ProductImageGroupOutputRepresentation

Details about a product image group.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
images

```

#### List< ConnectApi. List of product images in the group. 55.0

```
ProductImage
```

`OutputRepresentation` 

`viewType` String The type of product images in the group. 55.0

#### ConnectApi.ProductImageOutputRepresentation

Details about a product image.

**Property Name** **Type** **Description** **Available Version**

`alternateText` String Alternate text for accessibility. 55.0

`mediaType` String Media type. 55.0

`thumbnailUrl` String URL of the thumbnail version of the product image. 55.0

`title` String Title. 55.0

`url` String URL of the product image. 55.0

#### ConnectApi.ProductsListOutputRepresentation

Output representation of products with product data along with expand details.

**Property Name** **Type** **Description** **Available Version**

`product` ListConnectApi.ProductOutputRepresentation<> The product’s identifier. **59.0**

#### ConnectApi.ProductMedia

Media associated with a product.

**Property Name** **Type** **Description** **Available Version**

`alternateText` String Alternative text for the product media. 49.0

`contentVersionId` String ID of the latest published content version if the media 49.0
is stored as a ContentDocument. If the image is a

customer-provided external URL, the value is `null` .
Not supported in enhanced CMS workspaces.

`id` String ID of the product image. 49.0

#### mediaType ConnectApi. Type of product media. Values are: 49.0

```
           ProductMediaType
```

**•** `Document`

**•** `Image`

**•** `Video`


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`sortOrder` Integer Sort order of a media item within a media group. 49.0

`thumbnailUrl` String URL of the thumbnail for product media. If a value 49.0
exists, it should be used for the thumbnail whether

the image is natively uploaded or hosted externally.
Not supported in enhanced CMS workspaces.

`title` String Title of the product media. 49.0

`url` String URL of the product media. 49.0

SEE ALSO:

ConnectApi.CartItemProduct

ConnectApi.ProductDetail

#### ConnectApi.ProductMediaGroup

ConnectApi.OrderItemSummaryProduct

ConnectApi.ProductSummary

#### ConnectApi.ProductMediaGroup

Media group associated with a product.

**Property Name** **Type** **Description** **Available Version**

`developerName` String API name of the product media group. 49.0

`id` String ID of the product media group. 49.0

#### mediaItems List< ConnectApi. List of media items within a product media group. 49.0

`ProductMedia`            

`name` String Name of the product media group. 49.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
usageType

```

SEE ALSO:

#### ConnectApi. Usage type of a product media item within a media 49.0

`ProductMedia` group. Values are:

```
UsageType
```

**•** `Attachment` —Product media group with
product documents as attachments.

**•** `Banner` —Product category media group with
banner images of the product.

**•** `Listing` —Product media group with listing
images of the product.

**•** `Standard` —Product media group with
standard images and videos of the product.

**•** `Tile` —Product category media group with tile
images of the product.

ConnectApi.ProductDetail

ConnectApi.ProductCategoryDetail

#### ConnectApi.ProductOutputRepresentation

Output representation for product data.

**Property Name** **Type** **Description** **Available Version**

`expand` `ConnectApi.ProductExpandOutputRepresentation` Output representation for expand feature. **59.0**

`products` String Product data. **59.0**

#### ConnectApi.ProductOverview

Overview of a product, with summary information about prices, selected fields, and the product’s default image.

**Property Name** **Type** **Description** **Available Version**

#### defaultImage ConnectApi. Media representation of the product's default image. 54.0

```
           ProductMedia

#### error ConnectApi. Error code and error message. 54.0

           ErrorResponse

```

`fields` Map<String, String> Map of fields belonging to the product. 54.0

`id` String ID of the product. 54.0

```
prices

```

#### `ConnectApi.`

```
PricingResult

LineItem

```

Price of the product. 54.0–57.0

To get pricing information for products in version 58
and later, use the CommerceStorePricing Class.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`sku` String SKU of the product. 54.0

`success` Boolean

Represents whether execution was successful and 54.0
product overview information was retrieved without
error.

#### ConnectApi.ProductOverviewCollection

Collection of product overviews.

**Property Name** **Type** **Description** **Available Version**

#### products List< ConnectApi. Collection of product overview. 54.0

`ProductOverview`          

`total` Integer Total number of products returned. 54.0

#### ConnectApi.ProductPrice

Pricing information for a product.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String

Three-letter ISO 4217 currency code associated with 49.0
the product.

Products are priced using the currency for the buyer
account or guest buyer profile. If your store doesn’t

support the currency for the buyer account or guest
buyer profile, products are priced using the default
currency for your store.

`listPrice` String List price for the product. 49.0

`lowestUnitPrice` String Lowest unit price for the product. 49.0

```
priceAdjustment

```

#### `ConnectApi.`

```
PriceAdjustment

Schedule

```

Price adjustment schedule for the product. If a 49.0
product selling model ID is specified in a request
parameter, this property is empty.

ID of the price book entry. If a product selling model 49.0
ID is specified in a request parameter, this property
is empty.

`pricebookEntryId` String

#### productPriceEntries List< ConnectApi.ProductPriceEntry > List of line item prices for the product. 56.0

`unitPrice` String

Unit price for the product. If a product selling model 49.0
ID is specified in a request parameter, this property
is empty.


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ProductPriceEntry

Line item price for the product.

**Property Name** **Type** **Description** **Available Version**

#### error ConnectApi. Error code and error message. 56.0

```
             ErrorResponse

```

`listPrice` String List price for the product entry. 56.0

```
priceAdjustment

```

#### ConnectApi. Price adjustment schedule. 56.0

```
PriceAdjustment

Schedule

```

`pricebookEntryId` String ID of the pricebook entry. 56.0

`productSelling` String

```
ModelId

```

ID of the product selling model. If no product selling 56.0
model ID is specified in a request parameter, this
property is empty.

`success` Boolean Specifies whether execution was successful ( `true` ) 56.0
or not ( `false` ).

`unitPrice` String Unit price for the product entry. 56.0

#### ConnectApi.ProductReturnRateListOutputRepresentation

Products with corresponding return rates.

**Property Name** **Type** **Description** **Available Version**

#### productReturnRateList <List ConnectApi.ProductReturnRateOutputRepresentation > List of product return rates. 59.0 ConnectApi.ProductReturnRateOutputRepresentation

Return rate of a product (units returned divided by units sold).

**Property Name** **Type** **Description** **Available Version**

`productId` String ID of the product. 59.0

`returnRate` Double Return rate of specified product. Values range from 59.0
0 to 1.

#### ConnectApi.ProductSearchFacetOutputRepresentation

Product search facet value.

**Property Name** **Type** **Description** **Available Version**

`attributeType` String Attribute type of the facet value. 59.0


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`displayName` String Display name of the facet value. 59.0

`displayRank` Integer Display rank of the facet value. 59.0

`displayType` String Display type of the facet value. 59.0

`facetType` String Type of the facet. 59.0

`nameOrId` String Name or ID of the facet. 59.0

#### values <List ConnectApi.ProductSearchFacetValueOutputRepresentation > A list of facet values for the search. 59.0 ConnectApi.ProductSearchFacetValueOutputRepresentation

Output representation of a product search facet value.

**Property Name** **Type** **Description** **Available Version**

`displayName` String Display name of the search facet. 59.0

`nameOrId` String Unique name or ID of the search facet. 59.0

`productCount` Integer Number of products found with the search facet. 59.0

`type` String Type of the search facet. 59.0

#### ConnectApi.ProductSearchImageOutputRepresentation

Output representation of the product search image.

**Property Name** **Type** **Description** **Available Version**

`alternateText` String Alternate text for the product image. 59.0

`mediaType` String Media type of the product image. 59.0

`sortOrder` Integer Sort order of the product image. 59.0

`title` String Title of the product image. 59.0

`url` String URL of the product image. 59.0

#### ConnectApi.ProductSearchOutputRepresentation

Output representation of the product search response

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 59.0
the product.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`facets` <List `ConnectApi.ProductSearchFacetOutputRepresentation`   - A list of facet names to filter the search.For example, 59.0

`["size_medium", "color_red"]` .

`locale` String Locale used for the product search. 59.0

`pageNumber` Integer Maximum number of search results pages to return. 59.0
If you don't specify a value, the default is 1.

`pageSize` Integer

Number of items per page. Valid values are from 1 59.0
through 100. If you don’t specify a value, the default
size is 20.

#### products <List ConnectApi.ProductSearchProductOutputRepresentation > List of products found by the search. 59.0

`totalRecordsFound` Integer Total products found. 59.0

#### ConnectApi.ProductSearchProductOutputRepresentation

Product found by a product search.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the product. 59.0

`image` `ConnectApi.ProductSearchImageOutputRepresentation` Image of the product. 59.0

`name` String Name of the product. 59.0

`productClass` String Class of the product. 59.0

`stockKeepingUnit` String Stock Keeping Unit (SKU) of the product. 59.0

`variationAttributeSet` <List `ConnectApi.ProductVariationAttributeOutputRepresentation` - Variation attribute set of the product. 59.0

#### ConnectApi.ProductSearchResults

Product search results.

**Property Name** **Type** **Description** **Available Version**

#### categories ConnectApi. Categories from the search results. 52.0

```
           SearchCategory

```

`correlationId` String Reserved for future use. 55.0

#### facets List< ConnectApi. Facets from the search results. 52.0

`SearchFacet`          

`locale` String Locale of the search results. 52.0

#### productsPage ConnectApi. Page of products from the search results. 52.0

```
           ProductSummaryPage

```


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ProductSearchSuggestionsResults

Product search suggestions results.

**Property Name** **Type** **Description** **Available Version**

#### recentSearch List< ConnectApi. Suggestions based on the user’s recent searches. 52.0

`Suggestions` `SearchSuggestion`   
#### ConnectApi.ProductSellingModel

Product selling model for Commerce subscriptions.

**Property Name** **Type** **Description** **Available Version**

`description` String Description of the product selling model displayed 60.0
on the UI.

`displayName` String Name of the product selling model displayed on the 60.0
UI.

`id` String ID of the product selling model. 56.0

`name` String Name of the product selling model. 56.0

`pricingTerm` Integer Number of pricing term units in the pricing term. 56.0
Used with `pricingTermUnit` to define the

length of the pricing term. For example, if
`pricingTermUnit` is `Months` and this
property is 1, the subscription is priced monthly.
However, if the `sellingModelType` property
is set to `OneTime`, the `pricingTerm` property
is empty, because the product isn’t sold as a
subscription. The only allowed value for this property
is 1.

#### pricingTermUnit ConnectApi. Unit of time used to define a pricing term. Value is: 56.0

```
             PricingTermUnit
```

**•** `Months` —Product is priced on a monthly basis.

**•** `Annual` —Product is priced on an annual basis.

This unit of time is combined with a number
(specified by the `pricingTerm` property) to
define the full term of the subscription. For example,
if the unit of time is `Months` and the
`pricingTerm` property is set to 1, the
subscription is priced monthly. However, if the
`sellingModelType` property is set to
`OneTime`, the `pricingTermUnit` property is
empty, because the product isn’t sold as a
subscription.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### sellingModelType ConnectApi. Type of product selling model. Values are: 56.0

```
             SellingModelType
```

**•** `Evergreen` —A subscription without an end
date. An evergreen subscription continues until
the shopper affirmatively cancels it.

**•** `OneTime` —A product that isn’t sold as a
subscription.

**•** `TermDefined` —A subscription with a defined
end date. The subscription continues for a
specified time period. When the term ends, the
subscription ends.

```
subscriptionTermRule

```

#### ConnectApi. Rules for the subscription term. 59.0

```
Subscription

TermRule

```

#### ConnectApi.ProductSummary

Product summary.

**Property Name** **Type** **Description** **Available Version**

#### defaultImage ConnectApi. Default image of the product. 52.0

```
           ProductMedia

```

```
fields

```

Map<String, Map of fields belonging to the product. 52.0

#### `ConnectApi.`

`FieldValue` 

`id` String ID of the product. 52.0

`name` String Name of the product. 52.0

```
prices

```

#### ConnectApi. Prices of the product. 52.0

```
PricingResult

LineItem

```

#### productClass ConnectApi. Class of product. Values are: 52.0

```
          ProductClass
```

**•** `Bundle`

```
productSelling

ModelInformation

```

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

#### ConnectApi. Product selling model information. 59.0

```
CommerceProduct

SellingModel

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

```
purchaseQuantityRule

```

#### ConnectApi. If one exists, purchase quantity rule for the product. 52.0

```
PurchaseQuantity

Rule

```

`urlName` String SEO-friendly URL name for the product. 59.0

```
variationAttributeSet

```

SEE ALSO:

#### ConnectApi. Variation attribute set that’s associated with the 52.0

`ProductAttribute` product.

```
SetSummary

```

#### ConnectApi.ProductSummaryPage ConnectApi.ProductSummaryPage

Page of product summaries.

**Property Name** **Type** **Description** **Available Version**

`currencyIsoCode` String Three-letter ISO 4217 currency code associated with 52.0
the product.

`pageSize` Integer Number of products per page in the search results. 52.0

#### products List< ConnectApi. Collection of product summaries. 52.0

`ProductSummary`          

`total` Long Total number of products in the search results. 52.0

SEE ALSO:

ConnectApi.ProductSearchResults

#### ConnectApi.ProductVariantOutputRepresentation

Details about a product variation.

**Property Name** **Type** **Description** **Available Version**

`listPrice` Double List price. 55.0

`price` Double Price. 55.0

`productId` String Product ID. 55.0

`stockKeepingUnit` String Stock Keeping Unit. 55.0

`unitPrice` Double Unit price. 55.0

`variationValues` Map<String, String> The variation attribute values that define the variation. 55.0


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ProductVariationAttributeOutputRepresentation

Details about a product variation attribute.

**Property Name** **Type** **Description** **Available Version**

`apiName` String API name of the attribute. 55.0

`label` String Label of the attribute. 55.0

#### variationAttribute List< ConnectApi. List of valid values for the variation attribute. 55.0

```
   Values ProductVariation

             AttributeValue
```

`OutputRepresentation`                
#### ConnectApi.ProductVariationAttributeValueOutputRepresentation

Valid value for a product variation attribute.

**Property Name** **Type** **Description** **Available Version**

`name` String API Name of the attribute this value belongs to. 55.0

`orderable` Boolean Whether the value defines an orderable product 55.0
variation.

`value` String Value of the value. 55.0

#### ConnectApi.ProductVariationInfo

Product variation attributes, metadata, and mappings of attribute combinations to variation product IDs.

**Property Name** **Type** **Description** **Available Version**

#### attributesTo List< ConnectApi. List ordered by 50.0

`ProductMappings` `ProductAttributes` `ProductAttribute.Sequence` values that

`ToProductEntry`            - map the attribute value combinations to the variation

product ID.

```
variationAttributeInfo

```

SEE ALSO:

Map<String, Map of field API name to product attribute 51.0
#### ConnectApi. information.

`ProductAttributeInfo` 

ConnectApi.ProductDetail

#### ConnectApi.PromotionApproachingDiscount

Qualifier for a promotion with an approaching discount.


Apex Reference Guide ConnectApi Output Classes

**Property** **Type** **Description** **Required or** **Available Version**
**Optional**

`promotionId` String ID of the promotion with an approaching Required 64.0
discount.

`qualifyingAmount` String Qualifying amount when promotion is Required 64.0
applied.

`qualifying` String Qualifying product total. Required 64.0

```
   ProductTotal

```

`targetType` `ConnectApi.TargetType` Target type of a promotion discount. Required 64.0

**•** `Shipping` —Promotion discounts
shipping amount.

**•** `Transaction` —Promotion
discounts total transaction amount.

#### ConnectApi.PromotionCart

A cart, its items, and its adjustment groups.

**Property Name** **Type** **Description** **Available Version**

#### cartAdjustment <List ConnectApi.PromotionCartAdjustmentGroup > Cart adjustment groups belonging to the cart. 57.0

```
   Groups

#### cartItems List< ConnectApi.PromotionCartItem > Cart items belonging to the cart. 57.0

```

`currencyIsoCode` String Currency code of the cart. 57.0

`id` String ID of the cart. 57.0

`totalAdjustment` String Total adjustment base amount for the cart. 57.0

```
   BaseAmount

```

`totalNetAmount` String Total price of the cart, including adjustments. 57.0

`totalProduct` String Total price of all cart items in the cart. 57.0

```
   BaseAmount

```

SEE ALSO:

ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionCartAdjustmentGroup

Adjustment group associated with a cart.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`adjustmentBasis` String ID of the associated coupon, if applicable. 57.0

```
   Reference

```

`adjustment` String Description of the adjustment. 57.0

```
   Description

#### adjustmentType ConnectApi. How the price adjustment amount is calculated. 57.0
```

`AdjustmentType` Values are:

**•** `AdjustmentAmount` —The adjustment is a
fixed amount.

**•** `AdjustmentPercentage` —The adjustment
is a percentage.

`adjustmentValue` String Price value of the adjustment. 57.0

`baseAmount` String Total amount of the adjustment. 57.0

`cartId` String ID of the cart. 57.0

`id` String ID of the cart adjustment group. 57.0

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.PromotionEvaluation

evaluate(salesTransaction)

#### ConnectApi.PromotionCoupon

A coupon used in a promotion.

**Property Name** **Type** **Description** **Available Version**

`couponCode` String Coupon code. 57.0

`couponErrorCode` String Error code returned if the coupon is invalid. 57.0

`id` String ID of the coupon. 57.0

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

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### coupons List< ConnectApi. Collection of coupon codes to enable promotions. A 57.0

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


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.QueryPath

```

Represents a query path.

**Property Name** **Type** **Description** **Available Version**

`fieldLabel` String Label of the field. 60.0

`fieldName` String Name of the field. 60.0

`objectLabel` String Label of the object. 60.0

`objectName` String Name of the object. 60.0

#### ConnectApi.QueryPathConfig

Represents a query path configuration.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

#### queryPath List< ConnectApi.QueryPath > Query path. 60.0 ConnectApi.QueryPathConfigList

Represents a list of query path configurations.

**Property Name** **Type** **Description** **Available Version**

#### queryPathConfig List< ConnectApi.QueryPathConfig > List of query path configurations. 60.0 ConnectApi.QuerySqlOutput

Represents the SQL query output.

**Property Name** **Type** **Description** **Available Version**

`dataRows` `ConnectApi.QuerySqlRowRepresentation` Data associated with the SQL. 62.0

#### metadata ConnectApi.QuerySqlMetadataItem Metadata associated with the SQL. 62.0

`returnedRows` Long Number of rows returned by the query. 62.0

`status` `ConnectApi.QuerySqlStatus` Metadata related to the status of an SQL query. 62.0

SEE ALSO:

querySql(input)

querySql(input, dataspace)

querySql(input, workloadName, dataspace)

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### dataRows ConnectApi.QuerySqlRowRepresentation Data associated with the SQL. 62.0

`metadata` `ConnectApi.QuerySqlMetadataItem` Metadata associated with the SQL. 62.0

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


Apex Reference Guide ConnectApi Output Classes

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

`rowCount` Long Number of rows available for extraction. 62.0

SEE ALSO:

querySqlStatus(queryId)

querySqlStatus(queryId, waitTimeMs)

querySqlStatus(queryId, dataspace)

querySqlStatus(queryId, dataspace, waitTimeMs)

querySqlStatus(queryId, workloadName, dataspace)

querySqlStatus(queryId, workloadName, dataspace, waitTimeMs)

#### ConnectApi.RangeFacetDisplayMetadataRepresentation

Display metadata representation for a range facet.


Apex Reference Guide ConnectApi Output Classes

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

`displayMetadata` `ConnectApi.RangeFacetDisplayMetadataRepresentation` Metadata required for rendering the range facet. 64.0
on page 2491

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.ReadByPage ConnectApi.ReadByCapability

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`currentPageUrl` String Connect REST API URL identifying the current page. 40.0
The default is 25 items per page.

#### items List< ConnectApi. Collection of read-by information, including users 40.0

`ReadBy`            - and when they last read the feed element.

`nextPageToken` String Token identifying the next page, or `null` if there 40.0
isn’t a next page.

`nextPageUrl` String Connect REST API URL identifying the next page, or 40.0
`null` if there isn’t a next page.

`previousPageToken` String Reserved for future use. 40.0

`previousPageUrl` String Reserved for future use. 40.0

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
on page 2155

`businessObjectiveId` String 18-character business objective ID associated with 59.0
the recommended action.

`channelId` String Associated channel ID for the recommended action. 61.0

`createdDate` Datetime Creation date of the recommended action. 61.0

`description` String Description of the recommended action. 59.0

`domain` String Domain category of the recommended action (e.g., 59.0
"Product").


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`lastModifiedDate` Datetime Date that the recommended action was last modified. 61.0

`name` String Display name of the recommended action. 59.0

```
output

```

`ConnectApi.ActionInfo` Stores the last executed snapshot of the 61.0
`OutputRepresentation` recommended action.
on page 2155

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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
page 2494>

#### ConnectApi.RecommendationAudience

A custom recommendation audience.


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.RecommendedObject

A recommended object, such as a custom or static recommendation.

Subclass of ConnectApi.Actor

**Property Name** **Type** **Description** **Available Version**

`idOrEnum` String ID of a recommendation definition for a custom 34.0
recommendation or the enum value `Today` for

static recommendations that don’t have an ID
(version 35.0 and later).

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`value` Object Field raw value. 63.0

SEE ALSO:

ConnectApi.SearchResult

#### ConnectApi.RecordSnapshot

A record snapshot in a recommendation reaction.

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available**
**Version**

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

ConnectApi.RecordView

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

`RecordsetFilterCriteria`              - record IDs.

SEE ALSO:

evaluateRecordsetFilterCriteria(recordsetFilterCriteriaInput)


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.ReferencedRefundResponse

```

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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

`refundSequence` <List `ConnectApi.RefundSequenceItemOutputRepresentation`   - The order payment summary ID and value of the 65.0
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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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

#### ConnectApi.ReplyIntents


Apex Reference Guide ConnectApi Output Classes

#### ConnectApi.ReplyIntents

List of reply intents for a social post.

**Property Name** **Type** **Description** **Available Version**

#### replies List< ConnectApi.ReplyIntent > List of reply intents for the social post. 45.0

SEE ALSO:

ConnectApi.SocialPostIntents

#### ConnectApi.RepositoryFileDetail

A detailed description of a repository file.

Subclass of ConnectApi.AbstractRepositoryFile.

No additional properties.

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`nextPageUrl` String URL to the next page of items, or `null` if there isn’t 39.0
a next page.

`previousPageUrl` String URL to the previous page of items, or `null` if there 39.0
isn’t a previous page.

#### ConnectApi.RepositoryFolderSummary

A summary of a repository folder.

Subclass of ConnectApi.AbstractRepositoryFolder.

No additional properties.

SEE ALSO:

#### ConnectApi.RepositoryFolderItem ConnectApi.RepositoryGroupSummary

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`levelNumber` Integer

SEE ALSO:

ConnectApi.Reputation

#### ConnectApi.RequestHeader

An HTTP request header name and value pair.

Reputation level number, which is the numerical rank 32.0
of the level, with the lowest level at 1. Administrators
define the reputation level point ranges.

**Property Name** **Type** **Description** **Available Version**

`name` String The name of the request header. 33.0

`value` String The value of the request header. 33.0

SEE ALSO:

ConnectApi.ActionLinkDefinition

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`returnOrderId` String ID of the created ReturnOrder. 50.0

SEE ALSO:

createReturnOrder(returnOrderInput)

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

#### ConnectApi.ScheduledRecommendation

```

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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
Partner Central sites, disabled custom
recommendations no longer appear.

`id` String 18-character ID of the scheduled custom 35.0
recommendation.

`rank` Integer The rank determining the order of this scheduled 35.0
custom recommendation.

`recommendation` String ID of the audience for the scheduled custom 35.0
`AudienceId` recommendation.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.ScopedSearchResults

Keyword search results for an object.

**Property Name** **Type** **Description** **Available Version**

#### metadata ConnectApi. All search metadata associated with the object. 63.0

```
           ObjectMetadata

#### objectQueryInfo ConnectApi. Query execution information for the object. 64.0

           ObjectQueryInfo

```


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

#### ConnectApi.SearchCategory

Search category.

**Property Name** **Type** **Description** **Available Version**

#### category ConnectApi. Information about the category. 52.0

```
           ProductCategoryData

#### children List< ConnectApi. First-level child categories of the category searched 52.0
```

`SearchCategory`          - with non-empty search results.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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

`nameOrId` String Developer name of the attribute. In version 52.0 and 52.0
later, the ID of the attribute isn’t supported.

SEE ALSO:

ConnectApi.ProductSearchResults


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

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
page 2519>

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
           on page 2182

```

`balanceStateOriginalOrderSummary` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the original order Big, 61.0
`on page 2182` summary.


Apex Reference Guide ConnectApi Output Classes

**Property Name** **Type** **Description** **Available Version**

`balanceStateReturnOrder` `ConnectApi.BalanceStatePreviewOutput` The balance state preview for the return order. Big, 61.0

```
              on page 2182

```

`changeBalances` `ConnectApi.ChangeItemOutputRepresentation` Change order financial values for a preview order Big, 60.0
`on page 2234` action.

#### errors List< ConnectApi. Any errors that were returned. Big, 60.0

`ErrorResponse`            

`exchangeOrderSummaryId` String Exchange order summary ID. Big, 60.0

`orderSummaryId` String ID of the order summary. Big, 60.0

`success` Boolean Indicates whether the transaction was successful. Big, 60.0

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

`feeChangeOrderId` String

#### ConnectApi.Subscription

Subscription.

ID of the change order created for the returned order 48.0
items and shipping charges. Use this change order
to create a credit memo.

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


Apex Reference Guide ConnectApi Output Classes

**Name** **Type** **Description** **Available Version**

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


Apex Reference Guide ConnectApi Output Classes

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


Apex Reference Guide ConnectApi Output Classes

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

`ConnectApi.` Customer file source of the activation platform.

```
   ActivationPlatformCustomerFileSource
```
**•** `First_And_Third_Party`

**•** `First_Party`

**•** `Third_Party`

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


Apex Reference Guide ConnectApi Enums

**Enum** **Description**

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


### Apex Reference Guide ConnectApi Exceptions

**Enum** **Description**

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


### Apex Reference Guide ConnectApi Utilities

All exceptions classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3767.

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

```


### Apex Reference Guide ConnectApi Release Notes

```
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

## Context Namespace The Context namespace provides classes and methods to manage the sharing and consumption of business application data by

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


Apex Reference Guide Database Namespace

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


### Apex Reference Guide Batchable Interface Batchable Interface

The class that implements this interface can be executed as a batch Apex job.

Namespace

Database

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)_ : Using Batch

#### Batchable Methods

### The following are methods for Batchable .

IN THIS SECTION:

##### execute(jobId, recordList)

Gets invoked when the batch job executes and operates on one batch of records. Contains or calls the main execution logic for the
batch job.

finish(jobId)
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


Apex Reference Guide Batchable Interface

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


### Apex Reference Guide BatchableContext Interface

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

Namespace

Database

SEE ALSO:

Batchable Interface

#### BatchableContext Methods

### The following are methods for BatchableContext .

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


### Apex Reference Guide Cursor Class

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

Usage

A cursor is created when a SOQL query is executed on a `Database.getCursor()` or a `Database.getCursorWithBinds()`
call. When the SOQL query is invoked, the corresponding rows are returned from the cursor. The maximum number of rows per cursor
is 50 million, regardless of the operation being synchronous or asynchronous.

Example

```
   public class QueryChunkingQueuable implements Queueable {

      private Database.Cursor locator;

      private integer position;

      public QueryChunkingQueuable() {

        locator = Database.getCursor

              ('SELECT Id FROM Contact WHERE LastActivityDate = LAST_N_DAYS:400');

        position = 0;

      }

      public void execute(QueueableContext ctx) {

        List<Contact> scope = locator.fetch(position, 200);

        position += scope.size();

        // do something, like archive or delete the scope list records

        if(position < locator.getNumRecords() ) {

           // process the next chunk

           System.enqueueJob(this);

        }

      }

   }

```

IN THIS SECTION:

Cursor Methods


Apex Reference Guide Cursor Class

#### Cursor Methods The following are methods for Cursor .

IN THIS SECTION:

##### fetch(position, count)

Fetches cursor rows that correspond to the offset position and the specified record count. The maximum number of rows per cursor
is 50 million, regardless of the operation being synchronous or asynchronous. Calling the `Cursor.fetch()` method counts
against the SOQL query limit, and the rows fetched count against the SOQL query row limit.

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

Type: List on page 3874<sObject>

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

Type: List on page 3874<sObject>

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

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_insert_3)_ : Database.insert()

_Apex Reference Guide_ [: SObject.setOptions()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_sobject.htm#apex_System_SObject_setOptions)

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
2681 to check out the entire sample applicaton.

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

A pagination cursor is created when a SOQL query is executed on a `Database.getPaginationCursor()` on page 3634 or a
`Database.getPaginationCursorWithBinds()` on page 3635 call. When the SOQL query is invoked, the corresponding
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

Type: Database.CursorFetchResult on page 2633

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
on page 2681 to check out the entire sample applicaton.

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
DuplicateResult Class on page 2681 to check out the entire sample applicaton.

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
on page 2681 to check out the entire sample applicaton.

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

**•** Each element contains an array of `DuplicateResult` on page 2681 objects, which each represent a duplicate rule that
`FindDuplicates` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2697 objects,
which each represent a matching rule that the duplicate rule applied. If `FindDuplicates` doesn’t find any duplicates for
that matching rule, then the `MatchResult.getMatchRecords()` on page 2698 array is empty. Otherwise, the
`MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2695 elements, which each represent a
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

**•** Each element contains an array of `DuplicateResult` on page 2681 objects, which each represent a duplicate rule that
`FindDuplicatesByIds` applied. Within each `DuplicateResult` object is an array of `MatchResult` on page 2697
objects, which each represent a matching rule that the duplicate rule applied. If `FindDuplicatesByIds` doesn’t find any
duplicates for that matching rule, then the `MatchResult.getMatchRecords()` on page 2698 array is empty. Otherwise,
the `MatchResult.getMatchRecords()` array contains `MatchRecord` on page 2695 objects, which each represent
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

See Column Properties on page 2706 for information about each parameter.

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

See Column Properties on page 2706 for information about each parameter.

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

See Column Properties on page 2706 for information about each parameter.

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

See Column Properties on page 2706 for information about each parameter.

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

See Column Properties on page 2706 for information about each parameter.

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
