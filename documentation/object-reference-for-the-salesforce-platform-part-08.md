**ProductFeaturedProductChangeEvent**

Change events are available for the object.

### ProductItem

Represents the stock of a particular product at a particular location in field service, such as all bolts stored in your main warehouse.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product item was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductItem

**Field Name** **Details**

**Description**
The date when the product item was last viewed.

```
LocationId

OwnerId

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Location associated with the product item. This usually indicates where the
product item is stored.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product item’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Product associated with the product item, which represents the type of product
in your inventory.

This is a relationship field.


Standard Objects ProductItem

**Field Name** **Details**

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductItemNumber

ProductName

QuantityOnHand

QuantityUnitOfMeasure

SerialNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A name for the product item. Try to select a name that indicates what is being
stored where; for example, Batteries in Warehouse A.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity at the location. If you want to add a serial number, this value must
be 1.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the product item; for example, kilograms or liters. Quantity Unit of Measure
picklist values are inherited from the Quantity Unit of Measure field on products.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ProductItemTransaction

**Field Name** **Details**

**Description**
A unique number for identification purposes. If you want to enter a serial number,
the Quantity on Hand must be 1.

Usage

Each product item is associated with a product and a location in Salesforce. If a product is stored at multiple locations, the product will
be tracked in a different product item for each location.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductItemFeed**

Feed tracking is available for the object.

**ProductItemHistory**

History is available for tracked fields of the object.

**ProductItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductItemShare**

Sharing is available for the object.

### ProductItemTransaction

Represents an action taken on a product item in field service. Product item transactions are auto-generated records that help you track
when a product item is replenished, consumed, or adjusted.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `undelete()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Only users with Modify All Data or Modify All Records permissions can delete this object.


Standard Objects ProductItemTransaction

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

LastViewedDate

ProductItemId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the transaction. The description is blank when the transaction
record is created, but can be updated.

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
Create, Filter, Group, Sort

**Description**
The associated product item.

This is a relationship field.

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem


Standard Objects ProductItemTransaction

**Field Name** **Details**

```
ProductItemTransactionNumber

Quantity

RelatedRecordId

TransactionType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item transaction.

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
The quantity of the product item involved in the transaction. If inventory was
consumed, the quantity is negative.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The product consumed or product transfer related to the action. If
the action wasn’t related to consumption or transfer, the related record is blank.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
ProductTransfer, Visit

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The action that the transaction tracks.

**•** Replenished: When a part is stocked at a location. A Replenished transaction
is created when a product item is created.

**•** Consumed: When parts are consumed to complete a work order. A Consumed
transaction is created when a record is added to the Products Consumed
related list on a work order or work order line item.


### Standard Objects ProductMedia

**Field Name** **Details**

**•** Adjusted: When there’s a discrepancy or a change in consumption. An
Adjusted transaction is created when a product item’s Quantity on Hand is
edited, a product consumed is updated or delete, or a product transfer is
deleted.

**•** Transferred: When parts are transferred between locations.

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ProductItemTransactionChangeEvent**

Change events are available for the object.

**ProductItemTransactionFeed**

Feed tracking is available for the object.

**ProductItemTransactionHistory**

History is available for tracked fields of the object.

### ProductMedia

Represents the rich media, including images and attachments, that can be added to products.This object is available in API version 49.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access product media.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar


Standard Objects ProductMedia

**Field** **Details**

```
ElectronicMediaGroupId

ElectronicMediaId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media group.

This field is a relationship field.

**Relationship Name**
ElectronicMediaGroup

**Relationship Type**
Lookup

**Refers To**
ElectronicMediaGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media record.

This field is a polymorphic relationship field.

**Relationship Name**
ElectronicMedia

**Relationship Type**
Lookup

**Refers To**
ManagedContent, ManagedContentInfo

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


Standard Objects ProductMedia

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
Name

ProductId

SortOrder

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the media.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that the media is associated with.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product media is displayed in.

**ProductMediaChangeEvent (API version 57.0)**
Change events are available for the object.

**ProductMediaHistory on page 63**
History is available for tracked fields of the object.

**ProductMediaOwnerSharingRule on page 65**
Sharing rules are available for the object.


### Standard Objects ProgramProduct

**ProductMediaShare on page 67**
Sharing is available for the object.

### ProgramProduct

Represents a junction between Program and Product2. This will hold Product2 values related to a Program. This object is available in
API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
Name

ProductId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ProgramProduct object.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Program.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2


Standard Objects ProgramProduct

**Field** **Details**

```
ProgramId

Status

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Program parent object associated with the record.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup

**Refers To**
Program

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the ProgramProduct object.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Pending For Approval`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ProgramProductChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ProgramProductFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ProgramProductHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ProgramProductOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ProgramProductShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects ProductQuantityRule ProductQuantityRule

Represents the relationship between a quantity rule and a product. This object assigns quantity rules to a product. This object is available
in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ProductQuantityRule object is available only if the B2B Commerce license or Automotive Cloud license is enabled.

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
The ISO code for the currency that’s specified on the buyer’s account. This field is exposed
in orgs that have multicurrency enabled. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product quantity rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product.

This field is a relationship field.


### Standard Objects ProductRelatedComponent

**Field** **Details**

**Relationship Name**
### Product

**Relationship Type**
Lookup

**Refers To**
Product2

```
PurchaseQuantityRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related purchase quantity rule.

This field is a relationship field.

**Relationship Name**
PurchaseQuantityRule

**Relationship Type**
Lookup

**Refers To**
PurchaseQuantityRule

### ProductRelatedComponent

Represents a product that is included in a product bundle, a set, or a product and an add-on. This object is available in API version 57.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, Industries Automotive, Industries EPC, or Subscription
Management is enabled.

In version 57.0, this object is available when B2B Commerce, B2C Commerce, or Industries Automotive is enabled.


Standard Objects ProductRelatedComponent

Fields

**Details**

```
ChildProductId

ChildProductRole

ChildSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated product.

This field is a relationship field. In a bundle relationship, this item is the child product.

**Relationship Name**
ChildProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The position of the associated product in the relationship.

Possible values are:

**•** `AddOnComponent` —The child product is an add-on to another product. Available
in API version 58.0 and later.

**•** `BundleComponent` —The child product is a component in a bundle.

**•** `SetComponent` —The child product is a component in a set.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the associated product’s sales model.

This field is a relationship field.

**Relationship Name**
ChildSellingModel

**Relationship Type**
Lookup


Standard Objects ProductRelatedComponent

**Details**

**Refers To**
ProductSellingModel

```
DoesBundlePriceIncludeChild

IsComponentRequired

IsDefaultComponent

IsQuantityEditable

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the bundle price includes the associated product’s price.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is required for configuring a bundle or set.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is part of the product bundle or set automatically,
or can be added after the bundle’s or set’s creation.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether you can edit the component’s quantity in the bundle or set after the
bundle’s or set’s creation.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductRelatedComponent

**Details**

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

MaxQuantity

MinQuantity

Name

ParentProductId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user accessed this record or list view ( `LastReferencedDate` )
without viewing it.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed maximum quantity.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed minimum quantity.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the associated product.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the main product around which the bundle or set is built.

This field is a relationship field.


Standard Objects ProductRelatedComponent

**Details**

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

```
ParentProductRole

ParentSellingModelId

ProductComponentGroupId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main product in the relationship.

Possible values are:

**•** `AddOn` —The main product is the add-on parent. Available in API version 58.0 and later.

**•** `Bundle` —The main product is the bundle parent.

**•** `Set`  - The main product is the set parent.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the main product’s sales model.

This field is a relationship field.

**Relationship Name**
ParentSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the group of a product bundle or set. This group contains the
associated products that can be included in the main product’s bundle or set.

This field is a relationship field.


Standard Objects ProductRelatedComponent

**Details**

**Relationship Name**
ProductComponentGroup

**Relationship Type**
Lookup

**Refers To**
ProductComponentGroup

```
ProductRelationshipTypeId

Quantity

QuantityScaleMethod

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier of the record that describes the relationship between the main and
associated products.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit count of the associated product.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The scaling method is used to calculate the associated product’s quantity based on changes
made to the main product’s quantity in a transaction.

Possible values are:

**•** `Constant`  - The associated product’s quantity remains the same in relation to the
main product’s quantity. For example, the main product has a quantity of one and the
associated component has a quantity of one. If you increase the quantity of the main
product to two, the associated component’s quantity remains at one.


### Standard Objects ProductRelationshipType

**Details**

**•** `Proportional`                   - The associated product’s quantity increases or decreases based
on the main product’s quantity. For example, the main component has a quantity of one
and the associated product has a quantity of two. If you increase the quantity of the main
product to two, the associated product’s quantity increases to four.

The default value is `Proportional` .

```
Sequence

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.

### ProductRelationshipType

Defines the relationship between two sales transaction items. For example, defines a relationship between a bundle and a bundle
component. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, or Subscription Management is enabled.

In version 57.0, this object is available when B2B Commerce or B2C Commerce is enabled.

Fields

**Field** **Details**

```
AssociatedProductRoleCat

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The position category that the associated product plays in the relationship.

Possible values are:

**•** `AddOnComponent` —The associated product is an add-on.


Standard Objects ProductRelationshipType

**Field** **Details**

**•** `BundleComponent`                   - The associated product is part of a bundle.

**•** `SetComponent`                   - The associated product is part of a set.

```
LastReferencedDate

LastViewedDate

MainProductRoleCat

Name

```

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
the user might have only accessed this record or list view ( `LastReferencedDate` ), but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The position category that the main product plays in the relationship.

Possible values are:

**•** `AddOn` —The parent of the add-on.

**•** `Bundle` —The bundle parent.

**•** `Set` —The set parent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the relationship between two product items.


### Standard Objects ProductRequest ProductRequest

Represents an order for a part or parts in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Authenticated external users can create and update ProductRequest objects.

Fields

**Field Name** **Details**

```
AccountId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the product request.

This is a relationship field.

**Relationship Name**
Case


Standard Objects ProductRequest

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Case

```
CurrencyIsoCode

Description

DestinationLocationId

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
`Currency ISO Code` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text field for details not recorded in the provided fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProductRequest

**Field Name** **Details**

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

```
LastViewedDate

NeedByDate

OwnerId

ProductRequestNumber

ShipToAddress

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shipment.

This is a polymorphic relationship field.

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
An auto-assigned number that identifies the shipment.

**Type**
address


Standard Objects ProductRequest

**Field Name** **Details**

**Properties**
Filter, Nillable

**Description**
The address that the product is to be delivered to.

```
ShipToCity

ShipToCountry

ShipToCountryCode

ShipToGeocodeAccuracy

ShipToLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city that the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country that the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase country code conforming to the ISO 3166-1 alpha-2
standard.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The accuracy of the geocode for the shipping address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the product is to be delivered to.


Standard Objects ProductRequest

**Field Name** **Details**

```
ShipToLongitude

ShipToPostalCode

ShipToState

ShipToStateCode

ShipToStreet

ShipmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the state where the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase state code conforming to the ISO 3166-1 alpha-2 standard.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values by default:


Standard Objects ProductRequest

**Field Name** **Details**

**•** None

**•** Rush

**•** Overnight

**•** Next Business Day

**•** Pick Up

```
SourceLocationId

Status

WorkOrderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location the product is shipped from.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder


### Standard Objects ProductRequestLineItem

**Field Name** **Details**

```
WorkOrderLineItemId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order line item that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductRequestChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestFeed**

Feed tracking is available for the object.

**ProductRequestHistory**

History is available for tracked fields of the object.

**ProductRequestOwnerSharingRule**

Sharing rules are available for the object.

**ProductRequestShare**

Sharing is available for the object.

### ProductRequestLineItem

Represents a request for a part in field service. Product request line items are components of product requests.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProductRequestLineItem

Special Access Rules

Field Service must be enabled. You can't use product request line item as a master in an master detail relationship (through a custom
field) with a custom object with data.

Fields

**Field Name** **Details**

```
AccountId

CareProgramEnrolleeId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request line item.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the care program enrollee associated with the product request line
item. This field is available from API version 49.0 and later.

This is a relationship field.

**Relationship Name**
CareProgramEnrollee

**Relationship Type**
Lookup

**Refers To**
CareProgramEnrollee

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The case associated with the product request line item.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
Description

DestinationLocationId

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Details not recorded in the provided fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
NeedByDate

ParentId

Product2Id

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The product request that the line item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The product associated with the product request line item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


Standard Objects ProductRequestLineItem

**Field Name** **Details**

```
ProductRequestLineItemNumber

QuantityRequested

QuantityUnitOfMeasure

ShipToAddress

ShipToCity

ShipToCountry

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) An auto-assigned number that identifies the product request line
item.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The amount requested.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the requested product; for example, grams, liters, or units. The picklist
values can be customized.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The country of the address where the product is needed.

```
ShipToGeocodeAccuracy

ShipToLatitude

ShipToLongitude

ShipToPostalCode

ShipToState

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the product is needed. See
Compound Field Considerations and Limitations for details on geolocation
compound fields. This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. See Compound Field Considerations and Limitations for
details on geolocation compound fields. This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields. This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The state of the address where the product is needed.

```
ShipToStreet

ShipmentType

SourceLocationId

Status

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the product is needed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values, which can be
customized:

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is at the time of the request.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ProductRequestLineItem

**Field Name** **Details**

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** `Draft`

**•** `Submitted`

**•** `Received`

```
WorkOrderId

WorkOrderLineItemId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order for which the product is needed.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order line item for which the product is needed.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ProductRequired

**ProductRequestLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestLineItemFeed**

Feed tracking is available for the object.

**ProductRequestLineItemHistory**

History is available for tracked fields of the object.

### ProductRequired

Represents a product that is needed to complete a work order or work order line item in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ProductRequired

**Field Name** **Details**

**Description**
The work order or work order line item that the product is required for.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Visit, WorkOrder, WorkOrderLineItem, WorkType

```
ParentRecordType

Product2Id

ProductName

ProductRequiredNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the parent record is a work order or a work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The required product.

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
The name of the product required.

**Type**
string


Standard Objects ProductRequired

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the product required.

```
QuantityRequired

QuantityUnitOfMeasure

```

Usage

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity required of the product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the required product; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

Required products can be added to work types, work orders, and work order line items to ensure that the assigned service resource
arrives with the right equipment.

Adding required products to work types saves you time and keeps your business processes consistent. Work orders and work order line
items inherit their work type’s required products. For example, if all light bulb replacement jobs require a ladder and a light bulb, add
the ladder and light bulb as required products to your Light Bulb Replacement work type. When it’s time to create a work order for a
customer’s light bulb replacement, applying that work type to the work order adds the required products.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductRequiredChangeEvent**

Change events are available for the object.

**ProductRequiredFeed**

Feed tracking is available for the object.

**ProductRequiredHistory**

History is available for tracked fields of the object.


### Standard Objects ProductSellingModel ProductSellingModel

Defines one method by which a product can be sold; for example, as a one-time sale, an evergreen subscription, or a term-defined
subscription. If the product is sold on subscription, this object defines the subscription’s term. A product can have multiple product
selling models. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Revenue Cloud and Subscription Management. This object is available for Commerce when the Subscriptions
(Beta) permission is enabled.

Fields

**Field** **Details**

```
Name

PricingTerm

PricingTermUnit

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name given to the product selling model.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the duration of the pricing term for a given selling model. Used with
`PricingTermUnit` . For example, if this field’s value is 1 and the `PricingTermUnit`
is `Months`, the subscription is priced monthly.

If the selling model is one-time, this field must be null.

Possible value is:

**•** `1`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProductSellingModel

**Field** **Details**

**Description**
The unit of time used to define the pricing term. Used with `PricingTerm` to define the
length of the pricing term. For example, if this field is `Months` and `PricingTerm` is 1,
the subscription is priced monthly. If the selling model is one-time, this field must be null.

Possible values are:

**•** `Annual` —UI label is `Years`

**•** `Months`

```
SellingModelType

Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the product is sold as a one-time sale, an evergreen subscription, or a
subscription with a defined term.

Possible values are:

**•** `Evergreen` —A subscription without an end date. An evergreen subscription continues
until the customer affirmatively cancels it.

**•** `OneTime` —A product that isn’t sold as a subscription.

**•** `TermDefined` —A subscription with a defined end date. The subscription continues
for a specified time period. When the term ends, the subscription ends.

The default value is `OneTime` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the product selling model.

Possible values are:

**•** `Active` —An active product selling model can’t be deleted, and only the `Name` and
`Status` fields can be modified. An active product selling model can’t be changed back
to draft.

**•** `Draft` —A draft product selling model can be modified and deleted.

**•** `Inactive` —An inactive product selling model can’t be deleted, and only the `Name`
and `Status` fields can be modified. An inactive product selling model can’t be changed
back to draft.

The default value is `Draft` .


### Standard Objects ProductSellingModelOption ProductSellingModelOption

A junction object between Product Selling Model and Product2. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. Some fields require Industries EPC to
be enabled.

Fields

**Field** **Details**

```
Description

DisplayName

Increment

IsDefault

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the product selling model option.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model option to display to customers.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of pricing term units that can be used to increase a subscription term.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ProductSellingModelOption

**Field** **Details**

**Description**
Indcates the default product selling model for a product. Setting a default is optional. A
product can only have one default product selling model.

The default value is `false` . This field requires Industries EPC.

```
LastReferencedDate

LastViewedDate

Maximum

Minimum

Name

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
the user might have only accessed this record or list view but not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of pricing term units for a subscription term.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum number of pricing term units for a subscription term.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model.


Standard Objects ProductSellingModelOption

**Field** **Details**

```
Product2Id

ProductSellingModelId

ProrationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Product2 record associated with this ProductSellingModelOption record.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProductSellingModel record associated with this ProductSellingModelOption
record.

This is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the ProrationPolicy record associated with this ProductSellingModelOption record.

This is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup


### Standard Objects ProductServiceCampaign

**Field** **Details**

**Refers To**
ProrationPolicy

### ProductServiceCampaign

Represents a set of activities to be performed on a product service campaign asset, such as a product recall for safety issues or product
defects. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

EndDate

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the product service campaign.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the product service campaign ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. The UI label is Last Modified Date.


Standard Objects ProductServiceCampaign

**Field** **Details**

```
LastViewedDate

OwnerId

Priority

Product2Id

ProductServiceCampaignName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product service campaign’s owner. By default, the product service campaign owner is
the user who created the product service campaign record. The UI label is Product Service
Campaign Owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the product service campaign.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Product2 associated with this campaign. The UI label is Product.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the product service campaign.


Standard Objects ProductServiceCampaign

**Field** **Details**

```
StartDate

Status

StatusCategory

Type

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date on which the product service campaign starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `New` —Product service campaign created, but there hasn’t yet been any activity.

**•** `In Progress` —Product service campaign has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work couldn’t be completed.

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a _`Waiting for Response`_ value, add it the _`On Hold`_ category.
To learn which processes reference `StatusCategory` [, see How are Status Categories](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ProductServiceCampaignItem

**Field** **Details**

**Description**
The type of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `Modification` —The asset requires an on-site alteration.

**•** `Recall` —The asset must be returned to the manufacturer for modification or upgrade.

**•** `Service` —The asset needs to be serviced.

**•** `Upgrade` —The asset needs updating.

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the product service campaign. A customer uses this field as
a guide when setting work type for work orders for the product service campaign.
`Duration`, `Duration Type`, and required skills.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignFeed**

Feed tracking is available for the object.

**ProductServiceCampaignHistory**

History is available for tracked fields of the object.

**ProductServiceCampaignOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignShare**

Sharing is available for the object.

### ProductServiceCampaignItem

Represents a product service campaign's asset. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ProductServiceCampaignItem

Fields

**Field** **Details**

```
AssetId

LastReferencedDate

LastViewedDate

Product2Id

ProductServiceCampaignId

ProductServiceCampaignItemNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the product service campaign. Must be present if `Product2Id`
is not present.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. Its UI label is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Product2 associated with this campaign. The UI label is Product. Must be present
if `AssetID` is not present.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The item’s parent product service campaign record.

**Type**
string


Standard Objects ProductServiceCampaignItem

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the product service campaign item.

```
Status

StatusCategory

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign item. The picklist includes the following values,
which can be customized:

**•** `New` —Product service campaign item created, but there hasn’t yet been any activity.

**•** `In Progress` —Product service campaign item has begun.

**•** `On Hold` —Product service campaign item is paused.

**•** `Completed` —Product service campaign item is complete.

**•** `Cannot Complete` —Product service campaign item couldn’t be completed.

**•** `Closed` —All product service campaign item and associated activity is complete.

**•** `Canceled` —Product service campaign item is canceled, typically before any work
began.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a _`Waiting for Response`_ value, add it to the _`On Hold`_
category. To learn which processes reference `StatusCategory` [, see How are Status](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignItemFeed**

Feed tracking is available for the object.

**ProductServiceCampaignItemHistory**

History is available for tracked fields of the object.


### Standard Objects ProductServiceCampaignItemStatus

**ProductServiceCampaignItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignItemShare**

Sharing is available for the object.

### ProductServiceCampaignItemStatus

Represents a status for a product service campaign item in field service. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

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
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on product service campaign items when
`true` . Only one status value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value in the UI.


### Standard Objects ProductServiceCampaignStatus

**Field** **Details**

```
SortOrder

StatusCode

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the dropdown list in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has seven values
that are identical to the default Status values.

The Status field on product service campaign items comes with the following values:

**•** New—Product service campaign item created, but there hasn’t been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work couldn’t be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The ProductServiceCampaignItemStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled
By Supplier—creates a product service campaign item status record, and vice versa.

Note: Product service campaign items also come with a Status Category field whose values are identical to the default status
values. If you create custom status values, you must indicate which category it belongs to. For example, if you create a _`Customer`_

_`Absent`_ value, add it to the _`Cannot Complete`_ [category. To learn which processes reference StatusCategory, see How are](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ProductServiceCampaignStatus

Represents a status for a product service campaign in field service. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects ProductServiceCampaignStatus

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ApiName

IsDefault

MasterLabel

SortOrder

StatusCode

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on product service campaigns when
`true` . Only one status value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the dropdown list in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has seven values
that are identical to the default Status values.


### Standard Objects ProductTransfer

Usage

The Status field on product service campaigns comes with the following values:

**•** New—Product service campaign created, but there hasn’t been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work couldn’t be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The ProductServiceCampaignStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled
By Supplier—creates a product service campaign status record, and vice versa.

Note: Product service campaigns also come with a Status Category field whose values are identical to the default status values.
If you create custom status values, you must indicate which category it belongs to. For example, if you create a _`Customer`_

_`Absent`_ value, add it to the _`Cannot Complete`_ [category. To learn which processes reference StatusCategory, see How are](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ProductTransfer

Represents the transfer of inventory between locations in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Description

DestinationLocationId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields.

**Type**
reference


Standard Objects ProductTransfer

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The place the product is to be delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

```
ExpectedPickupDate

IsReceived

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be picked up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Checkbox identifying that the product was received.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.


Standard Objects ProductTransfer

**Field Name** **Details**

```
OwnerId

Product2Id

Product2TransferRecordMode

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the product transfer.

This is a polymorphic relationship field.

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
Lookup field for the product associated with the product transfer.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If serialized, indicates when the serial number is recorded. It is visible on the
product transfer as a read-only field depending on the field-level security. Possible
values are:

**•** `SendAndReceive` —The serial number is recorded when sending or
receiving.

**•** `ReceiveOnly` —The serial number is recorded when receiving only.

**Relationship Name**
Product2.TransferRecordMode


Standard Objects ProductTransfer

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2.TransferRecordMode

```
ProductRequestId

ProductRequestLineItemId

ProductTransferNumber

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the product request associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product request line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the product transfer.


Standard Objects ProductTransfer

**Field Name** **Details**

```
QuantityReceived

QuantitySent

QuantityUnitOfMeasure

ReceivedById

ReturnOrderId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of product received at the destination location.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of product sent from the source location.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The units of the product, for example grams, liters, or units.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the contact who received the product at the destination location.

This is a polymorphic relationship field.

**Relationship Name**
ReceivedBy

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the product transfer.


Standard Objects ProductTransfer

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

```
ReturnOrderLineItemId

ShipmentExpectedDeliveryDate

ShipmentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the shipment related to the product transfer.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup


Standard Objects ProductTransfer

**Field Name** **Details**

**Refers To**
Shipment

```
ShipmentStatus

ShipmentTrackingNumber

ShipmentTrackingUrl

SourceLocationId

SourceProductItemId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the source location related to the product transfer.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference


### Standard Objects ProductWarrantyTerm

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product item related to the product transfer.

**Relationship Name**
SourceProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductTransferChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductTransferFeed**

Feed tracking is available for the object.

**ProductTransferHistory**

History is available for tracked fields of the object.

**ProductTransferOwnerSharingRule**

Sharing rules are available for the object.

**ProductTransferShare**

Sharing is available for the object.

### ProductWarrantyTerm

Defines the relationship between a product or product family and warranty term. This object is available in API version 50.0 and later.


Standard Objects ProductWarrantyTerm

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CoveredProductFamily

CoveredProductId

LastReferencedDate

LastViewedDate

ProductWarrantyTermNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product family that the warranty term applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product that the warranty term applies to.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier for this product warranty term.


### Standard Objects Profile

**Field** **Details**

```
WarrantyTermId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the warranty term.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductWarrantyTermChangeEvent (API version 62.0)**
Change events are available for the object.

### Profile

Represents a profile, which defines a set of permissions to perform different operations. Operations can include creating a custom profile
or querying, adding, updating, or deleting information.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, Customer Portal and Partner Portal users _can’t_ access this object.

To view the following settings, assignments, and permissions for standard and custom objects in a specified profile, the View Setup and
Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Starting in Winter ’21, only users with correct permissions can view profile names other than their own if the Profile Filtering setting is
enabled.


Standard Objects Profile

Important: Profile names are also exposed when users with permissions to perform the following tasks take these actions:

**•** Create a tab or record type with a wizard step that includes the assignment of tabs and record types to profiles.

**•** Configure a login flow where viewing profile lists is required to make flow associations.

**•** Set up delegated admins where looking up profiles is needed to identify assignable profiles.

**•** Administer an org as a delegated customer admin.

**•** Administer an org as a delegated admin to view and assign profiles of the delegated group.

Fields

**Field** **Details**

```
Description

IsSsoEnabled

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the profile.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to this profile can delegate username and password authentication
to a corporate database instead of the user database.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this profile. Available
in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this profile. Available in API version 29.0
and later.


Standard Objects Profile

**Field** **Details**

```
Name

Permissions PermissionName

UserLicenseId

UserType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true`, users assigned to this profile have the named
permission. The number of fields varies depending on the permissions for the org and license
type.

Tip: To get a list of available permissions in SOAP API, use `describeSObjects()` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the UserLicense associated with this profile.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and later,
valid values include:


Standard Objects Profile

**Field** **Details**

**•** Standard: user license. This user type also includes Salesforce Platform and Salesforce
Platform One user licenses. Label is **Standard** .

**•** PowerPartner: User whose access is limited because they’re a partner and typically access
the application through a partner portal or Experience Cloud site. Label is **Partner** .

**•** CspLitePortal: user whose access is limited because they’re an org's customer and access
the application through a Customer Portal or Experience Cloud site. Label is **High Volume**
**Portal** .

**•** CustomerSuccess: user whose access is limited because they’re an org's customer and
access the application through a Customer Portal. Label is **Customer Portal User** .

**•** PowerCustomerSuccess: user whose access is limited because they’re an org's customer
and access the application through a Customer Portal. Label is **Customer Portal Manager** .

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is **Chatter Free** .

**•** Guest: user whose access is limited because they’re an unauthenticated user without login
credentials. Label is **Guest** .

`UserType` replaces `LicenseType`, which is unavailable as of API version 10.0. In API
versions 8.0 and 9.0 `LicenseType` is still available with the following valid values:

**•** AUL: Lightning Platform user license. Label is **Apex Platform** .

**•** AUL1: Lightning Platform user license with only one user. Label is **Apex Platform One** .

**•** Salesforce: Salesforce user license. Label is **Salesforce** .

**•** PackageManager: user who can create and work with managed packages for AppExchange.
Label is **Package Manager** .

**•** PRM: user whose access is limited because they’re a partner and typically accesses the
application through a partner portal. Label is **Partner** .

**•** CustomerUser: user whose access is limited because they’re an org's customer and accesses
the application through a Customer Portal. Label is **Customer Portal User** .

**•** CustomerManager: user whose access is limited because they’re an org's customer and
accesses the application through a Customer Portal. Label is **Customer Portal Manager** .

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

In API version 53.0 and later, you can’t set the value of `UserType` using Apex.

Usage

Use the Profile object to create custom profiles that start without any permissions enabled except for required permissions for the profile’s
user license. While you can use the Profile Metadata type to deploy profiles, we recommend that you use the Profile SOAP API object
because it allows you to create empty profiles.

You can also query the set of currently configured user profiles in your org. Your client application can use Profile objects to obtain valid
profile IDs for use when querying or modifying users through the API.


### Standard Objects ProfileSkill

In the user interface, profiles can be used to assign user licenses from specific pools (Lightning Platform user license or Salesforce user
license, for example). When users are reassigned to profiles with different license types, the number of available licenses in the old license
type pool increases, one per user assignment updated. Also, the number of available licenses decreases by the same amount in the new
license type pool.

SEE ALSO:

Overview of Salesforce Objects and Fields

PermissionSet

### ProfileSkill

Represents a profile skill, which describes a user’s professional knowledge. This is a global record for the organization, and users are
associated through the ProfileSkillUser object.

Note: For information about Live Agent skills, see the Skill topic.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

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
Description of the profile skill.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the current user last viewed a record related to
this profile skill. Available in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ProfileSkill

**Field Name** **Details**

**Description**
The timestamp indicating when the current user last viewed this profile skill.
Available in API version 29.0 and later.

```
Name

OwnerId

UserCount

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile skill.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the profile skill.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users with the profile skill.

Use the ProfileSkill object to look up the attributes of a skill that can be assigned to a user. This is a global object and is not owned by
any specific user.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects ProfileSkillEndorsement

**ProfileSkillFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillHistory**

History is available for tracked fields of the object.

**ProfileSkillOwnerSharingRule**

Sharing rules are available for the object.

**ProfileSkillShare**

Sharing is available for the object.

### ProfileSkillEndorsement

Represents a detail relationship of ProfileSkillUser. An endorsement of a profile skill shows approval and support of another user’s publicly
declared skill.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

ProfileSkillUserId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the profile skill being endorsed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkillUser record that is being endorsed.

This is a relationship field.

**Relationship Name**
ProfileSkillUser

**Relationship Type**
Lookup

**Refers To**
ProfileSkillUser


### Standard Objects ProfileSkillShare

**Field Name** **Details**

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the person giving the endorsement.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Use the ProfileSkillEndorsement object to query about a single endorsement given to a user about a specific skill. Users can’t endorse
themselves, they can only be endorsed by others unless they are administrators with the “Modify All Data” permission.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillEndorsementChangeEvent (API version 62.0)**
Change events are available for the object.

**ProfileSkillEndorsementFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillEndorsementHistory**

History is available for tracked fields of the object.

### ProfileSkillShare

Represents a sharing entry on a ProfileSkill.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


Standard Objects ProfileSkillShare

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field Name** **Details**

```
AccessLevel

ParentId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the ProfileSkill. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for ProfileSkill objects.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ProfileSkill

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects ProfileSkillUser

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values may include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the ProfileSkill with them.

**•** `Owner` —The User is the owner of the ProfileSkill or is in a role above the
ProfileSkill owner in the role hierarchy.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the ProfileSkill.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object is read only. It is visible because of constraints to the ProfileSkill object, but it is ignored and does not control which users
and groups can view and edit ProfileSkill records owned by other users.

### ProfileSkillUser

Represents a detail relationship of User. The object connects profile skills with users.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ProfileSkillUser

Fields

**Field Name** **Details**

```
EndorsementCount

Name

ProfileSkillId

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of endorsements.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the skill user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkill.

This is a relationship field.

**Relationship Name**
ProfileSkill

**Relationship Type**
Lookup

**Refers To**
ProfileSkill

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user. This field can’t be changed once it is created.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects ProgramRebateType

**Field Name** **Details**

**Refers To**
User

Usage

Use this object to assign specific skills to specific users. ProfileSkillUser appears on the Overview tab on the Chatter profile page. Users
can only create a skill mapping for themselves, they can’t create skill mappings for others unless they are administrators with the “Modify
All Data” permission. Additionally, users can only edit this object if they are the context user and are not editing the `UserId` field.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillUserFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillUserHistory**

History is available for tracked fields of the object.

### ProgramRebateType

Represents a rebate structure associated with a Rebate Program. This object is available in API version 63.0 and later.

A ProgramRebateType record is created to define how benefits are calculated—such as accruals, payouts, or both—based on specified
measure fields and logic.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccrualRate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The rate of accrual based on the value selected in the Measure Type field. For example, when
the measure type is percent and you enter 10, the accrual rate is 10%.


Standard Objects ProgramRebateType

**Field** **Details**

```
AggregateObjectName

BenefitQualifierField

CalcObjectId

CalculationBasis

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The object that stores the aggregation results.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The field on the aggregation object used to define thresholds for qualifying benefits (minimum
or maximum).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to a calculation definition from the Data Processing Engine.

This field is a relationship field.

**Relationship Name**
CalcObject

**Refers To**
BatchCalcJobDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the method used to calculate the rebate amount.

Possible values are:

**•** `Accrual`

**•** `Payout`

**•** `PayoutAndAccrual` —Payout and Accrual

The default value is `Payout` .


Standard Objects ProgramRebateType

**Field** **Details**

```
CalculationMethod

CalculationType

ExecutionProcedureId

FilterAction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines how tiered rebate benefits are calculated.

Possible values are:

**•** `Retrospective`

**•** `Stepped`

The default value is `Retrospective` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of rebate calculation logic to use.

Possible values are:

**•** `AggregateBased` —Aggregate Based

**•** `Custom`

**•** `GrowthBased` —Growth Based

**•** `PerTransaction` —Per Transaction

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links to business rules that define custom execution logic.

This field is a relationship field.

**Relationship Name**
ExecutionProcedure

**Refers To**
ExpressionSet

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProgramRebateType

**Field** **Details**

**Description**
Logical operator to apply between filter conditions.

Possible values are:

**•** `AllConditionsMet` —All Conditions Are Met (AND)

**•** `AnyConditionMet` —Any Condition Is Met (OR)

**•** `CustomLogic` —Custom Condition Logic

**•** `NoConditionsMet` —No Conditions Are Met

```
FilterCriteria

FilterLogic

IsIntegratable

LastReferencedDate

```

**Type**
textarea

**Properties**
Nillable

**Description**

Holds the filter conditions in textual format. Used to define eligibility criteria for rebate
qualification.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Logical formula used to combine filter conditions, typically using field references and logical
operators.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When selected, allows this rebate type to be applied on transactional records such as orders
or opportunities.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last referenced by the user. Useful for user
activity tracking.


Standard Objects ProgramRebateType

**Field** **Details**

```
LastViewedDate

MeasureField

Name

OwnerId

ProductFilterType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last opened or viewed. Tracks user interaction
history.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The aggregation object field used with measure type and benefit value to calculate the
rebate amount. This is required for the Amount per Unit and Percentage of Revenue measure
types.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique name that identifies the rebate type configuration. Used as a reference label across
related components.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Identifies the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ProgramRebateType

**Field** **Details**

**Description**
Specifies whether the rebate applies to included or excluded products.

Possible values are:

**•** `ExcludeProducts` —Exclude Products

**•** `IncludeProducts` —Include Products

```
RebateMeasureType

RebateProgramId

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the method to measure benefit payout.

Possible values are:

**•** `AmountperUnit` —Amount per Unit

**•** `Custom`

**•** `FixedAmount` —Fixed Amount

**•** `PercentageOfRevenue` —Percentage of Revenue

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Links this rebate type to its parent rebate program.

This field is a relationship field.

**Relationship Name**
RebateProgram

**Relationship Type**
Master-detail

**Refers To**
RebateProgram (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies whether the rebate type is currently active.

Possible values are:

**•** `Active`


### Standard Objects Promotion

**Field** **Details**

**•** `Inactive`

The default value is `Inactive` .

```
UnitOfMeasureId

ValidityDuration

ValidityDurationType

### Promotion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the unit of measure associated with the rebate type.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Duration for which the inventory is eligible for price protection.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to measure ValidityDuration.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Years`

The default value is `Years` .

Represents a promotion for B2B or D2C stores. This object is available in API version 52.0 and later.


Standard Objects Promotion

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Some of the fields on the Promotion object are available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AreQualItemsExclFromDiscounts

CurrencyIsoCode

Description

DiscountOrder

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Exclude qualifying items from discount. You can use this field to create buy-one-get-one
promotions. The default value is false. This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to apply discounts first to the least expensive products or to the most
expensive products.

Possible values are:


Standard Objects Promotion

**Field** **Details**

**•** `LeastExpensive`

**•** `MostExpensive`

The default value is `MostExpensive` .

This field is available in API version 56.0 and later.

```
DiscountRestriction

DisplayName

EndDateTime

ExclusivityType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to restrict the products that can be discounted based on the least expensive
qualifying product.

Possible values are:

**•** `LeastExpensive`

**•** `None`

The default value is `None` .

This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Display name of the promotion.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion ends.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether a promotion can be combined with other promotions.

Possible values are:

**•** `No`  - Can be combined with other promotions.


Standard Objects Promotion

**Field** **Details**

**•** `Class`                   - Can’t be combined with a promotion of the same class (product, order, or
shipment), but allows for promotions of separate classes to be combined. For example,
an order discount on top of a product discount.

**•** `Global`                   - Only promotion that can be applied to the order, regardless of class.

The default value is `Class` .

This field is available in API version 58.0 and later.

```
IsActive

IsApproachingDiscountApplicable

IsAutomatic

IsCommercePromotion

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the promotion is active (true) or inactive (false).

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the promotion shows an approaching discount message. Set an approaching
discount threshold value on the PromotionQualifier object. This field is available in API version
64.0 and later.

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the promotion is automatic or manual. If the promotion is automatic,
it automatically applies to eligible carts with no buyer action required. if the promotion is
manual, the buyer applies a coupon to redeem the promotion.

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the promotion is a B2B Commerce promotion (true) or not (false).


Standard Objects Promotion

**Field** **Details**

The default value is false.

```
IsTiered

LastReferencedDate

LastViewedDate

MaximumUsageCount

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the promotion uses promotion tiers (true) or not (false). This value can’t
be changed.

The default value is false.

A tiered promotion can have up to 10 associated tiers.

This field is available in API version 57.0 and later.

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
possible that this record was referenced and not directly accessed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of times the promotion can be applied to a cart. If left blank, the default
value is 1. This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects Promotion

**Field** **Details**

**Description**
Name of the promotion.

```
Objective

OwnerId

PriorityNumber

QualifierCriteria

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
More information, if any, about the purpose of the promotion.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the promotion.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority for the promotion. The priority determines which promotions apply first. The lower
the number, the higher the priority.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple qualifiers, this field determines whether all qualifiers must be
met or whether any must be met for the promotion to apply.

Possible values are:

**•** `All`


Standard Objects Promotion

**Field** **Details**

**•** `Any`

The default value is 'All'.

This field is available in API version 53.0 and later.

```
StartDateTime

TargetCriteria

TermsAndConditions

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion begins.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple targets, indicates whether a cart must meet the criteria for any
target or the criteria for all targets.

Possible values are:

**•** `All`

**•** `Any`

This field is available in API version 56.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Terms and conditions the buyer accepts before applying the promotion.

This field is available in API version 53.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionFeed on page 55**
Feed tracking is available for the object.

**PromotionHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects PromotionLineItemRule

**PromotionShare on page 67**
Sharing is available for the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionLineItemRule

Lists compound conditions about a promotion. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssociatedReferenceId

AssociatedType

```

**Type**
Reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated reference.

**Relationship Name**
AssociatedReference

**Relationship Type**
Lookup

**Refers To**
PromotionQualifier, PromotionTarget

**Type**
Picklist


Standard Objects PromotionLineItemRule

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of object the rule is associated with.

Possible values are:

**•** `PromotionQualifier`

**•** `PromotionTarget`

```
Name

OperatorType

OwnerId

```

**Type**
String

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion rule.

**Type**
Picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Operator type for promotion line item rule.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_OR_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_OR_EQUAL_TO`

**•** `NOT_EQUAL_TO`

The default value is `EQUAL_TO` .

**Type**
Reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects PromotionMarketSegment

**Field** **Details**

**Refers To**
Group, User

```
Type

TypeReferenceId

TypeValue

```

**Type**
Picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type on which the rule is being applied.

Possible values are:

**•** `Attribute`

**•** `Price`

**•** `Product`

**•** `ProductCategory`

**Type**
Reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the type.

**Relationship Name**
TypeReference

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Value of the type selected.

### PromotionMarketSegment

Represents a market segment within B2B Commerce that promotions can be assigned to. This object is available in API version 52.0 and
later.


Standard Objects PromotionMarketSegment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionMarketSegment object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.


Standard Objects PromotionMarketSegment

**Field** **Details**

```
PromotionId

PromotionSegmentId

```

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to associate with your promotion segment.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion segment that you want to associate with.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment


### Standard Objects PromotionQualifier PromotionQualifier

Represents the product, product category, or order that you want to target with your promotion qualifier in a B2B or D2C store. This
object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionQualifier object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ApproachingDiscountThreshold

CurrencyIsoCode

ExternalQualifier

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount that a customer has to reach before seeing an approaching discount message.

For example, if a promotion qualifier minimum is set at $150 and this field is set at $50, then
a customer receives a banner notification that they're approaching the discount when they
have at least $50 in their cart. This field is available in API version 64.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A qualifying product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.


Standard Objects PromotionQualifier

**Field** **Details**

Note: This field is available through the API only.

```
LastReferencedDate

LastViewedDate

MinimumAmount

MinimumQuantity

Name

PromotionId

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum dollar amount that a buyer must purchase to qualify for the promotion.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum quantity that a buyer must purchase to qualify for the promotion.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion qualifier.

**Type**
reference


Standard Objects PromotionQualifier

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to associate with your promotion qualifier.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

```
PromotionTierId

QualifierId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion tier associated with the qualifier. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the qualifier.

This is a polymorphic relationship field.

**Relationship Name**
Qualifier

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory


Standard Objects PromotionQualifier

**Field** **Details**

```
QualifierOperator

QualifierProductCategoryName

QualifierProductName

QualifierProductSku

QualifierRuleCriteriaType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** `EQUAL_TO`

**•** `NONE`

**•** `NOT_EQUAL_TO`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the qualifier. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the qualifier. This field is available in API version 55.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the qualifier. This field is available in API
version 55.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier rule criteria.

Possible values are:


### Standard Objects PromotionSegment

**Field** **Details**

**•** `All`

**•** `Any`

```
QualifierType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier that you want to add to the promotion. `Product` applies the qualifier
to a single product, `ProductCategory` to a predetermined group of products, and
`TransactionTotal` to the entire order.

Possible values are:

**•** `Product`

**•** `ProductCategory`

**•** `TransactionTotal`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionQualifierFeed on page 55**
Feed tracking is available for the object.

**PromotionQualifierHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment PromotionSegmentBuyerGroup PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegment

Represents a promotion segment, which you can assign to different stores or buyer groups, allowing them to access the promotion.
This object is available in API version 52.0 and later.


Standard Objects PromotionSegment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegment object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

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
Name of the promotion segment.


### Standard Objects PromotionSegmentBuyerGroup

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
The ID of the user who created this promotion segment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentFeed on page 55**
Feed tracking is available for the object.

**PromotionSegmentHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegmentBuyerGroup

Represents a promotion segment, associated with a buyer group, and used for B2B Commerce. This object is available in API version
52.0 and later.


Standard Objects PromotionSegmentBuyerGroup

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegmentBuyerGroup object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
BuyerGroupId

CurrencyIsoCode

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Buyer Group that you want to include in your market segment.

This is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

This field is available in API version 53.0 and later.


Standard Objects PromotionSegmentBuyerGroup

**Field** **Details**

```
LastViewedDate

Name

PromotionSegmentId

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

This field is available in API version 53.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion segment you want to associate with your buyer group.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentBuyerGroupFeed on page 55**
Feed tracking is available for the object.


### Standard Objects PromotionSegmentSalesStore

**PromotionSegmentBuyerGroupHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

### PromotionSegment

PromotionSegmentBuyerGroup

### PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### PromotionSegmentSalesStore

Represents a promotion segment, associated with a store, and used for B2B Commerce. This object is available in API version 52.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionSegmentSalesStore object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects PromotionSegmentSalesStore

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

PromotionSegmentId

SalesStoreId

```

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion segment you want to associate with your store.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store you want to include in your promotion segment.

This is a relationship field.

**Relationship Name**
SalesStore


### Standard Objects PromotionTarget

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
WebStore

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentSalesStoreFeed on page 55**
Feed tracking is available for the object.

**PromotionSegmentSalesStoreHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

### PromotionTarget

PromotionTier

### PromotionTarget

Represents the product, product category, or order that you want to target with your promotion in a B2B Store or D2C store. This object
is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PromotionTarget object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects PromotionTarget

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentPercent

AdjustmentType

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The promotion discount is expressed as an amount, not as a percentage.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage discount of the promotion. Valid values include numbers from 1 through
100.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of adjustment discount applied to the product or group of products.

Possible values are:

**•** `FixedAmountOffLineItemTotal` —Fixed amount off the total of all line
items.

**•** `FixedAmountOffTransaction` —Fixed amount off the entire transaction.
This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice` —Fixed amount off the unit price.

**•** `FixedPrice` —Fixed price for a product. This value is available in API version
56.0 and later.

**•** `TotalFixedPrice` —Fixed price for a set number of products. Requires a
quantity limit. This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice` —Fixed amount off the unit price.

**•** `PercentageDiscount` —Percentage discount.

**•** `BonusProduct` —Gift product at no additional cost after qualifying purchases.
This value is available in API version 64.0 and later.

**Type**
picklist


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code
for any currency allowed by the organization.

```
ExternalTarget

IsMinItemCountRequired

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A target product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.

Note: This field is available through the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the max value in the `RestrictionQuantity` field must be met before
the promotion is applied. The default value is `false` . This field is available in API version
56.0 and later.

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


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion target.

```
PromotionId

PromotionTierId

RestrictionQuantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to reference.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion tier associated with the target. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum number of times the discount can be applied to the target. This field is
available in API version 56.0 and later.


Standard Objects PromotionTarget

**Field** **Details**

```
TargetId

TargetOperator

TargetProductCategoryName

TargetProductName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product or product category that you want to target.

This is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
For product and category targets, specify if the qualifying product or item in the
qualifying category must be in the cart to determine if the cart satisfies the promotions
criteria. For example, a quantity or amount across one or more items. This field is available
in API version 59.0 and later.

Possible values are:

**•** `EQUAL_TO` —Specifies that the qualifying product or item in the qualifying category
must be in the cart.

**•** `NOT_EQUAL_TO` —Specifies that the qualifying product or item in the qualifying
category isn’t required to be in the cart.

**•** `NONE` —Specifies that none of the other possible values apply. If the target type is
for an order, you must use none.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the target. This field is available in API
version 55.0 and later.

**Type**
string


Standard Objects PromotionTarget

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the target. This field is available in API version
55.0 and later.

```
TargetProductSku

TargetRuleCriteriaType

TargetType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the target. This field is available in
API version 55.0 and later.

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls what promotion rules must be met for the promotion to be valid. This field is
available in API version 59.0 and later.

Possible values are:

**•** `ALL` —Specifies that all of the promotion rules must be met.

**•** `ANY` —Specifies that any of the promotion rules can be met.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The target of the promotion.

Possible values are:

**•** `Product` —Applies the promotion to a single product.

**•** `ProductCategory` —Applies the promotion to a group of products.

**•** `Shipping` —Applies the promotion to all shipping methods on the order.

**•** `StandardShippingRate` —Applies the promotion to a single shipping method
on the order.


### Standard Objects PromotionTier

**Field** **Details**

**•** `Transaction` —Applies the promotion to the entire order.

SEE ALSO:

### Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

### PromotionTier PromotionTier

Represents a tier of a promotion that includes multiple tiers. A promotion can have up to 10 tiers. This object is available in API version
57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

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


Standard Objects PromotionTier

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it can mean that the user accessed this record or list view ( `LastReferencedDate` ) but
didn’t view it.

```
Name

PromotionId

Rank

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the promotion tier.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the promotion tier.

This field is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of the tier among the associated promotion’s tiers. Tiers are evaluated in order from
lowest to highest rank. Each tier in a promotion must have a unique rank.

Use promotion tiers with promotion qualifiers and promotion targets to create tiered promotions. Instead of associating one promotion
qualifier and one promotion target with each promotion, associate one promotion qualifier and one promotion target with each
promotion tier.


### Standard Objects Prompt

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionTierFeed on page 55**
Feed tracking is available for the object.

**PromotionTierHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier

### Prompt

Represents record details about an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

### Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.

Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

### Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects Prompt

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the in-app guidance was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


### Standard Objects PromptAction

**Field** **Details**

refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

### PromptAction

Represents how the user interacted with the in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
LastDisplayDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last displayed to the user.


Standard Objects PromptAction

**Field** **Details**

```
LastResult

LastResultDate

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the last user interaction. Valid values are:

**•** `CustomAction`

**•** `Dismiss`

**•** `Error`

**•** `Finish` —(walkthroughs only)

**•** `NoAction`

**•** `NotSeen`

**•** `Snooze`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last interacted with.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the in-app guidance.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects PromptAction

**Field** **Details**

**Refers To**
Group, User

```
PromptVersionId

SnoozeUntil

StepCount

StepNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptVersion object.

This is a relationship field.

**Relationship Name**
PromptVersion

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp for when the user’s snooze request expires. The user won’t see the prompt
again until they navigate to the page after the snooze time expires.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the total number of steps in the walkthrough. Available in API version 49.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the number of the last step the user viewed or interacted with in a walkthrough.
Maximum value is 10. Available in API version 49.0 and later.


Standard Objects PromptAction

**Field** **Details**

```
TimesActionTaken

TimesDismissed

TimesDisplayed

TimesSnoozed

UserId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user took action on the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user dismissed the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the in-app guidance was displayed to the user.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of times the user snoozes the prompt.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects PromptError

Associated Objects

This object has the following associated objects. They are available in API version 46.0 and later.

**PromptActionOwnerSharingRule**

Sharing rules are available for the object.

**PromptActionShare**

Sharing is available for the object.

### PromptError

Represents the error or warning associated with the PromptAction. Available in API version 52.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
IsError

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the in-app guidance had an error `true` or a warning `false` . The default is
`false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the PromptError record.


Standard Objects PromptError

**Field** **Details**

```
OwnerId

PromptActionId

StepNumber

Type

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptAction that the PromptError is related to.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the step number that the user encountered an error or warning in a walkthrough.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the type of error or warning. Possible values are:

**•** `NoAccessToApp` —A step on this walkthrough is on an app that some of your users
don’t have access to.

**•** `NoAccessToPage` —A step on the walkthrough is on a page that some of your users
don’t have access to.

**•** `ReferenceElementNotFound` —The target element has moved or is no longer
on your page. Targeted prompts attached to unavailable elements convert to floating
prompts. Check your access to the element, or enter targeting mode and reassign the
targeted prompt.

**•** `Unavailable` —Users tried to open this walkthrough using its URL, but it's inactive
or the users aren’t licensed to see it. To make it accessible to users, check its settings or
activate it.


### Standard Objects PromptActionOwnerSharingRule

Associated Objects

This object has the following associated objects. They are available in API version 52.0 and later.

**PromptErrorOwnerSharingRule**

Sharing rules are available for the object.

**PromptErrorShare**

Sharing is available for the object.

### PromptActionOwnerSharingRule Represents a rule which determines PromptAction sharing access for the owners. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
   create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

   update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AccessLevel

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the access level of users for in-app guidance. Valid values are `Read` and `Edit` .

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the in-app guidance. Maximum of 255 characters.


### Standard Objects PromptActionShare

**Field** **Details**

```
DeveloperName

GroupId

Name

UserOrGroupID

### PromptActionShare

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### ID of the group whose PromptAction are shared.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the in-app guidance.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### ID of the user or group with whom PromptAction access is shared.

Represents a sharing entry on a prompt action record. Available in API version 46.0 and later.


Standard Objects PromptActionShare

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AccessLevel

ParentId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the access level of users for in-app guidance. Valid values are `Read`, `Edit`, and
`All` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects PromptLocalization

**Field** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule` —The User or Group has access via a sharing rule.

**•** `GuestRule` —The User or Group has access via a guest user sharing rule.

**•** `Manual` —The User or Group has access because a User with “All” access manually
shared the prompt action with them.

**•** `Owner` —The User is the owner of the prompt action.

```
UserOrGroupId

### PromptLocalization

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the User or Group.

Represents the translated value of a label for record details about in-app guidance when the Translation Workbench is enabled for your
org. Available in API version 48.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects PromptLocalization

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

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
Indicates the language used in the org where the in-app guidance was created.

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

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update


### Standard Objects PromptVersion

**Field** **Details**

**Description**
The actual translated record details for the in-app guidance.

### PromptVersion

Represents an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, see Considerations for](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)
[Creating In-App Guidance and Permissions for Creating and Accessing In-App Guidance in](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US) _Salesforce Help_ for permissions.

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field** **Details**

```
ActionButtonLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the action button or link. Maximum of 25 characters. For a walkthrough, specify
this value on the last step.


Standard Objects PromptVersion

**Field** **Details**

```
ActionButtonLink

Body

DelayDays

Description

DismissButtonLabel

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for the action button or link. Maximum of 1,000 characters. You can’t use the `GROUP`
`BY` option in a SOQL query for this field. For a walkthrough, specify this value on the last
step.

**Type**
textarea

**Properties**
Create, Update

**Description**
Body content.

In API version 60.0 and later, enter up to 4,000 characters for all prompt types.

In earlier API versions, enter up to 240 characters for floating prompts and targeted prompts.
Enter up to 4,000 characters for docked prompts.

For docked prompts, the maximum characters include HTML markup, not just readable text.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of days between occurrences. For a walkthrough, specify this value on the first step.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the dismiss button of a floating or targeted prompt. Maximum of 15 characters.


Standard Objects PromptVersion

**Field** **Details**

```
DisplayPosition

DisplayType

ElementRelativePosition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position of a floating prompt on the page. Valid values are:

**•** `TopLeft`

**•** `TopCenter`

**•** `TopRight`

**•** `MiddleLeft`

**•** `MiddleCenter`

**•** `MiddleRight`

**•** `BottomLeft`

**•** `BottomCenter`

**•** `BottomRight`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of prompt. Valid values are:

**•** `DockedComposer` —A docked prompt

**•** `FloatingPanel` —A floating prompt

**•** `Targeted` —A targeted prompt. Available in API version 52.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The location of a targeted prompt relative to the element. This field is available in API version
52.0 and later. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `LeftBottom`

**•** `LeftCenter`

**•** `LeftTop`


Standard Objects PromptVersion

**Field** **Details**

**•** `RightBottom`

**•** `RightCenter`

**•** `RightTop`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

```
EndDate

Experience

ExperienceContextId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date to stop showing the in-app guidance. For a walkthrough, specify this value on the
first step.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field corresponds to the **Environment** picklist in In-App Guidance Builder. Available in
version 60.0 and later.

Possible values are:

**•** `Lightning` —Default. The in-app guidance is used in a Lightning Experience app or
page.

**•** `Site` —The in-app guidance is used in a supported Experience Cloud site page.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the value of `Experience` is `Site` . The ID of the Experience Cloud site context
associated with the in-app guidance prompt. Available in version 60.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ExperienceContext

**Relationship Type**
Lookup

**Refers To**
Site


Standard Objects PromptVersion

**Field** **Details**

```
Header

ImageAltText

ImageId

ImageLocation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label for the header of a docked prompt. This value is the label contained in the window’s
browser bar. Maximum of 36 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the alt text of an image. Required if `ImageLocation` or `ImageID` is specified.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentAsset that holds the image. Required if `ImageLocation` or
`ImageAltText` is specified.

This is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the location of the image in relation to the body text. Required if `ImageID` or
`ImageAltText` is specified. Valid values are:

**•** `Top`

**•** `Bottom`

**•** `Right`, which is for floating or targeted prompts only

**•** `Left`, which is for floating or targeted prompts only


Standard Objects PromptVersion

**Field** **Details**

```
IndexWithIsPublished

IndexWithoutIsPublished

IsPublished

MasterLabel

ParentId

```

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Used by Salesforce for efficient querying.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance is active ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Prompt


Standard Objects PromptVersion

**Field** **Details**

```
PublishedByUserId

PublishedDate

ReferenceElementContext

ShouldDisplayActionButton

ShouldIgnoreGlobalDelay

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who activated the in-app guidance. If the in-app guidance is part of a
package, this value is the user who installed the package.

This is a relationship field.

**Relationship Name**
PublishedByUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was activated. If installed from a package, this value
is the date when the package was installed. For walkthroughs, this field can only be specified
on the first step.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Used by Salesforce to identify the element that the targeted prompt is associated with.
Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an action button or link is included ( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects PromptVersion

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the in-app guidance ignores the global time delay and instead shows on
page load ( `true` ) or not ( `false` ). This field is available in API version 48.0 and later.

```
StartDate

StepNumber

TargetAppDeveloperName

TargetAppNamespacePrefix

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the date to start showing the in-app guidance. For a walkthrough, specify this value
on the first step.

In API version 48.0 and earlier, this field is required.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for walkthroughs only. Indicates the number of the last step the user viewed or
interacted with in a walkthrough. Include up to 10 steps. Numbers must be consecutive
without repeated or skipped numbers. Available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s developer name where the in-app guidance appears. Deprecated in API version
51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The app’s namespace prefix where the in-app guidance appears. This value must match the
target app’s `NamespacePrefix` in the org that the package is being installed into.
Maximum of 15 characters. Deprecated in API version 51.0 and later.


Standard Objects PromptVersion

**Field** **Details**

```
TargetPageKey1

TargetPageKey1Ref

TargetPageKey2

TargetPageKey3

TargetPageKey4

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Used by Salesforce to identity the prompt’s page location along with
`targetPageKey2`, `targetPageKey3`, `targetPageKey4`, and
`targetPageType` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey2`,
`TargetPageKey3`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey1`,
`TargetPageKey3`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the prompt’s page location along with `TargetPageKey1`,
`TargetPageKey2`, `TargetPageKey4`, and `TargetPageType` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to identify the page location along with `TargetPageKey1`,
`TargetPageKey2`, `TargetPageKey3`, and `TargetPageType` . This field is available
in API version 53.0 and later.


Standard Objects PromptVersion

**Field** **Details**

```
TargetPageType

TargetRecordType

ThemeColor

ThemeSaturation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of page where the in-app guidance appears.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by Salesforce to determine if in-app guidance is specific to a record type. This field is
available in API version 53.0 and later.

**Relationship Name**
TargetRecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which custom theme color is applied to the in-app guidance. Required if
`ThemeSaturation` is specified. For a walkthrough, specify this value on the first step.
Valid values are:

**•** `Theme1` —derived from the current brand color

**•** `Theme2` —derived from the current page background color

**•** `Theme3` —derived from the current global header color

**•** `Theme4` —derived from the current app theme color

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects PromptVersion

**Field** **Details**

**Description**
Indicates which color value, or saturation, is applied to the in-app guidance that has a custom
theme color. Required if `ThemeColor` is specified. For a walkthrough, specify this value
on the first step. Valid values are:

**•** `Dark`

**•** `Light`

```
TimesToDisplay

Title

UserAccess

UserProfileAccess

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if recurrences are scheduled. The maximum number of times to show the in-app
guidance. Salesforce detects whether the user interacts with the in-app guidance, then
determines whether to show the in-app guidance again or cancel scheduled recurrences.
Maximum value of 30. For a walkthrough, specify this value on the first step.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The label for the title. Maximum of 36 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which permissions can see the in-app guidance. Valid values are:

**•** `Everyone`, which indicates that there’s no permission restrictions

**•** `SpecificPermissions`, which indicates that only users with all the specific user
permissions specified can see the in-app guidance

In API version 48.0 and earlier, this field is required.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates which profiles can see the in-app guidance. This field is available in API version 48.0
and later. Valid values are:


### Standard Objects PromptVersionLocalization

**Field** **Details**

**•** `Everyone`, which indicates that there are no profile restrictions

**•** `SpecificProfiles`, which indicates that users with any of the specified user profiles
can see the in-app guidance

```
VersionNumber

VideoLink

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The number remains `1` since multiple versions aren’t saved in the org.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The embed URL for a video in a docked prompt. Maximum of 1,000 characters. You can
specify this field or the `image` field, but not both. This field is available in API version 48.0
[and later. See Considerations for Creating In-App Guidance.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)

### PromptVersionLocalization

Represents the translated value of a label for-app guidance when the Translation Workbench is enabled for your org. Available in API
version 48.0 and later.

Use prompts and walkthroughs to display announcements, training, or news to users within the app. Choose to add an action button
or link that links to a URL of your choice. Track views, action button clicks, and walkthrough completions.

Supported Calls

```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),

update(), upsert()

```

Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_wt_license.htm&type=5&language=en_US)

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)


Standard Objects PromptVersionLocalization

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

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
Indicates the language used in the org where the in-app guidance was created.

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

**•** In orgs that aren't Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update


### Standard Objects Prospect

**Field** **Details**

**Description**
The actual translated label of the in-app guidance.

### Prospect

Represents a prospect. A prospect is an individual who has shared contact information, but isn't yet qualified. This object is available in
API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Address

AnnualRevenue

City

Company

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Street address of the prospect. Up to 255 characters are allowed.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The prospect company's yearly revenue.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City that's included in the prospect’s address.

**Type**
string


Standard Objects Prospect

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's company.

```
ConvertedAccountId

ConvertedContactId

ConvertedDate

ConvertedLeadId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the account into which the prospect converted.

This is a relationship field.

**Relationship Name**
ConvertedAccount

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the contact into which the prospect converted.

This is a relationship field.

**Relationship Name**
ConvertedContact

**Refers To**
Contact

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date on which this prospect was converted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Prospect

**Field** **Details**

**Description**
Object reference ID that points to the lead into which the prospect has been converted.

This is a relationship field.

This field is a relationship field.

**Relationship Name**
ConvertedLead

**Refers To**
Lead

```
ConvertedOpportunityId

Country

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the opportunity into which the prospect has been
converted.

This is a relationship field.

**Relationship Name**
ConvertedOpportunity

**Refers To**
Opportunity

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Prospect's country.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects Prospect

**Field** **Details**

**Description**
The prospect’s description.

```
Email

FirstName

GenderIdentity

GeocodeAccuracy

Industry

IsConverted

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's email address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect’s first name. Up to 40 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect’s self-identified experience of their gender, which does or doesn’t correspond
to the prospect’s designated sex at birth.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. For details on geolocation compound fields,
see Geolocation Compound Field on page 18.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Primary business of the prospect’s company

**Type**
boolean


Standard Objects Prospect

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the prospect has been converted ( `true` ) or not ( `false` ). Label is
**Converted** .

```
LastName

Latitude

LeadSource

Longitude

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The Last name of the prospect. Up to 80 characters are allowed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –90 and 90 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations on page 19.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin or source of the lead.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations on page 19.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Prospect

**Field** **Details**

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

```
NumberOfEmployees

Phone

PostalCode

ProspectRecordName

ProspectStatus

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of employees at the prospect's company. Label is **Employees** .

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code that's included in the prospect's address. Label is **Zip/Postal Code** .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the prospect record used for managing prospects.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the prospect.

Possible values are:

**•** `Contacted`

**•** `New`


Standard Objects Prospect

**Field** **Details**

**•** `Nurturing`

**•** `Qualified`

**•** `Unqualified`

The default value is `New` .

```
Salutation

State

Street

Title

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's preferred title.

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Mx.`

**•** `Prof.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State that's included in the prospect's address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street number or name that's included in the prospect's address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prospect's business title, such as CFO or CEO. The maximum size is 128 characters. When
converting a prospect to a person account, the conversion fails if the prospect Title field
contains more than 80 characters.


### Standard Objects ProrationPolicy ProrationPolicy

Defines how the price of a subscription is divided into time periods and how the price is calculated for each time period. This object is
available in API version 55.0 and later.

The proration policy defines whether partial periods are allowed and how remainder amounts are handled.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   search()

```

Special Access Rules

This object is available when Subscription Management is enabled.

Fields

**Field** **Details**

```
ArePartialPeriodsAllowed

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a subscription can be canceled partway through a period.

Set the value to `True` if a subscription can be canceled partway through a period. Otherwise,
set the value to `false` .

For example, if the proration period is monthly and this field is `true`, then customers can
cancel a subscription partway through the month. If the proration period is monthly and
this field is `false`, then the subscription is canceled at the end of the current month.

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


Standard Objects ProrationPolicy

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list `viewLastReferencedDate` but
not viewed it.

```
Name

ProrationPolicyType

RemainderStrategy

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the proration policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of proration policy.

Possible values are:

**•** `StandardTimePeriods` —Indicates that the proration policy divides the subscription
into similar time periods, and prorates the subscription using the time periods. For
example, a monthly subscription that's subscribed to for 12 months for a total amount
of $120 is prorated as $10 per month.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates how the leftover amount from the price calculation is allocated.

For example, if the total amount is $100 and the subscription has 12 periods, the price per
period is $8.33, with $0.04 remaining. To indicate that the $0.04 is included in the first period,
use the value `AddToFirst` . To indicate that the $0.04 is included in the final period, use
the value `AddToLast` .

Possible values are:

**•** `AddToFirst` —Add the remaining amount to the first period.

**•** `AddToLast` —Add the remaining amount to the last period.


### Standard Objects PublicComplaint PublicComplaint

Represents the complaints submitted by public users. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Fields added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

Fields

**Field** **Details**

```
AccountId

BusinessAddress

BusinessName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Account associated with this complaint.

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
Create, Filter, Nillable, Sort, Update

**Description**
The address of the business.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The name of the business.

```
CauseSubtype

CauseType

Comments

CompensationAmount

ComplaintCaseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Misleading advertisement or documentation`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Product Communication`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Additional details about the complaint. This field is available in API version 51.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Any amount of money offered to resolve the complaint. This field is available in API version
58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The ID of the related Case. This field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ComplaintCase

**Relationship Type**
Lookup

**Refers To**
Case

```
ComplaintCaseStatus

ComplaintSubType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The status of the related Case. This field is available in API version 58.0 and later.

Possible values are:

**•** `Closed`

**•** `Escalated`

**•** `In Progress`

**•** `Merged`

**•** `New`

**•** `On Hold`

**•** `Response Received`

**•** `Waiting for Customer`

**•** `Working`

The default value is `New` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint. All values except `Fire Safety` are available in API version
58.0 and later.

Possible values are:

**•** `Account Opening/Closure`

**•** `Amount Not Dispensed`

**•** `Attempts to Collect Debt not Owed`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Auto Debit Mandate`

**•** `Communication Tactics`

**•** `Credit Limit Changed`

**•** `Credit Report / Credit Score`

**•** `Delays / Timescales`

**•** `Disputes over sums/charges`

**•** `Errors / not following instructions`

**•** `Fire Safety`

**•** `Fraud Handling`

**•** `Inaccessible ATMs`

**•** `Inaccessible Branch Entrances`

**•** `Inaccessible Mobile banking features`

**•** `Inaccessible Website`

**•** `Misleading Advertising`

**•** `Mobile Banking - Features or Functionality`

**•** `No Written Notification About Debt`

**•** `Online Banking - Features or Functionality`

**•** `Other General Admin/Customer Service`

**•** `Others`

**•** `Problem when Making Payments`

**•** `Product Disclosure Information`

**•** `Product Performance/Features`

**•** `Unauthorised Transaction(s)`

**•** `Unclear Arrangement`

**•** `Unclear Guidance`

**•** `Unsuitable Advice`

```
ComplaintSummary

ComplaintType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of customer complaints and related cases. This field is available in API version
62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The type of complaint. All values except `Safety` are available in API version 58.0 and later.

Possible values are:

**•** `Accessibility Issues`

**•** `Advising, Selling and Arranging`

**•** `Digital or Technology`

**•** `Financial Hardship or Collections`

**•** `General Admin/ Customer Service`

**•** `Information, sums/ charges or Product Performance`

**•** `Lending / Credit`

**•** `Marketing or Corporate Communications`

**•** `Others`

**•** `Safety`

**•** `Transaction Related`

```
Description

Email

EscalationCause

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the complaint.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email of the complainant.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the complaint was escalated. This field is available in API version 58.0 and later.

Possible values are:

**•** `Alleged ADA Violation`

**•** `Alleged Discrimination`

**•** `Alleged MLA Violation`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Alleged SCRA Violation`

**•** `Alleged UDAAP Violation`

**•** `Consumer Protection Agency Involvement`

**•** `Lawsuit Filed`

**•** `Media Involvement`

**•** `None`

**•** `Received by Executive Leadership`

The default is `None` .

```
FirstName

IncidentDate

IsComplainantAuthorized

IsReporterConfidential

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The given name of the complainant.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date of the incident.

The default is the date this record was created, but this field is editable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the person who filed the complaint is an authorized representative of the Account.
This field is available in API version 58.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The reporter's request for confidentiality.

The default value is `false` .


Standard Objects PublicComplaint

**Field** **Details**

```
LastName

LastReferencedDate

LastViewedDate

MobileNumber

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The family name of the complainant.

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
possibly the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The mobile number of the complainant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the complaint.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects PublicComplaint

**Field** **Details**

**Description**
The ID of the complaint owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Priority

ProductType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the complaint.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `Medium` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product that the complaint is about. This field is available in API version 58.0 and later.

Possible values are:

**•** `ATM / debit card`

**•** `Credit Card or Prepaid Card`

**•** `Insurance`

**•** `Investments`

**•** `Merchant Services`

**•** `Mobile / electronic banking`

**•** `Money transfers, virtual currency, and money services`

**•** `Mortgage / Home Finance`

**•** `Other`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Personal Loan / other loans`

**•** `Vehicle loan or lease`

```
ReceivedDate

ReferenceRecordId

ReporterAddress

ReporterCategory

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the complaint was received. This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset, vehicle, or financial account that’s associated with the public complaint. This field
is available in API version 64.0 and later with Automotive Cloud.

This field is a relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Financial Account, Asset, Vehicle, Product2

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address of the reporter for further communication.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Role of the reporter in the organization.

Possible values are:

**•** `Childcare Providers`

**•** `Healthcare worker`


Standard Objects PublicComplaint

**Field** **Details**

**•** `Law Enforcement`

**•** `Medical Examiners`

**•** `Mental Health Professionals`

**•** `Other`

**•** `School Personnel`

**•** `Social Worker`

The default value is `School Personnel` .

```
ReporterOrganization

ShouldInclInRegulatoryRpt

SourceType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The organization the reporter is part of.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this complaint must be included in a regulatory report. This field is available in API
version 58.0 and later.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the complaint. This field is available in API version 58.0 and later.

Possible values are:

**•** `Branch`

**•** `Consumer Protection Agency`

**•** `Contact Centre`

**•** `Mobile App`

**•** `Regulatory Agency`

**•** `Social Media`

**•** `Web Chat`


### Standard Objects PurchaseQuantityRule

**Field** **Details**

```
Status

Subject

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the complaint.

Possible values are:

**•** `In Review`

**•** `Resolved`

**•** `Submitted`

The default value is `Submitted` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Subject of the complaint. This field is available in API version 51.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PublicComplaintFeed on page 55**
Feed tracking is available for the object.

**PublicComplaintHistory on page 63**
History is available for tracked fields of the object.

**PublicComplaintOwnerSharingRule on page 65**
Sharing rules are available for the object.

**PublicComplaintShare on page 67**
Sharing is available for the object.

### PurchaseQuantityRule

Represents a rule that restricts the quantity of a product that can be purchased. The rule can be an increment, minimum, or maximum
rule. This object is available in API version 52.0 and later.


Standard Objects PurchaseQuantityRule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The PurchaseQuantityRule object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Increment

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Quantity of product that can be added with each increase.

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


Standard Objects PurchaseQuantityRule

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

```
Maximum

Minimum

Name

OwnerId

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Maximum quantity that can be purchased.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Minimum quantity that can be purchased.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the purchase quantity rule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects PushTopic PushTopic

Represents a query that is the basis for notifying Streaming API clients of changes to records in an org. This object is available in API
version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** To receive notifications, users must have read access on both the object in the PushTopic query and the PushTopic itself.

Fields

**Field** **Details**

```
ApiVersion

Description

IsActive

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. API version to use for executing the query specified in `Query` . It must be an API
version greater than 20.0. If your query applies to a custom object from a package, this value
must match the package's `ApiVersion` .

Example value:

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the PushTopic. Limit: 400 characters

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the record currently counts towards the organization's allocation.


Standard Objects PushTopic

**Field** **Details**

```
Name

NotifyForFields

NotifyForOperationCreate

NotifyForOperationDelete

NotifyForOperationUndelete

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Descriptive name of the PushTopic, such as `MyNewCases` or
`TeamUpdatedContacts` . Limit: 25 characters. This value identifies the channel and
must be unique.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies which fields are evaluated to generate a notification.

Possible values are:

**•** `All`

**•** `Referenced` (default)

**•** `Select`

**•** `Where`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a create operation should generate a notification, otherwise, `false` . Defaults to
`true` . This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a delete operation should generate a notification, otherwise, `false` . Defaults to
`true` . Clients must connect using the `cometd/29.0` (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

**Type**
boolean


Standard Objects PushTopic

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
`true` if an undelete operation should generate a notification, otherwise, `false` . Defaults
to `true` . Clients must connect using the `cometd/29.0` (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

```
NotifyForOperationUpdate

NotifyForOperations

Query

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if an update operation should generate a notification, otherwise, `false` . Defaults
to `true` . This field is available in API version 29.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies which record events may generate a notification.

In API version 29.0 and later, this field is read-only, and doesn’t contain information about
delete and undelete events. Use `NotifyForOperationCreate`,
`NotifyForOperationDelete`, `NotifyForOperationUndelete` and
`NotifyForOperationUpdate` to specify which record events should generate a
notification.

Possible values are:

**•** `All` (default)

**•** `Create`

**•** `Extended`

**•** `Update`

A value of `Extended` means that neither create or update operations are set to generate
events.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The SOQL query statement that determines which record changes trigger events
to be sent to the channel.


### Standard Objects PushUpgradeCustomization

**Field** **Details**

Limit: 1,300 characters

Usage

The PushTopic defines when notifications are generated in the channel. Determine which fields to configure by checking out these links
in the _Streaming API Developer Guide_ .

**•** [PushTopic Queries](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/pushtopic_queries.htm)

**•** [Events](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/events.htm)

**•** [Notifications](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/notifications.htm)

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_streaming.meta/api_streaming/intro_stream.htm)_

### PushUpgradeCustomization

Customized push upgrades allow a package subscriber to block push upgrades to their org. Package developers control which subscribers
can opt into customized push upgrades. Each push upgrade customization maps to a specific package and to a specific subscriber org.
This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomUpgradeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of push upgrade customization.

Possible values are:

**•** `BlockedBySubscriber` —Blocked By Subscriber

**•** `None`

The default value is `None` .


### Standard Objects QueuedExecutionEventLog

**Field** **Details**

```
HasRestrictionEnabled

IsCustomUpgradeAllowed

IsRestrictionOverridden

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the subscriber org has blocked push upgrades.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the package developer has allowed a subscriber to opt into customized
push upgrades.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether customized push upgrades have been overridden by Salesforce Customer
Support for the subscriber org.

The default value is `false` .

### QueuedExecutionEventLog

Queued Execution events contain details about queued executions—for example, batch Apex. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects QueuedExecutionEventLog

Fields

**Field** **Details**

```
ClientIp

CpuTime

DatabaseTotalTime

LoginKey

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DB_CPU_TIME. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

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
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.


Standard Objects QueuedExecutionEventLog

**Field** **Details**

```
RequestStatus

RunTime

SessionKey

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

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


Standard Objects QueuedExecutionEventLog

**Field** **Details**

For example: `20130715233322.670` .

```
Uri

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.


### Standard Objects QueueRoutingConfig

**Field** **Details**

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### QueueRoutingConfig

Represents the settings that determine how work items are routed to agents. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
CapacityPercentage

CapacityWeight

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a specific type of
work item from this service channel.

Voice calls must have a capacity percentage of _`100`_ . If an agent receives a voice call, the
agent won’t receive new work items until the call ends, because at that point the agent’s
capacity will have reached 100%.

This field is available in API version 33.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a work item from this
service channel.


Standard Objects QueueRoutingConfig

**Field** **Details**

For example, if an agent has a capacity of _`6`_, and cases are assigned a capacity weight of _`2`_,
an agent can be assigned up to 3 cases before the agent is at capacity and can’t receive new
work items. Voice calls must use the entire capacity weight.

This field is available in API version 33.0 and later.

```
DeveloperName

DropAdditionalSkillsTimeout

IsAttributeBased

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group Nillable, Sort, Update

**Description**

The number of seconds to wait before a skill marked as **Additional Skill** is dropped from
Omni-Channel routing. The case is then routed to the best-matched agent even if they don’t
have all the skills.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this routing is attribute-based. Available in API version 45.0 and later.

**Type**
picklist


Standard Objects QueueRoutingConfig

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the presence status.

```
MasterLabel

OverflowAssigneeId

PausedCapacityPercentage

PausedCapacityWeight

PushTimeout

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the presence status.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user or queue that’s set as the Overflow Assignee.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a paused work
item from this service channel. The paused capacity feature is available with status-based
capacity and Enhanced Omni-Channel only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a paused work item
from this service channel. The paused capacity feature is available with status-based capacity
and Enhanced Omni-Channel only.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects Question

**Field** **Details**

**Description**
The number of seconds set for push timeout. **0** is returned when push timeout isn’t enabled.
Available in API version 36.0 and later.

```
RoutingModel

RoutingPriority

ServiceChannelId

### Question

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The routing type that determines how work items are routed (pushed) to agents. Possible
values are `Least Active` and `Most Available` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority in which work items from the service channels that are related to this routing
configuration are routed to agents. Work items from routing configurations that have lower
priority values (for example, _`0`_ ) are routed to agents first.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service channel that’s associated with this configuration. This field is available
in API version 32.0 and earlier.

Represents a question in a zone that users can view and reply to.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Question

Special Access Rules

This object is only available if the Answers permission and AnswersEnabled preference or PortalFeed permission and PortalFeedEnabled
preference are enabled in your org.

Fields

**Field** **Details**

```
BestReplyId

BestReplySelectedById

Body

CommunityId

CreatorFullPhotoUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the reply that has been identified as the best answer to the question. Use
the user interface to identify the best answer for a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who selected the best answer to the question.

This field is available in API version 24.0 and later. In API version 24.0 through version
29.0, you must update this field using the UI. In API version 30.0 and later, you can
update this field using the API.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the question.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the question. After you create a question, you can’t
change the zone ID associated with that question.

**Type**
string


Standard Objects Question

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to
view this field. This field is available in API version 26.0 and later.

```
CreatorName

CreatorSmallPhotoUrl

HasSingleFieldForContent

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal
users (agents) appears to portal users in the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the content of a Chatter Answers question is:

**•** Included in only one field: `Title` if the content is unformatted and less than
255 characters; or `Body` if the content is formatted or more than 255 characters
( `true` )

**•** Included in two fields: `Title` and `Body` ( `false` )

This field also determines if content displays in one or two fields in Chatter Answers
question feeds.

This field is available in API version 25.0 and later.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


Standard Objects Question

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastReplyDate

LastReplyId

LastViewedDate

MostReportAbusesOnReply

NumReplies

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last reply (child Reply object) was posted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last reply (child Reply object) posted to the question.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is null,
this record might only have been referenced ( `LastReferencedDate` ) and not
viewed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most number of user-reported abuses on a Reply associated with the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies (child Reply object) that users have submitted for the question.


Standard Objects Question

**Field** **Details**

```
NumReportAbuses

NumSubscriptions

Origin

Title

UpVotes

VoteScore

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of user-reported abuses on the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of users following the question.

This field is available in API version 24.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the question, such as `Chatter Answers` .

This field is available in API version 24.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The descriptive title of the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for the question.

**Type**
double


### Standard Objects QuestionDataCategorySelection

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the question, used to sort questions and articles on the Popular
tab in the application user interface. The internal algorithm that determines the score
gives older votes less weight than newer votes, simulating exponential decay. The
score itself doesn’t display in the application user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate
function with this field.

Usage

Use this object to track questions in a zone.

### QuestionDataCategorySelection

A data category selection represents a data category that classifies a question.

This object can be used to associate a question with a data category from a data category group or to query the categorization for a
question.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To create, read or update data category selection, you must have create, read or update permission on the categorized question. Users
who can update question can also delete its category selection. Users who can create questions can only select categories visible to
their role.

Fields

**Field Name** **Details**

```
DataCategoryGroupName

```

**Type**
DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category group which has a category associated with
the question.


Standard Objects QuestionDataCategorySelection

**Field Name** **Details**

```
DataCategoryName

ParentId

```

Usage

**Type**
DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category associated with the question.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the question associated with the data category selection.

Every question can be categorized in a data category. You can use the QuestionDataCategorySelection object to query and manage
question categorization. Client applications can create categorization for a question. They can also delete, query, and retrieve question
categorization.

Warning: Even though the API lets you select more than one category for QuestionDataCategorySelection, the Answers tab only
supports one data category selection for questions. Selecting multiple categories through QuestionDataCategorySelection may
result in unexpected behavior in the Answers tab, such as losing your multiple selections. You should only select one data category
when using QuestionDataCategorySelection.

Sample Code—Java

In the following example, the `selectCategory` method adds a category to a question data category selection. The
`retrieveCategorySelections` method returns all the categories from a question data category selection.

```
public void selectCategory(ID parentId, String categoryGroupName, String categoryName) {

   try {

     QuestionDataCategorySelection categorySelection = new

QuestionDataCategorySelection();

     categorySelection.setParentId(parentId);

     categorySelection.setDataCategoryGroupName(categoryGroupName);

     categorySelection.setDataCategoryName(categoryName);

     binding.create(new SObject[]{categorySelection});

   } catch (RemoteException e) {

     System.out.println("An unexpected error has occurred." + e.getMessage());

   }

}

public String[] retrieveCategorySelections(String parentId) {

   QueryResult qr = null;

```


### Standard Objects QuestionReportAbuse

```
      try {

        qr = binding.query("SELECT DataCategoryName FROM QuestionDataCategorySelection

   WHERE Id = '" + parentId + "'");

      } catch (RemoteException e) {

        System.out.println("An unexpected error has occurred." + e.getMessage());

      }

      String[] categoryNames = new String[qr.getRecords().length];

      for (int index = 0; index < qr.getRecords().length; index++) {

        categoryNames[index] =

   ((QuestionDataCategorySelection)qr.getRecords()[index]).getDataCategoryName();

      }

      return categoryNames;

   }

```

Salesforce Knowledge uses a similar object for article data category selection. See Article Type __DataCategorySelection
__DataCategorySelection for SOQL examples using this object.

SEE ALSO:

Article Type __DataCategorySelection __DataCategorySelection

### QuestionReportAbuse

Represents a user-reported abuse on a Question in a Chatter Answers zone. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

QuestionId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Question from which the user reported abuse.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects QuestionSubscription

**Field** **Details**

**Description**
The ID of the Question from which the user reported abuse.

```
Reason

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Question, such as `Spam`, `Hateful`, or
`Inappropriate` .

Use this object to track user-reported abuse on questions created in a Chatter Answers zone.

### QuestionSubscription

Represents a subscription for a user following a Question. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommunityId

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the zone associated with the Question the user is following. This field
can’t be updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort


### Standard Objects QueueSobject

**Field** **Details**

**Description**
The name of the question subscription.

```
QuestionCreatedDate

QuestionId

SubscriberId

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Required. Creation date of the Question which the user is following. This field can’t
be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Question which the user is following. This field can’t be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the User who is following the Question. This field can’t be updated.

Things to consider when following a Question:

**•** A user can only follow questions that they have permission to view.

**•** Administrators and users with the “Modify All Data” permission can configure other users to follow questions that the other user has
read access to.

**•** Administrators and users with the “Modify All Data” permission can configure users to stop following questions.

Queries on QuestionSubscription:

**•** Users with the “Read” permission on Question can see which questions other users are following.

**•** A query must include a LIMIT clause and the limit can’t exceed 1,000.

**•** A query using a `WHERE` clause can only filter by fields on Question.

### QueueSobject

Represents the mapping between a queue Group and the types associated with the queue, including custom objects.


Standard Objects QueueSobject

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

A queue is a Group whose `Type` is `Queue` . To create a Group, you must have the Manage Users permission.

Fields

**Field** **Details**

```
 QueueId

 SobjectType

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a queue.

This field is a relationship field.

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
A list of object types that can be associated with the queue specified by the `QueueId` .

Use this object to associate a queue with the sObject that can be associated with the queue, including custom objects.

Warning: You can't update or insert more than 18 queues at once when using the Bulk API.

SEE ALSO:

Overview of Salesforce Objects and Fields


### Standard Objects QuickText QuickText

This object stores a snippet of text that allows users to send a quick response to a customer. Use quick text to create greetings, answers
to common questions, short notes, and more. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Channel

FolderId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
A customizable picklist that can be used to group multiple related quick text
records together

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
A multi-select picklist that can be used to specify where specific quick text
messages are available, such as in Chat or in the Email publisher in Case Feed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Returns the ID of the folder that contains the quick text. Available in API version
44.0 and later.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup


Standard Objects QuickText

**Field Name** **Details**

**Refers To**
Folder

```
FolderName

IsInsertable

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the quick text. Available in API version 44.0 and
later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the quick text is available in the channels selected in the `Channel`
field. If `false`, the quick text is not available. The label in the UI is **Include in**
**selected channels** . By default:

**•** This field is set to `true` on quick text records created from the Quick Text
page or via the API.

**•** This field is set to `false` on quick text records created during the Einstein
Reply Recommendations reply publishing process.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.


Standard Objects QuickText

**Field Name** **Details**

```
Message

Name

OwnerId

SourceType

```

**Type**
textarea

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Sort (unavailable in API
version 25.0 and later), Update

**Description**
The content of the quick text record

**Type**
string

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Group, idLookup, Sort
(unavailable in API version 25.0 and later), Update

**Description**
A descriptive label for the quick text record

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Queue that owns the quick text record

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
(Used with Einstein Reply Recommendations.) Indicates how the text was
composed. This field is not available in the UI.

Possible values are:

**•** `EINSTEIN_GENERATED` —Text was generated by Einstein Reply
Recommendations


### Standard Objects QuickTextUsage

**Field Name** **Details**

**•** `USER_EDITED` —Text was generated by Einstein Reply Recommendations,
and then edited by a user

**•** `USER_GENERATED` —User wrote the text

Usage

Use this object to create and manage the quick text messages available to users. You can categorize multiple quick text records into
groups using the Category field. The Category field can also be a parent to multiple custom-dependent Picklist fields to create a hierarchical
structure of categories.

QuickText is also used in Einstein Reply Recommendations, a feature that recommends stock replies for support agents to use in chats
in the Lightning Service Console. During setup, Einstein Reply Recommendations scans past chats to generate a list of commonly used
replies. Each generated reply is a ReplyText record. The admin then publishes, or converts, the replies to quick text, creating a corresponding
QuickText record for each reply. Therefore, certain QuickText fields are used only on quick text records that originated as a ReplyText
record.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuickTextChangeEvent (API version 48.0)**
Change events are available for the object.

**QuickTextHistory**

History is available for tracked fields of the object.

**QuickTextOwnerSharingRule**

Sharing rules are available for the object.

**QuickTextShare**

Sharing is available for the object.

### QuickTextUsage

Represents the usage of quick text on a record, including which quick text was used, who used it, and how they used it. Quick text is a
snippet of text that allows users to send a quick response to a customer. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is always read-only.


Standard Objects QuickTextUsage

Fields

**Field** **Details**

```
AppContext

Channel

FolderId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the quick text was used. Possible values are:

**•** `Aloha` —Salesforce Classic

**•** `Lightning` —Lightning Experience

**•** `Unknown`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The channel in which the quick text was used. Possible values are:

**•** `Email`

**•** `Event`

**•** `Generic`

**•** `Internal`

**•** `Knowledge`

**•** `Live Agent`

**•** `Messaging`

**•** `Phone`

**•** `Portal`

**•** `Social`

**•** `Task`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the quick text at the time it was used.

This is a relationship field.

**Relationship Name**
Folder


Standard Objects QuickTextUsage

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Folder

```
LaunchSource

LoggedTime

Name

OwnerId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the user started the quick text. Possible values are:

**•** `Floater`

**•** `Keyboard shortcut`

**•** `Macro`

**•** `Toolbar`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the quick text was used.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the quick text.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the quick text.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects QuickTextUsage

**Field** **Details**

**Refers To**
Group, User

```
QuickTextID

UserId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the quick text.

This is a relationship field.

**Relationship Name**
QuickText

**Relationship Type**
Lookup

**Refers To**
QuickText

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that used the quick text.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**QuickTextUsageChangeEvent (API version 62.0)**
Change events are available for the object.

**QuickTextUsageOwnerSharingRule**

Sharing rules are available for the object.

**QuickTextUsageShare**

Sharing is available for the object.


### Standard Objects Quote Quote

Represents a quote, which is a record showing proposed prices for products and services. Available in API version 18.0 and later.

### Quotes can be created from and synced with opportunities, and emailed as PDFs to customers

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

AdditionalAddress

AdditionalCity

AdditionalCountry

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account that’s associated with the quote.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the additional address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's additional address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's additional address. Up to 80 characters allowed.


Standard Objects Quote

**Field** **Details**

```
AdditionalCountryCode

AdditionalLatitude

AdditionalLongitude

AdditionalName

AdditionalPostalCode

AdditionalState

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s additional address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `AdditionalLongitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `AdditionalLatitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –180 and 180
with up to 15 decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name associated with the quote's additional address. Limited: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's additional address.

**Type**
string


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's additional address. Up to 80 characters allowed.

```
AdditionalStateCode

AdditionalStreet

BillToContactId

BillingAddress

BillingCity

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s additional address.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Street name for the quote's additional address.

**Type**
reference

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
ID of the contact that the order is billed to. This field is available in API version
56.0 and later. This field is available with Subscription Management.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the billing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's billing address. Up to 40 characters allowed.


Standard Objects Quote

**Field** **Details**

```
BillingCountry

BillingCountryCode

BillingLatitude

BillingLongitude

BillingName

BillingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's billing address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a
billing address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Entity that the quote is billed to.

**Type**
string


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's billing address.

```
BillingState

BillingStateCode

BillingStreet

CalculationStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's billing address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the quote's billing address.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Price calculations are performed by Salesforce. Tax calculations are performed
by a third-party tax provider integration with Salesforce. Both of these
calculations are asynchronous, and you can use this field to see the status of
the asynchronous processes.

This field is available with Subscription Management or Revenue Cloud.

Possible values are:

**•** `CompletedWithPricing` —Indicates that pricing is complete and
tax will now be calculated.

**•** `CompletedWithTax` —Indicates that pricing and tax calculation are
complete.


Standard Objects Quote

**Field** **Details**

**•** `CompletedWithoutPricing` —Indicates that pricing and tax
calculation were skipped.

**•** `ConfigurationFailed` —Indicates that configuration failed. Available
in API version 62.0

**•** `ConfigurationInProgress` —Indicates that the configuration is
in progress. Available in API version 62.0

**•** `GroupRampConfigurationFailed` —Indicates that the checks for
group ramps have failed. Available in API version 65.0 and later.

**•** `NotStarted`

**•** `PriceCalculationFailed` —Indicates that pricing failed. Available
in API version 58.0 and later.

**•** `PriceCalculationInProgress` —Available in API version 58.0
and later.

**•** `PriceCalculationQueued` —The request is sent to the asynchronous
price calculation process, but the process hasn’t started. Available in API
version 58.0 and later.

**•** `QuoteRequestFailed` —Indicates that the requested quote changes
weren’t saved. Available in API version 62.0

**•** `QuoteRequestPartiallySaved` —Indicates that the requested
quote changes were partially saved. Available in API version 62.0

**•** `ReconciliationFailed` —Indicates that the arrangement of quote
data failed. Available in API version 62.0

**•** `ReconciliationInProgress` —Indicates that the arrangement of
data is in progress. For a sales rep, this value appears as `Saving` on the
quote page. Available in API version 62.0

**•** `SaveFailedOrIncomplete` —Some or all of the records couldn’t be
saved. For example, some of the quote line item records weren’t saved.
Available in API version 58.0 and later.

**•** `Saving`

**•** `TaxCalculationFailed`

**•** `TaxCalculationInProcess`

**•** `TaxCalculationSuccess` —Available in API versions 56.0 and 57.0

**•** `TaxCalculationWaiting`

The default value is `NotStarted` .

```
CanCreateQuoteLineItems

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
This field isn’t used.


Standard Objects Quote

**Field** **Details**

```
ContactId

ContractId

CurrencyIsoCode

Description

Discount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact that’s associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract that’s associated with the quote.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

If the organization has multicurrency and a `Pricebook2Id` specified on the
quote, then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

This value is copied from the related Opportunity and can't be changed.

**Type**
textarea

**Properties**
Nillable

**Description**
Text description of the quote. Limit: 32,000 characters.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The difference between the QuoteLineItem record’s subtotal and its discounted
total, divided by the QuoteLineItem’s subtotal. Expressed as a percentage.


Standard Objects Quote

**Field** **Details**

```
Email

ExpirationDate

Fax

GrandTotal

IsSyncing

```

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the contact who’s associated with the quote.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The date when this quote is no longer valid.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The fax number for the contact who’s associated with the quote.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total price of the quote plus shipping and taxes.

Note:

The `GrandTotal` is a system-calculated summary field and is not directly
referenceable or usable in custom formula fields on the Quote object. Attempts
to do so result in an error message. For example, "Error: Field GrandTotal does
not exist. Check spelling." To perform calculations based on the total value of
a quote, consider using a **Roll-Up Summary** field from related Quote Line Items
or performing calculations directly on the QuoteLineItem on page 4564 object.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the quote is syncing with an opportunity.


Standard Objects Quote

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LineItemCount

Name

OpportunityId

Phone

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view but not
viewed it directly.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The number of line items on the quote.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
Required. Name for the quote. Limit: 225 characters.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID for the opportunity associated with the quote.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update


Standard Objects Quote

**Field** **Details**

**Description**
The phone number of the contact who’s associated with the quote.

```
Pricebook2Id

QuoteAccountId

QuoteNumber

QuoteToAddress

QuoteToCity

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the price book associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with the quote. This field is available in API version
58.0 and later only when the **Create Quotes Without a Related Opportunity**
setting on the Quotes Settings page is enabled.

This field is a relationship field.

**Relationship Name**
QuoteAccount

**Refers To**
Account

**Type**
string

**Properties**
Defaulted on create, Filter

**Description**
A system-generated number that identifies the quote.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the quote to address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the address to send the quote to for approval, such as a third
party-agency representing a buyer. Up to 40 characters allowed.

```
QuoteToCountry

QuoteToLatitude

QuoteToLongitude

QuoteToName

QuoteToPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the address to send the quote to for approval. Up to 80 characters
allowed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `QuoteToLongitude` to specify the precise geolocation of a
quote to address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `QuoteToLatitude` to specify the precise geolocation of a quote
to address. Acceptable values are numbers between –180 and 180 with up to
15 decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval. Limit: 255 characters.

**Type**
string


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address to send the quote to for approval.

```
QuoteToState

QuoteToStreet

RecordSource

RecordTypeID

RelatedWorkId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the address to send the quote to for approval. Up to 80 characters
allowed.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the address to send the quote to for approval.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the source application context for the record.

This field is available with Digital Insurance in API version 66.0 and later.

Possible values are:

**•** `DigitalInsurance`

**•** `Null`

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to the object.

**Type**
reference


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Relationship field that’s visible only if Field Service and Quotes are enabled in
the Salesforce org. This field refers to the work order that the quote is created
from. When a mobile worker creates a quote using the New Quote action in
the Field Service mobile app, this field is automatically populated. This field is
used in the related list that shows all of the quotes related to the work order.

```
ShippingAddress

ShippingCity

ShippingCountry

ShippingCountryCode

ShippingHandling

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the shipping address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's shipping address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's shipping address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s shipping address.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update


Standard Objects Quote

**Field** **Details**

**Description**
The total shipping and handling costs for the quote.

```
ShippingLatitude

ShippingLongitude

ShippingName

ShippingPostalCode

ShippingState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a
shipping address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the quote's shipping address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's shipping address. Up to 80 characters allowed.


Standard Objects Quote

**Field** **Details**

```
ShippingStateCode

ShippingStreet

Status

Subtotal

Tax

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the quote's shipping address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**

The status of the quote. The standard options are:

**•** —None—

**•** Draft

**•** Needs Review

**•** In Review

**•** Approved

**•** Rejected

**•** Presented

**•** Accepted

**•** Denied

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The sum of sales price multiplied by quantity for line items, not including the
discount.

**Type**
currency


Standard Objects Quote

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
The total taxes for the quote.

```
TotalPrice

TotalPriceWithTax

TotalTaxAmount

```

Usage

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total of the quote line items after discounts and before taxes and shipping.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalPrice` and `TotalTaxAmount` . This field is available in
API version 55.0 and later. This field is available if Subscription Management is
enabled in your org.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all taxes. This field is available in API version 55.0 and later.
This field is available if Subscription Management is enabled in your org.

This field is a calculated field.

Use Quote to manage proposed product prices for customers. To update a Quote, your client application needs “Edit” permission.

**•** Client applications can create, update, delete, and query Attachment records associated with a quote via the API.

**•** You can sync a quote and its parent Opportunity.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects QuoteAction

**QuoteChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteFeed (API version 39.0)**
Feed tracking is available for the object.

**QuoteHistory (API version 57.0)**
History is available for tracked fields of the object.

**QuoteOwnerSharingRule (API version 41.0)**
Sharing rules are available for the object.

**QuoteShare (API version 41.0)**
Sharing is available for the object.

SEE ALSO:

QuoteLineItem

QuoteDocument

Opportunity

### QuoteAction

Indicates the type of sales transaction that’s being quoted; for example, a renewal sale. This object is available in API version 59.0 and
later.

If a quote doesn't have a quote action, Salesforce treats it as a quote of the `Add` type. When such a quote is used to create an order,
Salesforce automatically creates an order action of the `Add` type.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in orgs with Revenue Cloud. It’s also available in Industries Automotive and Industries Field Service.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects QuoteAction

**Field** **Details**

**Description**
ISO code of the currency. Use only one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` . Must be unique within your
organization. Label is **Currency ISO Code** .

The default value is `USD` .

[See Supported Currencies (ICU) for a list of currency codes Salesforce supports. This field is](https://help.salesforce.com/s/articleView?id=xcloud.admin_supported_currencies.htm&type=5&language=en_US)
available in Revenue Cloud in API version 66.0 and later.

```
LastReferencedDate

LastViewedDate

Name

QuoteId

```

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
the user accessed this record or list view indirectly, but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name given to the quote action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote related to this quote action.

This field is a relationship field.

**Relationship Name**
Quote


Standard Objects QuoteAction

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Quote

```
SourceAssetId

Subtype

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset changed by this sales transaction. For example, if the quote action is a quantity
amendment, this field contains the ID of the asset that’s amended.

This field is a relationship field.

**Relationship Name**
SourceAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The subtype of the action on the quote line item.

Valid values are:

**•** `DowngradeFrom` —Available in API version 66.0 and later.

**•** `DowngradeTo` —Available in API version 66.0 and later.

**•** `FieldAmendment`

**•** `Rollback`

**•** `StartDateAdjustment`

**•** `SwapIn` —Available in API version 66.0 and later.

**•** `SwapOut` —Available in API version 66.0 and later.

**•** `TransferFrom`

**•** `TransferTo`

**•** `UpgradeFrom` —Available in API version 66.0 and later.

**•** `UpgradeTo` —Available in API version 66.0 and later.

This field is available with Revenue Cloud in API version 64.0 and later.


### Standard Objects QuoteAdjustmentGroup

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of sales transaction that the related quote is for.

Valid values are:

**•** `Add`

**•** `Amend`

**•** `Association` —Available in API version 66.0 and later.

**•** `Cancel`

**•** `No Change`

**•** `Renew`

**•** `Transfer` —Available with Revenue Cloud in API version 65.0 and later.

### QuoteAdjustmentGroup

Group containing a set of adjustments applied to a quote. This object is available in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.

Fields

**Field** **Details**

```
AdjustmentSource

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the origin of the price adjustment.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually; for example, by a sales rep.


Standard Objects QuoteAdjustmentGroup

**Field** **Details**

**•** `Promotion` —The adjustment is part of a promotion; for example, a holiday sale
discount.

**•** `Rule` —The adjustment is due to a price rule.

**•** `System` —The adjustment originates from the system, for example, a volume discount.

```
AdjustmentType

AdjustmentValue

Description

Name

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of mathematical adjustment to be applied to the quote.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override. Available in API
version 59.0 and later.

**Type**
double

**Properties**
Filter, Sort

**Description**
The specified `AdjustmentType` amount that is applied to the quote. For example, when
`AdjustmentType` is `AdjustmentAmount`, `AdjustmentValue` is the cash
amount of the price adjustment. When `AdjustmentType` value is
`AdjustmentPercentage`, `AdjustmentValue` is the percent value of the price
adjustment. When `AdjustmentType` is `OverrideAmount`, `AdjustmentValue`
overrides the total amount of the quote.

**Type**
textarea

**Properties**
Nillable

**Description**
User-entered information about the quote adjustment group.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects QuoteAdjustmentGroup

**Field** **Details**

**Description**
The user-defined name of the quote adjustment group.

```
Priority

QuoteId

TotalAmount

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A numeric value that represents the order of precedence of the quote adjustment group. It
can also represent the order of precedence when applying the `AdjustmentType` values.

For example, a quote can have two adjustments: a $100 discount and a 10% discount. This
field indicates which adjustment to apply first.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote related to the adjustments in this group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total of all quote adjustments in this quote adjustment group, excluding tax.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteAdjustmentGroupChangeEvent on page 68**
Change events are available for the object.


### Standard Objects QuoteDocument

**QuoteAdjustmentGroupFeed on page 55**
Feed tracking is available for the object.

**QuoteAdjustmentGroupHistory on page 63**
History is available for tracked fields of the object.

**QuoteAdjustmentGroupOwnerSharingRule on page 65**
Sharing rules are available for the object.

**QuoteAdjustmentGroupShare on page 67**
Sharing is available for the object.

### QuoteDocument

Represents a quote in document format. Available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContentVersionDocumentId

CurrencyIsoCode

Discount

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID for the document’s version.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist

**Description**
Available only for organizations with the multicurrency feature enabled.

Contains the ISO code for any currency allowed by the organization. If the
organization has multicurrency and a `Pricebook2Id` specified on the quote,
then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

**Type**
percent


Standard Objects QuoteDocument

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The discount for the quote used in the document.

```
Document

DocumentTemplate

GrandTotal

Name

QuoteId

Status

```

**Type**
base64

**Properties**
Create, Nillable

**Description**
The binary data of the document stored in the QuoteDocument object.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the template used to generate the document.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Grand total for the quote used in the document.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Name of the quote document.

**Type**
reference

**Properties**
Create, Filter, GroupSort

**Description**
ID for the quote used for the document.

**Type**
picklist


### Standard Objects QuoteLineGroup

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the document.

Possible values are:

**•** `Completed`

**•** `Failed`

**•** `Generating`

**•** `In Progress`

**•** `None`

**•** `Queued`

The default value is `None` .

Usage

Use the QuoteDocument object to store a document that can be used to present the quote information to the customer.

SEE ALSO:

### Quote

QuoteLineItem

### QuoteLineGroup

Stores the group information for line items in a quote. It also stores the aggregated line field information (subtotal). It contains a
parent-child relationship to quote. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
Description

```

**Type**
string


Standard Objects QuoteLineGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the group.

```
EndDate

Name

QuoteId

SortOrder

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user.


### Standard Objects QuoteLineItem

**Field** **Details**

```
StartDate

SummarySubtotal

Type

### QuoteLineItem

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total amount of all the line items in the group.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the group.

Possible values are:

**•** `CPQQuoteGroup` —CPQ Line Grouping

The default value is `CPQQuoteGroup` .

Represents a quote line item, which is a member of the list of Product2 products associated with a quote, along with other information
about those line items on that quote. Available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The user must have “Edit” permissions on quote records to create or update quote line items on a quote. The user must have “Edit”
permissions on quote records to delete a quote line item.

Some of the fields are available when you turn on Subscription Management.


Standard Objects QuoteLineItem

Fields

**Field** **Details**

```
BatchIdentifier

BillingFrequency

BillingReference

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier for a product bundle in a transaction processing batch. This value makes sure that
quote lines from the same bundles process together.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period that indicates how often the quote line item is billed. This field is available
in API version 55.0 and later. This field is available when Subscription Management is enabled.

Possible values are:

**•** `Annual`

**•** `Monthly`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reference to the original quote for which this quote line item is created. This field is available
in API version 61.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Available only for organizations enabled for multiple currencies. Contains the ISO code for
any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 specified on the quote (the
`Pricebook2Id` field isn’t blank), then the currency value of this field must match the
currency of the PricebookEntry objects for any associated quote line items.

This value comes from the related quote and can't be changed.


Standard Objects QuoteLineItem

**Field** **Details**

```
CustomProductName

Description

Discount

DiscountAmount

DoesAutomaticallyRenew

Division

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Custom product name for the quote line item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the line item. Limit: 225 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional discount percentage, specified by the sales representative at the line level.
Editable number from 0 to 100.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The fixed amount discount to apply to the quote line item. Available in API version 59.0 and
later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the quote line item is set to automatically renew (True) or not (False).

The default value is `false` .

**Type**
picklist


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

```
EffectiveGrantDate

EndDate

EndDateTime

EndQuantity

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the resources associated with the quote line item are granted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription ends. This field is available in API version 55.0 and later. This field is available if
Subscription Management is enabled in your org.

You can indicate a subscription’s length by using either `StartDate` and `EndDate`, or
by using `StartDate` and `SubscriptionTerm` . If you provide a value for both
`EndDate` and `SubscriptionTerm`, `EndDate` is used to determine the subscription’s
length.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time of the quote line item, which is derived from the End Date and End
Time fields in the time zone specified in the Start and End Time Zone field. If the time zone
isn't specified, the default is Coordinated Universal Time (UTC).

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
If the quote line item is sold on a subscription, this field indicates the end quantity when
the subscription ends. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

```
EndTime

HasQuantitySchedule

HasRevenueSchedule

HasSchedule

IsPrimarySegment

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end time of the quote line item.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a quantity schedule.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a revenue schedule. If this object has a revenue schedule, the `GrandTotal` and
`TotalPrice` fields can't be updated. In addition, the `Quantity` field can't be updated
if this object has a quantity schedule. The system ignores any attempt to update this field.
The update isn't rejected but the updated value is ignored.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the line item uses schedules.

**Type**
boolean


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the segment for the quote line item is a primary segment (true) or not
(false).

The default value is `false` .

```
LastReferencedDate

LastViewedDate

LegalEntityId

LineNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user only accessed this record or list view ( `LastReferencedDate` ) but not viewed
it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the legal entity record associated with the quote line item.

This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
Read-only. An automatically generated number identifying the quote line item. In the form
of `QL-XXXXX` .

```
ListPrice

ListPriceTotal

Margin

MarginAmount

NetTotalPrice

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Corresponds to the `UnitPrice` on the PricebookEntry that is associated with
this line item, which can be in the standard price book or a custom price book. A client app
can use this information to show whether the unit price (or sales price) of the line item differs
from the price book entry list price.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The `ListPrice` times the `Quantity` . This field is a calculated field.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional margin percentage, specified by the sales representative at the line item level.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The optional margin amount, specified by the sales representative at the line item level.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This field is a calculated field equal to `TotalAdjustmentAmount` plus
`TotalLineAmount` .

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

```
NetUnitPrice

OpportunityLineItemId

ParentQuoteLineItemId

PartnerDiscountPercent

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The unit price after all price adjustments are applied.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the related opportunity line item. This field is populated by the API during creation of
the quote line item. Not editable. Available in API version 40.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the related line item in the parent quote.

This field is populated by the API during creation of the quote line item.

This field is available in version 58.0 and later. This field is available when Subscription
Management is enabled.

This field is a relationship field.

**Relationship Name**
ParentQuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
percent


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The partner’s discount percent applied to the quote lines. Available in API version 59.0 and
later.

```
PartnerUnitPrice

PeriodBoundary

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price after applying the discount given to the partner for the quote line item.
Available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period boundary helps determine the start and end date of the billing periods.

This field is available in API version 55.0 and later. This field is available with Subscription
Management and Revenue Cloud.

Possible values are:

**•** `AlignToCalendar` —the period starts on the first day of the term unit; for example,
the first day of the month.

**•** `Anniversary` —The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod` —the period starts on the day indicated by `PeriodBoundaryDay` .

**•** `LastDayOfPeriod` —the period starts on the last day of the pricing term unit.

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** For termed selling models where the `PeriodBoundary` value is `Anniversary`,
the value of the `PeriodBoundary` field is automatically converted to
`DayOfPeriod` .

**•** Start date adjustment operation on an asset preserves the original value without
conversion.


Standard Objects QuoteLineItem

**Field** **Details**

```
PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when `PeriodBoundary` is `DayOfPeriod` . Indicates day of the week or
month that marks the period boundary. Must be an integer from 1 through 31.

This field is available in API version 55.0 and later. This field is available with Subscription
Management and Revenue Cloud.

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** When `PeriodBoundary` field value is converted from `Anniversary` to
`DayOfPeriod` for termed selling models, the value of the `PeriodBoundaryDay`
field is automatically populated with the day value from AssetActionSource.StartDate.

**•** Start date adjustment operation on an asset preserves the original value without
conversion.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
The field is populated based on input in the StartDate, PeriodBoundary, and
PeriodBoundaryDay when BillingFrequency is Annual and PricingTermUnit is Annual or by
manual user entry. Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`

**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`


Standard Objects QuoteLineItem

**Field** **Details**

Keep these considerations in mind for amendment, renewal, and cancellations of assets in
Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the AssetActionSource (initial
sale), by default.

**•** For termed selling models where `PeriodBoundary` field value is `Anniversary`
and `PricingTermUnit` field value is `ANNUAL`, `SEMI_ANNUAL`, or `QUARTERLY`,
the value of the `PeriodBoundaryStartMonth` field is automatically recalculated
by using AssetActionSource.StartDate.month.

**•** Start date adjustment operation on an asset preserves the original value without
conversion.

```
PricebookEntryId

PriceRevisionPolicyId

PricingContractId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated PricebookEntry. Exists only for orgs with Products enabled. In
API 38.0 and earlier, if `Product2Id` is populated with `PricebookEntryId` data,
you receive an error message. In API 39.0 and later, `Product2Id` is nulled, and
`PricebookEntryId` is populated with the `PricebookEntryId` data.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price uplift policy associated with this quote line item.

This field is a relationship field.

**Relationship Name**
PriceRevisionPolicy

**Refers To**
PriceRevisionPolicy

Label is **Price Revision Policy** .

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contract used for pricing that's associated with the quote line item.


Standard Objects QuoteLineItem

**Field** **Details**

This field is a relationship field.

**Relationship Name**
PricingContract

**Refers To**
Contract

```
PriceWaterfallIdentifier

PricingTerm

PricingTermCount

PricingTermUnit

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing
of the detail record. Available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. For example, if a monthly subscription is priced
yearly, this field is 12.

This field is available in API version 55.0 and later. This field is available with Subscription
Management.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of time for the pricing term. This field is available in API version 55.0 and later. This
field is available with Subscription Management.

Possible values are:

**•** `Annual` —Available in API version 58.0 and later. UI label is `Years` .


Standard Objects QuoteLineItem

**Field** **Details**

**•** `Months` .

```
Product2Id

ProductInstanceIdentifier

ProductSellingModelId

ProrationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with this QuoteLineItem. In API 38.0 and earlier, if
`Product2Id` is populated with `PricebookEntryId` data, you receive an error
message. In API 39.0 and later, `Product2Id` is nulled, and `PricebookEntryId` is
populated with the `PricebookEntryId` data.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product instance that’s added to a quote. Each quote line item created for the
same product instance has the same product instance identifier value.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. This field is available in API version 55.0 and later. This
field is available with Subscription Management.


Standard Objects QuoteLineItem

**Field** **Details**

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

```
Quantity

QuantityUnitOfMeasureId

QuoteActionId

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The number of units for the line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unit of measure for the quantity, start quantity, and end quantity.

This field is a relationship field.

**Relationship Name**
QuantityUnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related quote action. This field is available in API version 58.0 and later. This
field is available with Subscription Management and Revenue Lifecycle Management.

This field is a relationship field.

**Relationship Name**
QuoteAction

**Relationship Type**
Lookup

**Refers To**
QuoteAction


Standard Objects QuoteLineItem

**Field** **Details**

```
QuoteId

QuoteLineGroupId

QuoteLineItemRecipientId

RampIdentifier

RelatedQuoteLineItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the quote line group for the quote line item.

This field is a relationship field.

**Relationship Name**
QuoteLineGroup

**Refers To**
QuoteLineGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recipient for the quote line item.

This field is a relationship field.

**Relationship Name**
QuoteLineItemRecipient

**Refers To**
QuoteLineItemRecipient

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp ID used to group quote line item segments.

**Type**
reference


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The quote line item ID related to the order item created.

This field is a relationship field.

**Relationship Name**
RelatedQuoteLineItem

**Refers To**
OrderItem

This field is available in Revenue Cloud in API version 65.0 and later.

```
SegmentIdentifier

SegmentName

SegmentType

SellingModelType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the segment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the quote line item segment.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period for the segment.

Possible values are:

**•** `Custom`

**•** `FreeTrial` —Free Trial

**•** `Yearly`

The default value is `Yearly` .

**Type**
picklist


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the quote line item is sold as a one-time purchase, an evergreen
subscription, or as a termed subscription. This field is available in API version 55.0 and later.
This field is available with Subscription Management.

Possible values are:

**•** `Evergreen`

**•** `OneTime`

**•** `TermDefined`

The default value is `OneTime` .

```
ServiceDate

SortOrder

StartDate

StartDateTime

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the product revenue is recognized and the product quantity is shipped.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of where the line item is in the sorted order such as 1, 2, 3. The SortOrder value
determines the order in which a quote line item appears in the Quote Line Items related list
and the Quote PDF. Client apps can use this value to match the sort order in Salesforce. This
field is only available in API versions 21.0 and greater.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription starts. This field is available in API version 55.0 and later. This field is available
with Subscription Management.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
The start date and time of the quote line item, which is derived from the Start Date and Start
Time fields in the time zone specified in the Start and End Time Zone field. If the time zone
isn't specified, the default is Coordinated Universal Time (UTC).

This field is available in Revenue Cloud in API version 65.0 and later.

```
StartEndTimeZone

StartTime

StartQuantity

StartingPriceTotal

StartingUnitPriceSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone for the quote line item's start and end dates, times, and datetimes.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start time of the quote line item.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
If the quote line item is sold on a subscription, this field indicates the item quantity when
the subscription starts. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The starting unit price times the quantity.

**Type**
picklist


Standard Objects QuoteLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was entered manually or calculated. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

Possible values are:

**•** `Manual`

**•** `System`

**•** `Inherited`

```
Status

SubscriptionTerm

SubscriptionTermUnit

```

**Type**
dynamic picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the quote line item. This field is available in API version 60.0 and
later. The `QuoteLineItemStatus` permission is required to access this field.

Possible values are:

**•** `In Progress`

**•** `Pending`

**•** `Approved`

**•** `Rejected`

Default value is `In Progress` .

**Type**
int

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The number of terms in the subscription.

You can indicate a subscription’s length by using either `StartDate` and `EndDate`, or
by using `StartDate` and `SubscriptionTerm` . If you provide a value for both
`EndDate` and `SubscriptionTerm`, `EndDate` is used and `SubscriptionTerm`
is ignored.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
The unit of time used to define the subscription. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

Possible values are:

**•** `Annual` —UI label is `Years`

**•** `Months`

```
Subtotal

TotalAdjustment

TotalAdjustmentAmount

TotalCost

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The line item's `Quantity` multiplied by the `UnitPrice` . In Revenue Cloud, `Subtotal`
is set to `TotalLineAmount` when `TotalLineAmount` has a value.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The total discount percentage applied at the line item level. This percentage is calculated
by using the formula: (Total Line Amount - Net Total Price) / Total Line Amount.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the adjustments applied to the quote line item, inclusive of quantity, prorated
for the duration of the subscription.

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total cost of all products sold in the quote, calculated by multiplying the quantity by
the unit cost.


Standard Objects QuoteLineItem

**Field** **Details**

This field is available in Revenue Cloud in API version 65.0 and later.

```
TotalLineAmount

TotalMargin

TotalMarginAmount

TotalPrice

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price of the quote line item, before price adjustments, inclusive of quantity, prorated
for the duration of the subscription. This price is a calculated field equal to `ListPrice`
times `Quantity` times `PricingTermCount` .

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The effective margin percentage at the line item level. This percentage is calculated by using
the formula: (Net Total Price - Total Cost) / Net Total Price.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The effective margin amount at the line item level. This amount is calculated by subtracting
total cost from net total price.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Calculated by applying the `Discount` to the `Subtotal` . This field is nillable,
but you can't set both `TotalPrice` and `UnitPrice` to null in the same update. To
insert the `TotalPrice` for a quote line item via the API (given only a unit price and the
quantity), calculate this field as the unit price multiplied by the quantity. This field is read
only if the quote line item has a revenue schedule.


Standard Objects QuoteLineItem

**Field** **Details**

```
UnitCost

UnitPrice

UnitPriceUplift

ValidationResult

Visibility

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit cost of a product sold as part of the quote.

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The price per unit for the quote line item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage increase of the quote line item's unit price.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the quote line item was configured and priced by Revenue Lifecycle
Management.

A quote can be activated only after all its quote line items are configured and priced by
Revenue Lifecycle Management.

Valid values are:

**•** `Warning` —Indicates that the quote line item wasn’t configured and priced by Revenue
Lifecycle Management.

Available in API version 60.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects QuoteLineItem

**Field** **Details**

**Description**
Specifies how Salesforce shows a quote line item in the Transaction Line Editor and a quote
document.

Possible values are:

**•** `Always` —Quote line items are always displayed in the Transaction Line Editor.

**•** `Never` —Quote line items aren't displayed in the Transaction Line Editor or in the quote
document.

**•** `Quote Document Only` —Quote line items are displayed only in the quote
document, but not in the Transaction Line Editor.

**•** `Transaction Line Editor Only` —Quote line items are displayed only in
the Transaction Line Editor, but not in the quote document.

The default value is `Always` .

Usage

A quote record can have QuoteLineItem records only if the quote has a Pricebook2. A QuoteLineItem must correspond to a Product2
that is listed in the quote's Pricebook2.

Note: If the multicurrency option is enabled, the `CurrencyIsoCode` field is present. It can't be modified, it’s always set to
the value of the `CurrencyIsoCode` of the parent quote.

Effects on Quotes

Quotes with related QuoteLineItem objects are affected in the following ways:

**•** Creating a QuoteLineItem increments the quote value by the `TotalPrice` of the QuoteLineItem.

**•** When you create or update a QuoteLineItem, the API verifies that the line item corresponds to a PricebookEntry in the Pricebook2
associated with the quote.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteLineItemHistory (API version 57.0)**
History is available for tracked fields of the object.

SEE ALSO:

Quote

QuoteDocument

Opportunity


### Standard Objects QuoteLineItemRecipient QuoteLineItemRecipient

Represents a site, employee, or other entity for which services are being quoted. This could include details such as the recipient's name,
contact information, associated site or location, and any specific requirements or preferences for the quoted services. This object is
available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BroadbandConnectionType

LastReferencedDate

LastViewedDate

MaxDownloadSpeed

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the broadband connection that's available at the address.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum download speed available at the address.


Standard Objects QuoteLineItemRecipient

**Field** **Details**

```
MaxUploadSpeed

Name

QuoteId

RecipientType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum upload speed available at the address.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the customer's site or location.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the recipient.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of recipient of the service.

Possible values are:

**•** `Location`

**•** `Subscriber`

The default value is `Location` .


Standard Objects QuoteLineItemRecipient

**Field** **Details**

```
ServiceAddrValidationDate

Service Account

ServiceAddrValidationMsg

ServiceAddrValidationResult

ServiceAddress

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the address was validated.

**Type**
entityid

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the Account Entity where the product is used, serviced, or installed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message sent after the validation of the address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the address validation.

Possible values are:

**•** `Fail`

**•** `Partial Success`

**•** `Success`

The default value is `Success` .

**Type**
address

**Properties**
Filter

**Description**
The address where the recipient receives the service.


Standard Objects QuoteLineItemRecipient

**Field** **Details**

```
ServiceCity

ServiceCountry

ServiceGeocodeAccuracy

ServiceLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the recipient receives the service.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the accuracy level of the geocoded address coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip` —Extended Zip

**•** `NearAddress` —Near Address

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the recipient receives the service.


Standard Objects QuoteLineItemRecipient

**Field** **Details**

```
ServiceLongitude

ServicePostalCode

ServiceState

ServiceStreet

ServiceabilityCheckDate

ServiceabilityData

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the recipient receives the service.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street where the recipient receives the service.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the serviceability check was done.

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

**Description**
The information about serviciability, such as broadband connection, download, and upload
speeds available at the address.

```
SiteName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the customer's site or location.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[QuoteLineItemRecipientHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

### QuoteLinePriceAdjustment

Indicates the calculated price adjustment that is applied to the quote line, for example, a calculated volume discount or the prorated
value of a manual discount. Use the quote line price adjustment to inform potential customers about the type, value, and total amount
of their discounts. This object is available in API version 56.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.

Fields

**Field** **Details**

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total` —The adjustment applies to the line item's total and isn’t multiplied by the
quantity. The adjustment amount is prorated for the duration of the subscription.

**•** `Unit` —The adjustment is multiplied by the line item’s quantity, prorated for the duration
of the subscription.

**•** `UnproratedTotal` —The adjustment applies to the line item's total and isn’t
multiplied by the quantity. The adjustment amount isn’t prorated for the duration of the
subscription.

```
AdjustmentSource

AdjustmentType

AdjustmentValue

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The source of the adjustment.

Possible values are:

**•** `Discretionary` —The adjustment is entered manually; for example, by a sales rep.

**•** `Promotion` —Reserved for future use.

**•** `Rule` —The adjustment results from a system rule, such as a price rule or product rule.

**•** `System` —The adjustment is determined by the pricing configuration for the product;
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of adjustment to apply to a quote line.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override. Available in API
version 59.0 and later.

**Type**
double


Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The value of the adjustment. Used together with `AdjustmentAmountScope` to
determine the amount of the adjustment.

```
AppliedPromotionDate

CouponCode

Description

Name

PriceAdjustmentCauseId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time on which the promotion was applied to the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the coupon code that was applied.

**Type**
textarea

**Properties**
Nillable

**Description**
The system-entered description of the quote line price adjustment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-entered name of the quote line price adjustment.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. `Null` if `AdjustmentSource` is
`Discretionary`, indicating a manual adjustment.


Standard Objects QuoteLinePriceAdjustment

**Field** **Details**

For example, if the price adjustment is due to a price adjustment tier, this field contains the
ID of the `PriceAdjustmentTier` record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

```
Priority

QuoteAdjustmentGroupId

QuoteLineItemId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**reference**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the quote adjustment group, which totals all price adjustments for the quote.

This field is a relationship field.

**Relationship Name**
QuoteAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
QuoteAdjustmentGroup

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote line item that this price adjustment applies to.

This field is a relationship field.

**Relationship Name**
QuoteLineItem


### Standard Objects QuoteLineRelationship

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

```
TotalAmount

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total amount of the adjustment that applies to the quote line item, inclusive of quantity,
prorated for the duration of the subscription.

### QuoteLineRelationship

Describes the relationship between quote line items, such as items in a bundle. When you create a QuoteLineRelationship object, it’s
immutable: it can’t be edited or removed. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Subscription Management or Revenue Cloud is enabled.

Fields

**Field** **Details**

```
AssociatedQuantScaleMethod

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How to scale the quantity of the associated quote line, relative to the main quote line. If this
field has a non-null value, you can't edit the associated quote line's quantity.

Possible values are:

**•** `Constant`  - The associated quote’s line quantity remains the same in relation to the
main quote line’s quantity. For example, the main quote line has a quantity of one and


Standard Objects QuoteLineRelationship

**Field** **Details**

the associated quote line has a quantity of one. If you increase the quantity of the main
quote line to two, the associated quote line’s quantity remains at one.

**•** `Proportional`                   - The associated order’s item quantity increases or decreases based
on the main quote line’s quantity. For example, the main quote line has a quantity of
one and the associated quote line has a quantity of two. If you increase the quantity of
the main quote line to two, the associated quote line’s quantity increases to four.

The default value is `Proportional` .

```
AssociatedQuoteLineId

AssociatedQuoteLinePricing

AssociatedQuoteLineRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle
component.

**Relationship Name**
AssociatedQuoteLine

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the associated quote line item is priced relative to the main quote line item.

Possible values are:

**•** `IncludedInBundlePrice`  - The associated quote line’s cost is $0 because it’s
included in the bundle’s price.

**•** `NotIncludedInBundlePrice`  - The associated quote line has a cost because
it’s not included in the bundle’s price.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Describes the position of the associated quote line item in the relationship.


Standard Objects QuoteLineRelationship

**Field** **Details**

Possible values are:

**•** `BundleComponent` —The associated quote line item is part of a bundle.

**•** `SetComponent` —The associated quote line item is part of a set.

```
IsPriceInclusive

LastReferencedDate

LastViewedDate

MainQuoteLineId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether child products are included in the root bundle price. If set to `true`, the
price of each child product is zero.

The default value is `false` .

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
the user might have only accessed this record or list view ( `LastReferencedDate` ), but
not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the main quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle parent.

**Relationship Name**
MainQuoteLine

**Relationship Type**
Lookup


Standard Objects QuoteLineRelationship

**Field** **Details**

**Refers To**
QuoteLineItem

```
MainQuoteLineRole

Name

ProductRelatedComponentId

ProductRelationshipTypeId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main quote line item in the relationship.

Possible values are:

**•** `Bundle` —The main quote line item is the bundle parent.

**•** `Set` —The main quote line item is the set parent.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the quote line relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the product related component.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent

**Refers To**
ProductRelatedComponent

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of record that describes the relationship between the main and
associated quote lines.

This field is a relationship field.


Standard Objects QuoteLineRelationship

**Field** **Details**

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

```
QuoteId

RootQuoteLineId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the quote to which the main and associated quote lines belong.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The root quote line for the quote line relationship. In a bundle relationship, the root quote
line is the root bundle.

This field is a relationship field.

**Relationship Name**
RootQuoteLine

**Refers To**
QuoteLineItem

This object has the following associated objects.

**QuoteLineRelationshipFeed**

Feed tracking is available for the object.


### Standard Objects QuoteItemTaxItem

**QuoteLineRelationshipHistory**

History is available for tracked fields of the object.

### QuoteItemTaxItem

The tax that is applied to a quote line item. This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available if Subscription Management is enabled in your org.

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

Description

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The tax amount for the quote line item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.

Possible values are:

**•** `BHD` —Bahraini Dinar

**•** `EUR` —Euro

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

The default value is 'USD'.

**Type**
textarea


Standard Objects QuoteItemTaxItem

**Field** **Details**

**Properties**
Nillable

**Description**
User-defined description of the tax. For example, state sales tax or value-added tax (VAT).

```
Name

QuoteLineItemId

Rate

TaxEffectiveDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the tax.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the related quote line item.

This is a relationship field.

**Relationship Name**
QuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
If the tax is a percentage tax, then this field contains the percent value. If the tax is a fixed
amount, then this field is null.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date used to calculate the tax rate.


### Standard Objects QuoteLineWorkSource

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Whether the tax is estimated or calculated by the tax provider.

Possible values are:

**•** `Actual`

**•** `Estimated`

### QuoteLineWorkSource

Represents an association between a quote and work sources, such as assets, quote line items, order products, or work type groups. This
object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

OrderItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Asset

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects QuoteLineWorkSource

**Field** **Details**

**Description**
The order product associated with the quote work source.

This field is a relationship field.

**Relationship Name**
OrderItem

**Refers To**
OrderItem

```
QuoteId

QuoteLineItemId

WorkTypeGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
QuoteLineItem

**Refers To**
QuoteLineItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the work source


### Standard Objects QuoteRecipientGroup

**Field** **Details**

This field is a relationship field.

**Relationship Name**
WorkTypeGroup

**Refers To**
WorkTypeGroup

### QuoteRecipientGroup

Represents a recipient group for which offers or products with the same configuration are being added. This also includes reusing these
groups to add or remove recipients. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActualMemberCount

Description

ExpectedMemberCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The actual number of members in the quote recipient group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the quote recipient group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The expected number of members in the quote recipient group.


Standard Objects QuoteRecipientGroup

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

QuoteId

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the quote recipient group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a quote recipient group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the quote recipient group is active.


### Standard Objects QuoteRecipientGroupMember

**Field** **Details**

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Active` .

### QuoteRecipientGroupMember

Represents a junction between a quote line item recipient and a quote recipient group. This object is available in API version 64.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user viewed this record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the quote recipient group member.


Standard Objects QuoteRecipientGroupMember

**Field** **Details**

```
OwnerId

QuoteLineItemRecipientId

QuoteRecipientGroupId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of a quote recipient group member.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote line item recipient associated with the quote recipient group.

This field is a relationship field.

**Relationship Name**
QuoteLineItemRecipient

**Refers To**
QuoteLineItemRecipient

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote line item recipient group associated with the quote recipient group.

This field is a relationship field.

**Relationship Name**
QuoteRecipientGroup

**Refers To**
QuoteRecipientGroup


### Standard Objects RecentFieldChange RecentFieldChange

Use this virtual object to see how an opportunity has changed in the past seven days. Learn the previous value of a field, who made the
change, and when the change was made. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To use RecentFieldChange, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.

Fields

**Field** **Details**

```
ChangeDate

CurrencyIsoCode

FieldName

```

**Type**
dateTime

**Properties**

**Description**
The date and time that the specified field was changed.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency value. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as USD, GBP, or JPY.

The default value is 'USD'.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the opportunity field that you want the previous value of. Possible values are:

**•** `Amount`

**•** `CloseDate`

**•** `StageName`

**•** `ForecastCategory`


Standard Objects RecentFieldChange

**Field** **Details**

**•** `NextStep`

```
ParentId

PreviousCurrencyValue

PreviousDateOnlyValue

PreviousTextValue

ValueChangedById

```

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity that you want the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Nillable

**Description**
The previous value of a currency field on an opportunity.

**Type**
date

**Properties**
Group, Nillable

**Description**
The previous value of a date field on an opportunity.

**Type**
string

**Properties**
Group, Nillable

**Description**
The previous value of a text field on an opportunity.

**Type**
reference

**Properties**
Group


### Standard Objects RecentlyViewed

**Field** **Details**

**Description**
The ID of the user who changed the specified field's value during the specified time period.

This is a relationship field.

**Relationship Name**
ValueChangedBy

**Relationship Type**
Lookup

**Refers To**
User

Usage

One recentFieldChange record is returned for each field that was changed in the past seven days. The supported fields are Amount,
Close Date, Forecast Category, Next Step, and Stage Name. Only the most recent previous value is returned.

Example: To see the most recent previous amount for an opportunity, use the following query. Replace `006R0000XXXXXXXXXX`
with the ID of the opportunity.

```
      select PreviousTextValue from RecentFieldChange where ParentId = '006R0000003JkHBIA0'

      and FieldName = 'StageName'

```

If the sales rep didn't change the opportunity stage name in the past seven days, no values are returned. If the sales rep changed
the opportunity amount several times in the past seven days, only the most recent previous value is returned.

Example: To see the most recent previous amount, close date, forecast category, next step, and stage name for an opportunity,
use the following query. Replace `006R0000XXXXXXXXXX` with the ID of the opportunity.

```
      select PreviousTextValue, PreviousCurrencyValue, PreviousDateOnlyValue from

      RecentFieldChange where ParentId = '006R0000XXXXXXXXXX' and FieldName IN ('StageName',

      'Amount', 'CloseDate')

```

If the opportunity amount, close date, forecast category, next step, and stage name didn’t change in the past seven days, no values
are returned.

### RecentlyViewed

Represents records or list views that the current user has recently viewed or referenced (by viewing a related record). List views are
available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `update()`


Standard Objects RecentlyViewed

Special Usage Rules

The RecentlyViewed object doesn’t support the Event, Task, Report, KnowledgeArticle, and Article objects.

The RecentlyViewed object supports only certain objects, and supports list views only for those supported objects. Supported objects
have the fields `LastReferencedDate` and `LastViewedDate` .

Note: RecentlyViewed records for users who are members of several communities can’t be retrieved automatically into a map
via Apex. This is because records of a user with different networks can result in duplicate IDs that maps don’t support.

Fields

**Field** **Details**

```
Alias

Email

FirstName

Id

IsActive

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias on the record.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address on the record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name on the record. If the recently viewed record is a user, the value is the user’s
first name.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the recently viewed record or list view.

**Type**
boolean


Standard Objects RecentlyViewed

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the recently viewed record is an active user ( `true` ) or not ( `false` ). This
field contains a value only if the recently viewed record is a user.

```
LastName

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name on the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:

**•** Viewing or opening a record.

**•** Selecting a record in a lookup search or related list search.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name on the recently viewed record or list view. If the recently viewed record is a user,
contact, or lead, the value is a concatenation of the `firstname` and `lastname` field
values.


Standard Objects RecentlyViewed

**Field** **Details**

```
NetworkId

Phone

ProfileId

Title

Type

```

**Type**
reference

**Properties**
Filter,Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can add a `NetworkId` only when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 27.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number on the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the user’s profile ID.

This field is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the title of the user; for example CFO or
CEO.

**Type**
picklist


Standard Objects RecentlyViewed

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object type for this recently viewed record or list view. Valid values include any standard
or custom objects that RecentlyViewed supports.

```
UserRoleId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user role associated with this object.

This field is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

This object provides a heterogeneous list of different object types. The list consists of recently viewed records, records that were recently
referenced (a related record was viewed), or recently viewed list views. A record is considered viewed when the user sees the record
details, but not when the user sees the record in a list with other records. Use this object to programmatically construct a list of recently
viewed items specific to the current user. For example, use this object on a custom user interface or for search auto-complete options.
You can also retrieve a filtered list of records by object type ( `Type` ). The RecentlyViewed data is periodically truncated down to 200
records and 200 list views. RecentlyViewed data is retained for 90 days, after which it’s removed on a periodic basis.

Use this query in your code to retrieve a list of all the records and list views that were recently viewed. The results are ordered from most
to least recent.

```
SELECT Id, Name

FROM RecentlyViewed

WHERE LastViewedDate !=null

ORDER BY LastViewedDate DESC

```

Use this query to retrieve data that was either viewed or referenced, but only for a limited set of objects.

```
SELECT Id, Name

FROM RecentlyViewed

WHERE Type IN ('Account', 'Contact', 'Plan__c')

ORDER BY LastViewedDate DESC

```


### Standard Objects Recommendation

This query retrieves a list of all recently viewed contacts with contact-specific fields, such as the contact’s account name, and the custom
website field. Records are ordered from most to least recent.

```
   SELECT Account.Name, Title, Email, Phone, Website__c

   FROM Contact

   WHERE LastViewedDate != NULL

   ORDER BY LastViewedDate DESC

### Recommendation

```

Represents the recommendations surfaced as offers and actions for Einstein Next Best Action. This object is available in API version 45.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

You must have the Modify All Data or Manage Next Best Action Recommendations user permission to create and edit recommendations.

Fields

**Field** **Details**

```
AcceptanceLabel

ActionReference

Description

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label that appears as the accept option on the surfaced recommendation. Maximum size is
80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Flow referenced for this recommendation. Label is **Action** .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects Recommendation

**Field** **Details**

**Description**
Text description of the recommendation. Maximum size is 255 characters.

```
ExternalId

ImageId

IsActionActive

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores an identifier for the recommendation source, such as product, so Einstein can group
all responses for a given recommendation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Image referenced by this recommendation. Label is **Image** .

This is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow referenced in the Action field is active (true) or not (false). Read
only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last referenced.


Standard Objects Recommendation

**Field** **Details**

```
LastViewedDate

Name

NetworkId

RecommendationKey

RejectionLabel

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recommendation. Maximum size is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Track responses to a recommendation when it doesn’t have an ID. Maximum size is 255
characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label that appears as the reject option on the surfaced recommendation. Maximum size is
80 characters.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects RecommendationResponse

**RecommendationChangeEvent (API version 48.0)**
Change events are available for the object.

### RecommendationResponse

Represents the user responses to a presented offer or recommendation for Einstein Next Best Action. This object is available in API version
51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated() query()`, `retrieve()`,

Special Access Rules

You must have one of these user permissions to read, delete, or update recommendation responses:

**•** Modify All Data

**•** Manage Next Best Action Recommendations

**•** Manage Next Best Action Strategies

Fields

**Field** **Details**

```
ActionReference

ContextRecord

ContextRecordName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The full name of an action flow at the time of the response. The full name includes the action’s
namespace.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of context record that contains the Einstein Next Best Action component. For example,
if the Einstein Next Best Action component is on a case record the ContextRecord is the ID
of the case record.

**Type**
string


Standard Objects RecommendationResponse

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the context record.

```
ContextRecordType

NetworkId

OnBehalfOf

OnBehalfOfName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the ContextRecord field.
For example, Account, Case, or Contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable). This is
a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The user ID or record that is indirectly reacting to the recommendation.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the value stored for `OnBehalfOf` at time of response.


Standard Objects RecommendationResponse

**Field** **Details**

```
OnBehalfOfType

RecommendationKey

RecommendationName

RecommendationType

Response

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the OnBehalfOf field. For
example, Account, Case, or Contact.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
RecommendationId if available, otherwise a generated string that represents the
recommendation name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Name of the recommendation returned from the recommendation strategy.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Object type of the recommendation. It can be Recommendation or any object type mapped
to the Recommendation object. For example, if you map Product to Recommendation, the
RecommendationType is Product.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The user’s response to the recommendation.

Possible values are:

**•** `Accepted`

**•** `Rejected`


### Standard Objects RecordAction

**Field** **Details**

```
StrategyReference

StrategyVersion

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The full name of a recommendation strategy flow at the time of the response. The response
is formatted as `namespace` underscore `prefix` double underscore `flowname`, such
as `namespace_prefix__flowname` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The recommendation strategy version that’s active at the time of the response.

The RecommendationResponse object can’t be customized with additional fields.

### RecordAction

Represents a relationship between a record and an action, such as a flow. Create a RecordAction for every action that you want to
associate with a particular record. Available in API version 42.0 and later.

Note: Access to the RecordAction object is determined by a user’s access to the associated parent record.

Supported Calls

`create()`, `delete()`,, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.


Standard Objects RecordAction

Fields

**Field** **Details**

```
ActionDefinition

ActionType

FlowDefinition

FlowInterviewId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required in Lightning Flow for Service implementations that use version 44.0 or later of the
API. The API name of the action to associate with the record; for example, the API name of
a flow. Use this field rather than FlowDefinition. To distinguish a quick action from a flow
with the same API name, we prepend "QuickAction" to the API name of every quick action.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required in Lightning Flow for Service implementations that use version 46.0 or later of the
API. The type of action. Possible values are:

**•** `Flow` (default)

**•** `QuickAction`

For versions of the API prior to version 46.0, this field is set to Flow.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional in Lightning Flow for Service implementations using version 42.0 or 43.0 of the API.
An upgrade to Winter '19 or later, which uses API version 44.0 or later, copies FlowDefinition
to ActionDefinition. For versions 42.0 and 43.0, this field is the API name of the flow that’s
associated with the record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The flow interview ID of the paused or completed flow. This field can’t be set in
Process Builder.

This is a relationship field.


Standard Objects RecordAction

**Field** **Details**

**Relationship Name**
FlowInterview

**Relationship Type**
Lookup

**Refers To**
FlowInterview

```
IsMandatory

IsUiRemoveHidden

Order

ParticipantRoleId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Optional. Specifies whether the action is mandatory. The default value is false.

Note: At runtime, we show a reminder when the user closes a mandatory flow
without completing it. We don't show the reminder for quick actions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Optional. Specifies whether the ability to remove the action is hidden in the UI. The default
value is false. If true, the UI hides the ability to remove the action. However, actions can still
be deleted using the API.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The order of the action among all actions associated with this record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The participant role that's associated with the record action.

This field is a polymorphic relationship field and is available in API version 58.0 and later.

**Relationship Name**
ParticipantRole


Standard Objects RecordAction

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ParticipantRole

```
Pinned

RecordId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Specifies whether the action is pinned to the top or bottom of the component. If
an action is pinned, users see the Remove option in the UI unless `IsUiRemoveHidden`
is set to true. Possible values are:

**•** None (default)

**•** Top

**•** Bottom

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Record associated with the action. In version 46.0 and above, we support most
[object types. To learn about supported objects, see the Lightning Flow for Service Developer’s](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/guided_engagement_support.htm)
[Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/guided_engagement_support.htm)

This is a relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssetRelationship, AssignedResource, AssociatedLocation, Campaign,
CampaignMember, CarePreauth, CarePreauthItem, Case, ChangeRequest, CollaborationGroup,
Contact, ContactRequest, Contract, CoverageBenefit, CoverageBenefitItem,
EnhancedLetterhead, Incident, Lead, Location, MemberPlan, OperatingHours, Opportunity,
Order, PlanBenefit, PlanBenefitItem, Problem, Pricebook2, PricebookEntry, Product2,
ProductItem, ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, PurchaserPlan, PurchaserPlanAssn,
RebateMemberAggregateItem, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, Shipment, SkillRequirement, SocialPersona,


Standard Objects RecordAction

**Field** **Details**

SocialPost, TimeSlot, User, Visit, VoiceCall, WorkOrder, WorkOrderLineItem, WorkType,
WorkTypeGroup

ChangeRequest, Incident, Problem are available in API version 53.0 and later.

RebateMemberAggregateItem is available in API version 54.0 and later.

```
Status

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The current state of the action. Possible values are:

**•** `New` (default)

**•** `Paused`

**•** `Complete`

**•** `Started`

**•** `Unlinked` —The action was unlinked because the flow was paused and the current
record for the flow interview changed.

Paused and unlinked statuses do not apply to quick actions. This field can’t be set in Process
Builder.

The RecordAction object works with the Actions & Recommendations component in Lightning Experience. Although this junction object
can be used to create relationships between records and actions in Salesforce Classic, those relationships can’t be displayed in Salesforce
Classic.

Note: API version 44.0 added a field, ActionDefinition, so that a RecordAction in future releases can support other types of actions
in addition to flows. API version 44.0 and later maintain the FlowDefinition field to support processes that reference this field in
earlier API versions. Upgrading an org to Winter '19 or later, which uses API version 44.0 or later, copies the FlowDefinition field to
the ActionDefinition field. FlowDefinition will be deprecated in a future release, so use ActionDefinition instead.

When an action is deleted that’s referenced in an ActionDefinition or FlowDefinition, the RecordAction object is deleted. RecordAction
objects are also deleted when the associated parent record is deleted, or when a flow is paused and the current record context has
changed. When an action is completed, the associated RecordAction object is also deleted.

Deleted RecordActions are removed from the list when the page is refreshed.

[For more information about the Actions & Recommendations component and how it works with RecordActions, see the Lightning Flow](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)
[for Service Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)


Standard Objects RecordAction

Java Example

Here’s an example of how to associate flows to a record using the RecordAction object.

```
   public void associateNewCustomerFlowWithAccount(Account a) {

     try {

       RecordAction newRecordAction = new RecordAction();

       newRecordAction.setRecordId(a.getId());

       newRecordAction.setActionDefinition(“New_Customer_Flow”);

       newRecordAction.setOrder(1);

       SaveResult[] results = connection

           .create(new SObject[] { newRecordAction });

     } catch (ConnectionException ce) {

       ce.printStackTrace();

     }

   }

```

Data Model

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects RecordActionHistory **RecordActionHistory**

History is available for tracked fields of the object.

### RecordActionHistory

Represents the lifecycle of a RecordAction as it goes through different states. Available in API version 44.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
ActionDefinitionApiName

ActionDefinitionLabel

ActionType

IsMandatory

```

**Type**
string

**Description**
Required. The API name of the action associated with the record. To distinguish a quick action
from a flow with the same API name, we prepend "QuickAction" to the API name of every
quick action.

**Type**
string

**Description**
Required. The label of the action that took place.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist

**Description**
Required. The type of action associated with the record. Possible values are:

**•** `Flow` (default)

**•** `QuickAction`

**Type**
boolean


Standard Objects RecordActionHistory

**Field** **Details**

**Properties**
Defaulted on create

**Description**
Optional. Specifies whether the action is mandatory. The default value is false.

```
LoggedTime

ParentRecordId

Pinned

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The timestamp when the state change occurred.

**Type**
reference

**Properties**
Filter, Sort

**Description**
Required. The parent record for the associated action.

This is a relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssetRelationship, AssociatedLocation, Case, ChangeRequest,
CollaborationGroup, Contact, ContactRequest, Contract, EnhancedLetterhead, Incident, Lead,
Location, OperatingHours, Opportunity, Order, Pricebook2, PricebookEntry, Problem, Product2,
ProductItem, ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, RebateMemberAggregateItem, ResourceAbsence,
Scorecard, ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shipment, SkillRequirement, SocialPersona, SocialPost, TimeSlot,
User, Visit, VoiceCall, WorkType

ChangeRequest, Incident, Problem are available in API version 53.0 and later.

RebateMemberAggregateItem is available in API version 54.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Nillable, Restricted picklist

**Description**
Optional. Specifies whether the action is pinned to the top or bottom, or unpinned. Possible
values are:


Standard Objects RecordActionHistory

**Field** **Details**

**•** None

**•** Top

**•** Bottom

```
RecordActionId

State

UserId

```

Usage

**Type**
string

**Properties**
Filter, Sort

**Description**
Required. The ID of the RecordAction.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist

**Description**
Required. The state of the action. A state change triggers the logging of a history event.
Possible values are:

**•** `Started` (default)

**•** `Paused`

**•** `Resumed`

**•** `Completed`

**•** `Unlinked` —The action was unlinked because the flow was paused and the current
record for the flow interview changed.

**Type**
reference

**Description**
Required. The user that conducted the action.

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

The RecordActionHistory object represents the lifecycle of an action on a record as it goes through different states.


### Standard Objects RecordsetFilterCriteria

The RecordActionHistory object is a big object. For this reason, when you use synchronous SOQL, SOAP, REST, Bulk, or Apex APIs to read
this object, queries must follow a specific pattern or they fail. Queries must match one of these patterns and use fields in this precise
order when more than one field is used.

**•** ParentRecordId

**•** ParentRecordId, LoggedTime (DESC)

**•** ParentRecordId, LoggedTime (DESC), RecordActionId

For example, this SOQL query follows the ParentRecordId, LoggedTime (DESC) pattern.

```
   SELECT ActionDefinitionApiName, User, State FROM RecordActionHistory WHERE

         ParentRecordId = {CaseId} ORDER BY ParentRecordId, LoggedTime DESC

```

Asynchronous SOQL queries do not need to follow a pattern, and can query any field.

Apex triggers cannot reference big object records. Use SOQL queries if you want to query RecordActionHistory records in Apex.

[For more information about the Actions & Recommendations component and how it works with RecordActions, see the Lightning Flow](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)
[for Service Developer Guide. Learn more about big objects and how to query them in the Query Big Objects module on Trailhead.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)

Java Example

Here’s a Java example of how to query a RecordActionHistory object.

```
   public void queryHBPOs(String parentRecordId) {

     try {

      SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");

        // query for the RecordActionHistory associated with ParentRecord

        QueryResult queryResults = connection.query("SELECT ActionDefinitionApiName,

   LoggedTime, State " +

         "FROM RecordActionHistory WHERE ParentRecordId = '" + parentRecordId + "' LIMIT

   50");

        if (queryResults.getSize() > 0) {

         for (int i=0;i<queryResults.getRecords().length;i++) {

          // cast the SObject to a strongly-typed RecordActionHistory

          RecordActionHistory raa = (RecordActionHistory)queryResults.getRecords()[i];

         System.out.println("ActionDefinitionApiName: " + raa.getActionDefinitionApiName()

    + " - LoggedTime: "+ format.format(raa.getLoggedTime().getTime()) + " - State: " +

            raa.getState());

         }

        }

     } catch (Exception e) {

        e.printStackTrace();

     }

     }

### RecordsetFilterCriteria

```

Represents a set of filters that can be used to match service appointments or assets based on your criteria fields. For example, you can
create recordset filter criteria so that only service appointments that satisfy the filter criteria are matched to the filtered shifts, and likewise
only maintenance work rules that satisfy your criteria are matched to assets. This object is available in API version 50.0 and later. Assets
and maintenance work rules are available in API version 52.0 and later.


Standard Objects RecordsetFilterCriteria

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

FilteredObject

IsActive

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the recordset filter criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object used to define the filter criteria. Available in API version 52.0 or later.

Possible values are:

**•** `Asset`

**•** `ServiceAppointment`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the recordset filter criteria is associated with shifts or maintenance work
rules ( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects RecordsetFilterCriteria

**Field** **Details**

**Description**
The date when the recordset filter criteria was last referenced.

```
LastViewedDate

LogicalOperator

Name

OwnerId

SourceObject

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines the logic to evaluate multiple recordset filter criteria rules. Available in API version
53.0 and later.

Possible values are:

**•** `AND`

**•** `OR`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the recordset filter criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects RecordsetFilterCriteria

**Field** **Details**

**Description**
The source object that the filtered criteria are applied to. Shifts and maintenance work rules
are available in API version 52.0 and later. Appointment bundle objects are available in API
version 53.0 and later.

Possible values are:

**•** `ApptBundleAggrPolicy` —Appointment Bundle Aggregation Policy

**•** `ApptBundleConfig` —Appointment Bundle Config

**•** `Shift`

**•** `ContractLineOutcome`

**•** `MaintenanceWorkRule`

Usage Rate Field

Usage Rate Unit

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS

Let's say an employee is open to working a 9 am to 5 pm shift on a Sunday but only for emergency appointments. In this case, the
`SourceObject` is `Shift` and the `FilteredObject` is `ServiceAppointment` . The service appointments available for
that shift are filtered for emergency appointments using the `RecordsetFilterCriteriaRule` object.

RecordSetFilterCriteria isn’t available for report types.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**RecordsetFilterCriteriaFeed**

Feed tracking is available for the object.


### Standard Objects RecordsetFilterCriteriaRule

**RecordsetFilterCriteriaHistory**

History is available for tracked fields of the object.

**RecordsetFilterCriteriaOwnerSharingRule**

Sharing rules are available for the object.

**RecordsetFilterCriteriaShare**

Sharing is available for the object.

### RecordsetFilterCriteriaRule

Represents a rule using fields from the designated source object to create filters on the filtered, or target, object. RecordsetFilterCriteriaRule
is associated with the RecordsetFilterCriteria object. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
CriteriaField

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The field the filter rule is applied to. Asset fields are available in API version 52.0 and later.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment` . The format is, for
example, `Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` . All standard and
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

**Type**
dateTime


Standard Objects RecordsetFilterCriteriaRule

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last referenced.

```
LastViewedDate

NextOccurence

Operator

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field’s value is compared to the Usage Field to determine if the rule is true.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment` . The format is, for
example, `Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` . All standard and
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The relational operator between `CriteriaField` and `Value` . Available in API version
52.0 or later.

Possible values are:

**•** `Equals` —Default

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`


Standard Objects RecordsetFilterCriteriaRule

**Field** **Details**

```
RecordsetFilterCriteriaId

RecordsetFilterCriteriaRuleNumber

Type

Value

Usage Rate Field

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the RecordsetFilterCriteria record to associate this rule with.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically assigned number of the recordset filter criteria rule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of criteria rule. Possible values are:

**•** `Criteria` —Default

**•** `Usage`

**•** `UsageCounter— Usage(Counter)`

**•** `UsageDuration— Usage(Duration)`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The expected value of `CriteriaField` applied to the filter rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day. Possible
values are derived from the source object’s standard and custom fields. Possible standard
source objects are `Asset` and `ServiceAppointment` . The format is, for example,


### Standard Objects RecordsetFltrCritMonitor

**Field** **Details**

`Asset.PricingSource` or
`ServiceAppointment.GroupAppointmentAccessType` .

```
Usage Rate Unit

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS

If you want to create a filter rule for service appointments with a dispatched status, set `CriteriaField` to
`ServiceAppointment.Status` and `Value` to `Dispatched` . Then add the ID from a RecordsetFilterCriteria record to
`RecordsetFilterCriteriaId` to associate this rule with a filter criteria for shifts.

### RecordsetFltrCritMonitor

Monitors whether the value of an asset attribute is within the threshold of a recordset filter criteria (RFC). You can monitor one or more
RFCs for an Asset. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects RecordsetFltrCritMonitor

**Field** **Details**

**Description**
The ID of the asset to link the RFC to.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

```
Description

IsWithinThreshold

Name

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the RFC associated with the recordset filter criteria monitor.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the value of the asset attribute is within the threshold of the RFC.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria monitor.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last referenced.

**Type**
dateTime


### Standard Objects RecordType

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last viewed.

```
RecordsetFilterCriteriaId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the recordset filter criteria.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RecordsetFltrCritMonitorChangeEvent on page 68**
Change events are available for the object.

**RecordsetFltrCritMonitorHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

AttributePicklistValue

### RecordType

Represents a record type.


Standard Objects RecordType

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

Important: Don’t use record types as an access control mechanism. Profile assignment governs create and edit access for an
object but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular record type can't
create records with that record type, but can access records associated with that record type. Users with access to an object can
read all record type information for that object. We strongly recommend against storing sensitive information in the record type
description, name, or label. Instead, store sensitive information in a separate object or fields to which you’ve applied appropriate
access controls.

**Field** **Details**

```
BusinessProcessId

Description

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for Opportunity and Lead record types in API version 17.0 and later. ID of an
associated BusinessProcess.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of this record. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Record Type Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.


Standard Objects RecordType

**Field** **Details**

```
IsActive

IsPersonType

Name

NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Only active record types can
be applied to records. Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this record has been designated as a person account ( `true` ) or not
( `false` ). Visible only if the organization has the person account feature enabled.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Label of the record type in the user interface. Limit: 80 characters. Label is **Record**
**Type Label** .

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


### Standard Objects RecordTypeLocalization

**Field** **Details**

```
 SobjectType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object to which this record type applies, including custom objects.

Use this object to offer different BusinessProcess records and subsets of picklist values to different users based on their Profile. Your client
application can describe or query RecordType records.

Client applications can create or update values in `RecordTypeId` on these objects, specifying a valid record type ID associated with
these objects.

Note: You can’t create or update the `RecordTypeId` field on the CampaignMember records. Set the CampaignMember
record type using the `CampaignMemberRecordTypeId` field on Campaign.

A client application can retrieve the list of valid record type IDs for a given object by querying the RecordType.

### RecordTypeLocalization

Represents the translated value of a label for a record type when the Translation Workbench is enabled for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, Unlimited, or Performance Edition and be enabled for the
Translation Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
Language

```

**Type**
string

**Properties**
Create, Filter, Nillable, Restricted picklist


Standard Objects RecordTypeLocalization

**Field** **Details**

**Description**
The language for this translated label.

```
NamespacePrefix

 ParentId

 Value

```

Usage

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the RecordType associated with the label that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the record type. Label is **Translation** .

Use this object to translate the labels of your record types into other supported languages.


### Standard Objects RecordVisibility (Pilot) RecordVisibility (Pilot)

Represents the visibility attributes that determine a record’s read access. This object is read only and is available in API version 46.0 and
later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you need a CRM Analytics license or to contact Salesforce to participate in the pilot program. You must also have
the “View All Data” or “Enable RecordVisibility API” user permission.

Note: We provide the RecordVisibility object to selected customers through a pilot program that requires agreement to specific
terms and conditions. To be nominated to participate in the program, contact Salesforce. Pilot programs are subject to change,
and we can’t guarantee acceptance. The RecordVisibility object isn’t generally available unless or until Salesforce announces its
general availability in documentation or in press releases or public statements. We can’t guarantee general availability within any
particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features. You
[can provide feedback and suggestions for the RecordVisibility object in the group in the Trailblazer Community.](https://success.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000DN7N)

Fields

**Field Name** **Details**

```
RecordId

VisibilityAttribute

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The ID of the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The visibility attributes that determine the read access of a given record. For
example, a user ID, parent record ID, or group ID.

The output of visibility attributes is in JSON format and must be deserialized.


### Standard Objects RedirectWhitelistUrl

Usage

Use this object to query the attributes that determine the visibility of one or more records. You can’t create, delete, or update any records
using this object.

Up to 200 record IDs can be queried. You can include an `ORDER BY` clause for any field that is being selected in the query.

This sample query returns the visibility attributes for the indicated record.

```
   SELECT RecordId, VisibilityAttribute

   FROM RecordVisibility

   WHERE RecordId=[single ID] // or Record IN [list of IDs]

```

The `RecordId` and `VisibilityAttribute` fields must be a part of the fields that are being selected despite `RecordId`
being used in the filter criteria as well.

RecordVisibility is a foreign key on the records. This query returns the visibility attributes for Account records:

```
   SELECT Id, Name, RecordVisibility.VisibilityAttribute

   FROM Account

```

You can’t filter `RecordId` fields when using RecordVisibility as a lookup or foreign key.

You can use `RecordVisibilityContext` to filter `WITH` clauses in queries. For more information, see `WITH` _[filteringExpression](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_with.htm)_
in the _SOQL and SOSL Reference_ .

### RedirectWhitelistUrl

Represents a trusted URL for external user redirections. Redirections to a different Salesforce org, including its publicly served pages and
content, are allowed from your Salesforce org only when the URL is a RedirectWhitelistUrl. For non-Salesforce URLs, a session setting
controls whether redirections from pages and components built in Salesforce Classic are restricted to RedirectWhitelistUrl objects. Except
for cross-org redirections, you can’t restrict redirections that originate from pages and components built with Lightning Experience. This
object is available in API version 48.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only authenticated internal and external users with the View Setup and Customize Application permissions can access or edit this object.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects RedirectWhitelistUrl

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the custom help section in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. The label corresponds to the section title in the user interface.
Limit: 80 characters.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

```
Language

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the label.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the trusted URL.

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


Standard Objects RedirectWhitelistUrl

**Field** **Details**

field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
 Url

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The trusted URL.

These formats are accepted: `example.com`, `*.example.com`, and
`https://example.com` .

The host section of the URL can include an asterisk ( `*` ) as a wildcard. Otherwise, the URL
cannot be malformed. Examples of malformed URLs that fail a syntax check are
`malformed^url.example.com`, and `https://{subdomain}.example.com` .

To add a URL to a `RedirectWhitelistUrl` based on parameters, build the URL before
you update the `Url` field.

Only redirections are restricted to the URLs in this object. A direct anchor link to an external URL is always allowed, even if that URL isn’t
in the allowlist. An example of a direct anchor link is `<a href="` _**`targetUrl`**_ `">` _**`linkText`**_ `</a>` .

Redirections include parameters that redirect the user and anchor links that include a redirection. For example, this anchor link includes
a redirection: `<a href="/?startURL=` _**`targetUrl`**_ `">` _**`linkText`**_ `</a>` . And this form action redirects the user through the
`saveURL` parameter: `<form action="/xyz?saveURL=` _**`targetURL`**_ `">` .

If the _`targetUrl`_ belongs to another Salesforce org, the redirection is permitted only when the target URL is a RedirectWhitelistUrl.

If the _`targetUrl`_ isn’t a Salesforce org URL, the redirection is checked against the RedirectWhitelistUrl object only when both of these
conditions are met.

**•** The redirection originates from a Salesforce Classic page or component.

**•** Either the `redirectBlockModeEnabled` or `redirectionWarning` [SessionSettings field in the SecuritySettings Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_securitysettings.htm)
API is `true` .

Note: Salesforce verifies the initial redirection outside of Salesforce against the RedirectWhitelistUrl object. However, Salesforce
can’t verify subsequent redirections. For example, if a link on a Visualforce page takes the user to https://www.example.com,
Salesforce verifies that you allowed redirections to https://www.example.com. If that URL then redirects the user to
https://spam.example.com, Salesforce can’t check that redirection, because it occurs outside of Salesforce.

For non-Salesforce URLs, you can choose whether to alert users about untrusted external redirections or to block those redirections
entirely via the `redirectBlockModeEnabled` and `redirectionWarning` fields on the SecuritySettings metadata API type.
These restrictions apply only to redirections from pages and components built in Salesforce Classic.


### Standard Objects Refund

There’s one last special case to cover. For Salesforce org URLs, Salesforce always allows redirections to URLs within the same org, including
redirections from previous My Domain URLs. When the `enableCrossOrgRedirect` field on the SecuritySettings metadata API
type is `false`, Salesforce checks user redirections to other Salesforce orgs via a direct link, a post-action URL, or a post-login URL. If the
URL isn’t a RedirectWhitelistURL, the user isn’t redirected. An example of a direct link is `<a`

`href="https://www.example.com”>example.com</a>` . Post-action URLs and post-login URLs use a protected URL
redirect parameter, such as `retURL`, `startURL`, `saveURL`, `cancelURL`, and `targetURL` .

### Refund

Represents a refund made against a payment. This object is available in API version 48.0 and later.

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
The customer account containing the payment that this refund targets.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of this refund.

```
Balance

CancellationDate

CancellationEffectiveDate

CancellationGatewayDate

CancellationGatewayRefNumber

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Remaining balance following refund line applications. Equal to the Amount field – the Net
Applied field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the refund was canceled. This is a required parameter for void services.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the cancellation of this refund takes effect.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the cancellation transaction was processed in the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique ID for the cancellation transaction. Generated by the payment gateway.


Standard Objects Refund

**Field** **Details**

```
CancellationGatewayResultCode

CancellationSfResultCode

ClientContext

Comments

CurrencyIsoCode

Date

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code for the cancellation transaction. Generated by the payment
gateway. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

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
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
dateTime


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The date and time that this refund was created.

```
EffectiveDate

Email

GatewayDate

GatewayRefNumber

GatewayResultCode

GatewayResultCodeDescription

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Defines the date and time when the refund application becomes effective.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the person who initiated the refund.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that a successful gateway communication caused the creation of this refund.

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
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string


Standard Objects Refund

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the GatewayResultCode. Useful for providing additional context as to why the
gateway returned a specific result code.

```
ImpactAmount

IpAddress

LastReferencedDate

LastViewedDate

MacAddress

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows the refund’s financial impact against the customer’s accounts receivable. If the refund
amount is valid, it equals the Amount field. Equals 0 when the refund amount is void. Has a
null value when the refund is canceled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the person who initiated the payment.

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
record can have been referenced (LastReferencedDate) but not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Refund

**Field** **Details**

**Description**
The MAC address of the person who initiated the refund.

```
NetApplied

OrderPaymentSummaryId

PaymentGatewayId

PaymentGroupId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Equals the Total Applied field minus the Total Unapplied field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summary record that shows the balances of each authorization, capture, and
refund made against an order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment gateway used to process this refund.

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

**Description**
The payment group for the payment being refunded.

This is a relationship field.

**Relationship Name**
PaymentGroup


Standard Objects Refund

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

```
PaymentID

PaymentIntentID

PaymentMethodId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment record.

This field is a relationship field.

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
ID of the payment intent record.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup

**Refers To**
PaymentIntent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method used to create the payment being refunded.

This is a relationship field.


Standard Objects Refund

**Field** **Details**

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

```
Phone

ProcessingMode

RefundNumber

SfResultCode

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the refund.

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
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this refund.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:


Standard Objects Refund

**Field** **Details**

**•** `Decline` : The gateway call failed but the transaction can be attempted again. For
example, the customer had insufficient funds or briefly lost their connection.

**•** `Indeterminate` : The gateway didn’t respond to the call. This response usually
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail` : The gateway call failed and can’t work even if tried again. Gateway
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

```
Status

TotalApplied

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of this refund.

Possible values are:

**•** `Canceled` : This refund has been voided and can no longer be allocated.

**•** `Draft` : The refund can be edited before posting it and allocating it to a target.

**•** `Processed` : This refund has been finalized and can be allocated against a target.

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of Amount fields across all of this refund’s applied refund lines.


### Standard Objects RefundLinePayment

**Field** **Details**

```
TotalUnapplied

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of Amount fields across all of this refund’s unapplied refund lines.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how this refund is used.

Possible values are:

**•** `NonReferenced` : Standalone refund not linked to any payment.

**•** `Referenced` : Refund made against a payment.

### RefundLinePayment

A refund line that has been applied to a payment. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated.

Fields

**Field** **Details**

```
Amount

```

**Type**
currency

**Properties**
Create, Filter, Sort


Standard Objects RefundLinePayment

**Field** **Details**

**Description**
The total amount applied to or unapplied from a payment by the refund line.

```
AppliedDate

AssociatedAccountId

AssociatedRefundLinePaymentId

Comments

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that the refund was applied to the linked payment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The account for the payment that received the refund.

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
The refundLine that was unapplied. Populated only when RefundLinePayment’s Type has a
value of Unapplied.

This is a relationship field.

**Relationship Name**
AssociatedRefundLinePayment

**Relationship Type**
Lookup

**Refers To**
RefundLinePayment

**Type**
textarea


Standard Objects RefundLinePayment

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can add comments to provide additional information on the refund line payment.

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
By default, the day the refund line payment record was created. Users can also enter a different
date.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Defines the date and time when the refund line application or unapplication becomes
effective.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied. If there’s an unapplied line related to this record,
EffectiveImpactAmount has a value of 0.

Note: EffectiveImpactAmount evaluates only the applied and unapplied line pair.
Therefore, the effective impact amount could be different for different lines within
the same refund.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shows whether this refund line has been unapplied.

Possible values are:


Standard Objects RefundLinePayment

**Field** **Details**

**•** `No`

```
ImpactAmount

PaymentBalance

PaymentId

RefundBalance

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The payment record’s balance following the application or unapplication of this refund line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The payment record that this refund line targets. Refund applications and unapplications
are made against this payment.

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The refund record’s balance following the application or unapplication of this payment
refund line.


Standard Objects RefundLinePayment

**Field** **Details**

```
RefundId

RefundLinePaymentNumber

Type

UnappliedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent refund of this refund line.

This is a relationship field.

**Relationship Name**
Refund

**Relationship Type**
Lookup

**Refers To**
Refund

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this refund line.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this line represents a refund that’s been applied or unapplied from a payment.

Possible values are:

**•** `Applied`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this refund line was unapplied from a payment.


### Standard Objects RegisteredExternalService

Usage

When you’re ready to apply a refund’s balance to a payment, create a refund line ( `RefundLinePayment` ). The refund line represents
the balance taken from the payment and applied toward the invoice. You can apply a refund’s balance when you create the refund
record or afterward. The refund line must have the same currency as the parent refund.

A refund has an amount, which represents the total amount taken from the refund, and a balance, which represents the remaining
amount after the refund line has been applied to a payment. A refund’s amount can’t be less than the sum of all of its refund line amounts.
You can apply any portion of a refund’s balance to a payment.

You can apply a refund to transactions on the same account or to different transacations across different

accounts.

### RegisteredExternalService

Represents a registered external service used for checkout integrations by data integrators. This object is available in API version 49.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The RegisteredExternalService object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
ConfigUrl

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to the configuration page for the integration.


Standard Objects RegisteredExternalService

**Field** **Details**

```
Description

DeveloperName

DocumentationUrl

ExtensionPointName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the external service provider.

This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to documentation for the registered external service.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field is available in API version 55.0 and later. Name of an extension point.

Possible values are:

**•** `Commerce_Domain_Cart_Calculate`

**•** `Commerce_Domain_Checkout_CreateOrder`

**•** `Commerce_Domain_Inventory_CartCalculator`

**•** `Commerce_Domain_Inventory_Service`

**•** `Commerce_Domain_OrderManagement_Product`


Standard Objects RegisteredExternalService

**Field** **Details**

**•** `Commerce_Domain_Pricing_CartCalculator`

**•** `Commerce_Domain_Pricing_Service`

**•** `Commerce_Domain_Promotions_CartCalculator`

**•** `Commerce_Domain_Promotions_ShippingCalculator`

**•** `Commerce_Domain_Shipping_CartCalculator`

**•** `Commerce_Domain_Shipping_SplitShipment`

**•** `Commerce_Domain_Tax_CartCalculator`

**•** `Commerce_Domain_Tax_Service`

**•** `Commerce_Endpoint_Account_Address`

**•** `Commerce_Endpoint_Account_Addresses`

**•** `Commerce_Endpoint_Cart_Item` —This field value is available in API version
62.0 and later.

**•** `Commerce_Endpoint_Cart_ItemCollection` —This field value is available
in API version 62.0 and later.

**•** `Commerce_Endpoint_Catalog_Product`

**•** `Commerce_Endpoint_Catalog_Products`

**•** `Commerce_Endpoint_Search_ProductSearch`

**•** `Commerce_Endpoint_Search_Products`

**•** `Commerce_Endpoint_Search_ProductsByCategory`

```
ExternalServiceProviderId

ExternalServiceProviderType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of an Apex class functioning as a provider. The Apex class can either implement one
of the following interfaces:

**•** sfdc_checkout.CartInventoryValidation

**•** sfdc_checkout.CartPriceCalculations

**•** sfdc_checkout.CartShippingCharges

**•** sfdc_checkout.CartTaxCalculations

[or the Apex class can extend one of the base classes for an extension. See Available Extensions.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of external service provider. For an extension, you set the type to `Extension`,
and you specify an `extensionPointName` . For example, for a Pricing Cart Calculator


Standard Objects RegisteredExternalService

**Field** **Details**

extension, you specify `Commerce_Domain_Pricing_CartCalculator` as the
`extensionPointName` . For an integration, you set the type to one of the other possible
values, such as `Price`, and you omit `extensionPointName` .

Possible values are:

**•** `Extension` (this value is available in API version 55.0 and later)

**•** `Inventory`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

```
IconUri

IsApplication

Language

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URI of icon for the extension provider.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the extension provider is contained within a managed package.

The default value is `false` .

This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language for labels displayed
in an application.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish


Standard Objects RegisteredExternalService

**Field** **Details**

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
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The primary label for the registered external service.

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

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


### Standard Objects RelatedListColumnDefinition RelatedListColumnDefinition

Represents information about a column in a related list. A related list specifies a set of records for a related object, based on specific
criteria. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
Alias

ColumnSoql

DataType

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique alias of the column in the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query string used in a SELECT clause for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The field type of the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects RelatedListColumnDefinition

**Field** **Details**

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

```
FieldDefinitionId

IsDefault

IsDescribable

Label

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FieldDefinition associated with the column, if applicable.

This is a relationship field.

**Relationship Name**
FieldDefinition

**Relationship Type**
Lookup

**Refers To**
FieldDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the column appears on the related list by default `(true)` or not
`(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in `describeLayout` call results `(true)`
or not `(false)` .

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects RelatedListDefinition

**Field** **Details**

**Description**
The label for the column.

```
LookupId

### `RelatedListDefinitionId`

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lookup ID for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the RelatedListDefinition that contains the column.

This is a relationship field.

**Relationship Name**
### RelatedListDefinition

**Relationship Type**
Lookup

**Refers To**
### RelatedListDefinition

**Find all available columns on a related list definition.**

```
  SELECT Alias, ColumnSoql, DurableId FROM RelatedListColumnDefinition WHERE

### `RelatedListDefinitionId = 'Account.Opportunities'` RelatedListDefinition

```

Represents information about a related list. A related list specifies a set of records for a related object, based on specific criteria. This
object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects RelatedListDefinition

Special Access Rules

This object is read-only.

Fields

**Field** **Details**

```
DefaultSort

DurableId

EntityDefinitionId

IsCustomizable

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The default sort string for the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the entity containing the related list.

This is a relationship field.

**Relationship Name**
EntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects RelatedListDefinition

**Field** **Details**

**Description**
Indicates whether columns on the related list can be customized `(true)` or not `(false)` .

The default value is `false` .

```
IsDescribable

IsLayoutable

Label

ParentEntityDefinitionId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in `describeLayout` call results `(true)`
or not `(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can be assigned to a layout `(true)` or not `(false)` .

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ParentEntityDefinition that’s associated with the rows in the related list.

This is a relationship field.

**Relationship Name**
ParentEntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition


### Standard Objects RemoteKeyCalloutEvent

**Field** **Details**

```
RelatedListId

RelatedListName

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the related list in the API.

**Find all available related lists for a given entity, for example, an Account record.**

```
  SELECT DurableId, Label, RelatedListName FROM RelatedListDefinition WHERE

  ParentEntityDefinitionId = 'Account'

### RemoteKeyCalloutEvent

```

[The documentation has moved to RemoteKeyCalloutEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_remotekeycalloutevent.htm) _Platform Events Developer Guide_ .

### Reply

Represents a reply that a user has submitted to a question in an answers zone.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Body

```

**Type**
textarea


Standard Objects Reply

**Field** **Details**

**Properties**
Create, Update

**Description**
Body of this reply.

```
CommunityId

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

DownVotes

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the question and its reply. This field is available in API
version 27.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to
view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal
users (agents) appears to portal users in the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
int


Standard Objects Reply

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of down votes for a reply.

```
Name

NumReportAbuses

QuestionId

UpVotes

VoteTotal

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
When creating a Reply, the `Name` field is automatically populated with a truncated,
plain text version of the Reply `Body` field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of reported abuses on the reply by users.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Question to which this reply was made.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for a reply.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of all votes for a reply, including up and down votes.


### Standard Objects ReplyEmailSettings

Usage

Use this object to track replies to a Question.

### ReplyEmailSettings

Represents a reply mail management configuration, which is used to configure emails that are received by an email sending domain.
This object is available in API version 62.0 and later.

When you send an email campaign in Marketing Cloud, you often receive several replies to your messages, including unsubscribe
requests and automatic out-of-office replies. Reply mail management (RMM) reduces the time and effort required to review these
messages, and provide a better experience by automatically handling opt-outs and forwarding messages to the appropriate teams.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutoReplyMessage

DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The content of the reply message. This reply is sent when a message is received at the sending
address.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores


Standard Objects ReplyEmailSettings

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
DomainName

FwdEmailAddress

IsAutoReplyEnabled

IsDeleteAutoRepliesEnabled

IsEmailForwardingEnabled

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The domain that the reply mail management settings apply to. This field is unique within
your organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address to forward a copy of each incoming message to. This value is honored
only if the value of `IsEmailForwardingEnabled` is `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to forward automatic replies, such as out-of-office messages, to the address
specified in the `FwdEmailAddress` field. This value is honored only if the value of
`IsEmailForwardingEnabled` is `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to delete automatic replies, such as out-of-office messages. This value is
honored only if the value of `IsEmailForwardingEnabled` is `true` .

The default value is `false` .

**Type**
boolean


### Standard Objects ReplyReportAbuse

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to forward email replies to the address specified in the
`FwdEmailAddress` field.

The default value is `false` .

```
IsUnsubscribeManualRequestsEnabled

Language

MasterLabel

### ReplyReportAbuse

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether subscribers can opt out of your campaigns by replying to your email with
a keyword such as `unsubscribe` .

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The combined language and locale ISO code, which controls the language of the
ReplyEmailSettings object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this ReplyEmailSettings value. This value is the internal label that doesn’t get
translated.

Represents a user-reported abuse on a Reply in a Chatter Answers zone. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


### Standard Objects ReplyText

Fields

**Field** **Details**

```
Name

Reason

ReplyId

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Reply from which the user reported abuse.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Reply, such as `Spam`, `Hateful`, or
`Inappropriate` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Reply from which the user reported abuse.

Use this object to track user-reported abuse on replies created in a Chatter Answers zone.

### ReplyText

A text reply generated by Einstein Reply Recommendations that is based on closed chat transcripts. Admins review replies and publish
them to quick text, editing them as needed. Einstein recommends relevant published replies to support agents in the Lightning Service
Console, and agents can insert replies into chats or messaging sessions. This object is available in API version 49.0 and later.

Important: Because the replies generated by Einstein are taken from closed chats with your customers, they may contain customer
data. You can edit replies before they are recommended to agents.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
update()

```


Standard Objects ReplyText

Fields

**Field** **Details**

```
Language

Name

RawTextMessage

Source

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language used in the reply. This field is available in API version 51.0 and later. Possible
values are languages supported in Einstein Reply Recommendations.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Eight-digit auto-generated number identifying the reply.

**Type**
textarea

**Properties**

**Description**
The text of the reply.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates who last modified the reply.

Possible values are:

**•** `EINSTEIN_GENERATED` —Reply was generated by Einstein and has not been edited.

**•** `USER_EDITED` —Reply was generated by Einstein and then edited by a user.

**•** `USER_GENERATED` —This value is not currently in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the reply.

Possible values are:


### Standard Objects Report

**Field** **Details**

**•** `NEW` —Einstein has generated the reply and it hasn’t yet been published.

**•** `PUBLISHED` —The reply has been published to quick text. When the reply
recommendation model is activated, the reply can be recommended to support agents.

**•** `PUBLISH_FAILED`                   - An attempt to publish the reply to quick text failed. Publishing
failure can be due to validation errors, access errors, or corrupted files. To hide the reply
from the list of generated replies, delete it.

Usage

To get started with Einstein Reply Recommendations, create a predictive model that analyzes closed chats for frequently used text
snippets. When the model is ready, Einstein generates a list of these snippets as ReplyText records for you to review and publish, or
convert, to quick text. ReplyText records appear on the Einstein Reply Recommendations Setup page.

You can select one or more replies to publish at a time. If you publish a single reply, you can edit the reply text during publishing. If you
publish multiple replies at once, you can edit each reply’s text on the quick text page after publishing is complete. Replies aren’t
recommended to support agents until you activate your reply recommendation model.

When a reply is published, a corresponding QuickText record is created. During publishing, select a quick text folder to add the replies
to and make sure that agents have access to the folder. To edit a reply after it is published, edit the related quick text record.

Einstein generates the list of replies only once, when your model finishes building. It’s not possible to generate a new list.

**Copyright**

Rights of ALBERT EINSTEIN are used with permission of The Hebrew University of Jerusalem. Represented exclusively by Greenlight.

### Report

Represents a report, a set of data that meets certain criteria, displayed in an organized way. Access is read-only. This object is available
in API version 20.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Fields

**Field** **Details**

```
Description

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the report. Limit: 255 characters.


Standard Objects Report

**Field** **Details**

```
DeveloperName

FolderName

Format

IsDeleted

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Report Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the report. Available in API version 35.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Indicates the format of the report. This field is available in API version 29.0 and
later. Can have one of these values:

**•** **Tabular** for reports in that format. In the application, the label is `Tabular` .

**•** **Summary** for reports in that format. In the application, the label is `Summary` .

**•** **Matrix** for reports in that format. In the application, the label is `Matrix` .

**•** **Multiblock** for reports in joined format. In the application, the label is `Joined` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .


Standard Objects Report

**Field** **Details**

```
LastReferencedDate

LastRunDate

LastViewedDate

Name

NamespacePrefix

```

**Type**
datetime

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
Returns the date the report was last run. Label is **Last Run** .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The report label used in the user interface.

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


Standard Objects Report

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

```
OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the folder that contains the report. There are 2 special folders:

**•** Private, where the ID is the user ID

**•** Public, where the ID is the org ID

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

Supported Query Scopes

Use these scopes to help specify the data your SOQL query returns.

**allPrivate**
Records saved in all users’ private folders.

[Requires the user permission "Manage All Private Reports and Dashboards" and Enhanced Analytics Folder Sharing. If your organization](https://help.salesforce.com/HTViewHelpDoc?id=analytics_sharing_enable.htm&language=en_US)
was created after the Summer ’13 release, you already have Enhanced Analytics Folder Sharing. Available in API version 36.0 and
later.

**created**
Records created by the user running the query.

**everything**
All records except records saved in other users’ private folders.

**mine**
Records saved in the private folder of the user running the query.


### Standard Objects ReportEventLog

**organizationOwned**
Records saved in Unfiled Public Reports. In Lightning Experience, the Unfiled Public Reports folder is called Public Reports.

Usage

Use the report object to get report metadata. Query, search, or retrieve specific metadata on reports. Report object fields are read-only.

Example: Reports with “Sales” in Their Name

This SOQL query returns reports that contain the name “Sales” and lists their developer names, format, ID, and report name.

```
   SELECT DeveloperName,Format,Id,Name FROM Report WHERE Name LIKE '%Sales%'

```

Example: Reports in an Inactive User’s Private Folder

This SOQL query returns reports saved in a specific user’s private folder.

```
   SELECT Id FROM Report USING SCOPE allPrivate WHERE OwnerId = ‘005A0000000Bc2deFG’

```

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ReportFeed**

Feed tracking is available for the object.

SEE ALSO:

ReportTag

Dashboard

### ReportEventLog

Report event logs contain information about what happened when a user ran a report. This event type includes all activity that's in the
Report Export event type, and additional information. For example, it has user activity for reports exported as both Formatted Report
and Details Only output. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects ReportEventLog

Fields

**Field** **Details**

```
AverageRowSize

BucketCount

ClientIp

ColumnCount

CpuTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average row size of all rows in the Report event, in bytes. A large average size, coupled
with a high `RowCount`, can indicate that a user is downloading information for fraudulent
purposes. For example, a salesperson who downloads all sales leads before departing for a
competitor. For example: `700` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of buckets that were used in the report.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of columns in the report.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.


Standard Objects ReportEventLog

**Field** **Details**

```
DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

DisplayType

ExceptionFilterCount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how much activity is occurring in the database. A high value for this field suggests
that adding indexes or filters on your queries would benefit performance.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The report display type, indicating the run mode of the report.

Possible values are:

**•** `D` —Dashboard

**•** `S` —Show Details

**•** `H` —Hide Details

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ReportEventLog

**Field** **Details**

**Description**
The number of exception filters that are used in the report.

```
LoginKey

ObjectName

Origin

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object referenced by the report.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context in which the report executed, such as from a UI (Classic, Lightning, Mobile),
through an API (synchronous, asynchronous, Apex), or through a dashboard.

Possible values are:

**•** `ReportOpenedFromMobileDashboard` : Report executed when a user clicked
a dashboard component on a mobile device and drilled down to a report.

**•** `DashboardComponentUpdated` : Report executed when a user refreshed a
dashboard component.

**•** `DashboardComponentPreviewed` : Report executed from a Lightning dashboard
component preview.

**•** `ReportRunUsingSynchronousApi` : Report executed from a synchronous API.

**•** `ReportRunUsingAsynchronousApi` : Report executed from an asynchronous
API.

**•** `ReportRunUsingApexSynchronousApi` : Report executed from the synchronous
Apex API.

**•** `ReportRunUsingApexAsynchronousApi` : Report executed from the
asynchronous Apex API.

**•** `ReportExported` : Report executed from a printable view or report export that was
not asynchronous nor an API export.


Standard Objects ReportEventLog

**Field** **Details**

**•** `ReportRunFromClassic` : Report executed from the Run Report option of Salesforce
Classic.

**•** `ReportRunFromMobile` : Report executed from the Run Report option of the mobile
Salesforce app.

**•** `ReportRunFromLightning` : Report executed from the Run option in Lightning
Experience from a non-mobile browser.

**•** `ReportRunFromRestApi` : Report executed from REST API.

**•** `ReportPreviewed` : Report executed when a user got preview results while using
the report builder.

**•** `ReportScheduled` : Report was scheduled.

**•** `ProbeQuery` : Report executed from a probe query.

**•** `ReportRunFromReportingSnapshot` : Report executed through Snapshot
Analytics.

**•** `ReportExportedAsynchronously` : Report was exported asynchronously.

**•** `ReportExportedUsingExcelConnector` : Report was exported using the
Excel connector.

**•** `ChartRenderedOnVisualforcePage` : Report executed from a rendered chart
on a VisualForce Page.

**•** `ChartRenderedInEmbeddedAnalyticsApp` : Report executed from a rendered
chart in an embedded Analytics app.

**•** `ReportRunAndNotificationSent` : Report executed through the notifications
API.

**•** `ChartRenderedOnHomePage` : Report executed from a rendered chart on the
home page.

**•** `ReportResultsAddedToWaveTrending` : Report executed when a user trended
a report in CRM Analytics.

**•** `ReportAddedToCampaign` : Report was added from an Add to Campaign action.

**•** `ReportResultsAddedToEinsteinDiscovery` : Report executed synchronously
from Einstein Discovery.

**•** `Unknown` : Report execution origin is unknown.

**•** `Test` : Report execution resulted from a test.

```
RenderingType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the format of the report output in Salesforce Classic. If the report was exported in
Lightning Experience, this field is blank.

Possible values are:

**•** `W` : Web (HTML)


Standard Objects ReportEventLog

**Field** **Details**

**•** `E` : Email

**•** `P` : Printable

**•** `X` : Excel

**•** `C` : Comma-separated values (CSV)

**•** `J` : JavaScript Object Notation (JSON)

**•** `D` : Dummy data

```
ReportIdentifier

RequestIdentifier

RequestStatus

RowCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the report that was run.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
int


Standard Objects ReportEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The number of rows that were processed in the Report event. High row counts, coupled
with a high `AverageRowSize`, can indicate that a user is downloading information for
fraudulent purposes. For example, a salesperson who downloads all sales leads before
departing for a competitor. For example: `150` .

```
RunTime

SessionKey

SortOrder

Timestamp

Uri

```

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
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The sort column and order that was used in the report.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string


Standard Objects ReportEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

```
UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.


### Standard Objects ReportExportEventLog ReportExportEventLog

Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports a
report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that data,
see the Report event type. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientInfo

ClientIp

CpuTime

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the client that’s using Salesforce services.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string


Standard Objects ReportExportEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

```
ReportDescription

RequestIdentifier

RunTime

SessionKey

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the report that was run.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

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


### Standard Objects ReportTag

**Field** **Details**

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
Uri

UserIdentifier

### ReportTag

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

Associates a word or short phrase with a Report. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.


### Standard Objects ReputationLevel

**Field Name** **Details**

```
Name

TagDefinitionId

Type

```

Usage

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

ReportTag stores the relationship between its parent TagDefinition and the Report being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

SEE ALSO:

Report

### ReputationLevel

Represents a reputation level defined for an Experience Cloud site. This object is available in API version 32.0 and later.


Standard Objects ReputationLevel

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.

Fields

**Field Name** **Details**

```
Label

LevelNumber

ParentId

Threshold

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the reputation level.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The rank of the reputation level.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site the reputation level applies to.

**Type**
double

**Properties**
Filter, Sort

**Description**
The lower limit of reputation points associated with this reputation level. The
maximum number of reputation points a user can accrue is 999,999,999,999,999.


### Standard Objects ReputationLevelLocalization ReputationLevelLocalization

Represents the translated value of a reputation level. Reputation level localization only applies for reputation levels in Experience Cloud
sites. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

This object is available only if digital experiences is enabled in your org and reputation is enabled in your Experience Cloud site.

Fields

**Field Name** **Details**

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The language the reputation level is translated into. The picklist contains the
following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.


### Standard Objects ReputationPointsRule

**Field Name** **Details**

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

```
NamespacePrefix

ParentId

Value

### ReputationPointsRule

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the reputation level this translated value applies to.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the reputation level. Label is **Translation Text** .

Represents the reputation point rules for an Experience Cloud site. Each rule specifies an action that members can earn points from and
the points associated with those actions in a particular site. This object is available in API version 32.0 and later.


Standard Objects ReputationPointsRule

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.

Fields

**Field Name** **Details**

```
ParentId

Points

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site that the point rule applies to.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**

The reputation points associated with the member action this rule is for. The
maximum value this field can contain is 999,999.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The member action associated with this rule, limited to one of these actions:

**•** Write a post ( `FeedItemWriteAPost` )

**•** Write a comment ( `FeedItemWriteAComment` )

**•** Receive a comment ( `FeedItemReceiveAComment` )

**•** Like something ( `FeedItemLikeSomething` )

**•** Receive a like ( `FeedItemReceiveALike` )

**•** Share a post ( `FeedItemShareAPost` )

**•** Someone shares your post ( `FeedItemSomeoneSharesYourPost` )

**•** Mention someone ( `FeedItemMentionSomeone` )

**•** Receive a mention ( `FeedItemReceiveAMention` )


### Standard Objects ResourceAbsence

**Field Name** **Details**

**•** Ask a question ( `FeedItemPostQuestion` )

**•** Answer a question ( `FeedItemAnswerAQuestion` )

**•** Receive an answer ( `FeedItemReceiveAnAnswer` )

**•** Mark an answer as best ( `FeedItemMarkAnswerAsBest` )

**•** Someone marks your answer as best
( `FeedItemYourAnswerMarkedBest` )

**•** Endorse someone for knowledge on a topic
( `EndorseSomeoneForKnowledgeOnATopic` )

**•** Someone endorses you for knowledge on a topic
( `EndorsedForKnowledgeOnATopic` )

**•** Upload a profile picture ( `ProfilePhotoUpload` ) This action is available
in API version 45.0 and later.

### ResourceAbsence

Represents a time period in which a service resource is unavailable to work in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
AbsenceNumber

Address

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the absence.

**Type**
address


Standard Objects ResourceAbsence

**Field Name** **Details**

**Properties**
Filter

**Description**
The compound form of the address associated with the absence.

```
City

Country

Description

End

GeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address associated with the absence. Maximum length is 40
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the absence.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence ends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ResourceAbsence

**Field Name** **Details**

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

```
LastReferencedDate

LastViewedDate

Latitude

Longitude

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.


Standard Objects ResourceAbsence

**Field Name** **Details**

```
Postal Code

ResourceId

Start

State

Street

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the absence. Maximum length is
20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The absent service resource.

This is a relationship field.

**Relationship Name**
Resource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ResourcePreference

**Field Name** **Details**

**Description**
The street number and name of the address associated with the absence.

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The type of absence: _`Meeting`_, _`Training`_, _`Medical`_, or _`Vacation`_ . The
default value is _`Vacation`_ . You can add custom values if needed, but the name
_`Break`_ is reserved for the Field Service managed package.

Resource absences you define periods of time when a service resource is unavailable to work. Unless you’re using the Field Service
managed package, service resources can still be assigned to appointments that conflict with their absences.

Tip: Create a trigger that sends an approval request to a supervisor when a service resource creates an absence.

If you’re not using the Field Service managed package, a calendar view isn’t available for individual service resources.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ResourceAbsenceChangeEvent (API version 48.0)**
Change events are available for the object.

**ResourceAbsenceFeed**

Feed tracking is available for the object.

**ResourceAbsenceHistory**

History is available for tracked fields of the object.

### ResourcePreference

Represents an account’s preference for a specified service resource on field service work.

Resource preferences indicate which service resources can be assigned to field service work. You can designate service resources as
preferred, required, or excluded on specific accounts, assets, locations, work orders, or work order line items. Work orders inherit their
associated account’s resource preferences.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects ResourcePreference

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

PreferenceType

RelatedRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource preference was last modified.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource preference was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Resource preference type. Values include:

**•** Preferred: Indicates that the customer would like their field service work
assigned to the resource.

**•** Required: Indicates that the resource must be assigned to the customer’s
field service work.

**•** Excluded: Indicates that the customer doesn’t want their field service work
assigned to the resource.

Resource preferences serve more as a suggestion than a requirement. You can
still assign a service appointment to any resource regardless of the related work
order’s resource preferences.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The work order or account with the resource preference.


Standard Objects ResourcePreference

**Field Name** **Details**

This field is a polymorphic relationship.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Accounts, Assets, Locations, Work Orders, or Work Order Line Items

```
ResourcePreferenceNumber

ServiceResourceId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the resource preference.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that is preferred, required, or excluded.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ResourcePreferenceChangeEvent (API version 54.0)**
Change events are available for the object.

**ResourcePreferenceFeed**

Feed tracking is available for the object.

**ResourcePreferenceHistory**

History is available for tracked fields of the object.


### Standard Objects RestApiEventLog RestApiEventLog

REST API event logs contain details about REST-specific requests. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ClientIp

CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the bot.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The bot session ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects RestApiEventLog

**Field** **Details**

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

```
DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

ExceptionMessage

FieldCount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how much activity is occurring in the database. A high value for this field suggests
that adding indexes or filters on your queries would benefit performance.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The exception message for a REST API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects RestApiEventLog

**Field** **Details**

**Description**
The number of fields or columns, where applicable.

```
LoginKey

MediaType

Method

ObjectName

PlannerIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The media type of the response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: `GET`, `POST`, `PUT`, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request. For example: `Account`,
`Opportunity`, `Contact`, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.


Standard Objects RestApiEventLog

**Field** **Details**

```
RequestIdentifier

RequestSize

RequestStatus

ResponseSize

RowsProcessed

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
int


Standard Objects RestApiEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Numbers of rows that are processed by the REST API.

```
RunTime

SessionKey

StatusCode

Timestamp

Uri

```

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
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP response status code for the request.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .


### Standard Objects ReturnOrder

**Field** **Details**

```
UserIdentifier

UserType

### ReturnOrder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose access is limited because
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your customers can view and interact
with your site without logging in.

**•** `PowerCustomerSuccess` —Power Customer Success license. Users whose access
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

Represents the return or repair of inventory or products in Field Service, or the return of order products in Order Management. This object
is available in API version 42.0 and later.


Standard Objects ReturnOrder

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Order Management must be enabled. If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category Activated. The default Statuses corresponding to Activated are Submitted
and Approved.

Fields

**Field Name** **Details**

```
AccountId

CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the return order.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the return order.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup


Standard Objects ReturnOrder

**Field Name** **Details**

**Refers To**
Case

```
ContactId

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the return order.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the
currency of the OrderSummary associated with the ReturnOrder.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order.


Standard Objects ReturnOrder

**Field Name** **Details**

```
DestinationLocationId

ExpectedArrivalDate

ExpirationDate

GrandTotalAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the items are expected to arrive at the destination location.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Authorizations can’t be captured after their expiration dates.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges
on the return order. This includes all return order line items associated with the
return order. This amount is equal to TotalAmount + TotalTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.


Standard Objects ReturnOrder

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

LifeCycleType

OrderId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order was last viewed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the order summary is managed by Salesforce Order
Management (MANAGED) or by an external system (UNMANAGED). An
unmanaged order summary is stored in Salesforce for reference purposes.

**•** Some Order Management APIs reject input records that are associated with
unmanaged order summaries.

**•** Order Management does not update financial bucket fields on some records
that are associated with unmanaged order summaries.

**•** A user with the EditUnmanagedOrderSummaries or B2BCommerceIntegrator
permission can edit certain fields on objects related to unmanaged order
summaries that are normally only accessible via APIs.

Possible values are:

**•** `MANAGED` —Managed

**•** `UNMANAGED` —Unmanaged

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
The order associated with the return order. When you associated a return order
with an order, you can associate the return order’s line items with order products.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

```
OrderSummaryId

OwnerId

ProductRequestId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order summary associated with the return order.

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the return order.

This is a polymorphic relationship field.

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
The product request associated with the return order. When you associated a
return order with a product request, you can associate the return order’s line
items with the product request’s line items.


Standard Objects ReturnOrder

**Field Name** **Details**

A return order might be related to a product request if the return order tracks
the return of unused products or products to be repaired or replaced. For example,
a technician creates a product request for three motors to prepare for a field visit.
If the technician finds that only two motors are needed, they can create a return
order to return the third to the original location, and list the product request in
this field.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest

This field is available only if Field Service or Health Cloud is enabled.

```
ProductServiceCampaignId

RefundInstructionsHint

ReturnOrderNumber

ReturnedById

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the return order

This field is available only if Field Service is enabled.

**Type**
textarea

**Properties**
Nillable

**Description**
Stores a JSON representation of the payment credit and refund sequences for
ensure credit, ensure refund, and the change orders associated with it.

This field is available in API version 65.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the return order.

**Type**
reference


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user returning the items.

This is a relationship field.

**Relationship Name**
ReturnedBy

**Relationship Type**
Lookup

**Refers To**
User

```
ShipFromAddress

ShipFromCity

ShipFromCountry

ShipFromGeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The return shipping address. This address tracks the location of the items at the
start of the return or repair. For example, if a customer is returning an item, the
Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the return shipping address. This address tracks the location of
the items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
picklist


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the return shipping address. See Compound
Fields Considerations and Limitations for details on geolocation compound fields.
This field is available in the API only.

```
ShipFromLatitude

ShipFromLongitude

ShipFromPostalCode

ShipFromState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places. See Compound Fields Considerations and Limitations for details
on geolocation compound fields. This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places. See Compound Fields Considerations and Limitations for details
on geolocation compound fields. This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the return shipping address. This address tracks the location
of the items at the start of the return or repair. For example, if a customer is
returning an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
The state of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

```
ShipFromStreet

ShipmentType

SourceLocationId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment associated with the return order. Available values are:

**•** `Standard` (default value)

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location


Standard Objects ReturnOrder

**Field Name** **Details**

```
Status

StatusCategory

TaxLocaleType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the return order. Available values are:

**•** `Draft`

**•** `Submitted`

**•** `Approved`

**•** `Canceled`

**•** `Closed`

If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category `Activated` .
The default Statuses corresponding to Activated are Submitted and Approved.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status category of the return order. Processing of the return order depends on
this value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `Activated`

**•** `Canceled`

**•** `Closed`

**•** `Draft`

**•** `Pending`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original order associated with the return
order. Gross usually applies to taxes like value-added tax (VAT), and Net usually
applies to taxes like sales tax.

Possible values are:

**•** `Automatic` (displays most prices and taxes as combined values)


Standard Objects ReturnOrder

**Field Name** **Details**

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

This field is available in API version 50.0 and later.

```
TotalAmount

TotalDeliveryAdjustAmount

TotalDeliveryAdjustAmtWithTax

TotalDeliveryAdjustTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the return order line items, including products,
fees, and delivery charges, on the ReturnOrder.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order. This value only includes adjustments to return order line items of
type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order, inclusive of tax. This value only includes adjustments to return order
line items of type code Charge. This amount is equal to
TotalDeliveryAdjustAmount + TotalDeliveryAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Tax on the TotalDeliveryAdjustAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalDeliveryAmount

TotalDeliveryAmtWithTax

TotalDeliveryTaxAmount

TotalFeeAdjustAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges on the return order. This value only includes return
order line items of type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the return order, inclusive of tax. This
value only includes return order line items of type code Charge. This amount is
equal to TotalDeliveryAmount + TotalDeliveryTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Total amount of the price adjustments applied to the fees on the return order.
This value only includes adjustments to return order line items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

```
TotalFeeAdjustAmtWithTax

TotalFeeAdjustTaxAmount

TotalFeeAmount

TotalFeeAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the return order,
inclusive of tax. This value only includes adjustments to return order line items
of type Fee. This amount is equal to TotalFeeAdjustAmount +
TotalFeeAdjustTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjustAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the fees on the return order. This value only includes return order line
items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrder

**Field Name** **Details**

**Description**
Total amount of the fees on the return order, inclusive of tax. This value only
includes return order line items of type Fee. This amount is equal to
TotalFeeAmount + TotalFeeTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

```
TotalFeeTaxAmount

TotalProductAdjustAmount

TotalProductAdjustAmtWithTax

TotalProductAdjustTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order. This value only includes adjustments to return order line items of type
code Product.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order, inclusive of tax. This value only includes adjustments to return order line
items of type code Product. This amount is equal to TotalProductAdjustAmount
+ TotalProductAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalProductAmount

TotalProductAmtWithTax

TotalProductTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the product charges on the return order. This value only includes return
order line items of type code Product.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the product charges on the return order, inclusive of tax. This
value only includes return order line items of type code Product. This amount is
equal to TotalProductAmount + TotalProductTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency


Standard Objects ReturnOrder

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

Usage

You can use return orders to track customer returns, customer repairs, or the return of inventory from a technician’s van stock to a
warehouse or supplier. Customers can initiate a return from a community, or agents can create return orders in response to a customer
call or technician request.

Return orders are composed of return order line items, which allow you to add details about the items being returned. To represent the
returned items, each line item must list one or more of the following: product, product item, asset, product request line item, and order
product. Return orders can be associated with a product request, case, account, contact, and order if needed. This versatility lets you use
return orders to track a wide range of return scenarios.

Example

```
   {

     "RefundInstructionsHint": {

      "PaymentCreditSequence": [

       {

        "OrderPaymentSummaryId": "0bMxx0000000000001",

        "Amount": 50,

        "CreditType": "GIFT_CARD",

        "Rank": 1

       },

       {

        "OrderPaymentSummaryId": "0bMxx0000000000002",

        "Amount": 50,

        "CreditType": "CHECK",

        "Rank": 2

       }

      ]

     },

     "RefundSequence": [

      {

       "OrderPaymentSummaryId": "0bMxx0000000000001",

       "Amount": 50,

       "Rank": 1

      },

      {

       "OrderPaymentSummaryId": "0bMxx0000000000002",

       "Amount": 50,

```


### Standard Objects ReturnOrderItemAdjustment

```
       "Rank": 2

      }

     ],

     "ChangeOrders": [

      {

       "ChangeOrderId": "801xx000003Gd01111",

       "FeeChangeOrderId": null,

       "NetAmount": -75

      }

     ]

   }

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderFeed**

Feed tracking is available for the object.

**ReturnOrderHistory**

History is available for tracked fields of the object.

**ReturnOrderOwnerSharingRule**

Sharing rules are available for the object.

**ReturnOrderShare**

Sharing is available for the object.

### ReturnOrderItemAdjustment

Represents a price adjustment on a return order line item. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Order Management must be enabled.


Standard Objects ReturnOrderItemAdjustment

Fields

**Field** **Details**

```
Amount

Description

OrderItemAdjustLineSummaryId

ReturnOrderId

ReturnOrderItemAdjustmentNumber

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item adjustment line summary associated with the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order associated with the return order line item to which the adjustment
applies.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string


Standard Objects ReturnOrderItemAdjustment

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item adjustment.

```
ReturnOrderLineItemId

TotalAmtWithTax

TotalTaxAmount

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order line item to which this adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ReturnOrderItemTax ReturnOrderItemTax

Represents the tax on a return order line item or return order item adjustment. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Order Management must be enabled.

Fields

**Field** **Details**

```
Amount

Description

OrderItemTaxLineItemSummaryId

Rate

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the return order item tax.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the return order item tax.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item tax line item summary associated with the order item summary that
corresponds to the return order line item to which the tax applies.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrderItemTax

**Field** **Details**

**Description**
Tax rate used to calculate the Amount.

```
ReturnOrderId

ReturnOrderItemAdjustmentId

ReturnOrderItemTaxNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated return order.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this object represents a tax on an adjustment, this value is the ID of the return order item
adjustment to which the tax applies. If this value is null, the adjustment applies to a return
order line item.

This is a relationship field.

**Relationship Name**
ReturnOrderItemAdjustment

**Relationship Type**
Lookup

**Refers To**
ReturnOrderItemAdjustment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item tax.


Standard Objects ReturnOrderItemTax

**Field** **Details**

```
ReturnOrderLineItemId

TaxEffectiveDate

Type

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents a tax on a return order line item, this value is the ID of that return
order line item. If this object represents a tax on an adjustment, this value is the ID of the
return order line item to which the adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows whether the amount on the tax line is an estimate or the final calculated amount.
Doesn’t set a value by default. Users can define automation to set and change the value as
needed.

Possible values are:

**•** `Actual`

**•** `Estimated`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ReturnOrderLineItem ReturnOrderLineItem

Represents a specific product that is returned or repaired as part of a return order in Field service, or a specific order item that is returned
as part of a return order in Order Management. This object is available in API version 42.0 and later.

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Order Management must be enabled.

Fields

**Field Name** **Details**

```
AssetId

ChangeOrderItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the return order line item. One or more of the following
fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId, and
ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the change order item associated with the return order line item.

This field is available in API version 50.0 and later.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
ChangeOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

```
CurrencyIsoCode

Description

DestinationLocationId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for the currency of the original Order associated with the
ReturnOrderLineItem.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

```
GrossUnitPrice

LastReferencedDate

LastViewedDate

OrderItemId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price, including tax, of the product represented by the associated order item
summary.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

This is a relationship field.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Relationship Name**
OrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

```
OrderItemSummaryId

ProcessingPlan

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item summary associated with the return order line item.

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the preferred fate of the items following their return. Available values
are:

**•** `Repair` —Repair the items and return them to the owner

**•** `Discard` —Discard the items

**•** `Salvage` —Salvage the items’ working parts

**•** `Restock` —Return the items to your inventory

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Refers To**
Product2

```
ProductItemId

ProductRequestLineItemId

ProductServiceCampaignId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product item representing the location of the product at the start of the
return. One or more of the following fields must be filled out: AssetId, OrderItemId,
Product2Id, ProductItemId, and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product request line item associated with the return order line item. One or
more of the following fields must be filled out: AssetId, OrderItemId, Product2Id,
ProductItemId, and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product service campaign associated with the return order line item.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

```
ProductServiceCampaignItemId

QuantityExpected

QuantityReceived

QuantityRejected

QuantityReturned

QuantityUnitOfMeasure

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the return order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity of items expected to be returned.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual quantity of items received for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity of items rejected for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of items being returned. If multiple types of products are being
returned, track each product in a different return order line item.

**Type**
picklist


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the returned items; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

```
ReasonForRejection

ReasonForReturn

ReasonForChangeText

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Reason for rejecting returned items on this return order line item.

Possible values are:

**•** `Damaged Item`

**•** `Expired Warranty`

**•** `Missing Item or Part`

**•** `Wrong Item`

The default value is `Missing Item or Part` .

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the items are being returned. Available values are:

**•** `Damaged`

**•** `Defective`

**•** `Duplicate Order`

**•** `Wrong Item`

**•** `Wrong Quantity`

**•** `Not Satisfied`

**•** `Outdated`

**•** `Other`

The default value is `Damaged` .

**Type**
string


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
Details about the reason for return change

```
RepaymentMethod

ReturnOrderId

ReturnOrderLineItemNumber

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The method by which the customer or owner will be reimbursed for the items
being returned. Available values are:

**•** `Replace` —The items will be replaced

**•** `Refund` —The items will be returned and the owner will be refunded

**•** `Credit` —The items will be returned and the owner will receive credit for
them

**•** `Return` —The items will be returned to the owner (for example, following
their repair)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The return order that the return order line item belongs to.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number that identifies the return order line item.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

```
SourceLocationId

TotalAdjustmentAmount

TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all price adjustments applied to the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the return order line item,
inclusive of tax. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

**Description**
Tax on the TotalAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

```
TotalAmount

TotalLineAmount

TotalLineAmountWithTax

TotalLineTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total, not including adjustments or tax, of the return order line item.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the return order line item, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

This is a calculated field.

This field is available in API version 50.0 and later.


Standard Objects ReturnOrderLineItem

**Field Name** **Details**

```
TotalPrice

TotalTaxAmount

Type

TypeCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the return order line item. Equal to
UnitPrice times Quantity.

This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the return order line item. Matches the type of the associated order item
summary. Delivery Charge indicates that the return order line item represents a
delivery charge. Fee indicates that it represents another type of fee, such as a
return fee. Order Product indicates that it represents any other type of product,
service, or charge. Each type corresponds to one type code, shown here in
parentheses.

Possible values are:

**•** `Delivery Charge (Charge)`

**•** `Fee (Charge)` This value is available in API v56.0 and later.

**•** `Order Product (Product)`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ReturnOrderOwnerSharingRule

**Field Name** **Details**

**Description**
Type code of the return order line item. Matches the type code of the associated
order item summary. Processing depends on this value. Charge indicates that
the return order line item represents a delivery charge. Product indicates that it
represents an other type of product, service, or charge. Each type category
corresponds to one or more types.

Possible values are:

**•** `Charge`

**•** `Product`

This field is available in API version 50.0 and later.

```
UnitPrice

```

Associated Objects

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Unit price of the return order line item.

This field is available in API version 50.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderLineItemFeed**

Feed tracking is available for the object.

**ReturnOrderLineItemHistory**

History is available for tracked fields of the object.

### ReturnOrderOwnerSharingRule

Represents the rules for sharing a return order with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 42.0 and later.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)


Standard Objects ReturnOrderOwnerSharingRule

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

DeveloperName

GroupId

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A return order owned by a User in the source Group
triggers the rule to give access.

**Type**
string


### Standard Objects RevenueAsyncOperation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

```
ServiceResourceAccessLevel

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### RevenueAsyncOperation

Represents the status of an asynchronous process initiated by a REST request in Subscription Management. This object is available in
API versions 57.0 to 59.0. Use AsyncOperationTracker instead of RevenueSyncOperation in API version 59.0 and later.

For example, `asset-management/assets/collection/actions/initiate-amend-quantity` creates a
### RevenueAsyncOperation record when it initiates an asynchronous process. The ID of the record is returned in the REST response.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management.


Standard Objects RevenueAsyncOperation

Fields

**Field** **Details**

```
AsyncOperationNumber

CorrelationIdentifier

ExpiresAt

FailedJobItems

FinishedAt

JobType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique identifier for this revenue async operation record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the API request associated with this revenue async operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items that weren’t successfully processed by the sync operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects RevenueAsyncOperation

**Field** **Details**

**Description**
The REST request that initiated the asynchronous process.

Valid values are:

**•** `ASMAdServerCheckAvailability`

**•** `ASMAdServerIntegration`

**•** `ASMApplyMediaPlanTemplateJob`

**•** `ASMApplyTargetingTemplateJob`

**•** `ASMCreateAmendQuoteJob`

**•** `ASMMediaPlanAsTemplate`

**•** `ASMMediaPlanClone`

**•** `ASMMediaPlanCopyJob`

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion`

**•** `AutomaticRefunds`

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`

**•** `InvoicedDocgenJob`

**•** `InvoicedDocgenPostProcessJob`

**•** `InvoicedDocfenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `InvoiceEstimatedTaxCallout`

**•** `PST Base Job - Top-Level`

**•** `PSTConfig - Configuration`

**•** `PSTPersist - Save`

**•** `PSTPrice - Price`

**•** `PearAmendQtyAssets`

**•** `PearCancelAssets`

**•** `PearRenewAssets`

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote`

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`


Standard Objects RevenueAsyncOperation

**Field** **Details**

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment`

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `StandaloneBillingSchedulesCreation`

**•** `TestSerialMessageStepJob`

**•** `TransactionLineBom`

```
LastReferencedDate

LastViewedDate

ParentOperationId

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
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

This field is a relationship field.

**Relationship Name**
ParentOperation

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation


Standard Objects RevenueAsyncOperation

**Field** **Details**

```
ReferenceEntityId

StartedAt

Status

SubmittedAt

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a polymorphic field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
CreditMemo, Order, Product2, Quote

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when Salesforce started the asynchronous process.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the asynchronous process.

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures`

**•** `Failure`

**•** `InProgress`

**•** `Submitted`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

```
SuccessfulJobItems

TotalJobItems

```

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items successfully processed by the sync operation.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of items processed by the sync operation, including both successfully
processed items and failed items.

### RevenueTransactionErrorLog

Contains information about errors that occurred while processing a request. The error record persists until another error with the same
category, primary record, and (optionally) related record occurs. This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_revenuetransactionerrorlog.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_revenuetransactionerrorlog.htm)

Fields

**Field** **Details**

```
AsyncOperationTrackerId

```

**Type**
reference


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the async operation tracker record created by the request. Async operation tracker
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
AsyncOperationTracker

**Relationship Type**
Lookup

**Refers To**
AsyncOperationTracker

```
Category

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides context about the source of error. For example, if an error occurs while processing
an `/assets/collection/actions/initiate-cancellation` request, the
category is `InitiateCancel` .

Possible values are:

**•** `ApplyAPI`

**•** AutomatedNegativeInvoiceLineConversion

**•** AutomaticRefunds

**•** `ConvertNegativeInvoiceLineToCredit` —available in API version 56.0 and
later

**•** `Core Invoice Generation Failure`

**•** `CreditInvoiceAPI`

**•** `CreditTaxIntegrationAPI`

**•** `InitiateAmendment` —available in API version 56.0 and later

**•** `InitiateCancel`

**•** `InitiateRenewal`

**•** `InsufficientAccess` —Insufficient Access to start Invoice run

**•** `InvoiceBatchRun`

**•** `InvoiceBatchRunInvoiceGeneration`

**•** `InvoiceBatchRunPostProcessor`

**•** `InvoiceBatchRunPreProcessor`

**•** `InvoiceBatchRunRecovery`


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

**•** `InvoiceBatchRunSelectionStep`

**•** `InvoiceBatchRunSummarizer`

**•** `InvoiceBatchRunTaxProcessor`

**•** `MaterialLineGeneration` —available in API version 58.0 and later

**•** `Invalid Tax API Input`

**•** `Invalid Tax Integration Input`

**•** `OrderTaxCalculationFailure` —available in API version 61.0 and later of
Revenue Cloud.

**•** `OrderToAsset`

**•** `OrderItemToAsset` —available in API version 59.0 and later

**•** `OrderToBillingSchedule`

**•** `PaymentSale`

**•** `PaymentScheduleGeneration` —available in API version 56.0 and later

**•** `QuotePriceCalculationFailure` —available in API version 61.0 and later of
Revenue Cloud.

**•** `QuoteTaxCalculationFailure` —available in API version 61.0 and later of
Revenue Cloud.

**•** `QuoteToOrder` —available in API version 56.0 and later

**•** `Post Tax API Failure`

**•** `Post-Credit Tax Failure`

**•** `Pre-Credit Tax Failure`

**•** `StandaloneCreditAPI`

**•** `Tax API Failure`

**•** `TransactionToContract` —available in API version 59.0 and later

**•** `Unknown Failure` —available in API version 56.0 and later

**•** `VoidPostedInvoiceAPI`

```
ErrorCode

ErrorLogNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code; for example, INVALID_INPUT.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated unique ID that identifies the error.


Standard Objects RevenueTransactionErrorLog

**Field** **Details**

```
ErrorMessage

OwnerId

PrimaryRecordId

RelatedRecordId

```

**Type**
textarea

**Description**
Contains information about the error and how to resolve it.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who made the request that resulted in the creation of the error log.

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
Filter, Group, Sort

**Description**
The ID of the record that’s associated with this error. For example, if the error occurred while
creating an invoice from an order, the primary ID is the ID of the order.

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryRecord

**Relationship Type**
Lookup

**Refers To**
Asset, BillingBatchScheduler, BillingSchedule, CardPaymentMethod, CreditMemo, Invoice,
InvoiceBatchRun, InvoiceBatchRunRecovery, Order, Payment, PaymentBatchRun,
PaymentGateway, Quote, Refund

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects RpaFlowResultEvent

**Field** **Details**

**Description**
Optional. The ID of a record that can provide additional context about the error. For example,
if `PrimaryRecordId` is the ID of an order, this field could be the ID of an order item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
BillingBatchScheduler, BillingSchedule, BillingScheduleGroup, CreditMemo, CreditMemoLine,
Invoice, InvoiceLine, OrderItem, Payment, PaymentSchedule, PaymentScheduleItem,
QuoteLineItem, Refund

```
RequestIdentifier

RevenueAsyncOperationId

### RpaFlowResultEvent

```

Reserved for future use.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID returned by the request. Use this ID to identify the revenue transaction error
log records for a specific request. This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the revenue async operation record created by the request. Revenue async operation
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
RevenueAsyncOperation

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation


### Standard Objects RpaRobot RpaRobot

Reserved for future use.

### RpaRobotAsgnMaintWindow

Reserved for future use.

### RpaRobotAsgnSessionInf

Reserved for future use.

### RpaRobotDefinition

Reserved for future use.

### RpaRobotMaintWindow

Reserved for future use.

### RpaRobotMaintWindowDef

Reserved for future use.

### RpaRobotPool

Reserved for future use.

### RpaRobotPoolAsgnRobot

Reserved for future use.

### RpaRobotPoolDefinition

Reserved for future use.

### RpaRobotPoolFlowAsgn

Reserved for future use.


### Standard Objects RpaRobotSessionInfo RpaRobotSessionInfo

Reserved for future use.

### RpaRobotSessionInfoDef

Reserved for future use.

### RuleTerritory2Association

Represents a record-assignment rule and its association to an object, such as Account. Available if Sales Territories has been enabled.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived` ).

Fields

**Field Name** **Details**

```
IsInherited

RuleId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the rule is an _inherited_ rule ( `true` ) or a _local_ rule ( `false` ).
Rule inheritance flows from the parent territory where the rule is created to the
rule’s descendent territories (if any) in the territory model hierarchy. A local rule
is created within a single territory and affects that territory only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the rule.


### Standard Objects SalesAIScoreCycle

**Field Name** **Details**

```
Territory2Id

### SalesAIScoreCycle

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory where the rule was created.

Represents the cycle type and ID used to score records. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To see score cycle information, users need a Sales Cloud Einstein license with the View Scoring Model Factors permission enabled. The
permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field** **Details**

```
CycleType

Name

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The cycle used to create scores on opportunity records can be one of two types.

**•** `OpportunityScoreModeling` —Provides model factors, which Sales Cloud
Einstein uses to build a scoring model.

**•** `OpportunityScoreScoring` —Provides scores and key factors to individual
records, which are based on Sales Cloud Einstein’s scoring model.

Note: When the value `OpportunityScoreModeling` is returned, use the
Sales AI Score Model Factor object to get information about the model factors.

**Type**
string


### Standard Objects SalesAIScoreModelFactor

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the cycle. Currently, the name is a system-generated unique value.

### SalesAIScoreModelFactor

Represents the factors that Sales Cloud Einstein uses to build a scoring model. Scoring models are used by features, such as Opportunity
Scoring, to score individual records. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To see model factor information, users need a Sales Cloud Einstein license with the “View Scoring Model Factors” permission enabled.
The permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this
object.

Fields

**Field** **Details**

```
Factor

FactorSummaryOrgLanguage

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A factor that contributes to a scoring model. For example, a factor could indicate that an
amount increase has a positive effect on an opportunity score (AmountIncreasePositive). Or,
it could indicate that a change to the close date has a negative effect on an opportunity
score (CloseDateChangeNegative).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the factor in English. For example, the factor field value AmountChangePositive
is summarized as “Amount change has positive effect”.


Standard Objects SalesAIScoreModelFactor

**Field** **Details**

```
Name

OperatorType

PrimarySourceFieldName

PrimarySourceFieldValue

PrimarySourceFieldValueText

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the model factor. Currently, the name is a system-generated value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operator used to analyze field values. For example, the factor HighSuccessLeadSource
uses the Lead Source field as the primary source field. When building the scoring model,
Einstein uses the Equals operator to determine `PrimarySourceFieldValue =`
`Internet` . The other supported operator is `IsNull` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the primary field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the PrimarySourceFieldValueText, such as a record ID or value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the primary source field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field, and the value of the
Industry field is manufacturing.

Note: This field’s value is retrieved from the `PrimarySourceFieldValue`
field. If the `PrimarySourceFieldValue` field is a record ID, then


Standard Objects SalesAIScoreModelFactor

**Field** **Details**

`PrimarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull`, then `PrimarySourceFieldValue`
returns `true` and `PrimarySourceFieldValueText` returns `null` .

```
SalesAiScoreCycleId

ScoreCorrelation

SecondarySourceFieldName

SecondarySourceFieldValue

SecondarySourceFieldValueText

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the score cycle used to generate model factors. Each score cycle can have multiple
model factors associated to it.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The strength between a model factor and a score. If score correlation value is closer to `+1`,
it’s more likely that the model factor contributing toward a high score. If score correlation
value is closer to `-1`, it’s more likely that the model factor is contributing toward a low score.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the secondary field used in the model factor. For example, the factor
HighAmountActivity uses Task as the primary field and Event as the secondary field. Not all
model factors use a secondary source field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the SecondarySourceFieldValueText, such as a record ID or value.
Not all model factors use a secondary source field. This field is available in API version 50.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects SalesforceLoginAsEventLog

**Field** **Details**

**Description**
When the model factor is based on two source fields, this field represents the value of the
secondary source field. For example, the factor HighSuccessMultipleSameFieldValue might
use the opportunity’s related product as the primary field and pricebook as the secondary
field. The product and pricebook names are indicated by the PrimarySourceFieldValueText
and SecondarySourceFieldValueText, respectively. Not all model factors use a secondary
source field. This field is available in API version 50.0 and later.

Note: This field’s value is retrieved from the `SecondarySourceFieldValue`
field. If the `SecondarySourceFieldValue` field is a record ID, then

`SecondarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull`, then `SecondarySourceFieldValue`
returns `true` and `SecondarySourceFieldValueText` returns `null` .

```
Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Determines whether the model factor is active or inactive.

Use the SalesAIScoreModelFactor object to run a query that retrieves the latest highest influencing model factors.

```
SELECT Id,Factor,ScoreCorrelation,FactorSummaryOrgLanguage

FROM SalesAIScoreModelFactor

WHERE Status='Active' and SalesAIScoreCycle.CycleType='OpportunityScoreModeling'

ORDER BY ScoreCorrelation desc

### SalesforceLoginAsEventLog

```

Salesforce LoginAs Event provides details about the Salesforce User's login into Customer Org as Customer's authorized user. This object
is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects SalesforceLoginAsEventLog

Fields

**Field** **Details**

```
ActualUserIdentifier

CaseIdentifier

IpAddress

OperationType

RequestIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The actual user's identifier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce case ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
IP address of the browser.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of operation. For example, login or logout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects SalesChannel

**Field** **Details**

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

### SalesChannel

Represents the origin of an order. For example, a web storefront, physical store, marketplace, or mobile app. If you integrate Salesforce
Order Management with Salesforce B2C Commerce, set up a SalesChannel corresponding to each Site in your B2C Commerce
implementation. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
Description

ExternalChannelNumber

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the SalesChannel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External system identifier for the SalesChannel.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SalesChannel

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

OwnerId

SalesChannelName

Type

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this SalesChannel. Default value is the user logged in
to the API to perform the create.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the SalesChannel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the SalesChannel. Each Type corresponds to one Type Category. You can customize
the Type picklist to represent your business processes, but the Type Category picklist is fixed
because some order processing is based on those values. If you customize the Type picklist,
include at least one value for each Type Category. This field is available in API version 53.0
and later.

Default values are:

**•** `B2B`

**•** `B2C`

**•** `Other`


### Standard Objects SalesforceContract

**Field** **Details**

```
TypeCategory

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type Category of the SalesChannel. Each Type Category corresponds to one or more Types.
This field isn’t visible in the UI. This field is available in API version 53.0 and later.

Possible values are:

**•** `B2B`

**•** `B2C`

**•** `Other`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesChannelChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

Order

OrderSummary

### SalesforceContract

Read-only virtual object used in the Your Account App. Represents contract information related to your organization’s Salesforce
subscription.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
AutoRenewCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Determines if contract renews automatically

Possible values are:

**•** `No`

**•** `Yes`

```
BillingAddressCity

BillingAddressCountry

BillingAddressPostalCode

BillingAddressState

BillingAddressStreet

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this contract.


Standard Objects SalesforceContract

**Field** **Details**

```
BillingCompany

BillingEmail

BillingFrequency

BillingName

BillingPhone

ContractId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the billing company.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Define billing periods.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contact name for this contract.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Phone number for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID for this contract.


Standard Objects SalesforceContract

**Field** **Details**

```
ContractNumber

CreditCardExpirationMonth

CreditCardExpirationYear

CreditCardNumber

CreditCardType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Number of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Month the credit card expires.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Year the credit card expires.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
16-digit credit card number.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Credit card provider.

Possible values are:

**•** `AmericanExpress`  

**•** `JCB`

**•** `MasterCard`

**•** `Visa`


Standard Objects SalesforceContract

**Field** **Details**

```
EndDate

ExternalId

FirstNameOnCreditCard

LastNameOnCreditCard

PaymentTerm

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Cardholder’s first name on the credit card.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Cardholder’s last name on the credit card.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment terms definition.

Possible values are:

**•** `Net0` —Due upon receipt

**•** `Net10` —DD-Germany: Net 10

**•** `Net30`  

**•** `Net30EOM` —JP-Net 30 EOM

**•** `Net45`  


Standard Objects SalesforceContract

**Field** **Details**

**•** `Net60`                   

**•** `Net60EOM` —JP-Net 60 EOM

```
PaymentType

SalesforceContractStatus

ShippingAddressCity

ShippingAddressCountry

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment type definition.

Possible values are:

**•** `Check`

**•** `CreditCard`  

**•** `DirectDebit`  

**•** `WireTransfer`  

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the contract

Possible values are:

**•** `Activated`

**•** `Draft`

**•** `Expired`

**•** `Terminated`

**•** `inApproval`  

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. City maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesforceContract

**Field** **Details**

**Description**
Details of the shipping address. Country maximum size is 80 characters.

```
ShippingAddressPostalCode

ShippingAddressState

ShippingAddressStreet

StartDate

SubscriptionDaysLeft

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. State maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address. Maximum of 255 characters.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Start date of the contract.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Days remaining for this subscription.

Used by Your Account to manage contracts related to your organization’s Salesforce subscription. Read-only.


### Standard Objects SalesforceInvoice

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

### **SalesforceInvoice**

**SalesforcePayment**

**SalesforceQuote**

### SalesforceInvoice

Read-only virtual object used in the Your Account App. Represents information about your organization’s invoices with Salesforce.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
Balance

DueDate

ExternalId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.


Standard Objects SalesforceInvoice

**Field** **Details**

```
InvoiceCurrency

InvoiceDate

InvoiceNumber

SalesforceContractId

SalesforceInvoiceStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Currency associated with this invoice.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate` . For example, an invoice with an `InvoiceDate` of April 1 and Net 30 payment
terms would have a `DueDate` of May 1.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
System-created ID for this invoice.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce Contract ID

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup

**Refers To**
SalesforceContract

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects SalesforcePayment

**Field** **Details**

**Description**
The state of the invoice.

Possible values are:

**•** `DueSoon`                   

**•** `Paid`

**•** `PastDue`                   

**•** `Pending`

```
TotalAmount

```

Usage

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` of the invoice items.

Used by Your Account to manage invoices for your organization’s Salesforce contract. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

### **SalesforcePayment**

**SalesforceQuote**

### SalesforcePayment

Read-only virtual object used in the Your Account App. Represents information about payments related to your organization’s Salesforce
invoice.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`


Standard Objects SalesforcePayment

Fields

**Field** **Details**

```
AppliedAmount

AppliedDate

Memo

PaymentCurrency

SalesforcePaymentName

SalesforcePaymentType

```

**Type**
double

**Properties**
Nillable, Sort

**Description**
Payment amount applied to your Salesforce invoice.

**Type**
date

**Properties**
Nillable, Sort

**Description**
Date the payment is applied to your Salesforce invoice.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Credit memo ID. Credit memos are issued for overpayment, rebates, and so forth.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Type of currency used for the payment.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Payment name.

**Type**
picklist

**Properties**
Nillable, Sort


### Standard Objects SalesforceQuote

**Field** **Details**

**Description**
Payment method. Possible values are:

**•** `Boleto`

**•** `Check`

**•** `Credit Card`

**•** `Credit Memo`

**•** `Direct Debit`

**•** `Unknown`

**•** `Wire Transfer`

Usage

Used by Your Account to manage payments for your organization’s Salesforce contract. Read-only.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
SalesforcePayment.

**SalesforceContract**

**SalesforceInvoice**

### **SalesforceQuote** SalesforceQuote

Read-only virtual object used in the Your Account App. Represents information about your organization’s quotes with Salesforce.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ExternalId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.


Standard Objects SalesforceQuote

**Field** **Details**

```
QuoteNumber

SalesforceContractId

SalesforceQuoteStatus

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A system-generated number that identifies the quote.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contract that’s associated with the quote.

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup

**Refers To**
SalesforceContract

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the quote.

Possible values are:

**•** `Complete`

**•** `Expired`

**•** `NeedsApproval`  

**•** `NeedsSignature`  

**•** `Processing`

Used by Your Account to manage quotes related to your organization’s Salesforce contract. Read-only.


### Standard Objects SalesStoreCatalog

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

**SalesforceInvoice**

**SalesforcePayment**

### SalesStoreCatalog

Represents the catalog associated with a store. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a store.

Fields

**Field** **Details**

```
CurrencyIsoCode

ImplementorType

ProductCatalogId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of implementor. WebStoreCatalog is the only available implementor type for
### SalesStoreCatalog.

**Type**
reference


### Standard Objects SalesTransactionItemShape

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID that references the product catalog.

```
SalesStoreId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID that references the store.

### SalesTransactionItemShape

Defines the business logic for a sales transaction shape item, for example, an item in an order. This object is available in API version 57.0
and later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
BasisTransactionItemShapeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the sales transaction shape item to use as a reference when pricing this transaction.
For example, when pricing an order, this field refers to the order being canceled. This field
is available if Subscription Management is enabled.

This field is a relationship field.


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Relationship Name**
BasisTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

```
BillingFrequency

EndDate

ListPrice

ListPriceTotal

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period that indicates how often the sales transaction shape item is billed. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `Annual`

**•** `Monthly`

**•** `Quarterly`

**•** `Semi-Annual`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The last day the sales transaction shape item is available. For example, the last day of the
subscription. This field is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The list price for the sales transaction shape item. This value is inherited from the related
price book entry.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Description**
The list price, inclusive of quantity. This calculated field is equal to `ListPrice` times
`Quantity` .

```
NetUnitPrice

ObligatedAmount

ParentTransactionItemShapeId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final unit price of the product, after all adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**

**Description**
In a subscription, the amount a subscriber is billed for products used during the subscription
period that the subscriber returns before the subscription end date. This field's value is the
price for use of the product.

This field is available in version 57.0 and later. This field is available when Subscription
Management is enabled.

Note:

**•** A subscriber must submit a quantity amendment in order to change the
subscription's product quantity. A quantity amendment request is only valid until
the subscription end date.

**•** A subscriber is eligible for a refund only for the periods when the products weren’t
used.

**•** The subscription's proration policy indicates whether the obligated amount and
the refund are prorated for partial periods.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the parent TransactionItemShape.

This field is a relationship field.

**Relationship Name**
ParentTransactionItemShape


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Refers To**
SalesTransactionItemShape

```
PeriodBoundary

PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The period boundary helps determine the start and end date of the billing periods. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `AlignToCalendar` —The period starts on the first day of the term unit, for example,
the first day of the month.

**•** `Anniversary`  - The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod`  - The period starts on the day indicated by `PeriodBoundaryDay` .

**•** `LastDayOfPeriod`  - The period starts on the last day of the pricing term unit; for
example, the last day of the month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required when `PeriodBoundary` is `DayOfPeriod` . Indicates day of the week or
month that marks the period boundary. Must be an integer from 1 through 31. This field is
available if Subscription Management is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency is Annual or by manual user entry. Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`


Standard Objects SalesTransactionItemShape

**Field** **Details**

**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`

```
PricebookEntryId

PricingTermCount

PricingTransactionType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related price book entry. The related price book entry contains all the pricing
information about the product being sold.

This field is a polymorphic relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntryInterface

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available if Subscription Management is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of pricing transaction, for example, a new sale, an amendment, or a renewal.
This field is available if Subscription Management is enabled.

Possible values are:

**•** `AmendmentAtLastNegotiatedPrice`  - Calculate the price of the amended
sales transaction shape item using the same price book and price adjustments as the


Standard Objects SalesTransactionItemShape

**Field** **Details**

new sale item. For example, an order item that is amended using a pricing transaction
type of `AmendmentAtLastNegotiatedPrice` is priced using the same price
book information and price adjustments as the new sale item. The amended order item
has the same price as the new sale order item.

**•** `AmendmentStartingFromListPrice`                   - Calculate the price of the amended
sales transaction shape item using current price book information, disregarding any
pricing information or adjustments that were applied to the new sale item. Typically, an
amended transaction item has a different price than the new sale transaction item.

**•** `Cancellation`                   - Calculate the price of the canceled transaction. For example, let’s
say that a 1-year subscription was purchased on January 1, then canceled on July 31.
The price of the canceled products and services from August 1 through Dec 31 is
calculated.

**•** `NewSale`                   - The price of a new transaction is calculated.

**•** `RenewalAtLastNegotiatedPrice`                   - Calculate the price of the renewal sales
transaction shape item using the same price book and price adjustments as the new
sale item. For example, an order item that is renewed using a pricing transaction type
of `RenewalAtLastNegotiatedPrice` is priced using the same price book
information and price adjustments as the new sale item. The renewal order item has the
same price as the new sale order item.

**•** `RenewalAtListPrice`                   - Calculate the price of the renewal sales transaction shape
item using current price book information, disregarding any pricing information or
adjustments that were applied to the new sale item. Typically, a renewal transaction
item has a different price than the new sale transaction item.

```
ProductId

ProductSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related product.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Description**
The ID of the related product selling model. The product selling model defines one method
by which a product can be sold; for example, as a one-time sale, an evergreen subscription,
or a termed subscription. This field is available if Subscription Management is enabled.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

```
ProrationPolicyId

Quantity

SalesItemType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. The proration policy defines how the price is calculated
for each subscription period; for example, whether partial periods are allowed, and how
remainder amounts are handled. This field is available if Subscription Management is enabled.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Number of units in the sales transaction shape item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of sale.


Standard Objects SalesTransactionItemShape

**Field** **Details**

Possible values are:

**•** `Charge`                   - An item that acts as a fee and can’t be fulfilled. For example, a delivery
charge, a shipping fee, or a membership fee.

**•** `Product`                   - An item that is a good or service that can be fulfilled. For example, a widget
or a widget warranty.

```
SalesTransactionItemShapeName

SalesTransactionShapeId

StartDate

StartingPriceTotal

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Required. The name of the sales transaction shape item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the sales transaction shape. A sales transaction shape is the way in which
the sales transactions occur. For example, a cart, an order, or a quote.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The start date of the subscription. This field is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


Standard Objects SalesTransactionItemShape

**Field** **Details**

**Description**
The starting unit price, inclusive of quantity, prorated for the duration of the subscription.
This field has two ways to obtain its value. The value can be manually entered or automatically
calculated. The calculation is equal to `StartingUnitPrice` times `Quantity` .

```
StartingUnitPrice

StartingUnitPriceSource

StockKeepingUnit

SubscriptionTerm

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The unit price before any adjustments.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was inherited, entered manually, or calculated.

Possible values are:

**•** `Inherited`  - The starting unit price is copied from a previous transaction; for example,
from the order item being renewed.

**•** `Manual`  - The starting unit price is entered manually, for example, by a sales rep.

**•** `System`  - The starting unit price is calculated using pricing information that was
configured by an administrator; for example, a pricing tier.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The SKU assigned to the related product.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. You can indicate a subscription’s length using
either the start and end dates, or by using the start date and the subscription term. This field
is available if Subscription Management is enabled.


Standard Objects SalesTransactionItemShape

**Field** **Details**

```
TotalAdjustmentAmount

TotalAdjustmentDistAmount

TotalLineAmount

TotalPrice

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the related sales transaction shape items, inclusive of
quantity, prorated for the duration of the subscription. Includes distributed price adjustment
items and price adjustment items applied directly. This calculated field is equal to the sum
of `TotalAdjustmentAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the sales transaction shape
item, prorated for the duration of the subscription. Doesn’t include price adjustment items
that are applied directly. A distributed price adjustment is automatically created to apply a
transaction-level adjustment to the transaction items. For example, let’s say that you have
an order with two order items: one for a file storage service and another for a video streaming
service. A 10% volume discount and a 15% manual discount are applied to the entire order.
An additional 20% discount is applied to the file storage service. To distribute the order-level
discounts, the system creates a 10% price adjustment item and a 15% price adjustment item
for each order item. In this example, the file storage service’s sales transaction shape item
has the following field values:

**•** `TotalAdjustmentAmount`  - The sum of all item-level adjustments, including
the 10% price adjustment item, the 15% price adjustment item, and the 20% price
adjustment item.

**•** `TotalAdjustmentDistAmount`  - The sum of the distributed item-level
adjustments, including the 10% price adjustment item and the 15% price adjustment
item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price before price adjustments, inclusive of quantity, prorated for the duration of
the subscription. This calculated field is equal to `StartingPriceTotal` times
`PricingTermCount` .

**Type**
currency


### Standard Objects SalesTransactionShape

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This calculated field is equal to `TotalAdjustmentAmount` plus
`StartingPriceTotal` .

### SalesTransactionShape

Defines the business logic for a sales transaction; for example, an order, a quote, or a cart. This object is available in API version 57.0 and
later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier for the account associated with this sales transaction shape. This field
is available when OrgPermissions or Platform is enabled.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


Standard Objects SalesTransactionShape

**Field** **Details**

```
SalesTransactionShapeName

TotalAdjustmentAmount

TotalAdjustmentDistAmount

TotalAmount

TotalListAmount

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the sales transaction shape. For example, Quote.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the sales transaction shape, inclusive of quantity,
prorated for the duration of the subscription. Includes distributed price adjustment items
and price adjustment items applied directly. This calculated field is equal to the sum of
`TotalAdjustmentAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the related sales transaction
shape items, inclusive of quantity, prorated for the duration of the subscription. Does not
include price adjustment items that are applied directly. This calculated field is equal to the
sum of `TotalAdjustmentDistAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final price of the sales transaction shape, after all adjustments, inclusive of quantity,
prorated for the duration of the subscription. This calculated field equal to the sum of
`TotalPrice` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


### Standard Objects SalesTransactionType

**Field** **Details**

**Description**
The sum of the list price of the related sales transaction shape items, inclusive of quantity,
prorated for the duration of the subscription. This calculated field is equal to the sum of
`ListPriceTotal` on the related sales transaction shape items.

```
TotalProductAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price of all related sales transaction shape items of type Product, before price
adjustments, inclusive of quantity, prorated for the duration of the subscription. This calculated
field is equal to the sum of `TotalLineAmount` on the related sales transaction shape
items of type Product.

### SalesTransactionType

Represents the type of sales transaction, such as an initial, renewal, or amendment sale, and its related pricing configuration.. This object
is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available when Revenue Cloud is enabled.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the sales transaction type.


### Standard Objects SalesTrxnItemRelationShape

**Field** **Details**

```
Name

PricingProcedureId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the sales transaction type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The pricing procedure related to the sales transaction type.

This field is a relationship field.

**Relationship Name**
PricingProcedure

**Refers To**
ExpressionSetDefinition

This object has the following associated objects.

**SalesTransactionTypeShare on page 67**
Sharing is available for the object.

### SalesTrxnItemRelationShape

Describes the relationship between sales transaction shape items; for example, a bundle or set. This object is available in API version 57.0
and later.

Supported Calls

`create() describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management, B2B Commerce, or B2C Commerce.


Standard Objects SalesTrxnItemRelationShape

Fields

**Field** **Details**

```
AssocSalesTrxnItemShapeId

AssocSalesTrxnItemShapeRole

AssociatedItemShapePricing

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the associated sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle component.

**Relationship Name**
AssocSalesTrxnItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated sales transaction shape item in the relationship.

Possible values are:

**•** `BundleComponent` —The associated sales transaction shape item is part of a bundle.

**•** `SetComponent` —The associated sales transaction shape item is part of a set.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes how the associated sales transaction shape item is priced, relative to the main
sales transaction shape item.

Possible values are:

**•** `IncludedInBundlePrice`  - The associated sales transaction shape item’s cost
is $0 because it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice`  - The associated sales transaction shape item
has a cost because it’s not included in the bundle’s price.


Standard Objects SalesTrxnItemRelationShape

**Field** **Details**

```
MainSalesTrxnItemShapeId

MainSalesTrxnItemShapeRole

ProductRelationshipTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the main sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle parent.

**Relationship Name**
MainSalesTrxnItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the position of the main sales transaction shape item in the relationship.

Possible values are:

**•** `AddOnComponent`  - The main sales transaction shape item is an add on component.
Available in API version 58.0 and later.

**•** `Bundle`  - The main sales transaction shape item is the bundle parent.

**•** `Set`  - The main sales transaction shape item is the set parent.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that describes the relationship between the main and associated sales
transaction shape items.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup


Standard Objects SalesTrxnItemRelationShape

**Field** **Details**

**Refers To**
ProductRelationshipType

```
QuantityScaleMethod

SalesTransactionShapeId

SalesTrxnItemRelationShapeName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How to scale the quantity of the associated sales transaction shape item, relative to the main
sales transaction shape item. The value is informative; the system doesn’t check whether the
scaled quantities are correct. If this field has a non-null value, you can't edit the associated
sales transaction shape item’s quantity.

Possible values are:

**•** `Constant` —The associated sales transaction’s item quantity remains the same in
relation to the main sales transaction shape item’s quantity. For example, let’s say that
the main sales transaction shape item has a quantity of one and the associated sales
transaction shape item has a quantity of one. If you increase the quantity of the main
sales transaction shape item to two, the associated sales transaction shape item’s quantity
remains at one.

**•** `Proportional` —The associated sales transaction’s item quantity increases or
decreases based on the main sales transaction shape item’s quantity. For example, let’s
say that the main sales transaction shape item has a quantity of one and the associated
sales transaction shape item has a quantity of two. If you increase the quantity of the
main order item to two, the associated order item’s quantity increases to four.

The default value is `Proportional` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related sales transaction shape.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

**Type**
string


### Standard Objects SalesTrxnItemRelationship

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Name of the relationship of the sales transaction shape item.

### SalesTrxnItemRelationship

Describes the relationship between sales transaction items; for example, a bundle or set. This object interface is available in API version
58.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object interface is available if Subscription Management is enabled.

Fields

**Field** **Details**

```
AssociatedItemPricing

AssociatedSalesTrxnItemId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes how the associated sales transaction item is priced, relative to the main sales
transaction item.

Possible values are:

**•** `IncludedInBundlePrice`  - The associated sales transaction item’s cost is $0
because it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice` —The associated sales transaction item has a
cost because it’s not included in the bundle’s price.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SalesTrxnItemRelationship

**Field** **Details**

**Description**
The unique identifier of the associated sales transaction item.

This field is a polymorphic relationship field. In a bundle relationship, this sales transaction
item is the bundle component.

**Relationship Name**
AssociatedSalesTrxnItem

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItem

```
AssociatedSalesTrxnItemRole

ImplementorType

MainSalesTrxnItemId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated sales transaction item in the relationship.

Possible values are:

**•** `AddOnComponent` —The associated sales transaction item is an add-on component.

**•** `BundleComponent` —The associated sales transaction item is part of a bundle.

**•** `ClassificationComponent` —The associated sales transaction item is a
classification component.

**•** `SetComponent` —The associated sales transaction item is part of a set.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object that is implementing this object interface; for example, an OrderProduct object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the main sales transaction item.

This field is a polymorphic relationship field. In a bundle relationship, this sales transaction
item is the bundle parent.

**Relationship Name**
MainSalesTrxnItem


Standard Objects SalesTrxnItemRelationship

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItem

```
MainSalesTrxnItemRole

ProductRelationshipTypeId

QuantityScaleMethod

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the position of the main sales transaction item in the relationship.

Possible values are:

**•** `Bundle` —The main sales transaction item is the bundle parent.

**•** `Set` —The main sales transaction item is the set parent.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the record that describes the relationship between the main and
associated sales transaction items.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How to scale the quantity of the associated sales transaction item, relative to the main sales
transaction item. The value is informative; the system doesn’t check whether the scaled
quantities are correct. If this field has a non-null value, you can't edit the associated sales
transaction item’s quantity.

Possible values are:


### Standard Objects SalesWorkQueueSettings

**Field** **Details**

**•** `Constant`                   - The associated sales transaction’s item quantity remains the same in
relation to the main sales transaction item’s quantity. For example, let’s say that the main
sales transaction item has a quantity of one and the associated sales transaction item
has a quantity of one. If you increase the quantity of the main sales transaction item to
two, the associated sales transaction item’s quantity remains at one.

**•** `Proportional`                   - The associated sales transaction’s item quantity increases or
decreases based on the main sales transaction item’s quantity. For example, let’s say that
the main sales transaction item has a quantity of one and the associated sales transaction
item has a quantity of two. If you increase the quantity of the main order item to two,
the associated order item’s quantity increases to four.

The default value is `Proportional` .

```
SalesTransactionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the sales transaction to which the main and associated sales
transaction items belong to.

This field is a polymorphic relationship field.

**Relationship Name**
SalesTransaction

**Relationship Type**
Lookup

**Refers To**
SalesTransaction

### SalesWorkQueueSettings

Represents settings used to customize work queue options for third-party scoring. Third-party scoring enables custom number fields
on person accounts, contacts, and leads. You must be a Sales Engagement customer to update this object. Previously, you could only
use the Einstein Intelligence Score for third-party scoring. Available starting in Version 47.0.

Note: This object can’t be packaged.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects SandboxStatusEventLog

Fields

**Field** **Details**

```
FeatureName

TargetEntity

TargetField

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A value that represents the name of the work queue settings.

To use custom number fields in the work queue, the value must be entered as
`ThirdPartyScore` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The related record object of the custom number field. Acceptable SObjects include
PersonAccount, Contact, and Lead.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the DeveloperName of the custom number field related to the
TargetEntity. Custom fields must have a custom number data type.

**•** To use Einstein Intelligence Score for lead scoring, enter
`ScoreIntelligence.Score` for the DeveloperName.

**•** To remove custom number fields from the work queue, enter `None` .

### SandboxStatusEventLog SandboxStatusEventLog stores details about Sandbox copies. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects SandboxStatusEventLog

Fields

**Field** **Details**

```
CurrentSandboxOrganizationIdentifier

PendingSandboxOrganizationIdentifier

RequestIdentifier

SandboxOrganizationIdentifier

Status

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the current sandbox organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the sandbox copy.

**Type**
dateTime


### Standard Objects SamlSsoConfig

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: 20130715233322.670.

```
UserIdentifier

### SamlSsoConfig

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: 00530000009M943YAS

.

Represents a SAML Single Sign-On configuration.This object is available in API version 32.0 and later.

Single sign-on is a process that allows network users to access all authorized network resources without having to log in separately to
each resource. Single sign-on allows you to validate usernames and passwords against your corporate user database or other client
application rather than having separate user passwords managed by Salesforce.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission or both the Customize Application and Modify
All Data permissions can access this object.

Fields

**Field Name** **Details**

```
AttributeFormat

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For SAML 2.0 only and when `identityLocation` is set to `Attribute` .
Possible values include `unspecified`, `emailAddress`, or `persistent` .


Standard Objects SamlSsoConfig

**Field Name** **Details**

All legal values can be found in the “Name Identifier Format Identifiers” section
[of the Assertions and Protocols SAML 2.0 specification.](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

```
AttributeName

Audience

DeveloperName

ErrorUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the identity provider’s application. Get this name value from your
identity provider.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The Issuer, also called the “Entity ID.” The value is a URL that uniquely identifies
the SAML identity provider.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
When there's an error during login, specify the URL of the page where users are
directed. It must be publicly accessible, such as a public site Visualforce page.
The URL can be absolute or relative.


Standard Objects SamlSsoConfig

**Field Name** **Details**

```
ExecutionUserID

IdentityLocation

IdentityMapping

Issuer

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The user that runs the Apex handler class. The user must have the “Manage Users”
permission. A user is required if you specify a SAML JIT handler class.

This is a relationship field.

**Relationship Name**
ExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The location in the assertion where a user is identified. Valid values are:

**•** `SubjectNameId` —The identity is in the `<Subject>` statement of the
assertion.

**•** `Attribute` —The identity is specified in an `<AttributeValue>`,
located in the `<Attribute>` of the assertion.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The identifier that the service provider uses for the user during Just-in-Time user
provisioning. Valid values are:

**•** `Username` —The user’s Salesforce username.

**•** `FederationId` —The federation ID from the user object; the identifier
that’s used by the service provider for the user.

**•** `UserId` —The user ID from the user’s Salesforce organization.

**Type**
string


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Properties**
Filter, idLookup, Group, Sort

**Description**
Also called the “Entity ID.” The value is a URL that uniquely identifies the SAML
identity provider.

```
Language

LoginUrl

LogoutUrl

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL where Salesforce sends a SAML request to start the
login sequence.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL to direct users to where they click the Logout link.
The default is `https://salesforce.com` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The text that’s used to identify the Visualforce page in the Setup area of Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
OptionsSpInitBinding

OptionsUseConfigRequestMethod

OptionsUseSameDigestAlgoForSigning

```

**Type**
boolean

**Properties**
Filter

**Description**

The service provider initiated request binding, either HTTP Redirect ( `true` ) or
HTTP POST ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, applies the selected Request Signature Method (RSM) during single
logout. If `false`, the default RSM ( `RSA-SHA1` ) is applied.

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, uses a SAML digest algorithm based on the selected Request Signature
Method (RSM). For example, if the selected RSM is `RSA-SHA256`, the digest
algorithm is set to `SHA-256` .

If `false`, uses the default digest algorithm ( `SHA-1` ), regardless of the selected
RSM.


Standard Objects SamlSsoConfig

**Field Name** **Details**

This field is available in API version 55.0 and later. You can edit this field only for
legacy SAML configurations created before the Spring ’22 release. For
configurations created after Spring ’22, this field is `true` by default.

```
OptionsRequireMfaSaml

OptionsUserProvisioning

RequestSignatureMethod

SamlJitHandlerId

```

**Type**
boolean

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this SAML
configuration based on the MFA status of each user. For this setting to trigger
MFA, you must apply MFA directly to users via one of two methods. 1) Assign
the user permission Multi-Factor Authentication for User Interface Logins. 2)
Enable the org setting Require multi-factor authentication (MFA) for all direct UI
logins to your Salesforce org.

**Type**
boolean

**Properties**
Filter

**Description**
If `true`, Just-in-Time user provisioning is enabled, which creates users on the
fly the first time that they try to log in. Specify `Federation ID` for the
`identityMapping` value to use this feature.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The method that’s used to sign the SAML request. Valid values are:

**•** `RSA-SHA1`

**•** `RSA-SHA256`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of an existing Apex class that implements the
`Auth.SamlJitHandler` interface.

This is a relationship field.


Standard Objects SamlSsoConfig

**Field Name** **Details**

**Relationship Name**
SamlJitHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

```
SingleLogoutBinding

SingleLogoutUrl

ValidationCert

Version

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Determines where to put the LogoutRequest or LogoutResponse in the SAML
request during single logout (SLO). The value is base64 encoded. Valid values
are:

**•** `RedirectBinding`  - Sent in the query string, deflated.

**•** `PostBinding`  - Sent in the POST body, not deflated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SAML single logout endpoint. This URL is the endpoint where Salesforce
sends LogoutRequests (when Salesforce initiates a logout), or LogoutResponses
(when the identity provider initiates a logout).

**Type**
string

**Properties**
Filter, Sort

**Description**
The certificate that’s used to validate the request. Get this certificate value from
your identity provider.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The SAML version. Valid values are:


### Standard Objects SavedPaymentMethod

**Field Name** **Details**

**•** `SAML1_1`

**•** `SAML2_2`

### SavedPaymentMethod

Represents a payment method saved by an authenticated customer. This object is available in API version 58.0 and later

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountHolderEmail

AccountHolderName

AsyncGatewayRefNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address of the payment method holder.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Full name of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort


Standard Objects SavedPaymentMethod

**Field** **Details**

**Description**
The payment transaction ID created by the payment gateway for asynchronous payments.
This field is available in API version 66.0 and later.

**•** For Adyen, use the pspReference.

**•** For Stripe, use the fingerprint value.

```
BankAccountHolderType

BankAccountType

BankCode

BankName

BillingAddress

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines whether the bank account is held by a business or an individual.

Possible values are:

**•** `Business`

**•** `Individual`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Characterizes the bank account, such as a checking or savings account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Code that represents the bank who issued the payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the bank that issued the payment method.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects SavedPaymentMethod

**Field** **Details**

**Description**
The billing address of the account holder of the payment method. This is the compound
form of the billing address. Read-only. For details on compound address fields, see Address
Compound Fields.

```
BillingCity

BillingCountry

BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 80 characters.

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

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects SavedPaymentMethod

**Field** **Details**

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

```
BillingPostalCode

BillingState

BillingStreet

ExpiryMonth

ExpiryYear

ExtendedPaymentMethodType

```

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Month the payment method expires.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Year the payment method expires.

**Type**
string


Standard Objects SavedPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Other saved payment methods used for the transaction. This field is required when the value
of the `Type` field is `extd_altrn_payment_method_type` or `extd_wallet` .
This field is available in API version 66.0 and later.

```
GatewayReference

GatewayToken

IsDefault

IsMerchantCreated

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A reference to the saved payment owner at the payment gateway. For example, a Stripe
customer ID.

**Type**
encryptedstring

**Properties**
Nillable

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the card
payment method during transactions. `GatewayToken` is for use with APIs earlier than
version 52.0. For version 53.0 and latter, use the GatewayTokenEncrypted field. To secure
the token, use the `GatewayTokenEncrypted` field.

An error message appears if you try to record a `GatewayToken` for a card payment
method that already has a `GatewayToken` or `GatewayTokenEncrypted` value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Customer’s default payment method.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the merchant saved the payment method on behalf of the payer. The
Payer must provide consent to the merchant to save this information.


Standard Objects SavedPaymentMethod

**Field** **Details**

The default value is `false` .

```
IsSharedWithinSameAccount

Issuer

Last4

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the saved payment method is visible to all contacts in an account ( `true` )
or only to the contact who created it ( `false` ). The default value is `false` .

This field is available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Financial institution issuing the payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Last four digits of the payment method account number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record or list view related to this
record, but didn’t access it directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user referenced this record but didn’t view it directly.


Standard Objects SavedPaymentMethod

**Field** **Details**

```
MerchantAccountId

Name

Network

Nickname

PaymentGatewayId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifies the Salesforce Payments Merchant Account.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the saved payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Saved payment method card network, for example Visa or Union Pay.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional name or label to easily identify the payment method.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects SavedPaymentMethod

**Field** **Details**

**Description**
The payment gateway that is used to create a gateway token. For transactions with a saved
payment method in Salesforce, this field stores the payment gateway ID used in the
transaction. This field is a relationship field.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

```
PaymentMethodSubType

ProcessingMode

ReferenceOwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of the Card payment method. This field
is available in API version 66.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the payment was made outside of the Salesforce platform. This field is
available in API version 66.0 and later.

Possible values are:

**•** `External`

**•** `Salesforce`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Account or Contact record that owns the payment method.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceOwner


Standard Objects SavedPaymentMethod

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account or Contact

```
StandardEntryClassCode

Status

Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A three-letter code that indicates how a customer or a business initiated and authorized an
ACH payment.

Possible values are:

**•** `CCD` —Corporate credit or debit entry

**•** `PPD` —Prearranged payment or deposit entry

**•** `TEL` —Telephone-initiated entry

**•** `WEB` —Internet or mobile-initiated entry

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the saved payment method.

Possible values are:

**•** `Active`

**•** `AwaitingPayment`

**•** `Errored` —Failed

**•** `Expired`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of saved payment method.

Possible values are:

**•** `au_becs_debit`

**•** `bacs_debit`

**•** `bancontact`


### Standard Objects SavedPaymentMethodEvent

**Field** **Details**

**•** `card`

**•** `extd_apm_type`

**•** `extd_wallet`

**•** `ideal`

**•** `sepa_debit`

**•** `us_bank_account`                   - ACH Direct Debit

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates if the payment method is used on or off session.

Possible values are:

**•** `OffSession`

**•** `OnSession`

**•** `RestrictedOffSession`

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**SavedPaymentMethodChangeEvent on page 68**
Change events are available for the object.

**SavedPaymentMethodFeed on page 55**
Feed tracking is available for the object.

**SavedPaymentMethodHistory on page 63**
History is available for tracked fields of the object.

**SavedPaymentMethodOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SavedPaymentMethodShare on page 67**
Sharing is available for the object.

### SavedPaymentMethodEvent

Represents a saved payment method platform event. Subscribe to these events so you can listen and respond to them when they’re
published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API
version 59.0 and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)


Standard Objects SavedPaymentMethodEvent

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

SavedPaymentMethodId

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of saved payment method event, which triggers an event notification. You can write
code to operate conditionally on the value of this field. For example, you can ignore a create
change but get notified of updates.

Possible values are:

**•** `Create` –Saved payment method created.

**•** `Delete` –Saved payment method deleted.

**•** `Update` –Saved payment method property changed.

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the SavedPaymentMethod record for which the event occurs.

This field is a relationship field.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod


### Standard Objects SchedulingAdherenceDetail SchedulingAdherenceDetail

Represents the breakdown of daily shift adherence data by agent status. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
IsShrinkage

Name

SchedulingAdherenceSummaryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the linked status is considered as shrinkage time ( `true` ) or not ( `false` ).
Shrinkage time is time, such as breaks, when an agent doesn’t receive work.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this detail record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Scheduling Adherence Summary.

This is a relationship field.

**Relationship Name**
SchedulingAdherenceSummary


### Standard Objects SchedulingAdherenceSummary

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
### SchedulingAdherenceSummary

```
StatusId

StatusName

TotalStatusMinutes

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the agent status represented by this detail record.

This is a relationship field.

**Relationship Name**
Status

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the agent status represented by this detail record.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present with this status.

### SchedulingAdherenceSummary

Represents daily shift adherence data for a service resource in a service territory and job profile on a specific date. This object is available
in API version 54.0 and later.


Standard Objects SchedulingAdherenceSummary

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
AdherencePercentage

ConformancePercentage

Date

```

**Type**
double

**Properties**
Filter, Sort

**Description**
Percentage of time that the agent was present during the scheduled shift time.

This is a calculated field.

**Formula**

```
  AdherencePercentage =

  TotalAdherenceMinutes / TotalScheduledMinutes

```

**Type**
double

**Properties**
Filter, Sort

**Description**
Percentage of time when the agent was present versus the duration of scheduled shifts. The
time that the agent is present can extend beyond the scheduled shift.

This is a calculated field.

**Formula**

```
  ConformancePercentage =

  TotalPresenceMinutes / TotalScheduledMinutes

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date for which the adherence data is calculated.


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
JobProfileId

JobProfileName

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the job profile.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the job profile.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this summary record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the schedule adherence summary.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
ServiceResourceId

ServiceResourceName

ServiceTerritoryId

ServiceTerritoryName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service resource.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service resource.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service territory.


Standard Objects SchedulingAdherenceSummary

**Field** **Details**

```
TotalAdherenceMinutes

TotalInteractionMinutes

TotalPresenceMinutes

TotalScheduledMinutes

TotalShrinkageMinutes

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present during a shift.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was actively receiving work.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total minutes of agent presence time.

This is a calculated field.

**Formula**

```
  TotalPresenceMinutes =

  TotalInteractionMinutes + TotalShrinkageMinutes

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Total minutes of scheduled shift time for the agent.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present but not receiving work, such as break times.


### Standard Objects SchedulingConstraint

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SchedulingAdherenceSummaryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SchedulingAdherenceSummaryShare on page 67**
Sharing is available for the object.

### SchedulingConstraint

Represents scheduling constraints on each service resource. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The org requires the Workforce Engagement license. To view records, the user requires the Workforce Engagement Agent permission
set. To create, edit, or delete records, the user requires the Workforce Engagement Planner permission set.

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MaxNonstandardShiftsPerMonth

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last modified. Its label in the user interface is
Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last viewed.

**Type**
int


Standard Objects SchedulingConstraint

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of non-standard shifts assigned to an agent in a month.

This field is available in API version 54.0 and later.

```
MaxShiftsPerDay

MaxShiftsPerMonth

MaxShiftsPerWeek

MaxWorkingHoursPerDay

MaxWorkingHoursPerMonth

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a day.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a week.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a day.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a month.


Standard Objects SchedulingConstraint

**Field** **Details**

```
MaxWorkingHoursPerWeek

Name

OwnerId

RestTimeMinutes

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a week.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling constraint record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the scheduling constraint.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum rest time, in minutes, between an agent’s consecutive shifts.

This field is available in API versions 56.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects SchedulingObjective

**SchedulingConstraintOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SchedulingConstraintShare on page 67**
Sharing is available for the object.

### SchedulingObjective

Represents business goals that the scheduling tools consider. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.

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
Create, Nillable, Update

**Description**
The scheduling objective description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects SchedulingRule

**Field** **Details**

**Description**
Possible values are the supported languages for Workforce Engagement.

```
MasterLabel

SchedulingCategory

SchedulingObjectiveType

### SchedulingRule

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling objective name.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The record that the scheduling objective applies to.

Possible values are:

**•** `A` —Appointment

**•** `B` —Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of scheduling objective.

Possible values are:

**•** `AgentPreference` —Scheduling tools consider agents’ service resource preferences.
In the UI, this value appears as Maximized Preferences.

**•** `BalanceNonStandardShifts` —Scheduling tools balance the number of shifts
across available agents within a time period.

**•** `BalanceShifts` —Scheduling tools balance the number of non-standard shifts
across available agents within a time period.

Represents scheduling rules that are hard constraints in the scheduling logic engine. This object is available in API version 52.0 and later.


Standard Objects SchedulingRule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The scheduling rule description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name value of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the scheduling rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling rule name.


### Standard Objects SchedulingRuleParameter

**Field** **Details**

```
SchedulingCategory

SchedulingRuleType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shifts.

Possible values are:

**•** `A` —Appointment

**•** `B` —Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The scheduling rule type.

Possible values are:

**•** `A` —Active Resources

**•** `B` —Match Skills

**•** `C` —Availability

**•** `LimitNonstandardShifts` —Specifies a rule type that limits how many
non-standard shifts can be assigned to each agent. This type is available in API version
54.0 and later.

**•** `M` —Match Territory

**•** `Q` —Match Queues

**•** `RestTimeMinutes` —Specifies a rule type that requires the agent to have a minimum
rest time between consecutive shifts. This type is available in API version 56.0 and later.

**•** `W` —Work Limit

### SchedulingRuleParameter

Represents scheduling rule parameters associated with a scheduling rule. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects SchedulingRuleParameter

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user needs to have the Workforce
Engagement Planner permission set.

Fields

**Field** **Details**

```
SchedulingParameterKey

SchedulingRuleId

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The scheduling rule parameter name.

Possible values are:

**•** `ConsiderAbsence` —Consider absences when determining a service resource’s
availability. This type is available in API version 56.0 and later.

**•** `ConsiderSTM` —Consider service territory membership when determining a service
resource’s availability. Service territory membership defines the resource’s working hours
in a location. This type is available in API version 56.0 and later.

**•** `C` —Constraint Field Name

**•** `L` —Limit Type

**•** `R` —Resolution

**•** `T` —Time Resolution

**•** `W` —Work Unit

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The scheduling rule ID.

This is a relationship field.

**Relationship Name**
SchedulingRule

**Relationship Type**
Lookup

**Refers To**
SchedulingRule

**Type**
string


### Standard Objects Scontrol

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The scheduling rule parameter value.

### Scontrol

A custom s-control, which is custom content that is hosted by the system but executed by the client application.

Important: Visualforce pages supersede s-controls. Organizations that haven’t previously used s-controls can’t create them.
Existing s-controls are unaffected, and can still be edited. We recommend that you move your s-controls to Visualforce. We continue
to support the Scontrol object.

Represents a custom s-control, which is custom content that the system hosts, but client applications execute. An s-control can contain
any type of content that you can display or run in a Web browser.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Enterprise, Developer, or Unlimited Edition and be enabled for custom s-controls.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Binary

BodyLength

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Binary content of this custom s-control, such as an ActiveX control or a Java archive. Can be
specified when created, but not when updated. Limit: 5 MB.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects Scontrol

**Field** **Details**

**Description**
The length of the custom s-control. Label is **Binary Length** .

```
ContentSource

Description

DeveloperName

EncodingKey

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the source of the s-control content, either custom HTML, a snippet (s-controls that
are included in other s-controls), or a URL.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the custom s-control.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **S-Control Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Picklist of character set encodings, including ISO-08859-1, UTF-8, EUC, JIS, Shift-JIS, Korean
(ks_c_5601-1987), Simplified Chinese (GB2312), and Traditional Chinese (Big5).


Standard Objects Scontrol

**Field** **Details**

```
Filename

HtmlWrapper

Name

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An uploaded object to display when the custom s-control is added to a custom link. Can be
a Java applet, an ActiveX control, or any other type of desired content.

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. HTML page that will be delivered when the user views this custom s-control. This
HTML page can be the entire content of the custom s-control, or it can reference the binary.
Limit: 1,048,576 characters. Label is **HTML Body** .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Name of this custom s-control. Label is **Label** .

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


### Standard Objects ScontrolLocalization

**Field** **Details**

```
SupportsCaching

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the s-control supports caching ( `true` ) or not ( `false` ).

Use custom s-controls to manage custom content that extends application functionality. All users can view custom s-controls, but the
“Customize Application” permission is required to create or update custom s-controls.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ScontrolLocalization

The translated value of the field label for an s-control.

Important: Visualforce pages supersede s-controls. Organizations that haven’t previously used s-controls can’t create them.
Existing s-controls are unaffected, and can still be edited.

When the Translation Workbench is enabled for your organization, provides the translation of the field label of an s-control.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, or Unlimited Edition and be enabled for the Translation
Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
LanguageLocaleKey

```

**Type**
picklist


Standard Objects ScontrolLocalization

**Field** **Details**

**Properties**
Create,

Filter,

Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

This picklist contains the following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in
English.

The following end-user only languages are available.

**•** Arabic: `ar`


Standard Objects ScontrolLocalization

**Field** **Details**

**•** Bulgarian: `bg`

**•** Croatian: `hr`

**•** Czech: `cs`

**•** English (UK): `en_GB`

**•** Greek: `el`

**•** Hebrew: `iw`

**•** Hungarian: `hu`

**•** Indonesian: `in`

**•** Polish: `pl`

**•** Portuguese (European): `pt_PT`

**•** Romanian: `ro`

**•** Slovak: `sk`

**•** Slovenian: `sl`

**•** Turkish: `tr`

**•** Ukrainian: `uk`

**•** Vietnamese: `vi`

The following platform languages are available for organizations that use Salesforce
exclusively as a platform.

**•** Albanian: `sq`

**•** Afrikaans: `af`

**•** Amharic: `am`

**•** Arabic (Algeria): `ar_DZ`

**•** Arabic (Bahrain): `ar_BH`

**•** Arabic (Egypt): `ar_EG`

**•** Arabic (Iraq): `ar_IQ`

**•** Arabic (Jordan): `ar_JO`

**•** Arabic (Kuwait): `ar_KW`

**•** Arabic (Lebanon): `ar_LB`

**•** Arabic (Libya): `ar_LY`

**•** Arabic (Morocco): `ar_MA`

**•** Arabic (Oman): `ar_OM`

**•** Arabic (Qatar): `ar_QA`

**•** Arabic (Saudi Arabia): `ar_SA`

**•** Arabic (Sudan): `ar_SD`

**•** Arabic (Syria): `ar_SY`

**•** Arabic (Tunisia): `ar_TN`

**•** Arabic (United Arab Emirates): `ar_AE`

**•** Arabic (Yemen): `ar_YE`


Standard Objects ScontrolLocalization

**Field** **Details**

**•** Armenian: `hy`

**•** Basque: `eu`

**•** Bosnian: `bs`

**•** Bengali: `bn`

**•** Burmese: `my`

**•** Catalan: `ca`

**•** Chinese (Hong Kong): `zh_HK`

**•** Chinese (Singapore): `zh_SG`

**•** Chinese (Malaysia): `zh_MY`

**•** Dutch (Belgium): `nl_BE`

**•** English (Australia): `en_AU`

**•** English (Belgium): `en_BE`

**•** English (Canada): `en_CA`

**•** English (Cyprus): `en_CY`

**•** English (Germany): `en_DE`

**•** English (Hong Kong): `en_HK`

**•** English (India): `en_IN`

**•** English (Ireland): `en_IE`

**•** English (Israel): `en_IL`

**•** English (Malaysia): `en_MY`

**•** English (Malta): `en_MT`

**•** English (Netherlands): `en_NL`

**•** English (New Zealand): `en_NZ`

**•** English (Philippines): `en_PH`

**•** English (Singapore): `en_SG`

**•** English (South Africa): `en_ZA`

**•** English (United Arab Emirates): `en_AE`

**•** Estonian: `et`

**•** Farsi: `fa`

**•** French (Belgium): `fr_BE`

**•** French (Canada): `fr_CA`

**•** French (Luxembourg): `fr_LU`

**•** French (Morocco): `fr_MA`

**•** French (Switzerland): `fr_CH`

**•** Georgian: `ka`

**•** German (Austria): `de_AT`

**•** German (Belgium): `de_BE`

**•** German (Luxembourg): `de_LU`


Standard Objects ScontrolLocalization

**Field** **Details**

**•** German (Switzerland): `de_CH`

**•** Greek (Cyprus): `el_CY`

**•** Greenlandic: `kl`

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Icelandic: `is`

**•** Irish: `ga`

**•** Italian (Switzerland): `it_CH`

**•** Kannada: `kn`

**•** Kazakh: `kk`

**•** Khmer: `km`

**•** Latvian: `lv`

**•** Lithuanian: `lt`

**•** Luxembourgish: `lb`

**•** Macedonian: `mk`

**•** Malay: `ms`

**•** Malayalam: `ml`

**•** Maltese: `mt`

**•** Marathi: `mr`

**•** Montenegrin: `sh_ME`

**•** Romanian (Moldova): `ro_MD`

**•** Romansh: `rm`

**•** Russian (Armenia): `ru_AM`

**•** Russian (Belarus): `ru_BY`

**•** Russian (Kazakhstan): `ru_KZ`

**•** Russian (Kyrgyzstan): `ru_KG`

**•** Russian (Lithuania): `ru_LT`

**•** Russian (Moldova): `ru_MD`

**•** Russian (Poland): `ru_PL`

**•** Russian (Ukraine): `ru_UA`

**•** Samoan: `sm`

**•** Serbian (Cyrillic): `sr`

**•** Serbian (Latin): `sh`

**•** Spanish (Argentina): `es_AR`

**•** Spanish (Bolivia): `es_BO`

**•** Spanish (Chile): `es_CL`


Standard Objects ScontrolLocalization

**Field** **Details**

**•** Spanish (Colombia): `es_CO`

**•** Spanish (Costa Rica): `es_CR`

**•** Spanish (Dominican Republic): `es_DO`

**•** Spanish (Ecuador): `es_EC`

**•** Spanish (El Salvador): `es_SV`

**•** Spanish (Guatemala): `es_GT`

**•** Spanish (Honduras): `es_HN`

**•** Spanish (Nicaragua): `es_NI`

**•** Spanish (Panama): `es_PA`

**•** Spanish (Paraguay): `es_PY`

**•** Spanish (Peru): `es_PE`

**•** Spanish (Puerto Rico): `es_PR`

**•** Spanish (United States): `es_US`

**•** Spanish (Uruguay): `es_UY`

**•** Spanish (Venezuela): `es_VE`

**•** Swahili: `sw`

**•** Tagalog: `tl`

**•** Tamil: `ta`

**•** Te reo: `mi`

**•** Telugu: `te`

**•** Urdu: `ur`

**•** Welsh: `cy`

**•** Xhosa: `xh`

**•** Zulu: `zu`

The values in this field are not related to the default locale selection.

```
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed


### Standard Objects Scorecard

**Field** **Details**

managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 ScontrolId

 Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Scontrol that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated field label of the s-control. Label is **Translation** .

Use this object to translate your s-controls into a supported language. Users with the Translation Workbench enabled can view s-control
translations, but either the “Customize Application” or “Manage Translation” permission is required to create or update s-control
translations.

SEE ALSO:

CategoryNodeLocalization

WebLinkLocalization

### Scorecard

Use scorecards to measure partner performance and establish benchmarks for channel programs within Experience Cloud. Display any
report summary results that your channel account manager or executive team wants to see. This object is available in API version 40.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects Scorecard

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the scorecard.

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
The name of the scorecard visible to end users.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the scorecard.

This is a polymorphic relationship field.


### Standard Objects ScorecardAssociation

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

The Scorecard object is used in tandem with the ScorecardMetric and ScorecardAssociation objects.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ScorecardOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ScorecardShare on page 67**
Sharing is available for the object.

### ScorecardAssociation

Represents a connection between a specific scorecard and the associated account, channel program, or channel program level. This
object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects ScorecardAssociation

**Field** **Details**

```
LastViewedDate

Name

ScorecardId

TargetEntityId

```

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Scorecard Association.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the scorecard that the association is related to. Several metrics can be tied to a
single scorecard.

This is a relationship field.

**Relationship Name**
Scorecard

**Relationship Type**
Lookup

**Refers To**
Scorecard

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated object that a specific scorecard is associated with.

This is a polymorphic relationship field.

**Relationship Name**
TargetEntity


### Standard Objects ScorecardMetric

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, ChannelProgram, ChannelProgramLevel

### ScorecardMetric

Stores information about a Salesforce report that is run and summarized to get a single value. The stored value is added as a metric to
the related Scorecard object. This object is available in API version 40.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Category

Description

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Groups metrics together. It comes with a predefined set of dropdown list entries and can
be extended to address vendor’s needs each category is user-generated and can be localized
through translation workbench.

Possible values are:

**•** `Adoption`

**•** `Field Enablement`

**•** `Marketing`

**•** `Sales`

**•** `Support`

The default value is 'Sales'.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ScorecardMetric

**Field** **Details**

**Description**
The description of the metric that appears on a scorecard.

```
Name

ReportId

ScorecardId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric that appears on a scorecard.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the report that is run and summarized to return a single value.

This is a relationship field.

**Relationship Name**
Report

**Relationship Type**
Lookup

**Refers To**
Report

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the scorecard that the metric is related to. Several metrics can be tied to a single
scorecard.

This is a relationship field.

**Relationship Name**
Scorecard

**Relationship Type**
Lookup

**Refers To**
Scorecard


### Standard Objects ScoreIntelligence ScoreIntelligence

For internal use only.

### ScratchOrgInfo

Represents a scratch org and its audit log. Use this object to create a scratch org and keep a log of its creation and deletion. This object
is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AdminEmail

AuthCode

ConnectedAppCallbackUrl

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The email address of the scratch org’s Administration user. The read only
`SignupEmail` field is populated with this value. If you don't provide a value
for `AdminEmail`, the field is left blank and the `SignupEmail` is populated
with the email address of the org user who is creating this object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A one-time authorization code that can be exchanged for an OAuth access token
and refresh token using standard Salesforce APIs. It’s used with
`ConnectedAppCallbackUrl` and `ConnectedAppConsumerKey`,
when the specified connected app hasn't been configured with an X.509
certificate. This field is read only.

**Type**
textarea

**Properties**
Create


Standard Objects ScratchOrgInfo

**Field Name** **Details**

**Description**
Required. When used with `ConnectedAppConsumerKey`, it specifies the
callback URL used for OAuth. If using Salesforce CLI, the default is
`http://localhost:1717/OauthRedirect` .

```
ConnectedAppConsumerKey

Country

DeletedBy

DeletedDate

Description

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. When used with `ConnectedAppCallbackUrl`, it specifies the
connected app that is approved automatically during scratch org creation. If
using Salesforce CLI and the default connected app, indicate `PlatformCLI` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The two-character, upper-case ISO-3166 country code. You can find a full list of
these codes at several sites, such as:
[www.iso.ch/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html.](http://www.iso.ch/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html)
The language of the scratch org is auto-determined based on the value of this
field. If you don’t specify a value, this field defaults to the Dev Hub’s country code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who requested that the scratch org be deleted. This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the `DeletedBy` user requested that the scratch org be deleted.
This field is read only.

**Type**
textarea


Standard Objects ScratchOrgInfo

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
A free-form text field for you to enter a description of this scratch org.

```
DurationDays

Edition

ErrorCode

ExpirationDate

Features

```

**Type**
int

**Properties**
Create, Filter, Nillable, Group, Sort

**Description**
Number of days after which the scratch org expires. Valid values are 1–30. The
default is 7.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required if you don’t provide Snapshot or SourceOrg. The org edition of this
scratch org. Valid values are `Group`, `Developer`, `Enterprise`, and
`Professional` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code if the scratch org creation isn’t successful. This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org expires. This field is read only.

**Type**
textarea

**Properties**
Create, Nillable


Standard Objects ScratchOrgInfo

**Field Name** **Details**

**Description**
A semi-colon delimited list of the features enabled in this scratch org, such as
MultiCurrency. See the _Salesforce DX Developer Guide_ for the full list of valid
features.

```
HasSampleData

Language

LastLoginDate

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the scratch org contains sample data. If set to `true`, the
sample data is similar to the data in a Salesforce free trial org.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the scratch org being created. Specify the language using a
language code listed under "Supported Languages" in Salesforce Help. For
example, use `zh_CN` for simplified Chinese. The value you select overrides the
language set by locale.

If you don’t specify a value, the language is based on the `Country` used during
scratch org creation. If you don’t specify a value for `Country`, the value defaults
to the Dev Hub’s country.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date of the last user login to the scratch org. This field is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record. This field is read only.


Standard Objects ScratchOrgInfo

**Field Name** **Details**

```
LastViewedDate

LoginUrl

Name

Namespace

OrgName

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, and `LastReferenceDate` isn’t null, the user accessed this
record or list view indirectly. This field is read only.

**Type**
textarea

**Properties**
Nillable

**Description**
A URL that logs you in to the scratch org. This field is read only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated ID of this scratch org. This field is read only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The namespace you want to associate with this scratch org. The value of this field
corresponds to the `NamespacePrefix` field of the `NamespaceRegistry`
object that describes your namespace.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The name of the scratch org. This name appears as the Organization
Name in the Company Information Setup page.

**Type**
reference


Standard Objects ScratchOrgInfo

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this scratch org.

```
Release

ScratchOrg

SignupCountry

SignupEmail

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The release of the scratch org. During Salesforce's major release transitions, this
field allows you to select the Salesforce release version, based on the version of
your Dev Hub. This field is available in API version 46.0 and later. Valid values are:

**•** Current

**•** Preview

**•** Previous

[See Select the Salesforce Release for a Scratch Org for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_version_selection.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org ID of the scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The country code of the scratch org. This field is populated with the value of the
`Country` field. If you didn’t provide a value for `Country`, it’s the country
code of the Dev Hub. This field is read only.

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
The email address of the scratch org’s Administration user. This field is populated
with the value of the `AdminEmail` field. If you didn't provide a value for


Standard Objects ScratchOrgInfo

**Field Name** **Details**

`AdminEmail`, it's the email address of your user in the Dev Hub. This field is
read only.

```
SignupInstance

SignupLanguage

SignupTrialDays

SignupUsername

Snapshot

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce instance on which this scratch org resides. This field is read only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the scratch org. This field is populated with the value of the
`Language` field. If you didn’t provide a value for `Language`, it’s the language
of the Dev Hub. This field is read only.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days between the scratch org's creation and expiration. This field
is read only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The username of the Administration user of this scratch org. This field is populated
with the value of the `Username` field. If you didn’t provide a value for
`Username`, the value of this field is auto-generated. This field is read only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects ScratchOrgInfo

**Field Name** **Details**

**Description**
If this scratch org was created from a scratch org snapshot, then this field contains
either the name or ID of the snapshot. Specifically, the name corresponds to the
`Name` field of the snapshot’s record in the OrgSnapshot standard object; the ID
corresponds to the record ID.

If this scratch org wasn’t created from a snapshot, this field is empty.

If you specify `Snapshot`, you can’t specify `Edition` or `SourceOrg` .

This field is available in API version 61.0 and later.

```
SourceOrg

Status

Username

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the org whose shape (features, settings, limits, and licenses) information
is used for creating scratch orgs. If you specify `SourceOrg`, you can’t specify
`Edition` or `Snapshot` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the scratch org, such as active, expired, or deleted. This field is read
only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The username of the Administration user of this scratch org.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ScratchOrgInfoFeed**

Feed tracking is available for the object.

**ScratchOrgInfoHistory**

History is available for tracked fields of the object.


### Standard Objects SearchActivity

**ScratchOrgInfoShare**

Sharing is available for the object.

SEE ALSO:

ActiveScratchOrg

NamespaceRegistry

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev)_

### SearchActivity

Represents search activity on a Knowledge article. Also known as KnowledgeSearchActivity. This object is available in API version 38.0
and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

The Knowledge Base Search Dashboard permission must be enabled in your org.

Fields

**Field** **Details**

```
AvgNumResults

ClickRank

ClickedRecordId

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The number of search results returned for the search term. If Period is also included, this
value is aggregated based on the time period specified.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that the article appeared in the search results when the user sorted the results by
relevance and clicked it from the list of results.

**Type**
reference


Standard Objects SearchActivity

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the clicked article.

This field is a polymorphic relationship field.

**Relationship Name**
ClickedRecord

**Relationship Type**
Lookup

**Refers To**
Knowledge__kav

```
ClickedRecordName

CountQueries

CountUsers

KbChannel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the clicked article taken when the user sorts the search results by relevance.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of searches for the period (day, month, or year).

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of individual users who clicked the article.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The channel that’s applicable to the article.

Possible values are:

**•** `AllChannels` —All Channels


Standard Objects SearchActivity

**Field** **Details**

**•** `App` —Internal App

**•** `Csp` —Customer

**•** `Pkb` —Public Knowledge Base

**•** `Prm` —Partner

```
Name

Period

QueryDate

QueryLanguage

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of search activity.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The time period that the search count is applied to. For example, a record where the Count
is 70 and the Period is Monthly indicates that 70 searches took place over the past month.
Totals are aggregated daily for the current month, monthly from the past full month through
the past full year, and yearly beyond that.

Activity totals are collected nightly and aren’t in real time.

Possible values are:

**•** `DAY`

**•** `MONTH`

**•** `YEAR`

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date of the search.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language filter that’s applied to the user’s search.


### Standard Objects SearchClickEventLog

**Field** **Details**

```
SearchTerm

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first 100 characters of the search term that was used to search published articles in the
knowledge base.

### SearchClickEventLog

Search Click Event Log contains details about the user’s interaction with the search results. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClickedRecordIdentifier

QueryIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the result the user clicked in the search results page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the search query.


### Standard Objects SearchEventLog

**Field** **Details**

```
Rank

RequestIdentifier

Timestamp

UserIdentifier

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ranking of the result clicked in the search results page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

All searches within the app, including Experience Cloud sites, are included. However, unauthenticated guest users don’t have a unique
Salesforce user ID.

### SearchEventLog

Search Event Log provides details about the user’s search query. This object is available in API version 61.0 and later.


Standard Objects SearchEventLog

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
PrefixesSearched

QueryIdentifier

RequestIdentifier

ResultCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A space-delineated list of key prefixes that are searched.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the search query.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of results returned by the search query.


### Standard Objects SearchLayout

**Field** **Details**

```
SearchQuery

Timestamp

UserIdentifier

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first 100 characters of the search query.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

All searches within the app, including Experience Cloud sites, are included. However, unauthenticated guest users don’t have a unique
Salesforce user ID.

### SearchLayout

Represents a search layout defined for an object. This object is available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

Users with the View Setup and Configuration permission can access this object.


Standard Objects SearchLayout

Fields

**Field** **Details**

```
ButtonsDisplayed

DurableId

EntityDefinitionId

FieldsDisplayed

```

**Type**

[SearchLayoutButtonsDisplayed](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_searchlayout.htm#searchlayoutbuttonsdisplayed)

**Properties**
Nillable

**Description**

The list of buttons available in list views for an object.

This field is equivalent to the `listViewButtons` [field on SearchLayouts](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_searchlayouts.htm) in Metadata
API.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. `DurableId` in queries allows
you to find the right record without having to retrieve the entire record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record in `EntityDefinition` . Use in subqueries.

This field is a relationship field.

**Relationship Name**
EntityDefinition

**Refers To**
EntityDefinition

**Type**

[SearchLayoutFieldsDisplayed](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_searchlayout.htm#searchlayoutfieldsdisplayed)

**Properties**
Nillable

**Description**

The list of fields displayed in a search result for the object. The name field is required. It’s
always displayed as the first column header, so it isn’t included in this list; all additional fields
are included. The field name relative to the object name, for example MyCustomField__c,
is specified for each custom field.


Standard Objects SearchLayout

**Field** **Details**

This field is equivalent to `searchResultsAdditionalFields` [on SearchLayouts](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_searchlayouts.htm)
in Metadata API.

```
Label

LayoutType

ListLayout

Profile

ProfileName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for this search layout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of search layout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Identifies the list layout a search layout is related to. Available
in API version 48.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Unique identifier for the field. Identifies the profile to which a search layout applies. Available
in API version 48.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the profile to which a search layout applies. Available in API version 48.0 and
later.


### Standard Objects SearchPromotionRule

Usage

Use the SearchLayout object to control the fields displayed and actions available to a user profile. The search layout applies to global
and lookup searches.

### SearchPromotionRule

Represents a promoted search term, which is one or more keywords that you associate with a Salesforce Knowledge article. When a
user’s search query includes these keywords, the associated article is returned first in search results. This object is available in API version
31.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

A user must have the “Manage Promoted Search Terms” permission.

Fields

**Field Name** **Details**

```
PromotedEntityId

Query

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the KnowledgeArticleVersion that the promoted search term is
associated with. The article must be in published status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text of the promoted search term. Maximum length: 100 characters.

You can associate the same promoted search term with multiple articles. If the
user’s search matches the promoted term, all associated articles are promoted
in search results, ordered by relevancy. For best results, create promoted search
terms selectively and limit the number of articles that are promoted per term.


### Standard Objects SecurityCustomBaseline

Usage

Use this object to optimize article search results in Salesforce Knowledge.

### SecurityCustomBaseline

Provides the ability to read, create, and delete user-defined custom security baselines, which define an org’s security standards. This
object is available in API version 39.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “View Health Check” permission to read a custom baseline, and the “Manage Health Check” permission to create,
edit, or delete one.

Fields

**Field Name** **Details**

```
Baseline

DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The definition of an org’s security settings standards.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


### Standard Objects SelfServiceUser

**Field Name** **Details**

```
IsDefault

Language

MasterLabel

NamespacePrefix

### SelfServiceUser

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Sets the baseline as the default in Security Health Check.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the package.

Represents a Contact who has been enabled to use your organization’s Self-Service portal, where he or she can obtain online support.

Note: Starting with Spring ’12, the Self-Service portal isn’t available for new Salesforce orgs. Existing orgs continue to have access
to the Self-Service portal.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects SelfServiceUser

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ContactId

Email

FirstName

IsActive

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. All Self-Service users must be associated with a Contact. The contact’s email should
match the Self-Service user email. The contact must have a value in the `AccountId` field
or an error occurs.

**Type**
email

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Make this the same as the email address for the Contact associated with this
SelfServiceUser. Password resets and other system communication will be sent to this email
address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the Self-Service user.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Self-Service user is allowed to log in to the Self-Service portal ( `true` )
or not ( `false` ). Note that there is no way to delete a Self-Service user. They can only be
marked as inactive.

**Type**
boolean


Standard Objects SelfServiceUser

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
LanguageLocaleKey

LastLoginDate

LastName

LocaleSidKey

Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. It is the primary language for the user. All on-screen
text in the Self-Service portal is displayed in this language.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the Self-Service user last logged in.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the Self-Service user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. The value of this field affects the formatting and
parsing of values, especially numeric values, in the Self-Service portal. Values are two-letter
codes that indicate language and sometimes language and country. The codes are based
on ISO standards.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects SelfServiceUser

**Field** **Details**

**Description**
Concatenation of `FirstName` and `LastName` . Limited to 203 characters, including
whitespaces.

```
 SuperUser

 TimeZoneSidKey

 Username

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this Self-Service user is a super user with additional access on his or her
company's Self-Service portal ( `true` ) or not ( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. The time zone of a affects the offset used when
displaying or entering times in the Self-Service portal.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This contains the name that a Self-Service user enters to log into the Self-Service
portal. Value must be unique in your organization. If you try to create or update a user with
a duplicate value, the operation is rejected and an error is returned.

For security reasons, you can’t query Self-Service user passwords via the API or the user interface. However, the API allows you to set and
reset Self-Service user passwords using the `setPassword()` and `resetPassword()` calls.

SelfServiceUser records created from the API don’t cause a notification email to be sent. If you want to notify the user, you must send
them an email after creating the user.

SEE ALSO:

Contact

User


### Standard Objects Seller Seller

Represents the seller role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the seller’s role became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the seller’s role is no longer active.

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


Standard Objects Seller

**Field** **Details**

```
Name

OwnerId

PartyId

SalesAmount

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this seller.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this seller.

This is a polymorphic relationship field.

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
Required. Represents the record based on the Individual object you want to associate the
seller with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SenderEmailAddress

**Field** **Details**

**Description**
The total revenue amount gained from this seller.

```
SellerTier

SellerType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The tier at which this seller is ranked.

Possible values are:

**•** `Bronze`

**•** `Gold`

**•** `Silver`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of sales this seller specializes in.

Possible values are:

**•** `Distributor`

**•** `Reseller`

**•** `SalesPartner`

**•** `Wholesaler`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SellerHistory on page 63**
History is available for tracked fields of the object.

**SellerShare on page 67**
Sharing is available for the object.

### SenderEmailAddress

Represents a From address in a marketing email. This object is available in API version 63.0 and later.


Standard Objects SenderEmailAddress

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DisplayName

EmailDomainKeyId

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive name that makes the sender email address easier to identify.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique system ID of the domain associated with the sender email address.

This field is a relationship field.

**Relationship Name**
EmailDomainKey

**Refers To**
EmailDomainKey

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique identifier for the sender email address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique user ID of the user who owns the sender email address object.

This field is a polymorphic relationship field.


### Standard Objects ServiceAppointment

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
Group, User

```
Username

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The part of the email address that comes before the @ symbol.

### ServiceAppointment

Represents an appointment to complete work for a customer in Field Service, Lightning Scheduler,Intelligent Appointment Management,
and Virtual Care.This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The account associated with the appointment. If the parent record
is a work order or work order line item, this field’s value is inherited from the
parent. Otherwise, it remains blank.

This is a relationship field.

**Relationship Name**
Account


Standard Objects ServiceAppointment

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
ActualDuration

ActualEndTime

ActualStartTime

Address

AppointmentNumber

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that it took the resource to complete the appointment
after arriving at the address. When values are first added to the `Actual`
`Start` and `Actual End` fields, the `Actual Duration` is automatically
populated to list the difference between the `Actual Start` and `Actual`
`End` . If the `Actual Start` and `Actual End` fields are subsequently
updated, the `Actual Duration` field doesn’t re-update, but you can
manually update it.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual date and time the appointment ended.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual date and time the appointment started.

**Type**
address

**Properties**
Filter

**Description**
The address where the appointment is taking place. The address is inherited from
the parent record if the parent record is a work order or work order line item.

**Type**
string


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the appointment.

```
ArrivalWindowEndTime

ArrivalWindowStartTime

BundlePolicyId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the window of time in which the technician is scheduled to arrive at
the site. This window is typically larger than the Scheduled Start and End window
to allow time for delays and scheduling changes. You may choose to share the
Arrival Window Start and End with the customer, but keep the Scheduled Start
and End internal-only.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The beginning of the window of time in which the technician is scheduled to
arrive at the site. This window is typically larger than the Scheduled Start and
End window to allow time for delays and scheduling changes. You may choose
to share the Arrival Window Start and End with the customer, but keep the
Scheduled Start and End internal-only.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the bundle policy associated with this service appointment.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ServiceAppointment

**Field Name** **Details**

```
City

ContactId

Country

Description

DueDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the appointment is completed. Maximum length is 40 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the parent record. If needed, you can manually
update the service appointment contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the work order is completed. Maximum length is 80 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the appointment.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


Standard Objects ServiceAppointment

**Field Name** **Details**

**Description**
The date by which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

```
Duration

DurationType

EarliestStartTime

GeocodeAccuracy

IsAnonymousBooking

```

**Type**
double

**Properties**
Create, Nillable, Filter, Sort, Update

**Description**
The estimated length of the appointment. If the parent record is work order or
work order line item, the appointment inherits its parent’s duration, but it can
be manually updated. The duration is in minutes or hours based on the value
selected in the `Duration Type` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the Duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date after which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
boolean


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a service resource was automatically assigned to the
appointment. The default value is false.

This field is available in API version 49.0 and later.

```
IsBundle

IsBundleMember

IsManuallyBundled

IsOffsiteAppointment

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle service appointment. The default
value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle member service appointment.
The default value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this bundle was created manually. The default value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any type of work that can be done remotely.

This field is available in API version 58.0 and later.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Latitude

Longitude

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with `Longitude` to specify the precise geolocation of the address where
the service appointments is completed. Acceptable values are numbers between
–90 and 90 with up to 15 decimal places.

To integrate data from an external data source for latitude, map your data to the
`ServiceAppointment.Latitude` and not the

```
  ServiceAppointment.FSL__InternalSLRGeolocation__Latitude__s
```

field.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with `Latitude` to specify the precise geolocation of the address where
the service appointment is completed. Acceptable values are numbers between
–180 and 180 with up to 15 decimal places.

To integrate data from an external data source for longitude, map your data to
the `ServiceAppointment.Longitude` and not the

```
  ServiceAppointment.FSL__InternalSLRGeolocation__Longitude__s
```

field.


Standard Objects ServiceAppointment

**Field Name** **Details**

Note: This field is available in the API only.

```
OwnerId

ParentRecordId

ParentRecordStatusCategory

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service appointment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The parent record associated with the appointment. The parent record can’t be
updated after the service appointment is created.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account, Asset, Lead, Opportunity, ServiceAppointmentGroup, WorkOrder,
WorkOrderLineItem

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read only) The `Status Category` of the parent record. If the parent record
is a work order or work order line item, this field is populated; otherwise, it remains
blank.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
ParentRecordType

PostalCode

RelatedBundleId

SchedEndTime

SchedStartTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of parent record: Account, Asset, Lead, Opportunity, Work
Order, or Work Order Line Item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bundle that this service appointment is a member of.

This is a relationship field.

**Relationship Name**
RelatedBundle

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to end. If you are using the Field
Service managed package with the scheduling optimizer, this field is populated
once the appointment is assigned to a resource. `Scheduled End`   `Scheduled Start` = `Estimated Duration` .

**Type**
dateTime


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to start. If you are using the
Field Service managed package with the scheduling optimizer, this field is
populated once the appointment is assigned to a resource.

```
ServiceDocumentTemplate

ServiceTerritoryId

State

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory associated with the appointment. If the parent record is a
work order or work order line item, the appointment inherits its parent’s service
territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the service appointment is completed. Maximum length is 80
characters.

**Type**
picklist


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the appointment. The picklist includes the following values, which
can be customized:

**•** `None` —Default value.

**•** `Scheduled` —Appointment has been assigned to a service resource.

**•** `Dispatched` —Assigned service resource has been notified about their
assignment.

**•** `In Progress` —Work has begun.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.

**•** `Canceled` —Work is canceled, typically before any work began

While you can set the status to null via the API, setting the status to null returns
an error. To prevent errors, use one of the picklist values.

```
StatusCategory

Street

Subject

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field’s values are identical to the default `Status` values.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Customer Absent`_ value, you may
decide that it belongs in the _`Cannot Complete`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the service appointment is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short phrase describing the appointment.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
Transaction

WorkTypeId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last transaction ID of the scheduling and optimization request that updated
this object. The transaction ID is automatically generated and populated by the
Enhanced Scheduling and Optimization engine. Available in API version 63.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the service appointment. The work type is inherited
from the appointment’s parent record if the parent is a work order or work order
line item.

Note: If Lightning Scheduler is also in use, this field is editable. However,
users see an error if they update it to list a different work type than the
parent record’s work type.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Service appointments always have a parent record, which can be a work order, work order line item, opportunity, account, or asset. The
type of parent record tells you about the nature of the service appointment:

**•** Service appointments on _work orders_ and _work order line items_ offer a more detailed view of the work being performed. While work
orders and work order line items let you enter general information about a task, service appointments are where you add the details
about scheduling and ownership.

**•** Service appointments on _assets_ represent work being performed on the asset.

**•** Service appointments on _accounts_ represent work being performed for the account.

**•** Service appointments on _opportunities_ represent work that is related to the opportunity.

**•** Service appointments on _leads_ represent work that is related to lead—for example, a site visit to pursue a promising lead.


### Standard Objects ServiceAppointmentStatus

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceAppointmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceAppointmentFeed**

Feed tracking is available for the object.

**ServiceAppointmentHistory**

History is available for tracked fields of the object.

**ServiceAppointmentOwnerSharingRule**

Sharing rules are available for the object.

**ServiceAppointmentShare**

Sharing is available for the object.

### ServiceAppointmentStatus

Represents a possible status of a service appointment in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ApiName

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ServiceAppointmentStatus

**Field Name** **Details**

**Description**
Indicates that the status value is the default status on service appointments. Only
one status value can be the default.

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
The label for the picklist value that appears in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the drop-down list of values in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.

The Status field on service appointments comes with the following values:

**•** None—Default value.

**•** Scheduled—Appointment has been assigned to a service resource.

**•** Dispatched—Assigned service resource has been notified about their assignment.

**•** In Progress—Work has begun.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Canceled—Work is canceled, typically before any work began

**•** CheckedIn—The customer has arrived for their scheduled appointment.

Important: While you can set the status to null via the API, setting the status to null returns an error. To prevent errors, use one
of the documented picklist values.


### Standard Objects ServiceChannel

The ServiceAppointmentStatus object corresponds to the Status field. Adding a value to the Status field—for example, Waiting—creates
a service appointment status record, and vice versa.

Note: Service appointments also come with a StatusCategory field whose values are identical to the default Status values. If you
create custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_
value, you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory,
[see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### ServiceChannel

Represents a channel of work items that are received from your organization—for example, cases, chats, or leads. This object is available
in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AcwExtensionDuration

AfterConvoWorkMaxTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Specify a value from 10 through 3600.
Available only for service channels of type Messaging or Voice.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if `HasAfterConvoWorkTimer` is set
to `true` . Specify a value from 10 through 3600. Available only for service channels of type
Messaging or Voice.


Standard Objects ServiceChannel

**Field** **Details**

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type Messaging, this field is available in API version 56.0 and later.

```
CapacityModel

CustomSoundId

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, RestrictedPicklist, Sort, Update

**Description**
The method that determines when an agent's capacity for a work item is released. With the
Status-Based capacity routing model, work remains assigned and applied to an agent’s
capacity until the work is completed or reassigned to a different agent. In contrast, the
tab-based capacity model releases an agent’s capacity when a work tab is closed in the
service console. Possible values are StatusBased and TabBased.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  CustomSound

```

**Relationship Type**
Lookup

**Refers To**

```
  StaticResource

```

**Description**
The ID of the static resource for the custom sound selected to play for the
`PresenceUserConfig` object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.


Standard Objects ServiceChannel

**Field** **Details**

```
DoesCheckCapOnOwnerChange

DoesCheckCapOnStatusChange

DoesMinimizeWidgetOnAccept

DoesOverridePresenceAudio

HasAcwExtensionEnabled

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reassigned to a specific agent, you
can choose to override the capacity check and keep the work assigned to the agent. The
default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reopened, you can choose to
override the capacity check keep the work assigned to a specific agent. The default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Automatically minimizes the Omni-Channel widget when an agent accepts work. The default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Service channel settings override the audio settings for each agent’s presence configuration.
The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, agents can extend their After Conversation Work (ACW) time. Available only
if `HasAfterConvoWorkTimer` is set to `true` . If set to `true`, you must also set the


Standard Objects ServiceChannel

**Field** **Details**

`AcwExtensionDuration` and `MaxExtensions` fields. The default value is `false` .
Available only for service channels of type Messaging or Voice.

This field is available in API version 56.0 and later.

```
HasAfterConvoWorkTimer

HasAutoAcceptEnabled

Language

MasterLabel

MaxExtensions

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, After Conversation Work (ACW) time can be configured for the channel. If
set to `true`, you must also set the `AfterConvoWorkMaxTime` field. The default value
is `false` . Available only for service channels of type Messaging or Voice.

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type messaging, this field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Work items in a service channel open automatically in the agent’s workspace so that the
agent doesn’t have to manually accept them. The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the service channel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the service channel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ServiceChannel

**Field** **Details**

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true` . Available only for service channels of
type Messaging or Voice.

This field is available in API version 56.0 and later.

```
RelatedEntity

RoutingConfigurationId

SecRoutingPriorityField

SoundLength

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of object that’s associated with this service channel. This field is unique within your
organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**

```
  RoutingConfiguration

```

**Refers To**

```
  QueueRoutingConfig

```

**Description**
The ID of the routing configuration. This field is a relationship field. This field is available in
API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The name of the standard field or the id of the custom field that is used for secondary routing
priority. This field is unique within your organization.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.


### Standard Objects ServiceChannelFieldPriority

**Field** **Details**

```
StatusField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The picklist field that you use to track work status in the Status-Based capacity routing model.
Use ServiceChannelStatusField to specify the values that indicate completed and in-progress
work-item status.

### ServiceChannelFieldPriority

Represents a secondary routing priority field-value mapping. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
Priority

ServiceChannelId

Value

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority number assigned to the mapped field value.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
string


### Standard Objects ServiceChannelStatus

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The value of the SecRoutingPriorityField field defined in parent ServiceChannel.

### ServiceChannelStatus

Represents the status that’s associated with a specific service channel. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
ServiceChannelId

ServicePresenceStatusId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s associated with the service channel that’s specified by
the `ServicePresenceChannelId` .


### Standard Objects ServiceChannelStatusField ServiceChannelStatusField

Represents the values that you use to indicate completed and in-progress work item status for the status field in the Status-Based Capacity
routing model. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel and Status-Based Capacity Model must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
ServiceChannelId

Type

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For the field that you use to track work status, specifies whether the values are for completed
or in-progress work.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Specifies the values that you use to indicate completed and in-progress work status. Valid
values are `Completed`, `InProgress`, and `Paused` .


### Standard Objects ServiceContract ServiceContract

Represents a customer support contract (business agreement). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

ActivationDate

AdditionalDiscount

ApprovalStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account associated with the service contract.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The initial day the service contract went into effect (whereas `StartDate` may include
a renewal date).

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Extra discount percentage for the service contract. Available in API version 55.0 and
later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Approval status of the service contract.


Standard Objects ServiceContract

**Field** **Details**

`BillingAddress` (beta)

```
BillingCity

BillingCountry

BillingCountryCode

BillingLatitude

BillingLongitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ServiceContract

**Field** **Details**

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

```
BillingPostalCode

BillingState

BillingStateCode

BillingStreet

ContactId

ContractNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
string

**Properties**
Group, Sort, Filter, Nillable

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s billing address.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Contact associated with the service contract. Must be a valid ID.

**Type**
string


Standard Objects ServiceContract

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Unique number automatically assigned to the service contract.

```
Description

Discount

EndDate

GrandTotal

IsDeleted

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the service contract.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

Discount percentage for the service contract.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last day the service contract is in effect.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the service contract plus shipping and taxes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .


Standard Objects ServiceContract

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LineItemCount

Name

OwnerId

ParentServiceContractId

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number of ContractLineItem records associated with the service contract.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the service contract.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns the service contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ServiceContract

**Field** **Details**

**Description**
The service contract’s parent service contract, if it has one.

```
Pricebook2Id

RootServiceContractId

```

`ShippingAddress` (beta)

```
ShippingCity

ShippingCountry

ShippingCountryCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Pricebook2 associated with the service contract. Must be a valid ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level service contract in a service contract hierarchy. Depending
on where a service contract lies in the hierarchy, its root could be the same as its parent.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Country maximum size is 40 characters.

**Type**
picklist


Standard Objects ServiceContract

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s shipping address.

```
ShippingLatitude

ShippingLongitude

ShippingPostalCode

ShippingState

ShippingStateCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a shipping
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. State maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s shipping address.


Standard Objects ServiceContract

**Field** **Details**

```
ShippingStreet

SpecialTerms

StartDate

Status

Subtotal

Tax

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The street address of the shipping address. Maximum of 255 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Any terms specifically agreed to and tracked in the service contract.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first day the service contract is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
The status of the service contract, such as Inactive.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Total of the service contract line items (products) before discounts, taxes, and shipping
are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update


### Standard Objects ServiceContractOwnerSharingRule

**Field** **Details**

**Description**
Total taxes for the service contract.

```
Term

TotalPrice

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
Number of months that the service contract is valid.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Total of the contract line items (products) after discounts and before taxes and shipping.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceContractChangeEvent (API version 44.0)**
Change events are available for the object.

**ServiceContractFeed (API version 23.0)**
Feed tracking is available for the object.

**ServiceContractHistory**

History is available for tracked fields of the object.

### **ServiceContractOwnerSharingRule**

Sharing rules are available for the object.

**ServiceContractShare**

Sharing is available for the object.

SEE ALSO:

### ServiceContractOwnerSharingRule ServiceContractOwnerSharingRule

Represents the rules for sharing a ServiceContract (customer service agreement) with users other than the owner. This object is available
in API version 18.0 and later.


Standard Objects ServiceContractOwnerSharingRule

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A value that represents the type of sharing allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

This field is available in API version 24.0 and later. When creating large sets of data,
always specify a unique `DeveloperName` for each record. If no


### Standard Objects ServiceCrew

**Field Name** **Details**

`DeveloperName` is specified, performance slows down while Salesforce generates
one for each record.

```
GroupId

Name

UserorGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
The ID representing the source group. Service contracts owned by users in the source
group trigger the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** in the user interface.

**Type**
reference

**Properties**
Create, Filter

**Description**
The ID representing the target user or group. Target users or groups are given access.

Use this object to manage the sharing rules for a service contract. General sharing and territory management-related sharing use this
object.

SEE ALSO:

ServiceContract

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### ServiceCrew

Represents a group of service resources who can be assigned to service appointments as a unit.

A service crew is a group of service resources whose combined skills and experience make them a good fit to work together on
appointments. For example, a wellhead repair crew might include a hydrologist, a mechanical engineer, and an electrician.


Standard Objects ServiceCrew

Service appointments can only be assigned to service resources. To assign a service crew to service appointments, you must create a
service resource with a resource type of Crew that represents the crew, then use the resource for assignment purposes.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
CrewSize

LastReferencedDate

LastViewedDate

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of members on the crew. This field is manual, so it doesn’t
auto-update when you add or remove members.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ServiceCrewMember

**Field Name** **Details**

**Description**
The name of the service crew. For example, Repair Crew.

```
OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The crew owner. By default, the owner is the person who created the service
crew.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceCrewChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceCrewFeed**

Feed tracking is available for the object.

**ServiceCrewHistory**

History is available for tracked fields of the object.

**ServiceCrewOwnerSharingRule**

Sharing rules are available for the object.

**ServiceCrewShare**

Sharing is available for the object.

### ServiceCrewMember

Represents a technician service resource that belongs to a service crew.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ServiceCrewMember

Fields

**Field Name** **Details**

```
EndDate

IsLeader

LastReferencedDate

LastViewedDate

ServiceCrewId

ServiceCrewMemberNumber

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last day that the service resource belongs to the crew. You can use this field
to track employment dates for contractors.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the member is the crew leader.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The crew that the service resource belongs to.

**Type**
string


### Standard Objects ServiceCrewOwnerSharingRule

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service crew member.

```
ServiceResourceId

StartDate

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that belongs to the crew. Only service resources whose
resource type is Technician can be added to service crews.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The day the service resource joins the crew. Service resources can
belong to multiple crews as long as their start and end dates don’t overlap.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceCrewMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceCrewMemberFeed**

Feed tracking is available for the object.

**ServiceCrewMemberHistory**

History is available for tracked fields of the object.

### ServiceCrewOwnerSharingRule

Represents the rules for sharing a service crew with user records other than the owner or anyone above the owner in the role hierarchy.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)


Standard Objects ServiceCrewOwnerSharingRule

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

DeveloperName

GroupId

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A service crew owned by a User in the source Group
triggers the rule to give access.

**Type**
string


### Standard Objects ServicePresenceStatus

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

```
ServiceResourceAccessLevel

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### ServicePresenceStatus

Represents a presence status that can be assigned to a service channel. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects ServiceReport

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

### ServiceReport

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

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence status.

Represents a report that summarizes a work order, work order line item, or service appointment.

The fields that appear on a service report are determined by its service report template. Service reports can be signed by the customer
and shared as a PDF.


Standard Objects ServiceReport

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()update( )

```

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ContentVersionDocumentId

DocumentBody

DocumentContentType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the service report version, used for storage.

**Type**
base64

**Properties**
Create, Nillable

**Description**
The report output. `DocumentBody` can’t be retrieved via REST API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data used for the report output.. Possible values are:

**•** `audio/ogg`

**•** `text/calendar`

**•** `video/3gpp2`

**•** `video/3gpp`

**•** `image/avif`

**•** `text/calendar`

**•** `audio/x-caf`

**•** `image/webp`


Standard Objects ServiceReport

**Field Name** **Details**

```
DocumentLength

DocumentName

DocumentTemplate

IsSigned

ParentId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the report output.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the report output, always set to Service Report.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The template used to generate service documents for the Document Builder
feature.

Important: `DocumentTemplate` is different from `Template` . The
document template needs to reference a flexipage that is of type

`serviceDocument` and must target the object used to generate the
service document. For example, you can't use an Account flexipage for a
service report tied to a work order.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the service report contains one or more signatures. This field
isn’t supported for Document Builder.

Tip: Add this field to the Service Reports related list on work orders, work
order line items, and service appointments.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceReport

**Field Name** **Details**

**Description**
The ID of the service appointment, work order, or work order line item that the
service report summarizes. For example, if you click **Create Service Report** on
a service appointment, this field lists the service appointment’s record ID.

```
ServiceReportLanguage

ServiceReportNumber

Status

Template

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Restricted picklist

**Description**
The language used for the service report. The language is selected in the
`ServiceReportLanguage` field on the associated work order. If the work
order doesn’t specify a service report language, the report is translated in the
default language in Salesforce of the person generating the report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service report.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service report. Available in API version 53.0 and later.

Possible values are:

**•** `Completed`

**•** `Failed`

**•** `Generating`

**•** `In Progress`

**•** `None`

**•** `Queued`

The default value is `None` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects ServiceReportLayout

**Field Name** **Details**

**Description**
The service report template used to generate the service report.

Note: If the person creating the service report doesn’t have access to
certain objects or fields that are included in the service report template,
those fields aren’t visible in the report they create.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceReportChangeEvent on page 68**
Change events are available for the object. Available in API version 55.0 and later.

**ServiceReportHistory**

History is available for tracked fields of the object.

### ServiceReportLayout

Represents a service report template in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled. All users with Field Service Standard user permission can view the ServiceReportLayout object via the
API.

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
The developer name of the service report template.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


Standard Objects ServiceReportLayout

**Field Name** **Details**

```
Language

LastViewedDate

MasterLabel

TemplateType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the service report template uses.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the service report template was last viewed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the service report template. For example, Maintenance Report
Template.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the service report template. Available in API version 46.0 and later.

Possible values are:

**•** `DigitalForm`

**•** `ServiceReport`

The default value is `ServiceReport` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceReportLayoutChangeEvent on page 68**
Change events are available for the object. Available in API version 55.0 and later.


### Standard Objects ServiceRequest ServiceRequest

Represents a formal request from a user for something to be provided, such as access, information, hardware, or software. This object
manages the lifecycle of these tasks, which are typically low-risk, and can be fulfilled through a defined, repeatable process. For example,
a Service Request can be created for an employee requesting a new laptop or a student needing a transcript. This object is available in
API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssignedGroupId

AssignedUserId

BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user group assigned to the service request.

This field is a relationship field.

**Relationship Name**
AssignedGroup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user assigned to the service request.

This field is a relationship field.

**Relationship Name**
AssignedUser

**Refers To**
User

**Type**
reference


Standard Objects ServiceRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the business hours used to determine the SLA calculation.

This field is a relationship field.

**Relationship Name**
BusinessHours

**Refers To**
BusinessHours

```
ClosedDate

Description

IsClosed

IsPaused

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the service request was closed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A detailed description of the service request.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the service request is closed (true) or not (false). The default value is false.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the SLA timer is paused (true) or not (false). The default value is false.

The default value is `false` .


Standard Objects ServiceRequest

**Field** **Details**

```
LastReferencedDate

LastViewedDate

MilestoneStatus

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
The timestamp for when the current user last viewed this record

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Information about the milestone the service request reached.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the service request record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects ServiceRequest

**Field** **Details**

```
ParentServiceRequestId

Priority

ReportedById

ResolutionDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent request that this service request belongs to.

This field is a relationship field.

**Relationship Name**
ParentServiceRequest

**Refers To**
ServiceRequest

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of a service request.

Valid values are:

**•** `High`

**•** `Medium`

**•** `Low`

The default value is `Low` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the person who reported the service request.

This field is a polymorphic relationship field.

**Relationship Name**
ReportedBy

**Refers To**
Account, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ServiceRequest

**Field** **Details**

**Description**
The date and time when the service request was resolved.

```
ResolutionSummary

SlaEndDate

SlaPauseDate

SlaStartDate

Status

StatusCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Resolution summary for the service request.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the SLA timer ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the SLA timer was paused.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the SLA timer started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of a service request.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ServiceResource

**Field** **Details**

**Description**
The code that displays the status of the service request lifecycle.

Valid values are:

**•** `Closed`

**•** `Canceled`

**•** `InProgress`

**•** `New`

**•** `OnHold`

**•** `Resolved`

The default value is `New` .

```
Subject

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A short description of the service request.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceRequestFeed on page 55**
Feed tracking is available for the object.

**ServiceRequestHistory**

History is available for tracked fields of the object.

**ServiceRequestShare**

Sharing is available for the object.

### ServiceResource

Represents a service technician or service crew in Field Service and Salesforce Scheduler, or an agent in Workforce Engagement. This
object is available in API version 38.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`


Standard Objects ServiceResource

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
Description

IsActive

IsCapacityBased

IsOptimizationCapable

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the resource.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When selected, this option means that the resource can be assigned to work
orders. For service tracking purposes, resources can’t be deleted, so deactivating
a resource is the best way to send them into retirement.

Deactivating a user doesn’t deactivate the related service resource. You can’t
create a service resource that is linked to an inactive user.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Capacity-based resources are limited to a certain number of hours or
appointments in a specified time period.

Tip: The Capacities related list shows a resource’s capacity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is reserved for Field Service and the managed package. Create a custom
field instead of using this field to include a service resource in optimization.


Standard Objects ServiceResource

**Field Name** **Details**

```
LastKnownLatitude

LastKnownLongitude

LastKnownLocation

LastKnownLocationDate

LastReferencedDate

LastViewedDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the last known location.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the last known location.

**Type**
location

**Properties**
Nillable

**Description**
The service resource’s last known location. You can configure this field to display
data collected from a custom mobile app. This field isn’t visible in the user
interface, but you can expose it on service resource page layouts or set up field
tracking to be able to view a resource’s location history.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time of the last known location.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource was last modified. Its label in the user interface
is `Last Modified Date` .

**Type**
dateTime


Standard Objects ServiceResource

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource was last viewed.

```
LocationId

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The location associated with the service resource. For example, a service vehicle
driven by the service resource.

LocationId is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The resource’s name, for example the name or title of the associated user or
service crew.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service resource.

OwnerId is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ServiceResource

**Field Name** **Details**

```
RelatedRecordId

ResourceType

ServiceCrewId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The associated user. Its label in the UI is `User` . If the service resource represents
a service crew rather than a user, leave the `User` field blank and select the
related crew in the `ServiceCrewId` field.

RelatedRecordId is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the resource is a Technician (T), Dispatcher (D), Crew (C), Asset
(S), Agent (A), or Planner (P). The default value is Technician (T). Resources who
are dispatchers can’t be capacity-based or included in scheduling optimization.
Only users with the Field Service Dispatcher permission-set license can be
dispatchers. You can’t add additional resource types.

To create a dependent lookup filter with ServiceResource.ResourceType, use only
the first letter of the picklist value, for example T for Technician.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The associated service crew. If the service resource represents a crew, select the
crew.

Note: This field is hidden for all users by default. To use it, update its
field-level security settings in Setup and add it to your service resource
page layouts.


### Standard Objects ServiceResourceCapacity

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceResourceChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceResourceFeed**

Feed tracking is available for the object.

**ServiceResourceHistory**

History is available for tracked fields of the object.

**ServiceResourceOwnerSharingRule**

Sharing rules are available for the object.

**ServiceResourceShare**

Sharing is available for the object.

### ServiceResourceCapacity

Represents the maximum number of scheduled hours or number of service appointments that a capacity-based service resource can
complete within a specific time period. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
CapacityInHours

CapacityInWorkItems

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of hours that the resource can work per time period. You must fill
out this field, the `CapacityInWorkItems` field, or both.

**Type**
int


Standard Objects ServiceResourceCapacity

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of service appointments that the resource can complete per
time period. You must fill out this field, the `CapacityInHours` field, or both.

```
CapacityNumber

EndDate

LastReferencedDate

LastViewedDate

ServiceResourceId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the capacity record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the capacity ends; for example, the end date of a contract.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced ( `LastReferencedDate` )
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceResourceCapacity

**Field Name** **Details**

**Description**
The associated service resource. You can set multiple capacities for a resource as
long as their start and end dates do not overlap.

```
StartDate

TimePeriod

```

Usage

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The date the capacity goes into effect.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Days, Hours, or Months. For example, if a resource can work 80 hours per month,
the capacity’s `Time Period` would be _`Month`_ and `Hours per Time`
`Period` would be _`80`_ .

Service resources who are capacity-based can only work a certain number of hours or complete a certain number of service appointments
within a specified time period. Contractors tend to be capacity-based. To indicate that a service resource is capacity-based, select
**Capacity-Based** on the service resource record, then create a capacity record for the service resource.

You must fill out at least one of these fields: `CapacityInWorkItems` and `CapacityInHours` . If you’re using the Field Service
managed package and would like to measure capacity both in hours and in number of work items, enter a value for both. The resource
is considered to reach their capacity based on whichever term is met first—hours or number of work items.

Important: If you aren’t using the Field Service managed package, capacity serves more as a suggestion than a rule. Resources
can still be as scheduled beyond their capacity, and you aren’t notified when a resource exceeds their capacity.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceCapacityChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceCapacityFeed**

Feed tracking is available for the object.

**ServiceResourceCapacityHistory**

History is available for tracked fields of the object.


### Standard Objects ServiceResourceCapacityHistory ServiceResourceCapacityHistory

Represents the history of changes made to tracked fields on a service resource capacity record. This object is available in API version 38.0
and later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for service resource capacity fields must be configured.

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

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
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort


### Standard Objects ServiceResourceDataTranslation

**Field Name** **Details**

**Description**
The value of the field before it was changed.

```
ServiceResourceCapacityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the service resource capacity being tracked. The history is displayed on the
detail page for this record.

### ServiceResourceDataTranslation

Represents the translated values of the data stored within a ServiceResource record’s fields. This object is available in API version 54.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

Fields

**Field** **Details**

```
Description

IsOutOfDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The translated value for the ServiceResource description.

**Type**
boolean


### Standard Objects ServiceResourceOwnerSharingRule

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ServiceResource record is updated after the last translation was
filed.

```
Language

Name

ParentId

```

Usage

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
The translated value for the ServiceResource record name. This field is required to translate
the text in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the ServiceResource associated with the data that is being translated.

Use this object to translate the data stored in a ServiceResource record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ServiceResource object, additional ServiceResourceDataTranslation fields exist for translating
the data contained within those fields.

You can’t use a custom external id field in an upsert call for a ServiceResourceDataTranslation object.

### ServiceResourceOwnerSharingRule

Represents the rules for sharing a service resource with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 38.0 and later.


Standard Objects ServiceResourceOwnerSharingRule

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
Description

DeveloperName

GroupId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A service resource owned by a User in the source
Group triggers the rule to give access.


### Standard Objects ServiceResourcePreference

**Field** **Details**

```
Name

ServiceResourceAccessLevel

UserOrGroupId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

### ServiceResourcePreference

Represents the service resource scheduling preferences that are considered as a business objective in the scheduling logic engine. This
object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Agent or Workforce Engagement Planner permission set.


Standard Objects ServiceResourcePreference

Fields

**Field** **Details**

```
EndDate

LastReferencedDate

LastViewedDate

Name

OperatingHoursId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date period that this preference is effective.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last modified. Its label in the user interface
is **Last Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The service resource preference record name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The operating hours associated with the service resource preference.

This is a relationship field.

**Relationship Name**
OperatingHours


Standard Objects ServiceResourcePreference

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
OperatingHours

```
OwnerId

ServiceResourceId

StartDate

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service resource preference.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource associated with the service resource preference.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The start date period that this preference is effective.


### Standard Objects ServiceResourceSkill ServiceResourceSkill

Represents a skill that a service resource possesses in Field Service and Lightning Scheduler. This object is available in API version 38.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
EffectiveEndDate

EffectiveStartDate

LastReferencedDate

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the skill expires. For example, if a service resource needs to be
re-certified after six months, the end date would be the date their certification
expires.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource gains the skill. For example, if the skill
represents a certification, the start date would be the date of certification.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last modified. Its label in the user interface
is `Last Modified Date` .


Standard Objects ServiceResourceSkill

**Field Name** **Details**

```
LastViewedDate

ServiceResourceId

SkillId

SkillLevel

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service resource who possesses the skill.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill the service resource possesses.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The service resource’s skill level. Skill level can range from zero to 99.99.


### Standard Objects ServiceSetupProvisioning

**Field Name** **Details**

```
SkillNumber

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource skill assignment.

You can assign skills to all service resources in your org to indicate their certifications and areas of expertise, and specify each resource’s
skill level from 0 to 99.99. For example, you can assign Maria the “Welding” skill, level 50.

If you intend to use the skills feature, determine which skills you want to track and how skill level should be determined. For example,
you may want the skill level to reflect years of experience, certification levels, or license classes.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceSkillChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceSkillFeed**

Feed tracking is available for the object.

**ServiceResourceSkillHistory**

History is available for tracked fields of the object.

### ServiceSetupProvisioning

Represents a task completed by the Service Setup Assistant. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ServiceSetupProvisioning is accessible only if the Service Setup Assistant is turned on. Users need the Customize Application permission

to access it.


Standard Objects ServiceSetupProvisioning

Fields

**Field** **Details**

```
JobName

Name

Status

TaskAction

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of a group of tasks completed by the Service Setup Assistant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the task being completed by the Service Setup Assistant.

Possible values are:

**•** `

**•** `Completed` —The task completed successfully.

**•** `ExistingSetup` —The task couldn’t be completed due to conflicting configurations.

**•** `FailedFatalError` —The task couldn’t be completed.

**•** `InProgress` —The task is in progress.

**•** `PRE_CONDITION_NOT_MET` —The task couldn’t be completed because one or more
prerequisites weren’t met.

**•** `VALIDATION_NOT_MET` —The task is considered as completed but the condition
defined in the implementation was not true. No retry will be executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action taken by the task.

Possible values are:


### Standard Objects ServiceTerritory

**Field** **Details**

**•** `updatesOrgSettings`

**•** `updatesOrgValues`

**•** `sortApps`

**•** `setForecastingUserFeatureLicense`

**•** `recalculatePermissionSetGroup`

**•** `deploysMetadata`

**•** `createsSetupEntityAccess`

**•** `clearGuidanceCenterCache`

**•** `callsConnectApi`

**•** `assignsPermissionSets`

**•** `assignsPermissionSetGroups`

```
TaskActionContext

TaskContext

TaskName

### ServiceTerritory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional details about the `TaskAction` parameter, including how much of the action
has been processed.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the changes included in the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the task.

Represents a geographic or functional region in which work can be performed in Field Service, Salesforce Scheduler, or Workforce
Engagement. This object is available in API version 38.0 and later.


Standard Objects ServiceTerritory

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Address

AvgTravelTime

City

Country

```

**Type**
address

**Properties**
Filter

**Description**
An address to associate with the territory. For example, you can list the address
of the territory’s headquarters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The average travel time for this service territory. The value is added to the Work
Capacity Usage for each scheduled service appointment in the service territory.
Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the associated address. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to associate with the territory. Maximum length is 80 characters.


Standard Objects ServiceTerritory

**Field Name** **Details**

```
Description

GeocodeAccuracy

IsActive

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.This field is available in the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service territory is meant to be used. If a territory is inactive,
you can’t add members to it or link it to work orders, work order line items, or
service appointments.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last viewed.

**Type**
double


Standard Objects ServiceTerritory

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.This field is available in the API only.

```
Longitude

Name

OperatingHoursId

ParentTerritoryId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory’s operating hours, which indicate when service appointments within
the territory can occur. Service resources who are members of a territory
automatically inherit the territory’s operating hours unless different hours are
specified on the resource record.

This field is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference


Standard Objects ServiceTerritory

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The territory’s parent service territory, if it has one. For example, a _`Northern`_
_`California`_ territory can have a _`State of California`_ territory as
its parent. A service territory hierarchy can contain up to 10,000 territories.

This field is a relationship field.

**Relationship Name**
ParentTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
PostalCode

State

Street

TopLevelTerritoryId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the territory. Maximum length is
20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the territory. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the address associated with the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ServiceTerritory

**Field Name** **Details**

**Description**
(Read only) The top-level territory in a hierarchy of service territories. Depending
on where a territory lies in the hierarchy, its top-level territory can be the same
as its parent.

This field is a relationship field.

**Relationship Name**
TopLevelTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
TravelModeId

TravelTimeBuffer

TypicalInTerritoryTravelTime

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the TravelMode used for travel time calculations. The travel mode includes
information about the type of transportation, such as a car or walking, whether
a vehicle can take toll roads, and whether a vehicle is transporting hazardous
materials.

This field is a relationship field.

**Relationship Name**
TravelMode

**Relationship Type**
Lookup

**Refers To**
TravelMode

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Add additional time to driving time, such as time to find parking or to walk to
the site. This value overrides the Travel Time Buffer value defined in Field Service
Settings | Scheduling | Routing.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects ServiceTerritoryDataTranslation

**Field Name** **Details**

**Description**
Estimated number of minutes needed to travel from one location to another
within the service territory. You can use this field in Apex customization.

Usage

If you want to use service territories, determine which territories to create. Depending on how your business works, you can create
territories based on cities or counties, or on functional categories such as sales versus service. If you plan to build out a hierarchy of service
territories, create the highest-level territories first.

For example, you can create a hierarchy of territories to represent the areas where your team works in California. Include a top-level
territory named _`California`_, three child territories named _`Northern California`_, _`Central California`_, and
_`Southern California`_, and a series of third-level territories corresponding to California counties. Assign service resources to each
county territory to indicate who is available to work in that county.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**ServiceTerritoryChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryFeed**

Feed tracking is available for the object.

**ServiceTerritoryHistory**

History is available for tracked fields of the object.

**ServiceTerritoryOwnerSharingRule**

Sharing rules are available for the object.

**ServiceTerritoryShare**

Sharing is available for the object.

### ServiceTerritoryDataTranslation

Represents the translated values of the data stored within a ServiceTerritory record’s fields. This object is available in API version 54.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.


Standard Objects ServiceTerritoryDataTranslation

**•** Translation Workbench and data translation must be enabled in your org.

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
Create, Nillable,Update

**Description**
The translated value for the ServiceTerritory description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date ( `true` ) or current ( `false` ). A translation
is out-of-date if the parent ServiceTerritory record is updated after the last translation was
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
The translated value for the ServiceTerritory record name. This field is required to translate
the text in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the ServiceTerritory associated with the data that is being translated.


### Standard Objects ServiceTerritoryLocation

Usage

Use this object to translate the data stored in a ServiceTerritory record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ServiceTerritory object, additional ServiceTerritoryDataTranslation fields exist for translating
the data contained within those fields.

You can’t use a custom external id field in an upsert call for a ServiceTerritoryDataTranslation object.

### ServiceTerritoryLocation

Represents a location associated with a particular service territory in field service.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
LocationId

ServiceTerritoryId

### `ServiceTerritoryLocationNumber`

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location that is associated with the service territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read only) Auto-generated number identifying the service territory location.


### Standard Objects ServiceTerritoryMember

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryLocationChangeEvent (API version 55.0)**
Change events are available for the object.

**ServiceTerritoryLocationFeed**

Feed tracking is available for the object.

**ServiceTerritoryLocationHistory**

History is available for tracked fields of the object.

### ServiceTerritoryMember

Represents a service resource who can be assigned in a service territory in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
Address

City

```

**Type**
address

**Properties**
Filter

**Description**
The member’s address. You may want to list the related service resource’s address
in this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the member’s address. Maximum length is 40 characters.


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

```
Country

EffectiveEndDate

EffectiveStartDate

GeocodeAccuracy

LastReferencedDate

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the member’s address. Maximum length is 80 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the service resource is no longer a member of the territory. If the
resource will be working in the territory for the foreseeable future, leave this field
blank. This field is mainly useful for indicating when a temporary relocation ends.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource becomes a member of the service territory.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory member was last modified. Its label in the user
interface is `Last Modified Date` .


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

```
LastViewedDate

Latitude

Longitude

MemberNumber

OperatingHoursId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory member was last viewed.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the service territory member.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours assigned to the service territory member. If no operating
hours are specified, the member is assumed to use their parent service territory’s


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

operating hours. If a member needs special operating hours, create them in Setup
and select them in the `Operating Hours` lookup field on the member’s
detail page.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

```
PostalCode

ServiceResourceId

ServiceTerritoryId

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the member’s address. Maximum length is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource assigned to the service territory.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service territory that the service resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceTerritory


Standard Objects ServiceTerritoryMember

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
State

Street

TerritoryType

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the member’s address. Maximum length is 80 characters.

**Type**
textarea

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the member’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Primary, Secondary, or Relocation.

**•** The primary territory is typically the territory where the resource works most
often—for example, near their home base. Service resources can only have
one primary territory.

**•** Secondary territories are territories where the resource can be assigned to
appointments if needed. Service resources can have multiple secondary
territories.

**•** Relocation territories represent temporary moves for service resources. If
you’re using the Field Service managed packages with the scheduling
optimizer, resources with relocation territories are always assigned to services
within their relocation territories during the specified relocation dates; if they
don’t have a relocation territory, the primary territories are favored over the
secondary.

For example, a service resource might have the following territories:

**•** Primary territory: _`West Chicago`_

**•** Secondary territories:

**–** _`East Chicago`_


### Standard Objects ServiceTerritoryWorkType

**Field Name** **Details**

**–** _`South Chicago`_

**•** Relocation territory: _`Manhattan`_, for a three-month period

```
TravelModeId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the TravelMode used for travel time calculations. The travel mode includes
information about the type of transportation, such as a car or walking, whether
a vehicle can take toll roads, and whether a vehicle is transporting hazardous
materials.

This field is a relationship field.

**Relationship Name**
TravelMode

**Relationship Type**
Lookup

**Refers To**
TravelMode

If you delete a service territory with members, the service resources who were members no longer have any connection to the territory.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceTerritoryMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryMemberFeed**

Feed tracking is available for the object.

**ServiceTerritoryMemberHistory**

History is available for tracked fields of the object.

### ServiceTerritoryWorkType

Represents the relationship between a ServiceTerritory object and a WorkType object for Salesforce Scheduler appointments. This object
is available in API version 45.0 and later.


Standard Objects ServiceTerritoryWorkType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsSlotPublished

LastReferencedDate

LastViewedDate

Name

ServiceTerritoryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicate whether records in the Shift object are created for the selected Service Territory and
Work Type.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this object.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this service territory-work type relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ServiceTerritoryWorkType

**Field** **Details**

**Description**
The ID of the service territory that’s related to the work type indicated in the `WorkTypeId`
field.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
TeamId

WorkTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the team associated with the service territory for a specific work type.

This field is a relationship field and is available in API version 58.0 and later.

**Relationship Name**
Team

**Relationship Type**
Lookup

**Refers To**
Team

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that’s related to the service territory indicated in the
`ServiceTerritoryId` field.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


### Standard Objects SessionPermSetActivation

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryWorkTypeFeed**

Feed tracking is available for the object.

**ServiceTerritoryWorkTypeHistory**

History is available for tracked fields of the object.

### SessionPermSetActivation

The SessionPermSetActivation object represents a permission set assignment activated during an individual user session. When a
### SessionPermSetActivation object is inserted into a permission set, an activation event fires, allowing the permission settings to apply to

the user’s specific session. This object is available in API versions 37.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Note: If you include session-based permission sets in a permission set group, the permissions in them do not require session-based
activation for users assigned to the group.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

Fields

**Field Name** **Details**

```
AuthSessionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The session ID related to this permission set assignment for its duration.

This is a relationship field.

**Relationship Name**
AuthSession

**Relationship Type**
Lookup

**Refers To**
AuthSession


Standard Objects SessionPermSetActivation

**Field Name** **Details**

```
Description

PermissionSetGroupId

PermissionSetId

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session details, such as device used and browser.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The permission set group ID related to this permission set group assignment and
user for its duration. This field is available in API version 53.0 and later.

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
Filter, Group, Sort

**Description**
The permission set ID related to this permission set assignment and user for its
duration.

This is a relationship field.

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects SessionPermSetActivation

**Field Name** **Details**

**Description**
The user ID of the user to whom this permission set assignment applies for its
duration.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Usage

Use SessionPermSetActivation to create a permission set available only for a specified session’s duration. For example, create permission
sets that provide access to specific applications only during authenticated sessions.

In the following Apex example, an identified session is activated after session information is submitted via a button. Successful activation
results in a confirmation message displayed to the user.

```
   public class SessionPermSetActivationController {

      // id of the session permission set to be activated

      private final String sessionPermSetId = '0PSxx00000004rJ';

      private final String sessionId;

      public SessionPermSetActivationController() {

        Map<String, String> sessionManagement = Auth.SessionManagement.getCurrentSession();

        String parentSessionId = sessionManagement.get('ParentId');

        String currentSessionId = sessionManagement.get('SessionId');

        sessionId = parentSessionId != null ? parentSessionId : currentSessionId;

      }

      public PageReference activate() {

        // activate the permission set

        SessionPermSetActivation activation = new SessionPermSetActivation();

        activation.AuthSessionId = sessionId;

        activation.PermissionSetId = sessionPermSetId;

        activation.Description = 'created by SessionPermSetActivationController';

        insert activation;

        return null;

      }

      public boolean getActivated() {

        Integer alreadyActivated = [SELECT count()

                              FROM SessionPermSetActivation

```


### Standard Objects SetupAssistantStep

```
                              WHERE AuthSessionId = :sessionId

                             And PermissionSetId = :sessionPermSetId LIMIT

    1];

        return alreadyActivated > 0;

      }

   }

   <apex:page controller="SessionPermSetActivationController">

       <apex:outputPanel rendered="{!!Activated}">

         <h3>Activate Session Permission Set</h3>

         <br />

         <apex:form >

             <apex:commandButton action="{!activate}" value="Activate"

   id="activateButton"/>

         </apex:form>

       </apex:outputPanel>

       <apex:outputPanel rendered="{!Activated}">

         <h3>Session Permission Set is already active.</h3>

       </apex:outputPanel>

   </apex:page>

### SetupAssistantStep

```

For internal use only.

### SetupAuditTrail

Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API version
15.0 and later.

Note: SetupAuditTrail is not a supported standard controller. Using SetupAuditTrail as a standard controller in a Visualforce page
results in an error.

Supported Calls

`query()`, `retrieve()`

Note: Aggregate queries aren’t supported on this object. For example, `SELECT count() FROM SetupAuditTrail`
works but `SELECT count(Id) FROM SetupAuditTrail` fails.

Fields

**Field** **Details**

```
Action

```

**Type**
string


Standard Objects SetupAuditTrail

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The category of the change made in Setup. For example, a value of _`PermSetCreate`_
indicates that an administrator created a permission set. The `Display` field contains more
specific information.

```
CreatedByContext

CreatedByIssuer

DelegateUser

Display

Section

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context under which the Setup change was made. For example, if Einstein uses
cloud-to-cloud services to make a change in Setup, the value of this field is _`Einstein`_ .
This field is available in API version 48.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Login-As user who executed the action in Setup. If a Login-As user didn’t perform the
action, this field is blank. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Nillable, Sort

**Description**
The full description of changes made in Setup. For example, if the `Action` field has a value
of _`PermSetCreate`_, the `Display` field has a value like “Created permission set MAD:
with user license Salesforce.”

**Type**
string


### Standard Objects SetupEntityAccess

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
The section in the Setup menu where the action occurred. For example, Manage Users or
Company Profile.

Note: You can use SOQL joins to get the information you need more quickly. For example, running `SELECT CreatedBy.Name`
`FROM SetupAuditTrail LIMIT 10` returns the first and last names of the last 10 people to make changes in Setup.

### SetupEntityAccess

Represents the enabled setup entity access settings (such as for Apex classes) for the parent PermissionSet. This object is available in
API version 25.0 and later.

To grant users access to an entity, associate the appropriate SetupEntityAccess record with a PermissionSet that’s assigned to a user.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with "View Setup and Configuration" permission can access this object.

Fields

**Field Name** **Details**

```
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet


Standard Objects SetupEntityAccess

**Field Name** **Details**

```
SetupEntityId

SetupEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity for which access is enabled, such as an Apex class or
Visualforce page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of setup entity for which access is enabled. Valid values are:

**•** `ApexClass` for Apex classes

**•** `ApexPage` for Visualforce pages

**•** In API version 64.0 and later, `BotDefinition` for agents

**•** In API version 28.0 and later, `ConnectedApplication` for OAuth
connected apps

**•** In API version 48.0 and later, `CustomEntityDefinition` for Custom
Settings and Custom Metadata Types

**•** In API version 31.0 and later, `CustomPermission` for custom permissions

**•** In API version 62.0 and later, `EmailRoutingAddress` for email routing
addresses.

**•** In API version 60.0 and later, `ExternalClientApplication` for
external client apps.

**•** In API version 58.0 and later, `ExternalCredentialParameter` for
external credential principals.

**•** In API version 58.0 and later, `FlowDefinition` for flows

**•** In API version 62.0 and later, `MessagingChannel` for messaging channels

**•** In API version 58.0 and later, `OrgWideEmailAddress` for
organization-wide email addresses

**•** In API version 28.0 and later, `ServiceProvider` for service providers

**•** In API version 60.0 and later, `StandardInvocableActionType` for
standard invocable actions.

**•** In API version 28.0 and later, `TabSet` for apps


Standard Objects SetupEntityAccess

Usage

Because SetupEntityAccess is a child of the PermissionSet object, the usage is similar to other PermissionSet child objects like
FieldPermissions and ObjectPermissions.

For example, the following code returns all permission sets that grant access to any setup entities for which access is enabled:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

```

The following code returns permission sets that grant access only to Apex classes:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE SetupEntityType='ApexClass'

```

The following code returns permission sets that grant access to any setup entities, and are not owned by a profile:

```
   SELECT Id, ParentId, Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE ParentId

   IN (SELECT Id

     FROM PermissionSet

     WHERE isOwnedByProfile = false)

```

You may want to return only those permission sets that have access to a specific setup entity. To do this, query the parent object. For
example, this code returns all permission sets that grant access to the `helloWorld` Apex class:

```
   SELECT Id, Name,

     (SELECT Id, Parent.Name, Parent.Profile.Name

     FROM SetupEntityAccessItems)

   FROM ApexClass

   WHERE Name = 'helloWorld'

```

While it’s possible to return permission sets that have access to a `ConnectedApplication`, `ServiceProvider`, or `TabSet`
by `SetupEntityId`, it’s not possible to return permission sets that have access to these `SetupEntityType` fields by any other
AppMenuItem attribute, such as `Name` or `Description` . For example, to find out if a user has access to the Recruiting app, you’d
run two queries. First, query to get the AppMenuItem ID:

```
   SELECT Id, Name, Label

   FROM AppMenuItem

   WHERE Name = 'Recruiting'

```

Let’s say the previous query returned the AppMenuItem `ApplicationId` 02uD0000000GIiMIAW. Using this ID, you can now run a
query to find out if a user has access to the Recruiting app:

```
   SELECT Id, SetupEntityId, SetupEntityType

   FROM SetupEntityAccess

   WHERE ParentId

   IN

     (SELECT PermissionSetId

     FROM PermissionSetAssignment

```


### Standard Objects ShapeRepresentation

```
     WHERE AssigneeId = '005D0000001QOzF')

   AND (SetupEntityId = '02uD0000000GIiMIAW')

```

SEE ALSO:

PermissionSet

FieldPermissions

ObjectPermissions

ApexClass

ApexPage

### ShapeRepresentation

Contains information about the shape of an org. The shape of an org includes licenses and limits information. You can easily create
scratch orgs based on a source org’s shape. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A free-form text field for you to enter a description of this org shape. This field has a maximum
length of 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the org shape was last referenced. This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects SharingRecordCollection

**Field** **Details**

**Description**
Date when the org shape was last viewed. This field is read-only.

```
Name

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The alias for the org shape.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of this org shape. You can use an org shape when it’s Active. This field is read-only.

Possible values are:

**•** `Active`

**•** `Error`

**•** `InProgress`

**•** `Inactive`

**•** `New`

### SharingRecordCollection

Represents a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Record collections are limited to 100 items and 100 members for each record collection.

Fields

**Field** **Details**

```
Description

```

**Type**
string


Standard Objects SharingRecordCollection

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection.

```
GroupId

LastAdded

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The group ID of the record collection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when an item was last added to the record collection.

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
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection.


### Standard Objects SharingRecordCollectionItem

**Field** **Details**

```
NumberOfRecords

OwnerId

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of records in the record collection. The limit is 100.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record collection owner.

### SharingRecordCollectionItem

Represents a single record in a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Record collections are limited to 100 items for each record collection.

Fields

**Field** **Details**

```
CollectionId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SharingRecordCollectionMember

**Field** **Details**

**Description**
The description of the record collection item.

```
ItemId

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record collection item.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection item.

### SharingRecordCollectionMember

Represents a user with access to a collection of records. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Record collections are limited to 100 members for each record collection.

Fields

**Field** **Details**

```
AccessLevel

CollectionId

```

**Type**
picklist

**Properties**
Read, Edit

**Description**
The access level on the related record collection.

**Type**
reference


### Standard Objects Shift

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

```
UserOrGroupId

### Shift

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user or group with access to the record collection.

Represents a shift for service resource scheduling. Available in API versions 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `upsert()`

Special Access Rules

Field Service, Service Engagement, or Workforce Engagement must be enabled. For Field Service, users must have Field Service permissions.
For Service Engagement, users must have the Service Engagement Planner permission set. For Workforce Engagement, users must have
the Workforce Engagement Admin or Planner permission set.

Fields

**Field** **Details**

```
BackgroundColor

EndTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
dateTime


Standard Objects Shift

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift ends.

```
IsHolidayShift

IsNonStandard

JobProfileId

Label

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates a shift that overlaps with holiday hours. The default value is false. Available in API
version 55.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The job profile associated with the shift. Available in API versions 47.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label that a shift is given.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed a related record.


Standard Objects Shift

**Field** **Details**

```
LastViewedDate

OwnerId

RecordsetFilterCriteriaId

ServiceResourceId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift.

This is a polymorphic relationship field.

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
The ID of the recordset filter criteria selected for the shift. Available in API version 49.0 and
later.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shift

**Field** **Details**

**Description**
The ID of the service resource the shift belongs to. Available in API versions 47.0 and later.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

```
ServiceTerritoryId

ShiftNumber

ShiftTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory the shift belongs to. Available in API versions 47.0 and later.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number automatically given to the shift upon creation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The shift template ID, if the shift was created from a shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate


Standard Objects Shift

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

```
StartTime

Status

StatusCategory

TimeSlotType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift starts.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the status of the shift. Users can create custom values. Default values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. This field is derived from `Status` using
the mapping defined in setup.

Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of time slot for the shift. The same setup values as the `TimeSlot` field in the
OperatingHours object.


### Standard Objects ShiftHistory

**Field** **Details**

Possible values are:

**•** `Normal` (default value)

**•** `Extended`

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0, and is a pilot feature in API version
47.0.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftChangeEvent (API version 54.0)**
Change events are available for the object.

**ShiftFeed**

Feed tracking is available for the object.

### **ShiftHistory**

History is available for tracked fields of the object.

**ShiftOwnerSharingRule**

Sharing rules are available for the object.

**ShiftShare**

Sharing is available for the object.

### ShiftHistory

Represents the history of changes made to tracked fields on a time sheet. Available in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Field Service must be enabled in your organization, and field tracking for shift fields must be configured.


Standard Objects ShiftHistory

Fields

**Field** **Details**

```
DataType

Field

NewValue

OldValue

ShiftId

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
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the shift being tracked. The history is displayed on the detail page for this record.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup


### Standard Objects ShiftOwnerSharingRule

**Field** **Details**

**Refers To**
### Shift

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftOwnerSharingRule

Represents the rules for sharing a shift with user records other than the owner or anyone above the owner in the role hierarchy. Available
in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not


Standard Objects ShiftOwnerSharingRule

**Field** **Details**

include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
GroupId

Name

ServiceResourceAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A time sheet owned by a User in the source Group
triggers the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.


### Standard Objects ShiftPattern

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftPattern

Represents a pattern of templates for creating shifts. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled. Users must have Field Service permission.

Fields

**Field** **Details**

```
Description

IsActive

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A short description of the shift pattern to help users identify the pattern.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the shift pattern can be used to create shifts.

The default value is ‘false’.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last used.


Standard Objects ShiftPattern

**Field** **Details**

```
LastViewedDate

Name

OwnerId

PatternLength

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A short, descriptive name of the shift pattern.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the shift pattern. Default is the user who creates the shift pattern.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration in days of the shift pattern.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftPatternChangeEvent (API version 54.0)**
Change events are available for the object.


### Standard Objects ShiftPatternEntry

**ShiftPatternFeed on page 55**
Feed tracking is available for the object.

**ShiftPatternHistory on page 63**
History is available for tracked fields of the object.

**ShiftPatternShare on page 67**
Sharing is available for the object.

SEE ALSO:

### ShiftPatternEntry

[Shift Patterns](https://help.salesforce.com/articleView?id=fs_shift_patterns.htm&language=en_US)

### ShiftPatternEntry ShiftPatternEntry links a shift template to a shift pattern. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled. Users must have Field Service permission.

Fields

**Field** **Details**

```
DayOrder

LastReferencedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
`DayOrder` links the shift template to the specific day within the shift pattern duration that
the template. For example, if the DayOrder is 2 then a shift from the associated template is
created on the second day of the pattern.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last used.


Standard Objects ShiftPatternEntry

**Field** **Details**

```
LastViewedDate

Name

ShiftPatternId

ShiftTemplateId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated reference number for the shift pattern entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the shift pattern that the shift pattern entry is linked to.

This is a relationship field.

**Relationship Name**
ShiftPattern

**Relationship Type**
Lookup

**Refers To**
ShiftPattern

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the shift template that’s used to create shifts for this shift pattern entry.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate


### Standard Objects ShiftSegment

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftPatternEntryChangeEvent (API version 54.0)**
Change events are available for the object.

SEE ALSO:

ShiftPattern

### ShiftSegment

Represents a scheduled activity within a shift. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
EndTime

IsInAdherence

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the agent is in adherence ( `true` ) or not ( `false` ) for the scheduled
segment activity.

The default value is `true` .


Standard Objects ShiftSegment

**Field** **Details**

```
Name

SegmentTypeId

ShiftId

StartTime

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the shift segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the associated shift segment type.

This is a relationship field.

**Relationship Name**
SegmentType

**Relationship Type**
Lookup

**Refers To**
ShiftSegmentType

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the shift in which the segment is scheduled.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup

**Refers To**
Shift

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment starts.


### Standard Objects ShiftSegmentType ShiftSegmentType

Represents a type of activity scheduled within a shift. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.

Fields

**Field** **Details**

```
AdherenceThreshold

Category

Color

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A threshold, in minutes. If the agent starts the scheduled activity within this threshold, the
shift segment activity is in adherence.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A category for the type of shift segment.

Possible values are:

**•** `Break` —Break times, such as a coffee or lunch break.

**•** `NonWork` —Non-working activities, such as training or meetings.

**•** `Work` —Work activities, such as answering calls, responding to chats, or handling cases.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shift activities of this type are displayed in the UI. Use a 3- or
6-digit hexadecimal format, for example #FF00FF.


Standard Objects ShiftSegmentType

**Field** **Details**

```
Description

DeveloperName

IsActive

Language

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the shift segment type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

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
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the shift segment type is active ( `true` ) or not ( `false` ).

The default value is `true` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the shift segment type.

Possible values are the languages that Workforce Engagement supports.


### Standard Objects ShiftShare

**Field** **Details**

```
MasterLabel

ServicePresenceStatusId

### ShiftShare

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the shift segment type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the associated service presence status for segments of this type.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

Represents a sharing entry on a field service shift. Available in API versions 46.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects ShiftShare

Fields

**Field** **Details**

```
AccessLevel

ParentId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the shift. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn’t valid for create or update calls.)

Set to an access level that is at least equal to the organization’s default shift access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The shift associated with the sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Shift

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the shift record.

**•** `Owner` —The User is the owner of the shift.

**•** `Rule` —The User or Group has access via a shift sharing rule.


### Standard Objects ShiftStatus

**Field** **Details**

**•** `GuestRule` —The User or Group has access via a shift guest user sharing rule.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Read only) ID of the user or group that has access to the shift record.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftStatus

Represents a shift, such as Tentative, Published, or Confirmed. Available in API versions 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects ShiftStatus

**Field** **Details**

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

```
IsDefault

MasterLabel

SortOrder

StatusCode

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default shift status value ( `true` ) or not ( `false` ) in the picklist.
Only one value can be the default value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this shift status value. This display value is the internal label that does not
get translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the shift status picklist. These numbers are not guaranteed
to be sequential, as some previous shift status values might have been deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.


### Standard Objects ShiftTemplate ShiftTemplate

Represents a template for creating shifts. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled. For Field Service, users must have Field Service permission. For Workforce
Engagement, the user needs to have a Workforce Engagement Admin or Planner permission set.

Fields

**Field** **Details**

```
BackgroundColor

Description

Duration

IsActive

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the shift like number of breaks or activities.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
How long the shift lasts. The unit of measurement for this field is determined by
### ShiftTemplateDurationType .

**Type**
boolean


Standard Objects ShiftTemplate

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is active or inactive.

```
IsNonStandard

JobProfileId

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Job Profile record. This field is optional.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last modified. Its label in the user interface is **Last**
**Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last viewed.


Standard Objects ShiftTemplate

**Field** **Details**

```
Name

OwnerId

RecordsetFilterCriteriaId

ShiftTemplateDurationType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The shift template record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift template.

This is a polymorphic relationship field.

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
The ID of the recordset filter criteria selected for the shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects Shipment

**Field** **Details**

**Description**
The unit of measurement for the shift template duration.

Possible values are:

**•** `H` —Hours

**•** `M` —Minutes

The default value is `H` .

```
StartTime

TimeSlotType

```

Associated Objects

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time of day when the shift starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are:

**•** `Normal`

**•** `Extended`

You can use _`Extended`_ to represent overtime shifts. Available in API version 55.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftTemplateOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ShiftTemplateShare on page 67**
Sharing is available for the object.

**ShiftTemplateChangeEvent on page 68**
Change Data Capture events are available for the object. Available in API version 54.0 and later.

### Shipment

Represents the transport of inventory in field service or a shipment of order items in Order Management.


Standard Objects Shipment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution

Fields

**Field Name** **Details**

```
ActualDeliveryDate

DeliveredToId

DeliveryMethodId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product was delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person or entity the product was delivered to.

This is a polymorphic relationship field.

**Relationship Name**
DeliveredTo

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
The delivery method used for the shipment.

This field is available in API version 51.0 and later.

```
Description

DestinationLocationId

ExpectedDeliveryDate

FulfillmentOrderId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The place the product is to be delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The fulfillment order that the shipment belongs to.

This field is available in API version 51.0 and later.


Standard Objects Shipment

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

OrderSummaryId

OwnerId

Provider

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order summary associated with the shipment.

This field is available in API version 51.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shipment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company or person making the transfer.

```
ReturnOrderId

ShipFromAddress

ShipFromCity

ShipFromCountry

ShipFromGeocodeAccuracy

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For a return Shipment, the associated ReturnOrder.

This field is available in API version 53.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The place the product is coming from. The compound form of the ship to address.
Read-only. For details on compound address fields, see Address Compound
Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment originates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
Accuracy level of the geocode for the address where the shipment originates.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

```
ShipFromLatitude

ShipFromLongitude

ShipFromPostalCode

ShipFromState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shipment

**Field Name** **Details**

**Description**
The state of the address where the shipment originates.

```
ShipFromStreet

ShipToAddress

ShipToCity

ShipToCountry

ShipToGeocodeAccuracy

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment originates.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the shipment is delivered. The compound form of
the ship to address. Read-only. For details on compound address fields, see
Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment is delivered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the shipment is delivered.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.


Standard Objects Shipment

**Field Name** **Details**

Note: This field is available in the API only.

```
ShipToLatitude

ShipToLongitude

ShipToName

ShipToPostalCode

ShipToState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The shipment recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment is delivered.

**Type**
string


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the shipment is delivered.

```
ShipToStreet

ShipmentNumber

SourceLocationId

Status

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment is delivered.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field service location where the shipment originates.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** _`Created`_ —Shipment has been created.


Standard Objects Shipment

**Field Name** **Details**

**•** _`Delivered`_ —Shipment has been delivered.

**•** _`In Transit`_ —Shipment is in transit.

**•** _`Shipped`_ —Order has been shipped.

**•** _`Voided`_ —Shipment has been cancelled.

```
TotalItemsQuantity

TrackingNumber

TrackingUrl

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total quantity of items included in the shipment. This value is calculated as
the sum of the quantities of the shipment items in the shipment.

This field is available in API version 51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Tracking number for the shipment.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL of website used for tracking the shipment.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShipmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ShipmentFeed**

Feed tracking is available for the object.

**ShipmentHistory**

History is available for tracked fields of the object.

**ShipmentOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects ShipmentItem

**ShipmentShare**

Sharing is available for the object.

SEE ALSO:

### ShipmentItem ShipmentItem

Represents an order item included in a shipment. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution

Fields

**Field** **Details**

```
Description

ExpectedDeliveryDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the shipment item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Expected delivery date of the shipment that contains the shipment item.


Standard Objects ShipmentItem

**Field** **Details**

```
FulfillmentOrderLineItemId

OrderItemSummaryId

Product2Id

Quantity

ReturnOrderLineItemId

```

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The FulfillmentOrderLineItem (fulfillment order product) corresponding to the shipment
item.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The OrderItemSummary (order product summary) corresponding to the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product represented by the shipment item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of products represented by the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ShipmentItem

**Field** **Details**

**Description**
For a return ShipmentItem, the associated ReturnOrderLineItem.

This field is available in API version 53.0 and later.

```
ShipmentId

ShipmentItemNumber

TrackingNumber

TrackingUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The shipment that contains the shipment item.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup

**Refers To**
Shipment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking number of the shipment that contains the shipment item.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking URL of the shipment that contains the shipment item.


### Standard Objects ShippingCarrier

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShipmentItemFeed**

Feed tracking is available for the object.

**ShipmentItemHistory**

History is available for tracked fields of the object.

SEE ALSO:

Shipment

FulfillmentOrderLineItem

### ShippingCarrier

Shipping company or carrier responsible for transporting goods or packages. Examples include UPS, FedEx, and USPS. This object is
available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingCarrier object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ExternalReference

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the shipping carrier associated with the delivery. Can
be used for internal tracking or integration purposes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ShippingCarrier

**Field** **Details**

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

```
LastViewedDate

ManagedShippingCarrier

Name

ShipFromCountry

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-managed shipping carrier information that provides estimated transit times. This
field is available in API version 65.0 and later.

Possible values are:

**•** `FEDEX`

**•** `UPS`

**•** `USPS`

**Type**
text

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Country where the shipment originates. This field is available in API version 65.0 and later.

Possible values are:

**•** `AD` —Andorra

**•** `AE` —United Arab Emirates

**•** `AF` —Afghanistan


Standard Objects ShippingCarrier

**Field** **Details**

**•** `AG` —Antigua and Barbuda

**•** `AI` —Anguilla

**•** `AL` —Albania

**•** `AM` —Armenia

**•** `AO` —Angola

**•** `AQ` —Antarctica

**•** `AR` —Argentina

**•** `AS` —American Samoa

**•** `AT` —Austria

**•** `AU` —Australia

**•** `AW` —Aruba

**•** `AX` —Aland Islands

**•** `AZ` —Azerbaijan

**•** `BA` —Bosnia and Herzegovina

**•** `BB` —Barbados

**•** `BD` —Bangladesh

**•** `BE` —Belgium

**•** `BF` —Burkina Faso

**•** `BG` —Bulgaria

**•** `BH` —Bahrain

**•** `BI` —Burundi

**•** `BJ` —Benin

**•** `BL` —Saint Barthélemy

**•** `BM` —Bermuda

**•** `BN` —Brunei Darussalam

**•** `BO` —Bolivia, Plurinational State of

**•** `BQ` —Bonaire, Sint Eustatius and Saba

**•** `BR` —Brazil

**•** `BS` —Bahamas

**•** `BT` —Bhutan

**•** `BV` —Bouvet Island

**•** `BW` —Botswana

**•** `BY` —Belarus

**•** `BZ` —Belize

**•** `CA` —Canada

**•** `CC` —Cocos (Keeling) Islands

**•** `CD` —Congo, the Democratic Republic of the

**•** `CF` —Central African Republic


Standard Objects ShippingCarrier

**Field** **Details**

**•** `CG` —Congo

**•** `CH` —Switzerland

**•** `CI` —Cote d'Ivoire

**•** `CK` —Cook Islands

**•** `CL` —Chile

**•** `CM` —Cameroon

**•** `CN` —China

**•** `CO` —Colombia

**•** `CR` —Costa Rica

**•** `CU` —Cuba

**•** `CV` —Cape Verde

**•** `CW` —Curaçao

**•** `CX` —Christmas Island

**•** `CY` —Cyprus

**•** `CZ` —Czechia

**•** `DE` —Germany

**•** `DJ` —Djibouti

**•** `DK` —Denmark

**•** `DM` —Dominica

**•** `DO` —Dominican Republic

**•** `DZ` —Algeria

**•** `EC` —Ecuador

**•** `EE` —Estonia

**•** `EG` —Egypt

**•** `EH` —Western Sahara

**•** `ER` —Eritrea

**•** `ES` —Spain

**•** `ET` —Ethiopia

**•** `FI` —Finland

**•** `FJ` —Fiji

**•** `FK` —Falkland Islands (Malvinas)

**•** `FM` —Micronesia

**•** `FO` —Faroe Islands

**•** `FR` —France

**•** `GA` —Gabon

**•** `GB` —United Kingdom

**•** `GD` —Grenada

**•** `GE` —Georgia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `GF` —French Guiana

**•** `GG` —Guernsey

**•** `GH` —Ghana

**•** `GI` —Gibraltar

**•** `GL` —Greenland

**•** `GM` —Gambia

**•** `GN` —Guinea

**•** `GP` —Guadeloupe

**•** `GQ` —Equatorial Guinea

**•** `GR` —Greece

**•** `GS` —South Georgia and the South Sandwich Islands

**•** `GT` —Guatemala

**•** `GU` —Guam

**•** `GW` —Guinea-Bissau

**•** `GY` —Guyana

**•** `HK` —Hong Kong SAR China

**•** `HM` —Heard Island and McDonald Islands

**•** `HN` —Honduras

**•** `HR` —Croatia

**•** `HT` —Haiti

**•** `HU` —Hungary

**•** `ID` —Indonesia

**•** `IE` —Ireland

**•** `IL` —Israel

**•** `IM` —Isle of Man

**•** `IN` —India

**•** `IO` —British Indian Ocean Territory

**•** `IQ` —Iraq

**•** `IR` —Iran, Islamic Republic of

**•** `IS` —Iceland

**•** `IT` —Italy

**•** `JE` —Jersey

**•** `JM` —Jamaica

**•** `JO` —Jordan

**•** `JP` —Japan

**•** `KE` —Kenya

**•** `KG` —Kyrgyzstan

**•** `KH` —Cambodia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `KI` —Kiribati

**•** `KM` —Comoros

**•** `KN` —Saint Kitts and Nevis

**•** `KP` —Korea, Democratic People's Republic of

**•** `KR` —Korea, Republic of

**•** `KW` —Kuwait

**•** `KY` —Cayman Islands

**•** `KZ` —Kazakhstan

**•** `LA` —Lao People's Democratic Republic

**•** `LB` —Lebanon

**•** `LC` —Saint Lucia

**•** `LI` —Liechtenstein

**•** `LK` —Sri Lanka

**•** `LR` —Liberia

**•** `LS` —Lesotho

**•** `LT` —Lithuania

**•** `LU` —Luxembourg

**•** `LV` —Latvia

**•** `LY` —Libya

**•** `MA` —Morocco

**•** `MC` —Monaco

**•** `MD` —Moldova, Republic of

**•** `ME` —Montenegro

**•** `MF` —Saint Martin (French part)

**•** `MG` —Madagascar

**•** `MH` —Marshall Islands

**•** `MK` —North Macedonia

**•** `ML` —Mali

**•** `MM` —Myanmar

**•** `MN` —Mongolia

**•** `MO` —Macao

**•** `MP` —Northern Mariana Islands

**•** `MQ` —Martinique

**•** `MR` —Mauritania

**•** `MS` —Montserrat

**•** `MT` —Malta

**•** `MU` —Mauritius

**•** `MV` —Maldives


Standard Objects ShippingCarrier

**Field** **Details**

**•** `MW` —Malawi

**•** `MX` —Mexico

**•** `MY` —Malaysia

**•** `MZ` —Mozambique

**•** `NA` —Namibia

**•** `NC` —New Caledonia

**•** `NE` —Niger

**•** `NF` —Norfolk Island

**•** `NG` —Nigeria

**•** `NI` —Nicaragua

**•** `NL` —Netherlands

**•** `NO` —Norway

**•** `NP` —Nepal

**•** `NR` —Nauru

**•** `NU` —Niue

**•** `NZ` —New Zealand

**•** `OM` —Oman

**•** `PA` —Panama

**•** `PE` —Peru

**•** `PF` —French Polynesia

**•** `PG` —Papua New Guinea

**•** `PH` —Philippines

**•** `PK` —Pakistan

**•** `PL` —Poland

**•** `PM` —Saint Pierre and Miquelon

**•** `PN` —Pitcairn

**•** `PR` —Puerto Rico

**•** `PS` —Palestine

**•** `PT` —Portugal

**•** `PW` —Palau

**•** `PY` —Paraguay

**•** `QA` —Qatar

**•** `RE` —Reunion

**•** `RO` —Romania

**•** `RS` —Serbia

**•** `RU` —Russian Federation

**•** `RW` —Rwanda

**•** `SA` —Saudi Arabia


Standard Objects ShippingCarrier

**Field** **Details**

**•** `SB` —Solomon Islands

**•** `SC` —Seychelles

**•** `SD` —Sudan

**•** `SE` —Sweden

**•** `SG` —Singapore

**•** `SH` —Saint Helena, Ascension and Tristan da Cunha

**•** `SI` —Slovenia

**•** `SJ` —Svalbard and Jan Mayen

**•** `SK` —Slovakia

**•** `SL` —Sierra Leone

**•** `SM` —San Marino

**•** `SN` —Senegal

**•** `SO` —Somalia

**•** `SR` —Suriname

**•** `SS` —South Sudan

**•** `ST` —Sao Tome and Principe

**•** `SV` —El Salvador

**•** `SX` —Sint Maarten (Dutch part)

**•** `SY` —Syrian Arab Republic

**•** `SZ` —Eswatini

**•** `TC` —Turks and Caicos Islands

**•** `TD` —Chad

**•** `TF` —French Southern Territories

**•** `TG` —Togo

**•** `TH` —Thailand

**•** `TJ` —Tajikistan

**•** `TK` —Tokelau

**•** `TL` —Timor-Leste

**•** `TM` —Turkmenistan

**•** `TN` —Tunisia

**•** `TO` —Tonga

**•** `TR` —Türkiye

**•** `TT` —Trinidad and Tobago

**•** `TV` —Tuvalu

**•** `TW` —Taiwan

**•** `TZ` —Tanzania, United Republic of

**•** `UA` —Ukraine

**•** `UG` —Uganda


### Standard Objects ShippingCarrierMethod

**Field** **Details**

**•** `UM` —U.S. Outlying Islands

**•** `US` —United States

**•** `UY` —Uruguay

**•** `UZ` —Uzbekistan

**•** `VA` —Holy See (Vatican City State)

**•** `VC` —Saint Vincent and the Grenadines

**•** `VE` —Venezuela, Bolivarian Republic of

**•** `VG` —Virgin Islands, British

**•** `VI` —U.S. Virgin Islands

**•** `VN` —Vietnam

**•** `VU` —Vanuatu

**•** `WF` —Wallis and Futuna

**•** `WS` —Samoa

**•** `YE` —Yemen

**•** `YT` —Mayotte

**•** `ZA` —South Africa

**•** `ZM` —Zambia

**•** `ZW` —Zimbabwe

```
OwnerId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrier object. Default value is the user logged
in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### ShippingCarrierMethod

Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of transit
times available for each carrier. This object is available in API version 61.0 and later.


Standard Objects ShippingCarrierMethod

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingCarrierMethodId object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ExternalReference

LastReferencedDate

LastViewedDate

ManagedShippingCarrierMethod

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the shipping carrier associated with the delivery. Can
be used for internal tracking or integration purposes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-managed shipping carrier method that provides estimated transit times. This field
is available in API version 65.0 and later.


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
MaxTransitTime

MinTransitTime

Name

OwnerId

```

**Type**
integer

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Maximum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the maximum transit time is set to 3, the carrier takes no more than 3 units
of the specified transit time unit to deliver the order.

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the minimum transit time is set to 1, the carrier takes at least 1 unit of the
specified transit time unit to deliver the order.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrierMethod object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
ShippingCarrierId

ShippingScope

TransitTimeUnit

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Id of the company or service responsible for transporting and delivering the order to the
customer.

This is a relationship field.

**Relationship Name**
ShippingCarrier

**Refers To**
ShippingCarrier

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of shipping carrier method. This field is available in API version 65.0 and later.

Possible values are:

**•** `Domestic`

**•** `DomesticAndInternational`

**•** `International`

The default value is `Domestic` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Unit of measurement used for transit time. Specifies the time interval in which the minimum
and maximum transit times are expressed.

The available options are:

**•** `Days`

**•** `Hours`

**•** `Weeks`


### Standard Objects ShippingConfigurationSet ShippingConfigurationSet

Shipping configuration for a set of products in a store. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingConfigurationSet object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
IsDefault

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shipping configuration is the default `(True)` or not `(False)` .

The default value is `False` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping configuration set.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the shipping configuration owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects ShippingConfigSetProduct

**Field** **Details**

**Refers To**
Group, User

```
ProcessTime

ProcessTimeUnit

TargetRecordId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time to process an order before it is ready to ship.

The default value is `1 Day` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time to process an order.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the target record.

This field is a relationship field.

**Relationship Name**
TargetRecord

**Relationship Type**
Lookup

**Refers To**
WebStore

### ShippingConfigSetProduct

Represents a product associated with a shipping configuration. This object is available in API version 64.0 and later.


Standard Objects ShippingConfigSetProduct

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingConfigSetProduct object is available only if you've a B2B Commerce or D2C Commerce license and the MultipleShippingProfile
org perm is enabled.

Fields

**Field** **Details**

```
Name

Product2Id

ShippingProfileId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping configuration set product record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Product2 record that is associated with shipping configuration set record.

This field is a relationship field.

**Relationship Name**
Product2

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile


### Standard Objects ShippingRateArea

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ShippingConfigurationSet (the master object)

### ShippingRateArea

A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateArea object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Countries

Name

Regions

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Countries in the shipping rate area.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate area.

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects ShippingRateGroup

**Field** **Details**

**Description**
Reserved for future use.

### `ShippingRateGroupId` ShippingRateGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping rate group

This field is a relationship field.

**Relationship Name**
### ShippingRateGroup

**Relationship Type**
Lookup

**Refers To**
### ShippingRateGroup

Available shipping rates based on shipping destination. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate group.


### Standard Objects SignupRequest

**Field** **Details**

```
ShippingProfileId

### SignupRequest

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile

**Relationship Type**
Lookup

**Refers To**
ShippingConfigurationSet

Represents a request for a new sign-up. SignupRequest isn’t supported in sandbox instances and will result in an error. This object is
available in API version 27.0 and later.

[Note: You’re limited to 20 sign-ups per day. To make additional sign-ups, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com)
For product, specify **Sales** . For topic, specify **AppExchange & Managed Packages** .

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Fields

**Field Name** **Details**

```
AuthCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A one-time authorization code that can be exchanged for an OAuth access token and refresh
token using standard Salesforce APIs. It’s used with `ConnectedAppCallbackUrl` and
`ConnectedAppConsumerKey` when the specified connected app hasn’t been configured
with an X.509 certificate. The system provides this read-only field after the sign-up request
has been processed. This field is available in API version 29.0 and later.


Standard Objects SignupRequest

**Field Name** **Details**

```
Company

ConnectedAppCallbackUrl

ConnectedAppConsumerKey

Country

CreatedOrgId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the company requesting the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with `ConnectedAppConsumerKey`, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with `ConnectedAppCallbackUrl`, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The default value is the country of the requesting org. To override the default, enter the
two-character, uppercase ISO-3166 country code (Alpha-2 code). A complete list of the codes
[is located at https://www.iso.org/obp/ui/#search. The language of the trial org is](https://www.iso.org/obp/ui/#search)
auto-determined based on the value of this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the trial org created. The system provides this read-only field after
