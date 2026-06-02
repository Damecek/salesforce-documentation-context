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

createCartFromQuote(webstoreId, quoteId, cartFromQuoteInput)
Create a cart from an approved quote, or duplicate a draft quote into a cart by converting the quote into cart items.

createQuoteFromCart(webstoreId, activeCartOrId, createQuoteFromCartInput)
Create a new quote from an active cart by converting cart items into quote line items.

cloneCart(webstoreId, activeCartOrId, targetEffectiveAccountId, targetType)
Clones an existing cart to create a secondary, read-only cart to support Pay Now functionality. Sets the guest cart status to
`PendingDelete` in a B2B store.

deleteCart(webstoreId, effectiveAccountId, activeCartOrId)
Delete a cart. Sets the guest cart status to `PendingDelete` in a B2B store or `Closed` in a D2C store.

deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId)
Delete a coupon from a cart.

deleteCartCoupon(webstoreId, effectiveAccountId, activeCartOrId, cartCouponId, currencyIsoCode)
Delete a coupon from a cart.


Apex Reference Guide CommerceCart Class

deleteCartItem(webstoreId, effectiveAccountId, activeCartOrId, cartItemId)
Delete an item from a cart.

deleteInventoryReservation(webstoreId, activeCartOrId, effectiveAccountId) (Pilot)
Delete an inventory reservation.

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


Apex Reference Guide CommerceCart Class

getCartSummary(webstoreId, effectiveAccountId, activeCartOrId)
Get a cart.

getCartSummary(webstoreId, effectiveAccountId, activeCartOrId, currencyIsoCode)
Get a cart in a specific currency.

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

##### **`createCartFromQuote(webstoreId, quoteId, cartFromQuoteInput)`**

Create a cart from an approved quote, or duplicate a draft quote into a cart by converting the quote into cart items.

This method performs one of the following operations based on the quote status:

**•** Create Cart from Quote—

**–** Create a cart from a quote only when its status is Approved or Accepted, as initiated by the Accept & Buy action on the My
Quotes page of the B2B storefront.

**–** All items are added at the negotiated and discounted prices.

**–** A quote can be converted to a cart only once if the resulting cart is used to place an order. After the order is placed, the same
quote can't be reused.

**–** If the cart is cleared after conversion (before placing an order), the quote can be converted to a cart again.

**•** Duplicate Quote to Cart—


Apex Reference Guide CommerceCart Class

**–** Duplicate the quote to cart, as initiated by the Duplicate to Cart action on the My Quotes page of the B2B storefront. This operation
isn't supported only for quotes in Approved or Accepted status.

**–** All items are added at their original prices.

Duplicate-to-cart and convert-to-cart operations succeed only when the cart has no matching products. For example, if both the quote
and the cart contain Product A, the API returns an error. Partial conversion or duplication, promotions, and bonus products aren't
supported.

Supported product types by license:

**•** Simple products: Supported with B2B Commerce only or B2B Commerce and Revenue Cloud licenses.

**•** Static bundles: Supported only with the B2B Commerce and Revenue Cloud license.

**•** Dynamic bundles: Supported only with the B2B Commerce and Revenue Cloud license.

**•** Subscription products: Not supported with either B2B Commerce Only or B2B Commerce and Revenue Cloud licenses.

API Version

