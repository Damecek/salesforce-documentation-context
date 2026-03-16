Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later. An exchange order is an OrderSummary
object whose SourceProcess property is set to Exchange. An original order summary can have an exchange order, which in turn can
have yet another exchange order, and so on. The OrderSummaryRelationship object maintains this relationship between OrderSummary
objects.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssociatedOrderItemInventory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls whether the inventory of the associated order item is included in the inventory of
the main order item.

Possible values are:

**•** `IncludedInMainInventory` —Included in Main Inventory

**•** `NotIncludedInMainInventory` —Not Included in Main Inventory


Standard Objects OrderItemSummaryRelationship

**Field** **Details**

```
AssociatedOrderItemSumPricing

AssociatedOrderItemSummaryId

AssociatedOrderItemSummaryRole

AssociatedQuanScaleMethod

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
An enum that describes how the related order item summary is priced relative to the primary
order item summary.

Possible values are:

**•** `IncludedInBundlePrice` —Included in Bundle Price

**•** `NotIncludedInBundlePrice` —Not Included in Bundle Price

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related order item summary of this order item summary relationship. For bundle
relationships, this denotes the ID of the child order item summary.

This field is a relationship field.

**Relationship Name**
AssociatedOrderItemSummary

**Refers To**
OrderItemSummary

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the associated order item summary of this relationship.

Possible values are:

**•** `AddOnComponent` —Addon Component

**•** `BundleComponent` —Bundle Component

**•** `ClassificationComponent` —Product Classification Component

**•** `SetComponent` —Set Component

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects OrderItemSummaryRelationship

**Field** **Details**

**Description**
An enum that describes how to scale the quantity of the associated order item summary
relative to the main order item summary.

Possible values are:

**•** `Constant`

**•** `Proportional`

The default value is `Proportional` .

```
CurrencyIsoCode

MainOrderItemSummaryId

MainOrderItemSummaryRole

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency of the OrderSummary.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The primary order item summary ID of this order item summary relationship.

This field is a relationship field.

**Relationship Name**
MainOrderItemSummary

**Relationship Type**
Master-detail

**Refers To**
OrderItemSummary (the master object)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the primary order item summary of this relationship.

Possible values are:

**•** `AddOn` —Addon Parent


Standard Objects OrderItemSummaryRelationship

**Field** **Details**

**•** `Bundle` —Bundle Parent

**•** `Set` —Set Parent

```
MainOrderSummaryId

Name

OrderItemRelationshipId

ProductRelatedComponentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the main order item summary.

This field is a relationship field.

**Relationship Name**
MainOrderSummary

**Refers To**
OrderSummary

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order summary ID of the order item summary.

This field is a relationship field.

**Relationship Name**
OrderItemRelationship

**Refers To**
OrderItemRelationship

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The lookup ID from the product related component.

This field is a relationship field.


### Standard Objects OrderItemTaxLineItem

**Field** **Details**

**Relationship Name**
ProductRelatedComponent

**Refers To**
ProductRelatedComponent

```
ProductRelationshipTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lookup from the product relationship type.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Refers To**
ProductRelationshipType

### OrderItemTaxLineItem

The tax amount that has been applied to an order item. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

Fields

**Field** **Details**

```
Amount

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update


Standard Objects OrderItemTaxLineItem

**Field** **Details**

**Description**
The total amount of the tax line. The value is rounded to the nearest possible amount
associated with the currency of the order item.

```
CalculationReferenceNumber

Description

Name

OrderId

OrderItemAdjustmentLineItemId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider, such as Stripe, in the tax calculation API
response.

This field is available in API version 62.0.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add a custom description to the record to provide additional detail.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the tax line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the parent order for the order item related to the tax line

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order item adjustment line item that the tax line applies to.


Standard Objects OrderItemTaxLineItem

**Field** **Details**

```
OrderItemId

Rate

ReferenceNumber

RelatedTaxLineItemId

TaxEffectiveDate

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order item that the tax line applies to.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage value of the tax. Null if the tax is a flat amount.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider (like Stripe) for each line item in the tax
calculation API call. Use this unique ID to revert taxes during cancellation or return of an
order.

This field is available in API version 62.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The original order item tax line. Useful for reference in change order scenarios.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date used to calculate the effective tax rate. This field may require an update to
accommodate different buyer time zones.

**Type**
picklist


### Standard Objects OrderItemTaxLineItemSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows whether the amount on the tax line is an estimate or the final calculated amount.
Doesn’t set a value by default. Users can define automation to set and change the value as
needed.

Possible values are:

**•** `Actual`

**•** `Estimated`

### OrderItemTaxLineItemSummary

Represents the current tax on an OrderItemSummary or OrderItemAdjustmentLineSummary. Corresponds to one or more order item
tax line items, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and
later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Amount

CalculationReferenceNumber

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of tax represented by the OrderItemTaxLineItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string


Standard Objects OrderItemTaxLineItemSummary

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider, such as Stripe, in the tax calculation API
response.

```
CurrencyIsoCode

Description

Name

OrderItemAdjustmentLine

SummaryId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderItemTaxLineItemSummary. The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
Description of the OrderItemTaxLineItemSummary.

This field can be edited.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderItemTaxLineItemSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects OrderItemTaxLineItemSummary

**Field** **Details**

**Description**
If this object represents tax on an adjustment, this value is the ID of the
OrderItemAdjustmentLineSummary to which the tax applies. If this value is null, the
adjustment applies to an OrderItemSummary.

```
OrderItemSummaryId

OrderSummaryId

OriginalOrderItemTax

LineItemId

Rate

ReferenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
If this object represents tax on an OrderItemSummary, this value is the ID of that
OrderItemSummary. If this object represents tax on an adjustment, this value is the ID of the
OrderItemSummary to which the adjustment applies.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary that the associated OrderItemSummary or
OrderItemAdjustmentLineSummary belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original order item tax line item associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Tax rate used to calculate the Amount.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string


Standard Objects OrderItemTaxLineItemSummary

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Reference number provided by the tax provider (like Stripe) for each line item in the**
**tax calculation API call. Use this unique ID to revert taxes during cancellation or return**
**of an order.**

```
TaxEffectiveDate

TransactionReferenceNumber

Type

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**

**Reference number provided by the tax provider, such as Stripe, in the tax transaction**
**commit API request.**

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the Amount is actual or estimated.

Possible values are:

**•** `Actual`

**•** `Estimated`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


### Standard Objects OrderItemType

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemTaxLineItemSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

FulfillmentOrderItemTax

OrderItemAdjustmentLineSummary

OrderItemSummary

OrderItemTaxLineItem

### OrderItemType

Shows whether the order product is a product line or charge line. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsDefault

MasterLabel

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default order item type status value `(true)` or not `(false)`
in the picklist.

**Type**
string


### Standard Objects OrderOwnerSharingRule

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this order item type status value. This display value is the internal label that
doesn’t get translated.

```
SortOrder

TypeCode

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the order item status picklist. These numbers aren’t
guaranteed to be sequential, as some previous contract status values might have been
deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Code indicating the type of order item.

Possible values are:

**•** `Charge` —API Name DeliveryCharge.

**•** `Product` —For API Name Product.

### OrderOwnerSharingRule

Represents a rule which determines order sharing access for the order’s owners.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal users can't access this object.


Standard Objects OrderOwnerSharingRule

Fields

**Field** **Details**

```
CreatedById

CreatedDate

Description

DeveloperName

GroupId

Id

```

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the creator of the order owner sharing rule.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the order owner sharing rule was created.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the order owner sharing rule. Maximum length is 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the developer of the order owner sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group whose orders are shared.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort


Standard Objects OrderOwnerSharingRule

**Field** **Details**

**Description**
ID of the order owner sharing rule.

```
LastModifiedById

LastModifiedDate

Name

OrderAccessLevel

SystemModstamp

UserOrGroupId

```

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the user who last modified the order owner sharing rule.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the order owner sharing rule was last modified.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Name of the order owner sharing rule. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Access level for the order owner sharing rule.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
System modification time for the order owner sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects OrderPaymentSummary

**Field** **Details**

**Description**
ID of the user or group with whom order access is shared.

Usage

Use this object to manage the sharing rules for orders. For example, the following code creates an order owner sharing rule between
two public groups, which can also contain portal users.

```
   OrderOwnerSharingRule rule = new OrderOwnerSharingRule();

   rule.setName("RuleName"); // Set the sharing rule name

   rule.setDeveloperName("RuleDeveloperName"); // Set the sharing rule developer name

   rule.setGroupId("00Gx00000000000"); // Set the group of users to share records from

   rule.setUserOrGroupId("00Gx00000000001"); // Set the group of users to share records to

   rule.setOrderAccessLevel("Edit");

   connection.create(rule);

```

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### OrderPaymentSummary

Represents the current properties and state of payments using a single payment method that are applied to one OrderSummary. This
object is available in API version 48.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Unlike most summary objects, an OrderPaymentSummary isn’t related to a similarly named order payment object. Instead, it combines
values from multiple payment objects that use the same payment method and apply to the same OrderSummary.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects OrderPaymentSummary

Fields

**Field** **Details**

```
AuthorizationAmount

AuthorizationReversal

Amount

AvailableToCaptureAmount

AvailableToRefundAmount

BalanceAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been authorized.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the AuthorizationAmount that has been reversed.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s available to be captured. Equal to
AuthorizationAmount minus (CapturedAmount and PendingCaptureAmount and
AuthorizationReversalAmount and PendingReverseAuthAmount). However, if the calculated
amount is a negative number, this value is 0.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s available to be refunded. Equal to
CapturedAmount plus PendingCaptureAmount minus (RefundedAmount and
PendingRefundAmount). However, if the calculated amount is a negative number, this value
is 0.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total balance of all payments associated with this summary object.


Standard Objects OrderPaymentSummary

**Field** **Details**

```
CapturedAmount

CurrencyIsoCode

FullName

LastPaymentGatewayLogId

LastPaymentGateway

Message

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been captured.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the OrderPaymentSummary. Order
Management APIs and actions that create an OrderPaymentSummary for an OrderSummary
set this value. The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The full name of the payment method user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the most recent payment gateway log associated with the OrderPaymentSummary.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects OrderPaymentSummary

**Field** **Details**

**Description**
The most recent message received from the payment gateway associated with the
OrderPaymentSummary.

```
LastReferencedDate

LastViewedDate

Method

OrderSummaryId

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed a record related to this record.

This field is available in API version 49.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record. A null value can mean that this
record was only referenced (LastReferencedDate) and not viewed.

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderPaymentSummary.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderPaymentSummary.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OrderPaymentSummary

**Field** **Details**

**Description**
ID of the user who currently owns this OrderPaymentSummary. Default value is the user
logged in to the API to perform the create.

```
PaymentCreditedAmount

PaymentMethodId

PendingAuthorization

Amount

PendingCaptureAmount

PendingRefundAmount

PendingReverseAuth

Amount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of credit associated with this OrderPaymentSummary.

This field is available in API version 65.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the payment method associated with this OrderPaymentSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending authorization.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending capture.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending refund.

**Type**
currency


Standard Objects OrderPaymentSummary

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the AuthorizationAmount that’s pending reversal.

```
 RefundedAmount

ReservedBalanceTotalAmount

 Type

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that was refunded.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field that summarizes the ReservedBalanceAmount for all
OrderPaymentSummaryReferences for the OrderPaymentSummary.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The payment method type associated with the OrderPaymentSummary. For example, `visa`,
`mastercard`, `check`, or `giftcard` .

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**OrderPaymentSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

**OrderPaymentSummaryFeed**

Feed tracking is available for the object.

**OrderPaymentSummaryOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects OrderPaymentSummaryReference

**OrderPaymentSummaryShare**

Sharing is available for the object.

SEE ALSO:

OrderSummary

Payment

PaymentAuthorization

PaymentMethod

### OrderPaymentSummaryReference OrderPaymentSummaryReference is a junction object that allows an order payment summary to be shared with another order summary.

This object is available in API version 60.0 and later.

An order summary can share an order payment summary with any of its child order summaries (exchange order summaries). Each child
can share the order payment summary with its children, and so on. Conceptually, the original order summary and its children form a
tree structure, with the original order summary as the root node. If a new order payment summary is created for an exchange order
summary anywhere in the tree, the new order payment summary can only be shared with that exchange order summary’s children (and
their descendents), if any.

The purpose of the OrderPaymentSummaryReference object is to establish how order summaries share order payment summaries. This
is only possible if the relationship between the two order summaries has already been established. A corresponding
OrderSummaryRelationship record must already exist that relates a parent order summary ( `MainOrderSummary` ) with its child
( `AssociateOrderSummary` ). The record’s `AssociatedRelationshipType` field must be set to Exchange.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AuthorizationAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been authorized.


Standard Objects OrderPaymentSummaryReference

**Field** **Details**

```
CapturedAmount

CurrencyIsoCode

LastReferencedDate

LastViewedDate

Method

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been captured.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the OrderPaymentSummary. Order
Management APIs and actions that create an OrderPaymentSummary for an OrderSummary
set this value. The default value is USD.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed a record related to this record.

This field is available in API version 49.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record. A null value can mean that this
record was only referenced (LastReferencedDate) and not viewed.

This field is available in API version 49.0 and later.

**Type**
string


Standard Objects OrderPaymentSummaryReference

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderPaymentSummary.

```
OrderPaymentSummaryId

OrderSummaryId

RefundedAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the OrderPaymentSummary shared with the OrderSummary (exchange order).

This field is a relationship field.

**Relationship Name**
OrderPaymentSummary

**Relationship Type**
Lookup

**Refers To**
OrderPaymentSummary

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the OrderSummary (exchange order) that the OrderPaymentSummary is shared with.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that was refunded.


### Standard Objects OrderShare

**Field** **Details**

```
ReservedBalanceAmount

ReservedBalanceTotalAmount

Type

### OrderShare

```

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Reserved balance amount for the exchange order for the order payment summary relationship.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Summary of all the ReservedBalanceAmount for all the order payment summary references.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of reference between the OrderSummary and the OrderPaymentSummary.

Possible values are:

**•** `Shared`

Represents a sharing entry on an Order. This object is available in API version 48.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects OrderShare

Fields

**Field** **Details**

```
OrderAccessLevel

OrderId

RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the user or group has to the order.

Possible values are:

**•** `All` —Owner. This value isn’t valid when creating, updating, or deleting records.

**•** `Edit` —Read/Write

**•** `Read` —Read Only

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects OrderStatus

**Field** **Details**

**Description**
ID of the user or group that has been given access to the order. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit orders owned by other users.

If you attempt to create a record that matches an existing record, any modified fields are updated, the system returns the existing record.

### OrderStatus

Represents the status of the order entity. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects OrderStatus

**Field** **Details**

**Description**
Indicates whether this is the default order status value `(true)` or not `(false)` in the
picklist.

```
MasterLabel

SortOrder

StatusCode

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this order status value. This display value is the internal label that doesn’t
get translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the order status picklist. These numbers aren’t guaranteed
to be sequential, as some previous contract status values might have been deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the order.

Possible values are:

**•** `Activated`

**•** `Draft`

**•** `Superseded-This value is applicable only to Revenue Cloud`

```
   Advanced users and is available in API version 64.0 and

   later.

```

This object represents a value in the order status picklist. The order status picklist provides additional information about the status of an
Order, such as its current state ( `Draft`, `Activated`, or _`Superseded`_ ). You can query these records to retrieve the set of values in
the order status picklist, and then use that information while processing Order objects to determine more information about a given
order. For example, the application could test whether a given order is activated based on its Status value and the value of the StatusCode
property in the associated OrderStatus object.


### Standard Objects OrderSummary OrderSummary

Represents the current properties and state of an order. Corresponds to one or more order objects, consisting of an original object and
any change objects applicable to it. This object is available in API version 48.0 and later.

For performance and data integrity reasons, CRUD operations on OrderSummary records don't fire Apex triggers.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AccountId

ActiveProcess

ExceptionCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account or person account associated with the OrderSummary. It represents the
shopper in the storefront.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of active process exceptions on the OrderSummary.


Standard Objects OrderSummary

**Field** **Details**

This field is available in API version 50.0 and later.

```
BillingAddress

BillingCity

BillingCountry

BillingCountryCode

BillingEmailAddress

BillingGeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Billing address associated with the OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address country.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO country code for the billing address. The default value is `US` .

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address on the billing address.

**Type**
picklist


Standard Objects OrderSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the billing address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
BillingLatitude

BillingLongitude

BillingPhoneNumber

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLongitude to specify the precise geolocation of the billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLatitude to specify the precise geolocation of the billing address. Acceptable
values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the billing address.


Standard Objects OrderSummary

**Field** **Details**

```
BillingPostalCode

BillingState

BillingStateCode

BillingStreet

BillToContactId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address state.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO state or province code for the billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address street.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the OrderSummary. It represents the shopper in the
storefront when not using person accounts.

If the `OrderLifeCycleType` field is set to UNMANAGED, then users with the Edit
Unmanaged Order Summaries or B2B Commerce Integrator user permission can modify this
field.

This field is available in API version 49.0 and later.

**Relationship Name**
BillToContact


Standard Objects OrderSummary

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
BusinessModel

ChangeOrderId

CurrencyIsoCode

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business model of the OrderSummary.

Possible values are:

**•** `B2B`

**•** `B2C`

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only with the multicurrency feature enabled. Contains the ISO code for the currency
of the original Order associated with the OrderSummary.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

**Type**
textarea


Standard Objects OrderSummary

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
Description of the OrderSummary.

This field can be edited.

```
EffectiveDate

ExternalReference

Identifier

GrandTotalAmount

IsSuspended

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date at which the order becomes effective. Label is **Order Start Date** .

This field is available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Used internally to prevent duplicate records. This value is case-sensitive.

In API version 56.0 and later, for orders ingested from B2C Commerce, this value is set to
_`B2C realm ID`_ + "_" + _`B2C instance ID`_ + "@" + _`B2C Commerce`_
_`catalog/domain ID`_ + "@" + _`B2C Commerce order number`_ .

In API version 55.0, the standard B2C Commerce integration set this value to "SFDC" + "@"
+ _`nanotime`_ + "@" + _`UUID`_ and High Scale Orders set it to the value used in later versions.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount, including adjustments and tax, of the OrderSummary.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the OrderSummary is suspended. The default value is false.

This field is available in API version 50.0 and later.


Standard Objects OrderSummary

**Field** **Details**

```
LastReferencedDate

OperationInProgress

LastViewedDate

OrderedDate

OrderLifeCycleType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Current operation.

Possible values are:

**•** `Cancellation`

**•** `None`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date of the original order associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects OrderSummary

**Field** **Details**

**Description**
Specifies whether the OrderSummary is managed by Salesforce Order Management
(MANAGED) or by an external system (UNMANAGED). An unmanaged OrderSummary is
stored in Salesforce for reference purposes.

**•** Some Order Management APIs reject input records that are associated with unmanaged
OrderSummaries.

**•** Order Management does not update financial bucket fields on some records that are
associated with unmanaged OrderSummaries.

**•** A user with the EditUnmanagedOrderSummaries or B2BCommerceIntegrator permission
can edit certain fields on objects related to unmanaged OrderSummaries that are normally
only accessible via APIs.

Possible values are:

**•** `MANAGED` —Managed

**•** `UNMANAGED` —Unmanaged

This field is available in API version 49.0 and later.

```
OrderNumber

OrderProductLineCount

OriginalOrderId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderSummary.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of unique products ordered on this Order Summary.

This field is available in API version 52.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the original order associated with this OrderSummary. Label is **Original Order** .

This field is a relationship field.

**Relationship Name**
OriginalOrder


Standard Objects OrderSummary

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Order

```
OwnerId

PoDate

PoNumber

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this OrderSummary. Default value is the ID of the user
who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Purchase order date associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Purchase order number associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


Standard Objects OrderSummary

**Field** **Details**

```
Pricebook2Id

RoutingAttempts

SalesChannelId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the pricebook associated with this OrderSummary.

This field is available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of attempts that have been made to route the order summary to inventory
locations.

This field is available in API version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the SalesChannel associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is a relationship field.

**Relationship Name**
SalesChannel

**Relationship Type**
Lookup

**Refers To**
SalesChannel


Standard Objects OrderSummary

**Field** **Details**

```
SalesStoreId

SourceProcess

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the RetailStore or WebStore associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the order process that created the OrderSummary.

Possible values are:

**•** `Exchange` The OrderSummary was created by an Exchange process

**•** `OrderOnBehalf` The OrderSummary was created by an Order on Behalf Of process

**•** `Standard` The OrderSummary was not created by an Order on Behalf Of or Exchange
process

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the order summary. Unlike the Status and Status Category fields on the order and
FulfillmentOrder objects, this field is optional.

We recommend that you use the same values in this picklist that you use in the Status picklist
for the order object.


Standard Objects OrderSummary

**Field** **Details**

```
SourceOrderSummaryId

TaxLocaleType

TotalAdjDelivery

AmtWithTax

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source order summary that’s associated with this OrderSummary.

This field is populated when the SourceProcess of this OrderSummary is an exchange process.

**Relationship Name**
SourceOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original Order associated with the OrderSummary.
Gross usually applies to taxes like value-added tax (VAT), and Net usually applies to taxes like
sales tax. Automatic taxes use currency to determine if the tax is added on top of the price
(excluded) or included in the price.

Possible values are:

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

**•** `Automatic` (displays most prices and taxes as combined or separate, based on
the currency)

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of all OrderItemSummaries of type Delivery Charge belonging to this
OrderSummary, inclusive of item-level adjustments and tax. This amount is equal to
TotalAdjustedDeliveryAmount + TotalAdjustedDeliveryTaxAmount.


Standard Objects OrderSummary

**Field** **Details**

This field is available in API version 49.0 and later.

```
TotalAdjDistAmount

TotalAdjDist

AmountWithTax

TotalAdjDistTaxAmount

TotalAdjFeeAmtWithTax

TotalAdjProduct

AmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of distributed adjustments applied to OrderItemSummaries belonging to this
OrderSummary. This amount is equal to TotalProductAdjDistAmount plus
TotalDeliveryAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of distributed adjustments applied to OrderItemSummaries belonging to this
OrderSummary, inclusive of tax. This amount is equal to TotalAdjDistAmount plus
TotalAdjDistTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of all OrderItemSummaries of type Fee belonging to this OrderSummary,
inclusive of item-level adjustments and tax. This amount is equal to TotalAdjustedFeeAmount
plus TotalAdjustedFeeTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects OrderSummary

**Field** **Details**

**Description**
Total amount of all OrderItemSummaries of type code Product belonging to this
OrderSummary, inclusive of item-level adjustments and tax. This amount is equal to
TotalAdjustedProductAmount plus TotalAdjustedProductTaxAmount.

This field is available in API version 49.0 and later.

```
TotalAdjusted

DeliveryAmount

TotalAdjusted

DeliveryTaxAmount

TotalAdjustedFeeAmount

TotalAdjusted

FeeTaxAmount

TotalAdjustedProduct

Amount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type Delivery Charge belonging to this OrderSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type Fee belonging to this OrderSummary.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedFeeAmount.

This field is available in API version 56.0 and later.

**Type**
currency


Standard Objects OrderSummary

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type code Product belonging to this OrderSummary.

```
TotalAdjustedProduct

TaxAmount

TotalAmount

TotalDeliveryAdj

DistAmount

TotalDeliveryAdj

DistAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedProductAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of all OrderItemSummaries belonging to this
OrderSummary. Equal to TotalAdjustedProductAmount plus TotalAdjustedFeeAmount plus
TotalAdjustedDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Delivery
Charge belonging to this OrderSummary. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Delivery
Charge belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalDeliveryAdjDistAmount + TotalDeliveryAdjDistTaxAmount.

This field is available in API version 49.0 and later.


Standard Objects OrderSummary

**Field** **Details**

```
TotalDeliveryAdj

DistTaxAmount

TotalDeliveryAmount

TotalDeliveryAmount

WithTax

TotalDeliveryTaxAmount

TotalFeeAdjDistAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type Delivery Charge belonging
to this OrderSummary, not including adjustments or tax.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type Delivery Charge belonging to this OrderSummary,
including tax but not including adjustments. It is equal to TotalDeliveryAmount +
TotalDeliveryTaxAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects OrderSummary

**Field** **Details**

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Fee
belonging to this OrderSummary. This value includes OrderItemAdjustmentLineSummaries
that belong to OrderAdjustmentGroupSummaries of type Header.

This field is available in API version 56.0 and later.

```
TotalFeeAdj

DistAmtWithTax

TotalFeeAdj

DistTaxAmount

TotalFeeAmount

TotalFeeAmountWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Fee
belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalFeeAdjDistAmount + TotalFeeAdjDistTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjDistAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type Fee belonging to this
OrderSummary, not including adjustments or tax.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type Fee belonging to this OrderSummary, including tax
but not including adjustments. It is equal to TotalFeeAmount + TotalFeeTaxAmount.


Standard Objects OrderSummary

**Field** **Details**

This field is available in API version 56.0 and later.

```
TotalFeeTaxAmount

TotalProductAdj

DistAmount

TotalProductAdj

DistAmtWithTax

TotalProductAdj

DistTaxAmount

TotalProductAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type code
Product belonging to this OrderSummary. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type code
Product belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalProductAdjDistAmount + TotalProductAdjDistTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects OrderSummary

**Field** **Details**

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type code Product belonging
to this OrderSummary, not including adjustments or tax.

This field is available in API version 54.0 and later.

```
 TotalProductAmount

 WithTax

 TotalProductTaxAmount

 TotalTaxAmount

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type code Product belonging to this OrderSummary,
including tax but not including adjustments. It is equal to TotalProductAmount +
TotalProductTaxAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax on all OrderItemSummaries belonging to this OrderSummary. Equal to
TotalAdjustedDeliveryTaxAmount plus TotalAdjustedFeeTaxAmount plus
TotalAdjustedProductTaxAmount.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

**OrderSummaryFeed**

Feed tracking is available for the object.


### Standard Objects OrderSummaryAdditionalInfo

**OrderSummaryOwnerSharingRule**

Sharing rules are available for the object.

**OrderSummaryShare**

Sharing is available for the object.

SEE ALSO:

FulfillmentOrder

### Order

OrderItemSummary

OrderPaymentSummary

OrderSummaryRoutingSchedule

PendingOrderSummary

SalesChannel

### OrderSummaryAdditionalInfo

Stores information related to OrderSummary including context around the order, such as inventory reservation details, order origination,
and other values that Einstein uses to perform order analysis. Only reservation details can be stored in this object. This object is available
in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentsVersion

CurrencyIsoCode

```

**Type**
text

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the adjustment algorithm that was used to create adjustments for this order

**Type**
picklist


Standard Objects OrderSummaryAdditionalInfo

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderSummaryAdditionalInfo.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
InventoryReservationExtRef

InventoryReservationIdentifier

InventoryReservationMessage

InventoryReservationState

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Holds an external reference identifier for tracking the inventory reservation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Inventory reservation identifier for the order, if available. Since this value can come from
external systems, the value type has no lookup or enforcement.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Holds any details or other relevant information that can further explain the status of the
reservation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the reservation, if available.

Possible values are:

**•** `DEFERRED`


Standard Objects OrderSummaryAdditionalInfo

**Field** **Details**

**•** `NOT_APPLICABLE`

**•** `PERMANENT`

**•** `TEMPORARY`

```
Name

OrderId

OrderSummaryId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderSummaryAdditionalInfo record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unique ID of the order associated with this record.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the associated OrderSummary to which the specific OrderSummaryAdditionalInfo
applies.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary


### Standard Objects OrderSummaryRelationship

**Field** **Details**

```
OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the ID of the user who
created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderSummaryAdditionalInfoFeed on page 55**
Feed tracking is available for the object.

**OrderSummaryAdditionalInfoOwnerSharingRule on page 65**
Sharing rules are available for the object.

**OrderSummaryAdditionalInfoShare on page 67**
Sharing is available for the object.

SEE ALSO:

### OrderSummary OrderSummaryRelationship

Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later.

An exchange order is an OrderSummary object whose `SourceProcess` property is set to Exchange. An original order summary can
have an exchange order, which in turn can have yet another exchange order, and so on. The OrderSummaryRelationship object maintains
this relationship between OrderSummary objects.


Standard Objects OrderSummaryRelationship

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AssociatedOrderSummaryId

AssociatedOrderSummaryStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated OrderSummary.

This field is a relationship field.

**Relationship Name**
AssociatedOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Status of the associated OrderSummary.

Possible values are:

**•** `Activated`

**•** `Approved`

**•** `Canceled`

**•** `Created`

**•** `Fulfilled`

**•** `Returned`

**•** `Waiting to Fulfill`

The default value is `Created` .


Standard Objects OrderSummaryRelationship

**Field** **Details**

```
AssociatedRelationshipType

CurrencyIsoCode

MainAttachedToId

MainOrderSummaryId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Relationship type of the associated OrderSummary.

Possible values are:

**•** `Exchange`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of an Order (Change Order) or a ReturnOrder that belongs to the parent OrderSummary
(whose ID is stored in the `MainOrderSummaryId` field).

This field is a polymorphic relationship field.

**Relationship Name**
MainAttachedTo

**Relationship Type**
Lookup

**Refers To**
Order, ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects OrderSummaryRoutingSchedule

**Field** **Details**

**Description**
ID of the associated OrderSummary’s parent.

This field is a relationship field.

**Relationship Name**
MainOrderSummary

**Relationship Type**
Lookup

**Refers To**
### OrderSummary

```
Name

RootOrderSummaryId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the OrderSummaryRelationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the original OrderSummary that existed before any exchange orders were created.

This field is a relationship field.

**Relationship Name**
RootOrderSummary

**Relationship Type**
Lookup

**Refers To**
### OrderSummary

### OrderSummaryRoutingSchedule

Represents an attempt to route an order summary to one or more inventory locations for fulfillment. You can use it to schedule future
attempts and to record completed attempts. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects OrderSummaryRoutingSchedule

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OrderSummaryId

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the order summary routing schedule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The order summary associated with the routing schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this order summary routing schedule. Default value is the
User logged in to the API to perform the create.


Standard Objects OrderSummaryRoutingSchedule

**Field** **Details**

```
Reason

ScheduleStatus

ScheduledDatetime

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reason for the routing attempt. You can customize this list.

The list has one default value:

**•** `Unknown`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies whether this routing attempt has already run or is scheduled to run.

Possible values are:

**•** ABANDONED

**•** COMPLETED

**•** SCHEDULED

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Identifies when this routing attempt was run or is scheduled to run. If the
`ScheduleStatus` is ABANDONED or COMPLETED, then you can’t modify this value.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**OrderSummaryRoutingScheduleOwnerSharingRule**

Sharing rules are available for the object.

**OrderSummaryRoutingScheduleShare**

Sharing is available for the object.

SEE ALSO:

OrderSummary


### Standard Objects Organization Organization

Represents key configuration information for an organization.

Executing a SOQL SELECT query returns the value of fields in this object, but no value is visible for some of the fields.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

`Address` (beta)

```
AllowsSelfServiceLogin

City

ComplianceBccEmail

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address
Compound Fields for details on compound address fields.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether the organization allows Self-Service login ( `true` )
or not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the city for the organization's address.

**Type**
email


Standard Objects Organization

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for compliance blind carbon copies. Limit: 80
characters.

```
Country

CountryCode

DailyWebToCaseCount

DailyWebToCaseLimit

DailyWebToLeadCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the country for the organization's address. Limit: 80
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the organization’s address. Enable state
and country/territory picklists to use this field. For more information,
[see Enable and Disable State and Country/Territory Picklists in](https://help.salesforce.com/s/articleView?id=xcloud.admin_state_country_picklist_enable.htm&type=5&language=en_US)
Salesforce Help.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The number of web form submissions that have been converted to
cases for the day.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The maximum number of web form submissions that can be
converted to cases per day.

**Type**
int


Standard Objects Organization

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
The number of web form submission that have been converted to
leads for the day

```
DailyWebToLeadLimit

DefaultAccountAccess

DefaultAccountAndContactAccess

```

**Type**
int

**Properties**
Filter, Nillable

**Description**
The maximum number of web form submissions that can be
converted to leads per day.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
In API version 10.0 and later, represents the default access level for
accounts, contracts, and assets. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

In versions before 10.0,
`DefaultAccountAndContactAccess` represented this
value.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Default access level for accounts, contacts, contracts, and assets.
This field is supported for backward compatibility only and is not
available in API version 10.0 or later. In version 10.0 and later, use
either `DefaultAccountAccess` or
`DefaultContactAccess` .


Standard Objects Organization

**Field** **Details**

```
DefaultCalendarAccess

DefaultCampaignAccess

DefaultCaseAccess

DefaultContactAccess

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for calendars. The possible values are listed,
followed by the user interface labels in parentheses:

**•** `HideDetails` (Hide Details)

**•** `HideDetailsInsert` (Hide Details and Add Events)

**•** `ShowDetails` (Show Details)

**•** `ShowDetailsInsert` (Show Details and Add Events)

**•** `AllowEdits` (Full Access)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for campaigns. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for cases. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ReadEditTransfer`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects Organization

**Field** **Details**

**Description**
Default access level for contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByParent`

In versions before 10.0,
`DefaultAccountAndContactAccess` represented this
value.

When `DefaultContactAccess` is set to “Controlled by
Parent,” you can’t update the `ContactAccessLevel` field.

```
DefaultLeadAccess

DefaultLocaleSidKey

DefaultOpportunityAccess

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for leads. The possible values are:

**•** `NoneRead`

**•** `Edit`

**•** `ReadEditTransfer`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Default locale SID key. For more information on picklist options, see
[Supported Number, Name, and Address Formats (ICU) in Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.admin_supported_locales.htm&language=en_US)
help.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for opportunities. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`


Standard Objects Organization

**Field** **Details**

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

```
DefaultPricebookAccess

DefaultTerritoryCaseAccess

DefaultTerritoryContactAccess

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for price books. The possible values are listed,
followed by the user interface labels in parentheses:

**•** `None` (No access)

**•** `Read` (Read only)

**•** `ReadSelect` (Use)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for cases associated with accounts in territories.
The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for contacts associated with accounts in
territories. The possible values are:

**•** `NoneRead`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

When `DefaultContactAccess` is set to “Controlled by Parent”
you can’t update this field.


Standard Objects Organization

**Field** **Details**

```
DefaultTerritoryOppAccess

Division

Fax

FiscalYearStartMonth

HomepageHtml

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for opportunities in territories.

Valid values:

**•** `NoneRead`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the division for this organization. This field is not related
to the Division object.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Fax number. Limit: 40 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number that corresponds to the month that this organization's fiscal
year starts.

**Type**
textarea

**Properties**
Nillable, Update


Standard Objects Organization

**Field** **Details**

**Description**
The Home tab custom links and company message for this
organization.

```
InstanceName

IsSandbox

LanguageLocaleKey

LastWebToCaseDate

LastWebToLeadDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. The name of the instance. Available in API version 31.0
or later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the current organization is a sandbox
( `true` ) or production ( `false` ) instance. Available in API version
31.0 or later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The same as `Language`, the two-to-five character code which
represents the language and locale ISO code. This controls the
language for labels displayed in an application.

**Type**
dateTime

**Properties**
Filter, Nillable

**Description**
The last date that a web form submission was converted to a case.

**Type**
dateTime

**Properties**
Filter, Nillable


Standard Objects Organization

**Field** **Details**

**Description**
The last date that a web form submission was converted to a lead.

```
Latitude

Longitude

MaxActionsPerRule

MaxRulesPerEntity

MonthlyPageViewsEntitlement

```

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 up
to 15 decimal places. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
int

**Properties**
Filter, Nillable

**Description**
Maximum number of actions per workflow, assignment, escalation,
and auto-response rules. This field is unavailable in version 15.0 and
later.

**Type**
int

**Properties**
Filter, Nillable

**Description**
Maximum number of rules per object, inclusive of workflow,
assignment, escalation, and auto-response rules. This field is
unavailable in version 15.0 and later.

**Type**
int


Standard Objects Organization

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views allowed for the current calendar month
for the sites in your organization. To access this field, Salesforce Sites
must be enabled for your organization.This field is generally available
in API versions 18.0 and later.

```
MonthlyPageViewsUsed

Name

NamespacePrefix

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views used in the current calendar month for
the sites in your organization. To access this field, Salesforce Sites
must be enabled for your organization. This field is generally available
in API versions 18.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of the organization.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each
Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component
in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the
namespace prefix of the org for all objects that support it, unless
an object is in an installed managed package. In that case, the
object has the namespace prefix of the installed managed
package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.


Standard Objects Organization

**Field** **Details**

**•** In orgs that are not Developer Edition orgs,
`NamespacePrefix` is set only for objects that are part of
an installed managed package. All other objects have no
namespace prefix.

```
OrganizationType

Phone

PostalCode

PreferencesEventScheduler

PreferencesRequireOpportunityProducts

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Edition of the organization, for example Enterprise Edition or
Unlimited Edition.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address of the organization. Limit: 20 characters.

**Type**
boolean

**Properties**
Update

**Description**
Indicates whether opportunities require products ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether opportunities require products ( `true` ) or not
( `false` ).


Standard Objects Organization

**Field** **Details**

```
PreferencesS1BrowserEnabled

PreferencesTerminateOldestSession

PreferencesTransactionSecurityPolicy

PrimaryContact

ReceivesAdminInfoEmails

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the Salesforce mobile web is enabled for all users
in your organization ( `true` ) or is disabled for all users ( `false` ).

This field is available in API version 29.0 or later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the oldest login session is automatically closed
when a policy specifying the maximum number of sessions is
triggered.

This field is available in API version 35.0 — 49.0. As of API version
50.0, this field is removed.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the Transaction Security feature has been enabled.

This field is available in API version 35.0 — 49.0. As of API version
50.0, this field is removed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the primary contact for the organization. Limit: 80
characters.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update


Standard Objects Organization

**Field** **Details**

**Description**
Indicates whether the organization receives administrator emails
( `true` ) or not ( `false` ).

```
ReceivesInfoEmails

SelfServiceCasePlural

SelfServiceCaseSingle

SelfServiceCaseSubmitRecordTypeId

SelfServicDefaultCaseOrigin

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the organization receives informational email
from Salesforce ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The plural version of the term used to represent the Case object in
the Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The singular version of the term used to represent the Case object
in the Self-Service portal.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the record type associated with a case submitted via the
Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The default origin of a case submitted via the Self-Service portal.


Standard Objects Organization

**Field** **Details**

```
SelfServiceEmailSenderAddress

SelfServiceEmailSenderName

SelfServiceEmailUserOnCaseCreationTemplateId

SelfServiceEnabledForResponseRules

SelfServiceFeatureConfig

```

**Type**
email

**Properties**
Filter, Nillable, Update

**Description**
The Self-Service email address from which new Self-Service user and
password email messages are sent, such as `support@acme.com` .

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The name associated with the email address in the
`SelfServiceEmailSenderAddress` field, such as `Acme`
`Customer Support` .

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when email is sent to a Self-Service
user when he or she creates a case.

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether the Self-Service portal is enabled for auto-response
rules ( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
An integer representing the active Self-Service feature configuration
for this organization.


Standard Objects Organization

**Field** **Details**

```
SelfServiceLogoutUrl

SelfServiceMaxNumSuggestions

SelfServiceNewCommentCheckedByDefault

SelfServiceNewCommentTemplateId

SelfServiceNewPassTemplateId

```

**Type**
url

**Properties**
Filter, Nillable, Update

**Description**
The Web page that displays when a Self-Service user logs out of the
Self-Service portal.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum number of suggested solutions allowed for a
Self-Service case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
If `true`, When a customer notification is automatically sent when
a new comment is added to a case.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used to send a notification to
Self-Service users when a public comment is added to one of their
cases.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when new passwords are
generated for Self-Service users.


Standard Objects Organization

**Field** **Details**

```
SelfServiceNewUserTemplateId

SelfServicePageHeight

SelfServicePageWidth

SelfServiceSelfClosedCaseStatus

SelfServiceSolutionCategoryAvailable

SelfServiceSolutionCategoryStartNodeId

```

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when new Self-Service users are
enabled.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum height in pixels of Self-Service pages.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum width in pixels of Self-Service pages.

**Type**
picklist

**Properties**
Filter, Nillable, Update

**Description**
The default status for cases closed by Self-Service users.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether solution categories are available in the Self-Service
portal ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Nillable, Update


Standard Objects Organization

**Field** **Details**

**Description**
The ID of the top-level category in the Self-Service portal.

```
SelfServiceSolutionPlural

SelfServiceSolutionSingle

SelfServiceStyleSheetUrl

SelfServiceWelcomePageConfig

SelfServiceWelcomeText

```

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The plural version of the term used to represent the Solution object
in the Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The singular version of the term used to represent the Solution object
in the Self-Service portal.

**Type**
url

**Properties**
Filter, Nillable, Update

**Description**
The public URL of your organization's Self-Service portal stylesheet.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
Integer that represents the welcome page configuration for the
Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The custom welcome message displayed at the top of the
Self-Service home page when Self-Service users log in. Limit: 32,000
characters.


Standard Objects Organization

**Field** **Details**

```
SignupCountryIsoCode

State

StateCode

Street

TrialExpirationDate

TimeZoneSidKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO country code specified by the user for a sign-up request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
State of the address of the organization. Limit: 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the organization’s address.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Street address for the organization. Limit: 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that this organization's trial license expires.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies the default time zone of the organization.


Standard Objects Organization

**Field** **Details**

```
UiSkin

UsesStartDateAsFiscalYearName

UsesWebToCase

UsesWebToLead

WebToCaseAssignedEmailTemplateId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort,
Update

**Description**
The user interface theme selected for the organization.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the calendar year when the fiscal year begins is
referred to as the year of the company's fiscal year ( `true` ) or not
( `false` ). For example, if the fiscal year begins in February 2006, a
`true` value means the fiscal year is FY2006, and a `false` value
means the fiscal year is FY2007.

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether this organization can use Web-to-Case ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether this organization can use Web-to-Lead ( `true` )
or not ( `false` ).

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when a new case is assigned to
a user via Web-to-Case.


### Standard Objects OrgDeleteRequest

**Field** **Details**

```
WebToCaseCreatedEmailTemplateId

WebToCaseDefaultCreatorId

WebToCaseDefaultOrigin

```

Usage

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when a new case is created via
Web-to-Case.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the user specified as the default creator of cases created
via Web-to-Case.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The default value for the **Case Origin** field on cases submitted via
Web-to-Case. Limit: 40 characters.

Query this object to obtain information about an organization's settings. Only one organization object exists per organization.

SEE ALSO:

Overview of Salesforce Objects and Fields

### OrgDeleteRequest

Represents a request to delete a developer edition (DE) org. This object is available in API version 42.0 and later. It is available only in
Developer and Database.com editions.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects OrgDeleteRequest

Fields

**Field Name** **Details**

```
Name

OwnerId

RequestType

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this OrgDeleteRequest object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The ID of the user who initiated the org delete request.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether you want to deactivate or reactivate the org. When you
deactivate an org, you have 30 days to change your mind and reactivate it. After
30 days, the org is locked, and you must contact Salesforce Customer Support
to reactivate it. After 60 days, the org is permanently deleted from Salesforce
servers.

Valid values:

**•** `Deactivate`

**•** `Reactivate`

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**OrgDeleteRequestOwnerSharingRule**

Sharing rules are available for the object.

**OrgDeleteRequestShare**

Sharing is available for the object.


### Standard Objects OrgEmailAddressSecurity OrgEmailAddressSecurity

Defines the assignment of a user profile to an org-wide email address. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Only authenticated users with the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
OrgWideEmailAddressId

ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of an organization-wide email address.

This field is a relationship field.

**Relationship Name**
OrgWideEmailAddress

**Relationship Type**
Lookup

**Refers To**
OrgWideEmailAddress

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The profile ID that’s allowed to use an organization-wide email address.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


### Standard Objects OrgMetric

**Field** **Details**

**Refers To**
Profile

Usage

You can use this object with OrgWideEmailAddress and Profile objects to retrieve user profiles that have access to a specific org-wide
email address. To find specific users, use the `ProfileId` field on the User object.

You can also retrieve the org-wide email addresses that a specific user can access. Note that any users assigned to those org-wide email
addresses via permission set aren’t returned.

### OrgMetric

Represents a feature or metric that Salesforce Optimizer evaluates. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,
`update()`, `upsert()`

Special Access Rules

This object is only available in orgs where Salesforce Optimizer is enabled. Requires the Modify All Data and Customize Application user
permissions.

Fields

**Field** **Details**

```
Category

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The category of the feature evaluated.

Possible values are:

**•** `Custom Code`

**•** `Custom Layouts`

**•** `Fields`

**•** `Improve Org Security`

**•** `Improve User Experience`


Standard Objects OrgMetric

**Field** **Details**

**•** `Increase User Adoption`

**•** `Object Limits`

**•** `Org Limits`

**•** `Reports And Dashboards`

**•** `Usage`

**•** `User Management`

**•** `Workflow`

The default value is `Org Limits` .

```
FeatureType

LatestOrgMetricScanSummaryId

Name

```

SEE ALSO:

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
[The feature evaluated. For a full list, see Features Evaluated in Salesforce Optimizer.](https://help.salesforce.com/s/articleView?id=xcloud.optimizer_included_features.htm&type=5&language=en_US)

The default value is `Unassigned Page Layouts` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The feature’s `OrgMetricScanSummaryID` from the most recent Optimizer evaluation.

This field is a relationship field.

**Relationship Name**
LatestOrgMetricScanSummary

**Refers To**

OrgMetricScanSummary on page 3907

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A unique number that identifies the feature.

_Salesforce Help_ [: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=xcloud.optimizer_introduction.htm&type=5&language=en_US)


### Standard Objects OrgMetricScanResult OrgMetricScanResult

Represents data or an item associated with a feature’s results in a Salesforce Optimizer evaluation. For example, for the Custom Field
Limit feature, an OrgMetricScanResult object represents an object flagged for approaching the custom field limit. This object is available
in API version 47.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `upsert()`

Special Access Rules

This object is only available in orgs where Salesforce Optimizer is enabled. Requires the Modify All Data and Customize Application user
permissions.

Fields

**Field** **Details**

```
Date

Flags

ItemStatus

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date associated with an item in a feature’s Optimizer evaluation.

**Example**
For the Unsupported Browsers feature, `Date` indicates the date that the user last logged
in with an unsupported browser.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The flags associated with an item in a feature’s Optimizer evaluation.

**Example**
For the API Versions feature, `Flags` indicates the API version of an object that Optimizer
evaluates as outdated.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects OrgMetricScanResult

**Field** **Details**

**Description**
The recommended action for an item in a feature’s Optimizer evaluation.

Possible values are:

**•** `Action Required`

**•** `Immediate Action Required`

**•** `No Action Required`

**•** `Not Currently Enabled`

**•** `Review Required`

**•** `Unable to Analyze`

The default value is `No Action Required` .

```
Name

Object

OrgMetricScanSummaryId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the item in a feature’s Optimizer evaluation, such as an object name.

**Example**
For the Unassigned Roles feature, `Name` refers to the name of the unassigned role.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The object ID associated with the item in a feature’s Optimizer evaluation.

For the Release Update feature only, `Object` indicates the release that the update is
scheduled for.

**Example**
For the Unused Reports feature, `Object` refers to the ID of the unused report.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The feature’s OrgMetricScanSummary ID from the most recent Optimizer run.

This field is a relationship field.

**Relationship Name**
OrgMetricScanSummary


Standard Objects OrgMetricScanResult

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**

OrgMetricScanSummary on page 3907 (the master object)

```
Profile

Quantity

Type

Url

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The profile ID associated with the item in a feature’s Optimizer evaluation.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A quantity associated with the item in a feature’s Optimizer evaluation.

**Example**
For the Custom Field Limits feature, `Quantity` indicates the total number of fields on an
object that approaches the custom field limit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The type of item or data in a feature’s Optimizer evaluation.

**Example**
For the Unsupported Browsers feature, `Type` indicates the unsupported browser and
platform used.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL associated with the item in a feature’s Optimizer evaluation.

**Example**
For the Unassigned Page Layouts feature, the `URL` represents a link to the unassigned layout.


### Standard Objects OrgMetricScanSummary

**Field** **Details**

```
User

```

SEE ALSO:

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The user ID or username associated with the item in a feature’s Optimizer evaluation. For
the Release Update feature only, `User` indicates the name of the release update that requires
review.

**Example**
For the User Logins feature, `User` indicates the username of a user who hasn’t recently
logged in.

_Salesforce Help_ [: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=xcloud.optimizer_introduction.htm&type=5&language=en_US)

### OrgMetricScanSummary

Represents the results summary for a specific feature in a Salesforce Optimizer evaluation. This object is available in API version 47.0 and
later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `upsert()`

Special Access Rules

This object is only available in orgs where Salesforce Optimizer is enabled. Requires the Modify All Data and Customize Application user
permissions.

Fields

**Field** **Details**

```
ErrorMessage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The message returned if an error occurred during the most recent Optimizer evaluation.


Standard Objects OrgMetricScanSummary

**Field** **Details**

```
FeatureLimit

ImplementationEffort

ItemCount

Name

OrgMetricId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The numerical limit of a feature.

**Example**
For the Custom Field Limits feature, `FeatureLimit` is `500` for Developer Edition orgs.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The estimated time needed to complete the recommended actions for the feature.

Possible values are:

**•** `1 - 2 hours`

**•** `30 - 60 minutes`

**•** `< 30 minutes`

**•** `> 2 hours`

The default value is `30 minutes` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of issues found for the feature. Corresponds to the number of
`OrgMetricScanResult` objects generated for the feature in an Optimizer evaluation.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A number that identifies the feature’s results summary.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects OrgMetricScanSummary

**Field** **Details**

**Description**
The OrgMetric ID that represents the feature analyzed in the Optimizer evaluation.

This field is a relationship field.

**Relationship Name**
OrgMetric

**Relationship Type**
Master-detail

**Refers To**

OrgMetric on page 3902 (the master object)

```
PercentUsage

ScanDate

Status

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort

**Description**
A percentage associated with a feature.

**Example**
For the Incomplete Chatter Profiles feature, the `PercentUsage` value is `100` if 100% of
users have complete Chatter profiles.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time that the report for the Optimizer evaluation was generated.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The recommended action for the feature.

Possible values are:

**•** `Action Required`

**•** `Immediate Action Required`

**•** `No Action Required`

**•** `Not Currently Enabled`

**•** `Review Required`

**•** `Unable to Analyze`


### Standard Objects OrgSnapshot

**Field** **Details**

The default value is `No Action Required` .

```
Unit

```

SEE ALSO:

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unit of measurement used in the feature’s results summary.

**Example**
For the Data Storage feature, the `Unit` is `MB` .

_Salesforce Help_ [: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=xcloud.optimizer_introduction.htm&type=5&language=en_US)

### OrgSnapshot

Represents a snapshot of a scratch org. Snapshots capture the state of a scratch org so that you can use it to quickly spin up new scratch
orgs using its configuration. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

A snapshot must belong to the Dev Hub org that you’re using to create the scratch org. You must enable the scratch org snapshot
feature in your Dev Hub org using Setup.

Fields

**Field** **Details**

```
Content

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.


Standard Objects OrgSnapshot

**Field** **Details**

```
Description

Error

ExpirationDate

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A free-form text field (maximum 255 characters) for you to enter a description of this scratch
org snapshot.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org snapshot expires.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OrgSnapshot

**Field** **Details**

**Description**
The ID of the user who owns the scratch org snapshot.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Provider

ProviderSnapshot

ProviderSnapshotVersion

SnapshotName

SourceOrg

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the scratch org snapshot. This field value is unique within your org.

**Type**
string


### Standard Objects OrgWideEmailAddress

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The org ID of the scratch org that the snapshot was created from.

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the snapshot.

Possible values are:

**•** `Active` —The snapshot is created and can be used to create scratch orgs.

**•** `Error` —The snapshot couldn’t be created.

**•** `Expired` —The snapshot has expired.

**•** `In Progress` —The snapshot is in the process of being created.

**•** `New` —The snapshot creation request has been received.

The default value is `New` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrgSnapshotFeed on page 55**
Feed tracking is available for the object.

**OrgSnapshotHistory on page 63**
History is available for tracked fields of the object.

**OrgSnapshotShare on page 67**
Sharing is available for the object.

### OrgWideEmailAddress

Represents an organization-wide email address for user profiles.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects OrgWideEmailAddress

Special Access Rules

Only authenticated users with the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
Address

DisplayName

IsAllowAllProfiles

IsVerified

```

**Type**
email

**Properties**
Create, Filter, Sort, Update

**Description**
An email alias that can be used by users of your org.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The name used to identify the sender of the email.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, any user profile in your organization can use this object. If `false`, only specified
user profiles can use this object when sending email. If you do not have the appropriate user
profile, you can’t use this object.

The default value is `false.` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email address has been verified by its owner.

The default value is false.

This field is available in API version 58.0 and later.

**Purpose**
Picklist

Possible values are DefaultNoreply, UserSelection, UserSelectionAndDefaultNoReply


### Standard Objects OSAsyncChgCompletedEvent

**Field** **Details**

```
Purpose

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how an email address can be used. `UserSelection` allows users with the
correct profile to select the address as the From address for an email.

Possible values are `DefaultNoreply`, `UserSelection`,
`UserSelectionAndDefaultNoReply` .

This object represents an email alias to use as the From address for an email, which can be selected by users with a user profile. You can
pass in the OrgWideEmailAddress ID when calling `[sendEmail()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_sendemail.htm)` for a SingleEmailMessage.

### OSAsyncChgCompletedEvent

An event that allows the processing of the credit memo, invoices, and other entities after a bulk action has successfully completed. The
event provides all of the values that would exist on the synchronous APIs. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `describeSObjects()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
ActionType

```

**Type**
string

**Properties**
Create, Nillable

**Description**
The type of the action that gets applied to Order Summary

Possible values are:

**•** CANCEL_ALL


Standard Objects OSAsyncChgCompletedEvent

**Field** **Details**

**•** RETURN_ALL

```
AsyncOperationLogId

CurrencyIsoCode

EventUuid

FeeChangeOrderId

```

**Type**
reference

**Properties**
Create, Nillable

**Description**
The ID of the AsyncOperationLog.

This field is a relationship field.

**Relationship Name**
AsyncOperationLog

**Refers To**
AsyncOperationLog

**Type**
string

**Properties**
Create, Nillable

**Description**
The ISO code for the currency of the OrderSummary that's associated with the
FulfillmentOrder. This field is available only for orgs with multicurrencies enabled.

Possible values are:

**•** `CNY` —Chinese Yuan

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Nillable

**Description**
Uniquely identifies an event message. The ID used to match the events that are returned in
the callback result with the events in the publish call.

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for the fee ID. This order usually used for invoices.


Standard Objects OSAsyncChgCompletedEvent

**Field** **Details**

This field is a relationship field.

**Relationship Name**
FeeChangeOrder

**Refers To**
Order

```
GrandTotalAmount

InFulfillmentChangeOrderId

OrderSummaryId

PostFulfillmentChangeOrderId

```

**Type**
double

**Properties**
Create, Nillable

**Description**
The new order summary's grand total.

This amount is equal to TotalAmount + TotalTaxAmount.

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for any items during fulfillment.

This field is a relationship field.

**Relationship Name**
InFulfillmentChangeOrder

**Refers To**
Order

**Type**
reference

**Properties**
Create, Nillable

**Description**
The foreign key for the master Order Summary entity.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Refers To**
OrderSummary

**Type**
reference


Standard Objects OSAsyncChgCompletedEvent

**Field** **Details**

**Properties**
Create, Nillable

**Description**
The change order for any items post-fulfillment. This ID is used for credit memos refunds

This field is a relationship field.

**Relationship Name**
PostFulfillmentChangeOrder

**Refers To**
Order

```
PreFulfillmentChangeOrderId

TotalAdjDistAmount

TotalAdjDistTaxAmount

TotalAdjustedDeliveryAmount

```

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for any items that haven't been fulfilled.

This field is a relationship field.

**Relationship Name**
PreFulfillmentChangeOrder

**Refers To**
Order

**Type**
double

**Properties**
Create, Nillable

**Description**
The total distributed adjustment amount without taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total distributed adjustment taxes.

**Type**
double

**Properties**
Create, Nillable


Standard Objects OSAsyncChgCompletedEvent

**Field** **Details**

**Description**
The total delivery adjusted amount without taxes.

```
TotalAdjustedDeliveryTaxAmount

TotalAdjustedProductAmount

TotalAdjustedProductTaxAmount

TotalAmount

TotalExcessFundsAmount

TotalFeeAmount

```

**Type**
double

**Properties**
Create, Nillable

**Description**
The total delivery adjusted tax amount .

**Type**
double

**Properties**
Create, Nillable

**Description**
The total adjusted product amount without tax.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total adjusted product tax amount.

This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total amount, not including taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The amount used to determine if a refund is needed pre-fulfillment.

**Type**
double


### Standard Objects OutOfOffice

**Field** **Details**

**Properties**
Create, Nillable

**Description**
Total fee amount, not including taxes.

```
TotalFeeTaxAmount

TotalRefundableAmount

TotalRequiredFundsAmount

TotalTaxAmount

### OutOfOffice

```

**Type**
double

**Properties**
Create, Nillable

**Description**
The total fee tax amount.

**Type**
double

**Properties**
Create, Nillable

**Description**
The amount that can be refunded to the client.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total amount of required funds.

**Type**
double

**Properties**
Create, Nillable

**Description**
The combined total of all taxes.

Represents a user-set value on a profile that shows when the user intends to be out of the office. This object is available in API version
41.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `undelete()`, `upsert()`, `update()`


Standard Objects OutOfOffice

Special Access Rules

In Lightning Experience, lets users set a message next to their name in Chatter to show when they plan to be out of the office. The
message appears in Lightning Experience, Salesforce Classic, and mobile views. Messages expire automatically after their end date. You
can control whether out-of-office functionality is available to your users. Set it up in the Out of Office section in **Setup**     - **Chatter Settings** .

Only internal users can set an out-of-office message.

Fields

**Field Name** **Details**

```
EndDate

IsEnabled

Message

StartDate

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the last day a person is out of the office. After the message expires,
it goes away automatically.

**Type**

boolean

**Properties**
Create, Defaulted on create

**Description**
Indicates whether an out-of-office message can be displayed for a user. The
default value is `true` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The message portion of the out-of-office message. This text, along with start and
end dates, is appended to the user’s name in the Salesforce user interface. The
maximum length of this string is 40 characters.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the first day a person is out of the office.


### Standard Objects OutgoingEmail

**Field Name** **Details**

```
UserId

```

Usage

**•** Maximum message length is 60 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user associated with the out-of-office message.

**•** Users can set only their own out-of-office message. An admin can set an out-of-office message for any user.

**•** The out-of-office message can be set only for internal users.

### OutgoingEmail

For internal use only.

### OutgoingEmailRelation

For internal use only.

### OwnedContentDocument

Represents a file owned by a user. This object is available in version 30.0 and later.

Supported Calls

```
describeSObjects()

```

Fields

**Field Name** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the document.


Standard Objects OwnedContentDocument

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

```
ContentSize

ContentSizeLong

ContentUrl

ExternalDataSourceName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for documents smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL for links and Google Docs. This field is set only for links and Google Docs,
and is one of the fields that determine the `FileType` .

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects OwnedContentDocument

**Field Name** **Details**

**Description**
The name of the external data source in which the document is stored. This field
is set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

```
ExternalDataSourceType

FileExtension

FileType

OwnerId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, which is determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the owner of the document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects OwnerChangeOptionInfo

**Field Name** **Details**

**Refers To**
User

```
Title

### OwnerChangeOptionInfo

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Title of the document.

Represents default and optional actions that can be performed when a record’s owner is changed. Available in API version 35.0 and later,
but to query for change owner metadata, use the OwnerChangeOptionInfo object in Tooling API instead. For more information, see
### OwnerChangeOptionInfo in the Tooling API.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Use `EntityId` or `DurableId` when querying this object.

### PackageInstallEventLog PackageInstallEventLog stores details about package installation in the organization. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

```

**Type**
string


Standard Objects PackageInstallEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CpuTime

ErrorType

IsManaged

IsPush

IsReleased

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A general categorization of any error that’s encountered.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the operation is performed on a managed package.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the package was installed as a result of a push upgrade.

The default value is `false` .

**Type**
boolean


Standard Objects PackageInstallEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the operation is performed on a released package.

The default value is `false` .

```
IsSuccessful

LoginKey

OperationType

PackageName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the package was successfully installed.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of package operation.

**Possible Values**

**•** INSTALL

**•** UPGRADE

**•** EXPORT

**•** UNINSTALL

**•** VALIDATE_PACKAGE

**•** INIT_EXPORT_PKG_CONTROLLER

**Type**
string


Standard Objects PackageInstallEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the package that’s being installed.

```
RequestIdentifier

RunTime

SessionKey

Timestamp

Uri

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
string


### Standard Objects PackageLicense

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

```
UserIdentifier

### PackageLicense

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

Represents a license for an installed managed package. This object is available in API version 31.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field Name** **Details**

```
AllowedLicenses

ExpirationDate

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of users allowed to use the package.

**Type**
dateTime


Standard Objects PackageLicense

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the package license expires.

```
IsAvailableForIntegrations

IsProvisioned

NamespacePrefix

Status

UsedLicenses

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for internal use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The namespace prefix associated with the package.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the license. Possible values are: `Active`, `Expired`, `Free`, and `Trial` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of users who have a license to the package.


Standard Objects PackageLicense

Usage

Use this object to determine the number of licenses allowed and in use for a managed package installed in your organization.

The following example demonstrates the use of the API to manage licenses for a package. The example defines an Apex class that does
the following.

**•** Retrieves the PackageLicense record for the specified package (identified by its namespace prefix).

**•** Defines a function that returns a list of all users with the specified profile.

**•** Creates a UserPackageLicense record for each user with that profile, which has the effect of assigning a license for the package to
all users with that profile.

**•** Returns an error message if the number of users exceeds the number of available licenses.

```
   public class AssignPackageLicense {

      static String PACKAGE_NAMESPACE_PREFIX = 'acme_101';

      static String PROFILE_ID = '00exx000000jz1SAAQ';

      public static String exceptionText {get; set;}

      public AssignPackageLicense() {

         exceptionText = 'Initialized';

      }

     static List<User> getUsersWithProfile(){

       String userQuery = 'SELECT Id FROM User WHERE ProfileId = :PROFILE_ID';

       List<User> matchingUsers = new List<User>();

       matchingUsers = [SELECT Id FROM User WHERE ProfileId = :PROFILE_ID];

       return matchingUsers;

      }

      public static void assignLicenseByProfile() {

        //find the PackageLicense Id

        PackageLicense pl = [SELECT Id, NamespacePrefix, AllowedLicenses, UsedLicenses,

            ExpirationDate,Status FROM PackageLicense WHERE

            NamespacePrefix = :PACKAGE_NAMESPACE_PREFIX];

        System.assert(pl != null, 'PackageLicense cannot be null.');

        List<User> usersToAssignLicenses = getUsersWithProfile();

        List<UserPackageLicense> firstUPLs = new List<UserPackageLicense>();

        //create a new UserPackageLicense record for each user with the specified profile

        for (Integer i = 0; i< usersToAssignLicenses.size(); i++){

            UserPackageLicense upl = new UserPackageLicense();

            upl.PackageLicenseId = pl.Id;

            upl.UserId = usersToAssignLicenses[i].Id;

            firstUPLs.add(upl);

        }

        try {

         //bulk insert

         insert(firstUPLs);

         } catch(DmlException e) {

           for (Integer i = 0; i < e.getNumDml(); i++) {

           // process exception here

```


### Standard Objects PackagePushError

```
            System.debug(e.getDmlMessage(i));

            String status = e.getDmlStatusCode(i);

            System.debug(status + ' ' + e.getDmlMessage(i));

            if(status.equals('LICENSE_LIMIT_EXCEEDED')){

             exceptionText = 'You tried to assign more licenses than available. '

             +' You tried to create '+ firstUPLs.size()+' licenses but only have '

             + (pl.AllowedLicenses - pl.UsedLicenses) + ' licenses free.';

             System.debug(exceptionText);

            }

           }

         }

      }

    }

### PackagePushError

```

Represents an error encountered during a push request. The number of PackagePushError records created depends on the number of
push jobs in the request that result in an error.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

Fields

**Field Name** **Details**

```
ErrorDetails

ErrorMessage

```

**Type**
string

**Properties**
Nillable, Sort

**Description**
Explanation of the error.

**Type**
string


Standard Objects PackagePushError

**Field Name** **Details**

**Properties**
Nillable, Sort

**Description**
The error code that appears in the API.

```
ErrorSeverity

ErrorTitle

ErrorType

PackagePushJobId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Valid values are:

**•** Error

**•** Warning

**Type**
string

**Properties**
Nillable, Sort

**Description**
The error message title that appears in the API.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Valid values are:

**•** ApexTestFailure

**•** DeployError

**•** FeatureMissing

**•** IneligibleUpgrade

**•** LimitExceeded

**•** LockingFailure

**•** PACError

**•** UnclassifiedError

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects PackagePushJob

**Field Name** **Details**

**Description**
Required. The parent push job record ID.

Usage

Suppose that your push upgrade request wasn’t successful due to some of its jobs failing. Let’s write some code to find out what those
errors were.

This code sample uses the Web Services Connector (WSC).

```
   // Retrieves all PackagePushError objects associated with the PackagePushJob with the given

   // ID

   final String PACKAGE_PUSH_ERROR_QUERY = "Select ErrorMessage, ErrorDetails, ErrorTitle,"

   + " ErrorSeverity, ErrorType from PackagePushError where PackagePushJobId = '%s'";

   // job is a PackagePushJob instance

   QueryResult queryResult = conn.query(String.format(PACKAGE_PUSH_ERROR_QUERY, job.getId()));

   StringBuilder errorMessages = new StringBuilder();

   errorMessages.append("Errors for PackagePushJob [").append(job.getId()).append("]:")

    .append("\n");

   // There can be multiple PackagePushErrors for a given PackagePushJob

   for(SObject r : queryResult.getRecords()) {

    PackagePushError e = (PackagePushError) r;

    errorMessages.append("Title: ").append(e.getErrorTitle()).append("\n");

    errorMessages.append("Severity: ").append(e.getErrorSeverity()).append("\n");

    errorMessages.append("Type: ").append(e.getErrorType()).append("\n");

    errorMessages.append("Message: ").append(e.getErrorMessage()).append("\n");

    errorMessages.append("Details: ").append(e.getErrorDetails()).append("\n");

    errorMessages.append("\n");

   }

   String errors errorMessages.toString();

### PackagePushJob

```

Represents an individual push job for upgrading a package in an org from one version to another version. There can be multiple push
jobs created for one push request. For example, if you want to upgrade five orgs as part of one push, you have one PackagePushRequest
record and five PackagePushJob records.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects PackagePushJob

Special Access Rules

To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

Fields

**Field Name** **Details**

```
DurationSeconds

EndTime

PackagePushRequestId

StartTime

```

**Type**
int

**Properties**
Group, Nillable

**Description**
The length of time in seconds, that the push upgrade took to complete. This field
is new in API version 51.0.

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade ended, in ISO 8601 format.
This field is new in API version 51.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the parent push request record that must have been created.

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade started, in ISO 8601 format.
This field is new in API version 51.0.


Standard Objects PackagePushJob

**Field Name** **Details**

```
Status

SubscriberOrganizationKey

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the job. Valid values are:

**•** Canceled

**•** Created (default)

**•** Failed

**•** In Progress

**•** Pending

**•** Succeeded

Don’t specify this value when you create the push job. The default value of
`Created` is used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The organization key of the org where the package is upgraded. This
references `orgKey` in PackageSubscriber.

Suppose that you want to push version 3.4.6 of your package to all orgs. You’ve already identified the orgs eligible for the upgrade by
using MetadataPackageVersion and created the push request using PackagePushRequest. Now let’s write some code to create a push
job for each eligible org.

This code sample uses the Web Services Connector (WSC).

```
PackageSubscriber[] subscribers = new PackageSubscriber[];

// ... populate eligible and desired subscribers

// Create the PackagePushJob array

PackagePushJob[] jobs = new PackagePushJob[subscribers.length];

for (int i = 0; i < subscribers.length; i++) {

 // create a job for each subscriber...

 PackagePushJob job = new PackagePushJob();

 // ... associate it to the PackagePushRequest ppr...

 job.setPackagePushRequestId(ppr.getId());

 // ... and add the orgKey

```


Standard Objects PackagePushJob

```
    job.setSubscriberOrganizationKey(subscribers[i].getOrgKey());

    jobs[i] = job;

   }

   // Save the jobs

   SaveResult[] saveResults = conn.create(jobs);

   // Add the newly generated id's to the PackagePushJob objects

   for (int i = 0; i < saveResults.length; i++) {

    if (saveResults[i].isSuccess()) {

     jobs[i].setId(saveResults[i].getId());

    }

   }

```

Or, if you’re using REST API, submit a POST request to the PackagePushJob sObject endpoint, as in the following example. SOAP API is
also supported. This example returns the push job ID (starting with 0DX) that is required to query the status of the job.

```
   POST

   /services/data/v38.0/sobjects/packagepushjob/

   {

     "PackagePushRequestId" : "0DV...",

     "SubscriberOrganizationKey" : "00DR00..."

   }

```

**Checking the Status of a Push Job**

To check the job status, simply query the `Status` field. For example:

```
   SELECT Id, Status FROM PackagePushJob WHERE PackagePushRequestId ='0DV...'

```

Here’s an example in Java.

```
   // Finds the status of the PackagePushJob with the given id

   String PACKAGE_PUSH_JOB_STATUS_QUERY = "Select status from PackagePushJob where Id = '%s'";

   // job is a PackagePushJob instance

   QueryResult queryResult = conn.query(String.format(PACKAGE_PUSH_JOB_STATUS_QUERY,

   job.getId()));

   // extract the status from the QueryResult

   String status = ((PackagePushJob) queryResult.getRecords()[0]).getStatus();

   // optionally, update the PackagePushJob instance with the latest status

   job.setStatus(status);

```

You can also continuously poll the job status until the job is done. The following Java example polls the status every 10 seconds.

```
   // The set of states that indicate a PackagePushJob has completed

   final Set<String> TERMINAL_STATES = new HashSet<>();

   TERMINAL_STATES.add("Succeeded");

   TERMINAL_STATES.add("Failed");

   TERMINAL_STATES.add("Canceled");

   String status = queryJobStatus(job); // this method returns the status as retrieved in the

    previous code sample

   // If the status is not one of the completed statuses...

```


### Standard Objects PackagePushRequest

```
   while(!TERMINAL_STATES.contains(status)) {

    Thread.sleep(10 * 1000); // ... wait 10 seconds and try again

    status = queryJobStatus(job);

   }

### PackagePushRequest

```

Represents the push request for upgrading a package in one or many orgs from one version to another version.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review, and unlocked packages. To enable push upgrades for your managed package, log a support case in the Salesforce Partner](https://partners.salesforce.com/)
[Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

Fields

**Field Name** **Details**

```
DurationSeconds

EndTime

```

**Type**
int

**Properties**
Group, Nillable

**Description**
The length of time in seconds, that the push upgrade took to complete. This field
is new in API version 51.0.

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade ended, in ISO 8601 format.
This field is new in API version 51.0.


Standard Objects PackagePushRequest

**Field Name** **Details**

```
PackageVersionId

ScheduledStartTime

StartTime

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The non-beta, non-deprecated package version that the package is
being upgraded to.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (UTC) at which the push request is processed, in ISO 8601
format. Set this value to the earliest time that you want Salesforce to attempt to
start the push. As a best practice, schedule pushes at off-peak hours like 1:00 AM
Saturday. If you don’t specify a value, the push starts when the package push
request’s Status is set to `Pending` .

Note: Scheduled push upgrades begin as soon as resources are available
on the Salesforce instance, which is either at or after the start time you
specify. In certain scenarios, the push upgrade could start a few hours
after the scheduled start time.

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade actually started, in ISO 8601
format. This field is new in API version 51.0.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the push. Valid values are:

**•** Canceled

**•** Created (default)

**•** Failed

**•** In Progress

**•** Pending


Standard Objects PackagePushRequest

**Field Name** **Details**

**•** Succeeded

Don’t specify this value when you create the push request. The default value of
Created is used. Later, change the status to Pending to schedule the push upgrade.

Usage

Suppose that you want to push version 3.4.6 of your package to all orgs. You’ve already identified the orgs eligible for the upgrade by
using MetadataPackageVersion. Now let’s write some code to create a push request, which holds a push job for each eligible org.

This code sample uses the Web Services Connector (WSC).

```
   // Create a new PackagePushRequest for the versionId to upgrade to

   // (for example, versionId is the "04t..." id of version

   // 3.4.6 of the package

   PackagePushRequest ppr = new PackagePushRequest();

   ppr.setPackageVersionId(versionId);

   // Optionally, set the start time of the PackagePushRequest to schedule it to begin

   // automatically; scheduledStartTime is a java.util.Calendar instance

   ppr.setScheduledStartTime(scheduledStartTime);

   // Save the PackagePushRequest

   SaveResult[] saveResults = conn.create(new SObject[] { ppr });

   if (saveResults[0].isSuccess()) {

    // Add the newly generated Id to the object

    ppr.setId(saveResults[0].getId());

   } else {

    for (Error error : saveResults[0].getErrors()) {

     System.out.println(error.getMessage());

    }

   }

```

Or, if you’re using REST API, submit a POST request to the PackagePushRequest sObject endpoint, as in the following example. SOAP API
is also supported.

This example returns the push request ID (starting with 0DV) that’s required to create push jobs.

```
   POST

   /services/data/v38.0/sobjects/packagepushrequest/

   {

     "PackageVersionId" : "04t...",

     "ScheduledStartTime" : "2016-08-24T21:00:00"

   }

```

As your next step, create a push job for each eligible subscriber you want to upgrade using PackagePushJob.

**Scheduling the Push Upgrade**

To signal that the push upgrade is ready to be processed, change the status of the push request to Pending. If you didn’t set a
`ScheduledStartTime`, the push upgrade starts immediately after you change the status.


Standard Objects PackagePushRequest

See the following Java example.

```
   // ppr is the PackagePushRequest instance

   ppr.setStatus("Pending");

   conn.update(new SObject[] { ppr });

```

If you’re using REST API, submit a PATCH request to the PackagePushRequest sObject endpoint, as in the following example. SOAP API
is also supported.

```
   PATCH

   /services/data/v38.0/sobjects/packagepushrequest/0DV...

   {

     "Status" : "Pending"

   }

```

**Checking the Status of a Push Request**

The PackagePushRequest status is `Succeeded` if all its associated jobs are successful; it’s `Failed` if at least one job failed.

```
   // Finds the status of the PackagePushRequest for a given Id

   final String PACKAGE_PUSH_REQUEST_STATUS_QUERY = "Select status from PackagePushRequest"

   +

    " where Id = '%s'";

   // ppr is a PackagePushRequest instance

   QueryResult queryResult = conn.query(String.format(PACKAGE_PUSH_REQUEST_STATUS_QUERY,

    ppr.getId()));

   // extract the status from the QueryResult

   String status = ((PackagePushRequest) queryResult.getRecords()[0]).getStatus();

   // optionally, update the PackagePushRequest instance with the latest status

   ppr.setStatus(status);

```

You can also check the status of a job by querying the PackagePushJob’s `Status` field.

**Aborting a Push Request**

You can abort a package push request by changing its status to Canceled.

For example, if you’re using the REST API, submit a PATCH request to the PackagePushRequest sObject endpoint.

```
   PATCH

   /services/data/v38.0/sobjects/packagepushrequest/0DV...

   {

     "Status" : "Canceled"

   }

```

The following example is for Java.

```
   // ppr is the PackagePushRequest instance

   ppr.setStatus("Canceled");

```

You can abort a package push request only if its status is Created or Pending. If the abort succeeds, all associated push jobs are also
canceled. If you try to abort when the current PackagePushRequest status is Canceled, Succeeded, Failed, or In Progress, the abort doesn’t
occur, and an error message is returned.


### Standard Objects PackageSubscriber PackageSubscriber

Represents an installation of a package in an org. This object contains installation information for managed or unlocked packages
developed in the org you’re logged in to.

One record is created per installation. For example, if 5 orgs installed 2 packages, 10 records are created.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

Fields

**Field Name** **Details**

```
CustomUpgradeType

HasRestrictionEnabled

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of push upgrade customization.

Possible values are:

**•** `BlockedBySubscriber` —Blocked By Subscriber

**•** `None`

The default value is `None` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the subscriber org has blocked push upgrades.

The default value is `false` .


Standard Objects PackageSubscriber

**Field Name** **Details**

```
InstalledStatus

InstanceName

IsCustomUpgradeAllowed

MetadataPackageId

MetadataPackageVersionId

OrgKey

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the package is installed in the org, the value is `i` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The instance that hosts the subscriber org.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the package developer has allowed a subscriber to opt into
customized push upgrades.

The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The package ID. Package Ids have a prefix of `033` . This field is available in API
version 49.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character package version ID starting with `04t` .

**Type**
string


Standard Objects PackageSubscriber

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID that represents the Salesforce org.

```
OrgName

OrgStatus

OrgType

ParentOrg

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of the org where the package is installed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Valid values are:

**•** `Active`

**•** `Demo`

**•** `Free`

**•** `Inactive`

**•** `Trial`

Orgs with an `OrgStatus` of `Inactive` can’t receive push upgrades.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Valid values are:

**•** `Production`

**•** `Sandbox`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PackageSubscriber

**Field Name** **Details**

**Description**
The production org from which a sandbox was created.

Usage

Here are examples of the types of API queries you can perform.

**Query** **String**

Get all package subscriber orgs with a specific package ID

Get all package subscriber orgs that have an installed package
created by the org you’re logged in to

**Filter PackageSubscriber Objects by Instance**

```
SELECT Id, OrgKey, OrgStatus, OrgName,

OrgType FROM PackageSubscriber WHERE

MetadataPackageVersionId = '04t...'

SELECT Id, OrgKey, OrgStatus, OrgName,

OrgType FROM PackageSubscriber WHERE

InstalledStatus = 'i'

```

If you have packages with many subscribers, querying PackageSubscriber objects can take a while. To improve query performance, add
filters to your PackageSubscriber queries, such as an `InstanceName` filter. `InstanceName` is a field that represents the instance
that the subscriber org is hosted on.

**1.** Get the org’s package and the latest released version of the package.

```
  /**

  * Get the MetadataPackage object corresponding to this org's managed package

  */

  public MetadataPackage getMetadataPackage() throws ConnectionException {

   // retrieve the managed package, which won’t have an empty namespace

  QueryResult result = conn.query("select id from MetadataPackage where namespaceprefix

   <> ''");

   return (MetadataPackage) result.getRecords()[0];

  }

  /**

  * Get the latest MetadataPackageVersion object of the given MetadataPackage

  */

  public MetadataPackageVersion getLatestMetadataPackageVersion(MetadataPackage

  metadataPackage)

  throws ConnectionException {

   // get the latest released version of the given package

   String query = "Select id, ReleaseState, MajorVersion, MinorVersion, PatchVersion,

  MetadataPackageId"

   + " From MetadataPackageVersion"

   + " Where MetadataPackageId = '%s' and ReleaseState = 'Released'"

   + " Order by majorversion desc, minorversion desc, patchversion desc";

```


Standard Objects PackageSubscriber

```
      QueryResult result = conn.query(String.format(query, metadataPackage.getId()));

      return (MetadataPackageVersion) result.getRecords()[0];

     }

```

**2.** Get eligible subscribers. The following query strings and methods are modified to allow querying for PackageSubscribers filtered by
an instance.

```
     static final String PACKAGE_SUBSCRIBER_ORG_KEY_QUERY = "Select OrgKey from

     PackageSubscribers where OrgStatus = 'Active'"

      + " and InstalledStatus = 'I'"

      + " and InstanceName = '%s'"; // placeholder for instance values

     static final String METADATA_PACKAGE_VERSION_QUERY = "Select Id, Name, ReleaseState,

     (%s) from MetadataPackageVersion"

      + " where MetadataPackageId = '%s' AND ReleaseState = 'Released'"

      + " AND (MajorVersion < %s OR (MajorVersion = %s and MinorVersion < %s)"

      + " OR (MajorVersion = %s and MinorVersion = %s and PatchVersion < %s))";

     /**

     * Get all PackageSubscribers on the given instance that are eligible to upgrade to the

      given

     * MetadataPackageVersion

     */

     public PackageSubscriber[] getEligibleSubscriberIds(MetadataPackageVersion version,

     String instanceName) throws ConnectionException {

      String allPackageId = version.getMetadataPackageId();

      Integer major = version.getMajorVersion();

      Integer minor = version.getMinorVersion();

      Integer patch = version.getPatchVersion();

      return getEligibleSubscriberIds(major, minor, patch, allPackageId, instanceName);

     }

     public PackageSubscriber[] getEligibleSubscriberIds(Integer major, Integer minor, Integer

      patch, String packageId, String instanceName) throws ConnectionException {

     String subscriberQuery = String.format(PACKAGE_SUBSCRIBER_ORG_KEY_QUERY, instanceName);

     QueryResult results = conn.query(String.format(METADATA_PACKAGE_VERSION_QUERY,

     subscriberQuery, packageId, major, major, minor, major, minor, patch));

      return Arrays.stream(results.getRecords()).map(MetadataPackageVersion.class::cast)

      .filter(mpv -> mpv.getPackageSubscribers() != null)

      .flatMap(mpv -> Arrays.stream(mpv.getPackageSubscribers().getRecords()))

      .map(PackageSubscriber.class::cast)

      .toArray(PackageSubscriber[]::new);

     }

```

**3.** Put it all together. The following code sample shows how to use the previous methods to modify the workflow to perform package
pushes by instance.

```
     String[] instances = { "NA4" }; // Here we list the instances we would like to push to

     MetadataPackage metadataPackage = api.getMetadataPackage();

     MetadataPackageVersion version = api.getLatestMetadataPackageVersion(metadataPackage);

```


### Standard Objects Participant

```
     // do pushes by instance to avoid API timeouts retrieving PackageSubscribers

     for (String instanceName : instances) {

     PackageSubscriber[] eligibleSubscribers = api.getEligibleSubscriberIds(version,

     instanceName);

     // ... proceed with creating PushRequests and PushJobs as before

### Participant

```

Represents a participant in a ConversationParticipant. An existing or new Participant is referenced each time a new ConversationParticipant
is created. This object is available in API version 57.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

### `ParticipantAppType` `ParticipantRole` `ParticipantSubject`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The type of app used by the participant, such as messaging, chatbot, live_message, agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of this participant in the conversation, such as System, Agent, Chatbot, EndUser,
Supervisor, or Router.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Partner

**Field** **Details**

**Description**
The subject of this participant in the conversation.

### Partner

Represents a partner relationship between two Account records or between an Opportunity record and an Account record.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AccountFromId

AccountToId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if `OpportunityId` is null. ID of the main account in a partner relationship
between two accounts. Specifying this field when creating a Partner record creates two
AccountPartner records, one for each direction of the relationship. If you specify the
`OpportunityId` field, you can’t specify this field as well.

This is a relationship field.

**Relationship Name**
AccountFrom

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects Partner

**Field** **Details**

**Description**
Required. ID of the Partner Account related to either an opportunity or an account. You must
specify this field when creating an Opportunity Partner or an Account Partner record.

This is a relationship field.

**Relationship Name**
AccountTo

**Relationship Type**
Lookup

**Refers To**
Account

```
IsPrimary

OpportunityId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Valid for Opportunity Partners only.

Indicates that the account is the primary partner for the opportunity. Only one account can
be marked as primary for an opportunity. If you set this field to 1 ( `true` ) upon insert of a
new opportunity partner, this field is automatically set to 0 ( `false` ) for any other primary
partners for that opportunity.

Label is **Primary** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if `AccountFromId` is null. ID of the opportunity in a partner relationship between
an account and an opportunity. Specifying this field when creating a record creates an
OpportunityPartner record. If you specify the `AccountFromId` field, you can’t also specify
this field.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity


Standard Objects Partner

**Field** **Details**

```
ReversePartnerId

Role

```

Roles

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the reciprocal Parnter record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
UserRole that the account has toward the related opportunity or account, such as consultant
or distributor.

In the Salesforce user interface, system administrators can set up the valid role values and their corresponding reverse role values in the
PartnerRole object. Each account in the relationship is assigned a `Role` (such as `Consultant` or `Distributor` ) designating
that account’s role toward the related account or opportunity.

Creating an Account-Opportunity Partner Relationship

When you create a partner relationship between an account and an opportunity (when you create a Partner record and specify the
`OpportunityId` field), the API automatically creates two OpportunityPartner records, one for the forward relationship and one for
the reverse.

**•** The value of the Partner field `AccountToId` maps to the value of the OpportunityPartner field `AccountToId` .

**•** The values of the `OpportunityId`, `Role`, and `IsPrimary` fields in both the Partner and OpportunityParnter records are the
same.

**•** If you set the `IsPrimary` value to 1 ( `true` ) upon insert of a new OpportunityPartner, the `IsPrimary` value is automatically
set to 0 ( `false` ) for any existing primary partners for that opportunity.

This mapping allows the API to manage the records and their relationships efficiently.

Creating an Account-Account Partner Relationship

When you create a partner relationship between two accounts (when you create a Partner record and specify the `AccountFromId` ),
the API automatically creates two AccountPartner records, one for the forward relationship and one for the reverse. For example, if you
create a Partner relationship with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId`, the API
automatically creates two AccountPartner records:

**•** The forward relationship AccountPartner with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId` .

**•** The reverse relationship AccountPartner with “Acme Consulting” as the `AccountFromId` and “Acme, Inc.” as the `AccountToId` .


### Standard Objects PartnerFundAllocation

**•** The value of the `Role` field in the reverse relationship AccountPartner is set to the PartnerRole record `ReverseRole` value
associated with the value of the `Role` field in the forward relationship AccountPartner.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

AccountPartner

OpportunityPartner

UserRole

PartnerRole

### PartnerFundAllocation

Represents allocated funds from a partner marketing budget for channel partners. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Amount

BudgetId

ChannelPartnerId

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of the allocation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner marketing budget.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the channel partner.


Standard Objects PartnerFundAllocation

**Field Name** **Details**

Note: The ChannelPartnerId field isn’t supported for formula fields, custom
buttons, or custom links for the PartnerFundAllocation object. This
limitation also applies to the PartnerMarketingBudget and
PartnerFundRequest objects.

```
Description

LastReferencedDate

LastViewedDate

OwnerId

Title

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the allocation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the allocation.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The title of the allocation.


### Standard Objects PartnerFundClaim

**Field Name** **Details**

```
TotalApprovedFcs

TotalApprovedFrs

TotalReimbursedFcs

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund claims.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund requests.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of reimbursed fund claims.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundAllocationFeed**

Feed tracking is available for the object.

**PartnerFundAllocationHistory**

History is available for tracked fields of the object.

**PartnerFundAllocationOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundAllocationShare**

Sharing is available for the object.

### PartnerFundClaim

Represents a claim of funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and later.

Supported Calls

```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()
```

`search()update()`, `upsert()`


Standard Objects PartnerFundClaim

Fields

**Field Name** **Details**

```
AllocationId

Amount

BudgetId

ChannelPartnerId

Description

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner fund allocation.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of the claim.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner marketing budget.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the channel partner.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the fund claim.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PartnerFundClaim

**Field Name** **Details**

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

```
LastViewedDate

OwnerId

RequestId

Status

Title

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the fund claim.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner fund request.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable Restricted picklist, Sort, Update

**Description**
Status of the fund claim. Values are:

**•** `Draft`

**•** `Approved`

**•** `Rejected`

**•** `Paid`

**Type**
string


### Standard Objects PartnerFundRequest

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the fund claim.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundClaimFeed**

Feed tracking is available for the object.

**PartnerFundClaimHistory**

History is available for tracked fields of the object.

**PartnerFundClaimOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundClaimShare**

Sharing is available for the object.

### PartnerFundRequest

Represents a request for funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and
later.

Supported Calls

`create()`, `delete()describeLayout()describeSObjects()`
`getDeleted()getUpdated()query()retrieve()search() update()`, `upsert()`

Fields

**Field Name** **Details**

```
Activity

AllocationId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Activity that is covered by the funds, for example, a trade show or seminar.

**Type**
reference


Standard Objects PartnerFundRequest

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the partner fund allocation.

```
Amount

BudgetId

ChannelPartnerId

Description

DesiredOutcome

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Approved amount of request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the partner marketing budget.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel partner.

Note: The ChannelPartnerId field isn’t supported for formula fields, custom
buttons, or custom links for the PartnerFundRequest object. This limitation
also applies to the PartnerFundAllocation and PartnerMarketingBudget
objects.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the fund request.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PartnerFundRequest

**Field Name** **Details**

**Description**
Desired outcome if requested funds are used.

```
LastReferencedDate

LastViewedDate

OwnerId

RequestedAmount

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the fund request.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of the fund request.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Restricted picklist, Sort, Update

**Description**
Status of the fund request. Values are:

**•** `Draft`

**•** `Approved`


### Standard Objects PartnerMarketingBudget

**Field Name** **Details**

**•** `Rejected`

```
Title

TotalApprovedFcs

TotalReimbursedFcs

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the fund request.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund claims.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of reimbursed fund claims.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundRequestFeed**

Feed tracking is available for the object.

**PartnerFundRequestHistory**

History is available for tracked fields of the object.

**PartnerFundRequestOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundRequestShare**

Sharing is available for the object.

### PartnerMarketingBudget

Represents a budget that provides funds to channel partners for selling and marketing products and services. This object is available in
API version 41.0 and later.


Standard Objects PartnerMarketingBudget

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Amount

ChannelPartnerId

Description

EndDate

IsIgnoreValidation

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of the budget.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the channel partner. This field is available in API version 45.0 and later.

Note: The ChannelPartnerId field isn’t supported for formula fields, custom
buttons, or custom links for the PartnerMarketingBudget object. This
limitation also applies to the PartnerFundAllocation and
PartnerFundRequest objects.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the budget.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the budget is no longer available.

**Type**
boolean


Standard Objects PartnerMarketingBudget

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When enabled, ignores restrictions related to the child objects connected to the
budget. Note that individual totals for allocation amounts, request amounts, and
claims amounts cannot exceed the total of their parent budget. Field is default
off (false) on create. Once enabled (true), this field cannot be disabled. This field
is available in API version 44.0 and later.

```
LastReferencedDate

LastViewedDate

OwnerId

StartDate

Title

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the budget.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the budget becomes available.

**Type**
string


Standard Objects PartnerMarketingBudget

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the budget.

```
TotalAllocatedAmount

TotalApprovedFcs

TotalApprovedFrs

TotalReimbursedFcs

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total funds allocated to channel partners or as a fund pool.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund claims.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund requests.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of reimbursed fund claims.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of budget. Values are:

**•** `Co-Operated Budget` —Funds accrue based on a percentage of partner
sales. The funds are available based on previous activity.


### Standard Objects PartnerNetworkConnection

**Field Name** **Details**

**•** `Marketing Funds` —Funds are issued to partners in advance of sales.
The funds are awarded based on predicted or expected behavior.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerMarketingBudgetFeed**

Feed tracking is available for the object.

**PartnerMarketingBudgetHistory**

History is available for tracked fields of the object.

**PartnerMarketingBudgetOwnerSharingRule**

Sharing rules are available for the object.

**PartnerMarketingBudgetShare**

Sharing is available for the object.

### PartnerNetworkConnection

Represents a Salesforce to Salesforce connection between Salesforce organizations.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Winter ’21 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AccountId

ConnectionName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Account associated with this connection.

**Type**
string


Standard Objects PartnerNetworkConnection

**Field** **Details**

**Properties**
Filter, idLookup, Sort

**Description**
A descriptive name for the connection. Limit: 295 characters.

```
ConnectionStatus

ConnectionType

ContactId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the Salesforce to Salesforce connection. The picklist includes the following
values:

**•** `Sent`

**•** `Received`

**•** `Pending`

**•** `Accepted`

**•** `Rejected`

**•** `Inactive`

**•** `Disconnecting`

**•** `ConnectionSuspended`

**•** `SubscribeInProgress`

**•** `UsersInitialSync`

**•** `BulkSyncMetadata`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of Salesforce to Salesforce connection. The picklist includes the following
values:

**•** `Standard`

**•** `Replication`

This field is available in API version 30.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PartnerNetworkConnection

**Field** **Details**

**Description**
ID of the Contact associated with this connection.

```
IsSyncAuditFields

IsSyncMetadata

IsSyncUsers

PrimaryContactId

ReplicationRole

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether audit fields are synced between the primary and secondary
organization in a replication connection. This field is available in API version 32.0 and
later, and is only accessible in Salesforce organizations where Organization Sync is
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether supported types of metadata are synced from the primary to the
secondary organization in a replication connection. This field is available in API version
33.0 and later, and is only accessible in Salesforce organizations where Organization
Sync is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether users with standard Salesforce user licenses are synced between
the primary and secondary organization in a replication connection. This field is
available in API version 35.0 and later, and is only accessible in Salesforce organizations
where Organization Sync is enabled.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User associated with this connection.

**Type**
picklist


### Standard Objects PartnerNetworkRecordConnection

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The role of this Salesforce organization in the replication connection. The picklist
includes the following values:

**•** `Primary`

**•** `Secondary`

This field is available in API version 30.0 and later, and is only accessible in Salesforce
organizations where Organization Sync is enabled.

```
ResponseDate

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the connection was accepted or rejected.

Represents Salesforce to Salesforce standard and replication connections. This object is referenced by all objects that have been shared
with other organizations, enabling you to determine which connections shared a record with you. If the organization does not have
Salesforce to Salesforce enabled, the PartnerNetworkConnection object is not available, and you can’t access it via the API.

SEE ALSO:

### PartnerNetworkRecordConnection PartnerNetworkRecordConnection

Represents a record shared between Salesforce organizations using Salesforce to Salesforce.

Supported Calls

`create()`, `query()`

Special Access Rules

As of Winter ’21 and later, only authenticated internal and external users can access this object.


Standard Objects PartnerNetworkRecordConnection

Fields

**Field** **Details**

```
ConnectionId

EndDate

LocalRecordId

ParentRecordId

PartnerRecordId

RelatedRecords

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. ID of the connection a record is shared with.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date that sharing of the record was stopped.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the shared record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the parent record of the shared record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shared record in the connection's organization.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort


Standard Objects PartnerNetworkRecordConnection

**Field** **Details**

**Description**
A comma-separated list of API names for child records to be shared with a parent
record.

```
SendClosedTasks

SendEmails

SendOpenTasks

StartDate

Status

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Forwards closed tasks related to the shared record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Sends an email notifying the connection's representative that you have forwarded
the record to them. Only new recipients of a record will receive a notification email.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Forwards open tasks related to the shared record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date that the shared record was accepted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the shared record. One of the following values:

**•** `Active (received)`

**•** `Active (sent)`


### Standard Objects PartnerNetworkSyncLog

**Field** **Details**

**•** `Connected`

**•** `Inactive`

**•** `Inactive (converted)`

**•** `Inactive (deleted)`

**•** `Pending (sent)`

Usage

When you create a PartnerNetworkRecordConnection, you forward a record to a connection.

Note: Attempting to forward a record from an object to which the connection is not subscribed results in an `Invalid`
`Partner Network Status` error.

When you delete a PartnerNetworkRecordConnection, you stop sharing a record with a connection.

**•** To share a record, use the following fields: `LocalRecordID` and `ConnectionId`

**•** To share a child of a parent record, use the following fields: `LocalRecordID`, `ConnectionId`, and `ParentRecordID`

**•** To share a child of a parent record and its child records, use the following fields: `LocalRecordID`, `ConnectionId`,
`ParentRecordID`, and `RelatedRecords`

If the organization does not have Salesforce to Salesforce enabled, the PartnerNetworkRecordConnection object is not available, and
you can’t access it using the API.

SEE ALSO:

PartnerNetworkConnection

### PartnerNetworkSyncLog

Represents the Org Sync Log tab in Salesforce, where Salesforce administrators can track the replication of record inserts and updates
being performed in Organization Sync. The Connection Detail page for the replication connection also displays the Org Sync Log’s twenty
most recent entries, and provides a link to the log.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

The Org Sync Log tab can only be added in organizations where Organization Sync has been enabled. To add the tab to the Salesforce
user interface, users must also have the “Manage Connections” user permission.


Standard Objects PartnerNetworkSyncLog

Fields

**Field Name** **Details**

```
ConnectionEvent

ConnectionId

Description

EntityType

Error

LocalRecord

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The action being replicated to the partner organization, such as a record insertion.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Salesforce to Salesforce replication connection in which the
replication event succeeded or failed.

**Type**
textarea

**Properties**
Nillable

**Description**
A description of the replication event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of record being inserted or updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The code used to describe the replication failure or success.

**Type**
string

**Properties**
Filter, Group, Sort


### Standard Objects PartnerRole

**Field Name** **Details**

**Description**
The record being inserted or updated.

```
Status

### PartnerRole

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
An item is added to the Organization Sync Log if it failed to be replicated to the
linked organization. This picklist includes the following values:

**•** `Failed` : The replication continued to fail after multiple retries, and won’t
be retried further.

**•** `Resolved` : The replication succeeded after retrying.

**•** `Retrying` : Salesforce is retrying the replication.

This field is available in API version 35.0 and later.

Represents a role for an account Partner, such as consultant, supplier, and so on.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or master label.


### Standard Objects PartyConsent

**Field** **Details**

```
MasterLabel

ReverseRole

SortOrder

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this partner role value. This display value is the internal label that does not
get translated. Limit: 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the reverse role that corresponds to this partner role. For example, if the role is
“subcontractor,” then the reverse role might be “general contractor.” In the user interface,
assigning a partner role to an account creates a reverse partner relationship so that both
accounts list the other as a partner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the partner role picklist. These numbers are not guaranteed
to be sequential, as some previous partner role values might have been deleted.

This object represents a value in the partner role picklist. In the user interface, the partner role picklist provides additional information
about the role of a Partner, such as their corresponding reverse role. Query this object to retrieve the set of values in the partner role
picklist, and then use that information while processing PartnerRole records to determine more information about a given partner role.
For example, the application could determine the reverse role of a given Partner `Role` value and the value of the `ReverseRole`
property in the associated PartnerRole object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### PartyConsent

Represents consent preferences for an individual. This object is available in API version 48.0 and later.


Standard Objects PartyConsent

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Action

CaptureContactPointType

CaptureDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The action that the Individual is consenting to.

Possible values are:

**•** `CrossDevice`

**•** `DataCollection`

**•** `Reidentification`

**•** `Segment`

**•** `ShareData`

**•** `Target`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Indicates how you captured consent.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when consent was captured.


Standard Objects PartyConsent

**Field** **Details**

```
CaptureSource

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the party consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects PartyConsent

**Field** **Details**

**Refers To**
Group, User

```
 PartyId

 PrivacyConsentStatus

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to associate consent
with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identifies whether the individual associated with this record agrees to this form of
contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.

**•** `Seen`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PartyConsentChangeEvent**

Change events are available for the object.


### Standard Objects Payment

**PartyConsentFeed**

Feed tracking is available for the object.

**PartyConsentHistory**

History is available for tracked fields of the object.

**PartyConsentOwnerSharingRule**

Sharing rules are available for the object.

**PartyConsentShare**

Sharing is available for the object.

### Payment

Represents a single event when a shopper makes a payment. For credit cards, this event is a payment capture or payment sale, but it
doesn't appear on the shopper's credit card statement. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Note: You can edit or delete a payment only in draft state, which you specify with the **Status** field.

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account of the customer who made the payment.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


Standard Objects Payment

**Field** **Details**

```
Amount

Balance

CancellationDate

CancellationEffectiveDate

CancellationGatewayDate

CancellationGatewayRefNumber

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The amount to be debited or captured.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount – the net applied amount.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the payment was voided.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the cancellation of this payment takes effect.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gateway provides this date following a successful cancellation request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
System-provided unique transaction ID from the payment gateway.


Standard Objects Payment

**Field** **Details**

```
CancellationGatewayResultCode

CancellationSfResultCode

ClientContext

Comments

CorporateCurrencyCvsnDate

CorporateCurrencyCvsnRate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A Salesforce result code that can be mapped to one or more gateway result codes. We
recommend that the payment gateway adapter layer maps gateway-specific codes to the
Salesforce result code.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains caller context for payment APIs. Useful for re-establishing context during an
asynchronous payment transaction.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can provide additional details about the payment record. Supports a maximum of
1000 characters.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date on which the invoice s total amount with tax was converted to the corporate
currency. Available in API version 63.0 and later.

**Type**
double


Standard Objects Payment

**Field** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The exchange rate that s used to convert the invoice s total amount with tax to the corporate
currency. Available in version 63.0 and later.

```
CorporateCurrencyISOCode

CurrencyIsoCode

Date

EffectiveDate

Email

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The currency ISO code of the corporate currency. Available in version 63.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this payment record was created.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that this payment takes effect.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the user who initiated the payment.


Standard Objects Payment

**Field** **Details**

```
GatewayDate

GatewayRefDetails

GatewayRefNumber

GatewayResultCode

GatewayResultCodeDescription

ImpactAmount

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gateway provides this date for reference following a successful gateway communication.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional data that can’t be stored in other fields on the payment record. You can use this
field for transactions following the initial transaction that creates the payment record. You
can use any data that isn’t normalized in financial entities. This field has a maximum length
of 1000 characters and can store data as JSON or XML.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code that must map to a Salesforce-specific result code. One Salesforce
result code can map to multiple gateway result codes.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code.

**Type**
currency


Standard Objects Payment

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Shows the payment’s financial impact against the customer’s accounts receivable. If the
payment is valid, this value is the negative of the payment amount. If the payment is voided,
this value is 0.

```
IpAddress

LastReferencedDate

LastViewedDate

LegalEntityId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the user who initiated the payment.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record is possibly referenced (LastReferencedDate) but not viewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The legal entity used in this invoice. Available in API version 65.0 and later. This field is a
relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity


Standard Objects Payment

**Field** **Details**

```
MacAddress

NetApplied

NetPaymentCreditApplied

NetRefundApplied

OrderPaymentSummaryId

PaymentAuthorizationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the payment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total payment amount that has been applied, including adjustments.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total payment amount that has been credited. This amount is equal to
TotalPaymentCreditApplied - TotalPaymentCreditUnapplied. This field is a calculated field.

This field is available in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total refund amount that has been applied to the payment, including adjustments.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.

**Type**
reference


Standard Objects Payment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The authorization record for this payment. If there's a delayed capture (when the capture
occurs after the authorization), all captures must be made against a previously successful
authorization transaction.

This field is a relationship field.

**Relationship Name**
PaymentAuthorization

**Relationship Type**
Lookup

**Refers To**
PaymentAuthorization

```
PaymentGatewayId

PaymentGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment gateway that processed the payment. If there’s a delayed payment, the
field is populated from the authorization record.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment groups organize all the payment transactions that have been made against a record
such as an account or contract. If there’s a delayed payment, the field is populated from the
authorization record.

This field is a relationship field.

**Relationship Name**
PaymentGroup


Standard Objects Payment

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

```
PaymentIntentGuid

PaymentMethodId

PaymentNumber

Phone

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
Unique ID of the payment sent to Stripe or PayPal. Links the Payments Merchant Account
record with the payment at the payment provider.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method that the customer used to provide this payment information.

This field is a relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this payment record.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the payment.


Standard Objects Payment

**Field** **Details**

```
ProcessingMode

SfResultCode

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:

**•** `External` : Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` : Salesforce made and recorded an external call to the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline` : The gateway call failed, but if the problem is fixed and the transaction is
retried, it can work. For example, the customer had insufficient funds or briefly lost their
connection.

**•** `Indeterminate` : The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` : The gateway call failed. If tried again, it still doesn't work. Gateway
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview` : The customer bank requires more information before completing
the payment.

**•** `Success` : The gateway call succeeded.

**•** `SystemError` : Salesforce ended the payment request before receiving a response.
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError` : Customer payment data was incorrect, such as a misspelling in
the credit card address or an incorrect CVV.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects Payment

**Field** **Details**

**Description**
Defines the state of this payment.

Possible values are:

**•** `Canceled` : This payment has been unapplied from its target and can no longer be
allocated.

**•** `Draft` : The payment can be edited before posting it and allocating it to a target. The
payment can also be deleted.

**•** `Processed` : This payment has been finalized and can be allocated against a target.

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

```
TotalApplied

TotalPaymentCreditApplied

TotalPaymentCreditUnapplied

TotalRefundApplied

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of this payment’s balance that has been applied against an invoice.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total amount of all credit types that have been applied against this payment. This field
is a calculated field.

This field is available in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total amount of all credit types that haven't been applied against this payment. This field
is a calculated field.

This field is available in API version 65.0 and later.

**Type**
currency


### Standard Objects PaymentAuthAdjustment

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of a refund that has been applied against this payment.

```
TotalRefundUnapplied

TotalUnapplied

Type

```

SEE ALSO:

OrderPaymentSummary

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of a previously applied refund that has since been unapplied from this
payment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of this payment that was previously applied and then unapplied.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the customer used this payment.

Possible values are:

**•** `Capture`

**•** `Sale`

### PaymentAuthAdjustment

Shows information about an adjustment made to an authorized transaction. This object is available in API version 51.0 and later.


Standard Objects PaymentAuthAdjustment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Note: You can only delete a payment in draft state, which you specify in the **Status** field.

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

Amount

Comments

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account for the payment authorization adjustment. Inherited from the payment
authorization.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of adjustment applied to the parent payment authorization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects PaymentAuthAdjustment

**Field** **Details**

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

```
CurrencyIsoCode

Date

EffectiveDate

Email

GatewayDate

GatewayRefDetails

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment authorization adjustment
record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the adjustment occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the adjustment takes effect on the authorization.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the parent payment authorization owner.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the reversal transaction occurred in the payment gateway.

**Type**
textarea


Standard Objects PaymentAuthAdjustment

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional data that can’t be stored in other fields on the payment record. You can use this
field for transactions following the initial transaction that creates the payment record. You
can use any data that isn’t normalized in financial entities. This field has a maximum length
of 1000 characters and can store data as JSON or XML.

```
GatewayRefNumber

GatewayResultCode

GatewayResultCodeDescription

IpAddress

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code. This field is useful for providing more information
around why the gateway returned a certain result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the user who initiated the payment adjustment.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PaymentAuthAdjustment

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

MacAddress

PaymentAuthAdjustmentNumber

PaymentAuthorizationId

PaymentIntentId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced `(LastReferencedDate)` and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the payment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-provided unique ID for a payment authorization adjustment record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the payment authorization on which the adjustment occurred.

This is a relationship field.

**Relationship Name**
PaymentAuthorization

**Relationship Type**
Lookup

**Refers To**
PaymentAuthorization

**Type**
reference


Standard Objects PaymentAuthAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment intent record.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup

**Refers To**
PaymentIntent

```
Phone

ProcessingMode

SfResultCode

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the authorization adjustment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` —Salesforce made and recorded an external call to the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline` —The gateway call failed, but it might work if the transaction is attempted
again. For example, the customer had insufficient funds or briefly lost their connection.


Standard Objects PaymentAuthAdjustment

**Field** **Details**

**•** `Indeterminate` —The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` —The gateway call failed and won’t work even if tried again. Gateway
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview` —The customer bank requires more information before completing
the payment.

**•** `Success` —The gateway call succeeded.

**•** `SystemError` —Salesforce ended the payment request before receiving a response.
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError` —Customer payment data was incorrect, such as a misspelling
in the credit card address or an incorrect CVV.

```
Status

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of the payment authorization reversal.

Possible values are:

**•** `Canceled` —The payment authorization reversal has been canceled. The parent
authorization has returned to its pre-reversal balance.

**•** `Draft` : The payment authorization reversal can be edited before applying it against
the parent authorization.

**•** `Pending` : The payment authorization reversal is pending. This value is available in API
version 61.0 and later.

**•** `Processed` —The payment authorization reversal has been finalized.

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the customer used the reversal.


### Standard Objects PaymentAuthorization

**Field** **Details**

Possible value is:

**•** `Reversal`

### PaymentAuthorization

Represents a single payment authorization event where users can capture or reverse a payment against a reserve of funds. This object
is available in API version 48.0 and later.

A common type of payment authorization occurs when a user sees a pending transaction against their credit card account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Note: You can only delete a payment in draft state, which you specify in the **Status** field.

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

Amount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customer account.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency


Standard Objects PaymentAuthorization

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The amount authorized for the payment event.

```
Balance

Comments

CurrencyIsoCode

Date

EffectiveDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Authorized amount – total processed captured amount – total processed authorization
reversal amount. Balance can be positive or negative.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can enter comments to provide additional details about the authorization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment authorization record.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
By default, the day the authorization record was created. Users can also enter a different
date. Editable only when the payment authorization’s status is Draft.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the authorization takes effect. Editable only when the payment
authorization’s status is Draft.


Standard Objects PaymentAuthorization

**Field** **Details**

```
Email

ExpirationDate

GatewayAuthCode

GatewayDate

GatewayRefDetails

GatewayRefNumber

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the person who initiated the payment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Authorizations can’t be captured after their expiration dates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Authorization approval code from the payment gateway.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that of the gateway communication that leads to the successful payment
authorization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional data that can’t be stored in other fields on the payment record. You can use this
field for transactions following the initial transaction that creates the payment record. You
can use any data that isn’t normalized in financial entities. This field has a maximum length
of 1000 characters and can store data as JSON or XML.

**Type**
string


Standard Objects PaymentAuthorization

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID from the payment gateway.

```
GatewayResultCode

GatewayResultCodeDescription

IpAddress

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code. This field is useful for providing more information
around why the gateway returned a certain result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the user who initiated the payment authorization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced `(LastReferencedDate)` and not viewed.


Standard Objects PaymentAuthorization

**Field** **Details**

```
MacAddress

OrderPaymentSummaryId

PaymentAuthorizationNumber

PaymentGatewayId

PaymentGroupId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the payment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-provided unique ID for a payment authorization record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce payment gateway record that created this authorization. This gateway will
be used for subsequent captures.

This is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PaymentAuthorization

**Field** **Details**

**Description**
Payment groups organize all the payment transactions that have been made against a record
such as an account or contract. Populated from the authorization record if there is delayed
payment.

This is a relationship field.

**Relationship Name**
PaymentGroup

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

```
PaymentIntentGuid

PaymentMethodId

Phone

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
Unique ID of the payment sent to Stripe or PayPal. Links the Payments Merchant Account
record with the payment at the payment provider.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer payment method provided during this authorization.

This is a relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the person who initiated the payment.


Standard Objects PaymentAuthorization

**Field** **Details**

```
ProcessingMode

SfResultCode

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` —Salesforce made and recorded an external call to the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline` —The gateway call failed, but it may still work if the transaction is attempted
again. For example, the customer had insufficient funds or briefly lost their connection.

**•** `Indeterminate` —The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` —The gateway call failed and won’t work even if tried again. Gateway
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview` —The customer bank requires more information before completing
the payment.

**•** `Success` —The gateway call succeeded.

**•** `SystemError` —Salesforce ended the payment request before receiving a response.
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError` —Customer payment data was incorrect, such as a misspelling
in the credit card address or an incorrect CVV.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects PaymentCredit

**Field** **Details**

**Description**
Defines the state of this payment.

Possible values are:

**•** `Canceled` —This payment has been unapplied from its target and can to longer be
allocated.

**•** `Draft` —The payment can be edited before posting it and allocating it to a target.

**•** `Failed` —Authorization for the payment failed.

**•** `Pending`                   

**•** `Processed` —This payment has been finalized and can be allocated against a target.

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

```
TotalAuthReversalAmount

TotalPaymentCaptureAmount

```

SEE ALSO:

OrderPaymentSummary

### PaymentCredit

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all processed authorization reversals against the payment authorization.

This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all authorization captures related to this payment authorization.

Tracks the amount of money returned to the customer. The return can be a store credit, a gift card, or another type of credit. It's linked
to the original payment record and includes the total credit amount issued. This object is available in API version 65.0 and later.


Standard Objects PaymentCredit

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled. Users
require the PaymentCredit and PaymentPlatform permission sets.

Fields

**Field** **Details**

```
AccountId

Amount

Balance

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account of the customer who made the payment.

This field is a relationship field.

This is a required field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
The amount to be credited.

This is a required field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Balance of payment credits ( `NetApplied - TotalCredit TransactionAmount`

`- TotalCredit PendingTransactionAmount` ).


Standard Objects PaymentCredit

**Field** **Details**

```
Comments

CreditMemoId

CreditType

CreditTypeCategory

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Provide additional details about the payment credit transaction.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the credit memo associated with the payment credit.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Credit types available.

This is a dynamic picklist that the user can define. Possible values are:

**•** `Credit`

**•** `Gift Card`

**•** `Gift Certificate`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A static enum showing the credit category type.

Possible value is:

**•** `Credit`


Standard Objects PaymentCredit

**Field** **Details**

```
CurrencyIsoCode

EffectiveDate

LastReferencedDate

LastViewedDate

NetApplied

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization.

Possible values are:

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Effective date of the payment credit.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all credit amounts apllied for this payment credit ( `TotalCreditApplied -`
`TotalCreditUnapplied` ).


Standard Objects PaymentCredit

**Field** **Details**

```
OrderPaymentSummaryId

PaymentCreditNumber

PaymentId

ReturnOrderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the order payment summary.

This field is a relationship field.

**Relationship Name**
OrderPaymentSummary

**Refers To**
OrderPaymentSummary

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the payment credit record. This field is automatically generated.

Example: `PC-{000000000}` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the payment associated with the payment credit.

This field is a relationship field.

**Relationship Name**
Payment

**Refers To**
Payment

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the return order associated with the payment credit.

This field is a relationship field.


### Standard Objects PaymentCreditLinePayment

**Field** **Details**

**Relationship Name**
ReturnOrder

**Refers To**
ReturnOrder

```
TotalApplied

TotalCreditPendingTxnAmt

TotalCreditTxnAmt

TotalUnapplied

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all applied amounts from the payment credit line payment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of pending payment credits.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of processed payment credits.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all the unapplied amounts from the payment credit line payment.

### PaymentCreditLinePayment

A payment credit line payment. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects PaymentCreditLinePayment

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled. Users
require the PaymentCredit and PaymentPlatform permission sets.

Fields

**Field** **Details**

```
Amount

AppliedDate

AssociatedAccountId

AssociatedLineId

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount to apply to or unapply from the payment to the credit.

This is a required field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date payment was applied. Can be the current date or a provided date.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the customer account.

This field is a relationship field.

**Relationship Name**
AssociatedAccount

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the associated line.

This field is a relationship field.


Standard Objects PaymentCreditLinePayment

**Field** **Details**

**Relationship Name**
AssociatedLine

**Refers To**
PaymentCreditLinePayment

```
CurrencyIsoCode

Description

HasBeenUnapplied

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization.

Possible values are:

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description regarding the payment credit.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the refund line record with type `Applied` has been unapplied. Not
applicable for a refund line record with type `Unapplied` .

This is a required field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.


Standard Objects PaymentCreditLinePayment

**Field** **Details**

```
LastViewedDate

PaymentCreditId

PaymentCreditLine

PaymentNumber

PaymentId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the payment credit.

This field is a relationship field.

This is a required field.

**Relationship Name**
PaymentCredit

**Refers To**
PaymentCredit

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the payment credit line payment. This field is automatically generated.

Example: `PCLP-{000000000}` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the applied payment credit.

This field is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Master-detail


### Standard Objects PaymentCreditTransaction

**Field** **Details**

**Refers To**
Payment (the master object)

```
Type

UnappliedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Payment credit type. This is a required field.

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date payment was unapplied. Can be the current date or a provided date.

### PaymentCreditTransaction

A payment credit transaction. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled. Users
require the PaymentCredit and PaymentPlatform permission sets.

Fields

**Field** **Details**

```
Amount

```

**Type**
currency


Standard Objects PaymentCreditTransaction

**Field** **Details**

**Properties**
Create, Filter, Sort

**Description**
Amount of the payment credit transaction.

This is a required field.

```
AssociatedAccountId

ClientContext

CurrencyIsoCode

ExternalReference

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the customer account.

This field is a relationship field.

**Relationship Name**
AssociatedAccount

**Refers To**
Account

**Type**
textarea

**Properties**
Nillable

**Description**
Additional information about the payment credit transaction.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization.

Possible values are:

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string


Standard Objects PaymentCreditTransaction

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference ID used to track the payment credit transaction.

```
LastReferencedDate

LastViewedDate

PaymentCreditId

PaymentCreditTransactionNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the payment credit.

This field is a relationship field.

This is a required field.

**Relationship Name**
PaymentCredit

**Relationship Type**
Master-detail

**Refers To**
PaymentCredit (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the payment credit transaction. This field is automatically generated.


### Standard Objects PaymentGateway

**Field** **Details**

Example: `PCT-{000000000` }.

```
ProcessingMode

Status

TransactionMessage

### PaymentGateway

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Credit transaction processing mode.

Possible values are:

**•** `External`

**•** `Salesforce`

This is a required field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A static enum showing the status of the credit transaction.

Possible values are:

**•** `Canceled`

**•** `Draft`

**•** `Failed`

**•** `Pending`

**•** `Processed`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Message describing the transaction.

Platform object that represents the connection to an external payment gateway. This object is available in API version 48.0 and later.


Standard Objects PaymentGateway

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
Comments

DefaultTapToPayLocation

ExternalReference

GatewayMode

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Admin-provided details about a record. Maximum of 1000 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Stores the locationId of the location record created at Stripe. The Field Service app uses the
location to process where tap-to-pay transactions are made.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Identifier of an external payment gateway. This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The operational mode of the payment gateway. This field determines the payment gateway’s
ability to accept payments. For production orgs, the gateway must be in Live mode.

Possible values are:


Standard Objects PaymentGateway

**Field** **Details**

**•** `Connected`                   - Payment gateway is active but it can’t accept payments. This option is
only valid in production orgs.

**•** `Live`                   - Payment gateway is active and can accept payments. This option is only valid
in production orgs.

**•** `Test` –Payment gateway is active but not able to accept payments. This option is only
valid in sandbox orgs, and the account can accept only test transactions.

```
LastReferencedDate

LastViewedDate

MerchantAccountId

MerchantCredentialId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible this record is only referenced (LastReferencedDate) but not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the merchant account used by the payment gateway. This merchant account links to
a merchant account at a payment processor.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects PaymentGateway

**Field** **Details**

**Description**
ID of the merchant credential setup entity to reference merchant information.

This field is a relationship field.

**Relationship Name**
MerchantCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

```
PaymentGatewayName

PaymentProcessor

PaymentStatus

PayoutStatus

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Admin-defined name for the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of payment gateway provider.

Possible values are:

**•** `Paypal`

**•** `Stripe`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The payment gateway is active and can accept payments.

Possible values are:

**•** `Enabled`

**•** `Disabled`

The default value is Disabled.

**Type**
picklist


Standard Objects PaymentGateway

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Money can be moved from the payment provider account to the merchant bank account
linked to it.

Possible values are:

**•** `Enabled`

**•** `Disabled`

The default value is Disabled.

```
PaymentGatewayProviderId

ProviderAccount

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the payment gateway that handles transactions between the merchant account and
the payment processor.

This field is a relationship field.

**Relationship Name**
PaymentGatewayProvider

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Account ID assigned by the payment provider that identifies the linked Salesforce Payments
account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines whether Salesforce Payments can use this payment gateway for calls to the external
payment gateway. Inactive payment gateways can’t be used.

Possible values are:


### Standard Objects PaymentGatewayLog

**Field** **Details**

**•** `Active`                   - the merchant account can accept payments.

**•** `Complete`                   - `PaymentStatus` and `DepositStatus` are enabled and the
account provided all the required information.

**•** `Enabled`                   - `PaymentStatus` and `PayoutStatus` are enabled, but the payment
provider can require more information later. If the merchant doesn't provide the
information then the account can become restricted. The time limit that the merchant
has to provide the information is longer than the RestrictedSoon state.

**•** `Pending` –The merchant account exists but it can’t accept payments. This option
maintains backward compatibility for accounts that were created with API version 55.0
and earlier. Pending is no longer in use for API version 57.0 and higher.

**•** `Rejected`                   - The payment provider has rejected the merchant account with an
explanation.

**•** `Restricted`                   - merchant account functionality is limited. This state is only applicable
if `PaymentStatus`, `PayoutStatus`, or both are disabled.

**•** `RestrictedSoon`                   - `PaymentStatus` and `PayoutStatus` are enabled, but
the payment provider requires more information. If the merchant doesn't provide the
information in a specific time period, then the merchant account becomes restricted.

### PaymentGatewayLog

Stores information exchanged between the Salesforce payments platform and external payment gateways. Gateway logs can also record
payloads from external payment entities. This object is available in API version 48.0 and later.

Deleting or archiving a payment gateway log doesn’t impact financial data on other payment entities.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist


Standard Objects PaymentGatewayLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
GatewayAuthCode

GatewayAVSCode

GatewayDate

GatewayMessage

GatewayRefNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Authorization approval code from the gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Code sent by gateways that use an address verification system.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that of the gateway communication that leads to the creation of this
gateway log.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information or error messages sent from the gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.


Standard Objects PaymentGatewayLog

**Field** **Details**

```
GatewayResultCode

GatewayResultCodeDescription

InteractionStatus

InteractionType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code. This field is useful for providing more information
around why the gateway returned a certain result code.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes the result of communication between the payments platform and a payment
gateway.

Possible values are:

**•** `Failed`

**•** `Initiated`

**•** `NoOp`

**•** `Success`

**•** `Timeout`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the type of interaction with the gateway. This field is required for logs created in
Salesforce.

Possible values are:

**•** `Authorization`

**•** `AuthorizationReversal`

**•** `Avs`


Standard Objects PaymentGatewayLog

**Field** **Details**

**•** `Capture`

**•** `CheckGiftCardBalance`

**•** `PostAuth`

**•** `ReferencedRefund`

**•** `Sale`

**•** `Tokenize`

**•** `Void`

```
IsNotification

LastReferencedDate

LastViewedDate

OrderPaymentSummaryId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
For asynchronous transactions, shows whether the gateway log belongs to the notification
( `yes` ) or the initial transaction ( `no` ).

Possible values are:

**•** `No`

**•** `Yes`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.


Standard Objects PaymentGatewayLog

**Field** **Details**

```
PaymentGatewayId

PaymentGatewayLogNumber

ReferencedEntityId

Request

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Payments Platform payment gateway record used for communication with the external
payment gateway.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique ID for this payment gateway log record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key with DomainSet of PaymentAuth and Payment.

This field is a polymorphic relationship field.

**Relationship Name**
ReferencedEntity

**Relationship Type**
Lookup

**Refers To**
CardPaymentMethod, Payment, PaymentAuthAdjustment, PaymentAuthorization, Refund

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects PaymentGatewayLog

**Field** **Details**

**Description**
Raw payload. No sensitive attributes are stored.

```
Response

RetryCategory

SfRefNumber

SfResultCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Raw payload.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The retry category returned by the payment gateway for the failed payment. This field is
available in API version 66.0 and later.

Possible values are:

**•** `CardLimit`  - Insufficient funds, exceeded spending limits, or other restrictions on
the card.

**•** `GatewayConnection`  - Connectivity or communication errors between systems,
including upstream gateway errors.

**•** `PaymentInformation`  - Missing or incorrect data such as incorrect card numbers,
addresses, or currencies.

**•** `PaymentProcessing`  - Payment account is invalid, closed, restricted, or the
transaction was declined for reasons other than insufficient funds.

**•** `Security`  - Security violations or issues such as fraud, risk, authentication, verification,
and authorization.

**•** `Unknown`  - Payment gateway error code isn't recognized or isn't mapped to a specific
category.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If an IdempotencyKey was passed in the API request, its value is stored here in text format.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects PaymentGatewayProvider

**Field** **Details**

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline` : The gateway call failed. If the transaction is attempted again, it can still work.
For example, the customer has insufficient funds or briefly lost their connection.

**•** `Indeterminate` : The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` : The gateway call failed and can’t work. Gateway calls fail
permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview` : The customer bank requires more information before completing
the payment.

**•** `Success` : The gateway call succeeded.

**•** `SystemError` : Salesforce ended the payment request before receiving a response.
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError` : Customer payment data was incorrect, such as a misspelling in
the credit card address or an incorrect CVV.

### PaymentGatewayProvider

Setup entity for payment gateways. Defines the connection to a payment gateway Apex adapter. This object is available in API version
48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.


Standard Objects PaymentGatewayProvider

Fields

**Field** **Details**

```
ApexAdapterId

Comments

DeveloperName

IdempotencySupported

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of an APEX adapter class. The adapter interacts with your payment gateway to complete
transactions. This field is unique within your organization.

This field is a relationship field.

**Relationship Name**
ApexAdapter

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional details about a record. Maximum of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
(Optional) An internal name you assign the adapter. For reference only.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the same payment request is made in rapid succession, this field defines whether the
Payments platform charges the customer or merchant’s card multiple times for the same
transaction. This situation can occur when a user clicks a Pay button twice, or the gateway’s


Standard Objects PaymentGatewayProvider

**Field** **Details**

server goes down after fulfilling a payment request and the client immediately tries making
another payment. If this field has a value of Yes, the Payments platform ignores identical
payment requests made immediately after an original request.

Different payment gateways have varying levels of idempotency support. When configuring
a new payment gateway integration, plan accordingly.

Possible values are:

**•** `No`

**•** `Yes`

```
Language

LastViewedDate

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Customer language used for the payment gateway.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
User-friendly name of the payment gateway provider.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace for the payment gateway platform.


### Standard Objects PaymentGroup PaymentGroup

Top-level object that groups all payment transactions that are processed for an order or invoice. PaymentGroup is a standalone object,
so it isn’t required for users to execute payment transactions (authorizations, captures, refunds, and sales). This object is available in API
version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated. Commerce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

### `PaymentGroupNumber`

```
SourceObjectId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for the payment group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order or invoice related to all the payment transactions in the payment group.

This is a relationship field.

**Relationship Name**
SourceObject

**Relationship Type**
Lookup

**Refers To**
Order


### Standard Objects PaymentInitiationSource PaymentInitiationSource

Represents the originating source of a payment. This information helps other Salesforce products integrate with Salesforce Payments.
This object is available in API version 63.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

Application

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The account record that initiated this payment.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce application initiating the payment.

Possible values are:

**•** `Collections`

**•** `Commerce`

**•** `Custom`

**•** `FieldService`

**•** `OrderManagement`


Standard Objects PaymentInitiationSource

**Field** **Details**

**•** `Payments`

**•** `Revenue`

**•** `Sales`

**•** `Scheduler`

**•** `Service`

```
Channel

CollectionPlanId

ContactId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The origin of the submitted payment. For example, D2C, virtual terminal, or merchant MOTO
(mail order or phone order).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The collection plan record that submitted payment. This field is available only for
merchant-initiated payment collections. For example, a merchant collects an outstanding
balance using a Pay Now payment link or over the phone.

This field is a relationship field.

**Relationship Name**
CollectionPlan

**Refers To**
CollectionPlan

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The contact record of the contact that made the payment.

This field is a relationship field.

**Relationship Name**
Contact

**Refers To**
Contact


Standard Objects PaymentInitiationSource

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

LastViewedDate

Name

OpportunityId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. This field contains
the ISO code for any currency allowed by the organization.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the payment initiation source record. For example,
d9e01178-b6878-2f4b-a14d-b0132b7ret67

**Type**
reference


Standard Objects PaymentInitiationSource

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The opportunity record that made the payment.

This field is a relationship field.

**Relationship Name**
Opportunity

**Refers To**
Opportunity

```
OrderSummaryId

PaymentScheduleItemId

Process

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order summary record that initiated the payment. This field is available with Salesforce
Order Management and Commerce applications.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The payment schedule item record that initiated the payment. This field is available only
with the Scheduler application.

This field is a relationship field.

**Relationship Name**
PaymentScheduleItem

**Refers To**
PaymentSchedleItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects PaymentInitiationSource

**Field** **Details**

**Description**
Component within the application that’s initiating the payment. Maximum length of the
string is 255 characters. For example, managed or custom checkout, product description
page (PDP).

```
QuoteId

ServiceAppointmentId

SiteId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The quote record that initiated the payment.

This field is a relationship field.

**Relationship Name**
Quote

**Refers To**
Quote

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The service appointment record that initiated the payment. This field is available only with
the Field Service application.

This field is a relationship field.

**Relationship Name**
ServiceAppointment

**Refers To**
Appointment

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The site record that initiated the payment. This field is for applications that don't have a web
store, but created a digital experience site to accept payments

This field is a relationship field.

**Relationship Name**
Site


Standard Objects PaymentInitiationSource

**Field** **Details**

**Refers To**
Site

```
WebCartId

WebStoreId

WorkOrderId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The web cart record that submitted the payment.

This field is a relationship field.

**Relationship Name**
WebCart

**Refers To**
WebCart

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The web store record that initiated the payment. For example, a B2B, D2C, or Pay Now store.

This field is a relationship field.

**Relationship Name**
WebStore

**Refers To**
WebStore

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The work order record that submitted the payment. This field is available only for the Field
Service application.

This field is a relationship field.

**Relationship Name**
WorkOrder

**Refers To**
WorkOrder


### Standard Objects PaymentIntent

**Field** **Details**

```
WorkOrderLineItemId

### PaymentIntent

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The work order line item record that made the payment. This field is only available with the
Field Service application.

This field is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Refers To**
WorkOrderLineItem

Represents data temporarily stored during a transaction’s lifecycle that can identify the buyer, the merchant, and the amount the buyer
is sending to the merchant. Data such as timestamp and amount returned can also be stored in PaymentIntent. This object is available
in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account record of the buyer.

This field is a relationship field.


Standard Objects PaymentIntent

**Field** **Details**

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

```
AmountCapturable

AmountRefundable

AuthorizationReversal

Amount

AuthorizedAmount

BillingAddress

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Payment amount that a merchant can collect after the fulfillment of an order.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the payment that the merchant can refund.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount canceled before completing the transfer of funds from buyer to merchant.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount authorized by the payer’s bank.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects PaymentIntent

**Field** **Details**

**Description**
The billing address of the account holder. This field is the compound form of the billing
address. Read-only. For details on compound address fields, see Address Compound Fields.

```
BillingCity

BillingCountry

BillingCountryCode

BillingGeocodeAccuracy

BillingLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the billing address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.


Standard Objects PaymentIntent

**Field** **Details**

```
BillingLongitude

BillingPostalCode

BillingState

BillingStreet

CapturedAmount

ContextData

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 80 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount that a merchant secured from a buyer.

**Type**
string

**Properties**
Nillable


Standard Objects PaymentIntent

**Field** **Details**

**Description**
Additional metadata or information about a payment, such as the source of the payment,
user data, or any other relevant information that can help in processing or tracking the
payment.

```
CurrencyIsoCode

DisputeEvidenceDueDate

DisputeFee

DisputeStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for any currency allowed by the organization. Available only for orgs with the
multicurrency feature enabled.

Possible values are:

**•** `Euro`

**•** `USD`

The default is USD.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date by which the merchant must submit information related to the dispute.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that the credit card company charges the merchant for each disputed payment.
The fee is also known as a chargeback fee.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the disputed transaction.

Possible values are:

**•** `Closed` —The dispute inquiry is closed.

**•** `Created` —The payment gateway opens a payment dispute.


Standard Objects PaymentIntent

**Field** **Details**

**•** `Lost` —The bank ruled in the account owner’s favor and refunded the charge. The
refund is permanent and the dispute fee isn’t returned.

**•** `Won` —The bank ruled in the merchant's favor. The issuing bank returns the debited
chargeback amount to the payment gateway, who passes this amount back to the
merchant.

```
DisputedAmount

EntryMode

Guid

IncurrenceStatus

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount the customer is challenging.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how the payment information was provided.

Possible values are:

**•** `Flow` —Salesforce flow that initiated the payment.

**•** `Merchant` —The credit card isn’t available so the merchant entered the payment
information via the phone or an email.

**•** `Payer_Online` —The payer entered their payment information online.

**•** `Place_Order_V2` —The payment was initiated from the Place Order V2 Orchestration.

**•** `TapToPay` —The card was available and the payer tapped that card or device on the
payment terminal.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique ID of the payment sent to Stripe or PayPal. This ID links the Payments Merchant
Account record with the payment at the payment provider.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects PaymentIntent

**Field** **Details**

**Description**
Status of an orphaned payment. An orphaned payment occurs when a payment transaction
is complete, but the workflow is disrupted, and the payment isn't recorded in the consuming
flow. An unexpected error can cause an orphaned payment. For example, a payment is
accepted at checkout, but the order doesn't get placed because of a network issue.

Possible values are:

**•** `Canceled` —The workflow was disrupted and the payment was canceled or refunded.

**•** `Claimed` —The payment was recorded and the workflow was completed.

**•** `Pending` —The consuming workflow hasn't recorded the payment yet.

If there isn't a value for this field, it means that the consumer doesn't rely on it to track
orphaned payments.

```
IntentAmount

IsCaptureComplete

IsEvidenceSubmitted

LastReferencedDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount that a merchant expects to receive from a buyer.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Verification whether the funds for a given payment are paid.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Status of the requested information that the merchant provides to the bank about the dispute.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects PaymentIntent

**Field** **Details**

```
LastViewedDate

MerchantAccountId

PaymentGatewayId

PaymentGroupId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced but not viewed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required field. The merchant account record associated with a payment intent record.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment gateway record that processed the payment.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PaymentIntent

**Field** **Details**

**Description**
Payment groups organize all the payment transactions that have been made against a record
such as an account or contract.

This is a relationship field.

This field is available in API version 65.0 and later.

**Relationship Name**
PaymentGroup

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

```
PaymentInitiationSourceId

PaymentIntentNumber

PaymentLinkGmvDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment initiation source record associated with the payment. The record identifies the
originating application and object of the payment..lo

**Relationship Name**
PaymentInitiationSource

**Relationship Type**
Lookup

**Refers To**
PaymentInitiaionSource

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated number assigned to the payment record, for example `PI-000000001` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Date the payment is captured from a payment link transaction. The total amount paid is
expressed as the Gross Merchandise Value (GMV).


Standard Objects PaymentIntent

**Field** **Details**

```
PaymentLinkId

PaymentMethodDetails

PaymentMethodId

PaymentMethodSubType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment link record.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Relationship Type**
Lookup

**Refers To**
PaymentLink

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional information about the payment method type such as the four last digits of a card
number.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment method record, indicating a card payment method, digital wallet, or alternative
payment method.

This field is a polymorphic relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PaymentIntent

**Field** **Details**

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of payment method types such as Apple
Pay and Google Pay.

```
PaymentMethodType

ProviderReference

RefundedAmount

ShippingAddress

ShippingCity

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment method used for the transaction.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A payment record at the payment gateway that identifies the payment provider.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total or partial amount refunded to the buyer due to product return, merchant’s lack of
inventory, or shipping and delivering problems.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Delivery address for the purchase. The compound form of the shipping address. Read-only.
See Address Compound Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. City maximum size is 40 characters.


Standard Objects PaymentIntent

**Field** **Details**

```
ShippingCountry

ShippingCountryCode

ShippingGeocodeAccuracy

ShippingLatitude

ShippingLongitude

ShippingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the shipping address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. For
details on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
string


Standard Objects PaymentIntent

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The maximum size of the postal code is 20 characters.

```
ShippingState

ShippingStreet

Status

SubmittedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. State maximum size is 80 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Maximum of 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the payment record.

Possible values are:

**•** `Authorized`

**•** `Canceled`

**•** `Created`

**•** `Expired`

**•** `Failed`

**•** `PartiallyCaptured`

**•** `PartiallyRefunded`

**•** `Pending`

**•** `Refunded`

**•** `Succeeded`

**Type**
reference


### Standard Objects PaymentIntentEvent

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The submitted by record, which identifies who processes the payment on the customer's
behalf. The customer provides the authorization to submit the payment over the phone or
through the mail.

This field is a relationship field.

**Relationship Name**
SubmittedBy

**Relationship Type**
Lookup

**Refers To**
User

### PaymentIntentEvent

Represents a payment intent platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0
and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)

Supported Calls

```
   describeSObjects()

```

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
ChangeType

```

**Type**
picklist

**Properties**
Restricted picklist


Standard Objects PaymentIntentEvent

**Field** **Details**

**Description**
Type of payment intent event that triggers an event notification. You can write code to
operate conditionally on the value of this field. For example, you can ignore an authorization
but get notified of captures.

Possible values are:

**•** `Authorize` –Payment is authorized.

**•** `AuthorizeFailure` –There’s an error preventing the payment authorization

**•** `Capture` –Payment is captured.

**•** `CaptureFailure`                   - An error prevented the payment capture.

**•** `Refund` –Payment is refunded.

**•** `RefundFailure` –An error prevented the payment refund.

```
PaymentInitiationSourceApplication

PaymentInitiationSourceChannel

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
Salesforce application initiating the payment. This field is available in API version 63.0 and
later.

Possible values are:

**•** `Collections`

**•** `Commerce`

**•** `Custom`

**•** `FieldService`

**•** `OrderManagement`

**•** `Payments`

**•** `Revenue`

**•** `Sales`

**•** `Scheduler`

**•** `Service`

**Type**
string

**Properties**
Nillable

**Description**
Identifies the channel in the Payment Initiation Source record for which the event occurs.
This field is available in API version 63.0 and later.


Standard Objects PaymentIntentEvent

**Field** **Details**

```
PaymentInitiationSource

PaymentInitiationSourceProcess

PaymentIntentGuid

PaymentIntent

```

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the Payment Initiation Source record for which the event occurs. This field is available
in API version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentInitiationSource

**Refers To**
PaymentInitiationSource

**Type**
string

**Properties**
Nillable

**Description**
Identifies the process in the Payment Initiation Source record for which the event occurs.

**Type**
string

**Properties**
Nillable

**Description**
Identifies the GUID in the Payment Initiation Source record for which the event occurs. This
field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the PaymentIntent record for which the event occurs. This field is available in API
version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup


### Standard Objects PaymentLineInvoice

**Field** **Details**

**Refers To**
PaymentIntent

```
PaymentLink

### PaymentLineInvoice

```

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the payment link record for which the event occurs. This field is available in API
version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Refers To**
PaymentLink

Represents a payment allocated to or unallocated from an invoice. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated. Commerce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
Amount

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Total amount applied or unapplied by this payment line.


Standard Objects PaymentLineInvoice

**Field** **Details**

```
AppliedDate

AssociatedAccountId

AssociatedPaymentLineId

Comments

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this line was applied to an invoice or payment. If this field is null, it inherits the
value of the payment line invoice’s Date field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The account for this payment line’s target invoice.

This is a relationship field.

**Relationship Name**
AssociatedAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The paymentLine that was unapplied. Populated only when PaymentLineInvoice’s Type field
has a value of Unapplied.

This is a relationship field.

**Relationship Name**
AssociatedPaymentLine

**Relationship Type**
Lookup

**Refers To**
PaymentLineInvoice

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects PaymentLineInvoice

**Field** **Details**

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

```
Date

EffectiveDate

EffectiveImpactAmount

HasBeenUnapplied

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time that this payment line was created.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Defines the date and time when the payment line application or unapplication becomes
effective.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment invoice line impacts a customer’s accounts receivable. This value
is positive when PaymentLineInvoice’s Type field is Applied, and negative when
PaymentLineInvoice’s Type is Unapplied. If there’s an unapplied line related to this record,
EffectiveImpactAmount has a value of 0.

Note: EffectiveImpactAmount evaluates only the applied and unapplied line pair.
Therefore, the effective impact amount could be different for different lines within
the same payment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this payment line has been unapplied from the target invoice. Has a value
of NA when PaymentInvoiceLine’s Type field has a value of Unapplied. Can be No or Yes if
Type has a value of Applied.

Possible values are:

**•** `NA`


Standard Objects PaymentLineInvoice

**Field** **Details**

**•** `No`

**•** `Yes`

```
ImpactAmount

InvoiceId

LastReferencedDate

LastViewedDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows the payment’s financial impact against the customer’s accounts receivable. If
PaymentLineInvoice has a Type of Applied, the ImpactAmount is the negative equivalent of
the line’s Amount field. Otherwise, ImpactAmount equals Amount.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Target invoice for this payment line.

This is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.


Standard Objects PaymentLineInvoice

**Field** **Details**

```
PaymentBalance

PaymentId

PaymentLineInvoiceNumber

Type

UnappliedDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total balance of this line’s parent payment record following the application or unapplication
of this payment line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Parent payment for this payment line.

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for this payment line.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this payment line has been applied or unapplied to the target invoice.

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime


### Standard Objects PaymentLink

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this payment line was unapplied from the target invoice. Populated only when
the Type field equals Unapplied. Inherits the value of the Date field.

Usage

Use a payment line to apply all or part of a payment’s balance to an invoice. The PaymentLineInvoice object represents the balance
taken from the payment and applied toward the invoice. You can apply a payment’s balance when you create the payment record or
afterward. The payment line must have the same currency as the parent payment.

A payment line has an amount, which represents the total amount taken from the payment, and balance, which represents the remaining
amount after the payment line has been applied to an invoice. A payment’s amount can’t be less than the sum of all of its payment line
amounts.

One payment can have multiple payment lines. A payment line must be related to only payment.

You can create multiple payment lines on a payment apply each line to different invoices on the same account, or to invoices on different
accounts.

Here’s one way you could use Salesforce API to apply a payment to an invoice using a payment line.

### PaymentLink

A link that a merchant can share with customers to collect payments for products and services. The payment link, which you can embed
into a Salesforce app or send directly to a customer, directs the customer to a Pay Now payment page. The page can show a total amount
owed or an itemized list or products, shipping and tax charges, and a total amount owed. The customer enters their contact and payment
details, and submits their payment. The amounts are shown in the store's currency. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects PaymentLink

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

Amount

CartId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payer account.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount the payer owes.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the cart record.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
Webcart


Standard Objects PaymentLink

**Field** **Details**

```
CollectionPlanId

CurrencyIsoCode

Description

Expiry Time

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The collection plan associated with the payment link.

This field is a relationship field.

Available in API version 63.0 and later with Financial Services and Automotive Cloud.

**Relationship Name**
CollectionPlan

**Refers To**
CollectionPlan

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
3-digit ISO code for the payment currency that is shown on the Pay Now page. Possible
values are:

**•** EUR – Euro

**•** GBP – British Pound

**•** USD – US Dollar

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text on the Pay Now payment page that’s visible to your customers. This text can
communicate any information you want.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the payment link expires. The time is based on the user’s time zone,
not the org’s time zone.


Standard Objects PaymentLink

**Field** **Details**

```
LastReferencedDate

LastViewedDate

OwnerId

PaymentInitiationSource

PaymentLinkNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record can be referenced and not viewed directly.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this record.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The origin of the payment, based on the information in the Payment Link record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number that identifies the payment link.


Standard Objects PaymentLink

**Field** **Details**

```
PaymentMethodSetId

PaymentScheduleItemId

PaymentUrl

QrCodeImageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the PaymentMethodSet object, which determines what payment methods are
shown to the payer.

This field is a relationship field.

**Relationship Name**
PaymentMethodSet

**Relationship Type**
Lookup

**Refers To**
MerchAccPaymentMethodSet

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment schedule item associated with the payment link.

This field is a relationship field.

Available in API version 63.0 and later with Financial Services and Automotive Cloud.

**Relationship Name**
PaymentScheduleItem

**Refers To**
PaymentScheduleItem

**Type**
url

**Properties**
Filter, Group, Sort

**Description**
Unique URL of the Pay Now page. This URL IS auto-generated, and not editable.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference to the QR code image included in the payment link record.


Standard Objects PaymentLink

**Field** **Details**

This field is a relationship field.

**Relationship Name**
QrCodeImage

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
Status

TaxAmount

Title

Type

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the payment link is active and can be used.

Possible values are:

**•** `Active`

**•** `Disabled`

The default value is `Active` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of the tax for the purchase. This amount is shown on the Pay Now page.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the Pay Now page, indicating what is being paid.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of payment link created, which the merchant can share with the customer
to receive payment. The payment link also determines which Pay Now page is generated
and what’s included on that page.


### Standard Objects PaymentLinkEvent

**Field** **Details**

Possible values are:

**•** `CheckoutWithOrder` (only for orgs with Payments and Commerce)—includes the
amount owed based on the products you select, lists the products purchased, and
calculates tax using the billing address and selected shipping options. After a customer
makes a payment, this link type creates an order record.

**•** `PredefinedAmount` —shows only an amount due for products purchased. The
merchant enters the amount due when creating the payment link.

**•** `WithProducts` —Deprecated. New payment links can't be created with this link type.

The default value is `PredefinedAmount` .

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Determines whether the payment link is used one time or multiple times before the
configured expiration date and time.

Possible values are:

**•** `MultiUse`

**•** `SingleUse`

The default value is `MultiUse` .

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**PaymentLinkOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PaymentLinkShare on page 67**
Sharing is available for the object.

### PaymentLinkEvent

Represents a payment link platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0
and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)


Standard Objects PaymentLinkEvent

Supported Calls

```
   describeSObjects()

```

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
ChangeType

PaymentLinkId

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of payment link event, which triggers and event notification.

Possible values are:

**•** `Create` –Payment link created.

**•** `Delete` –Payment link deleted.

**•** `Update` –Payment link property changed.

**Type**
reference

**Properties**
Nillable

**Description**
Type of payment link event. You can write code to operate conditionally on the value of this
field. For example, you can ignore a create change but get notified of updates.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Relationship Type**
Lookup

**Refers To**
PaymentLink


### Standard Objects PaymentMethod PaymentMethod

Represents the method that a buyer uses to compensate the seller of a good or service. Common payment methods include cash, checks,
credit or debit cards, money orders, bank transfers, and online payment services. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

Comments

CompanyName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account entity linked to this payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
textarea

**Properties**
Nillable

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
string


Standard Objects PaymentMethod

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Company name for this payment method. Part of the payment method’s address.

```
ImplementorType

IsAutoPayEnabled

Name

NickName

PaymentMethodAddress

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Shows the type of payment method.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Payment Method page layout in the UI. It isn't automatically added.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A unique number assigned to the payment method. Numbers start at 1000 and are read
only, but administrators can change the format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User-defined nickname for this payment method.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects PaymentMethod

**Field** **Details**

**Description**
Full address related to the alternative payment method. For more information about address
fields, see Address Compound Fields.

```
PaymentMethodCity

PaymentMethodCountry

PaymentMethodDetails

PaymentMethodGeocodeAccuracy

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Accuracy level of the geocode for the payment method address. An accuracy level contains
information about the location of a latitude and longitude. For more information about
geolocation fields, see Geolocation Compound Field.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`


Standard Objects PaymentMethod

**Field** **Details**

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
PaymentMethodLatitude

PaymentMethodLongitude

PaymentMethodPostalCode

PaymentMethodState

PaymentMethodStreet

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Longitude of the payment method address. Used with the PaymentMethodLatitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Part of the address for this payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PaymentMethod

**Field** **Details**

**Description**
Payment method address details.

```
PaymentMethodSubType

PaymentMethodType

SavedPaymentMethodId

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be a digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The payment method used for the transaction, such as Visa, Mastercard, EPS, SepaDebit,
UnionPay, and Klarna. Method types can also be direct debit payments like ACH, Becs, and
BACS. This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the payment method.

Possible values are:

**•** `Active` —The Payments platform can use the payment method to make payments.


### Standard Objects PymtSchdDistributionMethod

**Field** **Details**

**•** `Canceled` —The Payments platform can no longer use the payment method to make
payments.

**•** `InActive` —The Payments platform currently can’t use the payment method to make
payments. Admins can change this value to Active when needed.

### PymtSchdDistributionMethod

Indicates how the total payment is divided into partial payments. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_pymtschddistributionmethod.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_pymtschddistributionmethod.htm)

Fields

**Field** **Details**

```
Description

DistributionCount

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
User-entered description of the payment schedule distribution method.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of payment schedule items for the payment schedule. The payment schedule
items are used to distribute the payment schedule’s total payment into partial payments.

Possible values are:

**•** `1` —Full distribution. Currently, each payment schedule must have exactly one payment
schedule item.


Standard Objects PymtSchdDistributionMethod

**Field** **Details**

```
DistributionMethodType

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Distribution method time interval.

Possible values are:

**•** `FullDistribution` —The full amount on the payment schedule is distributed to
a single payment schedule item.

**•** `LumpSum` —The specified payment amount on the payment schedule is distributed to
a single payment schedule item.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Monthly` —The specified payment amount on the payment schedule is distributed
evenly across multiple monthly payments.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Quarterly` —The specified payment amount on the payment schedule is distributed
evenly across multiple quarterly payments.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Weekly` —The specified payment amount on the payment schedule is distributed
evenly across multiple weekly payments.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.


### Standard Objects PaymentScheduleTreatmentDtl

**Field** **Details**

```
Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
User-entered name for the payment schedule distribution method.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

### PaymentScheduleTreatmentDtl

Contains configuration information for the payment schedule treatment detail. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduletreatmentdtl.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduletreatmentdtl.htm)


Standard Objects PaymentScheduleTreatmentDtl

Fields

**Field** **Details**

```
DateOffset

Description

InstallmentPaymentType

LastReferencedDate

LastViewedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A number equal to or less than 0. The date offset is subtracted from the processing date
reference to determine the processing date.

For example, suppose that the invoice due date is 01/17/2022 and offset is -7. In this case,
the payment schedule item is processed by the jobs that run on or before 01/10/2022.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user-entered description of the payment schedule treatment detail.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the payment amount is divided into multiple payments.

Possible values are:

**•** `Percentage`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PaymentScheduleTreatmentDtl

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
PaymentMethodSelectionType

PaymentRunMatchingValue

PaymentScheduleTreatmentDetailNumber

PaymentScheduleTreatmentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the payment method is specified.

Possible values are:

**•** `Manual` —the payment method is entered by a user

**•** `MostRecentAutopay` —the payment method is the most recent automatic payment
method used

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:

**•** `AMER`

**•** `APAC`

**•** `EMEA`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique identifier for this payment schedule treatment detail.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related payment schedule treatment.

This field is a relationship field.


Standard Objects PaymentScheduleTreatmentDtl

**Field** **Details**

**Relationship Name**
PaymentScheduleTreatment

**Relationship Type**
Lookup

**Refers To**
PaymentScheduleTreatment

```
Percentage

ProcessingDateReference

PymtSchdDistributionMethodId

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of the source amount that is used to create the payment schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the source of the reference date.

Possible values are:

**•** `InvoiceDueDate` —use the invoice’s due date as the date reference

**•** `UserInputDate` —User Input Date

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distribution method that contains the information on how to create the payment schedule
items.

This field is a relationship field.

**Relationship Name**
PymtSchdDistributionMethod

**Relationship Type**
Lookup

**Refers To**
PymtSchdDistributionMethod


### Standard Objects PaymentTerm PaymentTerm

Defines your company's method and expectations for receiving payment. This object is available in API version 55.0 and later.

Timely payment helps your company maintain cash flow. Payment terms are used to determine the payment due date on invoices. Use
with the PaymentTermItem object.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentterm.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentterm.htm)

Fields

**Field** **Details**

```
Description

IsDefault

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined field that describes the payment term. For example, use _`Net 30`_ to describe
a payment term where the payment is due within 30 days of the billing date.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this payment term is the default term for your org. A default payment
term must be defined in your org.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PaymentTerm

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

Name

Status

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the payment term. For example, _`Net 30`_ or _`Cash on delivery (COD)`_ .

This name appears on the invoice.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the payment term is available for use on invoices.

Possible values are:

**•** `Active` —The payment term is available for use and can be applied to an order. Only
active payment terms can be applied to transactions or orders.

**•** `Draft` —The payment term exists but isn't activated yet.

**•** `Inactive` —The payment term exists but can't be applied to new transactions or
orders.

The default value is `Draft` .

A payment term is applied to an order or transaction, and is passed on to the billing schedule that’s used to generate the invoice. The
due date on the invoice is derived from the payment.

For example, a Net 30 payment term means that the customer has 30 days to pay from the invoice date. Suppose that an invoice with
a Net 30 payment term is generated on January 1. The invoice date is January 1, and the due date is January 31 (1 + 30 days = 31).


### Standard Objects PaymentTermItem PaymentTermItem

Defines the attributes of a payment term that your company uses. The PaymentTermItem is used to determine the due date on invoices.
This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymenttermitem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymenttermitem.htm)

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined field that describes the details of the payment term item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects PaymentTermItem

**Field** **Details**

```
Name

PaymentTermId

PaymentTimeframe

Period

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated sequential number, such as PTI-000001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the payment term that this payment term item is associated with.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the time period when the payment is expected.

Possible values are:

**•** `Standard` —Indicates that payment is expected by the date specified in the payment
term. If payment isn't received by the due date, the payment becomes overdue.

The default value is `Standard` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of units in the payment period. Used with the `PeriodUnit` field.

For example, to define a payment term of Net 30, enter _`30`_ as the `Period` and select
_`Days`_ as the `PeriodUnit` .


### Standard Objects PaymentSchedule

**Field** **Details**

```
PeriodUnit

Type

### PaymentSchedule

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the unit of time for the payment period. Used with the `Period` field.

For example, to define a payment term of Net 30, enter _`30`_ as the `Period` and select
_`Days`_ as the `PeriodUnit` .

Possible values are:

**•** `Days`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies how the payment term and invoice due date are derived.

Possible values are:

**•** `Period-Based` —Tells the system to use the `Period` and `PeriodUnit` fields
to calculate the invoice due date.

The default value is `Period-Based` .

The payment schedule represents a collection of payments that a customer wants to collect at different times for a certain record. A
schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each of a schedule’s
items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts. When a
payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment processing
if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentschedule.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentschedule.htm)


Standard Objects PaymentSchedule

Fields

**Field** **Details**

```
AvailableRequestedAmount

Comments

CurrencyIsoCode

DefaultPaymentAccountId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The payment schedule’s remaining amount available for the creation of payment schedule
items. Equals `TotalRequestedAmount`   - `TotalLineRequestedAmount` .

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined comments.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When a payment run creates payments from a payment schedule item, it sets the payment’s
account to the item’s `PaymentAccountId` . Upon payment schedule item creation, the
item’s `PaymentAccountId` inherits the schedule’s `DefaultPaymentAccountId` .
However, you can override the `PaymentAccountId` with a different account as needed.
If you do, future payments made from the item use the new account.

This is a relationship field.

**Relationship Name**
DefaultPaymentAccount

**Relationship Type**
Lookup

**Refers To**
Account


Standard Objects PaymentSchedule

**Field** **Details**

```
DefaultPaymentMethodId

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When a payment run creates payments from a payment schedule ID, it sets the payment’s
account to the item’s `PaymentMethodId` . Upon payment schedule item creation, the
item’s `PaymentMethoId` inherits the schedule’s `DefaultPaymentMethodId` .
However, you can override the `PaymentMethodId` with a different account as needed.
If you do, future payments made from the item will use the new account.

**Relationship Name**
DefaultPaymentMethod

**Relationship Type**
Lookup

**Refers To**
CardPaymentMethod, DigitalWallet

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who created the payment schedule.

This is a polymorphic relationship field.

**Relationship Name**
Owner


Standard Objects PaymentSchedule

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PaymentScheduleNumber

PaymentScheduleTreatmentDtlId

PaymentSource

ReferenceEntityId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the payment schedule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment schedule treatment detail associated with the payment schedule record.

This field is a relationship field.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**Relationship Name**
PaymentScheduleTreatmentDtl

**Refers To**
PaymentScheduleTreatmentDtl

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the name of the funding source that is used to fulfill a payment commitment.

Available in API version 63.0 and later with Financial Services and Automotive Cloud.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The object that receives payments as a result of payment schedule items processed from
the payment schedule.

This is a polymorphic relationship field.


Standard Objects PaymentSchedule

**Field** **Details**

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**

API version 55.0 and later:

**•** `Contract`

**•** `Order`

**•** `Invoice`

API version 62.0 and later with Financial Services and Automotive Cloud:

CollectionPlan

```
RemainingAmountToBeProcessed

Status

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total pending amount of payment schedule items that haven’t yet been processed for
payment. Equals `TotalLineRequestedAmount`   - `TotalProcessedAmount` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment schedule.

Possible values are:

**•** `Accepted` : The payment schedule is approved and is ready for payment run evaluation.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Approval Pending` : The payment schedule needs approval.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Canceled` : Payment runs can’t evaluate payment schedules or use them to create
payments.

**•** `Completed` : All of the payment schedule’s payment schedule items have been
processed for payments.

**•** `Draft` : The payment schedule can be edited and configured. Payment runs don’t
evaluate draft payment schedules.

**•** `On Hold` : The payment schedule can't be considered for payment runs due to missing
information, the need for additional review, or other unresolved external factors.


Standard Objects PaymentSchedule

**Field** **Details**

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Open` : The payment schedule is available for payment run evaluation.

**•** `Rejected` : The payment schedule isn't approved and can't be considered for payment
run evaluation.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

```
TotalAppliedAmount

TotalCanceledAmount

TotalPaymentsReceived

TotalPaymentScheduleItemAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of all payment schedule items that have been applied to payments.

This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all `RequestedAmount` values on payment schedule items with a status of
Canceled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The cumulative sum of payments received for all payment schedule items linked to a payment
schedule.

This field is a calculated field.

Available in API version 63.0 and later with Financial Services and Automotive Cloud.

**Type**
currency

**Properties**
Filter, Nillable, Sort\

**Description**
The total amount allocated from the payment schedule to its payment schedule items. Equals
the sum of each payment schedule item’s `RequestedAmount`   - the sum of each payment
schedule item’s `Canceled Amount` .


Standard Objects PaymentSchedule

**Field** **Details**

```
TotalProcessedAmount

TotalRequestedAmount

Type

UsageType

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `ProcessedAmount` values on payment schedule items with a status of
Processed.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The total amount available for a payment schedule to distribute to its payment schedule
items. The sum of payment schedule items can’t be greater than the
`TotalLineRequestedAmount` of the parent payment schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of payment for which the payment schedule is created.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

Possible values are:

**•** `PaymentPlan` —Payment Plan

**•** `PromiseToPay` —Promise to Pay

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the usage type for the record.

Possible value is:

**•** `CollectionPlan`

Available in API version 62.0 and later with Financial Services and Automotive Cloud.


### Standard Objects PaymentScheduleItem PaymentScheduleItem

A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each
of a schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts.
When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment
processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduleitem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduleitem.htm)

Fields

**Field** **Details**

```
Comments

CurrencyIsoCode

LastPaymentGatewayLogId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined comments.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment schedule item record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most recent payment gateway log created following a payment gateway request to
make a payment based on the payment schedule item.

This is a relationship field.


Standard Objects PaymentScheduleItem

**Field** **Details**

**Relationship Name**
LastPaymentGatewayLog

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayLog

```
LastReferencedDate

LastViewedDate

PaymentAccountId

PaymentBatchRunId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account assigned to payments made from the payment schedule item. When a payment
schedule item is created, its `PaymentAccountId` inherits the payment schedule’s
`DefaultPaymentAccountId` . However, you can provide a new
`PaymentAccountId` at any time. If you change the `PaymentAccountId`, only
payments made after the change use the new account.

This is a relationship field.

**Relationship Name**
PaymentAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference


Standard Objects PaymentScheduleItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment batch run that evaluated the payment schedule item for payment processing.

This is a relationship field.

**Relationship Name**
PaymentBatchRun

**Relationship Type**
Lookup

**Refers To**
PaymentBatchRun

```
PaymentId

PaymentMethodId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment that a payment run created for the payment schedule item after picking up
the parent payment schedule. This field is unique within your organization

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method assigned to payments created from the payment schedule item. When
a payment schedule item is created, its `PaymentMethodId` inherits the payment
schedule’s `DefaultPaymentMethodId` . However, you can provide a new
`PaymentMethodId` at any time. If you change the `PaymentMethodId`, only payments
made after the change use the new account.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup


Standard Objects PaymentScheduleItem

**Field** **Details**

**Refers To**
CardPaymentMethod, DigitalWallet

```
PaymentProcessingMessage

PaymentsReceived

PaymentRunMatchingValue

PaymentScheduleId

PaymentScheduleItemNumber

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Shows information about whether the payment creation process has completed.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The payment received from the borrower for the payment schedule item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value used to match a payment schedule item to a payment run based on the payment
run’s matching criteria.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent payment schedule for the payment schedule item.

This is a relationship field.

**Relationship Name**
PaymentSchedule

**Relationship Type**
Lookup

**Refers To**
PaymentSchedule

**Type**
string


Standard Objects PaymentScheduleItem

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
User-defined reference number for the payment schedule item.

```
PaymentSource

PaymentsReceived

ProcessedAmount

RequestedAmount

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The feature that caused a payment to be created from the payment schedule item.

Possible values are:

**•** `PaymentRun`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The payment received from the borrower for the payment schedule item.

Available in API version 63.0 and later with Financial Services and Automotive Cloud.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the payment schedule item that has been processed for payment and
converted to a payment record.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The initial amount of the payment schedule item upon creation.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects PaymentScheduleItem

**Field** **Details**

**Description**
The status of the payment schedule item.

Possible values are:

**•** `Applied` : The payment schedule item has been successfully applied.

**•** `Apply Failed` : The payment run encountered an error when attempting to process
the payment schedule item for payment. For more information, review the payment
run’s revenue transaction error log.

**•** `Approval Pending` The payment schedule item is waiting for approval before it
can be processed by payment runs.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Canceled` : The payment schedule item can’t be picked up by payment runs for
processing. When a user or process changes the item’s status to Canceled, the item’s
`CanceledAmount` becomes `RequestedAmount`                  - `ProcessedAmount` .

**•** `Deferred Payment` The payment schedule item has been postponed and will be
processed at a later date.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**•** `Payment Waived Off` The payment schedule item has been canceled, and the
payment will not be processed.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

```
TargetPaymentProcessingDate

UsageType

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date after picking up a payment schedule item that the payment run makes a payment
request to the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the usage type for the record.

Possible value is:

**•** `CollectionPlan`

Available in API version 62.0 and later with Financial Services and Automotive Cloud.


### Standard Objects PaymentSchedulePolicy PaymentSchedulePolicy

Contains configuration information for the payment schedule policy. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and the PaymentScheduleAutomation permission, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentschedulepolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentschedulepolicy.htm)

Fields

**Field** **Details**

```
DefaultTreatmentId

Description

IsOrgDefault

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default payment schedule treatment.

This field is a relationship field.

**Relationship Name**
DefaultTreatment

**Relationship Type**
Lookup

**Refers To**
PaymentScheduleTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
User-entered description of the payment schedule policy.

**Type**
boolean


Standard Objects PaymentSchedulePolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
`true` if the payment schedule policy is the default policy for the org, otherwise `false` .
An org can have a maximum of one default payment policy.

The default value is `false` .

```
LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-entered name of the payment policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


### Standard Objects PaymentScheduleTreatment

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Status

TreatmentSelection

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The payment schedule policy’s status.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the payment schedule treatment.

Possible values are:

**•** `Default` —use the payment schedule treatment indicated by
`DefaultTreatmentId` .

### PaymentScheduleTreatment

Contains configuration information for the payment schedule. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).


Standard Objects PaymentScheduleTreatment

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduletreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_paymentscheduletreatment.htm)

Fields

**Field** **Details**

```
Description

IsApprovalRequired

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user-entered description of the payment schedule treatment.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this payment schedule treatment requires approval or not.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string


Standard Objects PaymentScheduleTreatment

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-entered name of the payment schedule treatment.

```
OwnerId

PaymentPlanTag

PaymentSchedulePolicyId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A list of key annotations or insights about the payment plan, such as requires approval or
recommended, to help guide the user in selecting the most suitable payment plan.

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related payment schedule policy.

This field is a relationship field.

**Relationship Name**
PaymentSchedulePolicy

**Relationship Type**
Lookup

**Refers To**
PaymentSchedulePolicy


### Standard Objects PendingOrderSummary

**Field** **Details**

```
Status

TriggerSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The payment schedule treatment’s status.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the action that caused the payment schedule treatment to be created.

Possible values are:

**•** `InvoicePosted` —an invoice is posted

**•** `UserAction` —User Action

Available in API version 65.0 and later with Financial Services and Automotive Cloud.

### PendingOrderSummary

Object representing a B2C Commerce order ingested via High Scale Orders before an OrderSummary is created for it. Optimized for
online transaction processing (OLTP). This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `query()`

Special Access Rules

This object is only available in Salesforce Order Management orgs where the High Scale Orders feature is enabled.


Standard Objects PendingOrderSummary

Fields

**Field** **Details**

```
AccountId

BillToContactId

BillingEmailAddress

BillingPhoneNumber

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account or person account associated with the PendingOrderSummary. It represents
the shopper in the storefront.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the PendingOrderSummary. It represents the shopper in
the storefront when not using person accounts.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
Email address on the billing address.

**Type**
phone


Standard Objects PendingOrderSummary

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Phone number of the billing address.

```
CurrencyIsoCode

Description

ExternalId

ExternalReferenceIdentifier

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the original Order associated with the PendingOrderSummary.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the PendingOrderSummary.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is used internally.

This field isn’t synced with ZOS, so you can’t use it in a query or insert operation.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects PendingOrderSummary

**Field** **Details**

**Description**
Used internally to prevent duplicate records. This value is case-sensitive. On creation, this
value is set to _`B2C realm ID`_ + "_" + _`B2C instance ID`_ + "@" + _`B2C Commerce`_
_`catalog/domain ID`_ + "@" + _`B2C Commerce order number`_ .

When the OrderSummary is created, this value is copied to its ExternalReferenceIdentifier
field. If you ingest orders from multiple sources, you can maintain uniqueness by including
a prefix based on the source.

```
GrandTotalAmount

OrderNumber

OrderedDate

Payload

PayloadType

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total amount, including adjustments and tax, of the PendingOrderSummary.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the PendingOrderSummary.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date of the original order associated with this PendingOrderSummary.

**Type**
textarea

**Properties**

**Description**
The order data payload.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The datatype of the Payload.


Standard Objects PendingOrderSummary

**Field** **Details**

Possible values are:

**•** `JSON_GZIP`

**•** `JSON_RAW`

ProcessingInstructions

```
SalesChannelId

SalesStoreId

```

**Type**
textarea

**Properties**
Nillable

**Description**
Instructions about how the HSOI service should create the order summary. Options include
using the default without customizations or using a custom flow.

Also includes instructions about how the HSOI service should dedupe account and contact
information using platform duplication and matching rules or by using simple email methods.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the SalesChannel associated with this PendingOrderSummary. The SalesChannel Name
matches the B2C Commerce catalog/domain ID.

This field is a relationship field.

**Relationship Name**
SalesChannel

**Relationship Type**
Lookup

**Refers To**
SalesChannel

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the RetailStore or WebStore associated with this PendingOrderSummary.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup


Standard Objects PendingOrderSummary

**Field** **Details**

**Refers To**
WebStore

```
ShopperName

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first name and last name of the shopper that placed the original order.

If you need to view or service an ingested B2C Commerce order before the automated High Scale Orders process has created an
OrderSummary for it, you can manually trigger creation of the OrderSummary. In Salesforce, open the PendingOrderSummaries list, find
the record, and click **Import** .

PendingOrderSummary only supports certain methods and queries. It doesn’t support Apex triggers.

Supported Apex Methods:

**•** `Database.query(` _**`queryString`**_ `)`

**•** `Database.query(` _**`queryString`**_ `,` _**`accessLevel`**_ `)`

Supported SOAP API Methods:

**•** `create()`

**•** `delete()`

**•** `describeLayout()`

**•** `query()`

**•** `queryMore()`

Supported REST API Methods:

**•** `/services/data/v` _**`XX.X`**_ `/sobjects/` _**`sObject`**_ `/ GET`

**•** `/services/data/v` _**`XX.X/`**_ `sobjects/` _**`sObject`**_ `/id/ GET`

**•** `/services/data/v` _**`XX.X`**_ `/sobjects/` _**`sObject`**_ `/id/ DELETE`

**•** `/services/data/v` _**`XX.X`**_ `/sobjects/` _**`sObject`**_ `/id/ POST`

**•** `/services/data/v` _**`XX.X`**_ `/sobjects/` _**`sObject`**_ `/describe/compactLayouts/ GET`

**•** `/services/data/v` _**`XX.X`**_ `/sobjects/` _**`sObject`**_ `/quickActions/ GET`

Supported Queries:

**convertCurrency() function**
Example: `SELECT Id, convertCurrency(AnnualRevenue) FROM Account`

**Child-to-Parent subquery**
Example: `SELECT ExternalReferenceIdentifier, Account.Name FROM PendingOrderSummary`

```
  WHERE ExternalReferenceIdentifier = 'a'

```


### Standard Objects PendingServiceRouting

**Limit clause**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`

```
    ExternalReferenceIdentifier = 'a' LIMIT 1

```

**Filter by index**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`

```
    ExternalReferenceIdentifier = 'a'

```

**Filter by secondary index**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE AccountId`

```
    = 'xxx'

```

**ORDER BY clause**
When using ORDER BY, you don’t need to specify a direction. However, if you sort ASC, you can’t use NULLS LAST. If you sort DESC,
you can only use NULLS LAST.

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`

```
    ExternalReferenceIdentifier

```

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`

```
    ExternalReferenceIdentifier ASC NULLS FIRST

```

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`

```
    ExternalReferenceIdentifier DESC NULLS LAST

```

**Equality filter**
Range filters aren’t supported.

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`

```
    ExternalReferenceIdentifier = 'realm_tenant@storesite@0000001'

```

Invalid example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`

```
    ExternalReferenceIdentifier < 'a'

```

SEE ALSO:

OrderSummary

Order

### PendingServiceRouting

Represents the routing details of a work item that’s waiting to be routed or assigned. This object is available in API version 40.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


Standard Objects PendingServiceRouting

Fields

**Field** **Details**

```
BotId

BotType

CapacityPercentage

CapacityWeight

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Enhanced Einstein Bot or AI agent that performed the work. This is a relationship
field. This field is available in API version 52.0 and later.

This field is a relationship field.

**Relationship Name**
Bot

**Relationship Type**
Lookup

**Refers To**
BotDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of bot. Valid values are:

**•** Bot. Refers to an Einstein bot.

**•** ExternalCopilot. Refers to an AI agent with whom your customers can interact.

The default value is Bot. This field is available in API version 63.0 and later.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Indicates the amount of work that this work item represents as a percentage. Valid values
are from 0 to 100.

Voice calls must have a capacity percentage of _`100`_ . If an agent receives a voice call, the
agent won’t receive new work items until the call ends, because at that point the agent’s
capacity will have reached 100%.

**Type**
double


Standard Objects PendingServiceRouting

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Indicates the amount of work that this work item represents as a whole number. Voice calls
must use the entire capacity weight.

```
CustomRequestedDateTime

DropAdditionalSkillsTimeout

ExternalBotId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Retains the datetime of this work item’s initial request, so work items are rerouted using the
datetime of the initial work request. When left blank, work items are rerouted using the
datetime when they’re rerouted.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Time to wait before a skill marked as additional is dropped from Omni-Channel routing. The
case is then routed to the best-matched agent even if they don’t have all the skills.

[If CustomRequestedDateTime is set in the PendingServiceRouting object,](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
DropAdditionalSkillsTimeout uses CustomRequestedDateTime as the start time. If
CustomRequestedDateTime + DropAdditionalSkillsTimeout has already passed, Omni-Channel
immediately drops the additional skills after the pending service request is created.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the third-party bot that handles the work item. This is a relationship field. This field
is available in API version 64.0 and later.

**Relationship Name**
ExternalBot

**Relationship Type**
Lookup

**Refers To**
ExternalConversationBotDef


Standard Objects PendingServiceRouting

**Field** **Details**

```
GroupId

IsInterruptible

IsOwnerChangeInitiated

IsPreferredUserRequired

IsPushAttempted

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Omni-Channel queue.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item consumes interruptible or primary capacity. The default value
is false. Available in version 57.0 and later when the Interruptible Capacity feature is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item owner change triggered the direct assignment of this work
item to the agent. The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item stays with the preferred user even when the user isn’t
available. The default value is `false` . This field is available in API version 50.0 and later.

When a specific agent is required, don’t set `PushTimeout` . These options aren’t supported
in this case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a push has been attempted. `true` if this work item was pushed to an
agent at least one time and `false` otherwise.


Standard Objects PendingServiceRouting

**Field** **Details**

```
IsPushed

IsReadyForRouting

IsStatusChangeInitiated

IsTransfer

LastDeclinedAgentSession

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item is pushed to an agent.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this work item is ready to be routed to an agent. If `true`, you can’t edit
this PendingServiceRouting record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item status change triggered the direct assignment of this work
item to the agent. The default value is `false` . This field is available in API version 50.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item routing is a transfer request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Chat session ID of the agent who last declined this work item.

**Type**
string


Standard Objects PendingServiceRouting

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PendingServiceRouting record.

```
OwnerId

PausedCapacityPercentage

PausedCapacityWeight

PreferredUserId

PushTimeout

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this PendingServiceRouting record.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of capacity that’s consumed when this work item is paused. The paused
capacity feature is available with status-based capacity and Enhanced Omni-Channel only.
This field is available in API version 62.0 and later.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The amount of capacity that’s consumed when this work item is paused. The paused capacity
feature is available with status-based capacity and Enhanced Omni-Channel only. This field
is available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the preferred user to handle the work item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PendingServiceRouting

**Field** **Details**

**Description**
The time limit set for an agent to respond to an item before it’s rerouted and the agent’s
status is changed accordingly. The time limit is measured in seconds. This field is available
in API version 36.0 and later.

Effective API version 57.0, for inbound Voice calls, this field represents the time limit set for
an agent to respond to a call before it’s declined. The value must be from 0 through 20. The
value is capped at 20, so any number greater than that is treated as 20 seconds. Latency on
the part of the telephony provider can result in agents having less than 20 seconds to answer
a call before it’s rerouted. When an agent attempts to answer a call within 20 seconds and
finds that the call was rerouted, the agent’s status remains unchanged. This scenario applies
to these telephony models.

**•** Service Cloud Voice with Amazon Connect

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

When `IsPreferredUserRequired` is set to true, don’t set this option. When a specific
agent is required, this option isn’t supported.

```
QueueId

RoutingModel

RoutingPriority

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Omni-Channel queue. Due to API changes, `QueueId` is no longer recommended.
Use `GroupId` instead.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of routing model.

Possible values are:

**•** `ExternalRouting`

**•** `LeastActive`

**•** `MostAvailable`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PendingServiceRouting

**Field** **Details**

**Description**

Order in which work items are routed to agents. This field is considered with skills-based
routing only. Queue-based routing sets a work item's priority from the routing configuration.

```
RoutingType

SecondaryRoutingPriority

Serial

ServiceChannelId

TransferRequesterId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates whether the work item is routed by queue or by skills-based routing.

Possible values are:

**•** `QueueBased`

**•** `SkillsBased`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the secondary routing priority.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Serial number of the PendingServiceRouting record. The serial number is automatically
incremented each time the PendingServiceRouting record is modified.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service channel.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PendingServiceRouting

**Field** **Details**

**Description**
The user ID of the rep who reassigned the work using the Reassign action. This field is
populated in reassigned AgentWork records only, not the original AgentWork record. This
is a relationship field. This field is available in API version 63.0 and later.

**Relationship Name**
TransferRequester

**Relationship Type**
Lookup

**Refers To**
User

```
WorkItemId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the work item.

**Refers To**
Custom objects and these standard objects: Account, Activity, Case, Claim, ClaimCoverage,
ClaimRecovery, Contact, ContactRequest, CustomEntityData, Incident, Lead,
LiveChatTranscript, MessagingSession, Opportunity, Orchestration Work Items, Order, Order,
PaymentRequest, PersonTraining, Referral, SocialPost, SwarmMember, and VoiceCall.
WorkOrder is available in version 58.0 and later.

When you use the PendingServiceRouting object for queue-based routing, the object doesn’t invoke triggers before or after insert, or
any action (trigger, workflow rule, validation) that could interfere with the creation of the record.

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**PendingServiceRoutingChangeEvent (API version 62.0)**
Change events are available for the object.

**PendingServiceRoutingOwnerSharingRule**

Sharing rules are available for the object.

**PendingServiceRoutingShare**

Sharing is available for the object.


### Standard Objects PendingServiceRoutingInteractionInfo

Limits

You can view the number of Pending Service Routing records that are currently in use in your org, as well as the current hourly use rate.
From Setup, enter _`Omni-Channel`_ in the Quick Find box and select **Limits** . The Limits page also displays the current Pending Service
Routing record usage percentage and the Pending Service Routing record limits for your org.

### PendingServiceRoutingInteractionInfo

Represents PendingServiceRouting interaction information that’s used when work is routed to an agent. For a screen pop, it specifies
which records to open when work is routed to an agent from a specific channel. PendingServiceRoutingInteractionInfo is read-only. This
object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled. To view this object, you must have the “Manage Flow” user permission.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
IsFocused

Name

PendingServiceRoutingId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this record shows on the agent’s screen when multiple records open at
the same time.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the PendingServiceRoutingInteractionInfo.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects PendingServiceRoutingInteractionInfo

**Field** **Details**

**Description**
The ID of the PendingServiceRouting on page 4102 from which the AgentWork on page 465
is created.

This is a relationship field.

**Relationship Name**
PendingServiceRouting

**Relationship Type**
Lookup

**Refers To**
PendingServiceRouting

```
PrimaryRecordId

TargetFlowName

TargetObjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the object that’s routed to the agent through Omni-Channel.

**Relationship Name**
PrimaryRecord

**Relationship Type**
Lookup

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name and namespace prefix, if any, of the screen flow to open when work is routed
to the agent. This field and the `TargetFlowId` field can't be populated at the same time.
Available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record to open when work is routed to the agent. This field is required in API version
56.0 and earlier. In API version 57.0 and later, this field is optional and can’t be populated at
the same time as the `TargetFlowName` field.

**Relationship Name**
TargetObject


### Standard Objects Period

**Field** **Details**

**Relationship Type**
Lookup

### Period

Represents a fiscal period defined in FiscalYearSettings.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only Chatter Free users and standard users can access this object.

Fields

**Field** **Details**

```
EndDate

FiscalYearSettingsId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The last date of the fiscal period.

**Type**
reference

**Properties**
Filter, Nillable, Group, Sort

**Description**
The parent record for this period.

This is a relationship field.

**Relationship Name**
FiscalYearSettings

**Relationship Type**
Lookup

**Refers To**
FiscalYearSettings


Standard Objects Period

**Field** **Details**

```
FullyQualifiedLabel

IsForecastPeriod

Number

PeriodLabel

QuarterLabel

StartDate

```

**Type**
string

**Properties**
Group, Nillable

**Description**
Represents the period’s complete name in the UI. For example, “September FY 2016”.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the period is associated with Salesforce Forecasting ( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
If the labeling scheme of your fiscal year's quarters or months is numbered, this field indicates
the relative number of the row.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the months in your fiscal year use custom names, then this field contains the appropriate
name for rows of type Month.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
If the quarters in your fiscal year use custom names, then this field contains the appropriate
name for rows of type Quarter.

**Type**
date

**Properties**
Filter, Group, Sort


### Standard Objects PermissionSet

**Field** **Details**

**Description**
The first date of the fiscal period.

```
 Type

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the period is of type Month, Quarter, Week, or Year. Label is the field value.

In API version 36.0 and earlier, querying the Period object yields no results. In API version 37.0 and later, a query returns period records.

SEE ALSO:

FiscalYearSettings

### PermissionSet

Represents a set of permissions that’s used to grant more access to one or more users without changing their profile or reassigning
profiles. This object is available in API version 22.0 and later.

### PermissionSet has a read-only child relationship with PermissionSetGroup. PermissionSet contains the aggregated permissions for the

group.

You can use permission sets to grant access, but not to deny access.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

**•** Manage Profiles and Permission Sets

To view the following settings, assignments, and permissions for standard and custom objects in a specified permission set, the View
Setup and Configuration permission is required.

**•** Client settings

**•** Field permissions


Standard Objects PermissionSet

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Fields

**Field Name** **Details**

```
Description

HasActivationRequired

IsCustom

IsOwnedByProfile

Label

```

**Type**
string

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
A description of the permission set. Limit: 255 characters.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the permission set requires an associated active session ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the permission set is custom (created by an admin); if `false`, the permission set
is standard and related to a specific permission set license.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the permission set is owned by a profile. Available in API version 25.0 and later.

**Type**
string


Standard Objects PermissionSet

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The permission set label, which corresponds to **Label** in the user interface. Limit: 80 characters.

```
LicenseId

Name

NamespacePrefix

Permissions PermissionName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of either the related PermissionSetLicense or UserLicense associated with this
permission set. Available in API version 38.0 and later. Use this field instead of
`UserLicenseId`, which is deprecated and only available up to API Version 37.0.

This is a polymorphic relationship field.

**Relationship Name**
License

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicense, UserLicense

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your organization. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. Corresponds to **API Name** in the user interface. Limit: 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for a permission set that's been installed as part of a managed package.
If the permission set isn't packaged or is part of an unmanaged package, this value is empty.
Available in API version 23.0 and later.

**Type**
boolean


Standard Objects PermissionSet

**Field Name** **Details**

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true`, users assigned to this permission set have the named
permission. The number of fields varies depending on the permissions for the organization
and license type. To get a list of available permissions in the SOAP API, use
`describeSObjects()` .

```
PermissionSetGroupId

ProfileId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the permission set is owned by a permission set group, this field returns the ID of the
permission set group. If the permission set isn’t owned by a permission set group, this field
returns a null value. Available in API version 45.0 and later.

This is a relationship field.

**Relationship Name**
PermissionSetGroup

**Relationship Type**
Lookup

**Refers To**
PermissionSetGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the permission set is owned by a profile, this field returns the ID of the Profile. If the
permission set isn’t owned by a profile, this field returns a null value. Available in API version
25.0 and later.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
reference


Standard Objects PermissionSet

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available in API version 46.0 and later.

```
UserLicenseId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the UserLicense associated with this permission set. This field is nillable in API version
26.0 and later and available up to API version 37.0 In API version 38.0 and later, use
`LicenseId` .

Use the PermissionSet object to query existing permission sets.

For example, to search for all permission sets that contain the “Modify All Data” permission:

```
SELECT Name, PermissionsModifyAllData

FROM PermissionSet

WHERE PermissionsModifyAllData=true

```

When combined with the PermissionSetAssignment object, you can create a nested query that returns all users assigned to a particular
permission like “Modify All Data”:

```
SELECT Name, (SELECT AssigneeId FROM Assignments)

FROM PermissionSet

WHERE PermissionsModifyAllData=true

```

If the permission set isn’t assigned to a user, you can also create or delete a permission set.

User Licenses

The user license controls the permissions that are available in a permission set.

Every permission set can be associated with a user license or permission set license. If you plan to assign a permission set to multiple
users with different user and permission set licenses, leave `LicenseId` empty. If only users with one type of license use this permission
set, set the `LicenseId` to that single user or permission set license. If you want a permission set associated with a permission set
license, then set `LicenseId` to the permission set license. To get the `LicenseId`, run this query:

```
SELECT Id, Name

FROM UserLicense

```

Alternatively, to query a user or profile for the `LicenseId` .

```
SELECT Id, Profile.UserLicenseId

FROM User

```


Standard Objects PermissionSet

Child Objects

When using the API, think of each permission set or related set of access controls as an empty container that you fill with permission
records.

In the API, a permission set can contain user, object, and field permissions, and setup entity access settings for other settings, such as
Apex classes.

**•** ObjectPermissions and FieldPermissions objects are available in API version 24.0 and later.

**•** The SetupEntityAccess object is available in API version 25.0 and later.

**•** The PermissionSetGroupComponent object is available in API version 45 and later.

Only user permissions are managed in the PermissionSet API object; all other permission types are managed in child API objects.

In these child objects, access is stored in a record, while the absence of a record indicates no access. To return a record in a SOQL query,
a minimum permission or setting is required for each child object.

Because permissions are stored in related objects, it’s important to understand what questions to ask when using SOQL. For example,
let’s say you want to know which permission sets have “Delete” on an object. You also want to know which ones include permissions
that allow approval of a return merchandise authorization (where the approval checkbox is controlled with field permissions). Asking
the right questions when using SOQL with permission sets ensures that you get the information you need, such as whether to migrate
permissions or assign a permission set to a user.

For example, the following returns all permission sets where the “Read” permission is enabled for the Merchandise__c object.

```
   SELECT SobjectType, ParentId, PermissionsRead

   FROM ObjectPermissions

   WHERE PermissionsRead = True AND SobjectType = 'Merchandise__c'

```

You can query for all permission sets that have “Read” on an object. However, you can’t query for permission sets that have no access
on an object, because no records exist for that object. For example, the following returns no records because the object must have at
least “Read” to return any records.

```
   SELECT SobjectType, ParentId, PermissionsRead

   FROM ObjectPermissions

   WHERE PermissionsRead = False AND SobjectType = 'Merchandise__c'

```

If you have at least the “Read” permission on an object, you can create a conditional query on other permissions in the same object. For
example, the following returns any records where the object has at least the “Read” permission but not the “Edit” permission.

```
   SELECT ParentId, PermissionsRead, PermissionsEdit

   FROM ObjectPermissions

   WHERE PermissionsEdit = False AND SobjectType = 'Merchandise__c'

```

To set an object or field permission to no access, delete the record that contains the permission. For example, to disable all object
permissions in the Merchandise__c object for a particular permission set, first query to retrieve the ID of the object permission record.

```
   SELECT Id

   FROM ObjectPermissions

   WHERE SobjectType = 'Merchandise__c'

```

Then delete the IDs returned from the query.

Note: If you try to update the object or field permissions by setting all permissions to false, the permission record is automatically
deleted. Any subsequent queries for the record ID won’t return results and you must add a new permission record to grant access.


Standard Objects PermissionSet

View a Permission Set with Nested Queries

You can build on the PermissionSet object using child relationships that show all of the permissions in a single permission set. For
example, the following returns all permission sets and displays the “Transfer Leads” permission, as well as any “Read” permissions on
any objects and fields.

```
   SELECT Label, PermissionsTransferAnyLead,

   (SELECT SobjectType, PermissionsRead FROM ObjectPerms),

   (SELECT SobjectType, Field, PermissionsRead FROM FieldPerms)

   FROM PermissionSet

```

Associated Profiles

In API version 25.0 and later, every profile is associated with a permission set that stores the profile’s user, object, and field permissions,
as well as setup entity access settings. You can query permission sets that are owned by profiles but not modify them.

The following example returns all permission sets, including those owned by a profile.

```
   SELECT Id, Label, ProfileId, Profile.Name

   FROM PermissionSet

```

The following returns all permission sets except those permissions owned by profiles.

```
   SELECT Id, Label, ProfileId, Profile.Name, IsOwnedByProfile

   FROM PermissionSet

   WHERE IsOwnedByProfile = FALSE

```

Because permission sets have child objects in the API, you can query their values on permission sets owned by a profile. For example,
the following returns all enabled object permission records for profiles only.

```
   SELECT Id,ParentId, PermissionsRead, SobjectType, Parent.ProfileId

   FROM ObjectPermissions

   WHERE Parent.IsOwnedByProfile = TRUE

```

Once you have the IDs for permission sets that are owned and not owned by profiles, use the PermissionSetAssignment object to see
if users can access objects or fields via their profile permissions or their permission sets. For example, the following SOQL query returns
all users who have the “Read” permission on the Merchandise__c object. It also specifies whether the permission is granted through a
profile or permission set.

```
   SELECT Assignee.Name, PermissionSet.Id, PermissionSet.isOwnedByProfile

   FROM PermissionSetAssignment

   WHERE PermissionSetId

   IN (SELECT ParentId

   FROM ObjectPermissions

   WHERE SObjectType = 'Merchandise__c' AND PermissionsRead = true)

```


### Standard Objects PermissionSetAssignment

Note: For permission sets that are owned by profiles, don’t use Name and Label values that are returned in a query. Name and
Label values from queries can change.

SEE ALSO:

ObjectPermissions

FieldPermissions

SetupEntityAccess

### PermissionSetAssignment

Profile

### PermissionSetAssignment

Represents a user’s assignment to a permission set or permission set group. This object is available in API version 22.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Assign Permission Sets

**•** Manage User

Fields

**Field Name** **Details**

```
AssigneeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that is assigned the permission set indicated in `PermissionSetId`
or the permission set group indicated in `PermissionSetGroupId` .

This is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup


Standard Objects PermissionSetAssignment

**Field Name** **Details**

**Refers To**
User

```
ExpirationDate

IsActive

IsRevoked

LastCreatedByChangeId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the assignment of the permission set or permission set group expires for the
specified user. This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the assignment is active ( `true` ) or not ( `false` ). Defaults to `false` .
This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the assignment was revoked ( `true` ) or not ( `false` ). Defaults to `false` .
This field is available only if user access policies are enabled. This field is available in API
version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user access change record related to this permission set or permission set group
assignment. This field is available only if user access policies are enabled. This field is available
in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup


Standard Objects PermissionSetAssignment

**Field Name** **Details**

**Refers To**
UserAccessChange

```
LastDeletedByChangeId

PermissionSetGroupId

PermissionSetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user access change record related to this permission set or permission set group
assignment being revoked. This field is available only if user access policies are enabled. This
field is available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the permission set group assigned to the user specified in `AssigneeId` . This
field is available in API version 45.0 and later.

This is a relationship field.

**Relationship Name**
PermissionSetGroup

**Relationship Type**
Lookup

**Refers To**
PermissionSetGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the permission set assigned to the user specified in `AssigneeId` .

This is a relationship field.


Standard Objects PermissionSetAssignment

**Field Name** **Details**

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet

Usage

**Finding Permission Set Assignments**
Use the PermissionSetAssignment object to query permission set assignments to find out which permission sets are assigned to
which users. Because each user can be assigned to many permission sets and each permission set can be assigned to many users,
each PermissionSetAssignment ID represents the association of a single user and single permission set.

For example, to search for all permission sets assigned to a particular user:

```
     SELECT Id, PermissionSetId

     FROM PermissionSetAssignment

     WHERE AssigneeId = '005600000017cKt'

```

To search for all users assigned to a particular permission set:

```
     SELECT Id, AssigneeId

     FROM PermissionSetAssignment

     WHERE PermissionSetId = '0PS30000000000e'

```

You can also create a new permission set assignment, or use delete to remove a permission set that's assigned to a user. To update
an assignment, delete an existing assignment and insert a new one.

**User Licenses**
When assigning a permission set, if the PermissionSet has a `UserLicenseId`, its `UserLicenseId` and the Profile
`UserLicenseId` must match. To determine a user's license assignment, query the user's profile and then query the profile's
license.

For example, to find a user's profile ID:

```
     SELECT Id, ProfileId

     FROM User

     WHERE Id = '005D0000001GMAT'

```

To find a permission set's `UserLicenseId` :

```
     SELECT Id, LicenseId

     FROM PermissionSet

     WHERE Id = '0PS30000000000e'

```

If the IDs match, the assignment succeeds.


### Standard Objects PermissionSetGroup

To find all the permission sets with no license that are assigned to any user:

```
     SELECT Id, Assignee.Name, PermissionSet.Name

     FROM PermissionSetAssignment

     WHERE PermissionSet.LicenseId = null

```

**Revoked Assignments from User Access Policies**
After you revoke a permission set or permission set group assignment via a user access policy, the `IsRevoked` field is updated
to `true` . The PermissionSetAssignment record isn’t deleted. If the permission set or permission set group is assigned to the user
again, the `IsRevoked` field is then updated to `false` .

To find permission set or permission set group assignments that were revoked:

```
     SELECT Id, ExpirationDate, Assignee.Name, PermissionSet.Name

     FROM PermissionSetAssignment

     WHERE IsRevoked=true ALL ROWS

```

SEE ALSO:

### PermissionSet PermissionSetGroup

Represents a group of permission sets and the permissions within them. Use permission set groups to organize permissions based on
job functions or tasks. Then, you can package the groups as needed. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeObject()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, to view this object, users must have one of these permissions:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

To edit this object, users must have the Manage Profiles and Permission Sets permission.

Fields

**Field Name** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PermissionSetGroup

**Field Name** **Details**

**Description**
The Permission Set Group description.

```
DeveloperName

HasActivationRequired

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The permission set group name used in the API.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the permission set group requires an associated active session ( `true` ) or
not ( `false` ). The default value is `false` . This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The Permission Set Group language.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)


Standard Objects PermissionSetGroup

**Field Name** **Details**

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

```
MasterLabel

NamespacePrefix

Status

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The permission set group label for the aggregated permissions.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The permission set group namespace prefix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates permission set group recalculation status.

**•** `Updated` . The group is current.

**•** `Outdated` . The group requires recalculation.

**•** `Updating` . The group is in recalculation mode.

**•** `Failed` . The group recalculation failed.

Use the PermissionSetGroup object to query existing permission set groups and to find which aggregated permissions are included in
the group.

For example, to search for all object permissions in a permission set group named StandardAccountingUsers:

```
SELECT SObjectType

FROM ObjectPermissions

WHERE Parent.PermissionSetGroup.DeveloperName = 'StandardAccountingUsers'

```

To create a permission set group using REST API, you can submit a POST request.

```
POST

/services/data/v45.0/tooling/sobjects/PermissionSetGroup/

```


### Standard Objects PermissionSetGroupComponent

```
   {

      "DeveloperName":"Sales", "MasterLabel": "sales_label"

   }

### PermissionSetGroupComponent

```

A junction object that relates the PermissionSetGroup and PermissionSet objects via their respective IDs; enables permission set group
recalculation to determine the aggregated permissions for the group. This object is available in API version 45.0 and later.

### PermissionSetGroupComponent is a child object of PermissionSet and PermissionSetGroup.

Supported Calls

`create()`, `delete()`, `describeSObject()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with the "View Setup and Configuration" permission can access this object.

Fields

**Field Name** **Details**

```
PermissionSetGroupId

PermissionSetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique permission set group ID.

This is a relationship field.

**Relationship Name**
### PermissionSetGroup

**Relationship Type**
Lookup

**Refers To**
### PermissionSetGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique permission set ID of a permission set in a permission set group.


### Standard Objects PermissionSetLicense

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
### PermissionSet

**Relationship Type**
Lookup

**Refers To**
### PermissionSet

Usage

Use the PermissionSetGroupComponent object to add members to or delete members from a permission set group, or to query for
group members.

### PermissionSetLicense

Represents a license that’s used to enable one or more users to receive a specified permission without changing their profile or reassigning
profiles. You can use permission set licenses to grant access, but not to deny access. This object is available in API version 29.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is


Standard Objects PermissionSetLicense

**Field Name** **Details**

specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
ExpirationDate

IsAvailableForIntegrations

```

`IsSupplementLicense` (Developer
Preview)

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date at which the permission set license expires.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the permission set license is enabled for integrations ( `true` )
or not ( `false` ). When this field is set to `true`, Salesforce integration features
can access data. The default value is `false` . This field is read-only in the API
and can be edited only in Setup.

If integrations are required for feature functionality and the license isn't enabled
for integrations, you receive an error when setting up the session-based
permission set or executing the feature. Only enable integrations if necessary for
the feature.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a custom permission set license is a supplement license ( `true` )
or a foundation license ( `false` ). The default value is `false` .

This field is only available if the Partner Licensing Platform developer preview is
enabled. This field is available in API version 55.0 and later.

Note: The Partner Licensing Platform is available as a developer preview.
The Partner Licensing Platform isn’t generally available unless or until
Salesforce announces its general availability in documentation or in press
releases or public statements. All commands, parameters, and other
features are subject to change or deprecation at any time, with or without
notice. Don't implement functionality developed with these commands
or tools in your production package.


Standard Objects PermissionSetLicense

**Field Name** **Details**

```
Language

MasterLabel

MaximumPermissions PermissionName

PermissionSetLicenseKey

Status

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language of the permission set license.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the permission set license. Label is **Permission Set License Label** .

**Type**
boolean

**Properties**
Filter

**Description**
One field for each permission. For example,
`MaximumPermissionsIdentityConnect` corresponds to the “Use
Identity Connect” permission.

If _`true`_, this PermissionSetLicense grants the specified permission. The number
of fields varies depending on the permissions available for the organization.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A string that uniquely identifies a particular permission set license.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a permission set license. If `Active`, the permission set license is
available. If `Disabled`, the permission set license has expired.


### Standard Objects PermissionSetLicenseAssign

**Field Name** **Details**

```
TotalLicenses

UsedLicenses

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of this permission set license that are available to your
organization.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of this permission set license that are currently assigned to users.

Users with the “View Setup and Configuration” permission can use the PermissionSetLicense object to view the set of currently defined
permission set licenses in your organization.

Use the PermissionSetLicense object to query existing permission licenses.

For example, to return a list of all active permission set licenses:

```
SELECT MasterLabel

FROM PermissionSetLicense

WHERE Status = 'Active'

```

When combined with the PermissionSetLicenseAssign object, you can create a nested query that returns all users assigned to a particular
permission set license like “Identity Connect”:

```
SELECT MasterLabel, (SELECT AssigneeId FROM PermissionSetLicenseAssign)

FROM PermissionSetLicense

WHERE MaximumPermissionsIdentityConnect=true

```

SEE ALSO:

### PermissionSetLicenseAssign PermissionSetLicenseAssign

Represents the association between a User and a PermissionSetLicense. This object is available in API version 29.0 and later.

### Note: The relationship name for PermissionSetLicenseAssign is PermissionSetLicenseAssignments .


Standard Objects PermissionSetLicenseAssign

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Assign Permission Sets

Fields

**Field Name** **Details**

```
AssigneeId

IsRevoked

LastCreatedByChangeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User to assign the permission set license specified in
`PermissionSetLicenseId` .

This is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Reserved for internal use. This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PermissionSetLicenseAssign

**Field Name** **Details**

**Description**
ID of the user access change record related to this permission set license
assignment. This field is available only if user access policies are enabled. This
field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

```
LastDeletedByChangeId

PermissionSetLicenseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user access change record related to this permission set license
assignment being revoked. This field is available only if user access policies are
enabled. This field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the permission set license the user is assigned to.

This is a relationship field.

**Relationship Name**
PermissionSetLicense

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicense


### Standard Objects PermissionSetLicenseDefinition (Developer Preview)

Usage

Use the PermissionSetLicenseAssign object for querying permission set license assignments to find out which permission set licenses
are assigned to which users. Because each user can be assigned to many permission set licenses, each PermissionSetLicenseAssign ID
represents the association of a single user and single permission set license.

For example, to search for all of the permission sets assigned to a particular user:

```
   SELECT Id, PermissionSetLicenseId

   FROM PermissionSetLicenseAssign

   WHERE AssigneeId = '005D0000001RFek'

```

To search for all users assigned to a particular permission set license:

```
   SELECT AssigneeId

   FROM PermissionSetLicenseAssign

   WHERE PermissionSetLicenseId = '0PLD000000003mwOAA'

```

You can also create a new permission set license assignment, or use delete to remove a permission set license that’s been assigned to
a user. To update an assignment, delete an existing assignment and insert a new one.

SEE ALSO:

### PermissionSetLicense PermissionSetLicenseDefinition (Developer Preview)

Represents the definition of a custom permission set license, which entitles specified features in a package. This object is available in API
version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access PermissionSetLicenseDefinition, you must have the Partner Licensing Platform developer preview enabled. To participate in
[this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community group.](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects PermissionSetLicenseDefinition (Developer Preview)

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters and must be unique in your organization. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed package
and the changes are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
IsSupplementLicense

Language

LicenseExpirationPolicy

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the custom permission set license is a supplement license ( `true` ) or a
foundation license ( `false` ). The default value is `false` . This field is available in API version
55.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The two- to five-character code that represents the language and locale ISO. This code
controls the language for labels displayed in an application.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The license expiration policy of the custom permission set license.

Possible values are:

**•** `BlockNamespaceAccess` —Package access is blocked for existing users when all
custom permission set licenses expire. This is the default value.

**•** `AllowNamespaceAccess` —Package access isn’t blocked for existing users when
all custom permission set licenses expire.

This field is available in API version 55.0 and later.


Standard Objects PermissionSetLicenseDefinition (Developer Preview)

**Field** **Details**

```
MasterLabel

NamespacePrefix

UserLicenseRestrictions

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this PermissionSetLicenseDefinition value. This display value is the internal label
that does not get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The user license categories that can be assigned the custom permission set license. If no
user license categories are specified, all users can be assigned the license. Possible values
include:

**•** `${communities}`

**•** `${communitiesLogin}`

**•** `${customerCommunities}`

**•** `${customerCommunitiesLogin}`

**•** `${internal}`

**•** `${partnerCommunity}`

**•** `${partnerCommunityLogin}`


### Standard Objects PermissionSetTabSetting

**Field** **Details**

**•** `${platform}`

[For more information, see User License Restriction Categories (Developer Preview). This field](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/partner_licensing_platform_restriction_categories.htm)
is available in API version 55.0 and later.

Usage

After the PermissionSetLicenseDefinition is created, it must be referenced in LicenseDefinitonCustomPermission.

[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.260.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)

### PermissionSetTabSetting

Represents a permission set tab setting. Requires the View Setup permission. Use this object to query all tab settings of the permission
set. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only users with "View Setup and Configuration" permission can access this object.

Fields

**Field Name** **Details**

```
Name

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The tab name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The permission set Id.

This is a relationship field.


### Standard Objects PersnlBatchDecision

**Field Name** **Details**

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

```
Visibility

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the tab is visible by default. Possible values are:

**•** `DefaultOff`

**•** `DefaultOn`

Use the PermissionSetTabSetting object to find tab setting visibility settings, parent permission sets, and so forth.

For example, to find the visibility setting of a tab named “standard-Lead,” do something like the following.

```
SELECT Visibility

FROM PermissionSetTabSetting

WHERE Name = 'standard-Lead'

### PersnlBatchDecision

```

Represents a batch personalization that delivers personalization decisions (content or recommendations) to a customer segment.
Available in API version 64.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
ActivationTriggerType

```

**Type**
picklist


Standard Objects PersnlBatchDecision

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of trigger that activates the batch personalization decision. The default value is `None`
and possible values are:

**•** `Automatic` —Automatically On Job Completion

**•** `None`

```
BatchStatus

DataSpaceId

Description

DeveloperName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the batch personalization decision. The default value is `Active` and possible
values are:

**•** `Active`

**•** `Error`

**•** `Paused`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the data space from where batch personalization decision resources originate.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the batch personalization decision.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PersnlBatchDecision

**Field** **Details**

**Description**
The unique name of the batch personalization decision in the API.

```
ErrorCode

RefreshMode

Name

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The issue that’s causing an error. The default value is `None` and possible values are:

**•** `ConfigurationMissingError` —A required configuration setting is missing.

**•** `DpcJobError` —A problem occurred during processing.

**•** `Internal Error` —An internal error occurred during processing.

**•** `ModelValidationError` —The model is invalid.

**•** `None`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the batch personalization data is refreshed. The default value is `FULL_REFRESH`
and possible values are:

**•** `FULL_REFRESH` —Generates new decisions for all members in a segment.

**•** `INCREMENTAL` —Generates decisions only for the new members added to the segment
after the last run.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The name of the batch personalization decision.

PersnlBatchDecision provides details about refresh modes, model versions, and refresh states for specific market segments.


### Standard Objects PersonAccountOwnerPowerUser PersonAccountOwnerPowerUser

Represents a user who can own more than 50,000 customer or partner portal accounts. Person account owner power users can own a
large number of either customer or partner users. Their role can’t be changed and they must be at the root of the role hierarchy. Person
account owner power user objects can't be created if deferred sharing is turned on for your org. Person account owner power user
objects can be created while deferred sharing is turned off for an org. Deferred sharing can be turned back on after person account
owner power user objects have been created. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Create a PersonAccountOwnerPowerUser object. Enter the user ID of the power user and the type of users that they can own, `Customer`
`Portal` or `Partner` .

Note: Only users at the highest level of a hierarchy can be added to the PersonAccountOwnerPowerUser object.

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language that the user’s account is set to. The user is specified using the `UserId` field.

See Salesforce Help for a full list of languages.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label entered when the person account owner power user is created.


### Standard Objects PersonalOrgInfo

**Field** **Details**

```
PortalType

UserId

### PersonalOrgInfo

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of portal user account that the person account owner power user can own.

A possible value is:

**•** `CustomerPortal` —Customer Portal

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID associated with the person account owner power user.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents the information for a Tableau Next personal org. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.


Standard Objects PersonalOrgInfo

Fields

**Field** **Details**

```
DeletedBy

DeletedDate

Description

Details

ErrorCode

IsPersonalOrgDeleted

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID that deleted the personal org.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the personal org was deleted.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The description for the personal org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The details for the personal org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code for the personal org.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update


Standard Objects PersonalOrgInfo

**Field** **Details**

**Description**
Indicates whether the personal org is deleted ( `true` ) or not ( `false` ).

The default value is `false` .

```
LastReferencedDate

LastViewedDate

Name

OrgName

PersonalOrg

PrimaryOrgUser

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the personal org was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the personal org was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the personal org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the personal org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the personal org.

**Type**
string


Standard Objects PersonalOrgInfo

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The email for the primary user of the personal org.

```
PrimaryOrgUserIdentifier

SignupCountry

SignupEmail

SignupInstance

SignupLanguage

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user ID for the primary user of the personal org.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The country of the personal org signup.

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
The user email used for personal org signup.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce org instance used for personal org signup.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language used for personal org setup.

Possible values are:

**•** `da` —Danish


Standard Objects PersonalOrgInfo

**Field** **Details**

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
SignupUsername

SourceType

Status

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user name used for personal org signup.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the personal org.

Possible values are:

**•** `TableauEinstein` —Tableau Next

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the personal org.


### Standard Objects PersonalizationDecision

**Field** **Details**

Possible values are:

**•** `Active`

**•** `Creating`

**•** `Deleted`

**•** `Error`

**•** `New`

The default value is `New` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PersonalOrgInfoFeed on page 55**
Feed tracking is available for the object.

**PersonalOrgInfoHistory on page 63**
History is available for tracked fields of the object.

### PersonalizationDecision

Represents a set of targeting rules within a personalization point that determine an individual's eligibility to receive personalized content
and the content to deliver. Available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
CurrencyIsoCode

DataSpaceId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
reference


Standard Objects PersonalizationDecision

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space from where a personalization decision's
resources originate. This is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Description

DeveloperName

Name

PersonalizationPointId

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the personalization decision. This is an optional field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization decision. This is a required field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization decision.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to a personalization point.

**Relationship Name**
PersonalizationPoint

**Relationship Type**
Primary-detail


Standard Objects PersonalizationDecision

**Field** **Details**

**Refers To**
PersonalizationPoint (the primary object)

```
PersonalizerId

```

Priority

State

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the personalizer service called at runtime, which retrieves the
necessary information for a decision response.

**Relationship Name**
Personalizer

**Refers To**
PersonalizationRecommender

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the order in which personalization decisions are evaluated. If an individual qualifies
for multiple decisions, the one with the highest priority is returned. The possible values are
positive integers such as 1, 2, and 3.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the state of the decision. The default value is `Draft`, and
accepted values are Draft and Live. Personalization evaluates only live decisions.

Use this object for defining and managing personalized responses. It includes targeting rules to determine eligibility and specifies the
content to return, such as product recommendations.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.


### Standard Objects PersonalizationObjective

**[PersonalizationDecisionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationDecisionFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationDecisionHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationDecisionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationDecisionShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### PersonalizationObjective

Represents a specific business outcome that you want to achieve when creating a recommender. Available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
CurrencyIsoCode

DataSpaceId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where an objective's resources originate. This
is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace


Standard Objects PersonalizationObjective

**Field** **Details**

```
Description

DeveloperName

LastReferencedDate

LastViewedDate

Name

```

Usage

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the personalization objective. This is an optional field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization objective. This is a required field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the personalized objective was referenced by another
resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the personalization objective.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization objective.

Use this object to define a business objective. The personalized, targeted recommendations generated using deep learning algorithms
are intended to help achieve this objective. For example, the objective “maximizing revenue” can return recommendations that aim to
increase checkout frequency, increase cart value at checkout, or both.


### Standard Objects PersonalizationPoint

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[PersonalizationObjectiveChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationObjectiveFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationObjectiveHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationObjectiveOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationObjectiveShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### PersonalizationPoint

Represents a specific touch point in an experience where a personalization decision can be made. It connects a data space, profile data
graph, personalization type, and response template to deliver personalized content at that time in a customer journey. Available in API
version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

AbnExperimentId

```
CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to a related experiment.

**Relationship Name**
AbnExperiment

**Refers To**
AbnExperiment

**Type**
picklist


Standard Objects PersonalizationPoint

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

```
DataSpaceId

Description

DeveloperName

```

IsAuthenticationRequired

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where a personalization point's resources
originate. This is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the personalization point. This is an optional field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization point. This is a required field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the personalization point must use authenticated endpoints for real-time
data capture and recommendation requests. When set to `true`, all interactions with Data
Cloud are secured and verified.

The default value is `false` .


Standard Objects PersonalizationPoint

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MaxItemsCount

Name

PersonalizationSchemaEnum

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the personalized point was referenced by another
resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the personalization point.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the maximum number of recommendations to return.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization point.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the type of personalization schema, which is related to where a
personalization decision is created. The accepted values are

**•** DecisionDefined

**•** ExperienceVariation

**•** FlowPath


Standard Objects PersonalizationPoint

**Field** **Details**

```
PersonalizationSchemaId

```

ProfileDataGraphId

RootPersonalizationPoint

Source

SourceRecordId

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the schema that’s related to the personalization point.

**Relationship Name**
PersonalizationSchema

**Refers To**
PersonalizationSchema

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the profile data graph that’s used with the personalization
point.

**Relationship Name**
ProfileDataGraph

**Refers To**
DataGraph

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the personalization point from where data is gathered.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the personalization point from where data is gathered.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PersonalizationPoint

**Field** **Details**

**Description**
Unique identifier that refers to the specific record that contains the personalization point.

**Relationship Name**
SourceRecord

**Refers To**
FlowRecordElement, ManagedContent

Status

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the state of the personalization point. The default value is `Processing`, and the
accepted values are:

**•** Active

**•** CreateError—Error

**•** DeleteError—Error

**•** Deleting

**•** EditError—Error

**•** Processing

Use this object to define a specific touch point in an experience where personalization decisions can be made. For example, a
personalization point can be an banner on a webpage. After setting up data space, profile data graph, personalization type, and schema,
you can add decisions and targeting rules to the personalization point to tailor the user experience.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[PersonalizationPointChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationPointFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationPointHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationPointOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationPointShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects PersonalizationSchema PersonalizationSchema

Represents a personalization response template that’s used when you build a personalization decision. Available in API version 62.0 and
later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
CurrencyIsoCode

DataSpaceId

Description

DeveloperName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where a response template's resources originate.
This is a required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the response template. This is an optional field.

**Type**
string


Standard Objects PersonalizationSchema

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the personalization response template. This is a
required field.

```
LastReferencedDate

LastViewedDate

Name

PersonalizationType

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the personalized response template was referenced
by another resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the response template.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the personalization response template.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the kind of personalization content to present. The default value is
Recommendations, and the accepted values are ManualContent and Recommendations.

A response template outlines the attributes that marketers use to configure the personalization response. It defines an expected format
and shape for all decision response data.


### Standard Objects PersonalizationTargetInfo

**•** For a recommendation-focused personalization, the response template can include an optional placeholder attribute to include
header text before a set of recommendations.

**•** For a manual content personalization, the response template can include placeholders for background images, links, call-to-action
text, and so on.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[PersonalizationSchemaChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[PersonalizationSchemaFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[PersonalizationSchemaHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[PersonalizationSchemaOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[PersonalizationSchemaShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### PersonalizationTargetInfo

Represents a target for an audience. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ContainerId

DraftRowId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Experience Cloud site or org that contains the target.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PersonalizationTargetInfo

**Field** **Details**

**Description**
ID of the draft PersonalizationTargetInfo.

```
GroupName

PublishStatus

TargetType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Group name of the target. Groups bundle related targets.You can have up to 2,000 groups
and 500 targets per group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Publish status of the target.

Possible values are:

**•** `Draft`

**•** `Live`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target.

Possible values are:

**•** `ExperienceVariation`

**•** `NavigationLinkSet`

**•** `Topic`

**•** `CollaborationGroup`

**•** `KnowledgeArticle`

**•** `ContentDocument`

**•** `ManagedContent`

**•** `Report`

**•** `Dashboard`

**•** Custom objects

You can have up to 2,500 `ExperienceVariation` targets and 25,000 record targets.


### Standard Objects PermissionUpdateEventLog

**Field** **Details**

```
TargetValue

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Value of the target. For ExperienceVariation, this is the developer name of the Experience
Variation or the record ID for the object.

### PermissionUpdateEventLog

Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets or
permission set groups. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
Context

Description

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context for what is happening for this update.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the update that occurred in the profile, permission set, or permission set
group.


Standard Objects PermissionUpdateEventLog

**Field** **Details**

```
FeatureIdentifier

LoginKey

PermissionType

RequestIdentifier

SessionKey

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the feature, such as a profile, permission set, or permission set group, that was
updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of permission, such as user, object, or field, or setup entity access, such as tab
settings or Apex class access, that was updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
dateTime


### Standard Objects PersonTraining

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

```
UpdateType

UserIdentifier

### PersonTraining

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For object permissions, user permissions, and setup entity access, the type of update that
occurred. For example, a permission was updated or deleted. For other changes in profiles,
permission sets, or permission set groups, this information is tracked in the DESCRIPTION
field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who made the permission update.

Represents an assignment of a learning module in Workforce Engagement. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The org requires a Workforce Engagement license and an Enablement Sites (myTrailhead) license. The user requires at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Admin, Workforce Engagement Analyst, Workforce Engagement
Planner, or Workforce Engagement Agent.

Workforce Engagement Management uses this object to route training to agents. To assign modules to agents, users with the Learning
Manager profile require Read, Create, and View All Records access to this object. To receive routed modules, users with the Learner profile
require Read access to this object.


Standard Objects PersonTraining

Fields

**Field** **Details**

```
AssigneeId

Name

OwnerId

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A valid user ID for the user who’s assigned the training. `AssigneeId` can’t be empty if
the `Status` field is Assigned. We recommend that you set `AssigneeId` to the value
in `OwnerId` .

This is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the learning module.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the person training.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects PersonTraining

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the training.

Possible values are:

**•** `A` —Assigned; when the `Status` is assigned, the `AssigneeId` field can’t be empty.

**•** `C` —Completed

**•** `I` —In Progress

**•** `N` —New

**•** `P` —Paused

The default value is 'N'.

```
TrainingId

TrainingType

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the learning module.

This is a relationship field.

**Relationship Name**
Training

**Relationship Type**
Lookup

**Refers To**
LearningContent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of training.

Possible values are:

**•** `T` —Trailhead

In version 54.0 and later releases, Workforce Engagement uses this object instead of the AgentTraining object to route learning modules
to agents. If you set up agent engagement in your org in an earlier release, we rename AgentTraining records as PersonTraining records.


### Standard Objects PicklistValueInfo PicklistValueInfo

Represents the active picklist values for a given picklist field. This object is available in API version 40.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DurableId

EntityParticleId

IsActive

IsDefaultValue

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the picklist field to which this value is related.

**Relationship Name**
EntityParticle

**Relationship Type**
Lookup

**Refers To**
EntityParticle

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the picklist value is active or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects PickTicket

**Field** **Details**

**Description**
Indicates whether this value is the default for the picklist field. Only one value can be the
default value.

```
Label

ValidFor

Value

### PickTicket

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A set of bits where each bit indicates a controlling value for which this picklist value is valid.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the picklist value.

A PickTicket represents quantities of one or more products to be picked for fulfillment at a location. It can include products belonging
to one or more fulfillment orders. This object is available in API version 57.0 and later.

A PickTicket is associated with one or more PickTicketAssignments and one or more PickTicketProducts. Each PickTicketAssignment
represents the relationship between the PickTicket and a FulfillmentOrder. Each PickTicketProduct represents the quantity of a product
to be picked as part of the PickTicket. If multiple FulfillmentOrders associated with the PickTicket include the same product, one
### PickTicketProduct can represent the total quantity of that product to be picked for all of those FulfillmentOrders.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects PickTicket

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
AssignedToId

LastReferencedDate

LastViewedDate

LocationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user assigned to pick the items associated with the PickTicket.

This field is a relationship field.

**Relationship Name**
AssignedTo

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PickTicket

**Field** **Details**

**Description**
The location fulfilling the items to be picked.

This field is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

```
OwnerId

PickTicketNumber

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the PickTicket record. By default, the asset owner is the user who created the
record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicket.

**Type**
picklist

**Properties**
Create, Filter, Group, Printed, Sort, Update

**Description**
Status of the PickTicket. Each status corresponds to one status category, shown here in
parentheses. You can customize the status picklist to represent your business processes, but
the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.


Standard Objects PickTicket

**Field** **Details**

Default values are:

**•** `Assigned` (Active)

**•** `Canceled` (Canceled)

**•** `Completed` (Completed)

**•** `Created` (Active)

**•** `Draft` (Draft)

**•** `Picked` (Active)

**•** `Picking` (Active)

```
StatusCategory

```

Associated Objects

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status category of the PickTicket. Processing of the PickTicket depends on this value. Each
status category corresponds to one or more status values.

Possible values are:

**•** `ACTIVE`

**•** `CANCELED`

**•** `COMPLETED`

**•** `DRAFT`

The default value is `DRAFT` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PickTicketFeed on page 55**
Feed tracking is available for the object.

**PickTicketShare on page 67**
Sharing is available for the object.

SEE ALSO:

PickTicketAssignment

PickTicketProduct


### Standard Objects PickTicketAssignment PickTicketAssignment

Represents the association of a FulfillmentOrder with a PickTicket. A PickTicket has one PickTicketAssignment for each FulfillmentOrder
containing products to be picked as part of that PickTicket. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
AttachedToId

### `PickTicketAssignmentNumber`

PickTicketId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the FulfillmentOrder to associate with a PickTicket.

This field is a relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects PickTicketProduct

**Field** **Details**

**Description**
ID of the PickTicket to associate with a FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
### PickTicket

**Relationship Type**
Lookup

**Refers To**
### PickTicket

SEE ALSO:

### PickTicket

FulfillmentOrder

### PickTicketProduct PickTicketProduct

Represents a quantity of a product to be picked as part of a PickTicket. It can include quantities for multiple FulfillmentOrders. This object
is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with an Order Management Growth license.

Fields

**Field** **Details**

```
PickTicketId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the PickTicket associated with the PickTicketProduct.

This field is a relationship field.


Standard Objects PickTicketProduct

**Field** **Details**

**Relationship Name**
PickTicket

**Relationship Type**
Lookup

**Refers To**
PickTicket

```
PickTicketProductNumber

PickedQuantity

Product2Id

ProductCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketProduct.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity of the PickTicketProduct that has been picked.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product associated with the PickTicketProduct.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code of the product associated with the PickTicketProduct.


Standard Objects PickTicketProduct

**Field** **Details**

```
Quantity

RejectReason

RejectedQuantity

StockKeepingUnit

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Total quantity that’s requested to be picked of the associated product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reason why some or all of the requested quantity isn’t being picked.

Possible values are:

**•** `Defected`

**•** `Other`

**•** `Out of stock`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested quantity that hasn’t been picked. When the status category of the associated
PickTicket is set to `Completed`, this value is automatically calculated as `Quantity`   `PickedQuantity` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the associated product.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects PipelineInspectionListView

**PickTicketProductFeed on page 55**
Feed tracking is available for the object.

SEE ALSO:

PickTicket

PickTicketAssignment

Product2

### PipelineInspectionListView

Represents a pipeline view, an intelligence view, or a saved filter. A pipeline view shows a set of opportunity records, based on specific
criteria. An intelligence view shows a set of account, lead, or contact records, based on specific criteria. This object is available in API
version 53.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable the Pipeline Inspection user permission and the Pipeline Inspection setting. To create and modify list views,
users must have the Create and Customize List Views permission. To create and modify public list views, users must have the Manage
Public List Views permission.

Fields

**Field** **Details**

```
ChangePeriodLiteralType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The date literal associated with the pipeline changes metrics group, used for filtering by a
custom time period.

Possible values are:

**•** `CUSTOM_DATE`

**•** `FOUR_WEEKS_AGO`

**•** `ONE_MONTH_AGO`

**•** `ONE_WEEK_AGO`

**•** `START_OF_THE_PERIOD`

**•** `THIS_MONTH`


Standard Objects PipelineInspectionListView

**Field** **Details**

**•** `THIS_WEEK`

**•** `THREE_MONTHS_AGO`

**•** `THREE_WEEKS_AGO`

**•** `TWO_MONTHS_AGO`

**•** `TWO_WEEKS_AGO`

```
ChangePeriodStartDate

DateLiteralType

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date used when filtering by a custom time period for pipeline changes metrics and
forecast category metrics groups.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The date literal associated with the pipeline and intelligence views, used for filtering by the
close date, created date, or activity date.

Possible values are:


Standard Objects PipelineInspectionListView

**Field** **Details**

                           - Available in API version 60.0 and later.

** Available on the "My Important" list views.

```
EndDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date used when filtering by a custom time period for close dates.


Standard Objects PipelineInspectionListView

**Field** **Details**

```
IsSystemManaged

ListViewId

MarketSegments

StartDate

SummaryField

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the system is managing changes to visibility and deletion of a pipeline
view ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ListView record. This field is unique within your organization.

This is a relationship field.

**Relationship Name**
ListView

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The customer segments selected in the Prospecting Center view.

This field is available in API version 61.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date used when filtering by a custom time period for close dates.

**Type**
picklist


Standard Objects PipelineInspectionListView

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The opportunity field specified in a pipeline view to summarize pipeline inspection metrics.

Possible values are standard field names or custom field IDs for custom currency and number
fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** _**`custom_field_ID`**_

This field is available in API version 56.0 and later.

```
UserId

ViewType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user whose records you want to see by default in the list view. This field is a
relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The corresponding API name for the pipeline or intelligence view type.

Possible values are:

**•** `MY_ACCOUNTS` –Available in API version 60.0 and later.

**•** `MY_CONTACTS`

**•** `MY_IMPORTANT_ACCOUNTS` –Available in API version 60.0 and later.

**•** `MY_IMPORTANT_CONTACTS`

**•** `MY_IMPORTANT_LEADS`

**•** `MY_IMPORTANT_OPPORTUNITIES`


### Standard Objects PipelineInspectionSumField

**Field** **Details**

**•** `MY_LEADS`

**•** `MY_PIPELINE`

**•** `MY_PROSPECTING_CENTER_ACCOUNTS–Available in API version`

```
                     61.0 and later.

```

Usage

Use this object to retrieve the metadata for a pipeline inspection view.

### PipelineInspectionSumField

Use this object to learn which field from the opportunity object is used to aggregate Pipeline Inspection metrics on a pipeline view. This
object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To use PipelineInspectionSumField, enable Pipeline Inspection. Users with a Pipeline Inspection user permission, the Customize Application
permission or the Modify All Data permission can access this object. To create and modify records, users must have either the Customize
Application permission or the Modify All Data permission.

Fields

**Field** **Details**

```
SobjectType

SummaryField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that stores the summary fields.

Possible values are:

**•** `Opportunity`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


### Standard Objects PipelineInspMetricConfig

**Field** **Details**

**Description**
The field used to summarize Pipeline Inspection metrics. Possible values are standard field
names or custom field IDs for custom currency and number fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** custom_field_ID

### PipelineInspMetricConfig

Represents the configuration of a forecast category metric that appears in the Pipeline Inspection view. This object is available in API
version 55.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

IsCumulative

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Read only. The unique name of a Pipeline Inspection metric configuration in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Whether the metric is cumulative.

**Type**
picklist


### Standard Objects PipelineInspMetricConfigLocalization

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Read only. The language of the Pipeline Inspection metric.

```
MasterLabel

Metric

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Customized label of the Pipeline Inspection metric. Limit: 50 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The Pipeline Inspection metric.

Possible values are:

**•** `BestCase`

**•** `ClosedLost`

**•** `ClosedWon`

**•** `Commit`

**•** `MostLikely`

**•** `OpenPipeline`

**•** `TotalPipeline`

### PipelineInspMetricConfigLocalization

Represents the translated label of a Pipeline Inspection metric. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`


Standard Objects PipelineInspMetricConfigLocalization

Fields

**Field** **Details**

```
Language

NamespacePrefix

ParentId

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language of the Pipeline Inspection metric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the Pipeline Inspection metric language.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related Pipeline Inspection metric.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PipelineInspMetricConfig

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the Pipeline Inspection metric.


### Standard Objects PlatformAction PlatformAction PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device format,

and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ActionListContext

ActionTarget

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The list context this action applies to. Valid values are:

**•** `Assistant`

**•** `BannerPhoto`

**•** `Chatter`

**•** `Dockable`

**•** `FeedElement`

**•** `Flexipage`

**•** `Global`

**•** `ListView`

**•** `ListViewDefinition`

**•** `ListViewRecord`

**•** `Lookup`

**•** `MruList`

**•** `MruRow`

**•** `ObjectHomeChart`

**•** `Photo`

**•** `Record`

**•** `RecordEdit`

**•** `RelatedList`

**•** `RelatedListRecord`

**Type**
textarea


Standard Objects PlatformAction

**Field** **Details**

**Properties**
Nillable

**Description**
The URL to invoke or describe the action when the action is invoked. If the action is a standard
button overridden by a Visualforce page, the ActionTarget returns the URL of the Visualforce
page, such as `/apex/` _`pagename`_ .

This field is available in API version 35.0 and later.

```
ActionTargetType

ActionTargetUrl

Category

ConfirmationMessage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the target when this action is triggered. Valid values are:

**•** `Describe` —applies to actions with a user interface, such as quick actions

**•** `Invoke` —applies to actions with no user interface, such as action links or invocable
actions

**•** `Visualforce` —applies to standard buttons overridden by a Visualforce page

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to invoke or describe the action when the action is invoked. This field is deprecated in
API version 35.0 and later. Use `ActionTarget` instead.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Applies only to action links. Denotes whether the action link shows up in the feed item list
of actions or the overflow list of actions. Valid values are:

**•** `Primary`

**•** `Overflow`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PlatformAction

**Field** **Details**

**Description**
Applies only to action links. The message to display before the action is invoked. Field is null
if no confirmation is required before invoking the action.

```
DeviceFormat

ExternalId

GroupId

IconContentType

IconHeight

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies which action icon the PlatformAction query returns. If this field isn’t specified, it
defaults to Phone. Valid values are:

**•** `Aloha`

**•** `Desktop`

**•** `Phone`

**•** `Tablet`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID for the PlatformAction. If the action doesn’t have an ID, its API name is used.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a group of action links.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type—such as .jpg, .gif, or .png—of the icon for this action. Applies to both
custom and standard icons assigned to actions.

**Type**
int


Standard Objects PlatformAction

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The height of the icon for this action. Applies only to standard icons.

```
IconUrl

IconWidth

InvocationStatus

InvokedByUserId

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the icon for this action.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The width of the icon for this action. Applies only to standard icons.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the action within the feed item. Applies to action links only. Valid values are:

**•** `Failed`

**•** `New`

**•** `Pending`

**•** `Successful`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who most recently invoked this action within the current feed item. Applies
to action links only.

This is a relationship field.

**Relationship Name**
InvokedByUser


Standard Objects PlatformAction

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
IsGroupDefault

IsMassAction

Label

PrimaryColor

RelatedListRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Denotes whether this action is the default in an action link group. False for other action types.
Applies to action links only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action can be performed on multiple records.

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label to display for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary color of the icon for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of a record in an object’s related list.


Standard Objects PlatformAction

**Field** **Details**

This field is available in API version 38.0 and later.

```
RelatedSourceEntity

Section

SourceEntity

Subtype

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the `ActionListContext` is RelatedList or RelatedListRecord, this field represents
the API name of the related list to which the action belongs.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The section of the user interface the action resides in. Applicable only to Lightning Experience.
Valid values are:

**•** ActivityComposer

**•** CollaborateComposer

**•** NotesComposer

**•** Page

**•** SingleActionLinks

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The object or record with which this action is associated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subtype of the action. For quick actions, the subtype is `QuickActionType` . For
custom buttons, the subtype is `WebLinkTypeEnum` . For action links, subtypes are `Api`,
`ApiAsync`, `Download`, and `Ui` . Standard buttons and productivity actions have no
subtype.


Standard Objects PlatformAction

**Field** **Details**

```
TargetObject

TargetUrl

Type

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of object record the action creates, such as a contact or opportunity.

This field is available in API version 41.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The URL that a custom button or link points to.

This field is available in API version 41.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the action. Valid values are:

**•** `ActionLink` —An indicator on a feed element that targets an API, a web page, or a
file, represented by a button in the Salesforce Chatter feed UI.

**•** `CustomButton` —When clicked, opens a URL or a Visualforce page in a window or
executes JavaScript.

**•** `InvocableAction`

**•** `ProductivityAction` —Productivity actions are predefined and attached to a
limited set of objects. Productivity actions include Send Email, Call, Map, View Website,
and Read News. Except for the Call action, you can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit, and Delete.

PlatformAction can be described using describeSObject().

You can directly query for PlatformAction. For example, this query returns all fields for actions associated with each of the records of the
listed objects:

```
SELECT ExternalId, ActionTargetType, ActionTargetUrl, ApiName, Category,

    ConfirmationMessage, ExternalId, GroupId, UiTheme, IconUrl, IconContentType,

```


### Standard Objects PlatformEventUsageMetric

```
       IconHeight, IconWidth, PrimaryColor, InvocationStatus, InvokedByUserId,

       IsGroupDefault, Label, LastModifiedDate, Subtype, SourceEntity, Type

   FROM PlatformAction

   WHERE SourceEntity IN ('001xx000003DGsH', '001xx000003DHBq', ‘Task’) AND

       ActionListContext = ‘Record’;

```

Note: To query PlatformAction, provide the `ActionListContext` and `SourceEntity` . If you query for
`ActionListContext` with a value of `RelatedList`, and don't specify a `RelatedSourceEntity`, the query returns
the API name of the related list. In API v43.0 and before, `SourceEntity = '` _**`Object API Name`**_ `' and`
`ActionListContext = 'ListView'` is an invalid combination to fetch quick actions in a SOQL query. Use
`SourceEntity = '` _**`Object ID`**_ `' and ActionListContext = 'ListView'` instead.

This query uses multiple `ActionListContext` values in its `WHERE` clause to return all actions in the Lightning Experience user
interface ( `DeviceFormat = 'Desktop'` ) for the specified object:

```
   SELECT ActionListContext, Label, Type, Subtype, Section, SourceEntity,

      RelatedSourceEntity, ActionTarget, ActionTargetType, ApiName, Category,

      ConfirmationMessage, DeviceFormat, ExternalId, GroupId, IconContentType,

      IconHeight, IconUrl, IconWidth, Id, InvocationStatus, InvokedByUserId,

      IsGroupDefault, LastModifiedDate, PrimaryColor

   FROM PlatformAction

   WHERE ActionListContext IN ('Record','Chatter','RelatedList') AND

       SourceEntity = '001xx000003DlvX' AND

       DeviceFormat = 'Desktop'

### PlatformEventUsageMetric

```

Contains usage data for event publishing and delivery to CometD and Pub/Sub API clients, `empApi` Lightning components, and event
relays. If Enhanced Usage Metrics isn't enabled, usage data is available for the last 24 hours, ending at the last hour, and for historical
daily usage. In API 58.0 and later, you can enable Enhanced Usage Metrics to get usage data by event name and client for granular time
intervals. PlatformEventUsageMetric contains separate usage metrics for platform events and change data capture events. This object
is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
Client

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The ID of the client. The
`Client` field is populated with one of the following values.


Standard Objects PlatformEventUsageMetric

**Field** **Details**

The `Client` field can be one of these values.

**•** For a Streaming API (CometD) client and the empApi Lightning component, the client
value is the ID of the CometD session.

**•** For a Pub/Sub API client, the client value is `PUB_SUB_API` .

**•** For an event relay, the client value is `EVENT_RELAY` .

**•** For the publish usage of Change Data Capture events, the client value is `SYSTEM` .

**•** For publish usages using REST API, the client value is `REST_API` .

**•** For publish usages using Flow, the client value is `FLOW` .

**•** For publish usages using SOAP API, the client value is `SOAP_API` .

**•** For publish usages using Bulk API, the client value is `BULK_API` .

**•** For Apex, the publish usage client value is `APEX` and the delivery usage client value is
the Apex Trigger ID starting with 01q.

```
EndDate

EventName

EventType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time in UTC used for querying usage metrics. The date granularity is hourly.

To get usage data for the last 24 hours, the end date is the current date in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-04T11:00:00.000Z

To get historical data, the end date in UTC is the end of the date range with hours specified
as 0. For example: 2020-08-04T00:00:00.000Z. To query a date range, you can use the < or
<= operators.

[For the date format to use, see Date Formats and Date Literals in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm) _SOQL and SOSL Reference_ .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The API name of a
custom platform event or a change event.

**•** Custom platform event with the label My Event: `My_Event__e`

**•** Change event example: `AccountChangeEvent`

When you query usage metrics for `EventName`, specify the `UsageType` field in the
`SELECT` or `WHERE` clause.

**Type**
picklist


Standard Objects PlatformEventUsageMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event you would
like to query usage metrics for, such as a change event or a custom platform event.

Possible values are:

**•** `CHANGE_EVENT` —A Change Data Capture event.

**•** `CUSTOM_PLATFORM_EVENT` —A platform event that an admin defined in your
Salesforce org.

When you query usage metrics for `EventType`, specify the `UsageType` field in the
`SELECT` or `WHERE` clause.

```
ExternalId

Name

StartDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the metric to get usage for.

Possible values are:

**•** `CHANGE_EVENTS_DELIVERED` —Number of change data capture events delivered
to CometD and Pub/Sub API clients, `empApi` Lightning components, and event relays

**•** `CHANGE_EVENTS_PUBLISHED` —Number of change data capture events published

**•** `PLATFORM_EVENTS_DELIVERED` —Number of platform events delivered to CometD
and Pub/Sub API clients, `empApi` Lightning components, and event relays

**•** `PLATFORM_EVENTS_PUBLISHED` —Number of platform events published

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date and time in UTC used for querying usage metrics. The date granularity is hourly.


Standard Objects PlatformEventUsageMetric

**Field** **Details**

To get usage data for the last 24 hours, the start date is the previous day in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-03T11:00:00.000Z

To get historical data, the start date is the start of the date range with hours specified as 0.
For example: 2020-08-03T00:00:00.000Z. To specify a date range, you can use the > or >=
operators.

If Enhanced Usage Metrics is enabled, keep in mind these tips.

**•** Make sure the time span between `StartDate` and `EndDate` is valid for the
`TimeSegment` value chosen.

**•** The maximum date range that you can specify between `StartDate` and `EndDate`
is 60 days.

[For the date format to use, see Date Formats and Date Literals in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm) _SOQL and SOSL Reference_ .

```
TimeSegment

UsageType

```

**Type**
picklist


**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The time interval used for
aggregating usage data returned in the query results. Valid `TimeSegment` values depend
on the time range specified with `StartDate` and `EndDate` .

Possible values are:

### Standard Objects PlatformStatusAlertEvent

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event usage
metrics to query for, such as event publishing or event delivery. Use this field with the
`EventName` or `EventType` fields.

Possible values are:

**•** `PUBLISH` —Usage metrics for published events.

**•** `DELIVERY` —Usage metrics for events that were delivered to subscribers.

```
Value

```

Usage

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The usage value for the specified metric and date range.

[For more information, see Monitor Platform Event Publishing and Delivery Usage in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_monitor_usage.htm) _Platform Events Developer Guide_ .

### PlatformStatusAlertEvent

[The documentation has moved to PlatformStatusAlertEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_platformstatusalertevent.htm) _Platform Events Developer Guide_ .

### PortalDelegablePermissionSet PortalDelegablePermissionSet is a base platform object used to store permission sets that can be assigned by a delegated portal/external

user admin (DPUA) to portal users. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


### Standard Objects PresenceConfigDeclineReason

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string used to identify the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
Language

MasterLabel

PermissionSetId

ProfileId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string to identify the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the permission set the DPUA profile can assign to other portal users.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the DPUA profile.

### PresenceConfigDeclineReason

Represents the settings for a decline reason that a presence user provides when declining work. This object is available in API version
37.0 and later.


### Standard Objects PresenceDeclineReason

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

### `PresenceDeclineReasonId`

```
PresenceUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the PresenceDeclineReason record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the PresenceUserConfig record where the decline reasons are added.

### PresenceDeclineReason

Represents an Omni-Channel decline reason that agents can select when declining work requests. This object is available in API version
37.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects PresenceUserConfig

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the PresenceDeclineReason.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label for the PresenceDeclineReason.

### PresenceUserConfig

Represents a configuration that determines a presence user’s settings. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`


Standard Objects PresenceUserConfig

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AcwExtensionDuration

AfterConvoWorkMaxTime

Capacity

CustomSoundId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Specify a value from 10 through 3600.

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if `HasAfterConvoWorkTimer` is
set to `true` . Specify a value from 10 through 3600.

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The maximum number of work units an agent can be assigned at one time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  CustomSound

```


Standard Objects PresenceUserConfig

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**

```
                   StaticResource

```

**Description**
The ID of the static resource for the custom sound selected to play for the
`PresenceUserConfig` object.

```
DeveloperName

HasAcwExtensionEnabled

HasAfterConvoWorkTimer

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance may slow while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, agents can extend their After Conversation Work (ACW) time. Available only
if `HasAfterConvoWorkTimer` is set to `true` . If set to `true`, you must also set the
`AcwExtensionDuration` and `MaxExtensions` fields. The default value is `true` .

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects PresenceUserConfig

**Field** **Details**

**Description**
If set to `true`, After Conversation Work (ACW) time can be configured for the channel. If
set to `true`, you must also set the `AfterConvoWorkMaxTime` field. The default value
is `false` .

This field is available in API version 56.0 and later.

```
Language

MasterLabel

MaxExtensions

OptionsIsAllowAnyDestinationQueueForTransferEnabled

OptionsIsAllowAnyDestinationFlowForTransferEnabled

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence configuration.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true` .

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
queue ( `true` ) or only the selected queues ( `false` ).

This field is available in API version 61.0 and later.

**Type**
boolean


Standard Objects PresenceUserConfig

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
flow ( `true` ) or only the selected flows ( `false` ).

This field is available in API version 61.0 and later.

```
OptionsIsAllowAnyDestinationProfileForTransferEnabled

OptionsIsAutoAcceptEnabled

OptionsIsDeclineEnabled

OptionsIsDeclineReasonEnabled

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
profile ( `true` ) or only the selected profiles ( `false` ).

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether work items that are routed to agents are automatically accepted ( `true` )
or not ( `false` ). Available only if `OptionsIsDeclineEnabled` is set to `false` .

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can decline work items that are routed to them ( `true` ) or not
( `false` ). Available only if `OptionsIsAutoAcceptEnabled` is set to `false` .

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can select a reason for declining work requests ( `true` ) or not
( `false` ). This can be selected only if decline reasons are enabled.


Standard Objects PresenceUserConfig

**Field** **Details**

```
OptionsIsDisconnectSoundEnabled

OptionsIsRequestSoundEnabled

PresenceStatusOnDeclineId

PresenceStatusOnPushTimeoutId

SoundLength

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound is played when agents are disconnected from Omni-Channel
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound plays with incoming work requests ( `true` ) or not ( `false` ). Set
to `true` by default.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
declines a work item. Available only if `OptionsIsDeclineEnabled` is set to `true` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
doesn’t respond to a work item before push timeout occurs. Available in API version 36.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.


### Standard Objects PresenceUserConfigProfile PresenceUserConfigProfile

Represents a configuration that determines the settings that are assigned to presence users who are assigned to a specific profile.
User-level configurations override profile-level configurations. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
PresenceUserConfigId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If an individual user is also assigned a presence configuration through the
### PresenceUserConfigProfile, this configuration will override that.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the profile that’s associated with this presence configuration. A profile can be
associated with only one presence configuration.

### PresenceUserConfigUser

Represents a configuration that determines the settings that are assigned to a presence user. These user-level configurations override
profile-level configurations. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`


### Standard Objects PriceAdjustmentGroupShape

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
PresenceUserConfigId

UserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the presence configuration.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user who’s associated with this presence configuration. A user can be associated
with only one presence configuration.

### PriceAdjustmentGroupShape

Defines the business logic for a top-level price adjustment, for example, a discount applied to an entire order. This object is available in
API version 57.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AdjustmentSource

```

**Type**
picklist


Standard Objects PriceAdjustmentGroupShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the source of the adjustment. This field is available with B2B Commerce.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually, for example, by a sales rep.

**•** `Promotion` —The adjustment is part of a promotion.

**•** `Rule` —Reserved for future use.

**•** `System` —The adjustment is configured by the system data, for example, as part of a
pricing rule or discount schedule.

```
AdjustmentType

AdjustmentValue

Description

PriceAdjustmentCauseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the adjustment is a percentage, an amount, or an override.

Possible values are:

**•** `AdjustmentAmount` —Reserved for future use. The adjustment value is a numerical
amount.

**•** `AdjustmentPercentage`  - The adjustment value is a percentage.

**•** `OverrideAmount`  - The override value is a numerical amount.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The value of the adjustment. To indicate a discount, use a negative number.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
User-entered description of the price adjustment group. Available in API versions 57.0.

**Type**
reference


Standard Objects PriceAdjustmentGroupShape

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that is the source of the adjustment. For example, if the price adjustment
is due to a promotion, this field contains the ID of the promotion record. If the price
adjustment is due to a price adjustment tier, this field contains the ID of the price adjustment
tier record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

```
PriceAdjustmentGroupShapeName

Priority

SalesTransactionShapeId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Name of the price adjustment group shape.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A positive integer indicating the order in which this price adjustment group is applied, relative
to other price adjustment groups. A `Priority` of `1` indicates this price adjustment group
is applied first.

Price adjustments with a null priority are applied after price adjustments with a specified
priority. If two or more price adjustments have a null priority, percentage adjustments are
applied **before** amount adjustments. Applying a percentage adjustment before an amount
adjustment results in a larger total adjustment.

Note: The value of `Priority` must be unique among price adjustment groups
in the same sales transaction.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
The ID of the sales transaction that the price adjustment group belongs to.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

```
TotalAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total amount of adjustments of all related price adjustment items, inclusive of quantity,
prorated for the duration of the subscription. This field is a calculated field equal to the sum
of the `TotalAmount` fields in the related price adjustment items.

### PriceAdjustmentItemShape

Defines the business logic for an item-level price adjustment, for example, a discount on an order item. This object is available in API
version 57.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total` —The adjustment applies to the line item's total and isn’t multiplied by the
quantity.

For example, let's say a sales transaction item quantity is `10` and the
`TotalLineAmount` is `1000` . If the price adjustment item has an
`AdjustmentValue` of `-10`, an `AdjustmentType` of `AdjustmentAmount`,
and an `AdjustmentAmountScope` of `Total`, the $10 discount is applied to the
total line amount. The `TotalAmount` of the price adjustment item is $1000 + (-$10)
= $990.

**•** `Unit` —The adjustment is multiplied by the line item’s quantity.

For example, let's say a sales transaction item quantity is `5` and the
`TotalLineAmount` is `1000` . If the price adjustment item has an
`AdjustmentValue` of `-10`, an `AdjustmentType` of `AdjustmentAmount`,
and an `AdjustmentAmountScope` of `Unit`, the $10 discount is applied to each
line amount. The TotalAmount of the price adjustment item is $1000 + (-$10 x 5) = $950.

**•** `UnproratedTotal` —No adjustment is applied to the line items.

```
AdjustmentSource

AdjustmentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the source of the adjustment.

Possible values are:

**•** `Discretionary`  - The adjustment is entered manually; for example, by a sales rep.

**•** `Promotion`  - The adjustment is a promotion.

**•** `Rule`  - Reserved for future use.

**•** `System`  - The adjustment is determined by the pricing configuration for the product;
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the adjustment is a percentage, an amount, or an override.

Possible values are:

**•** `AdjustmentAmount` —The adjustment value is a numerical amount.


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**•** `AdjustmentPercentage`                   - The adjustment value is a percentage.

**•** `OverrideAmount`                   - The override value is a numerical amount.

```
AdjustmentValue

Description

PriceAdjustmentCauseId

PriceAdjustmentGroupShapeId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The value of the adjustment. Used together with `AdjustmentAmountScope` to
determine the amount of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The user-entered description of the price adjustment item. Available in API version 57.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. For example, if the price adjustment is due
to a promotion, this field contains the ID of the Promotion record. If the price adjustment is
due to a price adjustment tier, this field contains the ID of the `PriceAdjustmentTier`
record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects PriceAdjustmentItemShape

**Field** **Details**

**Description**
A reference to the object interface or object that summarizes the values from multiple price
adjustment items. If the related entity is an object, the object must implement the
`PriceAdjustmentGroupShape` object.

This field is a relationship field.

**Relationship Name**
PriceAdjustmentGroupShape

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentGroupShape

```
PriceAdjustmentItemShapeName

Priority

SalesTransactionItemShapeId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the price adjustment item shape.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A positive integer indicating the order in which this price adjustment item is applied, relative
to other price adjustment items. A `Priority` of `1` indicates this price adjustment item
is applied first.

Price adjustments with a null priority are applied after price adjustments with a specified
priority. If two or more price adjustments have a null priority, percentage adjustments are
applied **before** amount adjustments. Applying a percentage adjustment before an amount
adjustment results in a larger total adjustment.

Note: The value of `Priority` must be unique among price adjustment items
related to the same price adjustment group. For example, you can’t have two price
adjustment items with a priority of `1` .

For example, let’s say that two price adjustment items apply to the same item to be priced.
The first price adjustment, Spring_Promotion, defines a 10% discount and has `Priority`
of `1` . The second price adjustment, Early_Renewal_Discount, defines a $2,000 discount and
has a `Priority` of `2` . In this case, the Spring_Promotion price adjustment is applied
before the Early_Renewal_Discount price adjustment.

**Type**
reference


### Standard Objects PriceAdjustmentSchedule

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the sales transaction shape item that the price adjustment item applies to.

This field is a relationship field.

**Relationship Name**
SalesTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

```
TotalAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total amount of the adjustment that applies to the item to be priced, inclusive of quantity,
prorated for the duration of the subscription.

For example, let’s say the price adjustment item has an `AdjustmentAmountScope` of
`Unit`, an `AdjustmentType` of `AdjustmentAmount`, and an `AdjustmentValue`
of `-10` . This configuration indicates a $10 per-unit discount. If the subscription is priced for
12 months and the pricing term is `1`, the `PricingTermCount` on the sales transaction
item is 12. If the quantity is 5, the value of `TotalAmount` is 5 x 12 x -10 = -600

### PriceAdjustmentSchedule

Represents a series of discounts offered depending on your product's configuration, quantity, and when they’re purchased in combination
with other products. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when the B2B Commerce license is enabled or when Subscription Management is enabled.


Standard Objects PriceAdjustmentSchedule

Fields

**Field** **Details**

```
AdjustmentMethod

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method for applying tiered pricing. Possible values are:

**•** `Range` —All items receive the discount of the highest tier the quantity falls in.

**•** `Slab` —Items receive the discount defined for the tier they fall in.

The default value is `Range` . Term-based discounts can’t be of type `Slab` . This field is
available in API version 51.0 and later.

The `Slab` method functions in the same way as the `Range` method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price adjustment schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price adjustment schedule is active ( `true` ) or not ( `false` ). You can
change this field’s value as often as necessary. Label is **Active** . The default value is `False` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates whether the price adjustment schedule has been archived ( `true` ) or not ( `false` ).
This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PriceAdjustmentSchedule

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

ScheduleType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the price adjustment schedule. This field is read-only. Label is **Price**
**Adjustment Schedule Name** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The Salesforce ID of the sales representative who owns the price adjustment schedule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the price adjustment is determined. This field is available when Subscription
Management is enabled. This field is available in API version 55.0 and later.

Possible values are:

**•** `Attribute` —The characteristics or properties of a product determine the price
adjustment.

**•** `Bundle` —The price adjustment that is determined when you want to sell a group of
products or services as a unit.

**•** `Custom` —The price adjustment that can be customized for the user's needs.

**•** `Term` —The length of the subscription determines the price adjustment. Available in
API version 58.0 and later.

**•** `Volume` —The quantity purchased determines the price adjustment.

The default value is `Volume` .


Standard Objects PriceAdjustmentSchedule

Usage

When you create a PriceAdjustmentSchedule, you associate PriceAdjustmentTiers with it. A PriceAdjustmentSchedule is inactive until
at least one PriceAdjustmentTier is added to it. A PriceAdjustmentSchedule comprises all related PriceAdjustmentTiers, with a maximum
limit of 25 PriceAdjustmentTiers for Subscription Management.

To use PriceAdjustmentSchedule, associate it with a PriceBookEntry.

**•** You can associate a PriceBookEntry with up to five PriceAdjustmentSchedules, but only one PriceAdjustmentSchedule can be
associated with a PriceBookEntry.

**•** When you activate or deactivate a PriceAdjustmentSchedule, its PriceBookEntry association is also activated or deactivated.

**•** An adjustment to a PriceBookEntry is applied only if the associated PriceAdjustmentSchedule is active.

**•** After a PriceAdjustmentSchedule is associated with a PriceBookEntry, if multicurrency is enabled, the currencyIsoCode field can’t be
modified.

**•** When you associate a PriceAdjustmentSchedule with a PricebookEntry, a junction object PricebookEntryAdjustment is created.

You can modify the PriceAdjustmentTier object, and the `ScheduleType` and `AdjustmentMethod` fields, only when a
PriceAdjustmentSchedule is inactive.

Code Sample

```
   public void priceAdjustmentScheduleSample()

             {try

              /* This code snippet will do the following:

     *

     * 1. Create a new Price Adjustment Schedule

     * 2. Create and attach a Price Adjustment Tier to the Schedule

     * 3. Activate the Schedule

     * 4. Create a new PricebookEntry Adjustment. This will associate the Schedule to a

   Pricebook Entry. */

     //Create a Price Adjustment Schedule

     PriceAdjustmentSchedule pas = new PriceAdjustmentSchedule();

     pas.Name = 'Sample PAS';

     pas.Description = 'Sample Price Adjustment Schedule';

     pas.AdjustmentMethod = 'Range';

     insert pas;

     //Attach a valid Price Adjustment Tier

     PriceAdjustmentTier pat = new PriceAdjustmentTier();

     pat.PriceAdjustmentScheduleId = pas.Id;

     pat.LowerBound = 1.0;

     pat.UpperBound = 100.0;

     pat.TierType = 'AdjustmentPercentage';

     pat.TierValue = 5.0;

     insert pat;

     //Activate the Schedule

     pas.IsActive = true;

     upsert pas;

     //Create a new PricebookEntry Adjustment

     PricebookEntryAdjustment pbea = new PricebookEntryAdjustment();

```


### Standard Objects PriceAdjustmentTier

```
     pbea.PricebookEntryId = '01uRM0000007Hb5YAE';

     pbea.PriceAdjustmentScheduleId = pas.Id;

     insert pbea;

    } catch (ConnectionException ce) {

     ce.printStackTrace();

    }

   }

```

SEE ALSO:

### PriceAdjustmentTier

PricebookEntryAdjustment

### PriceAdjustmentTier

Represents a discount tier in a price adjustment schedule. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
LowerBound

Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The minimum quantity the discount can be applied to. It must be a positive integer and less
than or equal to the upper bound of the tier.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.


Standard Objects PriceAdjustmentTier

**Field** **Details**

```
PriceAdjustmentScheduleId

TierType

TierValue

UpperBound

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the price adjustment schedule that the discount is applied to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of the discount. Possible values are:

**•** `AdjustmentAmount` —An amount discounted from an item’s list price. Label is
Amount.

**•** `AdjustmentPercentage` —A percentage discounted from an item’s list price.
Label is Percentage.

**•** `AdjustmentOverride` —An override of an item’s list price. Label is Override.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the discount.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum quantity the discount can be applied to. The quantity must be a positive
integer. Not inclusive. Set this value one digit higher than the quantity you want the tier to
include. For example, if a tier’s upper bound is 99, set the value of `UpperBound` to 100.
For the last tier, the value is optional.

To use PriceAdjustmentTiers, associate them with a PriceAdjustmentSchedule.


### Standard Objects Pricebook2

Tiers can’t overlap, and no gaps are allowed between tiers.

SEE ALSO:

PriceAdjustmentSchedule

### Pricebook2

Represents a price book that contains the list of products that your org sells.

Note: Price books are represented by Pricebook2 objects. As of API version 8.0, the Pricebook object is no longer available. Requests
containing Pricebook are refused, and responses don’t contain the Pricebook object.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

IsActive

IsArchived

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price book.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price book is active ( `true` ) or not ( `false` ). Inactive price books are
hidden in many areas in the user interface. You can change this field’s value as often as
necessary. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the price book has been archived (true) or not (false). This field is read
only.


Standard Objects Pricebook2

**Field** **Details**

```
IsDeleted

IsStandard

LastReferencedDate

LastViewedDate

Name

ValidFrom

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the price book has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the price book is the standard price book for the org ( `true` ) or not
( `false` ). Every org has one standard price book—all other price books are custom price
books.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this object. This field is read-only for the standard price book. Label is
**Price Book Name** .

**Type**
dateTime


Standard Objects Pricebook2

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is initially valid. If this field is `null`, the
price book is valid immediately when active. Available in API version 48.0 and later.

```
ValidTo

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is valid to. If this field is `null`, the price
book is valid until it’s deactivated. Available in API version 48.0 and later.

A price book is a list of products that your org sells.

**•** Each org has one standard price book that defines the standard or generic list price for each product or service that it sells.

**•** An org can have multiple custom price books to use for specialized purposes, such as for discounts, different channels or markets,
or select accounts or opportunities. While your client application can create, delete, and update custom price books, your client
application can only update the standard price book.

**•** For some orgs, the standard price book is the only price needed. If you set up other price books, you can reference the standard
price book when setting up list prices in custom price books.

Use this object to query standard and custom price books that have been configured for your org. A common use of this object is to
allow your client application to obtain valid Pricebook2 object IDs for use when configuring PricebookEntry records via the API.

Your client application can perform the following tasks on PricebookEntry objects:

**•** Query

**•** Create for the standard price book or custom price books.

**•** Update

**•** Delete

**•** Change the `IsActive` field when creating or updating records

PriceBook2, Product2, and PricebookEntry Relationships

In the API:

**•** Price books are represented by Pricebook2 records (as of version 8.0, the Pricebook object is no longer available).

**•** Products are represented by Product2 records (as of version 8.0, the Product object is no longer available).

**•** Each price book contains zero or more entries (represented by PricebookEntry records) that specify the products that are associated
with the price book. A price book entry defines the price for which you sell a product at a particular currency.


Standard Objects Pricebook2

These objects are defined only for those orgs that have products enabled as a feature. If the org doesn’t have the products feature
enabled, the Pricebook2 object doesn’t appear in the `describeGlobal()` call, and you can’t access it via the API.

If you delete a Pricebook2 while a line item references PricebookEntry in the price book, the line item is unaffected, but the Pricebook2
is archived and unavailable from the API.

For a visual diagram of the relationships between Pricebook2 and other objects, see Product and Schedule Objects.

Price Book Setup

The process of setting up a price book via the API usually means:

**1.** Load product data into Product2 records (creating one Product2 record for each product that you want to add).

**2.** For each Product2 record, create a PricebookEntry that links the Product2 record to the standard Pricebook2. Define a standard price
for a product at a given currency (if you have multicurrency enabled) before defining a price for that product in the same currency
in a custom price book.

**3.** Create a Pricebook2 record to represent a custom price book.

**4.** For each Pricebook2 record, creating a PricebookEntry for every Product2 that you want to add, specifying unique properties for
each PricebookEntry (such as the `UnitPrice` and `CurrencyIsoCode` ) as needed.

Code Sample—Java

```
   public void pricebookSample() {

     try {

      //Create a custom pricebook

      Pricebook2 pb = new Pricebook2();

      pb.setName("Custom Pricebok");

      pb.setIsActive(true);

      SaveResult[] saveResults = connection.create(new SObject[]{pb});

      pb.setId(saveResults[0].getId());

      // Create a new product

      Product2 product = new Product2();

      product.setIsActive(true);

      product.setName("Product");

      saveResults = connection.create(new SObject[]{product});

      product.setId(saveResults[0].getId());

      // Add product to standard pricebook

      QueryResult result = connection.query(

        "select Id from Pricebook2 where isStandard=true"

      );

      SObject[] records = result.getRecords();

      String stdPbId = records[0].getId();

      // Create a pricebook entry for standard pricebook

      PricebookEntry pbe = new PricebookEntry();

      pbe.setPricebook2Id(stdPbId);

      pbe.setProduct2Id(product.getId());

      pbe.setIsActive(true);

      pbe.setUnitPrice(100.0);

      saveResults = connection.create(new SObject[]{pbe});

```


### Standard Objects Pricebook2History

```
      // Create a pricebook entry for custom pricebook

      pbe = new PricebookEntry();

      pbe.setPricebook2Id(pb.getId());

      pbe.setProduct2Id(product.getId());

      pbe.setIsActive(true);

      pbe.setUnitPrice(100.0);

      saveResults = connection.create(new SObject[]{pbe});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[Pricebook2ChangeEvent (API version 48.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **Pricebook2History**

History is available for tracked fields of the object.

### Pricebook2History

Represents historical information about changes that have been made to the standard fields of the associated Pricebook2, or to any
custom fields with history tracking enabled. This object is available in API version 66.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
Pricebook2Id

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects Pricebook2History

**Field** **Details**

**Description**
ID of the Pricebook2 associated with this record.

This is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
DataType

Field

IsDeleted

NewValue

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name of the price book field that was modified, or a special value to indicate some other
modification to the price book.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
This is a standard system field. Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified price book field. Maximum of 255 characters.


### Standard Objects PricebookEntry

**Field** **Details**

```
 OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified price book field. Maximum of 255 characters.

Price book history entries are indirectly created each time a price book is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Pricebook2

### PricebookEntry

Represents a product entry (an association between a Pricebook2 and Product2) in a price book.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

Note: Salesforce Object Search Language (SOSL) allows you to search records across standard and custom objects. When filtering
records in the PriceBookEntry object using SOSL, you can only sort by fields related to Product2.

**Field** **Details**

```
ActivePriceAdjustmentQuantity

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects PricebookEntry

**Field** **Details**

**Description**
The count of active price adjustment schedules associated with the price book entry. This
field is available in API version 49.0 and later. This field is available with a B2B or D2C
Commerce license.

```
CurrencyIsoCode

IsActive

IsArchived

Name

Pricebook2Id

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry is active ( `true` ) or not ( `false` ). Although you can
never delete PricebookEntry records, your client application can set this flag to `false` .
Inactive PricebookEntry records are hidden in many areas in the user interface. You can
change this flag on a PricebookEntry record as often as necessary.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the PricebookEntry has been archived (true) or not (false). This field is set
to `true` when the Product2 record it’s associated with is archived, or when the Pricebook2
record is archived. This field is read only. Available in API version 45.0 and later. Label is
**Archived** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this PricebookEntry record. This read-only field references the value in the Name
field of the Product2 record. Label is **Product Name** .

**Type**
reference


Standard Objects PricebookEntry

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Pricebook2 record with which this record is associated. This field must
be specified when creating Pricebook2 records. It can’t be changed in an update.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
Product2Id

ProductCode

ProductSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 record with which this record is associated. This field must be
specified when creating Product2 records. It can’t be changed in an update.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code for this record. This read-only field references the value in the **ProductCode**
field of the associated Product2 record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects PricebookEntry

**Field** **Details**

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and later.
This field is available when Subscription Management is enabled.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

```
UnitPrice

UseStandardPrice

```

Usage

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Unit price for this price book entry. You can specify a value only if
`UseStandardPrice` is set to `false` . Label is **List Price** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry uses the standard price defined in the standard
Pricebook2 record ( `true` ) or not ( `false` ). If set to `true`, then the `UnitPrice` field is
read-only, and the value is the same as the `UnitPrice` value in the corresponding
PricebookEntry in the standard price book (that is, the PricebookEntry record whose
`Pricebook2Id` refers to the standard price book and whose `Product2Id` and
`CurrencyIsoCode` are the same as this record). For PricebookEntry records associated
with the standard Pricebook2 record, this field must be set to `true` .

Use this object to define the association between your organization’s products (Product2) and your organization’s standard price book
or to custom price books ( Pricebook2). Create one PricebookEntry record for each standard or custom price and currency combination
for a product in a Pricebook2.

When creating these records, you must specify the IDs of the associated Pricebook2 record and Product2 record. Once these records are
created, your client application can’t update these IDs.

This object is defined only for those organizations that have products enabled as a feature. If the organization doesn’t have the products
feature enabled, then the PricebookEntry object doesn’t appear in the describeGlobal call, and you can’t access it.

If you delete a PriceBookEntry that is referenced by a line item, the line item is unaffected, but the PriceBookEntry is archived and
unavailable from the API. Deleted PriceBookEntry records can’t be recovered.


### Standard Objects PricebookEntryAdjustment

You must load the standard price for a product before you’re permitted to load its custom prices.

Associated Objects

This object has the following associated objects. Unless otherwise noted, they’re available in the same API version as this object.

**PricebookEntryChangeEvent(API version 57.0)**
Change events are available for the object.

**PricebookEntryHistory**

History is available for tracked fields of the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### PricebookEntryAdjustment

Read-only junction object created when you associate a price adjustment schedule with a price book entry. This object is available in
API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Name

PriceAdjustmentScheduleId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects PriceProtectionExecution

**Field** **Details**

**Description**
The ID of the price book entry adjustment.

```
PricebookEntryId

```

SEE ALSO:

PriceAdjustmentSchedule

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book entry that this price book entry adjustment is associated with.

### PriceProtectionExecution

Represents an instance of running the price protection process, capturing execution time, status, and the effective date of price changes.
This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ExecutionJobId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Data processing engine instance responsible for creating price protection records.

This field is a relationship field.

**Relationship Name**
ExecutionJob

**Refers To**
BatchCalcJobDefinition


Standard Objects PriceProtectionExecution

**Field** **Details**

```
ExecutionReferenceNumber

LastExecutionTime

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

Unique reference number generated by the Data Processing Engine for this execution. This
can be used to associate related line items to the same execution.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date and time when the price protection execution was last performed by the Data Processing
Engine.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the record was last referenced. This is used internally to optimize
performance and user experience.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Date and timestamp when the record was last viewed in the Salesforce UI. Helps track user
engagement.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

Auto-generated name for the price protection execution record. Used as the primary identifier
within the system.


### Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
OwnerId

PriceChangeEffectiveDate

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifier for the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Date when the new price goes into effect as part of the price protection execution.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the current lifecycle status of the price protection execution process.

Possible values are:

**•** `Completed`

**•** `New`

**•** `Processing`

### PriceProtectExecLineItem

Represents a line item created as part of a Price Protection Execution. This object is available in API version 63.0 and later.

A PriceProtectExecLineItem record is automatically generated by the Data Processing Engine when eligible product transactions are
processed for price protection. It links to execution records, products, and pricing terms, and stores per-unit pricing, eligibility, and
calculation details.


Standard Objects PriceProtectExecLineItem

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

CalculatedAmount

CalculationReferenceRecordId

ClaimReferenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the partner account related to the transaction being evaluated for price protection.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total protected amount calculated based on the applicable price difference and quantity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the rebate or pricing rule used to compute the claim.

This field is a relationship field.

**Relationship Name**
CalculationReferenceRecord

**Refers To**
ProgramRebateType

**Type**
reference


Standard Objects PriceProtectExecLineItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to the related rebate claim, if one has been generated.

This field is a polymorphic relationship field.

**Relationship Name**
ClaimReference

**Refers To**
RebateClaim

```
HasWarnings

InTransitQuantity

IsEligible

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the execution line item has associated warnings.

The default value is `false` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity of the product in transit.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the record qualifies for price protection.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by a user or system.


Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
LastViewedDate

LocationId

Name

NewSalePricePerUnit

NewSalePriceType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and timestamp when the record was last opened in the UI.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the inventory or sales location relevant to the line item.

This field is a relationship field.

**Relationship Name**
Location

**Refers To**
Location

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated identifier for the line item record.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The new sale price per unit after the price change.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of sale price applied post-adjustment (e.g., List Price, Net Price).


Standard Objects PriceProtectExecLineItem

**Field** **Details**

```
PriceDifference

PriceProtectionExecutionId

PriceProtectionTermId

ProductId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Difference between the old and new sale price per unit.

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Links to the parent Price Protection Execution record.

This field is a relationship field.

**Relationship Name**
PriceProtectionExecution

**Relationship Type**
Master-detail

**Refers To**
PriceProtectionExecution (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the Price Protection Term used for evaluating eligibility and calculations.

This field is a relationship field.

**Relationship Name**
PriceProtectionTerm

**Refers To**
PriceProtectionTerm

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the product involved in the price protection claim.


Standard Objects PriceProtectExecLineItem

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Product

**Refers To**
Product2

```
RemainingQuantity

SalePricePerUnit

SalePriceType

Status

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Quantity of product still eligible for claim after partial adjustments.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Original sale price per unit before the price adjustment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of sale price recorded during the original transaction.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Current processing state of the line item.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `New`

**•** `ReadyForClaim` —Ready For Claim

**•** `ReadyForPricing` —Ready For Pricing

**•** `ReadyForSimulation` —Ready For Simulation


### Standard Objects PriceProtectionTerm

**Field** **Details**

```
StatusReason

TransactionDate

TransactionReferenceId

WarningMessage

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional explanation or message associated with the current status.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date when the original sale or transaction occurred.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the transaction record from which this line item originates.

This field is a polymorphic relationship field.

**Relationship Name**
TransactionReference

**Refers To**
PartnerUnsoldInventory

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Descriptive warning associated with this line item, if applicable.

### PriceProtectionTerm

Represents a configuration record that defines the rules, types, and eligible conditions for price protection. This object is available in API
version 63.0 and later.

A PriceProtectionTerm record is referenced during claims processing to calculate supported price and quantity adjustments based on
predefined terms.


Standard Objects PriceProtectionTerm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CalculationReferenceRecordId

IsPayable

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Rebate type that's applicable for the claim amount calculation. This field is a relationship
field.

**Relationship Name**
CalculationReferenceRecord

**Refers To**
ProgramRebateType

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the inventory is eligible for payment or refund after a price protection
adjustment.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the record was last referenced by the current user. Useful for activity
tracking.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PriceProtectionTerm

**Field** **Details**

**Description**

Date and the timestamp when the record was last viewed by the user. Helps in understanding
record engagement.

```
Name

NewSalePriceType

OwnerId

PriceProtectionType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique name for the Price Protection Term. This is typically used as a primary identifier for
UI display or business logic.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the type of new sale price applicable after a price protection scenario. This helps
classify how the adjusted sale price can be handled.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifier for the user or group who owns the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the type of price protection applied.

Possible values are:

**•** `PriceProtection` —Price Protection

**•** `ReversePriceProtection` —Reverse Price Protection


### Standard Objects PrivacyHold

**Field** **Details**

The default value is `PriceProtection` .

```
SalePriceType

SupportedPricePercent

SupportedQuantityPercent

### PrivacyHold

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of sale price before price protection is applied. This helps calculate the
protection delta during claim processing.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of the price that is supported for price protection. Helps calculate
eligible claim amounts.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of quantity that is eligible for price protection. Used to determine
prorated reimbursement.

Represents a Privacy Hold that indicates that a record should be preserved from masking or deletion by Data Management policies in
Privacy Center. This object is available in API version 59.0 and later.

Use Privacy Hold with Data Management policies in Privacy Center. Add a condition to your policy to exclude records with an active
Privacy Hold status from masking or deletion actions.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.


Standard Objects PrivacyHold

Fields

**Field** **Details**

```
EndDate

IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if Privacy Hold is active on the record.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Hold.

**Type**
reference


Standard Objects PrivacyHold

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PrivacyHoldReasonId

ReferenceRecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the associated Privacy Hold Reason.

This field is a relationship field.

**Relationship Name**
PrivacyHoldReason

**Relationship Type**
Lookup

**Refers To**
PrivacyHoldReason

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record marked for the Privacy Hold.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, Lead, User


### Standard Objects PrivacyHoldReason

**Field** **Details**

```
ReferenceRecordType

RegisteredDate

### PrivacyHoldReason

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the record with the Privacy Hold is associated with.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`

**•** `User`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold was added to the record.

Represents the business or legal purpose for why a record has a Privacy Hold. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.

Fields

**Field** **Details**

```
Detail

```

**Type**
string


Standard Objects PrivacyHoldReason

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The details of the Privacy Hold Reason, such as the business or legal purpose for the hold.

```
LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Hold Reason.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects PrivacyJobSession PrivacyJobSession

Represents the status of past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and later.

This object is Read-only.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
CreationDate

CurrentObject

EndTime

FailureLog

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that the policy job is currently processing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job finished executing.

**Type**
textarea

**Properties**
Nillable


Standard Objects PrivacyJobSession

**Field** **Details**

**Description**
The description of why the policy job failed to execute.

```
JobStartType

JobStatus

Name

OptionsProcessingFailed

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the policy job session was started.

Possible values are:

**•** `manual`

**•** `scheduled`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the status of the policy job session.

Possible values are:

**•** `cancelled`

**•** `completed`

**•** `failures`

**•** `inactive`

**•** `running`

**•** `running_next`

**•** `scheduled`

**•** `suspended`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
boolean

**Properties**
Filter


Standard Objects PrivacyJobSession

**Field** **Details**

**Description**
Indicates that the policy job session failed to process the records with the deletion or masking
rules in the policy.

```
OptionsTraversalComplete

OptionsTraversalFailed

OwnerId

PolicyDescription

PolicyName

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session was completed without errors.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session was completed with errors.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the policy the job session is associated with.

**Type**
string


Standard Objects PrivacyJobSession

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy the job session is associated with.

```
PolicyType

PrivacyPolicyDefinitionId

PrivacyRtbfRequestId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of policy the job session is associated with.

Possible values are:

**•** `datamanagement` —Data Management.

**•** `datamask` —This policy type is reserved for future use.

**•** `rtbf`  - Right to Be Forgotten.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the policy the job session is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyPolicyDefinition

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Right to Be Forgotten request the policy job is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyRtbfRequest


### Standard Objects PrivacyObjectSession

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PrivacyRTBFRequest

```
ScheduledTime

SerializedPolicy

StartTime

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session is scheduled to run.

**Type**
textarea

**Properties**
Nillable

**Description**
The serial ID of a snapshot of the policy the job session is for. A snapshot of the policy is taken
to maintain consistent metadata for the policy the job is for, in case changes are made to
the policy while the job is executing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session started executing.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyJobSessionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyJobSessionShare on page 67**
Sharing is available for the object.

### PrivacyObjectSession

Represents the status of each object being processed in past, ongoing, and scheduled policy jobs in Privacy Center. This object is available
in API version 59.0 and later.


Standard Objects PrivacyObjectSession

See the status of each object as a policy executes. For example, if a Data Management policy includes an Account object and a Contact
object, then a PrivacyObjectSession record is created for each object.

Each object in a policy has five potential queues to enter. The first queue captures and stores records targeted by the policy filters. If the
first queue run fails to capture every record, then the object goes through three retry attempts to capture the remaining records. The
fifth queue stores the record IDs of any records that weren’t captured in any of the four attempts.

This object is Read-only.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
CurrentEntity

Name

ObjectFailureLog

ObjectStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object in the policy.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
textarea

**Properties**
Nillable

**Description**
This field is reserved for later use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects PrivacyObjectSession

**Field** **Details**

**Description**
The policy execution status for the object.

Possible values are:

**•** `processing_completed`

**•** `processing_failed`

**•** `processing_ongoing`

**•** `processing_pending`

**•** `traversal_completed`

**•** `traversal_failed`

**•** `traversal_ongoing`

```
OwnerId

PolicyNode

Position

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with the customer that the policy was executed
for.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object in the serialized policy. This field associates the object session in the
policy execution with the coordinating object in the Privacy Center policy.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a record’s position in the batch queue for the object being processed.


Standard Objects PrivacyObjectSession

**Field** **Details**

```
PrivacyJobSessionObjectId

ProcessType

ProcessedFailures

ProcessedSuccesses

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyJobSessionObject

**Relationship Type**
Lookup

**Refers To**
PrivacyJobSession

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of action being executed on the object in the policy.

Possible values are:

**•** `delete`

**•** `mask`

**•** `retry_delete`

**•** `retry_mask`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution failed to process.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution successfully processed.


Standard Objects PrivacyObjectSession

**Field** **Details**

```
ProcessedTotal

Processor

Queue

QueueLength

RecordsAffected

Retry

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records processed in the policy job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the deletion, masking, or traversal processor executing the policy job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for later use.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records in the queue to be processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects PrivacyRequest

**Field** **Details**

**Description**
The queue number of the retry session after a failed policy execution attempt. Each attempt
to retry the policy execution is put into a retry queue.

```
TraversalEndTime

TraversalStartTime

UniqueConstraint

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end time of the record-capturing phase for the object session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start time of the record-capturing phase for the object session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For internal use only.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyObjectSessionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyObjectSessionShare on page 67**
Sharing is available for the object.

### PrivacyRequest

See details and monitor the status of Data Subject Access Requests made in Privacy Center. This object is available in API version 54.0
and later.


Standard Objects PrivacyRequest

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

Fields

**Field** **Details**

```
CompletedDateTime

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Request.

**Type**
reference


Standard Objects PrivacyRequest

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RelatedRecord

StartedDateTime

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Subject Access Request (DSAR) or Right to Be Forgotten request (RTBF) record
related to the request.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Approved`

**•** `Cancelled`

**•** `Completed`

**•** `Created`

**•** `In Progress`

**•** `Rejected`


Standard Objects PrivacyRequest

**Field** **Details**

```
TargetRecord

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record that is listed in the request.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the type of request that was made.

Possible values are:

**•** `DSAR`

**•** `GlobalOptOut`

**•** `RTBF`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRequestFeed on page 55**
Feed tracking is available for the object.

**PrivacyRequestHistory on page 63**
History is available for tracked fields of the object.

**PrivacyRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyRequestShare on page 67**
Sharing is available for the object.

Usage

In API version 66.0 and later, users can click **New Privacy Request** to create privacy requests directly from the Privacy Requests page.
This action supports Right to Be Forgotten (RTBF) request types. The New Privacy Request button uses a custom dialog based on search
criteria defined in Setup. The standard New button uses the default record creation dialog. To streamline the user interface and avoid
redundancy, hide the standard New button.


### Standard Objects PrivacyRTBFRequest PrivacyRTBFRequest

Represents a Right to Be Forgotten Request made in Privacy Center. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

Fields

**Field** **Details**

```
Description

JobRecord

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the customer’s Right to Be Forgotten request.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID that is processed by the Right to Be Forgotten request.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PrivacyRTBFRequest

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

PolicyNameId

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Right to Be Forgotten request.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Right to Be Forgotten policy applied to this request.

This field is a relationship field.

**Relationship Name**
PolicyName

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
picklist


### Standard Objects PrivacySessionRecordFailure

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Cancelled`

**•** `Complete`

**•** `Error`

**•** `Pending`

**•** `Scheduled`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRTBFRequestHistory on page 63**
History is available for tracked fields of the object.

**PrivacyRTBFRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacyRTBFRequestShare on page 67**
Sharing is available for the object.

### PrivacySessionRecordFailure

Represents error messages encountered during policy job executions in Privacy Center. This object is available in API version 59.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.


Standard Objects PrivacySessionRecordFailure

Fields

**Field** **Details**

```
ErrorMessage

ErrorType

Name

OwnerId

PrivacyObjectSessionId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the error encountered during the policy job execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of error encountered during the policy job execution.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with the customer that the policy was executed
for.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


### Standard Objects Problem

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the object in the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyObjectSession

**Relationship Type**
Lookup

**Refers To**
PrivacyObjectSession

```
RecordIdNumber

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that failed to be processed by the policy job.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacySessionRecordFailureOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PrivacySessionRecordFailureShare on page 67**
Sharing is available for the object.

### Problem Problems represent the root cause data of one or more incidents. This object contains all the details of a problem, documenting the

history of the problem from detection to closure. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Problem

Fields

**Field** **Details**

```
Category

Description

Impact

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The type of problem. Administrators set field values.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The problem's impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Problem

**Field** **Details**

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view.
( `LastReferencedDate` ) but not viewed it.

```
OwnerId

ParentProblemId

Priority

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This is a polymorphic relationship field that represents the user or group assigned to resolve
the problem.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a problem above one or more related problems in a problem hierarchy.

This is a relationship field.

**Relationship Name**
ParentProblem

**Relationship Type**
Lookup

**Refers To**
Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the problem.

Possible values are:

**•** `Critical`


Standard Objects Problem

**Field** **Details**

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
PriorityOverrideReason

ProblemNumber

ResolutionDateTime

ResolutionSummary

ResolvedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the priority should be changed or edited.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated problem number.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the problem was resolved.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the steps needed to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who resolved the problem.

This is a relationship field.


Standard Objects Problem

**Field** **Details**

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

```
RootCauseSummary

Status

StatusCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem resolution or root cause. This field can store up to 32 KB of data,
but only the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages customers wants to track. This will be a dependent picklist.

Possible values are:

**•** `Closed`

**•** `Fix in Progress`

**•** `Known Error`

**•** `New`

**•** `Open`

**•** `Pending Change`

**•** `Resolved`

**•** `Root Cause Analysis`

**•** `Work In Progress`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the problem.

Possible values are:


Standard Objects Problem

**Field** **Details**

**•** `Closed`

**•** `FixInProgress`

**•** `KnownError`

**•** `New`

**•** `Open`

**•** `PendingChange`

**•** `Resolved`

**•** `RootCauseAnalysis`

**•** `WorkInProgress`

The default value is 'New'.

```
SubCategory

Subject

Urgency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of problem. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the problem.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long a resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


### Standard Objects ProblemIncident ProblemIncident

Represents a junction object that relates a Problem to an Incident. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IssueId

Name

RelatedEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

**Relationship Name**
Issue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident that's related to the problem.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object type of the related entity.

Possible values are:

**•** `Incident`


Standard Objects ProblemIncident

**Field** **Details**

**•** `Problem`

```
RelatedIssueId

RelationshipType

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the Problem and Incident records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Similar`

The default value is `Caused By` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemIncidentChangeEvent on page 68**
Change events are available for the object.

**ProblemIncidentFeed on page 55**
Feed tracking is available for the object.

**ProblemIncidentHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ProblemRelatedItem ProblemRelatedItem

Represents a junction object that relates a Problem to an Asset. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

Comment

ImpactLevel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the Problem.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the problem.

Possible values are:

**•** `High`


Standard Objects ProblemRelatedItem

**Field** **Details**

**•** `Low`

**•** `Medium`

The default value is `High` .

```
ImpactType

Name

ProblemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The effect of the problem-related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the problem-related item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Problem ID that’s related to the Asset.

This field is a relationship field.

**Relationship Name**
Problem

**Relationship Type**
Lookup

**Refers To**
Problem


### Standard Objects ProcessDefinition

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemRelatedItemChangeEvent on page 68**
Change events are available for the object.

**ProblemRelatedItemFeed on page 55**
Feed tracking is available for the object.

**ProblemRelatedItemHistory on page 63**
History is available for tracked fields of the object.

### ProcessDefinition

Represents the definition of a single approval process.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Portal and communities users with the Customer Community Plus and Partner Community licenses can access this object. All users in
org with approvals enabled have read access to ProcessDefinition.

Fields

**Field** **Details**

```
Description

DeveloperName

LockType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description of this process, with a maximum of 3,000 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique process name, used internally.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects ProcessDefinition

**Field** **Details**

**Description**
The type of lock applied to the record being approved. When a record is in the approval
process, it’s always locked, and only an administrator can edit it. However, the currently
assigned approver can also be allowed to edit the record.

**•** Total

**•** Admin

**•** Owner

**•** Workitem

**•** Node

**•** none

```
Name

State

TableEnumOrId

Type

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The external name of the process; the name seen by users.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current state of this process.

**•** Active

**•** Inactive

**•** Obsolete

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the object associated with the approval process, such as Account or Contact.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this process.


### Standard Objects ProcessException

**Field** **Details**

**•** Approval Process—Used to control the action taken for a record.

**•** State-based Process—Used internally to track various control processes, such as for
developing Salesforce Knowledge articles.

Usage

Use this object to read the description of an approval process. The definition is read-only.

### ProcessException

Represents a business exception, such as a processing failure on an order summary. A separate process is required to resolve the failure
that caused the process exception before processing can continue. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AttachedToId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the object associated with the ProcessException.

This field is a polymorphic relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
AsyncOpSyndicationFeedFile, AsyncOperationTracker

CreditMemo, FulfillmentOrder, Invoice, Order, OrderItem, OrderItemSummary,
OrderPaymentSummary, OrderSummary, Payment, PaymentAuthorization, Refund,
ReturnOrder

**Type**
reference


Standard Objects ProcessException

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the case associated with the ProcessException.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
Category

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ProcessingException type. You can customize the category picklist to represent your business
processes.

Possible values are:

**•** `Fulfillment`

**•** `Invoicing`

**•** `Order Activation`

**•** `Order Approval`

**•** `Order To Asset`

**•** `Order Item Summary To Asset`

**•** `Order To Billing Schedule`

**•** `Payment`

The default value is `Order Activation` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the ProcessException.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro


Standard Objects ProcessException

**Field** **Details**

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
Description

ExternalReference

FlowOrchestrationInstRelaObj

GroupById

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Detailed description of the ProcessException.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of external entities associated with the ProcessException.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The flow orchestration instance related object associated with this record.

This field is a relationship field.

**Relationship Name**
FlowOrchInstRelaObj

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstRelaObj

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID used in the entity to group exceptions, such as the Async Operation Tracker.

This field is a polymorphic relationship field.

**Relationship Name**
GroupBy


Standard Objects ProcessException

**Field** **Details**

**Refers To**
AsyncOperationTracker

```
LastReferencedDate

LastViewedDate

Message

OrderSummaryId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. A null value can mean that this
record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Short description of the ProcessException

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the OrderSummary associated with the ProcessException. The ProcessException
component is displayed on this OrderSummary.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary


Standard Objects ProcessException

**Field** **Details**

```
OwnerId

Priority

ProcessExceptionNumber

Severity

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this ProcessException. Default value is the User who
created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Resolution priority for the ProcessException. You can customize the priority picklist to
represent your business processes.

Possible values are:

**•** `High`

**•** `Low`

The default value is `Low` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the ProcessException, formatted as PE-(00000000).

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ProcessException

**Field** **Details**

**Description**
Severity of the ProcessException. Each severity value corresponds to one severity category.
You can customize the severity picklist to represent your business processes. If you customize
the severity picklist, include at least one severity value for each severity category.

Possible values are:

**•** `High`

**•** `Low`

The default value is `High` .

```
SeverityCategory

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Severity category of the ProcessException. Each severity category corresponds to one or
more severity values. The severity category is used to show the severity icon in the
ProcessException list view.

Possible values are:

**•** `HIGH`

**•** `LOW`

**•** `MEDIUM`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the ProcessException. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes.
If you customize the status picklist, include at least one status value for each status category.

Possible values are:

**•** `Ignored` (Inactive)

**•** `New` (Active)

**•** `Paused` (Inactive)

**•** `Resolved` (Resolved)

**•** `Triaged` (Active)

**•** `Voided` (Inactive)

The default value is `New` .


### Standard Objects ProcessFlowMigration

**Field** **Details**

```
StatusCategory

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the ProcessException. Each status category corresponds to one or more
statuses.

Possible values are:

**•** `ACTIVE`

**•** `INACTIVE`

**•** `RESOLVED`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProcessExceptionChangeEvent (API version 62.0)**
Change events are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.

### ProcessFlowMigration

Represents a process's migrated criteria and the resulting migrated flow. This object is available in API version 58.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ProcessFlowMigration

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.

```
Language

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Lanaguage of the `MasterLabel` .

Possible values are:

**•** `af` —Afrikaans

**•** `am` —Amharic

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)

**•** `ar_EG` —Arabic (Egypt)

**•** `ar_IQ` —Arabic (Iraq)

**•** `ar_JO` —Arabic (Jordan)

**•** `ar_KW` —Arabic (Kuwait)

**•** `ar_LB` —Arabic (Lebanon)

**•** `ar_LY` —Arabic (Libya)

**•** `ar_MA` —Arabic (Morocco)

**•** `ar_OM` —Arabic (Oman)

**•** `ar_QA` —Arabic (Qatar)

**•** `ar_SA` —Arabic (Saudi Arabia)

**•** `ar_SD` —Arabic (Sudan)

**•** `ar_SY` —Arabic (Syria)

**•** `ar_TN` —Arabic (Tunisia)

**•** `ar_YE` —Arabic (Yemen)

**•** `bg` —Bulgarian

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh

**•** `da` —Danish


Standard Objects ProcessFlowMigration

**Field** **Details**

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `el_CY` —Greek (Cyprus)

**•** `en_AE` —English (United Arab Emirates)

**•** `en_AU` —English (Australian)

**•** `en_BE` —English (Belgium)

**•** `en_CA` —English (Canadian)

**•** `en_CY` —English (Cyprus)

**•** `en_DE` —English (Germany)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IL` —English (Israel)

**•** `en_IN` —English (Indian)

**•** `en_MT` —English (Malta)

**•** `en_MY` —English (Malaysian)

**•** `en_NL` —English (Netherlands)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

**•** `es_CR` —Spanish (Costa Rica)

**•** `es_DO` —Spanish (Dominican Republic)

**•** `es_EC` —Spanish (Ecuador)

**•** `es_GT` —Spanish (Guatemala)

**•** `es_HN` —Spanish (Honduras)

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)


Standard Objects ProcessFlowMigration

**Field** **Details**

**•** `es_PA` —Spanish (Panama)

**•** `es_PE` —Spanish (Peru)

**•** `es_PR` —Spanish (Puerto Rico)

**•** `es_PY` —Spanish (Paraguay)

**•** `es_SV` —Spanish (El Salvador)

**•** `es_US` —Spanish (United States)

**•** `es_UY` —Spanish (Uruguay)

**•** `es_VE` —Spanish (Venezuela)

**•** `et` —Estonian

**•** `eu` —Basque

**•** `fa` —Farsi

**•** `fi` —Finnish

**•** `fr` —French

**•** `fr_BE` —French (Belgium)

**•** `fr_CA` —French (Canadian)

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `fr_MA` —French (Morocco)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `haw` —Hawaiian

**•** `hi` —Hindi

**•** `hmn` —Hmong

**•** `hr` —Croatian

**•** `ht` —Haitian Creole

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ji` —Yiddish

**•** `ka` —Georgian

**•** `kk` —Kazakh

**•** `kl` —Greenlandic

**•** `km` —Khmer


Standard Objects ProcessFlowMigration

**Field** **Details**

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo

**•** `mk` —Macedonian

**•** `ml` —Malayalam

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pa` —Punjabi

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `ru_AM` —Russian (Armenia)

**•** `ru_BY` —Russian (Belarus)

**•** `ru_KG` —Russian (Kyrgyzstan)

**•** `ru_KZ` —Russian (Kazakhstan)

**•** `ru_LT` —Russian (Lithuania)

**•** `ru_MD` —Russian (Moldova)

**•** `ru_PL` —Russian (Poland)

**•** `ru_UA` —Russian (Ukraine)

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sm` —Samoan

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)


Standard Objects ProcessFlowMigration

**Field** **Details**

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_MY` —Chinese (Malaysia)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
MasterLabel

MigratedCriteriaLabel

MigratedCriteriaName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the ProcessFlowMigration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the criteria that was migrated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the criteria that was migrated.


### Standard Objects ProcessInstance

**Field** **Details**

```
NamespacePrefix

### ProcessInstance

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the package containing the process flow migration object.

Represents an instance of a single, end-to-end approval process. Use this and the node, step, and workitem process instance objects to
create approval history reports.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

For approval process instances that were completed before the Summer '14 rollout, all Process Instance fields are automatically populated,
with one exception: `CompletedDate` is never populated for approval process instances that were completed before January 1, 2013.
For approval process instances that were pending during the Summer '14 rollout, all ProcessInstance fields are automatically populated,
with two exceptions: `CompletedDate` and `LastActorId` are populated only after the approval process instance is complete.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompletedDate

ElapsedTimeInDays

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of the approval process. The `ElapsedTimeDay,`
`ElapsedTimeHours`, and `ElapsedTimeMinutes` field values are calculated using
`CompletedDate` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ProcessInstance

**Field** **Details**

**Description**
The total elapsed time in days between when the approval process instance was started and
now.

```
ElapsedTimeInHours

ElapsedTimeInMinutes

LastActorId

ProcessDefinitionId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in hours between when the approval process instance was started
and now.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in minutes between when the approval process instance was started
and now.

**Type**
reference

**Properties**
Group, Filter, Nillable, Sort

**Description**
The last actor that approved, rejected, or recalled the process.

This is a relationship field.

**Relationship Name**
LastActor

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Group, Filter, Sort

**Description**
The ID of this approval process instance.

This is a relationship field.


Standard Objects ProcessInstance

**Field** **Details**

**Relationship Name**
ProcessDefinition

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition

```
Status

SubmittedById

TargetObjectId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of this approval process instance.

Possible values are:

**•** `Approved`

**•** `Fault`

**•** `Held`

**•** `NoResponse`

**•** `Pending`

**•** `Reassigned`

**•** `Rejected`

**•** `Removed`

**•** `Started`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who submitted the approval process.

This is a relationship field.

**Relationship Name**
SubmittedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


Standard Objects ProcessInstance

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval process instance.

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, Award, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, Campaign, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CodeSetBundle, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConsumptionRate, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, DataStream, DataUseLegalBasis,
DataUsePurpose, DelegatedAccount, DigitalSignature, DocumentChecklistItem,
DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType,
EnrollmentEligibilityCriteria, ExternalEventMapping, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, IdentityDocument,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, LocationTrustMeasure,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingEndUser,
MessagingSession, MktCalculatedInsight, Opportunity, Order, OrgMetricScanResult,
OrgMetricScanSummary, OtherComponentTask, PartyConsent, PaymentAuthAdjustment,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, ProcessException, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction,
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, Quote, ReceivedDocument,


### Standard Objects ProcessInstanceHistory

**Field** **Details**

ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, ServiceAppointment, ServiceResource,
ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SharingRecordCollection, SharingRecordCollectionItem, SharingRecordCollectionMember,
Shift, Shipment, ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel,
UnitOfMeasure, UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording,
Visit, VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember

Usage

Use this object to query or retrieve an approval process.

The following SOQL query returns details for all the ProcessInstanceStep records related to individual ProcessInstance records. The nested
query references `Steps`, which is the child `relationshipName` for ProcessInstanceStep in the ProcessInstance object.

```
   SELECT Id, (SELECT Id, StepStatus, Comments FROM Steps)

   FROM ProcessInstance

```

The following SOQL query returns details for all the ProcessInstanceWorkItem records related to individual ProcessInstance records. The
nested query references `Workitems`, which is the child `relationshipName` for ProcessInstanceWorkItem in the ProcessInstance
object.

```
   SELECT Id, (SELECT Id, ActorId, ProcessInstanceId FROM Workitems)

   FROM ProcessInstance

### ProcessInstanceHistory can help provide a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects.

```

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

### **ProcessInstanceHistory**

History is available for tracked fields of the object.

**ProcessInstanceChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

### ProcessInstanceHistory

ProcessInstanceStep

ProcessInstanceWorkitem

### ProcessInstanceHistory

This read-only object shows all steps and pending approval requests associated with an approval process (ProcessInstance).


Standard Objects ProcessInstanceHistory

Supported Calls

```
   describeSObjects()

```

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
ActorId

Comments

ElapsedTimeInDays

ElapsedTimeInHours

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is assigned to this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Comments for a ProcessInstanceStep . This field doesn't apply to ProcessInstanceWorkitem
records.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days between when the approval process instance was started and when
it was completed.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ProcessInstanceHistory

**Field** **Details**

**Description**
The total time in hours between when the approval process instance was started and when
it was completed.

```
ElapsedTimeInMinutes

IsPending

OriginalActorId

ProcessInstanceId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes between when the approval process instance was started and
when it was completed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the ProcessInstance is pending ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance.

This is a relationship field.


Standard Objects ProcessInstanceHistory

**Field** **Details**

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

```
ProcessNodeId

RemindersSent

StepStatus

TargetObjectId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of reminders that have been sent. Default is 0 (zero).

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the ProcessInstanceStep.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object being approved.


Standard Objects ProcessInstanceHistory

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, Award, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, Campaign, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CodeSetBundle, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConsumptionRate, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, DataStream, DataUseLegalBasis,
DataUsePurpose, DelegatedAccount, DigitalSignature, DocumentChecklistItem,
DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType,
EnrollmentEligibilityCriteria, ExternalEventMapping, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, IdentityDocument,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, LocationTrustMeasure,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingEndUser,
MessagingSession, MktCalculatedInsight, Opportunity, Order, OrgMetricScanResult,
OrgMetricScanSummary, OtherComponentTask, PartyConsent, PaymentAuthAdjustment,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, ProcessException, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction,
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, ReceivedDocument, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType, SharingRecordCollection,
SharingRecordCollectionItem, SharingRecordCollectionMember, Shift, Shipment,
ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel, UnitOfMeasure,


### Standard Objects ProcessInstanceNode

**Field** **Details**

UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording, Visit,
VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

Usage

This object helps you replicate the related list functionality of the Salesforce user interface for approval processes. Use ProcessInstanceHistory
for a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects. You can’t query ProcessInstanceHistory.
Instead, you can query ProcessInstanceHistory by including it in a nested query on the parent ProcessInstance object. For example, this
SOQL query returns all the ProcessInstanceHistory records related to individual ProcessInstance records. The nested query references
`StepsAndWorkitems`, which is the child `relationshipName` for ProcessInstanceHistory in the ProcessInstance object.

```
   SELECT Id, (SELECT Id, StepStatus, Comments FROM StepsAndWorkitems)

     FROM ProcessInstance

```

This object respects field-level security on the parent object.

SEE ALSO:

### ProcessInstance

ProcessInstanceStep

ProcessInstanceWorkitem

### ProcessInstanceNode

Represents a step in an instance of an approval process. Compare to ProcessNode, which describes the step in a process definition. Use
this object to retrieve approval history.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceNode fields are never populated for approval process instances that were completed before the Summer '14 rollout. For

approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceNode fields are populated only after
the approval process instance is next acted upon after the Summer '14 rollout.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ProcessInstanceNode

Fields

**Field** **Details**

```
CompletedDate

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

LastActorId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of this step in the approval process. The `ElapsedTimeDay,`
`ElapsedTimeHours`, and `ElapsedTimeMinutes` field values are calculated using
`CompletedDate` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this step was started.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last actor that approved or rejected this step.

This is a relationship field.

**Relationship Name**
LastActor


Standard Objects ProcessInstanceNode

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
NodeStatus

ProcessInstanceId

ProcessNodeId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval instance, for example Started, Pending, or Approved.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval process this step is part of.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The identifier for this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode


### Standard Objects ProcessInstanceStep

**Field** **Details**

```
ProcessNodeName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of this step.

The contents of this field can be publicly viewed.

### ProcessInstanceStep

Represents one work item in an approval process (ProcessInstance).

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceStep fields are never populated for approval process instances that were completed before the Summer '14 rollout. For

approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceStep fields are populated only after the
approval process instance is next acted upon after the Summer '14 rollout.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActorId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who’s assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ProcessInstanceStep

**Field** **Details**

```
Comments

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

OriginalActorId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Limit: 4,000 bytes.

The contents of this field can be publicly viewed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this step was started.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup


Standard Objects ProcessInstanceStep

**Field** **Details**

**Refers To**
Group, User

```
ProcessInstanceId

StepNodeId

StepStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance that this approval step belongs to.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the node currently assigned to this approval step.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval step.

**•** Approved

**•** Fault

**•** Held

**•** NoResponse

**•** Pending

**•** Reassigned

**•** Rejected

**•** Removed

**•** Started


### Standard Objects ProcessInstanceWorkitem

**Field** **Details**

If the approval step requires unanimous approval and one approver rejects the request, the
value of this field for the other approvers changes to NoResponse. Likewise, if approval is
based on the first response and an approver responds, the value of this field for the other
approvers changes to NoResponse.

Usage

Query or retrieve a new step in an approval process (ProcessInstance).

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ProcessInstanceStepChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

### ProcessInstance

ProcessInstanceHistory

### ProcessInstanceWorkitem ProcessInstanceWorkitem

Represents a user’s pending approval request.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

### ProcessInstanceWorkitem fields are never populated for approval process instances that were completed before the Summer ’14 rollout.

For approval process instances that were pending during the Summer ’14 rollout, all ProcessInstanceWorkitem fields are populated after
the approval process instance is next acted upon after the Summer ’14 rollout, with three exceptions. The `ElapsedTimeInDays`,
`ElapsedTimeInHours`, and `ElapsedTimeInMinutes` fields are never populated in ProcessInstanceWorkitem records for
which equivalent ProcessInstanceStep records were created before the Summer ’14 rollout.

For all other ProcessInstanceWorkitem records, these three fields are populated after the approval process instance is next acted upon
after the Summer ’14 rollout.

ProcessInstanceHistory combines fields from ProcessInstanceStep and ProcessInstanceWorkitem. As a result, incorrect elapsed times of
0 can appear in ProcessInstanceHistory records because the elapsed time fields were never populated in the related
### ProcessInstanceWorkitem record.

Note: Knowledge articles use ProcessInstanceWorkitem records to track the article history, so ProcessInstanceWorkitems records
associated with Knowledge articles can’t be deleted.


Standard Objects ProcessInstanceWorkitem

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
ActorId

ElapsedTimeInDays

ElapsedTimeInHours

ElapsedTimeInMinutes

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user responsible for approving an approval request.

This field is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this approval request was started.


Standard Objects ProcessInstanceWorkitem

**Field** **Details**

```
 OriginalActorId

 ProcessInstanceId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user originally assigned this approval request.

This field is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the ProcessInstance associated with this approval request.

This field is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

Use this object to manage a pending approval request for a user.

SEE ALSO:

ProcessInstance

ProcessInstanceHistory

ProcessInstanceStep


### Standard Objects ProcessNode ProcessNode

Describes a step in a process definition. Compare to ProcessInstanceNode, which describes a step in a running process. This object is
available in API version 31.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Description

DeveloperName

Name

ProcessDefinitionId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description of this node, no longer than 3,000 bytes.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The external name of the node that’s seen by users.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique node name.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval instance.

A relationship field.

**Relationship Name**
ProcessDefinition


### Standard Objects ProducerCommission

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition

Usage

Use this object to get details about the process node or the process definition that it's associated with.

### ProducerCommission

Represents a producer's commission for an insurance policy. The commission can be calculated from the commissionable transactions
or can be populated from an external system. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommissionableAmount

CommissionAmount

CommissionScheduleId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount on which the commission is applied. This can be a transaction amount or a
portion of the premium.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The calculated commission amount for the insurance policy transaction.

**Type**
reference


Standard Objects ProducerCommission

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
CommissionSchedule

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule

```
InsurancePolicyAssetId

InsurancePolicyCoverageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insured item for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyAsset

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyAsset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy coverage for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyCoverage

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyCoverage


Standard Objects ProducerCommission

**Field** **Details**

```
InsurancePolicyId

InsurancePolicyTransactionId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insurance policy for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicy

**Relationship Type**
Lookup

**Refers To**
InsurancePolicy

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The transaction for which the commission record was created.

This is a relationship field.

**Relationship Name**
InsurancePolicyTransaction

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyTransaction

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProducerCommission

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

```
MaxCommissionAmount

MinCommissionAmount

Name

OwnerId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the producer commission.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ProducerCommission

**Field** **Details**

```
ParentProducerCommissionId

PaymentDatetime

ProcessingProducerId

ProducerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The original commission record that was adjusted or modified.

This is a relationship field.

**Relationship Name**
ParentProducerCommission

**Relationship Type**
Lookup

**Refers To**
ProducerCommission

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the commission was paid.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer who performed the commissionable event.

This is a relationship field.

**Relationship Name**
ProcessingProducer

**Relationship Type**
Lookup

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.


Standard Objects ProducerCommission

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Producer

```
ProducerProductionCode

SourceSystem

SourceSystemIdentifier

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The production code for the producer who performs the commissionable event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The system from which the producer commission record was sourced.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the producer commission record in the source system. This field is unique within
your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the commission payment.

Possible values are:

**•** `Disputed`

**•** `Paid`

**•** `Pending`

**•** `Reversed`


### Standard Objects Product2

**Field** **Details**

```
Type

### Product2

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of commission paid to a producer, account, or contact for a commissionable
transaction.

Possible values are:

**•** `Advance`

**•** `Bonus`

**•** `Chargeback`

**•** `Commission`

**•** `Contingent Commission`

Represents a product that your company sells.

This object has several fields that are used only for quantity and revenue schedules (for example, annuities). Schedules are available only
for orgs that have enabled the products and schedules features. If these features aren’t enabled, the schedule fields don’t appear, and
you can’t query, create, or update the fields.

Note: As of API version 8.0, the Product object is no longer available. Requests that contain Product are refused, and responses
don’t contain the Product object. Use the Products2 object instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ConfigureDuringSale and IsSoldOnlyWithOtherProds fields are available in version 58.0 and later when Industry Automotive or
Subscription Management is enabled.

Fields

**Field** **Details**

```
BillingPolicyId

```

**Type**
reference


Standard Objects Product2

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related billing policy. This field is available when Subscription Management is
enabled. This field is available in API version 55.0 and later.

This field is a relationship field.

**Relationship Name**
BillingPolicy

**Relationship Type**
Lookup

**Refers To**
BillingPolicy

```
CanUseQuantitySchedule

CanUseRevenueSchedule

ConnectionReceivedId

ConnectionSentId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the product can have a quantity schedule ( `true` ) or not ( `false` ). Label
is **Quantity Scheduling Enabled** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the product can have a revenue schedule ( `true` ) or not ( `false` ). Label
is **Revenue Scheduling Enabled** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your org. This field is
available when Salesforce to Salesforce is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Product2

**Field** **Details**

**Description**
ID of the PartnerNetworkConnection that this record is shared with. This field is available
Salesforce to Salesforce is enabled. In API version 16.0 and later, this value is `null` . Use
PartnerNetworkRecordConnection object to forward records to connections.

```
ConfigureDuringSale

CurrencyIsoCode

Description

DisplayUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether a user can edit a configuration when creating a bundle order or quote.

This field is available in API version 58.0 and later.

This field is available when Industries Automotive or Subscription Management is enabled.

Possible values are:

**•** `Allowed`  - Changes are allowed while adding line items to a bundle; for example,
when adding products or editing quantity.

**•** `NotAllowed` —Changes aren’t allowed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A text description of this record. Label is **Product Description** .

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL leading to a specific version of a record in the linked external data source.


Standard Objects Product2

**Field** **Details**

```
ExternalDataSourceId

ExternalId

Family

IsActive

IsArchived

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the related external data source.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of a record in the linked external data source. For example, _`ID #123`_ .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the product family associated with this record. Product families are configured as
picklists in the user interface. To obtain a list of valid values, call `describeSObjects()`
and process the result for the values associated with the `Family` field. Label is **Product**
**Family** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Inactive Product2 records
are hidden in many areas in the user interface. You can change the `IsActive` flag on a
Product2 object as often as necessary. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Describes whether the product is archived. The default value is `false` .

**Type**
boolean


Standard Objects Product2

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
IsSerialized

IsSoldOnlyWithOtherProds

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates if a product is a serialized product ( `true` ) or not ( `false` ). Label is **Serialized** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the product can be sold independently or only as part of a bundle.

This field is available in API version 58.0 and later.

This field is available when Industries Automotive or Subscription Management is enabled.

The default value is `false`, which means that the product can be sold independently.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.


Standard Objects Product2

**Field** **Details**

```
Name

NumberOfQuantityInstallments

NumberOfRevenueInstallments

ProductClass

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the product has a quantity schedule, the number of installments.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the product has a revenue schedule, the number of installments.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
This field is read-only. Its value is determined by the value of the `Type` field and whether
the product is associated with a `ProductAttribute` record. It describes whether a
product is a bundle, set, or simple product, a variation parent, or a product variation. Possible
values are:

**•** `Bundle` —This product is a parent or component in a product bundle.

**•** `Set` —This product is included in a product set.

**•** `Simple` —This product has no variations

**•** `VariationParent` —This product is a variation parent. It’s the base product for one
or more product variations and, though it has its own stock-keeping unit (SKU), isn’t a
sellable entity. Instead, it’s the parent of sellable entities—its variations.

**•** `Variation` —This product is a variation of a parent product. Each variation has its
own SKU.

When the value of `ProductClass` = `VariationParent`, it never changes. The
value of `ProductClass` changes between `Simple` and `Variation` when you attach
or detach a `ProductAttribute` record to the product.


Standard Objects Product2

**Field** **Details**

If you attach a `ProductAttribute` record to a product, then the product’s
`ProductClass` value changes to `Variation` . Conversely, when you detach all
`ProductAttribute` records from a product, the `ProductClass` value changes to
`Simple` .

The default value is `Simple` .

This field is available in API version 50.0 and later. It was introduced to support of B2B and
B2C Commerce implementations.

```
ProductCode

QuantityInstallmentPeriod

QuantityScheduleType

QuantityUnitOfMeasure

RecalculateTotalPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default product code for this record. Your org defines the product’s code-naming pattern.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the product has a quantity schedule, the amount of time covered by the schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the quantity schedule, if the product has one.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unit of the product; for example, kilograms, liters, or cases. This field comes with only one
value, Each, so consider creating your own. The `QuantityUnitOfMeasure` field on
ProductItem inherits this field’s values.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Product2

**Field** **Details**

**Description**
Changes behavior of OpportunityLineItem calculations when a line item has child schedule
rows for the `Quantity` value. When enabled, if the rollup quantity changes, then the
quantity rollup value is multiplied against the sales price to change the total price.

```
RevenueInstallmentPeriod

RevenueScheduleType

StockCheckMethod

StockKeepingUnit

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the product has a revenue schedule, the time period covered by the schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the revenue schedule, if the product has one.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The method for how a product's inventory is checked. Stock checks on parent products are
common when bundles are prepackaged and individual child components can't be sold
separately. Stock checks on child products are common when bundles aren't prepackaged
and must be put together during fulfillment. If bundles aren’t prepackaged, child components
can usually be sold separately.

Possible values are:

**•** `Null` —Check stock on the product SKU.

**•** `DoNotCheck` —The stock shouldn't be check.

**•** `ParentProduct` —If the product is a parent of a bundle, check stock on the parent
product.

**•** `ChildProducts` —If the product is a parent of a bundle, check stock on the child
components.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Product2

**Field** **Details**

**Description**
The SKU for the product. Use in tandem with or instead of the `ProductCode` field. For
example, you can track the manufacturer’s identifying code in the Product Code field and
assign the product a SKU when you resell it.

```
TaxPolicyId

TransferRecordMode

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax policy.

This field is available when Subscription Management is enabled. This field is available in API
version 55.0 and later.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If serialized, indicates when the serial number is recorded. This field is visible based on
field-level security.

The value affects the read-only value of the `Product2TransferMode` field on the
`ProductTransfer` object.

Possible values are:

**•** `SendAndReceive` —The serial number is recorded when sending or receiving.

**•** `ReceiveOnly` —The serial number is recorded when receiving only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects Product2

**Field** **Details**

**Description**
The type of product. This field's value affects the read-only value of the `ProductClass` field
on the `Product2` object. The following mappings define how the `Type` selection updates
the `ProductClass` .

**•** `Base` —When `Type` = `Base`, then `ProductClass` = `VariationParent` .

**•** `Null` —When `Type` = `Null`, then `ProductClass` = `Simple` for standalone
products.

**•** `Null` —When `Type` = `Null`, then `ProductClass` = `Variation` for variation
products.

**•** `Bundle` —When `Type` = `Bundle`, then `ProductClass` = `Bundle` .

**•** `Set` —When `Type` = `Set`, then `ProductClass` = `Set` .

Note:

**•** Revenue Cloud doesn't support products with:

**–** `Type` = `Base` and `ProductClass` = `VariationParent` .

**–** `Null` and `ProductClass` = `Variation` .

.

**•** Values `Null`, `Base`, `Bundle`, and `Set` are available in environments where
both Commerce and Revenue Cloud co-exist.

**•** The Type field can only be updated from Null to Bundle for products with a Simple
ProductClass

This field is available when Revenue Cloud, B2B Commerce, B2C Commerce, or other clouds
with PCM add-on is enabled.

This field is available in API version 50.0 and later.

```
UnitOfMeasureId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the unit of measure associated with the product.

This field is a relationship field.

This field is available when Revenue Cloud is enabled.

This field is available in API version 63.0 and later.

**Relationship Name**
UnitOfMeasure

**Refers To**
UnitOfMeasure


Standard Objects Product2

Schedule Enabled Flags

When enabling the schedules feature, you can decide whether to enable quantity schedules, revenue schedules, or both. In addition,
you can use the API to control quantity and revenue scheduling at the product level via the `CanUseQuantitySchedule` and
`CanUseRevenueSchedule` flags. A value of `true` for either flag indicates that the product and any `OpportunityLineItems`
can have a schedule of that type. These flags can be set when creating or updating Product2 records.

Default Schedule Fields

The remaining schedule fields for this object define default schedules. Default schedule values are used to create an
OpportunityLineItemSchedule when an OpportunityLineItem is created for the Product.

The default schedule fields support the following valid values (all fields are also nillable).

**Field** **Valid Values**

`RevenueScheduleType` Divide, Repeat

`RevenueInstallmentPeriod` Daily, Weekly, Monthly, Quarterly, Yearly

`NumberOfRevenueInstallments` Integer from 1 to 150, inclusive.

`QuantityScheduleType` Divide, Repeat

`QuantityInstallmentPeriod` Daily, Weekly, Monthly, Quarterly, Yearly

`NumberOfQuantityInstallments` Integer from 1 to 150, inclusive

When you attempt to set the schedule fields when creating or updating, the API applies cross-field integrity checks. The integrity
requirements are:

**•** If the schedule type is nil, the installment period and number of installments must be nil.

**•** If the schedule type is set to any value, then the installment period and number of installments must be non-nil.

Any create or update that fails these integrity checks is rejected with an error.

These default schedule fields, `CanUseQuantitySchedule`, and `CanUseRevenueSchedule`, are restricted picklist fields and
are available only if the org has the schedules feature enabled.

Usage

Use this object to define the default product information for your org. This object is associated by reference with Pricebook2 objects via
PricebookEntry objects. The same product can be represented in different price books as price book entries. In fact, the same product
can be represented multiple times (as separate PricebookEntry records) in the same price book with different prices or currencies. A
product can only have one price for a given currency within the same price book. To be used in custom price books, all standard prices
must be added as price book entries to the standard price book.

Note: Note: You can’t create lookup fields to Product2 object, which have **Required** check box set to true or the **Don't Allow**
**Deletion** " radio button selected, as the platform would otherwise interpret this and throw an error that you cannot create a
master-detail relationship to the object.

You can query the products that have been configured for your org. For example, you can allow your client application to obtain valid
product IDs for use when configuring PricebookEntry records via the API. Your client application can perform the following tasks on
PricebookEntry objects:


### Standard Objects Product2DataTranslation

**•** Query

**•** Create for the standard price book or custom price books.

**•** Update

**•** Delete

**•** Change the `IsActive` field when creating or updating records

This object is defined only for those orgs that have products enabled as a feature. If the org doesn’t have the products feature, this object
doesn’t appear in the describeGlobal call, and you can't describe or query this object.

If you try to delete a product via the API but there's an opportunity that uses that product, the delete fails. The workaround is to delete
the product in the user interface, which gives you an option to archive the product.

Note: On opportunities and opportunity products, the workflow rules, validation rules, and Apex triggers fire when an update to
a child opportunity product or schedule causes an update to the parent record. This means your custom application logic is
enforced when there are updates to the parent record, ensuring higher data quality and compliance with your organization’s
business policies.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[Product2ChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[Product2Feed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[Product2History](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[Product2OwnerSharingRule (API version 50.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**
Sharing rules are available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### Product2DataTranslation

Represents the translated values of the data stored within a Product2 record’s fields. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.


Standard Objects Product2DataTranslation

**•** To view this object, you must have the “View Setup and Configuration” permission

Fields

**Field** **Details**

```
Description

IsOutOfDate

Language

Name

ParentId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The translated value for the Product2 description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent Product2 record is updated after the last translation was filed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the Product2 record name. This field is required to translate the text
in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the Product2 associated with the data that is being translated.


### Standard Objects ProductAttribute

Usage

Use this object to translate the data stored in a Product2 record into the different languages supported by Salesforce. If data translation
is enabled for custom fields on the Product2 object, additional Product2DataTranslation fields exist for translating the data contained
within those fields.

You can’t use a custom external id field in an upsert call for a Product2DataTranslation object.

### ProductAttribute

Represents the attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeLayout()`, `describeSObjects()`, `getDeleted`, `getUpdated`, `query()`, `retrieve()`,
`undelete`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

ProductId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ProductAttributeSet

**Field** **Details**

**Description**
The ID of the product that the attribute is associated with. This field is unique within your
organization.

```
Sequence

VariantParentId

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product attributes appear in.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the variation parent record associated with the product attribute.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductAttributeEvent (API version 55.0)**
Change events are available for the object.

### ProductAttributeSet

Represents a group of attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeSObjects()`, `query()`, `retrieve()`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.


Standard Objects ProductAttributeSet

Fields

**Field** **Details**

```
Description

DeveloperName

Language

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Text description of the product attribute set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish


### Standard Objects ProductAttributeSetItem

**Field** **Details**

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the product attribute set.

### ProductAttributeSetItem

Represents a set of attributes that can be associated with a product. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeSObjects()`, `query()`, `retrieve()`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.

Fields

**Field** **Details**

```
Field

FieldApiName

```

**Type**
reference

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The field’s API name.

**Type**
string

**Properties**
Filter, Sort

**Description**

A derived field whose values comes from CustomFieldDefinition object.


### Standard Objects ProductAttributeSetProduct

**Field** **Details**

```
IsGroupedBy

ProductAttributeSetId

Sequence

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if product variations are grouped by a specific attribute.

This field is available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the product attribute set.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product attributes appear in.

### ProductAttributeSetProduct

Represents the product associated with a set of attributes. This object is available in API version 50.0 and later.

Supported Calls

`create`, `delete`, `describeLayout()`, `describeSObjects()`, `getDeleted`, `getUpdated`, `query()`, `retrieve()`,
`undelete`, `update`, `upsert`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access products.


### Standard Objects ProductCatalog

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

ProductAttributeSetId

ProductId

### ProductCatalog

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The name of the product associated with the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product associated with the product attribute set.

The container that holds a Product Category hierarchy. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProductCatalog

Special Access Rules

You must have the Industries, Retail, or B2B Commerce license.

Fields

**Field** **Details**

```
CatalogCode

CatalogType

CurrencyIsoCode

Description

```

**Type**
text

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique ID associated with the catalog. Maximum size is 80 alphanumeric characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The category of an entry in the catalog.

Possible values are:

**•** `Sales`

**•** `ServiceProcess` —Service Process

The default value is `Sales` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.


Standard Objects ProductCatalog

**Field** **Details**

```
EffectiveEndDate

EffectiveStartDate

LastReferencedDate

LastViewedDate

Name

NumberOfCategories

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the ProductCatlog record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ProductCategory

**Field** **Details**

**Description**
Number of ProductCategory records assigned to this ProductCatalog record.

```
OwnerId

Status

### ProductCategory

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive

Represents the category that products are organized in.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access product media.


Standard Objects ProductCategory

Fields

**Field** **Details**

```
CatalogId

CurrencyIsoCode

Description

IsNavigational

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the catalog.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductCategory

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
Name

NumberOfProducts

ParentCategoryId

SortOrder

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the category.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of products in a category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product’s parent category.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order that the category is displayed in.


### Standard Objects ProductCategoryProduct

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryChangeEvent (API version 55.0)**
Change events are available for the object.

### ProductCategoryProduct

Holds the relation between product and product category to assign products to a category. This object is available in API version 55.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the Industries, Retail, or B2B Commerce license.

Fields

**Field** **Details**

```
Catalog

CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the ProductCatalog ID of the Category.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** EUR—Euro

**•** USD—U.S. Dollar

The default value is `USD` .


Standard Objects ProductCategoryProduct

**Field** **Details**

```
EffectiveEndDate

EffectiveStartDate

IsPrimaryCategory

Name

ProductCategory

Product

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the ProductCategory is the primaryProductCategory for a given product in a
ProductCatalog. The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the ProductCategoryProduct record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the ProductCategory ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ProductCategoryDataTranslation

**Field** **Details**

**Description**
ID of the product.

```
ProductToCategory

Status

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenated Product ID and Category ID.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryProductEvent (API version 55.0)**
Change events are available for the object.

### ProductCategoryDataTranslation

Represents the translated values for the data stored within a ProductCategory record’s fields. This object is available in API version 46.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission


Standard Objects ProductCategoryDataTranslation

Fields

**Field** **Details**

```
Description

IsOutOfDate

Language

Name

ParentId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The translated value for the Product Category description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ProductCategory record is updated after the last translation was
filed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the Product Category name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the category being translated.


### Standard Objects ProductComponentGroup

Usage

Use this object to translate the data stored in a Product Category record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ProductCategory object, additional ProductCategoryDataTranslation fields exist for
translating the data contained within those fields.

### ProductComponentGroup

Represents the logical grouping of associated products in a bundle and the products’ arrangement policy (group cardinality). This object
is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when Industries EPC or Subscription Management is enabled.

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Describes the group items of a product bundle feature. For example, a group’s contents can
be the associated products that accompany a main product in a bundle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a related record or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductComponentGroup

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user indirectly accessed this record ( `LastReferencedDate` ), but
not viewed it.

```
MaxBundleComponents

MinBundleComponents

Name

OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of associated products allowed in a group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum number of associated products allowed in a group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the product component group. Maximum length is 255 characters (of any type).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique identifier of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects ProductConsumed

**Field** **Details**

```
ParentProductId

Sequence

### ProductConsumed

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier associated with the main product record.

This field is a relationship field.

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.

Represents an item from your inventory that was used to complete a work order or work order line item in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Note: To create products consumed, you need Read permission on product items.

Note: To delete or undelete product consumed for non-serialized products, you need Edit, Create, and Read permission on
product consumed. For product consumed records that lookup to serialized products, you need Modify All Data or Modify All
Records permission on product consumed.


Standard Objects ProductConsumed

Fields

**Field Name** **Details**

```
Description

IsConsumed

IsLocked

IsProduct2Serialized

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes and context about the product consumed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that a product consumed has been processed if the Product2 it refers
to has IsSerialized=true selected. The default is false.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates if a product is a serialized product. The default is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime


Standard Objects ProductConsumed

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last viewed.

```
MayEdit

PricebookEntryId

Product2Id

ProductConsumedNumber

ProductItemId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record can be edited or not.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Price book associated with the product consumed. If the work order and the
product item’s associated product are related to the same price book, the Price
Book Entry auto-populates based on the product item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product associated with the product consumed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) Auto-generated number identifying the product consumed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects ProductConsumed

**Field Name** **Details**

**Description**
Product item associated with the product consumed. Creating a product
consumed record subtracts the quantity consumed from the linked product
item’s quantity.

```
ProductName

QuantityConsumed

QuantityUnitOfMeasure

TotalPrice

UnitPrice

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name for the product consumed.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of products consumed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Units of the consumed item; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price paid for the product items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The price per unit of the product consumed.


### Standard Objects ProductDetectedPriceChange

**Field Name** **Details**

```
WorkOrderId

WorkOrderLineItemId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Work order that the product was consumed for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work order line item that the product was consumed for.

When a product is consumed during the completion of a work order, create a product consumed record to track its consumption. You
can add products consumed to work orders or work order line items. Track product consumption at the line item level if you want to
know which products were used for each line item’s tasks.

The way you use products consumed depends on how closely you want to track the state of your inventory in Salesforce. If you want
to track the entire lifecycle of items in your inventory, including their storage, transfer, and consumption, link your products consumed
records to product items. This approach ensures that your inventory numbers auto-update to reflect the consumption of products from
your inventory. If you want to track product consumption only, however, specify a Price Book Entry on each product consumed record
and leave the Product Item field blank.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductConsumedChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductConsumedFeed**

Feed tracking is available for the object.

**ProductConsumedHistory**

History is available for tracked fields of the object.

### ProductDetectedPriceChange

Represents a detected change in price for a product associated with a partner account. This object is available in API version 63.0 and
later.


Standard Objects ProductDetectedPriceChange

A ProductDetectedPriceChange record is automatically created when the system identifies a change in product pricing that can require
price protection evaluation or further processing.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

EffectiveDate

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the partner account for which the price change was detected.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date when the new price becomes effective for the product.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by the current user. Useful for activity
tracking.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductDetectedPriceChange

**Field** **Details**

**Description**
Date and the timestamp the record was last referenced by a user or system process.

```
Name

OwnerId

ProcessingStatus

ProductId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique name or identifier for the price change record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
User or group that owns this record. This is a polymorphic relationship field.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the current processing stage of the price change.

Possible values are:

**•** `Completed`

**•** `Inactive`

**•** `New`

**•** `Processing` —In Progress

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
References the product for which the price change was detected.


### Standard Objects ProductEntitlementTemplate

**Field** **Details**

This field is a relationship field.

**Relationship Name**
### Product

**Refers To**
Product2

### ProductEntitlementTemplate

Represents predefined terms of customer support (Entitlement) that users can add to products (Product2).

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
EntitlementTemplateId

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the entitlement template. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with the entitlement template. Must be a
valid ID.


### Standard Objects ProductFeaturedProduct

Usage

Use to query and manage entitlement templates.

SEE ALSO:

Entitlement

### ProductFeaturedProduct

Represents the user-defined collection of featured products that are meant to cross-sell or upsell with your product. This object is available
in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
FeatrProdtRelaType

FeaturedProductId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the featured product is related to the product.

Possible values are:

**•** `Complete the Look`

**•** `Featured Products`

**•** `New Arrivals`

**•** `Top Seller`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the featured product that is linked to the product.

This field is a relationship field.


Standard Objects ProductFeaturedProduct

**Field** **Details**

**Relationship Name**
FeaturedProduct

**Refers To**
Product2

```
LastReferencedDate

LastViewedDate

Name

ProductId

Sequence

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the user-defined collection of featured products.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that your company sells.

This field is a relationship field.

**Relationship Name**
Product

**Refers To**
Product2

**Type**
int


### Standard Objects ProductItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the order in which featured products are displayed.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
