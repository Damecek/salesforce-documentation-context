the owner's or subordinates’ and child territories’ forecasts. It doesn’t include


Standard Objects ForecastingItem

**Field Name** **Details**

adjustments made by forecast managers above the owner in the forecast
hierarchy.

```
AmountWithoutOwnerAdjustment

ForecastAmount

ForecastCategoryName

ForecastQuantity

```

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The forecast amount as seen by the forecast owner without the owner's
adjustment. This amount is the sum of the subordinate's and child territories’
opportunities, including adjustments made by their manager or by the
subordinate themselves, plus the rollup of the owner's own opportunities. _It_
_doesn’t include adjustments made by the forecast owner._

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The revenue forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ and child territories’ opportunities, including all
forecast adjustments.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A forecast category is the category within the sales cycle to which an opportunity
is assigned based on its opportunity stage. The standard forecast categories are
Pipeline, Best Case, Commit, Omitted (not included in forecasts), and Closed.
Salesforce admins can add a Most Likely category and can customize the forecast
category names in single category rollups. Change the forecast category name
only. Changing a forecast category’s API name can have unintended results.

**Type**
double

**Properties**
Filter, Sort, Nillable


Standard Objects ForecastingItem

**Field Name** **Details**

**Description**

The quantity forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ opportunities, including all forecast adjustments.
This field is available in API version 28 and later.

```
ForecastingGroupItemId

ForecastingItemCategory

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the forecast total belongs to. This field is a relationship field. Available in API
version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
This field indicates which type of forecast rollup the forecasting item belongs to.
Depending on whether your organization uses individual forecast category rollups
or cumulative forecast rollups, you have these possible values for the
`ForecastingItemCategory` field.

_**Individual forecast category rollups:**_

**•** PipelineOnly - Rollup from Pipeline opportunities only.

**•** BestCaseOnly - Rollup from Best Case opportunities only. Adjustable.

**•** MostLikelyOnly - Rollup from Most Likely opportunities only. Adjustable.

**•** CommitOnly - Rollup from Commit opportunities only. Adjustable.

_**Cumulative forecast rollups:**_

**•** OpenPipeline - Rollup from Pipeline + Best Case + Most Likely + Commit
opportunities.

**•** BestCaseForecast - Rollup from Best Case + Most Likely + Commit +
Closed opportunities. Adjustable.

**•** MostLikelyForecast - Rollup from Most Likely + Commit + Closed
opportunities. Adjustable.


Standard Objects ForecastingItem

**Field Name** **Details**

**•** CommitForecast - Rollup from Commit + Closed opportunities.
Adjustable.

_**Either cumulative or individual forecast category rollups:**_

**•** ClosedOnly - Rollup from Closed opportunities only.

The `ForecastingItemCategory` field differs from the
`ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category
of the _underlying opportunities_ rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the `ForecastCategoryName` field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of_
_rollup_ a forecast amount or adjustment is from. In organizations using
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

```
ForecastingTypeId

HasAdjustment

HasOwnerAdjustment

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes a _manager_ adjustment. This
flag is true only when the item includes an adjustment and the user performing
the query has read access to the adjustment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes an _owner_ adjustment. This flag
is true only when the item includes an adjustment and the user performing the
query has read access to the adjustment. Available in API version 33.0 and later.


Standard Objects ForecastingItem

**Field Name** **Details**

```
IsAmount

IsQuantity

IsUpToDate

OwnerId

OwnerOnlyAmount

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a revenue amount. If false, then
`IsQuantity` must be true. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a quantity amount. If false, then
`IsAmount` must be true. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag indicating whether a specific forecasting item reflects current information.
For example, if users are making adjustments that are in process, the item isn’t
up to date.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the forecast owner.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s revenue opportunities, without adjustments.


Standard Objects ForecastingItem

**Field Name** **Details**

```
OwnerOnlyQuantity

ParentForecastingItemId

PeriodId

ProductFamily

QuantityWithoutAdjustments

```

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s quantity opportunities, without adjustments. This field is
available in API version 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ForecastingItem that the current item rolls up to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the forecast.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product family of the forecast item. This field is available in API version 29.0
and later. Read only.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The sum of a person’s owned quantity opportunities and also his or her
subordinates’ opportunities, without adjustments. Subordinates include everyone
reporting up to a person in the forecast hierarchy. This field is available in API
version 28.0 and later.


Standard Objects ForecastingItem

**Field Name** **Details**

```
QuantityWithoutManagerAdjustment

QuantityWithoutOwnerAdjustment

SubordinateOverrides

Territory2Id

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast number as seen by the forecast owner. This number is the sum of
the owner’s quantity opportunities and subordinates’ opportunities, including
adjustments made on the subordinates’ forecasts. It doesn’t include adjustments
made by forecast managers above the owner in the forecast hierarchy. This field
is available in API version 28 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast quantity as seen by the forecast owner without the owner's
adjustment. This number is the sum of the subordinate's opportunities, including
adjustments made by their manager or by the subordinate themselves, plus the
rollup of the owner's own opportunities. _It doesn’t include adjustments made by_
_the forecast owner._ This field is available in API version 38.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of adjustments made to a forecast down the hierarchical chain.
For example, User A has a forecast without adjustments. If User A adjusts User
B’s forecast, User A’s `SubordinateOverrides` value is 1. Then if User B
adjusts User C’s forecast, User A’s `SubordinateOverrides` value is 2. If
User A removes his adjustment from User B’s forecast, User A’s
`SubordinateOverrides` value is 1.

This field is available in API version 38.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.


### Standard Objects ForecastingOwnerAdjustment

Usage

Use this object to obtain individual forecast amounts, either with or without adjustments, based on a user’s perspective and forecast
role. The ForecastingItem object is visible to all users, but only forecast managers and users above them in the forecast hierarchy can
read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
### ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingQuota

### ForecastingOwnerAdjustment

This object represents an individual forecast user’s adjustment of their _own_ forecast, including territory forecasts they own, via a
ForecastingItem. Available in API versions 33.0 and later. This object is different from the ForecastingAdjustment object, which represents
managers’ adjustments of _subordinates’_ and child territories’ forecasts.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the importing
user’s personal currency.


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

```
ForecastCategoryName

ForecastOwnerId

ForecastingGroupItemId

ForecastingItemCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category within the sales cycle that an opportunity is assigned to based on
its opportunity stage. The standard forecast categories are Pipeline, Best Case,
Commit, Omitted, and Closed. You can add a Most Likely category and can
customize forecast category names in single category rollups. The forecast
categories display information for that specific category; for example, Best Case
only reflects amounts in the Best Case category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the forecast owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the owner adjustment belongs to. This field is a relationship field. Available in
API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
This field indicates which type of forecast rollup the owner adjustment belongs
to. Depending on whether your organization uses individual forecast category


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

rollups or cumulative forecast rollups, you have these possible values for the
`ForecastingItemCategory` field.

_**Individual forecast category rollups:**_

**•** PipelineOnly - Rollup from Pipeline opportunities only.

**•** BestCaseOnly - Rollup from Best Case opportunities only. Adjustable.

**•** MostLikelyOnly - Rollup from Most Likely opportunities only. Adjustable.

**•** CommitOnly - Rollup from Commit opportunities only. Adjustable.

_**Cumulative forecast rollups:**_

**•** OpenPipeline - Rollup from Pipeline + Best Case + Most Likely + Commit
opportunities.

**•** BestCaseForecast - Rollup from Best Case + Most Likely + Commit +
Closed opportunities. Adjustable.

**•** MostLikelyForecast - Rollup from Most Likely + Commit + Closed
opportunities. Adjustable.

**•** CommitForecast - Rollup from Commit + Closed opportunities.
Adjustable.

_**Either cumulative or individual forecast category rollups:**_

**•** ClosedOnly - Rollup from Closed opportunities only.

The `ForecastingItemCategory` field differs from the
`ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category
of the _underlying opportunities_ rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the `ForecastCategoryName` field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of_
_rollup_ a forecast amount or adjustment is from. In organizations using
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

When inserting owner adjustments, the values you insert for
`ForecastCategoryName` and `ForecastingItemCategory` must
be compatible with each other. In organizations using cumulative forecast rollups,
the `ForecastCategoryName` is nillable. These pairs are the valid pairs.

**Individual forecast category rollups:**

**•** `ForecastCategoryName` : BestCase,
`ForecastingItemCategory` : BestCaseOnly

**•** `ForecastCategoryName` : Commit,
`ForecastingItemCategory` : CommitOnly


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**Cumulative forecast category rollups:**

**•** `ForecastCategoryName` : null, `ForecastingItemCategory` :
BestCaseForecast

**•** `ForecastCategoryName` : null, `ForecastingItemCategory` :
CommitForecast

```
ForecastingItemId

ForecastingTypeId

IsAmount

IsQuantity

OwnerAdjustedAmount

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**Description**

The revenue amount of an individual forecast item, after an adjustment.

```
OwnerAdjustedQuantity

OwnerAdjustmentNote

PeriodId

ProductFamily

StartDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field does not appear in reports.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the adjustment. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.


### Standard Objects ForecastingQuota

**Field Name** **Details**

```
Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to obtain a user’s adjustment details for a specified ForecastingItem in their own forecast.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
### ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
### object to determine the ID for each forecast type and then filter ForecastingQuota, ForecastingAdjustment,

`ForecastingItem`, or `ForecastingFact` records as necessary.

**ForecastingOwnerAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.

### ForecastingQuota

This object represents an individual user’s or territory’s quota for a specified time period. The Managed Quotas user permission is required
for creating, updating, or deleting quotas. (Users can only edit their subordinates’ or child territories’ quotas, not their own.) The View
All Forecasts permission is required to view any user's forecast, regardless of the forecast hierarchy. Available in API versions 25.0 and
later. Forecast managers can view the forecasts of subordinates and territories below them in the forecast hierarchy.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

```

**Type**
picklist


Standard Objects ForecastingQuota

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the quota. If omitted, the default is the importing user’s
personal currency.

```
ForecastingGroupItemId

ForecastingTypeId

IsAmount

IsQuantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the quota belongs to. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` . This field is available in API version 28.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ForecastingQuota

**Field Name** **Details**

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` . This field is available in API version 28.0 and later.

```
PeriodId

ProductFamily

QuotaAmount

QuotaOwnerId

QuotaQuantity

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the quota. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product family for the quota. This field is available in API version 29.0 and
later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue quota amount for an individual user or territory and for a specific
period.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

ID that identifies the quota owner.

**Type**
double

**Properties**
Create, Filter, Sort, Update


### Standard Objects ForecastingShare

**Field Name** **Details**

**Description**

The quantity quota amount for an individual user and for a specific period. This
field is available in API version 28.0 and later.

```
StartDate

Territory2Id

```

Usage

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The start of the quota, expressed as month and year. The date can include any
day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to get an individual user’s or territory’s quota for a specified time period.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingItem

### ForecastingShare

Represents forecasts shared between a forecast manager and a user. Available in API version 44.0 and later.


Standard Objects ForecastingShare

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
AccessLevel

SharedForecastManagerRoleId

RoleType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

Whether the user you’re sharing your forecasts with can view and adjust the
forecasts or view only. This field is new since the pilot.

Picklist values:

**•** `ViewAndEdit`

**•** `ViewOnly`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of either:

**•** The role of the manager whose forecasts you want to share.

**•** The territory whose forecasts you want to share.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of hierarchy associated with the forecast share.

**•** `R`  - Role-based

**•** `T`  - Territory-based

**•** `Y`  - Territory2-based


### Standard Objects ForecastingSourceDefinition

**Field Name** **Details**

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the user with whom the forecast is shared.

Use this object to let any stakeholder at your company view and adjust forecast managers’ forecasts.

### ForecastingSourceDefinition

Represents the object, measure, date type, and hierarchy that a forecast uses to project sales. This object is available in API version 52.0
and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CategoryField

DateField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Name of the forecast category that is associated with the forecast type.

Possible values are:

**•** `Opportunity.ForecastCategoryName`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ForecastingSourceDefinition

**Field** **Details**

**Description**
Field that is used for the forecast type’s date type. For example, the CloseDate field on
Opportunity is used for opportunity close date-based forecast types.

Possible values are:

**•** `Opportunity.CloseDate`

**•** `OpportunityLineItem.ServiceDate`

**•** `OpportunityLineItemSchedule.ScheduleDate`

```
DeveloperName

FamilyField

Language

MasterLabel

MeasureField

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting source definition.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Use this field to group forecasts by product family. Possible values are:

**•** `Product2.Family`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting source definition. For example, English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting source definition.

**Type**
picklist


Standard Objects ForecastingSourceDefinition

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Field that is used for the forecast type’s measure. For example, the Amount field on
Opportunity is associated with revenue-based forecast types.

Possible values are*:

**•** `Opportunity.Amount`

**•** `Opportunity.` _**`Custom`**_

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.` _**`Custom`**_

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItemSchedule.` _**`Custom`**_

**•** `OpportunityLineItemSchedule.Quantity`

**•** `OpportunityLineItemSchedule.Revenue`

**•** `OpportunitySplit.` _**`Custom`**_

**•** `OpportunitySplit.SplitAmount`

*Where _**`Custom`**_ represents the name of the custom field that a forecast type’s measure is
based on. Example: Use `Megawatts__c` to forecast energy consumption.

```
SourceObject

Territory2Field

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object associated with this forecasting source definition.

Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `OpportunityLineItemSchedule`

**•** `OpportunitySplit`

**•** `Product2`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For a territory-based forecast type, indicates the field that is used for territory information.


Standard Objects ForecastingSourceDefinition

**Field** **Details**

Possible values are:

**•** `Opportunity.Territory2Id`

For user role-based forecast types, this value is `null` .

```
UserField

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies who owns the forecast.

Possible values are:

**•** `Opportunity.OwnerId`

**•** `OpportunitySplit.SplitOwnerId`

Use ForecastingSourceDefinition to define a forecast type’s structure. A forecasting source definition is joined via
`ForecastingTypeSource` to `ForecastingType` .

In this example, a user role-based forecast type called Custom Amount Forecast is based on the Amount and Close Date fields on
opportunities.

```
ForecastingType type = new sforce.SObject("ForecastingType");

type.DeveloperName = "Custom_Amount_Forecast";

type.MasterLabel = "Custom Amount Forecast";

type.IsAmount = true;

type.IsQuantity = false;

type.RoleType = "R";

type.DateType = "OpportunityCloseDate";

String typeId = insert(type);

ForecastingSourceDefinition sourceDefinition = new

sforce.SObject("ForecastingSourceDefinition")

sourceDefinition.DeveloperName = "Custom Amount Source";

sourceDefinition.MasterLabel = "Custom_Amount_Source";

sourceDefinition.SourceObject = "Opportunity";

sourceDefinition.MeasureField = "Opportunity.Amount";

sourceDefinition.DateField = "Opportunity.CloseDate";

sourceDefinition.UserField = "Opportunity.OwnerId";

sourceDefinition.CategoryField = "Opportunity.ForecastCategoryName";

String sourceDefinitionId = insert(sourceDefinition);

ForecastingTypeSource typeSource = new sforce.SObject("ForecastingTypeSource");

typeSource.MasterLabel = "Custom Amount Type Source";

typeSource.DeveloperName = "Custom_Amount_Type_Source";

typeSource.ForecastingTypeId = typeId;

typeSource.ForecastingSourceDefinitionId = sourceDefinitionId;

```


### Standard Objects ForecastingSrcRecJudgment

```
   typeSource.SourceGroup = 1;

   insert(typeSource);

### ForecastingSrcRecJudgment

```

Represents forecast managers’ judgment of whether they consider an opportunity-related deal to be certain to close. This object is
available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
CurrencyIsoCode

JudgmentOwnerId

JudgmentValue

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the judgment. If omitted, the default is USD.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast manager.

This field is a relationship field.

**Relationship Name**
JudgmentOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ForecastingSubmission

**Field** **Details**

**Description**
Whether the deal is likely to close ( `IN` ) or not ( `OUT` ).

```
ReferenceObjectId

Territory2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the opportunity-related object.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory that the judgment is on.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Territory2

### ForecastingSubmission

Represents a submitted forecast. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ForecastingSubmission

Special Access Rules

Available for forecast types that aren’t grouped by product family forecast.

Fields

**Field** **Details**

```
CurrencyIsoCode

ForecastOwnerId

ForecastingGroupItemId

ForecastingTypeId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast owner.

This field is a relationship field.

**Relationship Name**
ForecastOwner

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use. Forecast submissions aren't supported in forecast types with groups.

**Relationship Name**
ForecastingGroupItem

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects ForecastingSubmission

**Field** **Details**

**Description**
The ID of the forecast type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

```
IsLatest

Name

Note

PeriodId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the forecast submission is the most recent submission.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. ID of this record.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The note attached to the submitted forecast.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the period to which the submission applies.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period


Standard Objects ForecastingSubmission

**Field** **Details**

```
PeriodStartDate

ProductFamily

SubmissionDateTime

Territory2Id

```

Usage

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Indicates the start date of the forecast period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Must be set to `none` . Forecast submissions aren't supported in forecast types grouped by
product families.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the forecast submission was made. Calculated internally.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

ForecastingSubmission is a detail object that contains the submitted item category values. Each record represents the values for a single
item category. ForecastingSubmission is always used as a detail object for the submission, and inserted only as part of a transaction that
includes all detail objects.


### Standard Objects ForecastingSubmissionItem ForecastingSubmissionItem

Represents the values for each forecast category in a submitted forecast. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

ForecastingItemCategory

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Amount as the measure, the amount for the forecast category.
Amounts must be provided in the corporate currency.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly` —Rollup from Pipeline opportunities only.

**•** `BestCaseOnly` —Rollup from Best Case opportunities only.

**•** `MostLikelyOnly` —Rollup from Most Likely opportunities only.

**•** `CommitOnly` —Rollup from Commit opportunities only.

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline` —Rollup from Pipeline, Best Case, Most Likely, and Commit
opportunities.


Standard Objects ForecastingSubmissionItem

**Field** **Details**

**•** `BestCaseForecast` —Rollup from Best Case, Most Likely, Commit, and Closed
opportunities.

**•** `MostLikelyForecast` —Rollup from Most Likely, Commit, and Closed
opportunities.

**•** `CommitForecast` —Rollup from Commit and Closed opportunities.

**For either cumulative or individual forecast category rollups, the possible values**
**are:**

**•** `ClosedOnly` —Rollup from Closed opportunities only.

```
ForecastingSubmissionId

Name

Quantity

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast submission.

This field is a relationship field.

**Relationship Name**
ForecastingSubmission

**Relationship Type**
Master-detail