67.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartFromQuoteOutput createCartFromQuote(String webstoreId,

   String quoteId, ConnectApi.CartFromQuoteInput cartFromQuoteInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   quoteId
```

Type: String

ID of the quote to convert to a cart.

```
   cartFromQuoteInput
```

Type: `ConnectApi.CartFromQuoteInput`

Representation for creating a cart from a quote.

Return Value

Type: `ConnectApi.CartFromQuoteOutput`

##### **`createQuoteFromCart(webstoreId, activeCartOrId, createQuoteFromCartInput)`**

Create a new quote from an active cart by converting cart items into quote line items.

To access the method, your org must have the B2B Commerce license. The method is available only to authenticated users.


Apex Reference Guide CommerceCart Class

This method is used to create a quote from an active cart, retaining pricing and customer details. Buyers can also specify an expiration
date and add comments for negotiation.

Note: Carts must contain at least one product to create a quote. Empty carts return an error. Promotions and bonus products
aren't supported.

Supported product types by license:

**•** Simple products—Supported with B2B Commerce Only or B2B Commerce and Revenue Cloud licenses.

**•** Static bundles—Supported only with the B2B Commerce and Revenue Cloud licenses.

**•** Dynamic bundles—Supported only with the B2B Commerce and Revenue Cloud licenses.

**•** Subscription products—Not supported with either B2B Commerce Only or B2B Commerce and Revenue Cloud licenses.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CreateQuoteFromCartOutput createQuoteFromCart(String webstoreId,

   String activeCartOrId, ConnectApi.CreateQuoteFromCartInput createQuoteFromCartInput)

```

Parameters

```
   webstoreId
```

Type: String

Description

```
   activeCartOrId
```

Type: String

Description

```
   createQuoteFromCartInput
```

Type: `ConnectApi.CreateQuoteFromCartInput`

Description

Return Value

Type: `ConnectApi.CreateQuoteFromCartOutput`

##### **`cloneCart(webstoreId, activeCartOrId, targetEffectiveAccountId, targetType)`**

Clones an existing cart to create a secondary, read-only cart to support Pay Now functionality. Sets the guest cart status to
`PendingDelete` in a B2B store.

API Version

60.0


Apex Reference Guide CommerceCart Class

Available to Guest Users

60.0

Requires Chatter

No

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

Type: `ConnectApi.CartSummary on page 2263`

Usage

[The cloneCart method is valid only for the Pay Now feature. See Salesforce Pay Now for Embedded Payment Solutions.](https://help.salesforce.com/s/articleView?language=en_US&id=sf.pay_now_intro_prereqs.htm)

##### **`deleteCart(webstoreId, effectiveAccountId, activeCartOrId)`**

Delete a cart. Sets the guest cart status to `PendingDelete` in a B2B store or `Closed` in a D2C store.

API Version

49.0

Available to Guest Users

54.0


Apex Reference Guide CommerceCart Class

Requires Chatter

No

Signature

```
   public static Void deleteCart(String webstoreId, String effectiveAccountId, String

   activeCartOrId)

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


Apex Reference Guide CommerceCart Class

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

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

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


Apex Reference Guide CommerceCart Class

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

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

```
   effectiveAccountId
```

Type: String

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

##### **`getCartItemPromotion(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  cartItemPromotionCollectionInput)

```

Get promotions for a cart item.

API Version

52.0

Available to Guest Users

57.0

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


Apex Reference Guide CommerceCart Class

API Version

57.0

Available to Guest Users

57.0

Requires Chatter

No

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


Apex Reference Guide CommerceCart Class

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam, Integer pageSize)

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


Apex Reference Guide CommerceCart Class

Requires Chatter

No

Signature

```
   public static ConnectApi.CartItemCollection getCartItems(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String pageParam, Integer pageSize,

   ConnectApi.CartItemSortOrder sortParam)

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


Apex Reference Guide CommerceCart Class

##### **`getCartItems(webstoreId, effectiveAccountId, activeCartOrId, productFields,`**

```
  pageParam, pageSize, sortParam)

```

Get a specified size, sorted page of items filtered by product fields in a cart.

API Version

49.0

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

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

```


Apex Reference Guide CommerceCart Class

```
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


Apex Reference Guide CommerceCart Class

API Version

60.0

Available to Guest Users

54.0

Requires Chatter

No

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


Apex Reference Guide CommerceCart Class

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

ID of the cart, `active`, or `current` . The `current` value indicates a cart with a status that isn’t `Closed` or `PendingDelete` .
Use active only for B2B Aura stores; all other stores must use current.

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


Apex Reference Guide CommerceCart Class

```
   currencyIsoCode
```

Type: String

Currency ISO code of the cart.

Return Value

Type: `ConnectApi.CartPromotionCollection`

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


Apex Reference Guide CommerceCart Class

##### **`getCartSummary(webstoreId, effectiveAccountId, activeCartOrId,`**

```
  currencyIsoCode)

```

Get a cart in a specific currency.

API Version

57.0

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


Apex Reference Guide CommerceCart Class

API Version

49.0

Available to Guest Users

54.0

Requires Chatter

No

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


Apex Reference Guide CommerceCart Class

Available to Guest Users

57.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CartSummary getOrCreateActiveCartSummary(String webstoreId,

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


Apex Reference Guide CommerceCart Class

Available to Guest Users

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCartItem getProductCartItem(String webstoreId, String

   effectiveAccountId, String activeCartOrId, String productId, String currencyIsoCode)

```

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

Type: `ConnectApi.ProductCartItem on page 2523`

##### **`getProductCartItems(webstoreId, effectiveAccountId, activeCartOrId, pageSize,`**

```
  pageNumber, currencyIsoCode)

```

Get the items in a cart, sorted by product ID.

API Version

60.0


Apex Reference Guide CommerceCart Class

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

Type: `ConnectApi.ProductCartItemCollection on page 2524`

##### **`makeCartPrimary(webstoreId, activeCartOrId, effectiveAccountId)`**

Make a secondary cart a primary cart.


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

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

ID of the cart, `active`, or `current` . The `current` value is available in version 50.0 and later and indicates a cart with a status
that isn’t `Closed` or `PendingDelete` . Use active only for B2B Aura stores; all other stores must use current.

```
   currencyIsoCode
```

Type: String

The currency ISO code of the cart.

Return Value

Type: `ConnectApi.PreserveCart` on page 2516

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

```
   messageVisibility
```

Type: `ConnectApi.CartMessagesVisibilityInput`

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
   cartItemId
```

Type: String

ID of the cart item.

```
   cartItem
```

Type: `ConnectApi.CartItemInput`

A `ConnectApi.CartItemInput` object representing a cart item to update.

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


Apex Reference Guide CommerceCart Class

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


Apex Reference Guide CommerceCart Class

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


### Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups, excludeFields, excludeMedia,
excludePrimaryProductCategory, excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule, excludeProductSellingModels,
excludeDynamicAttributeInfo, noCache)
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


Apex Reference Guide CommerceCatalog Class

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

Type: ConnectApi.NavigationMenuItemCollection on page 2470

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, excludeFields,`**

```
  mediaGroups, excludeMedia, excludeEntitlementDetails,

  excludePrimaryProductCategory)

```

Get a product.

API Version

49.0

Supported in API versions 49.0 to 63.0.


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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

Return Value

Type: `ConnectApi.ProductDetail`


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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

```


Apex Reference Guide CommerceCatalog Class

```
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


Apex Reference Guide CommerceCatalog Class

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

```


Apex Reference Guide CommerceCatalog Class

```
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


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

API Version

64.0

Supported in API versions 64.0 to 65.0.

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


Apex Reference Guide CommerceCatalog Class

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

##### **`getProduct(webstoreId, productId, effectiveAccountId, fields, mediaGroups,`**

```
  excludeFields, excludeMedia, excludePrimaryProductCategory,

  excludeVariationInfo, excludeAttributeSetInfo, excludeQuantityRule,

  excludeProductSellingModels, excludeDynamicAttributeInfo, noCache)

```

Get detailed information for a product without its entitlement information.


Apex Reference Guide CommerceCatalog Class

API Version

65.0

Available to Guest Users

65.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductDetail getProduct(String webstoreId, String productId,

   String effectiveAccountId, List<String> fields, List<String> mediaGroups, Boolean

   excludeFields, Boolean excludeMedia, Boolean excludePrimaryProductCategory, Boolean

   excludeVariationInfo, Boolean excludeAttributeSetInfo, Boolean excludeQuantityRule,

   Boolean excludeProductSellingModels, Boolean excludeDynamicAttributeInfo, String noCache)

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


Apex Reference Guide CommerceCatalog Class

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
returned. If the permission is off, product selling models are not returned, regardless of whether you omit the parameter or provide
a value.

```
   excludeDynamicAttributeInfo
```

Type: Boolean

Specifies whether the dynamic attribute information for the product is returned ( `false` ) or not ( `true` ). If unspecified, defaults to
`true` . This behavior of this parameter depends on whether you turn on the Commerce Dynamic Bundles permission. If dynamic
bundles are supported, and if you set the parameter to `false` (or if you omit the parameter), count is returned. If dynamic bundles
are supported, and if you set the parameter to `true`, count is not returned. If dynamic bundles aren't supported, count isn't returned,
regardless of whether you omit the parameter or provide a value.

```
   noCache
```

Type: String

Specifies whether to ignore cached data and return the latest response ( `true` ) or not ( `false` ).

Return Value

Type: `ConnectApi.ProductDetail`

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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

Type: `ConnectApi.ProductCategoryDetailCollection`

##### **`getProductCategoryPath(webstoreId, productCategoryId, effectiveAccountId)`**

Get the product category path from the root category to the current category.

API Version

49.0

Available to Guest Users

51.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductCategoryPath getProductCategoryPath(String webstoreId,

   String productCategoryId)

```


Apex Reference Guide CommerceCatalog Class

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

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductChildCollection getProductChildCollection(String

   webstoreId, String productId, String effectiveAccountId, List<String> fields,

   List<String> mediaGroups, Boolean excludeFields, Boolean excludeMedia, Boolean

   excludeAttributeSetInfo, Boolean excludeQuantityRule, String pageToken, Integer pageSize)

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
   pageToken
```

Type: String


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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

Supported in API versions 58.0 to 62.0.

Available to Guest Users

58.0

Requires Chatter

No


Apex Reference Guide CommerceCatalog Class

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

##### **`getProducts(webstoreId, effectiveAccountId, ids, skus, fields, excludeMedia,`**

```
  includeQuantityRule, includeProductSellingModels, includeAttributeSetInfo,

  includeGroupByAttributeVariationInfo)

```

Get fields and default images for a list of products.

API Version

63.0

Supported in API versions 63.0 to 64.0.


Apex Reference Guide CommerceCatalog Class

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


Apex Reference Guide CommerceCatalog Class

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


### Apex Reference Guide CommerceCatalogManagement Class

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

Return Value

Type: `ConnectApi.ProductOverviewCollection`

### CommerceCatalogManagement Class

Create or update a composite product. Create a variation product.


Apex Reference Guide CommerceCatalogManagement Class

Namespace

ConnectApi

#### CommerceCatalogManagement Methods These methods are for CommerceCatalogManagement . All methods are static.

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

##### **`compositeCommerceProductUpdate(webstoreId, productId,`**

```
  compositeCommerceProductInputRepresentation)

```

Update a composite product.

API Version

61.0


Apex Reference Guide CommerceCatalogManagement Class

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

Signature

```
   public static ConnectApi.CompositeCommerceVariationOutputRepresentation

   compositeCommerceVariationCreate(String webstoreId,

   ConnectApi.CompositeCommerceVariationInputRepresentation

   compositeCommerceVariationInputRepresentation)

```


### Apex Reference Guide CommercePromotions Class

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

##### decreaseRedemption(couponCodeRedemption)

Get coupon code redemption usage to revert a previously redeemed coupon code.

evaluate(salesTransaction)
Determine which promotions the customer is eligible for based on the store and buyer group, and compute the applicable price
adjustments based on the coupons and the items in the cart. This API evaluates only the first 50 active manual promotions and first
50 active automatic promotions, based on priority. This API computes and returns applicable price adjustments, but it does not apply
those adjustments to the webcart record. If you want to enable promotions based on shipping, contact Salesforce Customer Support.

increaseRedemption(couponCodeRedemption)
Get coupon code redemption addition (increase) usage.

##### **`decreaseRedemption(couponCodeRedemption)`**

Get coupon code redemption usage to revert a previously redeemed coupon code.

API Version

58.0


Apex Reference Guide CommercePromotions Class

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

Type: `ConnectApi.CouponCodeRedemptionInput on page 2065`

Tracks each coupon code redemption.

Return Value

Type: `ConnectApi.CouponCodeRedemptionCollection on page 2326`

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


### Apex Reference Guide CommerceQuotes Class

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

Type: `ConnectApi.CouponCodeRedemptionInput on page 2065`

Tracks each coupon code redemption.

Return Value

Type: `ConnectApi.CouponCodeRedemptionCollection on page 2326`

### CommerceQuotes Class

Namespace

ConnectApi

#### CommerceQuotes Methods

### These methods are for CommerceQuotes . All methods are static.


Apex Reference Guide CommerceQuotes Class

IN THIS SECTION:

##### updateQuote(webstoreId, quoteId, updateQuoteInput)

Initiate a quote renegotiation or decline a quote.

getQuoteDetail(webstoreId, quoteId, effectiveAccountId, fields)
Get quote details associated with a specified account.

getQuotes(webstoreId, effectiveAccountId, fields, sortParam, pageSize, pageToken, earliestDate, latestDate)
Get all quotes associated with a specified account.

createQuoteFromProduct(webstoreId, productId, createQuoteFromProductInput)
Create a quote from a product.

##### **`updateQuote(webstoreId, quoteId, updateQuoteInput)`**

Initiate a quote renegotiation or decline a quote.

This method initiates negotiation only when the quote status is Approved, as triggered by the Renegotiate or Decline action on the My
Quotes page of the B2B storefront.

Updates quote status based on user action, changing Approved quotes back to Draft for renegotiation while saving comments, or setting
status to Denied for rejected quotes.

API Version

67.0

Requires Chatter

No

Signature

```
   public static ConnectApi.UpdateQuoteOutput updateQuote(String webstoreId, String quoteId,

   ConnectApi.updateQuoteInput updateQuoteInput)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore

```
   quoteId
```

Type: String

ID of the quote whose status is to be updated.

```
   updateQuoteInput
```

Type: `ConnectApi.updateQuoteInput`

Representation for updating the quote status and optionally creating an associated note.

Return Value

Type: `ConnectApi.UpdateQuoteOutput`


Apex Reference Guide CommerceQuotes Class

##### **`getQuoteDetail(webstoreId, quoteId, effectiveAccountId, fields)`**

Get quote details associated with a specified account.

API Version

66.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CommerceQuoteDetail getQuoteDetail(String webstoreId, String

   quoteId, String effectiveAccountId, String fields)

```

Parameters

```
   webstoreId
```

Type: String

ID of the web store.

```
   quoteId
```

Type: String

ID of the quote.

```
   effectiveAccountId
```

Type: String

User account ID used to retreive associated quote details.

```
   fields
```

Type: String

[List of fields to include in the response. Supports fields from the objects, including Quote, Quote Line Item, and Product2.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_quote.htm)

Return Value

Type: `ConnectApi.CommerceQuoteDetail`

##### **`getQuotes(webstoreId, effectiveAccountId, fields, sortParam, pageSize,`**

```
  pageToken, earliestDate, latestDate)

```

Get all quotes associated with a specified account.

API Version

66.0

Requires Chatter

No


Apex Reference Guide CommerceQuotes Class

Signature

```
   public static ConnectApi.CommerceQuoteCollection getQuotes(String webstoreId, String

   effectiveAccountId, String fields, ConnectApi.CommereQuotesSortOrder sortParam, Integer

   pageSize, String pageToken, String earliestDate, String latestDate)

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

User account ID used to retreive associated quotes.

```
   fields
```

Type: String

[List of fields to include in the response. Supports fields from the objects, including Quote, Quote Line Item, and Product2.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_quote.htm)

```
   sortParam
```

Type: `ConnectApi.CommereQuotesSortOrder`

Sort order for quotes. Valid values:

**•** CreatedDateAsc—Sorts by the oldest created date.

**•** CreatedDateDesc—Sorts by the most recent created date.

```
   pageSize
```

Type: Integer

Number of items per page. Valid values are from 1 through 200. The default value is 25.

```
   pageToken
```

Type: String

Base64 encoded page token to use to view a page of information. Page tokens are pageToken String returned as part of the response,
such as currentPageToken or nextPageToken. If you don’t specify a value, the first page is returned.

```
   earliestDate
```

Type: String

ISO 8601 date string for the oldest date from which to get quote records. Return quotes created on or after this date. Valid format:
yyyy-MM-dd'T'HH:mm:ss.SSSZ.

```
   latestDate
```

Type: String

ISO 8601 date string for the most recent date from which to get quote records. Return quotes created before this date. Valid format:
yyyy-MM-dd'T'HH:mm:ss.SSSZ.

Return Value

Type: `ConnectApi.CommerceQuoteCollection`


### Apex Reference Guide CommerceSearch Class

##### **`createQuoteFromProduct(webstoreId, productId, createQuoteFromProductInput)`**

Create a quote from a product.

This method creates a new quote from a product on the Product Display Pages (PDP) in a B2B storefront. It creates a temporary (secondary)
cart to process the request. It converts the product details into quote line items based on the specified product ID and quantity. After
processing, the secondary cart is deleted, regardless of whether the API call succeeds or fails.

Supported product types by license:

**•** Simple products—Supported with B2B Commerce Only or B2B Commerce and Revenue Cloud licenses.

**•** Static Bundled—Supported only with the B2B Commerce and Revenue Cloud licenses.

API Version

67.0

Requires Chatter

No

Signature

```
   public static ConnectApi.CreateQuoteFromProductOutput createQuoteFromProduct(String

   webstoreId, String productId, ConnectApi.CreateQuoteFromProductInput

   createQuoteFromProductInput)

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

ID of the product to convert to a quote.

```
   createQuoteFromProductInput
```

Type: `ConnectApi.CreateQuoteFromProductInput`

Representation for creating a quote from a product.

Return Value

Type: `ConnectApi.CreateQuoteFromProductOutput`

### CommerceSearch Class

Get sort rules for the live search index. Get product search suggestions. Search products.

Namespace

ConnectApi


Apex Reference Guide CommerceSearch Class

#### CommerceSearch Methods These methods are for CommerceSearch . All methods are static.

IN THIS SECTION:

##### getSortRules(webstoreId)

Get sort rules for the live index.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults)
Get suggestions for product searches.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults, includeSuggestedProducts, maxSuggestedProducts)
Get suggestions for product searches.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults, includeSuggestedProducts, maxSuggestedProducts,
suggestedFields)
Get suggestions for product searches.

getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults, includeSuggestedProducts, maxSuggestedProducts,
suggestedFields, includeSuggestedTerms, popularProductsCategoryId)
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


Apex Reference Guide CommerceSearch Class

Return Value

Type: `ConnectApi.SortRulesCollection`

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


Apex Reference Guide CommerceSearch Class

##### **`getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults,`**

```
  includeSuggestedProducts, maxSuggestedProducts)

