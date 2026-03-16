is null, it adopts the duration value from the Work Type object when the work
type is updated or inserted.

Work order duration and work order line item duration are independent of each
other. If you want work order duration to automatically show the sum of the
work order line items’ duration, replace the Duration field on work orders with a
custom roll-up summary field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The estimated duration in minutes. For internal use only.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The date when the work order is completed. This field is blank unless you set up
an Apex trigger or quick action to populate it. For example, you can create a quick
action that sets the `EndDate` to 365 days after the `StartDate` .

```
EntitlementId

GeocodeAccuracy

GrandTotal

IsClosed

IsGeneratedFromMaintenancePlan

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entitlement associated with the work order.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total price of the work order with tax added.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the work order is closed ( `true` ) or open ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
(Read Only) Indicates that the work order was generated from a maintenance
plan ( `true` ), rather than manually created ( `false` ).


Standard Objects WorkOrder

**Field Name** **Details**

```
IsStopped

LastReferencedDate

LastViewedDate

Latitude

LineItemCount

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a milestone is paused ( `true` ) or counting down ( `false` ).
This field is available only if **Enable stopped time and actual elapsed time** is
selected on the Entitlement Settings page.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of work order line items in the work order. Its label in the user
interface is `Line Items` .


Standard Objects WorkOrder

**Field Name** **Details**

```
LocationId

Longitude

MaintenancePlanId

MaintenanceWorkRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the work order. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order. When the work order is
auto-generated from a maintenance plan, this field automatically lists the related
plan.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this work order. This field is
available in API version 50.0 and above.


Standard Objects WorkOrder

**Field Name** **Details**

```
MilestoneStatus

MinimumCrewSize

OwnerId

ParentWorkOrderId

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the status of a milestone. This field is visible if an entitlement process
is applied to a work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the work order.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order’s minimum crew size requirement.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The work order’s assigned owner.

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
The work order’s parent work order, if it has one. Create a custom report to view
a work order’s child work orders.

This is a relationship field.


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Name**
ParentWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

PostWorkSummary

```
PostalCode

```

PreWorkBriefPromptTemplate

```
Pricebook2Id

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of a completed work order that’s either entered manually or created
by an AI agent.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the activated Pre-Work Brief prompt template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price book associated with the work order. Adding a price book to the work
order lets you assign different price book entries to the work order’s line items.
This is only available if Product2 is enabled.

This is a relationship field.

**Relationship Name**
Pricebook2


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
Priority

ProductServiceCampaignId

ProductServiceCampaignItemId

RecommendedCrewSize

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the work order. The picklist includes the following values, which
can be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the work
order. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.


Standard Objects WorkOrder

**Field Name** **Details**

```
ReturnOrderId

ReturnOrderLineItemId

RootWorkOrderId

ServiceAppointmentCount

ServiceContractId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level work order in a work order hierarchy. Depending on
where a work order lies in the hierarchy, its root could be the same as its parent.
View a work order’s child work order in the Child Work Orders related list.

This is a relationship field.

**Relationship Name**
RootWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The service contract associated with the work order.

```
ServiceDocumentTemplate

ServiceReportLanguage

ServiceReportTemplateId

ServiceTerritoryId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for all service reports and service report previews created for
the work order, its service appointments, and its work order line items and their
service appointments. If the field is blank, service reports are generated in the
default language in Salesforce of the person creating the report.

To appear as an option in the ServiceReportLanguage field, a language must be
[set up in Translation Workbench or be one of Salesforce’s 18 fully supported](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
[languages. Rich text fields and service report section names aren’t translated.](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template that the work order uses. If you don’t specify a service
report template on a work order, it uses the service report template listed on its
work type. If the work type doesn’t list a template or no work type is specified,
the work order uses the default service report template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the work order is taking place.

This is a relationship field.


Standard Objects WorkOrder

**Field Name** **Details**

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
SlaExitDate

SlaStartDate

StartDate

State

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the work order exits the entitlement process.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the work order enters the entitlement process. You can update or
reset the time if you have “Edit” permission on work orders.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the work order goes into effect. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the StartDate to the date when the Status changes to In
Progress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the work order is completed. Maximum length is 80 characters.

**Type**
picklist


Standard Objects WorkOrder

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the work order. The picklist includes the following values, which
can be customized:

**•** `New` —Work order was created, but there hasn’t yet been any activity.

**•** `In Progress` —Work has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

Changing a work order’s status does not affect the status of its work order line
items or associated service appointments.

```
StatusCategory

StopStartDate

Street

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field has eight default values: seven values which are identical to the default
`Status` values, and a `None` value for statuses without a status category.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Waiting for Response`_ value,
you may decide that it belongs in the _`On Hold`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the milestone was paused. The label in the user interface is
`Stopped Since` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
The street number and name where the work order is completed.

```
Subject

Subtotal

SuggestedMaintenanceDate

Tax

TotalPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the work order. Try to describe the nature and purpose of the job
to be completed. For example, “Annual On-Site Well Maintenance.” Maximum
length is 255 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total of the work order line items’ subtotals before discounts and
taxes are applied.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The suggested date that the work order is completed. When the work order is
auto-generated from a maintenance plan, this field is automatically populated
based on the maintenance plan’s settings.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total tax on the work order. You can enter a number with or without the
currency symbol and use up to two decimal places. For example, in a work order
whose total price is $100, enter $10 to apply a 10% tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects WorkOrder

**Field Name** **Details**

**Description**
Read only. The total of the work order line items’ prices. This value has discounts
applied but not tax.

```
WorkOrderNumber

WorkTypeId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An eight-digit, auto-generated number that identifies the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the work order. When a work type is selected, the
work order automatically inherits the work type’s `Duration`, `Duration`
`Type`, and required skills. If the `Duration` field for the work type is null, enter
the duration value.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderFeed**

Feed tracking is available for the object.

**WorkOrderHistory**

History is available for tracked fields of the object.

**WorkOrderOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects WorkOrderHistory

**WorkOrderShare**

Sharing is available for the object.

### WorkOrderHistory

Represents the history of changes made to tracked fields on a work order. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Work orders or Field Service must be enabled in your organization, and field tracking for work order fields must be configured.

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


### Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

```
WorkOrderId

### WorkOrderLineItem

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the work order being tracked. The history is displayed on the detail page
for this record.

This is a relationship field.

**Relationship Name**
### WorkOrder

**Relationship Type**
Lookup

**Refers To**
### WorkOrder

Represents a subtask on a work order in field service. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Work orders or Field Service must be enabled.

Fields

**Field Name** **Details**

```
Address

```

**Type**
address


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable

**Description**
The compound form of the address where the line item is completed.

```
AssetId

AssetWarrantyId

City

Country

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the work order line item. The asset is not automatically
inherited from the parent work order.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset warranty term associated with the work order line item. This field is
available in API version 50.0 and above.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the line item is completed. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the line item is completed. Maximum length is 80 characters.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

```
CurrencyIsoCode

Description

Discount

Duration

DurationInMinutes

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization. The label in the user interface
is `Currency ISO Code` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work order line item. Try to describe the steps needed to
mark the line item Completed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percent discount to apply to the line item. You can enter a number with or
without the percent symbol, and you can use up to two decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated time required to complete the line item. Specify the duration unit
in the `Duration Type` field. If the `Duration` field on a Work Order is null,
it adopts the duration value from the Work Type object when the work type is
updated or inserted.

Note: Work order duration and work order line item duration are
independent of each other. If you want work order duration to
automatically show the sum of the work order line items’ duration, replace
the Duration field on work orders with a custom roll-up summary field.

**Type**
double


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The estimated duration in minutes. For internal use only.

```
DurationType

EndDate

GeocodeAccuracy

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the line item is completed. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the EndDate to 365 days after the StartDate.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

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


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**•** `Unknown`

**•** `Zip`

```
IsClosed

IsGeneratedFromMaintenancePlan

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the line item has been closed. Changing the line item’s status
to `Closed` causes this checkbox to be selected in the user interface (sets
`IsClosed` to `true` ).

Tip: Use this field to report on closed versus open work order line items.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Identifies whether the work order line item is generated from a maintenance
plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Used with `Longitude` to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

Note: This field is available in the API only.

```
LineItemNumber

ListPrice

LocationId

Longitude

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number that identifies the work order line item. Each work
order’s line items start at 1.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

The price of the line item (product) as listed in its corresponding price book entry.
If a price book entry isn’t specified, the list price defaults to zero.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A location associated with the work order line item. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Used with `Latitude` to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.

```
MaintenancePlanId

MaintenanceWorkRuleId

MinimumCrewSize

OrderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this line item. This field is available
in API version 50.0 and above.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the line item.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order line item’s minimum crew size
requirement.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order associated with the line item. For example, you may need to order
replacement parts before you can complete the line item.

This is a relationship field.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

```
ParentWorkOrderLineItemId

PostalCode

PricebookEntryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent work order line item, if it has one.

Tip: Create a custom report to view a line item’s child line items.

This is a relationship field.

**Relationship Name**
ParentWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the line item is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price book entry (product) associated with the line item. The label in the user
interface is `Product` . This field’s lookup search only returns products that are
included in the work order’s price book.

This is a relationship field.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

```
Priority

Product2Id

ProductServiceCampaignId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the line item. The picklist includes the following values, which can
be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Read only) The product associated with the price book entry. This field is not
available in the user interface. For best results, use the `PricebookEntryId`
field in any custom code or layouts.

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
The product service campaign associated with the work order line item.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