**Refers To**
ForecastingSubmission (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. The ID of this record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Quantity as the measure, the quantity for the forecast category.
Quantities must be provided in the corporate currency.


### Standard Objects ForecastingType ForecastingType

Used to identify the forecast type associated with `ForecastingAdjustment`, `ForecastingOwnerAdjustment`,
`ForecastingQuota`, `ForecastingFact`, and `ForecastingItem` objects. Available in API version 30.0 and greater.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()` . `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CanDisplayQuotas

DateType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a forecast type can show quota information. The default value
is `false` . Available in API version 38.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The date type that forecast amounts are based on. These values are available for
forecast types that were available before Summer ’21.

**•** `OpportunityCloseDate` : Base forecasts on opportunity close dates.

**•** `ProductDate` : Base forecasts on opportunity product line item dates, if
available.

**•** `ScheduleDate` : Base forecasts on opportunity product schedule dates,
if available.

These values are available in API version 52.0 and later in Performance Edition
and in Unlimited Edition with the Sales Cloud.


Standard Objects ForecastingType

**Field Name** **Details**

**•** `OLIMeasureCloseDateOnly` : Base forecasts on opportunity close
dates.

**•** `ProductDateOnly` : Base forecasts on opportunity product line item
dates, if available.

**•** `ScheduleDateOnly` : Base forecasts on opportunity product schedule
dates, if available.

These values to create forecasts on custom date fields are available in API version
57.0 and later in Performance, Professional, Enterprise, and Unlimited Edition
with the Sales Cloud.

**•** `OLIMeasureOppCustomDateOnly` : Base forecasts on custom
opportunity dates, if available.

**•** `OpportunityCustomDate` : Base forecasts on custom opportunity
dates.

The custom date field used must be on the opportunity object and based on the
date type.

```
DeveloperName

ForecastingGroupID

HasAdjustments

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the forecasting type. The `DeveloperName` is called `name` in
the Metadata API and Forecasting Type in custom reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a group assignment, and if so, the
name of the group. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroup

**Relationship Type**
Lookup

**Refers To**
ForecastingGroup

**Type**
boolean


Standard Objects ForecastingType

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecast managers can adjust forecasts of their immediate
subordinates and child territories. The default value is `false` . Available in API
version 60.0 and later.

```
HasOwnerAdjustments

HasProductFamily

IsActive

IsAmount

IsPlatformType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether all forecast users can adjust their own forecasts, including the
territory forecasts that they own. The default value is `false` . Available in API
version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
Indicates whether a forecasts view includes product families. The default value
is `false` . Available in API version 40.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecasting type is enabled. The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the revenue measure. The
default value is `false` .

**Type**
boolean


Standard Objects ForecastingType

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a legacy forecast type that wasn’t available before Summer ’21. The
default value is `false` . Available in API version 52.0 and later.

```
IsQuantity

Language

LastActivatedDate

MasterLabel

OpportunitySplitTypeId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the quantity measure. The
default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the forecasting type.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date when a forecast type was activated. Read only. Available in API version
53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Controlling label for this forecasting type value. This display value is the internal
label that doesn’t get translated.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects ForecastingType

**Field Name** **Details**

**Description**
Indicates whether the forecasting type has a split type, and if so, the name of the
split type. This field is a relationship field. Available in API version 41.0 and later.

**Relationship Name**
OpportunitySplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

```
OpptyLineItemSplitTypeId

RoleType

Territory2ModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a product split type, and if so, the
name of the product split type. This field is a relationship field. Available in API
version 58.0 and later.

**Relationship Name**
OpptyLineItemSplitType

**Relationship Type**
Lookup

**Refers To**
OpptyLineItemSplitType

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the role type has a forecasting type, and if so, which forecasting
type. Available in API version 41.0 and later.

Possible values are:

**•** `R` —User role-based forecasting type

**•** `T` —Territory1-based forecasting type; not used

**•** `Y` —Territory2-based forecasting type

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects ForecastingTypeSource

**Field Name** **Details**

**Description**
Indicates whether the forecasting type has a Territory2 model, and if so, the name
of the Territory2 model. Available in API version 41.0 and later.

### ForecastingTypeSource

Maps a forecasting source definition to a forecast type. This object is available in API version 52.0 and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

ForecastingSourceDefinitionId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting type source.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecasting source definition. This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition

**Relationship Type**
Lookup


Standard Objects ForecastingTypeSource

**Field** **Details**

**Refers To**
ForecastingSourceDefinition

```
ForecastingTypeId

Language

MasterLabel

ParentSourceDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecast type. Can be linked only to forecast types created in Summer ’21 and later.
This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting type source.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting type source.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For forecast types not based on the opportunity object and not based on a custom measure,
this value represents the parent ForecastingSourceDefinition of the linked
ForecastingSourceDefinition. This field is a relationship field.

**•** Opportunity Product is the parent of Opportunity.

**•** Opportunity Split is the parent of Opportunity.


### Standard Objects ForecastingUserPreference

**Field** **Details**

**•** Line Item Schedule is the parent of Opportunity Product.

**Relationship Name**
ParentSourceDefinition

**Relationship Type**
Lookup

**Refers To**
ForecastingSourceDefinition

```
RelationField

SourceGroup

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the field linking the source objects of the parent ForecastingSourceDefinition to
the child ForecastingSourceDefinition.

Possible values are:

**•** `OpportunityLineItem.OpportunityId`

**•** `OpportunityLineItem.Product2Id`

**•** `OpportunityLineItemSchedule.OpportunityLineItemId`

**•** `OpportunitySplit.OpportunityId`

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Represents a grouping of forecasting source definitions.

Use this object to define a forecast type’s structure. This junction object links `ForecastingSourceDefinition` to
`ForecastingType` .

For an example, see ForecastingSourceDefinition.

### ForecastingUserPreference

Represents the forecasting selections that a user has made, such as display options, date range, forecasting type, and currency.


Standard Objects ForecastingUserPreference

Supported Calls

`create()`, `describeSObjects()`, `query()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
ExternalId

ForecastingDisplayedTypeId

ForecastingPeriodDuration

ForecastingPeriodType

ForecastingStartPeriod

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A unique system-generated numerical identifier for the user.

**Type**
reference

**Properties**
Create, Group, Sort, Update

**Description**

An identifier for the forecasting type that’s displayed.

**Type**
int

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

How long the forecasting period lasts.

**Type**
picklist

**Properties**
Create, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The forecasting period’s type. Valid values include: Month, Quarter, Week, or Year

**Type**
int


Standard Objects ForecastingUserPreference

**Field Name** **Details**

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The date when the forecasting period begins.

```
ForecastingViewCurrency

IsForecastingHideZeroRows

IsForecastingShowQuantity

IsHideForecastingGuidedTour

IsHideForecastingQuotaColumn

```

**Type**
string

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The currency shown on the forecasts page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows zero-value rows.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows forecast quantity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows the guided tour.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows a quota column.


### Standard Objects FormulaFunction

**Field Name** **Details**

```
IsShowForecastingChangeSignals

IsShowForecastingQuotaAttainment

### FormulaFunction

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows changes in the last 7 days.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows quota attainment information.

Represents a function used when building a formula, including examples and uses. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
CategoryId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FormulaFunctionCategory.

This is a relationship field.

**Relationship Name**
Category

**Relationship Type**
Lookup

**Refers To**
### FormulaFunctionCategory


Standard Objects FormulaFunction

**Field** **Details**

```
Description

DurableId

ExampleString

IsAllowedInEntityContext

IsAllowedInFlowContext

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the formula function.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the function and what arguments you can use with it.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether you can use the formula function on an Entity ( `true` ) or not ( `false` ).
For example, you cannot use the PRIORVALUE function in a custom Account formula field.
The default value is `false` . This field is removed in API version 48.0 and later. Use the
FormulaFunctionAllowedType on page 2812 object instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in a Flow ( `true` ) or not ( `false` ). The
default value is `false` . This field is removed in API version 48.0 and later. Use the
FormulaFunctionAllowedType on page 2812 object instead.


### Standard Objects FormulaFunctionAllowedType

**Field** **Details**

```
IsAllowedInVisualforceContext

Label

Name

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in Visualforce ( `true` ) or not ( `false` ).
The default value is `false` . This field is removed in API version 48.0 and later. Use the
### FormulaFunctionAllowedType on page 2812 object instead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The formula function label that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the formula function.

Query FormulaFunction to search for available formula functions, such as `AND()`, `ISBLANK()`, `MAX()`, `MIN()`, and others.

### FormulaFunctionAllowedType

Represents the functions that are supported in the given formula context. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DurableId

```

**Type**
string


### Standard Objects FormulaFunctionCategory

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

```
FunctionId

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the supported function.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
### FormulaFunction

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the formula type in which the function is supported.

Possible values are:

**•** `FLOW`

**•** `VALIDATION`

**•** `VISUALFORCE`

### FormulaFunctionCategory

Represents the category to which a formula belongs when building a formula. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`


### Standard Objects FrcstCustmCatgRampRateSrc

Fields

**Field** **Details**

```
 DurableId

 Label

 Name

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label of the FormulaFunctionCategory that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the FormulaFunctionCategory.

Query FormulaFunctionCategory to search for categories of available formula functions, such as `Math`, `Logical`, `Date and Time`,
and others.

### FrcstCustmCatgRampRateSrc

Represents the total contract value used for custom bulk adjustments. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects FrcstCustmCatgRampRateSrc

Fields

**Field** **Details**

```
BaseValueFrcstSrcDefinitionId

DeveloperName

ForecastingCustomCategoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The DMO that contains the field in which the total contract value exists. This field is a
relationship field.

**Relationship Name**
BaseValueFrcstSrcDefinition

**Refers To**
ForecastingSourceDefinition

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

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory


### Standard Objects FrcstCustmzAdjustment

**Field** **Details**

**Refers To**
ForecastingCustomCategory

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the
FrcstCustmCatgRampRateSrc.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this FrcstCustmCatgRampRateSrc value. This display value is the internal label that
doesn't get translated.

### FrcstCustmzAdjustment

Represents an individual forecast manager’s adjustment of a subordinate’s consumption forecast. Available in API version 63.0 and later.
This object is different from the ForecastingAdjustment object, which represents managers’ adjustments of subordinates’ pipeline
forecasts.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdjustedAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue amount of an individual forecast item, after an adjustment.


Standard Objects FrcstCustmzAdjustment

**Field** **Details**

```
AdjustedQuantity

AdjustmentNote

ForecastingCustomCategoryId

ForecastingTypeId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text note providing information about the adjustment. The maximum length is 255
characters.

This field doesn’t appear in reports.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related forecasting type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType


Standard Objects FrcstCustmzAdjustment

**Field** **Details**

```
IsAmount

IsQuantity

OwnerId

PeriodId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, IsQuantity must be
set to `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the adjustment is made in a quantity amount. If `false`, IsAmount must be set to
`true` .

The default value is `false` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the forecast owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Period ID for the adjustment.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period


### Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

```
Territory2Id

```

Associated Objects

**Type**
reference

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FrcstCustmzAdjustmentChangeEvent on page 68**
Change events are available for the object.

**FrcstCustmzAdjustmentFeed on page 55**
Feed tracking is available for the object.

**FrcstCustmzAdjustmentHistory on page 63**
History is available for tracked fields of the object.

**FrcstCustmzAdjustmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FrcstCustmzAdjustmentShare on page 67**
Sharing is available for the object.

### FrcstCustmzOwnerAdjustment

Represents an individual forecast user’s adjustment of their own consumption forecast. Available in API version 63.0 and later. This object
is different from the ForecastingOwnerAdjustment object, which represents users’ adjustments of their pipeline forecasts.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdjustedAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

**Description**
The revenue amount of an individual forecast item, after an adjustment.

```
AdjustedQuantity

AdjustmentNote

CustomDimension

ForecastingCustomCategoryId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text note providing information about the adjustment. The maximum length is 255
characters.

This field doesn’t appear in reports.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the additional dimension of the forecasting adjustment. For example, account ID,
use case ID.

Any data imported from an external source must be exactly 15 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory


Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

```
ForecastingTypeId

IsAmount

IsQuantity

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related forecasting type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, IsQuantity must be
set to `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the adjustment is made in a quantity amount. If `false`, IsAmount must be set to
`true` .

The default value is `false` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the forecast owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


### Standard Objects FulfillmentOrder

**Field** **Details**

```
PeriodId

Territory2Id

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Period ID for the adjustment.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period

**Type**
reference

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FrcstCustmzOwnerAdjustmentChangeEvent on page 68**
Change events are available for the object.

**FrcstCustmzOwnerAdjustmentFeed on page 55**
Feed tracking is available for the object.

**FrcstCustmzOwnerAdjustmentHistory on page 63**
History is available for tracked fields of the object.

**FrcstCustmzOwnerAdjustmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FrcstCustmzOwnerAdjustmentShare on page 67**
Sharing is available for the object.

### FulfillmentOrder

Represents a group of products, fees, and delivery charges on a single order that share the same fulfillment location, delivery method,
and recipient. The FulfillmentOrderLineItems belonging to a FulfillmentOrder are associated with OrderItemSummary objects belonging
to a single OrderSummary. This object is available in API version 48.0 and later.


Standard Objects FulfillmentOrder

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
AccountId

ActiveDate

BillToContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Account or Person Account associated with the FulfillmentOrder. It represents the
shopper in the storefront.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
datetime

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the FulfillmentOrder becomes active.

This field is available in API version 61.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the FulfillmentOrder. It represents the shopper in the
storefront when not using person accounts.


Standard Objects FulfillmentOrder

**Field** **Details**

This field is available in API version 49.0 and later.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

```
ClosedDate

CurrencyIsoCode

DeliveryDate

```

**Type**
datetime

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the FulfillmentOrder closed. Automatically entered.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the OrderSummary associated with the FulfillmentOrder.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the FulfillmentOrder was delivered.

This field is a relationship field.


Standard Objects FulfillmentOrder

**Field** **Details**

```
DeliveryMethodId

FulfilledFromLocationId

FulfilledToAddress

FulfilledToCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the DeliveryMethod used for this FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location handling this FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
FulfilledFromLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
address

**Properties**
Filter, Nillable

**Description**
Address of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address city.


Standard Objects FulfillmentOrder

**Field** **Details**

```
FulfilledToCountry

FulfilledToEmailAddress

FulfilledTo

GeocodeAccuracy

FulfilledToLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address country.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the recipient.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy of the geocode for the recipient address.

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

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLongitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.


Standard Objects FulfillmentOrder

**Field** **Details**

```
FulfilledToLongitude

FulfilledToName

FulfilledToPhone

FulfilledToPostalCode

FulfilledToState

FulfilledToStreet

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLatitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name on the recipient address.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Recipient address street.

```
FulfillmentOrderNumber

GrandTotalAmount

InvoiceId

IsReship

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrder.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges on the
FulfillmentOrder. This amount includes all FulfillmentOrderLineItems associated with the
FulfillmentOrder. This amount is equal to TotalAmount + TotalTaxAmount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Invoice associated with the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the FulfillmentOrder is for a reshipment. The default value is false.

This field is available in API version 53.0 and later.


Standard Objects FulfillmentOrder

**Field** **Details**

```
IsSuspended

ItemCount

LastReferencedDate

LastViewedDate

OrderId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the FulfillmentOrder is suspended. The default value is false.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the quantities of the FulfillmentOrderLineItems included in the FulfillmentOrder.

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original Order that generated the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup


Standard Objects FulfillmentOrder

**Field** **Details**

**Refers To**
Order

```
OrderSummaryId

OwnerId

ProcessingTimeInMinutes

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderSummary associated with the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this FulfillmentOrder. Default value is the User logged in
to the API to perform the create.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
long

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
How many minutes it took to process the FulfillmentOrder, from the start of processing to
completion.


Standard Objects FulfillmentOrder

**Field** **Details**

```
StartFulfillmentDate

Status

StatusCategory

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the fulfillment process was started for the FulfillmentOrder.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Status of the FulfillmentOrder. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes,
but the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.

Default values are:

**•** `Allocated` (Activated)

**•** `Assigned` (Fulfilling)

**•** `Cancelled` (Cancelled)

**•** `Draft` (Draft)

**•** `Fulfilled` (Closed)

**•** `Pick Complete` (Fulfilling) This value is available in API v56.0 and later.

**•** `Pickpack` (Fulfilling)

**•** `Printed` (Fulfilling) This value is available in API v56.0 and later.

**•** `Rejected` (Rejected) This value is available in API v56.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `ACTIVATED` —Activated

**•** `CANCELLED` —Cancelled

**•** `CLOSED` —Closed

**•** `DRAFT` —Draft

**•** `FULFILLING` —Fulfilling


Standard Objects FulfillmentOrder

**Field** **Details**

**•** `REJECTED` —Rejected This value is available in API v56.0 and later.

```
TaxLocaleType

TotalAdjustmentAmount

TotalAdjustment

AmtWithTax

TotalAdjustmentTaxAmount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original Order associated with the FulfillmentOrder.
Gross usually applies to taxes like value-added tax (VAT), and Net usually applies to taxes like
sales tax.

Possible values are:

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the FulfillmentOrder. This
value only includes adjustments to FulfillmentOrderLineItems of type code Product, not
adjustments to delivery charges or fees.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the Fulfillment Order,
inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of type
code Product. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.


Standard Objects FulfillmentOrder

**Field** **Details**

```
TotalAmount

TotalDelivery

AdjustAmount

TotalDeliveryAdjust

AmtWithTax

TotalDelivery

AdjustTaxAmount

TotalDeliveryAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the FulfillmentOrderLineItems, including products, fees,
and delivery charges, on the Fulfillment Order.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the Fulfillment
Order. This value only includes adjustments to FulfillmentOrderLineItems of type Delivery
Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the Fulfillment
Order, inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of
type Delivery Charge. This amount is equal to TotalDeliveryAdjustAmount +
TotalDeliveryAdjustTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjustAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges on the FulfillmentOrder. This value only includes
FulfillmentOrderLineItems of type Delivery Charge.


Standard Objects FulfillmentOrder

**Field** **Details**

```
TotalDeliveryAmtWithTax

TotalDeliveryTaxAmount

TotalFeeAdjustAmount

TotalFeeAdjustAmtWithTax

TotalFeeAdjustTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the FulfillmentOrder, inclusive of tax. This value only
includes FulfillmentOrderLineItems of type Delivery Charge. This amount is equal to
TotalDeliveryAmount + TotalDeliveryTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the FulfillmentOrder. This value
only includes adjustments to FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the FulfillmentOrder, inclusive
of tax. This value only includes adjustments to FulfillmentOrderLineItems of type Fee. This
amount is equal to TotalFeeAdjustAmount + TotalFeeAdjustTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Tax on the TotalFeeAdjustAmount.

This field is available in API version 56.0 and later.

```
TotalFeeAmount

TotalFeeAmtWithTax

TotalFeeTaxAmount

TotalProductAmount

TotalProductAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the fees on the FulfillmentOrder, excluding adjustments and tax. This value
only includes FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the fees on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type Fee. This amount is equal to TotalFeeAmount +
TotalFeeTaxAmount.

This field is available in API version 56.0 and later.

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
Total price of the products on the FulfillmentOrder, excluding order adjustments, delivery
charges, and fees. This value only includes FulfillmentOrderLineItems of type code Product.

**Type**
currency


Standard Objects FulfillmentOrder

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the products on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type code Product. This amount is equal to TotalProductAmount
+ TotalProductTaxAmount.

This field is available in API version 49.0 and later.

```
TotalProductTaxAmount

TotalTaxAmount

Type

TypeCategory

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the FulfillmentOrder. Each type corresponds to one type category, shown here in
parentheses. You can customize the type picklist to represent your business processes, but
the type category picklist is fixed because processing is based on those values. If you customize
the type picklist, include at least one type value for each type category.

Default values are:

**•** `Download` (Digital)

**•** `Email` (Digital)

**•** `In Store Pickup` (Physical)

**•** `Retail Store` (Physical)

**•** `Supplier` (Drop Ship)

**•** `Warehouse` (Physical)

**Type**
picklist


### Standard Objects FulfillmentOrderItemAdjustment

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each type category corresponds to one or more types.

Possible values are:

**•** `DIGITAL` —Digital

**•** `DROPSHIP` —Drop Ship

**•** `PHYSICAL` —Physical

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[FulFillmentOrderChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[FulfillmentOrderFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[FulfillmentOrderOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[FulfillmentOrderShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

SEE ALSO:

FulfillmentOrderLineItem

Order

OrderSummary

### FulfillmentOrderItemAdjustment

Represents a price adjustment on a FulfillmentOrderLineItem. Corresponds to an OrderItemAdjustmentLineSummary associated with
the corresponding OrderItemSummary. This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects FulfillmentOrderItemAdjustment

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
Amount

CampaignName

CouponName

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Campaign associated with the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon associated with the adjustment.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the adjustment applies.
The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.


Standard Objects FulfillmentOrderItemAdjustment

**Field** **Details**

```
Description

FulfillmentOrderId

FulfillmentOrderItem

AdjustmentNumber

FulfillmentOrder

LineItemId

OrderItemAdjust

LineSummaryId

PromotionName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem to which the
adjustment applies.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItemAdjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrderLineItem to which this adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemAdjustmentLineSummary associated with the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects FulfillmentOrderItemTax

**Field** **Details**

**Description**
Promotion associated with the adjustment.

```
 TotalAmtWithTax

 TotalTaxAmount

```

SEE ALSO:

### FulfillmentOrder FulfillmentOrderItemTax

FulfillmentOrderLineItem

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.

OrderItemAdjustmentLineSummary

### FulfillmentOrderItemTax

Represents the tax on a FulfillmentOrderLineItem or FulfillmentOrderItemAdjustment. Corresponds to an OrderItemTaxLineItemSummary.
This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.


Standard Objects FulfillmentOrderItemTax

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

Description

FulfillmentOrderId

FulfillmentOrder

ItemAdjustId

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the FulfillmentOrderItemTax.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the tax applies. The
default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the FulfillmentOrderItemTax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated FulfillmentOrder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects FulfillmentOrderItemTax

**Field** **Details**

**Description**
If this object represents tax on an adjustment, this value is the ID of the
FulfillmentOrderItemAdjustment to which the tax applies. If this value is null, the adjustment
applies to a FulfillmentOrderLineItem.

```
FulfillmentOrderItem

TaxNumber

FulfillmentOrder

LineItemId

OrderItemTaxLineItem

SummaryId

Rate

TaxEffectiveDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderItemTax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents tax on a FulfillmentOrderLineItem, this value is the ID of that
FulfillmentOrderLineItem. If this object represents tax on an adjustment, this value is the ID
of the FulfillmentOrderLineItem to which the adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemTaxLineItemSummary associated with the OrderItemSummary that
corresponds to the FulfillmentOrderLineItem to which the tax applies.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tax rate used to calculate the Amount.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.


### Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the Amount is actual or estimated.

Possible values are:

**•** `Actual`

**•** `Estimated`

**FulFillmentOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

### FulfillmentOrder

FulfillmentOrderItemAdjustment

### FulfillmentOrderLineItem

OrderItemTaxLineItemSummary

### FulfillmentOrderLineItem

Represents a product or delivery charge belonging to a FulfillmentOrder. Corresponds to an OrderItemSummary. This object is available
in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the FulfillmentOrder associated with the FulfillmentOrderLineItem.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

```
Description

EndDate

FulfillmentOrderId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the FulfillmentOrderLineItem.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
End date of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
FulfillmentOrder

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
FulfillmentOrder

LineItemNumber

GrossUnitPrice

IsReship

MainFulfillmentOrderLineItemId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unit price, including tax, of the FulfillmentOrderLineItem. This value is equal to TotalPrice +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the FulfillmentOrderLineItem belongs to a reshipment. The default value
is false.

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original FulfillmentOrderLineItem.

This field is a relationship field.

This field is available in API version 63.0 and later.

**Relationship Name**
FulfillmentOrderLineItem

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrderLineItem


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
OrderItemId

OrderItemSummaryId

OriginalQuantity

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original OrderItem for the OrderItemSummary associated with the
FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemSummary associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItemSummary

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Original quantity of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Description**
ID of the product represented by the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
Quantity

QuantityUnitOfMeasure

RejectedQuantity

RejectReason

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Current quantity of the FulfillmentOrderLineItem. Equal to the original quantity minus any
canceled quantity.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unit of measure of the quantity, for example: unit, gallon, ton, or case.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used by the Distributed Order Management package and Store Fulfillment app to store the
quantity that has been rejected by a fulfillment location.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the FulfillmentOrderLineItem was rejected by a fulfillment location, the reason for the
rejection.


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

Default values are:

**•** `Damaged`

**•** `Just Sold`

**•** `Other`

**•** `Out of Packing Supplies`

**•** `Out of Stock`

This field is available in API version 56.0 and later.

```
ReshipReason

ServiceDate

ScopeIdentifierText

TotalAdjustmentAmount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the FulfillmentOrderLineItem belongs to a reshipment, the reason for the reshipment.

Default values are:

**•** `Damaged`

**•** `Lost`

**•** `Unknown`

**•** `Wrong Item`

This field is available in API version 53.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Service or start date of the FulfillmentOrderLineItem.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unique identifier used to identify the scope in which this fulfillment order line item record
is created.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Description**
Total of any price adjustments applied to the FulfillmentOrderLineItem.

```
TotalAdjustment

AmountWithTax

TotalAdjustment

TaxAmount

TotalAmount

TotalLineAmount

TotalLineAmountWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the FulfillmentOrderLineItem, inclusive of
tax. This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the FulfillmentOrderLineItem, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later.


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
TotalLineTaxAmount

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
Tax on the TotalLineAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the FulfillmentOrderLineItem. Equal to UnitPrice
times Quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalPrice.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of the FulfillmentOrderLineItem. Matches the type of the associated OrderItemSummary.
Delivery Charge indicates that the FulfillmentOrderLineItem represents a delivery charge.
Fee indicates that it represents another type of fee, such as a return fee. Order Product
indicates that it represents any other type of product, service, or charge. Each type corresponds
to one type code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge` (Charge)

**•** `Fee` (Charge) This value is available in API v56.0 and later.

**•** `Order Product` (Product)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


### Standard Objects FunctionConnection

**Field** **Details**

**Description**
Type code of the FulfillmentOrderLineItem. Matches the type code of the associated
OrderItemSummary. Processing depends on this value. Charge indicates that the
FulfillmentOrderLineItem represents a charge or fee. Product indicates that it represents any
other type of product, service, or charge. A type code can be associated with one or more
types.

Possible values are:

**•** `Charge`

**•** `Product`

```
 UnitPrice

```

**[FulFillmentOrderChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Unit price of the FulfillmentOrderLineItem.

Change events are available for the object.

SEE ALSO:

FulfillmentOrder

FulfillmentOrderItemAdjustment

FulfillmentOrderItemTax

OrderItemSummary

### FunctionConnection

Represents a connection between an org and Salesforce Functions. This object is available in API version 52.0 and later.

In API version 53.0, the name of this object was changed from SfFunctionsConnection to FunctionConnection.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`


Standard Objects FunctionConnection

Fields

**Field** **Details**

```
Error

FunctionsAccountLoginOrg

FunctionsAccountName

FunctionsAccountUuid

Sequence

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error string, if any, for the connection between the org and Salesforce Functions.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce Functions account login org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce Functions account name.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique Salesforce Functions account UUID. This is a generated ID that is not in Salesforce
object ID format.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Sequence number for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects FunctionInvocationRequest

**Field** **Details**

**Description**
The status of the connection between the org and Salesforce Functions.

Possible values are:

**•** `Attempted`

**•** `None`

**•** `TrustedBiDirection`

**•** `TrustedUniDirection`

The default value is 'None'. `TrustedBiDirection` indicates the connection is fully
established.

Usage

FunctionConnection is not intended for direct use and should be treated as a read-only object that represents the current connection
information between your org and Salesforce Functions. To create and manage connections between your org and Salesforce Functions
[use the steps and commands described in the Salesforce Functions developer documentation.](https://developer.salesforce.com/docs/platform/functions/guide/index.html)

FunctionConnection is not supported in Trialforce templates or org snapshots.

### FunctionInvocationRequest

Represents invocation information for a Salesforce Function. This object is available in API version 51.0 and later.

When a Salesforce Function is invoked using the Apex `functions.Function` invoke methods, a FunctionInvocationRequest
record is created that contains information on the status and results of the invocation.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`, `update()`

Fields

**Field** **Details**

```
CallbackStatus

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the callback for asynchronous invocations. This field is new in API version 52.0.

Possible values are:

**•** `Completed`  - Not used for the Salesforce Functions beta.


Standard Objects FunctionInvocationRequest

**Field** **Details**

**•** `Enqueued`                   - The Function has completed (either successfully or unsuccessfully), and
the callback has been enqueued for asynchronous execution in the Salesforce org.

**•** `Failed`                   - Not used for the Salesforce Functions beta.

**•** `PendingResponse`                   - The Function has not yet completed, so the callback has not
been called yet.

The default value is 'PendingResponse'.

```
ExecutionTime

ExtendedResponse

FunctionName

InvokingNamespacePrefix

NamespacePrefix

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The execution time of the Function in milliseconds.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
JSON object with additional information about the result of the Function execution.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the Function that was invoked. This name is case-sensitive and uses the format
“ `project name`   - `function name` ”

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Prefix of the namespace that invokes the function. A namespace can invoke the global
function using an installed package via Apex.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FunctionInvocationRequest

**Field** **Details**

**Description**
The namespace prefix that is associated with this object. This object is available in API version
53.0 and later. Each Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component in a managed package
by using the `namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
OwnerId

ResponseBody

ResponseContentType

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The owner of the FunctionInvocationRequest.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
base64

**Properties**
Nillable, Update

**Description**
Response body of the invoked Function.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects FunctionInvocationRequest

**Field** **Details**

**Description**
Content type of the response body of the invoked Function. For example, the content type
could be `application/json`, `text/csv`, or various other values depending on what
the Function returned.

```
ResponseLength

ResponseName

ResponseUncompressedLength

StackTrace

Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the response body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of response, not currently used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Uncompressed length of the Function response, if the response content was compressed.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
If there was an error invoking the function, this field contains the Function stack trace.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the invoked Function. Functions that are invoked asynchronously can be in a queued
`InProgress` state before they are invoked.

Possible values are:


### Standard Objects FunctionReference

**Field** **Details**

**•** `Dispatched`                   - Not used for the Salesforce Functions beta.

**•** `Error`                   - The Function failed to execute due to either an error starting the Function, or
an error while the Function was running.

**•** `FunctionInProgress`                   - The Function invocation has been sent to the Salesforce
Functions compute environment, and is running.

**•** `InProgress`                   - The Function invocation request has been enqueued.

**•** `New`                   - The Function invocation request has been created, but not enqueued yet.

**•** `Success`                   - The Function has completed execution. For status on whether the callback
has been called, see the CallbackStatus field.

The default value is 'New'.

Usage

Treat FunctionInvocationRequest records as read-only records used to get information about a specific Function invocation. To invoke
Functions, use the Apex `functions.Function` class invoke methods.

FunctionInvocationRequest is not supported in Trialforce templates or org snapshots.

### FunctionReference

Represents a deployed Salesforce Function associated with an org. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Access

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The label for whether managed components can access across namespaces.

Possible values are:

**•** `Global` —The managed components can access across namespaces.

**•** `Public` —The managed components can access within the same namespace.

The default value is `Public` .


Standard Objects FunctionReference

**Field** **Details**

```
Description

FunctionName

ImageReference

Language

MasterLabel

NamespacePrefix

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Function.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The developer name of the Function. This name is case sensitive and uses the format
“ `project name`   - `function name` ”. This field is unique within your organization.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Stores details about an image associated with a function. This is internal only, used by
packaging only, and should not be editable or set by the customer.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language code for the Function, such as “en_US”.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the Function.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects GenAIConversationSummary

**Field** **Details**

**Description**
The namespace prefix that is associated with this object. This object is available in API version
53.0 and later. Each Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component in a managed package
by using the `namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Usage

Treat FunctionReference records as read-only records used to get information about a specific Function associated with your org. To
invoke Functions, use the Apex `functions.Function` class invoke methods. To deploy and associate Functions with your org,
[use Salesforce CLI commands associated with Functions, as described in the Salesforce Functions developer documentation.](https://developer.salesforce.com/docs/platform/functions/guide/index.html)

FunctionReference is not supported in Trialforce templates or org snapshots.

### GenAIConversationSummary

Represents a generated summary of a voice or video call. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, Einstein Conversation Insights and Einstein for Sales must be enabled in your org.

Fields

**Field** **Details**

```
ConversationRecordId

```

**Type**
reference


Standard Objects GenAIConversationSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the related voice or video call record.

This field is a polymorphic relationship field.

**Relationship Name**
ConversationRecord

**Relationship Type**
Master-detail

**Refers To**
VideoCall, VoiceCall (the master object)

```
CurrencyIsoCode

ErrorMessage

Source

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

Possible values are:

**•** `MXN` —Mexican Peso

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An error message when there is a problem with sharing the conversation summary.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Whether the summary shown is content generated by Einstein or subsequently edited by a
user.

Possible values are:

**•** `EINSTEIN_GPT` —Einstein


### Standard Objects GenAiFunctionDefinition

**Field** **Details**

**•** `USER_EDITED` —User Edited

```
Status

Summary

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the summary.

Possible values are:

**•** `ERROR` —Error

**•** `GENERATING` —Generating

**•** `SUCCESS` —Success

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary text content.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**GenAIConversationSummaryChangeEvent on page 68**
Change events are available for the object.

**GenAIConversationSummaryFeed on page 55**
Feed tracking is available for the object.

**GenAIConversationSummaryHistory on page 63**
History is available for tracked fields of the object.

**GenAIConversationSummaryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**GenAIConversationSummaryShare on page 67**
Sharing is available for the object.

### GenAiFunctionDefinition

Represents an agent action. This object is available in API version 60.0 and later.


Standard Objects GenAiFunctionDefinition

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
Description

DeveloperName

InvocationTarget

InvocationTargetType

```

**Type**
textarea

**Properties**
Create, Update

**Description**
A description explaining the general purpose and domain of the action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target invocation used by invocation operations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Invocable action types used by invocation operations.

Possible values are:

**•** `apex`

**•** `flow`

**•** `generatePromptResponse`


Standard Objects GenAiFunctionDefinition

**Field** **Details**

```
IsConfirmationRequired

IsLocal

Language

LocalDeveloperName

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether confirmation is required for this action.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is a calculated field and is set to `true` if this action is an edited version of a standard
action.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the GenAiFunctionDefinition. The value for this field is the language value
of the org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name for this action within a topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the generative AI action.

**Type**
string


Standard Objects GenAiFunctionDefinition

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiFunctionDefinition.

```
ParentId

PlannerId

PluginId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the action.

This field is a relationship field.

**Relationship Name**
Parent

**Refers To**
GenAiPlannerFunctionDef

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent planner service for this action.

This field is a relationship field.

**Relationship Name**
Planner

**Refers To**
GenAiPlannerDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent topic for this agent action.

This field is a relationship field.

**Relationship Name**
Plugin

**Refers To**
GenAiPluginDefinition


### Standard Objects GenAiPlannerDefinition

**Field** **Details**

```
Source

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The optional source standard or custom action from which this action's configuration,
including description, input, and output, is copied. If there's no value, the action is used only
within the parent topic.

### GenAiPlannerDefinition

Represents an agent planner service that uses a large language model (LLM) and a reasoning strategy to decompose a given task into
smaller subtasks, identify the most suitable actions for each subtask, and invoke them. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
Capabilities

Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A set of tags associated with the agent planner service definition.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description explaining the general purpose and domain of the agent planner service
definition.


Standard Objects GenAiPlannerDefinition

**Field** **Details**

```
DeveloperName

Language

MasterLabel

NamespacePrefix

PlannerType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the GenAiPlannerDefinition. The value for this field is the language value
of the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the agent planner service definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiPlannerDefinition.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A particular approach to problem solving that is given as prompt instructions to a large
language model (LLM).

Possible values are:

**•** `AiCopilot__ReAct` —Uses a reactive planning strategy to solve problems with the
LLM. This strategy consists of prompting the LLM to generate the next step in response
to an event and the current context. It differs from a sequential planner in that it doesn’t
plan more than one step ahead of time.


### Standard Objects GenAiPlannerFunctionDef

**Field** **Details**

**•** `AiCopilot__SequentialPlannerIntentClassifier` —Uses an intent
classifier prompt and a sequential planner prompt. With each text input, the planner
asks the LLM to generate a step-by-step plan to finish the goal. It plans first, then executes.

### GenAiPlannerFunctionDef

Represents a relationship between the agent planner service and agent actions. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
PlannerId

Plugin

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
Planner

**Relationship Type**
Lookup

**Refers To**
GenAiPlannerDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A set of actions that contextualize the agent planner service.


### Standard Objects GenAiPluginDefinition GenAiPluginDefinition

Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents. This object is available in
API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
CanEscalate

Description

DeveloperName

IsLocal

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this topic is eligible for escalation to a rep.

The default value is `false` .

**Type**
textarea

**Properties**
Create, Update

**Description**
The description of the topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the API name of the topic. Can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

**Type**
boolean


Standard Objects GenAiPluginDefinition

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is a calculated field and is set to `true` if this topic is an edited version of a standard
topic.

The default value is `false` .

```
Language

LocalDeveloperName

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the topic.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name for this topic within an agent.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of these values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This


Standard Objects GenAiPluginDefinition

**Field** **Details**

field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
ParentId

PlannerId

PluginType

Scope

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the topic.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Refers To**
GenAiPlannerDefinition, GenAiPlannerFunctionDef

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent planner service for this topic.

This field is a relationship field.

**Relationship Name**
Planner

**Refers To**
GenAiPlannerDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `APICustomTopic`

**•** `Topic`

**Type**
textarea


### Standard Objects GenOpPlanRequest

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
A specific job description for a topic.

```
Source

### GenOpPlanRequest

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The optional source standard or custom topic from which this topic's configuration, including
description, instructions, and utterances, is copied. If there's no value, the topic is used only
within this agent version.

Represents a request to generate a service plan. This object is available in API version 67.0 and later.

[Each request is stored as record data. We support all delete operations at the record or bulk level. For example, you can use Bulk API 2.0](https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-manage-objects-delete-bulk.html)
[to delete multiple records in Marketing Cloud Next.](https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-manage-objects-delete-bulk.html)

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```

Special Access Rules

To access this object, you must have the Service Planner Access add-on license.

Fields

**Field Name** **Details**

```
CopilotId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The ID of the Einstein Copilot associated with the plan request.

This field is a relationship field.


Standard Objects GenOpPlanRequest

**Field Name** **Details**

**Relationship Name**
Copilot

**Refers To**
GenAiPlannerDefinition

```
CopilotName

ErrorCode

ErrorMessage

```

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The name of the Einstein Copilot associated with the plan request.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

(Optional) The standard error code when plan generation fails.

Possible values are:

**•** `AgentNotActive`

**•** `AgentNotFound`

**•** `CaseGroundingNotEnabled` (Service AI Grounding isn’t enabled)

**•** `InstructionsOrActionsNotFound`

**•** `InsufficientData`

**•** `InvalidRecordId`

**•** `NoEligibilityDefined` (No eligibility criteria defined)

**•** `NotEligible`

**•** `RagConfigurationError`

**•** `StepSummaryEmpty`

**•** `TopicIdNotFound`

**•** `TopicNotFound`

**•** `Unknown`

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The error message when plan generation fails.


Standard Objects GenOpPlanRequest

**Field Name** **Details**

```
LlmModelName

LlmProviderName

Name

ParentId

PromptTemplateDevName

```

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The name of the large language model used for plan generation. The maximum
length is 80 characters.

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The name of the LLM provider. The maximum length is 80 characters.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Required) The auto-generated name of the generated operation plan request.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

(Required) The ID of the service plan parent record.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Master-detail

**Refers To**
Case, Incident, MessagingSession, Opportunity (the master object)

**Type**
string

**Properties**
Filter, Group, Sort, Nillable


Standard Objects GenOpPlanRequest

**Field Name** **Details**

**Description**
(Optional) The developer name of the prompt template used for plan generation. The
maximum length is 80 characters.

```
PromptTemplateVersionNo

Reason

RequestSource

```

**Type**
int

**Properties**
Filter, Group, Sort, Nillable

**Description**
(Optional) The version number of the prompt template.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

(Required) The reason why plan generation failed or returned no steps.

Possible values are:

**•** `CannotGeneratePlan`

**•** `NoEligibilityConfig` (no eligibility criteria set)

**•** `None` (default)

**•** `NoPlanGenerated` PlanEmpty

**•** `PlanEmptyInsufficientData`

**•** `RagConfigurationError`

**•** `ThresholdError` (eligibility not met for unknown reason)

**•** `ThresholdNotMet`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

(Optional) The source where the plan request originated.

Possible values are:

**•** `CASE`

**•** `EINSTEIN_LEX` (Einstein Chat LEX component)

**•** `INCIDENT`


### Standard Objects GeoCountry

**Field Name** **Details**

```
RequestType

Status

Utterance

### GeoCountry

```

**Type**
picklist

**Properties**

Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

(Required) The type of service plan request.

Possible values are:

**•** `Close`

**•** `Generation`

**•** `Summary` (default)

**Type**
picklist

**Properties**

Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

(Required) The status of the plan generation request.

Possible values are:

**•** `Error`

**•** `Incomplete`

**•** `InProgress` (default)

**•** `Success`

**Type**
textarea

**Properties**
Nillable

**Description**
(Optional) The natural language input or prompt used for plan generation. The maximum
length is 32,000 characters.

Represents a country. This object is available in API version 56.0 and later.


Standard Objects GeoCountry

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The GeoCountry object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
Description

IsoCode

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Two-letter ISO code of the country as defined in the org’s State-Country picklist. This field is
unique within your organization

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


### Standard Objects GeolocationBasedAction

**Field** **Details**

```
Name

OwnerId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the country that corresponds with the ISO code.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the GeoCountry record. By default, the asset owner is the user who created
the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**GeoCountryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**GeoCountryShare on page 67**
Sharing is available for the object.

SEE ALSO:

GeoState

TaxGeoConfig

### GeolocationBasedAction

Represents a geolocation-based action, which is an action that’s triggered when a user enters, exits, or is within the area of the associated
object. Available in API version 61.0 and later.


Standard Objects GeolocationBasedAction

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ActionData

ActionType

Description

InitialTimeInvoked

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the selected action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action.

Possible values are:

**•** `PlatformAlert`

**•** `QuickAction`

**•** `ViewRecord`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the action.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects GeolocationBasedAction

**Field** **Details**

**Description**
Captures the first time the mobile worker invoked this action.

```
LastReferencedDate

LastTimeInvoked

LastViewedDate

Name

OwnerId

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
Create, Filter, Nillable, Sort, Update

**Description**
Captures the last time the mobile worker invoked this action.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the action.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.


Standard Objects GeolocationBasedAction

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Radius

ReferenceRecordId

TriggerType

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distance in meters from the location of the associated object that triggers the action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record that the action is associated with.

This field is a relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The event that triggered this action.

Possible values are:

**•** `GeoFenceEnter` —Enter

**•** `GeoFenceExit` —Exit


### Standard Objects GeoState GeoState

Represents a state. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The GeoState object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
Description

GeoCountryId

IsoCode

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the GeoCountry associated with this GeoState.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
string

**Properties**
Create, Filter, Group, Sort


### Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**Description**
Two-letter ISO code of the state as defined in the org’s State-Country picklist. This field is
unique within your organization

```
LastReferencedDate

LastViewedDate

Name

```

SEE ALSO:

GeoCountry

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
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the state that corresponds with the ISO code.

### GtwyProvPaymentMethodType

The gateway provider payment method type allows integrators and payment providers to choose an active payment to receive an
order's payment data rather than allowing the Salesforce Order Management platform to select a default payment method. This object
is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`


Standard Objects GtwyProvPaymentMethodType

Fields

**Field** **Details**

```
Comments

DeveloperName

GtwyProviderPaymentMethodType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can provide additional details about the gateway provider payment method type
record. Supports a maximum of 1000 characters.

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
for each record. If no `DeveloperName` is specified, Salesforce generates one for
each record, which slows performance.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links the Salesforce payment method to the payment method used in the Salesforce Order
Management storefront. Your payment gateway integration uses this field when finding a
payment method to link to a payment.

The value of `GtwyProviderPaymentMethodType` must match the payment method
value sent to the order's Payment Instrument in Salesforce Order Management.

Listed below are several examples of payment method values that Salesforce could receive
from Salesforce Order Management.

**•** `CREDIT_CARD`

**•** `BASIC_CREDIT`

**•** `CreditCard`

**•** `GooglePay`


Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**•** `ApplePay`

```
Language

LastViewedDate

MasterLabel

NamespacePrefix

PaymentGatewayProviderId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the payment gateway integration.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view `(LastReferencedDate)`
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The gateway provider payment method type name that appears in the user
interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace of the payment gateway integration classes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the payment gateway provider that Salesforce Order Management should use
when processing payments. One payment gateway provider can be related to multiple
payment method types.

This is a relationship field.


Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**Relationship Name**
PaymentGatewayProvider

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayProvider

```
PaymentMethodType

RecordTypeId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of payment method used on an order in Salesforce Order Management.

Possible values are:

**•** `AlternativePaymentMethod`

**•** `CardPaymentMethod`

**•** `DigitalWallet`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type entity related to the gateway provider payment method type.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

The Salesforce Order Management payment record must have a `ProcessorId` field with the same value as the payment gateway's
`ExternalReferenceId` field. The gateway provider payment method type record must have a `PaymentMethodType` field
that looks up to the payment method that you want to associate to your payment. Finally, the payment gateway and gateway provider
payment method type must have matching `PaymentGatewayProviderId` fields. When you've established these relationships,
the payment record can infer your payment method from the gateway provider payment method type record.


### Standard Objects Goal Goal

The Goal object represents the components of a goal such as its name, description, and status.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CompletionDate

Description

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the goal.

**Type**
textarea


Standard Objects Goal

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the goal. The maximum length is 65,535 characters.

```
DueDate

ImageUrl

IsKeyCompanyGoal

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the goal is due.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the goal image. The image must be stored in Documents and set as
externally available. Applicable only to Goal objects of `Type` : Goal.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the goal is a key company goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Goal

**Field Name** **Details**

**Description**
The timestamp that indicates when a user last viewed this goal. If this value is
null, this record might have been only referenced ( `LastReferencedDate` )
and not viewed.

```
Name

OwnerId

Progress

StartDate

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the goal. The maximum length is 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the goal.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The progress of the goal measured as a percentage.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the goal.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the goal.

Possible values:

**•** Draft


### Standard Objects GoalLink

**Field Name** **Details**

**•** Published

**•** Completed

**•** Canceled

**•** Not Completed

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**GoalFeed**

Feed tracking is available for the object.

**GoalHistory**

History is available for tracked fields of the object.

**GoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**GoalShare**

Sharing is available for the object.

### GoalLink

Represents the relationship between two goals. This is a many-to-many relationship, meaning that each goal can link to many other
goals.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated name of the goal link.


### Standard Objects GoogleDoc

**Field Name** **Details**

```
ParentGoalId

SubgoalId

### GoogleDoc

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the parent goal.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the subgoal.

Represents a link to a Google Document. This object is available in API version 14.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in **All** Editions except **Database.com** for Google Apps Premier Edition accounts. See the Salesforce online help
for more information.

Fields

**Field** **Details**

```
Name

Owner

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the Google document.

**Type**
reference


### Standard Objects Group

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The ID of the user who currently owns this Google Document. Default value is the
user logged in to the API to perform the create.

```
ParentId

Url

### Group

```

A set of User records.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the attachment's parent object. The following objects are supported
as parents of Google documents: Account, Asset, Campaign, Case, Contact, Contract,
Custom Object Behavior, Lead, Opportunity, Product2, and Solution.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The URL of the Google document.

### Groups are sets of users. They can contain individual users, other groups, the users in a particular role or territory, or the users in a particular

role or territory plus all the users below that role or territory in the hierarchy.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `search()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Authenticated internal and external users can access this object.


Standard Objects Group

Fields

**Field** **Details**

```
Description

DefaultDivision

DeveloperName

DoesIncludeBosses

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the group. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. This name is unique
by group type and corresponds to **Group Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Only your Salesforce org’s internal users can access this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether records shared with users in this group are also shared with users
higher in the role hierarchy ( `true` ) or not ( `false` ). This field is only available for public


Standard Objects Group

**Field** **Details**

groups. This field corresponds to the Grant Access Using Hierarchies checkbox in Setup.
This field is available in API version 18.0 and later.

```
DoesSendEmailToMembers

Email

Name

OwnerId

QueueRoutingConfigId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is sent ( `true` ) or not sent ( `false` ) to the group members.
The email is sent to queue members as well.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address for a group of type Case. Applies only for a case queue.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the group. Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the group.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Organization, User

**Type**
reference


Standard Objects Group

**Field** **Details**

**Properties**
Create, Delete, Query, Retrieve, Update

**Description**
The ID of the queue routing configuration associated with the queue.

```
RelatedId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the associated groups. For groups of type “Role,” the ID of the
associated UserRole. The `RelatedId` field is polymorphic.

This is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
User, UserRole

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of the group. One of the following values:

**•** `AllCustomerPortal` —Public group that includes all Customer Portal or
Customer Community Plus users. This type is only available when a Customer Portal
or a Customer Site is enabled for your org.

**•** `ChannelProgramGroup` —Public group for partners in a channel program.

**•** `CollaborationGroup` —Chatter group.

**•** `Manager` —Public group that includes a user’s direct and indirect managers. This
group is read-only.

**•** `ManagerAndSubordinatesInternal` —Public group that includes a user
and the user’s direct and indirect reports. This group is read-only.

**•** `Organization` —Public group that includes all the User records in the
organization. This group is read-only.

**•** `Participant` —Compliant Data Sharing group that includes internal users who
have the Use Compliant Data Sharing permission. A group can contain other
participant groups only, or a group can contain both internal users with the Use


Standard Objects Group

**Field** **Details**

Compliant Data Sharing permission and other participant groups. This value is only
available when Compliant Data Sharing is enabled for your org.

**•** `PRMOrganization` —Public group that includes all the partners in an organization
that has the partner site or portal feature enabled.

**•** `Queue` —Public group that includes all the User records that are members of a
queue.

**•** `Regular` —Standard public group. When you `create()` a group, its type must
be `Regular`, unless a partner site or portal is enabled for the organization, in which
case the type can be `Regular` or `PRMOrganization` .

**•** `Role` —Public group that includes all the User records in a particular UserRole.

**•** `RoleAndSubordinates` —Public group that includes all the User records in a
particular UserRole and all the User records in any subordinate UserRole. Only available
when digital experiences is enabled for your org and Experience Cloud site users are
created with external account roles other than a shared person account role.

**•** `RoleAndSubordinatesInternal` —Public group that includes all the User
records in an internal UserRole, excluding customer and partner roles, and all the
User records in any subordinate internal UserRole.

**•** `SharingRecordCollGroup` —Public group that has access to a
SharingRecordCollection.

**•** `Territory` —Public group that includes all the User records in an organization
that has the territory feature enabled.

**•** `TerritoryAndSubordinates` —Public group that includes all the User records
in a particular UserRole and all the User records in any subordinateUserRole in an
organization that has the territory feature enabled.

Only `Personal`, `Regular`, and `Queue` can be used when creating a group. The
other values are reserved.

Usage

Unlike users, this object can be deleted.

Only public groups are accessible via the API. Personal groups are not available.

In API version 34.0 and later, you can query a group using `Related.Name` to retrieve the group’s name. `Related.Name` is
supported for public groups, user roles, territories, manager groups, and user names.

In API version 13.0 and later, if you delete a public group, it is deleted even if it has been used in sharing, consistent with the behavior
for UserRole. In versions before 13.0, such sharing prevents the record from being deleted.

SEE ALSO:

GroupMember

Overview of Salesforce Objects and Fields


### Standard Objects GroupMember GroupMember

Represents a User or Group that is a member of a public group.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
GroupId

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Group.

This is a relationship field.

**Relationship Name**
### Group

**Relationship Type**
Lookup

**Refers To**
### Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the User or Group that is a direct member of the group.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects GroupMembershipEventLog

Usage

If your group contains more than 10,000 members, for improved performance, you can adjust group membership using the GroupMember
API object instead of the group's detail page in Setup. You can also adjust membership using the public group's access summary or user
access policies in Setup.

A record exists for every User or Group who is a direct member of a public group whose `Type` field is set to Regular. User records that
are indirect members of Regular public groups aren't listed as group members. A User can be an indirect member of a group if he or
she is in a UserRole above the direct group member in the hierarchy, or if he or she is a member of a group that is included as a subgroup
in that group.

If you attempt to create a record that matches an existing record, the system simply returns the existing record.

SEE ALSO:

Overview of Salesforce Objects and Fields

### GroupMembershipEventLog

Group Membership events capture details about changes to public group and queue membership, such as when members are added
to or removed from the public group or queue. This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
IP address of the client employing salesforce.com services.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects GroupMembershipEventLog

**Field** **Details**

**Description**
Amount of cpu cycles used by the request

```
GroupIdentifier

GroupType

LoginKey

MemberIdentifier

OperationType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the group whose membership changed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of group being updated.

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
The ID of the member added to or removed from the group. Public groups can contain
individual users, other groups, or users in a specified role or territory. Queues can contain
individual users, roles, public groups, territories, connections, or partner users.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of operation that occurred, such as a group member being added or removed from
a group.


Standard Objects GroupMembershipEventLog

**Field** **Details**

```
RequestIdentifier

RunTime

SessionKey

Timestamp

Uri

UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects GuestBuyerProfile

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

### GuestBuyerProfile

Represents a store's guest buyer profile, which allows unauthenticated buyers to browse the store. This object is available in API version
51.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency displayed to the guest buyer when they’re viewing the store.

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Detailed description of the profile. Includes information like which store the profile is used
in.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were modified


### Standard Objects HashtagDefinition

**Field** **Details**

```
LastViewedDate

Name

### HashtagDefinition

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were viewed

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the guest buyer profile. Including a reference to the store helps with later
identification.

### HashtagDefinition represents hashtag (#) topics in public Chatter posts and comments. Public posts and comments include those on

profiles and in public groups, but not those on records or in private groups. This object is available in API version 26.0 and later.

Important: Starting in Spring ’16, API access to HashtagDefinition is disabled across all API versions. Any integrations relying on
API queries to this object stop working. You can continue to use hashtags in posts and comments, and the hashtags continue to
create corresponding topics. We recommend that you redirect all API queries and reports using the HashtagDefinition object to
[use the Topic object instead. For more information, see Retiring the Legacy HashtagDefinition Object—FAQs.](https://help.salesforce.com/apex/HTViewSolution?urlname=Retiring-the-Legacy-HashtagDefinition-Object)

Supported Calls

`delete(), describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
HashtagCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a hashtag topic is used.


### Standard Objects HealthCareDiagnosis

**Field Name** **Details**

```
Name

NameNorm

NetworkId

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic, normalized
to remove capitalization and punctuation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the HashtagDefinition belongs. This field
is available only if digital experiences is enabled in your org.

Use this object to identify public hashtag topics and see how often they’re used.

SEE ALSO:

Topic

### HealthCareDiagnosis

Represents information related to industry-standard healthcare diagnosis codes. Before the Spring ’21 release, the Healthcare Procedure
and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used for
prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set Bundle
objects for this purpose instead.


Standard Objects HealthCareDiagnosis

Example: The Code Set and Code Set Bundle objects improve on the old objects by adding support for terminology system
information. This added support comes in the form of the Source System and Version fields.

Note: Objects, flows, and apps that previously used Healthcare Diagnosis and Healthcare Procedure have been or will be
extended to support the use of Code Set and Code Set Bundle. Healthcare Diagnosis and Healthcare Procedure are to be
gradually phased out with future releases.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Code

CodeDescription

CodeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates the category for this diagnosis such as newborn, pediatric, maternity,
or adult.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry-standard diagnosis code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Description of the diagnosis code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

**Description**

Type of diagnosis code represented in the record such as ICD-9 or ICD-10.

```
EffectiveDate

EndDate

Gender

IsActive

IsComplicationOrComorbidity

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Start date for the code.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

End date for the code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether this diagnosis is for males, females, or all genders.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the diagnosis code is available for use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a complication or
comorbidity.


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

```
IsHospitalAcquiredCondition

IsMajorComplicationOrComorbidity

IsPresentOnAdmissionExempt

IsPrimaryDiagnosis

IsUnacceptablePrincipalDxIpAdmit

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis represents a condition acquired while in the
hospital.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a major complication or
comorbidity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is exempt from the diagnosis present on
admission requirement.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code can be used as primary diagnosis only, or can
be used in any diagnosis sequence.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is an unacceptable principal diagnosis for
inpatient admission per Medicare Code Edits.


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

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
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate) and not
viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the code that displays in search and lookup fields. Salesforce
recommends using the code along with the description to populate this field.
For example, use <Code>: <Description> or <Code>-<Description> such as
(E08.37X9 - Diabetes mellitus due to underlying condition).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects HealthCareProcedure

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[HealthCareDiagnosisChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareDiagnosisHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareDiagnosisOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareDiagnosisShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### HealthCareProcedure

Represents information related to industry-standard healthcare procedure codes. Before the Spring ’21 release, the Healthcare Procedure
and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used for
prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set Bundle
objects for this purpose instead.

Example: The Code Set and Code Set Bundle objects improve on the old objects by adding support for terminology system
information. This added support comes in the form of the Source System and Version fields.

Note: Objects, flows, and apps that previously used Healthcare Diagnosis and Healthcare Procedure have been or will be
extended to support the use of Code Set and Code Set Bundle. Healthcare Diagnosis and Healthcare Procedure are to be
gradually phased out with future releases.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Code

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Category of the procedure code such as anesthesia, surgery, radiology, and so
on.

**Type**
string


Standard Objects HealthCareProcedure

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry standard procedure code such as CPT or HCPCS.

```
CodeDescription

CodeShortDescription

CodeType

EffectiveDate

EndDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Description of the procedure code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Short description of the procedure code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Type of procedure code represented in the record such as CPT or HCPCS.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Start date for the code.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

End date for the code.


Standard Objects HealthCareProcedure

**Field Name** **Details**

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

Indicates whether the diagnosis code is available for use.

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
null, it’s possible that this record was referenced (LastReferencedDate) and not
viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the code that displays in search and lookup fields. Salesforce
recommends using the code along with the description to populate this field.
For example, use <Code>: <Description> or <Code>-<Description> such as
95115: Allergy injection.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this record.


### Standard Objects Holiday

**Field Name** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[HealthCareProcedureChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareProcedureHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareProcedureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareProcedureShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### Holiday

Represents a period of time during which your customer support team is unavailable. Business hours and escalation rules associated
with business hours are suspended during any holidays with which they are affiliated.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can’t access this object.

All users, even those without the “View Setup and Configuration” user permission, can view holidays via the API.

Fields

**Field** **Details**

```
ActivityDate

```

**Type**
date


Standard Objects Holiday

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the Holiday `IsAllDay` flag is set to `true` (indicating that it is an all-day holiday), then
the holiday due date information is contained in the `ActivityDate` field. This field is a
date field with a timestamp that is always set to midnight in the Coordinated Universal Time
(UTC) time zone. The timestamp is not relevant, and you should not attempt to alter it to
account for any time zone differences.

```
Description

EndTimeInMinutes

IsAllDay

IsRecurrence

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the holiday.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end time of the holiday in minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the duration of the holiday is all day ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the holiday is scheduled to repeat itself ( `true` ) or only occurs once
( `false` ). This is a read only field on update, but not on create. If this field value is `true`,
then any recurrence fields associated with the given recurrence type must be populated.

**Type**
string


Standard Objects Holiday

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the holiday.

```
NextOccurrenceDate

RecurrenceDayOfMonth

RecurrenceDayOfWeekMask

```

**Type**
date

**Properties**
Filter, Group, Nillable

**Description**

The next date of the holiday. Applies to recurring holidays only. Available in API version 58.0
and later. To access this field, you must have Field Service enabled and the Field Service
Standard permission.

This field isn't sortable. To compare this date to other dates, you must parse the string into
a date value to compare it to other dates.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day of the month on which the holiday repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the holiday repeats. This field contains a bitmask. For
each day of the week, the values are as follows:

**•** Sunday = `1`

**•** Monday = `2`

**•** Tuesday = `4`

**•** Wednesday = `8`

**•** Thursday = `16`

**•** Friday = `32`

**•** Saturday = `64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.


Standard Objects Holiday

**Field** **Details**

```
RecurrenceEndDateOnly

RecurrenceInstance

RecurrenceInterval

RecurrenceMonthOfYear

RecurrenceStartDate

RecurrenceType

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the holiday repeats. For multiday recurring events, this is the day on
which the last occurrence starts.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring holiday. For example, `2nd` or `3rd` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring holidays.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year on which the event repeats.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the recurring holiday begins. Must be a date and time before
`RecurrenceEndDateOnly` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects IconDefinition

**Field** **Details**

**Description**
Indicates how often the holiday repeats. For example, daily, weekly, or every Nth month
(where “Nth” is defined in `RecurrenceInstance` ).

```
StartTimeInMinutes

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start time of the holiday in minutes.

Use this object to view and update holidays, which specify dates and times at which associated business hours and escalation rules are
suspended.

### IconDefinition

Represents the icon-related metadata for a custom tab. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
ContentType

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s content type, for example, “image/png.”

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects IconDefinition

**Field Name** **Details**

**Description**

A unique virtual Salesforce ID for the icon.

```
Height

TabDefinitionId

Theme

Url

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s height in pixels. If the icon content type is an SVG type, height and
width values are not used.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The `TabDefinition` ID.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon’s theme.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified URL for this icon.


### Standard Objects Idea

**Field Name** **Details**

```
Width

### Idea

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s width in pixels. If the icon content type is an SVG type, height and
width values are not used.

Represents an idea on which users are allowed to comment and vote, for example, a suggestion for an enhancement to an existing
product or process. This object is available in API version 12 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Note: For other standard objects, the `describeLayout()` call returns the `recordTypeMappings` section that contains
the layout ID and picklist values for each record type. However, the `recordTypeMappings` section and the fields it includes
are not available for the Idea object.

When performing a SOSL search on Idea objects, IdeaComment objects are also searched.

Fields

**Field** **Details**

```
AttachmentBody

AttachmentContentType

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**

File data for the attachment. This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Type of the attachment. This field is available in API version 28.0 and later.


Standard Objects Idea

**Field** **Details**

```
AttachmentLength

AttachmentName

Body

Categories

Category

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the attachment in bytes. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of the attachment. This field is available in API version 28.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the Idea.

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize Ideas into logical groupings.

Note: This field is only available if your organization has the `Categories` field
enabled. This field is enabled by default in organizations created after API version 14
was released. If the `Categories` field is enabled, API versions 13 and earlier do
not have access to either the `Categories` or `Category` fields.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable picklist of values used to organize Ideas into logical groupings.

Note: This field is not available if your organization has the multi-select
`Categories` field enabled.


Standard Objects Idea

**Field** **Details**

```
CommunityId

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

This is a relationship field.

**Relationship Name**
Community

**Relationship Type**
Lookup

**Refers To**
Community

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who posted the idea or commented on the idea.

This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.


Standard Objects Idea

**Field** **Details**

```
CurrencyIsoCode

IdeaThemeID

IsDeleted

IsHtml

IsMerged

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the idea theme associated with the idea.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. If this value is `true`, your organization has the Ideas HTML editor enabled, and
the Idea `Body` may contain HTML. If this value is `false`, the HTML editor is disabled and
the Idea `Body` only contains regular text.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether the idea has been merged with a parent idea ( `true` ) or not
( `false` ). You can’t vote for or add comments to a merged idea.

Note: In API version 27, `IsMerged` replaces `IsLocked` . Existing formula fields
that use `IsLocked` must be edited to use `IsMerged` .


Standard Objects Idea

**Field** **Details**

```
LastCommentDate

LastCommentId

LastReferencedDate

LastViewedDate

NumComments

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last comment (child IdeaComment object) was added.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last comment (child IdeaComment object).

This is a relationship field.

**Relationship Name**
LastComment

**Relationship Type**
Lookup

**Refers To**
IdeaComment

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects Idea

**Field** **Details**

**Description**
The number of comments (child IdeaComment objects) that users have submitted for the
given idea.

```
ParentIdeaId

RecordTypeId

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID associated with this idea's parent idea. When multiple ideas are merged together,
one idea becomes the parent (master) of the other ideas. The `ParentIdeaId` is
automatically set when you merge ideas.

This is a relationship field.

**Relationship Name**
ParentIdea

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record type assigned to this object.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customizable picklist of values used to specify the status of an idea.


Standard Objects Idea

**Field** **Details**

```
Title

VoteScore

VoteTotal

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The descriptive title of the idea.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the Idea, used to sort Ideas on the Popular tab in the application user
interface. The internal algorithm that determines the score gives older votes less weight than
newer votes, simulating exponential decay. The score itself does not display in the application
user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
An Idea's total number of points. Each vote a user makes is worth ten points, therefore the
value of this field is ten times the number of votes an idea has received.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.

Note: If you are importing Idea data and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Audit fields are automatically updated during API operations unless you request to set these fields yourself..

Usage

Use this object to track ideas, which are written suggestions on which users can vote and comment.

SEE ALSO:

IdeaComment

Vote


### Standard Objects IdeaComment IdeaComment

Represents a comment that a user has submitted in response to an idea.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Note: When performing a SOSL search on IdeaComment objects, Idea objects are also searched.

Fields

**Field** **Field Type**

```
CommentBody

CommunityId

CreatorFullPhotoUrl

CreatorName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Body of the submitted comment.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo. This field is available in API version 28.0 and later.

**Type**
string


Standard Objects IdeaComment

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who posted the idea or commented on the idea. This field is available in
API version 28.0 and later.

```
CreatorSmallPhotoUrl

IdeaId

IsHtml

UpVotes

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the idea on which this comment was made.

This is a relationship field.

**Relationship Name**
Idea

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. If this value is `true`, your organization has the Ideas HTML editor enabled, and
the `CommentBody` field may contain HTML. If this value is `false`, the HTML editor is
disabled and the `CommentBody` field only contains regular text.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects IdeaReputation

**Field** **Field Type**

**Description**

Total number of up votes for the question.

Note: If you import these records, and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

Use this object to track comments on ideas, which are users' text responses to ideas.

SEE ALSO:

### Idea

Vote

### IdeaReputation

Represents a collection of statistics and scores derived from a user’s activity within an Ideas zone or internal organization. This object is
available in API version 28.0 and later.

Supported Calls

`query()`, `retrieve()`,

Fields

**Field** **Details**

```
CommentCount

CommentsReceivedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments a user has created in a zone or the internal organization. This
number excludes comments the user creates on his or her own idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects IdeaReputation

**Field** **Details**

**Description**
The number of comments a user has received in a zone or the internal organization.

```
ContextId

DownVotesGivenCount

DownVotesReceivedCount

IdeaCount

ReputationLevel

Score

```

**Type**
reference

**Properties**
Filter, Group, Namepointing, Nillable, Sort

**Description**
The ID of the zone or internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has given in a zone or the internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has received in a zone or the internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of ideas a user has created in a zone or the internal organization.

**Type**
string

**Properties**
Nillable

**Description**
The reputation level that a user has achieved based on their score in a zone or within an
organization.

**Type**
double


### Standard Objects IdeaReputationLevel

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total score of a user’s activity within a zone or within an organization.

```
UpVotesGivenCount

UpVotesReceivedCount

UserId

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes a user has given in a zone or the internal organization. This number
doesn’t include the default vote the system applies when the user creates the idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes a user has received in a zone or the internal organization.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID associated with the reputation.

Use to query a user’s reputation within a zone.

### IdeaReputationLevel

Represents a reputation level within an Ideas zone or internal organization and is used by the system to calculate reputation. You can
create up to 25 levels per zone or internal organization. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects IdeaTheme

Fields

**Field Name** **Details**

```
ContextId

Name

Threshold

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Namepointing, Sort, Update

**Description**

The ID of the zone or internal organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level. The name must be unique within the zone or
internal organization. Maximum size is 50 characters.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level. The threshold must be unique within
the zone or internal organization and must be greater than or equal to zero.

Use to create or edit reputation levels for an Ideas zone or internal organization.

### IdeaTheme

Represents an invitation to zone members to submit ideas that are focused on a specific topic. This object is available in API version 26
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`,


Standard Objects IdeaTheme

Fields

**Field Name** **Details**

```
Categories

CommunityId

CurrencyIsoCode

Description

EndDate

LastReferencedDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize ideas and idea themes into
logical groupings.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort,

**Description**
The zone ID associated with the idea theme.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Description of the idea theme.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date marking the end of the idea theme.

**Type**
date


### Standard Objects IdpEventLog

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

```
StartDate

Status

Title

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date that the idea theme begins.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Customizable picklist of values used to specify the status of the idea theme.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**

Title of the idea theme.

Use the object to track ideas that are submitted to an idea theme.

### IdpEventLog

Represents the Identity Provider Event Log. This log records both problems and successes with inbound SAML or OpenID Connect
authentication requests from another app provider. It also records outbound SAML responses when Salesforce is acting as an identity
provider. This object is available in API version 39.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects IdpEventLog

Fields

**Field** **Details**

```
AppId

AuthSessionId

ErrorCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the app provider seeking authentication.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the authentication session.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The error code for the authentication issue.

Possible values are:

**•** `AppAccessDenied` —Error: App access denied

**•** `AppBlocked` —Error: App blocked

**•** `ClientUnapproved` —Error: Invalid grant

**•** `CodeExpired` —Error: Expired authorization code

**•** `ForceAuthNLogout` —User logged out due to forced authentication request

**•** `InternalError` —Error: Internal Error

**•** `InvalidAuthnRequest` —Error: Unable to parse AuthnRequest from service
provider

**•** `InvalidClientCredentials` —Error: Invalid client credentials

**•** `InvalidCode` —Error: Invalid authorization code

**•** `InvalidDeviceId` —Error: Invalid device ID

**•** `InvalidIdpEndpoint` —Error: Invalid Identity Provider Endpoint URL

**•** `InvalidIssuer` —Error: Invalid Issuer

**•** `InvalidScope` —Error: Invalid scope(s)

**•** `InvalidSessionLevel` —Error: Invalid session level

**•** `InvalidSettings` —Error: IdP certificate is invalid or does not exist

**•** `InvalidSignature` —Error: Invalid Signature


Standard Objects IdpEventLog

**Field** **Details**

**•** `InvalidSp` —Error: Misconfigured or invalid service provider

**•** `InvalidSpokeSp` —Error: Invalid spoke SP settings

**•** `InvalidUserCredentials` —Error: Invalid user credentials

**•** `NoAccess` —Error: User does not have access to this service provider

**•** `NoCustomAttrValue` —Error: User does not have a value for the subject custom
attribute

**•** `NoCustomField` —Error: Custom field not found

**•** `NoSpokeId` —Error: No Spoke ID found

**•** `NoSubdomain` —Error: No My Domain deployed in the org

**•** `NoUserFedId` —Error: User does not have a Federation Identifier selected

**•** `OauthError` —OAuth Error

**•** `Success`

**•** `UnableToResolve` —Error: Unable to resolve request into a Service Provider

**•** `UnknownError` —Unknown Error

```
IdentityUsed

InitiatedBy

OptionsHasLogoutUrl

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The identity (username) of the user being authenticated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The code describing how the authentication request was initiated.

Possible values are:

**•** `IdP` —IdP-Initiated SAML

**•** `OauthAuthorize` —OAuth Authorization

**•** `OauthTokenExchange` —OAuth Token Exchange

**•** `SP` —SP-Initiated SAML

**Type**
boolean

**Properties**
Filter


### Standard Objects IframeWhiteListUrl

**Field** **Details**

**Description**
Whether a logout URL has been assigned to the app. This URL is where users are redirected
when they log out.

```
 SamlEntityUrl

 SsoType

 Timestamp

 UserId

### IframeWhiteListUrl

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The authentication URL of the SAML provider.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of SSO. Options are:

**•** 0–SAML

**•** 1–OpenID Connect

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time on which the event occurred.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user seeking authentication.

Represents a list of trusted external domains that you allow to frame your Embedded Service, Surveys, and Visualforce pages. This object
is available in API version 45.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.


### Standard Objects Image

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Context

Url

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of content in the iframe.

Valid values are:

**•** `Surveys`

**•** `VisualforcePages`

**•** `DisclosureAndComplianceHubConnector`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique domain that is allowed to frame your Visualforce pages, surveys, or
Disclosure and Compliance Hub Connector. Accepts these formats: example.com,
*example.com, and https://example.com.

To use this object for framing Visualforce pages, on Session Settings in Setup, select **Enable clickjack protection for customer**
**Visualforce pages** either **with headers disabled** or **with standard headers** . These options both allow framing of Visualforce pages
on trusted external domains and provide clickjack protection.

Alternatively, you can customize session settings via the SecuritySettings Metadata API type. To use the IframeWhiteListUrl object, set
either the `enableClickjackNonsetupUser` or `enableClickjackNonsetupUserHeaderless` field to `true` . For
[more information, see SecuritySettings in the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_securitysettings.htm)

### Image

Represents the details of an image. This object is available in API version 47.0 and later.


Standard Objects Image

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AlternateText

CapturedAngle

ContentDocumentId

ImageClass

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Accessibility text to explain the image in words.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Angle at which the image was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of the content document where image is stored.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The image category.


Standard Objects Image

**Field** **Details**

Possible values are:

**•** `FOOD`

**•** `LOGOS`

**•** `OBJECTS`

**•** `SCENES`

```
ImageClassObjectType

ImageViewType

IsActive

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of image. Used in Einstein Object Detection to identify whether the image is used
to detect objects or build a model.

Possible values are:

**•** `DETECTION` —Actual Image

**•** `FEEDBACK`

**•** `TRAINING`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Orientation of the image.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if an image is active. The default value is False. An active image can be used for
building or updating a model in Einstein Object Detection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the image was last referenced.


Standard Objects Image

**Field** **Details**

```
LastViewedDate

Name

OwnerId

Title

Url

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the image was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Unique identifier of the record owner.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the image.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Public URL of the image file.


### Standard Objects Incident Incident

An Incident is any unplanned business interruption that has wide-sweeping impacts and requires an urgent fix. This object contains the
details of the incident, documenting the history of the incident from registration to closure. This object is available in API version 53.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Category

Description

DetectedDateTime

EndDateTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was first detected.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident ended.


Standard Objects Incident

**Field** **Details**

```
Impact

IncidentNumber

IsMajorIncident

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The incident's impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated number for the incident.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the incident is business-critical. If set to `true`, the incident is widespread
and business-critical. The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last accessed this record, a list view, or
another related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Incident

**Field** **Details**

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

```
OwnerId

ParentIncidentId

Priority

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned to resolve the
incident.

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
The unique ID of an incident above one or more related incidents in an incident hierarchy.

This is a relationship field.

**Relationship Name**
ParentIncident

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the incident.

Possible values are:

**•** `Critical`


Standard Objects Incident

**Field** **Details**

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
PriorityOverrideReason

ReportedMethod

ResolutionDateTime

ResolutionSummary

ResolvedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why a priority should be changed or edited.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates how the incident was reported to customer service.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was resolved.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of possible steps to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the user who resolved the incident.

This is a relationship field.


Standard Objects Incident

**Field** **Details**

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

```
StartDateTime

Status

StatusCode

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident began.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages a customer may want to track.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Open`

**•** `Problem Created`

**•** `Resolved`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The incident's status.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `Open`


Standard Objects Incident

**Field** **Details**

**•** `ProblemCreated`

**•** `Resolved`

The default value is 'New'.

```
SubCategory

Subject

Type

Urgency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the incident.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident, for example, question or problem. Administrators set field values.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long the resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


### Standard Objects IncidentRelatedItem

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentChangeEvent on page 68**
Change events are available for the object.

**IncidentFeed on page 55**
Feed tracking is available for the object.

**IncidentHistory on page 63**
History is available for tracked fields of the object.

**IncidentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**IncidentShare on page 67**
Sharing is available for the object.

### IncidentRelatedItem

Represents a junction object that relates an Incident to an Asset or Product. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Asset ID that's linked to the Incident.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


Standard Objects IncidentRelatedItem

**Field** **Details**

```
Comment

ImpactLevel

ImpactType

IncidentId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the incident.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The effect of the related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Incident ID that's linked to the Asset.

This field is a relationship field.


Standard Objects IncidentRelatedItem

**Field** **Details**

**Relationship Name**
Incident

**Relationship Type**
Lookup

**Refers To**
Incident

```
Name

Product2Id

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident-related item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product (Product2) ID that's linked to the Incident..

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentRelatedItemChangeEvent on page 68**
Change events are available for the object.

**IncidentRelatedItemFeed on page 55**
Feed tracking is available for the object.

**IncidentRelatedItemHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects Individual Individual

Represents a customer’s data privacy and protection preferences. Data privacy records based on the Individual object store your customers’
preferences. Data privacy records are associated with related leads, contacts, person accounts, and users. This object is available in API
version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
BirthDate

CanStorePiiElsewhere

ChildrenCount

ConsumerCreditScore

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s birthdate.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indication that you can store the customer’s personally identifiable information
(PII) outside of their legislation area. For example, you could store an EU citizen’s
PII data in the US.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of children the customer has.

**Type**
int


Standard Objects Individual

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person's credit score (for example, 740).

```
ConsumerCreditScoreProviderName

ConvictionsCount

DeathDate

FirstName

HasOptedOutGeoTracking

HasOptedOutProcessing

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that provided the credit score.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of convictions for the customer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s death date.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s first name. Maximum size is 40 characters.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track geolocation on mobile devices.

**Type**
boolean


Standard Objects Individual

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process personal data, which can include collecting, storing,
and sharing personal data.

```
HasOptedOutProfiling

HasOptedOutSolicit

HasOptedOutTracking

HasPrivacyHold

IndividualsAge

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process data for predicting personal attributes, such as interests,
behavior, and location.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not solicit products and services.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track customer web activity and whether the customer opens
email sent through Salesforce.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates the Privacy Hold status.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer is considered to be a minor.


Standard Objects Individual

**Field Name** **Details**

```
InfluencerRating

IsHomeOwner

LastName

LastViewedDate

MasterRecordId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A measure of the person's influence, irrespective of how we do business with
them.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the customer owns a home.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The customer’s last name. Maximum size is 80 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the
record that was kept. If this object was deleted for any other reason, or hasn’t
been deleted, the value is `null` .

This is a relationship field.

**Relationship Name**
MasterRecord


Standard Objects Individual

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Individual

```
MilitaryService

Name

Occupation

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer has served in the military.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` . Maximum size is 203
characters, including whitespaces.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s occupation. Maximum size is 150 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects Individual

**Field Name** **Details**

```
Salutation

SendIndividualData

ShouldForget

Website

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title for addressing the customer, such as Dr. or Mrs.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to export personal data for delivery to the customer.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to delete records and personal data related to this customer.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the customer’s website.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IndividualChangeEvent (API version 47.0)**
Change events are available for the object.

**IndividualHistory**

History is available for tracked fields of the object.

**IndividualShare**

Sharing is available for the object.


### Standard Objects IndividualApplicationItem IndividualApplicationItem

Captures individual application input data that is used during run-time. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
IndividualApplicationId

Name

RelatedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Individual Application parent object associated with the Individual Application Item.

This field is a relationship field.

**Relationship Name**
### IndividualApplication

**Relationship Type**
Lookup

**Refers To**
### IndividualApplication

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the object related to the Individual Application.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects IndividualApplicationItem

**Field** **Details**

**Description**
The related object associated with the Individual Application Item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedItem

**Relationship Type**
Lookup

**Refers To**
Benefit, ProgramProduct

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the approval status of the Individual Application.

Possible values are:

**•** `Approved`

**•** `Declined`

**•** `In Progress`

**•** `Pending`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[IndividualApplicationItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[IndividualApplicationItemFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[IndividualApplicationItemHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[IndividualApplicationItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[IndividualApplicationItemShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects IndividualHistory IndividualHistory

Represents the history of changes to values in the fields of a data privacy record, based on the Individual object. This object is available
in versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.

Fields

**Field Name** **Details**

```
DataType

Field

IndividualId

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
The name of the changed field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the data privacy record. Label is **Individual ID** .

This is a relationship field.

**Relationship Name**
### Individual


### Standard Objects IndividualShare

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
### Individual

```
NewValue

OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

Use this object to identify changes to data privacy records.

This object respects field-level security on the parent object.

### IndividualShare

Represents a list of access levels to a data privacy record along with an explanation of the access level. For example, if you have access
to a record because you own it, the `IndividualAccessLevel` is `All` and `RowCause` is Owner. This object is available in API
version 42.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects IndividualShare

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.

Fields

**Field Name** **Details**

```
IndividualAccessLevel

IndividualId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the data privacy record. The possible
values include:

**•** `Read`

**•** `Edit`

**•** `All` (Except for create or update.)

Set this field to an access level that’s higher than your default access level for
individuals.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Individual associated with this sharing entry. This field isn’t available for
updates.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects InsufficientAccessEventLog

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited. Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the data privacy record with them.

**•** `Owner` —The User is the owner of the data privacy record.

**•** `Rule` —The User or Group has access to the data privacy record via an
Individual sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the data privacy record.
This field isn’t available for updates.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object lets you determine which users and groups can view or edit Individual records owned by other users.

### InsufficientAccessEventLog

Insufficient Access event logs contain details about errors relating to insufficient account, case, contact, and opportunity record access.
This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Note: The Insufficient Access event type is disabled by default. You can enable this event type for a period of 24 hours by contacting
Salesforce Customer Support.

These insufficient access error scenarios are logged:


Standard Objects InsufficientAccessEventLog

**•** The user can’t share a case, contact, or opportunity because the user doesn’t have permission to share the parent account or the
recipient of the share doesn’t currently have read access to the parent account.

**•** The user can’t change ownership of a case, contact, or opportunity because the user doesn’t have permission to share the parent
account or the new owner doesn’t currently have read access to the parent account.

**•** The user can’t change the parent account of a case, contact, or opportunity because the user doesn’t have permission to share the
new parent account or the owner of the case, contact, or opportunity doesn’t have read access to the new parent account.

Insufficient access errors resulting from bulk operations involving two or more records aren’t logged.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AccessError

ActualLoggedInUserIdentifier

ErrorDescription

```

**Type**
String

**Description**
The type of insufficient access error that the user received. Valid values are:

**•** `DATA_NOT_AVAILABLE` —The record is no longer accessible. For example, a record
was deleted and moved to the Recycle Bin.

**•** `INVALID_TYPE` —The record type doesn’t exist.

**•** `NO_ACCESS` —The user doesn’t have the required access level to complete the
attempted action on the record.

**Example**

```
  NO_ACCESS

```

**Type**
Id

**Description**
The ID of the user who initiated the action that caused the insufficient access error. For
example, a user attempts to transfer ownership of a record to a teammate, but the operation
fails because the teammate doesn’t have the required access.

**Example**

```
  005XXXXXXXXXXXX

```

**Type**
String


Standard Objects InsufficientAccessEventLog

**Field** **Details**

**Description**
Description of the insufficient access error that the user received.

**Example**
User 005XXXXXXXXXXXX doesn't have full access for the record 001XXXXXXXXXXXX.

```
ObjectType

RecordIdentifier

RequestIdentifier

RequestedAccessLevel

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object for which the user received the insufficient access error.

**Type**
String

**Description**
The ID of the record that the user doesn’t have access to.

**Example**

```
  001XXXXXXXXXXXX

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The access level required by the user’s attempted action on the record. Valid values are:

**•** `DELETE`

**•** `FULL`

**•** `READ`

**•** `TRANSFER`

**•** `WRITE`

**Example**

```
  FULL

```

**Type**
dateTime


### Standard Objects InternalOrganizationUnit

**Field** **Details**

**Description**
The access time of Salesforce services in GMT.

**Example**

```
                   20130715233322.670

```

```
UserIdentifier

```

**Type**
Id

**Description**
The ID of the user for whom the insufficient access error occurred, either when the user
couldn’t access a record, the user couldn’t complete an operation, or the user was the
intended recipient of a record transfer that failed because the user didn’t have the required
access.

**Example**

```
  005XXXXXXXXXXXX

```

### InternalOrganizationUnit

Represents an organization that an Employee belongs to. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you have either a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission, or the Employee Management and Employee User add-on licenses. This object is also
available with the Referral Marketing license.

Fields

**Field** **Details**

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects InternalOrganizationUnit

**Field** **Details**

**Description**
A description of the organization the Employee is working in.

```
LastReferencedDate

LastViewedDate

OrganizationCode

OrganizationName

OwnerId

ParentOrganizationId

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The code of the organization the Employee is working in.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the organization the Employee is working in.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
reference


### Standard Objects InventoryItemReservation

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the parent organization.

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the record is for an internal or an external organization. This field is available
in API version 60.0 and later.

Possible values are:

**•** `EXTERNAL_BUSINESS_UNIT`

**•** `INTERNAL_ORGANIZATION`

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**InternalOrganizationUnitHistory (API version 49.0)**
History is available for tracked fields of the object.

**InternalOrganizationUnitOwnerSharingRule**

Sharing rules are available for the object.

**InternalOrganizationUnitShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### InventoryItemReservation

Used to store inventory item reservation information for a specific product and location. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects InventoryItemReservation

Special Access Rules

This object is available only if a B2B Commerce, D2C Commerce, B2C Commerce or Salesforce Order Management license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

ErrorCode

ErrorMessage

InventoryItemReservationName

InventoryReservationId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the inventory items.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the reservation isn’t successful.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
If an error occurred, this field contains the error message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the inventory item reservation (autogenerated, for example: PIR-0033).

**Type**
reference


Standard Objects InventoryItemReservation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the inventory reservation.

This field is a relationship field.

**Relationship Name**
InventoryReservation

**Relationship Type**
Lookup

**Refers To**
InventoryReservation

```
ItemReservationSourceId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity associated with the inventory item reservation.

This field is a relationship field.

**Relationship Name**
ItemReservationSource

**Relationship Type**
Lookup

**Refers To**
CartItem

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


Standard Objects InventoryItemReservation

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
ProductId

Quantity

ReservedAtLocationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the product on the inventory item reservation. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Number of products on the inventory item reservation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location or location group where the inventory item reservation originated.

This field is a polymorphic relationship field.

**Relationship Name**
ReservedAtLocation

**Relationship Type**
Lookup

**Refers To**
Location, LocationGroup


### Standard Objects InventoryReservation

**Field** **Details**

```
StockKeepingUnit

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the reserved item.

### InventoryReservation

Stores information about the status of cart inventory reservations in B2B and D2C Commerce. This object is available in API version 60.0
and later.

This object only applies to cart inventory reservation APIs in B2B and D2C Commerce. It isn't related to inventory reservation Connect
APIs used with Omnichannel Inventory and Order Management.

If your org is using Omnichannel Inventory as its inventory system, the inventory reservation record related to the cart also represents a
reservation in Omnichannel Inventory. If the org uses a different inventory system, the inventory reservation record related to the cart
represents a reservation in that inventory system.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if a B2B Commerce, D2C Commerce, B2C Commerce, or Salesforce Order Management license is enabled.

Fields

**Field** **Details**

```
ErrorCode

ErrorMessage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the reservation isn’t successful.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects InventoryReservation

**Field** **Details**

**Description**
If an error occurred, this field contains the error message.

```
InventoryReservationName

IsAsyncOperationInProgress

IsSuccess

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the inventory reservation (autogenerated, for example: PIR-0033).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if there’s an async operation in progress that could affect the reservation.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the most recent inventory system operation was successful.

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


Standard Objects InventoryReservation

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user could have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
OwnerId

ReservationDate

ReservationDurationInSeconds

ReservationIdentifier

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the inventory reservation.

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
Create, Filter, Sort, Update

**Description**
The timestamp when the inventory reservation was created.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total duration of the inventory reservation in seconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier (text value) for the reservation.


### Standard Objects InvocableActionEventLog

**Field** **Details**

```
ReservationSourceId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity associated with the inventory reservation.

This field is a polymorphic relationship field.

**Relationship Name**
ReservationSource

**Relationship Type**
Lookup

**Refers To**
Export_FOI__c, WebCart

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**InventoryReservationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InventoryReservationShare on page 67**
Sharing is available for the object.

### InvocableActionEventLog

Invocable Action events capture the calls to Salesforce Invocable Actions.This is particularly useful to monitor actions invoked during
Agentforce flows. This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects InvocableActionEventLog

Fields

**Field** **Details**

```
ActionName

ActionType

ActionVersion

ApiCaller

BotIdentifier

BotSessionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
InvocableActionType being referenced.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The invocable action version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the API caller. This is only populated when the action is invoked from a REST API
call

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


Standard Objects InvocableActionEventLog

**Field** **Details**

**Description**
The bot session ID.

```
Duration

FlowProcessType

FlowVersionIdentifier

PlannerIdentifier

RequestCount

RequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Time (in nanos) taken to process this set of requests.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The process type of the calling flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the version of the calling flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of invoked requests.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Invoice

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
Timestamp

UserIdentifier

### Invoice

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user employing salesforce.com services, whether through the user interface or API.

Represents a financial document describing the total amount a buyer must pay for goods or services provided. This object is available
in API version 48.0 and later.

Users can edit non-posted invoices. Posted invoices can’t be deleted. After an invoice is posted, users can make payments against it to
reduce its balance.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Salesforce Order Management or D2C Commerce license, and Billing (Revenue Cloud). A few fields require
Commerce Subscriptions to be enabled. These fields are available only in Lightning Experience.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoice.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoice.htm)


Standard Objects Invoice

Fields

**Field** **Details**

```
Balance

BillToContactId

BillingAccountId

CurrencyIsoCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The customer account for this invoice.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist


Standard Objects Invoice

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The three-letter ISO 4217 currency code associated with the invoice.

The default value is `USD` .

This field is available in API version 55.0 and later.

```
DaysInvoiceOpen

DaysInvoiceOverdue

Description

DocumentNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the invoice was created before it was paid.

This field is a calculated field.

This field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the date when payment was due.

This field is a calculated field.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Users can add more information about this invoice. Maximum of 1,000 characters.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-generated number that is used to organize financial documents. The number
can be sequential or random.


Standard Objects Invoice

**Field** **Details**

```
DueDate

FullSettlementDate

InvoiceBatchRunId

InvoiceDate

```

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the invoice is paid in full.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Id of the invoice batch run that generated this invoice.

This field is a relationship field.

This field is available in API version 55.0 and later.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate` . For example, an invoice with an `InvoiceDate` of 04/01 and Net 30 payment
terms has a `DueDate` of 05/01.


Standard Objects Invoice

**Field** **Details**

```
InvoiceNumber

LastReferencedDate

LastViewedDate

NetCreditsApplied

NetPaymentsApplied

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
System-created unique ID for this invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

This field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. If this value is null, it's possible the user accessed this record or list view
( `LastReferencedDate` ) but didn't view it.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Represents the net credits applied to an invoice. Calculated by subtracting the sum of all
unapplied lines from the sum of all applied lines.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
Represents net payments applied to an invoice. Calculated by subtracting the sum of
unapplied payments from the sum of payments applied to the invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

```
OwnerId

PaymentExclusionReason

PaymentTermId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns an invoice record.

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
The reason for skipping creation of payment schedules and payment schedule items for the
invoice. This field is only available if Commerce Subscriptions is enabled for your org. Available
in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment term used on this invoice.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm


Standard Objects Invoice

**Field** **Details**

```
PostedDate

ReferenceEntityId

SettlementStatus

ShouldExcludePayment

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the invoice was posted.

This field is available in API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the order or order summary that created this invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Order, OrderSummary

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the invoice's payment.

Possible values are:

**•** `Not Applicable`

**•** `Not Settled`

**•** `Partially Settled`

**•** `Settled`

This field is available when Subscription Management is enabled.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
Required. Indicates whether to skip creating payment schedules and payment schedule
items for the invoice ( `true` ) or not ( `false` ). The default value is `false` . This field is only
available if Commerce Subscriptions is enabled for your org. Available in API Version 63.0
and later.

```
Status

TaxLocaleType

TotalAdjustmentAmount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice.

Possible values are:

**•** `Canceled`  - Indicates that the invoice was generated and later canceled.

**•** `Draft`  - Indicates that the invoice is a draft. Available in API version 60.0 and later.

**•** `Draft In Progress`  - Indicates that the draft invoice is in progress. Available in
API version 60.0 and later.

**•** `Error`  - Indicates that an error occurred when processing the invoice.

**•** `Pending`  - Indicates that the invoice is being processed.

**•** `Posted`  - Indicates that the invoice has been generated and sent to the customer.

**•** `Posting In Progress` —Indicates that the invoice posting is in progress. Available
in API version 60.0 and later.

**•** `Void In Progress`  - Indicates that the invoice is pending a status change.

**•** `Voided`  - The invoice’s status after the API successfully voids the invoice.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The system used to handle tax on the original Order associated with the Invoice. Gross usually
applies to taxes like value-added tax (VAT), and Net usually applies to taxes like sales tax. This
field is available when Order Management or B2B Commerce is enabled.

Possible values are:

**•** Gross: Displays most prices and taxes as combined values

**•** Net: Displays most prices and taxes as separate values

This field is available in API version 56.0 and later.

**Type**
currency


Standard Objects Invoice

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice’s adjustment line amounts.

```
TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

TotalAmount

TotalAmountWithTax

TotalChargeAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's adjustment-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the invoice line's adjustment lines.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` values on the invoice’s lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalAmountWithTax` values on the invoice’s lines.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
The sum of the invoice’s charges.

This field is a calculated field.

```
TotalChargeAmountWithTax

TotalChargeTaxAmount

TotalConvertedNegAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's charge-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the invoice's charge lines.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all negative invoice lines that were converted to a credit memo. For example, if
one negative invoice line was for -$10 and one was for -$15, the total amount that’s converted
to a credit memo is -$25.

This field is a calculated field.

This field is available when Subscription Management is enabled.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TaxAmount` values on the invoice lines.

This field is a calculated field.


### Standard Objects InvoiceAddressGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceFeed on page 55**
Feed tracking is available for the object.

**InvoiceHistory on page 63**
History is available for tracked fields of the object.

**InvoiceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceShare on page 67**
Sharing is available for the object.

### InvoiceAddressGroup

Stores the buyer's address information. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceaddressgroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceaddressgroup.htm)

Fields

**Field** **Details**

```
Address

City

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer's address. Compound field that summarizes the invoice address group's address
component fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceAddressGroup

**Field** **Details**

**Description**
The buyer's city.

```
Country

GeocodeAccuracy

InvoiceAddressGroupNumber

InvoiceId

Latitude

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's country.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. The accuracy rating contains
information about the location of a latitude and longitude.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as DOC-000001.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice associated with the address group.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
double


Standard Objects InvoiceAddressGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's latitude.

```
Longitude

PostalCode

State

Street

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's longitude.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's postal code or ZIP code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's street.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceAddressGroupHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects InvoiceBatchRun InvoiceBatchRun

Represents a batch processing job in Subscription Management or Billing (Revenue Cloud). During an invoice batch run, all billing
schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version
55.0 and later.

An invoice batch run, controlled by a scheduler, tells the system to start the run at a scheduled date and time. The scheduler also includes
matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are included for
processing in the invoice batch run.

When an invoice batch run is started, Subscription Management or Billing (Revenue Cloud):

**•** Evaluates the billing schedule to see if it meets the criteria for inclusion in the batch invoice run.

**•** Generates an invoice record with a pending state.

**•** Makes calls to an external tax provider.

**•** Adds the tax to the invoice.

**•** Summarizes information about the billing schedules that were included in the invoice batch run and displays this information in
the Invoice Batch Run record.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrun.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrun.htm)

Fields

**Field** **Details**

```
BillingBatchSchedulerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related billing batch scheduler.

This field is a relationship field.

**Relationship Name**
BillingBatchScheduler

**Relationship Type**
Lookup


Standard Objects InvoiceBatchRun

**Field** **Details**

**Refers To**
BillingBatchScheduler

```
Comments

CompletionTime

InvoiceBatchRunNumber

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the invoice batch run finished processing.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last modified. Its UI label is Last Modified
Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last viewed.

**Type**
reference


Standard Objects InvoiceBatchRun

**Field** **Details**

**Properties**
Filter, Group, Sort, Update

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is Owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RecoveryStatus

StartTime

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the state of the invoice batch run recovery process. This field is available in API
version 56.0 and later.

Possible values are:

**•** `CompletelyRecovered` —All billing schedules included in the recovery run were
reset to _`Ready for Invoicing`_ . These billing schedules are included in the next
scheduled invoice batch run.

**•** `PartiallyRecovered` —Some, but not all, billing schedules that were part of the
recovery run were reset to _`Ready for Invoicing`_ . The billing schedules that
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to _`Ready for`_
_`Invoicing`_ so they can be processed.

**•** `RecoveryFailed` —The recovery job was unsuccessful. This value is available in API
version 57.0 and later.

**•** `RecoveryStarted` —The recovery job is in process.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Timestamp when the invoice batch run started processing.

**Type**
picklist


Standard Objects InvoiceBatchRun

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice batch run.

Possible values are:

**•** `Canceled` —This value is available in API version 57.0 and later.

**•** `Completed`

**•** `Failed`

**•** `Started`

**•** `Stopped` —This value is available in API version 57.0 and later.

The default value is `Started` .

```
TotalBillSchedRecovered

TotalBillSchedUnrecovered

TotalBillingSchedulesFailed

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that were reset to _`Ready`_
_`for Invoicing`_ . These billing schedules are included in the next scheduled invoice
batch run.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that weren't reset to
_`Ready for Invoicing`_ . These billing schedules that weren’t successfully recovered
must be manually reset to _`Ready for Invoicing`_ so they can be processed.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that weren’t successfully processed. When a billing
schedule isn’t successfully processed, then the system doesn’t generate an invoice for it. For
details about errors, check the Revenue Transaction Error Log. This field is available in API
version 56.0 and later.


Standard Objects InvoiceBatchRun

**Field** **Details**

```
TotalBsSuccessfullyProcessed

TotalDraftInvoiceAmount

TotalDraftInvoices

TotalFilteredBillingSchedules

TotalInvSuccessfullyProcessed

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules for which the system was able to generate and process
invoices. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice amounts for invoices in `Draft` status.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices in `Draft` status generated in the batch run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that met the invoice run scheduler’s matching criteria.
The matching criteria specify which billing schedules are included in the invoice batch run.
Its field label is Total Matching Billing Schedules. This field is available in API version 56.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceBatchRun

**Field** **Details**

**Description**
The total number of invoices that were successfully processed.

When Billing (Revenue Cloud) is enabled, the field's value is either the same as
`TotalPostedInvoices` or `TotalDraftInvoices` based on the Invoice Status
selected when the Invoice Scheduler is set up.

This field is available in API version 56.0 and later.

```
TotalInvoicedAmount

TotalInvoicesCanceled

TotalInvoicesFailed

TotalInvoicesGenerated

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of income including taxes represented by the successfully processed
invoices. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren't processed. To find out what went wrong, check
the Revenue Transaction Error Log. Fix the errors, then run the invoice batch run recovery
process.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren’t processed successfully. To find out what went
wrong, check the Revenue Transaction Error Log. Then fix the errors and run the invoice
batch run recovery process. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that were generated from the billing schedules processed by
the invoice batch run. This field is available in API version 56.0 and later.


### Standard Objects InvoiceBatchRunCriteria

**Field** **Details**

```
TotalPostedInvoices

TotBillSchdUpdtDurDrftToPost

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices in `Posted` status generated during the batch run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total billing schedules updated during the draft to posted run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceBatchRunChangeEvent on page 68**
Change events are available for the object.

**InvoiceBatchRunFeed on page 55**
Feed tracking is available for the object.

**InvoiceBatchRunHistory on page 63**
History is available for tracked fields of the object.

**InvoiceBatchRunOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceBatchRunShare on page 67**
Sharing is available for the object.

### InvoiceBatchRunCriteria

Represents a batch processing job and its required criteria in Subscription Management. During an invoice batch run, all billing schedules
that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version 55.0 and later.

A scheduled invoice batch run tells the system to start the run at a scheduled date and time by using certain criteria. The scheduler
includes the matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are
included for processing in the invoice batch run.


Standard Objects InvoiceBatchRunCriteria

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchruncriteria.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchruncriteria.htm)

Fields

**Field** **Details**

```
Comments

CriteriaExpression

CriteriaMatchType

ExpectedInvoiceStatus

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined information about the batch run criteria.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The formula that specifies criteria for filtering the billing schedules. For example, we can filter
billing schedules by currency code.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of matching criteria required for the batch.

Valid value is `MatchAll` .

The default value is `MatchAll` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects InvoiceBatchRunRecovery

**Field** **Details**

**Description**
The type of invoice a batch run generates.

Valid values are:

**•** `Draft`

**•** `Posted`

This field is available in API version 60.0 and later.

```
InvoiceBatchRunCriteriaNumber

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is `Owner` .

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

### InvoiceBatchRunRecovery

Provides information about an invoice batch run recovery procedure. This object is available in API version 57.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).


Standard Objects InvoiceBatchRunRecovery

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrunrecovery.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrunrecovery.htm)

Fields

**Field** **Details**

```
Comments

CompletionTime

InvoiceBatchRunId

InvoiceBatchRunRecoveryNumber

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run recovery procedure was completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique identifier of the invoice batch run related to this recovery run.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique identifier of the invoice batch run recovery process.


Standard Objects InvoiceBatchRunRecovery

**Field** **Details**

```
LastReferencedDate

LastViewedDate

StartTime

Status

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
it’s possible that the user indirectly accessed this record ( `LastReferencedDate` ), but
did not view it.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The timestamp when the invoice batch run recovery started.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The final state of the invoice batch run recovery process.

Possible values are:

**•** `Completed` —The recovery run successfully reset all billing schedules to _`Ready for`_
_`Invoicing`_ .

**•** `CompletedWithErrors` —Some, but not all, billing schedules included in the
recovery run were reset to _`Ready for Invoicing`_ . The billing schedules that
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to _`Ready for`_
_`Invoicing`_ so they can be processed.

**•** `Failed` —The recovery run was unable to complete the reset process.

**•** `Started` —Indicates that the recovery run reset process began, is ongoing, and has
not yet produced a result.

The default value is `Started` .


### Standard Objects InvoiceDocument

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceBatchRunRecoveryChangeEvent on page 68**
Change events are available for the object.

**InvoiceBatchRunRecoveryFeed on page 55**
Feed tracking is available for the object.

**InvoiceBatchRunRecoveryHistory on page 63**
History is available for tracked fields of the object.

**InvoiceBatchRunRecoveryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceBatchRunRecoveryShare on page 67**
Sharing is available for the object.

### InvoiceDocument

Tracks and displays the status of documents generated for invoices. Invoice documents are available in the related lists of invoice entity
records. This object is available in API version 61.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

This object is available with Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicedocument.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicedocument.htm)

Fields

**Field** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the generated PDF document.

This field is a relationship field.

**Relationship Name**
ContentDocument


Standard Objects InvoiceDocument

**Field** **Details**

**Refers To**
ContentDocument

```
DateGenerated

DocumentGenerationProcessId

DocumentNumber

ErrorMessage

InvoiceId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date on which the PDF is generated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the entity that contains the information used to create the PDF invoice.

This field is a relationship field.

**Relationship Name**
DocumentGenerationProcess

**Refers To**
DocumentGenerationProcess

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the generated document.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Errors that occur during PDF generation.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects InvoiceLine

**Field** **Details**

**Description**
The ID of the invoice entity to which the invoice document is attached.

This field is a relationship field.

**Relationship Name**
### Invoice

**Relationship Type**
Master-detail

**Refers To**
Invoice (the master object)

```
Status

### InvoiceLine

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the PDF generation process.

Possible values are:

**•** `Blocked`

**•** `Cancelled`

**•** `Failure`

**•** `Pending`

**•** `Success`

Represents the amount that a buyer must pay for a product, service, or fee. Invoice lines are created based on the amount of an order
line. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceline.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceline.htm)


Standard Objects InvoiceLine

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentAmountWithTax

AdjustmentTaxAmount

Balance

BillingAddressId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustments made to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustment amounts, including associated taxes related to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of tax adjustments to the invoice line.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for an invoice line. This is equal to the invoice’s total amount with
tax after deducting the payments made.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field to an InvoiceAddressGroup containing the billing address for the invoice line.
Assign one InvoiceAddressGroup to the invoiceLine's BillingAddressID, and another
InvoiceAddressGroup to the invoiceLine's ShippingAddressId.

This field is a relationship field. This field is available in API version 55.0 and later.


Standard Objects InvoiceLine

**Field** **Details**

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup

```
BillingScheduleGroupId

BillingScheduleId

ChargeAmount

ChargeAmountWithTax

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Refers To**
BillingScheduleGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the billing schedule for the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Sum of charges made to the invoice line.

**Type**
currency


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Amount on a charge invoice line, including tax.

This field is available in API version 55.0 and later.

```
ChargeTaxAmount

ConvertedNegAmount

Description

GroupReferenceEntityItemId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax to be applied on a charge invoice line.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount from an invoice line that is converted to credit.

This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the invoice line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Grouping field for adjustment line items.

This field is a polymorphic relationship field.

**Relationship Name**
GroupReferenceEntityItem

**Relationship Type**
Lookup


Standard Objects InvoiceLine

**Field** **Details**

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

```
HasMultipleItems

InvoiceId

InvoiceLineEndDate

InvoiceLineStartDate

InvoiceStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this field merges items from the same billing period.

The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The invoice that contains this invoice line.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the end date of the billing for the service.

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the first date of the billing for the service.

**Type**
string


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the invoice line. Inherited from the invoice’s status.

```
LegalEntityAccountingPeriodId

LegalEntityId

LineAmount

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntityAccountingPeriod

**Refers To**
LegalEntyAccountingPeriod

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the invoice line.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the invoice line.


Standard Objects InvoiceLine

**Field** **Details**

```
NetCreditsApplied

NetPaymentsApplied

Product2Id

Quantity

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total credit memo line amount applied to the invoice line. This amount is calculated by
subtracting the unapplied credit memo line amount from the applied credit memo line
amount.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total payment applied to the invoice line. This amount is calculated by subtracting the
unapplied payment amount from the applied payment amount.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The product that was charged or ordered to create the invoice line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Number of units of the order product that created the invoice line.


Standard Objects InvoiceLine

**Field** **Details**

```
ReferenceEntityItemId

ReferenceEntityItemType

ReferenceEntityItemTypeCode

RelatedLineId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order item or adjustment item that created the invoice line.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of transaction that created the invoice line.

Possible values are:

**•** `DeliveryCharge` —Charge

**•** `Fee` —Charge. This value is available in API version 56.0 and later.

**•** `OrderProduct` —Product

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that created the invoice line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects InvoiceLine

**Field** **Details**

**Description**
The original invoice line that was adjusted or taxed.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

```
ShippingAddressId

TaxAmount

TaxCode

TaxDocumentNumber

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address associated with the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
ShippingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate tax rate for the invoice line.

**Type**
string


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the latest record in the external tax engine in which this invoice line item is
included.

This field is available in API version 55.0 and later.

```
TaxEffectiveDate

TaxName

TaxRate

TaxTransactionNumber

TaxTreatmentId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the invoice line’s `TaxAmount` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for the applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update

**Description**
Percentage value used for calculating tax.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the transaction in the external tax engine in which the taxes for the line were
calculated for the invoice line.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceLine

**Field** **Details**

**Description**
The tax treatment used on this invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

```
 Type

 UnitPrice

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of transaction for the invoice line.

Possible values are:

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Price for one unit of the item on the invoice line.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceLineFeed on page 55**
Feed tracking is available for the object.

**InvoiceLineHistory on page 63**
History is available for tracked fields of the object.

**InvoiceLineOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceLineShare on page 67**
Sharing is available for the object.


### Standard Objects JobProfile JobProfile

Represents a job profile used for shift scheduling. This object is available in API versions 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field** **Details**

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
The date and time when the current user last viewed a related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the job profile.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects JobProfileQueueGroup

**Field** **Details**

**Description**
The ID of the owner of the job profile.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**JobProfileFeed**

Feed tracking is available for the object.

**JobProfileHistory**

History is available for tracked fields of the object.

**JobProfileOwnerSharingRule**

Sharing rules are available for the object.

**JobProfileShare**

Sharing is available for the object.

### JobProfileQueueGroup JobProfileQueueGroup defines the mapping between Queue and JobProfile and configurations for capacity plans in Workforce Engagement.

This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Org must have the Workforce Engagement, Workforce Engagement Configuration, and Omni org preferences enabled. User must have
the Workforce Engagement Analyst or Planner user permission set.

Fields

**Field** **Details**

```
AnswerTime

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The answer time (in seconds) for a specific group.


Standard Objects JobProfileQueueGroup

**Field** **Details**

```
CapacityPerJobProfile

GroupCapacity

GroupId

JobProfileId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The max number of work units that an agent can handle for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distributed number of work units among groups to which a specific job profile is
associated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the group or queue record.

This is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the job profile record.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup


### Standard Objects Knowledge__Feed

**Field** **Details**

**Refers To**
JobProfile

```
JobProfileShrinkage

Priority

ServiceLevelAgreementPerc

WorkType

### Knowledge__Feed

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The shrinkage for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority of a group per job profile.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The expected SLA percentage for a specific group.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A type of group, indicating whether a queue is synchronous or asynchronous.

Possible values are:

**•** `A` —Async

**•** `S` —Sync

The default value is 'S'.

Represents the feed for a knowledge article. This object is available in API version 39.0 and later.

For additional information about feeds, see FeedItem on page 2549.


Standard Objects Knowledge__Feed

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Lightning Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
BestCommentId

Body

CommentCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

**Type**
textarea

**Properties**
Nillable, Sort

**Description**
The body of the feed item. Required when `Type` is `TextPost` or `AdvancedTextPost` .
Optional when `Type` is `ContentPost` or `LinkPost` .

Although a value for `Body` is not required for the `ContentPost` type, an attachment
is required. If an attachment isn’t present, the type changes to `TextPost` or
`AdvancedTextPost`, depending on the API version. `TextPost` and
`AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the body of
rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.


Standard Objects Knowledge__Feed

**Field** **Details**

Tip: In a feed that supports pre-moderation, `CommentCount` isn’t updated until a
comment is published. For example, say that you comment on a post that already has
one published comment and your comment triggers moderation. Now there are two
comments on the post, but the count says there's only one. In a moderated feed,
comments aren’t counted until approved by an admin or someone with Can Approve
Feed Post and Comment or Modify All Data.

Feed moderation has implications on how you retrieve feed comments. In a moderated
feed, rather than retrieving comments by looping through `CommentCount`, go through
pagination until the end of comments is returned.

```
InsertedById

IsRichText

```

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text feed comment
using SOAP API, set `IsRichText` to `true` and escape HTML entities from the body.
Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`


Standard Objects Knowledge__Feed

**Field** **Details**

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a plain-text
representation.

```
LikeCount

LinkUrl

ParentId

RelatedRecordId

Title

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Nillable, Sort

**Description**
The URL of a `LinkPost` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Knowledge article to which the feed item is related.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC thanks posts,
it’s the ID of the WorkThanks object associated with a `RypplePost` . This field is typically
null for all posts except `ContentPost` and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed with `Type`
set to `ContentPost` .

**Type**
string


Standard Objects Knowledge__Feed

**Field** **Details**

**Properties**
Group, Nillable, Sort

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is the URL and
this field is the link name. The `Title` field can be updated on posts of `Type`
`QuestionPost` .

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`, and `TextPost`, don’t
create feed items of other types directly from the API.

**•** `ActivityEvent` —indirectly generated event when a user or the API adds a Task
associated with a feed-enabled parent record (excluding email tasks on cases). Also
occurs when a user or the API adds or updates a Task or Event associated with a case
record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the series only.
For a recurring Task with CaseFeed enabled, events are generated for the series and each
occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement and, in
Lightning Experience as of API version 39.0 and later, when a user shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric or gauge
exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a dashboard
snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.


### Standard Objects Knowledge__ka

**Field** **Details**

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post. Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply only to
CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through the user
interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment for a case
object.

**•** `ChangeStatusPost` —generated event when a user changes the status of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved to a case.

**•** `EmailMessageEvent` —generated event when an email related to a case object is
sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or reaches
violation status.

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData` and
`ContentFileName` .

### Knowledge__ka

Provides access to the concrete object that represents a Knowledge article, the parent object for article versions. This object is available
in API version 39.0 and later.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticle on page 3032.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.


Standard Objects Knowledge__ka

Fields

**Field** **Details**

```
ArchivedById

ArchivedDate

ArticleNumber

CaseAssociationCount

FirstPublishedDate

LastPublishedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was archived.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of cases attached to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Knowledge__ka

**Field** **Details**

**Description**
The date when the article was last published.

```
LastReferencedDate

LastViewedDate

MasterLanguage

MigratedToFromArticle

TotalViewCount

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
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports multiple
languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article. Contains values only in orgs that
migrate from Knowledge in Salesforce Classic to Lightning Knowledge. This field is available
in API version 45.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Knowledge__kav

**Field** **Details**

**Description**
Total number of views for this article. This field is available in API version 39.0 and later.

### Knowledge__kav

Provides access to the concrete object that represents a Knowledge article version. This object is available in API version 39.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticleVersion on page 3044.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

This object doesn’t retrieve `<ActionOverrides>` .

Special Access Rules

Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.

Fields

**Field** **Details**

```
ArchivedById

ArchivedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article version was archived.


Standard Objects Knowledge__kav

**Field** **Details**

```
ArticleArchivedById

ArticleArchivedDate

ArticleCaseAttachCount

ArticleCreatedById

ArticleCreatedDate

ArticleMasterLanguage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was archived.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cases where this article is attached.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who created the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects Knowledge__kav

**Field** **Details**

**Description**
The article's original language. Only accessible if your knowledge base supports multiple
languages.

```
ArticleNumber

ArticleTotalViewCount

AssignedById

AssignedToId

AssignmentDate

AssignmentDueDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for the article.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who assigned the article.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user assigned to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was assigned to a user.

**Type**
dateTime


Standard Objects Knowledge__kav

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The due date when an article is assigned.

```
AssignmentNote

ExternalRef

ExternalSourceId

ExternalUrl

FirstPublishedDate

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Notes to the assignee from the user who assigned the article.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the item being referenced on the external system. For example, the ID of a document
on a Google Drive or a page on Confluence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference to the external Knowledge data source object.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL of the knowledge content referenced in an external system. For example, the ID of
a document in Google Drive or a page in Confluence.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.


Standard Objects Knowledge__kav

**Field** **Details**

```
IsExternalData

IsLatestVersion

IsMasterLanguage

IsOutOfDate

IsVisibleInApp

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the data is external to the customer’s knowledge base ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article is the most current version. ( `true` ) or not ( `false` ). This field
can be `true` on the online or published version, a draft version in the primary language, a
draft version in a translation, and the latest archived version. However, you can’t filter by
(PublishState=’Online’) and (IsLatestVersion=false) because the online version is also the
latest version. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article has one or more translations associated with it ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the source article has been updated since this translated version was
created ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Articles tab ( `true` ) or not ( `false` ).


Standard Objects Knowledge__kav

**Field** **Details**

```
IsVisibleInCsp

IsVisibleInPkb

IsVisibleInPrm

KnowledgeArticleId

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the Customer Portal ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the public knowledge base ( `true` ) or
not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the partner portal ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article independent from its version. The value for this field is retrieved from
the `Id` field of the KnowledgeArticle object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
`(Traditional)` .

Querying or searching articles in SOSL require that you specify the `Language` field in the
WHERE clause. The language must be the same for all article types.


Standard Objects Knowledge__kav

**Field** **Details**

Before API version 47.0, you must include the `Language` field to filter queries on Knowledge
article versions. In API version 47.0 and later, you can filter queries on Knowledge article
versions with or without `Language` depending on what you are querying.

```
LastPublishedDate

MasterVersionId

MigratedToFromArticleVersion

NextReviewDate

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source article, if the article is the translation of a source article. Only accessible if
your knowledge base supports multiple languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article version. Contains values only in
orgs that migrate from Classic to Lightning Knowledge. Available in API version 43.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article must next be reviewed for accuracy. Available in API version 58.0
and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article's owner.


Standard Objects Knowledge__kav

**Field** **Details**

```
PublishStatus

RecordTypeId

SourceId

Summary

Title

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The publication status for the article:

**•** `Draft` : any draft articles.

**•** `Online` : articles published in Salesforce Knowledge.

**•** `Archived` : archived articles.

A user must have the “Manage Articles” permission enabled to use `Online` .

Article queries and searches in SOQL or SOSL require that you specify either the
`PublishStatus` or the `Id` field in the WHERE clause. You can search for only one
publication status per article type in a single SOSL query. When searching for articles with a
`PublishStatus` of `Archived`, also check that `IsLatestVersion` equals `false`
in your WHERE clause.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the API Name that describes the type of article. Use the record type to determine
the article structure and other settings for different types of content.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source from which the article was created (Case or Reply). This field is only accessible
from the API and isn’t visible in the Salesforce UI.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Summary of the article. Maximum size is 1000 characters.

**Type**
string


Standard Objects Knowledge__kav

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Article's title. Maximum size is 255 characters.

```
TranslationCompletedDate

TranslationExportedDate

TranslationImportedDate

UrlName

ValidationStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last translated. Only accessible if your knowledge base
supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last exported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last imported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Represents the article's URL. Can contain alphanumeric characters and hyphens
but can't begin or end with a hyphen. Use a unique value regardless of context. (For example,
a unique value allows you to get expected results when running an Apex test with
`SeeAllData` set to `false` .) `UrlName` is case-sensitive and its maximum size is 255
characters.