```

Get suggestions for product searches.

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


Apex Reference Guide CommerceSearch Class

Return Value

Type: `ConnectApi.ProductSearchSuggestionsResults`

##### **`getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults,`**

```
  includeSuggestedProducts, maxSuggestedProducts, suggestedFields)

```

Get suggestions for product searches.

API Version

59.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchSuggestionsResults getSuggestions(String

   webstoreId, String effectiveAccountId, String searchTerm, Integer maxResults, Boolean

   includeSuggestedProducts, Integer maxSuggestedProducts, List<String> suggestedFields)

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


Apex Reference Guide CommerceSearch Class

```
   maxSuggestedProducts
```

Type: Integer

Maximum number of product suggestions. Values are from 1 through 10. If unspecified, defaults to 6.

```
   suggestedFields
```

Type: List<String>

List of field names recommended for inclusion in the response based on the search context.

Return Value

Type: `ConnectApi.ProductSearchSuggestionsResults`

##### **`getSuggestions(webstoreId, effectiveAccountId, searchTerm, maxResults,`**

```
  includeSuggestedProducts, maxSuggestedProducts, suggestedFields,

  includeSuggestedTerms, popularProductsCategoryId)

```

Get suggestions for product searches.

API Version

64.0

Available to Guest Users

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.ProductSearchSuggestionsResults getSuggestions(String

   webstoreId, String effectiveAccountId, String searchTerm, Integer maxResults, Boolean

   includeSuggestedProducts, Integer maxSuggestedProducts, List<String> suggestedFields,

   Boolean includeSuggestedTerms, String popularProductsCategoryId)

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


Apex Reference Guide CommerceSearch Class

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

Type: Integer

Maximum number of product suggestions. Values are from 1 through 10. If unspecified, defaults to 6.

```
   suggestedFields