```
ProductServiceCampaignItemId

Quantity

RecommendedCrewSize

ReturnOrderId

ReturnOrderLineItemId

RootWorkOrderLineItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Number of units of the line item included in the associated work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the line
item. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
(Read only) The top-level line item in a work order line item hierarchy. Depending
on where a line item lies in the hierarchy, its root could be the same as its parent.

Note: View a line item’s child line items in the Child Work Order Line
Items related list.

This is a relationship field.

**Relationship Name**
RootWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

```
ServiceAppointmentCount

ServiceDocumentTemplate

ServiceReportTemplateId

ServiceTerritoryId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order line item.

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
The service report template that the line item uses. If you don’t specify a service
report template on a work order line item, it uses the service report template
listed on its work type. If the work type doesn’t list a template or no work type is
specified, the line item uses the default service report template.

**Type**
reference


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the line item is completed.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

```
StartDate

State

Status

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the line item goes into effect. This field is blank unless you
set up an Apex trigger or quick action to populate it. For example, you can create
a quick action that sets the StartDate to the date when the Status changes to In
Progress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the line item is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the line item. The picklist includes the following values, which can
be customized:

**•** `New` —Line item was created, but there hasn’t yet been any activity.

**•** `In Progress` —Work has begun.

**•** `On Hold` —Work is paused.

**•** `Completed` —Work is complete.

**•** `Cannot Complete` —Work could not be completed.


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**•** `Closed` —All work and associated activity is complete.

**•** `Canceled` —Work is canceled, typically before any work began.

```
StatusCategory

Street

Subject

Subtotal

SuggestedMaintenanceDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field has eight default values: seven values which are identical to the default
`Status` values, and a `None` value for statuses without a status category.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a _`Waiting for Response`_ value,
you may decide that it belongs in the _`On Hold`_ category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the line item is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A word or phrase describing the line item.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

(Read only) The line item’s unit price multiplied by the quantity.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkOrderLineItem

**Field Name** **Details**

**Description**
Date when maintenance work is planned.

```
TotalPrice

UnitPrice

WorkOrderId

WorkTypeId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The line item’s subtotal with discounts applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Initially, the unit price for a work order line item is the line item’s list price from
the price book, but you can change it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The line item’s parent work order. Because work order line items must be
associated with a work order, this is a required field.

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
The work type associated with the line item. When a work type is selected, the
line item automatically inherits the work type’s `Duration`, `Duration Type`,
and required skills. If the `Duration` field for the work type is null, enter the
duration value.


### Standard Objects WorkOrderLineItemHistory

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Usage

A work order line item is a child record of a work order. It represents a specific subtask on a work order.

For example, suppose a customer purchased a truck from you. The truck is represented as an asset in your Salesforce org. After some
time, the truck needs both headlight bulbs replaced. Here’s one way that you can use work orders and work order line items to track
the repair.

**1.** Create a work order named “Replace Headlight Bulbs” from the asset record detail page.

**2.** Add three work order line items to the work order: “Replace Left Headlight Bulb,” “Replace Right Headlight Bulb,” and “Test Headlights.”

**3.** Assign the work order to a technician via a queue.

**4.** As the technician completes each line item, he or she marks the item `Completed` .

**5.** When all the line items are complete, the technician marks the work order `Completed` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderLineItemFeed**

Feed tracking is available for the object.

### **WorkOrderLineItemHistory**

History is available for tracked fields of the object.

### WorkOrderLineItemHistory

Represents the history of changes made to tracked fields on a work order line item. This object is available in API version 36.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects WorkOrderLineItemHistory

Special Access Rules

Work orders or Field Service must be enabled in your organization, and field tracking for work order line item fields must be configured.

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

WorkOrderLineItemId

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
ID of the work order line item being tracked. The history is displayed on the detail
page for this record.


### Standard Objects WorkOrderLineItemStatus

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
### WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
### WorkOrderLineItem WorkOrderLineItemStatus

Represents a possible status of a work order line item in field service.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

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
Indicates that the status value is the default status on work orders. Only one status
value can be the default.

**Type**
string


### Standard Objects WorkOrderShare

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value that appears in the UI.

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
The value’s position in the drop-down list of values in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.

The Status field on work order line items comes with the following values:

**•** New—Line item was created, but there hasn’t yet been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The WorkOrderLineItemStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled By
Customer—creates a work order line item status record, and vice versa.

Note: Work order line items also come with a StatusCategory field whose values are identical to the default Status values. If you
create custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_
value, you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory,
[see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### WorkOrderShare

Represents a sharing entry on a work order. This object is available in API version 36.0 and later.


Standard Objects WorkOrderShare

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Work orders or Field Service must be enabled in your organization. External users can’t access this object.

Fields

**Field Name** **Details**

```
AccessLevel

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the work order. The possible values
are:

**•** _`Read`_

**•** _`Edit`_

**•** _`All`_ (This value isn’t valid for create or update calls.)

Set to an access level that is at least equal to the organization’s default work order
access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The work order associated with the sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


### Standard Objects WorkOrderStatus