**Type**
picklist


### Standard Objects Knowledge__DataCategorySelection

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group

**Description**

Shows whether the content of the article has been validated. Possible values are
`Validated` and `Not Validated` . The default value is `Not Validated` . This field
is available in API version 24.0 or later.

```
VersionNumber

```

**Type**
int

**Properties**
Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.

### Knowledge__DataCategorySelection

Represents a data category that classifies an article. This object is available in API version 39.0 and later.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Lightning Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
DataCategoryGroupName

```

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category group which has categories associated with the article.


### Standard Objects KnowledgeableUser

**Field** **Details**

```
 DataCategoryName

 ParentId

```

Usage

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the article associated with the data category selection.

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use this object to query and manage article categorization in your organization. Client applications can create
a categorization for an article with a Draft status. They can also delete and query article categorizations.

Note: When using this object to classify an article, you can't select both a category (for example USA) and one of its descendants
(California) or ascendant categories (North America). In this case, only the first category is selected.

### KnowledgeableUser

Represents a user identified as knowledgeable about a specific topic, and ranks them relative to other knowledgeable users. This object
is available in API version 31.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
NetworkId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects KnowledgeArticle

**Field Name** **Details**

**Description**
ID of the Experience Cloud site the topic exists in. This field is available only if
digigal experiences is enabled for your org.

```
RawRank