```

Type: List<String>

List of field names recommended for inclusion in the response based on the search context.

```
   includeSuggestedTerms
```

Type: Boolean

Specifies whether a request returns search term suggestions ( `true` ) or not ( `false` ). If unspecified, defaults to `true` . The value
returned can include recent or popular term suggestions. At least one of `includeSuggestedTerms` or
`includeSuggestedProducts` must be set to `true` .

```
   popularProductsCategoryId
```

Type: String

ID of the category that identifies a store's popular products. This category can be configured on the search input component. If
`popularProductsCategoryId` is populated, the search term for a request is empty, and `includeSuggestedProducts`
is `true`, product suggestions are returned from the specified category. If a search term is specified, `popularProducts`
`CategoryId` is ignored and suggestions are based on the search term instead.

Return Value

Type: `ConnectApi.ProductSearchSuggestionsResults`

##### **`searchProducts(webstoreId, effectiveAccountId, productSearchInput)`**

Search products.

API Version

52.0

Available to Guest Users

52.0

Requires Chatter

No


### Apex Reference Guide CommerceSearchConnectFamily Class

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

#### CommerceSearchConnectFamily Methods

### These methods are for CommerceSearchConnectFamily . All methods are static.

IN THIS SECTION:

searchProducts(webstoreId, searchTerm, categoryId, sortRuleId, grouping, fields, refinements, pageParam, pageSize, effectiveAccountId,
includeQuantityRule)
Search products by search term or category in a webstore.

searchProducts(webstoreId, searchTerm, categoryId, sortRuleId, searchFields, grouping, fields, refinements, page, pageSize,
effectiveAccountId, effectiveBuyerGroupIds, includeQuantityRule, includeProductVariationInfo)
Search products by search term or category in a webstore.


Apex Reference Guide CommerceSearchConnectFamily Class

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


Apex Reference Guide CommerceSearchConnectFamily Class

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

##### **`searchProducts(webstoreId, searchTerm, categoryId, sortRuleId, searchFields,`**

```
  grouping, fields, refinements, page, pageSize, effectiveAccountId,

  effectiveBuyerGroupIds, includeQuantityRule, includeProductVariationInfo)