**Field Name** **Details**

**Refers To**
### WorkOrder

```
RowCause

UserOrGroupId

### WorkOrderStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited. Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the work order.

**•** `Owner` —The User is the owner of the work order.

**•** `Rule` —The User or Group has access via a work order sharing rule.

**•** `GuestRule` —The User or Group has access via a work order guest user
sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Read Only) ID of the user or group that has access to the work order.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Represents a possible status of a work order in field service.


Standard Objects WorkOrderStatus

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

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
Indicates that the status value is the default status on work orders. Only one status
value can be the default.

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


### Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.

Usage

The Status field on work orders comes with the following values:

**•** New—Work order was created, but there hasn’t yet been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The WorkOrderStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled By
Customer—creates a work order status record, and vice versa.

Note: Work orders also come with a StatusCategory field whose values are identical to the default Status values. If you create
custom Status values, you must indicate which category it belongs to. For example, if you create a _`Customer Absent`_ value,
you may decide that it belongs in the _`Cannot Complete`_ category. To learn which processes reference StatusCategory, see
[How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

### WorkPerformanceCycle

Represents feedback that is gathered to assess the performance of a specific set of employees.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ActivityFrom

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Description**
The date that you want to start filtering the WDC objects to help requesters create
accurate summaries. The start of the evaluation period.

```
ActivityTo

CurrentTask

LastManagerRequestsSharedDate

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date that you want to stop filtering the WDC objects to help requesters create
accurate summaries. The end of the evaluation period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The current task that the performance summary cycle is engaged in, including
deploying and sharing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when all manager requests are set to be shared.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkPerformanceCycle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects WorkPerformanceCycle

**Field Name** **Details**

**Description**
The time stamp that indicates when the current user last viewed this
WorkPerformanceCycle. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

State

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the performance summary cycle that employees will participate in.
This name is created by the administrator and is visible on all respective
notifications and in the UI.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkPerformanceCycle.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state that the performance summary cycle is in. Available pick list values:

**•** Setup: The summary is in draft.

**•** In Progress: The summary is deployed and people are answering the questions
that were created.

**•** Finished: The summary is no longer in progress.

**•** Error: The summary encountered an error.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkPerformanceCycleFeed**

Feed tracking is available for the object.

**WorkPerformanceCycleHistory**

History is available for tracked fields of the object.


### Standard Objects WorkPlan

**WorkPerformanceCycleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPerformanceCycleShare**

Sharing is available for the object.

### WorkPlan

Represents a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

ExecutionOrder

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the work plan is executed. Only positive values or null are supported.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:


Standard Objects WorkPlan

**Field** **Details**

```
LastViewedDate

Name

OwnerId

ParentRecordId

```

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the work plan.

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
The ID of the work order, work order line item, or change request that the work plan is
associated with. Available in API version 54.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup


Standard Objects WorkPlan

**Field** **Details**

**Refers To**
ChangeRequest, WorkOrder, WorkOrderLineItem

```
ParentRecordType

WorkOrderId

WorkOrderLineItemId

WorkPlanTemplateId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes whether the parent record is a work order, work order line item, or change request.
Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the work order.

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
The ID of the work order line item.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects WorkPlanSelectionRule

**Field** **Details**

**Description**
The ID of the work plan template record. Available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
WorkPlanTemplate

**Relationship Type**
Lookup

**Refers To**
WorkPlanTemplate

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanChangeEvent on page 68**
Change events are available for the object. Available in API version 54.0 and later.

**WorkPlanFeed on page 55**
Feed tracking is available for the object.

**WorkPlanHistory on page 63**
History is available for tracked fields of the object.

**WorkPlanOwnerSharingRule on page 65**
Sharing rules are available for the object.

**WorkPlanShare on page 67**
Sharing is available for the object.

### WorkPlanSelectionRule

Represents a rule that selects a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkPlanSelectionRule

Fields

**Field** **Details**

```
AssetId

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the selection rule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this selection rule is active ( `true` ) or not ( `false` ). Default is `false` .
Label is Active.

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


Standard Objects WorkPlanSelectionRule

**Field** **Details**

```
LocationId

OwnerId

Product2Id

ServiceTerritoryId

WorkPlanSelectionRuleNumber

WorkPlanTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the location.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product. Label is Product.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number of the work plan selection rule, for example, WPSR-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work plan template.


### Standard Objects WorkPlanTemplate

**Field** **Details**

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanSelectionRuleChangeEvent**

Change events are available for the object.

**WorkPlanSelectionRuleFeed**

Feed tracking is available for the object.

**WorkPlanSelectionRuleHistory**

History is available for tracked fields of the object.

**WorkPlanSelectionRuleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanSelectionRuleShare**

Sharing is available for the object.

### WorkPlanTemplate

Represents a template for a work plan. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects WorkPlanTemplate

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan template.

```
IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether the specific template is available for application ( `true` ) or not ( `false` ).
Default is `false` . Label is Active.

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

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects WorkPlanTemplateEntry