TopicId

UserId

### KnowledgeArticle

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank of this user’s knowledge on the topic relative to other users.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the topic in Salesforce.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the user in Salesforce.

Provides read-only access to an article and the ability to delete the primary article. This object is available in API version 19.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Unlike KnowledgeArticleVersion, the ID of a KnowledgeArticle record is identical irrespective of the article's version (status).

Knowledge__ka on page 3018 is derived from this object.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects KnowledgeArticle

Special Access Rules

Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license.

Fields

**Field Name** **Details**

```
ArchivedById

ArchivedDate

ArticleNumber

CaseAssociationCount

FirstPublishedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was archived.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't
change the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of cases attached to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.


Standard Objects KnowledgeArticle

**Field Name** **Details**

```
IsGeneratedByLlm

LastPublishedDate

LastReferencedDate

LastViewedDate

MasterLanguage

MigratedToFromArticle

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the first version of an article was created with an LLM. This object is available
in API version 59.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value
is null, the user has not viewed this record or list view, though they might have
accessed it ( `LastReferencedDate` )

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports
multiple languages.

**Type**
string


### Standard Objects KnowledgeArticleEventLog

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article. Contains values only in
orgs that migrate from Knowledge in Salesforce Classic to Lightning Knowledge. This
field is available in API version 45.0 and later.