```

Search products by search term or category in a webstore.

API Version

58.0

Available to Guest Users

58.0

Requires Chatter

No


Apex Reference Guide CommerceSearchConnectFamily Class

Signature

```
   public static ConnectApi.CommerceProductSearchResults searchProducts(String webstoreId,

   String searchTerm, List<String> searchFields, String categoryId, String sortRuleId,

   String grouping, List<String> fields, String refinements, Integer page, Integer pageSize,

   String effectiveAccountId, List<String> effectiveBuyerGroupIds, Boolean

   includeQuantityRule, Boolean includeProductVariationInfo)

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
   page
```

Type: Integer

Number of the page you want returned. Starts at 0. If you don’t specify a value or if you specify 0, the first page is returned.

```
   pageSize
```

Type: Integer

Specifies the number of items per page. Valid values are from 1 through 200. If unspecified, defaults to 20.

```
   effectiveAccountId
```

Type: String


### Apex Reference Guide CommerceSearchSettings Class

ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the default value is determined from
context.

```
   includeQuantityRule
```

Type: Boolean

Specifies whether to include purchase quantity rule information for products in search results ( `true` ) or not ( `false` ). If unspecified,
defaults to `false` .

```
   includeProductVariationInfo
```

Type: Boolean

Specifies whether to include product variation information in search results ( `true` ) or not ( `false` ). If unspecified, defaults to

`false` .

```
   effectiveBuyerGroupIds
```

Type: List<String>

List containing an ID of the buyer group for which the request is made. This parameter accepts only a single ID in the list.

```
   searchFields
```

Type: List<String>

The subset of searchable fields to search. Only the fields specified in this parameter are searched. If you don't specify this parameter,
or if the fields specified are invalid, all searchable fields are searched. To use the `searchFields` parameter, you must also specify
the `searchTerm` parameter. The variation attribute field is not supported by the `searchFields` parameter.

Return Value

Type: `ConnectApi.CommerceProductSearchResults`

Usage

Searching products respects buyer View Product entitlements and only users entitled to view product data can access this resource.

### CommerceSearchSettings Class

Get indexes. Get index logs. Create an index of a product catalog.

Namespace

ConnectApi

#### CommerceSearchSettings Methods

### These methods are for CommerceSearchSettings . All methods are static.

IN THIS SECTION:

createCommerceSearchIndex(webstoreId, indexBuildType)
Create an index of a product catalog.

getCommerceSearchIndex(webstoreId, indexId)
Get a Commerce search index.


Apex Reference Guide CommerceSearchSettings Class

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

Usage

This method creates a live index that replaces the current live index. Any indexes that are in progress are removed when you manually
create an index with this method.

##### **`getCommerceSearchIndex(webstoreId, indexId)`**

Get a Commerce search index.


Apex Reference Guide CommerceSearchSettings Class

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


### Apex Reference Guide CommerceStorePricing Class

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

#### CommerceStorePricing Methods

### These methods are for CommerceStorePricing . All methods are static.

IN THIS SECTION:

getProductPrice(webstoreId, productId, effectiveAccountId)
Get the list and buyer price for a product.

getProductPrice(webstoreId, productId, effectiveAccountId, productSellingModelIds)
Get a product’s list and buyer price for specified product selling models.


Apex Reference Guide CommerceStorePricing Class

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

ID of the product.

```
   effectiveAccountId
```

Type: String

ID of the buyer account or guest buyer profile for which the request is made.

Return Value

Type: `ConnectApi.ProductPrice`


Apex Reference Guide CommerceStorePricing Class

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

```
   productSellingModelIds
```

Type: List<String>

List of product selling model IDs for the product.

Return Value

Type: `ConnectApi.ProductPrice`


Apex Reference Guide CommerceStorePricing Class

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

If a store is segmented into markets, this API looks at the language parameter appended to the URL to determine the shopper’s locale
and returns the appropriate values.

##### **`getProductPrices(webstoreId, effectiveAccountId, productIds, currencyIsoCode)`**

Get the prices for multiple products using multiple product IDs and a currency ISO code.


Apex Reference Guide CommerceStorePricing Class

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

##### **`getProductPrices(webstoreId, effectiveAccountId, pricingInput)`**

Get the prices for multiple products.


Apex Reference Guide CommerceStorePricing Class

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

API Version

57.0


### Apex Reference Guide CommerceWishlist Class

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

Namespace

ConnectApi


Apex Reference Guide CommerceWishlist Class

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

getWishlistSummaries(webstoreId, effectiveAccountId, includeDisplayedList, productFields, pageSize, sortItemsBy)
Get wishlist summaries with product fields sorted by items with a specified number of items per page.

removeWishlistItem(webstoreId, effectiveAccountId, wishlistId, wishlistItemId)
Remove an item from a wishlist.


Apex Reference Guide CommerceWishlist Class

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

##### **`addItemToWishlist(webstoreId, effectiveAccountId, wishlistId,`**

```
  wishlistItemInput)

```

Add an item to a wishlist.


Apex Reference Guide CommerceWishlist Class

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

Requires Chatter

No


Apex Reference Guide CommerceWishlist Class

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

```
   wishlistId
```

Type: String

ID of the wishlist.

```
   effectiveAccountId
```

Type: String


Apex Reference Guide CommerceWishlist Class

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

Usage

This method respects buyer View Product entitlements and only users entitled to view product data can access it.


Apex Reference Guide CommerceWishlist Class

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

API Version

49.0


Apex Reference Guide CommerceWishlist Class

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

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.

```
   wishlistInput
```

Type: `ConnectApi.WishlistInput`


Apex Reference Guide CommerceWishlist Class

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

Requires Chatter

No


Apex Reference Guide CommerceWishlist Class

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

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceWishlist Class

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

```
   effectiveAccountId
```

Type: String

ID of the account for which the request is made. If `null`, defaults to the account ID for the context user.


Apex Reference Guide CommerceWishlist Class

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

Signature

```
   public static ConnectApi.WishlistItemCollection getWishlistItems(String webstoreId,

   String effectiveAccountId, String wishlistId, String productFields, String pageParam,

   Integer pageSize, ConnectApi.WishlistItemSortOrder sortItemsBy)

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

API Version

49.0

Requires Chatter

No


Apex Reference Guide CommerceWishlist Class

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


Apex Reference Guide CommerceWishlist Class

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


Apex Reference Guide CommerceWishlist Class

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

Requires Chatter

No

Signature

