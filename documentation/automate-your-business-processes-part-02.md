**Input Parameter** **Description**

```
expCurrentState

```

Store Output Values

The current state of the session.

This input is an Apex-defined variable of enum `CheckoutStateEnum` .

**Output Parameter** **Description**

`requestId` The ID of the request that processes and then either creates or returns the Checkout Session.

Error Conditions

**Error Condition** **Description**

Expected Validation
Error

The current state of the checkout session, identified by `checkoutSessionId` parameter, doesn’t match
the `expectedState` parameter, so the validation fails.

HTTP Status Code: 4XX

Invalid Checkout
Invalid input for the Checkout Session ID.
Session ID
Error Code: UNKNOWN_EXCEPTION

HTTP Status Code: 403

Invalid Session or
Either the session doesn’t exist or the user doesn’t have the required permissions.
Inadequate User
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Access

HTTP Status Code: 400

User Can’t Invoke
Action

The caller doesn’t have the appropriate permissions to call the action, including the MAD or B2B Commerce
Integrator user perms.

Error Code: BAD_REQUEST

HTTP Status Code: 400

Account Associated
The effective account associated with the cart isn’t a valid account.
With Cart Is Invalid or
Error Code: INSUFFICIENT_ACCESS_OR_READONLY
Inaccessible

HTTP Status Code: 400

User Isn’t a Member of
The buyer user isn’t a member of the store.
the Store
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

To use the B2B Commerce Update Checkout Session Action, these requirements apply.

**•** The user has the appropriate permissions to invoke the action.

**•** The effective account is valid.

**•** The buyer account is a member of the store.

**•** The cart status isn’t set to `Closed` or `Processing` .

**•** The `CartcheckoutSession.IsProcessing` field is `false` .

SEE ALSO:

Add and Edit Elements

Commerce Checkout Flow Core Actions

The Commerce Checkout Flow provides several core actions for implementing a successful checkout
process within your Commerce org. To add one of these actions to your flow, add an Action element.
##### Then select the Commerce category, and search for the appropriate action. Cart actions aren’t

available in flows for B2B stores built on an Aura template.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex `ConnectApi` namespace. For more information on using Apex-defined variables in
flows, see Considerations for the Apex-Defined Data Type on page 260.

Flow Core Action for Commerce Checkout Flow: Add Cart Item
Add an item to a cart.

Flow Core Action for Commerce Checkout Flow: Create Cart
Create a cart.

Flow Core Action for Commerce Checkout Flow: Delete Cart
Delete a cart.

Flow Core Action for Commerce Checkout Flow: Get Cart Items
Get items in a cart.

Flow Core Action for Commerce Checkout Flow: Get Cart Promotions
Get promotions associated with a cart.

Flow Core Action for Commerce Checkout Flow: Add Cart Item

Add an item to a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

##### In Flow Builder, add an Action element to your flow. Select the Commerce category, and search
###### for Add Cart Item . To access this action from REST API, use the name addCartItem .


EDITIONS

Available in: Lightning
Experience

Available in: **Performance**,
**Professional**, and **Unlimited**
Editions

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Cart State or` ID of the cart or state of the cart to add an item to. Valid state values are: _`active`_ and _`current`_ . A current
`ID` cart is not closed or pending deletion.

`effectiveAccountId` (Optional) ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
default value is determined from context.

`Web Store ID` The ID of the web store.

`Cart Item` [This input is an Apex-defined variable of class ConnectApi.CartItemInput, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_cart_item.htm)

```
   Input
```

**•** `productId`            - ID of the product.

**•** `quantity`            - Quantity of the cart item. Use a value that can be converted to BigDecimal.

**•** `type`            - Type of the cart item. The only valid value is _`Product`_ .

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Added Cart` [This output is an Apex-defined variable of class ConnectApi.CartItem, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_cart_item.htm)

```
   Item
```

**•** `itemizedAdjustmentAmount`            - Total itemized adjustment amount for the item, including
promotions and excluding taxes.

**•** `listPrice`            - List price for the item.

**•** `salesPrice`            - Sales price for the item.

**•** `totalAdjustmentAmount`            - Adjustments made to the unit price for the item. This value is
informational only and isn’t used in pricing calculations.

**•** `totalAmount`            - Total amount for the item.

**•** `totalListPrice`            - Total list price for the item.

**•** `totalPrice`            - Total price for the item including adjustments but excluding taxes.

**•** `totalTax`            - Total tax for the item.

**•** `unitAdjustedPrice`            - Unit price, including adjustments, for the item. This value is informational
only and isn’t used in pricing calculations.

**•** `unitAdjustmentAmount`            - Total amount including discounts, but excluding shipping and tax, for
product items in the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to the cart.
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400

Flow Core Action for Commerce Checkout Flow: Create Cart

Create a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Create Cart . To access this action from REST API, use the name createCart .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Web Store ID` The ID of the web store.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Cart Input` [This input is an Apex-defined variable of class ConnectApi.CartInput, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_cart.htm)

**•** `effectiveAccountId`         - (Optional) ID of the buyer account or guest buyer profile for which the
request is made. If unspecified, the default value is determined from context.

**•** `isSecondary`         - (Optional) Specifies whether the cart is secondary ( _`true`_ ) or not ( _`false`_ ). If
unspecified, defaults to _`false`_ .

**•** `name`         - (Optional) Name of the cart. The name can have up to 250 Unicode characters. If unspecified,
defaults to the generated name.

**•** `type`         - (Optional) Type of cart. The only valid value is _`Cart`_ . If unspecified, defaults to _`Cart`_ .

Store Output Values

Use output values later in the flow. The values are assigned when the cart is created.

**Output Parameter** **Description**

`Cart Summary` [This output is an Apex-defined variable of class ConnectApi.CartSummary, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_cart_summary.htm)

**•** `accountId`          - ID of the account for the cart.

**•** `cartId`          - ID of the cart.

**•** `currencyIsoCode`          - Three-letter ISO 4217 currency code associated with the cart.

**•** `grandTotalAmount`          - Grand total amount including shipping and tax for items in the cart, in the
currency of the cart.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `isSecondary`            - Specifies whether the cart is secondary ( _`true`_ ) or not ( _`false`_ ).

**•** `name`            - Name of the cart.

**•** `purchaseOrderNumber`            - Purchase order for the cart.

**•** `status`            - Status of the cart. Possible values are:

**–** _`Active`_              - Cart is active.

**–** _`Checkout`_              - Cart is in checkout.

**–** _`Closed`_              - Cart is closed.

**–** _`PendingDelete`_              - Cart is pending deletion; for example, a user deleted the cart but the job hasn’t
completed yet.

**–** _`Processing`_              - Cart is processing.

**•** `totalChargeAmount`            - Total amount for shipping and other charges in the currency of the cart.

**•** `totalListPrice`            - Total list price for the cart.

**•** `totalProductAmount`            - Total amount including discounts, but excluding shipping and tax, for
product items in the cart.

**•** `totalProductAmountAfterAdjustments`            - Total product amount, including promotions.

**•** `totalProductCount`            - Total count of items in the cart.

**•** `totalPromotionalAdjustmentAmount`            - Total promotional adjustment amount for items in
the cart.

**•** `totalTaxAmount`            - Total tax amount for the cart, including tax on shipping, if applicable.

**•** `type`            - Type of cart. Value is always _`Cart`_ .

**•** `uniqueProductCount`            - Total count of unique items, or SKUs, in the cart.

**•** `webstoreId`            - ID of the web store of the cart.

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to create a cart. Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Commerce Checkout Flow: Delete Cart

Delete a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Delete Cart . To access this action from REST API, use the name deleteCart .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Cart State or` ID of the cart or state of the cart to delete. Valid state values are: _`active`_ and _`current`_ . A current cart is
`ID` neither closed nor pending deletion.

`effectiveAccountId` (Optional) ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
default value is determined from context.

`Web Store ID` ID of the web store associated with the cart.

Store Output Values

Output values aren’t available for this action.

Error Conditions

**Error Condition** **Description**

The user doesn’t have Error Message: You don't have access to this cart. If possible, contact the admin for this web store.
access to the cart.
Error Code: INSUFFICIENT_ACCESS_OR_READONLY

HTTP Status Code: 400

Flow Core Action for Commerce Checkout Flow: Get Cart Items

Get items in a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Get Cart Items . To access this action from REST API, use the name getCartItems .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Cart ID` The ID of the cart owned by the user.

`Effective` (Optional) The ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
`Account ID` default value is determined from context.

`User ID` The ID of the buying user who owns the cart.

`Web Store ID` The ID of the store associated with the cart.

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Cart Items` [An Apex ConnectApi.CartItemCollection record that includes a collection of line items in a cart.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cart_item_collection.htm)

Error Conditions

**Error Condition** **Description**

A required parameter Error Message: You must specify a value for the {0} parameter. <!--Where 0 is the API name of the parameter
hasn't been specified. that requires input.-->

Error Code: REQUIRED_FIELD_MISSING

HTTP Status Code: 400

The specified ID is Error Message: Something's not right with the ID "{0}" specified for the {1} parameter. Check it and try again.
invalid. <!--Where 0 is the invalid ID, and 1 is the API name of the input parameter with the invalid ID.-->

Error Code: INVALID_INPUT

HTTP Status Code: 400

The specified effective Error Message: The ID "{0}" specified for the {1} parameter isn't a valid {2} record. <!--Where 0 is the specified
account ID is invalid ID, and 1 is the API name of the parameter with the specified ID, and 2 is the name of the valid record type.-->
for the account or
Error Code: INVALID_TYPE
guest buyer profile.

HTTP Status Code: 400

The specified store or
cart doesn’t exist.

Error Message: We couldn't find a record with the ID "{0}" specified for the {1} parameter. Check the record and
try again. <!--Where 0 is the ID of the record that doesn't exist, and 1 is the parameter that the ID was specified
for–>

Error Code: RECORD_NOT_FOUND

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Commerce Checkout Flow: Get Cart Promotions

Get promotions associated with a cart.

Note: Cart actions aren’t available in flows for B2B stores built on an Aura template. To build
[a B2B Commerce Checkout flow for an Aura store, see B2B Commerce Checkout Flow (Aura).](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-setup-checkout-flow.html)

In Flow Builder, add an Action element to your flow. Select the **Commerce** category, and search
###### for Get Cart Promotions . To access this action from REST API, use the name

`getCartPromotions` .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

`Cart ID` The ID of the cart owned by the user.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

`Effective` (Optional) The ID of the buyer account or guest buyer profile for which the request is made. If unspecified, the
`Account ID` default value is determined from context.

`User ID` The ID of the buying user who owns the cart.

`Web Store ID` The ID of the store associated with the cart.

Store Output Values

Use output values later in the flow. The values are assigned when the item is created.

**Output Parameter** **Description**

`Cart` [An Apex ConnectApi.CartPromotionCollection record that includes a collection of line items in a cart.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cart_promotion_collection.htm)

```
Promotions

```

Error Conditions

**Error Condition** **Description**

A required parameter Error Message: You must specify a value for the {0} parameter. <!--Where 0 is the API name of the parameter
hasn't been specified. that requires input.-->

Error Code: REQUIRED_FIELD_MISSING

HTTP Status Code: 400

The specified ID is Error Message: Something's not right with the ID "{0}" specified for the {1} parameter. Check it and try again.
invalid. <!--Where 0 is the invalid ID, and 1 is the API name of the input parameter with the invalid ID.-->

Error Code: INVALID_INPUT

HTTP Status Code: 400


Automate Your Business Processes with Salesforce Flow Flow Reference

**Error Condition** **Description**

The specified effective Error Message: The ID "{0}" specified for the {1} parameter isn't a valid {2} record. <!--Where 0 is the specified
account ID is invalid ID, and 1 is the API name of the parameter with the specified ID, and 2 is the name of the valid record type.-->
for the account or
Error Code: INVALID_TYPE
guest buyer profile.

HTTP Status Code: 400

The specified store or
cart doesn’t exist.

Error Message: We couldn't find a record with the ID "{0}" specified for the {1} parameter. Check the record and
try again. <!--Where 0 is the ID of the record that doesn't exist, and 1 is the parameter that the ID was specified
for–>

Error Code: RECORD_NOT_FOUND

HTTP Status Code: 400

##### Salesforce Order Management Flow Core Actions

Salesforce Order Management provides several core actions for implementing order management
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the **Order Management** category, and search for the appropriate action.

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex ConnectApi namespace. For more information on using Apex-defined variables in flows,
see Considerations for the Apex-Defined Data Type on page 260.

Flow Core Action for Order Management: Add Order Item Summary
Add up to 100 order product summaries to an order summary. This action creates a change
order record, an order product record, and an order product summary record. It also creates
any supporting adjustment, tax, and summary records.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Flow Core Action for Order Management: Adjust Order Item Summaries Preview
Preview the expected results of adjusting the price of one or more order product summaries on an order summary, without executing
the adjustment. You can only apply a discount, not an increase. The output of this action contains the values that would be set on
the change orders created by submitting the proposed adjustment.

Flow Core Action for Order Management: Adjust Order Item Summaries Submit
Adjust the price of one or more order product summaries on an order summary. You can only apply a discount, not an increase. This
action creates one or more change order records.

Flow Core Action for Order Management: Authorize Payment
Authorize a payment on a credit card. You can include details for a new credit card or reference an existing PaymentMethod.

Flow Core Action for Order Management: Cancel Fulfillment Order Item
Cancel fulfillment order products from a fulfillment order. You can cancel more than one product and specify a quantity to cancel
for each of them. This action doesn’t cancel the associated order product summaries, it only reduces their allocated quantities.
Usually, you reallocate the canceled quantities to a new fulfillment order.

Flow Core Action for Order Management: Cancel Order Item Summaries Preview
Preview the expected results of canceling one or more order product summaries from an order summary without executing the
cancel. The output of this action contains the values that would be set on the change order created by submitting the proposed
cancel.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Cancel Order Item Summaries Submit
Cancel one or more order product summaries from an order summary. This action creates a change order record.

Flow Core Action for Order Management: Cancel Order Summary Preview
Preview the expected results of canceling all order product summaries for an order summary without executing the cancel. The
output of this action contains the values that would be set on the change order created by submitting the proposed cancel.

Flow Core Action for Order Management: Cancel Order Summary Submit
Cancel all order product summaries for an order summary. This action inserts a background operation into an asynchronous job
queue and returns the ID of that operation.

Flow Core Action for Order Management: Confirm Held Fulfillment Order Capacity
Confirm held fulfillment order capacity at one or more locations. This action decreases a location’s held capacity and increases its
assigned fulfillment order count. Confirm held capacity when you assign a fulfillment order to a location.

Flow Core Action for Order Management: Create Credit Memo
Create a credit memo to represent the refund for one or more change orders associated with an order summary.

Flow Core Action for Order Management: Create Fulfillment Order
Create one or more fulfillment orders and fulfillment order products for an order delivery group summary, which defines a recipient
and delivery method. You specify the order product summaries to fulfill and the fulfillment locations to handle them. If you specify
multiple fulfillment locations, a fulfillment order is created for each one.

Flow Core Action for Order Management: Create Fulfillment Orders
Create fulfillment orders and fulfillment order products for multiple order delivery group summaries, each of which defines a recipient
and delivery method. You specify the order product summaries to fulfill and the fulfillment locations to handle them. If you specify
multiple fulfillment locations for one order delivery group summary, a fulfillment order is created for each one.

Flow Core Action for Order Management: Create an Invoice from Change Orders
Create an invoice to represent the charges for one or more change orders. Create invoices for change orders that increase order
amounts, such as return fees. When you ensure the refund for a return, include the invoices for the associated return fees in the
input.

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order
Create an invoice for a fulfillment order that doesn’t have one.

Flow Core Action for Order Management: Create Order Payment Summary
Create an order payment summary for a payment authorization or payments that use the same payment method and are attached
to the same order summary.

Flow Core Action for Order Management: Create Order Summary
Create an order summary based on an order. That order is considered the original order for the order summary. Subsequent change
orders that apply to the order summary are also represented as order records.

Flow Core Action for Order Management: Create Return Order
Create a return order and return order items for order items belonging to an order summary. You can add return fees for any of the
order items.

Flow Core Action for Order Management: Ensure Funds Async
Ensure funds for an invoice, and apply them to it. If needed, capture authorized funds by sending a request to a payment provider.
This action inserts a background operation into an asynchronous job queue and returns the ID of that operation so you can track its
status. Payment gateway responses appear in the payment gateway log and don’t affect the background operation status.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Ensure Refunds Async
Ensure refunds for a credit memo or excess funds by sending a request to a payment provider. This action inserts a background
operation into an asynchronous job queue and returns the ID of that operation so you can track its status. Payment gateway responses
appear in the payment gateway log and don’t affect the background operation status.

Flow Core Action for Order Management: Find Routes with Fewest Splits
Evaluate ordered product quantities against available inventory to determine the smallest combination of locations that can fulfill
the order. If multiple combinations of the minimum number of locations can fulfill the order, the action returns multiple options.
Optionally, you can specify a maximum allowable number of locations. By default, the action executes up to 1,000,000 times, stopping
when it hits 10,000 results.

Flow Core Action for Order Management: Use OCI to Find Routes with Fewest Splits
Evaluate ordered product quantities against available inventory to determine the smallest combination of locations that can fulfill
the order. If multiple combinations of the minimum number of locations can fulfill the order, the action returns multiple options.
Optionally, you can specify a maximum allowable number of locations and a list of locations to exclude from the calculation. This
action combines the Omnichannel Inventory Get Availability action and the Order Management Find Routes with Fewest Splits
actions. Instead of calling Get Availability and including the output in the Find Routes with Fewest Splits input, call this action and
specify a location or location group to fulfill each ordered product. By default, this action executes up to 1,000,000 times, stopping
when it hits 10,000 results. This action handles the inventory check.

Flow Core Action for Order Management: Get Fulfillment Order Capacity Values
Get information about the current fulfillment order capacity of one or more locations.

Flow Core Action for Order Management: Hold Fulfillment Order Capacity
Hold capacity to process fulfillment orders at one or more locations. This action increases a location’s held capacity. Hold capacity
when you plan to assign a fulfillment order to a location.

Flow Core Action for Order Management: Order Routing Rank by Average Distance
Calculate the average distance from sets of inventory locations to an order recipient, and return the sets sorted by that average
distance. Use this action to compare the average shipping distances for different sets of locations that can fulfill an order.

Flow Core Action for Order Management: Release Held Fulfillment Order Capacity
Release held fulfillment order capacity at one or more locations. This action decreases a location’s held capacity without increasing
its assigned fulfillment order count. Release held capacity when you cancel assigning a fulfillment order to a location.

Flow Core Action for Order Management: Return Order Item Summaries Preview
Preview the expected results of a simple return of one or more order product summaries from an order summary without executing
the return. The output of this action contains the values that would be set on the change order created by submitting the proposed
return.

Flow Core Action for Order Management: Return Order Item Summaries Submit
Return one or more order product summaries from an order summary. This action is a simple return that creates a change order but
not a return order.

Flow Core Action for Order Management: Return Return Order Items
Process one or more return order line items belonging to a return order. This action creates a change order record for the returned
items and makes the processed return order line items read-only. You can include return order fees associated with the return order
line items. If you do, a change order record is created for the return fees. If a processed return order line item has a remaining expected
quantity, the action creates a separate return order line item representing that quantity.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Add Order Item Summary

Add up to 100 order product summaries to an order summary. This action creates a change order
record, an order product record, and an order product summary record. It also creates any supporting
adjustment, tax, and summary records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Add Order Item Summary .

Important: Don’t call this action via REST API. Use it only in flows.

Set Input Values

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Create record variables to use in the input. Use values from earlier in the flow to set their values.
The action generates records based on those values. Remember to include all required values for
each object type. For example, the order item summary record variable must include an order delivery group summary ID.

Note: For this action’s input values, use record variables, not existing records or record IDs.

**Input Parameter** **Description**

```
Order Item

Summary Input

```

Store Output Values

This input is an Apex-defined variable of class runtime_commerce_oms.AddOrderItemSummaries.

For information on setting up the input data, see the Usage section of this topic.

The variable has one field: `newItems` . This field is a list of one or more Apex-defined variables of class
runtime_commerce_oms.AddItem. Each of the variables includes these fields.

**•** `orderItemSummary` - An order product summary record variable representing the order product
to add.

**•** `reasonCode` - Reason for the addition. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

**•** `orderItemTaxLineItemSummaries` - A list of zero or more order product tax line item summary
record variables associated with the order product summary.

**•** `orderItemAdjustmentLineSummaries` - A list of zero or more Apex-defined variables of class
runtime_commerce_oms.AddItemAdjustment that has these fields.

**–** `orderItemAdjustmentLineSummary`  - An order product adjustment line summary record
variable associated with the order product being added.

**–** `orderItemTaxLineItemSummaries`  - A list of zero or more order product tax line item
summary record variables associated with the order product adjustment line summary.

**Output Parameter** **Description**

```
Order Item

Summary Output

```

This output is an Apex-defined variable of class ConnectApi.AddOrderItemSummaryOutputRepresentation. It
includes these fields.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `changeBalances` [— An Apex-defined variable of class ConnectApi.ChangeItemOutputRepresentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)
that has these fields.

**–** `grandTotalAmount`              - Change to the total with tax.

**–** `totalAdjDeliveryAmtWithTax`              - Change to the adjusted delivery subtotal, including tax.

**–** `totalAdjDistAmountWithTax`              - Change to the total order adjustments, including tax.

**–** `totalAdjProductAmtWithTax`              - Change to the adjusted product subtotal, including tax.

**–** `totalAdjustedDeliveryAmount`              - Change to the adjusted delivery subtotal.

**–** `totalAdjustedDeliveryTaxAmount`              - Change to the adjusted delivery subtotal tax.

**–** `totalAdjustedProductAmount`              - Change to the adjusted product subtotal.

**–** `totalAdjustedProductTaxAmount`              - Change to the adjusted product subtotal tax.

**–** `totalAdjustmentDistributedAmount`              - Change to the total order adjustments.

**–** `totalAdjustmentDistributedTaxAmount`              - Change to the total order adjustments tax.

**–** `totalAmount`              - Change to the pretax total.

**–** `totalExcessFundsAmount`              - The amount of excess funds available on the order payment
summaries related to the order summary. It’s equal to the captured amount that is owed as a refund
but isn’t associated with an invoice or credit memo. Excess funds normally occur when order products
are canceled before fulfillment but after payment has been captured. This situation isn’t common in
the US, where funds are normally authorized but not captured until the fulfillment process begins. This
value includes all excess funds related to the order summary, not only the funds related to the current
action.

**–** `totalRefundableAmount`              - The total amount available to be refunded. It’s the sum of the
excess funds and any outstanding change order grand total amounts that apply to post-fulfillment
changes. This value includes all refundable amounts related to the order summary, not only the amount
related to the current action.

**–** `totalRequiredFundsAmount`              - The total amount associated with the order products added
in the current action.

This amount isn’t necessarily the amount that must be captured. For example, in an even exchange
flow, the order amount reduction from canceling the exchanged products offsets the required funds
amount of the replacement products.

**–** `totalTaxAmount`              - Change to the total tax.

**•** `changeOrderId`            - ID of the change order generated by the action.

**•** `newItems`            - A list of one or more Apex-defined variables of class
ConnectApi.AddItemOutputRepresentation, each of which represents an added order product, and has
these fields.

**–** `id`              - ID of the order product summary.

**–** `name`              - Name of the order product summary.

**–** `orderItemAdjustmentLineSummaries`              - A list of zero or more Apex-defined variables of
class ConnectApi.AddItemAdjustmentOutputRepresentation, each of which represents an order product
adjustment line summary associated with the added order product summary, and has these fields.

**•** `id`               - ID of the order product adjustment line summary.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `name`               - Name of the order product adjustment line summary.

**•** `orderItemTaxLineItemSummaries`               - A list of zero or more Apex-defined variables of
class ConnectApi.AddItemTaxOutputRepresentation, each of which represents an order product
tax line item summary associated with the order product adjustment line summary, and has these
fields.

**–** `id`                 - ID of the order product tax line item summary.

**–** `name`                 - Name of the order product tax line item summary.

**–** `orderItemTaxLineItemSummaries`              - A list of zero or more Apex-defined variables of class
ConnectApi.AddItemTaxOutputRepresentation, each of which represents an order product tax line
item summary associated with the added order product summary, and has these fields.

**•** `id`               - ID of the order product tax line item summary.

**•** `name`               - Name of the order product tax line item summary.

**•** `orderSummaryId`            - ID of the order summary specified in the input.

To set up the Order Item Summary Input:

**1.** Use record variables to define the order product summaries, order product adjustment line summaries, and order product tax line
item summaries. Sending an Id isn’t required.

**•** Required fields for an order product summary:

**–** ListPrice (Only if Order Summary Pricebook2Id is NULL or empty)

**–** Name

**–** OrderDeliveryGroupSummaryId

**–** OrderSummaryId

**–** PricebookEntryId (Only if Order Summary Pricebook2Id is set)

**–** Product2Id

**–** Quantity

**–** TotalLineAmount

**–** UnitPrice

**–** TypeCode

**–** Type

**•** Required fields for an order product adjustment line summary:

**–** Amount

**–** Name

**–** OrderSummaryId

**•** Required fields for an order product tax line item summary:

**–** Amount

**–** Name

**–** OrderSummaryId


Automate Your Business Processes with Salesforce Flow Flow Reference

**–** TaxEffectiveDate

**–** Type

**2.** Use an assignment element to set the `orderItemSummary` field on a runtime_commerce_oms.AddItem variable to the order
product summary record variable.

**3.** For each adjustment to the product being added, use an assignment element to set the `orderItemAdjustmentLineSummary`
field on a runtime_commerce_oms.AddItemAdjustment variable to the corresponding order product adjustment line summary
record variable. Use assignment elements to add the order product tax line summary record variables associated with it to the
`orderItemTaxLineItemSummaries` field on the same runtime_commerce_oms.AddItemAdjustment variable.

**4.** Use an assignment element to add the runtime_commerce_oms.AddItemAdjustment variables to the
`orderItemAdjustmentLineSummaries` field on the runtime_commerce_oms.AddItem variable.

**5.** For each tax on the product being added, use an assignment element to add the corresponding order product tax line summary
record variable to the `orderItemTaxLineItemSummaries` field on the runtime_commerce_oms.AddItem variable.

**6.** Use an assignment element to set the `reasonCode` field on the runtime_commerce_oms.AddItem variable to a valid reason.

**7.** Use an assignment element to add the runtime_commerce_oms.AddItem variable to the `newItems` field on a
runtime_commerce_oms.AddOrderItemSummaries variable.

**8.** Repeat steps 1 through 6 for each order product that you want to include in the action, adding the inputs to the same
runtime_commerce_oms.AddOrderItemSummaries variable. You can add up to five order products at a time.

**9.** Use the runtime_commerce_oms.AddOrderItemSummaries variable in the action input.

Flow Core Action for Order Management: Adjust Order Item Summaries Preview

Preview the expected results of adjusting the price of one or more order product summaries on an
order summary, without executing the adjustment. You can only apply a discount, not an increase.
The output of this action contains the values that would be set on the change orders created by
submitting the proposed adjustment.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Adjust Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

`Order Summary` ID of the order summary associated with the order product summaries that you want to preview adjusting the
`Id` prices of.

###### Adjust Order This input is an Apex-defined variable of class ConnectApi.AdjustOrderItemSummaryInputRepresentation,

`Product` which includes these fields:

```
Summaries
```

**•** `adjustItems` —This field is a list of Apex-defined variables of class

`Input` [ConnectApi.AdjustItemInputRepresentation. Each of the variables includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_item.htm)

**–** `orderItemSummaryId` —ID of an order product summary to preview a price adjustment for.

**–** `description` —Optional description of the adjustment.

**–** `adjustmentType` —Specifies how to calculate the adjustment amount from the
`discountValue` field. It can have one of these values:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithTax`_ —The value of `discountValue` is the adjustment, including tax.

**•** _`AmountWithoutTax`_ —The value of `discountValue` is the adjustment, not including tax.
Tax is calculated on the value and added.

**•** _`Percentage`_ —The value of `discountValue` is a percentage discount. It’s divided by 100,
and then multiplied by the total price and total tax amount of the order product summary to
determine the adjustment amount.

**–** `discountValue` —The value used to calculate the adjustment amount, as specified by the
`adjustmentType` . It must be a negative value.

**–** `reason` —Adjustment reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `allocatedItemsChangeOrderType` —Specifies how change orders would be created for order
product summary quantities that are currently being fulfilled, defined as QuantityAllocated - QuantityFulfilled.
It can have one of these values:

**–** _`Disallowed`_ —When distributing the adjustment, ignore any quantities being fulfilled. If an order
product summary’s entire quantity is being fulfilled, return an error. This value is the default.

**–** _`InFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Submitting
the adjustment would create a separate change order for the adjustments made to those quantities.

**–** _`PreFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Submitting
the adjustment would include the adjustments made to those quantities in the change order for
pre-fulfillment quantity adjustments.

Store Output Values

Use output values later in the flow.

**Output Parameter** **Description**

```
Adjust Order

Product

Summary Output

```

[This output is an Apex-defined variable of class ConnectApi.AdjustOrderSummaryOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_adjust_output.htm)
contains the financial changes that would result from the proposed adjustment. Most of the values represent
the deltas of the values on the associated order summary.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment has been captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `postFulfillmentChangeOrderId` field is always null for a preview action.

The `preFulfillmentChangeOrderId` field is always null for a preview action.

The `inFulfillmentChangeOrderId` field is always null for a preview action.

Usage

When a price adjustment is applied to an order product summary, its quantities are considered in three groups:

**•** Pre-fulfillment—QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**•** In-fulfillment—QuantityAllocated - QuantityFulfilled

**•** Post-fulfillment—QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the `allocatedItemsChangeOrderType`
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

To set up the Adjust Order Product Summaries Input:

**•** Use Assignment elements to set the `orderItemSummaryId`, `description`, `adjustmentType`, `discountValue`,
and `reason` field values on one or more `ConnectApi.AdjustItemInputRepresentation` variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Use an Assignment element to add the `ConnectApi.AdjustItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use an Assignment element to set the `allocatedItemsChangeOrderType` field on the
`ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use the `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable and the order summary ID in
the action input.

In a flow for adjusting the prices of order product summaries, display the output of this action for the user to review before executing
the adjustment. When the user verifies the expected results, pass the same input to an Adjust Order Item Summaries Submit action.

SEE ALSO:

Flow Core Action for Order Management: Adjust Order Item Summaries Submit

Add and Edit Elements

Flow Core Action for Order Management: Adjust Order Item Summaries Submit

Adjust the price of one or more order product summaries on an order summary. You can only apply
a discount, not an increase. This action creates one or more change order records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Adjust Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` ID of the order summary associated with the order product summaries that you
`Summary` want to adjust the prices of.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Adjust`

```
Order

Product

Summaries

Input

```

This input is an Apex-defined variable of class
[ConnectApi.AdjustOrderItemSummaryInputRepresentation, which includes these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_order_item_summary.htm)
fields:

**•** `adjustItems` —This field is a list of Apex-defined variables of class
[ConnectApi.AdjustItemInputRepresentation. Each of the variables includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_adjust_item.htm)
these fields:

**–** `orderItemSummaryId` —ID of an order product summary to adjust
the price of.

**–** `description` —Optional description of the adjustment.

**–** `adjustmentType` —Specifies how to calculate the adjustment
amount from the `discountValue` field. It can have one of these
values:

**•** _`AmountWithTax`_ —The value of `discountValue` is the
adjustment, including tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithoutTax`_ —The value of `discountValue` is the adjustment, not including tax.
Tax is calculated on the value and added.

**•** _`Percentage`_ —The value of `discountValue` is a percentage discount. It’s divided by 100,
and then multiplied by the total price and total tax amount of the order product summary to
determine the adjustment amount.

**–** `discountValue` —The value used to calculate the adjustment amount, as specified by the
`adjustmentType` . It must be a negative value.

**–** `reason`              - Adjustment reason.The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `allocatedItemsChangeOrderType` —Specifies how to create change orders for order product
summary quantities that are currently being fulfilled, defined as QuantityAllocated - QuantityFulfilled. It can
have one of these values:

**–** _`Disallowed`_ —When distributing the adjustment, ignore any quantities being fulfilled. If an order
product summary’s entire quantity is being fulfilled, return an error. This value is the default.

**–** _`InFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Create a
separate change order for the adjustments made to those quantities.

**–** _`PreFulfillment`_ —When distributing the adjustment, include quantities being fulfilled. Include
the adjustments made to those quantities in the change order for pre-fulfillment quantity adjustments.

Store Output Values

Use output values later in the flow. The values are assigned when the change orders are created.

**Output Parameter** **Description**

`Adjust Order` [This output is an Apex-defined variable of class ConnectApi.AdjustOrderSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_adjust_output.htm)
`Product` Depending on the order product summaries included in the adjustment, one or more change orders are
`Summary Output` generated. If multiple change orders are generated, then the `changeBalances` values combine the values
from both of them.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment has been captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `postFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that have been fulfilled.

The `preFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that haven’t been fulfilled. If the input
specified an `allocatedItemsChangeOrderType` of _`PreFulfillment`_, this change order also
includes the changes applicable to order product summary quantities that are in the process of being fulfilled.

The `inFulfillmentChangeOrderId` is the ID of the change order representing the portion of the
adjustment that was applied to order product summary quantities that are in the process of being fulfilled.
This change order is only created for an input that specified an `allocatedItemsChangeOrderType`
of _`InFulfillment`_ .

Usage

When a price adjustment is applied to an order product summary, its quantities are considered in three groups:

**•** Pre-fulfillment—QuantityAvailableToFulfill, which is equal to QuantityOrdered - QuantityCanceled - QuantityAllocated

**•** In-fulfillment—QuantityAllocated - QuantityFulfilled

**•** Post-fulfillment—QuantityAvailableToReturn, which is equal to QuantityFulfilled - QuantityReturnInitiated

You can apply adjustments to these groups in three different ways, controlled by the `allocatedItemsChangeOrderType`
input property:

**•** Distribute the adjustment evenly between pre-fulfillment and post-fulfillment quantities. Ignore in-fulfillment quantities. Create one
change order for the adjustments to pre-fulfillment quantities and one change order for the adjustments to post-fulfillment quantities.

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to both pre-fulfillment and in-fulfillment quantities, and one change order for the adjustments to post-fulfillment
quantities.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Distribute the adjustment evenly between pre-fulfillment, in-fulfillment, and post-fulfillment quantities. Create one change order
for the adjustments to pre-fulfillment quantities, one change order for the adjustments to in-fulfillment quantities, and one change
order for the adjustments to post-fulfillment quantities.

To set up the Adjust Order Product Summaries Input:

**•** Use Assignment elements to set the `orderItemSummaryId`, `description`, `adjustmentType`, `discountValue`,
and `reason` field values on one or more `ConnectApi.AdjustItemInputRepresentation` variables.

**•** Use an Assignment element to add the `ConnectApi.AdjustItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use an Assignment element to set the `allocatedItemsChangeOrderType` field on the
`ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable.

**•** Use the `ConnectApi.AdjustOrderItemSummaryInputRepresentation` variable and the order summary ID in
the action input.

In a flow for adjusting the prices of order product summaries, run an Adjust Order Item Summaries Preview action before running this
action. Then display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

After submitting a price adjustment, process refunds as appropriate:

**•** If the discount only applied to order product summaries for which payment hasn’t been captured, it doesn’t require a refund. This
situation normally applies to order products in the US that haven’t been fulfilled.

**•** If the discount applied to order product summaries that haven’t been fulfilled and for which payment has been captured, process
a refund. In this case, pass the `totalExcessFundsAmount` from `changeBalances` to the Ensure Refunds Async action.

**•** If the discount applied to order product summaries that have been fulfilled, process a refund. Pass the
`postFulfillmentChangeOrderId` to the Create Credit Memo action, then pass the credit memo to the Ensure Refunds
Async action.

**•** If the discount applied to both fulfilled and unfulfilled order product summaries for which payment has been captured, process both
refunds. Pass the `postFulfillmentChangeOrderId` to the Create Credit Memo action, then pass the credit memo and
the `totalExcessFundsAmount` from `changeBalances` to the Ensure Refunds Async action.

Important: Excess funds aren’t reduced until the payment processor issues a refund. If you don’t process refunds promptly,
subsequent refunds can be inaccurate. Consider this example.

**•** An order with a total amount of $100 is placed, and the amount is captured immediately.

**•** A product is canceled from the order, resulting in $20 of excess funds.

**•** Before the excess funds are sent to the payment provider in an ensure refunds action, another product is canceled. This
cancellation adds another $20 of excess funds. However, because the original $20 hasn’t been refunded yet, the cancel action
returns a total excess funds amount of $40.

**•** The first excess funds amount ($20) is sent to the payment provider in an ensure refunds request.

**•** The second excess funds amount ($40) is sent to the payment provider in an ensure refunds request.

**•** The payment provider receives requests for $60 of refunds, when the correct refund total is $40. Because the total refund
amount is less than the total captured amount of $100, the payment provider issues $60 in refunds.

SEE ALSO:

Flow Core Action for Order Management: Adjust Order Item Summaries Preview

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Authorize Payment

Authorize a payment on a credit card. You can include details for a new credit card or reference an
existing PaymentMethod.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Authorize Payment . To access this action from REST API, use the name

`authorizePayment` .

Note: This action is available with the PaymentsAPIUser user permission.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

`Payment` [This input is an Apex-defined variable of class ConnectApi.AuthorizationRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_authorization.htm)

```
Authorization
```

**•** `accountId` —ID of the account that contains the payment transaction being authorized.
```
Request

```

**•** `accountId` —ID of the account that contains the payment transaction being authorized.

**•** `amount` —Authorization amount.

**•** `comments` —(Optional) Comments for the payment authorization.

**•** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group record.

**•** `effectiveDate` —Date that the authorization is applied to the transaction.

**•** `paymentGatewayId` —Payment gateway that processes the authorization.

**•** `paymentGroup` —(Optional) Payment group for the authorization. The payload must reference either
a paymentGroup or a paymentGroupId, but not both. This field is an Apex-defined variable of class
[ConnectApi.PaymentGroupRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_payment_group.htm)

**–** `createPaymentGroup` —(Optional) Specifies whether to create a payment group ( _`true`_ ) or not
( _`false`_ ).

**–** `currencyIsoCode` —(Optional) Three-letter ISO 4217 currency code associated with the payment
group record.

**–** `id` —(Optional) ID of the payment group record.

**–** `sourceObjectId` —(Optional) Source object ID of the payment group record. Supports only OrderId.

**•** `paymentMethod` —Payment method for the authorization. The payload must either reference an
existing payment method or include details for a new payment method, but not both. This field is an
[Apex-defined variable of class ConnectApi.AuthApiPaymentMethodRequest, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_auth_api_payment_method.htm)

[This input includes the fields from the parent class, ConnectApi.BaseApiPaymentMethodRequest.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_base_api_payment_method.htm)

**–** `address` —Address for the payment method. This field is an Apex-defined variable of class
[ConnectApi.AddressRequest. It includes these fields, all of which are optional:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_address.htm)

**•** `city`

**•** `companyName`

**•** `country`

**•** `postalCode`

**•** `state`

**•** `street`


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `cardPaymentMethod` —(Optional) When using a new payment method, the details of that method.
[This field is an Apex-defined variable of class ConnectApi.CardPaymentMethodRequest, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_card_payment_method.htm)
these fields:

**•** `accountId` —Salesforce account to which this payment method is linked.

**•** `cardCategory` —Valid values are _`CreditCard`_ and _`DebitCard`_ .

**•** `cardHolderFirstName` —First name of the card holder.

**•** `cardHolderLastName` —Last name of the card holder.

**•** `cardHolderName` —Full name of the card holder.

**•** `cardNumber` —Card number.

**•** `cardType` —Valid values are:

**–** _`AmericanExpress`_

**–** _`DinersClub`_

**–** _`JCB`_

**–** _`Maestro`_

**–** _`MasterCard`_

**–** _`Visa`_

**•** `comments` —(Optional) Comments for the payment method.

**•** `cvv` —CVV.

**•** `email` —Email of the card holder.

**•** `expiryMonth` —Card expiration month.

**•** `expiryYear` —Card expiration year.

**•** `nickName` —(Optional) Nickname for the payment method.

**•** `startMonth` —(Optional) Start month of the card.

**•** `startYear` —(Optional) Start year of the card.

**–** `id` —(Optional) When using an existing payment method, the ID of that method.

**–** `saveForFuture` —Whether to save the payment method for future use.

Store Output Values

Use output values later in the flow. The values are assigned when a response is received from the payment gateway.

**Output Parameter** **Description**

`Payment` [This output is an Apex-defined variable of class ConnectApi.AuthorizationResponse, which includes these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_authorization_output.htm)
`Authorization` fields:

```
   Response
```

**•** `error` —If an error is returned, details about that error. This field is an Apex-defined variable of class
[ConnectApi.ErrorResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)

**–** `errorCode` —Error code.

**–** `message` —More detail, if available.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `gatewayResponse` —Response from the payment gateway. This field is an Apex-defined variable of
[class ConnectApi.AuthorizationGatewayResponse, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_authorization_gateway_response.htm)

**–** `gatewayAuthorizationCode` —Payment authorization code.

**•** `paymentAuthorization` —Details about the payment authorization. This field is an Apex-defined
[variable of class ConnectApi.PaymentAuthorizationResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_authorization_output.htm)

**–** `accountId` —ID of the account that contains the payment transaction being authorized.

**–** `amount` —Amount that the gateway authorized for the payment transaction.

**–** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group
record.

**–** `effectiveDate` —Date that the authorization becomes effective.

**–** `expirationDate` —Date that the authorization expires.

**–** `id` —ID of the payment authorization record.

**–** `paymentAuthorizationNumber` —System-defined number for the payment authorization
record.

**–** `requestDate` —Date that the authorization occurred.

**–** `status` —Status of the payment authorization as returned by the gateway.

**•** `paymentGatewayLogs` —Payment gateway log information about the authorization transaction.
[This field is a list of Apex-defined variables of class ConnectApi.GatewayLogResponse, each of which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_gateway_log_output.htm)
includes these fields:

**–** `createdDate` —Date when the gateway log was created.

**–** `gatewayResultCode` —Result codes that show the status of a transaction as it is passed to the
financial institution and then returned to the client.

**–** `id` —ID of the gateway log record.

**–** `interactionStatus` —Gateway interaction status. It can be `SUCCESS`, `FAILED`, or `TIMEOUT` .

**•** `paymentGroup` —Details about the payment group. This field is an Apex-defined variable of class
[ConnectApi.PaymentGroupResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_group.htm)

**–** `currencyIsoCode` —Three-letter ISO 4217 currency code associated with the payment group
record.

**–** `id` —ID of the payment group record.

**–** `sourceObjectId` —Source object ID of the payment group record.

**•** `paymentMethod` —Details about the payment method. This field is an Apex-defined variable of class
[ConnectApi.PaymentMethodResponse, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_payment_method_output.htm)

**–** `accountId` —ID of the account for the payment method.

**–** `id` —ID of the payment method.

**–** `status` —Status of the payment method.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

Use this action in custom flows that require payment authorization, such as adding an item to an order or an uneven exchange. Before
using it, verify with your payment provider that it supports payment authorization calls from Salesforce Order Management.

Flow Core Action for Order Management: Cancel Fulfillment Order Item

Cancel fulfillment order products from a fulfillment order. You can cancel more than one product
and specify a quantity to cancel for each of them. This action doesn’t cancel the associated order
product summaries, it only reduces their allocated quantities. Usually, you reallocate the canceled
quantities to a new fulfillment order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Fulfillment Order Item .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Cancel`

```
Fulfillment

Order Items

Input

```

[This input is an Apex-defined variable of class ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order_line_items_to_cancel.htm)

The variable has one field, `fulfillmentOrderLineItemsToCancel`, which is a list of Apex-defined
[variables of class ConnectApi.FulfillmentOrderLineItemInputRepresentation. Each of those variables includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order_line_item.htm)
these fields:

**•** `fulfillmentOrderLineItemId` - Reference to the fulfillment order product to cancel.

**•** `quantity` - Quantity to cancel.

`Fulfillment` Reference to the fulfillment order that you want to cancel fulfillment order items from.

```
Order Id

```

Store Output Values

**Output Parameter** **Description**

###### `Cancel`

```
Fulfillment

Order Items

Output

```

Usage

This value is an Apex-defined variable of class
[ConnectApi.FulfillmentOrderCancelLineItemsOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_cancel_line_items_output.htm)

This action doesn’t return any data.

To set up the Cancel Fulfillment Order Items Input, first use Assignment elements to set the `fulfillmentOrderLineItemId`
and `quantity` field values on one or more `ConnectApi.FulfillmentOrderLineItemInputRepresentation`
variables. Then use an Assignment element to add those variables to the `FulfillmentOrderLineItemsToCancel` field on


Automate Your Business Processes with Salesforce Flow Flow Reference

a `ConnectApi.FulfillmentOrderLineItemsToCancelInputRepresentation` variable. Use that variable in the
action input.

SEE ALSO:

Add and Edit Elements

Add and Edit Elements

Flow Core Action for Order Management: Cancel Order Item Summaries Preview

Preview the expected results of canceling one or more order product summaries from an order
summary without executing the cancel. The output of this action contains the values that would
be set on the change order created by submitting the proposed cancel.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Cancel`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not
including tax. Tax is calculated on the value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is
`amount` divided by 100 and then multiplied by the `TotalPrice`
and `TotalTaxAmount` of the associated order product summary,
prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount
is `amount` divided by 100 and then multiplied by the
`TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to cancel. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to cancel.

**•** `reason` —Required. Cancel reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

`Order Summary` Reference to the order summary that you want to preview canceling order product summaries from.

```
   Id

```

Store Output Values

**Output Parameter** **Description**

```
Cancel Order

Product

Summary Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed cancel.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Cancel Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for canceling order product summaries, display the output of this action for the user to review before executing the cancel.
When the user verifies the expected results, pass the same input to a Cancel Order Item Summaries Submit action.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Cancel Order Item Summaries Submit

Cancel one or more order product summaries from an order summary. This action creates a change
order record.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Cancel Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Cancel Order

Product

Summary Items

Input

```

[This input is an Apex-defined variable of class ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemInputRepresentation. Each variable includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)

**–** `amount` —Required. Value used to calculate the fee amount, as described by the amountType. It must
be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated. It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not including tax. Tax is calculated on the
value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is `amount` divided by 100 and then
multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated order product
summary, prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount is `amount` divided by 100
and then multiplied by the `TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to cancel. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to cancel.

**•** `reason` —Required. Cancel reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

`Order Summary` Reference to the order summary that you want to cancel order product summaries from.

```
Id

```

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Cancel Order

Product

Summary Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.SubmitCancelOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_submit_cancel_output.htm)

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

The `changeOrderId` field is the ID of the change order record created for the canceled items. Use this
change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for any cancel fees. Use this
change order to create an invoice.

To set up the Cancel Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for canceling order product summaries, run a Cancel Order Item Summaries Preview action before running the action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

SEE ALSO:

Flow Core Action for Order Management: Cancel Order Item Summaries Preview

Add and Edit Elements

###### Flow Core Action for Order Management: Cancel Order Summary Preview

Preview the expected results of canceling all order product summaries for an order summary without
executing the cancel. The output of this action contains the values that would be set on the change
order created by submitting the proposed cancel.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Cancel Order Summary Preview** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Cancel

All Order

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CancelAllOrderItemsInputRepresentation, which contains details](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_cancel_all_order_items.htm)
about the order summary to preview canceling all order products for.

The `changeItemFees` field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeWithTaxInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_change_item_fee_with_tax.htm)
includes these fields:

**•** `amount` —Positive value used to calculate the fee amount.

**•** `changeItemFees` —List of taxes associated with the change item fees.

**•** `description` —Description of the fee.

**•** `orderDeliveryGroupSummaryId` —ID of the order delivery group
summary.

**•** `priceBookEntryId` —ID of the price book entry associated with the
fee product.

**•** `product2Id` —ID of the product representing the fee.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `reason` —Reason for the cancellation. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

The `excludedItems` field is a list of items to exclude from the cancellation preview.

The `orderSummaryId` field is the ID of the order summary to preview canceling all order products summaries
for.

The `reason` field is the reason for the cancellation. The value must match one of the picklist values on the
Reason field of the Order Product Summary Change object.

The `reasonText` field is the reason text used for the return insights. The value has a max of 255 characters.

Store Output Values

**Output Parameter** **Description**

```
Preview Cancel

Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed cancel.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund but isn’t associated
with an invoice or credit memo. Excess funds normally occur when order products are canceled before
fulfillment but after payment is captured. This situation isn’t common in the US, where funds are normally
authorized but not captured until the fulfillment process begins. This value includes all excess funds related
to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the cancellation.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the cancellation.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Cancel All Order Items Input:

**1.** Use Assignment elements to set the `amount`, `amountType`, `changeItemFees`, `description`,
`orderDeliveryGroupSummaryId`, `priceBookEntryId`, `product2Id`, and `reason` field values on one or more
`ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables.

**2.** Use an Assignment element to add the `ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables to
the `changeItemFees` field on a `ConnectApi.CancelAllOrderItemsInputRepresentation` variable.

**3.** Use the `ConnectApi.CancelAllOrderItemsInputRepresentation` variable and the order summary ID in the
action input.

In a flow for canceling all product summaries for an order, display the output of this action for the user to review before executing the
cancel. When the user verifies the expected results, pass the same input to a Cancel Order Summary Submit action.

###### Flow Core Action for Order Management: Cancel Order Summary Submit

Cancel all order product summaries for an order summary. This action inserts a background operation
into an asynchronous job queue and returns the ID of that operation.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Cancel Order Summary Submit** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Cancel

All Order

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CancelAllOrderItemsInputRepresentation, which contains details](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_cancel_all_order_items.htm)
about the order summary to preview canceling all order products for.

The `changeItemFees` field is a list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeWithTaxInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_input_change_item_fee_with_tax.htm)
includes these fields:

**•** `amount` —Positive value used to calculate the fee amount.

**•** `changeItemFees` —List of taxes associated with the change item fees.

**•** `description` —Description of the fee.

**•** `orderDeliveryGroupSummaryId` —ID of the order delivery group
summary.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `priceBookEntryId` —ID of the price book entry associated with the fee product.

**•** `product2Id` —ID of the product representing the fee.

**•** `reason` —Reason for the cancellation. The value must match one of the picklist values on the Reason
field of the Order Product Summary Change object.

The `excludedItems` field is a list of items to exclude from the cancellation preview.

The `orderSummaryId` field is the ID of the order summary to preview canceling all order products summaries
for.

The `reason` field is the reason for the cancellation. The value must match one of the picklist values on the
Reason field of the Order Product Summary Change object.

The `reasonText` field is the reason text used for the return insights. The value has a max of 255 characters.

Store Output Values

**Output Parameter** **Description**

`Cancel All` [This output is an Apex-defined variable of class ConnectApi.CancelAllOrderItemsAsyncOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_connectapi_output_cancel_all_order_items_async_output.htm)
`Order Items` which contains the ID of the asynchronous background operation.

```
   Async Output

```

Usage

To set up the Cancel All Order Items Input:

**1.** Use Assignment elements to set the `amount`, `amountType`, `changeItemFees`, `description`,
`orderDeliveryGroupSummaryId`, `priceBookEntryId`, `product2Id`, and `reason` field values on one or more
`ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables.

**2.** Use an Assignment element to add the `ConnectApi.ChangeItemFeeWithTaxInputRepresentation` variables to
the `changeItemFees` field on a `ConnectApi.CancelAllOrderItemsInputRepresentation` variable.

**3.** Use the `ConnectApi.CancelAllOrderItemsInputRepresentation` variable and the order summary ID in the
action input.

In a flow for canceling all product summaries for an order, run a Cancel Order Summary Preview action before running this action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action. When the action
completes, it generates OSAsyncChgCompletedEvent if successful and ProcessExceptionEvent if not.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Confirm Held Fulfillment Order Capacity

Confirm held fulfillment order capacity at one or more locations. This action decreases a location’s
held capacity and increases its assigned fulfillment order count. Confirm held capacity when you
assign a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Confirm Held Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.ConfirmHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_confirm_held_f_o_capacity_request.htm)
these fields:

###### Confirm This input is an Apex-defined variable of class

`Held` [ConnectApi.ConfirmHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_confirm_held_f_o_capacity_request.htm)
`Fulfillment` these fields:

```
Order
```

**•** `allOrNothing` —(Optional) Controls whether a single failed request
```
Capacity
```
cancels all other requests in the list ( _`true`_ ) or some requests can succeed
```
Input
```
if others fail ( _`false`_ ). The default value is _`false`_ .

```
Capacity

Input

```

**•** `capacityRequests` —This field is a list of Apex-defined variables of
[class ConnectApi.CapacityRequestInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
represents a request to confirm one fulfillment order assigned to one location,
and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can
be a UUID. To identify which requests succeeded or failed, use the action
request IDs in response data.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.

**Output Parameter** **Description**

###### Confirm Held This output is an Apex-defined variable of class

`Fulfillment` [ConnectApi.ConfirmHeldFOCapacityResponseOutputRepresentation, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_confirm_held_f_o_capacity_response_output.htm)

```
Order Capacity
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class

`Output` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Credit Memo

Create a credit memo to represent the refund for one or more change orders associated with an
order summary.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Credit Memo .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Credit

Memo

Input

```

This input is an Apex-defined variable of class
[ConnectApi.CreateCreditMemoInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_credit_memo.htm)

The variable has one field, `changeOrderIds`, which is a list of IDs of the
change orders to create a credit memo for.

`Order` Reference to the order summary associated with the change orders.

```
Summary

Id

```

Store Output Values

**Output Parameter** **Description**

```
Credit Memo

Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.CreateCreditMemoOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_create_credit_memo_output.htm)

The `creditMemoId` field contains the ID of the created credit memo.

To set up the Credit Memo Input, first use Assignment elements to add the change order IDs to a list of strings variable. Then use that
variable in the action input.

SEE ALSO:

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Fulfillment Order

Create one or more fulfillment orders and fulfillment order products for an order delivery group
summary, which defines a recipient and delivery method. You specify the order product summaries
to fulfill and the fulfillment locations to handle them. If you specify multiple fulfillment locations, a
fulfillment order is created for each one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Fulfillment Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Fulfillment

Order

Input

```

This input is an Apex-defined variable of class
[ConnectApi.FulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)

The variable has three fields:

**•** `fulfillmentGroups` - A list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupInputRepresentation. A fulfillment order is](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
created for each fulfillment group. A group represents a set of order product
summaries to fulfill from a single location, using the same fulfillment type.
Each fulfillment group variable has these fields:

**–** `fulfilledFromLocationId`  - Reference to the fulfillment
location.

**–** `fulfillmentType`  - The fulfillment type. Specify one of the values
that you defined for the `Type` field picklist on the Fulfillment Order
object.

**–** `orderItemSummaries`  - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)
these fields:

**•** `orderItemSummaryId`    - Reference to an order product
summary.

**•** `quantity`    - The quantity of the order product summary to
allocate to the fulfillment order.

**–** `referenceId`  - Reference to the fulfillment group input. This action
doesn’t use this value.

**•** `orderDeliveryGroupSummaryId` - Reference to the order delivery
group summary associated with the order product summaries.

**•** `orderSummaryId` - Reference to the order summary associated with
the order product summaries.

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Fulfillment

Order Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.FulfillmentOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_output.htm)

The `fulfillmentOrderIds` field is a list of IDs of the created fulfillment orders.

To set up the Fulfillment Order Input:

**1.** Use Assignment elements to set the `orderItemSummaryId` and `quantity` field values on one or more
`ConnectApi.OrderItemSummaryInputRepresentation` variables for each fulfillment group.

**2.** Use Assignment elements to add the `ConnectApi.OrderItemSummaryInputRepresentation` variables to the
`orderItemSummaries` fields on one or more `ConnectApi.FulfillmentGroupInputRepresentation` variables,
one for each fulfillment group.

**3.** Use Assignment elements to set the `fulfilledFromLocationId` and `fulfillmentType` field values on the fulfillment
group variables.

**4.** Use Assignment elements to add the fulfillment group variables to the `fulfillmentGroups` field on a
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**5.** Use Assignment elements to set the `orderDeliveryGroupSummaryId` and `orderSummaryId` field values on the
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**6.** Use the `ConnectApi.FulfillmentOrderInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Create Fulfillment Orders

Create fulfillment orders and fulfillment order products for multiple order delivery group summaries,
each of which defines a recipient and delivery method. You specify the order product summaries
to fulfill and the fulfillment locations to handle them. If you specify multiple fulfillment locations
for one order delivery group summary, a fulfillment order is created for each one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Fulfillment Orders .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Fulfillment

Orders

Input

```

This input is an Apex-defined variable of class
[ConnectApi.MultipleFulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_multiple_fulfillment_order.htm)

The variable has one field: `fulfillmentOrders` . This field is a list of
[Apex-defined variables of class ConnectApi.FulfillmentOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
Each variable has three fields:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `fulfillmentGroups`            - A list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupInputRepresentation. A fulfillment order is created for each fulfillment group.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_fulfillment_order.htm)
A group represents a set of order product summaries to fulfill from a single location using the same fulfillment
type. Each fulfillment group variable has these fields:

**–** `fulfilledFromLocationId`              - Reference to the fulfillment location.

**–** `fulfillmentType`              - The fulfillment type. Specify one of the values that you defined for the
`Type` field picklist on the Fulfillment Order object.

**–** `orderItemSummaries`              - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)

**•** `orderItemSummaryId`               - Reference to an order product summary.

**•** `quantity`               - The quantity of the order product summary to allocate to the fulfillment order.

**–** `referenceId`              - Reference to the fulfillment group input. Use this value to troubleshoot a failure.

**•** `orderDeliveryGroupSummaryId`            - Reference to the order delivery group summary associated
with the order product summaries.

**•** `orderSummaryId`            - Reference to the order summary associated with the order product summaries.

Store Output Values

**Output Parameter** **Description**

```
Fulfillment

Orders Output

```

[This value is an Apex-defined variable of class ConnectApi.MultipleFulfillmentOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_multiple_fulfillment_order_output.htm)

The variable has one field: `fulfillmentOrders` . This field is a list of Apex-defined variables of class
[ConnectApi.FulfillmentGroupOutputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_group_output.htm)

**•** `fulfilledFromLocationId` - Reference to the fulfillment location. This value is included so that
you can resubmit the creation if it fails.

**•** `fulfillmentOrderId` - Reference to the created fulfillment order.

**•** `fulfillmentType` - The fulfillment type. This value is included if the creation failed, so you can
resubmit it.

**•** `orderDeliveryGroupSummaryId` - Reference to the order delivery group summary associated
with the order product summaries. This value is included if the creation failed, so you can resubmit it.

**•** `orderItemSummaries` - A list of Apex-defined variables of class
[ConnectApi.OrderItemSummaryInputRepresentation. This value is included if the creation failed, so you](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_item_summary.htm)
can resubmit it. Each variable has these fields:

**–** `orderItemSummaryId`  - Reference to an order product summary.

**–** `quantity`  - The quantity of the order product summary to allocate to the fulfillment order.

**•** `orderSummaryId` - Reference to the order summary associated with the order product summaries.
This value is included if the creation failed, so you can resubmit it.

**•** `referenceId` - Reference to the fulfillment group input. Use this value to troubleshoot a failure.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

To set up the Fulfillment Orders Input:

**1.** For each order delivery group:

**a.** Use Assignment elements to set the `orderItemSummaryId` and `quantity` field values on one or more
`ConnectApi.OrderItemSummaryInputRepresentation` variables.

**b.** Use Assignment elements to add the `ConnectApi.OrderItemSummaryInputRepresentation` variables to the
`orderItemSummaries` fields on one or more `ConnectApi.FulfillmentGroupInputRepresentation`
variables, one for each fulfillment group.

**c.** Use Assignment elements to set the `fulfilledFromLocationId`, `fulfillmentType`, and `referenceId` field
values on the `ConnectApi.FulfillmentGroupInputRepresentation` variables.

**d.** Use Assignment elements to add the `ConnectApi.FulfillmentGroupInputRepresentation` variables to the
`fulfillmentGroups` field on a `ConnectApi.FulfillmentOrderInputRepresentation` variable.

**e.** Use Assignment elements to set the `orderDeliveryGroupSummaryId` and `orderSummaryId` field values on the
`ConnectApi.FulfillmentOrderInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.FulfillmentOrderInputRepresentation` variables to the
`fulfillmentOrders` field on a `ConnectApi.MultipleFulfillmentOrderInputRepresentation` variable.

**3.** Use the `ConnectApi.MultipleFulfillmentOrderInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Create an Invoice from Change Orders

Create an invoice to represent the charges for one or more change orders. Create invoices for change
orders that increase order amounts, such as return fees. When you ensure the refund for a return,
include the invoices for the associated return fees in the input.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create an Invoice from Change Orders .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Required. This input is an Apex-defined variable of class
[ConnectApi.CreateInvoiceFromChangeOrdersInputRepresentation. It has two](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_invoice_from_change_orders.htm)
fields.

###### Create Required. This input is an Apex-defined variable of class

`Invoice` [ConnectApi.CreateInvoiceFromChangeOrdersInputRepresentation. It has two](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_invoice_from_change_orders.htm)
`From` fields.

```
Change
```

The `changeOrderIds` field is a list of IDs of the change orders to create an

`Order` invoice for.
```
Input
```

The `orderSummaryId` field is the ID of the order summary associated with
the change orders.

The `changeOrderIds` field is a list of IDs of the change orders to create an
invoice for.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
Invoice Output

```

SEE ALSO:

[This value is an Apex-defined variable of class ConnectApi.ChangeOrdersInvoiceOutputRepresentation. It has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_orders_invoice_output.htm)
three fields.

The `errors` [field is a list of Apex-defined variables of class ConnectApi.ErrorResponse containing any errors](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
that were returned.

The `invoiceId` field contains the ID of the created invoice.

The `success` field indicates whether the transaction was successful.

Flow Core Action for Order Management: Create Return Order

Flow Core Action for Order Management: Return Return Order Items

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order

Create an invoice for a fulfillment order that doesn’t have one.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create an Invoice from Fulfillment Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Fulfillment` Reference to the fulfillment order that needs an invoice.

```
Order Id

```

Store Output Values

**Output Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Invoice

creation

output

```

SEE ALSO:

[This value is an Apex-defined variable of class ConnectApi.FulfillmentOrderInvoiceOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_fulfillment_order_invoice_output.htm)

The `invoiceId` field contains the ID of the created invoice.

Flow Core Action for Order Management: Ensure Funds Async

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Order Payment Summary

Create an order payment summary for a payment authorization or payments that use the same
payment method and are attached to the same order summary.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Order Payment Summary .

Set Input Values

Use values from earlier in the flow to set the inputs. Include at least one payment authorization or
list of payments. You don’t need both.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.CreateOrderPaymentSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_order_payment_summary.htm)

`Order` This input is an Apex-defined variable of class
`Payment` [ConnectApi.CreateOrderPaymentSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_create_order_payment_summary.htm)
`Summary` The variable includes these fields:
###### `Create`

**•** `orderSummaryId`       - Reference to the order summary associated with
```
Input
```
the payments. In orgs with the multicurrency feature enabled, the order
payment summary inherits the `ISO Currency` value from the order
summary.

The variable includes these fields:

**•** `paymentAuthorizationId`       - Reference to the payment
authorization to associate with the summary.

**•** `paymentIds`       - List of IDs of the payments to associate with the summary.

Store Output Values

**Output Parameter** **Description**

```
Order Payment

Summary Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.CreateOrderPaymentSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_create_order_payment_summary_output.htm)

The `orderPaymentSummaryId` field contains the ID of the created order payment summary.

To set up the Order Payment Summary Create Input for payments, first use Assignment elements to add the payment IDs to a list of
strings variable. Then use that variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Create Order Summary

Create an order summary based on an order. That order is considered the original order for the
order summary. Subsequent change orders that apply to the order summary are also represented
as order records.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Order Summary .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Order

Summary

###### `Create`

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OrderSummaryInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_order_summary.htm)

The variable has these fields:

**•** `businessModel` —The order’s business model. It can have one of these
values:

**–** B2B

**–** B2C

**•** `externalReferenceIdentifier` —Used to prevent duplicate
records. This value is case-sensitive.

**•** `name` —Order summary number to assign to the order summary.

**•** `orderId` —Required. The ID of the original order to create an order
summary for.

**•** `orderLifeCycleType` —Specifies whether the order is managed in
Salesforce Order Management or by an external system. It can have one of
these values:

**–** _`MANAGED`_ —The order is managed in Salesforce Order Management. If
no value is specified, the default is _`MANAGED`_ .

**–** _`UNMANAGED`_ —The order is managed by an external system.

**•** `sourceProcess` —Describes the order process creating the order
summary. It can have one of these values:

**–** _`OrderOnBehalf`_ —An Order on Behalf Of process.

**–** _`Standard`_ —Any process other than Order on Behalf Of.

**•** `status` —Status to assign to the order summary. The value must match
one of the picklist values on the `Status` field of the Order Summary object.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
Order Summary

Output

```

SEE ALSO:

[This value is an Apex-defined variable of class OrderSummaryOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_order_summary_output.htm)

The `orderSummaryId` field contains the ID of the created order summary.

Add and Edit Elements

Flow Core Action for Order Management: Create Return Order

Create a return order and return order items for order items belonging to an order summary. You
can add return fees for any of the order items.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Create Return Order .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management and
Returns

```
Return

Order

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ReturnOrderInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order.htm)

The variable has four fields:

**•** `orderSummaryId` —ID of the order summary containing the items to
be returned. The order summary’s order lifecycle type must be Managed.

**•** `returnOrderLifeCycleType` —The LifeCycleType of the return
order. Possible values are:

**–** _`Managed`_ —Process the return order using the actions and APIs. It can
generate change orders and affects financial fields and rollup calculations.

**–** _`Unmanaged`_ —The return order is for tracking purposes only. It isn’t
involved in any financial calculations and doesn’t generate any change
orders. The system doesn’t prevent the creation of duplicate return order
line items in an unmanaged return order for the same order item.

**•** `returnOrderLineItems` —A list of Apex-defined variables of class
[ConnectApi.ReturnOrderLineItemInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_line_item.htm)
these fields:

**–** `canReduceShipping` —Whether the associated shipping charge
can be refunded.

**–** `orderItemSummaryId` —ID of the associated OrderItemSummary.
If the OrderItemSummary already has an associated ReturnOrderLineItem,
then you must specify a different `reasonForReturn` . Duplicating
the reason breaks the financial calculations.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `quantityExpected` —Quantity expected to be returned.

**–** `quantityReceived` —(Optional) Quantity already physically returned. This value isn’t used by any
standard features, but it’s provided for use in customizations.

**–** `reasonForReturn` —(Optional) Reason for the return. The value must match an entry in the
ReturnOrderLineItem object’s ReasonForReturn picklist.

**–** `returnOrderLineItemFees` —(Optional) A list of Apex-defined variables of class
[ConnectApi.ReturnOrderLineItemFeeInputRepresentation. Each variable has these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_line_item_fee.htm)

**•** `amount` —Value used to calculate the fee amount, as described by the amountType. It must be a
positive value.

**•** `amountType` —Describes how the fee amount is calculated. It can have one of these values:

**–** _`AmountWithTax`_                - `amount` is the fee amount, including tax.

**–** _`AmountWithoutTax`_                - `amount` is the fee amount, not including tax. Tax is calculated on
the value and added.

**–** _`Percentage`_                - `amount` is a percentage. The fee amount is `amount` divided by 100 and
then multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated
OrderItemSummary, prorated for the quantity being returned.

**–** _`PercentageGross`_                - `amount` is a percentage. The fee amount is `amount` divided by
100 and then multiplied by the `TotalLineAmountWithTax` of the associated
OrderItemSummary, prorated for the quantity being returned.

**•** `description` —(Optional) Description of the fee.

**•** `product2Id` —ID of the product representing the fee.

**•** `reason` —Reason for the fee. The value must match an entry in the ReturnOrderLineItem object’s
`ReasonForReturn` picklist.

**•** `status` —Status to assign to the return order. The value must match one of the picklist values on the
Status field of the Return Order object.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Output

```

Usage

[This value is an Apex-defined variable of class ConnectApi.ReturnOrderOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_order_output.htm)

The `returnOrderId` field contains the ID of the created return order.

To set up the Create Return Order Input:

**1.** Use Assignment elements to set the `canReduceShipping`, `orderItemSummaryId`, `quantityExpected`,
`quantityReceived`, and `reasonForReturn` field values on one or more
`ConnectApi.ReturnOrderLineItemInputRepresentation` variables.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** If you want to add any return fees, use Assignment elements to set the `amount`, `amountType`, `description`, `product2Id`,
and `reason` field values on one or more `ConnectApi.ReturnOrderLineItemFeeInputRepresentation`
variables. The `product2Id` points to a fee product that you created.

**3.** Use Assignment elements to add the `ConnectApi.ReturnOrderLineItemFeeInputRepresentation` variables
to the `returnOrderLineItemFees` fields on the `ConnectApi.ReturnOrderLineItemInputRepresentation`
variables representing the associated return order items.

**4.** Use an Assignment element to add the `ConnectApi.ReturnOrderLineItemInputRepresentation` variables to
the `returnOrderLineItems` field on a `ConnectApi.ReturnOrderInputRepresentation` variable.

**5.** Use Assignment elements to set the `orderSummaryId`, `returnOrderLifeCycleType`, and `status` field values on
the `ConnectApi.ReturnOrderInputRepresentation` variable.

**6.** Use the `ConnectApi.ReturnOrderInputRepresentation` variable in the action input.

SEE ALSO:

Flow Core Action for Order Management: Return Return Order Items

Add and Edit Elements

Flow Core Action for Order Management: Ensure Funds Async

Ensure funds for an invoice, and apply them to it. If needed, capture authorized funds by sending
a request to a payment provider. This action inserts a background operation into an asynchronous
job queue and returns the ID of that operation so you can track its status. Payment gateway responses
appear in the payment gateway log and don’t affect the background operation status.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Ensure Funds Async .

Note: If the action creates a payment, the payment record’s ClientContext value isn’t
predictable. Don't use it in custom logic.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Ensure Funds`

```
Async Input

```

[This input is an Apex-defined variable of class ConnectApi.EnsureFundsAsyncInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_ensure_funds_async.htm)

The variable has one field: `invoiceId`, which is the ID of the invoice to ensure funds for and apply them to.

`Order Summary` Reference to the order summary associated with the invoice.

```
Id

```

Store Output Values

**Output Parameter** **Description**

###### `Ensure Funds`

```
Async Output

```

[This value is an Apex-defined variable of class EnsureFundsAsyncOutputRepresentation. It only returns the ID](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_ensure_funds_async_output.htm)
of the asynchronous background operation, regardless of whether a call is made to an external payment
gateway. It doesn’t include any errors from the operation.

The `backgroundOperationId` field contains the ID of the background operation.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

This action applies funds to the invoice balance from order payment summaries associated with the specified order summary following
this logic:

Note: If multiple order payment summaries have equal `BalanceAmount` values, their order of selection is random.

**1.** Verify that the invoice balance doesn’t exceed the total `BalanceAmount` of all the order payment summaries associated with
the order summary.

**2.** If an order payment summary has a `BalanceAmount` equal to the invoice balance, apply the funds from that order payment
summary.

**3.** If no exact match was found, apply funds from the order payment summary with the largest `BalanceAmount` .

**4.** If the invoice still has a balance to ensure, repeat steps 2 and 3 until the full balance is ensured or no captured funds remain.

**5.** If the invoice still has a balance, look for an order payment summary with an authorized amount equal to the remaining invoice
balance. If one exists, capture and apply the funds from that order payment summary.

**6.** If no exact match was found, capture and apply funds from the order payment summary with the largest authorized amount.

**7.** If the invoice still has a balance to ensure, repeat steps 5 and 6 until the full balance is ensured.

SEE ALSO:

Flow Core Action for Order Management: Create an Invoice from Fulfillment Order

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

Flow Core Action for Order Management: Ensure Refunds Async

Ensure refunds for a credit memo or excess funds by sending a request to a payment provider. This
action inserts a background operation into an asynchronous job queue and returns the ID of that
operation so you can track its status. Payment gateway responses appear in the payment gateway
log and don’t affect the background operation status.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Ensure Refunds Async .

Note: If the action creates a refund, the refund record’s ClientContext value isn’t predictable.
Don't use it in custom logic.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Ensure`

```
Refunds Async

Input

```

[This input is an Apex-defined variable of class ConnectApi.EnsureReundsAsyncInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_ensure_refunds_async.htm)

The variable has these fields. You must specify `creditMemoId` or `excessFundsAmount` . You can
specify both.

**•** `creditMemoId` —The ID of the credit memo to ensure refunds for.

**•** `excessFundsAmount` —The amount of excess funds to apply the refunds against.

**•** `invoicesToPay` —List of invoices for fees that reduce the refund, such as return fees.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `isAllowPartial` —This value controls the behavior when the amounts included in the `sequences`
list don’t cover the entire refund amount. If this value is false, the default refund logic is applied to ensure
the remaining refund amount. If this value is true, the unrefunded balance remains on the credit memo. If
you don’t specify a `sequences` list, this value is ignored, and the default refund logic is applied. The
default is false.

**•** `sequences` —This input is an ordered list of refund amounts and the OrderPaymentSummaries to apply
them to. The process traverses this list in order and stops when it has refunded the full amount. It’s a list of
Apex-defined variables of class SequenceOrderPaymentSummaryInputRepresentation. It contains these
fields:

**–** `amount` —Amount of the refund to apply to the OrderPaymentSummary.

**–** `orderPaymentSummaryId` —ID of the OrderPaymentSummary to apply the Amount to.

`Order Summary` Reference to the order summary associated with the credit memo.

```
   Id

```

Store Output Values

**Output Parameter** **Description**

```
Ensure Refunds

Async Output

```

Usage

[This value is an Apex-defined variable of class EnsureRefundsAsyncOutputRepresentation. It only returns the](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_ensure_refunds_async_output.htm)
ID of the asynchronous background operation, regardless of whether a call is made to an external payment
gateway. It doesn’t include any errors from the operation.

The `backgroundOperationId` field contains the ID of the background operation.

This action applies the refund to order payment summaries associated with the specified order summary following this logic.

Note: If multiple order payment summaries have equal `AvailableToRefund` amounts, their order of selection is random.

**1.** Verify that the credit memo balance and excess funds amount don't exceed the total `AvailableToRefund` amount of all the
order payment summaries associated with the order summary.

**2.** If `sequences` is specified, follow these steps.

**a.** Traverse the `sequences` list in order and apply the specified refund amounts to the specified order payment summaries.

**b.** If the specified credit memo and excess funds are fully refunded, or if `isAllowPartial` is true, then the action stops here.

**3.** If a credit memo is specified, follow these steps.

**a.** If an order payment summary has an `AvailableToRefund` amount matching the credit memo’s remaining balance, apply
the refund to that payment.

**b.** If no exact match was found, apply the refund to the order payment summary with the largest `AvailableToRefund`
amount.

**c.** If the credit memo has any remaining balance, repeat steps a and b until that balance is fully refunded.

**4.** If only one OrderPaymentSummary is specified but has multiple payments, follow these steps.


Automate Your Business Processes with Salesforce Flow Flow Reference

**a.** If a payment has an amount matching the CreditMemo’s remaining balance, apply the refund to that payment.

**b.** If no exact match was found but one or more payment has a large enough amount to cover the balance, use the payment with
the smallest amount.

**c.** If no single payment has a large enough amount, use multiple payments in descending order of amount. This ensures the fewest
payments are used.

**5.** If an excess funds amount is specified, follow these steps.

**a.** Examine those order payment summaries. If one has an `AvailableToRefund` amount matching the excess funds amount,
apply the refund to that payment.

**b.** If no exact match was found, apply the refund to the order payment summary with the largest `AvailableToRefund`
amount.

**c.** If any excess funds amount remains, repeat steps a and b until it’s fully refunded.

SEE ALSO:

Flow Core Action for Order Management: Create Credit Memo

Flow Core Action for Order Management: Create an Invoice from Change Orders

Flow Core Action for Order Management: Return Return Order Items

Flow Core Action for Order Management: Ensure Funds Async

Add and Edit Elements

Flow Core Action for Order Management: Find Routes with Fewest Splits

Evaluate ordered product quantities against available inventory to determine the smallest
combination of locations that can fulfill the order. If multiple combinations of the minimum number
of locations can fulfill the order, the action returns multiple options. Optionally, you can specify a
maximum allowable number of locations. By default, the action executes up to 1,000,000 times,
stopping when it hits 10,000 results.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Find Routes With Fewest Splits** .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

```
Order Routing

Minimize

Shipments

Input

```

[This input is an Apex-defined variable of class ConnectApi.FindRoutesWithFewestSplitsInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits.htm)

The `locationAvailableInventory` field is a list of Apex-defined variables of class
[ConnectApi.LocationAvailabilityInputRepresentation. Each of the variables represents a fulfillment location to](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_location_availability.htm)
consider and includes these fields:

**•** `externalReferenceId` - External reference ID of the inventory location.

**•** `quantity` - Available quantity of the product.

**•** `stockKeepingUnit` - Stock Keeping Unit (SKU) of the product.

The `maximumNumberOfSplits` field is the maximum allowable number of shipment splits. The action
doesn’t return routing options that involve more than this number of splits.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

Each split represents an additional shipment. Specifying a maximum of 0 returns only locations that can fulfill
the entire order in a single shipment. A maximum of 1 returns combinations of locations that can fulfill the
order in one or two shipments, and so on.

The `orderedQuantities` field is a list of Apex-defined variables of class
[ConnectApi.QuantityWithSkuInputRepresentation. Each of the variables represents an ordered product quantity](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_quantity_with_sku.htm)
to fulfill, and includes these fields:

**•** `quantity`            - Ordered quantity of the product.

**•** `stockKeepingUnit`            - SKU of the product.

Store Output Values

**Output Parameter** **Description**

```
Order Routing

Minimize

Shipments

Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.FindRoutesWithFewestSplitsOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_output.htm)
which contains the sets of fulfillment locations that meet the requirements.

The variable has one field: `targetLocations` . This field is a list of Apex-defined variables of class
[ConnectApi.AvailableLocationOutputRepresentation, each of which represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_available_location_output.htm)
that can combine to fulfill the ordered products.

Each of the variables includes one field: `locations` . This field is a list of the locations in the set.

To set up the Order Routing Minimize Shipments Input:

**1.** Use Assignment elements to set the `externalReferenceId`, `quantity`, and `stockKeepingUnit` field values on one
or more `ConnectApi.LocationAvailabilityInputRepresentation` variables.

**2.** Use Assignment elements to set the `quantity` and `stockKeepingUnit` field values on one or more
`ConnectApi.QuantityWithSkuInputRepresentation` variables.

**3.** Use an Assignment element to add the `ConnectApi.LocationAvailabilityInputRepresentation` variables to
the `locationAvailableInventory` field on a
`ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable.

**4.** Optionally, use an Assignment element to set the `maximumNumberOfSplits` field on the
`ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable.

**5.** Use an Assignment element to add the `ConnectApi.QuantityWithSkuInputRepresentation` variables to the
`orderedQuantities` field on the `ConnectApi.FindRoutesWithFewestSplitsInputRepresentation`
variable.

**6.** Use the `ConnectApi.FindRoutesWithFewestSplitsInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Use OCI to Find Routes with Fewest Splits

Evaluate ordered product quantities against available inventory to determine the smallest
combination of locations that can fulfill the order. If multiple combinations of the minimum number
of locations can fulfill the order, the action returns multiple options. Optionally, you can specify a
maximum allowable number of locations and a list of locations to exclude from the calculation.
This action combines the Omnichannel Inventory Get Availability action and the Order Management
Find Routes with Fewest Splits actions. Instead of calling Get Availability and including the output
in the Find Routes with Fewest Splits input, call this action and specify a location or location group
to fulfill each ordered product. By default, this action executes up to 1,000,000 times, stopping when
it hits 10,000 results. This action handles the inventory check.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
search for **Find Routes With Fewest Splits Using OCI** .

Note: Set the flow’s runtime API version to 54.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Find Routes`

```
With Fewest

Splits Using

OCI Input

```

Store Output Values

This input is an Apex-defined variable of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_using_o_c_i.htm)

The `findRoutesWithFewestSplitsUsingOCIInputs` field is a list of Apex-defined variables of
[class ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_group_using_o_c_i.htm)
represents one order and includes these fields:

**•** `excludeLocations` —List of locations to exclude from the routing calculations.

**•** `maximumNumberOfSplits` —Maximum allowable number of shipment splits. The action doesn’t
return routing options that involve more than this number of splits.

Each split represents an additional shipment. Specifying a maximum of 0 returns only locations that can
fulfill the entire order in a single shipment. A maximum of 1 returns combinations of locations that can fulfill
the order in one or two shipments, and so on.

**•** `orderedItems` —A list of Apex-defined variables of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation. Each of the variables represents](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_find_routes_with_fewest_splits_using_o_c_i_item.htm)
an ordered product quantity to fulfill and a location or location group, and includes these fields:

**–** `locationGroupIdentifier` —External reference ID of the inventory location or location group.

**–** `quantity` —Ordered quantity of the product.

**–** `stockKeepingUnit` —Stock Keeping Unit (SKU) of the product.

Use output values later in the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Find Routes

With Fewest

Splits Using

OCI Output

```

Usage

This output is an Apex-defined variable of class
[ConnectApi.FindRoutesWithFewestSplitsUsingOCIOutputRepresentation, which contains inventory availability](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_using_o_c_i_output.htm)
data and the sets of fulfillment locations that meet the requirements.

The variable has one field: `results` . This field is a list of Apex-defined variables of class
[ConnectApi.FindRoutesWithFewestSplitsWithInventoryOutputRepresentation, each of which represents the](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_find_routes_with_fewest_splits_with_inventory_output.htm)
output for one order, and includes these fields:

**•** `inventory` —Inventory availability data for the location groups and locations specified in the input.

**•** `targetLocations` —A list of Apex-defined variables of class
[ConnectApi.AvailableLocationOutputRepresentation, each of which represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_available_location_output.htm)
that can combine to fulfill the ordered products. Each of the variables includes one field `locations` .
This field is a list of the locations in the set.

To set up the Find Routes With Fewest Splits Using OCI Input:

**1.** Use assignment elements to set the values for the `locationGroupIdentifier`, `quantity`, and `stockKeepingUnit`
field values on one or more ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation variables.

**2.** Use assignment elements to add the ConnectApi.FindRoutesWithFewestSplitsUsingOCIItemInputRepresentation variables to the
`orderedItems` field on a ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable.

**3.** Optionally, use an assignment element to set the value for the `maximumNumberOfSplits` field on the
ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable.

**4.** Use an assignment element to add the ConnectApi.FindRoutesWithFewestSplitsGroupUsingOCIInputRepresentation variable to the
`findRoutesWithFewestSplitsUsingOCIInputs` field on a
ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable.

**5.** Repeat steps 1–4 for each order that you want to include in the action, adding the inputs to the same
ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable.

**6.** Use the ConnectApi.FindRoutesWithFewestSplitsUsingOCIInputRepresentation variable in the action input.

Flow Core Action for Order Management: Get Fulfillment Order Capacity Values

Get information about the current fulfillment order capacity of one or more locations.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Get Fulfillment Order Capacity Values .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Get` [This input is an Apex-defined variable of class ConnectApi.GetFOCapacityValuesRequestInputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_get_f_o_capacity_values_request.htm)
`Fulfillment` which includes this field:

```
   Order
```

**•** `locationIds` —List of IDs of the locations to get fulfillment order capacity information for.
```
   Capacity

   Values Input

```

Store Output Values

Use output values later in the flow.

**Output Parameter** **Description**

`Get` [This output is an Apex-defined variable of class ConnectApi.GetFOCapacityValuesOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_get_f_o_capacity_values_output.htm)
`Fulfillment` includes this field:

```
   Order Capacity
```

**•** `locations` —This field is a list of Apex-defined variables of class

`Values Output` [ConnectApi.LocationCapacityOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_location_capacity_output.htm)

**–** `assigned` —Value of the location’s Assigned Fulfillment Order Count.

**–** `capacity` —Value of the location’s Fulfillment Order Capacity. This property represents the location’s
maximum capacity.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `heldCapacity` —Number of fulfillment orders that the location is holding capacity for.

**–** `locationId` —ID of the location.

Flow Core Action for Order Management: Hold Fulfillment Order Capacity

Hold capacity to process fulfillment orders at one or more locations. This action increases a location’s
held capacity. Hold capacity when you plan to assign a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Hold Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Hold` [This input is an Apex-defined variable of class ConnectApi.HoldFOCapacityRequestInputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_hold_f_o_capacity_request.htm)
`Fulfillment` includes these fields:

###### `Order`

**•** `allOrNothing` —(Optional) Controls whether a single failed request cancels all other requests in the
```
   Capacity
```
list ( _`true`_ ) or whether some requests can succeed if others fail ( _`false`_ ). The default value is _`false`_ .
```
   Input
```

**•** `capacityRequests` —This field is a list of Apex-defined variables of class
[ConnectApi.CapacityRequestInputRepresentation. Each of the variables represents a request to hold capacity](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
for one fulfillment order at one location, and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can be a UUID. Use the action
request IDs in response data to identify which requests succeeded or failed.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.

**Output Parameter** **Description**

`Hold` [This output is an Apex-defined variable of class ConnectApi.HoldFOCapacityResponseOutputRepresentation,](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_hold_f_o_capacity_response_output.htm)
`Fulfillment` which includes this field:

```
   Order Capacity
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class

`Output` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).

Flow Core Action for Order Management: Order Routing Rank by Average Distance

Calculate the average distance from sets of inventory locations to an order recipient, and return
the sets sorted by that average distance. Use this action to compare the average shipping distances
for different sets of locations that can fulfill an order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Order Routing Rank By Average Distance .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

[This input is an Apex-defined variable of class ConnectApi.RankAverageDistanceInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_rank_average_distance.htm)

`Order Routing` [This input is an Apex-defined variable of class ConnectApi.RankAverageDistanceInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_rank_average_distance.htm)

```
Rank By
```

The `deliveryCountryCode` field is the country code of the order recipient.
```
Average
```

The `deliveryPostalCode` field is the postal code of the order recipient.
```
Distance
```

`Input` The `distanceUnit` field specifies whether to return average distances in miles or kilometers, respectively.
The value can be _`mi`_ or _`km`_ .

The `deliveryCountryCode` field is the country code of the order recipient.

The `sortResult` field specifies whether to sort the location sets in ascending or descending order by average
distance. The value can be _`ASC`_ or _`DESC`_ .

The `targetLocations` field is a list of Apex-defined variables of class
[ConnectApi.TargetLocationInputRepresentation. Each of the variables represents a set of fulfillment locations](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_target_location.htm)
that can fulfill an order together, and includes one field: `locations` . This field is a list of Apex-defined variables
[of class ConnectApi.LocationInputRepresentation, each of which represents one location in the list and contains](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_location.htm)
these fields:

**•** `countryCode`         - Country code of the location.

**•** `locationIdentifier`         - ID of the location.

**•** `postalCode`         - Postal code of the location.

Store Output Values

**Output Parameter** **Description**

[This output is an Apex-defined variable of class ConnectApi.RankAverageDistanceOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_rank_average_distance_output.htm)
contains the list of fulfillment location sets, sorted by average distance to the order recipient.

`Order Routing` This output is an Apex-defined variable of class
`Rank By` contains the list of fulfillment location sets, sorted by average distance to the order recipient.

```
Average
```

The `distanceUnit` field is the specified unit of distance. It can be _`miles`_ or
```
Distance
```

The `results` field is a list of Apex-defined variables of class
```
Output
```
[ConnectApi.AverageDistanceResultOutputRepresentation, each of which includes one field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)
`distanceCalculation` . It’s an Apex-defined variable of class
[ConnectApi.DistanceCalculationOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_distance_calculation_output.htm)

The `distanceUnit` field is the specified unit of distance. It can be _`miles`_ or _`kilometers`_ .

**•** `averageDistance`          - Average distance from the locations to the order recipient.

**•** `locations` [— A list of Apex-defined variables of class ConnectApi.LocationOutputRepresentation, each](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_location_output.htm)
of which represents a location in the set and includes two fields:

**–** `distance`           - Distance from the location to the order recipient.

**–** `locationIdentifier`           - ID of the location.

**•** `rank`          - This result’s rank among all results by average distance to the order recipient.

Usage

To set up the Order Routing Rank By Average Distance Input:

**1.** Use Assignment elements to set the `countryCode`, `locationIdentifier`, and `postalCode` field values on one or
more `ConnectApi.LocationInputRepresentation` variables to represent the locations in a set.


Automate Your Business Processes with Salesforce Flow Flow Reference

**2.** Use an Assignment element to add the `ConnectApi.LocationInputRepresentation` variables to the `locations`
field on a `ConnectApi.TargetLocationInputRepresentation` variable.

**3.** Repeat the previous two steps for each set of fulfillment locations.

**4.** Use an Assignment element to add the `ConnectApi.TargetLocationInputRepresentation` variables to the
`targetLocations` field on a `ConnectApi.RankAverageDistanceInputRepresentation` variable.

**5.** Use Assignment elements to set the `deliveryCountryCode`, `deliveryPostalCode`, `distanceUnit`, and
`sortResult` field values on the `ConnectApi.RankAverageDistanceInputRepresentation` variable.

**6.** Use the `ConnectApi.RankAverageDistanceInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Order Management: Release Held Fulfillment Order Capacity

Release held fulfillment order capacity at one or more locations. This action decreases a location’s
held capacity without increasing its assigned fulfillment order count. Release held capacity when
you cancel assigning a fulfillment order to a location.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Release Held Fulfillment Order Capacity .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

This input is an Apex-defined variable of class
[ConnectApi.ReleaseHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_release_held_f_o_capacity_request.htm)
these fields:

`Fulfillment` This input is an Apex-defined variable of class
`Order` [ConnectApi.ReleaseHeldFOCapacityRequestInputRepresentation, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_release_held_f_o_capacity_request.htm)
`Location` these fields:

###### `Release`

**•** `allOrNothing` —(Optional) Controls whether a single failed request
```
Held
```
cancels all other requests in the list ( _`true`_ ) or whether some requests can
```
Capacity
```
succeed if others fail ( _`false`_ ). The default value is _`false`_ .

```
Held
```

cancels all other requests in the list ( _`true`_ ) or whether some requests can
```
Capacity
```
succeed if others fail ( _`false`_ ). The default value is _`false`_ .
```
Input
```

**•** `capacityRequests` —This field is a list of Apex-defined variables of
[class ConnectApi.CapacityRequestInputRepresentation. Each of the variables](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_capacity_request.htm)
represents a request to release capacity for one fulfillment order at one
location, and includes these fields:

**–** `actionRequestId` —Unique string that identifies the request. Can
be a UUID. Use the action request IDs in response data to identify which
requests succeeded or failed.

**–** `locationId` —ID of the location associated with the request.

Store Output Values

Use output values later in the flow. The values are assigned when the capacity properties are updated.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

`Fulfillment` This output is an Apex-defined variable of class
`Order Location` [ConnectApi.ReleaseHeldFOCapacityResponseOutputRepresentation, which includes this field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_release_held_f_o_capacity_response_output.htm)

```
   Release Held
```

**•** `capacityResponses` —This field is a list of Apex-defined variables of class
`Capacity` [ConnectApi.CapacityResponseOutputRepresentation, each of which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_capacity_response_output.htm)
```
   Output
```

**–** `actionRequestId` —Unique string that identifies the original capacity request.

**–** `error` [—This field is an Apex-defined variable of class ConnectApi.ErrorResponse, which includes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_error_response.htm)
these fields:

**•** `errorCode` —Error code, if the request returned an error.

**•** `message` —More error detail, if available.

**–** `success` —Indicates whether the request was successful ( _`true`_ ) or not ( _`false`_ ).

Flow Core Action for Order Management: Return Order Item Summaries Preview

Preview the expected results of a simple return of one or more order product summaries from an
order summary without executing the return. The output of this action contains the values that
would be set on the change order created by submitting the proposed return.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Order Item Summaries Preview .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` Reference to the order summary that you want to preview returning order product
`Summary` summaries from.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Return`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** _`AmountWithoutTax`_               - `amount` is the fee amount, not including tax. Tax is calculated on the
value and added.

**•** _`Percentage`_               - `amount` is a percentage. The fee amount is `amount` divided by 100 and then
multiplied by the `TotalPrice` and `TotalTaxAmount` of the associated order product
summary, prorated for the quantity being returned.

**•** _`PercentageGross`_               - `amount` is a percentage. The fee amount is `amount` divided by 100
and then multiplied by the `TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in the org. ID of the price book
entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry in the Order Product Summary
Change object’s `Reason` picklist.

**•** `orderItemSummaryId` —Required. ID of an order product summary to return. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to return.

**•** `reason` —Required. Return reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Product

Summary Items

Output

```

[This output is an Apex-defined variable of class ConnectApi.PreviewCancelOutputRepresentation, which](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_preview_cancel_output.htm)
contains the values that would populate a change order record for the proposed return.

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `orderSummaryId` field is the ID of the order summary specified in the input.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that is owed as a refund, but it isn’t
associated with an invoice or credit memo. Excess funds normally occur when order products are canceled
before fulfillment but after payment is captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the return.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the return.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.

**•** `totalTaxAmount` —Change to the total tax.

Usage

To set up the Return Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for returning order product summaries, display the output of this action for the user to review before executing the return.
When the user verifies the expected results, pass the same input to a Return Order Item Summaries Submit action.

SEE ALSO:

Flow Core Action for Order Management: Return Order Item Summaries Submit

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Order Management: Return Order Item Summaries Submit

Return one or more order product summaries from an order summary. This action is a simple return
that creates a change order but not a return order.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Order Item Summaries Submit .

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

`Order` Reference to the order summary that you want to return order product summaries
`Summary` from.

```
Id

```

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management

###### `Return`

```
Order

Product

Summary

Items

Input

```

This input is an Apex-defined variable of class
[ConnectApi.ChangeInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change.htm)

The variable has one field: `changeItems` . This field is a list of Apex-defined
[variables of class ConnectApi.ChangeItemInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item.htm)
includes these fields:

**•** `changeItemFees` —A list of Apex-defined variables of class
[ConnectApi.ChangeItemFeeInputRepresentation. Each variable has these](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_change_item_fee.htm)
fields:

**–** `amount` —Required. Value used to calculate the fee amount, as
described by the amountType. It must be a positive value.

**–** `amountType` —Required. Describes how the fee amount is calculated.
It can have one of these values:

**•** _`AmountWithTax`_    - `amount` is the fee amount, including tax.

**•** _`AmountWithoutTax`_    - `amount` is the fee amount, not
including tax. Tax is calculated on the value and added.

**•** _`Percentage`_    - `amount` is a percentage. The fee amount is
`amount` divided by 100 and then multiplied by the `TotalPrice`
and `TotalTaxAmount` of the associated order product summary,
prorated for the quantity being returned.

**•** _`PercentageGross`_    - `amount` is a percentage. The fee amount
is `amount` divided by 100 and then multiplied by the
`TotalLineAmountWithTax` of the associated order product
summary, prorated for the quantity being returned.

**–** `description` —Description of the fee.

**–** `priceBookEntryId` —Required unless price books are optional in
the org. ID of the price book entry associated with the fee product.

**–** `product2Id` —Required. ID of the product representing the fee.

**–** `reason` —Required. Reason for the fee. The value must match an entry
in the Order Product Summary Change object’s `Reason` picklist.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** `orderItemSummaryId` —Required. ID of an order product summary to return. It can’t be a shipping
charge product.

**•** `quantity` —Required. Quantity to return.

**•** `reason` —Required. Return reason. The value must match one of the picklist values on the Reason field
of the Order Product Summary Change object.

**•** `shippingReductionFlag` —Required. Boolean flag that specifies whether to prorate any related
delivery charge based on the price change.

Store Output Values

**Output Parameter** **Description**

```
Return Order

Product

Summary Items

Output

```

[This output is an Apex-defined variable of class ConnectApi.SubmitReturnOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_submit_return_output.htm)

The sign of a value in the `changeBalances` field is the opposite of the corresponding value on a change
order record. For example, a discount is a positive value in `changeBalances` and a negative value on a
change order record.

The `changeBalances` field is an Apex-defined variable of class
[ConnectApi.ChangeItemOutputRepresentation, which includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_change_item_output.htm)

**•** `grandTotalAmount` —Change to the total with tax.

**•** `totalAdjDeliveryAmtWithTax` —Change to the adjusted delivery subtotal, including tax.

**•** `totalAdjDistAmountWithTax` —Change to the total order adjustments, including tax.

**•** `totalAdjProductAmtWithTax` —Change to the adjusted product subtotal, including tax.

**•** `totalAdjustedDeliveryAmount` —Change to the adjusted delivery subtotal.

**•** `totalAdjustedDeliveryTaxAmount` —Change to the adjusted delivery subtotal tax.

**•** `totalAdjustedProductAmount` —Change to the adjusted product subtotal.

**•** `totalAdjustedProductTaxAmount` —Change to the adjusted product subtotal tax.

**•** `totalAdjustmentDistributedAmount` —Change to the total order adjustments.

**•** `totalAdjustmentDistributedTaxAmount` —Change to the total order adjustments tax.

**•** `totalAmount` —Change to the pretax total.

**•** `totalExcessFundsAmount` —The amount of excess funds available on the order payment summaries
related to the order summary. It’s equal to the captured amount that’s owed as a refund, but it’s not
associated with an invoice or credit memo. Excess funds normally occur when order products are canceled
before fulfillment but after payment is captured. This situation isn’t common in the US, where funds are
normally authorized but not captured until the fulfillment process begins. This value includes all excess
funds related to the order summary, not only the funds related to the current action.

**•** `totalFeeAmount` —The total amount of the fees charged for the return.

**•** `totalFeeTaxAmount` —The total amount of tax on the fees charged for the return.

**•** `totalRefundableAmount` —The total amount available to be refunded. It’s the sum of the excess
funds and any outstanding change order grand total amounts that apply to post-fulfillment changes. This
value includes all refundable amounts related to the order summary, not only the amount related to the
current action.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `totalTaxAmount` —Change to the total tax.

The `changeOrderId` field is the ID of the change order record created for the returned items. Use this
change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for any return fees. Use this
change order to create an invoice.

Usage

To set up the Return Order Product Summary Items Input:

**1.** If you want to charge fees, use Assignment elements to set the `amount`, `amountType`, `description`, `priceBookEntryId`,
`product2Id`, and `reason` field values on one or more `ConnectApi.ChangeItemFeeInputRepresentation`
variables.

**2.** Use Assignment elements to set the `orderItemSummaryId`, `quantity`, `reason`, and `shippingReductionFlag`
field values on one or more `ConnectApi.ChangeItemInputRepresentation` variables.

**3.** If you’re charging fees, use Assignment elements to add the `ConnectApi.ChangeItemFeeInputRepresentation`
variables to the `changeItemFees` fields on the associated `ConnectApi.ChangeItemInputRepresentation`
variables.

**4.** Use an Assignment element to add the `ConnectApi.ChangeItemInputRepresentation` variables to the
`changeItems` field on a `ConnectApi.ChangeInputRepresentation` variable.

**5.** Use the `ConnectApi.ChangeInputRepresentation` variable and the order summary ID in the action input.

In a flow for returning order product summaries, run a Return Order Item Summaries Preview action before running this action. Then
display its output for the user to review. When the user verifies the expected results, pass the same input to this action.

SEE ALSO:

Flow Core Action for Order Management: Return Order Item Summaries Preview

Add and Edit Elements

Flow Core Action for Order Management: Return Return Order Items

Process one or more return order line items belonging to a return order. This action creates a change
order record for the returned items and makes the processed return order line items read-only. You
can include return order fees associated with the return order line items. If you do, a change order
record is created for the return fees. If a processed return order line item has a remaining expected
quantity, the action creates a separate return order line item representing that quantity.

In Flow Builder, add an Action element to your flow. Select the **Order Management** category, and
###### search for Return Return Order Items .

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Order Management and
Returns

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Return Order` Reference to the return order that you want to process return order line items from.

```
   Id

```

```
Return Items

Input

```

Store Output Values

[This input is an Apex-defined variable of class ConnectApi.ReturnItemsInputRepresentation. It has three fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_items.htm)

The `returnOrderItemDeliveryCharges` field is an optional list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation. Each variable includes one field:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item_delivery_charge.htm)

**•** `returnOrderLineItemId` —ID of a return order line item representing a shipping charge to return.

The `returnOrderItemFees` field is an optional list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemFeeInputRepresentation. Each variable includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item_fee.htm)

**•** `quantityReturned` —The quantity of the ReturnOrderLineItem to process. The amount of the fee to
charge is determined by multiplying the total fee amount by this value, divided by the quantityExpected.
For example, if the fee amount is $10 and the quantityExpected is 2, if the quantityReturned is 1, $5 is
charged. This value normally equals the quantity returned of the ReturnOrderLineItem for the returned item
that the fee applies to. The value must be greater than 0. If this value plus quantityToCancel is less than the
expected return quantity, the remaining quantity to be returned is added to a new ReturnOrderLineItem.

**•** `quantityToCancel` —The quantity of the ReturnOrderLineItem to remove. This value normally equals
the quantity canceled of the ReturnOrderLineItem for the returned item that the fee applies to. This value
can also be used to cancel a portion of the fee. The value must be 0 or greater. If this value plus
quantityReturned is less than the expected return quantity, the remaining quantity to be returned is added
to a new ReturnOrderLineItem.

**•** `returnOrderLineItemId` —ID of a return order line item representing a return fee to charge.

The `returnOrderItems` field is a list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemInputRepresentation. Each of the variables includes these fields:](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_return_order_item.htm)

**•** `quantityReceived` —(Optional) The quantity of the return order line item that has been received.
The value must be zero or greater. This value isn’t used by any standard features, but is provided for use in
customizations.

**•** `quantityRejected` —(Optional) The quantity of the return order line item that has been rejected for
return. The value must be zero or greater. This value isn’t used by any standard features, but is provided for
use in customizations.

**•** `quantityReturned` —The quantity of the return order line item that has been returned. The value
must be greater than zero. If this value plus quantityToCancel is less than the expected return quantity,
then the remaining quantity to be returned is added to a new return order line item.

**•** `quantityToCancel` —(Optional) The quantity of the return order line item to remove because it’s not
being returned. The value must be zero or greater. If this value plus quantityReturned is less than the
expected return quantity, then the remaining quantity to be returned is added to a new return order line
item.

**•** `reasonForRejection` —(Optional) The reason why the rejected quantity, if any, was rejected. This
value isn’t used by any standard features, but is provided for use in customizations.

**•** `returnOrderLineItemId` —The return order line item ID.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Return Items

Output

```

Usage

[This output is an Apex-defined variable of class ConnectApi.ReturnItemsOutputRepresentation. It has three](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_items_output.htm)
fields.

The `changeOrderId` field is the ID of the change order record created for the returned item and delivery
charges. Use this change order to create a credit memo.

The `feeChangeOrderId` field is the ID of the change order record created for the return fees. Use this
change order to create an invoice.

The `returnLineItemSplits` field is a list of Apex-defined variables of class
[ConnectApi.ReturnOrderItemSplitLineOutputRepresentation, which includes these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_return_order_item_split_line_output.htm)

After a change order is created for a return order line item, the return order line item is read-only. If this action
is used to return a partial quantity, it creates a new “split” return order line item to hold the remaining quantity
to be returned. In that case, it returns the IDs of the original and split return order line items in an element of
the `returnLineItemSplits` output list property.

**•** `newReturnOrderItemId` —ID of the new return order line item that holds the remaining return
quantity.

**•** `originalReturnOrderItemId` —ID of the original return order line item.

To set up the Return Return Order Items Input:

**1.** Use Assignment elements to set the `quantityReceived`, `quantityRejected`, `quantityReturned`,
`quantityToCancel`, `reasonForRejection`, and `returnOrderLineItemId` field values on one or more
`ConnectApi.ReturnOrderItemInputRepresentation` variables.

**2.** If you want to include a delivery charge, use Assignment elements to set the `returnOrderLineItemId` field value on one
or more `ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation` variables.

**3.** If you want to include a return fee, use Assignment elements to set the `quantityReturned`, `quantityToCancel`, and
`returnOrderLineItemId` field values on one or more
`ConnectApi.ReturnOrderItemFeeInputRepresentation` variables.

**4.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemInputRepresentation` variables to the
`returnOrderItems` field on a `ConnectApi.ReturnItemsInputRepresentation` variable.

**5.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemDeliveryChargeInputRepresentation`
variables to the `returnOrderItemDeliveryCharges` field on a
`ConnectApi.ReturnItemsInputRepresentation` variable.

**6.** Use an Assignment element to add the `ConnectApi.ReturnOrderItemFeeInputRepresentation` variables to the
`returnOrderItemFees` field on a `ConnectApi.ReturnItemsInputRepresentation` variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

**7.** Use the `ConnectApi.ReturnItemsInputRepresentation` variable and the return order ID in the action input.

SEE ALSO:

Flow Core Action for Order Management: Create Return Order

Flow Core Action for Order Management: Create Credit Memo

Flow Core Action for Order Management: Create an Invoice from Change Orders

Flow Core Action for Order Management: Ensure Refunds Async

Add and Edit Elements

##### Salesforce Omnichannel Inventory Flow Core Actions

Salesforce Omnichannel Inventory provides several core actions for implementing inventory
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the **Omnichannel Inventory Service** category, and search for the appropriate action.

These actions use Apex-defined input and output variables that map to input and output classes
in the Apex ConnectApi namespace. For more information on using Apex-defined variables in flows,
see Considerations for the Apex-Defined Data Type on page 260.

Important: A flow that uses Omnichannel Inventory actions must have a runtime API version
of 52.0 or later. If possible, always use the latest API version in your flows.

Flow Core Action for Omnichannel Inventory: Create Reservation
Create one or more inventory reservations at a location or location group.

Flow Core Action for Omnichannel Inventory: Fulfill Reservation
Fulfill one or more inventory reservations at a location.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

Flow Core Action for Omnichannel Inventory: Get Availability
Get inventory availability data for one or more products at one or more inventory locations or location groups.

Flow Core Action for Omnichannel Inventory: Release Reservation
Release one or more inventory reservations.

Flow Core Action for Omnichannel Inventory: Transfer Reservation
Transfer one or more inventory reservations between locations or location groups. This action reduces the reserved quantity at the
source and increases it at the destination. It doesn’t change physical quantities.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Omnichannel Inventory: Create Reservation

Create one or more inventory reservations at a location or location group.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Create Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

###### `Create`

Service

Reservation

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OCICreateReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_create_reservation.htm)

The variable has these fields.

**•** `actionRequestId` —A UUID that identifies the request. To identify
which actions succeeded or failed, use the action request IDs in the output
variables.

**•** `allowPartialReservations` —Optional. When _`true`_, if the system
can’t create the entire reservation, then it attempts to create a partial
reservation.

**•** `createRecords` —A list of up to 100 Apex-defined variables of class
[ConnectApi.OCICreateReservationSingleInputRepresentation. Each variable](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_create_reservation_single.htm)
has these fields.

**–** `locationGroupIdentifier` —Identifier of the location group
at which to reserve inventory. Either `locationGroupIdentifier`
or `locationIdentifier` is required, but not both.

**–** `locationIdentifier` —Identifier of the location at which to
reserve inventory. Either `locationIdentifier` or
`locationGroupIdentifier` is required, but not both.

**–** `quantity` —The quantity of the product to reserve.

**–** `stockKeepingUnit` —The Stock Keeping Unit (SKU) of the product
to reserve.

**•** `expirationSeconds` —Optional. A length of time in seconds. If the
reservation isn’t fulfilled within this amount of time after the reservationTime,
then it expires. The maximum value is 14400.

**•** `externalRefId` —Optional The external reference ID.

**•** `reservationTime` —Optional The time at which to record the
reservation. Example: 2020-07-24T21:13:00Z

Store Output Values


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service Create

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCICreateReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_output.htm)

The variable has these fields.

**•** `details` —A list of Apex-defined variables of class
[ConnectApi.OCICreateReservationSingleOutputRepresentation. Each variable represents one product being](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_single_output.htm)
reserved and has these fields.

**–** `errorCode` —The error code, if any.

**–** `locationGroupIdentifier` —Identifier of the location group where the inventory is reserved.

**–** `locationIdentifier` —Identifier of the location where the inventory is reserved

**–** `quantity` —The reserved quantity of the product.

**–** `stockKeepingUnit` —The SKU of the reserved product.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCICreateReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_create_reservation_error_output.htm)
and has these fields.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `expirationTime` —The time at which the reservation would expire.

**•** `reservationTime` —The time when the reservation was recorded.

**•** `success` —Indicates whether the reservation succeeded.

To set up the Omnichannel Inventory Create Service Reservation Input:

**1.** For each product to reserve, use Assignment elements to set the `locationGroupIdentifier` or `locationIdentifier`
field, `quantity` field, and `stockKeepingUnit` field values on a
`ConnectApi.OCICreateReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCICreateReservationSingleInputRepresentation`
variables to the `createRecords` field on a `ConnectApi.OCICreateReservationInputRepresentation`
variable.

**3.** Use Assignment elements to set the `actionRequestId`, `allowPartialReservations`, `expirationSeconds`,
`externalRefId`, and `reservationTime` field values on the
`ConnectApi.OCICreateReservationInputRepresentation` variable.

**4.** Use the `ConnectApi.OCICreateReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Omnichannel Inventory: Fulfill Reservation

Fulfill one or more inventory reservations at a location.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Fulfill Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

###### `Fulfill`

Reservation

Input

```

This input is an Apex-defined variable of class
[ConnectApi.OCIFulfillReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_fulfill_reservation.htm)

The variable has one field: `fulfillmentRecords` . This field is a list of up
to 100 Apex-defined variables of class

[ConnectApi.OCIFulfillReservationSingleInputRepresentation. Each variable has](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_fulfill_reservation_single.htm)
these fields.

**•** `actionRequestId` —A UUID that identifies the request. To identify
which actions succeeded or failed, use the action request IDs in the output
variables.

**•** `externalRefId` —Optional. The external reference ID.

**•** `locationIdentifier` —Identifier of the location at which to fulfill the
reserved inventory.

**•** `quantity` —The quantity of the product to fulfill.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to fulfill.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

###### `Fulfill`

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCIFulfillReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCIFulfillReservationErrorOutputRepresentation. Each variable represents a returned error and](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_error_output.htm)
has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCIFulfillReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_fulfill_reservation_single_output.htm)
error and includes the values from the input so you can resubmit them:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `locationIdentifier` —Identifier of the location at which to fulfill the reserved inventory.

**•** `quantity` —The quantity of the product to fulfill.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to fulfill.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the fulfillment succeeded.

To set up the Omnichannel Inventory Service Fulfill Reservation Input:

**1.** For each reservation to fulfill, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`locationIdentifier`, `quantity`, and `stockKeepingUnit` field values on a
`ConnectApi.OCIFulfillReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCIFulfillReservationSingleInputRepresentation`
variables to the `fulfillmentRecords` field on a `ConnectApi.OCIFulfillReservationInputRepresentation`
variable.

**3.** Use the `ConnectApi.OCIFulfillReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Get Availability

Get inventory availability data for one or more products at one or more inventory locations or
location groups.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Get Availability** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input** **Description**
**Parameter**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

###### `Get`

```

This input is an Apex-defined variable of class
[ConnectApi.OCIGetInventoryAvailabilityInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_get_inventory_availability.htm)

The variable has these fields.

**•** `locationGroupIdentifier` —Optional. Can’t combine with
```
Availability
```
`locationGroupIdentifiers` or `locationIdentifiers` . The
```
Input
```
identifier of a location group to retrieve inventory availability data for.
Specifying this value retrieves inventory data for all locations belonging to
this group.

**•** `locationGroupIdentifiers` —Optional; can’t combine with
`locationGroupIdentifier` or `locationIdentifiers` . A list


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

of up to 100 identifiers of location groups to retrieve inventory availability data for.

**•** `locationIdentifiers` —Optional; can’t combine with `locationGroupIdentifier` or
`locationGroupIdentifiers` . A list of up to 100 identifiers of locations to retrieve inventory
availability data for.

**•** `stockKeepingUnit` —Optional; can’t combine with `stockKeepingUnits` . The SKU of a product
to retrieve inventory availability data for. Specifying a SKU with no locations or location groups returns
availability data for that SKU at all inventory locations that aren’t assigned to location groups.

**•** `stockKeepingUnits` —Optional; can’t combine with `stockKeepingUnit` . A list of up to 100
SKUs of products to retrieve inventory availability data for.

**•** `useCache` —Optional. Fetch the inventory data from the cache. The default value is `true` .

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service Get

Availability

Output

```

[This input is an Apex-defined variable of class ConnectApi.OCIGetInventoryAvailabilityOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_get_inventory_availability_output.htm)

The variable has these fields.

**•** `locationGroups` —A list of Apex-defined variables of class
[ConnectApi.OCILocationGroupAvailabilityOutputRepresentation. Each variable represents availability data](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_location_group_availability_output.htm)
for one location group and has these fields.

**–** `inventoryRecords` —A list of Apex-defined variables of class
[ConnectApi.OCIInventoryRecordOutputRepresentation. Each variable represents the availability of one](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_inventory_record_output.htm)
product and has these fields.

**•** `availableToFulfill` —The Available To Fulfill quantity.

**•** `availableToOrder` —The Available To Order quantity.

**•** `effectiveDate` —The effective date of the inventory.

**•** `futures` —A list of Apex-defined variables of class
[ConnectApi.OCIFutureInventoryOutputRepresentation. Each variable represents one future restock](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_future_inventory_output.htm)
and has these fields.

**–** `expectedDate` —Date when the future inventory is expected.

**–** `quantity` —Quantity of the future inventory.

**•** `onHand` —The On Hand quantity.

**•** `reserved` —The Reserved quantity.

**•** `safetyStockCount` —The Safety Stock Count.

**•** `stockKeepingUnit` —The SKU of the product.

**–** `locationGroupIdentifier` —The identifier of the location group.

**•** `locations` —A list of Apex-defined variables of class
[ConnectApi.OCILocationAvailabilityOutputRepresentation. Each variable represents availability data for](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_location_availability_output.htm)
one location and has these fields.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

**–** `inventoryRecords` —A list of Apex-defined variables of class
[ConnectApi.OCIInventoryRecordOutputRepresentation. Each variable represents the availability of one](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_inventory_record_output.htm)
product and has these fields.

**•** `availableToFulfill` —The Available To Fulfill quantity.

**•** `availableToOrder` —The Available To Order quantity.

**•** `effectiveDate` —The effective date of the inventory.

**•** `futures` —A list of Apex-defined variables of class
[ConnectApi.OCIFutureInventoryOutputRepresentation. Each variable represents one future restock](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_future_inventory_output.htm)
and has these fields.

**–** `expectedDate` —Date when the future inventory is expected.

**–** `quantity` —Quantity of the future inventory.

**•** `onHand` —The On Hand quantity.

**•** `reserved` —The Reserved quantity.

**•** `safetyStockCount` —The Safety Stock Count.

**•** `stockKeepingUnit` —The SKU of the product.

**–** `locationIdentifier` —The identifier of the location.

To set up the Omnichannel Inventory Service Get Availability Input:

**1.** Use Assignment elements to set the `locationGroupIdentifier`, `locationGroupIdentifiers`, or
`locationIdentifiers` field value, `stockKeepingUnit` or `stockKeepingUnits` field value, and `useCache`
field value on a `ConnectApi.OCIGetInventoryAvailabilityInputRepresentation` variable.

**2.** Use the `ConnectApi.OCIGetInventoryAvailabilityInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Release Reservation

Release one or more inventory reservations.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Release Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Omnichannel

Inventory

Service

Release

```

[This input is an Apex-defined variable of class ConnectApi.OCIReleaseReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_release_reservation.htm)

The variable has one field: `releaseRecords` . This field is a list of up to 100 Apex-defined variables of class
[ConnectApi.OCIReleaseReservationSingleInputRepresentation. Each variable has these fields.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_release_reservation_single.htm)

**•** `actionRequestId` —A UUID that identifies the request. To identify which actions succeeded or failed,
```
Reservation
```
use the action request IDs in the output variables.
```
Input

```

**•** `externalRefId` —Optional. The external reference ID.

**•** `locationGroupIdentifier` —Identifier of the location group at which to release the reserved
inventory. Either `locationGroupIdentifier` or `locationIdentifier` is required, but not
both.

**•** `locationIdentifier` —Identifier of the location at which to release the reserved inventory. Either
`locationIdentifier` or `locationGroupIdentifier` is required, but not both.

**•** `quantity` —The quantity of the product to release.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to release.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

Release

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCIReleaseReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCIReleaseReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_error_output.htm)
and has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCIReleaseReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_release_reservation_single_output.htm)
error and includes the values from the input so you can resubmit them:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `locationGroupIdentifier` —Identifier of the location group at which to release the
reserved inventory.

**•** `locationIdentifier` —Identifier of the location at which to release the reserved inventory.

**•** `quantity` —The quantity of the product to release.

**•** `stockKeepingUnit` —The Stock Keeping Unit of the product to release.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the release succeeded.

To set up the Omnichannel Inventory Service Release Reservation Input:


Automate Your Business Processes with Salesforce Flow Flow Reference

**1.** For each reservation to release, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`locationGroupIdentifier` or `locationIdentifier`, `quantity`, and `stockKeepingUnit` field values on a
`ConnectApi.OCIReleaseReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCIReleaseReservationSingleInputRepresentation`
variables to the `releaseRecords` field on a `ConnectApi.OCIReleaseReservationInputRepresentation`
variable.

**3.** Use the `ConnectApi.OCIReleaseReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Omnichannel Inventory: Transfer Reservation

Transfer one or more inventory reservations between locations or location groups. This action
reduces the reserved quantity at the source and increases it at the destination. It doesn’t change
physical quantities.

In Flow Builder, add an Action element to your flow. Select the **Omnichannel Inventory Service**
category, and search for **Omnichannel Inventory Service Transfer Reservation** .

Note: Set the flow’s runtime API version to 52.0 or later.

Set Input Values

Use values from earlier in the flow to set the inputs.

**Input Parameter** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions with Salesforce
Omnichannel Inventory

```
Omnichannel

Inventory

Service

```

[This input is an Apex-defined variable of class ConnectApi.OCITransferReservationInputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_transfer_reservation.htm)

The variable has these fields.

**•** `allOrNothingTransferId` —Optional. Controls whether a single failed transfer cancels all other
###### `Transfer`
transfers in the transferRecords list.
```
Reservation
```

`Input` **–** To allow some transfers in the transferRecords list to succeed when others fail, don’t set this value.

**–** To cancel all the transfers in the transferRecords list when any of them fail, set this value to a UUID. The
ID must be unique, but isn’t otherwise used.

**•** `transferRecords` —A list of up to 100 Apex-defined variables of class
[ConnectApi.OCITransferReservationSingleInputRepresentation. Each variable represents an inventory transfer](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_input_o_c_i_transfer_reservation_single.htm)
and has these fields.

**–** `actionRequestId` —A UUID that identifies the request. To identify which actions succeeded or
failed, use the action request IDs in the output variables.

**–** `externalRefId` —Optional. The external reference ID.

**–** `fromLocationGroupIdentifier` —The identifier of the location group transferring the
reservation. Either `fromLocationGroupIdentifier` or `fromLocationIdentifier` is
required, but not both.

**–** `fromLocationIdentifier` —The identifier of the location transferring the reservation. Either
`fromLocationIdentifier` or `fromLocationGroupIdentifier` is required, but not
both.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**–** `ignoreAvailabilityCheck` —If true, force the transfer even if the receiving location doesn’t
have sufficient available inventory. The default value is false.

**–** `quantity` —The quantity of the product reservation to transfer.

**–** `stockKeepingUnit` —The Stock Keeping Unit (SKU) of the product reservation to transfer.

**–** `toLocationGroupIdentifier` —The identifier of the location group receiving the reservation.
Either `toLocationGroupIdentifier` or `toLocationIdentifier` is required, but not
both.

**–** `toLocationIdentifier` —The identifier of the location receiving the reservation. Either
`toLocationIdentifier` or `toLocationGroupIdentifier` is required, but not both.

Store Output Values

**Output Parameter** **Description**

```
Omnichannel

Inventory

Service

Transfer

Reservation

Output

```

[This value is an Apex-defined variable of class ConnectApi.OCITransferReservationOutputRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_output.htm)

The variable has these fields.

**•** `errors` —A list of Apex-defined variables of class
[ConnectApi.OCITransferReservationErrorOutputRepresentation. Each variable represents a returned error](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_error_output.htm)
and has these fields.

**–** `details` —An Apex-defined variable of class
[ConnectApi.OCITransferReservationSingleOutputRepresentation. Each variable represents a returned](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connectapi_output_o_c_i_transfer_reservation_single_output.htm)
error and includes the fields from the input:

**•** `actionRequestId` —A UUID that identifies the failed request.

**•** `externalRefId` —The external reference ID.

**•** `fromLocationGroupIdentifier` —The identifier of the location group transferring the
reservation.

**•** `fromLocationIdentifier` —The identifier of the location transferring the reservation.

**•** `ignoreAvailabilityCheck` —Whether this call ignored availability data at the location
that received the reservation.

**•** `quantity` —The quantity of the product reservation to transfer.

**•** `stockKeepingUnit` —The SKU of the product reservation to transfer.

**•** `toLocationGroupIdentifier` —The identifier of the location group intended to receive
the reservation.

**•** `toLocationIdentifier` —The identifier of the location intended to receive the reservation.

**–** `errorCode` —The error code.

**–** `message` —Details of the error, if available.

**•** `success` —Indicates whether the transfer succeeded.

To set up the Omnichannel Inventory Service Transfer Reservation Input:


Automate Your Business Processes with Salesforce Flow Flow Reference

**1.** For each reservation to transfer, use Assignment elements to set the `actionRequestId`, `externalRefId`,
`fromLocationGroupIdentifier` or `fromLocationIdentifier`, `quantity`, `stockKeepingUnit`, and
`toLocationGroupIdentifier` or `toLocationIdentifier` field values on a
`ConnectApi.OCITransferReservationSingleInputRepresentation` variable.

**2.** Use Assignment elements to add the `ConnectApi.OCITransferReservationSingleInputRepresentation`
variables to the `transferRecords` field on a `ConnectApi.OCITransferReservationInputRepresentation`
variable.

**3.** Use an Assignment element to set the `allOrNothingTransferId` field on the
`ConnectApi.OCITransferReservationInputRepresentation` variable.

**4.** Use the `ConnectApi.OCITransferReservationInputRepresentation` variable in the action input.

SEE ALSO:

Add and Edit Elements

Flow Core Actions: Send Conversation Messages

Send a messaging component to one or more messaging users in enhanced WhatsApp, enhanced
Apple Messages for Business, enhanced SMS, or Messaging for In-App.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Messages`_, and
##### select Send Conversation Messages .

Set Input Values


EDITIONS

Available in: Lightning
Experience

Available
in: Enterprise, Unlimited,
and Developer Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

Here’s an example of the Send Conversation Messages action in a simple flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

To track messages sent by this action, query the ConvMessageSendRequest object.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Send Custom Notification

Add the Send Custom Notification action to a flow, then add recipients and content.

Important: The Send Custom Notifications user permission is enforced in orgs created in
Winter ’21 or later.

The Send Custom Notifications user permission isn’t required to trigger the Send Custom
Notification action in processes or flows that run in system context.

Tip:

**•** Before you begin, make sure that the custom notification type you want to call from your
[process exists. If not, create the notification type.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_custom_type.htm&language=en_US)

**•** To query for the Notification Type ID directly from a flow, add the Get Record element to
your flow and filter by API name. If you’ve installed a notification type via a managed
package, filter by the namespace prefix as well as the API name.

**•** To add recipients, define Recipient ID as a resource. Then add values to your Recipient ID
collection by adding the Assignment element to your flow.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Notifications`_,
##### and select Send Custom Notification .

Set Input Values

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To trigger the Send Custom
Notification action in flows
that run in user context, REST
API calls, and Apex callouts:
##### • Send Custom

Notifications

Use values from earlier in the flow to set the inputs for the email. Specify at least one recipient for the email.

**Field** **Description**

`Custom Notification` The ID of the Custom Notification Type being used for the notification.
```
Type ID
```

This parameter accepts single-value resources of any type. That value is treated as text.

`Notification Body` The body of the notification that recipients see.

[The content of mobile push notifications depends on the Display full content push notifications](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)
[setting.](https://help.salesforce.com/s/articleView?id=sf.salesforce_app_notifications_full_content_enable.htm&language=en_US)

This parameter accepts single-value resources of any type. That value is treated as text and is limited
to 750 characters.

`Notification Title` The title of the notification as seen by recipients.

This parameter accepts single-value resources of any type. That value is treated as text and is limited
to 250 characters.

`Recipient IDs` The ID of the recipient or recipient type of the notification.

Valid values are:

**•** _`User ID`_ —The notification is sent to this user, if this user is active.

**•** _`Account ID`_ —The notification is sent to all active users who are members of this account’s
Account Team. Valid only if account teams are enabled for your org.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

**•** _`Opportunity ID`_ —The notification is sent to all active users who are members of this
opportunity’s Opportunity Team. Valid only if team selling is enabled for your org.

**•** _`Group ID`_ —The notification is sent to all active users who are members of this group.

**•** _`Queue ID`_ —The notification is sent to all active users who are members of this queue.

This parameter accepts collection variables of type Text and is limited to 500 values. The values that
you enter for an individual Send Custom Notification action can represent a total of up to 10,000 users
as recipients.

`Target ID` Optional. The Record ID for the target record of the notification.

Specify either a Target ID or a Target Page Reference.

This parameter accepts single-value resources of any type. That value is treated as text.

`Target Page` Optional. The Page Reference for the navigation target of the notification.
```
   Reference
```

Specify either a Target ID or a Target Page Reference.

This parameter accepts single-value resources of any type. That value is treated as text.

[To see how to specify the target using JSON, see pageReference.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_navigation_page_definitions.htm)

`Sender ID` Optional. The User ID of the sender of the notification.

This parameter accepts single-value resources of any type. That value is treated as text.

Usage

**•** Each notification can have up to 10,000 users as recipients. However, you can add an action to the same process within Process
Builder or to the same flow in Flow Builder to have more recipients.

**•** Your org saves your most recent 1 million custom notifications for view in notification trays. Your org can save up to 1.2 million
custom notifications, but it trims the amount to the most recent 1 million notifications when you reach the 1.2 million limit.

**•** An org can execute up to 10,000 notification actions per hour. When you exceed this limit, no more notifications are sent in that
hour, and all unsent notifications are lost. Notification actions resume in the next hour.

For example, your notification action processes are triggered 10,250 times between 4:00 and 4:59. Salesforce executes the first 10,000
of those actions. The remaining 250 notifications aren’t sent and are lost. Salesforce begins executing notification actions again at
5:00.

SEE ALSO:

[Create and Send Custom Desktop or Mobile Notifications](https://help.salesforce.com/s/articleView?id=sf.notif_builder_custom.htm&language=en_US)

Flow Run Context

Flow Elements

Add and Edit Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action: Send Email

Send and optionally log an email by specifying the email content and recipients in a flow. If you’re
using Marketing Cloud Growth, use the Send Email Message on page 377 element to send an email
to your audience segment.

Note: If you're using Marketing Cloud Growth, use the Send Email Message action instead
of the Send Email action. The Send Email action doesn't work with audience segments.

Before you begin:

**•** Use a Get Records element to get the email template to use, using the Email Template object
and filtering by the **Name** (Email Template Name) field.

**•** Then, in `Email Template ID`, select the ID of the record found by the Get Records. For
example, if you labeled your Get Records element _`Get Email Template`_, select **Email**
**Template from Get_Email_Template** .

**•** Then, select **Id** (Email Template ID).

##### In Flow Builder, search for Send Email in the element menu, and select Send Email .

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Important: If the Sender Type is OrgWideEmailAddress, ensure that the user running the flow has the proper profile configurations
required by the specific org-wide email address being used. Proceeding without the proper configuration results in an error.

Set Input Values

To set the inputs for the email, use values from earlier in the flow. Specify at least one recipient for the email.

Example: You want to send and log an email to a contact record, and also log to its related account record. For the email content,
you want to use an email template with Contact and Account merge fields. Set `Email Template ID` to the ID of the email
template to use. Next, set `Log Email on Send` to **{!$GlobalConstant.True}** . Then, set `Recipient ID` to the contact
record’s ID and `Related Record ID` to the account record’s ID.

**Input Parameter** **Description**

```
Add Threading Token

to Body

Add Threading Token

to Subject

```

Optional. Indicates whether to create a unique token for the related record and add it to the email
body.

When the related record is a case record, Email-to-Case uses the token to link future email responses
to that case.

To link future email responses to other records, create an Apex Email Service and use the
`EmailMessages.getRecordIdFromEmail` function to find the record that matches the
token.

Optional. Indicates whether to create a unique token for the related record and add it to the email
subject.

When the related record is a case record, Email-to-Case uses the token to link future email responses
to that case.

To link future email responses to other records, create an Apex Email Service and use the
`EmailMessages.getRecordIdFromEmail` function to find the record that matches the
token.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
BCC Recipient

Address List

Body

CC Recipient Address

List

Email Template ID

```

Optional. A comma-delimited list of recipient email addresses to send a copy of the email to. Email
addresses in the BCC list are hidden from all recipients.

This parameter accepts single-value resources of any type. The value is treated as text.

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

The body of the email.

Optional if you’re using an email template. The email template overrides the entry in this field.

Required if you’re not using an email template.

Enter text or select a single-value resource of any type that contains your content, for example, a Text
Template resource.

If entering text, the value is treated as plain text. If you’re using a resource, the value can be treated
as plain text or rich text, depending on your selection in `Rich-Text-Formatted Body` .

Optional. A comma-delimited list of recipient email addresses to send a copy of the email to.

This parameter accepts single-value resources of any type. The value is treated as text.

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of the Classic or Lightning email template to use for the email subject and body.

If the email template has merge fields from an object other than the one associated with `Recipient`
`ID`, specify the record used to supply those merge fields in `Related Record ID` .

If you’re using this parameter, `Recipient ID` is required.

This parameter can be used with `Log Email on Send` .

Using email templates in the Send Email action changes the API called by the action, which changes
[the daily email send limit to the General Email Limit instead of the Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)

`Log Email on Send` Optional. Indicates whether to log the email on the specified records’ activity timelines and activity
history. Valid values are:

**•** **{!$GlobalConstant.True}** —Log the email to the record associated with `Recipient ID`,
`Related Record ID`, or both.

**•** **{!$GlobalConstant.False}** —Don’t log the email to a record. This value is the default.

To log an email, you must specify a value for `Recipient ID`, `Related Record ID`, or both.

This parameter can be used with `Email Template ID` .

Logging emails with the Send Email action changes the API called by the action, which changes the
[daily email send limit to the General Email Limit instead of the Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Recipient Address

Collection

Recipient Address

List

Recipient ID

Related Record ID

```

Optional. A collection of the recipients' email addresses.

This parameter accepts collection variables of type Text.

If `Log Email on Send` is set to **{!$GlobalConstant.True}**, the email is logged to the ID specified
for `Recipient ID`, not the records associated with the email addresses in `Recipient`
`Address Collection` .

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. A comma-delimited list of the recipients' email addresses.

This parameter accepts single-value resources of any type. The value is treated as text.

If `Log Email on Send` is set to **{!$GlobalConstant.True}**, the email is logged to the ID specified
for `Recipient ID`, not the records associated with the email addresses in `Recipient`

```
Address List

```

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of a lead or a contact record.

Required if `Email Template ID` is specified.

If `Log Email on Send` is included, this parameter is the ID of the person to send and log the
email to.

If `Email Template ID` is included, this parameter is the ID of the person to send an email to
and populate recipient merge fields with.

If the ID entered in this parameter is a lead record, you can’t use `Related Record ID` .

The maximum size for this field is 4,000 bytes.

You can enter values for `BCC Recipient Address List`, `CC Recipient Address`
`List`, `Recipient ID`, `Recipient Address List`, and `Recipient Address`
`Collection` as long as the combined number of recipients is 150 or fewer.

Optional. The ID of a non-recipient record. For example, the ID of a case record.

If `Log Email on Send` is included, this parameter is the ID of a secondary record to log the
email to.

If `Email Template ID` is included, this parameter is the ID of the non-recipient record used
to populate email template merge fields.

You can’t use this parameter if the ID entered in `Recipient ID` is a lead record.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

`Rich-Text-Formatted` Optional. Indicates whether you want the resource specified for the `Body` parameter to use rich
`Body` text. Valid values are:

**•** **{!$GlobalConstant.True}** —Use rich text for the email body.

**•** **{!$GlobalConstant.False}** —Use plain text for the email body. This value is the default.

```
Sender Email Address

```

Optional. The organization-wide email address that’s used to send the email.

Required when `Sender Type` is set to _`OrgWideEmailAddress`_ .

Required when the running flow user is the guest user.

This parameter accepts a single-value resource of any type. The value is treated as text.

`Sender Type` Optional. The type of sender that the email is sent from. Valid values are:

**•** _`CurrentUser`_ —The email address of the user running the flow. This value is the default.

**•** _`DefaultWorkflowUser`_ —The email address of the default workflow user.

**•** _`OrgWideEmailAddress`_ —The organization-wide email address that is specified in `Sender`
`Email Address` . When the running flow user is the guest user, the `Sender Email`
`Address` must be set to a verified organization-wide email. Emails sent from the guest user
and not using a verified organization-wide email are blocked.

```
Subject

```

The subject of the email.

Optional if you’re using an email template. The email template overrides the entry in this field.

Required if you’re not using an email template.

Enter text or select a single-value resource of any type that contains your content, for example, a Text
Template resource. The value is treated as plain text.

`Use Line Breaks` Optional. Indicates whether to render the line breaks in the rich-text-formatted body text template.
Valid values are true and false. The default value is false.

Usage

At run time, the email isn’t sent until the interview’s transaction completes. Transactions are complete when the interview either finishes
or executes a Screen, Local Action, or Wait element. Before activating your flow, confirm that your org can send email in **Setup** **Deliverability** - **Access to Send Email (All Email Services)** - **All email** .

If you set Email Deliverability to No Access and:

**•** If you don't set `Email Template ID` or `Log Email on Send` fields, the flow runs but doesn't send the email.

**•** If you do set `Email Template ID` or `Log Email on Send` fields, the flow returns an error when it sends the email.

Setup Configurations for Scheduled Flows

If you use the Send Email action element in a Scheduled-Triggered flow, you must configure the organization-wide email address in
Setup.

**•** Set the organization-wide email address in **Setup** - **Email** - **Organization-Wide Email Addresses**

**•** Add the organization-wide email address in **Setup** - **Process Automation Settings** - **Automated Process User Email Address**


Automate Your Business Processes with Salesforce Flow Flow Reference

Email Sending Limits

**•** If you’re using `Log Email on Send` or `Email Template ID`, the daily email send limit is based on the single email limit.
[For details, see General Email Limits.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)

**•** If you’re not using `Log Email on Send` or `Email Template ID`, the daily email send limit is based on the daily workflow
[email limit. For details, see Proactive Alert Monitoring: Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000382442&type=1&language=en_US)

Considerations

**•** Emails sent using the Send Email action don't include email signatures from My Email Settings. To include a signature, add one to
the email template, flow text template, or other resource used in the Send Email action.

**•** If the `Related Record ID` is set as a Case ID by the flow, Customer Community users can't create an `EmailMessage`
[record. For details, see Experience Cloud User Licenses.](https://help.salesforce.com/s/articleView?id=sf.users_license_types_communities.htm&language=en_US)

SEE ALSO:

Add and Edit Elements

Options for Sending Emails from Flows

Flow Resource: Text Template

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

Options for Sending Emails from Flows

Flow Core Action: Send Notification Actions

Call a notification type to send. Each Send Notification action corresponds to a supported notification
type. Send Notification actions are available only for Slack-enabled custom notification types and
certain Slack-enabled standard notification types.

Note: [To send notifications for Slack, enable Salesforce for Slack Integrations.](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

[To create a custom Slack notification type supported by a Send Notification action, see Create](https://help.salesforce.com/s/articleView?id=sf.notif_builder_create_send_slack.htm&language=en_US)
[and Send Custom Slack Notifications.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_create_send_slack.htm&language=en_US)

Add an Action element to the flow. In the Action field, select the Send Notification-supported
notification type that you want to configure. Each Send Notification action corresponds to a
supported notification type. For example, if you created a custom notification type named My
Opportunity Notification, look for the My Opportunity Notification action in the Notifications category.

Set Input Values

Use values from earlier in the flow to set the inputs for the notification type.

**Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To trigger a Send Notification
action in flows that run in
user context and REST API
calls:

**•** Send Custom
Notifications

```
Recipient IDs

```

Required. The IDs of the notification recipients or recipient types.

[The value must be a collection variable that represents one or more](https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_variable_populate.htm&language=en_US)
Salesforce User IDs or Collaboration Room IDs.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

Some Salesforce features link standard objects to Collaboration Room through the Swarm object. For
these features, you can find an existing Collaboration Room ID from the Swarm object.

The collection variable’s Data Type must be Text. The collection can have up to 500 values.

```
Record ID

```

Required. The ID of the record that the notifications are about. The record ID must be an ID from the
Salesforce object related to the notification type. For example, enter the record ID for an opportunity
when configuring a notification type associated with the Opportunity object.

For custom notification types, you can find the related object by viewing the notification type's
settings from Custom Notifications in Setup. For supported standard notification types, refer to the
Standard Notification Types and Related Objects table.

Enter a record ID or select a variable that identifies the record.

This parameter accepts single-value resources of any type. That value is treated as text.

Standard Notification Types and Related Objects

Use this table to identify which object applies to each standard notification type that’s supported by a Send Notification action. The
object determines the value that you enter for `Record Id` .

**Standard Notification Type** **Related Salesforce Object**

`Amount Updated` Opportunity

`Close Date Reminder` Opportunity

`Close Date Updated` Opportunity

`Deal Won` Opportunity

`Deals to Watch` Opportunity

`High Priority Case` Case

`New Allergy` Allergy Intolerance
```
Intolerance

```

`New Child` Opportunity
```
Opportunity

```

`New Care Determinant` Care Determinant

`New Health Condition` Health Condition

`New or Updated Care` Task
```
Plan Task

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Standard Notification Type** **Related Salesforce Object**

`Next Step Reminder` Opportunity

`Stage Reminder` Opportunity

`Stage Updated` Opportunity

`Updated Care Plan` Case

Usage

**•** Each notification can have up to 10,000 users as recipients. However, you can add another action to the same flow in Flow Builder
to have more recipients.

**•** You can save up to 1.2 million custom notifications, but notification trays show only your most recent 1 million custom notifications.

**•** You can execute up to 10,000 notification actions per hour. When you exceed this limit, no more notifications are sent in that hour,
and all unsent notifications are lost. Notification actions resume in the next hour.

**•** The sending rates of Slack notifications are also subject to the limits of the Slack service.

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_collaborationroom.htm)_ : CollaborationRoom

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_swarm.htm)_ : Swarm

Flow Core Action: Send Surveys

Create an action to send an active survey by specifying the name, subject, recipients, and invitation
link options in the flow.

In Flow Builder, add an Action element to your flow. In the Action field, enter the name of an active
survey. Or, in the left navigation, click **Survey**, and then in the Action field, select an active survey.
Define the name of the action and the survey recipients.

Note: If you deactivate a survey after it’s added to a flow and then activate it, the Flow Builder
renders an incorrect Action layout for that survey.

Example: You want to collect feedback from all the participants when a case is closed. First,
create a flow and get all records where the status of the case object is closed. Then, create
an action that selects the survey to send to the participants for feedback.

Set Input Values

Specify at least one recipient for the survey.

**Field** **Description**

`Label` Name for the action.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

```
API Name

```

Associate an API name for the action.

This parameter auto-generates the API name based on the label, which you can edit, if necessary.

`Description` Optional. Description about the purpose of the action.

```
Survey Subject

Recipient Type

```

Optional. Select a survey subject that you want to perform the action on. For example, to get all case
records, select the survey subject as Case, or create a required resource for the subject.

This parameter accepts flow variables of type Text.

Select the type of recipient of the survey. Choose the Lead or Contact recipient type only when there’s
a default Experience Cloud site selected for sending public surveys.

This parameter accepts flow variable of type Text.

`Unique link` Optional. Each participant receives a unique survey invitation. The responses are mapped to the
participant name.

`Anonymize responses` Optional. The responses received aren’t mapped to any participant.

`Don’t require` Optional. By default, surveys sent to lead or contact require authentication. However, you can enable
`authentication` this option to allow access to the survey without any authentication.

`Invitation expires` Optional. Define the number of days after which the access to the survey is restricted.

```
in days

```

SEE ALSO:

Add and Edit Elements

Flow Core Action: Perform Survey Sentiment Analysis

Get insights into the sentiments that underlie survey responses.

In Flow Builder, add an Action element to your flow. In the Action field, enter _`Sentiment`_, and
##### select Perform Survey Sentiment Analysis . Or, in the left navigation, click Survey, enter Sentiment in the Action field, and select Perform Survey Sentiment Analysis . Define the

name of the action and the survey recipients.

To access this action from the API, use the name `performSurveySentimentAnalysis` .

Set Input Values

**Field** **Description**

`End Date` Required. The date until when participant responses are processed to get
sentiment insights.

`Operation` Required. The action performed on the AI Sentiment Result records.

**•** **Create** : Use the create operation when sentiment analysis is yet to
be done on survey responses and there are no associated AI Sentiment


EDITIONS

Available in: both Salesforce
Classic (not available in all
orgs) and Lightning
Experience

Available in: **Enterprise**,
**Unlimited**, and **Developer**
Editions

Available with Survey
Response Pack, Feedback
Management - Starter, and
Feedback Management Growth licenses

Automate Your Business Processes with Salesforce Flow Flow Reference

**Field** **Description**

Result records, or to analyze the sentiment again. After the processing is completed, AI Sentiment
Result records are created with the sentiment of the survey responses and with the Submitted
status.

**•** **Update** : Use the update operation to bulk process survey responses that have associated AI
Sentiment Result records in Draft status. After the processing is completed, the AI Sentiment
Result records are updated with the sentiment of the survey responses and their status is changed
to Submitted.

`Question IDs` Required. The IDs of the questions for whose responses you want to get sentiment insights.

`Start Date` Required. The date from when participant responses are processed to get sentiment insights.

`Survey ID` Required. The ID of the survey containing the questions for whose responses you want to get sentiment
insights.

Usage

At run time, the AI Sentiment Result record isn’t created until the interview’s transaction is completed. After the transactions are completed,
AI Sentiment Result records are created with Completed status.

Flow Core Action: Get Assessment Response Summary

Create a printable summary view of assessments taken. This action enables you to extract responses
saved in an assessment and create a flow to generate a document.

In Flow Builder, add an Action element to your flow. In the Action field, search for Get Assessment
Response Summary invocable action to configure.

Set Input Values

**Field** **Description**

`assessmentId` Required. The ID of the assessment record for which to summarize responses.

Set Output Values

**Set Field** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`assessmentResponseSummary` A JSON string containing the summary assessment question texts and responses for the specified assessment
record.

Usage

##### Get Assessment Response Summary makes it easy to use a flow to trigger server-side document generation using Docgen. You can use

this invocable action to pass assessment summary data to the downstream processes. This invocable action provides a summary JSON
that can be consumed in Docgen workflows to generate documents.


Automate Your Business Processes with Salesforce Flow Flow Reference

The Get Assessment Response Summary invocable action takes assessment ID as the input to get the OmniProcess ID, which is used to
retrieve the OmniProcess elements. The assessment ID also retrieves the assessment response and merges the response with the
OmniProcess elements to create an assessment summary response in JSON.

DocGen Limitations

OmniScript doesn’t provide a modification history of the same OmniScript form, such as the addition or removal of questions. It’s
recommended that you trigger the document generation when you submit an assessment. The summary API fetches the layout data
from the active version of the OmniScript.

DocGen has the following limits:

**•** Token data is limited to 131,072 characters.

**•** Server-side document generation - Maximum supported document size is 1 MB.

**•** Client-side document generation - Maximum supported document size is 10 MB.

**•** There’s no image-type support for server-side document generation. Image-type support is only available on the client-side.

##### Slack Flow Core Actions

Manage Slack channels, channel members, and messages from flows. As your Salesforce records
change, a flow can trigger changes in Slack.

Important: Slack core actions execute in user context. The flow has access to whatever the
running user of the flow has access to.

Before using a core action for Slack, enable Salesforce for Slack integrations.

##### In Flow Builder, add an Action element to your flow. Select the Slack category, and search for an

action.

Flow Core Actions for Slack: Archive Slack Channel
Archive a Slack channel in a Slack workspace.

Flow Core Actions for Slack: Check If Users Are Connected to Slack
Determine whether a collection of Salesforce users is connected to a given Slack workspace.

Flow Core Actions for Slack: Create Slack Channel
Create a Slack channel in a Slack workspace.

Flow Core Actions for Slack: Edit Slack Message
Edit a message that was previously sent to Slack.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow Core Actions for Slack: Get Information About Slack Conversation
Retrieve the name of a Slack channel and find out whether it’s archived. Archived channels are closed to new activity, but users can
still view and search an archived channel’s message history.

Flow Core Actions for Slack: Invite Users to Slack Channel
Add users who are connected to a given Slack app to a Slack channel or direct message.

Flow Core Actions for Slack: Pin or Unpin Slack Message
Pin or unpin a message in a Slack channel or direct message. Pin messages so that they’re readily available from the conversation
header.

Flow Core Actions for Slack: Send Slack Message
Send a message to a Slack channel, direct message, or the Messages tab of a Slack app.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Message to Launch Flow
Send a message to a Slack channel, direct message, or the Messages tab of a Slack app that includes a button that a recipient can
use to launch a screen flow.

Flow Core Actions for Slack: Archive Slack Channel

Archive a Slack channel in a Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Archive Slack Channel .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Channel

**Input Parameter** **Description**

```
Slack Channel ID

```

Required. The ID of the channel to archive.

Get the Slack channel ID by logging in to Slack.com and launching Slack in your browser.
The channel ID is the last parameter in the URL. For example, in this URL, the channel ID
is `C56789FGHIJ` :


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
                    https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Check If Users Are Connected to Slack

Determine whether a collection of Salesforce users is connected to a given Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Check If Users Are Connected to Slack .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com
and launching Slack in your browser. The workspace ID is the
penultimate parameter in the URL. For example, in this URL, the
workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Salesforce User ID` Required. The collection resource that contains the Salesforce
`Collection Resource` user IDs to check. The maximum number of user IDs is 1,000.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

`Collection of Salesforce` A collection resource that contains the Salesforce user IDs connected to Slack.

```
   User IDs Connected to Slack

```

`Collection of Salesforce` A collection resource that contains the Salesforce user IDs not connected to Slack.

```
   User IDs Not Connected to

   Slack

```

Usage

This action is available only if you enable the connection to Slack in Setup. Otherwise, the action fails. Additionally, the user that initiates
the flow and any users impacted by the action must have logged in to a Salesforce Slack app at least once.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Create Slack Channel

Create a Slack channel in a Slack workspace.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Create Slack Channel .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Slack Channel Details

**Input Parameter** **Description**

`Slack Channel Name` Required. The name of the new channel. Specify a value or select a resource.

`Channel Type` Select a value or Boolean resource. Valid values are:

**•** Public

**•** Private

**•** Resource

If you select a Boolean resource that evaluates to true, the channel type is private. If you
select a Boolean resource that evaluates to false, the channel type is public. The default
channel type is public.

`Slack Workspace ID for` Indicates whether to associate the new channel with a different workspace ID than the
`Channel` workspace ID of the Slack app. If you turn on this option, select a value or resource.

Store Output Values

**OUTPUT Parameter** **Description**

`Slack Channel ID` The ID of the new channel.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Edit Slack Message

Edit a message that was previously sent to Slack.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Edit Slack Message .

Set Input Values

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App ID for

Token

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

The Slack app must be a member of the conversation that
contains the message to edit.

`Slack Conversation` Required. The ID of the channel or the direct message to send
`ID` the message to. Alternatively, specify a Slack user ID if the
message was sent to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to
Slack.com and launching Slack in your browser. The conversation
ID is the last parameter in the URL. For example, in this URL, the
conversation ID is `C56789FGHIJ` :

```
            https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Slack Message` Required. The message to send. Use alongside Post Message
action. For best results, include no more than 4,000 characters.

Slack truncates messages containing more than 40,000
characters. Enter a value or select a resource. This action only
supports editing messages with standard markdown formatting.

Slack supports text formatting with Slack `mrkdown` . To disable
formatting for a plain text message that contains Slack
`mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders
rich text messages as plain text.

```
Slack Message

Timestamp

```

Required. The timestamp of the message sent. Enter a value or
select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix
timestamp. The numerals after the period character specify
microseconds.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

```
Slack Workspace ID for Token

```

Usage

Required. The Slack workspace where the Slack app is installed. Select a value or resource.
The input value evaluates to the Slack workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com and launching Slack
in your browser. The workspace ID is the penultimate parameter in the URL. For example,
in this URL, the workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Get Information About Slack Conversation

Retrieve the name of a Slack channel and find out whether it’s archived. Archived channels are
closed to new activity, but users can still view and search an archived channel’s message history.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Get Information About Slack Conversation .

Set Connection Values for Slack

The flow sends the connection values that you provide to Slack to retrieve an access token.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

The Slack app must be a member of the conversation to execute the action on.

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Slack Conversation

**Input Parameter** **Description**

```
Slack Conversation ID

```

Store Output Values

Required. The ID of the channel to retrieve information about.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

**Output Parameter** **Description**

`Conversation Is Archived` Indicates whether the conversation is archived.

`Conversation Is Shared` Indicates whether the conversation is shared with people outside of your org that aren't
`Externally` part of your Enterprise Grid in Slack.

`Slack Conversation ID` The ID of the Slack conversation that you retrieved information about.

`Slack Conversation Name` The name of the Slack conversation that you retrieved information about.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Invite Users to Slack Channel

Add users who are connected to a given Slack app to a Slack channel or direct message.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Invite Users to Slack Channel .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Channel Details

Use values from earlier in the flow to set the inputs for the action.

**Input Parameter** **Description**

```
Slack Channel ID

```

Required. The ID of the channel or direct message to invite users to.

You can obtain the Slack channel ID by logging in to Slack.com and launching Slack in
your browser. The channel ID is the last parameter in the URL. For example, in this URL,
the channel ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Slack Workspace ID for

Channel

```

Required. The Slack workspace that contains the channel. Select a value or resource. The
input value evaluates to the Slack workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com and launching Slack
in your browser. The workspace ID is the penultimate parameter in the URL. For example,
in this URL, the workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Salesforce User ID` The collection resource that contains the Salesforce user IDs to invite to the channel. The
`Collection Resource` maximum number of user IDs is 1,000.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails. Additionally, the user that initiates the flow and any users impacted by the action must have logged in to a Salesforce
Slack app at least one time.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Actions for Slack: Pin or Unpin Slack Message

Pin or unpin a message in a Slack channel or direct message. Pin messages so that they’re readily
available from the conversation header.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Pin or Unpin Slack Message .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

The Slack app must be a member of the conversation to execute the action on.

**•** User Who Runs the Flow—Execute the action as the user who runs the flow. The user
can execute the action only when the flow runs in the user context. If the flow runs
in the system context, the Slack app executes it.

The user must be a member of the conversation to execute the action on.

Set Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

Slack Message Timestamp

Pin or Unpin Message

```

Usage

Required. The ID of the channel or group direct message to send the message to. Enter
a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

Required. The timestamp of the sent message. Enter a value or select a resource. For
example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

Select a value or Boolean resource. Valid values are:

**Pin**
Pins the message to the conversation header.

**Unpin**
Unpins the message from the conversation header.

If you select a Boolean value that evaluates to true, the action pins the message. If you
select a Boolean value that evaluates to false, the action unpins the message. The default
is Pin.

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Slack Message

Send a message to a Slack channel, direct message, or the Messages tab of a Slack app.

Before using a core action for Slack, enable Salesforce for Slack integrations.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
###### then select Send Slack Message .

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.

Set Slack Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

```

Required. The ID of the channel or direct message to send the message to. Alternatively,
specify a Slack user ID to send the message to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Slack Message

```

Required. The message to send. For best results, include no more than 4,000 characters.
Slack truncates messages containing more than 40,000 characters. Enter a value or select
a resource.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

`Salesforce Record ID` [The record ID to send to the view. Defining a view is a pilot feature. For more information,](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views.html)
[see Define a View in the](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views_create.html) _Apex SDK for Slack (Pilot) Guide_ .

```
Slack Message Timestamp

```

The timestamp of the Slack message. Specify a timestamp to start a Slack thread. Enter a
value or select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

`View API Name` [The API name of the view that the Slack message is sent with. Defining a view is a pilot](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views.html)
[feature. For more information, see Define a View in the](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/views_create.html) _Apex SDK for Slack (Pilot) Guide_ .

Store Output Values

**OUTPUT Parameter** **Description**

`Slack Message Timestamp` The timestamp of the sent message.

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Actions for Slack: Send Message to Launch Flow

Send a message to a Slack channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow.

In Flow Builder, add an Action element to your flow. In the New Action window, select **Slack**, and
then select the name of the flow to send.

Set Connection Values for Slack

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials,**
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Slack App

Slack Workspace

```

Required. The Slack app that executes the action. Only Slack apps
that are installed for the org are available. The input value
evaluates to the Slack app ID.

Required. The Slack workspace where the Slack app is installed.
Select a value or resource. The input value evaluates to the Slack
workspace ID.

You can obtain the Slack workspace ID by logging in to Slack.com
and launching Slack in your browser. The workspace ID is the
penultimate parameter in the URL. For example, in this URL, the
workspace ID is `T01234ABCDE` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Execute Action As` The entity that executes the action. Valid values are:

**•** Slack App—Execute the action as the Slack app that you
selected in the Slack App field. It’s the default value.

The Slack app must be a member of the conversation to
execute the action on.

**•** User Who Runs the Flow—Execute the action as the user
who runs the flow. The user can execute the action only
when the flow runs in the user context. If the flow runs in
the system context, the Slack app executes it.

The user must be a member of the conversation to execute
the action on.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set Slack Message Details

**Input Parameter** **Description**

```
Slack Conversation ID

```

Required. The ID of the channel or the direct message to send the message to. Alternatively,
specify a Slack user ID to send the message to the user via the Messages tab of the Slack
app. Enter a value or select a resource.

You can obtain the Slack conversation ID by logging in to Slack.com and launching Slack
in your browser. The conversation ID is the last parameter in the URL. For example, in this
URL, the conversation ID is `C56789FGHIJ` :

```
https://app.slack.com/client/T01234ABCDE/C56789FGHIJ

```

`Slack Message` Required. The message to send. For best results, include no more than 4,000 characters.
Slack truncates messages containing more than 40,000 characters. Enter a value or select

a resource. The message to send can’t be edited. Using the Edit Message action or manual
editing results in process failures.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

```
Button Label

```

Required. The label for the button that appears below the message. The user clicks the
button to launch the flow from Slack.

Slack supports text formatting with Slack `mrkdown` . To disable formatting for a plain
text message that contains Slack `mrkdown`, use an escape sequence.

Slack doesn’t support text formatting with HTML and renders rich text messages as plain
text.

`Slack Bot Name` The name of the bot that sends the message in Slack. Enter a value or select a resource.

```
Slack Message Timestamp

```

Store Output Values

The timestamp of the Slack message. Specify a timestamp to start a Slack thread. Enter a
value or select a resource. For example, enter _`1234567890.123456`_ .

The numerals before the period character (.) specify a Unix timestamp. The numerals after
the period character specify microseconds.

You can store the Slack Message Timestamp output parameter of the Send Slack Message,
Edit Slack Message, or Send Message To Launch Flow action as a resource to use later.

**Input Parameter** **Description**

`Slack Message Timestamp` The timestamp of the message sent.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

This action is available only if you enable the connection to Slack in Setup and the user who runs the flow is connected to Slack. Otherwise,
the action fails.

SEE ALSO:

[Enable Salesforce for Slack Integrations](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

_Salesforce Admins_ [: How Admins Can Connect Salesforce and Slack](https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack)

Flow Core Action: Submit for Approval

Submit one Salesforce record for approval.

Tip: Before you begin, store the ID for the record that you want to submit for approval in a
variable.

##### In Flow Builder, add an Action element to your flow. In the Action field, enter Submit, and select Submit for Approval .

Set Input Values

Use values from earlier in the flow to set the inputs for the approval request.

**Input Parameter** **Description**

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Record ID

Approval Process

Name or ID

Next Approver IDs

Skip Entry Criteria

```

The ID of the record that you want to submit for approval.

This parameter accepts single-value resources of any type. That value is treated as text.

The unique name or ID of the approval process that you want to submit the record to. The process
must have the same object type as the record you specified in `Record ID` .

Required if `Skip Entry Criteria` is set to _`true`_ .

If this parameter and `Submitter ID` aren’t set, the flow succeeds only when: Make sure that:

**•** The approver on submit is determined automatically, and

**•** The user who launched the flow is an allowed initial submitter

**•** The approver on submit is determined automatically.

**•** The initial submitters for the approval processes related to this object include all users who could
launch this flow.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the user to be assigned the approval request when the approval process doesn’t assign the
approver.

This parameter accepts collection variables of type Text that include exactly one item.

If set to _`true`_, the record isn’t evaluated against the entry criteria set on the process that is defined
in `Approval Process Name or ID` .

This parameter accepts any single-value resource of type Boolean.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
Submission Comments

Submitter ID

```

Store Output Values

Text that you want to accompany the submission. Don’t reference merge fields or formula expressions.

Submission comments appear in the approval history for the specified record. This text also appears
in the initial approval request email if the template uses the `{!ApprovalRequest.Comments}`
merge field.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID for the user who submitted the record for approval. The user receives notifications about
responses to the approval request.

The user must be one of the allowed submitters for the process.

If you don’t set this field, the user who launched the flow is the submitter. If a workflow rule triggers
a flow that includes this element, the submitter is the user who triggered the workflow rule. Workflow
rules can be triggered when a user creates or edits a record. When the record is approved or rejected,
the user who launched the flow or triggered the workflow rule is notified.

This parameter accepts single-value resources of any type. That value is treated as text.

To use the approval request’s outputs later in the flow, store them in variables. The values are assigned when the approval request is
created.

**Optional Output** **Description**
**Parameter**

```
Instance ID

Instance Status

New Work Item IDs

Next Approver IDs

Record ID

```

The ID of the approval request that was submitted.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.

The status of the current approval request. Valid values are Approved, Rejected, Removed, or Pending.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.

The IDs of the new items submitted to the approval request. There can be 0 or 1 approval processes.

This parameter accepts collection variables of type Text.

The IDs of the users who are assigned as the next approvers.

This parameter accepts collection variables of type Text.

The ID of the record that the flow submitted for approval.

This parameter accepts single-value variables of type Text, Picklist, or Multi-Select Picklist.


Automate Your Business Processes with Salesforce Flow Flow Reference

Usage

At run time, the approval request isn’t created until the interview’s transaction is completed. Transactions are complete when the
interview either finishes or executes a Screen, Local Action, or Wait element.

SEE ALSO:

Flow Elements

Add and Edit Elements

Customize What Happens When a Flow Fails

Move and Connect Elements to Change a Flow Route

##### Salesforce Anywhere Core Flow Actions (Beta)

Salesforce Anywhere provides several core actions for implementing Salesforce Anywhere
functionality in flows. To add one of these actions to your flow, add an Action element. Then select
the Salesforce Anywhere category, and search for the appropriate action.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

These actions are available when you enable Salesforce Anywhere.

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

Flow Core Action for Salesforce Anywhere: Create a Salesforce Anywhere Chat (Beta)
Create a Salesforce Anywhere chat by specifying participants, and optionally, an initial message and chat title.

Flow Core Action for Salesforce Anywhere: Add a Message to a Salesforce Anywhere Chat (Beta)
Add a message to an existing Salesforce Anywhere chat by specifying the chat URL and message content.

Flow Core Action for Salesforce Anywhere: Add Users to a Salesforce Anywhere Chat (Beta)
Add users to an existing Salesforce Anywhere chat by specifying the chat URL and the users to be added.

Flow Core Action for Salesforce Anywhere: Send Salesforce Anywhere Alerts to Users (Beta)
Notify users about Salesforce Anywhere chat by specifying the chat URL and the users to be added.

SEE ALSO:

Add and Edit Elements


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Core Action for Salesforce Anywhere: Create a Salesforce Anywhere Chat (Beta)

Create a Salesforce Anywhere chat by specifying participants, and optionally, an initial message
and chat title.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`chat`_ . Select **Create Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the chat.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatMessage

userEmails

```

Store Output Values

The first message sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

A comma-separated list of email addresses belonging to one or more users getting added to the chat. Must
list at least two email addresses and no more than 50 email addresses.

Email addresses must be part of your Salesforce Anywhere organization. If an email address isn’t included in
your Salesforce Anywhere organization, the user isn’t included in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
chatId

chatTitle

chatUrl

```

Usage

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The name users see at the top of the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.

In Flow Builder, this action doesn’t check the number of email addresses or the validity of the email addresses. When either criteria is
invalid, the flow fails at run time.


Automate Your Business Processes with Salesforce Flow Flow Reference

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Add a Message to a Salesforce Anywhere Chat (Beta)

Add a message to an existing Salesforce Anywhere chat by specifying the chat URL and message
content.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`message`_ . Select **Add Message to Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the message.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatUrl

chatMessage

recordId

```

Store Output Values

The chat's URL.

This parameter accepts single-value resources of any type. That value is treated as text.

The message to send to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the Salesforce record to send to the chat. The record's compact layout is displayed in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
chatId

chatMessage

chatUrl

```

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The message sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Output Parameter** **Description**

```
recordId

```

Usage

The ID of the record sent to the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

Only existing chat members can trigger this action. For example, only an existing chat member can successfully run a flow that sends a
message to a chat about a service case when that case record is updated.

A flow can’t create a record and then reference that new record ID as an input for this action.

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Add Users to a Salesforce Anywhere Chat (Beta)

Add users to an existing Salesforce Anywhere chat by specifying the chat URL and the users to be
added.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`users`_ . Select **Add Users to Chat** .

Set Input Values

Use values from earlier in the flow to set the inputs for the new users.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
chatUrl

userEmails

```

The chat's URL.

This parameter accepts single-value resources of any type. That value is treated as text.

Required. A comma-separated list of email addresses belonging to up to 50 users getting added to the chat.

Email addresses must be part of your Salesforce Anywhere organization. If an email address isn’t included in
your Salesforce Anywhere organization, the user isn’t be included in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store Output Values

**Output Parameter** **Description**

```
chatId

chatUrl

chatTitle

```

Usage

The chat’s ID.

This parameter accepts single-value resources of any type. That value is treated as text.

The chat’s URL.

This parameter accepts single-value resources of any type. That value is treated as text.

The name users see at the top of the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

In Flow Builder, this action doesn’t check the number of email addresses or the validity of the email addresses. When either criteria is
invalid, the flow fails at run time.

Only existing chat members can trigger this action. For example, only an existing chat member can successfully run a flow that adds
new users to a chat about a service case when that case record is updated.

The API used for this action has a rate limit of 50 requests per minute and 750 requests per hour.

SEE ALSO:

Add and Edit Elements

Flow Core Action for Salesforce Anywhere: Send Salesforce Anywhere Alerts to Users (Beta)

Notify users about Salesforce Anywhere chat by specifying the chat URL and the users to be added.

Note: Salesforce Anywhere Beta is a Non-GA Service and not a “Service” or part of the
“Services”, as defined in the Main Services Agreement ("MSA") with Salesforce. Such Non-GA
[Service is subject to the terms and conditions of the Universal Pilot Research Agreement](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/Beta-Services-Agreement.pdf)
[("UPRA"), including the Data Processing Addendum to the UPRA. Use of this Non-GA Service](https://c1.sfdcstatic.com/content/dam/web/en_us/www/documents/legal/Agreements/beta-agreements/sfdc-pilot-dpa.pdf)
is at your sole discretion, and any purchase decisions are made only on the basis of Salesforce
generally available products and features.

In Flow Builder, add an Action element to your flow. Select the Salesforce Anywhere category, and
search for _`alert`_ . Select **Send Alert** .

Set Input Values

Use values from earlier in the flow to set the inputs for the alert.

**Input Parameter** **Description**

EDITIONS

Available in: **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Professional**,
**Developer**, and **Unlimited**
Editions

```
alertMessage

```

The message sent in the alert.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Input Parameter** **Description**

```
userEmails

recordId

```

Store Output Values

A comma-separated list of the users’ email addresses.

This parameter accepts single-value resources of any type. That value is treated as text.

The ID of the Salesforce record to send to the chat. The record's compact layout is displayed in the chat.

This parameter accepts single-value resources of any type. That value is treated as text.

**Output Parameter** **Description**

```
eventOperationId

```

SEE ALSO:

The unique ID generated for the alert.

This parameter accepts single-value resources of any type. That value is treated as text.

_Platform Events Developer Guide_ [: Platform Events Considerations](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_event_extras.htm)

Add and Edit Elements

Standard Flow Screen Components

Salesforce provides several standard screen components that extend the types of input fields
available in screens.

If you need more functionality, for example, to install a custom screen component from an external
[library, have a developer build one for you.](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_config_for_flow_screens_intro.htm)

Flow Screen Input Component: Action Button
Use the Action Button component so the running user can trigger a screen action with the click
of a button on a screen. The screen action runs an active autolaunched flow, and the results of
the autolaunched flow can be shown on the same screen as the button. Using this component
means that you need fewer screens so users can complete screen flows more quickly.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow Screen Input Component: Address
Simplify gathering address information by adding the Address component to a flow screen. The Address screen component displays
a complete address form that’s customized to your settings. It can also use state and country/territory picklists.

Flow Screen Input Component: Checkbox
Offer flow users a yes-or-no choice with a checkbox.

Flow Screen Input Component: Checkbox Group
Let users choose multiple options in a checkbox format.

Flow Screen Input Component: Choice Lookup
Let users search for and select one option from a set of choices on a flow screen. The component supports only Text values.

Flow Screen Input Component: Currency
Let users enter currency values from a flow screen.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Data Table
Let users select records from a table in a flow.

Flow Screen Input Component: Date
Let users enter date values from a flow screen.

Flow Screen Input Component: Date & Time
Let users enter date and time values from a flow screen, such as to request an appointment.

Flow Screen Input Component: Dependent Picklists
Display picklists in a flow screen in which the options for one picklist depend on the selected value of another picklist. The Dependent
Picklists screen component determines which options to display in each picklist by using an existing field dependency in your org.
A _field dependency_ connects two picklist fields on the same object.

Flow Screen Input Component: Display Image
Easily insert images in flow screens. Upload images to Salesforce as static resources and then you can reference them while configuring
the component.

Flow Screen Input Component: Email
Let users enter email address values from a flow screen.

Flow Screen Input Component: Enhanced Message
Let users send a messaging component in an enhanced Messaging session.

Flow Screen Input Component: File Upload
Let users upload files from a flow screen.

Flow Screen Input Component: Long Text Area
Let users enter a paragraph or two of text from a flow screen.

Flow Screen Input Component: Lookup
Let users search for and select one or more records in a flow.

Flow Screen Input Component: Multi-Select Picklist
Let users choose multiple options in a picklist format.

Flow Screen Input Component: Name
Let users enter multiple name values with one screen component. Instead of the Name screen component, you can use Text input
fields to capture name information, but it takes a lot more configuration.

Flow Screen Input Component: Number
Let users enter number values from a flow screen.

Flow Screen Input Component: Order Management Product Selector
Let users select which fields show in columns during product selector for various transaction types, such as returns or exchanges.

Flow Screen Input Component: Password
Let users enter sensitive information in a flow screen, such as a social security number. Text entered by the user is masked.

Flow Screen Input Component: Phone
Let users enter phone values from a flow screen.

Flow Screen Input Component: Picklist
Let users choose from a list of options in a picklist format.

Flow Screen Input Component: Radio Buttons
Let users choose from a list of options in a radio button format.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slack Channel Selector
Let users select a Slack channel to send a Slack message from a flow screen.

Flow Screen Input Component: Slack Workspace Selector
Let users select a Slack workspace to send a Slack message to from a flow screen.

Flow Screen Input Component: Slider
Let users visually specify number values from a flow screen.

Flow Screen Input Component: Text
Let users enter text from a flow screen, such as the name of the user’s company.

Flow Screen Input Component: Toggle
Let users flip a toggle in a flow screen.

Flow Screen Input Component: URL
Let users enter URL values in a flow screen.

Flow Screen Output Component: Display Text
Display information in a flow screen.

Flow Screen Display Component: Repeater
Collect information about multiple items of the same type on a screen with the Repeater component. To use the output of the
component elsewhere in the flow, loop over the output and save the relevant data in a variable. Use the variable to build a list of
records.

Flow Screen Output Component: Section
Organize screen components and record fields to give your users a better experience.

Flow Screen Input Component: Action Button

Use the Action Button component so the running user can trigger a screen action with the click of
a button on a screen. The screen action runs an active autolaunched flow, and the results of the
autolaunched flow can be shown on the same screen as the button. Using this component means
that you need fewer screens so users can complete screen flows more quickly.

For example, you can make it possible for users to select an account record in a Lookup component,
click a button to retrieve the contact records associated with the account record, and then display
the contact records in a Data Table component on the same screen.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Action Button Name

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

`Label` If you select Use Label as the table title, the user-friendly text that appears above the component.

```
Disabled

```

Configure the Action

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

**Attribute** **Description**

`Action` The screen action that launches the autolaunched flow. This is the flow that runs when the user clicks
the button rendered by the Action Button component. The autolaunched flow must be active.

`Label` The user-friendly name for the action associated with the component. This value can be different than
the label of the flow that you select as the action.

```
API Name

Set Input Values

View Output Values

```

The API name for the action associated with the component. This value can be different than the API
name of the flow that you select as the action.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

Specify the value of each input field required by the action associated with the component. For
example, if you select an autolaunched flow that requires an Account ID as an input, provide the
Account ID. Variables that are available for input in the autolaunched flow appear in this area.

View the outputs created by the action. To reference an output elsewhere in the flow, first reference
the Results field, for example, `actionButtonApiName. Results.output` . Variables that
are available for output in the autolaunched flow appear in this area. Output values include:

**•** ErrorMessage—Description of an error that occurred while executing the invocable action

**•** IsSuccess—If true, indicates that the invocable action ran without errors

**•** Action.Results.Flow__InterviewGuid—Unique identifier of the flow interview

**•** Action.Results.Flow__InterviewStatus—The status of the flow interview

**•** InProgress—If true, indicates that the screen action is running.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Specify Another Component’s Behavior with the In Progress Output Attribute

When a user clicks an action button, the In Progress attribute for the associated screen action is set to `true` . When the action completes,
the In Progress attribute is set back to `false` .

Use the In Progress attribute to specify another component’s behavior. For example, use it to disable a screen component while the
action is running. Set the value of the Disabled field on the component to the In Progress attribute. When In Progress is `true` the
Disabled field is also set to `true` . When the action completes and In Progress is set to `false`, the disabled field is also set to false.

Considerations

**•** If a user runs a flow with an Action Button component in a web browser, the outputs of the action associated with the component
are available to the browser. Don’t share sensitive information as the output of an Action Button component.

**•** Autolaunched flows that include Wait elements or subflows with Wait elements aren’t supported as Action Button actions because
the flow won’t resume after a Wait element.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Action Buttons aren’t supported in Repeater components.

**•** Launching a flow with an asynchronous path isn’t supported.

**•** If a flow launched from the action button doesn't have fault paths, and an error occurs, a generic error message shows under the
action button. To show a helpful error message to users instead, add fault paths to the launched flow. On each fault path, set an
output variable to `{!$Flow.FaultMessage}` . Then, on the flow screen with the action button, add a Display Text component
that's conditionally hidden and contains a helpful error message along with the fault message variable.

Note: Even if a Display Text component content contains an error message, screen readers don’t announce the content as
an error message.

**•** If an input or output variable in the screen action’s autolaunched flow is a record variable, and you change a field name on the object,
the new field name isn’t reflected when you refresh the inputs and outputs.

**•** If an input or output variable in the screen action’s autolaunched flow is an Apex variable, and you change the structure of the Apex
type, those changes aren't reflected when you refresh the inputs and outputs.

SEE ALSO:

Data Safety When Running Screen and Autolaunched Flows in System Context

_Video_ [: Action Button in Salesforce Flow](https://www.youtube.com/watch?v=GS5GAFHpVGk)

Flow Screen Actions

Flow Screen Input Component: Address

Simplify gathering address information by adding the Address component to a flow screen. The
##### Address screen component displays a complete address form that’s customized to your settings.

It can also use state and country/territory picklists.

For information about adding screen components to your flow screen, see Flow Element: Screen.

Note: This screen component requires Lightning runtime.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Address Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
City Value

Country Code

Country Options

Country Value

Disabled

Label

Postal Code Value

Required

Show Google Maps

Search Field

```

To give City a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The code for the country in the address. To give Country a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The active countries and territories configured in state and country/territory picklists. To override the
options, set this attribute to a comma-delimited set of countries and territories. This field populates a
dropdown menu of options.

This attribute accepts single-value resources. The value is treated as text.

The value for the country in the address. To give Country a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The label for the heading that appears above the group of address fields.

This attribute accepts single-value resources. The value is treated as text.

To give Postal Code a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

Indicates whether to include a search field powered by Google Maps in the component. To include
a search field, enter `true` as a boolean value. When a user selects an address in the search field, the
flow populates the other fields in the component.

The default value is `false` .

`Google Maps Search` The label that appears above the Google Maps search field.

```
Field Label

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
State or Province

Code

State or Province

Options

State or Province

Value

Street Value

```

The code for the state or province in the address. If `State/Province Options` is configured,
this value is selected by default. To give State a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

The active states configured in state and country/territory picklists. To override the options, set this
attribute to a comma-delimited set of states. This field populates a dropdown menu of options.

This attribute accepts single-value resources. The value is treated as text.

The value of the state or province in the address. If `State/Province Options` is configured,
this value is selected by default. To give State a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

To give Street a default value, set this attribute's value.

This attribute accepts single-value resources. The value is treated as text.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Store the Address Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
City Value

Country Code

Country Value

Postal Code Value

State or Province

Code

State or Province

Value

Street Value

```

What the user entered in the City Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Country Code field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Country Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Postal Code Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the State or Province Code field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the State of Province Value field. To update records in orgs with the State
and Country/Territory Picklists setting enabled, use State or Province Code instead.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Street Value field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
##### Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio

Buttons, and Text components.

**•** To update records in orgs with the State and Country/Territory Picklists setting enabled, use the Country Code and State or Province
Code outputs instead of the Country Value and State or Province Value outputs.

**•** The Google Maps search fields isn’t supported in Playground, Experience Builder sites, Lightning Out, Lightning Components for
Visualforce, and standalone apps.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Checkbox

Offer flow users a yes-or-no choice with a checkbox.

Configure the Checkbox Component

**Attribute** **Description**

```
API Name

Default Value

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Usage

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
##### Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio

Buttons, and Text components.

When the user selects the checkbox, the screen component evaluates to `true` . If the user doesn’t select the checkbox, the screen
component evaluates to `false` . If the associated screen isn’t executed, the screen component evaluates to `null` .

Example: Let users opt into a marketing campaign, agree to a follow-up call after a purchase, or confirm that they understand
an important policy.

SEE ALSO:

Flow Resource: Global Constant

Standard Flow Screen Components

Flow Screen Input Component: Checkbox Group

Let users choose multiple options in a checkbox format.

Configure the Checkbox Group Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become available:

**•** Checkbox Group

**•** Multi-select Picklist

`Data Type` Only Text choices are supported for this component.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

When a user clicks the info bubble for a Checkbox Group component, the help text appears in a separate window. For other types of
Salesforce-provided components, the help text appears in a popover.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Choice Lookup

Let users search for and select one option from a set of choices on a flow screen. The component
supports only Text values.

Configure the Choice Lookup Component

**Attribute** **Description**

`Label` User-friendly text that appears above the component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

`Require` Requires users to select a value before they can move to the next screen.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

Placeholder Text

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

`Let Users Select` Specifies whether the user can choose only one option or multiple options. The user can select up to
`Multiple Options` 25 options.

```
Choice

```

Add at least one Choice resource such as a record choice set or picklist choice set to this component.
Available only when you add a choice component to the screen component.

If you select a dynamic Choice resource such as a collection choice set or record choice set, ensure
that each value in the Choice resource is unique. Otherwise, if a user selects a duplicate value, the
value is set incorrectly in Salesforce.

You can’t reorder choices or select the same choice twice. Choices must be compatible with the
component’s `Data Type` setting.

Access the Choice Lookup Component’s Values in the Flow

The flow stores these attributes automatically. You can’t store output values for the Choice Lookup component manually.

**Attribute** **Description**

```
selectedChoiceLabels

selectedChoiceValues

```

If users can select only one option, the label of the choice option that the user running the flow
selected.

If users can select multiple options, the semi-colon separated labels of all the choice options the user
running the flow selected.

Reference the value later in the flow as `{!choiceLookup.selectedChoiceLabels}` .

If users can select only one option, the value of the choice option that the user running the flow
selected.

If users can select multiple options, the semi-colon separated values of all the choice options the user
running the flow selected.

Reference the value later in the flow as `{!choiceLookup.selectedChoiceValues}` .

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Choice Lookup flow screen component isn’t compatible with mobile devices or standalone Aura apps.

**•** The component searches for matches only in the Choice Label field of the Choice resource that you specify.

**•** Like other Choice fields, the Choice Lookup component supports the Was Selected operator.

**•** The search is case-sensitive.

**•** Initially, 20 choice options display. As you scroll, more choice options load in groups of 100, up to the maximum of 1,020.

**•** If you apply a filter after loading your initial choices, the display resets, showing the new 20 choices.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** The Choice Lookup component doesn’t support the Display text input field for Choice resources. For example, if you select the
Display text input checkbox when you configure a Choice resource and add the resource to the Choice Lookup component, the
component doesn’t display a text input field when the user selects the corresponding choice at run time.

SEE ALSO:

Choose a Lookup Option for a Flow Screen

Flow Screen Input Component: Currency

Let users enter currency values from a flow screen.

Configure the Currency Component

**Attribute** **Description**

```
API Name

Decimal Places

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Controls the number of digits to the right of the decimal point up to 17
places. If you leave this field blank or set it to zero, only whole numbers
appear when your flow runs.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The
default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Data Table

Let users select records from a table in a flow.

Configure the Data Table Name

**Attribute** **Description**

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` If you select Use Label as the table title, the user-friendly text that appears
above the component.

`Use Label as` Indicates whether to display the Label value above the table when you
`the table` run the flow.

```
title

```

Configure the Data Table Source

**Attribute** **Description**

`Source Collection` A collection of records to use to populate the table.

`Show search bar` Enables users to search and filter their record results.

Configure the Data Table Rows

**Attribute** **Description**

```
Row Selection Mode

```

Indicates how many rows the user can select in the table. You can set the value to:

**Multiple**
The user can select any number of rows between the Minimum Row Selection and Maximum
Row Selection values.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**Single**
The user can select up to one row.

**View only**
The user can’t select any rows.

`Minimum Row` Specifies the minimum number of rows that the user must select.

```
   Selection

```

`Maximum Row` Specifies the maximum number of rows that the user can select.

```
   Selection

```

`Default Selection` Collection that specifies which records to preselect in the table.

`Require user to make` Specifies whether the user must select a row before navigating to the next screen.

```
   a selection

```

Configure the Data Table Columns

To add the first column to the table, configure these fields. To add subsequent columns, click **Add column** . Drag and drop the columns
to reorder them.

**Attribute** **Description**

```
Source Field

```

Field from the Source Collection object to display in the column.

Fields with the anyType data type such as the NewValue field of the AccountHistory object aren’t
supported.

`Custom column label` Indicates whether to display the column Label value you specify as the column header.

`Label` If Custom column label is selected, the text to display as the column header. The text is also read by
screen readers.

```
Default Text

Overflow Mode

```

Specifies how text that is longer than the width of the column appears. You can set the value to:

**Wrap Text**
The screen displays the text on multiple lines.

**Clip Text**
The screen truncates the text to fit.

Note: If you're using a field that has a namespace, add the namespace to the beginning of the source field. For example, if your
field's namespace is Acme, enter _`Acme__FieldName__c`_ .

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Store the Data Table Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but most likely you must store these attributes.

**Attribute** **Description**

`First Selected Row` First record in the table selected by the flow user. If a user selects two records, this record is the first
selected record from top to bottom.

`Selected Rows` The list of records that the user selects. The records are ordered according to their position in the table
from top to bottom.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Data Table flow screen component isn’t compatible with mobile devices.

**•** If you use the Get Records flow element to retrieve the records to display in the Data Table, select Choose fields and let Salesforce
do the rest for the best performance.

**•** The maximum height of a Data Table is 400 pixels.

**•** If you choose to wrap the text in a Data Table, ensure that the text doesn’t overflow when you test your flow. Wrapped text can
overflow when a Data Table is compressed on a screen, for example, when it’s in one of multiple columns.

**•** A Data Table can display up to 1,500 records. However, your search is performed on the entire dataset.

**•** You can select up to 200 records in a Data Table.

**•** If you apply a filter after loading your initial records, only the new results are shown. The initial records are no longer included in the
display.

**•** If a Data Table includes a formula field and records or updates to records that haven’t been committed to the database, the table
doesn’t evaluate the formula properly.

For records that don’t exist in the database, update the value of the formula field with an assignment using a static value or Formula
resource. Doing so doesn’t affect any subsequent Create or Update operations in the flow.

For existing records that have been updated, use an invocable action to reevaluate the formula, or use the IN operator to refresh the
records and formula field values.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** If you include a lookup or master-detail relationship field in a Data Table, the table doesn’t display the field value. For example, a
Data Table can’t display the Name field of a related record. To display field values from related records, use object formula fields. You
can also use object formula fields to link to related record fields, for example:

```
    HYPERLINK( "/" & CASESAFEID(Id), Related_Record__r.Name, "_self" )

```

**•** You can’t search the Time field.

**•** In multi-currency orgs, the Data Table component doesn’t support records that are in a different currency from the user’s personal
currency.

**•** To display multilingual column header labels in the Data Table component, use the `$Label` global variable to specify custom
[labels. For more information about creating and translating custom labels, see Custom Labels.](https://help.salesforce.com/s/articleView?id=sf.cl_about.htm&type=5&language=en_US)

**•** [Data Table selections at runtime are subject to the client payload data limit described in Lightning Aura Components Developer](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_actions_call.htm)
[Guide. If you exceed this limit, the flow returns a generic error message. For example, if you include file data that exceeds the limit,](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_actions_call.htm)
the flow generates an error. We recommend avoiding fields like the VersionData field of ContentVersion records in your source
collection.

**•** If you rename a field in Object Manager that’s mapped to a column in a Data Table, Salesforce doesn’t update the column name. To
see the new name in the Data Table, remove the column and then add it again.

**•** If you have a flow open that has a Data Table component, and you update your user settings time zone on another page, refresh
the flow page to show the updated date and time fields in the Data Table component.

**•** When you set the row selection, be careful if you want to use the row selection of another Data Table component. Salesforce doesn’t
support the use of row selections that have duplicate record variables without record IDs.

**•** If you set the row-selection mode to single and make it required, or if you set the minimum and maximum row selection to 1,
Salesforce uses a radio button at run time. Otherwise, we use checkboxes at run time.

**•** If you package a flow that has a Data Table component, the fields used in the Data Table aren't automatically added to the package.
If you use a field in the Data Table component, you must manually add it to the package.

**•** If you delete a custom field that a Data Table component uses, you must also remove the field from the screen flow where the Data
Table component is used.

**•** If you use a Data Table component that uses a custom object or custom field in an org without a namespace, and then later add a
namespace to the org, you must also add that namespace to the associated column fields in the Data Table.

SEE ALSO:

Use Multilingual Labels in Data Table Column Headers

Data Safety When Running Screen and Autolaunched Flows in System Context

Flow Screen Input Component: Date

Let users enter date values from a flow screen.

Configure the Data Component

**Attribute** **Description**

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Default Value` Pre-populated value for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Date & Time

Let users enter date and time values from a flow screen, such as to request an appointment.

Configure the Date & Time Component

**Attribute** **Description**

```
API Name

Default Value

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Dependent Picklists

Display picklists in a flow screen in which the options for one picklist depend on the selected value
of another picklist. The Dependent Picklists screen component determines which options to display
in each picklist by using an existing field dependency in your org. A _field dependency_ connects two
picklist fields on the same object.

Note: This screen component requires Lightning runtime.

Configure the Dependent Picklists Component

Tip: Before you add a Dependent Picklists screen component to your flow, define field
dependencies for the appropriate picklist fields in your org.

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

**Attribute** **Description**

`API Name` The API name of the component.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Object API Name

Picklist 1 API Name

Picklist 1 Label

Picklist 1 Required

Picklist 1 Value

Picklist 2 API Name

Picklist 2 Label

Picklist 2 Required

Picklist 2 Value

Picklist 3 API Name

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The API name of the object. The picklist fields that you identify in Picklist 1 API Name, Picklist 2 API
Name, and Picklist 3 API Name must be associated with this object.

This attribute accepts single-value resources. The value is treated as text.

The API name of the first picklist field. For the specified object, this picklist field must be the controlling
field in a field dependency between Picklist 1 and Picklist 2.

This attribute accepts single-value resources. The value is treated as text.

The label for the first picklist field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the first picklist field. Configuring this attribute pre-selects an option for the
field.

This attribute accepts single-value resources. The value is treated as text.

The API name of the second picklist field. For the specified object, this picklist field must be the
dependent field in a field dependency between Picklist 1 and Picklist 2. If you display a third picklist
field, Picklist 2 must be the controlling field in a field dependency between Picklist 2 and Picklist 3.

This attribute accepts single-value resources. The value is treated as text.

The label for the second picklist field.

This attribute accepts single-value resources. That value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the second picklist field. Configuring this attribute pre-selects an option for
the field.

This attribute accepts single-value resources. The value is treated as text.

The API name of the third picklist field. For the specified object, this picklist field must be the dependent
field in a field dependency between Picklist 2 and Picklist 3.

This attribute accepts single-value resources. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Picklist 3 Label

Picklist 3 Required

Picklist 3 Value

```

The label for the third picklist field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

The default selection for the third picklist field. Configuring this attribute pre-selects an option for the
field.

This attribute accepts single-value resources. The value is treated as text.

Note: If your org has a namespace, add the namespace to the beginning of the object's API name, and each picklist API Name.
For example, if you have a custom object called Insurance_Agent__c, and your org's namespace is Acme,
enter _`Acme__Insurance_Agent__c`_ .

Store the Dependent Picklists Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
Picklist 1 Value

Picklist 2 Value

Picklist 3 Value

```

What the user selected for the first picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

What the user selected for the second picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

What the user selected for the third picklist field.

You can store this value in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Example: For example, in a Dinner Order flow, users select a specific dessert. Each dessert comes in different flavors, and the
flavor options change based on the dessert that the user selects.

**•** On the Guest Order custom object, define two picklist fields: Dessert and Flavor.

**•** Define a field dependency between Dessert and Flavor, where Dessert is the controlling picklist. Identify which Flavor options
apply to each Dessert option.

**•** In your flow screen, add a Dependent Picklists screen component. Configure the component with these values.

**Attribute** **Value**

`Object API Name` Guest_Order__c

`Picklist 1 API` Dessert__c

```
  Name

```

`Picklist 1 Label` Dessert

`Picklist 2 Value` Flavor__c

`Picklist 2 Label` Flavor

When a user runs the flow, the options for Flavor change based on what’s selected for Dessert.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

Screen input component values are set to null when they’re hidden by conditional visibility. But hidden picklists in a Dependent Picklists
component aren’t set to null unless the entire Dependent Picklists component is hidden.

SEE ALSO:

Standard Flow Screen Components

[Define Dependent Picklists](https://help.salesforce.com/s/articleView?id=sf.fields_defining_field_dependencies.htm&language=en_US)

Flow Screen Input Component: Display Image

Easily insert images in flow screens. Upload images to Salesforce as static resources and then you
can reference them while configuring the component.

For information about adding screen components to your flow screen, see Flow Element: Screen.

Note: This screen component requires Lightning runtime.

Configure the Display Image Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Horizontal

Alignment

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

If you don't want the browser to determine the image's horizontal
alignment, enter a specific alignment value. Valid values are: left, center,
or right.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Image Alt Text

Image CSS

Image Height

Image Name

Image Width

```

Alternative text for screen readers and other assistive technology and for browsers that can’t load the
image. Provide a meaningful description unless the image is purely decorative or redundant.

To have assistive technology skip the image, set `Image Alt Text` to `{`
`!$GlobalConstant.EmptyString}` .

If you don't set this attribute, assistive technology reads the file path from the image source ( `img`
`src` ), which can confuse your users and potentially create an accessibility compliance issue.

This attribute accepts single-value resources. The value is treated as text.

Override the CSS for your image by providing your own CSS string. Example: `border-radius:`

```
8px; box-shadow: 10px 5px 5px blue; opacity: 0.75;

```

This attribute accepts single-value resources. The value is treated as text.

If you don't want the browser to determine the image height, enter a specific height value. Valid values
are a number and unit, or a percentage of the container. Examples: 200 px, 2 cm, 50%. If you enter a
number value and don’t enter a unit value, the unit value defaults to pixels.

This attribute accepts single-value resources. The value is treated as text.

Required. The name of a static resource that contains an image file. The image must be a `.png` or
`.jpg` file.

This attribute accepts single-value resources. The value is treated as text.

If you don't want the browser to determine the image width, enter a specific width value. Valid values
are a number and unit, or a percentage of the container. Examples: 200 px, 2 cm, 50%. If you enter a
number value and don’t enter a unit value, the unit value defaults to pixels.

This attribute accepts single-value resources. The value is treated as text.

Store the Display Image Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Email

Let users enter email address values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Email Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Label

Placeholder Text

Read Only

Required

Value

```

The label that appears above the email field.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the email field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Email Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the email address that the user entered, store the Value attribute in a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Enhanced Message

Let users send a messaging component in an enhanced Messaging session.

Configure the Enhanced Message Component

EDITIONS

Messaging is available in:
Lightning Experience with
the Digital Engagement
add-on SKU

Messaging is available in:
**Enterprise**, **Unlimited**, and
**Developer** Editions with
Service Cloud or Sales Cloud


Automate Your Business Processes with Salesforce Flow Flow Reference

SEE ALSO:

Standard Flow Screen Components

_Salesforce Help_ [: Send Structured Content with Messaging Components](https://help.salesforce.com/s/articleView?id=sf.messaging_components_parent.htm&language=en_US)

Flow Screen Input Component: File Upload

Let users upload files from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the File Upload Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

```
Accepted Formats

```

Using the format _`.ext`_, enter a comma-separated list of the file extensions that the user can upload.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Allow Multiple Files

```

If set to _`$GlobalConstant.True`_, the user can upload multiple files.

This attribute accepts single-value Boolean resources.

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

File Upload Label

Hover Text

Related Record ID

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Required. Label that appears above the upload button.

This attribute accepts single-value resources. The value is treated as text.

Tooltip that appears when the user hovers over the component.

This attribute accepts single-value resources. The value is treated as text.

Required. ID of the record to associate the files with. If no value is passed, the component is disabled.

This attribute accepts single-value resources. The value is treated as text.

Note: Custom fields added to the ContentVersion object page are rendered in Experience Cloud sites through the
contentVersionEditWizard. The contentVersionEditWizard is supported on desktop, but not mobile. Since there’s no screen in
mobile to edit or add details to custom fields, file uploads fail when custom fields are marked as required.

Store the File Upload Component’s Values in the Flow

All attributes are available to store in flow variables, but usually you must store one of these attributes. The values are assigned to the
flow variables when the user navigates to the next screen.

**Attribute** **Description**

```
Content Document IDs

Uploaded File Names

```

The IDs of the uploaded files.

You can store this value in a Text collection variable.

The names of the uploaded files.

You can store this value in a Text collection variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

File Upload Limits

By default, you can upload up to 10 files simultaneously, unless Salesforce changed that limit. The org limit for the number of files
simultaneously uploaded is 25 files with a minimum of one file. The maximum file size you can upload is 2 GB. In Experience Cloud sites,
the file size limits and types allowed follow the settings determined by site file moderation. By default, guest user files are blocked from
being uploaded. Admins can change the settings to let guest users upload files. From **Setup**    - **, select**    - **General Settings**, and then
select **Allow site guest users to upload files** . This setting is only valid if the Secure guest user record access setting is enabled in the
org.

Note: The file upload component isn’t supported on mobile app or browser when used with flows that are accessed through
URLs. This restriction doesn’t apply when the file upload component is used in Lightning App Builder or Experience Builder.

Lightning Out doesn’t support the File Upload component.

Considerations

If a user doesn’t upload any files, the value of the `Content Document IDs` and `Uploaded File Names` outputs is an empty
collection, represented as `“[]”` . If you check the ISBLANK or ISNULL operator, the value is always `false` .

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Long Text Area

Let users enter a paragraph or two of text from a flow screen.

Configure the Long Text Area Component

**Attribute** **Description**

```
API Name

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Lookup

Let users search for and select one or more records in a flow.

Configure the Lookup Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Field API Name

Label

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The API name of a lookup field on the source object referenced in Object
API Name.

The lookup field referenced in Field API Name must be a field on the object
referenced in Object API Name.

For example, if you want to add a lookup for an account, find an object
that has an account lookup field on it. In this case, let’s use the account
lookup field on the Contact object. The API name of the account lookup
field on the Contact object is AccountId, so enter _`AccountId`_ for Field
API Name, then enter _`Contact`_ for Object API Name.

The text that shows at the top of the component that tells the running
user how to use the screen component. For example, if you’re adding an
account lookup, the label could be Select Account.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Object API Name` The API name of the source object that has the lookup field referenced in Field API Name.

The source object can be any object that has the type of lookup field that you want to use.

The lookup field referenced in Field API Name must be a field on the object referenced in Object AI
Name.

To use the Lookup component, the running user of the flow must have the Create permission on the
source object.

For example, if you want to add a lookup for a contact, find an object that has a contact lookup field
on it. In this case, let’s use the contact lookup field on the Case object. The API name of the Case object
is Case, so enter _`Case`_ for Object API Name, then enter _`ContactId`_ for Field API Name.

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Maximum Selections` The maximum number of records that the user can select. The default value is 1.

```
Record Id

Record Id Collection

Required

```

Initially, if Maximum Selections is _`1`_ or Maximum Selections is greater than 1 and the Record ID
Collection field is _`null`_, the record ID selected by default for the lookup.

When a user runs the flow, the value changes to the flow user’s selection.

Initially, if Maximum Selections is greater than 1, the default record IDs for the lookup.

If Maximum Selections is greater than 1 and the Record ID field is _`null`_, the first value is the record
IDs selected by default for the lookup.

You can specify any number of record IDs up to the Maximum Selections value.

When a user runs the flow, the value changes to the flow user’s selections.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

Note: If your org has a namespace, add the namespace to the beginning of the object's API name, and field's API Name. For
example, if you have a custom object called Insurance_Agent__c, and your org's namespace is Acme,
enter _`Acme__Insurance_Agent__c`_ .

Store the Lookup Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but most likely you must store these attributes.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Record ID

Record ID Collection

Record Name

```

If the Maximum Selections value is 1, the ID of the record that the user selects.

You can store this value in a Text variable.

If the Maximum Selections value is greater than 1, the list of IDs of the records that the user selects.

If the Maximum Selections value is 1 and Record ID is null, the first value in the collection is the ID of
the record that the user selects.

You can store this value in a Text collection variable.

If the Maximum Selections value is 1, the value of the Name field of the record that the user selects.

If the Maximum Selections value is greater than 1, the value of the Name field of the first record that
the user selects.

You can store this value in a Text variable.

This value isn’t populated when the Name field of the record is an external object.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** The Lookup flow screen component isn’t compatible with mobile devices or standalone Aura apps.

**•** Dependent lookup filters aren’t enforced for the Lookup component in a flow. Other lookup filters are enforced the same as they
are in Lightning Experience record pages. When the flow accesses the Salesforce database, lookup filters are enforced. For example,
when the flow executes the Create Records element, the flow fails if the value of the lookup field doesn’t meet the lookup filter
requirements.

**•** To filter records based on resources and information from the flow, consider using a Choice Lookup component.

**•** A custom lookup field to a user record isn’t supported.

Tip: To let a flow user choose from a list of user records, employ a standard User lookup field like `CreatedById` or
`LastModifiedById` . `OwnerId` isn’t supported.

**•** At run time, when the flow user types two characters in the field, it shows up to five recent records whose `Name` field matches the
query.

**•** Dependent lookup filters aren’t supported.


Automate Your Business Processes with Salesforce Flow Flow Reference

**•** During run time, if the lookup field defined in `Field API Name` isn’t on an assigned page layout, the lookup component displays
`Search undefined...` . To display the correct text, add the defined lookup field to all of the source object’s page layouts that
are assigned to running users.

**•** Invalid Record IDs are ignored. A Record ID is invalid if it isn’t a valid Salesforce Record ID or its key prefix doesn’t match with the field
API name object.

**•** If the Maximum Selections value is 1 and the Record ID Collection and Record ID are both changed, the Record ID takes precedence.
The Record ID Collection is ignored.

**•** If the Maximum Selections value is greater than 1, the Record ID Collection takes precedence when Record ID is populated. But, if
Record ID Collection isn’t populated, the Record ID is used to populate Record ID Collection as a single it

**•** Relationship fields that are related to more than one object, also known as polymorphic fields, aren’t supported. For example, because
a task record’s WhoId field can be related to a contact or a lead, it isn’t supported for this component.

**•** `Field API Name` and `Object API Name` are case-sensitive.

**•** The Lookup flow screen component doesn’t support filtering by the source object record type.

SEE ALSO:

Standard Flow Screen Components

[Considerations for Lookup Filters](https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters_notes.htm&language=en_US)

[The Enhanced Page Layout Editor](https://help.salesforce.com/s/articleView?id=sf.customize_layoutcustomize_pd.htm&language=en_US)

Flow Screen Input Component: Multi-Select Picklist

Let users choose multiple options in a picklist format.

Configure the Multi-Select Picklist Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become
available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become
available:

**•** Checkbox Group


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**•** Multi-select Picklist

`Data Type` Only Text choices are supported for this component.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** Rich text isn’t supported in the Multi-Select Picklist component.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Name

Let users enter multiple name values with one screen component. Instead of the Name screen
component, you can use Text input fields to capture name information, but it takes a lot more
configuration.

Note: This screen component requires Lightning runtime.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Configure the Name Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Fields to Display

First Name

Informal Name

Label

Last Name

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

By default, the component displays only the First Name and Last Name fields, but other fields are
available. To customize which fields to display at run time, set this attribute to a comma-separated
list of the field names.

**•** For First Name, use firstName

**•** For Last Name, use lastName

**•** For Middle Name, use middleName

**•** For Informal Name, use informalName

**•** For Salutation, use salutation

**•** For Suffix, use suffix

This attribute doesn’t control the order that the fields display in.

For example, to display all the fields, set this attribute to _`firstName, lastName,`_
_`middleName, informalName, salutation, suffix`_ .

This attribute accepts single-value resources. The value is treated as text.

The value of the First Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

The value of the Informal Name field. Setting this attribute prepopulates the field. To use the value
that the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

The label that appears above the name fields.

This attribute accepts single-value resources. The value is treated as text.

The value of the Last Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Middle Name

Read Only

Salutation

Salutation Options

Suffix

```

The value of the Middle Name field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The value of the Salutation field. Setting this attribute prepopulates the field. To use the value that
the user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

By default, the options for Salutation are Mr., Mrs., and Ms. To override these options, set this attribute
to a comma-separated list of values.

This attribute accepts single-value resources. The value is treated as text.

The value of the Suffix field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Name Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables. Most likely, you must store one of these attributes.

**Attribute** **Description**

```
First Name

Informal Name

Last Name

Middle Name

Salutation

```

What the user entered in the First Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Informal Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Last Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Middle Name field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

What the user entered in the Salutation field.

This value can be stored in a single-value Text variable or a Text field on a record variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Suffix

```

What the user entered in the Suffix field.

This value can be stored in a single-value Text variable or a Text field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Number

Let users enter number values from a flow screen.

Configure the Number Component

**Attribute** **Description**

```
API Name

Decimal Places

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Controls the number of digits to the right of the decimal point up to 17
places. If you leave this field blank or set it to zero, only whole numbers
appear when your flow runs.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Order Management Product Selector

Let users select which fields show in columns during product selector for various transaction types,
such as returns or exchanges.

Configure the Order Management Product Selector Component

[Note: This screen component requires Lightning runtime.](https://help.salesforce.com/s/articleView?id=sf.flow_distribute_runtime.htm&language=en_US)

Set the product fields by using data in the flow.

**Attribute** **Description**

Configure Columns Required. Select up to ten columns to display.

Order Product Required. A collection of product summaries.
Summaries

Selected Order Required. The subset collection of product summaries being changed.
Product Summaries

Selected Order Required. The order summary that the product summaries belong to.
Summary


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

Transaction Type Optional. The type of transaction. Valid values are Cancel, RMS, Return, Reship, Discount, and Exchange.

Attributes to Output

**Attribute** **Description**

Order Product Summaries A collection of product summaries.

Selected Order Summary The selected order summary.

Selected Order Product The subset collection of product summaries being changed.
Summaries

Transaction Type The type of transaction.

Flow Screen Input Component: Password

Let users enter sensitive information in a flow screen, such as a social security number. Text entered
by the user is masked.

Note: This screen component doesn’t encrypt the value entered by the user. When the flow
references a Password screen component, such as in an Assignment element or a Display
Text screen component, the value isn’t masked.

Configure the Password Component

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Default Value

Disabled

```

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Phone

Let users enter phone values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Phone Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Label

Disabled

Pattern

Placeholder Text

Read Only

Required

Value

```

The label that appears above the phone field.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

Determines whether the value is valid. By default, there’s no pattern.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts a resource with a single value. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the phone field. Setting this attribute prepopulates the field. To use the value that the
user enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.

Store the Phone Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the phone number that the user entered, map the Value attribute to a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Picklist

Let users choose from a list of options in a picklist format.

Starting with Flow Run-time API version 52, the first option listed for all picklists is --None--. If you
don’t set a default value for a picklist in Flow Builder, the --None-- option is automatically selected
at run time. --None-- is treated as a null value. If you set the picklist as required and the user selects
--None--, then the flow run time prevents the user from proceeding to the next screen.

Configure the Picklist Component

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.

`Component Type` Modify a choice component type.

If the user can select only one option, these component types become
available:

##### • Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become
available:

**•** Checkbox Group

**•** Multi-select Picklist


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Data Type` Controls which choices are available for this component. For example, if you choose Number, you
can’t select a Text choice.

```
Decimal Places

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your flow runs.

Available only when the data type is Number or Currency.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

Considerations

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

**•** Rich text isn’t supported in the Picklist component.

SEE ALSO:

Standard Flow Screen Components

Flow Screen Input Component: Radio Buttons

Let users choose from a list of options in a radio button format.

Configure the Radio Buttons Component

**Attribute** **Description**

```
API Name

Choice

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Add at least one choice, record choice set, or picklist choice set to this
component. Available only when you add a choice component to the
screen component.

If you select a dynamic Choice resource such as a collection choice set or
record choice set, ensure that each value in the Choice resource is unique.
Otherwise, if a user selects a duplicate value, the value is set incorrectly
in Salesforce.

All multi-select choice components use a text data type, but radio buttons
and picklists can also use numbers or Boolean choices.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Component Type` Modify a choice component type.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

If the user can select only one option, these component types become available:

**•** Picklist

**•** Radio Buttons

If the user can select multiple options, these component types become available:

**•** Checkbox Group

**•** Multi-select Picklist

`Data Type` Controls which choices are available for this component. For example, if you choose Number, you
can’t select a Text choice.

```
Decimal Places

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your flow runs.

Available only when the data type is Number or Currency.

`Default Value` Pre-selected choice for the component. If the associated screen isn’t executed or the conditions for
component visibility aren’t met, the stored value of the component is `null` .

```
Disabled

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Label` The text that appears with the screen component that tells the running user how to use it.

```
Let Users Select

Multiple Options

```

Specifies whether the user can choose only one option or multiple options. When you select Yes for
Let Users Select Multiple Options, Data Type is automatically set to Text, and non-text Choice resources
are cleared from the component configuration.

`Provide Help` Give your users more context with this screen component. The text you enter is available in an info
bubble next to the component.

`Require` Requires users to select a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: Slack Channel Selector

Let users select a Slack channel to send a Slack message from a flow screen.

Configure the Slack Channel Selector Component

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

Note: This screen component requires Lightning runtime.

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

`Slack app id` The ID of the Slack app connected to Salesforce. This attribute accepts Text variables.

[Only the Slack app owner can get the app ID. From https://api.slack.com, go to your apps, then Basic](https://api.slack.com)
Information, and find the app’s ID.

`Slack workspace id` The ID of the Slack workspace where the Slack app is installed. This attribute accepts Text variables.

To get the ID, open the web version of Slack and copy the alphanumeric section of the Slack URL
starting with T.

`Use Bot Token` Fetches a list of Slack channels based on the Slack app’s bot token.

This attribute accepts Boolean resources. If set to `$GlobalConstant.False`, the Slack app uses
the user token instead of the bot token.

`Use Channel Search` Indicates whether to use type-ahead Slack channel search to fetch a list of Slack channels.
```
   API
```

This attribute accepts Boolean resources. Requires that the Slack app be registered with Slack to use
the private API.

```
Label for dropdown

Placeholder for

dropdown

Required

```

Text that appears in the selector heading. Use text to give users a hint of what the Slack channel
selector is for.

This attribute accepts single-value resources. The value is treated as text.

Text that appears in the field when it’s empty. Use placeholder text to give users a hint about what
to enter in the field.

This attribute accepts single-value resources. The value is treated as text.

If set to `$GlobalConstant.True`, the running user must enter a value.

This attribute accepts single-value Boolean resources.

`Selected channel id` The ID of the selected Slack channel.

To get the channel ID, right-click the channel and select **View channel details** . The Channel ID is on
the About tab.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slack Workspace Selector

Let users select a Slack workspace to send a Slack message to from a flow screen.

Configure the Slack Workspace Selector Component

You can select resources from the flow, such as variables or global constants, or you can manually
enter a value.

Note: This screen component requires Lightning runtime.

**Attribute** **Description**

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
API Name

Slack appID

Workspace ID

Select...

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The ID of the Slack app connected to Salesforce. This attribute accepts
Text variables.

[Only the Slack app owner can get the app ID. From https://api.slack.com,](https://api.slack.com)
go to your apps, then Basic Information, and find the app’s ID.

The ID of the Slack workspace where the Slack app is installed. This
attribute accepts Text variables.

To get the ID, open the web version of Slack and copy the alphanumeric
section of the Slack URL starting with T.

Text that appears in the field when it’s empty. Use placeholder text to
give users a hint about what to enter in the field.

This attribute accepts single-value resources. The value is treated as text.

`Workspace Name` The name of the Slack workspace where the Slack app is installed.

This attribute accepts single-value resources. The value is treated as text.

```
Required

```

If set to true, the running user must enter a value. The default value is
false.

This attribute accepts a resource with a Boolean value.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component

```


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Slider

Let users visually specify number values from a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Slider Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Label

Disabled

Range Maximum

Range Minimum

##### `Slider Size`

```

This label appears above the slider.

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The maximum value of the slider range. The default is 100.

This parameter accepts single-value Number resources.

The minimum value of the slider range. The default is 0.

This parameter accepts Number resources.

Controls the size of the slider. The accepted values are x-small, small, medium, or large.

This parameter accepts single-value resources of any type. That value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Step Size

Value

```

Divides the slider into a set of steps. The default is 1.

For example, for a range of 0–100, set the Step Size to 10 to let the user select every 10th value. Other
example step sizes are 0.1 and 5.

This parameter accepts single-value Number resources.

The default value represented by the slider position. Setting this attribute from the Inputs tab pre-sets
the value.

This parameter accepts single-value Number resources.

Store the Slider Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the value that the user selected, map the Value attribute to a Number flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Text

Let users enter text from a flow screen, such as the name of the user’s company.

Configure the Text Component

**Attribute** **Description**

```
API Name

Default Value

Disabled

```

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

Pre-populated value for the component. If the associated screen isn’t
executed or the conditions for component visibility aren’t met, the stored
value of the component is `null` .

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

`Label` The text that appears with the screen component that tells the running
user how to use it.

`Provide Help` Give your users more context with this screen component. The text you
enter is available in an info bubble next to the component.

```
Read Only

```

If set to true, the user can’t modify the value, but the user can copy it. The
default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

`Require` Requires users to enter a value before they can move to the next screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Input Component: Toggle

Let users flip a toggle in a flow screen.

Note: This screen component requires Lightning runtime.

Configure the Toggle Component

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

```
Active Label

```

When the toggle is active, this label appears underneath the toggle. Use it to clarify what active means.
The default label is “Active.”

This attribute accepts single-value resources. The value is treated as text.

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Inactive Label

Label

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

When the toggle is inactive, this label appears underneath the toggle. Use it to clarify what inactive
means. The default label is “Inactive.”

This attribute accepts single-value resources. The value is treated as text.

This label appears next to the toggle and describes what the user is enabling.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

```
Value

```

Whether the toggle is active ( _`$GlobalConstant.True`_ ) or inactive
( _`$GlobalConstant.False`_ ). Setting this attribute from the Inputs tab controls the default state
of the toggle. To store the user’s selection in a flow variable, set this attribute from the Outputs tab.

This parameter accepts single-value Boolean resources.

Store the Toggle Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the user’s selection, map the Value attribute to a Boolean flow variable or a checkbox field on a record variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.


Automate Your Business Processes with Salesforce Flow Flow Reference

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

Flow Screen Input Component: URL

Let users enter URL values in a flow screen.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Flow Reference

Note: This screen component requires Lightning runtime.

Configure the URL Component

You can select resources from the flow, such as variables or global constants, or you can manually enter a value.

**Attribute** **Description**

`API Name` The API name of the component.

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

```
Disabled

Label

Pattern

Read Only

Required

Value

```

If set to true, the user can’t modify the value. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

The label that appears above the URL field.

This attribute accepts single-value resources. The value is treated as text.

Determines whether the value is valid. The default pattern verifies that the first character is a letter
and that the value includes a colon (:).

To force the user to enter a value in a specific format, use a regular expression. Make sure that your
regular expression checks for a valid protocol in the URL, such as https:// or file:///.

This example expression checks for a secure HTTP protocol (https://) and a specific domain
(acmewireless.com).

```
^https?://(?:www\.)?acmewireless\.com/?.*

```

This attribute accepts single-value resources. The value is treated as text.

If set to true, the user can’t modify the value, but the user can copy it. The default value is false.

This attribute accepts a resource with a Boolean value.

Not supported in Classic runtime for flows.

If set to true, the running user must enter a value. The default value is false.

This attribute accepts a resource with a Boolean value.

The value of the URL field. Setting this attribute prepopulates the field. To use the value that the user
enters, store this attribute’s output in a variable.

This attribute accepts single-value resources. The value is treated as text.


Automate Your Business Processes with Salesforce Flow Flow Reference

Store the URL Component’s Values in the Flow

The flow stores values automatically. If you store values manually, store the attribute’s output value in a variable.

To store values manually, select **Manually assign variables (advanced)** .

All attributes are available to store in flow variables, but Value is the most likely attribute you must store.

To store the URL that the user entered, map the Value attribute to a flow variable.

Tip: By default, screen components that run on Lightning runtime version 58 and prior have no memory. If a user enters a value,
and then does one of the following, the value is lost.

**•** Navigates to another screen and returns to the component’s screen.

**•** Pauses the flow then resumes it.

**•** Navigates to the next screen and triggers an input validation error.

Setting the attribute enables a flow to remember the value. The flow stores the value automatically. If you store values manually,
store the attribute’s output value in a variable.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Validate Input

Provide a formula that evaluates whether what the user entered is valid and the error message to display if invalid.

**Option** **Description**

`Error Message` Specify the error message that appears below the component if the user enters an invalid value.

`Formula` Provide a formula expression that returns a Boolean value.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

If the formula expression evaluates to `true`, the input is valid. If the formula expression evaluates to
`false`, the error message appears below the component.

If the user leaves the field blank and the field isn’t required, the flow doesn’t perform the validation.
If the user leaves the field blank and the field is required, the flow shows the default error message
and not your custom error message.

Specify the Behavior of Values on Revisited Screens

Specify what this component does when a user enters a value, navigates to a previous screen, and then returns to the screen with this
component.

**Option** **Description**

`Use values from when` The component retains the values that the user specified and doesn’t update the values to reflect
`the user last` changes made on previous screens.

```
   visited this screen

```

```
Refresh inputs to

incorporate changes

elsewhere in the

flow

```

SEE ALSO:

The component updates the user-specified values to reflect changes made on previous screens.

If you pause and then resume the flow, the flow retains user-specified values only in Checkbox,
Checkbox Group, Currency, Long Text Area, Multi-Select Picklist, Number, Password, Picklist, Radio
Buttons, and Text components.

Standard Flow Screen Components

_StackOverflow_ [: Sample Regular Expressions for Valid URLs](https://stackoverflow.com/questions/161738/what-is-the-best-regular-expression-to-check-if-a-string-is-a-valid-url)

_MDN_ [: What is a URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

Flow Screen Output Component: Display Text

Display information in a flow screen.

Configure the Display Text Component

**Attribute** **Description**

```
API Name

```

Text box

The API name of the component.

An API name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

The text to display to the flow user.

If you include a uniform resource identifier (URI), use one of these
supported URI prefixes:

**•** `http:`


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

**Attribute** **Description**

**•** `https:`

**•** `//`

**•** `/`

**•** `file:`

**•** `ftp:`

**•** `mailto:`

**•** `sfdc:`

**•** `data:`

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
   Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Example: Display a confirmation message that summarizes what the flow did on the user’s behalf.

SEE ALSO:

Standard Flow Screen Components


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Display Component: Repeater

Collect information about multiple items of the same type on a screen with the Repeater component.
To use the output of the component elsewhere in the flow, loop over the output and save the
relevant data in a variable. Use the variable to build a list of records.

For the best performance, we recommend setting the flow and runtime to API version 58.0 and
later.

Configure the Repeater Component

**Attribute** **Description**

`API Name` The API name of the component.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

An API name can include underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two consecutive underscores.

Screen readers use the API name to announce the Repeater component and its child components.


Automate Your Business Processes with Salesforce Flow Flow Reference

Configure Data Source

Select the collection of items that prepopulates the Repeater component at run time. The Repeater’s child components can reference
values from this collection.

**Attribute** **Description**

`Collection for` Fields from the selected collection become available to child components in the Repeater.
```
   Prepopulated Items

```

`Unique Identifier` The unique identifier for items is the API name of the field that contains a unique identifier for each
`for Items` item in the collection. This field is set automatically to the object’s ID field.

Configure Display Options

**Attribute** **Description**

```
Let Users Add or

Remove Items

```

Choose whether screen flow end users can add new items or remove prepopulated items in your
Repeater instance. End users can remove items that they added manually.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Usage

After you configure the Repeater component, add and configure one or more child components inside the Repeater. The flow stores
user input for the Repeater component in the `AllItems` attribute of the component. You can loop over the items in this collection
to create a collection variable that you can use later in the flow.


Automate Your Business Processes with Salesforce Flow Flow Reference

Considerations

**•** You can’t include the Action Button (Beta) component or record fields in a Repeater.

**•** The output of Repeater components isn’t supported in Transform, Collection Filter, or Collection Sort elements.

**•** You can’t reference the output of a different Repeater component in a Repeater child component.

**•** Choice components that reference a collection choice set resource in the Choice field aren’t reactive inside Repeater components.

**•** When you create or update a screen, you can move a component on the same screen into the Repeater component. You can also
move a component from inside a Repeater component to a different place on the screen. However, any references to the moved
component are broken.

**•** If you move a component with the Manually Assign Variables checkbox selected into a Repeater component, any manual assignments
are removed and the checkbox is deselected. However, the variables still exist in the flow. We recommend reviewing the component
after a move to ensure that it doesn’t include broken references.

**•** Users can add up to 30 instances of the Repeater component to the screen at runtime.

**•** The format for a reference to a Repeater component within the component itself is `{!` _**`repeaterAPIName`**_ `.` _**`fieldName`**_ `}` . In
validation messages and the flow metadata package, the format for the same reference is
`{!` _**`repeaterAPIName`**_ `.AllItems[$` _**`Items`**_ `].` _**`fieldName`**_ `}` .

**•** The `AllItems` attribute is empty when:

**–** The Repeater component contains only child components that don’t accept user input such as the Display Text component.

**–** A user doesn’t add Repeater instances to the screen.

**•** The `AllItems` attribute is null when all the child components are hidden by conditional field visibility.

Example: This example shows a screen that includes a Repeater component with Text, Date, Toggle, and Checkbox Group child
components to collect information about subscribers.

SEE ALSO:

Modify Records from User Input in Screens

Flow Example: Create a Contact for Each Beneficiary on a Policy


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Screen Output Component: Section

Organize screen components and record fields to give your users a better experience.

Note: This screen component requires Lightning runtime.

Usage

Use sections to organize screen components and fields to give users context and easier navigation.
The Section component contains an optional header and up to four side-by-side columns. Each
column can contain multiple components and fields. You can place multiple sections on a screen,
each with its own header and number of columns.

Tip: Apply conditional visibility rules to a section to affect all components and fields in that
section. Use this method to set visibility rules one time for a large number of components,
even if you want only one column.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Headers (1)—Use section headers to create a visual hierarchy to guide your users to the most important items on a screen. All
sections with headers are collapsible and open by default each time a user visits the screen. Also, section header labels can be
translated.

**•** Columns (2)—Use columns to organize your screen and save your users from unnecessary scrolling.

**•** Column Width (3)—When you add or delete a new column, Flow Builder sets the width of all columns in that section to be equal.
To change a column’s width, select a width from the predefined options.

**•** Column Deletion (4)—When you delete a column, all components and fields in that column are deleted.

Tip: To center or indent your components and fields, or add padding, include empty columns on your screen.

Set the Component Visibility

Specify the logic that determines when the flow displays the component.

**Option** **Description**

`When to Display` Configure when the component is displayed using conditional logic.
```
Component
```

You can set the components to:

**Always**
Always display the component.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Option** **Description**

**When all conditions are met (AND)**
Display the component when all of the conditions that you define are met. Define at least one
condition.

**When any condition is met (OR)**
Display the component when at least one of the conditions that you define is met. Define at least
one condition.

**When custom conditional logic is met**
Display the component when the condition logic that you define is met. Define at least one
condition and specify condition logic.

Considerations

**•** Sections are responsive to the size of the window that’s showing the flow. On small form factor devices, columns are stacked vertically
instead. However, it isn’t responsive to the width of Lightning page columns and utility bars. For example, if a Lightning page shows
a flow in a sidebar, the width of the entire window determines how the columns appear, even though the sidebar is narrower.

**•** If a screen contains a Section screen component, the screen ignores the Layout property when the flow is distributed in Experience
Builder, the Lightning App Builder, or the utility bar. Screens with a Section screen component also ignore the `flowLayout` URL
parameter when the flow is distributed via URL.

SEE ALSO:

Customize a Flow URL to Render Two-Column Screens

Set the Runtime Experience for URL-Based Flows

Flow Connectors

A connector determines the path that a flow takes at run time.

**Type** **Label** **Example** **Description**

Default _Unlabeled_ Identifies which element to execute
_(Free-Form)_ next.

Default _Unlabeled_ Identifies which element to execute
_(Auto-Layout)_ next.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Decision

```
Decision

outcome

label

```

Identifies which element to execute
when the criteria of a Decision
element outcome are met.


Automate Your Business Processes with Salesforce Flow Flow Reference

**Type** **Label** **Example** **Description**

Wait

_`Wait`_ Identifies which element to execute when an event
_`configuration`_ that’s defined in a Wait element occurs.

```
label

```

Fault Fault Identifies which element to execute when the
previous element results in an error.

Loop For each item Identifies the first element to execute for each
iteration of a Loop element.

Loop After last item Identifies which element to execute after a Loop
element finishes iterating through a collection.

Outgoing Go To _`Destination`_ Identifies which element to go to and execute next.

```
         element

```

Incoming Go To + _`x`_ connections Identifies how many incoming go to connections
an element has.

SEE ALSO:

Flow Elements

Move and Connect Elements to Change a Flow Route

Flow Operators

#### Operators behave differently, depending on what you’re configuring. In Assignment elements,

operators let you change resource values. In conditions and filters, operators let you evaluate
information and narrow the scope of a flow operation.

Flow Operators in Assignment Elements
Use Assignment element operators to change the value of a selected resource.

Flow Operators in Decision, Wait, and Collection Filter Elements
Use condition operators to verify the value of a selected resource. Conditions are used in Decision,
Wait, and Collection Filter elements.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Operators in Data Elements and Record Choice Sets
Filter conditions narrow the scope of records that the flow operates on. For example, use filter conditions to update only the contacts
that are associated with the Acme Wireless account. When you add an Update Records element, use filter conditions to narrow the
scope to just the contacts whose parent account is Acme Wireless. The In and Not In operators are available only in Create Records,
Get Records, and Update Records elements.

Flow Operators in Assignment Elements

Use Assignment element operators to change the value of a selected resource.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource.

Note: Looking for the sObject data type from Cloud Flow Designer? In Flow Builder, we
replaced sObject with the Record data type. So your sObject collection variables are now
record collection variables.

Apex-Defined

Match the _`@AuraEnabled`_ attribute’s Apex data type with a flow data type in this reference to
determine which operators are supported.

Boolean

Replace a Boolean resource with a new value.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Flow Reference

Collection

Update or replace the value of a collection variable or record collection variable.


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference

Currency and Number

Replace (Equals), add to (Add), or subtract from (Subtract) the value of a currency or number resource. Count (Equals Count) the number
of active stages or the number of items in a collection.

Date

Replace (Equals), add to (Add), or subtract from (Subtract) the value of a date/time resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date/Time

Replace a date/time resource with a new value (Equals).

Picklist

Replace a picklist resource with a new value (Equals) or concatenate a value onto the original value (Add).

Note: Before values are assigned or added to a picklist resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist

Replace a multi-select picklist resource with a new value (Equals), concatenate a value onto the original value (Add), or add a selection
to the resource (Add Item).

Note: Before values are assigned or added to a multi-select picklist resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Record

Replace a record variable with a new value (Equals).

Stage

You can’t update the value of a stage, but you can update the values of the stage global variables: `$Flow.CurrentStage` and
`$Flow.ActiveStages` .

Note: Assignments use the stage’s fully qualified name: _`namespace`_ `.` _`flowName`_ `:` _`stageName`_ or _`flowName`_ `:` _`stageName`_ .

```
$Flow.CurrentStage

```


Automate Your Business Processes with Salesforce Flow Flow Reference

Replace the stage selected in `$Flow.CurrentStage` .

```
$Flow.ActiveStages

```

Add or remove active stages in the `$Flow.ActiveStages` global variable.


Automate Your Business Processes with Salesforce Flow Flow Reference

Text

Replace a text resource with a new value (Equals) or concatenate a value onto the end of the original value (Add).

Note: Before values are assigned or added to a text resource, they’re converted into string values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Operators in Decision, Wait, and Collection Filter Elements

Use condition operators to verify the value of a selected resource. Conditions are used in Decision,
Wait, and Collection Filter elements.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource,

Note: Looking for the sObject data type from Cloud Flow Designer? In Flow Builder, we
replaced sObject with the Record. So your sObject collection variables are now record collection
variables.

Apex-Defined

Match the _`@AuraEnabled`_ attribute’s Apex data type with a flow data type in this reference to
determine which operators are supported.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Boolean

Check whether a Boolean resource’s value matches another value or resource.

Choice

Every choice resource has a data type and obeys the operator rules for that data type. However, choice resources support one extra
operator that other resources don’t, no matter what their data type is.


Automate Your Business Processes with Salesforce Flow Flow Reference

Collection

Check whether a Collection resource’s value contains or matches another value or resource.

Currency and Number

Check whether a Currency or Number resource’s value matches, is larger than, or is smaller than another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date and Date/Time

Check whether a Date or Date/Time resource’s value matches, is before, or is after another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Picklist

Check whether a Picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value.


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist

Check whether a multi-select picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value. If the resource’s value includes multiple items, the operators treat
the value as one string that happens to include semi-colons. It doesn’t treat each selection as a different value. For example, the
operators treat `red; blue; green` as a single value rather than three separate values.


Automate Your Business Processes with Salesforce Flow Flow Reference

Record

Check whether a record resource’s value matches another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Stage

Note: Stages resolve to the fully qualified stage name: `namespace.flowName:stageName` or `flowName:stageName` .

Check whether a Stage resource or the `$Flow.CurrentStage` global variable matches, ends with, or starts with another value or
resource.

Check whether `$Flow.ActiveStages` contains a particular stage, matches the value of a Text collection, or is null.

Text

Check whether a Text resource’s value matches, contains, ends with, or starts with another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Reference

Note:

**•** Before values are compared to a text resource, they’re converted into string values.

**•** Stages resolve to the fully qualified stage name: `namespace.flowName:stageName` or `flowName:stageName` .


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Operators in Data Elements and Record Choice Sets

Filter conditions narrow the scope of records that the flow operates on. For example, use filter
conditions to update only the contacts that are associated with the Acme Wireless account. When
you add an Update Records element, use filter conditions to narrow the scope to just the contacts
whose parent account is Acme Wireless. The In and Not In operators are available only in Create
Records, Get Records, and Update Records elements.

Use this reference, organized by the data type of the field that you select, to understand the
supported operators.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Flow Reference

Checkbox Fields

When you select a checkbox field under Field, these operators are available. A flow treats `null` as a different value than `false` . If you
filter for records whose checkbox field is null, no records are returned.

Currency, Number, and Percent Fields

When you select a currency, number, or percent field under Field, these operators are available.


Automate Your Business Processes with Salesforce Flow Flow Reference

Date and Date/Time

When you select a date or date/time field under Field, these operators are available.


Automate Your Business Processes with Salesforce Flow Flow Reference

Picklist and Text Fields

When you select a picklist or text field under Field, these operators are available. The In and Not In operators don’t support picklist fields.


Automate Your Business Processes with Salesforce Flow Flow Reference


Automate Your Business Processes with Salesforce Flow Flow Reference

Multi-Select Picklist Fields

When you select a multi-select picklist field under Field, these operators are available.

Tip: Be careful when using these operators to filter records based on a multi-select picklist field. Even if two resources have the
same items in a multi-select picklist, they can be mismatched if these cases differ.

**•** The spacing before or after the semi-colon. For example, one resource’s value is “red; green; blue” and the other’s value is
“red;green;blue”

**•** The order of the items. For example, one resource’s value is “red; green; blue” and the other’s value is “red; blue; green”

For best results, use the INCLUDES function in a flow formula.


Automate Your Business Processes with Salesforce Flow Flow Reference

Flow Version Properties

A flow version’s properties consist of its label, description, interview label, and type. These properties
drive the field values that appear on the flow’s detail page.

To change the properties of a flow version, open it in Flow Builder. Then click .

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Flow Reference


## Automate Your Business Processes with Salesforce Flow Automate Complex Processes with Orchestrations

SEE ALSO:

Change the Flow Run Context

API Version for Running a Flow

## Automate Complex Processes with Orchestrations

As your company grows, so does the complexity of your workflows. Processes often require input from multiple users in multiple
departments across multiple time zones. This increased complexity results in an increased amount of time spent waiting for each person
to complete their task in the proper order. Flow Orchestration helps you streamline this process with orchestrations: multi-step processes
that interact with multiple users and systems.

What Is Flow Orchestration?

An orchestration is a sequence of stages, each comprised of one or more steps. A stage can contain background, interactive, and MuleSoft
steps.

Interactive steps have an assigned user and execute a designated screen flow. An admin places the Flow Orchestration Work Guide
Lightning App Builder component on the page layout for the type of record where a person can complete the interactive step assigned
to them. When an orchestration runs an interactive step, the designated user receives an email with a link to their assigned action. The
assigned user clicks the link to go to the record where they complete their action in the Work Guide.

Background steps call an autolaunched flow that Salesforce executes. They can run synchronously or asynchronously and have no user
interaction.

MuleSoft steps call a MuleSoft action that Salesforce executes. They run asynchronously and have no user interaction.

When Should You Use Flow Orchestration?

Use Flow Orchestration to create advanced approval processes, task lists for groups, or any other processes that require multiple interrelated
steps. For example, consider employee onboarding that requires a new employee to go through a multi-level, multi-user, multi-system
approval process to get equipment and access to digital company resources. Use Flow Orchestration to compose and orchestrate that
complex process, and enjoy a top-level experience to manage and monitor every onboarding.

Flow Builder for Flow Orchestration
Get to know the Flow Builder requirements and user interface for Flow Orchestration.

Flow Orchestration Concepts
Learn about what an orchestration is made of and how it relates to flows.

Build an Orchestration
Use Flow Orchestration to build sophisticated business processes by combining and coordinating flows.


### Automate Your Business Processes with Salesforce Flow Flow Builder for Flow Orchestration

Deploy an Orchestration
After you design and test your orchestration, it’s time to put it to work!

Orchestration Run
An orchestration run is created for each instance of an orchestration.

Manage Orchestrations and Work Items
Manage orchestrations and work items with list views. Cancel or suspend a running orchestration. Resume an orchestration run that
failed within the previous 14 days because of an error in an action or flow called by a step. Or resume an orchestration run that was
manually suspended. Reassign work items that have been assigned, but not completed.

Troubleshoot Orchestrations
To troubleshoot a failed orchestration run, use the orchestration fault email. To test an orchestration and observe what happens as
it runs, use the debug option.

Flow Orchestration Limits and Considerations
When designing, managing, and running orchestrations, consider these issues.

Flow Orchestration Entitlements
Flow Orchestration has usage-based entitlements. An orchestration _run_ is a running instance of an orchestration. An _orchestration_
is an application built by your admin that uses stages, steps, and decisions to organize a complex business process.

Flow Orchestration Reference
Bookmark this page for quick access to information about orchestration elements, resources, events, and more.

### Flow Builder for Flow Orchestration

Get to know the Flow Builder requirements and user interface for Flow Orchestration.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Tour the Flow Builder User Interface for Flow Orchestration

Flow Orchestration uses the Auto-Layout canvas in Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Button Bar (1)—Manage your orchestration as you build it.

**•** To run the most recent saved version of the orchestration that’s open, click **Run** .

Note: The Run button is only available for autolaunched orchestrations.

**•** To the left of the buttons, you can see the version’s active or inactive status and when it was last saved.

**•** If the orchestration has warnings or errors, the Show Warnings icon ( ) or the Show Errors ( ) icon appears. To see their details,
click the icon.

Toolbox (2)—Create variables, constants, formulas, or text templates to use in your orchestration. Or view a list of all resources and
elements that you added.

Canvas (3)—Build an orchestration on the canvas. As you add elements to the canvas and connect them, you can see a diagram of your
orchestration.

Note: To insert an element, in the desired location, click . Flow Builder then shows the options and possible elements for this
location.

Details (4)—Set attributes for the element selected in the canvas. The Details panel closes when no element is selected.

Keyboard Shortcuts

Use these handy keyboard shortcuts for macOS and Windows to quickly navigate orchestrations.

Flow Orchestration Concepts

Learn about what an orchestration is made of and how it relates to flows.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

#### Orchestrations

An orchestration uses stages, steps, and decisions to organize complex business processes.

Building Blocks of Orchestrations
Stages and steps are the building blocks of an orchestration.

Anatomy of an Orchestration
Combine elements, connectors, and resources to build orchestrations.

Orchestration Types
An orchestration’s type determines how the orchestration can be distributed.

Triggers for Orchestrations
Creating or updating a record can trigger an orchestration that requires additional input from users, approval from assigned users,
other updates to the record, or changes to related records. In the Start element of a record-triggered orchestration, you can specify
new and changed records of a specific object. Autolaunched orchestrations don’t use triggers. Use another mechanism to launch
an autolaunched orchestration, such as custom Apex classes or custom URLs. Use Flow Orchestration to automate complex processes,
and use Flow Trigger Explorer to order record-triggered flows.

What’s the Difference Between a Flow and an Orchestration?
Salesforce offers several features that automate internal procedures and business processes to save time across your org.

Advanced Orchestration Concepts
After you understand the basics, you’re ready for a closer look at the context in which orchestrations run and how they perform work
items at the same time.

#### Orchestrations

An orchestration uses stages, steps, and decisions to organize complex business processes.

Build orchestrations using the Flow Orchestration tiles in Flow Builder. Flow Orchestration tiles limit
the available elements and available resources in your orchestration and include Stage elements
and Step resources that aren’t available in flows. Flow Orchestration always uses Auto-Layout in
Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration Run Life Cycle

Flow Orchestration Types

The Flow Orchestration tiles are Autolaunched Orchestration (No Trigger) and Record-Triggered Orchestration and can be found on the
All+Templates tab of the New Flow window. Trigger an autolaunched orchestration using a custom Apex class or a custom URL. The
creation or update of a record can trigger a record-triggered orchestration, but only after the record is saved.

Variables in Orchestrations

Autolaunched orchestrations can use input variables to require input from a process that calls it.

To reference output values from flows called by orchestration steps, use the step’s automatic output.

Record Refresh in Orchestrations

When you reference a record variable or a record collection in an orchestration configured to run on API version 58.0 and later, records
are refreshed with their latest values each time the orchestration run resumes. In an autolaunched orchestration run, all referenced
records are refreshed. In a record-triggered orchestration, all referenced records except $Record_Prior are refreshed.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Run Record Ownership

For flow orchestration run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

SEE ALSO:

Use Automatic Output in Orchestrations

Flow Orchestration Resource: Global Variables

#### Building Blocks of Orchestrations

##### Stages and steps are the building blocks of an orchestration.

Orchestration Stages
A stage groups related steps, organizing them into a logical phase. Stages are executed sequentially, and only one stage in an
orchestration can be in progress at a time. You configure the conditions that must be met for the stage to be considered complete.

Orchestration Steps
Steps are grouped in stages and can be run sequentially or concurrently. Interactive steps assign the completion of an active screen
flow to a person, group, or queue and require user intervention. Background steps run an active autolaunched flow synchronously
or asynchronously and have no user interaction. MuleSoft steps run an action imported from a MuleSoft operation and have no user
interaction.

Flows in Orchestrations
Each background and interactive step in an orchestration runs an associated flow. If the logic for controlling stage and step execution
calls for more than 3 requirements, use an evaluation flow to create more complex criteria.

Flow Orchestration Work Items
When an interactive step in an orchestration runs, it creates a work item and assigns it to a user, group, or queue. The orchestration
run then sends an email with a link to the specified record page to all assigned users. They complete the work in the Orchestrator
Work Guide component on the specified record page.

Orchestration Stages

A stage groups related steps, organizing them into a logical phase. Stages are executed sequentially,
and only one stage in an orchestration can be in progress at a time. You configure the conditions
that must be met for the stage to be considered complete.

General

An orchestration must contain at least one stage. You can’t control when a stage starts because
stages run sequentially. To control when a stage completes, select one of the exit conditions.

Note: The Stage element in Flow Orchestration isn’t related to the Stage resource in Flow
Builder.

Exit Condition

To control when a stage completes, select an exit condition.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Automatic Output

An orchestration has access to a stage’s status after it’s in progress. At design time, however, automatic output resources are available
throughout an orchestration, even before associated orchestration runs have access to the automatic output. This capability means that
when you create an orchestration you must reference automatic output resources only when associated orchestration runs have access
to it.

Status

When an orchestration is running, it manages the status for each stage. Because stages run sequentially and have no entry conditions,
they only have a status after they’re in progress. The corresponding orchestration stage run record is created after the stage is in progress.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

History

In history, an orchestration stage has several possible milestones.

Flow Orchestration Stage Run Record Ownership

For flow orchestration stage run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

SEE ALSO:

Evaluation Flows in Orchestrations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration Steps

##### Steps are grouped in stages and can be run sequentially or concurrently. Interactive steps assign

the completion of an active screen flow to a person, group, or queue and require user intervention.
Background steps run an active autolaunched flow synchronously or asynchronously and have no
user interaction. MuleSoft steps run an action imported from a MuleSoft operation and have no
user interaction.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Automatic Output

At design time, automatic output resources are available throughout an orchestration, even before
associated orchestration runs have access to the automatic output. This capability means that when
you create an orchestration you must reference automatic output resources only when associated
orchestration runs have access to it.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Note: To allow an orchestration access to a user-defined output variable in a flow called by a step, mark it as **Available for output**
in the flow.

Note: An orchestration uses the isOrchestrationConditionMet output variable in evaluation flows. All other user-defined output
variable values are discarded.

**Table 2: Orchestration Run Access to Automatic Output**


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Status

When an orchestration is running, it manages the status for each step.

History

In history, a step in an orchestration has several possible milestones.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Step Run Record Ownership

For flow orchestration step run records created in Winter ’23 or later, the Owner ID field is set to the ID of the automated process user.

Flow Orchestration Background Steps
A background step launches an active autolaunched flow and has no user interaction. You can control when a background step is
ready to start.

Flow Orchestration Interactive Steps
An interactive step launches an active screen flow and requires user interaction. You can control when an interactive step is ready
to start or when its status is set to completed.

Flow Orchestration MuleSoft Steps
A MuleSoft step asynchronously runs an operation imported from a MuleSoft API and has no user interaction. You can control when
a MuleSoft step is ready to start.

Flow Orchestration Background Steps

A background step launches an active autolaunched flow and has no user interaction. You can
control when a background step is ready to start.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Background Step Work Cycle


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Asynchronous Background Step

By default, background steps are processed synchronously. When you select **Contains external callouts or wait elements**, a background
step is processed asynchronously. Use an asynchronous background step when the background step calls an autolaunched flow that
contains a Pause or Wait element or an external callout.

When the autolaunched flow called by an asynchronous step is completed, it publishes a Flow Orchestration Event platform event. That
event causes the orchestration to evaluate the status of the current stage and each step with a status of Not Started or In Progress
contained within the stage.

When to Start the Step

To control when a background step starts, select a condition.

Running Context of an Action Called by a Background Step

For API version 60.0 and later, by default, an active autolaunched flow called by a background step runs in the context of the Automated
Process User. To run a background step in the context of a different user, use the Select Who to Run the Action As section in the background
step's Properties panel. To control the system context’s record-level access, use the How to Run the Flow advanced option of the
autolaunched flow.

For API version 59.0 and earlier, an active autolaunched flow called by a background step runs in the same context that the orchestration
runs in.

**Table 3: Running Contexts of Background Steps in API Version 59.0 and Earlier**

For API version 59.0 and earlier, the context that an active autolaunched flow called by an asynchronous background step runs in depends
on the context of the parent orchestration run


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

**Table 4: Running Contexts of Asynchronous Background Steps in API Version 59.0 and Earlier**

SEE ALSO:

Evaluation Flows in Orchestrations

Flow Orchestration Interactive Steps

An interactive step launches an active screen flow and requires user interaction. You can control
when an interactive step is ready to start or when its status is set to completed.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Interactive Step Work Cycle

For flows running in version 57.0 and earlier, after an interactive step is marked as complete, an orchestration run resumes in the context
of the user who completed the associated work item. If the person who completed a work item has granular access to specific flows
without the Run Flows permission, the orchestration run can’t resume. To resume the orchestration, someone with the Run Flows
permission can run another work item or an admin can trigger a Flow Orchestration Event with the ID of the paused orchestration run.

When to Start the Step

To control when an interactive step starts, select a condition.

When to Complete the Step

To control when an interactive step completes, select a condition.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Who Completes the Step

When an orchestration is designed, an interactive step is assigned to a user, group, or queue.

**Table 5: Interactive Step Assignees**

At run time, assigned users, groups, and queues receive a notification email with a link to their assigned work by default. You can stop
Flow Orchestration from sending these email notifications, but you can’t customize the default email. See Disable Default Email Notifications
for Work Item Assignments.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Where to Complete the Step

The assignee or a person from the assigned group or queue completes the associated screen flow on a related record page. A link to
this related record page is included in the email sent to the assigned person, group, or queue.

Running Context of a Flow Called by an Interactive Step

An active screen flow called by an interactive step runs in the context of the person who’s completing it.

SEE ALSO:

Running Context of an Orchestration

Evaluation Flows in Orchestrations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration MuleSoft Steps

A MuleSoft step asynchronously runs an operation imported from a MuleSoft API and has no user
interaction. You can control when a MuleSoft step is ready to start.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

MuleSoft Step Work Cycle

When to Start the Step

To control when a MuleSoft step starts, under Select When to Start the Step, select a condition.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Running Context of a MuleSoft Action Called by a MuleSoft Step

For API version 60.0 and later, by default, a MuleSoft action called by a MuleSoft step runs in the context of the Automated Process User.
To run a MuleSoft action in the context of a different user, use the Select Who to Run the Action As section in the MuleSoft step's Properties
panel.

For API version 59.0 and earlier, a MuleSoft action called by a MuleSoft step runs in the context of the user that the orchestration ran as
before the MuleSoft step starts.

SEE ALSO:

Evaluation Flows in Orchestrations

##### Flows in Orchestrations

Each background and interactive step in an orchestration runs an associated flow. If the logic for
controlling stage and step execution calls for more than 3 requirements, use an evaluation flow to
create more complex criteria.

Background Steps

Each background step calls an autolaunched flow.

Interactive Steps

Each interactive step assigns a screen flow to a user, group, or queue.

When to Start the Step

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Each step can call an evaluation flow to determine whether the step can be started. An evaluation flow is a flow with a process type of
Evaluation Flow. It’s an autolaunched flow that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` . To indicate that the custom entry conditions are met, the output variable must be set to
true.

Note: The Boolean `isOrchestrationConditionMet` variable defined in an evaluation flow must be initialized to false.

When to Complete the Step

An interactive step or a stage can call an evaluation flow to determine whether the step can be considered complete. An evaluation
flow is a flow with a process type of Evaluation Flow. It’s an autolaunched flow that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` . To indicate that the custom exit conditions are met, the output variable must be set to true.

Note: The Boolean `isOrchestrationConditionMet` variable defined in an evaluation flow must be initialized to false.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Variables

Flows can have internal-only, input, and output variables.

If the combined input values for a flow called by an orchestration step is more than 32,768 characters, the orchestration fails. This error
can be caused by passing one or more records to a flow called by a step. To avoid this error, pass a record ID to the referenced flow, and
use a Get Records element in the flow with the passed ID. Using a passed ID with a Get Records element also means that you always
have the latest version of the record.

Evaluation Flows in Orchestrations
When you need more than 3 requirements to control stage and step execution, use an evaluation flow. Select the Evaluation Flow
tile in the New Flow window to create an evaluation flow.

SEE ALSO:

Flow Types

Automate Tasks with Flows


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

###### Evaluation Flows in Orchestrations

When you need more than 3 requirements to control stage and step execution, use an evaluation
flow. Select the Evaluation Flow tile in the New Flow window to create an evaluation flow.

Variables in Evaluation Flows

When you select the Evaluation Flow tile in the New Flow window, you create an evaluation flow
that contains a predefined Boolean output variable named
`isOrchestrationConditionMet` .

Initialize `isOrchestrationConditionMet` to false, and to indicate that the custom
conditions are met, set `isOrchestrationConditionMet` to true.

Evaluation flows only return a value for `isOrchestrationConditionMet` . Values for any
other output variables are discarded.

Evaluation Flow Execution

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Every time an asynchronous background step, an interactive step, or a MuleSoft step within the current stage is completed, the orchestration
evaluates the conditions for that stage and its steps. To trigger an evaluation of conditions for the current stage and its steps, publish
an orchestration event with $Orchestration.Instance

The status of each stage or step determines which conditions the orchestration checks. If the condition being checked relies on an
evaluation flow, the evaluation flow runs.

**•** When a stage is in progress, the orchestration determines whether it can be completed.

**•** For each not started step within the current stage, the orchestration determines whether the step is ready to start.

**•** For each in progress interactive step within the current stage, the orchestration determines whether the step can be marked complete.

Running Context of an Evaluation Flow

In API version 60.0 and later, evaluation flows can be run only in system context without sharing and have access to all data.

In API version 58.0 and 59.0, evaluation flows always run in system context.

In API version 57.0 and earlier, evaluation flows run as specified in the flow’s How to Run the Flow advanced option.

SEE ALSO:

Trigger an Evaluation of Orchestration Stage and Step Conditions


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Flow Orchestration Work Items


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

When Assignment Notifications Are Made with the Omni-Channel Widget

When an interactive step is assigned to a queue associated with the Orchestration Work Item object, the queue members receive
notifications based on your defined routing logic in the Omni-Channel widget. The notification by Omni-Channel widget is in addition
to the default email notification sent to queue members.

Internal User Access to Work Items

Internal users get a link in their email notification to the related record page where they can complete their assigned work item. They
can also view and access their assigned work in the Flow Orchestration Work Items list view or in their To Do List. To allow internal users
to complete assigned work, before the orchestration runs, place the Flow Orchestration Work Guide component on the related record
page layout in Lightning App Builder.

Experience Cloud Site Visitor Access to Work Items

Credentialed Experience Cloud site visitors usually get a link in their email notification to the related record page of the oldest live
Experience Cloud site that they’re a member of. They can also view and access their assigned work in the Orchestration Work Item object
list view.

Before the orchestration runs, in Experience Builder, the admin sets up site visitor access to orchestration work items.

**•** In Experience Builder, the admin places the Flow Orchestration Work Guide component on the related record page in Aura and LWR
sites.

**•** In Experience Builder, the admin adds the Orchestration Work Item List object page to Aura and LWR sites.

Work Assigned to an Internal User

When an interactive step runs, the orchestration creates a work item and assigns it to the specified internal user. The assigned user
receives an email with a link to the internal related record page notifying them that they have a work item to complete. The work item
also appears in the assigned user's To Do List. When the user clicks the link to the work item, they then can complete the screen flow
associated with the interactive step in the Work Guide on the internal related record page.

Work Assigned to a Credentialed Experience Cloud Site Visitor

When an interactive step runs, the orchestration creates a work item and assigns it to the specified credentialed Experience Cloud site
visitor. The assignee receives an email that notifies them that they have a work item to complete. The email contains a link to the related
record page on the oldest live site that they’re a member of. When the site visitor clicks the email link, they then complete the associated
screen flow in the Work Guide on the related record page that they’ve been directed to.

Work Assigned to an Internal Group or Queue

When the interactive step runs, the orchestration creates a work item and assigns it to the specified group or queue. All users in the
assigned internal group or internal queue receive an email with a link to the internal related record page notifying them that they have
an action to complete. When a user clicks the link in the email and the work item opens, the user can run the screen flow in the Work
Guide on the internal related record page.

An assigned work item is completed by the first user to complete the screen flow. If two users execute the screen flow simultaneously,
the user who completes the flow second receives an error. After the work item is completed, other users from the assigned group or
queue see no related work in the Work Guide component on the internal related record page.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Work Assigned to a Group or Queue of Credentialed Experience Cloud Site Visitors

When the interactive step runs, the orchestration creates a work item and assigns it to the specified group or queue of credentialed
Experience Cloud site visitors. Site visitors in an assigned group or queue receive an email notifying them that they have an action to
complete. The email usually contains a link to the related record page of the oldest live Experience Cloud site that the visitors are all
members of. When a group or queue member clicks the link, the visitor is taken to the related record page of the oldest live Experience
Cloud site that all group or queue members are credentialed for. From that related record page, the site visitor can complete the associated
screen flow in the Work Guide.

Experience Cloud site visitors can also view work items assigned to them in the Orchestration Work Item List object page. From the
Orchestration Work Item List, they can also access their assigned work. When the credentialed site visitor goes to the related record page
of the Aura or LWR site that they’re a member of, the visitor can run the screen flow in the Work Guide.

An assigned work item is completed by the first credentialed site visitor to complete the screen flow. If two credentialed site visitors
execute the screen flow simultaneously, the one who completes the flow second receives an error. After the work item is completed,
other site visitors from the assigned group or queue see no related work in the Work Guide component on the related record page.

Work Items Reassigned to a User, Group, or Queue

You can reassign open work items for a running orchestration to a different user, group, or queue. After reassignment, a work item is
processed like it was after the running orchestration created it.

Work Item Statuses


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

History

In history, an orchestration work item has several possible milestones.

Flow Orchestration Work Item Record Ownership

For flow orchestration work item records created in Winter ’23 or later, the owner is either the assigned user or the automated process
user.

For flow orchestration work items created before Summer ’24 and assigned to a queue, the owner is the automated process user.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

SEE ALSO:

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Anatomy of an Orchestration

Combine elements, connectors, and resources to build orchestrations.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**•** Each element (1) represents an action that the flow can execute. Orchestrations use Stage and Decision elements.

**•** Each connector (2) defines an available path that the orchestration can take at run time.

**•** Each stage consists of one or more steps (3).


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

**•** Each resource (4) represents a value that you can reference through a stage, step, or decision.

#### Orchestration Types

An orchestration’s type determines how the orchestration can be distributed.

All orchestrations are made up of steps grouped within a series of stages. Interactive steps contain
a screen flow and require user interaction. Background steps contain an autolaunched flow and
don’t require user interaction. An orchestration’s type affects how an orchestration is launched.

#### Triggers for Orchestrations

Creating or updating a record can trigger an orchestration that requires additional input from users,
approval from assigned users, other updates to the record, or changes to related records. In the
Start element of a record-triggered orchestration, you can specify new and changed records of a
specific object. Autolaunched orchestrations don’t use triggers. Use another mechanism to launch
an autolaunched orchestration, such as custom Apex classes or custom URLs. Use Flow Orchestration
to automate complex processes, and use Flow Trigger Explorer to order record-triggered flows.

In Flow Orchestration, the trigger occurs after a record is saved.

#### What’s the Difference Between a Flow and an Orchestration?

Salesforce offers several features that automate internal procedures and business processes to save
time across your org.

Flow

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

A _flow_ is an application that automates a business process by collecting data and doing something in your Salesforce org or an external
system. Flows can provide screens to guide users through your business process.

Flows aren’t tied to any one object, but they are record-centric. Flows can look up, create, update, and delete records for multiple objects.
You can build flows with Flow Builder, a point-and-click tool.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Orchestration

An _orchestration_ is an application that builds sophisticated business processes by combining and coordinating a series of flows.
Orchestrations are user-centric. You can manage processes that involve different users and different parts of your organization through
one orchestration. Flow Orchestration lets you monitor operations and improve efficiency.

Advanced Orchestration Concepts

After you understand the basics, you’re ready for a closer look at the context in which orchestrations run and how they perform work
items at the same time.

Running Context of an Orchestration
The running context determines the access that an orchestration has to Salesforce data and the context used by a paused orchestration
to resume. By default, the running context of an orchestration is the Automated Process User in system context.

Orchestration Versioning
Flow Orchestration has two levels of versioning: the version of the orchestration and the version of a flow called by an orchestration.

Running Context of an Orchestration

The running context determines the access that an orchestration has to Salesforce data and the
context used by a paused orchestration to resume. By default, the running context of an orchestration
is the Automated Process User in system context.

The default running user for an orchestration depends on the type of orchestration and the API
version that it runs in.

Autolaunched Orchestration

For API version 60.0 and later, an autolaunched orchestration always launches and resumes in the
context of the Automated Process User in system context.

For API version 59.0 and earlier, an autolaunched orchestration usually launches in the context of
the user who launched the orchestration. If the orchestration is launched from Apex, it runs in a
system context. Control the context that an autolaunched orchestration launches and resumes in
with the How to Run the Orchestration advanced option.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

For API version 59.0 and earlier, the context that a paused, autolaunched orchestration resumes in depends on how it was launched or
what caused it to resume.

**Table 6: Resume Contexts for Autolaunched Orchestrations in API Version 59.0 and API Version 58.0**


Automate Your Business Processes with Salesforce Flow Flow Orchestration Concepts

Record-Triggered Orchestration

For API version 60.0 and later, a record-triggered orchestration always launches and resumes in the context of the Automated Process
User in system context.

For API version 59.0 and earlier, a record-triggered orchestration always launches in the context of the user who triggered the orchestration
in system context.

For API version 59.0 and earlier, the context that a paused, record-triggered orchestration resumes in a user in system context. The user
that the record-triggered orchestration resumes as depends on what caused it to resume.

**Table 7: User Contexts of Record-Triggered Orchestrations in API Version 59.0 and Earlier**

##### Orchestration Versioning

Flow Orchestration has two levels of versioning: the version of the orchestration and the version of
a flow called by an orchestration.

Orchestration Definition Versioning

An orchestration definition can have 1 active version at a time. The orchestration definition version
used by an orchestration run is the version that’s active at the time the run starts.

**•** If you activate a new version of an orchestration’s definition after an orchestration run based
on that definition starts, the orchestration run continues to run the definition version that it
started in.

**•** Only orchestration runs that start after the new version was activated use the new active version.

Flow Definition Versioning

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Interactive and background steps call flows. A step uses the definition version of the flow that’s active when the step starts.

**•** If you activate a new definition version of a referenced flow after the orchestration run starts and the associated step run is created,
the old version of the flow runs.


### Automate Your Business Processes with Salesforce Flow Build an Orchestration

**•** If you activate a new definition version of a referenced flow after the orchestration run starts but before the associated step run is
created, the new version of the flow runs.

### Build an Orchestration

Use Flow Orchestration to build sophisticated business processes by combining and coordinating
flows.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
### Builder:

It’s easier to automate a business process when you understand how the pieces fit. Before you
create your orchestration, talk to your stakeholders to understand the requirements. You can save
draft orchestrations without knowing all the required information, but you must specify all associated
flows and details before you can activate and run your orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Orchestrations are made up of Stage elements and Decision elements. Stages contain at least one step, each step calling an action to
run. Background and interactive steps call flows. MuleSoft steps call MuleSoft actions imported from MuleSoft APIs. Whenever possible,
create the flows and import the MuleSoft actions that you need before you build your orchestration.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start from Scratch**, and then click **Next** .

**3.** Select the orchestration type, and then click **Create** .

**4.** (Optional) To configure the Start element for a record-triggered orchestration, click **Edit** .

**5.** To add an element between the Start and End elements, click, and select the element.

**6.** To add steps to a stage, click **Add Step** .

**7.** To create a loop or connect to a different element, after the stage, click, click **Connect to element**, and then click on the
desired element.

**8.** Save your orchestration.

After you build an orchestration, activate it, and then test it to make sure that it’s working as you expect. You’re then ready to use it.

Use Decision Elements in an Orchestration
Control when an orchestration takes a specific decision outcome.

Define Requirements for Stages and Steps in an Orchestration
Use requirements to resume an orchestration when a record changes. Define up to three requirements to determine when a step
is ready to start or when to mark an interactive step or stage complete.

Assign an Interactive Step in an Orchestration
When you create an interactive step, you assign it to a user, group, or queue. A user can be an internal user or a credentialed Experience
Cloud site visitor. Groups or queues can include internal users, credentialed Aura site visitors, or credentialed LWR site visitors. You
can also assign an interactive step to a resource that contains a username, group API name, or queue API name when the orchestration
runs. When the active screen flow associated with the interactive step runs, an assigned user completes the flow on the related
context record.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

Route Orchestration Work Items with Omni-Channel
To use Omni-Channel routing in Service Cloud with orchestration work items, you must have at least one queue associated with the
Orchestration Work Item. When you assign an interactive step to that queue, members of the queue receive notifications via the
Omni-Channel widget based on your routing logic. Unless you disable default email notifications for work items, queue members
also receive email notifications.

Redirect an Orchestration Path
Flow Orchestration uses Auto-Layout in Flow Builder. In Auto-Layout, elements on the canvas are spaced and connected automatically.
Use Go To connectors when you have elements that don’t follow the usual consecutive auto-layout path.

Add an End Element to an Orchestration Path
All elements in an orchestration are connected automatically or connected by Go To connectors that you add manually. To finish a
path in your orchestration, add an End element.

Use Automatic Output in Orchestrations
An orchestration has access to output for its stages, steps, and decisions. Query the status of any stage or step in the orchestration.
Use output parameters from any step’s associated flow. In an orchestration configured to run on API version 58.0 and later, referenced
automatic outputs that contain a record or a record collection are refreshed with their latest values each time the orchestration run
resumes.

Trigger an Evaluation of Orchestration Stage and Step Conditions
Every time a step within the current stage completes, the orchestration evaluates the conditions for that stage and its steps. You
can also publish an orchestration event from a flow to trigger an evaluation of orchestration stage and step conditions.

Integrate an Orchestration with External Systems
Add a MuleSoft step to your orchestration to call an imported MuleSoft action. You can also use the
`$Orchestration.Instance` system variable to integrate external systems with your orchestration.

Create an Orchestration Template
You can save a new or existing orchestration as a template, and then use it as a starting point for creating other orchestrations in
Flow Builder. You can also distribute the template via a managed package so that subscribers can create orchestrations based on
the template.

Make Work Accessible to Assigned Users
When an orchestration runs an interactive step, it emails a notification to the assigned user, group, or queue. Credentialed Experience
Cloud site visitors can see and access their assigned Flow Orchestration work items on the Orchestration Work Item List object page.
Internal users and credentialed Experience Cloud site visitors complete their assigned work in the Work Guide.

#### Use Decision Elements in an Orchestration

Control when an orchestration takes a specific decision outcome.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Before you begin, add the Decision element to your orchestration.

**1.** Set up the conditions.

At run time, the conditions are evaluated in the order you specify.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Build an Orchestration

**2.** Identify the logic between the conditions.

**Column Header** **Description**

**Resource**
Options:

**•** Select an input variable or automatic output from a stage or step.

**•** Select a Decision element.

**•** Select a global variable.

**Operator** The available operators depend on the data type selected for `Resource` . See Flow Orchestration
Operators in Decision Elements.

```
Value

```

**Resource** and **Value** in the same row must have compatible data types.

Options:

**•** Select an orchestration resource, such as an input variable or automatic output from a stage
or step.

**•** Select a global variable.

**•** Manually enter a literal value.

When you add or subtract a number from a date value, the date adjusts in days, not hours.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Define Requirements for Stages and Steps in an Orchestration

Use requirements to resume an orchestration when a record changes. Define up to three
requirements to determine when a step is ready to start or when to mark an interactive step or
stage complete.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Before you begin, add a Stage element to your orchestration or a Step resource to a stage.

**1.** In the Properties panel, select the condition that allows you to create up to three requirements
to start a step or complete a stage or interactive step.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**2.** Set up the logic for the requirements.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**3.** Define up to three requirements.

A change to a record referenced in a requirement can trigger the orchestration to evaluate the status of the current stage and the
outstanding steps within it. Some requirement resources don’t trigger condition evaluations.

**Column Header** **Description**

**Resource**
Options:

**•** Select an orchestration resource

**–** Select a variable

**–** Select a record variable field

**–** Select automatic output from a step.

**•** Select a Stage element’s status

**•** Select a Step resource’s status.

**•** For record-triggered orchestrations, select the $Record global variable.

**•** Select a global variable.

**Operator** The available operators depend on the data type selected for **Resource** and work the same as
operators used for Decision elements. See Flow Orchestration Operators in Decision Elements.

**Value**

SEE ALSO:

**Resource** and **Value** in the same row must have compatible data types.

Options:

**•** Select an orchestration resource, such as a variable or automatic output from a step.

**•** Select a global constant

**•** Select a global variable.

**•** Manually enter a literal value.

When you add or subtract a number from a date value, the date adjusts in days, not hours.

Considerations for Orchestrations

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.244.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)_ : StandardObjectNameChangeEvent


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Assign an Interactive Step in an Orchestration

When you create an interactive step, you assign it to a user, group, or queue. A user can be an
internal user or a credentialed Experience Cloud site visitor. Groups or queues can include internal
users, credentialed Aura site visitors, or credentialed LWR site visitors. You can also assign an
interactive step to a resource that contains a username, group API name, or queue API name when
the orchestration runs. When the active screen flow associated with the interactive step runs, an
assigned user completes the flow on the related context record.

The User field for an interactive step’s assigned user includes internal users and credentialed
Experience Cloud site visitors. Whenever you assign an interactive step to a user or a credentialed
site visitor, ensure that they have the required access to the related record.

For an internal user to complete an interactive step, they must have access to the associated internal
Salesforce Lightning record page. For a credentialed Experience Cloud site visitor to complete an
interactive step, they must have access to the associated related record page in an Aura or LWR
site.

To use Omni-Channel routing with Flow Orchestration, set up Omni-Channel and associate at least
one queue with the Orchestration Work Item object. Then, to notify assigned users with the
Omni-Channel widget based on your defined routing logic, assign an interactive step to a queue
that’s associated with the Orchestration Work Item object.

**1.** Add an interactive step to a stage in your orchestration.

**2.** In the Properties panel for the interactive step, under Select Someone to Complete the Action,
select an assignment type.

**•** To specify a user, select **User** .

**•** To specify a regular public group, select **Group** .

**•** To specify a group that’s a queue, select **Queue** .

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To open, edit, or create an
orchestration in Flow Builder:

**•** Manage Flow

To complete assigned work
and resume a paused
orchestration

**•** Run Flows

**•** To specify a resource that contains a user’s username when the orchestration runs, select **User Resource** .

**•** To specify a resource that contains a group’s API name when the orchestration runs, select **Group Resource** .

**•** To specify a resource that contains a queue’s API name when the orchestration runs, select **Queue Resource** .

**3.** Specify the assigned user, group, or queue.

**•** If you selected User, search for the name of an internal user or a credentialed Experience Cloud site visitor, and select it from the
list.

**•** If you selected Group, search for a group’s label, and select it from the list.

**•** If you selected Queue, search for a queue’s label, and select it from the list.

**•** If you selected User Resource, specify the API name of the variable that contains the assignee’s username when the orchestration
runs.

Important: Don’t select $User for User Resource. The $User global variable evaluates to the system user when the orchestration
is running in system context and an interactive step can’t be assigned to the system user.

**•** If you selected Group Resource, specify the API name of the variable that contains the group API name when the orchestration
runs.


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**•** If you selected Queue Resource, specify the API name of the variable that contains the assigned queue’s API name when the
orchestration runs.

SEE ALSO:

Flow Orchestration Interactive Steps

Running Context of an Orchestration

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Route Orchestration Work Items with Omni-Channel

To use Omni-Channel routing in Service Cloud with orchestration work items, you must have at
least one queue associated with the Orchestration Work Item. When you assign an interactive step
to that queue, members of the queue receive notifications via the Omni-Channel widget based on
your routing logic. Unless you disable default email notifications for work items, queue members
also receive email notifications.

When you assign an interactive step to a group or queue, each group or queue member receives
an email notification by default. The email notification contains a link to the record where one of
the members can complete the assigned work.

When a queue associated with the Orchestration Work Item object is assigned to an interactive
step, the work item owner is the queue.

**1.** [Set up Omni-Channel.](https://help.salesforce.com/s/articleView?id=sf.service_presence_intro.htm&language=en_US)

**2.** Associate a queue with the Orchestration Work Item object.

**3.** Assign an interactive step to a queue associated with the Orchestration Work Item object.

SEE ALSO:

_Salesforce Help_ [: Route Work with Omni-Channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm.htm&language=en_US)

#### Redirect an Orchestration Path

Flow Orchestration uses Auto-Layout in Flow Builder. In Auto-Layout, elements on the canvas are
spaced and connected automatically. Use Go To connectors when you have elements that don’t
follow the usual consecutive auto-layout path.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

To add a Go To connector, you must have at least two elements in your orchestration.

**1.** Directly after the element that you want to change the connector for, click .

**2.** Click **Connect to element** .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To open, edit, or create an
orchestration in Flow Builder:

**•** Manage Flow

To complete assigned work
and resume a paused
orchestration

**•** Run Flows

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Build an Orchestration

**3.** Click on the element that you want to connect to.

The original element now has a dotted line connection to the specified element.

#### Add an End Element to an Orchestration Path

All elements in an orchestration are connected automatically or connected by Go To connectors
that you add manually. To finish a path in your orchestration, add an End element.

To add an End element, you must have at least one Decision element and two paths in your
orchestration.

**1.** After the last element in the path where you want to add the End element, click .

**2.** Select **End** .

The path now ends execution when this element is reached.

#### Use Automatic Output in Orchestrations

An orchestration has access to output for its stages, steps, and decisions. Query the status of any
stage or step in the orchestration. Use output parameters from any step’s associated flow. In an
orchestration configured to run on API version 58.0 and later, referenced automatic outputs that
contain a record or a record collection are refreshed with their latest values each time the
orchestration run resumes.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Add an element or resource to your orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

When you build an orchestration, automatic outputs for every stage and step in that orchestration are universally available. This universal
availability means that you can potentially use automatic output in your designed orchestration before it’s available in an orchestration
run. So, when using automatic output, consider the order in which an orchestration executes its elements and resources.

**1.** In a resource, value, or input parameter field, select a stage or step from the dropdown list.

**2.** Select the automatic output field from the dropdown list.

**3.** Save your work.

#### Trigger an Evaluation of Orchestration Stage and Step Conditions

Every time a step within the current stage completes, the orchestration evaluates the conditions for that stage and its steps. You can
also publish an orchestration event from a flow to trigger an evaluation of orchestration stage and step conditions.

SEE ALSO:

Publish an Orchestration Event


Automate Your Business Processes with Salesforce Flow Build an Orchestration

Integrate an Orchestration with External Systems

Add a MuleSoft step to your orchestration to call an imported MuleSoft action. You can also use the `$Orchestration.Instance`
system variable to integrate external systems with your orchestration.

##### Publish an Orchestration Event

To allow an external system to make a paused orchestration evaluate its stage and step conditions, publish an orchestration event
from a record-triggered orchestration.

SEE ALSO:

Flow Orchestration MuleSoft Steps

##### Publish an Orchestration Event Publish an Orchestration Event

To allow an external system to make a paused orchestration evaluate its stage and step conditions,
publish an orchestration event from a record-triggered orchestration.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

Add a custom field to the object to hold an orchestration run ID.

Create an autolaunched flow with an input variable that accepts an orchestration run ID and passes
it to the action that invokes an external system.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Add logic at the end of the action invoking the external system. After the external system finishes
its task, it must update the custom orchestration run ID field on the affected record with the orchestration run ID it was passed.

Call the autolaunched flow from an asynchronous background step in an orchestration, and pass $Orchestration.Instance to the appropriate
input parameter.

**1.** Create a record-triggered flow that runs when the custom orchestrator run ID field is updated on a record. If you have records of
more than one object affected by an external system, create a record-triggered flow for each object.

**2.** Add a Create Records element to the record-triggered flow.

**3.** Enter a label, API name, and description for the element.

**4.** Select **Use separate resources, and literal values.**

**5.** For Object, search for and select _`Orchestration Event`_ .

**6.** For Field, enter _`Orchestration`_, and then select **OrchestrationInstanceId** .

**7.** For Value, enter _`$Record`_, and then select **$Record** . Then select the name of the custom orchestration run ID field on the triggering
record.

**8.** Click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**9.** Save and activate the new record-triggered flow.

SEE ALSO:

_[Extend Salesforce with Clicks, Not Code](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&language=en_US)_ : Create Custom Fields

_[Automate Your Business Processes](https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_variable.htm&language=en_US)_ : Flow Resource: Variable

#### Create an Orchestration Template

You can save a new or existing orchestration as a template, and then use it as a starting point for
creating other orchestrations in Flow Builder. You can also distribute the template via a managed
package so that subscribers can create orchestrations based on the template.

**User Permissions Needed**

To open, edit, or create an orchestration in Flow Manage Flow
Builder:

**1.** To create an orchestration template from an orchestration:

**a.** Open an orchestration and click **Save As** .
The Save as dialog opens

.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**b.** Click **A New Orchestration** and enter a label, API name, and description for your orchestration template.

The description appears under the orchestration template’s name in the New Flow dialog and gives users information about
what your template does.

**c.** Click **Show Advanced** .

**d.** Select **Template** and click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

**2.** To make an orchestration into a template.

**a.** Open an orchestration and click .
The Edit version properties dialog opens.

**b.** Ensure that the orchestration has a description.

The description appears under the orchestration template’s name in the New Flow dialog and gives users information about
what your template does.

**c.** Click **Show Advanced** .

**d.** Select **Template** and click **Done** .

**3.** To use the new template, select it in the New Flow dialog. .

**a.** In Setup, from the Flows listview, click **New Flow** .

**b.** In the New Flow dialog, click **All + Templates**, and then click **Flow Orchestration** .
The new orchestration template is shown in the Flow Orchestration category on the All + Templates tab of the New Flow dialog.

**c.** Select the new template and click **Done** .


Automate Your Business Processes with Salesforce Flow Build an Orchestration

#### Make Work Accessible to Assigned Users

When an orchestration runs an interactive step, it emails a notification to the assigned user, group, or queue. Credentialed Experience
Cloud site visitors can see and access their assigned Flow Orchestration work items on the Orchestration Work Item List object page.
Internal users and credentialed Experience Cloud site visitors complete their assigned work in the Work Guide.

Add an Orchestration Work Item List Object Page to an Experience Cloud Site
Internal users can see and access their assigned work in the Flow Orchestration Work Items list view. Add the Orchestration Work
Item List object page to your Aura or LWR site so that credentialed site visitors can see and access their assigned Flow Orchestration
work items.

Add the Work Guide to a Record Page Layout
Add the Flow Orchestration Work Guide Lightning App Builder component to the page layouts for record types referenced by
interactive steps.

Add the Work Guide to an Experience Cloud Site
Add the Flow Orchestration Work Guide component to the related record page in your Aura and LWR sites for record types referenced
by interactive steps.

SEE ALSO:

Flow Orchestration Work Items


Automate Your Business Processes with Salesforce Flow Build an Orchestration

##### Add an Orchestration Work Item List Object Page to an Experience Cloud Site

Internal users can see and access their assigned work in the Flow Orchestration Work Items list view.
Add the Orchestration Work Item List object page to your Aura or LWR site so that credentialed site
visitors can see and access their assigned Flow Orchestration work items.

**1.** In Experience Builder, select **Pages** - **New Page** .

**2.** Select **Object Pages** .

**3.** In the New Object Pages dialog box, enter _`work item`_ in the Search box.

**4.** Select **Orchestration Work Item**, and click **Create** .

**5.** In the dialog box, click **Create** .

**6.** Select **Pages** - **Orchestration Work Item List** .

**7.** Preview and publish your site.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create an Experience
Cloud site:

**•** Create and Set Up
Experiences AND View
Setup and Configuration

To customize an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

**•** OR

**•** Be a member of the site
AND an experience
admin, publisher, or
builder in that site

To publish an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

**•** OR

**•** Be a member of the site
AND an experience
admin or publisher in
that site

To run a flow in an
Experience Builder site:

**•** Run Flows

Automate Your Business Processes with Salesforce Flow Build an Orchestration

##### Add the Work Guide to a Record Page Layout

Add the Flow Orchestration Work Guide Lightning App Builder component to the page layouts for
record types referenced by interactive steps.

**1.** To add the component to an existing page layout, on a page for a record type associated with
an interactive step, click, and then select **Edit Page** .

**2.** To create a page layout for a record type associated with an interactive step, from Setup, in the
Quick Find box, enter _`App Builder`_, and then select **Lightning App Builder** .

**a.** Click **New**

**b.** Select **Record Page**, and then click **Next** .

**c.** Give your record page a label, and then click **Next** .

The label can be up to 80 characters.

**d.** Select a page template, and click **Finish** .

**3.** Under Components, drag **Flow Orchestration Work Guide** onto the page layout.

If this page layout is new, add other components as needed.

**4.** Save your work.

**5.** If the page layout isn’t already activated, the Page Saved window appears and asks if you want
to activate the page.

Activate your orchestration.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

### Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

##### Add the Work Guide to an Experience Cloud Site

Add the Flow Orchestration Work Guide component to the related record page in your Aura and
LWR sites for record types referenced by interactive steps.

Your org must have Flow Orchestration enabled.

**1.** In Experience Builder, navigate to the related record page.

**2.** From the Components panel, drag **Flow Orchestration Work Guide** onto the page.

**3.** Save your work.

Add the Orchestration Work Item Object List page to your Aura or LWR site and ensure that the site
is published. Then activate the orchestration.

### Deploy an Orchestration

After you design and test your orchestration, it’s time to put it to work!


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create an Experience
Cloud site:

**•** Create and Set Up
Experiences AND View
Setup and Configuration

To customize an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

OR

**•** Be a member of the site
AND View Setup and
Configuration AND an
experience admin,
publisher, or builder in
that site

To publish an Experience
Cloud site:

**•** Be a member of the site
AND Create and Set Up
Experiences

OR

**•** Be a member of the site
AND an experience
admin or publisher in
that site

Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

#### Set Up an Org-Wide Email Address

To receive emails from Flow Orchestration, create an org-wide email address.

Activate or Deactivate an Orchestration
You can have multiple versions of an orchestration in Salesforce, but only one version of each orchestration can be active at a time.
You can activate or deactivate an orchestration in Flow Builder or from the orchestration’s detail page in Setup.

Deploy Orchestrations with Change Sets
Create, test, and debug your orchestrations in a sandbox. Use a change set to send the orchestration and its associated flows to
production when you’re ready to deploy.

#### Set Up an Org-Wide Email Address

To receive emails from Flow Orchestration, create an org-wide email address.

The email address you set up in this step acts as the From address in your emails from Flow
Orchestration. If you don’t have a From address, your notification emails don’t send.

Note: If you have an existing org-wide email address, you don’t have to set up a new one,
but make sure you’ve specified it as your Email Approval Sender in Process Automation
Settings in Setup.

**1.** From Setup, in the Quick Find box, enter _`Email`_, and select **Organization-Wide Address** .

**2.** Select **Add** .

**3.** Fill in the Organization-wide address form.

**a.** For **Display Name**, enter a name that labels your org-wide address.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**b.** For **Email Address**, enter a company email address that can be used as the **From Address** in your email alert.

**c.** Select **Allow All Profiles to Use this From Address** .

**d.** Save your work.

**4.** View your org-wide address and the status, which reads **Verification Request Sent** .

**5.** Navigate to the email address you specified in the Email Address field.

**6.** When Salesforce sends an email to the company address you entered previously, approve and verify the company email address.

**7.** Navigate back to Salesforce, and check to make sure that the status of your address is **Verified** .

**8.** From Setup, in the Quick Find box, enter _`automation settings`_, and then select **Process Automation Settings.** .

**9.** For **Email Approval Sender**, specify your org-wide email address.

**10.** Save your changes.

Activate your orchestration.

Important: If the Sender Type is OrgWideEmailAddress, ensure that the user running the flow has the proper profile configurations
required by the specific org-wide email address being used. Proceeding without the proper configuration results in an error.


Automate Your Business Processes with Salesforce Flow Deploy an Orchestration

#### Activate or Deactivate an Orchestration

You can have multiple versions of an orchestration in Salesforce, but only one version of each
orchestration can be active at a time. You can activate or deactivate an orchestration in Flow Builder
or from the orchestration’s detail page in Setup.

When you activate an orchestration version, the previously activated version, if one exists, is
deactivated. Any running orchestration continues to run using the version that it started with.

**1.** In Flow Builder, open the orchestration version.

#### 2. On the button bar, click Activate or Deactivate .

Deploy Orchestrations with Change Sets

Create, test, and debug your orchestrations in a sandbox. Use a change set to send the orchestration
and its associated flows to production when you’re ready to deploy.

**User Permissions Needed**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To activate or deactivate an
orchestration:

**•** Manage Flow

To activate a
record-triggered
orchestration:

**•** View All Data

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

To create, edit, or view processes:

To edit deployment connections:

Manage Flow

AND

View All Data

Deploy Change Sets

AND

Modify Metadata Through Metadata API
Functions

To use outbound change sets: Create and Upload Change Sets

To use inbound change sets: Deploy Change Sets AND Modify Metadata
Through Metadata API Functions

Create and upload the outbound change set in your sandbox, and deploy the inbound change set in production.


### Automate Your Business Processes with Salesforce Flow Orchestration Run

**1.** Ensure that all group names and queue names used in the source org to assign interactive steps to users duplicate the names used
in the target org.

**2.** Ensure that no interactive steps are directly assigned to a specific user.

**a.** Create constants for each assigned user who’s directly assigned to an interactive step in the orchestration.

**b.** Assign each interactive step to the appropriate assigned-user constant.

**3.** Activate your orchestration and all its referenced flows.

**4.** Create an outbound change set.

**5.** Add components to the new change set. These components include the orchestration, its associated flows, and any new custom
actions or new custom flow screen components that the associated flows depend on.

**6.** Upload your outbound change set.

**7.** Deploy your inbound change set in your target org.

**8.** Update any assigned-user constants in the orchestration, and save a new version of the orchestration.

**9.** Activate the new version of the orchestration.

Ensure that the page layouts for each context record referenced in the orchestration include the Orchestrator Work Guide Lightning
App Builder component.

SEE ALSO:

_[Sandboxes: Staging Environments for Customizing and Testing](https://help.salesforce.com/s/articleView?id=sf.changesets.htm&language=en_US)_ : Change Sets

### Orchestration Run

An orchestration run is created for each instance of an orchestration.

An _orchestration_ is an application built by your admin that uses stages, steps, and decisions to
organize a complex business process.An orchestration _run_ is a running instance of an orchestration.
The context an orchestration run uses depends on the orchestration type. You can also specify a
context with the How to Run the Orchestration advanced option.

Resuming a Failed Orchestration

If an orchestration run fails because of an error in an action called by one of its steps, you have up
to 14 days to fix the error in the action and resume the orchestration. If the orchestration run failed
because of some other type of error, it can’t be resumed. If the orchestration run failed but wasn’t
resumed within 14 days, it can no longer be resumed.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Orchestration Run

Statuses and Milestones

After it’s created, an orchestration run has an associated status.

In logging, an orchestration run has several milestones.


### Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

SEE ALSO:

Running Context of an Orchestration

### Manage Orchestrations and Work Items

### Manage orchestrations and work items with list views. Cancel or suspend a running orchestration.

Resume an orchestration run that failed within the previous 14 days because of an error in an action
or flow called by a step. Or resume an orchestration run that was manually suspended. Reassign
work items that have been assigned, but not completed.

View All Orchestration Work Items
Use the All Work Items list view to see all work items. Use the All Open Orchestration Work
Items list view to see all assigned but not completed work items. Assigned users can see and
access only their pending work items in the All Open Orchestration Work Items list view.

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

View Orchestration Work Items on a Record

Government Cloud Plus.

To see your assigned work items for a specific record, go to the associated record page. If you
have multiple work items assigned to you for that record, you can see them all in the
Orchestration Work Guide component. You can sort the work item list by last-modified date or select the item you want to complete
first. When you complete a work item, the work item list refreshes automatically.

View Orchestration Runs
Use the Orchestration Runs list view to see all in-progress, canceled, and completed orchestration runs in your org. Access orchestration
details and history through the orchestration runs list view.

Reassign an Orchestration Work Item
Reassign an assigned work item to a different user, group, or queue.

Disable Default Email Notifications for Work Item Assignments
By default, an orchestration sends an email notification when an orchestration work item is assigned or reassigned to a user, group,
or queue. Disable default work item notifications to stop sending emails to internal users and credentialed Experience Cloud site
visitors.

Suspend an In-Progress Orchestration
Suspend an orchestration run to wait until you’re ready to continue. When you suspend a running orchestration, the current stage
is also suspended. In-progress steps continue to run, but no new steps are started. If an in-progress step has output, it’s stored so it
can be processed when the orchestration is resumed.

Resume a Suspended Orchestration
Resume a suspended orchestration run to continue its processing. When a suspended orchestration run is resumed, the suspended
stage is also resumed. When the orchestration run is resumed, it evaluates the status of in-progress steps and updates the step status
where appropriate. Stored outputs from steps that were in progress when the orchestration run was suspended are processed.

Resume a Failed Orchestration
When an orchestration run failed within the previous 14 days because of an error in an action called by a step, you can fix the error
and resume the orchestration.


Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

Cancel a Running Orchestration
Cancel an in-progress orchestration from the orchestration runs list view.

Use Orchestration Reports
Use sample flow orchestration reports to track orchestration usage. Sample reports include Orchestration Runs, Orchestration Stage
Runs, Orchestration Step Runs, Orchestration Work Items, and Orchestration Run Logs. These sample reports are based on the
Orchestration Runs Spring ’24, Orchestration Stage Runs Spring ’24, Orchestration Step Runs Spring ’24, Orchestration Work Items
Spring ’24, and Orchestration Run Logs Spring ’24 custom report types.

Orchestration Statuses and Milestones
Each part of an orchestration has a status assigned when an orchestration runs.

View All Orchestration Work Items

Use the All Work Items list view to see all work items. Use the All Open Orchestration Work Items
list view to see all assigned but not completed work items. Assigned users can see and access only
their pending work items in the All Open Orchestration Work Items list view.

**1.** In the App Launcher, find and select **Orchestration Work Items** .

**2.** To see assigned and completed orchestration work items, from the dropdown list, select **All**
**Work Items** .

**3.** To see assigned orchestration work items, from the dropdown list, select **All Open Work Items** .

**4.** To see an assigned work item on its associated record page, click the assigned work item record
in the list view.

Note: Only the assigned user or a member of the assigned group or queue can see an
assigned work item on its associated record page.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To view all orchestration
work items:

**•** View access is based on
sharing settings

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

View Orchestration Work Items on a Record

To see your assigned work items for a specific record, go to the associated record page. If you have
multiple work items assigned to you for that record, you can see them all in the Orchestration Work
Guide component. You can sort the work item list by last-modified date or select the item you want
to complete first. When you complete a work item, the work item list refreshes automatically.

Assigned orchestration work items are shown in the Work Guide on the record page of their
associated record.

**1.** Go to a record that you have assigned work items for.

**2.** To sort orchestration work items in the Work Guide, click and then select how you want
to sort your assigned work.

**3.** To filter displayed orchestration work items in the Work Guide, click, and enter the term to
search for.
The Word Guide lists only those work items with labels that include the specified search term.

**4.** To complete a work item:

**a.** In the Work Guide, click for the item you want to complete.
The screen flow opens in the Work Guide.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To run a flow:

**•** Run Flows

**b.** After you’ve finished the screen flow, click **Finish** .
The work item status is set to Completed, and you’re returned to the refreshed list of work items in the Work Guide.

**c.** If you select an item that you don’t want to complete, click, and then click **OK** .
You return to the list of work items in the Work Guide.

SEE ALSO:

Make Work Accessible to Assigned Users

#### View Orchestration Runs

Use the Orchestration Runs list view to see all in-progress, canceled, and completed orchestration
runs in your org. Access orchestration details and history through the orchestration runs list view.

**1.** In the App Launcher, find and select **Orchestration Runs** .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To view orchestration runs:

**•** View access is based on
sharing settings

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**2.** To see details for a specific orchestration run, on the All Orchestration Runs list view, click the link for an orchestration, and then click
the **Related** tab.

**3.** To see the full orchestration run history, under **Orchestration Run Log**, click **View All** .

##### Add Comments to the Orchestration Run Log

Add custom comments to the Orchestration Run Log using variables in flows called by orchestration steps.

Add a Comments Column to the Orchestration Run Log
Add comments from flows called by orchestration steps to the Orchestration Run Log to customize log information.

##### Add Comments to the Orchestration Run Log

Add custom comments to the Orchestration Run Log using variables in flows called by orchestration
steps.

**1.** In a flow called by an orchestration step, add a variable named Comments.

**a.** For Resource Type, select **Variable** .

**b.** For API name, enter _`Comments`_ .

**c.** For Description, enter _`Stores custom text to be added to the`_
_`Comments field in the Flow Orchestration Log`_ .

**d.** Select **Available for output** .

**e.** For Data Type, select **Text** .

**2.** In an Assignment element in your flow, set the `Comments` variable to a string.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

##### Add a Comments Column to the Orchestration Run Log

Add comments from flows called by orchestration steps to the Orchestration Run Log to customize
log information.

**1.** From the Orchestration Run List View, click and select **Edit Object** .

**2.** In the Orchestration Run setup page, click **Page Layouts**, and select **Orchestration Instance**
**Layout** .

**3.** In the Related Lists section, click the for Orchestration Run Log.

**4.** In the Related List Properties - Orchestration Run Log window, under Available Fields, select
**Comments** and click .
The Comments field is added to the Selected Fields list.

**5.** To change the Comments field’s location in the Orchestration Run Log, use the up and down
arrows.

**6.** Click **OK**, and then click **Save** .

Reassign an Orchestration Work Item

Reassign an assigned work item to a different user, group, or queue.

You can reassign an assigned work item for an orchestration that’s still in progress.

**1.** In the App Launcher, find and select **Orchestration Work Items** .

**2.** On the All Open Work Items page, from the dropdown for the assigned work item, select
**Reassign Orchestration Work Item** .

**3.** In the Reassign Orchestration Work Item window, select the user, group, or queue to reassign
the work item to.

**4.** Click **Reassign Orchestration Work Item** .

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To reassign a work item

**•** Reassign Orchestration
Work Items

OR

**•** Manage Orchestration
Runs and Work Items

To complete assigned work

**•** Run Flows

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Disable Default Email Notifications for Work Item Assignments

By default, an orchestration sends an email notification when an orchestration work item is assigned
or reassigned to a user, group, or queue. Disable default work item notifications to stop sending
emails to internal users and credentialed Experience Cloud site visitors.

**1.** From Setup, in the Quick Find box, enter _`process automation`_, and then select **Process**
**Automation Settings** .

**2.** On the Process Automation Settings page, select **Stop Sending Orchestration Work Item**
**Default Email Notifications** .

#### Suspend an In-Progress Orchestration

Suspend an orchestration run to wait until you’re ready to continue. When you suspend a running
orchestration, the current stage is also suspended. In-progress steps continue to run, but no new
steps are started. If an in-progress step has output, it’s stored so it can be processed when the
orchestration is resumed.

You can suspend only an in-progress orchestration.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the in-progress orchestration, select
#### Suspend . 3. Click Suspend .

When you’re ready, resume the orchestration run.

SEE ALSO:

Resume a Suspended Orchestration


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To edit process automation
settings:

**•** Customize Application

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Resume a Suspended Orchestration

Resume a suspended orchestration run to continue its processing. When a suspended orchestration
run is resumed, the suspended stage is also resumed. When the orchestration run is resumed, it
evaluates the status of in-progress steps and updates the step status where appropriate. Stored
outputs from steps that were in progress when the orchestration run was suspended are processed.

You can resume a suspended orchestration or an orchestration that failed within the previous 14
days because of an error in an action or flow called by a step.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the suspended orchestration, select
#### Resume . 3. Click Resume . Resume a Failed Orchestration

When an orchestration run failed within the previous 14 days because of an error in an action called
by a step, you can fix the error and resume the orchestration.

You can resume a failed orchestration if it failed within the previous 14 days because of an error in
an action called by a step.

Remember to fix the error in the called flow or action before resuming the failed orchestration run.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the orchestration with a status of Error,
#### select Resume . 3. Click Resume .


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To suspend a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

#### Cancel a Running Orchestration

Cancel an in-progress orchestration from the orchestration runs list view.

You can only cancel an in-progress orchestration.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the in-progress orchestration, select
#### Cancel . 3. Click Cancel .

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)

#### Use Orchestration Reports

Use sample flow orchestration reports to track orchestration usage. Sample reports include
Orchestration Runs, Orchestration Stage Runs, Orchestration Step Runs, Orchestration Work Items,
and Orchestration Run Logs. These sample reports are based on the Orchestration Runs Spring ’24,
Orchestration Stage Runs Spring ’24, Orchestration Step Runs Spring ’24, Orchestration Work Items
Spring ’24, and Orchestration Run Logs Spring ’24 custom report types.

Note: Orchestration reports aren’t added to your org when it has the maximum number of
defined custom reports.

Note: If a sample report is deleted, you can’t regenerate it.

Sample orchestration reports are public reports. The reports only show work items assigned directly
to a user. To view work assignments for the groups or queues the user belongs to, change the filter
to view all work items assigned to the user’s groups or queues.

**1.** In the Reports list view, click **Public Reports** .

**2.** In the Search public reports box, enter _`orchestration`_ .
The five sample orchestration reports are listed.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To cancel a running
orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To create, edit, and delete
reports in public and private
folders:

**•** Report Builder

OR

**•** Report Builder (Lightning
Experience)

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**3.** To customize a sample report, edit the desired report.

SEE ALSO:

_Salesforce Help_ [: Build a Report in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.reports_build_lex.htm&language=en_US)

_Salesforce Help_ [: What are some common report limits?](https://help.salesforce.com/s/articleView?id=sf.faq_reports_common_limits.htm&language=en_US)

#### Orchestration Statuses and Milestones

Each part of an orchestration has a status assigned when an orchestration runs.

Orchestration Details

The orchestration details page gives the status of an orchestration that’s currently running.

#### Orchestration Status

When an orchestration runs, it can be completed, it can be canceled, it can end due to an error
with a flow, or it can remain in progress. Orchestration stages, steps, and work items statuses are
situation-dependent.

**Statuses of Items in a Completed Orchestration**

**Statuses of Items in a Canceled Orchestration**


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

**Statuses of Items in an Orchestration Stopped by Orchestration Error**

**Statuses of Items in an Orchestration Stopped by Stage Error**

**Statuses of Items in an Orchestration Stopped by Interactive Step Error**


Automate Your Business Processes with Salesforce Flow Manage Orchestrations and Work Items

Note: These statuses apply when the interactive step fails. When the screen flow associated with the interactive step fails, the
status for running stage and failed step is In Progress and the status for not started work items is Assigned.

**Statuses of Items in an Orchestration Stopped by Background Step Error**

Orchestration Run Milestones

When an orchestration runs, it logs milestones to the orchestration history.


### Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations Troubleshoot Orchestrations

To troubleshoot a failed orchestration run, use the orchestration fault email. To test an orchestration
and observe what happens as it runs, use the debug option.

#### Emails about Orchestration Errors

When an orchestration run fails, Salesforce sends an error email. The email is sent to either the
admin who last modified the associated orchestration or the Apex exception email recipients.

Debug an Orchestration
You can view debug information for in-progress and failed orchestrations.

#### Emails about Orchestration Errors

When an orchestration run fails, Salesforce sends an error email. The email is sent to either the
admin who last modified the associated orchestration or the Apex exception email recipients.

The email includes the error message with details about the:

**•** Orchestration

**•** Executed orchestration elements

**•** Flows called from orchestration steps

For activated orchestrations, the error email also has a link to show the failed orchestration run
details in Flow Builder.

If an orchestration fails because of a flow it calls, then the recipients receive an error email for the
orchestration failure and an error email for the flow failure.

Example:

```
   Error element Stage_1 (FlowOrchestratedStage).

   An error occurred when executing a flow interview.

   Flow Details

   Flow API Name: Create_Customer_Record

   Type: Orchestrator

   Version: 1

   Status: Inactive

```


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

```
      Org: signup.org.test.1640285093849 (00DRM000000G0SV)

      Flow Interview Details

      Interview Label: Create New Customer 2/11/2022, 1:57 PM

      Interview GUID: 1fb36a45416070aa772cba20517eea2a1236-7f18

      Current User: Test User (005RM0000025zTa)

      Start time: 2/11/2022, 1:57 PM

      Duration: 3 seconds

      How the Interview Started

      Orchestration Run ID: 0jERM0000004CQT

      Test User (005RM0000025zTa) started the flow interview.

      API Version for Running the Flow: 54

      ENTER STAGE: Stage 1

      ID: 0jFRM0000004CQY

      Status: Error

      BACKGROUND STEP: Create Account for New Customer

      ID: 0jLRM0000004Cfd

      Status: Error

      Entry Condition:

      When the stage starts, the step starts = true

      Flow (Create_Account_for_New_Customer)

      Inputs:

      None.

      Outputs:

      None.

      Error Occurred: An error occurred when executing a flow interview.

      Salesforce Error ID: 904995012-1848 (1749972898)

#### Debug an Orchestration

```

You can view debug information for in-progress and failed orchestrations.

How Does Debugging Work for Orchestrations?

View debug details in Flow Builder for only in-progress and failed orchestrations runs. View debug
details in error emails for failed flows.

Note: When an orchestration fails, it doesn’t necessarily roll back record additions, changes,
or deletions that were made before the orchestration failed. As a result, we recommend that
you design and debug your orchestration in a sandbox environment before deploying it to
production.

The debug information for in-progress and failed orchestrations is similar to the information displayed
for flow. In addition, orchestration debug details show milestones for orchestrations, stages, steps,
and work items.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

Milestones

Orchestration milestones are a part of orchestration debugging details.

Stage milestones are a part of orchestration debugging details.

Step milestones are a part of orchestration debugging details.


Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

Work item milestones are a part of orchestration debugging details.

Debug an In-Progress Orchestration
Debug an in-progress orchestration to better understand the path an orchestration takes with different scenarios and the variable
values at points in the automation

Debug a Failed Orchestration
Troubleshoot a failed orchestration, and gain insights about why it failed. You can debug a failed orchestration within 14 days of it
failing.


Automate Your Business Processes with Salesforce Flow Troubleshoot Orchestrations

##### Debug an In-Progress Orchestration

Debug an in-progress orchestration to better understand the path an orchestration takes with
different scenarios and the variable values at points in the automation

Sharing must be enabled for orchestration runs and flow interviews.

**•** The orchestration run to be debugged must be shared with the user.

**•** The flow interview associated with the orchestration run to be debugged must be shared with
the user.

**1.** In the App Launcher, find and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the desired in-progress orchestration,
select **Debug Orchestration** .

Note: If you started running an orchestration before upgrading to Spring ’22, stage and
step instance IDs are shown as null in orchestration debug information. Evaluation flow
output is also shown as null.

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)

##### Debug a Failed Orchestration

Troubleshoot a failed orchestration, and gain insights about why it failed. You can debug a failed
orchestration within 14 days of it failing.

**1.** From Setup, in the Quick Find box, enter, and select **Orchestration Runs** .

**2.** On the Orchestration Runs page, from the dropdown for the desired failed orchestration, select
##### Debug .

Note: If you started running an orchestration before upgrading to Spring ’22, stage and
step instance IDs are shown as null in orchestration debug information. Evaluation flow
output is also shown as null.

SEE ALSO:

_Salesforce Winter ’23 Release Notes_ [: Enable Sharing for Flow Orchestration Objects (Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)
[Update)](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To access the debug action
for a running orchestration:

**•** Manage Orchestration
Runs

OR

**•** Manage Orchestration
Runs and Work Items

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

USER PERMISSIONS

To debug a failed
orchestration:

**•** Manage Flow

Automate Your Business Processes with Salesforce Flow Flow Orchestration Limits and Considerations

Flow Orchestration Limits and Considerations

When designing, managing, and running orchestrations, consider these issues.

General Flow Orchestration Limits
When using orchestrations, keep orchestration limits, flow limits, and Apex governor limits in
mind.

Considerations for Orchestrations
Keep these considerations in mind when designing and using orchestrations.

Considerations for Evaluation Flows
Keep these considerations in mind when using evaluation flows as entry or exit conditions.

Security Considerations for Orchestrations
When designing orchestrations, keep these security considerations in mind.

General Flow Orchestration Limits

When using orchestrations, keep orchestration limits, flow limits, and Apex governor limits in mind.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**Per-Org Limit**

**Enterprise,**
**Unlimited,**
**Performance,**
**or Developer**
**Editions**

Versions per orchestration 50

Active flows plus orchestrations 2,000

Total flows plus orchestrations 4,000

SEE ALSO:

_[Automate Your Business Processes](https://help.salesforce.com/s/articleView?id=sf.flow_considerations_usage_entitlements.htm&language=en_US)_ : Flow Usage-Based Entitlements

_Sales Productivity_ [: Email Allocations per Edition](https://help.salesforce.com/s/articleView?id=sf.allocations_email_general.htm&language=en_US)

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_event_limits.htm)_ : Platform Event Allocations


Automate Your Business Processes with Salesforce Flow Flow Orchestration Limits and Considerations

#### Considerations for Orchestrations

Keep these considerations in mind when designing and using orchestrations.

Entry and Exit Condition Requirements

Resources selected for a requirement for a step entry condition or a stage or step exit condition can
contain orchestration resources or global variables. There are limitations for what can be included
in a requirement.

**•** To use a record for the Resource or Value fields, you must select a field on the record.

**•** The referenced record must use fields from its object, not fields from a related record.

Record-Change-Triggered Flow Orchestration Events

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

A requirement for a step entry condition or a stage or step exit condition can contain a reference
to a record. Changes to that record can trigger the orchestration to evaluate the status of the current stage and the outstanding steps
within it. There are limitations for when the record can trigger condition evaluations.

**•** The referenced record’s parent object must support change events.

**•** The referenced record fields aren’t IsDeleted, SystemModeStamp, or any field that’s derived from a related record or a formula.

**•** The referenced record is null or has an invalid ID.

**•** The referenced record is a global variable in an autolaunched orchestration.

**•** The referenced record is a global variable other than $Record in a record-triggered orchestration.

Input Values for Flows

If the combined input values for a flow called by an orchestration step is more than 32,768 characters, the orchestration fails. This error
can be caused by passing one or more records to a flow called by a step. To avoid this error, pass a record ID to the referenced flow, and
use a Get Records element in the flow with the passed ID. Using a passed ID with a Get Records element also means that you always
have the latest version of the record.

Email Notifications

When a flow called by a step fails and causes an orchestration to fail, two email notifications are sent.

**•** A flow error notification

**•** An orchestration error notification

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_orchestrator_enable_object_sharing.htm&language=en_US)_ : StandardObjectNameChangeEvent


Automate Your Business Processes with Salesforce Flow Flow Orchestration Entitlements

#### Considerations for Evaluation Flows

Keep these considerations in mind when using evaluation flows as entry or exit conditions.

An evaluation flow is a flow with a process type of Evaluation Flow. It’s an autolaunched flow that
contains a predefined Boolean output variable named `isOrchestrationConditionMet` .

General Guidelines

Use an evaluation flow to pause an orchestration until a specific field update occurs.

Don’t loop through records or make external callouts in evaluation flows.

To pass variables from the orchestration into an evaluation flow, use evaluation flow input variables.

Output Variable

An evaluation flow has one output variable named `isOrchestrationConditionMet` .

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

The `isOrchestrationConditionMet` output variable must be Boolean and initialized to false.

The values of all output variables other than `isOrchestrationConditionMet` are discarded and not used by the orchestration.

#### Security Considerations for Orchestrations

When designing orchestrations, keep these security considerations in mind.

Shield Platform Encryption

For enhanced security, enable Shield Platform Encryption for the `Screen Flow Inputs` field
of the `Flow Orchestration Work Item` object.

SEE ALSO:

_Salesforce Help_ [: Strengthen Your Data's Security with Shield Platform Encryption](https://help.salesforce.com/s/articleView?id=sf.security_pe_overview.htm&language=en_US)

Flow Orchestration Entitlements

Flow Orchestration has usage-based entitlements. An orchestration _run_ is a running instance of an
orchestration. An _orchestration_ is an application built by your admin that uses stages, steps, and
decisions to organize a complex business process.

Flow Orchestration is automatically enabled for the editions listed in the Required Editions table.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Reference

Bookmark this page for quick access to information about orchestration elements, resources, events,
and more.

Flow Orchestration Resources
Each _resource_ represents a value that you can reference throughout the orchestration.

Flow Orchestration Elements
Each _element_ represents an action that the orchestration can execute. Orchestrations can contain
Decision and Stage elements.

Flow Orchestration Connectors
_Connectors_ determine the available paths that an orchestration can take at run time. On the
canvas in Flow Builder, a connector looks like an arrow that points from one element to another.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Flow Orchestration Operators
In conditions and filters, operators let you evaluate information and narrow the scope of an orchestration operation.

Flow Orchestration Version Properties
An orchestration version’s properties consist of its label and description. These values drive the field values that appear on the
orchestration’s detail page.

Flow Orchestration Resources

Each _resource_ represents a value that you can reference throughout the orchestration.

In Flow Builder, the Manager tab shows the resources that are available in the orchestration.

You can create some resources by clicking **New Resource** . The system providers certain resources,
such as global constants and global variables. Other resources are created when you add an element
to an orchestration. For example, when you add a Decision element, a resource for each decision
outcome is created.

#### **Resource Description Creatable from**

**the Resources Tab**

Constant Store a fixed value that you can use throughout an
orchestration.

Decision When you add a Decision element to an orchestration, its
Outcome outcomes are available as Boolean resources. If an outcome


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Resource** **Description** **Creatable from the**
**Resources Tab**

path has already been executed in the running orchestration, the resource’s value is
`True` .

```
Element

```

Any element that you add to an orchestration is available as a resource with the `was`
`visited` operator in decision outcome criteria. An element is considered visited
when it’s executed in a running orchestration.

Formula Calculate a value when the formula is used in the orchestration.

Flow Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .
Orchestration
Resource:
Global
ConstantsGlobal
Constant

Global Variable Use system-provided variables that reference information about the Salesforce org
or running user, such as the user’s ID or the API session ID.

Flow Organize the work done in an orchestration stage.
Orchestration
Resource: Step

Text Template Store text that can be changed and used throughout the orchestration. To format the
text, use HTML tags.

Variable Store a value that can be changed throughout the orchestration.

Flow Orchestration Resource: Constant
Store a fixed value that you can use throughout an orchestration.

Flow Orchestration Resource: Formula
Calculate a value when the formula is used in the orchestration.

Flow Orchestration Resource: Global Constants
Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .

Flow Orchestration Resource: Global Variables
Use system-provided variables that reference information about the Salesforce org or running user, such as the user’s ID or the API
session ID.

Flow Orchestration Resource: Step
Organize the work done in an orchestration stage.

Flow Orchestration Resource: Text Template
Store text that can be changed and used throughout the orchestration. To format the text, use HTML tags.

Flow Orchestration Resource: Variable
Store a value that can be changed throughout the orchestration.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Resource: Constant

Store a fixed value that you can use throughout an orchestration.

**Field** **Description**

```
API Name

```

The requirement for uniqueness applies only to elements within the
current orchestration. Two elements can have the same API name,
provided they’re used in different orchestrations.An API name can include
underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two
consecutive underscores.

`Description` Helps you differentiate the constant from other resources.

`Data Type` Determines the type of value that the constant can store. You can’t change
the data type of a previously saved constant.

`Value` The constant’s value. This value doesn’t change throughout the
orchestration.

Flow Orchestration Resource: Formula

Calculate a value when the formula is used in the orchestration.

**Field** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within
the current orchestration. Two elements can have the same API
name, provided they’re used in different orchestrations. An API
name can include underscores and alphanumeric characters
without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

`Description` Helps you differentiate this formula from other resources.

`Data Type` The data type for the value returned by the formula. You can’t
change the data type of a previously saved variable.

```
Decimal Places

##### `Formula`

```

Controls the number of digits to the right of the decimal point up
to 17 places. If you leave this field blank or set it to zero, only whole
numbers appear when your orchestration runs.

Available only when the data type is Number or Currency.

The formula expression that the orchestration evaluates at run
time. The returned value must be compatible with `Data Type` .

Some formula functions aren’t supported in Flow Builder.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Resource: Global Constants

Use fixed, system-provided values such as `EmptyString`, `True`, and `False` .

Example: When you create a Boolean variable, `$GlobalConstant.True` and
`$GlobalConstant.False` are supported. When you create a Currency variable, no
global constants are supported.

Null Versus Empty String

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

At run time, `{!$GlobalConstant.EmptyString}` and `null` are treated as separate, distinct values. For example:

**•** When you leave a text field or resource value blank, the value is `null` at run time. If you want the value to be treated as an empty
string, set it to `{!$GlobalConstant.EmptyString}` .

**•** For an orchestration condition, use the `is null` operator to check whether a value is `null` . If the condition compares two text
variables, make sure that their default values are correctly set to `{!$GlobalConstant.EmptyString}` or left blank ( `null` ).

Flow Orchestration Resource: Global Variables

Use system-provided variables that reference information about the Salesforce org or running user,
such as the user’s ID or the API session ID.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Global Variable Considerations for Flows

**•** In a record-triggered orchestration, the `$Record` global variable doesn’t contain the triggering record’s values for fields whose
values are derived from other records. Examples of derived fields include `Contact.Name` and `User.MediumPhotoUrl` .

**•** Multi-select picklist, time, and location global variables are available only in formulas.

**•** If a field in the database has no value, the corresponding merge field returns a blank value. For example, if no value is set for your
org’s Country field, `{!$Organization.Country}` returns no value.

Flow Orchestration Resource: $Flow Global Variables
###### A $Flow global variable provides information about the running orchestration. Some variables contain system-provided values.

You can update the other variables throughout the orchestration by storing output values in the variables.

###### Flow Orchestration Resource: $Flow Global Variables

###### A $Flow global variable provides information about the running orchestration. Some variables

contain system-provided values. You can update the other variables throughout the orchestration
by storing output values in the variables.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

**Global Variable**

**Supported** **Description** **Value Set By**
**Resource**
**Types**

###### $Flow.ActiveStages Stage $Flow.CurrentDate Text, Date, and

Date/Time

A collection of stages that are Assignment
relevant to the current path of the
flow.

This system variable references the
flow Stage resource, not the

orchestration Stage element. It can
only be used in flows, including
those flows called by an
orchestration step, but it isn’t
supported for orchestrations.

Date when the flow interview System
executes the element that
references the global variable.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Global Variable** **Supported** **Description** **Value Set By**
**Resource Types**

`$Flow.CurrentRecord` Text

`$Flow.CurrentStage` Stage

ID of a related record. The value must be a single Assignment
ID for a valid object. All custom objects and most
standard objects are valid.

When a user pauses the flow interview or the
interview executes a Wait element, the interview

is associated with this record by creating a
FlowRecordRelation record. If the ID isn’t valid,
the interview fails to pause.

The currently selected stage. Assignment

This system variable references the flow Stage
resource, not the orchestration Stage element.

It can only be used in flows, including those
flows called by an orchestration step, but it isn’t
supported for orchestrations.

`$Flow.CurrentDateTime` Text, Date, and Date and time when the flow interview executes System
Date/Time the element that references the global variable.

`$Flow.FaultMessage` Text System fault message that can help flow System
administrators troubleshoot runtime issues.

`$Flow.InterviewGuid` Text Unique identifier for the interview. System

`$Flow.InterviewStartTime` Text, Date, and Date and time when the flow interview started. System
Date/Time For a flow launched by a Subflow element,

`$Flow.InterviewStartTime` indicates
when the initial parent flow started.

Flow Orchestration Resource: Step

Organize the work done in an orchestration stage.

Orchestrations have background steps and interactive steps.

Note: The Step resource in Flow Orchestration isn’t related to the discontinued Step element
in Flow Builder.

Background Steps

Background steps call autolaunched flows and run without user interaction.

**Field** **Description**

`Label` Helps you identify the element on the canvas.

`API Name` Automatically populated if empty when you fill out the `Label` field and
press TAB.The requirement for uniqueness applies only to elements within

the current orchestration. Two elements can have the same API name,


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

provided they’re used in different orchestrations. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and can’t end with an underscore.
It also can’t have two consecutive underscores.

```
   Description
```

Helps you remember what this resource does. When editing an element, appears after you click .

`Condition` Identifies the method used to determine whether a step is ready to start.

`Step Name` Specifies a step that must be marked complete before the current step can start. Available when the
entry condition is set to When another step is marked complete the step starts.

`Evaluation Flow` Specifies the flow that determines if the step can start. Available when the entry condition is set to
When the specified evaluation flow returns True, the step starts.

`Flow` Specifies which autolaunched flow to run for a step.

Interactive Steps

Interactive steps call screen flows and require user interaction.

**Field** **Description**

`Label` Helps you identify the element on the canvas.

`API Name` Automatically populated if empty when you fill out the `Label` field and press TAB.The requirement
for uniqueness applies only to elements within the current orchestration. Two elements can have the

same API name, provided they’re used in different orchestrations.An API name can include underscores
and alphanumeric characters without spaces. It must begin with a letter and can’t end with an
underscore. It also can’t have two consecutive underscores.

```
   Description
```

Helps you remember what this resource does. When editing an element, appears after you click .

`Condition` Identifies the method used to determine whether a step is ready to start or can be considered complete.

`Step Name` Specifies a step that must be marked complete before the current step can start. Available when the
entry condition is set to When another step is marked complete the step starts.

`Evaluation Flow` Specifies the flow that determines if the step can start or be marked complete. Available when the
entry condition is set to When the specified evaluation flow returns True, the step starts. Also available

when the exit condition is set to When the specified evaluation flow returns True, the step is marked
Completed.

`Flow` Specifies which screen flow to run for a step.

`Record ID` Specifies the ID of the record where the Work Guide displays the screen flow to the assigned user.

`Username` Specifies the user assigned to complete the screen flow.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Step Status

Flow Orchestration Resource: Text Template

Store text that can be changed and used throughout the orchestration. To format the text, use
HTML tags.

**Field** **Description**

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within the current
orchestration. Two elements can have the same API name, provided they’re
used in different orchestrations.An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and
can’t end with an underscore. It also can’t have two consecutive
underscores.

`Description` Helps you differentiate this text template from other resources.

##### Text Template The text for the template. To reference information from other resources,

use merge fields.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

Rich Text

Plain Text

Control the text font, size, color, and alignment. Add HTML links, bullet points, or numbered lists. Rich

text is on by default. To change to rich text, click .

Send email core actions use plain text. Some custom actions from AppExchange or built by Salesforce

developers also expect plain text. To change to plain text, click .

Flow Orchestration Resource: Variable

Store a value that can be changed throughout the orchestration.

**Field** **Description**

`Apex Class` Defines fields for the Apex-defined data type. Only fields with the
@AuraEnabled annotation are available in an orchestration.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

```

The requirement for uniqueness applies only to elements within the
current orchestration. Two elements can have the same API name,
provided they’re used in different orchestrations. An API name can include
underscores and alphanumeric characters without spaces. It must begin
with a letter and can’t end with an underscore. It also can’t have two
consecutive underscores.

`Description` Helps you differentiate this variable from other resources.

```
Data Type

```

Determines the types of values that the variable can store. You can’t
change the data type of a previously saved variable.

The Record data type can store multiple field values for one record. The
Apex-defined data type can store multiple field values for one Apex class.

Looking for sObject? In Flow Builder, that data type changed to Record.

`Allow multiple` When selected, the resource is a collection variable. You can store a list
`values` of values in collection variables. Collection variables can store only values
`(collection)` that are compatible with their data type. When the data type is Record,
the collection variable can only store values for the associated object’s
records.

For example, store multiple email addresses in a collection variable, and
reference the collection variable to send an email.

```
Object

```

The object whose field values you can store in the variable. You can’t
change the object of a previously saved variable.

Available only when the data type is Record.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

```
Decimal Places

Availability Outside

the Flow

Default Value

```

Controls the number of digits to the right of the decimal point up to 17 places. If you leave this field
blank or set it to zero, only whole numbers appear when your orchestration runs.

Available only when the data type is Number or Currency.

When a variable is available for input, it can be set at the start of the orchestration, such as when an
orchestration is started from a Lightning page.

Disabling input or output access for an existing variable can break the functionality of applications
and pages that call the orchestration and access the variable. For example, you can access variables
from URL parameters, processes, and other flows.

This field doesn’t affect how variables are assigned or used within the same orchestration.

Determines the variable value when the orchestration starts. If you leave this field blank, the value is
`null` .

Not available for Picklist and Multi-Select Picklist variables.

Flow Orchestration Elements

Each _element_ represents an action that the orchestration can execute. Orchestrations can contain
##### Decision and Stage elements.

In Flow Builder, the Add Element menu shows the types of elements that you can add to the flow
by selecting them. For a list of all elements already added to the orchestration, see the Elements
section of the Manager tab in the Toolbox.

Flow Orchestration Element: Decision
Evaluate a set of conditions, and then route users through the orchestration based on the
outcomes of those conditions. This element performs the equivalent of an if-then statement.

Flow Orchestration Element: Stage
Group a series of related steps in an orchestration.

Flow Orchestration Element: Decision

Evaluate a set of conditions, and then route users through the orchestration based on the outcomes
of those conditions. This element performs the equivalent of an if-then statement.

Outcomes

For each path that the orchestration can take, create an outcome. For each outcome, specify the
conditions that must be met for the orchestration to take that path. To relabel the path that the
flow takes if no outcome’s conditions are met, click **Default Outcome** .

**Field** **Description**

`Label` Identifies the connector for this outcome on the canvas.


EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

**Field** **Description**

`Outcome API` The requirement for uniqueness applies only to elements within the current orchestration. Two elements can
`Name` have the same API name, provided they’re used in different orchestrations.An API name can include underscores
and alphanumeric characters without spaces. It must begin with a letter and can’t end with an underscore. It
also can’t have two consecutive underscores.

`Condition` Determines whether the orchestration takes this outcome’s path. Sets logic and conditions for each outcome
`Requirements` that determine if the orchestration follows its path.

```
   to Execute

   Outcome

```

`When to` Available on record-triggered orchestrations. Determines whether this outcome’s path is taken based on
`Execute` whether the triggering record is updated to meet the condition requirements. For example, the opportunity
`Outcome` update that triggered the orchestration to run changed its stage to Closed Won from any value that isn’t Closed
Won.

Flow Orchestration Element: Stage

Group a series of related steps in an orchestration.

##### Stages run sequentially, one stage at a time, and contain steps.

Note: The Stage element in Flow Orchestration isn’t related to the Stage resource in Flow
Builder.

**Field** **Description**

`Label` Identifies the name for this stage on the canvas.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

```
API Name

Set Exit

Condition

```

The requirement for uniqueness applies only to elements within the current
orchestration. Two elements can have the same API name, provided they’re
used in different orchestrations. An API name can include underscores and
alphanumeric characters without spaces. It must begin with a letter and can’t
end with an underscore. It also can’t have two consecutive underscores.

Determines when a stage can be considered complete.

**When all steps have been marked Complete, the stage is marked**
**Complete**
The stage is marked complete and the orchestration moves to the next
element when every step in a stage is marked complete.

**When the specified evaluation flow returns True, the stage is marked**
**Complete**
The orchestration runs a specified evaluation flow to determine if the stage
can be marked complete. The orchestration doesn’t mark the stage complete
and move to the next element until the specified evaluation flow’s
`isOrchestrationConditionMet` output variable returns true.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Stage Status

Flow Orchestration Connectors

#### Connectors determine the available paths that an orchestration can take at run time. On the canvas

in Flow Builder, a connector looks like an arrow that points from one element to another.

**Label** **Example** **Description**

_Unlabeled_ Identifies which element to execute next.

_`Decision`_ Identifies which element to execute when
_`outcome`_ the criteria of a Decision outcome are met.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

_Go To_

Identifies which element to go to and
execute next. Use to create loops in an
orchestration.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Flow Orchestration Operators

In conditions and filters, operators let you evaluate information and narrow the scope of an
orchestration operation.

Flow Orchestration Operators in Decision Elements
Use condition operators to verify the value of a selected resource. Conditions are used in Decision
elements.

Flow Orchestration Operators in Decision Elements

Use condition operators to verify the value of a selected resource. Conditions are used in Decision
elements.

Use this reference to understand the supported operators. The list is organized according to the
data type that you select for Resource.

**•** Apex-Defined

**•** Boolean

**•** Collection

**•** Currency

**•** Date

**•** Date/Time

**•** Multi-Select Picklist

**•** Number

**•** Picklist

**•** Record

**•** Text

Apex-Defined

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

To determine which operators are supported, match the _`@AuraEnabled`_ attribute’s Apex data type with the Flow Orchestration data
type in this reference.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Boolean

Check whether a Boolean resource’s value matches another value or resource.

Collection

Check whether a Collection resource’s value contains or matches another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Currency and Number

Check whether a Currency or Number resource’s value matches, is larger than, or is smaller than another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Date and Date/Time

Check whether a Date or Date/Time resource’s value matches, is before, or is after another value or resource.

Picklist

Check whether a Picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Multi-Select Picklist

Check whether a multi-select picklist resource’s value matches or contains another value or resource.

Note: These operators treat the resource’s value as a text value. If the resource’s value includes multiple items, the operators treat
the value as one string that happens to include semicolons. It doesn’t treat each selection as a different value. For example, the
operators treat `red; blue; green` as a single value rather than three separate values.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference

Record

Check whether a record resource’s value matches another value or resource.

Text

Check whether a Text resource’s value matches, contains, ends with, or starts with another value or resource.


Automate Your Business Processes with Salesforce Flow Flow Orchestration Reference


## Automate Your Business Processes with Salesforce Flow Suggest Options to Users with Recommendation Strategies

Flow Orchestration Version Properties

An orchestration version’s properties consist of its label and description. These values drive the field
values that appear on the orchestration’s detail page.

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

This feature is supported in
Government Cloud and
Government Cloud Plus.

## Suggest Options to Users with Recommendation Strategies

Display the right recommendations to the right people at the right time with Einstein Next Best
Action. Create and display offers and actions for your users that are tailored to meet your unique
criteria. Develop a strategy that applies your business logic to refine those recommendations. Your
strategy distills your recommendations into a few key suggestions, like a repair, a discount, or an
add-on service. Display the final recommendations in your Lightning app or Experience Builder site.

Note: Where possible, we recommend building strategies in Flow Builder using the
Recommendation Strategy flow type, but you can also create them in Strategy Builder.

Get Started with Einstein Next Best Action
Just getting started with Einstein Next Best Action? Follow these steps to complete each phase
of the Next Best Action setup process, create personalized recommendations for your users,
and put decisions into action.

Einstein Next Best Actions Considerations
Keep these considerations in mind when working with strategies and recommendations.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Einstein Next Best Action Entitlements
Einstein Next Best Action has usage-based entitlements. All orgs receive a free monthly allowance of Next Best Action requests. If
your usage exceeds your allowance of free monthly requests or any entitlements that you purchase, Salesforce contacts you to
discuss additions to your contract. To track your usage, from Setup, navigate to **Company Information** .


### Automate Your Business Processes with Salesforce Flow Get Started with Einstein Next Best Action

Create Recommendations
Create offers or actions to recommend to users using Einstein Next Best Action. Recommendations are standard Salesforce records,
similar to accounts and contacts, that are processed by strategies and associated with flows. Strategies determine which
recommendation records are surfaced using business rules, predictive models, and other data sources. The result of this process is
context-specific recommendations that you present to your users.

Building a Strategy
A strategy determines when and how to present an Einstein Next Best Action recommendation on a Salesforce Lightning record
page. For example, if you want to offer a discount to a subset of customers, create a strategy that collects the appropriate customer
records and identifies the discount option to present. To create a strategy, you can use Flow Builder (recommended) or Strategy
Builder.

Display Recommendations
After creating a strategy, choose a page to run your strategy and display your recommendations. You can use a Lightning record
page, an app’s home page, an Experience Cloud site page, a Visualforce page, or an external site, depending on where you want
recommendations to appear.

Report On and Track a Recommendation
Create a custom report type to report on and track recommendation data and strategy metrics. You can see the monthly total
recommendations that a Salesforce org’s strategies served. And you can analyze which recommendations are accepted and rejected,
who responds to them, and more.

SEE ALSO:

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

### Get Started with Einstein Next Best Action

Just getting started with Einstein Next Best Action? Follow these steps to complete each phase of
the Next Best Action setup process, create personalized recommendations for your users, and put
decisions into action.

Einstein Next Best Action is a solution that uses flows, strategies, and the Recommendation object
to recommend actions to users. You can display these recommendations on many different types
of pages, including Lightning pages in your Salesforce org, Experience Cloud sites, or external sites.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Get Started with Einstein Next Best Action

Recommendations are displayed to users with the option to accept or reject the recommended action. Each recommendation contains
an image, important text values such as button text and a description, and an assigned flow that runs when a user responds. They can
be stored and referenced in the Recommendation standard object, or they can be manually assembled when building a strategy.

Strategies determine which recommendations to display to users, based on your data and business processes. When you set up Einstein
Next Best Action on a page, you assign a strategy to that location, which then defines the recommendations that appear there.

You can control which recommendations are displayed in any situation, even if your org has a large number of recommendation records.
Strategies can filter recommendations based on any available value, including recommendation fields, fields related to the running user,
and fields related to the record that’s currently displayed.

Important: In Flow Builder, you define which recommendations are displayed by making sure that they’re in the
outputRecommendations collection variable at the end of the flow. In Strategy Builder, you define which recommendations are
displayed by making sure that they’re not filtered out when they reach the Output element.

**1.** Plan Your Recommendations and Automation

Decide where the recommendation appears, who it appears to, and the conditions in which it appears. Create a plan for the automation
that you want to run when a user accepts the recommendation.

**2.** Build a Flow

In Flow Builder, design and build the flow that runs when a user accepts or rejects the recommendation. You can assign only screen
flows and autolaunched flows to a recommendation. If an inactive or invalid flow is assigned, the recommendation isn’t displayed
to users.

**3.** Create Recommendations

Recommendations are standard Salesforce records, similar to accounts and contacts. To create recommendations, you can:

**•** Create recommendation records on the Recommendation object.

**•** Build recommendations from other data when creating your strategy. In Flow Builder, use the Recommendation Assignment
element or a custom Apex invocable action.

**•** [Generate recommendations automatically through AI with Einstein Recommendation Builder.](https://help.salesforce.com/s/articleView?id=sf.custom_ai_recommendation_builder.htm&language=en_US)

**4.** Create a Strategy

After you create a flow and make a plan for your recommendation records, use Flow Builder or Strategy Builder to create your strategy.
Where possible, we recommend building strategies in Flow Builder using the Recommendation Strategy flow type, but you can also
create them in Strategy Builder.

Some features can be used only in strategies created in Strategy Builder.

**•** Limiting repeated showings of some recommendations

**•** Displaying recommendations on an Experience Cloud site or external site

**•** Displaying AI-generated recommendations from Einstein Recommendation Builder

To build a strategy in Flow Builder, follow these steps.

**a.** Go to the Flows page in Setup, and click `New Flow` .

**b.** Select **Use a Template**, and then click **Next** .

**c.** Select the **Recommendation Strategy** flow type, and then click **Create** .

**d.** To retrieve data from Salesforce records, such as the Recommendations object or an object related to the currently displayed
record, add Get Records elements. To filter which recommendations are stored in the element’s collection, use condition
requirements in the Get Records element. Or you can build recommendations from other data with the Recommendation
Assignment element or a custom Apex invocable action.


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**e.** To limit the number of recommendations that users see, add logic elements. Use Collection Sort and Collection Filter elements
to arrange and reduce the recommendations from the Get Records collection. If needed, you can also add other Flow elements
such as Decision and Loop to create more complex, branching logic.

**f.** To set recommendations in the `outputRecommendations` collection, add the Assignment element. When running a
strategy built in Flow Builder, Einstein Next Best Action displays only recommendation records in the
`outputRecommendations` collection.

**5.** Display Next Best Actions

After creating a strategy, choose a page to run your strategy and display your recommendations. You can use a Lightning record
page, an app’s home page, an Experience Cloud site page, a Visualforce page, or an external site, depending on where you want
recommendations to appear.

**•** Einstein Next Best Action Component

Use the Einstein Next Best Action component to display recommendations to users on most Lightning pages within your
Salesforce org, including record pages, home pages, and app pages.

**•** [Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

Use the Suggested Actions component to display recommendations on Experience Cloud sites. This component can run only
strategies created in Strategy Builder.

SEE ALSO:

Build a Flow

Create Recommendations

Strategy Builder Strategies

Display Recommendations

Launch a Flow When a Recommendation Is Accepted or Rejected

Einstein Next Best Action Component

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

### Einstein Next Best Action Examples

These examples walk you through the process of creating Einstein Next Best Action components.


EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

#### Offer a Gift Basket to Each Account

Use a Next Best Action component on the Lightning Account record page to offer a gift basket to
each of your accounts. When a customer accepts the offer, a form opens to collect the recipient’s
name and shipping address. After the form is submitted, a request email is sent to the shipping
department.

To configure this Einstein Next Best Action recommendation:

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**1.** Create an action flow on page 753 that executes when the gift basket recommendation is accepted.

**2.** Create a recommendation on page 755 that specifies how to present the gift basket offer.

**3.** Create a recommendation strategy flow on page 756 that determines when and how the recommendation is presented.

**4.** Add a Next Best Action component on page 757 that displays the recommendation on the Account record page and executes the
strategy.

Create an Action Flow

Create a flow that collects the recipient’s name and address and sends an email to the shipping department.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start From Scratch** and then click **Next** .

**3.** Select the **Screen** flow type and then click **Create** .

**4.** To collect the recipient’s name and address, add a Screen element to the flow.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**a.** Enter a label and API name.

**b.** Drag the **Name** and **Address** components to the canvas and assign an API name to each.

**c.** Click **Done** .

**5.** To create the text of the email message to send to the shipping department, click **New Resource** in the Flow Builder Toolbox. If the
toolbox isn’t visible, toggle the toolbox icon in the upper left corner of the Flow Builder canvas.

**a.** Add a Text Template resource type.

**b.** Enter _`EmailBody`_ as the API name.

**c.** In the Body area, enter the email text, inserting the name and address resources.

**d.** Click **Done** .

**6.** To create a task for the shipping department, click below the Screen element and add an Action element to the flow.

**a.** In the Action dropdown list, enter _`Send Email`_ and select the **Send Email** action.

**b.** Enter a label and API name.

**c.** For Body, select the **EmailBody** text element.

**d.** Enter a subject line.

**e.** For Recipient Email Addresses (comma-separated), select **Include** and add the email address of the shipping department.

**f.** To allow rich text formatting for the message, select Include and select the **True** global constant.

**g.** Set any other values as needed.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**h.** Click **Done** .

**7.** Save the flow and name it _`Gift Basket Offer`_ .

**8.** Activate the flow.

**9.** To return to the Flows page, click **Back** .

Create a Recommendation Record

Create a recommendation that specifies how to present the gift basket offer.

**1.** From the App Launcher ( ), in the Quick Find box, enter _`Recommendations`_, and select **Recommendations** .

**2.** Click **New** .

**3.** Enter a name and description for the recommendation.

The description appears in the Next Best Action component on the Lightning record page.

**4.** For **Action**, select the action flow that you created.

**5.** To add an image (optional), click **Upload Image** and follow the instructions.

For best results, use a 1000 px x 380 px image at 72 dpi or one with a similar ratio.

**6.** Enter text for the acceptance and rejection buttons.

**7.** Select the target audiences for the recommendation.

**8.** Click **Save** .

The Is Action Active checkbox is automatically selected, which makes the recommendation available to Einstein Next Best Action.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

Create a Recommendation Strategy Flow

The recommendation strategy flow determines when and how the recommendation is presented.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Use a Template** and then click **Next** .

**3.** Select the **Recommendation Strategy** flow type and then click **Create** .

**4.** To specify which records to use for the recommendation, add a Get Records element to the flow.

**a.** Enter a label and API name.

**b.** Select the **Account** object.

**c.** In the Filter section, add the condition _`Id equals recordId`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

**5.** To load possible recommendations into the strategy, add a Get Records element.

**a.** Enter the label _`Get Gift Recommendation`_ and the API name. _`Get_Gift_Recommendation`_ .

**b.** Select the **Recommendation** object.

**c.** In the Filter section, add the condition _`Name contains Gift Basket`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

In Flow Builder, you define which recommendations are displayed by making sure that they’re in the outputRecommendations
collection variable at the end of the strategy flow. The next step uses the Assignment element to add the recommendations to
outputRecommendations. To learn how to use the Limit Repetition element to assign the outputRecommendation variable while
also limiting the number of times that the user sees the recommendation, see Create Recommendations Based on Customer
Satisfaction Scores on page 758.

**6.** To move the recommendation output out of this flow so it becomes available to Einstein Next Best Action, click **+** below the
Recommendation Assignment element and add an Assignment element.

**a.** Enter a label and API name.

**b.** For Variable, select **outputRecommendations** .

**c.** For Operator, select **Equals** .


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**d.** For Value, select **Recommendations from Get Gift Recommendation** .

**e.** Click **Done** .

**7.** Save the flow and name it _`Gift Strategy`_ .

**8.** Activate the flow.

**9.** To return to the Flows page, click **Back** .

Display the Next Best Action Recommendation

Display the Next Best Action recommendation on the Account record page.

**1.** Open an Account record page.

**2.** Click the Setup icon ( ), and select **Edit Page** .

**3.** Drag the Einstein Next Best Action component to the desired location on the page layout.

**4.** Add _`Gift Basket Offer`_ as the component title.

**5.** For Strategy Source, select **Flow Builder** and then select the name of the recommendation strategy.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**6.** Save your changes.

**7.** Return to the Account record and refresh the page.

The recommendation is displayed. If the account rep clicks **Yes**, a form opens with entries for name and address. Completing the form
generates an email request for the shipping department to fulfill the order.

#### Create Recommendations Based on Customer Satisfaction Scores

This example lets a customer service or account rep base a Next Best Action recommendation on
whether a customer has a high or low customer satisfaction (CSAT) score. For customers with a low
CSAT, a rep can offer the customer a discount on their service contract renewal. For customers with
a high CSAT score, the rep can offer a new product preview.

Preparation

To record customer satisfaction scores and use them to determine which recommendation to
display, this example includes two custom fields. To follow along with the example, set up these
two fields before you begin.

Contact object custom field:

**•** Field Label: CSAT score

**•** API Label: CSAT_score

**•** Field type: Number (length 2, decimal places 0)

Recommendation object custom field:

**•** Field Label: Category

**•** API Label: category_c

**•** Field type: Text (length 18)

To set up these Next Best Action recommendations:

**1.** Create action flows on page 759 for the high and low CSAT recommendations.

**2.** Create recommendation records on page 759 for the high and low CSAT recommendations.

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**3.** Create a strategy flow on page 760 that determines how the recommendations are presented to the customer service or account
rep.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**4.** On the Contact record page, add the Next Best Strategy component on page 763 that displays the recommendations and executes
the strategy.

Create Action Flows

Create two simple screen flows, one to execute an action for the low CSAT recommendation and one to execute an action for the high
CSAT recommendation.

This example keeps things simple by displaying a different text message for each recommendation but not incorporating other automation.
For a real-world application, you can add additional elements to implement the service contract discount and the new product preview.
For an example of using an action flow to send an email request, see Offer a Gift Basket to Each of Your Accounts on page 753.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Select **Start from Scratch**, and then click **Next** .

**3.** Select **Screen Flow**, and then click **Create** .

**4.** Add a Screen element to the flow.

**5.** Enter a label and API name.

**6.** Drag a **Display Text** component to the canvas.

**7.** Enter an API name for the component.

**8.** Add text for the high or low CSAT recommendation.

**9.** Click **Done**

**10.** Save the flow and name it _`CSAT Action Flow - Discount`_ or _`CSAT Action Flow - Product Preview`_ .

**11.** Activate the flow.

**12.** Repeat these steps to create the second action flow.

Create Recommendation Records

Create records for the low CSAT and high CSAT recommendations.

**1.** From the App Launcher ( ), in the Quick Find box, enter _`Recommendations`_, and select **Recommendations** .

**2.** Click **New** .

**3.** Enter a name and description for the recommendation.

The description appears in the Next Best Action component on the Lightning record page. Make the description specific to the
particular recommendation (low CSAT or high CSAT).


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**4.** For **Action**, select the low CSAT or high CSAT action flow.

**5.** To add an image (optional), click **Upload Image** and follow the instructions.

For best results, use a 1000 px x 380 px image at 72 dpi or one with a similar ratio.

**6.** Enter text for the acceptance and rejection buttons.

**7.** Select the target audiences for the recommendation.

**8.** Click **Save** .

The Is Action Active checkbox is automatically selected, which makes the recommendation available to Einstein Next Best Action.

**9.** Repeat these steps to create the second recommendation record.

Create a Recommendation Strategy Flow

The recommendation strategy flow specifies when and how the recommendations are presented on the Contact record page.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** Click **Use a Template**, and then click **Next** .

**3.** Click **Recommendation Strategy**, select a template, and then click **Create** .

**4.** Load the Contact records that you want to use for your recommendations by adding a Get Records element to the flow.

**a.** Enter a label and API name.

**b.** Select the **Contact** object.

**c.** In the Filter section, add the condition _`Id equals recordId`_ .

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .

**5.** To accommodate different recommendations based on the customer’s CSAT score, add a decision step after the Get Records step.


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**a.** Enter the label _`CSAT Score?`_ and the API name _`CSAT_score`_ .

**b.** Create a _`Low CSAT`_ outcome with the condition that the value of the CSAT Score field on the Contact record is 3 or lower.

**c.** Create a _`High CSAT`_ outcome with the condition that the value of the CSAT Score field on the Contact record is 4 or higher.

**d.** Keep the Default outcome as-is for customers who don’t have a CSAT score.

**e.** Click **Done** .

**6.** Bring in the appropriate recommendation for the low and high CSAT conditions by adding a Get Records element for each.

**a.** Enter a label and API name.

**b.** Select the **Recommendation** object.

**c.** In the Filter section, add the appropriate condition by selecting the API name of the Category field in the Recommendation
object and specifying the low or high condition.

**d.** Select the options to store all records and all fields.

**e.** Click **Done** .


Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Examples

**7.** To show the recommendation only one time for each Account record and to assign the flow output, add a Limit Repetition element
for the low and high score paths.

**a.** Enter a label and API name.

**b.** For Recommendation Collection, select the low score or high score recommendation.

**c.** For Look for These Records, select **Accepted or Rejected** .

**d.** For Look for This Many Messages, keep the default setting of _`1`_ .

**e.** To make the output from this path available to Next Best Action, click **Advanced**, select **Manually assign variables**, and then
select **outputRecommendations** .

**f.** Click **Done** .

**8.** Save the flow and name it _`CSAT Strategy Flow`_ .


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Actions Considerations

**9.** Activate the flow.

**10.** To return to the Flows page, click **Back** .

Display the Next Best Action Recommendations

To make the recommendations available to the customer service or account rep, display the Next Best Action component on the Contact
record page.

**1.** Open a Contact record page.

**2.** Click the Setup icon ( ), and select **Edit Page** .

**3.** Drag the Einstein Next Best Action component to the desired location on the page layout.

**4.** Add _`CSAT Recommendations`_ as the component title.

**5.** For Strategy Source, select **Flow Builder** and then select the name of the recommendation strategy.

**6.** Save your changes.

**7.** Return to the Contact record and refresh the page.

Based on the contact’s CSAT score, the correct recommendation is displayed. When the customer accepts the offer and the account rep
clicks **Yes I Accept**, a form opens with the appropriate confirmation message.

### Einstein Next Best Actions Considerations

Keep these considerations in mind when working with strategies and recommendations.

Einstein Next Best Action relies on flows, recommendations, strategies, and components, and has
standard objects for reporting.

Flows

**•** All Recommendation objects reference a flow. If you don’t have any flows, you can’t surface a
recommendation.

**•** Strategies only load recommendations with active flows.

**•** When a flow is executed via REST API, the flow runs in the context of the user who is
authenticated via REST API. The running user’s profile and permission sets determine the object


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Actions Considerations

permissions and field-level access of the flow. We recommend that you create a profile and permission sets for users who run the
flow.

Recommendations

**•** Consider adding a custom category field to the recommendation object and layout. A category field gives you more control when
loading, sorting, and filtering recommendations and more options when creating flows.

**•** Create names, descriptions, acceptance labels, and rejection labels that are appropriate for your intended audience.

**•** Reusing a recommendation name creates a recommendation. It doesn’t overwrite an existing recommendation. Duplicated names
can cause strategies to display duplicate recommendations to customers.

**•** All flows, both inactive and active, display in the Action dropdown list. After you save your recommendation, you can see if the flow
is active.

**•** You can create a recommendation based on a flow that isn’t active, but no strategy loads it until the flow is activated.

Strategies

**•** All strategies require at least one recommendation.

**•** In Strategy Builder, you can load and filter the records of a Recommendation object. Or load and filter the records of any object, and
convert them into recommendations at the end of the strategy using the Map element.

**•** Load elements require at least one criteria.

**•** Strategies only load recommendations that are based on active flows.

**•** The Limit Reoffer element in Strategy Builder lets you hide a recommendation from all users based on its responses. A recommendation
is hidden if users respond more than a defined number of times within a defined number of days. For limit reoffers to work,
recommendations must have a unique record ID. If you want to continue to test a recommendation as a flow-entry point, delete
individual records from the Recommendations Reaction table with Rest API calls:

```
     GET /connect/recommendation-strategies/reactions

     { onBehalfOf: “005B00000018jK4IAI” }

     //Returns a list of reactions

     //For each result, if the reaction matches the strategyId of the strategy you’re testing:

     DELETE /connect/recommendation-strategies/reactions/${reactionId}

```

**•** Strategy Builder is available only in Lightning Experience.

Tracking and Reporting Reactions

**•** For strategies created in Flow Builder, create custom report types using the Recommendation Strategy Metrics and Recommendation
Responses primary objects. For strategies created in Strategy Builder, create custom report types using the Recommendation Strategy
Metrics and Recommendation Reactions primary objects.

**•** For reports created from the Recommendation Reactions primary object to correctly display the recommendation source name and
ID for limit reoffers, recommendations must have a unique record ID.


### Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Entitlements

```
   Rights of ALBERT EINSTEIN are used with permission of The Hebrew University of Jerusalem.

   Represented exclusively by Greenlight.

```

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Write a Strategy Builder Expression

_Apex Reference Guide_ [: NextBestAction Class](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_static_methods)

### Einstein Next Best Action Entitlements

Einstein Next Best Action has usage-based entitlements. All orgs receive a free monthly allowance
of Next Best Action requests. If your usage exceeds your allowance of free monthly requests or any
entitlements that you purchase, Salesforce contacts you to discuss additions to your contract. To
track your usage, from Setup, navigate to **Company Information** .

Note: Next Best Action entitlement usage is based on a rolling 30-day period, beginning
when the org is created. Entitlement usage listed on the Company Information page in Setup
is based on the calendar month's usage, not the rolling 30-day usage.

Einstein Next Best Action is automatically enabled for the editions listed in the Required Editions
table.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Einstein Next Best Action Entitlements

#### Next Best Action Request

A _request_ is a call to the Next Best Action engine that causes a strategy to run and return recommendations.

#### Next Best Action Request

A _request_ is a call to the Next Best Action engine that causes a strategy to run and return
recommendations.

Each time a page with an Einstein Next Best Action component is loaded or refreshed in a browser,
Salesforce generates a new request. For example, when a case status changes from New to In
Progress, the data change on the page triggers a refresh. This action also applies to the Actions &
Recommendations and Suggested Actions components.

Requests are also made when:

**•** A field is updated on a record detail page that includes the Next Best Action component.

**•** A user enters data in the Subject or Description field of a site contact support page that includes
the Next Best Action component.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Another way to make a request is to call a Next Best Action REST API resource from your own web app. You can also call Next Best Action
REST API resources from an iOS or an Android app. The app can make requests in response to a custom UI and return recommendations.

Paying customers can see the number of requests their org has made by navigating from Setup to **Company Information**, **Usage-based**
**Entitlements**, **Maximum Next Best Action Requests available** .

SEE ALSO:

Display Recommendations

Einstein Next Best Action Entitlements


### Automate Your Business Processes with Salesforce Flow Create Recommendations Create Recommendations

Create offers or actions to recommend to users using Einstein Next Best Action. Recommendations
are standard Salesforce records, similar to accounts and contacts, that are processed by strategies
and associated with flows. Strategies determine which recommendation records are surfaced using
business rules, predictive models, and other data sources. The result of this process is context-specific
recommendations that you present to your users.

Note:

**•** Salesforce has both a Recommendation object for Einstein Next Best Action (that’s this
page) and a Recommendation component for Experience Builder sites. The
Recommendation component isn’t related to Next Best Action.

**•** If you don't see Recommendations in the App Launcher, in Setup, select Default On in
the Recommendations tab settings for your user profile or permission set.

**•** You can load and filter the records of a Recommendation object. Or load and filter the
records of any object, and convert them into recommendations at the end of a strategy
using the Map element.

Before creating recommendations, create the action flow that runs when a customer accepts the
recommendation. For examples of action flows for Next Best Action, see Einstein Next Best Action
Examples on page 752.

**1.** In the Recommendations tab, click **New Recommendation** .

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage
recommendations:

**•** Modify All Data

OR

Manage Next Best
Action
Recommendations

**2.** Enter a friendly name (1) and a brief description (2) for your recommendation. The description appears on the recommendation that
is surfaced to users.

**3.** Optionally, click to upload an image (3) that you can display as a header for your recommendation. For best results, use a 1000 by
380 pixel image at 72 DPI, or an image with a similar ratio. You can choose whether the image displays using component properties.
After it’s uploaded, a thumbnail of your image displays on the Recommendations page. Customers can see the full image as a header
for your recommendation in either the Lightning App Builder or Experience Builder component.

**4.** Enter an acceptance label (4) and a rejection label (5) for the buttons that customers click to, respectively, accept and reject the
recommendation.

**5.** Create a flow. When a user accepts your recommendation, they’re taken to the flow specified in Action (6).


Automate Your Business Processes with Salesforce Flow Create Recommendations

**6.** Choose the flow that runs when a customer accepts the recommendation (6) and click **Save** . You can also choose a flow that runs
when a customer accepts or rejects the recommendation. The Action list displays both active and inactive flows. Choosing a flow
that isn't active hides the recommendation. When you’ve saved your recommendation, you can see if the flow is active from **Is**
**Action Active** (7).

**7.** Create a recommendation strategy in Strategy Builder that determines how your recommendations surface.

**8.** Optionally add a custom Category field to the Recommendation object and the Recommendation Layout. Adding a custom Category
field can simplify loading, filtering, and sorting recommendations in Strategy Builder.

Recommendation Fields
Recommendations are suggested actions that users see and interact with through Einstein Next Best Action strategies. When creating
a recommendation, use these fields to define its look and feel.

Launch a Flow When a Recommendation Is Accepted
Each recommendation is associated with a single flow. By default, Next Best Action launches a flow when a user accepts a
recommendation. The flow then performs an action, such as updating a case or sending an email.

Launch a Flow When a Recommendation Is Accepted or Rejected
Each recommendation is associated with a single flow. By default, Next Best Action launches a flow when a user accepts a
recommendation. The flow then performs an action, such as updating a case or sending an email. But you can also launch a flow
when a user rejects a recommendation, which gives you more flexibility. For example, a flow could run an automated process, write
to another system, or create a reminder email when a recommendation is rejected.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Add a Limit Repetitions Element to a Next Best Action Flow
You can add a Limit Repetitions element to your Recommendation Strategy flow to limit the number of times that the same
recommendation or offer appears on the same record or for the same user during a time period.

SEE ALSO:

Build a Flow

Strategy Builder Strategies

Display Recommendations

[View and Edit Tab Settings in Permission Sets and Profiles](https://help.salesforce.com/s/articleView?id=sf.users_tab_visibility.htm&language=en_US)

Get Started with Einstein Next Best Action

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

#### Recommendation Fields

Recommendations are suggested actions that users see and interact with through Einstein Next
Best Action strategies. When creating a recommendation, use these fields to define its look and
feel.

You can use these methods to create recommendations.

**•** Assemble recommendations as needed in Flow Builder or Strategy Builder.

**•** Create recommendations as standard Salesforce records, similar to accounts and contacts, in
the Recommendation object. You can create recommendation records on the Recommendations
tab in the App Launcher.

**•** [Generate recommendations automatically through AI with Einstein Recommendation Builder.](https://help.salesforce.com/s/articleView?id=sf.custom_ai_recommendation_builder.htm&language=en_US)

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Image (1)—The image that is shown in the recommendation. To display this image with the Einstein Next Best Action Lightning
page component, select `Show Image` when configuring the Lightning page component.

**•** Name (2)—The header text at the top of the recommendation. To display this text with the Einstein Next Best Action Lightning page
component, select `Show Title` when configuring the Lightning page component.

**•** Description (3)—Additional descriptive text displayed in the recommendation. To display this text with the Einstein Next Best Action
Lightning page component, select `Show Description` when configuring the Lightning page component.

**•** Acceptance Label (4)—The text of the button that accepts the recommendation. This option is always displayed.

**•** Rejection Label (5)—The text of the button that rejects the recommendation. To display this option with the Einstein Next Best
Action Lightning page component, select `Show Reject Option` when configuring the Lightning page component.

Use these fields to define how the recommendation runs.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Action

The flow that runs when a user selects the Accept option. To run this flow when the user accepts or rejects the recommendation, select
`Launch Flow on Rejection` when configuring the Einstein Next Best Action Lightning page component. If the referenced
flow is inactive, invalid, or has an unsupported Flow Type, the recommendation isn’t displayed to users. The supported flow types are
screen flows and autolaunched flows.

SEE ALSO:

Create Recommendations

Get Started with Einstein Next Best Action

#### Launch a Flow When a Recommendation Is Accepted

Each recommendation is associated with a single flow. By default, Next Best Action launches a flow
when a user accepts a recommendation. The flow then performs an action, such as updating a case
or sending an email.

For example, on a case, display a recommendation to the service agent to upsell a premium service
to the customer. When the agent accepts the recommendation, an autolaunched flow updates the
case and the customer’s order history and sends a receipt via email.

Or say that you have an autolaunched flow that sends a templated marketing campaign email to
a customer. Your service agents have to determine whether your customers are eligible for this
campaign. Doing so involves several clicks and complex calculations. Instead use Next Best Action
to check the customer’s eligibility and prompt the agent to accept the recommendation and launch
the flow.

**1.** In Flow Builder, configure a flow that’s associated with a recommendation. Be sure to activate
the flow because Next Best Action can’t call an inactive flow from a recommendation.

**2.** Add a flow action.

**3.** To add the flow, edit the recommendation.

SEE ALSO:

#### Launch a Flow When a Recommendation Is Accepted or Rejected


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Create Recommendations

#### Launch a Flow When a Recommendation Is Accepted or Rejected

Each recommendation is associated with a single flow. By default, Next Best Action launches a flow
when a user accepts a recommendation. The flow then performs an action, such as updating a case
or sending an email. But you can also launch a flow when a user rejects a recommendation, which
gives you more flexibility. For example, a flow could run an automated process, write to another
system, or create a reminder email when a recommendation is rejected.

For example, at a telecommunications company, the admin configures the Next Best Action
component to display recommendations to its customer service representatives (CSRs). When a
CSR accepts a recommendation for a customer who wants to purchase a discounted service, a flow
is launched to calculate the discount. The admin analyzes the reactions to the recommendation,
and is confused about why the CSRs are rejecting it. To help get answers, the admin uses Next Best
Action to launch a questionnaire flow every time the recommendation is rejected.

This feature is available for:

**•** The Einstein Next Best Action component used with Lightning record pages

**•** The Suggested Actions component used in Experience Builder

**•** The Actions and Recommendations component used with Lightning console apps

To assign a flow that runs when a customer accepts or rejects the recommendation, create an input
variable in the flow to accept the `isRecommendationAccepted` value. Then add a Decision
element to the flow that’s based on that value.

**1.** In Flow Builder, configure a flow that’s associated with a recommendation. Be sure to activate
the flow because Next Best Action can’t call an inactive flow from a recommendation.

**2.** Create the Boolean `isRecommendationAccepted` input variable.

**3.** Create a Decision element and use the `isRecommendationAccepted` variable in your
outcome conditions.

**4.** Create a decision outcome for what the flow does when the recommendation is accepted.

**5.** Create a decision outcome for what the flow does when the recommendation is rejected.


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Create Recommendations

**6.** Add any additional flow elements to handle each outcome path.

**7.** Add a flow action.

**8.** To add the flow, edit the recommendation.

**9.** When you add the Next Best Action component to a Lightning record page, select **Launch Flow on Rejection** .


Automate Your Business Processes with Salesforce Flow Create Recommendations

SEE ALSO:

Launch a Flow When a Recommendation Is Accepted

Flow Resource: Variable

Flow Element: Decision

Einstein Next Best Action Component


Automate Your Business Processes with Salesforce Flow Create Recommendations

#### Add a Limit Repetitions Element to a Next Best Action Flow

You can add a Limit Repetitions element to your Recommendation Strategy flow to limit the number
of times that the same recommendation or offer appears on the same record or for the same user
during a time period.

**•** You must have a collection of recommendations that has a valid value in the ID or
RecommendationKey fields. The RecommendationKey value must be a database ID or have
the syntax _`DYNAMIC_<custom id>`_ .

**•** If you include an Assignment element, from Actions, choose **Output from limit** . Or you can
skip this step and add the output from the Limit Repetitions element.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, and then select **Flows** .

**2.** Open or create a Recommendation Strategy.

**3.** After the collection of recommendations, add a Limit Repetitions element.

**4.** Enter a label and an API Name.

**5.** Add a description.

**6.** Search for and select the Recommendation Collection that you want to filter.

**7.** Select the responses that you want, and then enter the number of responses and days as whole
numbers.

Look Within This Many Days is based on days, not hours. If the number of days is set to 1 for an
accepted response, and the user accepts the recommendation at any time on Monday, the
recommendation doesn’t display again until the start of Wednesday. So a one-day time period
could be as few as 25 hours in duration or as many as 48 hours.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage
recommendations:

**•** Modify All Data

OR

Manage Next Best
Action
Recommendations

**8.** If you didn’t include an Assignment element, you can search for and select the collection that includes the limit repetition output.

**a.** In Advanced, select **Manually assign variables** .

**b.** From the Store Output Variables field, search for and select the output variable.

**9.** Click **Done** .

**10.** Save your work.


Automate Your Business Processes with Salesforce Flow Create Recommendations

Example:

**•** If you want one accepted response over 90 days, such as a password reset recommendation, and the user accepts one time
over 90 days, they don’t see the message again for 90 days. But if the user rejects the recommendation, they see the message
every time they reload the page until they accept it.

**•** If you want two accepted or rejected responses over 1 day, and a user accepts or rejects the recommendation only one time
every day, they still see the recommendation.

**•** If you want two accepted or rejected responses over 1 day, and a user accepts or rejects the recommendation twice on day
one, they don’t see the recommendation on day two. They see the recommendation again on day three.

If you add an Assignment element after the Limit Repetitions element and change the label for accept or reject, you must update the
limit repetitions output.

SEE ALSO:

Create Recommendations

Display Recommendations


### Automate Your Business Processes with Salesforce Flow Building a Strategy Building a Strategy

A strategy determines when and how to present an Einstein Next Best Action recommendation on
a Salesforce Lightning record page. For example, if you want to offer a discount to a subset of
customers, create a strategy that collects the appropriate customer records and identifies the
discount option to present. To create a strategy, you can use Flow Builder (recommended) or
Strategy Builder.

Note: When possible, we recommend building a strategy in Flow Builder using the
Recommendation Strategy flow type.

Why Choose Flow Builder Instead of Strategy Builder?

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Flow builder is a unified, feature-rich Salesforce tool for building business process automations and
is the home for all future flow automation features and enhancements. Strategy Builder is a legacy tool and no updates are planned for
it.

Strategy Builder Strategies
You can create strategies for Einstein Next Best Action using Strategy Builder or Flow Builder. Flow Builder is the recommended
method.

#### Flow Builder Strategies

A Flow Builder strategy specifies business logic and generates output for an Einstein Next Best
Action component on a Salesforce Lightning record page.

In a Flow Builder strategy, you generate recommendations in either of the following ways:

**•** Use predefined recommendations created in the Recommendations object on page 777. With
this method, you create recommendations individually in the Recommendation object and
then use them in one or more Next Best Action components. This method is best if you’re
creating a small number of recommendations.

**•** Create recommendations on the fly without using separate recommendation records on page
778. With this method, you create multiple recommendations dynamically in the strategy flow.
This method is best if you’re creating a large number of recommendations. For example, if you
have an extensive product list, you can create a different upsell recommendation for each
product in the list.

SEE ALSO:

Add and Edit Elements

Flow Element: Get Records

Flow Element: Assignment

Flow Element: Recommendation Assignment


EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Build a Strategy Flow Using Predefined Recommendations

Build a strategy flow based on predefined recommendations. This method works best if you have
a small number of recommendations and want to make them available to multiple Einstein Next
Best Action components. For example, you can create a recommendation that offers a discount to
a customer. You can then use the same recommendation when creating a strategy for birthday
discounts and for new customer discounts.

Before building your strategy flow, create recommendations in the Recommendations object on
page 767.

Note: If you want to create a large number of recommendations dynamically at one time,
you can build a strategy flow with on-the-fly recommendations on page 778 without creating
separate records in the Recommendation object.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** On the **Alt + Templates** tab, select the **Recommendation Strategy** flow type, and click
**Create** .

**3.** Load the records you want to use for your recommendation by adding a Get Records element
to the flow.

**a.** Enter a label and API name.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**b.** Select the object to use for the recommendations, such as the Accounts, Cases, or Contacts object.

**c.** In the Filter section, add conditions to limit which records from the object are used in your strategy.

**4.** Bring a predefined recommendation into the strategy by adding a Get Records element.

**a.** Enter a label and API name.

**b.** Select the **Recommendations** object.

**c.** In the Filter section, use conditions to specify the recommendation that you want to use.

**5.** Add other flow elements as needed to define the strategy.

**6.** Make your recommendation available for use in an Einstein Next Best Action component.

**a.** Add an Assignment element.

**b.** For Variable, select **outputRecommendations** .

**c.** For operator, select **Equals** .

**d.** For Value, select the predefined recommendation.

**7.** Save your flow.

**8.** Activate your flow.

You’re now ready to add a Next Best Action component to a Lightning record page. on page 807


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Build Strategy Using On-the-Fly Recommendations

Build a strategy flow with multiple recommendations that you create dynamically in bulk. For
example, you can create a strategy that offers a different upsell recommendation for each product
in your product list. With this method, you create recommendations directly in the strategy flow
without using separate Recommendation records.

Note: If you want to reuse recommendations in multiple Einstein Next Best Action
components, use pre-defined recommendations created in the Recommendations object
on page 777.

**1.** From Setup, in the Quick Find box, enter _`Flows`_, select **Flows**, and then click **New Flow** .

**2.** On the **Alt + Templates** tab, select the **Recommendation Strategy** flow type, and click
**Create** .

**3.** Load the records you want to use for your recommendations by adding a Get Records element
to the flow.

**a.** Enter a label and API name.

**b.** Select the object to use for the recommendations, such as the Product object.

**c.** In the Filter section, add conditions to limit which records from the object are used in your
strategy.

**4.** Add a Recommendation Assignment element.

**a.** Enter a label and API name.

**b.** For Record Collection Variable, select the variable that you generated with Get Records.

When you select the variable, the target fields are populated automatically.

**c.** Set values for the target fields:

**•** AcceptanceLabel—Button label to accept the offer.

**•** RejectionLabel—Button label to reject the offer.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

**•** ActionFlow—API name of the flow that performs an action when the offer is accepted or rejected.

**•** Description—Text that appears above the buttons in the Next Best Action component.

**5.** Make your recommendation available for use in an Einstein Next Best Action component.

**a.** Add an Assignment element.

**b.** For Variable, select **outputRecommendations** .

**c.** For operator, select **Equals** .

**d.** For Value, select the recommendation from the Recommendation Assignment step.

**6.** Save your flow.

**7.** Activate your flow.

You’re now ready to add a Next Best Action component to a Lightning record page on page 807.


Automate Your Business Processes with Salesforce Flow Building a Strategy

#### Strategy Builder Strategies

You can create strategies for Einstein Next Best Action using Strategy Builder or Flow Builder. Flow
Builder is the recommended method.

##### Tour the Strategy Builder Interface

Before you start building your strategy, learn about the primary pieces of Strategy Builder and
how they work together.

Create a Strategy with Strategy Builder
Once you’ve created flows and recommendation records, use Strategy Builder to funnel the
correct recommendations to your users at the right time.

Manage Strategy Builder Action Strategies
Test, troubleshoot, and create strategies using Strategy Builder management tools.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Strategy Builder Elements
Use this page to quickly access a list of Strategy Builder elements and learn how they work together to create unique strategies.

##### Tour the Strategy Builder Interface

Before you start building your strategy, learn about the primary pieces of Strategy Builder and how
they work together.

Find Strategy Builder in Setup by typing _`Strategies`_ or _`Next Best Action`_ in the Quick
Find box. Select **Next Best Action** .


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

Button Bar (1)

Manage your strategies with basic functions like Test and Save.

**•** **Test** runs the most recently saved version of your strategy and displays the recommendations that are surfaced for your users. Testing
your strategy allows you to determine if there are errors that must be fixed and confirms the recommendations that your users see.

**•** **Save** your strategies before you test them and before you leave Strategy Builder so you don’t lose your work.

**•** **Save As** allows you to duplicate a strategy and your currently saved work.

Elements, Manager, and Inspector Tabs (2)

Use the Toolbox to create the substance of your strategy. Add elements, connect external sources, and troubleshoot errors in your
strategy.

**•** From the **Elements** tab, drag new elements onto the canvas and create the building blocks of your strategy.

**•** From the **Manager** tab, add new connections from external sources or other Salesforce products.

**•** Use the **Inspector** tab to isolate specific elements and troubleshoot errors that appear during testing.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Canvas (3)

The canvas is a visual representation of your strategy. From here, you can rearrange elements and see how your recommendations are
flowing from one branch to the next and finally into the output.

SEE ALSO:

##### Create a Strategy with Strategy Builder

Manage Strategy Builder Action Strategies

Inspect Strategy Builder Element Results

##### Create a Strategy with Strategy Builder

Once you’ve created flows and recommendation records, use Strategy Builder to funnel the correct
recommendations to your users at the right time.

Before you start creating strategies, make sure that you create flows and recommendation records
that you can use in your strategy.

**1.** Open Strategy Builder. From Setup, enter _`Strategies`_ or _`Next Best Action`_ in the
Quick Find box, select **Next Best Action**, and click **New Strategy** .

**2.** Give your strategy a name and a description.

**3.** Select a context object from **Object Where Recommendations Display** .

Note: The object that you choose here provides the context for your entire strategy.

For example, if you plan to use this strategy on Case pages, select Case. When the strategy
executes and resolves your expressions, the Next Best Action engine interprets the
incoming recordId as a case object. The engine has to know to what type of object the
pages belong to resolve expressions correctly. Linking your strategy to a specific object
also enables Strategy Builder to provide intelligent assistance in other areas, such as the
Test feature.

**4.** Drag the appropriate elements onto the canvas.

Note: It’s best to start by adding a Load element, as loading recommendations is the
first step in any strategy.

**5.** Order your elements to make sure that recommendations are flowing through the correct
branches.

Note: Elements are divided into two main categories: Recommendation Logic and
Branch Logic. Recommendation Logic elements act directly on the recommendations
flowing into the element by filtering, sorting and limiting. Branch Logic elements act as
gates, using context information, such as the recordId of the page the user is viewing, to
decide which sets of recommendations to allow.

**6.** Save any changes to your strategy.

**7.** To make sure it’s working as expected, test your strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Note: If your strategy isn’t running properly or you see an unexpected error, try using the **Inspector** tab to find the problem.


Automate Your Business Processes with Salesforce Flow Building a Strategy

**8.** Display your strategy using the Suggested Actions component in Experience Builder or the Einstein Next Best Action component in
Lightning App Builder.

###### Write a Strategy Builder Expression

Create unique expressions using logic from the Salesforce expression builder to filter recommendations, select or deselect branches,
and determine which recommendations are available for consideration in a strategy.

Create a Strategy Builder Action Strategy Connection
Use Apex actions to integrate external data sources and information from your Salesforce org into your strategies.

Create a Custom Notification Flow for Next Best Action
Create a trigger in Process Builder to receive direct notifications about errors occurring in your strategies. Launch a flow to send error
information to your desired targets.

Create, Package, and Distribute a Strategy Builder Template
Enterprise developers can create and package strategy templates from Developer Edition orgs for use in multiple Salesforce orgs.
Independent software vendors can also publish templates on AppExchange for distribution to their subscribers. Strategies not
marked as templates in managed packages have intellectual property (IP) protection and can’t be edited or cloned. IP protection
safeguards proprietary information in your strategies.

SEE ALSO:

Test Strategy Builder Action Strategies

Inspect Strategy Builder Element Results

Create a Strategy with Strategy Builder

Build a Flow

###### Write a Strategy Builder Expression

Create unique expressions using logic from the Salesforce expression builder to filter
recommendations, select or deselect branches, and determine which recommendations are available
for consideration in a strategy.

Strategy Builder expressions, found on the Filter and Branch Selector elements, use standard
[Salesforce formula functions. To learn more about creating formulas in Salesforce, see Formula](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)
[Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

Strategies are designed to work with a particular object like Case or Contact. Strategy Builder
elements use `$Record` as a placeholder for the actual record that gets passed in when a strategy
runs.

**1.** Select the element you need for your strategy: **Filter** or **Branch Selector** .

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**2.** Enter your expression. You can build expressions in two different modes: standard and advanced. Standard is declarative: search
and select to build your formula. Use advanced mode for more complex expressions, when a given operator is unavailable in standard
mode, or when you use concatenation.

**3.** In standard mode, set up conditions. At run time, the conditions are evaluated in the order you specify.

**Column Header** **Description**

```
Resource

```

Recommendation resource whose value you want to evaluate, such as acceptance or rejection label,
action, ID, name. For example, a strategy is associated with a Case. Your resource can be
`$Record.Account.Type` or `$Record.Account.Contact.Name` .


Automate Your Business Processes with Salesforce Flow Building a Strategy

**Column Header** **Description**

`Operator` Select an appropriate operator for that resource, for example `Equals`, `Does Not Equal`,
`Starts With`, `Contains`, `Less Than Or Equal To`, and `Is Blank` . The available

operators depend on the data types associated with that resource. Data types include text, number,
Boolean, or picklist.

`Value` Options:

**•** Select a value that’s appropriate for the recommendation resource and the operator. For example,
if you enter `$Record.Status` as the resource and `Does Not Equal` as the operator,
available values are `On Hold`, `Escalated`, `Closed`, and `New` .

**•** Manually enter a literal value.

`Resource` and `Value` in the same row must have compatible data types.

When you add or subtract a number from a date value, the date adjusts in days, not hours.

**Option** **Behavior for Decision Outcomes**

`All Conditions Are Met` If one of the conditions is false, the recommendation evaluates the next outcome’s
conditions.

`Any Condition Is Met` If one of the conditions is true, the recommendation immediately takes this outcome’s
path.


Automate Your Business Processes with Salesforce Flow Building a Strategy

For example, say you create the custom field `Has_Mobile_Service__c` on the contact record. If you use
`$Record.Contact.Has_Mobile_Service__c = false` in a Strategy Builder expression, and you’re working with a case
record, the recordID provided with the request replaces `$Record` when the expression resolves. The recordID replaces `$Record`
because case records have a lookup relationship with contacts.

**•** Reference the context object in your formula using the _`$Record`_ function.

For example, _`ISPICKVAL($Record.Account.Tier__c, 'Premium')`_

Note: The Context object is the object where you plan to surface your recommendations. Choose the Context object, or change
it, by editing your strategy and choosing an object under **Object Where Recommendations Display** .

**•** Reference fields from the Recommendation object using the plain text label name. This option is available only in Filter and Load
elements, not Branch Selector elements.

For example, `AcceptanceLabel = =‘Yes, please’`


Automate Your Business Processes with Salesforce Flow Building a Strategy

**•** Access fields returned from external connections using
_`$nameOfExternalConnection.dataFromExternalConnection`_ syntax. Manage your external connections through
the **Manage** tab in the Toolbox.

For example, `$GetCreditScoreContext.output >= 760`

**•** Use _`$Request`_ to access information the user types into forms and use that information to request specific recommendations.
This option is available only on the Search and Contact Support pages in Experience Builder sites.

For example, `CONTAINS($Request.search, 'paperless billing') || CONTAINS($Request.search,`

```
   'order checks') || CONTAINS($Request.search, 'new address')

```

For multi-select picklist fields, enter values like `Includes ($Record.CarType__c, ‘Audi,’‘BMW’)`

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Create a Strategy Builder Action Strategy Connection

Use Apex actions to integrate external data sources and information from your Salesforce org into
your strategies.

Use Apex invocable actions to pull sources of data into your strategy.

**1.** In Strategy Builder, click the **Manager** tab.

**2.** Click **New Connection** .

**3.** Enter a label to visually identify the connection (1).

**4.** Enter an API name. This name is used in Strategy Builder elements that require conditional
statements, such as Branch Selector and Filter (2).

**5.** Enter a brief description for the connection (3).

**6.** Choose the action to use in logic elements’ conditions (4).

**7.** Enter any parameters for the selected action (5) and click **Done** .


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

**8.** Click the connection label to edit its associated information.

**9.** Click the **>** to the right of the connection label to edit or view its details or to delete it.

**Element** **Description**

**Apex Action** Assigns the invocable action that runs when the connection is referenced in elements’ conditions.

**API Name** Specifies the connection name to use in logic elements’ conditions. For example,
`$GetCreditScoreContext.output >= 760` .

Note: **API Name** is set to **Label** with underscores replacing spaces by default.

**Argument** Specifies one or more parameters that the selected invocable action requires. This textbox appears
only when the action has one or more arguments.

**Description** Specifies the description shown in the connection details.

**Label** Specifies the label displayed in the **Manager** pane for your connection.

SEE ALSO:

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_nba_resources.htm)_ Next Best Action Resources

Strategy Builder Strategies

_[Actions Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro_overview.htm)_ Overview


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Create a Custom Notification Flow for Next Best Action

Create a trigger in Process Builder to receive direct notifications about errors occurring in your
strategies. Launch a flow to send error information to your desired targets.

A custom notification flow allows you to choose how you want to be informed when errors happen
during Next Best Action strategy executions. It consists of two parts. First, a process created in
Process Builder that subscribes to the Platform Status Alert Event, which is generated when the
error occurs. Second, a notification flow that passes the information to your intended destination.
Add input variables to your flow to receive the expected variables.

**1.** In Flow Builder, create a flow. You can direct your notifications to different places, including
[Chatter posts, SMS text messages, and emails. Make sure to define input variables for payload](https://appexchange.salesforce.com/servlet/servlet.FileDownload?file=00P3A00000gAwX0UAK)
event fields that you want to use in your notifications. Input variables are flow variable resources,
type text, with **Available for Inputs** checked.

Note: A simple way to create your notification is to create a flow with the Send Email
core action. From there, manually add the email address where you want the notification
sent.

**2.** In Process Builder, create a process and for **The process starts when** select **A platform event**
**occurs** .

**3.** Add a trigger. Under **Platform Event** select **Platform Status Alert Event** .

**4.** Select an object that allows you to define matching conditions that produce a single result.

Note: For example, you could choose the User object and set **User ID** equal to the
**Created By** ID in the event payload.

**5.** Add other criteria.

**6.** Add an immediate action and select **Flows** .

**7.** Name your action and select the flow you created in step one.

**8.** Add mappings to connect data from the payload of your event to flow inputs.

**9.** Save and activate your process.

SEE ALSO:

Automate Tasks with Flows

[Configure the Process Trigger](https://help.salesforce.com/articleView?id=process_start.htm&language=en_US)

_[Object Reference Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_platformstatusalertevent.htm)_ : PlatformStatusAlertEvent


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

To open, edit, or create a
flow in Flow Builder:

**•** Manage Flow

To create, edit, or view
processes in Process
Builder:

**•** Manage Flow

AND

View All Data

Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Create, Package, and Distribute a Strategy Builder Template

Enterprise developers can create and package strategy templates from Developer Edition orgs for
use in multiple Salesforce orgs. Independent software vendors can also publish templates on
AppExchange for distribution to their subscribers. Strategies not marked as templates in managed
packages have intellectual property (IP) protection and can’t be edited or cloned. IP protection
safeguards proprietary information in your strategies.

You distribute changes to strategy templates via a managed package. Subscribers who install a
strategy template can open it in Strategy Builder and clone it to customize it for their own use.
When you publish updates to strategy templates via a package upgrade, template updates don’t
affect subscribers’ copies.

**1.** In Strategy Builder, create the strategy that you want to make into a template.

**2.** Open the strategy’s properties and select **Template** .

**3.** If you must, create your managed package.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create a strategy:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To create a managed
package:

**•** Create AppExchange
Packages

**4.** Distribute the strategy template in the managed package and let your subscribers know it’s available.

Example: Suppose you build and package strategies for insurance companies. Because insurance laws and regulations can vary
by location, your subscribers want the ability to modify your strategies when needed. They can do this using strategy templates
you create.

SEE ALSO:

Create a Strategy with Strategy Builder

_[First-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)_

[Create a First-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Manage Strategy Builder Action Strategies

Test, troubleshoot, and create strategies using Strategy Builder management tools.

###### Save Strategy Builder Action Strategies

Save your strategies or use Save As to create new a new strategy based on an existing one.

Test Strategy Builder Action Strategies
Test your strategy within Strategy Builder to see what recommendations display, given different
inputs.

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: Salesforce
Classic

Troubleshoot Strategy Builder Action Strategies
Strategies can be complex, which means it’s sometimes difficult to know where you went
wrong when you encounter unexpected results. Use this page to determine the best tool for troubleshooting your strategy.

Inspect Strategy Builder Element Results
View the full details of each step of your strategy’s execution from Strategy Builder’s **Inspector** tab. Trace the path of recommendations
through your strategy and identify problems in individual elements. Debug errors and see how your strategy is working behind the
scenes.

###### Save Strategy Builder Action Strategies

Save your strategies or use Save As to create new a new strategy based on an existing one.

###### Save your new or updated action strategy by clicking Save . Create a strategy based on an existing

one using **Save As** .

###### 1. To save your action strategy click Save .

**2.** To create an action strategy based on an existing one, click **Save As** .

**3.** Replace the existing name in **Name** .

**4.** Replace the existing API name in **API Strategy** .

You can have duplicate strategy names but we don’t recommend it. The API name must be
unique.

To automatically generate a new API name, delete the existing API name after you rename the
strategy. Click the **Name** textbox, and either tab over to or click the **API Name** textbox.

**5.** Optionally, replace the existing description.

**6.** If you want to base your strategy on a different object, click the **Object Where**
**Recommendations Display** textbox and choose a new object.

**7.** Click **Done** .

SEE ALSO:

Strategy Builder Strategies

Suggest Options to Users with Recommendation Strategies


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Test Strategy Builder Action Strategies

Test your strategy within Strategy Builder to see what recommendations display, given different
inputs.

In Strategy Builder, you can test the strategies underlying your recommendations.

**1.** Create or edit a strategy.

**2.** To save your changes, click **Save** .

Note: Always save before testing to test the most recent version of your strategy.

###### 3. Click Test .

**4.** Select an object for the test.

If you don’t see the object that you want to test the strategy against, close the Test Strategy
window. Select the properties wheel above the left pane. Change the object that the strategy
is linked to by selecting an object from **Object Where Recommendations Display** . If you
don’t see an object listed, the strategy hasn’t been linked to a specific object.

**5.** To test the underlying flow, choose a recommendation.

EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Note: Images associated with recommendations aren’t displayed when testing in Strategy Builder.

The Test Strategy window doesn’t show all possible error messages. Strategies are executed from right to left, starting at Output. If
a particular Branch Selector expression results in a closed branch, the child elements of that branch (the elements to the left) are
not executed. This process makes strategy evaluation faster, but it also means that any branches with false expressions could have
errors that aren’t exposed. The Test button shows what the user sees. To get a complete view of any errors occurring at run-time,
use the Inspector tab in the Toolbox. Inspector highlights errors from all elements.

SEE ALSO:

Inspect Strategy Builder Element Results

Strategy Builder Strategies


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Troubleshoot Strategy Builder Action Strategies

Strategies can be complex, which means it’s sometimes difficult to know where you went wrong
when you encounter unexpected results. Use this page to determine the best tool for troubleshooting
your strategy.

If something goes wrong with your strategy, you have several troubleshooting options.

**•** Start by using the basic test function in Strategy Builder. After you create and save a strategy,
click **Test** in the menu bar.

**•** For a more detailed view of your strategy execution, see the **Inspector** tab in the Strategy
Builder Toolbox. The Inspector tab lists specific errors and gives you a detailed view of how your
strategy executes.

**•** If you can’t find the problem in the **Inspector** tab, or you want to troubleshoot for a specific
[user, try using the Apex debug log. Next Best Action has a specific debug log category.](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_debugging_system_log_console.htm)

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** To receive full error reports sent directly to your email, a Chatter post, a text message, or other outlet, try creating a custom notification
[flow and a Process Builder trigger. Using a Platform Status Alert Event, you can subscribe to Next Best Action events and respond](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_platformstatusalertevent.htm)
when errors occur.

SEE ALSO:

###### Inspect Strategy Builder Element Results Inspect Strategy Builder Element Results

View the full details of each step of your strategy’s execution from Strategy Builder’s **Inspector** tab.
Trace the path of recommendations through your strategy and identify problems in individual
elements. Debug errors and see how your strategy is working behind the scenes.

When testing your strategy doesn’t return the recommendations you expect, investigate the
execution details of the strategy or a selected element using the **Inspector** tab.

**1.** Click the **Inspector** tab.

**2.** Click **Test** and select an object.

Note: Provide a sample _`recordId`_ to test your strategy in the inspector. You can do
so in either of the following ways:

**•** While Inspector is open, click **Test** and select a record. The _`recordId`_ of the selected
record is pasted into the **Record ID** field of the inspector. Close the Test window and
click **Run** in the inspector.

**•** Copy a record ID from the URL of a record page and paste it into the RecordId field
manually.

**3.** Click **Run** .


EDITIONS

Available in: Salesforce
Classic

**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

USER PERMISSIONS

To create or manage action
strategies:

**•** Modify All Data

OR

Manage Next Best
Action Strategies

To run an action strategy:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

Automate Your Business Processes with Salesforce Flow Building a Strategy

Note: Inspector can show a single element’s results, or the results for all elements in the strategy. If you select an element,
you see recommendations surfaced by that element. If you have no elements selected, you see recommendations surfaced
by the strategy.

Note: To see accurate results, you have to save your strategy before testing it. If you change the strategy or an element, **Run**
becomes **Save and Run** .

**4.** To scroll right, use the horizontal scroll bar at the bottom of the Inspector pane.

**5.** If you want to view recommendations for a different object, click **Test**, clear your current selection, and choose a new object from
the dropdown. To update the recommendations in the inspector, click **Run** .

SEE ALSO:

Test Strategy Builder Action Strategies

Strategy Builder Strategies


Automate Your Business Processes with Salesforce Flow Building a Strategy

##### Strategy Builder Elements

Use this page to quickly access a list of Strategy Builder elements and learn how they work together
to create unique strategies.

Use elements to create your strategies by opening Strategy Builder and selecting Elements in the
Toolbox. Drag elements onto the canvas to get started.

Strategy Builder Enhance Element
Get AI-driven predictions from services such as Einstein Discovery and Einstein Prediction Builder
to enhance Next Best Action recommendations with additional information, such as propensity
scores. The Enhance element allows you to modify a set of recommendations on the fly, every
time a strategy is executed. These recommendations can be static and live as records in
Salesforce, or dynamic and sourced from external data sources or other Salesforce objects.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Strategy Builder Generate Element
With the Generate element, you can dynamically generate personalized recommendations where a large number of possibilities
makes it inconvenient to create recommendations manually. The Generate element allows you to create in-memory, on-the-fly
recommendations, either from an external data source or from other Salesforce objects.

Strategy Builder Load Element
Load is the first element in a strategy branch. Load and filter the records of a Recommendation object. Or load and filter the records
of any object, and convert them into recommendations at the end of the strategy using the Map element. Your load elements
determine which of your recommendations are evaluated when your strategy executes.

Strategy Builder Filter Element
Create an expression that allows you to block or filter out undesirable recommendations, depending on the context. The expression
is evaluated for every recommendation that passes through the branch.

Strategy Builder Limit Reoffers Element
Determine how often a user sees the same recommendation. You can decide how many times the user must react to a
recommendation and how many days to wait before displaying the recommendation again.

Strategy Builder Map Element
The Map element lets you use formulas to create Recommendation fields and modify existing fields without Apex code. Instead, it
relies on expressions and formulas. Use the Map element to pass data from a Recommendation field with one name to a Flow input
with a different name. Or use it to modify current values for Description, Name, and other fields and personalize them with
context-specific data.

Strategy Builder Sort Element
Choose how recommendations are ordered within a branch and reorder them using Recommendation fields.

Strategy Builder Branch Merge Element
Combine recommendations from multiple branches into a single branch.

Strategy Builder Branch Selector Element
Filter multiple branches through a branch selector and create unique expressions for each branch. If the expression is true,
recommendations in the branch are allowed through and combined into a single branch.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Strategy Builder First Non-Empty Branch Element
The first non-empty branch element allows you to filter branches in the order they appear on the canvas. The first branch that
contains recommendations is allowed through, all other branches are blocked.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

###### Strategy Builder Enhance Element

Get AI-driven predictions from services such as Einstein Discovery and Einstein Prediction Builder
to enhance Next Best Action recommendations with additional information, such as propensity
scores. The Enhance element allows you to modify a set of recommendations on the fly, every time
a strategy is executed. These recommendations can be static and live as records in Salesforce, or
dynamic and sourced from external data sources or other Salesforce objects.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

```
Apex

Action

```

Search or select an Apex action, which calls an Apex class. An Apex class must
have a method marked as an invocable method to appear as an Apex action in
declarative tools like Strategy Builder.

`Argument` Specify one or more parameters for the selected Apex action.

Example: Assume that your company integrates separate data sources from the manufacturers of products your business sells.
Those data sources include information about the current availability of each item (in stock, back ordered, or unavailable). You can
connect an Enhance element to your strategy’s Load or Generate element to provide that information to users in the
recommendation.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: You can use the Enhance element to calculate a discount percentage for your customers based on how long your
company has managed their account. Or you can use it to A/B test two branches of recommendations.

Example: Suppose you use Next Best Action to provide upsell recommendations. You want to add a 5% discount to your product
recommendations for those customers who have been with your company for more than one year. Customers of more than two
years get a 10% discount, customers of more than five years get a 20% discount, and so on. Use the Enhance element to call an
Apex action that performs a SOQL query. The query retrieves the Account age and appends it to the description of all incoming
recommendations.

The strategy used with an Enhance element can be as simple as Load -> Enhance -> Output. All recommendations the Load
element retrieves or loads are passed as a list of recommendations to the underlying invocable method.

When configuring the Enhance element, select **Enhance with Discounts Based on Age** as the Apex action and specify **$Record.id**
as the input parameter.


Automate Your Business Processes with Salesforce Flow Building a Strategy

The Enhance element in turn calls the `getDiscounts` invocable method in the `Enhance_GetAccountDiscount` class.
Notice how the description of each recommendation has a discount value appended to it `(r.Description + ‘ with`
`a 5% discount’)` .

```
      global class Enhance_GetAccountDiscount {

        @InvocableMethod(label='Enhance with Discounts Based on Age' description='Returns

      an enhanced set of recommendations with appropriate discounts')

        global static List<List<Recommendation>> getDiscounts(List<DataContainer> inputData){

           List<Recommendation> recommendations = inputData[0].recommendations;

           List<List<Recommendation>> outputs = new List<List<Recommendation>>();

           Account[] accounts = [SELECT Name, Description,CreatedDate, id FROM Account

      WHERE id = :inputData[0].accountId];

            Double ageAccountMonths =

      accounts[0].CreatedDate.date().monthsBetween(date.today());

           Double ageAccount = ageAccountMonths/12;

           List<Recommendation> returnedRecommendations = new List<Recommendation>();

           for (Recommendation r:recommendations){

             if(ageAccount > 1){

               r.Description = r.Description + ' with a 5% discount' ;

             }

             else if (ageAccount > 2){

               r.Description = r.Description + ' with a 10% discount ';

             }

             else if (ageAccount > 5){

               r.Description = r.Description + ' with a 20% discount ';

             }

             returnedRecommendations.add(r);

           }

           outputs.add(returnedRecommendations);

           return outputs;

```


Automate Your Business Processes with Salesforce Flow Building a Strategy

```
        }

      }

```

Usage

The Enhance element requires an Apex action marked as an invocable method.

```
   @InvocableMethod(

   label='Enhance with Discounts Based on Age'

   description='Returns an enhanced set of recommendations with appropriate discounts')

```

Use the Enhance element in combination with the Strategy Builder Load or Generate element.

The Enhance element can pass any number of inputs to the Apex action. The input parameter must be a list or a list of lists of a user-defined
Apex object (for example, a custom class called `DataContainer` ). The user-defined Apex object must include a
`List<Recommendation>` variable. The `List<Recommendation>` variable is automatically defined with the recommendations
that pass into the Enhance element.

```
   global class DataContainer {

      @InvocableVariable

      public string accountId;

      @InvocableVariable

      public List<Recommendation> recommendations;

   }

   ________

   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

The Enhance element returns a list of recommendations, `List<List<Recommendation>>` . These recommendation enhancements
exist only in memory and don’t persist after the strategy is executed.

```
   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

SEE ALSO:

###### Strategy Builder Generate Element

Strategy Builder Load Element

Flow Element: Apex Action

###### Strategy Builder Generate Element

With the Generate element, you can dynamically generate personalized recommendations where
a large number of possibilities makes it inconvenient to create recommendations manually. The
Generate element allows you to create in-memory, on-the-fly recommendations, either from an
external data source or from other Salesforce objects.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

**Field** **Description**

`Description` Optional description of the element and how it works within the strategy.

`Apex Action` Search or select an Apex action, which calls an Apex class. An Apex class must have a method marked as an
invocable method in order to appear as an Apex action in declarative tools like Strategy Builder.

`Argument` Specify one or more parameters for the selected Apex action.

Example: Assume that your company has a large catalog of products and you use a screen flow to recommend accessories to
your customers based on their past product purchases. Instead of creating a single, static recommendation for each individual
accessory, you can maintain that information in the Account or Product object in Salesforce. Or you can store information in external
data sources like Commerce Cloud or a SQL database. Use a Generate element with an Apex invocable action to call the Apex class
and generate accessory recommendations dynamically for your strategy.

Example: Suppose you want to show a service agent a list of key accounts to follow up with after a set number of days has passed
since the previous contact. With the Generate element, you can call an Apex action that makes a SOQL query for Account where
the Owner is the logged-in user (the agent). This query identifies the accounts who were last contacted more than, say, 90 days
ago. Next Best Action returns the relevant accounts in the form of recommendations. The strategy can be as simple as the Generate
element with an Output element.

When you configure the Generate element, select **Accounts to Follow Up Today** as the Apex action and specify **$User.id** as an
input parameter.


Automate Your Business Processes with Salesforce Flow Building a Strategy

The Generate element calls the `getAccounts` invocable method in the `Generate_GetAccountsToFollowUp` Apex
class. This method retrieves the relevant accounts and creates a list of recommendations. The recommendation description includes
the name of the account ( `account.Name` ) and the number of days since the last contact ( `daysSinceLastContact` ).

```
      global class Generate_GetAccountsToFollowUp {

        @InvocableMethod(label='Accounts to Follow Up Today'

                  description='Recommend accounts the current user should follow

      up on today')

        global static List<List<Recommendation>> getAccounts(List<String> inputData){

           List<List<Recommendation>> outputs = new List<List<Recommendation>>();

           Integer daysSinceLastContact;

           Account[] accounts = [SELECT Name, Description, LastContactDate__c, OwnerId

      FROM Account WHERE OwnerId = :inputData[0]];

           List<Recommendation> recs = new List<Recommendation>();

           for (Account account:accounts) {

             if (account.LastContactDate__c != null){

               daysSinceLastContact =

      account.LastContactDate__c.daysBetween(date.today());

               if (daysSinceLastContact > 90){

                  Recommendation rec = new Recommendation(

                    Name = account.Name,

                    Description = 'Connect with the ' + account.Name + ' account,

      the last interaction was '+ daysSinceLastContact + ' days ago.',

                    //Pre-req: Create a screen flow with the name simpleFlow

                    ActionReference = 'simpleFlow',

                    AcceptanceLabel = 'View'

                  );

                  recs.add(rec);

               }

             }

           }

           outputs.add(recs);

           return outputs;

        }

      }

```

When you execute the strategy, the resulting recommendation includes the name of the account and the number of days since
the last contact with them.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Usage

The Generate element requires an Apex action marked as an invocable method.

```
   @InvocableMethod(

   label='Related Wikipedia Pages'

   description='Recommend wikipages that are related to the named input wikipage')

```

The Generate element can pass any number of inputs to the Apex action, either as lists or a list of lists of primitives, sObjects, and
user-defined Apex objects. To provide more than one input, the input parameter must be a list or a list of lists of a user-defined Apex
object (for example, a custom class called `DataContainer` ).

```
   List<String> relatedTo

```

OR

```
   global class DataContainer {

   @InvocableVariable

   public string accountId;

   }

   ____

   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

The Generate element returns a list of recommendations. Invocable methods support returning either a list of an sObject type or a list
of lists of an sObject type. Since the Enhance element operates not on a single recommendation but on a list of recommendations, the
method must return a `List<List<Recommendation>>` .

```
   global static List<List<Recommendation>> invocableMethod(List<DataContainer> inputData)

```

SEE ALSO:

Strategy Builder Enhance Element

Flow Element: Apex Action

###### Strategy Builder Load Element

Load is the first element in a strategy branch. Load and filter the records of a Recommendation
object. Or load and filter the records of any object, and convert them into recommendations at the
end of the strategy using the Map element. Your load elements determine which of your
recommendations are evaluated when your strategy executes.

Load recommendations from the records of any standard or custom object. You can use objects
such as Recommendation, Account, Product, and Opportunity when you build a strategy. Choose
criteria for when to load a recommendation. Filter out certain records from a strategy. Sort your
records by selecting an object value.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

A strategy treats another object the same as it does a Recommendation object until the end, when
it converts it into a recommendation. If you choose an object other than Recommendation, add a
Map element after the Load element. Use the Map element to map fields from the object’s records to required fields on the
Recommendation object.

In Strategy Builder, you can load up to 1,000 records in a strategy. A Strategy Builder strategy has a limit of 100 Load elements on the
canvas. To load more than 1,000 records, create your recommendation strategy in Flow Builder, which has a load limit of 50,000 records.


Automate Your Business Processes with Salesforce Flow Building a Strategy

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Object` The object whose records are loaded, filtered, and converted into recommendations.

```
Condition

Requirements

```

Determines the logic to evaluate conditions. To load the recommendation if it meets all the specified criteria,
select **All Conditions are Met** . To load the recommendation if it meets any listed criteria, select **Any Condition**
**is Met** .

`Field` Choose a field from the Recommendation object to evaluate whether the recommendation is loaded into the
strategy.

`Operator` Choose an operator.

`Value` Enter a value for your chosen field. Values can be simple numbers, string phrases, or formulas that use Salesforce
formula support. Don’t enclose string or number values with quotes. Picklists aren’t supported.

`Add Condition` Creates an extra set of conditions.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

Strategy Builder Enhance Element

###### Strategy Builder Filter Element

Create an expression that allows you to block or filter out undesirable recommendations, depending
on the context. The expression is evaluated for every recommendation that passes through the
branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Filter` Create an expression that is evaluated for each recommendation that you load
`Expression` into your strategy. If the expression is true, the recommendation is allowed
through. If false, the recommendation doesn’t progress further through the
strategy. Filter Expression accepts Standard Salesforce formulas. For more
[information, see Formula Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)


EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Building a Strategy

Note: Use _`$Record`_ to reference fields from the context object. The context object is the object where you intend to surface
your recommendations and can be changed by editing your strategy and choosing an object under **Object Where**
**Recommendations Display** . Use plain text field labels to reference Recommendation object fields. Examples: _`$Record.status`_
!= _`'New'`_, _`RejectionLabel`_ == _`‘No, thanks.’`_ For more information, see Write a Strategy Builder Expression.

Example: Suppose that you want to surface recommendations on the Case object so your service agents can suggest offers to
your customers. If you want to suggest only credit card offers, create a _`Category`_ field for the Recommendation object. Add a
Credit Card Offer category to your field. Add a filter element and use the formula _`Category_c`_ = _`‘CreditCardOffer’`_
in **Filter Expression** .

Usage

Filter is the best way to remove certain recommendations from a strategy branch. Add the element to a branch and create an expression
to evaluate every recommendation that passes through the branch.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Strategy Builder Limit Reoffers Element

Determine how often a user sees the same recommendation. You can decide how many times the
user must react to a recommendation and how many days to wait before displaying the
recommendation again.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To view a recommendation
strategy with a Limit Reoffers
element on a Lightning
record page:

**•** Run Flows

```
User

Reaction

```

Choose a user reaction to base your limits on. For example, if you select **User**
**Rejects the Recommendation**, your element only limits repeat offers after
the recommendation is rejected.

`Number of` Choose how many times you want the user to react before the recommendation
`Reactions` is limited.

```
Time

Period in

Days

```

Choose how many days the system waits after the user has reacted the specified
number of times before a repeat offer is shown to the same user.

Time Period in Days is based on days, not hours. If the time period is set to 1,
and the user accepts the recommendation at any time on Monday, the offer

doesn’t display again until the start of Wednesday. So a one-day time period
could be as few as 25 hours in duration or as many as 48 hours.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: Let’s say you have a renewal offer that you want to surface at most one time per year. If a user has already accepted
the offer and filled out the renewal, you don’t want to show the same offer again. For this example, for User Reaction, select **User**
**Accepts the Recommendation** . For Number of Reactions, select **1**, and set the time period for 365 days for an annual renewal.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

###### Strategy Builder Map Element

The Map element lets you use formulas to create Recommendation fields and modify existing fields
without Apex code. Instead, it relies on expressions and formulas. Use the Map element to pass
data from a Recommendation field with one name to a Flow input with a different name. Or use it
to modify current values for Description, Name, and other fields and personalize them with
context-specific data.

If you load an object other than Recommendation, add a Map element after the Load element and
before the Output element in your strategy. Use the Map element to map fields from the records
to required fields on the Recommendation object. For example, map the product Title field to the
recommendation Name field. Mapping fields converts the filtered records into recommendations
that are surfaced via the Next Best Action component and your own apps.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: You can include the name of a contact in a recommendation, and further personalize the recommendation with text.
Suppose that you have a recommendation with the description, “Thank you for being a loyal customer. We truly appreciate your
business!” Using the Map element, you can personalize the description. Add the name of the contact to the description, for example,
“Lauren Boyle, Thank you for being a loyal customer. We truly appreciate your business!”

**•** Use a Load element to load all the recommendations you want to change. Or you can add a Generate element and pass in
dynamically generated recommendations.

**•** Add a Map element. In the Name field, select **Description** and in the Value field, enter this expression:

`$Record.Contact.Name+ “, ” + Description` . Leave the Type field as `Text` .


Automate Your Business Processes with Salesforce Flow Building a Strategy

**•** Place the “Personalized Thank You” Map element after the Load element. It modifies the descriptions of all recommendations
that pass through it.

**•** When you execute the strategy, your recommendations include the contact name for the current case.

###### Strategy Builder Sort Element

Choose how recommendations are ordered within a branch and reorder them using
Recommendation fields.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Recommendation` Choose a field from the Recommendation object to sort on.

```
Field

```

`Sort` Choose whether you want to sort your recommendations in an ascending or
`Direction` descending order.

`Sort Empty` Recommendations that don’t contain information in the field you chose in
`Values to` Recommendation Field are sorted to the top when selected.

```
Top

```

`Maximum` Limits the number of recommendations allowed to pass through the element.

```
Recommendations

```

Usage

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Sort the order of your recommendations in a branch by choosing a value from the Recommendation object to sort on. Choose whether
you want to sort in an ascending or descending order, and decide how many recommendations to allow through.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations


Automate Your Business Processes with Salesforce Flow Building a Strategy

###### Strategy Builder Branch Merge Element

Combine recommendations from multiple branches into a single branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Maximum` Determines the maximum number of recommendations allowed through the
`Recommendations` branch where the sort element is placed.

Usage

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Merge multiple branches into a single branch and limit the number of recommendations allowed through the branch with the branch
merge element.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

###### Strategy Builder Branch Selector Element

Filter multiple branches through a branch selector and create unique expressions for each branch.
If the expression is true, recommendations in the branch are allowed through and combined into
a single branch.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

`Condition` Create an expression for each branch that flows through the element. If the
expression is true, the recommendations in the branch are allowed through. If

false, the recommendations in the branch don’t progress any further through
the strategy. Condition accepts standard Salesforce formula functions. For more
[information, see Formula Operators and Functions by Context.](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Note: Use _`$Record`_ to reference fields from the context object. The context object is the object where you intend to surface
your recommendations and can be changed by editing your strategy and choosing an object under **Object Where**
**Recommendations Display** . Example: _`ISPICKVAL($Record.status, 'New')`_ . For more information, see Write a
Strategy Builder Expression.


Automate Your Business Processes with Salesforce Flow Building a Strategy

Example: Suppose that you want to surface recommendations on the Case object so your service agents can suggest offers to
your customers. If a case has been escalated, you want to offer a special discount. To do so you, create a load element that loads
the recommendations associated with your offer. Create a branch selector that only allows recommendations from the branch if
the case has an escalated status. Make your offer load element a child of the branch selector element. In **Condition** on the branch
selector element, use the following formula: _`ISPICKVAL($Record.status, 'Escalated')`_ .

Usage

Branch selector is an important element when you want to weed out entire branches at once. Unlike a filter element, it can’t filter based
on individual recommendations.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Strategy Builder First Non-Empty Branch Element

The first non-empty branch element allows you to filter branches in the order they appear on the
canvas. The first branch that contains recommendations is allowed through, all other branches are
blocked.

**Field** **Description**

`Label` The name of the element as it appears on the canvas.

`API Name` The API name of the element. The API name must be unique.

`Description` Optional description of the element and how it works within the strategy.

EDITIONS

Available in: Salesforce
Classic

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: Let’s say you have five different types of credit card offers that could be surfaced to a single user. Although each offer
type is unique and must have its own branch, you only want to surface one type. To do so, filter all of your branches that contain
credit card offers through a first non-empty branch, in priority order from top to bottom. Your element only allows the first branch
that contains recommendations.

Usage

Branches are filtered through the first non-empty branch element in the order that they appear on the canvas, moving from top to
bottom. The element evaluates each branch until it finds one that contains recommendations. When the element recognizes that a
branch contains recommendations, it allows those recommendations through and blocks recommendations from all other branches.

SEE ALSO:

Suggest Options to Users with Recommendation Strategies

Create Recommendations

Display Recommendations


### Automate Your Business Processes with Salesforce Flow Display Recommendations Display Recommendations

After creating a strategy, choose a page to run your strategy and display your recommendations.
You can use a Lightning record page, an app’s home page, an Experience Cloud site page, a
Visualforce page, or an external site, depending on where you want recommendations to appear.

Lightning Page (Lightning App Builder)

**•** On a Lightning page in Lightning App Builder, create, edit, or clone a record page.

**•** Drag Einstein Next Best Action from the component list to the location on the page where you
want to display it.

**•** Choose an action strategy and the number of recommendations that you want the component
to display.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you want to show users flows and quick actions in addition to recommendations, use the Actions & Recommendations component
on your Lightning record page. You can create an Actions & Recommendations deployment that specifies action strategies and how
you want your recommendations to appear.

App Home Page

**•** Create a strategy for the Next Best Action component. Use global variables such as $User.Id when you create the strategy. Use global
variables because the home page isn’t a record page and isn’t associated with objects, like Case, Account, or Product.

**•** Navigate to your org’s Home page.

**•** Click, and select Edit Page.

**•** From the list of Lightning components on the left (1), drag the Einstein Next Best Action component to the home page (2).

Experience Builder Site Page (Experience Builder)

**•** In Experience Builder, create or edit a site page.

**•** Drag Suggested Actions from the component list to the location on the page where you want to display it.

Visualforce Page: Use Lightning Out to add the lightning:nextBestAction component.

Custom Apps: Add Einstein Next Best Action functionality into your app with the global lightning:nextBestAction component.


Automate Your Business Processes with Salesforce Flow Display Recommendations

#### Einstein Next Best Action Component

Einstein Next Best Action uses strategies that apply your org’s business rules to display context-sensitive suggested offers and actions
on your Lightning record pages.

SEE ALSO:

[Suggested Actions](https://help.salesforce.com/s/articleView?id=sf.rss_suggested_actions_component.htm&language=en_US)

[Flow Builder for Service and the Actions & Recommendations Component](https://help.salesforce.com/s/articleView?id=sf.console_lex_guided_action_list_component.htm&language=en_US)

_Lightning Aura Components Developer Guide:_ [Add Aura Components to Any App with Lightning Out (Beta)](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/lightning_out.htm)

Einstein Next Best Actions Considerations

#### Einstein Next Best Action Component

Einstein Next Best Action uses strategies that apply your org’s business rules to display
context-sensitive suggested offers and actions on your Lightning record pages.

**1.** Create a recommendation strategy in Strategy Builder.

**2.** Drag the Einstein Next Best Action component onto your record page.

Note: In Experience Builder, the component is called Suggested Actions.

**3.** In the property editor, select the strategy you want to display (1). Enter the maximum number
of recommendations to display (2) and choose where recommendations open when accepted
(3).


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create and save Lightning
pages in the Lightning App
Builder:

**•** Customize Application

To run a recommendation
strategy on a Lightning
record page:

**•** Run Flows

OR

Flow User field enabled
on the user detail page

OR

For Experience Cloud,
the FlowSites perm
provides org-wide
access. To restrict access
to users by profile or
permission set, add a
component visibility filter
to the Suggested Actions
component.

Automate Your Business Processes with Salesforce Flow Display Recommendations

**Component** **Description**

Title Displays the title for the component on the
Record page.

Hide Einstein Header Hides the Einstein Recommendations graphical
header.

Strategy Displays all available strategies created in Strategy
Builder.

Maximum Recommendations Displayed Displays up to four recommendations.

Hide Empty Component Displays the component only when there are
recommendations available initially.

Launch Recommended Action In Specifies whether recommendations open in a
display window or a new browser window.

Show Image

Shows images associated with each displayed
recommendation. If there isn’t an image, a
placeholder displays.

Show Description Displays the recommendation descriptions.

Show Reject Option Displays the reject option.

Set Component Visibility

[Allows Dynamic Lightning Pages by adding filter](https://help.salesforce.com/s/articleView?id=sf.lightning_page_components_visibility.htm&language=en_US)
conditions and logic to the component properties
in the Lightning App Builder.

Here’s how a strategy looks with the Einstein header and no images in the Service console:


### Automate Your Business Processes with Salesforce Flow Report On and Track a Recommendation Report On and Track a Recommendation

Create a custom report type to report on and track recommendation data and strategy metrics.
You can see the monthly total recommendations that a Salesforce org’s strategies served. And you
can analyze which recommendations are accepted and rejected, who responds to them, and more.

Salesforce updates recommendation strategy metrics each time a strategy is executed or a
recommendation is accepted or rejected. Analyze usage metrics to better understand how your
strategies are performing. Use this knowledge to improve your strategies’ logic and increase their
effectiveness.

For example, run A/B tests on two different strategies and compare their relative performance. If
your service agents accept more recommendations served from Strategy B, use metrics to discover
why.

**1.** For complete instructions on creating custom report types, search for Create a Custom Report
Type in Salesforce Help.

**2.** For strategy-level data that’s aggregated for each calendar month, use the Recommendation
Strategy Metrics primary object. For recommendation-level details, use the Recommendation
Reactions primary object instead.

**3.** Using the Recommendation Strategy Metrics primary object, combine fields from it (like
Recommendation Source ID) and the related strategy (like Context Record Type). Using the
Recommendation Reactions primary object, include fields to report on, such as Context Record
ID, Created Date, Last Modified Date, Recommendation Score, and Source ID.

To view recommendation
metrics data:

**•** Modify All Data or
Manage Next Best
Action Strategies

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create, edit and delete
custom report types:

**•** Manage Custom Report
Types

**4.** To analyze a strategy’s performance, group your strategy executions by recommendation source
ID, and the number of times a recommendation was served, accepted, and rejected. To compare
performance between two different strategies, group your strategy executions by recommendation source ID. Add useful metadata
to your report, such as recommendation description and create date.

**5.** Deploy the report types you want to make available to users.

**6.** Let users know that they can create reports using these custom report types.

**7.** Users can also create dashboards from the custom report type.


## Automate Your Business Processes with Salesforce Flow Automated Actions

SEE ALSO:

[Create a Custom Report Type](https://help.salesforce.com/s/articleView?id=sf.reports_defining_report_types.htm&language=en_US)

_[Connect REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_responses_n_b_a_reaction.htm)_ Recommendation Reaction

## Automated Actions

An automated action is a reusable component that performs some sort of action behind the
scenes—like updating a field or sending an email. After you create an automated action, add it to
a process, milestone, or other automated process.

EDITIONS

Available in: both Lightning
Experience and Salesforce
Classic

Flow triggers are available
in: Salesforce Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Outbound messages are
available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Email alerts are available in:
**Essentials**, **Professional**,
**Enterprise**, **Performance**,
**Unlimited**, and **Developer**
Editions

Considerations for Automated Actions
Before you start working with automated actions, familiarize yourself with relevant limits and
special behaviors.

[Manage Automated Actions in Workflow Rules](https://help.salesforce.com/apex/HTViewHelpDoc?id=managing_workflow_actions.htm&language=en_US#managing_workflow_actions)


### Automate Your Business Processes with Salesforce Flow Task Actions Task Actions

Task actions determine the details of an assignment given to a specified user by an automated
process. You can associate task actions with workflow rules, approval processes, or entitlement
processes.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

From Setup, enter _`Tasks`_ in the `Quick Find` box, and select **Tasks** . Then use these settings
to configure your task.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


### Automate Your Business Processes with Salesforce Flow Email Alert Actions

Notice that all your tasks include a **Created By** field. For tasks, this field contains the name of the person who saved the record that
triggered the rule to assign the task.

Tasks don't trigger task-based workflow rules if they’re created automatically, such as by clicking the **Send An Email** button or by using
the Email to Salesforce BCC address field.

SEE ALSO:

Associate Actions with Workflow Rules or Approval Processes

### Email Alert Actions

An email alert is an email generated by an automated process and sent to the designated recipients.
The action consists of the standard text and the list of recipients. You can use an email alert in an
automation, such as a flow, approval process, or entitlement process. Legacy workflow rules and
processes built in Process Builder or through the Invocable Actions REST API endpoint also use
email alerts.

From Setup, enter _`Email Alerts`_ in the Quick Find box, and select **Email Alerts** . Then use
these settings to configure your email alert.

Tip: Create a standardized letterhead to use for all email templates that you use for email
alert actions.


EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Email Alert Actions


Automate Your Business Processes with Salesforce Flow Email Alert Actions

The daily allocation for emails sent through email alerts is 1,000 per standard Salesforce license per org—except for free Developer
Edition and trial orgs, where the daily email allocation is 15. The overall org allocation is 2,000,000. This allocation applies to emails sent
through email alerts in automations or REST API. Single emails sent to external email addresses are also limited, and how those limits
are enforced depends on when your org was created.

SEE ALSO:

Recipient Types for Email Alerts

Daily Allocations for Email Alerts

Recipient Types for Email Alerts

When you configure an email alert, you identify who receives the email. The options available vary
based on your Salesforce settings and the object that you selected.

EDITIONS

Available in: both Salesforce
[Classic (not available in all](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
[orgs) and Lightning](https://help.salesforce.com/s/articleView?id=sf.overview_edition_lex_only.htm&language=en_US)
Experience

Available in: **Essentials**,
**Professional**, **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


### Automate Your Business Processes with Salesforce Flow Field Update Actions

The Recipient merge field isn’t supported in either Classic or Lightning email templates used for automations.

### Field Update Actions

Field update actions let you automatically update a field value. You can associate field updates with
workflow rules, approval processes, or entitlement processes.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

From Setup, enter _`Field Updates`_ in the `Update` box, and select **Field Updates** . Then use
these settings to configure your field update.

Before you begin, check the type of the field you want to update. Read-only fields like formula or
auto-number fields aren’t available for field updates.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Field Update Actions

SEE ALSO:

Associate Actions with Workflow Rules or Approval Processes

Cross-Object Field Updates

Considerations for Field Update Actions

#### Value Options for Field Update Actions

When you create a field update action, specify the new value of the field.

Available field update options depend on the type of field you’re updating.

**•** Choose **A specific value**, and enter the value in the space provided.

**•** Choose **A blank value (null)** if you want Salesforce to remove any existing value and leave
the field blank. This option isn't available for required fields, checkboxes, and some other types
of fields.

**•** For record owners, choose a user to assign to the record. For case, lead, and custom object
records, you can also choose a queue for this field. To send an email to the new record owner,
select `Notify Assignee` . (This option is unavailable when user control over task assignment
notifications is enabled.)

**•** For checkboxes, choose `True` to select the checkbox and `False` to deselect it.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

### Automate Your Business Processes with Salesforce Flow Outbound Message Actions

**•** For picklists, select a specific value from the dropdown list, or select the value above or below the current value based on the sorting
specified in the picklist definition. If you sort values alphabetically, the values above or below the current value can be different for
users in other languages.

**•** To calculate the value based on an expression, merge fields, or other values, select **Use a formula to set the new value** . For more
[information about using formulas in Salesforce, see Calculate Field Values with Formulas.](https://help.salesforce.com/s/articleView?id=sf.customize_formuladef.htm&language=en_US)

### Outbound Message Actions

An outbound message sends information to a designated endpoint, like an external service. You
configure outbound messages from Setup. You must configure the external endpoint and create
a listener for the messages using SOAP API. You can associate outbound messages with flows,
workflow rules, approval processes, or entitlement processes.

Note: Previously, outbound messages were available in Professional Edition with the purchase
of an add-on. The add-on is no longer available for Professional Edition.

For example, automatically initiate the reimbursement process for an approved expense report by
triggering an outbound API message to an external HR system.

### From Setup, in the Quick Find box, enter Outbound Messages, and then select Outbound

**Messages** . Then use these settings to configure your outbound message.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Outbound Message Actions

If your endpoint URL uses a client certificate, see Import a Client Certificate for Your Endpoint URL on page 821.

SEE ALSO:

Track the Delivery Status of an Outbound Message

Considerations for Outbound Messages

[SOAP API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/)

Associate Actions with Workflow Rules or Approval Processes

Considerations for Outbound Messages

#### Outbound Message Notifications

You can request that up to 5 users receive a notification listing all outbound messages that have
failed for at least 24 hours. A fresh notification is sent every 24 hours until you cancel the request.
Failed messages are deleted from the failed outbound messages related list after 7 days. Before
they’re removed, you can delete them yourself or request that they be retried again.

Note: Previously, outbound messages were available in Professional Edition with the purchase
of an add-on. The add-on is no longer available for Professional Edition. If outbound messages
are available in your Salesforce edition but you don’t see the Outbound Message Notifications
page, your org doesn’t have notifications for outbound messages enabled. Contact Salesforce
to enable notifications for outbound messages.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Create an Outbound Message Notification
You can request that up to five users receive a notification listing all outbound messages that have failed for at least 24 hours. A fresh
notification is sent every 24 hours until you cancel the request.

View an Outbound Message Notification Request
View or edit outbound message notification requests.


Automate Your Business Processes with Salesforce Flow Outbound Message Actions

##### Create an Outbound Message Notification

You can request that up to five users receive a notification listing all outbound messages that have
failed for at least 24 hours. A fresh notification is sent every 24 hours until you cancel the request.

Note: If you don’t see the Outbound Message Notifications page, your org doesn’t have
notifications for outbound messages enabled. Contact Salesforce to enable notifications for
outbound messages.

**1.** From Setup, enter _`Outbound Message Notifications`_ in the Quick Find box, then
select **Outbound Message Notifications** .

**2.** Click **New** .

**3.** Enter a full username, or click the icon to select it from a list of usernames.

**4.** Save the request.

##### View an Outbound Message Notification Request

View or edit outbound message notification requests.

From the detail page of an outbound message notification request:

**•** To change the username for a notification request, click **Edit** . It’s simpler than deleting the
request and then creating a one.

**•** To delete the notification request, click **Delete** .

**•** To create a notification request with the same username, click **Clone** .


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create an outbound
message notification:

**•** Modify All Data

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To view or edit outbound
message notification
request:

**•** Modify All Data

### Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

#### Track the Delivery Status of an Outbound Message

To track the status of an outbound message, from Setup, enter _`Outbound Messages`_ in the
`Quick Find` box, then select **Outbound Messages** .

**•** _Next items for delivery_ are awaiting delivery.

**•** _Oldest failures_ haven’t yet been deleted because they haven’t been delivered and aren’t 24
hours old.

**•** _Failed outbound messages_ failed to be delivered and are no longer being retried. Messages are
listed here only if you configure the message when you create it by selecting `Add failures`
`to failed outbound message related list` . If you don’t see this related list,
it hasn’t been enabled for your organization.

You can perform several tasks here.

**•** To view the action that triggered it, click any workflow or approval process action ID.

**•** To change the **Next Attempt** date to now, click **Retry** . This option causes the message delivery
to be immediately retried. If you select **Retry** in the **Failed outbound messages** related list,
the outbound message moves to the **Next items for delivery** related list and is retried for
another 24 hours.

**•** To permanently remove the outbound message from the queue, click **Del** .

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To track outbound
messages:

**•** Modify All Data

Note: If you don’t have this option, your org doesn’t have outbound messages enabled. Contact Salesforce to enable outbound
messages.

#### Import a Client Certificate for Your Endpoint URL

If the endpoint URL of your outbound message uses a client certificate, import it to put your
outbound message into action.

**1.** From Setup, enter _`API`_ in the `Quick Find` box, then select **API**

**2.** Click **Generate Client Certificate** .

**3.** Save the certificate to the appropriate location.

**4.** Import the downloaded certificate into your application server and configure your application
server to request the client certificate.

### Considerations for Automated Actions

Before you start working with automated actions, familiarize yourself with relevant limits and special
behaviors.

Considerations for Field Update Actions
Learn how to use field update actions to their full potential in workflow.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Considerations for Outbound Messages
Review the considerations for using outbound message actions before implementing them in your workflows.

SEE ALSO:

Daily Allocations for Email Alerts

#### Considerations for Field Update Actions

Learn how to use field update actions to their full potential in workflow.

[other]: Where possible, we changed noninclusive terms to align with our company value
of Equality. We maintained certain terms to avoid any effect on customer implementations.

When creating field updates for workflow rules or approval processes, consider the following:

Field Update Processing

**•** Field updates occur before email alerts, tasks, and outbound messages.

**•** Field updates occur after case assignment, lead assignment, and auto-response rules.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Field updates function independently of field-level security. Therefore, a workflow rule can update fields even though they’re hidden
on the user's page layout.

**•** The result of a field update is unpredictable when a single workflow rule includes multiple field updates that apply different values
to the same field.

**•** Field updates can affect the information in a related list. For example, if a field such as the `Amount` or `Close Date` of an
opportunity is set to be updated, it affects the Stage History related list on opportunities.

**•** If a user gets a field update error when saving a record, you can use the debug log to see which field update failed. The debug log
stops when a failure occurs.

**•** For reminder fields on tasks and events:

**–** Field updates can set the reminder for a task or event but they can't use the due date of a task or the scheduled time of an event.

**–** Formulas for date/time values are calculated in days. Divide the value by 1440—the number of minutes in a day—to express
the value in minutes. For example, the formula `Now()-7` means seven _days_ ago, while `Now()-7/1440` means seven
_minutes_ ago.

**•** If your organization uses multiple currencies, currency fields are updated using the record's currency. If you choose to update a field
based on a formula, any values in your formula are interpreted in the currency of the record.

**•** Field updates are tracked in the History related list if you have set history tracking on those fields.

**•** Workflow rules and some processes can invalidate previously valid fields. Invalidation occurs because updates to records based on
workflow rules and also on process-scheduled actions don’t trigger validation rules.

**•** If you have person accounts enabled, you can use the `Is Person Account` field as part of the evaluation criteria for workflow
rules. However, because the `Is Person Account` field is read-only, any field updates set up to modify it fails.

Tip: Salesforce processes rules in the following order:

**•** Validation rules

**•** Assignment rules

**•** Auto-response rules

**•** Workflow rules (with immediate actions)


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

**•** Escalation rules

Notes on Cross-Object Field Updates

**•** For all custom objects and some standard objects, you can create workflow and approval actions where a change to a detail record
updates a field on the related main record. Cross-object field updates work for custom-to-custom master-detail relationships,
custom-to-standard master-detail relationships, and a few standard-to-standard master-detail relationships. For more information,
see Cross-Object Field Updates on page 11.

**•** Approval processes can't use cross-object field update actions.

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** To create workflow rules so that case comments or emails automatically update fields on associated cases, select **Case Comment**
or **Email Message** in the Object dropdown list when creating a workflow rule and select **Case** in the Field to Update list. Email-to-Case
or On-Demand Email-to-Case must be enabled for your organization to use the Email Message in a workflow rule.

When cases are updated by an email-triggered workflow rule, the updated case can trigger:

**–** Workflow rules

**–** Validation rules

**–** Updates to roll-up summary fields

**–** Escalation rules

**–** Apex triggers

**–** Entitlement processes

The updated case can't trigger:

**–** Assignment rules

**–** Auto-response rules

Field Update Actions and Custom Fields

**•** Before changing a custom field’s type, make sure it isn’t the target of a workflow field update or referenced in a field update formula
that’s invalidated by the new type.

**•** You can't delete a custom field that is referenced by a field update.

**•** You can use field updates on encrypted custom fields, but if you try to use a formula to set the new value, the encrypted field isn't
available in the formula editor.

Field Update Actions on Opportunities and Contracts

**•** You can define field updates for the `Stage` field on opportunities, but be aware of how this field affects the `Type` and `Forecast`
`Category` fields.

**•** You can define field updates using the `Amount` field on opportunities but it only applies to those opportunities that don't have
products. Adding products to an opportunity changes the `Amount` field to a read-only field that is automatically calculated and
not affected by that field update.

**•** You can define field updates for the `Status` field on contracts. However, the value of this field can affect the value of the `Status`
`Category` field as well.

**•** Avoid creating a field update for contracts or orders that changes the `Status` field to any value other than Approved.


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Field Update Action Limitations

**•** The results of a field update can't trigger additional rules such as validation, assignment, auto-response, or escalation rules.

**•** The results of a field update can trigger additional workflow rules if you’ve flagged the field update to do so. For more information,
see Field Updates That Reevaluate Workflow Rules on page 826.

**•** Field updates that are executed as approval actions don’t trigger workflow rules or entitlement processes.

**•** These fields aren’t available for field update actions:

**–** Read-only fields like formula or auto-number fields

**–** The `Language` picklist field on multilingual solutions

**–** Some activity fields, such as `Related To` and `Private`

**•** Email message workflow rules can only be associated with field updates.

**•** If a field update references a specific user, you can't deactivate that user. For example, if your field update is designed to change the
owner of a record to Bob Smith, change the field update before deactivating Bob Smith.

**•** You can update long text area fields, but the option to insert `A specific value` restricts you to entering up to the maximum
number of characters allowed in the destination field.

**•** You can't make a field universally required if it's used by a field update that sets the field to a blank value.

**•** Workflow rules that update owners _don’t_ also transfer associated items. To ensure transfer, click **Change** next to the owner’s name
in a record and make your transfer selections.

##### Cross-Object Field Updates

For all custom objects and some standard objects, you can create actions where a change to a detail record updates a field on the
related main record. Cross-object field updates work for custom-to-custom master-detail relationships, custom-to-standard
master-detail relationships, and a few standard-to-standard master-detail relationships.

Field Updates That Reevaluate Workflow Rules
If `Re-evaluate Workflow Rules After Field Change` is enabled for a field update action, and a field update
results in a change to the value of the field, Salesforce reevaluates all workflow rules on the object.

SEE ALSO:

##### Cross-Object Field Updates Cross-Object Field Updates

For all custom objects and some standard objects, you can create actions where a change to a detail
record updates a field on the related main record. Cross-object field updates work for
custom-to-custom master-detail relationships, custom-to-standard master-detail relationships, and
a few standard-to-standard master-detail relationships.

[other]: Where possible, we changed noninclusive terms to align with our company value
of Equality. We maintained certain terms to avoid any effect on customer implementations.

For example, in a custom recruiting application, create a workflow rule that sets the status of an
application (the main object) to “Closed” when a candidate (the detail object) accepts the job. Or,
for standard objects, create a rule to change the status of a case from “Awaiting Customer Response”
to “In Progress” when a customer adds a case comment.


EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Custom Object to Custom Object

Cross-object field updates are supported for all custom objects that are children of custom objects in a master-detail relationship.

Custom Object to Standard Object

Cross-object field updates are supported for custom objects that are children of certain standard objects in a master-detail relationship.
The standard objects that support cross-object field updates from custom objects are:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contact

**•** Contract

**•** Contract Line Item

**•** Entitlement

**•** Opportunity

**•** Order

**•** Question

**•** Quote

**•** Service Contract

**•** Solution

Standard Object to Standard Object

Cross-object field updates are supported for standard objects that are children of standard objects in a master-detail relationship. However,
only these standard-to-standard relationships are supported.

Note: If you have workflow rules on converted leads and want to use cross-object field updates on the resulting accounts and
opportunities, you must enable the lead setting `Require Validation for Converted Leads` .

**•** Case Comments updating Case

**•** Email updating Case

Tip: To create workflow rules so that case comments or emails automatically update fields on associated cases, select **Case**
**Comment** or **Email Message** in the Object dropdown list when creating a workflow rule and select **Case** in the Field to Update
list. Email-to-Case or On-Demand Email-to-Case must be enabled for your organization to use the Email Message in a workflow
rule.

**•** Opportunity Product updating Opportunity

Note: Cross-object field updates to a parent opportunity's `Amount` and `Quantity` fields only work if the opportunity
has no opportunity products associated with it.

**•** Opportunity updating Account—Supported for both business accounts and person accounts.

Standard-to-standard cross-object field update actions:

**•** Can’t be used in, or assigned to, approval processes.

**•** Update a parent record even if the user doesn’t have edit access to it.


Automate Your Business Processes with Salesforce Flow Considerations for Automated Actions

Note: If you have Apex code that updates parent fields in the same relationships as a cross-object field update action, consider
replacing your code with cross-object field updates. Otherwise, both will fire, and since workflow rules run after Apex triggers, the
workflow field update will override any change made by your Apex code.

SEE ALSO:

Considerations for Field Update Actions

[Object Relationships Overview](https://help.salesforce.com/s/articleView?id=sf.overview_of_custom_object_relationships.htm&language=en_US)

##### Field Updates That Reevaluate Workflow Rules

If `Re-evaluate Workflow Rules After Field Change` is enabled for a field
update action, and a field update results in a change to the value of the field, Salesforce reevaluates
all workflow rules on the object.

**•** If the field update changes the field’s value, all workflow rules on the associated object are
reevaluated. Any workflow rules whose criteria are met as a result of the field update are
triggered.

**•** If any of the triggered workflow rules result in another field update that’s also enabled for
workflow rule reevaluation, a domino effect occurs, and more workflow rules can be reevaluated
as a result of the newly triggered field update. This cascade of workflow rule reevaluation and
triggering can happen up to five times after the initial field update that started it.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Make sure that your workflow rules aren’t set up to create recursive loops. For example, if a field update for Rule1 triggers Rule2, and
a field update for Rule2 triggers Rule1, the recursive triggers can cause your organization to exceed its limit for workflow time triggers
per hour.

**•** In a batch update, workflow is only retriggered on the entities where there’s a change.

**•** Only workflow rules on the same object as the initial field update are reevaluated and triggered.

**•** Only workflow rules that didn’t fire before are retriggered.

**•** Cross-object workflow rules aren’t candidates for reevaluation.

**•** Cross-object field updates that cause a field value to change don’t trigger workflow rule reevaluation on the associated object.

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** Time-dependent actions aren't executed for a reevaluated workflow rule in the following situations:

**–** The reevaluated workflow rule’s immediate actions cause the record to no longer meet the workflow rule criteria.

**–** An Apex `after` trigger that is executed as a result of a workflow or approvals action causes the record to no longer meet the
workflow rule criteria.

SEE ALSO:

Considerations for Field Update Actions


## Automate Your Business Processes with Salesforce Flow Approval Processes

#### Considerations for Outbound Messages

Review the considerations for using outbound message actions before implementing them in your
workflows.

When creating outbound messages for workflow rules or approval processes, keep these
considerations in mind.

**•** A single SOAP message can include up to 100 notifications. Each notification contains an ID
that uniquely identifies a record, and a reference to the data in the record. If the information in
the record changes after the notification is sent, but before the notification is delivered, only
the updated information is delivered. If the record is deleted before the notification is delivered,
the notification contains no data.

**•** Messages are queued until they’re sent, to preserve message reliability.

EDITIONS

Available in: Lightning
Experience and Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If the endpoint is unavailable, messages stay in the queue until sent successfully or until they’re 24 hours old. After 24 hours, messages
are dropped from the queue.

**•** If a message can't be delivered, the interval between retries increases exponentially, up to a maximum of two hours between retries.

**•** Messages are retried independent of their order in the queue, which can result in messages being delivered out of order.

**•** A message can be delayed by other, long-running messages in the queue. The queue can also contain messages that originate from
other Salesforce orgs that are hosted on the same Salesforce instance. The system attempts to optimize the execution of messages
that historically have fast run times so that they aren’t delayed by slow-running messages. To get the best performance, make sure
that the message endpoint runs efficiently. For slow-running messages, consider using asynchronous processes, such as platform
events or Apex future methods.

**•** You can't build an audit trail using outbound messages. While each message is delivered at least one time, it can be delivered more
than one time. Also, if delivery can’t be done within 24 hours, the message doesn’t get delivered at all. Finally, as noted above, the
source object can change after a notification is sent but before it’s delivered, so the endpoint will only receive the latest data, not
any intermediate changes.

SEE ALSO:

_[Platform Events Developers Guide](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm)_

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm)_ : Future Annotation

## Approval Processes

It’s likely that you’re familiar with process automation in the form of workflow rules. Approval
processes take automation one step further, letting you specify a sequence of steps that are required
to approve a record.

An approval process automates how records are approved in Salesforce. An approval process
specifies each step of approval, including from whom to request approval and what to do at each
point of the process.

Example: Your org has a three-tier process for approving expenses. This approval process
automatically assigns each request to right person in your org, based on the amount requested.

If an expense record is submitted for approval, lock the record so that users can’t edit it and
change the status to Submitted.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

### Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

If the amount is $50 or less, approve the request. If the amount is greater than $50, send an approval request to the direct manager.
If the amount is greater than $5,000 and the first approval request is approved, send an approval request to the vice president.

If all approval requests are approved, change the status to Approved and unlock the record. If any approval requests are rejected,
change the status to Rejected and unlock the record.

### Set Up an Approval Process

If Approvals is the right automation tool for your business process, follow these high-level steps to create one for your org.

Prepare Your Org for Approvals
Make sure that your users can submit their records for approval, and consider how you can make it easy for approvers to respond
to approval requests.

Limits and Considerations for Approvals
Before you automate something with an approval process, be aware of the limits and considerations.

Sample Approval Processes
Review samples of common approval processes to help you get started creating your own.

Approval History Reports
If you create a custom report type for approval process instances, users can view the historical details of completed and in-progress
approval processes and their individual steps.

Manage Multiple Approval Requests
Transfer multiple approval requests from one user to another or remove multiple approval requests from the approval process.

Approval Requests for Users
Your admin can set up approval processes that let you and other users submit records for approval, which results in _approval requests_ .

Approval Process Terminology
Salesforce uses this terminology for approval processes.

### Set Up an Approval Process

If Approvals is the right automation tool for your business process, follow these high-level steps to
create one for your org.

1. Prepare to Create an Approval Process
Plan each approval process carefully to ensure a successful implementation.

2. Choose the Right Wizard to Create an Approval Process
Before you create an approval process, determine which wizard is best for your needs.

3. Add an Approval Step to an Approval Process
Approval steps define the chain of approval for a particular approval process. Each step
determines which records can advance to that step, who to assign approval requests to, and
whether to let each approver’s delegate respond to the requests. The first step specifies what
to do if a record doesn’t advance to that step. Later steps specify what happens if an approver
rejects the request.

4. Add Automated Actions to an Approval Process
You can associate actions to approval steps, initial submission, final approval, final rejection, or
recall. Approval processes support four automated actions.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

5. Activate an Approval Process
After you’ve created at least one step for the approval process, activate the process.

SEE ALSO:

Approval Process Terminology

Sample Approval Processes

Prepare Your Org for Approvals

#### Prepare to Create an Approval Process

Plan each approval process carefully to ensure a successful implementation.

Review the following checklist before creating your approval process.

**•** Prepare an approval request email template.

**•** Prepare an approval request post template.

**•** Determine the approval request sender.

**•** Determine the assigned approver.

**•** Determine the delegated approver.

**•** Decide if your approval process needs a filter.

**•** Design initial submission actions.

**•** Decide if users can approve requests from a wireless device.

**•** Determine if users can edit records that are awaiting approval.

**•** Decide if records should be auto-approved or rejected.

**•** Determine how many levels your process has.

**•** Determine the actions when an approval request is approved or rejected.

Which email template do you want to use for approval requests?

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

The email template you specify on an approval process is used when notifying users that an approval request is assigned to them. You
can use the Salesforce default email template or create your own template. Include the appropriate approval process merge fields to
link directly to the approval request. Does your org have email approval response enabled? If so, the default email template includes
instructions for replying to an approval request. Type _`approve`_, _`approved`_, _`yes`_, _`reject`_, _`rejected`_, or _`no`_ in the first line of
the email body and add comments in the second line.

Which Chatter post template do you want to use for approval requests?

If your org has Approvals in Chatter enabled, specify an approval post template to use when notifying a user via Chatter about an assigned
approval request. You can use the Salesforce default post template or create your own.

Who is the sender of approval requests?

Approval request notifications are sent from the user who submitted the record for approval. When you configure an email alert, you
can add a different return email address for these notifications. You can choose the email address of the default workflow user or a
previously configured and verified org-wide address. Determine which email address to use.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Who can approve requests?

Any of the following can approve or reject a request.

**•** A user or queue that the approval request submitter chooses.

**•** A queue specified by the administrator.

**•** A user listed in the `Manager` standard field on the submitter’s user detail page.

**•** A user listed in a custom hierarchy field on the submitter’s user detail page.

**•** Any combination of users and related users (users listed in a standard or custom field on the submitted record) specified by the
administrator.

Do you want approval requests delegated to another user for approval?

An approver can designate a delegate to approve requests, but you can disable this option. To assign delegates, populate the `Delegated`
`Approver` field for each user’s detail page.

Note: Internal Salesforce users are listed by and can be added using the Delegated Approver lookup field. Use Data Loader and
a comma-delineated (CSV) file to add users with communities licenses as Delegated Approvers. The CSV uses the

`CommunityUserId` rather than the `UserId` for `DelegatedApproverId` . Communities licenses are used with Experience
Cloud sites and legacy portals.

Which records are included in this process?

Determine what attributes a record must have to be included in your approval process. If necessary, create the custom fields to store
this information so that you can use it in your filter criteria. For example, if you want to include expense records from your headquarters
office only, create a custom picklist field called `Office Location` that has two options: “HQ” and “Field.” Then, you would specify
in your filter criteria that records must have “HQ” in the `Office Location` field to be included in the approval process.

What happens when a record is first submitted for approval?

When users submit a record for approval, Salesforce automatically locks the record so that other users can’t change it while it’s awaiting
approval. You can still add campaign members to campaigns locked for approval.

Decide if you want other workflow actions to happen when a record is first submitted, such as email alerts, tasks, field updates, and
outbound messages. These actions become your initial submission actions.

Can users approve requests from a mobile device?

Determine if you want to require users to log in to Salesforce to approve requests. You can also set up your approval process to allow
users to approve requests remotely using a mobile browser.

Who can edit records that are awaiting approval?

Records submitted for approval are locked. Users with the “Modify All” object-level permission for the given object or the “Modify All
Data” permission can always unlock a record and edit it. You can also specify that the currently assigned approver can edit the record.
You can still add campaign members to campaigns locked for approval.

Can records be automatically approved, rejected, or skipped based on certain criteria?

You can set entry criteria for each step of your process. Configure Salesforce to approve, reject, or skip the process if a record doesn’t
meet the criteria. For example, all expenses submitted with an `Amount` less than $15 are automatically approved.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

How many people have to approve these requests?

An approval process can have several layers of approvals. Determine how many users have to approve requests and in what order.

What happens when a request is approved or rejected?

When a request is recalled, approved, or rejected, Salesforce can perform up to 10 instances of each of the following types of actions—up
to 40 actions total. You can also configure up to 40 actions to occur when a record has received all necessary approvals or is rejected.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals

Sample Approval Processes

#### Choose the Right Wizard to Create an Approval Process

Before you create an approval process, determine which wizard is best for your needs.

##### Create an Approval Process with the Jump Start Wizard

For approval processes that use a single step, use the jump start wizard. This wizard chooses
some default options for you.

Default Selections for the Approval Process Jump Start Wizard
To make it easier for you to get started with a simple approval process, the jump start wizard
automatically chooses some default options for you.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Create an Approval Process with the Standard Wizard
When your approval process is more complex and you want to define specific steps, use the standard wizard.

SEE ALSO:

Set Up an Approval Process

##### Create an Approval Process with the Jump Start Wizard

For approval processes that use a single step, use the jump start wizard. This wizard chooses some
default options for you.

**1.** From Setup, enter _`Approval Processes`_ in the `Quick Find` box, then select **Approval**
**Processes** .

**2.** Select an object.

**3.** Select **Create New Approval Process** - **Use Jump Start Wizard** .

**4.** Configure the approval process by following the wizard.

**a.** Default Selections for the Approval Process Jump Start Wizard

**b.** Choose Approval Request Notification Templates

**c.** Design the Approval Request Page

**d.** Control Which Records Apply to an Approval Process


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

**e.** Identify Assigned Approvers for an Approval Step

SEE ALSO:

##### Default Selections for the Approval Process Jump Start Wizard

Considerations for Configuring Approvals

Considerations for Setting Approvers

Set Up an Approval Process

Choose the Right Wizard to Create an Approval Process

##### Default Selections for the Approval Process Jump Start Wizard

To make it easier for you to get started with a simple approval process, the jump start wizard
automatically chooses some default options for you.

After creating an approval process using the jump start wizard, you can modify these default options
and add more steps from the approval process detail page. Exception: you can’t modify the Record
Lock action on the Initial Submission Actions list.

**•** To edit records awaiting approval in the approval process, users must have the “Modify All”
permission for the given object or the Modify All Data permission.

**•** The page layout for the approval request includes the record name (or number), owner, date
created, and approval history.

**•** The security settings require approvers to log in to Salesforce to view the approval page.

**•** Only the owner of the record can submit the record for approval.

**•** Records are locked when submitted for approval.

**•** Records remain locked until approved or rejected.

**•** Rejected records are unlocked.

**•** Only admins can recall a record after it’s submitted.

**•** There are no auto-approve or auto-reject actions.

**•** No email notification is sent upon approval or rejection.

**•** No field values are automatically updated during the approval process.

**•** An approver can’t automatically delegate another user to approve the approval requests.

**•** The **Allow submitters to recall approval requests** option isn’t selected.

SEE ALSO:

Create an Approval Process with the Jump Start Wizard

Choose the Right Wizard to Create an Approval Process


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

##### Create an Approval Process with the Standard Wizard

When your approval process is more complex and you want to define specific steps, use the standard
wizard.

From Setup, enter _`Approval Processes`_ in the `Quick Find` box, then select **Approval**
**Processes** .

Select an object, and then select **Create New Approval Process** - **Use Standard Setup Wizard** .
Configure the approval process.

###### 1. Control Which Records Apply to an Approval Process

Narrow down the list of records that can be part of the approval process by specifying criteria.
You can either use filters or write a formula.

2. Choose Approval Request Notification Templates
When an approval process assigns an approval request to a user, Salesforce sends the user an
approval request email. If Approvals in Chatter is enabled, Salesforce also posts the approval
request to Chatter. Choose templates for each of these notifications.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval
processes:

**•** Customize Application

3. Choose an Automated Approver Throughout an Approval Process
Associate a hierarchy field—such as the user’s manager—with an approval process. When selected, the field is available as an
assigned approver option for approval steps. You can always select a hierarchy field here but not use it for any approval steps.

4. Specify Who Can Edit Locked Records
When a record is submitted for approval, it’s locked to prevent users from editing it during the approval process. Use the record
editability properties to determine who can edit records that are locked in this approval process.

5. Design the Approval Request Page
The approval page is where an approver responds to an approval request. Customize which fields appear on that page and in which
order. This page is used only for this approval process.

6. Specify Who Can Submit Records to an Approval Process
Only specified individuals or roles can submit a record for approval. You can also let submitters recall an approval request.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals

###### Control Which Records Apply to an Approval Process

Narrow down the list of records that can be part of the approval process by specifying criteria. You
can either use filters or write a formula.

If you want all records to pass through the approval process, click Next. If only certain types of
records are considered, use one of the following options.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Example: This filter lets an expense report enter this approval process only if the employee who submitted the report is at
headquarters.

```
   Current User: Office Location Equals Headquarters

```

This formula lets a record enter this approval process only if its discount approval cutoff date is less than 30 days away.

```
   (Discount_Approval_CutoffDate__c < (CloseDate - 30)

```

SEE ALSO:

Considerations for Configuring Approvals

[Formula Operators and Functions by Context](https://help.salesforce.com/s/articleView?id=sf.customize_functions.htm&language=en_US)

###### Choose Approval Request Notification Templates

When an approval process assigns an approval request to a user, Salesforce sends the user an
approval request email. If Approvals in Chatter is enabled, Salesforce also posts the approval request
to Chatter. Choose templates for each of these notifications.

These fields are available from both the jump-start and standard wizards.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Note: If email approval response is enabled, be sure that the email template you use describes how to correctly use both response
options: clicking the link and replying by email. If the user doesn’t respond correctly (for example, if the user misspells _`approve`_
or types it on the wrong line), Salesforce doesn’t register the user’s response.

SEE ALSO:

Chatter Post Templates for Approval Requests

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Merge Fields for Approvals

###### Choose an Automated Approver Throughout an Approval Process

Associate a hierarchy field—such as the user’s manager—with an approval process. When selected,
the field is available as an assigned approver option for approval steps. You can always select a
hierarchy field here but not use it for any approval steps.

Set **Next Automated Approver Determined By** with one of the following options.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: If you select the `Manager` field, you can configure any step in this process to route approval requests to the submitting
user’s manager.

If you select **Use Approver Field of** _`Object`_ **Owner**, the first step that isn’t skipped is routed to the owner’s manager. All other
steps are routed to the previous approver’s manager.

SEE ALSO:

[Custom Field Types](https://help.salesforce.com/s/articleView?id=sf.custom_field_types.htm&language=en_US)

Considerations for Setting Approvers


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

###### Specify Who Can Edit Locked Records

When a record is submitted for approval, it’s locked to prevent users from editing it during the
approval process. Use the record editability properties to determine who can edit records that are
locked in this approval process.

Note:

**•** Even when a campaign is locked for approval, users can add campaign members to it.

**•** In Lightning Experience, you can't unlock Knowledge articles during an approval process.

###### Design the Approval Request Page

The approval page is where an approver responds to an approval request. Customize which fields
appear on that page and in which order. This page is used only for this approval process.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

###### Specify Who Can Submit Records to an Approval Process

Only specified individuals or roles can submit a record for approval. You can also let submitters
recall an approval request.

Initial Submitters

Page Layout Settings

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Submission Settings

#### Add an Approval Step to an Approval Process

Approval steps define the chain of approval for a particular approval process. Each step determines
which records can advance to that step, who to assign approval requests to, and whether to let
each approver’s delegate respond to the requests. The first step specifies what to do if a record
doesn’t advance to that step. Later steps specify what happens if an approver rejects the request.

You can add steps to an approval process only if it’s inactive.

From the approval process, click **New Approval Step**, and follow the wizard.

Steps are executed in the order specified.

1. Control Which Records Apply to an Approval Step
Control which records are part of the approval step by setting the step’s criteria. You can also
specify what happens to records that don’t meet the step’s criteria.

2. Identify Assigned Approvers for an Approval Step
Specify who to send an approval request for this step to.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval steps:

**•** Customize Application

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

3. Specify Rejection Behavior for an Approval Step
Configure what happens if an approver rejects a request. The final rejection actions for the approval process determine the first step’s
rejection behavior.

SEE ALSO:

Set Up an Approval Process

Enable Email Approval Response

##### Control Which Records Apply to an Approval Step

Control which records are part of the approval step by setting the step’s criteria. You can also specify
what happens to records that don’t meet the step’s criteria.

Criteria Options

If all records go through this approval step, leave **All records should enter this step** selected.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If only certain types of records are supposed to enter this process, select **Enter this step if the following...** and choose the appropriate
option (1). For details on the options, see Control Which Records Apply to an Approval Process.

(2) Else Options for Approval Step Criteria

If you specified filter criteria or entered a formula, choose what happens to records that don’t meet the criteria or if the formula doesn’t
return `True` .

Note: You can’t change your selection after the approval process has been activated, even if you deactivate the approval process.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

SEE ALSO:

Set Up an Approval Process

Enable Email Approval Response

##### Identify Assigned Approvers for an Approval Step

Specify who to send an approval request for this step to.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

SEE ALSO:

Considerations for Setting Approvers

##### Specify Rejection Behavior for an Approval Step

Configure what happens if an approver rejects a request. The final rejection actions for the approval
process determine the first step’s rejection behavior.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

#### Add Automated Actions to an Approval Process

You can associate actions to approval steps, initial submission, final approval, final rejection, or
recall. Approval processes support four automated actions.

Example: When expenses are approved, you want to print checks for payment. To do so, you add an outbound message, which
sends the appropriate information to your Oracle accounting service, as a Final Approval action.

Groups of Automated Actions in an Approval Process
Each approval process is organized into groups of actions based on when the actions occur, such as initial submission. To add an
automated action to your approval process, determine which group of actions to add it to.


Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

Add an Automated Action to Your Approval Process
If you didn’t create an automated action before configuring your approval process, you can create one directly from the approval
process.

Add an Existing Automated Action to Your Approval Process
If you’ve already created an automated action, you can add it to your approval process.

SEE ALSO:

Set Up an Approval Process

Automated Actions

Considerations for Automated Actions

##### Groups of Automated Actions in an Approval Process

Each approval process is organized into groups of actions based on when the actions occur, such
as initial submission. To add an automated action to your approval process, determine which group
of actions to add it to.

SEE ALSO:

Considerations for Automated Actions


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Set Up an Approval Process

##### Add an Automated Action to Your Approval Process

If you didn’t create an automated action before configuring your approval process, you can create
one directly from the approval process.

**1.** Open the approval process that you want to add an action to.

**2.** From the appropriate related list, click **Add New** . For an approval step where the Approval
Actions and Rejection Actions are hidden, click **Show Actions** .

**3.** Choose the type of action.

The list of available actions differs depending on your settings and whether you’ve reached the
limit for a type of action.

**4.** Configure the action.

SEE ALSO:

Set Up an Approval Process

Considerations for Automated Actions

Groups of Automated Actions in an Approval Process

##### Add an Existing Automated Action to Your Approval Process

If you’ve already created an automated action, you can add it to your approval process.

**1.** Open the approval process that you want to add an action to.

**2.** From the appropriate related list, click **Add Existing** . If that button is hidden, click **Show Actions** .

**3.** Choose the type of action.

**4.** Move the action from Available Actions to Selected Actions.

**5.** Save your changes.

SEE ALSO:

Groups of Automated Actions in an Approval Process

Considerations for Automated Actions


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval actions:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To select approval actions:

**•** Customize Application

### Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

#### Activate an Approval Process

After you’ve created at least one step for the approval process, activate the process.

**1.** Open the approval process.

**2.** Make sure that it’s configured correctly.

#### 3. Click Activate .

SEE ALSO:

### Prepare Your Org for Approvals

Considerations for Managing Approvals

### Prepare Your Org for Approvals

Make sure that your users can submit their records for approval, and consider how you can make
it easy for approvers to respond to approval requests.

Let Users Submit for Approval
After you activate an approval process for an object, customize the object’s page layouts to
support record submission.

Override the Sender for Email Approval Notifications
By default, the sender for email approval notifications is the user who submitted the record for
approval. You can override the sender with an organization-wide address, like
approval@acmewireless.com.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To activate approval
processes:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Let Users Respond to Approval Requests from Your Org
Give your users an instant view of their approval requests by customizing the Home page or navigation bar.

Let Users Respond to Approval Requests by Email
If the email notification includes all the information that an approver must decide, enable email approval response. That way, a user
can simply reply to the email notification.

Let Users Respond to Approval Requests from Chatter
If your users don’t need in-depth information to decide how to respond to an approval request, enable Approvals in Chatter. That
way, they don’t have to leave their feed to continue with their day-to-day tasks.

Let Users Respond to Approvals Requests in Slack
If your users don’t need in-depth information to decide how to respond to an approval request, and they have a connection to Slack,
enable Approvals in Slack. That way, a user can simply respond to the Slack notification.

SEE ALSO:

Set Up an Approval Process

Limits and Considerations for Approvals


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

#### Let Users Submit for Approval

After you activate an approval process for an object, customize the object’s page layouts to support
record submission.

Add the following components to your page layouts.

**•** Submit for Approval button

**•** Approval History related list

The Approval History related list lets users submit approval requests and track a record’s progress
through an approval process from the record detail page.

SEE ALSO:

[Page Layouts](https://help.salesforce.com/s/articleView?id=sf.customize_layout.htm&language=en_US)

Prepare Your Org for Approvals

#### Override the Sender for Email Approval Notifications

By default, the sender for email approval notifications is the user who submitted the record for
approval. You can override the sender with an organization-wide address, like
approval@acmewireless.com.

**User Permissions Needed**

To edit process automation settings: Customize Application

To create, update, and delete flow list views: Manage Flow

After you add an organization-wide address to your org:

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To modify page layouts:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**1.** From Setup, enter _`Process Automation Settings`_ in the Quick Find box, then select **Process Automation Settings** .

**2.** For Email Approval Sender, select the organization-wide address.

**3.** Save your changes.

#### Let Users Respond to Approval Requests from Your Org

Give your users an instant view of their approval requests by customizing the Home page or
navigation bar.

Lightning Experience:

**•** Add the Items to Approve component to the appropriate Lightning Home pages.

This component is available only for Home pages. To add it to a Home page, use the Lightning
App Builder in Setup.

**•** Add the Approval Requests navigation item to the appropriate Lightning apps.

This item is available only for Lightning apps. To add it to a Lightning app, use the App Manager
in Setup.

Salesforce mobile app:


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

Add the Approvals item to the navigation items of any Lightning app.

Salesforce Classic:

Add the Items to Approve related list to the appropriate home page layouts.

SEE ALSO:

[Create Lightning Apps](https://help.salesforce.com/s/articleView?id=sf.apps_lightning_create.htm&language=en_US)

[Set Up the Lightning Experience Home Page](https://help.salesforce.com/s/articleView?id=sf.admin_home_lex_intro.htm&language=en_US)

[Salesforce Classic Home Tab Page Layouts](https://help.salesforce.com/s/articleView?id=sf.customize_homepage.htm&language=en_US)

Prepare Your Org for Approvals

#### Let Users Respond to Approval Requests by Email

If the email notification includes all the information that an approver must decide, enable email
approval response. That way, a user can simply reply to the email notification.

##### Considerations for Email Approval Response

Before you enable the ability to act on approvals via email, review how email works with your
approval processes.

Default Template for Email Approval Response
When you enable email approval response, Salesforce uses a default email template for approval
processes—unless you specify a custom email template.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Enable Email Approval Response
After you’ve reviewed the considerations and prepared the right template, flip the switch that lets users respond to approval requests
directly from their email.

SEE ALSO:

Prepare Your Org for Approvals

Let Users Respond to Approval Requests from Chatter

##### Considerations for Email Approval Response

Before you enable the ability to act on approvals via email, review how email works with your
approval processes.

Compatibility with Approval Processes

Email approval response isn’t supported for approval processes that:

**•** Assign approval to a queue

**•** After the first step, let the approver manually select the next approver

Implicit Agreement with Salesforce

By enabling the email approval response feature, you agree to let Salesforce:

**•** Process email approval responses


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** Update approval requests for all active users in your org

**•** Update the approval object on behalf of your org’s users

SEE ALSO:

Limits and Considerations for Approvals

Let Users Respond to Approval Requests by Email

##### Default Template for Email Approval Response

When you enable email approval response, Salesforce uses a default email template for approval
processes—unless you specify a custom email template.

Example: _`Requesting User`_ has requested your approval for the following item.

To approve or reject this item, reply to this email with the word APPROVE, APPROVED, YES,
REJECT, REJECTED, or NO in the first line of the email message, or click this link:

```
  Link to approval request page

```

If replying via email you can also add comments on the second line. The comments are stored
with the approval request in Salesforce CRM.

Note: For Salesforce to process your response the word APPROVE, APPROVED, YES, REJECT,
REJECTED, or NO must be in the first line of the reply email. Also, any comment must be in
the second line.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If your org has Approvals in Chatter enabled and the approver opted to receive notifications as Chatter posts, the default email template
is appended with:

Example: You can also approve, reject, and comment on this request from your Chatter feed:

```
  Link to approval post in Chatter

```

Note: If you use a custom email template for your approval process, make sure that it explains both response options: clicking
the link and replying by email. If the user doesn’t respond correctly (for example, if the user misspells approve or types it on the
wrong line), Salesforce doesn’t register the response.

SEE ALSO:

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Merge Fields for Approvals

Let Users Respond to Approval Requests by Email


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

##### Enable Email Approval Response

After you’ve reviewed the considerations and prepared the right template, flip the switch that lets
users respond to approval requests directly from their email.

Before you begin, give the appropriate users the “API Enabled” user permission so that they can
respond to approval requests by email.

**1.** From Setup, enter _`Process Automation Settings`_ in the `Quick Find` box, then
select **Process Automation Settings** .

**2.** Select **Enable email approval response** .

**3.** Save your changes.

SEE ALSO:

Considerations for Email Approval Response

Let Users Respond to Approval Requests by Email

#### Let Users Respond to Approval Requests from Chatter

If your users don’t need in-depth information to decide how to respond to an approval request,
enable Approvals in Chatter. That way, they don’t have to leave their feed to continue with their
day-to-day tasks.

Prepare to Enable Approvals in Chatter
Because Approvals in Chatter relies on both Chatter and the Approvals feature, getting your
org set up involves more than just turning on the feature. Before you enable Approvals in
Chatter, understand the limitations and considerations for Approvals in Chatter and post
templates.

Considerations for Approvals in Chatter
Find out more about Approvals in Chatter, before you enable it.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable Email Approval
Response:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Enable Approvals in Chatter
If your organization has both Approvals and Chatter enabled, administrators can turn on Approvals in Chatter. Users then receive
approval requests as posts in their Chatter feeds.

Where Do Approval Request Posts Appear?
When your org has Approvals in Chatter enabled, approval request posts appear in various Chatter feeds. To see the approval request
post, you must have access to the approval record.

Chatter Post Templates for Approval Requests
Approval post templates for Chatter let you customize the information that is included in the approval request post when it displays
in a Chatter feed.


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

##### Prepare to Enable Approvals in Chatter

Because Approvals in Chatter relies on both Chatter and the Approvals feature, getting your org
set up involves more than just turning on the feature. Before you enable Approvals in Chatter,
understand the limitations and considerations for Approvals in Chatter and post templates.

Do the following for each object for which you want approval requests to appear in Chatter.

**1.** Enable feed tracking.

**2.** Create an approval post template.

Tip: For each object, create one post template that works for all approval processes. Mark
that post template the default for the object.

SEE ALSO:

[Feed Tracking](https://help.salesforce.com/s/articleView?id=sf.collab_feed_tracking_overview.htm&language=en_US)

Chatter Post Templates for Approval Requests

Where Do Approval Request Posts Appear?

##### Considerations for Approvals in Chatter Considerations for Approvals in Chatter

Find out more about Approvals in Chatter, before you enable it.

**•** When you enable Approvals in Chatter in your org, it’s turned on for all users. Users can then
update their own Chatter settings to opt out of receiving approval requests as posts in their
Chatter feeds.

**•** Chatter post approval notifications are available only for approval processes associated with an
object that has been enabled for feed tracking.

**•** If the approval object is a detail object in a master-detail relationship, `Owner` isn’t available
for approval page layouts or approval post templates.

Limitations

**•** Approvals in Chatter doesn't support delegated approvers or queues.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** You can’t recall or reassign an approval request from a post. Instead, perform these actions from the approval record.

**•** Approval requests from Sites or portal users aren’t supported.

Approval Posts

**•** Approval posts can't be deleted in the Salesforce user interface; you can only delete them through the API.

**•** If you don’t select an approval post template, the approval post uses the system default template or the default template for the
object, if available.

**•** Only users with access to the approval record can see the approval request post. Comments on approval posts aren’t persisted to
the approval record.

**•** Different users see different configurations of the approval request post.

**–** Only approvers see approval action buttons on their posts, and then only in their profile feed or their news feed.

**–** Only approvers see approver names in the header.


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** If you change the approver, step name, or the routing type on an approval process while it’s in progress, existing approval posts
aren’t updated.

**•** When an approval request is recalled, a new post is generated. It appears on the news feeds of the submitter, all approvers, and
followers of the object. It also appears on the record feed.

**•** If a step requires unanimous approval from multiple approvers, the approval request post for that step doesn’t list all selected
approvers in its header. Approvers see only their own name in the post header.

SEE ALSO:

Let Users Respond to Approval Requests by Email

Prepare to Enable Approvals in Chatter

##### Where Do Approval Request Posts Appear?

Limits and Considerations for Approvals

##### Enable Approvals in Chatter

If your organization has both Approvals and Chatter enabled, administrators can turn on Approvals
in Chatter. Users then receive approval requests as posts in their Chatter feeds.

Before you begin, make sure that all approval processes in your org are properly configured to take
advantage of Approvals in Chatter. After turning on this feature, all existing active approval processes
start generating Chatter posts.

**1.** From Setup, enter _`Chatter Settings`_ in the `Quick Find` box, then select **Chatter**
**Settings** .

**2.** Click **Edit** .

**3.** Select **Allow Approvals** .

**4.** Save your changes.

SEE ALSO:

Prepare to Enable Approvals in Chatter

Considerations for Approvals in Chatter

##### Where Do Approval Request Posts Appear? Where Do Approval Request Posts Appear?

When your org has Approvals in Chatter enabled, approval request posts appear in various Chatter
feeds. To see the approval request post, you must have access to the approval record.

Approval request posts show up in these feeds.

**•** Chatter feed of the assigned approver

**•** Submitter’s profile

**•** Chatter feed of the submitter if the submitter is following the approval request record

**•** Chatter feed of the approval request record

**•** Chatter feed of anyone following the approval request record

**•** Object-specific filter on the Chatter feed of anyone following the approval record


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable Approvals in
Chatter:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** Company filter of every user with access to the approval record

SEE ALSO:

What Happens When You Opt Out of Chatter Approval Requests?

Considerations for Approvals in Chatter

Let Users Respond to Approval Requests from Chatter

##### Chatter Post Templates for Approval Requests

Approval post templates for Chatter let you customize the information that is included in the
approval request post when it displays in a Chatter feed.

###### Considerations for Chatter Post Templates for Approval Requests

Keep these limitations and dependencies in mind when working with post templates.

Create a Chatter Post Template
Identify which fields to display in an approval request post.

SEE ALSO:

[Manage Deleted Custom Fields](https://help.salesforce.com/s/articleView?id=sf.fields_managing_deleted_fields.htm&language=en_US)

###### Considerations for Chatter Post Templates for Approval Requests

Keep these limitations and dependencies in mind when working with post templates.

Limitations

**•** The associated object must be enabled for approvals and feed tracking.

**•** If an approval post template is in use by an approval process, you can't delete it.

**•** Chatter posts for approval requests only appear in Salesforce Classic. To respond to approval
requests in Lightning Experience, users go to the Approval Requests tab.

Dependencies

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Deleting a custom field removes it from any approval post template that references it. Existing posts aren't affected. Undeleting the
custom field restores it to the available fields list, but doesn't restore it to any approval post templates that previously contained it.

**•** Deleting (or undeleting) a custom object also deletes (or undeletes) its associated approval post templates and any of its approval
request posts that are already in Chatter feeds.

**•** If you rename a custom object, approval post templates associated with it update accordingly.

SEE ALSO:

Create a Chatter Post Template

Limits and Considerations for Approvals


Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

###### Create a Chatter Post Template

Identify which fields to display in an approval request post.

**1.** From Setup, enter _`Post Templates`_ in the `Quick Find` box, then select **Post**
**Templates** .

**2.** Click **New Template** .

**3.** Select the object for your template.

**4.** Click **Next** .

**5.** Give the template a name and description.

**6.** If you want this template to be the default for the associated object, select **Default** .

**7.** Add up to four fields to display on the approval request post.

We recommend putting any text-heavy fields—such as Comments or Description—at the
bottom.

**8.** Save your changes.

SEE ALSO:

Choose Approval Request Notification Templates

Considerations for Chatter Post Templates for Approval Requests

#### Let Users Respond to Approvals Requests in Slack

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To create approval request
post templates:

**•** Customize Application

If your users don’t need in-depth information to decide how to respond to an approval request, and they have a connection to Slack,
enable Approvals in Slack. That way, a user can simply respond to the Slack notification.

##### Considerations for Approvals in Slack

Find out more about Approvals in Slack, before you enable it.

Enable Approval Notifications in Slack
If your org uses both Approvals and Salesforce Digital HQ app, approval notifications are automatically enabled in Slack. Users receive
approval requests as messages on the Salesforce Digital HQ’s Messages tab.

Where Do Slack Approval Notifications Appear?
When you have Approvals in Slack enabled, approval notifications are sent to the approver via the Salesforce Digital HQ app as a
direct message in Slack. To see the approval request post, you must have access to Slack.

##### Considerations for Approvals in Slack

Find out more about Approvals in Slack, before you enable it.

Users must have the Salesforce Digital HQ app in Slack. When you enable Approvals in Slack in your
org, it’s turned on for all users. Before you use Approvals in Slack, make sure you understand the
limitations.

**•** You can connect the Salesforce Digital HQ app to only one Salesforce org.

**•** The only available actions are Approve and Reject.

**•** The Show More link doesn’t work for Salesforce Classic users.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Prepare Your Org for Approvals

**•** If the approver has to manually select the next approver, they must log in to the full Salesforce site to complete the approval request.

**•** Users can respond only to approval requests without comments.

**•** Up to four fields only of an approval request can appear in a Slack notification.

##### Enable Approval Notifications in Slack

If your org uses both Approvals and Salesforce Digital HQ app, approval notifications are automatically
enabled in Slack. Users receive approval requests as messages on the Salesforce Digital HQ’s Messages
tab.

Note: Slack notifications are turned on automatically. Admins can turn off Slack notifications
from Setup on the Notification Delivery Settings page.

**1.** From Setup, in the Quick Find box, enter _`Notification Delivery Settings`_, and
select **Notification Delivery Settings** .

**2.** From the Approval requests dropdown menu, select **Edit** .

**3.** Select **Slack**, and enable **Salesforce Digital HQ** .

SEE ALSO:

[Salesforce for Slack](https://help.salesforce.com/s/articleView?id=sf.slack_apps_digital_hq.htm&language=en_US)

##### Where Do Slack Approval Notifications Appear?

When you have Approvals in Slack enabled, approval notifications are sent to the approver via the
Salesforce Digital HQ app as a direct message in Slack. To see the approval request post, you must
have access to Slack.

**•** Users review the request, and select **Approve** or **Reject**, or select **Show More** to be directed
to the Salesforce app to view details.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

To enable approvals in
Slack:

**•** Customize Application

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Users can continue to receive email, Lightning Experience, and mobile notifications about approval requests.


### Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals Limits and Considerations for Approvals

Before you automate something with an approval process, be aware of the limits and considerations.

Users can’t see which approval process is triggered when they click **Submit for Approval** . Familiarize
users on the criteria for each approval process and what each approval process does. If the record
doesn’t meet the entry criteria or if they’re not an allowed submitter for any approval processes,
Salesforce displays an error.

#### Approval Limits

Salesforce limits the number of approval processes in your org, as well as the number of steps
and actions in each approval process.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Considerations for Configuring Approvals
When creating or editing an approval process, keep in mind how approvals are compatible with other features. Before you start,
draw out the steps of your approval process.

Merge Fields for Approvals
Approval merge fields include _`{!ApprovalRequest.fieldName}`_ and
_`{!Approval_Requesting_User.fieldName}`_ . They’re supported in certain email templates and return different values
based on the status of the approval process instance.

Considerations for Setting Approvers
When you specify approvers for a given approval step—or for the only step if you’re using the jump start wizard—keep these
considerations in mind.

Considerations for Managing Approvals
Keep these things in mind when maintaining existing approval processes—including activating and deleting them.

Considerations for the Salesforce Mobile App
Learn about the approvals functionality in Lightning Experience on desktop that isn’t available or that works differently in the
Salesforce mobile app.

SEE ALSO:

Considerations for Email Approval Response

Considerations for Approvals in Chatter

[Approvals: What’s Different or Not Available in the Salesforce Mobile App](https://help.salesforce.com/s/articleView?id=sf.limits_mobile_sf1_approvals.htm&language=en_US)

Considerations for Approval History Reports

[Restrictions for Approval Processes in Change Sets](https://help.salesforce.com/s/articleView?id=sf.changesets_restrictions_approval_process.htm&language=en_US)

#### Approval Limits

Salesforce limits the number of approval processes in your org, as well as the number of steps and
actions in each approval process.

**Per-Org Limit** **Value**

Active approval processes 1,000

Total approval processes 2,000

Active approval processes per object 300


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

**Per-Org Limit** **Value**

Total approval processes per object 500

Steps per approval process 30

Approvers per step 25

Initial submission actions per approval process [2] 40

Final approval actions per approval process [2] 40

Final rejection actions per approval process [2] 40

Recall actions per approval process [2] 40

Maximum characters in approval request comments

#### Considerations for Configuring Approvals

4,000

In Chinese, Japanese, or Korean, the limit is 1,333 characters.

When creating or editing an approval process, keep in mind how approvals are compatible with
other features. Before you start, draw out the steps of your approval process.

Associated Object

If the approval object is a detail object in a master-detail relationship, `Owner` isn’t available for
approval page layouts or approval post templates.

Approval Criteria

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

In approval criteria—either the entry criteria or step criteria—don’t reference expressions that
resolve to random values. That way, if the criteria must be evaluated again, the record is evaluated the same every time.

Compatibility with Other Features

**•** Flows can delete records that are pending approval.

**•** Design automated actions so that you can use them for both workflow rules and approval processes.

Field Update Actions in Approvals

**•** An approval process can specify a field update action that reevaluates workflow rules for the updated object. If, however, the
reevaluated workflow rules include a cross-object field update, those cross-object field updates are ignored.

**•** Field updates that are executed as approval actions don’t trigger workflow rules or entitlement processes.

Anticipate Errors

Consider reviewing the content on approvals errors. That way, you can anticipate common issues and configure your approval process
so that the error is less likely.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Approvals in Unlocked Packages

**•** Unlocked packages can include Approvals with steps that reference related users or queues as approvers; users aren’t supported.

**•** Queues and related user fields (lookup fields) referenced by the approval steps must be included in the unlocked package.

**•** An Approval Process can only be included in unlocked packages that don’t have a specified namespace.

SEE ALSO:

What Does This Approvals Error Mean?

Set Up an Approval Process

Considerations for Automated Actions

Considerations for Chatter Post Templates for Approval Requests

#### Merge Fields for Approvals

Approval merge fields include _`{!ApprovalRequest.fieldName}`_ and
_`{!Approval_Requesting_User.fieldName}`_ . They’re supported in certain email
templates and return different values based on the status of the approval process instance.

Tip: The submitter isn’t always the current user. For custom email templates, use
_`{!Approval_Requesting_User.fieldName}`_ instead of
_`{!User.fieldName}`_ .

Where Are Approval Merge Fields Supported?

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

You can use approval process merge fields in email templates, but not mail merge templates. Except
for `{!ApprovalRequest.Comments}`, approval merge fields named `{!ApprovalRequest.field_name}` in email
templates return values only in approval assignment emails and email alerts for approval processes. When used in other emails—including
email alerts for workflow rules—the approval merge field returns `null` .

What Values Does a Merge Field Provide?

The generated value of an ApprovalRequest merge field depends on which step the approval process is in.

**•** In the approval request email, a merge field returns the submitter’s name and the name of the first step.

**•** When the request is approved, the merge field returns the most recent approver’s name and the name of the second step, if applicable.

**•** For subsequent actions, a merge field value returns the previous completed step.

**•** For an approval step that requires unanimous approval from multiple approvers, _`{!ApprovalRequest.Comments}`_ returns
only the most recently entered comment in emails.

SEE ALSO:

Default Template for Email Approval Response

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

#### Considerations for Setting Approvers

When you specify approvers for a given approval step—or for the only step if you’re using the jump
start wizard—keep these considerations in mind.

**•** Users with these permissions can respond to approval requests, even if they aren’t designated
approvers.

**–** Modify All Data

**–** Modify All for an object

**•** Make sure that the assigned approver has access to read the records for the approval requests.
For example, a user who can’t view expense records can’t view expense approval requests.

**•** Approval processes that let users select an approver manually also let users select themselves
as the approver.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** You can assign an approval request to the same user multiple times in a single step. However, Salesforce sends the user only one
request.

**•** In Lightning Experience, when an approval request has more than one assigned approvers, a `ProcessInstanceStep` is created
for each assigned approver. When the approval request has the Approval based on first response setting enabled, the values displayed
in `Assigned To` and `Actual Approver` are affected.

**–** Assigned to is set to an approver assigned to the record

**–** Actual Approver is set to the approver who approved the request

**•** Here’s what happens to the list of approvers after a record enters an approval step and the approval process later returns to that
step.

**–** If the user who responded isn’t in the designated approvers list and has either Modify All Data or Modify All permissions for the
object, that user replaces the original approver in the list of approvers.

**–** If a user who responded is in the designated approvers list, the list of approvers for that step doesn’t change. This behavior occurs
even if the field values that designate the approvers have changed.

For example, an approval process’s first step requests approval from a user’s manager. If the approval request is rejected in the second
step, the approval request returns to the first step. This table explores what happens to the list of approvers.

**•** A manager's manager is not an option for a designated approver.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Assigning Approval Steps to Queues

You can assign approval requests to a queue only if the associated object supports queues. Email approval response isn’t supported for
approval processes that assign approval to a queue.

When the assigned approver is a queue:

**•** Any queue member can approve or reject an approval request that is assigned to the queue.

**•** Approval request emails are sent to the queue email address. If the queue is set up to send email to members, approval request
emails get sent to the queue members, unless their approval user preferences are set to never receive approval request emails.

**•** Because email notifications to a queue aren’t intended for an external audience, `{!ApprovalRequest.External_URL}`
returns the equivalent internal URL.

**•** Salesforce mobile app notifications for approval requests aren’t sent to queues. For each approval step involving a queue, we
recommend adding individual users as assigned approvers, so at least those individuals can receive the approval request notifications
in the Salesforce mobile app. To have both queues and individual users as assigned approvers, select `Automatically assign`
`to approver(s)` instead of `Automatically assign to queue` in the approval step.

**•** When an approval request is rejected and returned to the previous approver and the previous approver was a queue, the approval
request is assigned to the user who approved it instead of the queue.

**•** The Approval History related list displays the queue name in the `Assigned To` column and the actual user who approved or
rejected the approval request in the `Actual Approver` column.

SEE ALSO:

Identify Assigned Approvers for an Approval Step

Limits and Considerations for Approvals

#### Considerations for Managing Approvals

Keep these things in mind when maintaining existing approval processes—including activating
and deleting them.

Admin Permissions

Users with one of these permissions are considered approval admins.

**•** Modify All object-level permission for the given object

**•** Modify All Data user permission

Approval admins can:

**•** Approve or reject pending approval requests without being part of the approval process

**•** Edit records that have been locked for approval

Activating Approval Processes

**•** An approval process must have at least one step before you can activate it.

**•** Before you activate your approval process, test it in your Salesforce sandbox.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** After an approval process is activated, you can’t add, delete, or change the order of the steps or change its reject or skip behavior,
even if the process is inactive.


Automate Your Business Processes with Salesforce Flow Limits and Considerations for Approvals

Monitoring In-Flight Approval Processes

Standard reports for approval requests are included in both the Administrative Reports folder and the Activity Reports folder.

Deploying over Existing Approval Processes

When you deploy an approval process with no entry criteria to overwrite an existing approval process with entry criteria, then the entry
criteria from the existing process are applied to the deployed process.

Deleting Approval Processes

Before you delete an approval process:

**•** Make sure it’s inactive.

**•** Delete all approval requests that are associated with it, and remove them from the Recycle Bin.

**•** Delete all records, for example, accounts that were submitted through the approval process regardless of status. By deleting the
records, the associated _`ProcessInstanceWorkitem`_ and _`ProcessInstance`_ records are also deleted automatically.

**•** If you can't delete the approval process, try again after 2 days. Salesforce can take up to 2 days to delete the files that you removed
from the recycle bin.

SEE ALSO:

Activate an Approval Process

Manage Multiple Approval Requests

Limits and Considerations for Approvals

#### Considerations for the Salesforce Mobile App

Learn about the approvals functionality in Lightning Experience on desktop that isn’t available or
that works differently in the Salesforce mobile app.

Approval Responses

You can’t unlock a record that’s locked for approval.

Salesforce Mobile App Notifications for Approval Requests

EDITIONS

Available in: Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Notifications for approval requests aren’t sent to queues or delegates. For each approval step
involving a queue, add individual users as assigned approvers, so those individuals can receive the approval request notifications in
the mobile app. To have both queues and individual users as assigned approvers, select **Automatically assign to approver(s)**
instead of **Automatically assign to queue** in the approval step.

**•** Notifications for approval requests are sent only to users who have access to the record being approved. Assigned approvers who
don’t have record access can receive email approval notifications, but they can’t complete the approval request until someone grants
record access.

Approvals in Chatter

In the Salesforce mobile app, you can’t respond to approval requests from Chatter. To respond to approval requests, go to the Approvals
navigation item.


### Automate Your Business Processes with Salesforce Flow Sample Approval Processes

Approval Comments

**•** The Salesforce mobile app prompts you for comments after you tap Approve or Reject.

**•** The Approval History related list displays truncated comments. To see the full comment for a given approval instance, tap the instance,
then tap **Comments** .

Approval History Related List

**•** The Approval History related list doesn’t include the Submit for Approval button.

**•** When working with approvals in Experience Cloud sites, role-based external users can see and take action from the Approval History
related list, but they can’t submit requests for approval.

### Sample Approval Processes

Review samples of common approval processes to help you get started creating your own.

#### Sample Approval Process: PTO Requests

Most companies require employees to file a PTO (Paid Time Off) request and have their manager approve it. In three phases, here's
how to automate a simple one-step PTO request process using Salesforce.

Sample Approval Process: Expense Reports
If your company requires that employees file expense reports for managers to approve, you can automate this process in Salesforce.

Sample Approval Process: Discounting Opportunities
Opportunities that are discounted more than 40% require a CEO approval. Use this example to create a one-step approval process.

Sample Approval Process: Job Candidates
When your company interviews candidates for a position, you can have several levels of approval before you can send an offer letter.
Use this example to create a three-step approval process that requires approval from multiple management levels.

#### Sample Approval Process: PTO Requests

Most companies require employees to file a PTO (Paid Time Off) request and have their manager
approve it. In three phases, here's how to automate a simple one-step PTO request process using
Salesforce.

Prep Your Organization

Before creating the approval process:

**•** If you don’t yet have a custom object to track your PTO requests, create a custom object and
tab called PTO Requests. Add the appropriate fields for your PTO Requests such as `Start`
`Date`, `End Date`, and `Employee Name` .

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** To notify approvers about a pending approval request, create an email template. To direct users to the approval page in Salesforce,
include approval process merge fields.

Create the Approval Process

Use the jump start wizard to create an approval process for the PTO Request custom object and specify the following:


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

Tip: To let the submitter withdraw a submitted PTO request, click **Edit** and choose **Initial Submitters** . Then select `Allow`
`submitters to recall approval requests` .

**•** Select the email template you created for this approval process.

**•** Don't specify filter criteria. That way, PTO requests are included in this approval process regardless of their attributes.

**•** Select the `Automatically assign an approver using a standard or custom hierarchy field`
option, then choose `Manager` .

**•** The jump start wizard automatically chooses the record owner as the only person who can submit PTO requests.

Wrap Things Up

**•** After you created the approval process, add the Approval History related list to the PTO Request object page layout.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Create a Custom Object](https://help.salesforce.com/s/articleView?id=sf.dev_objectcreate_task_parent.html&language=en_US)

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

Create an Approval Process with the Jump Start Wizard

Prepare Your Org for Approvals

#### Sample Approval Process: Expense Reports

If your company requires that employees file expense reports for managers to approve, you can
automate this process in Salesforce.

Use this example to create a two-step expense report approval process for all employees in your
headquarters office. It specifies that expenses less than $50 are automatically approved, expenses
$50 and over require manager approval, and expenses over $5,000 require additional approval from
two VPs. This example highlights a parallel approval process and the “else” option.

Prep Your Organization:

Before creating the approval process:

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** If you don’t yet have a custom object to track your expenses, create a custom object and tab
called Expense Reports. Add the appropriate fields such as `Amount`, `Description`, `Status`, `Start Date`, and `End`
`Date` .

**•** Create a custom field on the user object `Office Location` . Assign the “HQ” value to users in the headquarters office location.

Create the Approval Process:

Create an approval process using the Expense Report custom object and specify the following:

**•** The filter criteria for this approval process is _`Current User: Office Location equals HQ`_ . Records must meet this
criteria before they can be submitted to this approval process.

**•** Choose the `Manager` field as the next automated approver.

**•** To notify approvers that their approval is requested, create an email template. To direct users to the approval page in Salesforce,
include approval process merge fields.

**•** Choose the record owner or any other user who you want to be able to submit expense reports.


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

**•** Create these approval steps.

**1.** Create a step named _`Step 1: Manager Approval`_ with these specifications:

**–** Name this step _`Step 1: Manager Approval`_ .

**–** Select `Enter this step if the following` and choose **criteria are met** . Also, choose **approve record** for
the `else` option.

**–** Set the filter criteria to: _`Expense: Amount greater or equal 50`_ .

**–** In the `Automatically assign to approver(s)` option, select the manager of the user submitting the request.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**2.** Create an approval step named _`Step 2: Multiple VP Approval`_ and specify these attributes.

**–** Use the filter criteria _`Expense Amount greater or equal 5000`_ .

**–** Choose `Automatically assign to approver(s)` and select two users with a VP role.

**–** Select the `Require UNANIMOUS approval from all selected approvers` option. The request isn’t
approved unless both designated users approve.

**–** If appropriate, choose `The approver's delegate may also approve this request` if you want to
allow the user in the `Delegated Approver` field to approve requests.

**–** Choose `Perform ONLY the rejection actions for this step...` so that the request returns to the
manager for changes if one of the VPs rejects the request.

Tip: Consider creating these final approval actions:

**•** Define a field update to automatically change the `Status` field to “Approved.”

**•** Send an approval notification to the user who submitted the expense report.

**•** To print a reimbursement check, send an outbound message to your back-office financial system.

Wrap Things Up:

**•** After you created the approval process, add the Approval History related list to the Expense Report object page layout.

**•** Consider adding the Items To Approved related list to your custom home page layouts. The related list shows users all approval
requests that are waiting for their response.

**•** If you have a sandbox, test the approval process, then activate it.

SEE ALSO:

[Create a Custom Object](https://help.salesforce.com/s/articleView?id=sf.dev_objectcreate_task_parent.html&language=en_US)

[Email Templates in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.admin_emailtemplates.htm&language=en_US)

[Create Custom Fields](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&language=en_US)

Set Up an Approval Process

Prepare Your Org for Approvals


Automate Your Business Processes with Salesforce Flow Sample Approval Processes

#### Sample Approval Process: Discounting Opportunities