```
TotalViewCount

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for this article. This field is available in API version 39.0 and
later.

Use this object to query or retrieve articles. KnowledgeArticle can be used in a SOQL clause, but doesn’t provide access to the fields from
the article. Provides read-only access to an article and the ability to delete the primary article.

Usage for SOQL with KnowledgeArticle

To expose the `migrated_to_from_id` column on KnowledgeArticle and KnowledgeArticleVersion to the sObject API: expose
`MigratedToFromArticle` in KnowledgeArticle.

For SOQL:

**•** To filter by `MigratedToFromArticle`, remove any other filters.

**•** When filtering by `MigratedToFromArticle`, use the '=' or 'IN' operator.

**•** When filtering by `MigratedToFromArticle`, the value can't be null or empty.

SEE ALSO:

KnowledgeArticleVersion

### KnowledgeArticleEventLog

Knowledge Article View event logs contain user activity with your knowledge base. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects KnowledgeArticleEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ArticleIdentifier

ArticleStatus

ArticleVersion

ArticleVersionIdentifier

Context

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The id of the article. For example: `00Dxx0000001gEb` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the article.

Possible values are:

**•** `D` —Draft

**•** `O` —Online

**•** `A` —Archived

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The article version number. For example: `2` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the article version. For example: `ka0R00000005rt6` .

**Type**
string


Standard Objects KnowledgeArticleEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Context of the request.

```
IsLargeLanguageModel

IsLastVersion

Language

ObjectType

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Whether the article was written with an LLM.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if it is the last version of the article.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO code of the language. For example: `en_US` /

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object requested. For example: `Knowledge__kav` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects KnowledgeArticleEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
SessionIdentifier

Timestamp

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Session ID of the request. For example:
`gV7pCSW2vGaaJNFi3GSpuPIjNbKVbSxRvx34LJsIvuc=` .

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
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User type of the request.

Possible values are:

**•** `A` —App

**•** `C` —Customer Portal

**•** `P` —Partner Portal

**•** `G` —Guest


### Standard Objects KnowledgeArticleFeedback KnowledgeArticleFeedback

Represents information about feedback from users on Knowledge articles and details about assignment of feedback to the article owner
or team to take action. This object is available in API version 64.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `delete()`, `update()`

Note: A KnowledgeArticleFeedback record is created only when a user submits feedback.

Special Access Rules

Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license. Knowledge Article Feedback Org Preference
should also be enabled.

Fields

**Field Name** **Details**

```
AssignedToId

FeedbackResponseId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The queue name or user ID of the feedback assignee, who reviews and takes action
on the feedback.

This field is a polymorphic relationship field.

**Relationship Name**
AssignedTo

**Refers To**
Queue, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the feedback response associated with the feedback record.

This field is a relationship field.


Standard Objects KnowledgeArticleFeedback

**Field Name** **Details**

**Relationship Name**
FeedbackResponse

**Refers To**
SurveyResponse

```
FeedbackSource

FeedbackSubmitterId

IsLiked

KnowledgeArticle

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The source of feedback. Possible values are:

**•** `Internal`

**•** `Community`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who submitted feedback.

This field is a relationship field.

**Relationship Name**
FeedbackSubmitter

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The answer to the Article Liked question in the feedback form.

The default value is false

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the article associated with the feedback response.


Standard Objects KnowledgeArticleFeedback

**Field Name** **Details**

```
KnowledgeArticleUrl

KnowledgeArticleVersion

KnowledgeArticleVersionTitle

LastReferencedDate

LastViewedDate

LinkedArticleEntityId

```

**Type**
url

**Properties**
Filter, Sort

**Description**
The URL of the article version associated with the feedback response.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The version of the article associated with the feedback response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the article version associated with the feedback response.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the feedback record was last accessed or referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the feedback record was last viewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Internal entity that links a Knowledge article version and survey invitation.


Standard Objects KnowledgeArticleFeedback

**Field Name** **Details**

This field is a relationship field.

**Relationship Name**
LinkedArticleEntity

**Refers To**
LinkedArticle

```
Name

OwnerId

ReviewActionTaken

ReviewComment

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique name automatically assigned to the Knowledge article feedback when it's
created. You can't change the format or value of this field.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user ID of the article feedback owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable, Update

**Description**
The review action taken to address the feedback. You can configure the possible
values for this picklist field.

**Type**
textArea

**Properties**
Filter, Nillable, Sort, Update

**Description**

The review comment provided by the feedback assignee. This is optional. The
maximum length is 1,212 characters.


Standard Objects KnowledgeArticleFeedback

**Field Name** **Details**

```
ReviewCompletionDate

ReviewDueDate

ReviewStatus

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date when the review was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The due date for completing the feedback review.

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable, Update

**Description**
The review status of the feedback. You can configure the possible values for this
picklist field.

Use this object to query, retrieve, or search for article feedback based on your access level to the articles. You can filter feedback records
by Knowledge article, article version, or other criteria.

SOQL Samples

The SOQL clause queries KnowledgeArticleFeedback records which aren't reviewed.

```
SELECT FeedbackResponseId, IsLiked, KnowledgeArticleVersion

FROM KnowledgeArticleFeedback

WHERE ReviewCompletionDate = NULL

```

The SOQL clause queries KnowledgeArticleFeedback records for a specific article version.

```
SELECT FeedbackResponseId, IsLiked, KnowledgeArticleVersion, AssignedToId, ReviewStatus

FROM KnowledgeArticleFeedback

WHERE KnowledgeArticleVersion = 'ka0SG00000KSjjRYAT'

```


### Standard Objects KnowledgeArticleVersion KnowledgeArticleVersion

Provides a global view of standard article fields across all types of articles depending on their version. This object is available in API version
18.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Use this object to:

**•** Query or search generically across multiple types of articles.

**•** Filter on a specific version.

**•** Update standard fields in draft versions.

When you query on the archived article, the results include both the article and the article’s archived versions.

Knowledge__kav on page 3021 is derived from this object.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`

Note:

**•** You can only update draft versions.

**•** You can't update draft translations with the `knowledgeManagement` REST API.

**•** For Lightning Knowledge, to create, update, or delete a Knowledge article version, use the call on Knowledge__kav. For
example, to delete, use `Knowledge__kav.delete()` .

**•** For Knowledge in Salesforce Classic, to create, update, or delete a Knowledge article version, use the call on
_`ArticleType`_ `__kav`, where _`ArticleType`_ is the name of the article’s type. For example, to delete, use
`ArticleType__kav.delete()` .

Special Access Rules

Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license.

Fields

**Field Name** **Details**

```
ArchivedById

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

```
ArchivedDate

ArticleArchivedById

ArticleArchivedDate

ArticleCaseAttachCount

ArticleCreatedById

ArticleCreatedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article version was archived.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was archived.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cases where this article is attached.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who created the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was created.


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

```
ArticleMasterLanguage

ArticleNumber

ArticleTotalViewCount

ArticleType

AssignedById

AssignedToId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports
multiple languages.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't
change the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for the article.

**Type**
string

**Properties**
Defaulted on createFilter

**Description**
Indicates the API Name of the article type. The `ArticleType` is assigned to the
article when it's created. You can't change the value of this field. This field is available
in orgs using Knowledge in Salesforce Classic in API version 26.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who assigned the article.

**Type**
reference


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user assigned to the article.

```
AssignmentDate

AssignmentDueDate

AssignmentNote

FirstPublishedDate

IsLatestVersion

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was assigned to a user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The due date when an article is assigned.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Notes to the assignee from the user who assigned the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article is the most current version. ( `true` ) or not ( `false` ).
This field can be `true` on the online or published version, a draft version in the
primary language, a draft version in a translation, and the latest archived version.
However, you can’t filter by (PublishState=’Online’) and (IsLatestVersion=false) because


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

the online version is also the latest version. This field is available in API version 24.0
and later.

```
IsMasterLanguage

IsOutOfDate

IsVisibleInApp

IsVisibleInCsp

IsVisibleInPkb

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article has one or more translations associated with it ( `true` )
or not ( `false` ). Only accessible if your knowledge base supports multiple languages.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the source article has been updated since this translated version
was created ( `true` ) or not ( `false` ). Only accessible if your knowledge base supports
multiple languages.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Articles tab ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Customer Portal ( `true` ) or
not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

**Description**
Required. Indicates whether the article is visible in the public knowledge base ( `true` )
or not ( `false` ).

```
IsVisibleInPrm

KnowledgeArticleId

Language

LargeLanguageModel

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the partner portal ( `true` ) or not
( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article independent from its version. The value for this field is retrieved
from the `Id` field of the KnowledgeArticle object.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
`(Traditional)` .

Querying or searching articles in SOSL require that you specify the `Language` field
in the WHERE clause. The language must be the same for all article types.

Before API version 47.0, you must include the `Language` field to filter queries on
Knowledge article versions. In API version 47.0 and later, you can filter queries on
Knowledge article versions with or without `Language` depending on what you are
querying.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Shows the LLM used to create an article version. This object is available in API version
59.0 and later.


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

```
LastPublishedDate

MasterVersionId

MigratedToFromArticleVersion

NextReviewDate

OwnerId

PublishStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source article, if the article is the translation of a source article. Only accessible
if your knowledge base supports multiple languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article version. Contains values
only in orgs that migrate from Classic to Lightning Knowledge. Available in API version
43.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article must next be reviewed for accuracy. Available in API version
58.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article's owner.

**Type**
picklist


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The publication status for the article:

**•** `Draft` : any draft articles.

**•** `Online` : articles published in Salesforce Knowledge.

**•** `Archived` : archived articles.

A user must have the “Manage Articles” permission enabled to use `Online` .

Article queries and searches in SOQL or SOSL require that you specify either the
`PublishStatus` or the `Id` field in the WHERE clause. You can search for only
one publication status per article type in a single SOSL query. When searching for
articles with a `PublishStatus` of `Archived`, also check that
`IsLatestVersion` equals `false` in your WHERE clause.

```
SourceId

Summary

Title

TranslationCompletedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source from which the article was created (Case or Reply).

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Summary of the article. Maximum size is 1000 characters.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Article's title. Maximum size is 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

**Description**
Date and time when the article was last translated. Only accessible if your knowledge
base supports multiple languages.

```
TranslationExportedDate

TranslationImportedDate

UrlName

ValidationStatus

VersionNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last exported for translation. Only accessible if
your knowledge base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last imported for translation. Only accessible if
your knowledge base supports multiple languages.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Represents the article's URL. Can contain alphanumeric characters and
hyphens but can't begin or end with a hyphen. This value must be unique regardless
of context. (For example, a unique value allows you to get expected results when
running an Apex test with `SeeAllData` set to `false` .) `UrlName` is case-sensitive
and its maximum size is 255 characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group

**Description**

Shows whether the content of the article has been validated. Possible values are
`Validated` and `Not Validated` . The default value is `Not Validated` .
This field is available in API version 24.0 or later.

**Type**
int


Standard Objects KnowledgeArticleVersion

**Field Name** **Details**

**Properties**
Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version
24.0 and later.

Usage

Use this object to query, retrieve, or search for articles across all types of articles depending on their version. You can update draft primary
articles. Also, you can delete articles that aren’t drafts. Client applications can use KnowledgeArticleVersion with
`describeDataCategoryGroups()` and `describeDataCategoryGroupStructures()` to return the category
groups and the category structure associated with Salesforce Knowledge.

To access an article independent of its version, use the KnowledgeArticle object.

In Lightning Knowledge, the type of article is determined by the `RecordType` field on the concrete derived object (for example,
Knowledge__kav on page 3021). For Knowledge in Salesforce Classic, the type of article is determined by the `ArticleType` field and
the concrete derived object uses the prefix of the article type name (for example, FAQ__kav for the FAQ article type).

SOQL Samples

The following SOQL clause uses KnowledgeArticleVersion to query all published articles from all articles complying with the classification
specified in the WITH DATA CATEGORY clause:

```
   SELECT Title, Summary

   FROM KnowledgeArticleVersion

   WHERE PublishStatus='Online'

   AND Language = 'en_US'

   WITH DATA CATEGORY Geography__c ABOVE_OR_BELOW europe__c AND Product__c BELOW All__c

```

The following SOQL clause for Lightning Knowledge uses the `Offer` record type to limit the query to all draft articles:

```
   SELECT Id, Title

   FROM Knowledge__kav

   WHERE PublishStatus='Draft'

   AND Language = 'en_US'

   AND RecordTypeId = '<specify RecordTypeId for Offer here>'

   WITH DATA CATEGORY Geography__c AT (france__c,usa__c) AND Product__c ABOVE dsl__c

```

The following SOQL clause for Salesforce Classic uses the `Offer` article type to limit the query to all draft articles:

```
   SELECT Id, Title

   FROM Offer__kav

   WHERE PublishStatus='Draft'

   AND Language = 'en_US'

   WITH DATA CATEGORY Geography__c AT (france__c,usa__c) AND Product__c ABOVE dsl__c

```

The following SOQL clause uses KnowledgeArticleVersion to query the IDs of all archived versions of a particular article:

```
   SELECT Id

   FROM KnowledgeArticleVersion

```


Standard Objects KnowledgeArticleVersion

```
   WHERE PublishStatus='Archived'

   AND IsLatestVersion=false

   AND KnowledgeArticleId='kA1D00000001PQ6KAM'

```

SOQL and SOSL with KnowledgeArticleVersion

**•** Filter on a single value of `PublishStatus` for best results. To find all versions of each article, omit the `PublishStatus` filter,
but do filter on one or more master key IDs. To retrieve all archived versions for a given article, specify a SOQL filter where
`IsLatestVersion` is `false` .

**•** In API version 46.0 and earlier, queries without a filter on `PublishStatus` return published articles by default. In API version
47.0 and later, draft, published, and archived articles are returned when Lightning Knowledge is enabled.

**•** To support security, only users with the “View Draft Articles” permission see articles whose `PublishStatus` value is `Draft` .
Similarly, only users with the “View Archived Articles” permission see articles whose `PublishStatus` value is `Archived`

**•** Archived article versions are stored in the _**`Knowledge`**_ `__kav` object. To query archived article versions, specify the article `Id`
and set `IsLatestVersion='0'` .

**•** You can’t use binding variables in Apex SOQL statements with KnowledgeArticleVersion objects. For example, the following SOQL
statement causes a compilation error.

```
     final String PUBLISH_STATUS_ONLINE = 'Online';

     List<Knowledge__kav> articles = [

     SELECT Id FROM Knowledge__kav

     WHERE PublishStatus = :PUBLISH_STATUS_ONLINE

     ];

```

[Instead, use dynamic SOQL as follows. See Dynamic SOQL in](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm) _Apex Developer Guide_ .

```
     final String PUBLISH_STATUS_ONLINE = 'Online';

     final String q = 'SELECT Id, PublishStatus FROM Knowledge__kav

     WHERE PublishStatus = :PUBLISH_STATUS_ONLINE';

     List<Knowledge__kav> articles = Database.query(q);

```

Other Usage for SOQL and SOSL with KnowledgeArticleVersion

To expose the _migrated_to_from_id_ on **KnowledgeArticle** and **KnowledgeArticleVersion** to the sObject API: expose
**MigratedToFromArticleVersion** in **KnowledgeArticleVersion** .

**•** For SOQL:

**–** To filter by **MigratedToFromArticleVersion**, remove any other filters.

**–** When filtering by **MigratedToFromArticleVersion**, use the '=' or 'IN' operator.

**–** When filtering by **MigratedToFromArticleVersion**, the value can't be null or empty.

**•** SOSL doesn’t support **MigratedToFromArticleVersion** .

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.


### Standard Objects KnowledgeArticleVersionHistory **KnowledgeArticleVersionHistory**

History is available for tracked fields of the object.

SEE ALSO:

### KnowledgeArticle

KnowledgeArticleViewStat

KnowledgeArticleVoteStat

### KnowledgeArticleVersionHistory

Enables read-only access to the full history of an article. This object is available in API version 25.0 and later.