```
   public static Void removeWishlistItem(String webstoreId, String effectiveAccountId,

   String wishlistId, String wishlistItemId)

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


### Apex Reference Guide Communities Class

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

Return Value

Type: `ConnectApi.WishlistSummary`

### Communities Class

Get information about Experience Cloud sites in your org.


Apex Reference Guide Communities Class

Namespace

ConnectApi

#### Communities Methods These methods are for Communities . All methods are static.

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

API Version

28.0

Requires Chatter

No


Apex Reference Guide Communities Class

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

ID of an Experience Cloud site. You can’t specify `null` or `internal` .

Return Value

Type: `ConnectApi.Community`


### Apex Reference Guide CommunityModeration Class CommunityModeration Class

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

addFlagToFeedElement(communityId, feedElementId, note)
Add a moderation flag with a note to a feed element.

addFlagToFeedElement(communityId, feedElementId, type, note)
Add a moderation flag of the specified type with a note to a feed element.


Apex Reference Guide CommunityModeration Class

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

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId)

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

Visibility behavior of a flag for various user types.

**•** `ModeratorsOnly` —The flag is visible only to users with moderation permissions on the flagged element or item.


Apex Reference Guide CommunityModeration Class

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

Return Value

Type: `ConnectApi.ModerationFlags`


Apex Reference Guide CommunityModeration Class

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

API Version

38.0


Apex Reference Guide CommunityModeration Class

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

Requires Chatter

Yes


Apex Reference Guide CommunityModeration Class

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

Requires Chatter

Yes


Apex Reference Guide CommunityModeration Class

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

Signature

```
   public static ConnectApi.ModerationFlags addFlagToComment(String communityId, String

   commentId, ConnectApi.CommunityFlagType type, ConnectApi.CommunityFlagVisibility

   visibility, String note)

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

Requires Chatter

Yes


Apex Reference Guide CommunityModeration Class

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

```
   feedElementId
```

Type: String

ID of the feed element.


Apex Reference Guide CommunityModeration Class

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

Type of moderation flag.

**•** `FlagAsInappropriate` —Flag for inappropriate content.

**•** `FlagAsSpam` —Flag for spam.


Apex Reference Guide CommunityModeration Class

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

Usage

To add a flag to a feed element, Allow members to flag content must be selected for an Experience Cloud site.


Apex Reference Guide CommunityModeration Class

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

##### **`addFlagToFeedElement(communityId, feedElementId, type, visibility)`**

Add a moderation flag of the specified type and visibility to a feed element.


Apex Reference Guide CommunityModeration Class

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

##### **`addFlagToFeedElement(communityId, feedElementId, visibility, note)`**

Add a moderation flag of the specified visibility with a note to a feed element.


Apex Reference Guide CommunityModeration Class

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

API Version

38.0


Apex Reference Guide CommunityModeration Class

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

##### **`getFlagsOnComment(communityId, commentId)`**

Get the moderation flags on a comment.


Apex Reference Guide CommunityModeration Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### ContentHub Test Methods These test methods are for ContentHub . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
`promptTemplateGenerationsInput)` [to resolve a Sales Email prompt template. For more examples, see Resolve a Prompt](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_resolve_prompt_template.htm)
[Template.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectapi_examples_resolve_prompt_template.htm)

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

Type: `ConnectApi.PreviewCartToExchangeOrderInputRepresentation on page 2141`

Information required to preview a cart to exchange order.

Return Value

Type: `ConnectApi.PreviewCartToExchangeOrderOutputRepresentation on page 2516`

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

Type: `ConnectApi.SubmitCartToExchangeOrderInputRepresentation on page 2152`

Information required to submit a cart to exchange order.

Return Value

Type: `ConnectApi.SubmitCartToExchangeOrderOutputRepresentation on page 2589`

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

ConnectApi.EstimateDeliveryDateInputRepresentation on page 2082

Estimated delivery date.

```
   externalReference
```

Type: String

Delivery estimation setup external reference ID.

Return Value

Type: ConnectApi.EstimateDeliveryDateOutputRepresentation on page 2359

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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
Create FulfillmentOrders for multiple OrderDeliveryGroups in a single request.

createMultipleInvoices(invoicesInput)
Create Invoices for multiple FulfillmentOrders.

##### **`cancelFulfillmentOrderLineItems(fulfillmentOrderId,`**

```
  cancelFulfillmentOrderLineItemsInput)

```

Cancel FulfillmentOrderLineItems from a FulfillmentOrder. This action doesn’t cancel the associated OrderItemSummaries, so reallocate
the canceled quantities to a new FulfillmentOrder.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation

   cancelFulfillmentOrderLineItems(String fulfillmentOrderId,

```


Apex Reference Guide FulfillmentOrder Class

```
   ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation

   cancelFulfillmentOrderLineItemsInput)

```

Parameters

```
   fulfillmentOrderId
```

Type: String

ID of the FulfilllmentOrder.

```
   cancelFulfillmentOrderLineItemsInput
```

Type: `ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation`

List of FulfillmentOrderLineItems to cancel.

Return Value

Type: `ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation`

Example

```
   String fulfillmentOrderId = '0a3xx0000000085AAA';

   List<ConnectApi.FulfillmentOrderLineItemInputRepresentation> itemToCancelList = new

   List<ConnectApi.FulfillmentOrderLineItemInputRepresentation>();

   for(FulfillmentOrderLineItem fulfillmentOrderLineItem :

   fulfillmentOrder.FulfillmentOrderLineItems){

     ConnectApi.FulfillmentOrderLineItemInputRepresentation itemToCancel = new

   ConnectApi.FulfillmentOrderLineItemInputRepresentation();

     itemToCancel.fulfillmentOrderLineItemId = fulfillmentOrderLineItem.Id;

     itemToCancel.quantity = 1;

     itemToCancelList.add(itemToCancel);

   }

   ConnectAPI.FulfillmentOrderLineItemsToCancelInputRepresentation input = new

   ConnectAPI.FulfillmentOrderLineItemsToCancelInputRepresentation();

   input.fulfillmentOrderLineItemsToCancel = itemToCancelList;

   ConnectAPI.FulfillmentOrderCancelLineItemsOutputRepresentation result =

   ConnectAPI.FulfillmentOrder.cancelFulfillmentOrderLineItems(fulfillmentOrderId, input);

##### **`createFulfillmentOrders(fulfillmentOrderInput)`**

```

Create one or more FulfillmentOrders and FulfillmentOrderLineItems for an OrderDeliveryGroupSummary, which defines a delivery
method and recipient for an OrderSummary. You specify the OrderItemSummaries to allocate, which can be fulfilled from different
locations. Specifying multiple fulfillment groups creates one FulfillmentOrder for each location. For each OrderItemSummary, a
FulfillmentOrderLineItem is created and assigned to the corresponding FulfillmentOrder.

API Version

48.0


Apex Reference Guide FulfillmentOrder Class

Requires Chatter

No

Signature

```
   public static ConnectApi.FulfillmentOrderOutputRepresentation

   createFulfillmentOrders(ConnectApi.FulfillmentOrderInputRepresentation

   fulfillmentOrderInput)