**Field** **Details**

**Description**
The ID of the owner who created the work plan template.

```
RelativeExecutionOrder

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The relative execution order for sorting the work plan when it’s applied to the work order or
work order line item. Only positive integers are supported.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateChangeEvent**

Change events are available for the object.

**WorkPlanTemplateFeed**

Feed tracking is available for the object.

**WorkPlanTemplateHistory**

History is available for tracked fields of the object.

**WorkPlanTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanTemplateShare**

Sharing is available for the object.

### WorkPlanTemplateEntry

Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkPlanTemplateEntry

Fields

**Field** **Details**

```
ExecutionOrder

LastReferencedDate

LastViewedDate

WorkPlanTemplateEntryNumber

WorkPlanTemplateId

WorkStepTemplateId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequence number of when this entry is executed. Only positive values are supported.

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

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number of the work plan template entry, for example, WPTE-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the work plan template.

**Type**
reference


### Standard Objects WorkReward

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work step template.

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateEntryChangeEvent**

Change events are available for the object.

**WorkPlanTemplateEntryFeed**

Feed tracking is available for the object.

**WorkPlanTemplateEntryHistory**

History is available for tracked fields of the object.

### WorkReward

Used to store reward codes tied to a Reward Fund. Reward Funds must have at least one WorkReward record.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the Reward permission enabled in order to use the Rewards feature, including WorkRewardFund and WorkReward.

Additional Considerations and Related Objects

### WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record to be available for use. Each

WorkBadge record with a `RewardId` indicates a reward badge given to a Recipient.

Fields

**Field Name** **Details**

```
Code

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects WorkReward

**Field Name** **Details**

**Description**
Represents a singe reward code tied to a RewardFundId.

```
OwnerId

RecipientId

RedemptionDisclaimer

RedemptionInfo

RedemptionUrl

RewardFundId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the User ID of Owner of WorkReward record

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce User ID for User associated with this WorkReward record.

**Type**
textarea

**Properties**
Nillable

**Description**
The disclaimer information about the WorkReward.

**Type**
textarea

**Properties**
Nillable

**Description**
The instructions for redeeming the WorkReward.

**Type**
textarea

**Properties**
Nillable

**Description**
The URL for redeeming the WorkReward.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects WorkRewardFund

**Field Name** **Details**

**Description**
Salesforce unique ID for WorkRewardFund record that is associated with
WorkReward record.

```
RewardFundTypeId

Value

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType associated with the
WorkReward.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of the WorkReward.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardShare**

Sharing is available for the object.

### WorkRewardFund

Represents a Reward Fund and describes the Reward Fund attributes.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkRewardFund

Special Access Rules

To use the Rewards feature, including WorkRewardFund and WorkReward, you must have the Reward permission enabled. To create
Rewards, the user must have Create on WorkRewardFund, which is not a standard permission.

Additional Considerations and Related Objects

WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record available. Each
WorkBadgeDefinition with a RewardFundId is a “Reward Badge.”

Fields

**Field Name** **Details**

```
IsActive

LastReferencedDate