[Knowledge__VersionHistory is derived from this object. To access this derived object, turn on field history tracking for Knowledge objects.](https://help.salesforce.com/articleView?id=tracking_field_history_for_custom_objects.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Knowledge must be enabled in your org. This object respects field, entity, and record-level security. You must have at least “Read”
permission on the article type or the field to access its history. For data category security, Salesforce determines access based on the
categorization of the online version of an article. If there’s no online version, then security is applied based on the archived version,
followed by the security of the draft version.

Fields

**Field Name** **Details**

```
DataType

EventType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of data that is tracked in the history table. This field is available in API
version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects KnowledgeArticleVersionHistory

**Field Name** **Details**

**Description**

The type of event that is tracked in the history table.

```
FieldName

Language

NewValue

OldValue

ParentId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Name of the tracked field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
`(Traditional)` . Querying or searching articles in SOSL requires that you
specify the `Language` field in the WHERE clause. The language must be the
same for all article types.

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

The most recent value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the article.


### Standard Objects KnowledgeArticleViewStat

**Field Name** **Details**

```
ParentSobjectType

VersionId

VersionNumber

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of object that contains the field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID assigned to a version of the article.

This is a polymorphic relationship field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version
24.0 and later.

Use this object to query events in the history of an article. For example, you can retrieve the number of edits a particular user has made
to an article, how many times the article has been published, and so on.

### KnowledgeArticleViewStat

Provides certain statistics related to the number of views for the specified article across all article types. The view count statistics are for
published and archived articles only. View counts for draft articles aren’t tracked. This object is read-only and available in API version
20.0 and later.

Knowledge__ViewStat is derived from this object.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects KnowledgeArticleViewStat

Special Access Rules

Knowledge must be enabled in your org. Users must have access to the published and archived versions of an article to retrieve its views.
For more information on published and archived article versions, see the `PublishStatus` field in KnowledgeArticleVersion.

Fields

**Field Name** **Details**

```
Channel

NormalizedScore

ParentId

ViewCount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The channel where the article is viewed:

**•** `AllChannels` for article views across all channels.

**•** `App` for the internal Salesforce Knowledge application.

**•** `Pkb` for article views in the public knowledge base.

**•** `Csp` for Customer Portal.

**•** `Prm` for article view in partner portal.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Article's weighted views in the selected channel. The article with most views has a
score of 100. Other article views are then calculated relative to this highest view score.
For example, if the best read article has 2000 views and another has 1000. The first
one gets a score of 100 while the second gets 50.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the viewed article. This corresponds to a KnowledgeArticle record.

**Type**
int

**Properties**
Filter, Group, Sort


### Standard Objects KnowledgeArticleVoteStat

**Field Name** **Details**

**Description**
The number of unique views a published or archived article has received in the selected
channel. An article with a high number of views may not always have a high
normalized score. The normalized score for an article is calculated based on views
over time, with more recent views earning a higher score. This field is available in API
version 27.0 and later.

Usage

Use this object to query or retrieve certain statistics for article views.

Alternatively, client applications can use the article type `API Name` followed by `__ViewStat` to query or retrieve most viewed
articles from a specific article type.

SOQL Samples

The following SOQL clause uses KnowledgeArticleViewStat to query all the article views in Salesforce Knowledge and return the related
articles:

```
   SELECT Id, NormalizedScore, Parent.Id

        FROM KnowledgeArticleViewStat where Channel = 'App'

        ORDER BY NormalizedScore

```

Use the following clause to restrict your query to Offer articles for the `Offer` article type:

```
   SELECT Id, NormalizedScore, Parent.Id

        FROM Offer__ViewStat where Channel = 'App'

        ORDER BY NormalizedScore

```

SEE ALSO:

### KnowledgeArticle

KnowledgeArticleVersion

### KnowledgeArticleVoteStat KnowledgeArticleVoteStat

Provides the weighted rating for the specified article on a scale of 1 to 5 across all article types. This object is read-only and available in
API version 20.0 and later.

Knowledge__VoteStat is derived from this object.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects KnowledgeArticleVoteStat

Special Access Rules

Knowledge must be enabled in your org. Users must have access to the published version of an article to retrieve its votes. For more
information on published article version, see the `PublishStatus` field in KnowledgeArticleVersion

Fields

**Field Name** **Details**

```
Channel

NormalizedScore

ParentId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The channel where the article is rated:

**•** `AllChannels` for article views across all channels.

**•** `App` for the internal Salesforce Knowledge application.

**•** `Pkb` for article views in public knowledge base.

**•** `Csp` for Customer Portal.

**•** `Prm` for article view in partner portal.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Article's weighted score on a scale of 1 to 5. A higher score means more votes. Articles
without recent votes trend towards an average rating of three stars.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The rated article. This corresponds to a KnowledgeArticle record.

Use this object to query or retrieve the rating for an article.

Alternatively, client applications can use the article type `API Name` followed by `__VoteStat` to query or retrieve the rating for an
article for a specific article type.


### Standard Objects LandingPage

SOQL Samples

See KnowledgeArticleViewStat.

SEE ALSO:

KnowledgeArticle

KnowledgeArticleVersion

KnowledgeArticleViewStat

### LandingPage

Represents an Account Engagement landing page. A landing page is a web page that a visitor reaches after clicking a link or advertisement.
Landing pages can be created in Account Engagement and synced to Salesforce or created on the Landing Page object in Account
Engagement Lightning App. This object is available in API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set. To create,
update, or delete a builder landing page, the Use Account Engagement Content Experience permission set is required.

Fields

**Field Name** **Details**

```
CampaignId

ContentLastSaved

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects LandingPage

**Field Name** **Details**

**Description**

The date and time of the last time someone changed and saved the landing page
Name, Campaign, Content, IsHideFromSearchEngineIndex, or Vanity URL fields.
This field is available in API version 53.0 and later.

```
ContentLastSavedById

FallbackUrl

FooterCode

FormErrorRate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The user who last changed and saved the Content body. This is a relationship
field. This field is available in API version 53.0 and later.

**Relationship Name**

ContentLastSaved

**Relationship Type**

Lookup

**Refers To**

User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The URL used to redirect viewers after the landing page is unpublished. This field
is available in API version 54.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

`<Script>`, `<style>`, and `<link>` code added before the landing page’s
closing body tag. This field is available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Group, Sort


Standard Objects LandingPage

**Field Name** **Details**

**Description**

The percentage of errors made on the landing page form. Calculated as total
errors divided by total views.

```
FormSubmissionRate

HeaderCode

IsHideFromSearchEngineIndex

LastPublished

LastPublishedById

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of form submissions based on the total number of landing page
views.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

`<Script>`, `<style>`, and `<link>` code added to the head tag of the landing
page. This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the landing page is hidden from search engine indexing. The
default value is `false` . This field is available in API version 53.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time of the last time someone published the landing page. This
field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LandingPage

**Field Name** **Details**

**Description**

The user who last published the landing page. This is a relationship field. This
field is available in API version 53.0 and later.

**Relationship Name**

LastPublished

**Relationship Type**

Lookup

**Refers To**

User

```
LastReferencedDate

LastViewedDate

Name

PublicLink

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Indicates when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
`LastReferencedDate` ) and not viewed. This field is available in API version
53.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the landing page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LandingPage

**Field Name** **Details**

**Description**

The URL where the landing page is available. This field is available in API version
53.0 and later.

```
Source

Status

TotalFormErrors

TotalFormSubmissions

TotalTrackedLinkClicks

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates where the landing page was created. The default value is
`Salesforce` . This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates the state of the landing page: `Draft`, `Published`, or `Published`
`(Changes Pending)` . The default value is `Draft` . This field is available in
API version 53.0 and later.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a visitor or prospect enters an invalid email address
or leaves a required field blank on a landing page form.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a form on the landing page has been submitted.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects LandingPage

**Field Name** **Details**

**Description**

The number of times prospects clicked a link on the landing page’s thank you
page.

```
TotalViews

UniqueFormErrors

UniqueFormSubmissions

UniqueTrackedLinkClicks

UniqueViews

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times visitors and prospects viewed your landing page. This
total includes multiple views from the same person.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of individual visitors and prospects who made an error on the form.
This metric doesn’t include multiple errors from the same person.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of individual visitors who submitted a form on the landing page.
This metric doesn’t include multiple submissions from the same person.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a prospect clicked a link on the landing page’s thank you
page. This metric doesn’t include multiple clicks of the same link.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


### Standard Objects Lead

**Field Name** **Details**

**Description**

The number of individual visitors and prospects who viewed your landing page.
This metric doesn’t include multiple views from the same person.

```
VanityUrl

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The custom path that’s appended to tracker domains to create a vanity URL. This
field doesn’t support scheme or domain values. This field is available in API version
53.0 and later.

This object has the following associated objects. Unless otherwise noted, they’re available in the same API version as this object.

**LandingPageChangeEvent (API version 44.0)**
Change events are available for the object.

**LandingPageFeed**

Feed tracking is available for the object.

### Lead

Represents a prospect or lead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceAssigneeId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Lead

**Field** **Details**

**Description**
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 48.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

```
ActionCadenceId

ActionCadenceState

ActiveTrackerCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 48.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. This field is available in API version 50.0 and
later when the Sales Engagement license is enabled. To see this field, the user also needs
the Sales Engagement User or Sales Engagement Quick Cadence Creator user permission
set.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cadences that are actively running on this lead. This field is available in API
version 57.0 and later when the Sales Engagement license is enabled. To see this field, the
user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
user permission set.


Standard Objects Lead

**Field** **Details**

```
ActivityMetricId

ActivityMetricRollupId

Address

AnnualRevenue

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. For details on compound address fields, see
Address Compound Fields.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Lead

**Field** **Details**

**Description**
Annual revenue for the lead’s company.

```
City

CleanStatus

Company

CompanyDunsNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the lead’s address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the record's clean status compared with Data.com. .

Several values for `CleanStatus` appear with different labels on the lead record.

Values include:

**•** `Acknowledged - Reviewed`

**•** `Different`

**•** `Inactive`

**•** `Matched - In Sync`

**•** `NotFound - Not Found`

**•** `Pending - Not Compared`

**•** `SelectMatch - Select Match Skipped`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The lead’s company.

If person account record types have been enabled, and if the value of `Company` is null, the
lead converts to a person account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Lead

**Field** **Details**

**Description**
The Data Universal Numbering System (D-U-N-S) number, which is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database that has a
unique, separate, and distinct operation. Industries and companies use D-U-N-S numbers
as a global standard for business identification and tracking. Maximum size is 9 characters.

This field is only available to organizations that use Data.com Prospector or Data.com Clean.

```
ConvertedAccountId

ConvertedContactId

ConvertedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the account into which the lead converted.

This is a relationship field.

**Relationship Name**
ConvertedAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the contact into which the lead converted.

This is a relationship field.

**Relationship Name**
ConvertedContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Date on which this lead was converted.


Standard Objects Lead

**Field** **Details**

```
ConvertedOpportunityId

ConnectionReceivedId

ConnectionSentId

Country

CountryCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the opportunity into which the lead has been converted.

This is a relationship field.

**Relationship Name**
ConvertedOpportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

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

**Description**
ID of the PartnerNetworkConnection that this record is shared with. This field is available
Salesforce to Salesforce is enabled. In API version 16.0 and later, this value is `null` . Use
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s country.

**Type**
picklist


Standard Objects Lead

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the lead’s address.

```
CurrencyIsoCode

DandBCompanyId

Description

Division

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference ID to a Dun & Bradstreet [®] company record, associated with an account added
from Data.com.

**Relationship Name**
DandbCompany

**Refers To**
DandbCompany

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The lead’s description.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as North
America, Healthcare, or Consulting. Available only when the Division permission is enabled.


Standard Objects Lead

**Field** **Details**

```
Email

EmailBouncedDate

EmailBouncedReason

ExportStatus

Fax

```

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The lead’s email address.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the lead bounced, the date and
time of the bounce. Email bounce functionality isn't triggered by record updates, including
updates to this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the lead bounced, the reason for
the bounce. Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
picklist

**Properties**
Filter, Restricted picklist, Sort

**Description**
Derived field for the record map for Partner Connect. The export status of this opportunity
to the partner’s connected org. To see this field, enable Partner Connect and add the Export
Vendor Records to an Authorized Partner Org user permission to the cosell export user. See
[Set Up Partner Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ . Available in API version 62.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s fax number.


Standard Objects Lead

**Field** **Details**

```
FirstCallDateTime

FirstEmailDateTime

FirstName

GeocodeAccuracy

GenderIdentity

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the lead. This field is available in API version 48.0
when the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the lead. This field is available in API version 48.0
when the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s first name up to 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The lead’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.


Standard Objects Lead

**Field** **Details**

```
HasOptedOutOfEmail

HasOptedOutOfFax

IndividualId

Industry

IsConverted

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the lead doesn’t want to receive email from Salesforce ( `true` ) or does
( `false` ). Label is **Email Opt Out** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the lead doesn’t want to receive faxes from Salesforce ( `true` ) or does
( `false` ). Label is **FaxOpt Out** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this lead. This field is available if you enabled
Data Protection and Privacy in Setup.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Industry in which the lead works.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects Lead

**Field** **Details**

**Description**
Indicates whether the lead has been converted ( `true` ) or not ( `false` ). Label is **Converted** .

```
IsDeleted

IsPriorityRecord

IsUnreadByOwner

Jigsaw

JigsawContactId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the lead as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If true, lead has been assigned, but not yet viewed. See Unread Leads for more information.
Label is **Unread By Owner** .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ID of a contact in Data.com. If a lead has a value in this field, it means that a
contact was imported as a lead from Data.com. If the contact (converted to a lead) wasn’t
imported from Data.com, the field value is null. Maximum size is 20 characters. Available in
API version 22.0 and later. Label is **Data.com Key** .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
string


Standard Objects Lead

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to `Jigsaw` .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

```
LastActivityDate

LastName

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent of either:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the lead up to 80 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.


Standard Objects Lead

**Field** **Details**

```
Latitude

LeadSource

Longitude

MasterRecordId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –90 and 90 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations

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
compound fields, see Compound Field Considerations and Limitations.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this record was deleted for any other reason, or hasn’t been deleted, the value
is `null` .

When using Apex triggers to determine which record was deleted in a merge event, this
field’s value is the ID of the record that remains in `Trigger.old` . In `Trigger.new`,
the value is `null` .

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup


Standard Objects Lead

**Field** **Details**

**Refers To**
Lead

```
MiddleName

MobilePhone

Name

NumberOfEmployees

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s middle name. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s mobile phone number.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of employees at the lead’s company. Label is **Employees** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the lead’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner


Standard Objects Lead

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PartnerAccountId

Phone

PhotoUrl

PostalCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner account for the partner user that owns this lead. Available if Partner
Relationship Management is enabled or if digital experiences is enabled and you have partner
portal licenses.

In API version 16.0 and later, the `Partner Account` field is set to the appropriate account
for the partner user that owns the lead. If the owner of the lead isn’t a partner user, this field
has no value.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s phone number.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance ( _Example:_
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the lead. Generated URL returns an HTTP redirect (code 302)
to the social network profile image for the lead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address of the lead. Label is **Zip/Postal Code** .


Standard Objects Lead

**Field** **Details**

```
Pronouns

Rating

RecordTypeId

Salutation

ScheduledResumeDateTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The lead’s personal pronouns, reflecting their gender identity. Others can use these pronouns
to refer to the lead in the third person. The entry is selected from a picklist of available values,
which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Rating of the lead.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salutation for the lead.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Lead

**Field** **Details**

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.

```
ScoreIntelligenceId

State

StateCode

Status

Street

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the intelligent field record that contains lead score.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the address of the lead.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the lead’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status code for this converted lead. Status codes are defined in `Status` and represented
in the API by the LeadStatus object.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street number and name for the address of the lead.


Standard Objects Lead

**Field** **Details**

```
Suffix

Title

Website

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s name suffix. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title for the lead, such as CFO or CEO. The maximum size is 128 characters. When converting
a lead to a person account, the conversion fails if the lead Title field contains more than 80
characters.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Website for the lead.

Note: When importing lead data, users need the Set Audit Fields upon Record Creation permission to assign values to audit fields
such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields yourself.

Converted Leads

Leads have a special state to indicate that they’ve been converted into an account, a contact, and an opportunity. Your client application
can convert leads via the `convertLead()` call. Users can also convert leads in Salesforce. After a lead has been converted, it’s read
only. However, you can query converted lead records. Only users with the View and Edit Converted Leads permission can update
converted lead records.

Leads have several fields that indicate their converted status. These special fields are set when converting the lead in the user interface.

**•** `ConvertedAccountId`

**•** `ConvertedContactId`

**•** `ConvertedDate`

**•** `ConvertedOpportunityId`

**•** `IsConverted`

**•** `Status`


Standard Objects Lead

Unread Leads

Leads have a special state to indicate that they haven’t been viewed or edited by the lead owner. In Salesforce, it’s helpful for users to
know which leads have been assigned to them but that they haven’t touched yet. `IsUnreadByOwner` is `true` if the lead owner
hasn’t yet viewed or edited the lead, and `false` if the lead owner has viewed or edited the lead at least one time.

Lead Status Picklist

Each `Status` value corresponds to either a converted or unconverted status in the lead status picklist, as defined in the user interface.
To obtain the lead status values in the picklist, a client application can query LeadStatus.

You can't convert a lead via the API by changing `Status` to one of the converted lead status values. When you convert qualified leads
into an account, contact, and opportunity, you can select one of the converted status types for the lead. Leads with a converted status
type are no longer available in the Leads tab, although you can include them in reports.

Usage

If lead data is imported and you need to set the value for an audit field, such as `CreatedDate`, contact Salesforce Support. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

To update a lead or to convert one with `convertLead()`, log in to your client application with the Edit permission on leads.

When you create, update, or upsert a lead, your client application can have the lead assigned to multiple user records based on assignment
rules that have been configured in Salesforce.

To use this feature, your client application needs to set either of these options (but not both) in the AssignmentRuleHeader used in
create or update:

**Field** **Field Type** **Details**

`assignmentRuleId` reference

ID of the assignment rule to use. Can be an inactive assignment rule. If unspecified
and `useDefaultRule` is `true`, then the default assignment rule is used.

To find the ID for a given assignment rule, query the AssignmentRule object
(specifying `RuleType="leadAssignment"` ), iterate through the returned

AssignmentRule records, find the one you want to use, retrieve its ID, and then
specify its ID in this field in the AssignmentRuleHeader.

`useDefaultRule` boolean Specifies whether to use the default rule for rule-based assignment ( `true` ) or
not ( `false` ). Default rules are assigned in the user interface.

Java Sample

The following Java sample shows how to automatically assign a newly created lead.

```
package wsc;

import com.sforce.soap.enterprise.Connector;

import com.sforce.soap.enterprise.EnterpriseConnection;

import com.sforce.ws.ConnectionException;

import com.sforce.ws.ConnectorConfig;

import com.sforce.soap.enterprise.sobject.Lead;

```


Standard Objects Lead

```
   import com.sforce.soap.enterprise.QueryResult;

   import com.sforce.soap.enterprise.SaveResult;

   import com.sforce.soap.enterprise.sobject.SObject;

   public class LeadAssignment {

      static final String USERNAME = "REPLACE USER NAME";

      static final String PASSWORD = "REPLACE PASSWORD";

      static EnterpriseConnection connection;

      static LeadAssignment _leadAssignment;

      // Main

      public static void main(String[] args)

      {

        // Establish connection and login

        ConnectorConfig config = new ConnectorConfig();

        config.setUsername(USERNAME);

        config.setPassword(PASSWORD);

        try {

           connection = Connector.newConnection(config);

           System.out.println("Logged in, endpoint: " + config.getAuthEndpoint());

        } catch (ConnectionException e1) {

           e1.printStackTrace();

        }

        // Create lead

        _leadAssignment = new LeadAssignment();

        try {

           _leadAssignment.CreateLead();

        } catch (Exception e) {

           e.printStackTrace();

        }

        // Logout

        try {

           connection.logout();

           System.out.println("Logged out");

        } catch (ConnectionException ce) {

           ce.printStackTrace();

        }

      }

      public void CreateLead() throws ConnectionException

      {

        // Create a new Lead and assign various properties

        Lead lead = new Lead();

        lead.setFirstName("Joe");

        lead.setLastName("Smith");

        lead.setCompany("ABC Corporation");

        lead.setLeadSource("API");

        // The lead assignment rule will assign any new leads that

        // have "API" as the LeadSource to a particular user

```


Standard Objects Lead

```
        // In this sample we will look for a particular rule and if found

        // use the id for the lead assignment. If it is not found we will

        // instruct the call to use the current default rule. You can't use

        // both of these values together.

        QueryResult qr = connection.query("SELECT Id FROM AssignmentRule WHERE Name = " +

                     "'Mass Mail Campaign' AND SobjectType = 'Lead'");

        if (qr.getSize() == 0) {

           connection.setAssignmentRuleHeader(null, true);

        } else {

           connection.setAssignmentRuleHeader(qr.getRecords()[0].getId(), false);

        }

        // Every operation that results in a new or updated lead will

        // use the specified rule until the header is removed from the

        // connection.

        SaveResult[] sr = connection.create(new SObject[] {lead});

        for (int i=0;i<sr.length;i++) {

           if (sr[i].isSuccess()) {

             System.out.println("Successfully created lead with id of: " +

                        sr[i].getId() + ".");

           } else {

             System.out.println("Error creating lead: " +

                        sr[i].getErrors()[0].getMessage());

           }

        }

        // This call effectively removes the header, the next lead will

        // be assigned to the default lead owner.

        connection.clearAssignmentRuleHeader();

      }

   }

```

C# Sample

The following C# sample shows how to automatically assign a newly created lead.

```
   using System;

   using System.Collections.Generic;

   using System.Linq;

   using System.Text;

   using System.Threading.Tasks;

   using System.ServiceModel;

   using LeadSample.sforce;

   namespace LeadSample

   {

      class LeadAssignment

      {

        private static SoapClient client;

        private static SoapClient apiClient;

        private static SessionHeader header;

        private static LoginResult loginResult;

```


Standard Objects Lead

```
        private static readonly string Username = "REPLACE USERNAME";

        private static readonly string Password = "REPLACE PASSWORD AND SECURITY TOKEN";

        // Create the proxy binding and login

        private LeadAssignment()

        {

           client = new SoapClient();

           try

           {

             loginResult = client.login(null, Username, Password);

           }

           catch (Exception e)

           {

             Console.WriteLine("Unexpected login error: " + e.Message);

             Console.WriteLine(e.StackTrace);

             return;

           }

           // Access API endpoint and create new client

           header = new SessionHeader();

           header.sessionId = loginResult.sessionId;

           apiClient = new SoapClient("Soap", loginResult.serverUrl);

        }

        [STAThread]

        static void Main(string[] args)

        {

           LeadAssignment leadAssignment = new LeadAssignment();

           try

           {

             leadAssignment.CreateLead();

           }

           catch (Exception e)

           {

             Console.WriteLine(e.Message);

             Console.WriteLine(e.StackTrace);

             Console.WriteLine(e.InnerException);

           }

           // logout

           client.logout(header);

        }

        public void CreateLead()

        {

           // Create a new Lead and assign various properties

           Lead lead = new Lead();

           lead.FirstName = "John";

           lead.LastName = "Brown";

           lead.Company = "ABC Corporation";

           lead.LeadSource = "Advertisement";

           // Setting the lead source for a pre-existing lead assignment rule. This

           // rule was created outside of this sample and will assign any new leads

           // that have "Advertisement" as the LeadSource to a particular user.

```


Standard Objects Lead

```
           // Create the assignment rule header and add it to the proxy binding

           AssignmentRuleHeader arh = new AssignmentRuleHeader();

           // In this sample we will look for a particular rule and if found

           // use the id for the lead assignment. If it is not found we will

           // instruct the call to use the current default rule. Both these

           // values can't be used together.

           QueryResult qr = null;

           string query = "SELECT Id FROM AssignmentRule WHERE Name = " +

             "'Mass Mail Campaign' AND SobjectType = 'Lead'";

           try

           {

             LimitInfo[] limitArray = apiClient.query(

               header, // sessionheader

               null, // queryoptions

               null, // mruheader

               null, // packageversionheader

               query, // SOQL query

               out qr);

           }

           catch (Exception e)

           {

             Console.WriteLine("Unexpected query error: " + e.Message);

             Console.WriteLine(e.StackTrace);

           }

           if (qr.size == 0)

           {

             arh.useDefaultRule = true;

           }

           else

           {

             arh.assignmentRuleId = qr.records[0].Id;

           }

           // Create the lead using our Assignment Rule header

           LimitInfo[] li;

           SaveResult[] sr;

           apiClient.create(

             header, // sessionheader

             arh, // assignmentruleheader

             null, // mruheader

             null, // allowfieldtrunctionheader

             null, // disablefeedtrackingheader

             null, // streamingenabledheader

             null, // allornoneheader

             null, // duplicateruleheader

             null, // localeoptions

             null, // debuggingheader

             null, // packageversionheader

             null, // emailheader

             new sObject[] { lead },

             out li,

             out sr);

```


### Standard Objects LeadCleanInfo

```
           foreach (SaveResult s in sr)

           {

             if (s.success)

             {

               Console.WriteLine("Successfully created Lead with ID: {0}", s.id);

             }

             else

             {

               Console.WriteLine("Error creating Lead: {0}", s.errors[0].message);

             }

           }

        }

      }

   }

```

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[LeadChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[LeadFeed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[LeadHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**LeadOwnerSharingRule**

Sharing rules are available for the object.

**LeadShare**

Sharing is available for the object.

SEE ALSO:

LeadOwnerSharingRule

LeadShare

LeadStatus

PartnerNetworkConnection

### LeadCleanInfo

Stores the metadata Data.com Clean uses to determine a lead record’s clean status. Helps you automate the cleaning or related processing
of lead records.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)


Standard Objects LeadCleanInfo

Lead Clean Info provides a snapshot of the data in your Salesforce lead record and its matched Data.com record at the time the Salesforce
record was cleaned.

Lead Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field `IsDifferent` has an `IsDifferentTitle`
field. If the `IsDifferentTitle` field’s value is `False`, that means the `Title` field value is _the same_ on the Salesforce lead record
and its matched Data.com record.

LeadCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the lead record.

**•** `IsDifferent` indicates whether or not a field on the lead record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the lead record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the lead record is in a `Reviewed` state, which means that the value was
reviewed but not accepted..

Their individual bits are defined here

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Address

AnnualRevenue

City

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Estimated annual revenue of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Details for the billing address of the lead.

```
CleanedByJob

CleanedByUser

CompanyDunsNumber

CompanyName

ContactStatusDataDotCom

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead record was cleaned by a Data.com Clean job ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead record was cleaned by a Salesforce user ( `true` ) or
not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the company.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
The status of the contact associated with the lead per Data.com. Values are:
`Contact is Active per Data.com`, `Phone is Wrong per`
`Data.com`, `Email is Wrong per Data.com`, `Phone and`
`Email are Wrong per Data.com`, `Contact Not at Company`
`per Data.com`, `Contact is Inactive per Data.com`,

```
                        Company this contact belongs to is out of business
```

`per Data.com`, `Company this contact belongs to never`
`existed per Data.com` or `Email address is invalid per`
`Data.com` .

```
Country

DandBCompanyDunsNumber

DataDotComCompanyId

DataDotComId

Email

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The D-U-N-S Number on the D&B Company record (if any) that is linked to the
lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the company associated with the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact associated with the lead.

**Type**
email


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s email address.

```
FirstName

Industry

IsDifferentAnnualRevenue

IsDifferentCity

IsDifferentCompanyDunsNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s first name.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The industry the lead belongs to.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `AnnualRevenue` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `City` field value is different from the corresponding
value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is
different from the corresponding value on its matched Data.com record ( `true` )
or not ( `false` ).

```
IsDifferentCompanyName

IsDifferentCountry

IsDifferentCountryCode

IsDifferentDandBCompanyDunsNumber

IsDifferentEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Company Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Country` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Country Code` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `D&B Company D-U-N-S Number` field value
is different from the corresponding value on its matched Data.com record ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Email` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentFirstName

IsDifferentIndustry

IsDifferentLastName

IsDifferentNumberOfEmployees

IsDifferentPhone

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `First Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Industry` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Last Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `No. of Employees` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Phone` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentPostalCode

IsDifferentState

IsDifferentStateCode

IsDifferentStreet

IsDifferentTitle

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Postal Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `State Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Street` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Title` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsFlaggedWrongAddress

IsFlaggedWrongAnnualRevenue

IsFlaggedWrongCompanyDunsNumber

IsFlaggedWrongCompanyName

IsFlaggedWrongEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Annual Revenue` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is
flagged as wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company Name` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Email` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

```
IsFlaggedWrongIndustry

IsFlaggedWrongName

IsFlaggedWrongNumberOfEmployees

IsFlaggedWrongPhone

IsFlaggedWrongTitle

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Industry` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Name` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `No. of Employees` field value is flagged as
wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Phone` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Title` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

```
IsInactive

IsReviewedAddress

IsReviewedAnnualRevenue

IsReviewedCompanyDunsNumber

IsReviewedCompanyName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the lead has been reported to Data.com as _`Inactive`_
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Annual Revenue` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is in
a `Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `Company Name` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

```
IsReviewedDandBCompanyDunsNumber

IsReviewedEmail

IsReviewedIndustry

IsReviewedName

IsReviewedNumberOfEmployees

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `D&B Company D-U-N-S Number` field value
is in a `Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Email` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Industry` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Name` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the lead’s `No. of Employees` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

```
IsReviewedPhone

IsReviewedTitle

LastMatchedDate

LastName

LastStatusChangedById

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Phone` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Title` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the lead record was last matched and linked to a Data.com record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s last name.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of who or what last changed the record’s `Clean Status` field value:
a Salesforce user or a Clean job.


Standard Objects LeadCleanInfo

**Field Name** **Details**

```
LastStatusChangedDate

Latitude

LeadId

Longitude

Name

NumberOfEmployees

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the record’s `Clean Status` field value was last changed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the lead record was created.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Latitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is **Lead Clean Info Name** . The name of the lead. Maximum size is 255
characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LeadCleanInfo

**Field Name** **Details**

**Description**
The number of employees working at the lead.

```
Phone

PostalCode

State

Street

Title

```

Usage

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s title.

Developers can create triggers that read the Lead Clean Info fields to help automate the cleaning or related processing of lead records.


### Standard Objects LeadDailyMetric LeadDailyMetric

Represents the daily engagement metrics for a lead. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with the call result Not Interested.


Standard Objects LeadDailyMetric

**Field** **Details**

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsDeliveredRate

AllEmailsHardBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this lead with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this lead in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this lead in the day.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this lead. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
int


Standard Objects LeadDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this lead in the day.

```
AllEmailsOutOfOfficeCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this lead in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this lead in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead without engagement tracking enabled in the day.


Standard Objects LeadDailyMetric

**Field** **Details**

```
AllTotalCallsCount

DailyCutOffTimeStamp

Date

DateInt

HardBounceTrackableSends

InboundEngagementsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this lead with all call results in the day.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date on which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The date on which the engagement occurred, in yyyymmdd format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with hard bounce tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LeadDailyMetric

**Field** **Details**

**Description**
The number of inbound engagements for this lead in the day. This field is a calculated field.
The value is the sum of `UniqueEmailsOpenedCount`,
`UniqueEmailsRepliedCount`, and `UniqueEmailsLinkClickedCount` .

Available in API version 58.0 and later.

```
LeadId

LinkClickTrackableSends

OpenTrackableSends

OutOfOfficeTrackableSends

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lead.

This is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with link click tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with open tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LeadDailyMetric

**Field** **Details**

**Description**
The number of emails sent to this lead with out-of-office tracking.

Available in API version 54.0 and later.

```
OutboundEngagementsCount

ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound engagements for this lead in the day. This field is a calculated field.
The value is the sum of `AllTotalCallsCount` and `AllEmailsDeliveredCount` .

Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with reply tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with soft bounce tracking.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent


Standard Objects LeadDailyMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with link tracking that had link clicks. This field is
a calculated field.

Available in API version 54.0 and later.

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with open tracking that were opened by the
recipient. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with reply tracking that received replies. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with soft bounce tracking that soft bounced. This
field is a calculated field.


### Standard Objects LeadMonthlyMetric

**Field** **Details**

Available in API version 54.0 and later.

```
UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

### LeadMonthlyMetric

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the lead clicked a link in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the lead in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the lead in the day.

Represents the monthly engagement metrics for a lead. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

```

**Type**
int


Standard Objects LeadMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Call Back Later.

```
AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Unqualified.

**Type**
int


Standard Objects LeadMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this lead in the month.

This is a calculated field.

```
AllEmailsDeliveredCount

AllEmailsDeliveredRate

AllEmailsHardBouncedCount

AllEmailsOutOfOfficeCount

AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this lead in the month.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this lead. This field
is a calculated field.

This is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this lead in the month.

**Type**
int


Standard Objects LeadMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead in the month.

This is a calculated field.

```
AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

HardBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead without engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this lead with all call results in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with hard bounce tracking.


Standard Objects LeadMonthlyMetric

**Field** **Details**

Available in API version 54.0 and later.

```
LeadId

LinkClickTrackableSends

Month

MonthInt

OpenTrackableSends

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lead.

This is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with link click tracking.

Available in API version 54.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int


Standard Objects LeadMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with open tracking.

Available in API version 54.0 and later.

```
OutOfOfficeTrackableSends

ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with out-of-office tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with reply tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with soft bounce tracking.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent


Standard Objects LeadMonthlyMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with link tracking that had link clicks. This field is
a calculated field.

Available in API version 54.0 and later.

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with open tracking that were opened by the
recipient. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with reply tracking that received replies. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with soft bounce tracking that soft bounced. This
field is a calculated field.


### Standard Objects LeadOwnerSharingRule

**Field** **Details**

Available in API version 54.0 and later.

```
UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the lead clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the lead in the month.

### LeadOwnerSharingRule

Represents the rules for sharing a lead with users other than the owner.

Note: To enable access to this object, contact Salesforce customer support. However, we recommend that you instead use
Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation. The
[SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects LeadOwnerSharingRule

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

```
DeveloperName

GroupId

LeadAccessLevel

Name

```

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

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Leads owned by users in the source group
trigger the rule to give access.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
string


### Standard Objects LeadShare

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. The target user or group is being given
access.

Use these objects to manage the sharing rules for leads. General sharing and Territory-related sharing use this object.

SEE ALSO:

### Lead LeadShare

LeadStatus

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### LeadShare

Represents a sharing entry on a Lead.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Lead object can access this object.


Standard Objects LeadShare

Fields

The properties available for some fields depend on the default org-wide sharing settings. The properties listed are true for the default
settings of such fields.

**Field** **Details**

```
IsDeleted

LeadAccessLevel

LeadId

RowCause

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Lead. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid when creating or updating these records.

This field must be set to an access level that is higher than the organization’s default access
level for leads.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Lead associated with this sharing entry. This field can’t be updated.

This is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
picklist


Standard Objects LeadShare

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Lead with them.

**•** `Owner` —The User is the owner of the Lead.

**•** `Rule` —The User or Group has access via a Lead sharing rule.

**•** `GuestRule` —The User or Group has access via a Lead guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Lead via an account relationship data sharing rule.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Lead. This field can’t be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view or edit leads owned by other users.


### Standard Objects LeadStatus

If you attempt to create a record that matches an existing record, the existing record is returned.

SEE ALSO:

AccountShare

Case

CaseShare

OpportunityShare

### LeadStatus

Represents the status of a Lead record, such as Open, Qualified, or Converted.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsConverted

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

**Description**
Indicates whether this lead status value represents a converted lead ( `true` ) or not ( `false` ).
Multiple lead status values can represent a converted lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects LeadTag

**Field** **Details**

**Description**
Indicates whether this is the default lead status value ( `true` ) or not ( `false` ) in the picklist.

```
MasterLabel

SortOrder

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this lead status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the lead status picklist. These numbers are not guaranteed
to be sequential, as some previous lead status values might have been deleted.

This object represents a value in the lead status picklist (see Lead on page 3067). The lead status picklist provides additional information
about the status of a Lead on page 3067, such as whether a given status value represents a converted Lead on page 3067. Query this object
to retrieve the set of values in the lead status picklist, and then use that information while processing Lead on page 3067 objects to
determine more information about a given lead. For example, the application could test whether a given lead is converted based on its
Status value and the value of the `IsConverted` property in the associated LeadStatus record.

SEE ALSO:

LeadOwnerSharingRule

LeadShare

### LeadTag

Associates a word or short phrase with a Lead.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects LeadTag

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

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

LeadTag stores the relationship between its parent TagDefinition and the Lead being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects LearningContent

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### LearningContent

Represents a Trailhead or enablement site (myTrailhead) module assigned to a user in Workforce Engagement or Learning Paths. This
object also represents a Trailhead module or video in an Enablement program exercise. This object is available in API version 54.0 and
later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

**•** The org must have a Workforce Engagement license.

**•** The user must have at least one Workforce Engagement permission set assigned to them: Workforce Engagement Admin, Workforce
Engagement Analyst, Workforce Engagement Planner, Workforce Engagement Agent.

**•** For an enablement site (myTrailhead) module, the org must have a Sales Enablement license.

**•** For a Trailhead module or video in an Enablement program, the org must have an Enablement license.

Fields

**Field** **Details**

```
ApiName

AvailablePointCount

ContainsAssessmentType

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The module's human-readable API name, such as `pure-aloe-sales-strategies` .

**Type**
int

**Properties**
Group, Nillable

**Description**
The maximum points that a user can earn on their profile by completing the module. This
value is the sum of points that the content creator assigns to the module’s units.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist


Standard Objects LearningContent

**Field** **Details**

**Description**
Specifies the type of assessment that the content’s units include.

Possible values are:

**•** `MultipleChoiceQuiz` —All the content’s units have multiple-choice quizzes.

**•** `HandsOnChallenge` —At least one unit has a hands-on challenge.

```
ContentType

ContentUrl

Description

DurationCount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**
The type of content assigned to the user.

Possible values are:

**•** `All` —The content is any supported type.

**•** `Module` —The content is a Trailhead or enablement site (myTrailhead) module.

**•** `VideoLesson` —The content is a video that's specified in the Enablement workspace
in Digital Experiences and is used in an Enablement program.

**Type**
url

**Properties**
Group, Nillable

**Description**
The absolute URL to the content, such as
`https://purealoe.my.trailhead.com/en/content/sales-team-enablement/modules/pure-aloe-sales-strategies` .

**Type**
string

**Properties**
Nillable

**Description**
The module’s description.

**Type**
int

**Properties**
Group, Nillable

**Description**
The total time, in minutes, for a learner to complete all units in the module. This value is the
sum of the estimated times that the content creator assigns to the module’s units.


### Standard Objects LearningItem

**Field** **Details**

```
ExternalId

ImageUrl

IsPublic

Title

```

SEE ALSO:

PersonTraining

### LearningItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The GUID that Trailhead uses to reference the module.

**Type**
url

**Properties**
Group, Nillable

**Description**
The absolute URL to the module’s badge art image file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group

**Description**
Indicates whether the content is public Trailhead content ( `true` ) or private enablement
site (myTrailhead) content ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The module’s title.

Represents an item that requires users to take action, including a Learning Paths entry, an Enablement program, or an exercise with
linked content in an Enablement program. For Learning Paths, users are assigned a learning item to complete. For Enablement programs
and exercises, users are assigned a program or can self-enroll in shared programs. This object is available in API version 58.0 and later.


Standard Objects LearningItem

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CustomLearningItemTypeId

EnablementProgramId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a learning item type record if this learning item represents a custom exercise type
in an Enablement program. This field is required when the `Type` field’s value is
`CustomContent` .

This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomLearningItemType

**Relationship Type**
Lookup

**Refers To**
LearningItemType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an Enablement program that contains the outcome, milestone, or exercise.

This field is a relationship field.


Standard Objects LearningItem

**Field** **Details**

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

```
LearningContentId

OwnerId

StandardCustomContentMetadata

StandardCustomLearningItemType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that represents a Trailhead module or video in a sales program exercise.
This field is a relationship field.

**Relationship Name**
LearniningContent

**Refers To**
LearningContent

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
textarea

**Properties**
Nillable

**Description**
Reserved for future use.

**Type**
picklist


### Standard Objects LearningItemAssignment

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of learning item. Possible values are:

**•** `CustomContent` —Custom exercise content in an Enablement program, such as a
screen flow, content from external repositories, or other custom content sources. Available
in API version 62.0 and later.

**•** `EnablementProgram`

**•** `LearningContent` —Trailhead module

**•** `LearningLesson` —Lesson exercise in an Enablement program

**•** `LearningLink` —Audio Recording, Document, Scheduled Event, or Other exercise
in an Enablement program

**•** `LearningPractice` —Feedback Request exercise in an Enablement program

**•** `StandardCustomContent` —Standard Custom exercise content in an Enablement
program. Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemOwnerSharingRule on page 65 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemShare on page 67 (API version 60.0)**
Sharing is available for the object.

### LearningItemAssignment

Represents the assignment of a Learning Paths entry to users or groups or the enrollment of an Enablement program for a specific user.
This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LearningItemAssignment

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AssigneeId

AssignmentStatus

DueDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or group assigned to the learning item. This field is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of assigning an Enablement program to a user. Possible values are:

**•** `Failed`

**•** `InProgress`

**•** `Succeeded`

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LearningItemAssignment

**Field** **Details**

**Description**
The date that the assignment is due for the user or group.

```
EnrollmentType

IsOverdue

LearningItemId

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of enrollment for a user in an Enablement program. Possible values are:

**•** `Assigned`

**•** `SelfEnrolled`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the assigned learning item is overdue ( `true` ) or not ( `false` ). The default
value is `false` .

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
ID of the user who assigned the learning item. This field is a polymorphic relationship field.


Standard Objects LearningItemAssignment

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ProgressId

StartDate

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of record that represents a user's progress towards completing an assigned learning
item, such as a Learning Paths entry or sales program. This field is a relationship field.

**Relationship Name**
Progress

**Refers To**
LearningItemProgress

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The date that the learning item was assigned to the user or group.

You can assign a learning item to a user programmatically by querying the program and user, and then inserting a record into
LearningItemAssignment.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemAssignmentOwnerSharingRule on page 65 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemAssignmentShare on page 67 (API version 60.0)**
Sharing is available for the object.


### Standard Objects LearningItemProgress LearningItemProgress

Represents the progress that a user has made towards completing an assigned learning item, such as a Learning Paths entry or Enablement
program. This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CompletedDate

CompletedOnDay

CompletedPercent

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the user completed the learning item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the learning item.

**Type**
percent

**Properties**
Filter, Sort

**Description**
Percentage of the learning item that’s complete.


Standard Objects LearningItemProgress

**Field** **Details**

```
DaysInProgress

LearningItemId

OwnerId

ProgressStatus

```

**Type**
int

**Properties**
Nillable

**Description**
Number of days that have elapsed since the learning item was assigned.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the learning item. This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the learning item assignment. Possible values are:

**•** `Behind`

**•** `Completed`


### Standard Objects LearningItemSubmission

**Field** **Details**

**•** `CompletedLate`

**•** `CompletedOnTime`

**•** `InProgress`

**•** `NoLongerTracking`

**•** `NotStarted`

**•** `OnTrack`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

```
StartDate

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a user starts a Trailhead exercise in a sales program.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemProgressChangeEvent on page 68**
Change events are available for the object.

**LearningItemProgressOwnerSharingRule on page 65**
Sharing rules are available for the object.

**LearningItemProgressShare on page 67**
Sharing is available for the object.

### LearningItemSubmission

Represents a link to a resource, such as a video recording, that a user submits as part of a Feedback Request exercise in an Enablement
program. For peer and manager feedback, this resource can be a recording of a user’s sales patch. For Einstein Coach feedback, this
resource can be a video call, and Einstein generates feedback from the call’s transcription. This object is available in API version 59.0 and
later, but Einstein Coach is available only in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LearningItemSubmission

Special Access Rules

A learning item submission record is created when users take an Enablement program that includes a Feedback Request exercise for
peer and manager feedback.

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
CallId

LearningItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the video call that a user submits for Einstein Coach feedback. Einstein generates
feedback for the user based on the call’s transcription. This field is a polymorphic relationship
field.

Available in API version 61.0 and later.

**Relationship Name**
Call

**Relationship Type**
Lookup

**Refers To**
VideoCall

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise, where the `Type` of
the learning item is `LearningPractice` . This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup


### Standard Objects LearningItemType

**Field** **Details**

**Refers To**
### LearningItem

```
OwnerId

Url

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the learning item submission. This field is a polymorphic relationship
field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
URL of the content that a user submits for peer and manager feedback. For example, a link
to a video recording of a sales rep’s practice pitch.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemSubmissionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**LearningItemSubmissionShare on page 67**
Sharing is available for the object.

### LearningItemType

Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom exercise
type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition and
EnblProgramTaskSubCategory records for when admins create a program in Program Builder. This object is available in API version 62.0
and later.


Standard Objects LearningItemType

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

Important: Custom exercises aren’t compatible with Partner Enablement programs.

Fields

**Field** **Details**

```
ApexEvaluationHandlerId

ApexSerializerDeserializerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how progress and completion of the custom exercise
is assessed when users take the program in the Guidance Center.

This field is a relationship field.

**Relationship Name**
ApexEvaluationHandler

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how data related to the custom exercise type is retrieved
and deployed with change sets or managed packages.

This field is a relationship field.

**Relationship Name**
ApexSerializerDeserializer

**Refers To**
ApexClass


Standard Objects LearningItemType

**Field** **Details**

```
CustomField

CustomObject

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of a custom lookup field on the LearningItem object that references
the custom object used with this custom exercise. Add values to this picklist when you
implement a custom exercise type.

For example, if a custom exercise type shows a screen flow, maybe the custom object’s name
is `ScreenFlow_Object__c` and the custom field on LearningItem is named
`ScreenFlow_Field__c` [. For details, see Implement Custom Exercise Types for](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with Enablement Developer_
_Guide_ .

This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of the custom object used with this custom exercise. Add values
to this picklist when you implement a custom exercise type.

For example, if a custom exercise type shows a Quip document, maybe the custom object’s
name is `ScreenFlow_Object__c` [. For details, see Implement Custom Exercise Types](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with Enablement Developer_
_Guide_ .

This field is unique within your organization.

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


Standard Objects LearningItemType

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
Icon

Language

LightningComponentName

MasterLabel

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The icon to use for the custom exercise type in the Guidance Center.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon categories
[and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name, including the namespace, of the Lightning Web Component (LWC) used to show
the custom exercise’s content when a user opens the exercise in the Guidance Center. For
example, if the LWC for a screen flow custom exercise is named `screenFlowViewer`,
this value is `c:screenFlowViewer` .

This field can only be accessed from Metadata API and its value is derived from the
`lightningComponentDefinition` [field on the LearningItemType metadata type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this LearningItemType value. This display value is the internal label that doesn't get
translated.


### Standard Objects LearningPractice

**Field** **Details**

```
NamespacePrefix

### LearningPractice

```

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

Represents a Feedback Request exercise in an Enablement program. Users can submit a sample of their work and request feedback from
their peers and managers. Or, users can submit a video call and Einstein Coach generates feedback from the call’s transcription. This
object is available in API version 59.0 and later, but Einstein Coach feedback is available only in API version 61.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.


Standard Objects LearningPractice

Fields

**Field** **Details**

```
Description

InviteeQuantity

LearningItemId

Name

```

**Type**
string

**Properties**
Filter, Sort

**Description**
Instructions to the user to provide context for completing the Feedback Request exercise.
For example, `Record yourself giving a sales pitch and request`

```
  feedback from your peers.

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of peers or managers that the user is required to invite for giving feedback when
`Type` is `PeerFeedback` . Each peer or manager receives an invitation to the assessment
survey associated with the Feedback Request exercise.

When `Type` is `AIFeedback`, this value is always `1` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise. The value must be
unique. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the Feedback Request exercise. For example, `Practice Your Sales`
`Pitch` .


Standard Objects LearningPractice

**Field** **Details**

```
PromptTemplate

SurveyId

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prompt template to use with this exercise when `Type` is `AIFeedback` .

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the assessment survey that’s sent to peers and managers when `Type` is
`PeerFeedback` . This field is a relationship field.

**Relationship Name**
Survey

**Relationship Type**
Lookup

**Refers To**
Survey

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of feedback used with this exercise. Possible values are:

**•** `AIFeedback` —Users submit a video call, and Einstein Coach generates feedback from
the call’s transcription. With this type, `PromptTemplate` is required. Available in API
version 61.0 and later.

**•** `PeerFeedback` —Users submit a URL to a sample of their work, and select peers and
managers to review their work. Selected peers and managers complete an assessment
survey. With this type, `SurveyId` is required. Available in API version 61.0 and later.

**•** `Survey` —Users complete a survey as part of their enrolled employee enablement
program. Available in API version 64.0 and later.


### Standard Objects LegalEntity LegalEntity

Represents the way an organization is structured. An organization can be a single legal entity or it can comprise more than one legal
entity. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with the Salesforce Billing managed package and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_legalentity.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_legalentity.htm)

Fields

**Field** **Details**

```
CompanyName

Description

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that this legal entity represents.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the legal entity.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime


Standard Objects LegalEntity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

```
LegalEntityAddress

Name

OwnerId

Status

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the company that this legal entity represents. This field is a compound field
of type Address and combines these fields: LegalEntityCity, LegalEntityCountry,
LegalEntityGeocodeAccuracy, LegalEntityLatitude, LegalEntityLongitude,
LegalEntityPostalCode, LegalEntityState, and LegalEntityStreet. For more information, see
[Address Compound Fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/compound_fields_address.htm)

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the legal entity.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the legal entity.

Possible values are:

**•** `Active`

**•** `Inactive`


### Standard Objects LicenseDefinitionCustomPermission (Developer Preview)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**LegalEntityFeed**

Feed tracking is available for the object.

**LegalEntityHistory**

History is available for tracked fields of the object.

**LegalEntityOwnerSharingRule**

Sharing rules are available for the object.

**LegalEntityShare**

Sharing is available for the object.

### LicenseDefinitionCustomPermission (Developer Preview)

Represents a licensed custom permission that controls access to a license's features when included in a custom permission set license
definition. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access LicenseDefinitionCustomPermission, you must have the Partner Licensing Platform developer preview enabled. To participate
[in this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)
group.

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

Fields

**Field** **Details**

```
LicenseDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the custom permission set license definition that contains the licensed custom
permission.

This is a relationship field.


### Standard Objects LightningErrorEventLog

**Field** **Details**

**Relationship Name**
LicenseDefinition

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicenseDefinition

```
LicensedCustomPermissionId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the licensed custom permission that you're including in the permission set license
definition. On the CustomPermission object, the `isLicensed` field must equal true.

This is a relationship field.

**Relationship Name**
LicensedCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.260.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)

### LightningErrorEventLog

Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile app.
This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LightningErrorEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.


Standard Objects LightningErrorEventLog

**Field** **Details**

```
ClientIp

ComponentName

ConnectionType

DeviceIdentifier

DeviceModel

DevicePlatform

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the standard component that generated the error. The Salesforce
developer assigned the name when the standard component was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
string


Standard Objects LightningErrorEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

```
DeviceSessionIdentifier

ErrorMessage

LoginKey

MobileSdkAppType

MobileSdkVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. If the user reloads a page,
it starts a new session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile application type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile SDK version number.


Standard Objects LightningErrorEventLog

**Field** **Details**

```
OperatingSystemName

OperatingSystemVersion

PageAppName

PageContext

PageObjectIdentifier

PageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name.

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Context of the page where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique entity ID of event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningErrorEventLog

**Field** **Details**

**Description**
The entity type of event

```
PageStartTime

PageUrl

PreviousPageUrl

RequestIdentifier

SdkAppVersion

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time when page was initially loaded

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number.


Standard Objects LightningErrorEventLog

**Field** **Details**

```
SessionKey

StackTrace

Timestamp

UiEventIdentifier

UiEventSequenceNumber

UiEventSource

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stack trace contains the location in the code where the error occurred along with the
calling frames that led to the error.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Example**

```
  20130715233322.670

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Lightning event type.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sequence number of current event since start of session.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningErrorEventLog

**Field** **Details**

**Examples**
Here are some examples of error flags returned in this field.

**•** `AuraError`

**•** `Error`

**•** `InvalidStateError`

**•** `RangeError`

**•** `ReferenceError`

**•** `SecurityError`

**•** `SyntaxError`

**•** `TypeError`

**•** `unknown`

```
UiEventTimestamp

UiEventType

UserAgent

UserIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time at which this event occurred, measured in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of error event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.


### Standard Objects LightningExperienceTheme

**Field** **Details**

```
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

### LightningExperienceTheme

Represents information for a theme in Lightning Experience. This object is available in API Version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DefaultBrandingSetId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the default branding set.

This is a relationship field.

**Relationship Name**
DefaultBrandingSet

**Relationship Type**
Lookup

**Refers To**
BrandingSet

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the theme. Limit: 1,000 characters.


Standard Objects LightningExperienceTheme

**Field** **Details**

```
DeveloperName

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the theme in the API. This name can contain only underscores and
alphanumeric characters and must be unique in your organization. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. The label corresponds to the theme name in the user interface. Limit: 70
characters.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Language of the label. Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexico)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese (Brazil))

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


### Standard Objects LightningLoggerEventLog

**Field** **Details**

```
MasterLabel

NamespacePrefix

ShouldOverrideLoadingImage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the theme. Specify up to 70 characters.

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
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a custom image overrides the Salesforce loading image ( `true` ) or not
( `false` ).

### LightningLoggerEventLog

Lightning Logger Event Log provides information from observed Lightning component logs. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects LightningLoggerEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s browser version in major.minor format. Some browsers don’t provide a minor
version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of <Country>/<State|Province>.

**Type**
string


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

```
ClientIp

ConnectionType

DeviceModel

DevicePlatform

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.Possible values are:

**•** CDMA1x

**•** CDMA

**•** EDGE

**•** EVDO0

**•** EVDOA

**•** EVDOB

**•** GPRS

**•** HRPD

**•** HSDPA

**•** HSUPA

**•** LTE

**•** WIFI

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model. For example: iPad, iPhone.

**Type**
string


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in name:experience:form format. Possible values are:

Name

**•** APP_BUILDER

**•** CUSTOM

**•** S1

**•** SFX

Experience

**•** BROWSER

**•** HYBRID

Form

**•** DESKTOP

**•** PHONE

**•** TABLET

```
DeviceSessionIdentifier

LoginKey

Message

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session is based on page load time. When the user reloads
a page, a new session starts. For example: 321a1ddfaf924803a075f1e69fc87bc06f53ccd0

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
Filter, Nillable, Sort


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Description**
The message is passed to the `lightning/logger log()` method. The message can
be a JSON object or a string.

```
MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type. Possible Values:

**•** HYBRID

**•** HYBRIDLOCAL

**•** HYBRIDREMOTE

**•** NATIVE

**•** REACTNATIVE

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number. For example, 5.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from the `User Agent` . For example:

**•** Android

**•** iOS

**•** OSX

**•** Windows

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from the `User Agent` .


Standard Objects LightningLoggerEventLog

**Field** **Details**

```
PageContext

PageObjectIdentifier

PageObjectType

PageUrl

RequestIdentifier

SdkAppVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: 0013000000I3zJAAAZ.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: task, contacts.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl` . For example: /sObject/0064100000JXITSAA5/view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string


Standard Objects LightningLoggerEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app version used in this request.

```
SessionKey

Timestamp

UiRootActivityIdentifier

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

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
The ID for the root activity, if any, when this message was logged.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects LightningOnboardingConfig

**Field** **Details**

**Description**
Type of user employing Salesforce services, whether through the UI or API.

### LightningOnboardingConfig

Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the question,
how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in Lightning Experience
Setup. Available in API version 47.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

[See Switch to Salesforce Classic Feedback Form in Salesforce Help for more details.](https://help.salesforce.com/articleView?id=lex_encourage_work_feedback.htm&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

CustomQuestion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Chatter Group where the user feedback is posted.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the custom question added by the admin. Maximum of 1,000 characters.


Standard Objects LightningOnboardingConfig

**Field** **Details**

```
DeveloperName

FeedbackFormDaysFrequency

IsCustom

Language

MasterLabel

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

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days between showing the feedback form when a user switches. A value of
`0` indicates that the form is shown for every switch. Maximum of 30.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if a feedback form includes a custom question `yes` or not `no` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the feedback form was created.

**Type**
string


### Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the prompt. Maximum of 80 characters.

```
PromptDelayTime

SendFeedbackToSalesforce

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the amount of time in seconds to delay between instances of all prompts, both
org- and Salesforce-created. Minimum of 0 hours and 0 minutes. Maximum of 99 hours and
59 minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the user feedback can be shared with Salesforce. If `yes`, share the feedback with
Salesforce. If `no`, the feedback is only shared in the Chatter Group chosen when customizing
the form. The default value is `false` .

### LightningPageViewEventLog

Lightning Page View event logs represent information about the page on which the event occurred in Lightning Experience and the
Salesforce mobile app. A Lightning Page View event log tracks the page a user visited, how long the user spent on the page, and the
load time for the page. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LightningPageViewEventLog

Fields

**Field** **Details**

```
AppName

BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed. For example: Chrome, IE, Safari, Gecko.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of <Country>/<State|Province>. For example:
`United States/California` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
IP address of the client employing salesforce.com services.

```
ConnectionType

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

Possible values are:

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DeviceIdentifier`
is a generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model. For example: `iPad`, `iPhone` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
DevicePlatform

DeviceSessionIdentifier

DoesEffectivePageTimeDeviate

Duration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format. Possible values
are:

Name

**•** `APP_BUILDER`

**•** `CUSTOM`

**•** `S1`

**•** `SFX`

Experience

**•** `BROWSER`

**•** `HYBRID`

Form

**•** `DESKTOP`

**•** `PHONE`

**•** `TABLET`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started. For example:
`321a1ddfaf924803a075f1e69fc87bc06f53ccd0` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When a deviation is detected, `DoesEffectivePageTimeDeviate` records `true` .
The default value is `false` .

**Type**
double


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The duration in milliseconds since the page start time.

This field is being deprecated. Use `EffectivePageTime` instead.

```
EffectivePageTime

EffectivePageTimeErrorType

EffectivePageTimeReason

GrandparentUiElement

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how many milliseconds it took for the page to load before a user could interact
with the page’s functionality. Multiple factors can affect effective page time, such as network
speed, hardware performance, or page complexity. If an effective page time greater than 60
seconds is detected, the value of this field is set to `null` or `0` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the origin of an error. This field is populated when
EFFECTIVE_PAGE_TIME_DEVIATION_REASON contains the PAGE_HAS_ERROR value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason for deviation in page loading time.

Examples of possible values include:

**•** `PageInDom`  - The page was loaded from a cache

**•** `PageHasError`  - An undefined page loading error occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The grandparent scope of the page element where the event occurred.


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
LoginKey

MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
string

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
String

**Description**
The mobile SDK application version number.

**Example**
5.0

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `UserAgent` . For example: `Android`, `iOS`,
`OSX`, `Windows` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `UserAgent` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
PageAppName

PageContext

PageObjectIdentifier

PageObjectType

PageStartTime

PageUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the application that the user accessed from the App Launcher. For
example: `LightningSales` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
`clients:cardsContainer` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: `0013000000I3zJAAAZ` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: `task`, `contacts` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the page was initially loaded, measured in milliseconds. For example:
`1471564788642` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningPageViewEventLog

**Field** **Details**

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl` . For example:
`/sObject/0064100000JXITSAA5/view` .

```
ParentUiElement

PreviousPageAppName

PreviousPageContext

PreviousPageObjectIdentifier

PreviousPageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent scope of the page element where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the previous application that the user accessed from the App Launcher.
For example: `LightningSales` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context of the previous page where the event occurred. For example:
`clients:cardsContainer` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique previous page object identifier of the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The previous page object type of the event. For example: `task`, `contacts` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
PreviousPageUrl

RequestIdentifier

SdkAppVersion

SessionKey

TargetUiElement

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened. For example: `/sObject/006410000` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK application version number. For example: `5.0` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started. For example: `cdd09305cb6babf34059e27f70e47f1b11dec868` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The target page element where the event occurred. For example: `label bBody`
`truncate`, `tabitem-link` .


Standard Objects LightningPageViewEventLog

**Field** **Details**

```
Timestamp

UiEventSequenceNumber

UiEventTimestamp

UserAgent

UserIdentifier

UserType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The numeric code for the type of client used to make the request (for example, the browser,
application, or API) as a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API. For
example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

Possible values are:

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

### LightningPrfmEventLog

Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This object is available in
API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AppName

```

**Type**
string


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

```
BrowserName

BrowserVersion

ClientGeolocation

ClientIdentifier

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
ConnectionType

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

```
DevicePlatform

DeviceSessionIdentifier

Duration

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The duration in milliseconds since the page start time.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Example**

```
                   GeJCsym5eyvtEK2I

```

```
MobileSdkAppType

MobileSdkVersion

OperatingSystemName

OperatingSystemVersion

PageStartTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `USER_AGENT` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects LightningPrfmEventLog

**Field** **Details**

**Description**
The time when the page was initially loaded, measured in milliseconds.

```
PageUrl

PreviousPageUrl

RequestIdentifier

SdkAppVersion

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened.

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
Mobile SDK application version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hash of the session ID to allow tracking of all events in a session.


Standard Objects LightningPrfmEventLog

**Field** **Details**

```
Timestamp

UiEventIdentifier

UiEventSource

UiEventTimestamp

UiEventType

UserAgent

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Id of the Lightning event type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source of the performance event.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp of when event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of performance event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The client user agent string.


### Standard Objects LightningToggleMetrics

**Field** **Details**

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

For example: `00530000009M943`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

### LightningToggleMetrics

Represents users who switched from Lightning Experience back to Salesforce Classic. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
Action

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User switched from Lightning Experience to Salesforce Classic or from Salesforce
Classic to Lightning Experience.


### Standard Objects LightningUsageByAppTypeMetrics

**Field Name** **Details**

```
MetricsDate

RecordCount

UserId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user switched.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of user switches.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who switched.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### LightningUsageByAppTypeMetrics

Represents number of users on Lightning Experience and Salesforce Mobile. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.


### Standard Objects LightningUsageByBrowserMetrics

Fields

**Field Name** **Details**

```
AppExperience

MetricsDate

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s app (Lightning Experience or Salesforce Mobile).

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user accessed Lightning Experience or Salesforce Mobile.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId for user accessing Lightning Experience or Salesforce Mobile.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### LightningUsageByBrowserMetrics

Represents Lightning Experience usage grouped by user’s browser. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects LightningUsageByPageMetrics

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
Browser

MetricsDate

PageName

TotalCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Browser used to access Lightning Experience.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user accessed Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Page user viewed in Lightning Experience.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of pages accessed in Lightning Experience.

### LightningUsageByPageMetrics

Represents standard pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects LightningUsageByPageMetrics

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
MetricsDate

PageName

TotalCount

UserId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user viewed page in Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of page user viewed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of pages viewed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who viewed page.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects LightningUsageByFlexiPageMetrics

See Also

For more information about `LightningUsageByPageMetrics` [syntax and considerations, see REST API Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_lightning_usagebypagemetrics.htm)
[Lightning Usage by Page.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_lightning_usagebypagemetrics.htm)

### LightningUsageByFlexiPageMetrics

Represents custom pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
FlexiPageNameOrId

FlexiPageType

MetricsDate

TotalCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name or Id of custom page user viewed in Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Custom page type.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user viewed page in Lightning Experience.

**Type**
int


### Standard Objects LightningExitByPageMetrics

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of custom pages viewed.

### LightningExitByPageMetrics

Represents frequency metrics about the standard pages within which users switched from Lightning Experience to Salesforce Classic.
This object is available in API version 44.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Not available in sandbox orgs.

Fields

**Field Name** **Details**

```
MetricsDate

PageName

RecordCount

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date that the data was recorded.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the page from which the user switched from Lightning Experience
to Salesforce Classic.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects LinkedArticle

**Field Name** **Details**

**Description**
The number of records per user and page.

```
UserId

### LinkedArticle

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of the user who views page.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents a knowledge article that is attached to a work order, work order line item, or work type. This object is available in API version
37.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Knowledge must be enabled in your org. Field Service must be enabled. Only users that have access to the Knowledge article and the
parent record linked to it can access this object.

In Knowledge in Salesforce Classic, only Field Service objects such as Work Order, Work Type, and Work Order Line Item are supported
for linked articles. In Lightning Knowledge, other social objects such as Chat, Messaging, Voice Call, and Social Post are supported for
linked articles.

To call `update()` to attach or detach articles, enable the Read user permission on the Knowledge object and the Edit user permission
on the object whose article you update. Available in API version 58.0 and later.


Standard Objects LinkedArticle

Fields

**Field Name** **Details**

```
CurrencyIsoCode

KnowledgeArticleId

KnowledgeArticleVersionId

LinkedEntityId

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Knowledge article attached to the record. The label in the user
interface is Knowledge Article ID.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The version of the Knowledge article attached to the record. This field lists the
title of the attached version and links to the version. The label in the user interface
is Article Version.

When you attach an article to a work order, that version of the article stays
associated with the work order, even if later versions are published. If needed,
you can detach and reattach an article to a work order to link the latest version.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that the Knowledge article is attached to. The label in the
user interface is Linked Record ID.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects LinkedArticleFeed

**Field Name** **Details**

**Description**
The title of the article. The label in the user interface is Article Title.

```
RecordTypeId

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the article’s record type, if used. This field is only available for Lightning
Knowledge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of record that the Knowledge article is attached to. For
example, work order. The label in the user interface is Linked Object Type.

Admins can customize linked articles’ page layouts, fields, validation rules, and more from the Linked Articles page in Setup.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LinkedArticleChangeEvent (API version 62.0)**
Change events are available for the object.

### **LinkedArticleFeed**

Feed tracking is available for the object.

**LinkedArticleHistory**

History is available for tracked fields of the object.

### LinkedArticleFeed

Represents the comment feed on a linked article. This object is available in API version 39.0 and later.

For additional information about feeds, see FeedItem on page 2549.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects LinkedArticleFeed

Special Access Rules

Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
BestCommentId

Body

CommentCount

InsertedById

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

**Type**
textarea

**Properties**
Nillable, Sort

**Description**
The body of the feed item. Required when `Type` is `TextPost` or `AdvancedTextPost` .
Optional when `Type` is `ContentPost` or `LinkPost` .

Although a value for `Body` is not required for the `ContentPost` type, an attachment
is required. If an attachment isn’t present, the type changes to `TextPost` or
`AdvancedTextPost`, depending on the API version. `TextPost` and
`AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the body of
rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.


Standard Objects LinkedArticleFeed

**Field** **Details**

```
IsRichText

LikeCount

LinkUrl

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text feed comment
using SOAP API, set `IsRichText` to `true` and escape HTML entities from the body.
Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a plain-text
representation.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Nillable, Sort


Standard Objects LinkedArticleFeed

**Field** **Details**

**Description**
The URL of a `LinkPost` .

```
ParentId

RelatedRecordId

Title

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object type to which the feed item is related. For example, set this field to a `UserId`
to post to someone’s profile feed, or an `AccountId` to post to a specific account.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC thanks posts,
it’s the ID of the WorkThanks object associated with a `RypplePost` . This field is typically
null for all posts except `ContentPost` and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed with `Type`
set to `ContentPost` .

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is the URL and
this field is the link name. The `Title` field can be updated on posts of `Type`
`QuestionPost` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`, and `TextPost`, don’t
create feed items of other types directly from the API.

**•** `ActivityEvent` —indirectly generated event when a user or the API adds a Task
associated with a feed-enabled parent record (excluding email tasks on cases). Also
occurs when a user or the API adds or updates a Task or Event associated with a case
record (excluding email and call logging).


Standard Objects LinkedArticleFeed

**Field** **Details**

For a recurring Task with CaseFeed disabled, one event is generated for the series only.
For a recurring Task with CaseFeed enabled, events are generated for the series and each
occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement and, in
Lightning Experience as of API version 39.0 and later, when a user shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric or gauge
exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a dashboard
snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post. Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply only to
CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through the user
interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment for a case
object.

**•** `ChangeStatusPost` —generated event when a user changes the status of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved to a case.

**•** `EmailMessageEvent` —generated event when an email related to a case object is
sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or reaches
violation status.


### Standard Objects LinkedArticleHistory

**Field** **Details**

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData` and
`ContentFileName` .

### LinkedArticleHistory

Represents the history of changes made to tracked fields on a linked article. This object is available in API version 37.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

Knowledge must be enabled in your org.

Fields

**Field Name** **Details**

```
DataType

Field

LinkedArticleId

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
reference

**Properties**
Filter, Group, Sort


### Standard Objects ListEmail

**Field Name** **Details**

**Description**
The ID of the tracked linked article. The history is displayed on the detail page for
this record.

```
NewValue

OldValue

### ListEmail

```

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

Represents a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. When the list email is sent, the
recipients are generated by combining recipients in ListEmailIndividualRecipients and ListEmailRecipientSource. Duplicate and other
invalid recipients are removed. The result is the recipients sent any given list email. ListEmail has a one-to-many relationship with
### ListEmailRecipientSource and ListEmailIndividualRecipient. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the action cadence step that generated a list email record. Used for automated
emails in Sales Engagement.


Standard Objects ListEmail

**Field** **Details**

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

This field is available in API version 54.0 and later.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
CampaignId

ClickThroughRate

ClickToOpenRatio

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related campaign.

This field is available in API version 42.0 and later.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of visitors who click links contained in emails delivered (sent minus bounces)
to them. Multiple clicks for a same link are counted.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects ListEmail

**Field** **Details**

**Description**

The number of unique clicks divided by unique HTML opens.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

```
DeliveryRate

EmailContentId

FromAddress

FromName

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of the emails that were delivered compared to the number that bounced
(soft and hard). Note: this data includes emails that were delivered to the recipient's spam
folder.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the email content record associated with the list email.

This field is available in API version 50.0 or later. To access this field, your org must use Account
Engagement and users need the CRM User or Sales User permission set.

**Type**
textarea

**Properties**
Create, Filter, Update

**Description**
Read-only except when the list email is in a draft state. Validated against user’s addresses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Read-only except when the list email is in a draft state. Validated against user’s addresses.
This field is null for emails sent from Account Engagement.


Standard Objects ListEmail

**Field** **Details**

```
HasAttachment

HtmlBody

IsTracked

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Defaulted on create and update. Value is `true` if the list email has an attachment.
This field is null for emails sent from Account Engagement.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the list email. This field is null for emails sent from Account Engagement.

List emails can contain up to 32,000 characters for the body. These limits include visible
characters and other characters in the email, including markup.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if email tracking was on when the list email was sent. This field is blank for emails
sent from Account Engagement and synced to Salesforce. This field is null for emails sent
from Account Engagement.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when the current user last viewed a record that is related to
this list email. This field is null for emails sent from Account Engagement.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed. This
field is null for emails sent from Account Engagement.


Standard Objects ListEmail

**Field** **Details**

```
Name

OpenRate

OptOutRate

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Read-only except when the list email is in a draft state.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of unique HTML opens compared to the total number of emails delivered
(sent minus bounces).

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of users that have opted out compared to the total number of emails sent.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
References Group and User. This field is null for emails sent from Account Engagement.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects ListEmail

**Field** **Details**

```
ProgramName

ScheduledDate

SentVia

SpamComplaintRate

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**

The name of an Engagement Studio program where an automated email originates. Reserved
for future use.

This field is available in API version 46.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
dateTime

**Properties**
CreateFilter, Nillable, Sort, Update

**Description**
Read-only. If null and `Status` is set to Scheduled` defaults to created time.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates whether the email was sent from Salesforce or Account Engagement. The allowed
values are `Salesforce` or `Pardot` or `MessagingService` .

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of spam complaints compared to the total number of emails sent.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects ListEmail

**Field** **Details**

**Description**
Read-only except when the list email is in a draft state.

Changing the status to Scheduled causes the list email to be sent.

Valid values:

**•** `Draft`

**•** `Scheduled`

**•** `Sent`

**•** `Limit Error`

**•** `Canceled`

**•** `Running`

```
Subject

TextBody

TotalDelivered

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
Read-only except when the list email is in a draft state. This field is null for emails sent from
Account Engagement.

List emails can contain up to 3,000 characters for the subject. These limits include visible
characters and other characters in the email, including markup.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Read-only except when the list email is in a draft state. This field is null for emails sent from
Account Engagement.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The total number of emails minus hard and soft bounces. Note: this data includes emails
that were delivered to the recipient's spam folder.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


Standard Objects ListEmail

**Field** **Details**

```
TotalHardBounced

TotalOpens

TotalOutOfOffice

TotalReplies

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of emails that permanently bounced back to the sender because the
address is invalid. A hard bounce can occur because the domain name doesn't exist or
because the recipient is unknown.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a prospect’s email client loaded the images in the HTML version
of the email. We also record an open if the prospect clicks a link within the HTML or text
email without downloading images. A click indicates that they viewed the message. Some
email clients (Outlook, Apple Mail, Thunderbird) don’t display images by default. Account
Engagement counts an open each time the images load.

This field is available in API version 41.0 and later. To access this field. users need the Sales
Engagement User permission set or your org must use Account Engagement and users need
the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of replies received with an out-of-office message.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of replies received.


Standard Objects ListEmail

**Field** **Details**

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

```
TotalSent

TotalSoftBounced

TotalSpamComplaints

TotalTrackedLinkClicks

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only. The total number of list emails sent, including bounced, opted-out, and invalid
To: addresses.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a recipient’s mail server acknowledged the email, but returned it
to the sender. Sometimes it is because the recipient's mailbox is full or the mail server is
temporarily unavailable. A soft bounce message can sometimes be deliverable at another
time. After 5 soft bounces, Account Engagement opts the prospect out of emails.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of prospects that reported the email as spam.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times prospects clicked a link in the email.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


Standard Objects ListEmail

**Field** **Details**

```
Type

UniqueClickThroughRate

UniqueOpens

UniqueOptOuts

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

The type of email sent: list email or automated email. Reserved for future use.

This field is available in API version 46.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of visitors who clicked a link contained in an email.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of prospects who loaded the images in the HTML version of the email. The
Unique Opens category counts each recipient one time only, even if the prospect loaded
images several times.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Unique opt-outs represent the total number of prospects that have clicked the link to
unsubscribe or opted out of all emails in the Email Preference Center. These prospects are
removed from future email sends.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.


### Standard Objects ListEmailIndividualRecipient

**Field** **Details**

```
UniqueReplies

UniqueTrackedLinkClicks

```

Associated Objects

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique replies.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the Salesforce Engage permission set.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of times a prospect clicked a link in the email. This metric doesn’t include multiple
clicks of the same link.

This field is available in API version 41.0 and later. To access this field, your org must use
Account Engagement and users need the CRM User or Sales User permission set.

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ListEmailOwnerSharingRule**

Sharing rules are available for the object.

**ListEmailShare**

Sharing is available for the object.

### ListEmailIndividualRecipient

For a list email in Salesforce, represents a recipient. Each record represents a link from a list email to exactly one recipient for that list
email. Recipients can be contacts, leads, or campaign members. Has a one-to-many relationship with ListEmail. This object is available
in API version 44.0 and later.

The visibility and accessibility of this object is inherited from the related list email.


Standard Objects ListEmailIndividualRecipient

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionCadenceStepTrackerId

CurrencyIsoCode

ListEmailId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Understand which action cadence step tracker the list email individual recipient is related
to. Used for automated emails in Sales Engagement.

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

This field is available in API version 54.0 and later.

**Relationship Name**
ActionCadenceStepTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR` (Euro)

**•** `INR` (Indian Rupee)

**•** `USD` (US Dollars)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.


### Standard Objects ListEmailMonthlyMetric

**Field** **Details**

This is a relationship field.

**Relationship Name**
### ListEmail

**Relationship Type**
Lookup

**Refers To**
### ListEmail

```
Name

RecipientId

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the list email recipient source.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
the contact, lead, person account, or campaign member ID of the individual list email recipient.

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
CampaignMember, Contact, Lead

### ListEmailMonthlyMetric

Represents the monthly engagement metrics for a single list email. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ListEmailMonthlyMetric

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsOpenedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard and soft bounces that were triggered for this list email in the month.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received this list email in the month.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard bounces that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by the recipients of this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Description**
The number of recipients who opened this list email in the month.

```
AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

HardBounceTrackableSends

LinkClickTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of out-of-office replies that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies to this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients to whom this list email was sent in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total soft bounces that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with hard bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
int


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with link click tracking in the month.
Available in API version 53.0 and later.

```
ListEmailId

Month

MonthInt

OpenTrackableSends

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related list email.

This field is a relationship field.

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with open tracking in the month.
Available in API version 53.0 and later.


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

```
OutOfOfficeTrackableSends

ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with out-of-office tracking in the
month. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with reply tracking in the month.
Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with soft bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with hard bounce tracking, resulted
in a hard bounce in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who clicked on a link in this list email that was sent with link
click tracking in the month. Available in API version 53.0 and later.

This field is a calculated field.


Standard Objects ListEmailMonthlyMetric

**Field** **Details**

```
TrackableSendOpenRate

TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who opened this list email that was sent with open tracking in
the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom the list email, sent with out-of-office tracking, resulted
in an out-of-office reply in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with reply tracking, resulted in a
reply in the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with soft bounce tracking, resulted
in a soft bounce in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ListEmailRecipientSource

**Field** **Details**

**Description**
The number of unique recipients who clicked a link in this list email in the month.

```
UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to this list email in the month.

### ListEmailRecipientSource

For a list email in Salesforce, represents the dynamically defined sources of recipient email addresses. Each record represents a link to a
single list view or campaign that is examined when the list email is sent. Has a one-to-many relationship with ListEmail. This object is
available in API version 41.0 and later.

The visibility and accessibility of this object is inherited from the related list email.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `getDeleted()`, `getUpdated()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ListEmailId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.

This is a relationship field.


Standard Objects ListEmailRecipientSource

**Field** **Details**

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

```
Name

SourceListId

SourceType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the list email recipient source.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The id of a list view to send the list email to. Read-only except when list email is
in draft state.

This is a polymorphic relationship field.

**Relationship Name**
SourceList

**Relationship Type**
Lookup

**Refers To**
Campaign, ListView, Topic

**Type**
reference

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Read-only except when list email is in draft state.

Valid values:

**•** Include


### Standard Objects ListView ListView

Represents a list view. A list view shows a set of records for an object, based on specific criteria. This object is available in API version 32.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Fields

**Name** **Details**

```
DeveloperName

IsSoqlCompatible

LastModifiedById

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The fully qualified developer name of the list view.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the list view can be used with SOQL..

**Type**
User

**Properties**
Filter, Sort

**Description**
The ID of the user who last modified the list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last referenced, with a precision of one second.

**Type**
dateTime


### Standard Objects ListViewChart

**Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last viewed, with a precision of one second.

```
Name

NamespacePrefix

SobjectType

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the list view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the list view.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The API name of the sObject for the list view.

Use this object to retrieve the metadata for a pipeline inspection view.

### ListViewChart

Represents a graphical chart that’s displayed on Salesforce for Android, iOS, and mobile web list views. The chart aggregates data that
is filtered based on the list view that’s currently displayed. This object is available in API version 33.0 and later and is accessible by portal
users.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ListViewChart

Fields

**Name** **Description**

```
AggregateField

AggregateType

ChartType

DeveloperName

GroupingField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The field that’s used for calculating data on each group. `AggregateField` can’t be the
same as `GroupingField` .

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The type of calculations to run on each group. The supported `AggregateType` values are
`Count`, `Sum`, and `Avg` .

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist,Retrieve, Sort, Update

**Description**
The type of chart to create. The supported chart types are horizontal bar chart, vertical bar chart,
and donut chart.

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The fully qualified developer name of the chart.

Note: Only users with View DeveloperName OR View Setup and Configuration permission
can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update


Standard Objects ListViewChart

**Name** **Description**

**Description**
The field that’s used to divide the data into collections. The field must be supported by SOQL
`GROUP BY` functionality. `GroupingField` can’t be the same as `AggregateField` .

```
Language

MasterLabel

OwnerId

SobjectType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the `MasterLabel` .

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The label for the chart.

**Type**
reference

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The ID of the user who owns the chart.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort

**Description**
The API name of the sObject for the chart.


### Standard Objects ListViewChartInstance ListViewChartInstance

Retrieves metadata for all standard and custom charts for a given entity in context of a given list view. This object is available in API
versions 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
AggregateField

AggregateType

ChartType

DataQuery

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The field that’s used for calculating data on each group. `AggregateField`
can’t be the same as `GroupingField` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of calculations to run on each group. The supported `AggregateType`
values are `Count`, `Sum`, and `Avg` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of chart to create. The supported chart types are horizontal bar chart,
vertical bar chart, and donut chart.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart.


Standard Objects ListViewChartInstance

**Field Name** **Details**

```
DataQueryWithoutUserFilters

DeveloperName

ExternalId

GroupingField

IsDeletable

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart,
without user filters.

Available in API v43.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the chart. This name can contain only underscores and alphanumeric
characters, and must be unique in your org. It must begin with a letter, not include
spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a
managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The field that’s used to divide the data into collections. The field has to be
supported by SOQL `GROUP BY` functionality. `GroupingField` can’t be the
same as `AggregateField` .

**Type**
boolean


Standard Objects ListViewChartInstance

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the chart can be deleted.

```
IsEditable

IsLastViewed

Label

ListViewChartId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the chart can be edited. Standard charts are not editable.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if a chart is the last viewed by a user.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The display name of the chart.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the chart created by a user. For standard charts, this is null.

This is a relationship field.

**Relationship Name**
ListViewChart

**Relationship Type**
Lookup

**Refers To**
ListViewChart


Standard Objects ListViewChartInstance

**Field Name** **Details**

```
ListViewContextId

SourceEntity

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the list view in context of which the chart is generated. Required to query
`ListViewChartInstance` .

This is a relationship field.

**Relationship Name**
ListViewContext

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the entity to which the chart is related. Required to query
`ListViewChartInstance` .

**Example 1. Retrieve all custom and standard charts for Account entity for All Accounts list view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextId=’00BR0000000U8Hr’

```

**Example 2. Retrieve metadata for a specific custom chart by ID for Account entity and All Accounts list view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextID=’00BR0000000U8Hr’ and ListViewChartId=’0DdR00000004CBxKAM’

```

**Example 3. Retrieve metadata for a specific standard chart by its developer name for Account entity and All Accounts list**
**view**

```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,

   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,

  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’

   and ListViewContextID=’00BR0000000U8Hr’ and DeveloperName=’AccountsByIndustry’

```


### Standard Objects LiveAgentSession LiveAgentSession

This object is automatically created for each Chat session and stores information about the session. This object is available in API versions
28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`

Fields

**Field Name** **Details**

```
AgentId

ChatReqAssigned

ChatReqDeclined

ChatReqEngaged

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the agent associated with the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that were assigned to an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that were declined by an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chats in which an agent was engaged during a session.


Standard Objects LiveAgentSession

**Field Name** **Details**

```
ChatReqTimedOut

LastReferencedDate

LastViewedDate

LoginTime

LogoutTime

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that timed out in an agent’s queue during a session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time an agent logged in during the session.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time an agent logged out during a session.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookupSort

**Description**
The name of the session.


Standard Objects LiveAgentSession

**Field Name** **Details**

```
NumFlagLoweredAgent

NumFlagLoweredSupervisor

NumFlagRaised

OwnerId

TimeAtCapacity

TimeIdle

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the agent.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the supervisor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags raised by the agent.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with the maximum number of chats in his
or her queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects LiveAgentSession

**Field Name** **Details**

**Description**
The amount of time an agent spent idle during the session.

```
TimeInAwayStatus

TimeInChats

TimeInOnlineStatus

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with a status of “Away” during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent engaged in chats during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with a status of “Online” during a session.

Use this object to query and manage chat session records.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LiveAgentSessionHistory**

History is available for tracked fields of the object.

**LiveAgentSessionOwnerSharingRule**

Sharing rules are available for the object.

**LiveAgentSessionShare**

Sharing is available for the object.


### Standard Objects LiveAgentSessionHistory LiveAgentSessionHistory

This object is automatically created for each Chat session and stores information about changes made to the session. This object is
available in API versions 28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
DataType

Field

LiveAgentSessionId

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
The name of the field that was changed in a session record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the session record that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.


### Standard Objects LiveAgentSessionShare

**Field Name** **Details**

```
OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The original value of the field that was changed.

Use this object to identify changes to chat session records.

### LiveAgentSessionShare

This object is automatically created for each Chat session and stores information about the session. This object is available in API versions
28.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field Name** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects LiveAgentSessionShare

**Field Name** **Details**

**Description**
Level of access that the User or Group has to the LiveAgentSession. The possible
values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for chat transcripts.

```
ParentId

RowCause

UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values can include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the LiveAgentSession with them.

**•** `Owner` —The User is the owner of the LiveAgentSession or is in a role above
the LiveAgentSession owner in the role hierarchy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that has been given access to the LiveAgentSession.

This object lets you determine which users and groups can view and edit LiveAgentSession records owned by other users.


### Standard Objects LiveChatBlockingRule

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

### LiveChatBlockingRule

Represents a rule for blocking chat visitors’ IP addresses from starting new chats with agents. This object is available in API version 34.0
and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

To create a new rule, you must be logged in with the “Customize Application” permission or as a system administrator.

Fields

**Field Name** **Details**

```
Description

DeveloperName

```

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the blocking rule—for example, the reason why the given IP
address or range of addresses is being banned from starting new chats.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.


Standard Objects LiveChatBlockingRule

**Field Name** **Details**

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
FromIpAddress

Language

MasterLabel

ToIpAddress

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The IP address of the user that you want to block, or the beginning of the range
of IP addresses you want to block. If you want to block a range of IP addresses,
indicate the end of the range in the `ToIpAddress` field. If you don’t indicate
an IP address in the `ToIpAddress` field, the only IP address that will be blocked
is the IP address in the `FromIpAddress` field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Label for the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
(Optional) The end of the range of IP addresses that you want to block. The range
begins with and includes the IP address in the `FromIpAddress` field, and it
ends with and includes the IP address in the `ToIpAddress` field.

Use this object to query and manage rules for blocking customers from starting new chats with agents.


### Standard Objects LiveChatObjectAccessConfig LiveChatObjectAccessConfig

Represents the action you can perform on a specified object by the Chat API. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.

Fields

**Field** **Details**

```
AccessType

ParentId

SobjectType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The API action you can perform on the object specified in `SobjectType` .

Possible values are:

**•** `Create`

**•** `Find`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated LiveChatObjectAccessDefinition record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
LiveChatObjectAccessDefinition

**Type**
picklist


### Standard Objects LiveChatObjectAccessDefinition

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The object that the action specified by `AccessType` applies to.

Possible values are all standard and custom objects. Custom objects are available as picklist
values in API version 55.0 and later.

SEE ALSO:

### LiveChatObjectAccessDefinition LiveChatObjectAccessDefinition

Represents the parent record for one or more LiveChatObjectAccessConfig objects. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.

Fields

**Field** **Details**

```
DeveloperName

```

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


Standard Objects LiveChatObjectAccessDefinition

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
Language

MasterLabel

```

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

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object's record. This display value is the internal label that doesn’t get
translated.


### Standard Objects LiveChatButton LiveChatButton

Represents a button that allows visitors to request chats with Chat users. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Animation

AutoGreeting

ChasitorIdleTimeout

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of animation used when an automated chat invitation appears on-screen.
For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Appear`

**•** `Custom`

**•** `Fade`

**•** `Slide`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

Note: A greeting message in the `AutoGreeting` field of the
### LiveChatButton object overrides individual users’ greeting messages in

the `AutoGreeting` field in the LiveChatUserConfig object.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before the
chat times out.


Standard Objects LiveChatButton

**Field Name** **Details**

```
ChasitorIdleTimeoutWarning

ChatPageId

CustomAgentName

DeveloperName

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before a
warning appears and a timer begins a countdown. This value must be shorter
than the `ChasitorIdleTimeout` value. We recommend at least 30 seconds
shorter.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page that contains the custom chat
window code.

This field is a relationship field.

**Relationship Name**
ChatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The custom name of the agent associated with the button. Available in API version
29.0 and later.

Note: A custom agent name in the `CustomAgentName` field of the
LiveChatButton object overrides individual users’ custom agent name in
the `CustomAgentName` field in the LiveChatUserConfig object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects LiveChatButton

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

```
HasQueue

InviteEndPosition

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether or not to allow queing incoming chat requests until an
agent is available.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation ends.

Note: You don’t need to select an end position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`

**•** `BottomLeft`

**•** `BottomRight`

**•** `Center`

**•** `Left`

**•** `Right`

**•** `Top`

**•** `TopLeft`


Standard Objects LiveChatButton

**Field Name** **Details**

**•** `TopRight`

```
InviteImageId

InviteStartPosition

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource displayed on your automated chat
invitation. For automated chat invitations only. Available in API version 29.0 and
later.

This field is a relationship field.

**Relationship Name**
InviteImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation begins.

Note: You don’t need to select a start position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`

**•** `BottomLeft`

**•** `BottomLeftBottom`

**•** `BottomLeftLeft`

**•** `BottomRight`

**•** `BottomRightBottom`

**•** `BottomRightRight`

**•** `Left`

**•** `Top`

**•** `Right`

**•** `TopLeft`

**•** `TopLeftLeft`


Standard Objects LiveChatButton

**Field Name** **Details**

**•** `TopLeftTop`

**•** `TopRight` —Top Right

**•** `TopRightRight`

**•** `TopRightTop`

```
IsActive

IsRoutingFlowEnabled

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For automated chat invitations, specifies whether an automated chat invitation
is active or not.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether routing flow is enabled or not.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the chat.

Possible values are:

**•** `da` —Danish

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


Standard Objects LiveChatButton

**Field Name** **Details**

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

NumberOfReroutingAttempts

OfflineImageId

OnlineImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the chat button.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of times a chat request can be rerouted to available agents
if all agents reject the chat request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
offline (inactive).

This field is a relationship field.

**Relationship Name**
OfflineImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
reference


Standard Objects LiveChatButton

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
online (active).

This field is a relationship field.

**Relationship Name**
OnlineImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

```
OptionsHasChasitorIdleTimeout

OptionsHasInviteAfterAccept

OptionsHasInviteAfterReject

OptionsHasRerouteDeclinedRequest

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether Customer Time-Out is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has accepted a prior automated chat invitation ( `true` ) or not
( `false` ). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has rejected a prior automated chat invitation ( `true` ) or not
( `false` ). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean


Standard Objects LiveChatButton

**Field Name** **Details**

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request that has been rejected by all available agents
should be rerouted to available agents again ( `true` ) or not ( `false` ).

```
OptionsIsAutoAccept

OptionsIsInviteAutoRemove

OverallQueueLength

PerAgentQueueLength

PostchatPageId

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request should be automatically accepted by the agent
it’s assigned to ( `true` ) or not `false` ). For chat buttons and automated chat
invitations with `RoutingType` set to `Most Available` or `Least`
`Active` . Available in API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation should be automatically removed
from the screen after a certain amount of time ( `true` ) or not ( `false` ). For
automated chat invitations only. Available in API version 29.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue for each agent with
the required skill.

**Type**
reference


Standard Objects LiveChatButton

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed when the chat ends.

This field is a relationship field.

**Relationship Name**
PostchatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

```
PostchatUrl

PrechatFormPageId

PrechatFormUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to after the chat ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed before the chat begins.

This field is a relationship field.

**Relationship Name**
PrechatFormPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to before the chat begins.


Standard Objects LiveChatButton

**Field Name** **Details**

```
PushTimeout

QueueId

RoutingConfigurationId

RoutingType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds an agent has to answer a chat request before it’s routed
to the next available agent.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the queue used for this chat button.

This field is a relationship field.

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the routing configuration used for this chat button.

This field is a relationship field.

**Relationship Name**
RoutingConfiguration

**Relationship Type**
Lookup

**Refers To**
QueueRoutingConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects LiveChatButton

**Field Name** **Details**

**Description**
How chat requests are routed to agents. The values are:

**•** `Choice` —Incoming chat requests are added to the queue in Live Agent in
the Salesforce console and are available to any agent with the required skill.

**•** `Least Active` —Incoming chats are routed to the agent with the
required skill who has the fewest active chats.

**•** `Most Available` —Incoming chats are routed to the agent with the
required skill and the greatest difference between chat capacity and active
chat sessions. For example, if Agent A and Agent B each have a chat capacity
of five, and Agent A has three active chat sessions while Agent B has one,
incoming chats will be routed to Agent B.

**•** `Omni` —Incoming chats are routed using Omni-Channel queues.

```
SiteId

SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the site used for loading static resources and custom VisualForce
pages.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the skill used to route incoming chat requests. To associate
multiple skills with a chat button, reference one skill in the `SkillId` field and
use LiveChatButtonSkill junction objects for the remaining skills.

This field is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup


Standard Objects LiveChatButton

**Field Name** **Details**

**Refers To**
Skill

```
TimeToRemoveInvite

Type

WindowLanguage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds an automated invitation stays on-screen before it is
automatically removed. For automated chat invitations only. Available in API
version 29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of element to display to customers.

Possible values are:

**•** `Invite` —Automated invitation

**•** `Standard` —Chat button

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for standard chat windows. Custom chat windows use the
language of the user’s browser.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean


### Standard Objects LiveChatButtonDeployment

**Field Name** **Details**

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

Usage

Use this object to query and manage chat buttons and automated chat invitations.

### LiveChatButtonDeployment

Associates an automated chat invitation with a specific deployment. This object is available in API versions 28.0 and later.

Supported Calls

`create()`, `delete()query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
ButtonId

DeploymentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the automated invitation associated with the deployment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the deployment that will feature the automated invitation.


### Standard Objects LiveChatButtonSkill

Usage

Use this object to associate automated chat invitations with specific deployments.

### LiveChatButtonSkill

Represents all the skills available to a LiveChatButton except the one currently assigned. To retrieve the skill currently assigned, query
LiveChatButton. This object is available in API version 25.0 and later.

Supported Calls

`create()`, `delete()`, `update()`, `query()`

Fields

**Field Name** **Details**

```
ButtonID

SkillID

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the button.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.

Use this object to assign a specific skill to a specific button for multi-skill routing. For example:

```
String myButtonId = " button_Id ";

String myButtonDevName = " button_DeveloperName ";

List<String> skillIds = new List<String>();

//Get one skill ID from button

for(LiveChatButton lcb : [SELECT SkillId FROM LiveChatButton WHERE DeveloperName =:

myButtonDevName]) {

   skillIds.add(lcb.SkillId);

}

//Get remaining skills from LiveChatButtonSkill join object

```


### Standard Objects LiveChatDeployment

```
   for(LiveChatButtonSkill lcbs : [SELECT SkillID FROM LiveChatButtonSkill WHERE ButtonId =:

   myButtonId]) {

      skillIds.add(lcbs.SkillId);

   }

   //Retrieve all skills into a single list

   List<Skill> skills = [SELECT Id, DeveloperName FROM Skill WHERE Id IN :SkillIds];

### LiveChatDeployment

```

Represents the general settings for deploying Live Agent on a website. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
BrandingId

ConnectionTimeoutDuration

ConnectionWarningDuration

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource that’s displayed in the chat window.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before the chat times out, in seconds.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before a time-out warning is displayed to the agent,
in seconds.

**Type**
string


Standard Objects LiveChatDeployment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
Domains

HasTranscriptSave

Language

```

**Type**
textarea

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Nillable, Sort (unavailable
in API version 25.0 and later)

**Description**
A comma-separated list of domains the deployment is allowlisted for. Leave this
blank to allow the deployment to be used on any domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether visitors can download and save transcripts from the chat
window.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the deployment.


Standard Objects LiveChatDeployment

**Field Name** **Details**

```
MasterLabel

MobileBrandingId

OptionsHasPrechatApi

SiteId

WindowTitle

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the deployment

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource displayed in the mobile version of the
chat window.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether developers can access the Pre-Chat API.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the site used for loading static resources.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The text displayed in the title bar of the browser window used to launch the chat
window.

Use this object to query and manage live chat deployments.


### Standard Objects LiveChatSensitiveDataRule LiveChatSensitiveDataRule

Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). This object is available in
API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `update()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
ActionType

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action to take on the text (remove or replace) when the sensitive data rule
is triggered.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the sensitive data rule—for example, “Block social security
numbers.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the


Standard Objects LiveChatSensitiveDataRule

**Field Name** **Details**

object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
EnforceOn

IsEnabled

Language

MasterLabel

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Determines the roles on which the rule is enforced. The value is determined
using bitwise OR operation. There are seven possible values:

**1.** Rule enforced on Agent

**2.** Rule enforced on Visitor

**3.** Rule enforced on Agent and Visitor

**4.** Rule enforced on Supervisor

**5.** Rule enforced on Agent and Supervisor

**6.** Rule enforced on Visitor and Supervisor

**7.** Rule enforced on Agent, Visitor, and Supervisor

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a sensitive data rule is active ( `true` ) or not ( `false` ). Default
value (if none is provided) is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the sensitive data rule.

**Type**
string


Standard Objects LiveChatSensitiveDataRule

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the sensitive data rule.

```
NamespacePrefix

Pattern

Priority

Replacement

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
prefix of the org for all objects that support it, unless an object is in an
installed managed package. In that case, the object has the namespace prefix
of the installed managed package. This field’s value is the namespace prefix
of the Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
textarea

**Properties**
Create, Update

**Description**
The pattern of text blocked by the rule. Written as a JavaScript regular expression
(regex).

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the priority level of a Chat.

**Type**
string


### Standard Objects LiveChatTranscript

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The string of characters that replaces the blocked text (if `ActionType`
_`Replace`_ is selected).

Usage

Use this object to mask or delete data of specified patterns, such as credit card, social security, phone and account numbers, or even
profanity.

### LiveChatTranscript

This object is automatically created for each Live Agent chat session and stores information about the session. This object is available in
API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Abandoned

AccountId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time in seconds an incoming chat request remained unanswered
by an agent before the chat was disconnected by the customer.

**Type**
ID

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with the chat transcript.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
AverageResponseTimeOperator

AverageResponseTimeVisitor

Body

Browser

BrowserLanguage

CaseID

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent’s average response time (in seconds) to chat messages from the visitor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s average response time (in seconds) to chat messages from the agent.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The browser the visitor used for the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The language of the visitor’s browser.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with the chat transcript.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
ChatDuration

ChatKey

ContactID

EndedBy

EndTime

IpAddress

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total duration of the chat in seconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
The session ID of the chat before it is persisted. `ChatKey` can be used with
advanced integrations in the Salesforce console. This field is available in API
version 25.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact associated with the chat transcript.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The way the chat was ended: by the operator, the visitor, or the system.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat ended.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Description**
The auto-populated visitor’s IP address. Do not edit. Create a custom field if you
need an IP address field for your use case.

```
IsChatbotSession

LastReferencedDate

LastViewedDate

LeadID

LiveChatButtonID

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the visitor is chatting with a chatbot ( `true` ) or not ( `false` ).

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced ( `LastReferencedDate` )
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the lead associated with the chat transcript.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatButton the chat session originated from.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
LiveChatDeploymentID

LiveChatVisitorID

Location

MaxResponseTimeOperator

MaxResponseTimeVisitor

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatDeployment the chat session originated from.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the visitor associated with the chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated best-guess approximation of the visitor’s location. Do not
edit.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took an agent to respond to a chat visitor’s
message.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took a customer to respond to an agent’s
message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Description**
The name of the transcript.

```
OperatorMessageCount

OwnerID

Platform

ReferrerUri

RequestTime

ScreenResolution

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by one or more agents during the chat.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the operator who participated in the chat last; for missed chats, this is
a system user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s operating system platform.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated URI where the chat request originated. Do not edit.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the visitor requested the chat.

**Type**
string


Standard Objects LiveChatTranscript

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s screen resolution.

```
SkillId

StartTime

Status

SupervisorTranscriptBody

UserAgent

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated record ID of the primary Skill associated with the
LiveChatButton the chat session originated from. Do not edit. To associate multiple
skills with a LiveChatTranscript, use LiveChatTranscriptSkill junction objects.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The final status of the chat: completed, missed, or blocked.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The text body of the supervisor’s chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s user agent string.


Standard Objects LiveChatTranscript

**Field Name** **Details**

```
VisitorMessageCount

VisitorNetwork

WaitTime

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by the visitor during the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The network or service provider the chat visitor used for the chat.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total amount of time in seconds a chat request was waiting to be accepted
by an agent.

Use this object to query and manage live chat transcripts.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 44.0)**
Change events are available for the object.

**LiveChatTranscriptFeed (API version 47.0)**
Feed tracking is available for the object.

**LiveChatTranscriptHistory**

History is available for tracked fields of the object.

**LiveChatTranscriptOwnerSharingRule (API version 29.0)**
Sharing rules are available for the object.

**LiveChatTranscriptShare**

Sharing is available for the object.


### Standard Objects LiveChatTranscriptEvent LiveChatTranscriptEvent

Captures specific events that occur over the lifetime of a chat. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
AgentId

Detail

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the agent associated with the event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Details associated with the event.

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
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.


Standard Objects LiveChatTranscriptEvent

**Field Name** **Details**

```
LiveChatTranscriptId

Name

Time

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the live chat transcript associated with the event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the event.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the event happened.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of event that occurred.

**•** `Accept` —Accepted

**•** `AgentBlocked` —Blocked by Agent

**•** `AlertCriticalWaitChat` —Critical Wait Alert Time Reached

**•** `CancelBlocked` —Cancel (Blocked)

**•** `CancelNoAgent` —Cancel (No Agent)

**•** `CancelNoQueue` —Cancel (No Queue)

**•** `CancelVisitor` —Canceled by Visitor

**•** `ChasitorIdleTimeout` —Visitor Idle Time-Out

**•** `ChasitorIdleTimeoutWarningCleared` —Visitor Idle Time-Out
Warning Cleared

**•** `ChasitorIdleTimeoutWarningTriggered` —Visitor Idle Time-Out
Warning Appeared

**•** `ChatRequest` —Chat Requested


Standard Objects LiveChatTranscriptEvent

**Field Name** **Details**

**•** `ChatResumedAfterTransfer` —Chat resumed

**•** `ChatbotEndChat` —Chatbot end chat

**•** `ChatbotEndedChatByAction` —Conversation ended by automated
action

**•** `ChatbotEstablished` —Accepted by Chatbot

**•** `ChatbotNotEstablished` —Chatbot Request Failed

**•** `ChoiceRoute` —Routed (Choice)

**•** `ClearCriticalWaitChat` —Critical Wait Alert Cleared

**•** `ConferenceRequest` —Chat Conference Requested

**•** `ConferenceRequestCanceled` —Chat Conference Canceled

**•** `ConferenceRequestDeclined` —Chat Conference Declined

**•** `ConnectionTimeout` —Visitor connection timed out. Available in API
version 38.0 and later.

**•** `ConnectionWarning` —Warning that visitor hasn't been connected for
some time and that the connection times out soon. Available in API version
38.0 and later.

**•** `DeclineManual` —Decline (Manual)

**•** `DeclineTimeout` —Decline (Timeout)

**•** `EndAgent` —Ended by Agent

**•** `EndVisitor` —Ended by Visitor

**•** `Enqueue` —Queued

**•** `FileCanceledAgent` —File Transfer Canceled by Agent

**•** `FileCanceledChasitor` —File Transfer Canceled by Visitor

**•** `FileTransferFailure` —File Transfer Failure

**•** `FileTransferRequested` —File Transfer Requested by Agent

**•** `FileTransferSuccess` —File Transfer Success

**•** `FileTransferToChasitor` —File Transfer Initiated by Agent

**•** `FlagLoweredAgent` —Flag Lowered by Agent

**•** `FlagLoweredSupervisor` —Flag Lowered by Supervisor

**•** `FlagRaised` —Flag Raised

**•** `LeaveAgent` —Agent Left

**•** `LeaveVisitor` —Visitor Left

**•** `OperatorJoinedConference` —Agent Joined Conference

**•** `OperatorLeftConference` —Agent Left Conference

**•** `Other`

**•** `PushAssignment` —Routed (Push)

**•** `SensitiveDataAgent` —Sensitive data blocked (Agent)

**•** `SensitiveDataSupervisor` —Sensitive data blocked (Supervisor)

**•** `SensitiveDataVisitor` —Sensitive data blocked (Visitor)


### Standard Objects LiveChatTranscriptShare

**Field Name** **Details**

**•** `Transfer` —Transfer Accepted

**•** `TransferCancelled` —Transfer Request Canceled

**•** `TransferDeclined` —Transfer Request Declined

**•** `TransferRequest` —Transfer Requested

**•** `TransferToBotFailed` —Transfer to bot failed

**•** `TransferToButtonFailed` —Transfer to button failed

**•** `TransferToQueueFailed` —Transfer to queue failed

**•** `TransferredToBot` —Transferred to bot

**•** `TransferredToButton` —Transferred to button

**•** `TransferredToQueue` —Transferred to queue

**•** `TransferredToSbrSkill` —Transferred to skill

**•** `TransferredToSbrSkillFailed` —Transfer to skill failed

**•** `Unassigned`

Usage

Use this object to query and manage live chat transcript events.

Note: LiveChatTranscriptEvent records are inserted after the chat is closed and the LiveTranscript record updated). However, the
trigger on the LiveChatTranscriptEvent sObject fires separately on each LiveChatTranscriptEvent record within the same transaction.

All the LiveChatTranscriptEvent records are inserted in a single transaction but one by one. For example, the trigger is executed
for each individual record.

```
      trigger LCTE on LiveChatTranscriptEvent (before insert) {

         // Trigger.New will have only 1 record at a time and trigger will execute for

      individual record

         for(LiveChatTranscriptEvent l : Trigger.New)

         system.debug(l.Type + '>>' +l.Detail);

         }

```

To avoid hitting any governors and limits, design your functionality considering this behavior. You can execute the logic by filtering
the records based on the `Type` field of LiveChatTranscriptEvent.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 62.0)**
Change events are available for the object.

### LiveChatTranscriptShare

Represents a sharing entry on a LiveChatTranscript object. This object is available in API version 24.0 and later.


Standard Objects LiveChatTranscriptShare

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()update()`, `upsert()`

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
Level of access that the User or Group has to the LiveChatTranscript. The possible
values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for live chat transcripts.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects LiveChatTranscriptSkill

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values can include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the LiveChatTranscript with them.

**•** `Owner` —The User is the owner of the LiveChatTranscript or is in a role above
the LiveChatTranscript owner in the role hierarchy.

```
UserOrGroupID

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the LiveChatTranscript.

This object lets you determine which users and groups can view and edit LiveChatTranscript records owned by other users.

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

### LiveChatTranscriptSkill

Represents a join between LiveChatTranscript and Skill. This object is available in API version 25.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`

Fields

**Field Name** **Details**

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
The name of the transcript.

```
SkillId

TranscriptId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the transcript.

Use this object to assign a specific skill to a specific transcript for multi-skill routing.

### LiveChatUserConfig

Represents a setting that controls the console settings for Chat users. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
AutoGreeting

```

**Type**
textarea

**Properties**
Create, Nillable


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

```
Capacity

CriticalWaitTime

CustomAgentName

DeveloperName

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Limits the amount of active chat sessions an agent can engage in.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The amount of time before a chat flashes to alert an agent to answer it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The custom name of the agent associated with the Live Agent configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.


Standard Objects LiveChatUserConfig

**Field Name** **Details**

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
HasLogoutSound

HasNotifications

HasRequestSound

HasSneakPeek

HasTransferConferenceGreeting

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a sound plays when an agent logs out of the console.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether desktop notifications are enabled for the configuration.
Available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a sound plays when a chat request comes in.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether an agent sees a real-time preview of the messages typed
by a visitor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether to enable sending an autogreeting when you transfer to
another agent or invite an agent to a conference chat.

The default value is `false` . Available in API version 53.0 and later.


Standard Objects LiveChatUserConfig

**Field Name** **Details**

```
IsAutoAwayOnDecline

Language

MasterLabel

OptionsHasAgentFileTransfer

OptionsHasAgentSneakPeek

OptionsHasAssistanceFlag

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether agents’ status is automatically changed to Away when they
decline a chat request. Available in API version 26.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the configuration.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can initiate a file transfer from a chat customer.
Available in API version 31.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether Sneak Peek is enabled for agents. Available in API version
29.0 and later.

**Type**
boolean

**Properties**
Create, Filter


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
Determines whether assistance flags are enabled for agents. Available in API
version 29.0 and later.

```
OptionsHasChatConferencing

OptionsHasChatMonitoring

OptionsHasChatTransferToAgent

OptionsHasChatTransferToButton

OptionsHasChatTransferToSkill

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can invite other agents into a customer chat. Available
in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether supervisors can view agents’ ongoing chats. Available in
API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat directly to another agent. Available
in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat to an agent assigned to a particular
chat button. Available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter


Standard Objects LiveChatUserConfig

**Field Name** **Details**

**Description**
Specifies whether an agent can transfer a chat to agents assigned to a particular
skill. Available in API version 36.0 and later.

```
OptionsHasTransferConferenceGreeting

OptionsHasVisitorBlocking

OptionsHasWhisperMessage

OptionsIsAutoAwayOnPushTimeout

SupervisorDefaultAgentStatus

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an agent can transfer a chat to an autogreeting or conference
greeting. Available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent can block IP addresses of troublesome visitors.
Available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether supervisors can send private messages to agents within an
agent’s chat with a customer. Available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent’s status automatically changes to Away if the agent
doesn’t respond to a chat request within the specified push time-out limit.
Available in API version 34.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects LiveChatUserConfigProfile

**Field Name** **Details**

**Description**
The default agent status by which to filter agents in the Agent Status list in the
supervisor panel.

```
SupervisorDefaultButtonId

SupervisorDefaultSkillId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default button ID by which to filter agents in the Agent Status list in the
supervisor panel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default skill ID by which to filter agents in the Agent Status list in the
supervisor panel.

Use this object to query and manage agent configurations in Chat.

### LiveChatUserConfigProfile

Represents a join between LiveChatUserConfig and Profile. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.


### Standard Objects LiveChatUserConfigUser

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

ProfileId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the agent configuration

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the profile

Use this object to assign specific agent configurations to specific user profiles.

### LiveChatUserConfigUser

Represents a join between Live Chat User Config and User. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
LiveChatUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects LiveChatVisitor

**Field Name** **Details**

**Description**
The record ID of the agent configuration

```
UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the user

Use this object to assign specific agent configurations to specific users.

### LiveChatVisitor

Represents a website visitor who has started or tried to start a chat session. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`,

```
upsert()

```

Fields

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

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


### Standard Objects Location

**Field Name** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

```
Name

SessionKey

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the visitor

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session key used to uniquely identify the visitor.

Use this object to query and manage live chat visitors.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatVisitorChangeEvent (API version 62.0)**
Change events are available for the object.

### Location

Represents a warehouse, service vehicle, work site, or other element of the region where your team performs field service work. In API
version 49.0 and later, you can associate activities with specific locations. Activities, such as the tasks and events related to a location,
appear in the activities timeline when you view the location detail page. Also in API version 49.0 and later, Work.com users can view
Employees as a related list on Location records. In API version 51.0 and later, this object is available for Omnichannel Inventory and
represents physical locations where inventory is available for fulfilling orders.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Location

Special Access Rules

At least one of these features must be enabled:

**•** Commerce Store

**•** Contact Tracing for Employees

**•** Employee Experience

**•** Field Service

**•** Fulfillment Orders

**•** Health Cloud

**•** Industries Insurance

**•** Industries Visit

**•** Locations

**•** Omnichannel Inventory

**•** Public Sector

**•** Retail Execution

**•** Work.com

Fields

**Field Name** **Details**

```
AssignedFoCount

CloseDate

ConstructionEndDate

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of fulfillment orders assigned to the location. Confirming held
fulfillment order capacity increments this value. To reset the location’s capacity,
set this value to 0.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location closed or went out of service.

**Type**
date


Standard Objects Location

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction ended at the location.

```
ConstructionStartDate

DefaultPickupTime

DefaultProcessingTime

DefaultProcessingTimeUnit

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction began at the location.

**Type**
time

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default pickup time at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time unit at the location. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`


Standard Objects Location

**Field Name** **Details**

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

```
Description

DrivingDirections

EarliestPickupTimeOffset

ExternalReference

FoCapacity

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the location.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the location.

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest pickup time for BOPIS. This value is measured in minutes after the
start of business hours.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of a location.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.


Standard Objects Location

**Field Name** **Details**

This field is available in API version 55.0 and later.

```
FulfillingBusinessHours

FoCapacity

IsEligibleForPickup

IsInventoryLocation

IsMobile

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Fulfilling business hours at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates whether the location supports BOPIS

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location stores parts.

Note: This field must be selected if you want to associate the location
with product items.

**Type**
boolean


Standard Objects Location

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location moves. For example, a truck or tool box.

```
LastReferencedDate

LastViewedDate

LatestPickupTimeOffset

Latitude

Location

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the location was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date the location was last viewed.

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest pickup time for BOPIS. This value is measured in minutes before the
end of business hours.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location.

**Type**
location

**Properties**
Nillable

**Description**
The geographic location.


Standard Objects Location

**Field Name** **Details**

```
LocationLevel

LocationType

LogoId

Longitude

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location’s position in a location hierarchy. If the location has no parent or
child locations, its level is 1. Locations that belong to a hierarchy have a level of
1 for the root location, 2 for the child locations of the root location, 3 for their
children, and so forth.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Picklist of location types. It has no default values, so you must populate it before
creating any location records.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A ContentAsset representing a logo for the location.

This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
Logo

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location.


Standard Objects Location

**Field Name** **Details**

```
Name

OpenDate

OwnerId

ParentLocationId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location. For example, Service Van #4.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location opened or came into service.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The location’s owner or driver.

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
The location’s parent location. For example, if vans are stored at a warehouse
when not in service, the warehouse is the parent location.

This is a relationship field.

**Relationship Name**
ParentLocation

**Relationship Type**
Lookup


Standard Objects Location

**Field Name** **Details**

**Refers To**
Location

```
PickupProcessingTime

PossessionDate

Priority

RemodelEndDate

RemodelStartDate

```

**Type**
integer

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

**The processing time required for BOPIS orders at this location.**

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the location was purchased.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the location when routing orders. No default values are included.
Add values to the picklist and reference them in your custom routing logic.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction ended at the location.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction started at the location.


Standard Objects Location

**Field Name** **Details**

```
RootLocationId

ShouldSyncWithOci

ShouldTrackFoCapacity

TimeZone

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The top-level location in the location’s hierarchy.

This is a relationship field.

**Relationship Name**
RootLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should sync its data with Omnichannel Inventory.
The default value is `false` .

This field is available in API version 51.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should track its fulfillment order capacity. The
default value is `false` .

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.


Standard Objects Location

**Field Name** **Details**

```
VisitorAddressId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup to an account’s or client’s address.

This is a relationship field.

**Relationship Name**
VisitorAddress

**Relationship Type**
Lookup

**Refers To**
Address

Before creating any location records, add at least one value to the Location Type picklist. LocationType is a required field.

To track your inventory in Salesforce, create product items, which represent the stock of a particular product a particular location. For
example, create a product item that represents the 500 bolts you have in stock at your Warehouse A location. Each product item must
be associated with a location.

To get a more granular picture of your field service operation, associate locations with service territories. For example, if a warehouse is
located in a particular service territory, add it as a service territory location.

Important: “Location” in Salesforce can also refer to the geolocation compound field found on many standard objects. When
referencing the Location object in your Apex code, always use `Schema.Location` instead of `Location` to prevent confusion
with the standard Location compound field. If referencing both the Location object and the Location field in the same snippet,
you can differentiate between the two by using `System.Location` for the field and `Schema.Location` for the object.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationChangeEvent (API version 48.0)**
Change events are available for the object.

**LocationFeed**

Feed tracking is available for the object.

**LocationHistory**

History is available for tracked fields of the object.

**LocationOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects LocationGroup

**LocationShare**

Sharing is available for the object.

SEE ALSO:

### LocationGroup LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_ : Inventory Data Model

### LocationGroup

Represents a group of Omnichannel Inventory locations, providing an aggregate view of inventory availability across those locations.
Omnichannel Inventory can create an inventory reservation for an order at the location group level, then assign the reservation to one
or more locations in the group as needed. This object is available in API version 51.0 and later.

You can define location groups according to the logic of your business needs. For example, a location group can represent the warehouses
in a geographic region, or it can include the fulfillment centers associated with a particular online storefront.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.

Fields

**Field** **Details**

```
Description

ExternalReference

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the location group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used when OCI is integrated with B2C Commerce to associate the location group with an
inventory list in B2C Commerce. This value must match the inventory list ID in B2C Commerce.


Standard Objects LocationGroup

**Field** **Details**

```
IsEnabled

LastReferencedDate

LastViewedDate

LocationGroupName

OwnerId

ShouldSyncWithOci

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location group is in use. If set to _`false`_, then inventory functions
ignore this location group and its data isn’t synchronized with OCI. The default value is _`true`_ .

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
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this location group. Default value is the API user that
created the record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects LocationGroupAssignment

**Field** **Details**

**Description**
Specifies whether to synchronize inventory data for this location group with Omnichannel
Inventory. The default value is _`true`_ .

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationGroupChangeEvent (API version 62.0)**
Change events are available for the object.

**LocationGroupFeed**

Feed tracking is available for the object.

**LocationGroupHistory**

History is available for tracked fields of the object.

**LocationGroupOwnerSharingRule**

Sharing rules are available for the object.

**LocationGroupShare**

Sharing is available for the object.

SEE ALSO:

### Location LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_ : Inventory Data Model

### LocationGroupAssignment

Represents the assignment of a location to a location group. This object is available in API version 51.0 and later.

You can assign a location to multiple location groups, which associates it with one location group assignment for each location group
that it’s assigned to. Each location group assignment represents the relationship between one location and one location group, so a
location or location group can be associated with multiple location group assignments.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.


Standard Objects LocationGroupAssignment

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationExternalReference

LocationGroupAssignment

LocationGroupExternalReference

LocationGroupId

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
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the location group assignment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects LocationShippingCarrierMethod

**Field** **Details**

**Description**
(Master-Detail) The associated location group.

```
LocationGroupName

LocationId

LocationName

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location group name of the associated location group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The associated location.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated location.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LocationGroupAssignmentChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

### Location

LocationGroup

### LocationShippingCarrierMethod

The available shipping carrier services associated with a location or location group. Allows the assignment of different shipping methods
to a specific location and enables flexibility and customization in the shipping process. This object is available in API version 61.0 and
later.


Standard Objects LocationShippingCarrierMethod

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The LocationShippingCarrierMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationSourceId

Name

```

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
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location source ID.

This is a polymorphic relationship field.

**Relationship Name**
LocationSource

**Refers To**
Location, LocationGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects LocationTrustMeasure

**Field** **Details**

**Description**
Name of the shipping carrier service associated with the location or location group.

```
OwnerId

ShippingCarrierMethodId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this LocationShippingCarrierMethod object. Default value
is the user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Shipping carrier method ID.

This is a relationship field.

**Relationship Name**
ShippingCarrierMethod

**Refers To**
Location, ShippingCarrierMethod

### LocationTrustMeasure

Represents the COVID safety protocols that your business follows. For example, enforcement of masks, social distancing, cleanliness,
and capacity limits. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects LocationTrustMeasure

Fields

**Field** **Details**

```
Description

IconUrl

IsVisibleInPublic

LastReferencedDate

LastViewedDate

LocationExternalReference

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the safety protocol. For example, “Employees and customers are required
to wear a mask in the store.”

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A public image URL to display for the LocationTrustMeasure object.

**Type**
boolean

**Properties**
Create, defaulted on create, Filter, Group, Sort, Update

**Description**
If true, displays the LocationTrustMeasure object on your site. If false, hides the
LocationTrustMeasure object on your site.

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
The date on which the record was last viewed.

**Type**
string


Standard Objects LocationTrustMeasure

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
An ID assigned to the LocationTrustMeasure objects for a particular location.

```
LocationId

Name

OwnerId

SortOrder

Title

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID for the location associated with the LocationTrustMeasure.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned name for the LocationTrustMeasure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which to display LocationTrustMeasure objects on your site.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the safety protocol. For example, Enforcement of Masks.


### Standard Objects LocWaitlistMsgTemplate LocWaitlistMsgTemplate

Represents a junction object connecting LocationWaitlist to MessagingTemplate. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
LastReferencedDate

LastViewedDate

LocationWaitlistId

MessagingTemplateId

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
The date on which the record was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the LocationWaitlist record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the MessagingTemplate record.


### Standard Objects LocationWaitlist

**Field** **Details**

```
Name

OwnerId

Type

### LocationWaitlist

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `approaching` —In Progress

**•** `confirmation` —Confirmed

**•** `inactive` —Inactive

**•** `ready` —Ready

**•** `removed` —Removed

Represents a queue created for a specific location. Multiple queues can be created for a single location. For example, you can have a
queue for each sales agent or a standard queue and a queue for vulnerable groups. The specific party of people in a queue is represented
by LocationWaitlistedParty. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects LocationWaitlist

Fields

**Field** **Details**

```
BusinessHoursId

ClosedDateTime

CumulativeGuestCount

CumulativeGuestGroupCount

CurrentGuestCount

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the BusinessHours record that contains the hours the business is open.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is closed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of guests allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of groups allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current number of guests.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects LocationWaitlist

**Field** **Details**

**Description**
A brief description of this record.

```
GuestCapacity

LastReferencedDate

LastViewedDate

MaxPartySize

MessagingChannelId

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total capacity of guests.

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
The date on which the record was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum size of a group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The messaging channel ID.

**Type**
string


Standard Objects LocationWaitlist

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

```
OpenDateTime

OwnerId

PartyReminderDelayMinutes

PlaceId

ResourceCapacity

ResourceOccupancyCount

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is open.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of minutes between when a party is notified and when they receive a reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location ID for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The capacity for this resource.

**Type**
int


### Standard Objects LocationWaitlistedParty

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The occupancy count for this resource.

```
Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `closed`

**•** `open`

**•** `paused`

### LocationWaitlistedParty

Represents a specific party of people waiting in a queue. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

EntryDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this queue.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects LocationWaitlistedParty

**Field** **Details**

**Description**
The date and time a party is added to the queue.

```
EstimatedWaitHours

EstimatedWaitMinutes

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated hours of wait time for a party.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated minutes of wait time for a party.

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
The date on which the record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
reference


Standard Objects LocationWaitlistedParty

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

```
PartySize

PartyStatus

SignUpDateTime

WaitlistId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The size of the queued party.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