```

Parameters

```
   fulfillmentOrderInput
```

Type: `ConnectApi.FulfillmentOrderInputRepresentation`

OrderItemSummaries to allocate, with location and delivery information.

Return Value

Type: `ConnectApi.FulfillmentOrderOutputRepresentation`

Example

```
   String orderSummaryId = '1Osxx0000004CCG';

   String fulfillmentType = 'warehouse';

   String warehouseFromLocationId = [SELECT Id from Location WHERE LocationType='Warehouse'

   LIMIT 1].Id;

   ConnectApi.FulfillmentOrderInputRepresentation fulfillmentOrderInput = new

   ConnectApi.FulfillmentOrderInputRepresentation();

   fulfillmentOrderInput.orderSummaryId = orderSummaryId;

   List<OrderDeliveryGroupSummary> orderDeliveryGroupSummaryList = [SELECT Id FROM

   OrderDeliveryGroupSummary WHERE OrderSummaryId =: orderSummaryId];

   for (OrderDeliveryGroupSummary orderDeliveryGroupSummary: orderDeliveryGroupSummaryList){

     fulfillmentOrderInput.orderDeliveryGroupSummaryId = orderDeliveryGroupSummary.Id;

     List<ConnectApi.FulfillmentGroupInputRepresentation> fulfillmentGroups = new

   List<ConnectApi.FulfillmentGroupInputRepresentation>();

     ConnectApi.FulfillmentGroupInputRepresentation fulfillmentGroup = new

   ConnectApi.FulfillmentGroupInputRepresentation();

     fulfillmentGroup.fulfilledFromLocationId = warehouseFromLocationId;

     fulfillmentGroup.fulfillmentType = fulfillmentType;

     List<ConnectApi.OrderItemSummaryInputRepresentation> orderItemSummaries = new

   List<ConnectApi.OrderItemSummaryInputRepresentation>();

    List<OrderItemSummary> orderItemSummaryList = [Select Id, quantity FROM OrderItemSummary

    WHERE OrderSummaryId =: orderSummaryId AND OrderDeliveryGroupSummaryId =:

   orderDeliveryGroupSummary.Id];

     for(OrderItemSummary orderItemSummary : orderItemSummaryList){

```


Apex Reference Guide FulfillmentOrder Class

```
      ConnectApi.OrderItemSummaryInputRepresentation oisInputRepresentation = new

   ConnectApi.OrderItemSummaryInputRepresentation();

      oisInputRepresentation.orderItemSummaryId = orderItemSummary.Id;

      oisInputRepresentation.quantity = orderItemSummary.quantity;

      orderItemSummaries.add(oisInputRepresentation);

     }

     fulfillmentGroup.orderItemSummaries = orderItemSummaries;

     fulfillmentGroups.add(fulfillmentGroup);

     fulfillmentOrderInput.fulfillmentGroups = fulfillmentGroups;

   }

   ConnectApi.FulfillmentOrderOutputRepresentation result =

   ConnectAPI.FulfillmentOrder.createFulfillmentOrders(fulfillmentOrderInput);

##### **`createInvoice(fulfillmentOrderId, invoiceInput)`**

```

Create an invoice for a FulfillmentOrder that doesn’t have one.

API Version

48.0

Requires Chatter

No

Signature

```
   public static ConnectApi.FulfillmentOrderInvoiceOutputRepresentation createInvoice(String

   fulfillmentOrderId, ConnectApi.FulfillmentOrderInvoiceInputRepresentation invoiceInput)

```

Parameters

```
   fulfillmentOrderId
```

Type: String

ID of the FulfillmentOrder.

```
   invoiceInput
```

Type: `ConnectApi.FulfillmentOrderInvoiceInputRepresentation`

Required input with no data.

Return Value

Type: `ConnectApi.FulfillmentOrderInvoiceOutputRepresentation`

Example

```
   String fulfillmentOrderId = '0a3xx0000000085AAA';

```


Apex Reference Guide FulfillmentOrder Class

```
   ConnectApi.FulfillmentOrderInvoiceInputRepresentation input = new

   ConnectApi.FulfillmentOrderInvoiceInputRepresentation();

   ConnectAPI.FulfillmentOrderInvoiceOutputRepresentation result =

   ConnectApi.FulfillmentOrder.createInvoice(fulfillmentOrderId, input);

##### **`createMultipleFulfillmentOrder(multipleFulfillmentOrderInput)`**

```

Create FulfillmentOrders for multiple OrderDeliveryGroups in a single request.

API Version

50.0

Requires Chatter

No

Signature

```
   public static ConnectApi.MultipleFulfillmentOrderOutputRepresentation

   createMultipleFulfillmentOrder(ConnectApi.MultipleFulfillmentOrderInputRepresentation

   multipleFulfillmentOrderInput)

```

Parameters

```
   multipleFulfillmentOrderInput
```

Type: `ConnectApi.MultipleFulfillmentOrderInputRepresentation`

Wraps a list of inputs for creating fulfillment orders.

Return Value

Type: `ConnectApi.MultipleFulfillmentOrderOutputRepresentation`

##### **`createMultipleInvoices(invoicesInput)`**

Create Invoices for multiple FulfillmentOrders.

API Version

52.0

Requires Chatter

No

Signature

```
   public static ConnectApi.MultipleFulfillmentOrderInvoicesOutputRepresentation

   createMultipleInvoices(ConnectApi.MultipleFulfillmentOrderInvoicesInputRepresentation

   invoicesInput)

```


### Apex Reference Guide IBusinessObjectivesAndRecsFamily Class

Parameters

```
   invoicesInput