LastViewedDate

Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the WorkRewardFund is active ( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFund.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFund. If this value is null, this record might have been only referenced
( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the Reward Fund.


Standard Objects WorkRewardFund

**Field Name** **Details**

```
OwnerId

RewardFundTypeId

TotalCodeCount

Type

UsedCodeCount

Value

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of User who is the Owner of the WorkRewardFund record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType that is associated with the
WorkRewardFund.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are available in the WorkRewardFund. Derived from
WorkReward records that are associated with the WorkRewardFund.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
RewardType of the WorkRewardFund. Default is Amazon.com.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are used in the WorkRewardFund. Derived from the total
assigned WorkReward records that are associated with the WorkRewardFund.

**Type**
currency

**Properties**
Create, Filter, Sort, Update


### Standard Objects WorkRewardFundType

**Field Name** **Details**

**Description**
Value of each of the reward codes in the WorkRewardFund.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundFeed**

Feed tracking is available for the object.

**WorkRewardFundHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundShare**

Sharing is available for the object.

### WorkRewardFundType

Represents the type of WorkRewardFund object.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CreditSystem

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects WorkRewardFundType

**Field Name** **Details**

**Description**
The credit system that is used by the WorkRewardFundType object (gift codes
or points). If points are selected, the reward message will not consider the
`CurrencyCode` field.

```
CurrencyCode

IsActive

IsPredefined

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency code of the WorkRewardFundType

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the WorkRewardFundType is active and available in the UI

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the WorkRewardFundType is predefined ( `true` ) or not ( `false` )

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFundType.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFundType. If this value is null, this record might have been only
referenced ( `LastReferencedDate` ) and not viewed.


Standard Objects WorkRewardFundType

**Field Name** **Details**

```
Name

OwnerId

RedemptionDisclaimer

RedemptionInfo

RedemptionUrl

UploadCodeColumn

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkRewardFundType

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the WorkRewardFundType owner

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The redemption disclaimer text for the WorkRewardFundType

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Redemption text for the WorkRewardFundType

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that’s linked to the redemption

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects WorkStep

**Field Name** **Details**

**Description**
The column where the reward code is contained in the CSV file. The upload uses
the second value by default.

```
UploadValueColumn

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The column where the reward value is contained in the CSV file. The upload uses
the third column by default.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundTypeFeed**

Feed tracking is available for the object.

**WorkRewardFundTypeHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeShare**

Sharing is available for the object.

### WorkStep

Represents a work step in a work plan. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.


Standard Objects WorkStep

Fields

**Field** **Details**

```
ActionDefinition

ActionType

Description

EndTime

ExecutionOrder

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org. To launch Lightning Web Components from
Work Steps, you must use `QuickAction` on the action definition.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step ends. The value must be greater than or equal to
`StartTime` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects WorkStep

**Field** **Details**

**Description**
The order in which the work step is executed. Only positive integer values or null are
supported.

```
LastReferencedDate

LastViewedDate

Name

PausedFlowInterviewId

ProcessType

```

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

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The user-defined name of the work step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated ID of the flow interview paused by a user.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow process type launched from the work step.

Possible values are:


Standard Objects WorkStep

**Field** **Details**

**•** `DataCaptureFlow` —Data Capture Flow

**•** `DiscoveryFrameworkFlow` —Discovery Framework Data Capture Flow (Beta)

**•** `FieldServiceMobileFlow` —Field Service Mobile Flow

The default value is `DataCaptureFlow` .

```
StartTime

Status

StatusCategory

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The customizable status of the work order. Every status must be mapped to a status category,
but there can be status categories not mapped to a status.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Not Applicable`

**•** `Paused`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each status value belongs to. Each default status category is mapped to
the corresponding default status. If you create a custom status, you must indicate which
[status category it belongs to. To learn which processes reference StatusCategory, see How](https://help.salesforce.com/articleView?id=service.fs_status_categories.htm&type=5&language=en_US)
[are Status Categories Used?.](https://help.salesforce.com/articleView?id=service.fs_status_categories.htm&type=5&language=en_US)

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`


Standard Objects WorkStep

**Field** **Details**

**•** `Paused`

```
WorkOrderId

WorkOrderLineItemId

WorkPlanExecutionOrder

WorkPlanId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the work order line item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the plan execution order.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work plan.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepChangeEvent**

Change events are available for the object.

**WorkStepFeed**

Feed tracking is available for the object.

**WorkStepHistory**

History is available for tracked fields of the object.


### Standard Objects WorkStepStatus WorkStepStatus

Represents a picklist for a status category on a work step. This object is available in API version 52.0 and later.

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

SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The name of the work step status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Controls whether this status is the default value of the picklist of the corresponding status
category ( `true` ) or not ( `false` ). Default is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. The label of the work step status.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects WorkStepTemplate

**Field** **Details**

**Description**
Required. The order in which the work step statuses are displayed in the status category's
picklist.

```
StatusCode

### WorkStepTemplate

```

**Type**
picklist

**Properties**
Required. Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that this status belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`

**•** `Paused`

Represents a template for a work step. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ActionDefinition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects WorkStepTemplate

**Field** **Details**

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org.

```
ActionType

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step template.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this work step template is active `true` or not `false` . Default is `false` .

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


### Standard Objects WorkThanks

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

```
Name

OwnerId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work step template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner who created the work step template.

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepTemplateChangeEvent**

Change events are available for the object.

**WorkStepTemplateFeed**

Feed tracking is available for the object.

**WorkStepTemplateHistory**

History is available for tracked fields of the object.

**WorkStepTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkStepTemplateShare**

Sharing is available for the object.

### WorkThanks

Represents the source and message of a thanks post.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects WorkThanks

Additional Considerations and Related Objects

WorkBadge is a lookup to WorkThanks. Each WorkBadge record must derive a SourceId from WorkThanks.

Fields

**Field Name** **Details**

```
FeedItemId

GiverId

Message

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the FeedItem related to the thanks badge.

This is a relationship field.

**Relationship Name**
FeedItem

**Relationship Type**
Lookup

**Refers To**
FeedItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce user ID for the giver of the Thanks record.

This is a relationship field.

**Relationship Name**
Giver

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create

**Description**
Required. Message associated with the Thanks record.


### Standard Objects WorkType

**Field Name** **Details**

```
NetworkId

OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the community that this WorkThanks is associated with. This field is
available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce user ID for the owner of the badge record (typically the same user as
the giver of the record).

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkThanksChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkThanksOwnerSharingRule**

Sharing rules are available for the object.

**WorkThanksShare**

Sharing is available for the object.

### WorkType

Represents a type of work to be performed in Field Service and Lightning Scheduler. Work types are templates that can be applied to
work order or work order line items. This object is available in API version 38.0 and later.


Standard Objects WorkType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
Description

DurationType

EstimatedDuration

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work type. Try to add details about the task or tasks that
this work type represents.

**Type**
picklist

**Properties**
Create, Filter, Group, Defaulted on create, Restricted picklist, Sort, Update

**Description**
The unit of the `Estimated Duration` : Minutes or Hours.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The estimated length of the work. The estimated duration is in minutes or hours
based on the value selected in the `Duration Type` field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work type was last modified. Its label in the user interface is
`Last Modified Date` .


Standard Objects WorkType

**Field Name** **Details**

```
LastViewedDate

MinimumCrewSize

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work type was last viewed by the current user.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the work. Work orders
and work order line items inherit their work type’s minimum crew size.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits the minimum crew size requirement.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work type. Try to use a name that helps users quickly understand
the type of work orders that can be created from the work type. For example,
“Annual Refrigerator Maintenance” or “Valve Replacement.”

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The work type’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects WorkType

**Field Name** **Details**

```
RecommendedCrewSize

SaDocumentTemplate

ServiceReportTemplateId

ShouldAutoCreateSvcAppt

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the work.
For example, you might have a Minimum Crew Size of 2 and a Recommended
Crew Size of 3. Work orders and work order line items inherit their work type’s
recommended crew size.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a service appointment.
The ID is 15 to 18 characters long.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template associated with the work type. When users create
service reports from a work order or work order line item that uses this work type,
the reports use this template.

**Type**
boolean

**Properties**
Create, Filter, Group, Defaulted on create, Sort, Update

**Description**
Select this option to have a service appointment automatically created on work
orders and work order line items that use the work type.

Note:

**•** By default, the Due Date on auto-created service appointments is
seven days after the created date. Admins can adjust this offset from
the Field Service Settings page in Setup.

**•** If a work type with the Auto-Create Service Appointment option
selected is added to an existing work order or work order line item, a


Standard Objects WorkType

**Field Name** **Details**

service appointment is only created for the work order or work order
line item if it doesn’t yet have one.

**•** If someone updates an existing work type by selecting the Auto-Create
Service Appointment option, service appointments aren’t created on
work orders and work order line items that were already using the
work type.

```
WoDocumentTemplate

WoliDocumentTemplate

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a work order. The ID is
15 to 18 characters long.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The document template ID. If `ServiceDocumentTemplateId` isn’t
specified, this document template ID determines which service document
template is used for service documents generated from a work order line item.
The ID is 15 to 18 characters long.

Adding a work type to a work order or work order line item causes the record to inherit the work type’s duration values and required
skills and products.

Note:

**•** If needed, you can update the duration values and required skills and products on a work order or work order line item after
they’re inherited from the work type.

**•** If a work order or work order line item already has required skills or products, associating it with a work type doesn’t cause it
to inherit the work type’s requirements.

**•** If a work order or work order line item already has a duration value in its `Duration` field, associating it with a work type
doesn’t cause it to inherit the work type’s duration value.

**•** Customizations to required skills or products, such as validation rules or Apex triggers, are not carried over from work types to
work orders and work order line items.


### Standard Objects WorkTypeGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkTypeChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkTypeFeed**

Feed tracking is available for the object.

**WorkTypeHistory**

History is available for tracked fields of the object.

**WorkTypeOwnerSharingRule**

Sharing rules are available for the object.

**WorkTypeShare**

Sharing is available for the object.

### WorkTypeGroup

Represents a grouping of work types used to categorize types of appointments available in Lightning Scheduler, or to define scheduling
limits in Field Service. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdditionalInformation

Description

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Additional information about the types of appointments this work type group represents.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this work type group.


Standard Objects WorkTypeGroup

**Field** **Details**

```
GroupType

IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The category of this work type group. Possible values are:

**•** `Capacity` —A group of work types used to define a work capacity limit in Field Service.

**•** `Default` —A non-capacity group of work types used in Lightning Scheduler.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this work type group can be used for appointment scheduling or work
capacity limits. A work type can belong to only one active work type group of type Capacity.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this work type group.

**Type**
reference


### Standard Objects WorkTypeGroupMember

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupFeed**

Feed tracking is available for the object.

**WorkTypeGroupHistory**

History is available for tracked fields of the object.

**WorkTypeGroupOwnerSharingRule**

Sharing rules are available for the object.

**WorkTypeGroupShare**

Sharing is available for the object.

### WorkTypeGroupMember

Represents the relationship between a work type and the work type group it belongs to. This object is available in API version 45.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

```

**Type**
dateTime


Standard Objects WorkTypeGroupMember

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

```
LastViewedDate

Name

WorkTypeGroupId

WorkTypeId

```

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
Autogenerated number identifying the work type group membership. It uses the format
########.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type group that this record belongs to.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that this record corresponds to.

This is a relationship field.


Standard Objects WorkTypeGroupMember

**Field** **Details**

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupMemberFeed**

Feed tracking is available for the object.

**WorkTypeGroupMemberHistory**

History is available for tracked fields of the object.


## CHAPTER 7 Data Model

Entity relationship diagrams (ERDs) for standard Salesforce objects illustrate important relationships between objects. Salesforce ERDs
use crow’s foot notation.

[[other]: ERDs are hosted in the Data Model Gallery. The Salesforce Data Model Gallery is a curated collection of diagrams that](https://developer.salesforce.com/docs/platform/data-models/guide)
illustrate the underlying data models for Salesforce products, features, and clouds. It’s a resource designed to support customers,
developers, solution engineers, and data architects in understanding how data is structured across Salesforce — enabling better
solution design, integration planning, and implementation strategy.

The data model for your custom objects depends on what you create.


INDEX

A

AccountInsight object 289
AccountUserTerritory2View object 343
AnalyticsLicensedAsset object 546

B

Big Objects
Composite primary key 32
Custom Big Object 32
Defining 32
Deploying 32
# Index 32

Overview 31

C

ContactSuggestionInsight object 1457

D

Data access
standard objects 27
Delegated Account Objects 1852

E

Electronic_Media_Group_object 1915
Electronic_Media_Use_object 1917
External Account Hierarchy History Object 2497
External_Account_Hierarchy_object 2494
ExternalSocialAccount object 2514

F

FormulaFunction object 2810
FormulaFunctionCategory object 2813
Freeze users 5631

H

HealthCareDiagnosis object 2902
HealthCareProcedure object 2907

# I

IframeWhiteListUrl object 2933

L

LandingPage object 3061

M

Managed_Content 3375
Managed_Content_Channel 3377
Managed_Content_Channelobject 3377
Managed_Content_Info_object 3380
Managed_Content_object 3375
Managed_Content_Variant 3382
Managed_Content_Variant_object 3382
MarketingForm object 3385
MarketingLink object 3389

O

Object_name object 4803
ObjectPermissions object 3592
Objects
AccountInsight 289
AccountUserTerritory2View 343
AnalyticsLicensedAsset 546
ContactSuggestionInsight 1457
Electronic_Media_Group 1915
Electronic_Media_Use 1917
External_Account_Hierarchy 2494
ExternalSocialAccount 2514
FormulaFunction 2810
FormulaFunctionCategory 2813
HealthCareDiagnosis 2902
HealthCareProcedure 2907
IframeWhiteListUrl 2933
LandingPage 3061
LightningExperienceTheme 3158
Managed_Content_Info 3380
MarketingForm 3385
MarketingLink 3389
Object_name 4803
ObjectPermissions 3592
OmniSupervisorConfig 3605
OmniSupervisorConfigAction 3607
OmniSupervisorConfigGroup 3608
OmniSupervisorConfigProfile 3609
OmniSupervisorConfigUser 3614
OpportunityContactRoleSuggestionInsight 3651
OpportunityInsight 3658
PermissionSet 4139
PermissionSetGroup 4126, 4129
Product_Attribute 4326


**Index**

Objects _(continued)_
Product_Attribute_Set 4327
Product_Attribute_Set_Item 4329
Product_Attribute_Set_Product 4330
Product_Category 4334, 4337
Product_Media 4359
Prompt 4472, 4485
PromptAction 4463, 4467
PromptActionOwnerSharingRule 4469
PromptActionShare 4470, 4474
Recommendation 4616
Sales_Store_Catalog 4782
SocialPersona 5088
SocialPost 5094
SurveyQuestionScore 5160
UiFormulaCriterion 5456
UiFormulaRule 5457
VoiceCallQualityFeedback 5791
WebStore 5856, 5880
WebStoreCatalog 5868
OmniSupervisorConfig object 3605
OmniSupervisorConfigAction object 3607
OmniSupervisorConfigGroup object 3608
OmniSupervisorConfigProfile object 3609
OmniSupervisorConfigUser object 3614
OpportunityContactRoleSuggestionInsight object 3651
OpportunityInsight object 3658

P

PermissionSetGroup object 4126

PermissionSetGroupComponent object 4129
PermissionSetTabSetting object 4139
Product_Attribute_object 4326
Product_Attribute_Set_Item_object 4329
Product_Attribute_Set_object 4327
Product_Attribute_Set_Product_object 4330
Product_Category_object 4334, 4337
Product_Media_object 4359

R

Recommendation object 4616

S

Sales_Store_Catalog_object 4782
SocialPersona object 5088
SocialPost object 5094
Standard objects
data access 27
SurveyQuestionScore object 5160

U

UiFormulaCriterion object 5456
UiFormulaRule object 5457

V

VoiceCallQualityFeedback object 5791

W

WebStore object 5856, 5880
WebStoreCatalog_object 5868