```

Type: `ConnectApi.MultipleFulfillmentOrderInvoicesInputRepresentation`

The FulfillmentOrders to create Invoices for.

Return Value

Type: `ConnectApi.MultipleFulfillmentOrderInvoicesOutputRepresentation`

### IBusinessObjectivesAndRecsFamily Class

Get and patch business objectives, or goals. Get, create, patch, and update recommended actions for business objectives.

Namespace

ConnectApi

#### IBusinessObjectivesAndRecsFamily Methods

### These methods are for IBusinessObjectivesAndRecsFamily . All methods are static.

IN THIS SECTION:

##### createRecommendations(busObjRecommendationInput)

Create recommended actions for a business objective, or goal.

getBusinessObjectives(webstoreId, channelId, kpiName, includeRecSummary, includeInsightSummary)
Get business objectives, or goals, for a webstore.

getRecommendations(businessObjectiveId, domain, channelId, externalName, state, secondaryState, tertiaryState, grouping)
Get recommended actions for a business objective, or goal.

patchBusinessObjective(busObjRecommendationInput)
Partially update a business objective, or goal.

patchRecommendations(busObjRecommendationInput)
Partially update a recommended action associated with a business objective, or goal.

updateRecommendations(busObjRecommendationInput)
Update a recommended action for a business objective, or goal.

##### **`createRecommendations(busObjRecommendationInput)`**

Create recommended actions for a business objective, or goal.

API Version

60.0


Apex Reference Guide IBusinessObjectivesAndRecsFamily Class

Requires Chatter

No

Signature

```
   public static ConnectApi.RecRepresentation

   createRecommendations(ConnectApi.BusObjRecommendationInputRepresentation

   busObjRecommendationInput)

```

Parameters

```
   busObjRecommendationInput
```

Type: `ConnectApi.BusObjRecommendationInputRepresentation` on page 2026

A `ConnectApi.BusObjRecommendationInputRepresentation` object representing a recommended action for a
business objective.

Return Value

Type: `ConnectApi.RecRepresentation` on page 2555

##### **`getBusinessObjectives(webstoreId, channelId, kpiName, includeRecSummary,`**

```
  includeInsightSummary)

```

Get business objectives, or goals, for a webstore.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BusinessObjectivesSummaryOutputRepresentation

   getBusinessObjectives(String webstoreId, String channelId, String kpiName, Boolean

   includeRecSummary, Boolean includeInsightSummary)

```

Parameters

```
   webstoreId
```

Type: String

ID of the webstore.

```
   channelId
```

Type: String

ID of the channel.


Apex Reference Guide IBusinessObjectivesAndRecsFamily Class

```
   kpiName
```

Type: String

Name of the key performance indicator (KPI).

```
   includeRecSummary
```

Type: Boolean

Specifies whether to include a summary of recommended actions in the response.

```
   includeInsightSummary
```

Type: Boolean

Specifies whether to include insight summary information in the response.

Return Value

Type: `ConnectApi.BusinessObjectivesSummaryOutputRepresentation` on page 2247

##### **`getRecommendations(businessObjectiveId, domain, channelId, externalName,`**

```
  state, secondaryState, tertiaryState, grouping)

```

Get recommended actions for a business objective, or goal.

API Version

59.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecommendationsOutputRepresentation getRecommendations(String

   businessObjectiveId, String domain, String channelId, String externalName, String state,

   String secondaryState, String tertiaryState, String grouping)

```

Parameters

```
   businessObjectiveId
```

Type: String

ID of the business objective.

```
   domain
```

Type: String

Recommendation domain.

```
   channelId
```

Type: String

ID of the channel.

```
   externalName
```

Type: String


Apex Reference Guide IBusinessObjectivesAndRecsFamily Class

External name of the recommended action.

```
   state
```

Type: String

State of the recommended action.

```
   secondaryState
```

Type: String

Secondary state of the recommended action.

```
   tertiaryState
```

Type: String

Tertiary state of the recommended action.

```
   grouping
```

Type: String

Grouping associated with the recommended action. This is a free-form categorization field.

Return Value

Type: `ConnectApi.RecommendationsOutputRepresentation` on page 2557

##### **`patchBusinessObjective(busObjRecommendationInput)`**

Partially update a business objective, or goal.

API Version

62.0

Requires Chatter

No

Signature

```
   public static ConnectApi.BusObjSummaryOutputRepresentation

   patchBusinessObjective(ConnectApi.BusinessObjectivesInputRepresentation

   busObjRecommendationInput)

```

Parameters

```
   busObjRecommendationInput
```

Type: `ConnectApi.BusinessObjectivesInputRepresentation` on page 2025

A `ConnectApi.BusinessObjectivesInputRepresentation` object representing the business objective or objectives
to update.

Return Value

Type: `ConnectApi.BusObjSummaryOutputRepresentation` on page 2246


Apex Reference Guide IBusinessObjectivesAndRecsFamily Class

##### **`patchRecommendations(busObjRecommendationInput)`**

Partially update a recommended action associated with a business objective, or goal.

API Version

61.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecRepresentation

   patchRecommendations(ConnectApi.BusObjRecommendationInputRepresentation

   busObjRecommendationInput)

```

Parameters

```
   busObjRecommendationInput
```

Type: `ConnectApi.BusObjRecommendationInputRepresentation` on page 2026

A `ConnectApi.BusObjRecommendationInputRepresentation` object representing the recommended action to
update.

Return Value

Type: `ConnectApi.RecRepresentation` on page 2555

##### **`updateRecommendations(busObjRecommendationInput)`**

Update a recommended action for a business objective, or goal.

API Version

60.0

Requires Chatter

No

Signature

```
   public static ConnectApi.RecRepresentation

   updateRecommendations(ConnectApi.BusObjRecommendationInputRepresentation

   busObjRecommendationInput)

```

Parameters

```
   busObjRecommendationInput
```

Type: `ConnectApi.BusObjRecommendationInputRepresentation` on page 2026


### Apex Reference Guide Knowledge Class

A `ConnectApi.BusObjRecommendationInputRepresentation` object representing the recommended action to
update.

Return Value

Type: `ConnectApi.RecRepresentation` on page 2555

### Knowledge Class

Get information about trending articles in Experience Cloud sites.

Namespace

ConnectApi

#### Knowledge Methods

### These methods are for Knowledge . All methods are static.

IN THIS SECTION:

##### getTopViewedArticlesForTopic(communityId, topicId, maxResults)

Get the top viewed articles for a topic.

getTrendingArticles(communityId, maxResults)
Get trending articles for an Experience Cloud site.

getTrendingArticlesForTopic(communityId, topicId, maxResults)
Get the trending articles for a topic in an Experience Cloud site.

##### **`getTopViewedArticlesForTopic(communityId, topicId, maxResults)`**

Get the top viewed articles for a topic.

API Version

41.0

Available to Guest Users

41.0

Requires Chatter

No

Signature

```
   public static ConnectApi.KnowledgeArticleVersionCollection

   getTopViewedArticlesForTopic(String communityId, String topicId, Integer maxResults)

```


Apex Reference Guide Knowledge Class

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

#### Knowledge Test Methods These test methods are for Knowledge . All methods are static.

For information about using these methods to test your `ConnectApi` [code, see Testing ConnectApi Code.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)

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

_Apex Developer Guide_ [: Testing ConnectApi Code](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/connectAPI_TestingApex.htm)


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

[Service Appointments](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_service_appointments.htm)

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

[Service Appointments](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_service_appointments.htm)

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

