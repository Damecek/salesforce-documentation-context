Special Access Rules

This metadata type is available with Salesforce Pricing.

Fields

**Field Name** **Description**

```
defaultPricingProcedure

defaultPricingProcedureDeveloperName

defaultPricingProcedureId

developerName

isActive

isInternal

```

**Field Type**

[ExpressionSetDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_expressionsetdefinition.htm)

**Description**
Expression set definition that's associated with this pricing recipe setting.

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**
ID of the pricing procedure of the pricing recipe.

**Field Type**
string

**Description**

Required.

API name of the pricing recipe.

**Field Type**
boolean

**Description**
Indicates whether the pricing recipe is active ( `true` ) or not ( `false` ).

The default value is `false`

**Field Type**
boolean

**Description**
Indicates whether the price recipe record is created internally by the Salesforce platform
( `true` ) or not ( `false` ).


Metadata Types PricingRecipe

**Field Name** **Description**

The default value is `false`

```
masterLabel

pricingRecipeTableMapping

```

**Field Type**
string

**Description**

Required.

Name for pricing recipe that's defined when the pricing recipe is created.

**Field Type**

PricingRecipeTableMapping[]

**Description**
Mapping of the pricing components of a lookup table with the chosen pricing recipe.

PricingRecipeTableMapping

Represents the mapping of the lookup table with the chosen pricing recipe.

**Field Name** **Description**

```
isInternal

lookupTable

lookupTableDeveloperName

pricingComponentType

```

**Field Type**
boolean

**Description**
Indicates whether the price recipe field mapping record is created internally by the
Salesforce platform ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**

[DecisionTable](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_decisiontable.htm)

[DecisionMatrixDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_decisionmatrixdefinition.htm)

**Description**
Lookup table that's associated with either a decision matrix or decision table.

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**
Pricing component field data that the decision table is built on.


Metadata Types PricingRecipe

**Field Name** **Description**

Valid values are:

**•** `AttributeDiscount`

**•** `BundleDiscount`

**•** `DerivedPricing`

**•** `ListPrice`

**•** `PriceAdjustmentMatrix`

**•** `PromotionsDiscount`

**•** `VolumeDiscount`

**•** `VolumeTierDiscount`

**•** `DiscountDistributionService` . This value is available in API version
60.0 and later.

**•** `MinimumPrice` . Available in API version 62.0 and later.

```
pricingProcedureOutputMapList

pricingRecipe

```

**Field Type**

PricingProcedureOutputMap[]

**Description**
List of the mappings of the outputs of the pricing procedures to the associated lookup
tables. Available in API version 60.0 and later.

**Field Type**
string

**Description**

Required.

Pricing data store that's associated with this pricing recipe field mapping.

PricingProcedureOutputMap

Represents the mapping of the outputs of the pricing procedures to the associated lookup tables. Each record specifies the output
mapping of the associated lookup table based on the pricing component type specified in the PricingRecipeTableMapping object.

**Field Name** **Description**

```
fieldName

isPricingRecipeActive

```

**Field Type**
string

**Description**
For internal use only.

**Field Type**
boolean

**Description**
Indicates whether the associated pricing recipe is active ( `true` ) or not ( `false` ).


Metadata Types PricingRecipe

**Field Name** **Description**

The default value is `false` .

```
outputFieldName

outputFieldNameString

outputType

pricingElementType

```

**Field Type**
string

**Description**
Field name that contains the output type that's generated from the pricing element.

**Field Type**
string

**Description**
Derived field that references a specific column in a decision table or decision matrix.

**Field Type**
string

**Description**
Output type that's generated from a pricing element.

Valid values are:

**•** `AdjustmentType`

**•** `AdjustmentValue`

**•** `CustomOutput`

**•** `HashOutput`

**•** `UnitPrice`

**Field Type**
PricingElementType (enumeration of type string)

**Description**
Type of pricing element, which is a derived field from
`PricingRecipeTableMapping.PricingComponentType` .

Valid values are:

**•** `AssetDiscovery`

**•** `AttributeDiscount`

**•** `BundleDiscount`

**•** `DerivedPricing`

**•** `DiscountDistributionService`

**•** `ListPrice`

**•** `MinimumPrice`

**•** `PriceAdjustmentMatrix`

**•** `PriceRevision`

**•** `PromotionsDiscount`

**•** `RuleFetch`


Metadata Types PricingRecipe

**Field Name** **Description**

**•** `VolumeDiscount`

**•** `VolumeTierDiscount`

Declarative Metadata Sample Definition

The following is an example of a PricingRecipe component.

```
   <PricingRecipe xmlns="http://soap.sforce.com/2006/04/metadata">

      <defaultPricingProcedureId> </defaultPricingProcedureId>

      <developerName>CMEDefaultRecipe</developerName>

      <isActive>false</isActive>

      <isInternal>false</isInternal>

      <masterLabel>CMEDefaultRecipe</masterLabel>

      <pricingRecipeTableMapping>

        <isInternal>false</isInternal>

   <lookupTableDeveloperName>Bundle_Based_Adjustment_Decision_Table</lookupTableDeveloperName>

        <pricingComponentType>CUSTOMDISCOUNT</pricingComponentType>

        <fileBasedDecisionTableName>Bundle Based Adjustment

   Entries</fileBasedDecisionTableName>

        <pricingProcedureOutputMapList>

           <fieldName>AdjustmentValue</fieldName>

           <isPricingRecipeActive>false</isPricingRecipeActive>

           <outputFieldName>0lPxx000000000f</outputFieldName>

           <outputFieldNameString>false</outputFieldNameString>

           <outputType>AdjustmentValue</outputType>

       <pricingElementType>BundleDiscount</pricingElementType>

        </pricingProcedureOutputMapList>

        <pricingProcedureOutputMapList>

           <fieldName>AdjustmentType</fieldName>

           <isPricingRecipeActive>false</isPricingRecipeActive>

           <outputFieldName>0lPxx000000000m</outputFieldName>

           <outputFieldNameString>false</outputFieldNameString>

           <outputType>AdjustmentType</outputType>

       <pricingElementType>BundleDiscount</pricingElementType>

        </pricingProcedureOutputMapList>

        <pricingRecipe>CMEDefaultRecipe</pricingRecipe>

      </pricingRecipeTableMapping>

   </PricingRecipe>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PricingRecipe</name>

      </types>

      <version> 67.0 </version>

   </Package>

```


### Metadata Types Profile

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Profile

Represents a user profile. A profile defines a user’s permission to perform different functions within Salesforce. This type extends the
Metadata metadata type and inherits its `fullName` field.

In API version 29.0 and later, you can retrieve and deploy access settings for these managed components in profiles and permission sets:

**•** Apex classes

**•** Apps

**•** Custom field permissions

**•** Custom object permissions

**•** Custom tab settings

**•** External data sources

**•** Record types

**•** Visualforce pages

In API version 51.0 and later, you can retrieve and deploy access settings for login flows. For more information, see Managed Component
Access in the Components in a Module section of Sample `package.xml` Manifest Files.

As of API version 50.0 and later, only users with correct permissions can view profile names other than their own if the Profile Filtering
setting is enabled.

Important: Profile names are also exposed when users with permissions to perform the following tasks take these actions:

**•** Create a tab or record type with a wizard step that includes the assignment of tabs and record types to profiles.

**•** Configure a login flow where viewing profile lists is required to make flow associations.

**•** Set up delegated admins where looking up profiles is needed to identify assignable profiles.

**•** Administer an org as a delegated customer admin.

**•** Administer an org as a delegated admin to view and assign profiles of the delegated group.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.profile` . There's one file for each profile, stored in the `profiles` folder in the corresponding package directory.

Version

### Profiles are available in API version 10.0 and later.

Special Access Rules

As of Summer ’20 and later, Customer Portal and Partner Portal users can’t access this type.

To view the following settings, assignments, and permissions for standard and custom objects in a specified profile, the View Setup and
Configuration permission is required.


Metadata Types Profile

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Fields

The content of a profile returned by Metadata API depends on the content requested in the `RetrieveRequest` message. For
example, profiles only include field-level security for fields included in custom objects returned in the same `RetrieveRequest` as
the profiles. The profile definition contains the following fields:

Important: We designed Profile metadata deployment to overlay the existing Profile settings in a target org. For example, if you
disable permissions for a profile, the newly disabled permission information isn't exported. To force all Profile changes to deploy
through metadata, including permission disablement, add code that explicitly indicates disabled permissions. For example, add
this code to the Profile metadata `.xml` file before deploying into a target org: `<value>false</value>` .

If you deploy a profile that doesn’t exist in the target org and don't specify any permissions or settings, then the resulting profile
contains all permissions and settings in the standard Minimum Access - Salesforce profile (API version 60.0 and later) or the standard
Standard User profile (API version 59.0 and earlier).

Note: As of API version 38.0, you can change field permissions to make a field editable using the Metadata API for fields that you
can't change through the user interface. For example, you can deploy `Asset.ProductCode` as an editable field even though
you can't through the user interface.

**Field Name** **Field Type** **Description**

`agentAccesses` ProfileAgentAccess[] Indicates which agents are visible to users assigned to
this profile. Available in API version 63.0 and later.

`applicationVisibilities` ProfileApplicationVisibility[] Indicates which apps are visible to users assigned to this
profile. In API version 29.0 and earlier, this field supports

custom apps only. In API version 30.0 and later, this field
supports both standard and custom apps.

`categoryGroupVisibilities` ProfileCategoryGroupVisibility[]

Indicates which data category groups are visible to users
assigned to this profile. Available in API version 41.0 and
later.

`classAccesses` ProfileApexClassAccess[] Indicates which top-level Apex classes have methods
that users assigned to this profile can execute.

`custom` boolean

Indicates whether the profile is a custom ( `true` ) or
standard ( `false` ) profile. Available in API version 30.0
and later.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`customMetadataTypeAccesses` ProfileCustomMetadataTypeAccess[]

`customPermissions` ProfileCustomPermissions[]

`customSettingAccesses` ProfileCustomSettingAccesses[]

Indicates the custom metadata types that are
read-accessible to a user assigned to this profile. Available
in API version 47.0 and later.

Indicates which custom permissions are available to users
assigned to this profile. Available in API version 31.0 and
later.

Indicates the custom settings that are read-accessible to
a user assigned to this profile. Available in API version
47.0 and later.

`description` string The profile description. Limit: 255 characters. Available
in API version 30.0 and later.

`externalDataSourceAccesses` ProfileExternalDataSourceAccess[]

Indicates which data sources with identity type of `Per`
`User` are available to users assigned to this profile.
Available in API version 27.0 and later.

`fieldLevelSecurities` ProfileFieldLevelSecurity[] Indicates which fields are visible to a user assigned to this
profile, and the kind of access available (editable or

hidden). This field is available in API version 22.0 and
earlier.

`fieldPermissions` ProfileFieldLevelSecurity[] Indicates which fields are visible to a user assigned to this
profile, and the kind of access available (editable or

readable). This field is available in API version 23.0 and
later.

`flowAccesses` ProfileFlowAccess[] Indicates which flows can be accessed by a user assigned
to this profile. Available in API version 47.0 and later.

`genComputingSummaryDefAccess` ProfileGenComputingSummaryDefAccess
on page 1765[]

Indicates enhanced summary access configuration for
users assigned to this profile. Available in API version 66.0
and later.

`fullName` string The name can only contain characters, letters, and the
underscore (_) character. The name must start with a

letter, and can’t end with an underscore or contain two
consecutive underscore characters.

Inherited from the Metadata component, this field isn’t
defined in the WSDL for this component. It must be
specified when creating, updating, or deleting. See
create() to see an example of this field specified for a call.

`layoutAssignments` ProfileLayoutAssignments[] Indicates which layout to use for this profile.

`loginFlows` LoginFlow[] Indicates a business process that you direct users to
before they access Salesforce.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`loginHours` ProfileLoginHours[]

`loginIpRanges` ProfileLoginIpRange[]

Indicates the hours within which a user with this profile
can log in. If not specified, the profile doesn’t restrict a
user’s login hours.

This field is available in API version 25.0 and later.

The list of IP address ranges from which users with a
particular profile can log in.

This field is available in API version 17.0 and later.

`objectPermissions` ProfileObjectPermissions[] Indicates which objects are accessible to a user assigned
to this profile, and the kind of access available (create,

read, edit, delete, and so on). In API version 28.0 and later,
this field is only retrieved when `allowRead` is `true` .

In API version 50.0 and later, editing standard objects on
standard profiles is disabled.

`pageAccesses` ProfileApexPageAccess[] Indicates which Visualforce pages that users assigned to
this profile can execute.

`profileActionOverrides` ProfileActionOverride[] A list of the Lightning Experience Home page action
overrides that are assigned to this profile. When a user

logs in with a profile, a matching ProfileActionOverride
assignment takes precedence over existing overrides for
the Home tab specified in ActionOverride.

This field is available in API versions 37.0 to 44.0.

`recordTypeVisibilities` ProfileRecordTypeVisibility[]

`ServicePresenceStatusAccesses` ProfileServicePresenceStatusAccess[]
on page 1770

`tabVisibilities` ProfileTabVisibility[]

`userLicense` string

Indicates the visibility of record types for users assigned
to this profile. In API version 29.0 and later, this field isn’t
retrieved or deployed for inactive record types.

Indicates which Service presence statuses that the user
assigned to this profile can execute. Available in API
version 64.0 and later.

Indicates which record types are visible to a user assigned
to this profile, and therefore which tabs within an app
are visible.

The `User License` for the profile. A user license
determines the baseline of features that the user can
access. Every user must have exactly one user license.

This field is available in API version 17.0 and later.

`userPermissions` ProfileUserPermission[] Specifies a user permission (such as “API Enabled”) and
whether it’s enabled for this profile. This field retrieves

only enabled user permissions. Available in API version
29.0 and later.


Metadata Types Profile

LoginFlow

LoginFlow represents a business process that you direct users to before they access Salesforce. You can use Metadata API to define
[existing flows as login flows and to edit login flow definitions. To delete login flow definitions, use the Login Flow page.](https://help.salesforce.com/articleView?id=security_login_flow_associate.htm&language=en_US)

**Field Name** **Field Type** **Description**

`flow` string

Required only if the `uiLoginFlowType` is `VisualWorkflow` .
The `fullName` [of the Flow.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_visual_workflow.htm)

Before you can deploy the LoginFlow, the Flow referenced here must be
deployed in your org and its status must be `Active` .

```
flowtype

```

LoginFlowType Required. The value is `UI` .
(enumeration of type
string)

`friendlyname` string Required. The name of the LoginFlow.

```
uiLoginFlowType

```

UiLoginFlowType Required. The type of login flow. These are valid values.
(enumeration of type

**•** `VisualWorkflow` [—Indicates a Salesforce Flow. You can create](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_visual_workflow.htm)

string)

these flows using Flow Builder.

**•** `VisualForce` —Indicates a flow created using Visualforce.

`useLightningRuntime` boolean Indicates if Lightning Runtime is used ( `true` ) or not ( `false` (default)).
Used only if `uiLoginFlowType` is `VisualWorkflow` .

`vfFlowPage` string Required only if the `uiLoginFlowType` is `VisualForce` . The
name of the VisualForce page.

`vfFlowPageTitle` string Required only if the `uiLoginFlowType` is `VisualForce` . The
name of the VisualForce page.

ProfileActionOverride

ProfileActionOverride represents a user profile-based override of an ActionOverride on a standard Home tab in Lightning Experience.

Note:

**•** ProfileActionOverride can be defined only on Profile for API version 39.0 to 44.0. In API version 45.0 and later, ProfileActionOverride
must be defined for CustomApplication instead. Beginning with API version 45.0, Home page assignments related to user
profile must also have a corresponding app assignment because more granular Home page assignments are supported. As a
result, ProfileActionOverride is defined for CustomApplication rather than Profile.

**•** ProfileActionOverride settings aren’t retrieved in the `.profile` file unless a Lightning page is referenced in the
`package.xml` file.

**Field Name** **Field Type** **Description**

`actionName` string Required. The possible values are the same as the actions you can
override:

**•** `accept`


Metadata Types Profile

**Field Name** **Field Type** **Description**

**•** `clone`

**•** `delete`

**•** `edit`

**•** `list`

**•** `new`

**•** `tab`

**•** `view`

`content` string Set this field if `type` is set to `flexipage`,
`lightningcomponent`, `scontrol`, or `visualforce` . It refers

to the name of the Lightning page, Lightning component, s-control, or
Visualforce page to use as the override. To reference installed
components, use this format:
_**`Component_namespace`**_ `__` _**`Component_name`**_ .

The size of the page being overridden.

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and

`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is
reserved for future use. The `null` value (which is the same as specifying
no value) represents Salesforce Classic.

The name of the sObject type being overridden. Valid values are
`standard` and `custom` .

This value must be `standard-home` when actionName is `tab` .

```
formFactor

```

FormFactor
(enumeration of type
string)

`pageOrSobjectType` string

`recordType` string The record type assigned to the ProfileActionOverride. If the
`PageOrSobjectType` is `standard-home`, this field is null.

```
type

```

ProfileAgentAccess

ActionOverrideType Required. Represents the type of action override. Valid values are
(enumeration of type described in ActionOverrideType.
string)

ProfileAgentAccess represents the agent access configuration for users assigned through a profile.

**Field Name** **Field Type** **Description**

`agentName` string Required. The name of the employee agent.

`enabled` boolean Required. Indicates whether users assigned to this profile can use the
Agentforce Employee Agent ( `true` ) or not ( `false` ).


Metadata Types Profile

ProfileApplicationVisibility

ProfileApplicationVisibility determines whether an app is visible to a user assigned to this profile.

**Field Name** **Field Type** **Description**

`application` string Required. The name of the app.

`default` boolean Required. Indicates whether the app is the default app ( `true` ) or not
( `false` ). Only one app per profile can be set to `true` .

`visible` boolean Required. Indicates whether this app is visible to users assigned to this
profile ( `true` ) or not ( `false` ).

ProfileCategoryGroupVisibility

ProfileCategoryGroupVisibility determines whether a data category group is visible to a user assigned to this profile. Available in API
version 41.0 and later.

ProfileCustomMetadataTypeAccess

ProfileCustomMetadataTypeAccess represents the custom metadata type access for users assigned to a profile. Available in API version
47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom metadata
type are readable ( `true` ) or not ( `false` ).

`name` string Required. The custom metadata type name.

ProfileApexClassAccess

ProfileApexClassAccess determines which top-level Apex classes have methods that users assigned to this profile can execute.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`apexClass` string Required. The Apex class name.

`enabled` boolean Required. Indicates whether users assigned to this profile can execute
methods in the top-level class ( `true` ) or not ( `false` ).

ProfileCustomPermissions

ProfileCustomPermissions represents the custom permissions access for users assigned to a profile. Only enabled custom permissions
are retrieved.

**Field Name** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the custom permission is enabled ( `true` )
or not ( `false` ).

`name` string Required. The custom permission name.

ProfileCustomSettingAccesses

ProfileCustomSettingAccesses represents the custom setting access for users assigned to a profile. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom setting are
readable ( `true` ) or not ( `false` ).

`name` string Required. The custom setting name.

ProfileExternalDataSourceAccess

ProfileExternalDataSourceAccess represents the data source access for users with identity type of Available in API version 27.0 and
later. `Per User` .

**Field Name** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the data source is enabled ( `true` ) or not
( `false` ).

`externalDataSource` string The name of the external data source.

ProfileFieldLevelSecurity

ProfileFieldLevelSecurity represents the field level security for users assigned to a profile. In API version 30.0 and later, permissions for
required fields can’t be retrieved or deployed.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`editable` boolean

`field` string

`hidden` boolean

`readable` boolean

ProfileFlowAccess

Required. Indicates whether this field is editable ( `true` ) or not ( `false` ).

In API version 30.0 and later, when deploying a new custom field, this
field is `false` by default.

Required. Indicates the name of the field.

When referencing shared Activity fields, specify Event or Task. For
example, `Event.Meeting__c` .

Indicates whether this field is hidden ( `true` ) or not ( `false` ). This field
is available in API version 22.0 and earlier.

For portal profiles, this field is set to `true` by default in API version 19.0
and later.

Indicates whether this field is readable ( `true` ) or not ( `false` ). This field
is available in API version 23.0 and later. It replaces the `hidden` field.

In API version 30.0 and later, when deploying a new custom field, this
field is `false` by default.

For portal profiles, this field is set to `false` by default.

ProfileFlowAccess represents which flows a profile grants access to. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether users assigned this profile can access
the flow ( `true` ) or not ( `false` ). The default value is `false` .

`flow` string Required. The name of the flow to which access is granted.

ProfileGenComputingSummaryDefAccess

ProfileGenComputingSummaryDefAccess represents the enhanced summary access configuration for users assigned through a profile.
Available in API version 66.0 and later.

**Field** **Field Type** **Description**

`configName` string Required. The enhanced summary access configuration name given
by the admin.

`enabled` boolean Required. Indicates whether the configuration is enabled ( `true` )
or not ( `false` ).


Metadata Types Profile

ProfileLayoutAssignments

ProfileLayoutAssignments determines which layout to use for a profile and a given entity.

**Field Name** **Field Type** **Description**

`layout` string Required. Indicates the layout for this particular entity.

`recordType` string This field is optional. If the `recordType` of the record matches a layout
assignment rule, it uses the specified layout.

ProfileLoginHours

ProfileLoginHours restricts the days and times within which users with a particular profile can log in.

**Field Name** **Field Type** **Description**

_`weekday`_ `Start` string Specifies the earliest time on that day that a user with this profile can log
in. If a start time for a particular day is specified, an end time for that day

also must be specified. Start can’t be greater than end for a particular
day.

**•** Valid values for `weekday` : `monday`, `tuesday`, `wednesday`,
`thursday`, `friday`, `saturday`, or `sunday` . For example,
`mondayStart` indicates the beginning of the login period for
Monday.

**•** Valid values for Start: the number of minutes since midnight. Must
be evenly divisible by 60 (full hours). For example, `300` is 5:00 AM.

_`weekday`_ `End` string Specifies the time on that day that a user with this profile must log out
by.

**•** Valid values for `weekday` : `monday`, `tuesday`, `wednesday`,
`thursday`, `friday`, `saturday`, or `sunday` . For example,
`mondayEnd` indicates the close of the login period for Monday.

**•** Valid values for End: the number of minutes since midnight. Must be
evenly divisible by 60 (full hours). For example, `1020` is 5:00 PM.

To delete login hour restrictions from a profile that previously had them, you must explicitly include an empty loginHours tag without
any start or end times.

ProfileLoginIpRange

ProfileLoginIpRange IP defines an IP address range that users with a particular profile can log in from.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`description` string

Use this field to identify the purpose of the range, such as which part of
a network corresponds to this range. This field is available in API version
31.0 and later.

`endAddress` string Required. The end IP address for the range.

`startAddress` string Required. The start IP address for the range.

ProfileObjectPermissions

ProfileObjectPermissions represents a user's access to objects.

Note:

**•** In API version 18.0 and later, these permissions are disabled in new custom objects for any profiles where “View All Data” or
“Modify All Data” is disabled.

**•** In API version 50.0 and later, editing standard objects on standard profiles is disabled.

**Field Name** **Field Type** **Description**

`allowCreate` boolean

`allowDelete` boolean

`allowEdit` boolean

`allowRead` boolean

Indicates whether the object referenced by the `object` field can be
created by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named `revokeCreate` before version 14.0 and the logic
is reversed. The field name change and the update from `true` to

`false` and the reverse is automatically handled between versions and
doesn’t require any manual editing of existing XML component files.

Indicates whether the object referenced by the `object` field can be
deleted by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named The field name change and the update from
`revokeDelete` before version 14.0 and the logic is reversed. `true`

to `false` and the reverse is automatically handled between versions
and doesn’t require any manual editing of existing XML component files.

Indicates whether the object referenced by the `object` field can be
edited by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named The field name change and the update from
`revokeEdit` before version 14.0 and the logic is reversed. `true` to

`false` and the reverse is automatically handled between versions and
doesn’t require any manual editing of existing XML component files.

Indicates whether the object referenced by the `object` field can be
seen by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named The field name change and the update from
`revokeRead` before version 14.0 and the logic is reversed. `true` to

`false` and the reverse is automatically handled between versions and
doesn’t require any manual editing of existing XML component files.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`modifyAllRecords` boolean Indicates whether all records for the object referenced by the `object`
field can be read, edited, or deleted by the users assigned to this profile

( `true` ) or not ( `false` ), regardless of the sharing settings for the object.
This setting is equivalent to the Modify All Data user permission limited
to the individual object level. Available in API version 15.0 and later.

This field isn’t available for all objects. Refer to the profile in the user
interface to determine which objects currently support these permissions.
Profiles with Modify All Data ignore `modifyAllRecords` entries in
Metadata API and don't return an error if Modify All Data is enabled on
the profile.

`object` string Required. The name of the object whose permissions are altered by this
profile, for example, `MyCustomObject__c` .

`viewAllFields` boolean

Indicates whether all fields and field data for the object referenced by
the `object` field can be read by the users assigned to this profile
( `true` ) or not ( `false` ). Available in API version 63.0 and later.

`viewAllRecords` boolean Indicates whether all records for the object referenced by the `object`
field can be read by the users assigned to this profile ( `true` ) or not

( `false` ), regardless of the sharing settings for the object. This setting
includes private records (records with no parent object). This setting is
equivalent to the View All Data user permission limited to the individual
object level. Available in API version 15.0 and later.

This field isn’t available for all objects. Refer to the profile in the user
interface to determine which objects currently support these permissions.
Profiles with "View All Data" ignore `viewAllRecords` entries in the
Metadata API and don't return an error if View All Data is enabled on the
profile.

ProfileApexPageAccess

ProfileApexPageAccess determines which Visualforce pages that users assigned to this profile can execute.

**Field Name** **Field Type** **Description**

`apexPage` string Required. The Visualforce page name.

`enabled` boolean Required. Indicates whether users assigned to this profile can execute
the Visualforce page ( `true` ) or not ( `false` ).

ProfileRecordTypeVisibility

ProfileRecordTypeVisibility represents the visibility of record types for this profile. Record types let you offer different business processes,
picklist values, and page layouts to different users.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`default` boolean Required. Indicates whether the record type is the default when users
with this profile create records for this object ( `true` ) or not ( `false` ).

`personAccountDefault` boolean When Person Accounts is enabled, this field indicates whether the record
type is this profile’s default person account record type ( `true` ) or not

( `false` ). When Person Accounts is disabled, this field’s value has no
impact.

Person accounts aren’t enabled by default in Salesforce. To request person
accounts, contact Salesforce.

`recordType` string Required. The record type name, for example
`Account.MyRecordType` .

`visible` boolean Required. Indicates whether this record type is visible to users assigned
to this profile ( `true` ) or not ( `false` ).

ProfileTabVisibility

ProfileTabVisibility represents the visibility of tabs for this profile. For version 17.0 and later, ProfileTabVisibility supports visibility of tabs
for standard objects. The manifest file must include the standard object corresponding to a standard tab to retrieve the tab visibility in
a profile.

**Field Name** **Field Type** **Description**

`tab` string Required. The name of the tab.

```
visibility

```

TabVisibility Required. Indicates the visibility of the tab. Valid values are:
(enumeration of type

**•** `DefaultOff` —The tab is available on the All Tabs page. Users

string)

can individually customize their display to make the tab visible in
any app.

**•** `DefaultOn` —The tab is available on the All Tabs page and appears
in the visible tabs for its associated app. Users can individually
customize their display to hide the tab or make it visible in other
apps.

**•** `Hidden` —The tab isn’t available on the All Tabs page or visible in
any apps.

In API version 36.0 and earlier, `Hidden` is returned only if
`visibility` was set using the API. If it was set to `Hidden` from the
profile in Salesforce, the API doesn’t return a visibility value. For version
37.0 and later, when tab visibility is set to hidden, the API returns
`Hidden`, regardless of how the value was set.

ProfileUserPermission

ProfileUserPermission represents an app or system permission for a profile. Use one of these elements for each permission.


Metadata Types Profile

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the permission is enabled ( `true` ) or
disabled ( `false` ).

`name` string Required. The permission name.

ProfileServicePresenceStatusAccess

Represents the presence statuses that reps assigned to this profile have access. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`servicePresenceStatus` string Required. The name of Service Presence Status.

`enabled` boolean Required. Indicates whether the rep assigned to this profile has
access to the presence status ( `true` ) or not ( `false` ).

Java Sample

This sample uses picklists, profiles, record types, and a custom app:

```
   public void profileSample() {

     try {

      // Create an expense report record, tab and app...

      CustomObject expenseRecord = new CustomObject();

      expenseRecord.setFullName("ExpenseReport__c");

      expenseRecord.setLabel("Expense Report");

      expenseRecord.setPluralLabel("Expense Reports");

      expenseRecord.setDeploymentStatus(DeploymentStatus.Deployed);

      expenseRecord.setSharingModel(SharingModel.ReadWrite);

      CustomField nameField = new CustomField();

      nameField.setType(FieldType.AutoNumber);

      nameField.setLabel("Expense Report Number");

      nameField.setDisplayFormat("ER-{0000}");

      expenseRecord.setNameField(nameField);

      AsyncResult[] arsExpenseRecord =

        metadataConnection.create(new Metadata[] {expenseRecord});

      Picklist expenseStatus = new Picklist();

      PicklistValue unsubmitted = new PicklistValue();

      unsubmitted.setFullName("Unsubmitted");

      PicklistValue submitted = new PicklistValue();

      submitted.setFullName("Submitted");

      PicklistValue approved = new PicklistValue();

      approved.setFullName("Approved");

      PicklistValue rejected = new PicklistValue();

      rejected.setFullName("Rejected");

      expenseStatus.setPicklistValues(new PicklistValue[] {

```


Metadata Types Profile

```
        unsubmitted, submitted, approved, rejected}

      );

      CustomField expenseStatusField = new CustomField();

      expenseStatusField.setFullName(

        "ExpenseReport__c.ExpenseStatus__c"

      );

      expenseStatusField.setLabel("Expense Report Status");

      expenseStatusField.setType(FieldType.Picklist);

      expenseStatusField.setPicklist(expenseStatus);

      AsyncResult[] arsStatusField =

        metadataConnection.create(new Metadata[]

           {expenseStatusField});

      CustomTab expenseTab = new CustomTab();

      expenseTab.setFullName("ExpenseReport__c");

      expenseTab.setMotif("Custom70: Handsaw");

      expenseTab.setCustomObject(true);

      AsyncResult[] arsTab =

        metadataConnection.create(new Metadata[] {expenseTab});

      CustomApplication application = new CustomApplication();

      application.setFullName("ExpenseForce");

      application.setTab(new String[] {expenseTab.getFullName()});

      AsyncResult[] arsApp =

        metadataConnection.create(new Metadata[] {application});

      // Employees and managers have the same app visibility...

      ProfileApplicationVisibility appVisibility =

        new ProfileApplicationVisibility();

      appVisibility.setApplication("ExpenseForce");

      appVisibility.setVisible(true);

      Profile employee = new Profile();

      employee.setFullName("Employee");

      employee.setApplicationVisibilities(

        new ProfileApplicationVisibility[] {appVisibility}

      );

      AsyncResult[] arsProfileEmp =

      metadataConnection.create(new Metadata[] {employee});

      Profile manager = new Profile();

      manager.setFullName("Manager");

      manager.setApplicationVisibilities(

        new ProfileApplicationVisibility[] {appVisibility}

      );

      AsyncResult[] arsProfileMgr =

        metadataConnection.create(new Metadata[] {manager});

      // But employees and managers have different access

      // to the state of the expense sheet

      RecordType edit = new RecordType();

      edit.setFullName("ExpenseReport__c.Edit");

      RecordTypePicklistValue editStatuses =

```


Metadata Types Profile

```
        new RecordTypePicklistValue();

      editStatuses.setPicklist("ExpenseStatus__c");

      editStatuses.setValues(new PicklistValue[]

        {unsubmitted, submitted});

      edit.setPicklistValues(new RecordTypePicklistValue[]

        {editStatuses});

      AsyncResult[] arsRecTypeEdit =

        metadataConnection.create(new Metadata[] {edit});

      RecordType approve = new RecordType();

      approve.setFullName("ExpenseReport__c.Approve");

      RecordTypePicklistValue approveStatuses =

        new RecordTypePicklistValue();

      approveStatuses.setPicklist("ExpenseStatus__c");

      approveStatuses.setValues(new PicklistValue[]

        {approved, rejected});

      approve.setPicklistValues(new RecordTypePicklistValue[]

        {approveStatuses});

      AsyncResult[] arsRecTypeApp =

        metadataConnection.create(new Metadata[] {approve});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

Declarative Metadata Sample Definition

The definition of a profile in an organization with a custom app, custom object, record type, tab, and user permission is:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Profile xmlns="http://soap.sforce.com/2006/04/metadata">

      <applicationVisibilities>

        <application>PubApps__Myriad_Publishing</application>

        <default>false</default>

        <visible>true</visible>

      </applicationVisibilities>

      <custom>true</custom>

      <objectPermissions>

        <object>TestWeblinks__c</object>

        <allowCreate>true</allowCreate>

        <allowDelete>true</allowDelete>

        <allowEdit>true</allowEdit>

        <allowRead>true</allowRead>

        <viewAllRecords>false</viewAllRecords>

        <modifyAllRecords>false</modifyAllRecords>

        <viewAllFields>false</viewAllFields>

      </objectPermissions>

      <recordTypeVisibilities>

        <default>true</default>

        <recordType>TestWeblinks__c.My First Recordtype</recordType>

        <visible>true</visible>

      </recordTypeVisibilities>

      <tabVisibilities>

        <tab>Myriad Publications</tab>

```


Metadata Types Profile

```
        <visibility>DefaultOn</visibility>

      </tabVisibilities>

      <userPermissions>

        <enabled>true</enabled>

        <name>APIEnabled</name>

      </userpermissions>

   </Profile>

```

Usage

To create custom profiles, we recommend that you use the Profile object instead of the `deploy()` call on the Profile Metadata type.
The Profile object allows you to create empty profiles that start without any permissions enabled except for required permissions for the
profile’s user license.

When you use the `retrieve()` call to get information about profiles, the returned `.profile` files only include security settings
for the other metadata types referenced in the retrieve request. Exceptions include user permissions, IP address ranges, and login hours,
which are always retrieved. For example, the following `package.xml` file contains a `types` element that matches all custom
objects. The returned profiles contain object and field permissions for all custom objects in your organization but don’t include permissions
for standard objects, such as Account, and standard fields.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CustomObject</name>

      </types>

     <types>

        <members>*</members>

        <name>Profile</name>

      </types>

      <version>66.0</version>

   </Package>

```

The wildcard “*” on CustomObject doesn’t match standard objects. This wildcard behavior helps you to avoid making unintended,
high-impact profile changes. If you create a few custom objects in a Developer Edition organization, `retrieve()` the information,
and later `deploy()` the custom objects to your production org, the profile and field-level security for all your standard objects and
fields aren’t overwritten. You can only overwrite these standard objects and fields by explicitly creating separate `types` elements for
the objects or fields.

Metadata API intentionally makes it difficult to include standard fields in `retrieve()` calls to prevent unexpected profile changes.
But you can still retrieve and deploy profile permissions for custom and standard fields in standard objects, such as Account.

This `package.xml` file allows you to return profile permissions for Account standard and custom fields. Note how the standard
Account object is defined in a `types` element by specifying it as a member of a CustomObject type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Account</members>

        <name>CustomObject</name>

      </types>

     <types>

        <members>*</members>

        <name>Profile</name>

```


### Metadata Types ProfileActionOverride

```
      </types>

      <version>66.0</version>

   </Package>

```

This `package.xml` file allows you to return profile permissions for the `MyCustomField__c` custom field in the Account object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

        <members>Account.MyCustomField__c</members>

        <name>CustomField</name>

     </types>

     <types>

        <members>*</members>

        <name>Profile</name>

     </types>

     <version>66.0</version>

   </Package>

```

To retrieve field permissions for relationship fields, remove the “Id” part of the field. For example, in this `package.xml` file, to retrieve
field permissions for the `AccountId` field for Contacts, you reference this field as `Contact.Account` not
`Contact.AcccountId` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

        <members>Contact.Account</members>

        <name>CustomField</name>

     </types>

     <types>

        <members>*</members>

        <name>Profile</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_Salesforce DX Developer Guide_ [: Retrieve Changes to Profiles with Source Tracking](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking_source_tracking_profiles.htm)

### ProfileActionOverride

Represents an override of an ActionOverride by a user profile. You can use it to override an ActionOverride on a standard Home tab or
object record page in Lightning Experience. When a user logs in with a profile, a matching ProfileActionOverride assignment takes
precedence over existing overrides for the Home tab or record page specified in ActionOverride. In API versions 39.0 to 44.0, you can
access ProfileActionOverride by accessing its encompassing CustomApplication on page 707 or Profile on page 1757 metadata types. In
API version 45.0 and later, you can access ProfileActionOverride only by accessing its encompassing CustomApplication on page 707.


Metadata Types ProfileActionOverride

Note: ProfileActionOverrides aren’t supported in packaging. They’re supported in change sets, but you have to add them manually.

File Suffix and Directory Location

Profile-based action overrides are defined as part of a custom application or profile.

Version

ProfileActionOverrides are available in API version 39.0 and later.

ProfileActionOverride can be defined on Profile or CustomApplication for API version 39.0 to 44.0. In API version 45.0 and later,
ProfileActionOverride must be defined for CustomApplication instead. Beginning with API version 45.0, Home page assignments related
to user profile must also have a corresponding app assignment because more granular Home page assignments are supported. As a
result, ProfileActionOverride is defined for CustomApplication rather than Profile.

Fields

**Field Name** **Field Type** **Description**

`actionName` string

The name of the action. The only valid values are `Tab` and `View` .

If `pageOrSobjectType` is `standard-home`, this field must be
`Tab` . The `Tab` action is supported only when ProfileActionOverride is
being specified as part of a Profile in API version 39.0 to 44.0.

In API version 45.0 and later, this action is supported only when
ProfileActionOverride is being specified as part of a CustomApplication,
`pageOrSobjectType` is `standard-home`, and this field is `Tab` .

If `pageOrSobjectType` is `record-home`, this field must be
`View` . The `View` action is supported only when ProfileActionOverride
is being specified as part of a CustomApplication.

`content` string Read-only. Represents the name of the Lightning page being used as
the override.

```
formFactor

```

FormFactor The size of the page being overridden. The `Large` value represents
(enumeration of the Lightning Experience desktop environment.
type string)

`pageOrSobjectType` string

`recordType` string

The name of the page being overridden. The only valid values are
`record-home` and `standard-home` . If the `actionName` is
`Tab`, this field must be `standard-home`

The record type associated with the override. If
`pageOrSobjectType` is `standard-home`, this field must be
`null` . This field is required when `actionName` is set to `View` .

```
type

```

ActionOverrideType Read-only. The type of action override. The only valid value is
(enumeration of `flexipage` .
type string)


Metadata Types ProfileActionOverride

Usage

You can't delete custom app ProfileActionOverrides by deploying with `destructiveChange.xml` . To delete a ProfileActionOverride,
retrieve the app. In the app definition file, find the `<profileActionOverrides>` section, and remove the `<content>` row.
Then, change the `<type>` value in that same section to `default` instead of `flexipage` . Do this for every override you want to
reset. After making the changes, rezip the folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.

Avoid creating duplicate ProfileActionOverrides in your org. Duplicate ProfileActionOverrides can cause problems, including being unable
to select or deselect the **Disable end user personalization of nav items in this app** option in app settings and the **Disable Navigation**
**Bar Personalization in Lightning Experience** User Interface setting.

Declarative Metadata Sample Definition

You can define a ProfileActionOverride like this.

```
   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>CustomObjectFlexiPage</content>

        <formFactor>Large</formFactor>

        <pageOrSobjectType>TestObj__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>standard</profile>

        <recordType>TestObj__c.TestRecordType</recordType>

      </profileActionOverrides>

      <defaultLandingTab>standard-home</defaultLandingTab>

      <formFactors>Large</formFactors>

      <label>My Custom App</label>

      <tab>standard-Account</tab>

      <tab>standard-Opportunity</tab>

      <uiType>Lightning</uiType>

      <navType>Standard</navType>

   </CustomApplication>

```

Here’s an example `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyCustomApp</members>

        <name>CustomApplication</name>

      </types>

      <version>39.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ProfilePasswordPolicy ProfilePasswordPolicy

Represents a profile’s password policies. Profile password policies override org-wide password policies for that profile’s users. Use
### ProfilePasswordPolicy to retrieve password policies for a given profile. This type extends the Metadata metadata type and inherits its

`fullName` field.

File Suffix and Directory Location

### ProfilePasswordPolicy components have the suffix .profilePasswordPolicy and are stored in the

`profilePasswordPolicies` folder.

Version

### ProfilePasswordPolicy components are available in API version 40.0 and later.

Fields

**Field Name** **Field Type** **Description**

`forgotPasswordRedirect` boolean If `true`, reset password links in forgot password emails don’t
immediately expire the first time they’re clicked. Instead, the links stay

active until a user confirms the password reset request on an interstitial
page. The default value is `false` .

This field is available in API version 43.0 and later.

`lockoutInterval` int

Required. The duration of the login lockout, in minutes. If users are locked
out, they must wait until the lockout period expires. Valid values: `0`, `15`,
`30`, `60` .

`maxLoginAttempts` int Required. The number of times a user can enter a wrong password before
getting locked out. Valid values: `0`, `3`, `5`, `10` .

`minimumPasswordLength` int Required. Minimum number of characters required for a password. Valid
values: `5`                                  - `50` .

`minimumPasswordLifetime` boolean If `true`, a user cannot change a password more than once in a 24-hour
period.

`obscure` boolean If `true`, answers to security questions are hidden as the user types.

`passwordComplexity` int Required. Level of complexity required for the character types in a user’s
password.

**•** If `0`, the password can contain any type of character.

**•** If `1`, the password must contain at least one alphabetic character
and 1 number.

**•** If `2`, the password must contain at least one alphabetic character,
one number, and one of the following special characters: ! # $ % _ = + < >.


Metadata Types ProfilePasswordPolicy

**Field Name** **Field Type** **Description**

**•** If `3`, the password must contain at least one number, one uppercase
letter, and one lowercase letter.

**•** If `4`, the password must contain at least one number, one uppercase
letter, one lowercase letter, and one of the following special
characters: ! # $ % - _ = + < >.

`passwordExpiration` int Required. Number of days until user passwords expire and must be
changed. Valid values:

**•** `0` —If set to `0`, the password never expires.

**•** `30`

**•** `60`

**•** `90`

**•** `180`

**•** `365`

`passwordHistory` int Required. Number of previous passwords to save. Saving passwords is
required to ensure that users reset their password to a new, unique

password. This value must be set before a password reset succeeds. If
`0`, `passwordExpiration` must be set to `0` .

`passwordQuestion` int Required. If set to `1`, the answer to the password hint cannot contain
the password itself. If `0`, the answer has no restrictions.

`profile` string Required. Name of the user profile.

Declarative Metadata Sample Definition

The following is an example of a ProfilePasswordPolicy component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ProfilePasswordPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

      <forgotPasswordRedirect>true</forgotPasswordRedirect>

      <lockoutInterval>30</lockoutInterval>

      <maxLoginAttempts>0</maxLoginAttempts>

      <minimumPasswordLength>7</minimumPasswordLength>

      <minimumPasswordLifetime>false</minimumPasswordLifetime>

      <obscure>false</obscure>

      <passwordComplexity>1</passwordComplexity>

      <passwordExpiration>0</passwordExpiration>

      <passwordHistory>0</passwordHistory>

      <passwordQuestion>1</passwordQuestion>

      <profile>platformportal</profile>

   </ProfilePasswordPolicy>

```


### Metadata Types ProfileSessionSetting

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ProfileSessionSetting

Represents a profile’s session settings. Use ProfileSessionSetting to retrieve the session settings for a given profile. This type extends the
Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ProfileSessionSetting components have the suffix .profileSessionSetting and are stored in the

`profileSessionSettings` folder.

Version

### ProfileSessionSetting components are available in API version 40.0 and later.

Fields

**Field Name** **Field Type** **Description**

`profile` string Required. Name of the user profile.

`requiredSessionLevel` SessionSecurityLevel Session security level.

`sessionPersistence` boolean Beta. If `true`, keep users logged in to their Experience Cloud site until
the session times out—even if they close their browser. Use

`sessionPersistence` to reduce how often users must log in to
their site. Applies only to the External Identity profile.

`sessionTimeout` int Required. Specifies how many minutes of inactivity elapse before a user’s
authenticated session times out. At the end of the session, the user must

log in again. This session timeout value applies to users of the profile
and overrides the org-wide timeout value. Changes to the org-wide
timeout value don’t apply to users of this profile. Valid values:

**•** `0` —2 Hours

**•** `15` —15 Minutes

**•** `30` —30 Minutes

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours


### Metadata Types Prompt

**Field Name** **Field Type** **Description**

**•** `1440` —24 Hours

SessionSecurityLevel

Session security levels control access to certain types of resources based on the type of authentication used for logging in to the current
session. For example, username and password authentication requires the `standard` session security level. Multi-factor authentication
(MFA) requires `HIGH_ASSURANCE` .

**Field Name** **Field Type** **Description**

`SessionSecurityLevel` (enumeration of type User’s security level for the current session.
string)

**•** The `HIGH_ASSURANCE` security level for this session meets the High
Assurance requirements set in the org’s session settings under Session
Security Levels.

**•** The `STANDARD` security level for this session meets the Standard
requirements set in the org’s session settings under Session Security Levels.

**•** The `LOW` level isn’t available or used in the Salesforce UI. It’s used at the
API level, but users assigned to this level experience unpredictable and
reduced functionality.

Declarative Metadata Sample Definition

The following is an example of a ProfileSessionSetting component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ProfileSessionSetting xmlns="http://soap.sforce.com/2006/04/metadata">

      <profile>platformportal</profile>

      <requiredSessionLevel>HIGH_ASSURANCE</requiredSessionLevel>

      <sessionTimeout>1440</sessionTimeout>

   </ProfileSessionSetting>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Prompt

Represents the metadata related to in-app guidance, which includes prompts and walkthroughs. Help users discover your products and
services, adopt your processes, or learn how to use a new feature. Write the content, select the target audience, and specify where and
when the in-app guidance appears.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types Prompt

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Prompt components have the suffix `prompt` and are stored in the `prompts` folder.

Version

Prompt components are available in API version 46.0 and later.

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

**Field Name** **Description**

```
masterLabel

promptVersions

```

PromptVersion

**Field Type**
string

**Description**
Required. The label. Maximum of 80 characters.

**Field Type**

PromptVersion[]

**Description**
A list of in-app guidance entries. Each entry represents a different prompt or
walkthrough.

A list of in-app guidance entries. Each entry represents a different prompt or walkthrough.


Metadata Types Prompt

**Field Name** **Description**

```
actionButtonLabel

actionButtonLink

body

customApplication

delayDays

description

dismissButtonLabel

```

**Field Type**
string

**Description**
Label for the action button or link. Maximum of 25 characters. For a walkthrough, specify
this value on the last step.

**Field Type**
string

**Description**
URL for the action button or link. Maximum of 1,000 characters. You can’t use the `GROUP`
`BY` option in a SOQL query for this field. For a walkthrough, specify this value on the last
step.

**Field Type**
string

**Description**
Required. Body content.

In API version 60.0 and later, enter up to 4,000 characters for all prompt types.

In earlier API versions, enter up to 240 characters for floating prompts and targeted prompts.
Enter up to 4,000 characters for docked prompts.

For docked prompts, the maximum characters include HTML markup, not just readable
text.

**Field Type**
string

**Description**
Internal use only. No data is populated for this field.

**Field Type**
int

**Description**
Required if recurrences are scheduled. Number of days in between occurrences. For a
walkthrough, specify this value on the first step.

**Field Type**
string

**Description**
Description. Maximum of 255 characters.

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
Label for the dismiss button of a floating or targeted prompt. Maximum of 15 characters.

```
displayPosition

displayType

elementRelativePosition

```

**Field Type**
PromptDisplayPosition (enumeration of type string)

**Description**
The position of a floating prompt on the page. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

**Field Type**
PromptDisplayType (enumeration of type string)

**Description**
Required. The type of prompt. Valid values are:

**•** `DockedComposer` —A docked prompt

**•** `FloatingPanel` —A floating prompt

**•** `Targeted` —A targeted prompt. Available in API version 52.0 and later.

**Field Type**
PromptElementRelativePosition (enumeration of type string)

**Description**
Indicates the location of a targeted prompt relative to the element. Available in API version
52.0 and later. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `LeftBottom`

**•** `LeftCenter`

**•** `LeftTop`

**•** `RightBottom`

**•** `RightCenter`

**•** `RightTop`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`


Metadata Types Prompt

**Field Name** **Description**

```
endDate

header

image

imageAltText

imageLink

imageLocation

indexWithIsPublished

```

**Field Type**
date

**Description**
The date to stop showing the in-app guidance. For a walkthrough, specify this value on the
first step.

**Field Type**
string

**Description**
Label for the header of a docked prompt. This value is the label contained in the window’s
browser bar. Maximum of 36 characters.

**Field Type**
string

**Description**
The developer name of the contentAsset that holds the image. You can specify this field or
the `imageLink` field, but not both.

**Field Type**
string

**Description**
Indicates the alt text of an image. Required if `imageLocation`, `imageLink`, or `image`
is specified.

**Field Type**
string

**Description**
The URL for a prompt’s image. You can specify this field or the image field, but not both.
Available in API version 53.0 and later.

**Field Type**
picklist

**Description**
Indicates the location of the image in relation to the body text. Required if `image`,
`imageLink`, or `imageAltText` is specified. Valid values are:

**•** `Top`

**•** `Bottom`

**•** `Right`, which is for floating or targeted prompts only

**•** `Left`, which is for floating or targeted prompts only

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
Used by Salesforce for efficient querying.

```
indexWithoutIsPublished

isPublished

masterLabel

publishedByUser

publishedDate

referenceElementContext

shouldDisplayActionButton

```

**Field Type**
string

**Description**
Used by Salesforce for efficient querying.

**Field Type**
boolean

**Description**
Indicates whether the in-app guidance is active ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**
Required. The label.

**Field Type**
string

**Description**
Internal use only. No data is populated for this field.

**Field Type**
date

**Description**
Indicates the date the in-app guidance was activated. If installed from a package, this value
is the date when the package was installed. For walkthroughs, this field can only be specified
on the first step.

**Field Type**
textarea

**Description**
Used by Salesforce to identify the element that the targeted prompt is associated with.
Available in API version 52.0 and later.

**Field Type**
boolean

**Description**
Indicates whether an action button or link is included ( `true` ) or not ( `false` ).


Metadata Types Prompt

**Field Name** **Description**

```
shouldIgnoreGlobalDelay

startDate

stepNumber

targetAppDeveloperName

targetAppNamespacePrefix

targetPageKey1

targetPageKey2

```

**Field Type**
boolean

**Description**
Indicates whether the in-app guidance ignores the global time delay and instead shows
on page load ( `true` ) or not ( `false` ). This field is available in API version 48.0 and later.

**Field Type**
date

**Description**
Indicates the date to start showing the in-app guidance. For a walkthrough, specify this
value on the first step.

In API version 48.0 and earlier, this field is required.

**Field Type**
int

**Description**
Required for walkthroughs only. Indicates the number of the last step the user viewed or
interacted with in a walkthrough. Include up to 10 steps. Numbers must be consecutive
without repeated or skipped numbers. Available in API version 49.0 and later.

**Field Type**
string

**Description**
The app’s developer name where the in-app guidance appears. Deprecated in API version
51.0 and later.

**Field Type**
string

**Description**
The app’s namespace prefix where the in-app guidance appears. This value must match
the target app’s `NamespacePrefix` in the org that the package is being installed into.
Maximum of 15 characters. Deprecated in API version 51.0 and later.

**Field Type**
string

**Description**
Required. Used by Salesforce to identity the prompt’s page location along with
`targetPageKey2`, `targetPageKey3`, `targetPageKey4`, and
`targetPageType` .

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
Used by Salesforce to identity the prompt’s page location along with `targetPageKey1`,
`targetPageKey3`, `targetPageKey4`, and `targetPageType` .

```
targetPageKey3

targetPageKey4

targetPageType

targetRecordType

themeColor

themeSaturation

```

**Field Type**
string

**Description**
Used by Salesforce to identify the prompt’s page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey4`, and `targetPageType` .

**Field Type**
string

**Description**
Used by Salesforce to identify the prompt’s page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey3`, and `targetPageType` . This field is
available in API version 53.0 and later.

**Field Type**
string

**Description**
Required. Used by Salesforce to identity the page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey3`, and `targetPageKey4` .

**Field Type**
string

**Description**
Used by Salesforce to determine if in-app guidance is specific to a record type. This field is
available in API version 53.0 and later.

**Field Type**
PromptThemeColor (enumeration of type string)

**Description**
Indicates which custom theme color is applied to the in-app guidance. Required if
`themeSaturation` is specified. For a walkthrough, specify this value on the first step.
Valid values are:

**•** `Theme1`, which is derived from the current brand color

**•** `Theme2`, which is derived from the current page background color

**•** `Theme3`, which is derived from the current global header color

**•** `Theme4`, which is derived from the current app theme color

**Field Type**
PromptThemeSaturation (enumeration of type string)


Metadata Types Prompt

**Field Name** **Description**

**Description**
Indicates which color value, or saturation, is applied to the in-app guidance that has a
custom theme color. Required if `themeColor` is specified. For a walkthrough, specify
this value on the first step. Valid values are:

**•** `Dark`

**•** `Light`

```
timesToDisplay

title

uiFormulaRule

userAccess

userProfileAccess

```

**Field Type**
int

**Description**
Required if recurrences are scheduled. The maximum number of times to show the in-app
guidance. Salesforce detects whether the user interacts with the in-app guidance, then
determines whether to show the in-app guidance again or cancel scheduled recurrences.
Maximum value of 30. For a walkthrough, specify this value on the first step.

**Field Type**
string

**Description**
Required. The label for the title. Maximum of 36 characters.

**Field Type**

UiFormulaRule[]

**Description**
A set of one or more permission filters that define the conditions under which the in-app
guidance displays on the page.

If the rule evaluates to `true`, the in-app guidance displays on the page. If `false`, it doesn't
display. If this field is `null`, the in-app guidance displays by default.

**Field Type**
PromptUserAccess (enumeration of type string)

**Description**
Indicates which permissions can see the in-app guidance. Valid values are:

**•** `Everyone`, which indicates that there’s no permission restrictions

**•** `SpecificPermissions`, which indicates that only users with all the specific user
permissions specified can see the in-app guidance

In API version 48.0 and earlier, this field is required.

**Field Type**
PromptUserProfileAccess (enumeration of type string)

**Description**
Indicates which profiles can see the in-app guidance. This field is available in API version
48.0 and later. Valid values are:


Metadata Types Prompt

**Field Name** **Description**

**•** `Everyone`, which indicates that there are no profile restrictions

**•** `SpecificProfiles`, which indicates that users with any of the specified user
profiles can see the in-app guidance

```
versionNumber

videoLink

```

UiFormulaRule

**Field Type**
int

**Description**
Required. The number remains `1` since multiple versions aren’t saved in the org.

**Field Type**
string

**Description**
The embed URL for a video in a docked prompt. Maximum of 1,000 characters. You can
specify this field or the `image` field, but not both. This field is available in API version 48.0
[and later. See Considerations for Creating In-App Guidance.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)

A set of one or more filters that define the conditions under which a prompt displays on a Lightning Experience page.

**Field Name** **Description**

```
booleanFilter

criteria

```

UiFormulaCriterion

**Field Type**
string

**Description**
Specifies the AND filter condition.

**Field Type**

UiFormulaCriterion[]

**Description**
List of one or more filters that, when evaluated, determine visibility.

A single filter that, when evaluated, helps define visibility on a Lightning Experience page.

**Field Name** **Description**

```
leftValue

```

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
Required. The field used for filtering. Only standard and custom
permissions can be included. You can use these expressions in the
`leftValue` field when setting filters for visibility.

**•** `{!$Permission.CustomPermission.` _**`permissionName`**_ `}` —Use
this expression to control visibility based on the custom permissions
of the user viewing the Lightning page. Supported for app, Home,
and record pages only.

**•** `{!$Permission.StandardPermission.` _**`permissionName`**_ `}` —Use
this expression to control visibility based on the standard permissions
of the user viewing the Lightning page. Supported for app, Home,
and record pages only.

**•** `{!ENCODED:{!ID:$` _**`User.Profile.Key`**_ `}}` —Use this
expression to control visibility based on the custom or standard profile
of the user viewing the Lightning page. Available in API Version 48.0
and later.

```
operator

rightValue

```

**Field Type**
string

**Description**
Required. Defines the operator used to filter the data. Valid value is
`EQUAL` .

**Field Type**
string

**Description**
Specifies if you want to evaluate the visibility for permissions or the name
of the profile.

**•** For permissions, use `true` .

**•** For profiles, use the name of the profile. Available in API Version 48.0
and later. For example, `Standard` or `custom_regionalsales` .

Declarative Metadata Sample Definition

The following is an example of a Prompt component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Prompt xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Prompt Label</masterLabel>

   <promptVersions>

     <actionButtonLabel>Learn How</actionButtonLabel>

<actionButtonLink>https://trailhead.salesforce.com/en/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-kanban</actionButtonLink>

```


Metadata Types Prompt

```
        <body>Explore how the Path and the Kanban view can help you track, manage, and

   update your records.</body>

        <delayDays>1</delayDays>

        <description>Kanban floating prompt</description>

        <dismissButtonLabel>OK</dismissButtonLabel>

        <displayPosition>TopLeft</displayPosition>

        <displayType>FloatingPanel</displayType>

        <endDate>2019-03-11</endDate>

        <isPublished>true</isPublished>

        <masterLabel>Prompt Label</masterLabel>

        <publishedDate>2019-03-11</publishedDate>

        <shouldDisplayActionButton>false</shouldDisplayActionButton>

        <shouldIgnoreGlobalDelay>false</shouldIgnoreGlobalDelay>

        <startDate>2019-03-11</startDate>

        <targetAppDeveloperName>LightningSales</targetAppDeveloperName>

        <targetAppNamespacePrefix>standard</targetAppNamespacePrefix>

        <timesToDisplay>3</timesToDisplay>

        <title>Get on the Path to Success</title>

        <userAccess>SpecificPermissions</userAccess>

        <userProfileAccess>SpecificProfiles</userProfileAccess>

        <versionNumber>1</versionNumber>

        <videolink>https://www.youtube.com/embed/Ko-gcObzTVo</videolink>

        <uiFormulaRule>

           <booleanFilter>(1 AND 2 AND 3) AND (4 OR 5)</booleanFilter>

           <criteria>

             <leftValue>{!$Permission.StandardPermission.ActivitiesAccess}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

            <leftValue>{!$Permission.StandardPermission.ContentWorkspaces}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!$Permission.CustomPermission.MyCustomPerm}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!ENCODED:{!ID:$User.Profile.Key}}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>Standard</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!ENCODED:{!ID:$User.Profile.Key}}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>custom_mysysadmin</rightValue>

           </criteria>

        </uiFormulaRule>

      </promptVersions>

   </Prompt>

```


### Metadata Types PublicKeyCertificate

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>Prompt</name>

      </types>

      <version>46.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PublicKeyCertificate

Represents the public key certificate. On this entity we store a public certificate or a JSON web key, which is used to validate the
customer-provided JWT.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PublicKeyCertificate components have the suffix .PublicKeyCertificate and are stored in the PublicKeyCertificate

folder.

Version

### PublicKeyCertificate components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string


Metadata Types PublicKeyCertificate

**Field Name** **Description**

**Description**
A description of the public key certificate.

```
isActive

jsonWebKey

masterLabel

```

**Field Type**
boolean

**Description**
Indicates whether the public key certificate is active (true) or inactive (false). The default
value is false.

**Field Type**
string

**Description**
Represents a public cryptographic key that can be used to verify the validity of a token.

**Field Type**
string

**Description**

Required. The label for the public key certificate.

Declarative Metadata Sample Definition

The following is an example of a PublicKeyCertificate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PublicKeyCertificate xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>pck1</masterLabel>

   <isActive>true</isActive>

   <description>This is my description for a test PublicKeyCertificate</description>

   <jsonWebKey>

{

  "kid":"123456",

  "alg":"RS256",

  "use":"sig",

  "kty":"RSA",

  "x5c":["<Your public certificate>"],

  "y":"y",

  "n":"<Base64-encoded modulus>",

  "e":"<Base64-encoded public exponent>",

  "crv":"crv",

  "d":"d",

  "k":"k"

}

   </jsonWebKey>

</PublicKeyCertificate>

```


### Metadata Types PublicKeyCertificateSet

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2024 salesforce.com, inc.

     ~ All Rights Reserved

     ~ Company Confidential

     -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PublicKeyCertificate</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### PublicKeyCertificateSet

Represents a set of public certificate keys. On this entity we store a public certificates or JSON web keys.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PublicKeyCertificateSet components have the suffix .PublicKeyCertificateSet and are stored in the PublicKeyCertificateSet folder.

Version

### PublicKeyCertificateSet components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.


Metadata Types PublicKeyCertificateSet

Fields

**Field Name** **Description**

```
description

jwksEndPoint

jwtIssuer

masterLabel

publicKeyCertificateSetKeys

type

```

**Field Type**
string

**Description**
A description of the public key certificate set.

**Field Type**
string

**Description**
The URL of the HTTPS Server that returns the JWKS.

**Field Type**
string

**Description**
The user, organization, or service that issued the JSON web token. This value is
case-sensitive.

**Field Type**
string

**Description**

Required. The label for the public key certificate set.

**Field Type**

PublicKeyCertificateSetKey[]

**Description**
A set of public certificate keys associated with the public key certificate set.

**Field Type**
PublicKeyCertificateSetType (enumeration of type string)

**Description**

Required. Determines how the server's public key set is retrieved. The keys are
represented in JWK format.

Values are:

**•** `JWKS`  - Used to specify a certificate via the child Type PublicKeyCertificateSetKey.

**•** `JWKS_URL`  - Used to specify a certificate via the jwksEndPoint field on this Type.

PublicKeyCertificateSetKeys

Represents a set of public certificate keys associated with the public key certificate set.


### Metadata Types Queue

**Field Name** **Description**

```
publicKeyCertificate

```

**Field Type**
string

**Description**

Required.

The PublicKeyCertificate we want to reference.

Declarative Metadata Sample Definition

The following is an example of a PublicKeyCertificateSet component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PublicKeyCertificateSet xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>pcks1</masterLabel>

   <description>This is my description for a PublicKeyCertificateSet</description>

   <type>JWKS</type>

   <jwtIssuer>example.com</jwtIssuer>

   <publicKeyCertificateSetKeys>

        <publicKeyCertificate>pck1</publicKeyCertificate>

   </publicKeyCertificateSetKeys>

</PublicKeyCertificateSet>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>PublicKeyCertificate</name>

   </types>

   <types>

     <members>*</members>

     <name>PublicKeyCertificateSet</name>

   </types>

   <version>62.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Queue

Represents a holding area for items before they are processed.


Metadata Types Queue

Declarative Metadata File Suffix and Directory Location

The file suffix for queue components is `.queue` and components are stored in the `queues` directory of the corresponding package
directory. This component supports cases, leads, service contracts (if Entitlements are enabled), and custom objects.

Version

Queue components are available in API version 24.0 and later.

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this type.

Fields

This metadata type represents the valid values that define a queue:

**Field Name** **Field Type** **Description**

`doesIncludeBosses` boolean Required. Indicates whether records shared with users in this queue are
also shared with users higher in the role hierarchy ( `true` ) or not

( `false` ). This field corresponds to the Grant Access Using Hierarchies
checkbox on the queue’s detail page. Available in API version 67.0 and
later.

`doesSendEmailToMembers` boolean Indicates whether emails are sent to queue members ( `true` ) or not
( `false` ) when a new record is added to the queue.

`email` string The email address of the queue owner.

`name` string Required. The name of the queue. Corresponds to **Label** in the user
interface.

`queueMembers` QueueMembers[]

Represents queue members added to the queue. Members can be added
directly or selected by roles and public groups they belong to. Available
in API version 42.0 and later.

`queueRoutingConfig` string Routing configuration name. Applies to orgs that use Omni-Channel with
a routing configuration. Available in API version 42.0 and later.

`queueSobject` QueueSobject[] Indicates the supported entity types.

QueueMembers

Represents queue members added to the queue. Members can be added directly as users or selected by the roles and public groups
they belong to. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`publicGroups` PublicGroups[] Represents public groups in the org. Public groups are optionally used
to add queue members.


Metadata Types Queue

**Field Name** **Field Type** **Description**

`roleAndSubordinates` RoleAndSubordinates[]

`roleAndSubordinatesInternal` RoleAndSubordinatesInternal[]

Represents roles and their subordinates in the org’s role hierarchy,
including customer and partner roles. Roles and their subordinate
hierarchy are optionally used to add queue members.

Represents internal roles and their subordinates in the org’s role hierarchy,
excluding customer and partner roles. Roles and their subordinate
hierarchy are optionally used to add queue members.

`roles` Roles[] Represents roles in the org. Roles are optionally used to add queue
members.

`users` Users[] Represents users in the org. Users can be added directly as queue
members.

PublicGroups

Represents public groups in the org. Public groups are optionally used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`publicGroup` string Represents a public group.

RoleAndSubordinates

Represents roles and their subordinates in the org’s role hierarchy, including customer and partner roles. Roles and their subordinate
hierarchy can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`roleAndSubordinate` string Represents a role and its subordinates, including customer and partner
roles. Only available when digital experiences is enabled for your org and

Experience Cloud site users are created with external account roles other
than a shared person account role.

RoleAndSubordinatesInternal

Represents internal roles and their subordinates in the org’s role hierarchy, excluding customer and partner roles. Roles and their
subordinate hierarchy can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`roleAndSubordinateInternal` string Represents a role and its subordinates, excluding customer and partner
roles.


Metadata Types Queue

Roles

Represents roles in the org. Roles can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`role` string Represents a role.

Users

Represents users in the org. Users can be added directly as queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`user` string Represents a user. Specify the user’s username.

QueueSobject

QueueSobject represents an entity type that the queue supports.

**Field Name** **Field Type** **Description**

`sobjectType` string Valid values are:

**•** `Case`

**•** `ContactRequest`

**•** `Lead`

**•** `ServiceContract`

**•** `Task` (Available in API version 48.0 and later.)

**•** Custom objects (such as `ObjA_c` )

Declarative Metadata Sample Definition

The following is the definition of a queue, which supports Case, Lead, and a custom object named ObjA.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Queue xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesIncludeBosses>false</doesIncludeBosses>

      <doesSendEmailToMembers>true</doesSendEmailToMembers>

      <email>member@company.com</email>

      <fullName>Your Name</fullName>

      <name>memberQueue</name>

      <queueSobject>

        <sobjectType>Case</sobjectType>

      </queueSobject>

      <queueSobject>

        <sobjectType>Lead</sobjectType>

      </queueSobject>

```


### Metadata Types QueueRoutingConfig

```
      <queueSobject>

        <sobjectType>ObjA__c</sobjectType>

      </queueSobject>

   </Queue>

```

Here’s another definition of a queue containing queue members added directly or via public groups and roles. Queries retrieve values
using the `DeveloperName` field, not the `Name` field, so that the returned names are unique. The query also appends letters to the
end of duplicate names, so these groups and roles can be referred to independently.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Queue xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesIncludeBosses>false</doesIncludeBosses>

      <doesSendEmailToMembers>false</doesSendEmailToMembers>

      <name>queue1</name>

      <queueMembers>

        <publicGroups>

           <publicGroup>All Internal Users</publicGroup>

        <publicGroups>

        <queueRoleAndSubordinates>

           <queueRoleAndSubordinate>role1</queueRoleAndSubordinate>

           <queueRoleAndSubordinate>role2</queueRoleAndSubordinate>

           <queueRoleAndSubordinate>role3</queueRoleAndSubordinate>

        </queueRoleAndSubordinates>

        <roles>

           <role>role1</role>

        </roles>

        <users>

           <user>s@sm.com</user>

           <user>std@sm.com</user>

        </users>

      </queueMembers>

      <queueRoutingConfig>my_omni_routing_config</queueRoutingConfig>

      <queueSobject>

        <sobjectType>Case</sobjectType>

      </queueSobject>

      <queueSobject>

        <sobjectType>Lead</sobjectType>

      </queueSobject>

   </Queue>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### QueueRoutingConfig

Represents the settings that determine how work items are routed to agents.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types QueueRoutingConfig

File Suffix and Directory Location

ServicePresenceStatus components have the suffix `.queueRoutingConfig` and are stored in the `queueRoutingConfigs`
folder.

Version

QueueRoutingConfig components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`capacityPercentage` double The percentage of an agent’s capacity for work items that’s consumed
by a specific type of work item from this service channel. Voice calls must

have a capacity percentage of 100. If an agent receives a voice call, the
agent won’t receive new work items until the call ends, because at that
point the agent’s capacity will have reached 100%.

`capacityType` CapacityType [The setting applies for PSRs (PendingServiceRouting) that are created](https://help.salesforce.com/s/articleView?id=service.omnichannel_psr_lifecycle.htm&type=5&language=en_US)
and managed by the system.

**•** When set to `INHERITED`, the value of the Interruptible check box
or value set on the Service Channel applies.

**•** When set to `INTERRUPTIBLE`, the generated PSR has the
`isInterruptible` flag set to true.

**•** When set to NOT `INTERRUPTIBLE`, the generated PSR has the
`isInterruptible` flag set to false.

**•** When not set, its behavior is equivalent to `INHERITED` .

`capacityWeight` double The amount of an agent’s capacity for work items that’s consumed by
a work item from this service channel. For example, if an agent has a

capacity of 6, and cases are assigned a capacity weight of 2, an agent
can be assigned up to 3 cases before the agent is at capacity and can’t
receive new work items. Voice calls must use the entire capacity weight.

`dropAdditionalSkillsTimeout` int

The number of seconds to elapse before additional skills are dropped
from Omni-Channel routing. In skills-based routing, you can set some

skills to **Additional Skill** . After the timeout elapses, a skill marked as
**Additional Skill** is dropped from Omni-Channel routing and the case
is routed to the best-matched agent, even if the agent doesn’t have all
the skills.

[If CustomRequestedDateTime is set in the PendingServiceRouting object,](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
DropAdditionalSkillsTimeout uses CustomRequestedDateTime as the


Metadata Types QueueRoutingConfig

**Field Name** **Field Type** **Description**

start time. If CustomRequestedDateTime + DropAdditionalSkillsTimeout
has already passed, Omni-Channel immediately drops the additional
skills after the pending service request is created.

`isAttributeBased` boolean Indicates whether this routing configuration is used with skills-based
routing rules ( `true` ) or not ( `false` ).

`label` string Required. The label of the presence status.

`PausedCapacityPercentage` double The percentage of a rep’s capacity that’s consumed when this work item
is paused. The paused capacity feature is available with status-based

capacity and Enhanced Omni-Channel only. Available in API version 64.0
and later.

`PausedCapacityWeight` double The amount of a rep’s capacity that’s consumed when this work item is
paused. The paused capacity feature is available with status-based

capacity and Enhanced Omni-Channel only. Available in API version 64.0
and later.

`pushTimeout` int The number of seconds set for push timeout. `0` is returned when push
timeout isn’t enabled.

`queueOverflowAssignee` string The ID of the queue that’s set as the Overflow Assignee.

`QueueRoutingConfigSkill` QueueRoutingConfigSki **l** [] Default skills associated with the routing configuration. Work is routed
using a combination of rules and default skills.

```
routingModel

```

RoutingModel Required. The routing type that determines how work items are routed
(enumeration of (pushed) to agents. Possible values are:
type string)

**•** `LEAST_ACTIVE`

**•** `MOST_AVAILABLE`

**•** `EXTERNAL_ROUTING`

`routingPriority` int Required. The priority in which work items from the service channels
that are related to this routing configuration are routed to agents. Work

items from routing configurations that have lower priority values (for
example, 0) are routed to agents first.

`userOverflowAssignee` string The ID of the user that’s set as the Overflow Assignee.

QueueRoutingConfigSkill

Represents default skills associated with the routing configuration.


### Metadata Types QuickAction

Fields

**Field Name** **Field Type** **Description**

`skill` string Skill used to route a work item.

Declarative Metadata Sample Definition

The following is an example of a QueueRoutingConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <QueueRoutingConfig xmlns="http://soap.sforce.com/2006/04/metadata">

     <capacityWeight>1.0</capacityWeight>

     <label>Case Routing</label>

     <pushTimeout>120</pushTimeout>

     <queueOverflowAssignee>queueOverflow</queueOverflowAssignee>

     <routingModel>LEAST_ACTIVE</routingModel>

     <routingPriority>1</routingPriority>

     <capacityType>INHERITED</capacityType>

     <pausedCapacityWeight>0.25</pausedCapacityWeight>

   </QueueRoutingConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>QueueRoutingConfig</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### QuickAction

Represents a specified create or update quick action for an object that then becomes available in the Chatter publisher. For example,
you can create an action that, on the detail page of an account, allows a user to create a contact related to that account from the Chatter
feed on that page. QuickAction can be created on objects that permit custom fields.

The parent objects supported include:

**•** Account

**•** Campaign

**•** Case

**•** Contact


Metadata Types QuickAction

**•** ContentNote

**•** Custom objects

**•** Group

**•** Lead

**•** Opportunity

File Suffix and Directory Location

QuickAction components have the suffix `quickAction` and are stored in the `quickActions` folder.

Version

QuickAction components are available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`canvas` string If the custom action invokes a Canvas app, the app name. Returns the
fully qualified name of the Canvas app in the format

`<namespace>__<dev_name>`, if the quick action type is `Canvas` ;
otherwise, returns `null` .

This field is available in API version 29.0 and later.

`description` string The description of the action.

`fieldOverrides` FieldOverride on The specific field that can be overridden within a QuickAction on page
page 1807[] 1803.

`flowDefinition` string If the custom action invokes a flow, this field represents the API name
of the flow. Otherwise, this field is `null` .

`height` int If a custom action is created, this field represents the height in pixels of
the action pane.

`icon` string

`isProtected` boolean

The icon used to identify the action.

API version 32.0 and later returns different icons than in earlier API
versions.

Indicates whether this component is protected ( `true` ) or not ( `false` ).
Protected components cannot be linked to or referenced by components
created in the installing organization.

`label` string Identifies the action and displays to users. Also the default identifier used
for the API and managed packages.

`lightningComponent` string

If the custom action invokes a Lightning component, this field represents
the fully qualified name of the component. Otherwise, this field is `null` .

Available in API version 38.0 and later.


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

`optionsCreateFeedItem` boolean

Required. Indicates whether successful completion of the action creates
a feed item ( `true` ) or not ( `false` ). Applies only to Create Record,
Update Record, and Log a Call quick action types.

Available in API version 36.0 and later.

`page` string If the custom action invokes a Visualforce page, this field identifies the
page.

`quickActionLayout` QuickActionLayout The layout of fields on the action.

`quickActionParameter` QuickActionParameter[]

The input and output of the quick action.

Available in API version 63.0 and later.

```
standardLabel

```

QuickActionLabel Specifies the standard label to use for the action. The valid values are:
(enumeration of

**•** `AddRecord`

type string)

**•** `AddMember`

**•** `ChangeDueDate`

**•** `ChangePriority`

**•** `ChangeStatus`

**•** `CreateNew`

**•** `CreateNewRecordType` (For example, a label with something
like “Create New Idea”)

**•** `Defer`

**•** `EditDescription`

**•** `EnrollInProgram` (Available in API versions 46.0 and later only
if the org has Health Cloud enabled)

**•** `Escalate`

**•** `EscalateToRecord`

**•** `Forward` (Available in API version 42.0 and later)

**•** `LogACall`

**•** `LogANote`

**•** `ModifyAppointment` (Available in API version 47.0 and later)

**•** `New` (A new record)

**•** `NewChild` (A new child record)

**•** `NewChildRecordType`

**•** `NewRecordType` (For example, a label with something like “New
Idea”)

**•** `OfferFeedback`

**•** `PatientDetails` (Available in API version 57.0 and later if the
org has Health Cloud enabled)

**•** `PerformCount` (Available in API version 63.0 and later.)

**•** `Quick` (A quick record)


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

**•** `QuickRecordType`

**•** `RelocateAsset` (Available in API version 63.0 and later)

**•** `ReplaceAsset` (Available in API version 63.0 and later)

**•** `Reply` (Available in API version 42.0 and later)

**•** `ReplyAll` (Available in API version 42.0 and later)

**•** `RequestFeedback`

**•** `SendEmail` (This value is available in API version 31.0 and later.)

**•** `Update`

`successMessage` string

`targetObject` string

`targetParentField` string

The message that displays to the user upon successful completion of
the action.

Available in API version 36.0 and later.

The object for which the action is created and performed.

For example, you can create an action that, on the detail page of an
account, allows a user to create a contact related to that account from

the Chatter feed on that page. QuickAction can be created on objects
that permit custom fields. In this case, Contact is the `targetObject` .

The parent object type of the action. Links the target object to the parent
object. For example, use Account if the target object is Contact and the
parent object is Account.

`targetRecordType` string Specifies which record type to create. Valid values are:

**•** Business Account

**•** Person Account

**•** Master

```
type

```

QuickActionType Required. The type of quick action. Valid values are:
(enumeration of

**•** `Canvas`

type string)

**•** `Create`

**•** `Flow` (This value is available as a Beta in API version 41.0 and later)

**•** `LightningComponent` (This value is available in API version
38.0 and later.)

**•** `LogACall`

**•** `Post`

**•** `SendEmail` (This value is available in API version 31.0 and later.)

**•** `SocialPost`

**•** `Update`

**•** `VisualforcePage`


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

`width` int If a custom action is created, this field represents the width in pixels of
the action pane.

FieldOverride

Represents the field names and their respective formulas and literal values that comprise predefined value settings for a QuickAction on
page 1803. If a field on an action has both a predefined value and a default value set, the action uses the predefined value, not the default
value. A formula value takes precedence over a literal value if both are defined.

**Field Name** **Field Type** **Description**

`field` string Required. The name of the field to allow predefined values on.

`formula` string Specifies the formula to use when setting a field’s predefined value.
Supported for single-select picklists as of API version 43.0.

`literalValue` string

QuickActionLayout

Supported for picklists only. Specifies the literal value of the field defined
from values in the picklist. Corresponds to the Specific Value field in the
predefined value UI.

The layout of fields on the action. There’s no hard limit to the number of fields you can add to an action layout. However, for optimum
usability, we recommend a maximum of eight fields. Adding more than 20 fields can severely affect user efficiency.

**Field Name** **Field Type** **Description**

```
layoutSectionStyle

```

LayoutSectionStyle Required. The type of layout structure used. The valid values are:
(enumeration of type

**•** `TwoColumnsTopToBottom`

string)

**•** `TwoColumnsLeftToRight`

**•** `OneColumn`

**•** `CustomLinks`

`quickActionLayoutColumns` QuickActionLayoutColumn Specifies columns in a QuickActionLayout on page 1807.
on page 1807[]

QuickActionLayoutColumn

A column defined for a QuickActionLayout on page 1807.

**Field Name** **Field Type** **Description**

`quickActionLayoutItems` QuickActionLayoutItem Specifies row items in a QuickActionLayoutColumn on page 1807.
on page 1808 []


Metadata Types QuickAction

QuickActionLayoutItem

A row item comprised of fields and defined for a QuickActionLayoutColumn on page 1807.

**Field Name** **Field Type** **Description**

`emptySpace` boolean Controls if this layout item is a blank space ( `true` ) or not ( `false` ).

`field` string Represents a specific field in QuickActionLayoutItem on page 1808.

```
uiBehavior

```

UiBehavior Specifies user input behavior for specific fields in QuickActionLayoutItem
(enumeration of type on page 1808. The valid values are:
string)

**•** `Edit`

**•** `Required`

**•** `Readonly`

QuickActionParameter

Represents the input and output of the associated quick action. Available in API version 63.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Name of the parameter.

```
type

```

QuickActionParameterType Required. `Input` is the only valid value.
(enumeration of type
string)

`value` string Represents the value associated with the given parameter name.

Declarative Metadata Sample Definition

The following is an example of a QuickAction on page 1803 component:

```
<?xml version="1.0" encoding="UTF-8"?>

<QuickAction xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>testActionDefinitionTypesCreateTask</description>

   <label>testActionDefinitionTypesCreateTask</label>

   <optionsCreateFeedItem>true</optionsCreateFeedItem>

   <quickActionLayout>

     <layoutSectionStyle>TwoColumnsLeftToRight</layoutSectionStyle>

     <quickActionLayoutColumns>

        <quickActionLayoutItems>

          <emptySpace>false</emptySpace>

          <field>OwnerId</field>

          <uiBehavior>Required</uiBehavior>

        </quickActionLayoutItems>

        <quickActionLayoutItems>

          <emptySpace>false</emptySpace>

          <field>WhoId</field>

```


### Metadata Types RedirectWhitelistUrl

```
             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>WhatId</field>

             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>ActivityDate</field>

             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Subject</field>

             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Status</field>

             <uiBehavior>Required</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Priority</field>

             <uiBehavior>Required</uiBehavior>

           </quickActionLayoutItems>

        </quickActionLayoutColumns>

        <quickActionLayoutColumns/>

      </quickActionLayout>

      <successMessage>This is a success message</successMessage>

      <targetObject>Task</targetObject>

      <targetParentField>What</targetParentField>

      <type>Create</type>

   </QuickAction>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RedirectWhitelistUrl

Represents a trusted URL that’s excluded from redirection restrictions when the `redirectionWarning` or
`redirectBlockModeEnabled` field on the SessionSettings Metadata type is set to `true` . This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.


### Metadata Types RecommendationStrategy

File Suffix and Directory Location

RedirectWhitelistUrl components have the suffix `.redirectWhitelistUrl` and are stored in the `redirectWhitelistUrls`
folder.

Version

RedirectWhitelistUrl components are available in API version 48.0 and later.

Special Access Rules

Only authenticated internal and external users with the View Setup and Customize Application permissions can access or edit this type.

Fields

**Field Name** **Field Type** **Description**

`url` string
Required. The trusted URL.

These formats are accepted: `example.com`, `*.example.com`,
and `https://example.com` .

The host section of the URL can include an asterisk ( `*` ) as a wildcard.
Otherwise, the URL cannot be malformed. Examples of malformed URLs
that fail a syntax check are `malformed^url.example.com`, and
`https://{subdomain}.example.com` .

To add a `URL` based on parameters, build the URL before you add it to
this Metadata Type.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RecommendationStrategy

Represents a recommendation strategy. Recommendation strategies are applications, similar to data flows, that determine a set of
recommendations to be delivered to the client through data retrieval, branching, and logic operations.

File Suffix and Directory Location

### RecommendationStrategy components have the suffix .recommendationStrategy and are stored in the

`recommendationStrategies` folder.


Metadata Types RecommendationStrategy

Version

RecommendationStrategy components are available in API version 45.0 and later.

Special Access Rules

Metadata access for the RecommendationStrategy type is backed by the ManageRecommendationStrategies user permission.

Fields

**Field Name** **Field Type** **Description**

`actionContext` StrategyAction[] An array of action contexts used by the strategy.

`contextRecordType` string The sObject type of the $record used by the flow.

`description` string Description of the recommendation strategy.

`filter` StrategyNodeFilter[] An array of filter nodes.

`if` StrategyNodeIf[] An array of if nodes.

`invocableAction` StrategyNodeInvocableAction[] An array of Apex invocable action nodes. Available in API version 46.0
and later.

`isTemplate` boolean Indicates whether the recommendation strategy is a template ( `true` )
or not ( `false` ). When installed from managed packages,

recommendation strategies can’t be viewed or cloned by subscribers
because of intellectual property (IP) protection. But when those
recommendation strategies are templates, subscribers can open them
in a builder, clone them, and customize the clones. The default value of
this field is `false` . Available in API version 47.0 and later.

`label` string Required. Label for the flow.

`map` StrategyNodeMap[] An array of map nodes. Available in API version 46.0 and later.

`mutuallyExclusive` StrategyNodeExclusive[] An array of mutuallyExclusive nodes.

`onBehalfOfExpression` string

Formula expression defining the intended target of the recommendations
(in other words, the Contact associated with a Case). Mainly used for
reaction tracking.

`recommendationLimit` StrategyNodeRecommendationLimit[] An array of recommendation limit nodes.

`recommendationLoad` StrategyNodeRecommendationLoad[] An array of recommendation load nodes.

`sort` StrategyNodeSort[] An array of sort nodes.

`union` StrategyNodeUnion[] An array of union nodes.


Metadata Types RecommendationStrategy

StrategyNodeBase

Base class for all strategy nodes. This is an abstract class.

**Field Name** **Field Type** **Description**

`childNode` string Array of child node names, in order of execution.

`description` string Description of the node.

`label` string Label of the node.

`name` string Required. Unique name of the node.

StrategyAction

Defines a call to an invocable action from the strategy. Results are used by decision elements in the strategy.

**Field Name** **Field Type** **Description**

`action` string Required. The name or id of the InvocableAction to execute.

`argument` StrategyActionArg[] List of strategy action arguments.

`description` string Description of the strategy.

`label` string Label for the strategy action.

`name` string Required. Unique name of the strategy action, which is referenced by
decisioning elements in the strategy.

```
type

```

InvocableActionType Required. The action type. Valid values are:
(enumeration of type

**•** `activateSessionPermSet` —Activates a session-based permission

string)

set for the running user.

**•** `activationSchema`         - Gets the activation schema for the specified
activation. This value is available in API version 64.0 and later.

**•** `addMessageToChat` —Adds a message to an existing Salesforce
Anywhere chat. This value is available in API version 49.0 and later.

**•** `addMessageToQuipChat` —Adds a Quip message to an existing chat
room. This value is available in API version 46.0 and later.

**•** `addMessageToQuipDocument` —Adds a Quip message to an existing
Quip document, spreadsheet, or slide. This value is available in API version
46.0 and later.

**•** `addQuipDocumentToFolder` —Adds an existing Quip document,
spreadsheet, or slide to an existing folder. This value is available in API
version 46.0 and later.

**•** `addUsersToChat` —Adds users to an existing Salesforce Anywhere
chat. This value is available in API version 49.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `addUsersToQuipDocument` —Adds users, identified by their email
addresses, to an existing Quip document, spreadsheet, or slide. This value
is available in API version 46.0 and later.

**•** `addUsersToQuipChat` —Adds users, identified by their email
addresses, to an existing Quip chat room. This value is available in API
version 46.0 and later.

**•** `answerQuestionsWithSalesforceDocumentation` —Searches
Salesforce documentation to answer questions and provide links to relevant
articles.

**•** `attachQuipDocumentToRecord` —Attaches a Quip document,
spreadsheet, or slide to a Salesforce record. This value is available in API
version 46.0 and later.

**•** `apex` —Invokes an Apex method that has the @invocableMethod
annotation.

**•** `archiveKnowledgeArticles` —Archives a list of published
Knowledge articles. This value is available in API version 45.0 and later.

**•** `assignKnowledgeArticles` —Mass assigns knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `cdpRunIdentityResolution` —Runs a Data 360 identity resolution
process. This value is available in API version 57.0 and later.

**•** `chat` —Creates a Salesforce Anywhere chat. This value is available in API
version 49.0 and later.

**•** `chatterPost` —Posts to Chatter.

**•** `choosePricebook` —Selects a price book.

**•** `contactRequestAction` —Creates a contact request record. This
value is available in API version 45.0 and later.

**•** `component` —Invokes the Lightning component that implements the
`lightning:availableForFlowActions` interface and that is
referenced by `actionName` . This value is available in API version 43.0
and later.

**•** `contentWorkspaceEnableFolders` —Enables folders in a library.

**•** `convertAttributesToJson` —Converts the given attributes into
a JSON string format. This value is available in API version 64.0 and later.

**•** `copyQuipDocument` —Creates a copy of an existing Quip document,
spreadsheet, or slide, and gives it a new title. This value is available in API
version 46.0 and later.

**•** `createDraftFromOnlineKnowledgeArticle` —Creates a draft
from a published knowledge article. This value is available in API version
45.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
from a purchase order. Available to B2B Commerce. This value is available
in API version 49.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `createQuipChat` —Creates a Quip chat room. This value is available
in API version 46.0 and later.

**•** `createQuipDocument` —Creates a Quip document, spreadsheet, or
slide. This value is available in API version 46.0 and later.

**•** `createQuipFolder` —Creates a Quip folder. This value is available in
API version 46.0 and later.

**•** `customNotificationAction` —Sends a custom notification. This
value is available in API version 46.0 and later.

**•** `deactivateSessionPermSet` —Deactivates a session-based
permission set for the running user.

**•** `deleteKnowledgeArticle` —Deletes a draft version (translation
or master-language) or an entire archived knowledge article. This value is
available in API version 46.0 and later.

**•** `dynamicSendSurveyInvitation` —Sends customized notifications
to users about important events or updates to the records that they’re
working on. This value is available in API version 51.0 and later.

**•** `editQuipDocument` —Modifies the contents of an existing Quip
document, spreadsheet, or slide. This value is available in API version 46.0
and later.

**•** `emailAlert` —Sends an email by referencing a workflow email alert

**•** `emailSimple` —Sends an email by using flow resources

**•** `exploreConversation` —Retrieves insights from a conversation.
This value is available in API version 61.0 and later.

**•** `externalConnector` —Executes a process or method exposed via a
connector to an external system. This value is available in API version 63.0
and later.

**•** `externalService` —Invokes an External Service operation that makes
an HTTP request to an external system made available by an External Service
schema registered through Setup. This value is available in API version 46.0
and later.

**•** `findMatchingIndividuals` —Finds contact, lead, or employee
records that match a search term.

**•** `findPastCollaborators`

—Leverages insights from Einstein Activity Capture to identify individuals
with past collaborative ties, aiding in securing introductions to relevant
parties in ongoing or future deals. This value is available in API version 63.0
and later.

**•** `flow` —Invokes an autolaunched flow. This action type isn’t available for
flows with a processType of Flow or AutolaunchedFlow. To invoke an
autolaunched flow from one of those types, use FlowSubflow. This value
is available in API version 32.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `generateAiAgentResponse` —Generates a response from the AI
agent based on input and instructions to support intelligent, conversational
experiences. This value is available in API version 63.0 and later.

**•** `generateVerificationCode` —Sends a verification code to the
customer's email to verify their identity. This value is available in API version
63.0 and later.

**•** `getArticleSmartLinkUrl` —Gets the Smart Link URL of the
Salesforce Knowledge article. Smart links go to the right article and version,
even when a new version is published or the URL name changes. This value
is available in API version 54.0 and later.

**•** `getPoliciesByObject` —Gets Policy Center policies that contain a
given object and returns a list of matching policy names.

**•** `getPoliciesByPolicyType` —Gets Policy Center policies of the
type specified in the user input, such as Data Backup or Data Archive.

**•** `getPolicyDetails` —Gets details about a policy in Policy Center,
such as the policy type and the objects the policy targets.

**•** `getProductPricing` —Gets the pricing information of a product,
including relevant historical sale price data from previous won deals
involving the same product. This value is available in API version 63.0 and
later.

**•** `goToCadenceStep` —Jumps to the specified step in the Sales cadence.
This value is available in API version 57.0 and later.

**•** `internalTestAction` —Reserved for internal use.

**•** `internalTestConnectApiAction` —Reserved for internal use.

**•** `limitRepetitions` —Limit the number of times the same
recommendation or offer appears on the same record or for the same user
during a time period in a recommendation strategy flow. This value is
available in API version 55.0 and later.

**•** `massUpdateAccountForecast` —Bulk updates forecasts
asynchronously. This value is available in API version 48.0 and later.

**•** `massUpdateSalesAgreement` —Bulk updates sales agreements
asynchronously. This value is available in API version 48.0 and later.

**•** `quickAction` —Invokes a QuickAction.

**•** `publishActionableOrchSrcEvent` —Publishes events triggered
by an external system. This value is available in API version 62.0 and later.

**•** `publishKnowledgeArticles` —Mass publishes knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `restoreKnowledgeArticleVersion` —Restores an archived
version of a knowledge article. This value is available in API version 45.0
and later.

**•** `reviewBuyingCommittee` —Identifies and reviews key contacts
associated with a deal, their influence on that deal, and other deals that
they’ve impacted. This value is available in API version 63.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `sendAlert` —Sends Salesforce Anywhere alerts to users. This value is
available in API version 49.0 and later.

**•** `sendNotification` —Sends an available notification type. This value
is available in API version 54.0 and later.

**•** `sendSurveyInvitation` —Sends email survey invitations to leads,
contacts, and users in your org based on an action, such as when a customer
support case closes. This value is available in API version 47.0 and later.

**•** `performSurveySentimentAnalysis` —Perform survey sentiment
analysis to create or update the AI Sentiment Result records. This value is
available in API version 55.0 and later.

**•** `skillsBasedRouting` [—Creates a PendingServiceRouting record](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
used for Omni-Channel skills-based routing. This value is available in version
44.0 and later.

**•** `slackArchiveChannel` —Archives a Slack channel in a Slack
workspace. This value is available in API version 54.0 and later.

**•** `slackCheckUsersAreConnectedToSlack` —Indicates whether
a collection of Salesforce users is connected to a given Slack app. This value
is available in API version 54.0 and later.

**•** `slackCreateChannel` —Creates a Slack channel in a Slack workspace.
This value is available in API version 54.0 and later.

**•** `slackGetConversationInfo` —Retrieves the name of a Slack
channel or group direct message and finds out whether it’s archived. This
value is available in API version 54.0 and later.

**•** `slackInviteUsersToChannel` —Adds users who are connected
to a given Slack app to a Slack channel or group direct message. This value
is available in API version 54.0 and later.

**•** `slackPinMessage` —Pin or unpin a message in a Slack channel or
group direct message. This value is available in API version 54.0 and later.

**•** `slackPostMessage` —Send a message to a Slack channel or group
direct message. This value is available in API version 54.0 and later.

**•** `slackSendMessageToLaunchFlow` —Send a message to a Slack
channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow. This value is
available in API version 55.0 and later.

**•** `slackUpdateMessage` —Edits a message that was previously sent
to a Slack channel or group direct message. This value is available in API
version 54.0 and later.

**•** `submitKnowledgeArticleForTranslation` —Submits a
published or draft knowledge article for translation. This value is available
in API version 46.0 and later.

**•** `submit` —Submits a record for approval.

**•** `triggerJourney`                        - Send an individual to a specified journey. This
value is available in API version 64.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `verifyCustomerCode` —Verifies the code entered by the customer
to complete identity verification. This value is available in API version 49.0
and later.

These values are used in Omnichannel Inventory. If no version is specified, the
value is available in API version 51.0 and later.

**•** `ociCreateReservation` —Creates one or more inventory
reservations at a location or location group.

**•** `ociFulfillReservation` —Fulfills one or more inventory
reservations at a location.

**•** `ociGetAvailability` —Gets inventory availability data for one or
more products at one or more inventory locations or location groups.

**•** `ociReleaseReservation` —Releases one or more inventory
reservations.

**•** `ociTransferReservation` —Transfers one or more inventory
reservations between locations or location groups.

These values are used in the B2B Commerce Checkout Flow. If no version is
specified, the value is available in API version 47.0 and later.

**•** `updateCheckoutSessionStateAction` —Updates the checkout
session next state for checkout flows. This value is available in API version
49.0 and later.

**•** `priceCart` —Requests prices for all items in a cart during B2B Commerce
checkout. This value is available in API version 47.0 and later.

**•** `checkoutSessionAction` —Initiates or retrieves an existing
Checkout Session for Checkout Flows. Available to B2B Commerce. This
value is available in API version 49.0 and later.

**•** `cancelCartAsyncOperation` —Cancels a WebCart’s async
operation. Available to B2B Commerce. This value is available in API version
49.0 and later.

**•** `calcCartPromotionsAction` —Requests a full cart promotion
calculation of all applicable line items in the Web Cart during B2B
Commerce checkout. This value is available in API version 52.0 and later.

**•** `checkCartInventoryAction` —Requests an inventory for all items
in a Web Cart during B2B Commerce checkout. This value is available in
API version 47.0 and later.

**•** `calcCartShipmentAction` —Calculates the shipping cost for all
items in a Web Cart during B2B Commerce checkout. This value is available
in API version 47.0 and later.

**•** `cartToOrderAction` —Creates a Salesforce Standard Order in draft
mode. This value is available in API version 47.0 and later.

**•** `activateOrderAction` —Activates a draft order, which creates an
order summary. This value is available in API version 47.0 and later.

[For values used in Business Rules Engine, see Flow for Business Rules Engine.](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/bre_flow_metadata_api.htm)


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in Context Service. If no version is specified, the value is
available in API version 64.0 and later.

**•** `deleteContextCache` —Deletes the context instance from the
context cache using specified context ID.

**•** `queryContextTags` —Queries context instance tags associated with
a context definition.

**•** `updateContextAttributes` —Updates attributes on the context
instance using context tags.

These values are used in the Commerce Checkout Flow. If no version is specified,
the value is available in API version 55.0 and later.

**•** `addCartItem` —Adds an item to a cart during Commerce checkout.

**•** `createCart` —Creates a cart during Commerce checkout.

**•** `deleteCart` —Deletes a cart during Commerce checkout.

These values are used in Data 360. If no version is specified, the value is available
in API version 64.0 and later.

**•** `dataKitGetComponentAction` Gets the deployment status of
data kit deployment jobs.

**•** `dataKitDeployComponentAction` Deploys data kit components
in a target org.

These values are used in Salesforce CMS Workflows and Approvals. If no version
is specified, the value is available in API version 58.0 and later.

**•** `managedContentPublishVariant` —Publishes a content variant
associated with a flow. This value is available in API version 59.0 and later.

**•** `managedContentRoleStepInteractive` —Assigns a content
variant review to a CMS role.

**•** `managedContentUnpublishVariant` —Unpublishes a published
content variant associated with a flow. This value is available in API version
59.0 and later.

**•** `managedContentVariantSetLockStatus` —Sets the locked
status of a content variant.

**•** `managedContentVariantSetReadyStatus` —Sets the ready
for publication status of a content variant.

These values are used in Employee Service. If no version is specified, the value
is available in API version 64.0 and later.

**•** `createServiceRequestCase` —Creates a case or incident for the
requested service.

**•** `getDirectDepositDetails` —Gets the direct deposit details for
the specified record ID.

**•** `getLeaveBalance` —Gets the leave balance of a specific employee.

These values are used in Insurance. If no version is specified, the value is available
in API version 63.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `cancelInsurancePolicy` —Cancel an insurance policy by using a
set of user inputs that represent policy details.

**•** `endorseInsurancePolicy` —Endorse an insurance policy by using
a set of user inputs that represent policy details.

**•** `getInsurancePolicy` —Get the details of an insurance policy.

**•** `issueInsurancePolicy`                        - Issue an insurance policy by using a set
of user inputs that represent policy details.

**•** `renewInsurancePolicy` —Renew an insurance policy by using a
set of user inputs that represent policy details.

These values are used in Insurance Brokerage. If no version is specified, the
value is available in API version 63.0 and later.

**•** `computeProducerSplits` —Compute the producer splits for the
producers associated with an Insurance Policy, for a Commission Statement
Line Item.

**•** `createProducerCommissions` —Create records for the
commissions that producers receive for the insurance policy associated
with the specified commission statement line item, and update the
commission statement line item record status.

**•** `findInsurancePolicy` —Get the insurance policy associated with
a commission statement line item that matches the specified criteria, and
update the status of the commission statement line item record.

These values are used in Order Management. If no version is specified, the value
is available in API version 48.0 and later.

**•** `addOrderItemSummarySubmit` —Adds order item summaries to
an order summary. This value is available in API version 54.0 and later.

**•** `adjustOrderItemSummariesPreview` —Previews the expected
results of applying a price adjustment to order item summaries from an
order summary without actually applying it. This value is available in API
version 49.0 and later.

**•** `adjustOrderItemSummariesSubmit` —Applies a price adjustment
to order item summaries from an order summary. This value is available in
API version 49.0 and later.

**•** `authorizePayment` —Authorizes a card payment. This value is
available in API version 55.0 and later.

**•** `cancelFulfillmentOrderItem` —Removes items from a
fulfillment order.

**•** `cancelOrderItemSummariesPreview` —Previews the expected
results of canceling order item summaries from an order summary without
actually canceling them.

**•** `cancelOrderItemSummariesSubmit` —Cancels order item
summaries from an order summary.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `confirmHeldFulfillmentOrderCapacity` —Confirms held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `createCreditMemoOrderSummary` —Creates a credit memo for
an order summary.

**•** `createFieldGnrnPromptTmplResp` —Creates a field generation
prompt template response. This value is available in API version 62.0 and
later.

**•** `createFulfillmentOrder` —Creates one or more fulfillment orders
and fulfillment order products for an order delivery group summary, which
defines a recipient and delivery method.

**•** `createFulfillmentOrders` —Creates fulfillment orders and
fulfillment order products for multiple order delivery group summaries,
each of which defines a recipient and delivery method. This value is available
in API version 51.0 and later.

**•** `createInvoiceFromChangeOrders` —Creates an invoice for one
or more change orders. This value is available in API version 56.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
for a fulfillment order.

**•** `createOrderPaymentSummary` —Creates an order payment
summary for an authorization or payments belonging to an order summary.

**•** `createOrderSummary` —Creates an order summary for an order.

**•** `createReturnOrder` —Creates a return order and return order items
for an order.

**•** `ensureFundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure funds through a payment provider for an
invoice belonging to an order summary.

**•** `ensureRefundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure refunds through a payment provider for an
invoice belonging to an order summary.

**•** `getFulfillmentOrderCapacityValues` —Gets fulfillment
order capacity information. This value is available in API version 55.0 and
later.

**•** `holdFulfillmentOrderCapacity` —Holds fulfillment order
capacity. This value is available in API version 55.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplits` —Evaluates
ordered product quantities against available inventory to determine the
smallest combination of locations that can fulfill the order. This value is
available in API version 51.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplitsUsingOCI` —Evaluates
ordered product quantities against available inventory at specified location
groups and locations to determine the smallest combination of locations
that can fulfill the order. This value is available in API version 54.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `orderRoutingRankByAverageDistance` —Calculates the
average distance from sets of inventory locations to an order recipient, and
returns the sets sorted by that average distance. This value is available in
API version 51.0 and later.

**•** `releaseHeldFulfillmentOrderCapacity` —Releases held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `returnOrderItemSummariesPreview` —Previews the expected
results of returning order item summaries from an order summary without
actually returning them.

**•** `returnOrderItemSummariesSubmit` —Returns order item
summaries from an order summary.

**•** `returnReturnOrderItems` —Processes return order line items.

[For values used in Financial Services Cloud, see Flow for Financial Services](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_meta_visual_workforce.htm)
[Cloud.](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_meta_visual_workforce.htm)

For values used in Fundraising for Nonprofit Cloud, see Flow for Fundraising.

[For values used in Health Cloud, see Flow for Health Cloud.](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/health_cloud_flow_metadata_api.htm)

[For values used in Manufacturing Cloud, see Flow for Manufacturing Cloud.](https://developer.salesforce.com/docs/atlas.en-us.262.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_flow_metadata_api.htm)

[For values used in Automotive Cloud, see Flow for Automotive Cloud.](https://developer.salesforce.com/docs/atlas.en-us.mfg_api_devguide.meta/mfg_api_devguide/https://developer.salesforce.com/docs/atlas.en-us.262.0.automotive_cloud.meta/automotive_cloud/auto_flow_metadata_api.htm)

This value is used in Omnistudio.

**•** `executeIntegrationProcedure` —Executes an Integration
Procedure with Agentforce configured. This value is available in API version
64.0 and later.

These values are used in Rebate Management.

**•** `addRebateMemberList` —Adds a list of members to a rebate program.
This value is available in API version 51.0 and later.

**•** `calculateProjectedRebateAmount` —Calculates the projected
rebate amount for rebate types associated with a specified transaction ID.
This value is available in API version 54.0 and later.

**•** `calculateRebateAmountAndUpsertPayout` —Calculates the
rebate amount and upserts the rebate payout for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getBenefitAndCalculateRebateAmount`                        - Gets benefit details,
and optionally calculates the rebate amount for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getEligibleProgramRebateTypes` —Retrieves the eligible
program rebate types for a mapped object. This value is available in API
version 52.0 and later.

**•** `generateRebatePayoutPeriods` —Generates payout periods for
a rebate program based on the frequency specified in the program. This
value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `processRebatesBatchCalculationJob` —Processes a rebate
batch calculation job from the Data Processing Engine. This value is available
in API version 51.0 and later.

**•** `processProgramRebateTypeProducts` —Insert or delete records
in the Program Rebate Type Product object. This value is available in API
version 53.0 and later.

**•** `rebatesProcessCSV` —Processes an uploaded CSV file using Bulk
API 2.0 and converts the file’s data into records in the target object. This
value is available in API version 51.0 and later.

**•** `upsertCustomRebatePayout` —Upserts the custom calculated
rebate payout for the specified aggregate record. This value is available in
API version 51.0 and later.

These values are used in B2B Referral Management. If no version is specified,
the value is available in API version 64.0 and later.

**•** `enrollAdvocateB2bReferralProm` —Enroll an existing or new
customer as an advocate for a referral promotion.

**•** `processB2bReferralEvent` —Create referral event records when
an advocate refers a friend, or when referred friends sign up or make a
purchase.

These values are used in Referral Marketing.

**•** `processReferralEvent` —Create referral event records when an
advocate refers a friend, or when referred friends sign up or make a
purchase. This value is available in API version 60.0 and later.

These values are used in Loyalty Management.

**•** `adjustPoints` —Adjusts loyalty points for a specified program member
or journal transaction. This value is available in API version 51.0 and later.

**•** `assignTierBenefits`                        - Assigns Member Benefits to a member tier
for benefits that are associated with a Benefit Action. This value is available
in API version 51.0 and later.

**•** `cancelAccrual` —Cancels a specific set of accrual transactions.

**•** `creditPoints` —Credits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `cancelRedemption` —Reverts a specific set of redemption transactions.
This value is available in API version 51.0 and later.

**•** `changeTier` —Changes the tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `changeTierWhenNoErrors` —Changes tier for a specified loyalty
program member only when all the input parameters meet the criteria.
This value is available in API version 51.0 and later.

**•** `debitPoints` —Debits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `executeMemberBenefit` —Processes the benefit action associated
with the benefit, which is assigned to a loyalty program member. This value
is available in API version 51.0 and later.

**•** `generateMemberReferralCode` —Generates a unique 8-character
referral code for a loyalty program member. This value is available in API
version 57.0 and later.

**•** `getMemberActiveSegments` —Retrieve active Data 360 market
segments that a loyalty program member is a part of.

**•** `getTier` —Gets the current tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `getPointsBalance` —Gets the loyalty points balance for a specified
program member. This value is available in API version 51.0 and later.

**•** `getLoyaltyPromotion` —Gets active loyalty promotions based on
a transaction journal. This value is available in API version 53.0 and later.

**•** `getLoyaltyPromotionBasedOnSalesforceCDP` —Gets
promotions for a member based on the market segment the member
belongs to. This value is available in API version 53.0 and later.

**•** `issueVoucher` —Issues a voucher for a member or contract. This value
is available in API version 51.0 and later.

**•** `mergeLoyaltyProgramMembership` —Merges two active loyalty
program member records that both belong to the same loyalty program.
This value is available in API version 56.0 and later.

**•** `transferMemberPointsToGroups` —Transfers points from an
individual member or a corporate member to the member’s associated
group. This value is available in API version 53.0 and later.

**•** `transferPoints` —Transfers points from a source loyalty program
member to a target loyalty program member, or to a group that the
member is a part of. This value is available in API version 64.0 and later.

**•** `updateProgressForCumulativePromotionUsage` —Updates
the progress a member has made towards attaining a cumulative type
promotion. This value is available in API version 53.0 and later.

**•** `unmergeLoyaltyProgramMembership` —Unmerges loyalty
program member records that have a Merged status. The action unmerges
memberships in the Merged status from the previously merged
membership. This value is available in API version 56.0 and later.

**•** `runProgramProcess` —Triggers an active loyalty program process.
This value is available in API version 56.0 and later.

**•** `runProgramProcessForTransactionJournal` —Triggers an
active loyalty program process whose process type is TransactionJournal.
This value is available in API version 54.0 and later.

These values are for Decision Table.

**•** `decisionTableAction` —Runs an active decision table definition.
This value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `refreshDecisionTable` —Refreshes the decision table cache. This
value is available in API version 51.0 and later.

These values are for the Batch Management jobs.

**•** `batchJobAction` —Runs the batch management jobs definitions. This
value is available in API version 51.0 and later.

**•** `submitFailedRecordsBatchJob` —Resubmits an existing batch
job with failed records for processing. This value is available in API version
52.0 and later.

This value is for Data Processing Engine.

**•** `dataProcessingEngineAction` —Runs the data processing engine
definitions. This value is available in API version 51.0 and later.

This value is used for Einstein Visit Recommendation.

**•** `saveRecommendationDecision` —Save visit and task
recommendation decisions. This value is available in API version 51.0 and
later.

These values are used in Field Service. If no version is specified, the value is
available in API version 52.0 and later.

**•** `addWorkPlans` —Creates work plan and work step objects from the
work plan library. Available in API version 52.0 and later.

**•** `addWorkSteps` —Creates work step objects from the work plan library.
available in API version 52.0 and later.

**•** `deleteWorkPlans` —Deletes all the work plans and work steps
associated with a work order or work order line item. Available in API version
52.0 and later.

**•** `generateWorkPlans` —Generates work plans based off rules defined
in the work plan library. Available in API version 52.0 and later.

**•** `assignApptForServiceResourceForFieldService` —Assigns
the service appointment selected by the dispatcher to a service resource,
in the gap identified in the service resource’s schedule on a specific date.
Available in API version 63.0 and later.

**•** `assignApptForServiceResourceForFieldService` —Assigns
the service appointment selected by the dispatcher to a service resource,
in the gap identified in the service resource’s schedule on a specific date.

For values used in Intelligent Form Reader, see Flow for Intelligent Form Reader.

For values used in Intelligent Document Reader, see Flow for Intelligent
Document Reader.

This value is used in Public Sector Solutions.

**•** `createBenefitDisbursement` —Creates a benefit disbursement
for an eligible benefit assignment. This value is available in API version 57.0
and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `runRecordAggrBatchProcDef` —Runs a Data Processing Engine
definition to process an asynchronous batch job that creates or updates
record aggregation results. This value is available in API version 59.0 and
later.

These values are used in Unified Catalog. If no version is specified, the value is
available in API version 64.0 and later.

**•** `checkProductEligibility` —Determines whether a user is eligible
for a list of products, which represent service processes, based on
predefined criteria.

**•** `checkSvcPrcActionEligibility` —Determines whether an AI
agent is eligible for a list of products, which represent service processes,
and if the list is linked to a service process.

This value is used in the Get Opportunity Grounding Data flow.

**•** `getContentNote`                        - Gets the content note data for a specified record.
This value is available in API version 64.0 and later.

This value is used in the Process Field Update Suggestions flow.

**•** `getOrExecFieldUpdtSuggestion`                        - Enqueues requests to get
a field update suggestion from a field generation prompt template. This
value is available in API version 64.0 and later.

These values are used in Channel Revenue Management. Available in API
version 64.0 and later.

**•** `adjustPartnerInvShipAndDebit`                        - Adjusts the point of sale
during ship and debit claim processing to a different partner unsold
inventory. Available in API version 64.0 and later.

**•** `adjustPartnerUnsoldInventory`                        - Adjusts the partner unsold
inventory quantities and prices. Available in API version 64.0 and later.

This value is used in Einstein Conversation Insights.

**•** `getConversationTranscript` —Gets the conversation transcript
for the specified voice or video call record. This value is available in API
version 63.0 and later.

These values are reserved for future use.

**•** `thanks`

**•** `metricRefresh`

**•** `exportSurveyResponses`

StrategyActionArg

Defines arguments passed to invocable actions associated with a strategy action.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the parameter to pass to the invocable action.

`value` string Required. A Salesforce formula expression that is evaluated with the result
being used as the parameter value for the Strategy Action.

StrategyNodeUnionBase

Base class for nodes that perform a union of their children. Union nodes combine the outputs of their children to form the input to
themselves. StrategyNodeUnionBase extends StrategyNodeBase and inherits all of its fields. This is an abstract class.

**Field Name** **Field Type** **Description**

`limit` int Maximum number of results to output.

StrategyNodeFilter

Defines a filter element that filters recommendations. It extends StrategyNodeUnionBase and inherits all its fields.

**Field Name** **Field Type** **Description**

`expression` string

StrategyNodeIf

Required. A formula expression that results in a boolean value when executed
on each recommendation in the node’s input. Inputs that result in `true` form
the output, and inputs that result in `false` are excluded.

Selects specific children to execute and combines their results. Executes and returns results of children based on the array of child node
expressions. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`childNodeExpression` IfExpression[] Array of if expressions.

`onlyFirstMatch` boolean If `true`, selects only the results from the matching child. If `false`, selects
and combines results from all matching children. The default value is `false` .

IfExpression

Expression used by StrategyNodeIf.

**Field Name** **Field Type** **Description**

`childName` string Required. Name of child to match.

`expression` string Required. Formula expression returning `true` or `false` .


Metadata Types RecommendationStrategy

StrategyNodeInvocableAction

Defines an element that calls an Apex invocable action to generate or enhance a list of recommendations. It extends
StrategyNodeUnionBase and inherits all its fields.

**Field Name** **Field Type** **Description**

`action` string Required. The name of the invocable action to execute.

`argument` StrategyNodeInvocableActionArg[] List of arguments that are passed to the invocable action.

`isGenerator` boolean Required. If `true`, the UI displays the Generate element. If `false`, the UI
displays the Enhance element. Defaults to `false` .

```
type

```

InvocableActionType Required. The action type. Valid values are:
(enumeration of type

**•** `activateSessionPermSet` —Activates a session-based permission

string)

set for the running user.

**•** `activationSchema`         - Gets the activation schema for the specified
activation. This value is available in API version 64.0 and later.

**•** `addMessageToChat` —Adds a message to an existing Salesforce
Anywhere chat. This value is available in API version 49.0 and later.

**•** `addMessageToQuipChat` —Adds a Quip message to an existing chat
room. This value is available in API version 46.0 and later.

**•** `addMessageToQuipDocument` —Adds a Quip message to an existing
Quip document, spreadsheet, or slide. This value is available in API version
46.0 and later.

**•** `addQuipDocumentToFolder` —Adds an existing Quip document,
spreadsheet, or slide to an existing folder. This value is available in API
version 46.0 and later.

**•** `addUsersToChat` —Adds users to an existing Salesforce Anywhere
chat. This value is available in API version 49.0 and later.

**•** `addUsersToQuipDocument` —Adds users, identified by their email
addresses, to an existing Quip document, spreadsheet, or slide. This value
is available in API version 46.0 and later.

**•** `addUsersToQuipChat` —Adds users, identified by their email
addresses, to an existing Quip chat room. This value is available in API
version 46.0 and later.

**•** `answerQuestionsWithSalesforceDocumentation` —Searches
Salesforce documentation to provide answer to questions, as well as links
to relevant articles.

**•** `attachQuipDocumentToRecord` —Attaches a Quip document,
spreadsheet, or slide to a Salesforce record. This value is available in API
version 46.0 and later.

**•** `apex` —Invokes an Apex method that has the @invocableMethod
annotation.

**•** `archiveKnowledgeArticles` —Archives a list of published
Knowledge articles. This value is available in API version 45.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `assignKnowledgeArticles` —Mass assigns knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `cdpRunIdentityResolution` —Runs a Data 360 identity resolution
process. This value is available in API version 57.0 and later.

**•** `chat` —Creates a Salesforce Anywhere chat. This value is available in API
version 49.0 and later.

**•** `chatterPost` —Posts to Chatter.

**•** `choosePricebook` —Selects a price book.

**•** `contactRequestAction` —Creates a contact request record. This
value is available in API version 45.0 and later.

**•** `component` —Invokes the Lightning component that implements the
`lightning:availableForFlowActions` interface and that is
referenced by `actionName` . This value is available in API version 43.0
and later.

**•** `contentWorkspaceEnableFolders` —Enables folders in a library.

**•** `convertAttributesToJson` —Converts the given attributes into
a JSON string format. This value is available in API version 64.0 and later.

**•** `copyQuipDocument` —Creates a copy of an existing Quip document,
spreadsheet, or slide, and gives it a new title. This value is available in API
version 46.0 and later.

**•** `createDraftFromOnlineKnowledgeArticle` —Creates a draft
from a published knowledge article. This value is available in API version
45.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
from a purchase order. Available to B2B Commerce. This value is available
in API version 49.0 and later.

**•** `createQuipChat` —Creates a Quip chat room. This value is available
in API version 46.0 and later.

**•** `createQuipDocument` —Creates a Quip document, spreadsheet, or
slide. This value is available in API version 46.0 and later.

**•** `createQuipFolder` —Creates a Quip folder. This value is available in
API version 46.0 and later.

**•** `customNotificationAction` —Sends a custom notification. This
value is available in API version 46.0 and later.

**•** `deactivateSessionPermSet` —Deactivates a session-based
permission set for the running user.

**•** `deleteKnowledgeArticle` —Deletes a draft version (translation
or master-language) or an entire archived knowledge article. This value is
available in API version 46.0 and later.

**•** `dynamicSendSurveyInvitation` —Sends customized notifications
to users about important events or updates to the records that they’re
working on. This value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `editQuipDocument` —Modifies the contents of an existing Quip
document, spreadsheet, or slide. This value is available in API version 46.0
and later.

**•** `emailAlert` —Sends an email by referencing a workflow email alert

**•** `emailSimple` —Sends an email by using flow resources

**•** `exploreConversation` —Retrieves insights from a conversation.
This value is available in API version 61.0 and later.

**•** `externalService` —Invokes an External Service operation that makes
an HTTP request to an external system made available by an External Service
schema registered through Setup. This value is available in API version 46.0
and later.

**•** `findMatchingIndividuals` —Finds contact, lead, or employee
records that match a search term.

**•** `findPastCollaborators`

—Leverages insights from Einstein Activity Capture to identify individuals
with past collaborative ties, aiding in securing introductions to relevant
parties in ongoing or future deals. This value is available in API version 63.0
and later.

**•** `flow` —Invokes an autolaunched flow. This action type isn’t available for
flows with a processType of Flow or AutolaunchedFlow. To invoke an
autolaunched flow from one of those types, use FlowSubflow. This value
is available in API version 32.0 and later.

**•** `generateAiAgentResponse` —Generates a response from the AI
agent based on input and instructions to support intelligent, conversational
experiences. This value is available in API version 63.0 and later.

**•** `generateVerificationCode` —Sends a verification code to the
customer's email to verify their identity. This value is available in API version
63.0 and later.

**•** `getAgentConvTscp` —Retrieves the transcript of conversations
between the agent and the customer. This value is available in API version
50.0 and later.

**•** `getArticleSmartLinkUrl` —Gets the Smart Link URL of the
Salesforce Knowledge article. Smart links go to the right article and version,
even when a new version is published or the URL name changes. This value
is available in API version 54.0 and later.

**•** `getPoliciesByObject` —Gets Policy Center policies that contain a
given object and returns a list of matching policy names.

**•** `getPoliciesByPolicyType` —Gets Policy Center policies of the
type specified in the user input, such as Data Backup or Data Archive.

**•** `getPolicyDetails` —Gets details about a policy in Policy Center,
such as the policy type and the objects the policy targets.

**•** `getProductPricing` —Gets the pricing information of a product,
including relevant historical sale price data from previous won deals


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

involving the same product. This value is available in API version 63.0 and
later.

**•** `internalTestAction` —Reserved for internal use.

**•** `internalTestConnectApiAction` —Reserved for internal use.

**•** `limitRepetitions` —Limit the number of times the same
recommendation or offer appears on the same record or for the same user
during a time period in a recommendation strategy flow. This value is
available in API version 55.0 and later.

**•** `massUpdateAccountForecast` —Bulk updates forecasts
asynchronously. This value is available in API version 48.0 and later.

**•** `massUpdateSalesAgreement` —Bulk updates sales agreements
asynchronously. This value is available in API version 48.0 and later.

**•** `quickAction` —Invokes a QuickAction.

**•** `parseConvoAnalysis` —Parses conversation data to analyze
sentiment or extract actionable insights. This value is available in API version
51.0 and later.

**•** `publishActionableOrchSrcEvent` —Publishes events triggered
by an external system. This value is available in API version 62.0 and later.

**•** `publishKnowledgeArticles` —Mass publishes knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `restoreKnowledgeArticleVersion` —Restores an archived
version of a knowledge article. This value is available in API version 45.0
and later.

**•** `reviewBuyingCommittee` —Identifies and reviews key contacts
associated with a deal, their influence on that deal, and other deals that
they’ve impacted. This value is available in API version 63.0 and later.

**•** `sendAlert` —Sends Salesforce Anywhere alerts to users. This value is
available in API version 49.0 and later.

**•** `sendNotification` —Sends an available notification type. This value
is available in API version 54.0 and later.

**•** `sendSurveyInvitation` —Sends email survey invitations to leads,
contacts, and users in your org based on an action, such as when a customer
support case closes. This value is available in API version 47.0 and later.

**•** `performSurveySentimentAnalysis` —Perform survey sentiment
analysis to create or update the AI Sentiment Result records. This value is
available in API version 55.0 and later.

**•** `skillsBasedRouting` [—Creates a PendingServiceRouting record](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
used for Omni-Channel skills-based routing. This value is available in version
44.0 and later.

**•** `slackArchiveChannel` —Archives a Slack channel in a Slack
workspace. This value is available in API version 54.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `slackCheckUsersAreConnectedToSlack` —Indicates whether
a collection of Salesforce users is connected to a given Slack app. This value
is available in API version 54.0 and later.

**•** `slackCreateChannel` —Creates a Slack channel in a Slack workspace.
This value is available in API version 54.0 and later.

**•** `slackGetConversationInfo` —Retrieves the name of a Slack
channel or group direct message and finds out whether it’s archived. This
value is available in API version 54.0 and later.

**•** `slackInviteUsersToChannel` —Adds users who are connected
to a given Slack app to a Slack channel or group direct message. This value
is available in API version 54.0 and later.

**•** `slackPinMessage` —Pin or unpin a message in a Slack channel or
group direct message. This value is available in API version 54.0 and later.

**•** `slackPostMessage` —Send a message to a Slack channel or group
direct message. This value is available in API version 54.0 and later.

**•** `slackSendMessageToLaunchFlow` —Send a message to a Slack
channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow. This value is
available in API version 55.0 and later.

**•** `slackUpdateMessage` —Edits a message that was previously sent
to a Slack channel or group direct message. This value is available in API
version 54.0 and later.

**•** `submitKnowledgeArticleForTranslation` —Submits a
published or draft knowledge article for translation. This value is available
in API version 46.0 and later.

**•** `submit` —Submits a record for approval.

**•** `triggerJourney`                        - Send an individual to a specified journey. This
value is available in API version 64.0 and later.

**•** `verifyCustomerCode` —Verifies the code entered by the customer
to complete identity verification. This value is available in API version 63.0
and later.

These values are used in Omnichannel Inventory. If no version is specified, the
value is available in API version 51.0 and later.

**•** `ociCreateReservation` —Creates one or more inventory
reservations at a location or location group.

**•** `ociFulfillReservation` —Fulfills one or more inventory
reservations at a location.

**•** `ociGetAvailability` —Gets inventory availability data for one or
more products at one or more inventory locations or location groups.

**•** `ociReleaseReservation` —Releases one or more inventory
reservations.

**•** `ociTransferReservation` —Transfers one or more inventory
reservations between locations or location groups.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in the B2B Commerce Checkout Flow. If no version is
specified, the value is available in API version 47.0 and later.

**•** `updateCheckoutSessionStateAction` —Updates the checkout
session next state for checkout flows. This value is available in API version
49.0 and later.

**•** `priceCart` —Requests prices for all items in a cart during B2B Commerce
checkout. This value is available in API version 47.0 and later.

**•** `checkoutSessionAction` —Initiates or retrieves an existing
Checkout Session for Checkout Flows. Available to B2B Commerce. This
value is available in API version 49.0 and later.

**•** `cancelCartAsyncOperation` —Cancels a WebCart’s async
operation. Available to B2B Commerce. This value is available in API version
49.0 and later.

**•** `calcCartPromotionsAction` —Requests a full cart promotion
calculation of all applicable line items in the Web Cart during B2B
Commerce checkout. This value is available in API version 52.0 and later.

**•** `checkCartInventoryAction` —Requests an inventory for all items
in a Web Cart during B2B Commerce checkout. This value is available in
API version 47.0 and later.

**•** `calcCartShipmentAction` —Calculates the shipping cost for all
items in a Web Cart during B2B Commerce checkout. This value is available
in API version 47.0 and later.

**•** `cartToOrderAction` —Creates a Salesforce Standard Order in draft
mode. This value is available in API version 47.0 and later.

**•** `activateOrderAction` —Activates a draft order, which creates an
order summary. This value is available in API version 47.0 and later.

[For values used in Business Rules Engine, see Flow for Business Rules Engine.](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/bre_flow_metadata_api.htm)

These values are used in Context Service. If no version is specified, the value is
available in API version 64.0 and later.

**•** `deleteContextCache` —Deletes the context instance from the
context cache using specified context ID.

**•** `queryContextTags` —Queries context instance tags associated with
a context definition.

**•** `updateContextAttributes` —Updates attributes on the context
instance using context tags.

These values are used in the Commerce Checkout Flow. If no version is specified,
the value is available in API version 55.0 and later.

**•** `addCartItem` —Adds an item to a cart during Commerce checkout.

**•** `createCart` —Creates a cart during Commerce checkout.

**•** `deleteCart` —Deletes a cart during Commerce checkout.

These values are used in Salesforce CMS Workflows and Approvals. If no version
is specified, the value is available in API version 58.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `managedContentPublishVariant` —Publishes a content variant
associated with a flow. This value is available in API version 59.0 and later.

**•** `managedContentRoleStepInteractive` —Assigns a content
variant review to a CMS role.

**•** `managedContentUnpublishVariant` —Unpublishes a published
content variant associated with a flow. This value is available in API version
59.0 and later.

**•** `managedContentVariantSetLockStatus` —Sets the locked
status of a content variant.

**•** `managedContentVariantSetReadyStatus` —Sets the ready
for publication status of a content variant.

These values are used in Employee Service. If no version is specified, the value
is available in API version 64.0 and later.

**•** `createServiceRequestCase` —Creates a case or incident for the
requested service.

**•** `getDirectDepositDetails` —Gets the direct deposit details for
the specified record ID.

**•** `getLeaveBalance` —Gets the leave balance of a specific employee.

These values are used in Insurance. If no version is specified, the value is available
in API version 63.0 and later.

**•** `cancelInsurancePolicy` —Cancel an insurance policy by using a
set of user inputs that represent policy details.

**•** `endorseInsurancePolicy` —Endorse an insurance policy by using
a set of user inputs that represent policy details.

**•** `getInsurancePolicy` —Get the details of an insurance policy.

**•** `issueInsurancePolicy`                        - Issue an insurance policy by using a set
of user inputs that represent policy details.

**•** `renewInsurancePolicy` —Renew an insurance policy by using a
set of user inputs that represent policy details.

These values are used in Insurance Brokerage. If no version is specified, the
value is available in API version 63.0 and later.

**•** `computeProducerSplits` —Compute the producer splits for the
producers associated with an Insurance Policy, for a Commission Statement
Line Item.

**•** `createProducerCommissions` —Create records for the
commissions that producers receive for the insurance policy associated
with the specified commission statement line item, and update the
commission statement line item record status.

**•** `findInsurancePolicy` —Get the insurance policy associated with
a commission statement line item that matches the specified criteria, and
update the status of the commission statement line item record.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in Order Management. If no version is specified, the value
is available in API version 48.0 and later.

**•** `addOrderItemSummarySubmit` —Adds order item summaries to
an order summary. This value is available in API version 54.0 and later.

**•** `adjustOrderItemSummariesPreview` —Previews the expected
results of applying a price adjustment to order item summaries from an
order summary without actually applying it. This value is available in API
version 49.0 and later.

**•** `adjustOrderItemSummariesSubmit` —Applies a price adjustment
to order item summaries from an order summary. This value is available in
API version 49.0 and later.

**•** `authorizePayment` —Authorizes a card payment. This value is
available in API version 55.0 and later.

**•** `calcPriceProtectPayoutAmt` —Calculates the payout after a
price protection adjustment or execution is made. This value is available
in API version 63.0 and later.

**•** `cancelFulfillmentOrderItem` —Removes items from a
fulfillment order.

**•** `cancelOrderItemSummariesPreview` —Previews the expected
results of canceling order item summaries from an order summary without
actually canceling them.

**•** `cancelOrderItemSummariesSubmit` —Cancels order item
summaries from an order summary.

**•** `confirmHeldFulfillmentOrderCapacity` —Confirms held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `createCreditMemoOrderSummary` —Creates a credit memo for
an order summary.

**•** `createFieldGnrnPromptTmplResp` —Creates a field generation
prompt template response. This value is available in API version 62.0 and
later.

**•** `createFulfillmentOrder` —Creates one or more fulfillment orders
and fulfillment order products for an order delivery group summary, which
defines a recipient and delivery method.

**•** `createFulfillmentOrders` —Creates fulfillment orders and
fulfillment order products for multiple order delivery group summaries,
each of which defines a recipient and delivery method. This value is available
in API version 51.0 and later.

**•** `createInvoiceFromChangeOrders` —Creates an invoice for one
or more change orders. This value is available in API version 56.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
for a fulfillment order.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `createOrderPaymentSummary` —Creates an order payment
summary for an authorization or payments belonging to an order summary.

**•** `createOrderSummary` —Creates an order summary for an order.

**•** `createReturnOrder` —Creates a return order and return order items
for an order.

**•** `ensureFundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure funds through a payment provider for an
invoice belonging to an order summary.

**•** `ensureRefundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure refunds through a payment provider for an
invoice belonging to an order summary.

**•** `getFulfillmentOrderCapacityValues` —Gets fulfillment
order capacity information. This value is available in API version 55.0 and
later.

**•** `holdFulfillmentOrderCapacity` —Holds fulfillment order
capacity. This value is available in API version 55.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplits` —Evaluates
ordered product quantities against available inventory to determine the
smallest combination of locations that can fulfill the order. This value is
available in API version 51.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplitsUsingOCI` —Evaluates
ordered product quantities against available inventory at specified location
groups and locations to determine the smallest combination of locations
that can fulfill the order. This value is available in API version 54.0 and later.

**•** `orderRoutingRankByAverageDistance` —Calculates the
average distance from sets of inventory locations to an order recipient, and
returns the sets sorted by that average distance. This value is available in
API version 51.0 and later.

**•** `releaseHeldFulfillmentOrderCapacity` —Releases held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `returnOrderItemSummariesPreview` —Previews the expected
results of returning order item summaries from an order summary without
actually returning them.

**•** `returnOrderItemSummariesSubmit` —Returns order item
summaries from an order summary.

**•** `returnReturnOrderItems` —Processes return order line items.

These values are used in Financial Services Cloud.

**•** `createFinancialRecords` —Creates person accounts, contacts,
financial accounts, properties, assets, and liabilities from a residential loan
application. This value is available in API version 49.0 and later.

For values used in Fundraising for Nonprofit Cloud, see Flow for Fundraising.

[For values used in Health Cloud, see Flow for Health Cloud.](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/health_cloud_flow_metadata_api.htm)


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

[For values used in Manufacturing Cloud, see Flow for Manufacturing Cloud.](https://developer.salesforce.com/docs/atlas.en-us.262.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_flow_metadata_api.htm)

This value is used in Omnistudio.

**•** `executeIntegrationProcedure` —Executes an Integration
Procedure with Agentforce configured. This value is available in API version
64.0 and later.

These values are used in Rebate Management.

**•** `addRebateMemberList` —Adds a list of members to a rebate program.
This value is available in API version 51.0 and later.

**•** `calculateProjectedRebateAmount` —Calculates the projected
rebate amount for rebate types associated with a specified transaction ID.
This value is available in API version 54.0 and later.

**•** `calculateRebateAmountAndUpsertPayout` —Calculates the
rebate amount and upserts the rebate payout for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getBenefitAndCalculateRebateAmount`                        - Gets benefit details,
and optionally calculates the rebate amount for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getEligibleProgramRebateTypes` —Retrieves the eligible
program rebate types for a mapped object. This value is available in API
version 52.0 and later.

**•** `generateRebatePayoutPeriods` —Generates payout periods for
a rebate program based on the frequency specified in the program. This
value is available in API version 51.0 and later.

**•** `processRebatesBatchCalculationJob` —Processes a rebate
batch calculation job from the Data Processing Engine. This value is available
in API version 51.0 and later.

**•** `processProgramRebateTypeProducts` —Insert or delete records
in the Program Rebate Type Product object. This value is available in API
version 53.0 and later.

**•** `rebatesProcessCSV` —Processes an uploaded CSV file using Bulk
API 2.0 and converts the file’s data into records in the target object. This
value is available in API version 51.0 and later.

**•** `upsertCustomRebatePayout` —Upserts the custom calculated
rebate payout for the specified aggregate record. This value is available in
API version 51.0 and later.

These values are used in B2B Referral Management. If no version is specified,
the value is available in API version 64.0 and later.

**•** `enrollAdvocateB2bReferralProm` —Enroll an existing or new
customer as an advocate for a referral promotion.

**•** `processB2bReferralEvent` —Create referral event records when
an advocate refers a friend, or when referred friends sign up or make a
purchase.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in Referral Marketing.

**•** `processReferralEvent` —Create referral event records when an
advocate refers a friend, or when referred friends sign up or make a
purchase. This value is available in API version 60.0 and later.

These values are used in Loyalty Management.

**•** `adjustPoints` —Adjusts loyalty points for a specified program member
or journal transaction. This value is available in API version 51.0 and later.

**•** `assignTierBenefits`                        - Assigns Member Benefits to a member tier
for benefits that are associated with a Benefit Action. This value is available
in API version 51.0 and later.

**•** `cancelAccrual` —Cancels a specific set of accrual transactions.

**•** `creditPoints` —Credits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `cancelRedemption` —Reverts a specific set of redemption transactions.
This value is available in API version 51.0 and later.

**•** `changeTier` —Changes the tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `changeTierWhenNoErrors` —Changes tier for a specified loyalty
program member only when all the input parameters meet the criteria.
This value is available in API version 51.0 and later.

**•** `debitPoints` —Debits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `executeMemberBenefit` —Processes the benefit action associated
with the benefit, which is assigned to a loyalty program member. This value
is available in API version 51.0 and later.

**•** `generateMemberReferralCode` —Generates a unique 8-character
referral code for a loyalty program member. This value is available in API
version 57.0 and later.

**•** `getMemberActiveSegments` —Retrieve active Data 360 market
segments that a loyalty program member is a part of.

**•** `getTier` —Gets the current tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `getPointsBalance` —Gets the loyalty points balance for a specified
program member. This value is available in API version 51.0 and later.

**•** `getLoyaltyPromotion` —Gets active loyalty promotions based on
a transaction journal. This value is available in API version 53.0 and later.

**•** `getLoyaltyPromotionBasedOnSalesforceCDP` —Gets
promotions for a member based on the market segment the member
belongs to. This value is available in API version 53.0 and later.

**•** `issueVoucher` —Issues a voucher for a member or contract. This value
is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `mergeLoyaltyProgramMembership` —Merges two active loyalty
program member records that both belong to the same loyalty program.
This value is available in API version 56.0 and later.

**•** `transferMemberPointsToGroups` —Transfers points from an
individual member or a corporate member to the member’s associated
group. This value is available in API version 53.0 and later.

**•** `transferPoints` —Transfers points from a source loyalty program
member to a target loyalty program member, or to a group that the
member is a part of. This value is available in API version 64.0 and later.

**•** `updateProgressForCumulativePromotionUsage` —Updates
the progress a member has made towards attaining a cumulative type
promotion. This value is available in API version 53.0 and later.

**•** `unmergeLoyaltyProgramMembership` —Unmerges loyalty
program member records that have a Merged status. The action unmerges
memberships in the Merged status from the previously merged
membership. This value is available in API version 56.0 and later.

**•** `runProgramProcess` —Triggers an active loyalty program process.
This value is available in API version 56.0 and later.

**•** `runProgramProcessForTransactionJournal` —Triggers an
active loyalty program process whose process type is TransactionJournal.
This value is available in API version 54.0 and later.

These values are for Decision Table.

**•** `decisionTableAction` —Runs an active decision table definition.
This value is available in API version 51.0 and later.

**•** `refreshDecisionTable` —Refreshes the decision table cache. This
value is available in API version 51.0 and later.

These values are for the Batch Management jobs.

**•** `batchJobAction` —Runs the batch management jobs definitions. This
value is available in API version 51.0 and later.

**•** `submitFailedRecordsBatchJob` —Resubmits an existing batch
job with failed records for processing. This value is available in API version
52.0 and later.

This value is for Data Processing Engine.

**•** `dataProcessingEngineAction` —Runs the data processing engine
definitions. This value is available in API version 51.0 and later.

This value is used for Einstein Visit Recommendation.

**•** `saveRecommendationDecision` —Save visit and task
recommendation decisions. This value is available in API version 51.0 and
later.

These values are used in Field Service. If no version is specified, the value is
available in API version 52.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `addWorkPlans` —Creates work plan and work step objects from the
work plan library.

**•** `addWorkSteps` —Creates work step objects from the work plan library.

**•** `deleteWorkPlans` —Deletes all the work plans and work steps
associated with a work order or work order line item.

**•** `generateWorkPlans` —Generates work plans based off rules defined
in the work plan library.

For values used in Intelligent Form Reader, see Flow for Intelligent Form Reader.

For values used in Intelligent Document Reader, see Flow for Intelligent
Document Reader.

This value is used in Public Sector Solutions.

**•** `createBenefitDisbursement` —Creates a benefit disbursement
for an eligible benefit assignment. This value is available in API version 57.0
and later.

**•** `runRecordAggrBatchProcDef` —Runs a Data Processing Engine
definition to process an asynchronous batch job that creates or updates
record aggregation results. This value is available in API version 59.0 and
later.

These values are used in Unified Catalog. If no version is specified, the value is
available in API version 64.0 and later.

**•** `checkProductEligibility` —Determines whether a user is eligible
for a list of products, which represent service processes, based on
predefined criteria.

**•** `checkSvcPrcActionEligibility` —Determines whether an AI
agent is eligible for a list of products, which represent service processes,
and if the list is linked to a service process.

This value is used in the Get Opportunity Grounding Data flow.

**•** `getOpportunityContentNote`                        - Gets the content note data for
a specified opportunity record. This value is available in API version 64.0
and later.

This value is used in the Process Field Update Suggestions flow.

**•** `getOrExecFieldUpdtSuggestion`                        - Enqueues requests to get
a field update suggestion from a field generation prompt template. Also
enqueues requests to update a field based on the generated suggestion.
This value is available in API version 64.0 and later.

This value is used in Einstein Conversation Insights.

**•** `getConversationTranscript` —Gets the conversation transcript
for the specified voice or video call record. This value is available in API
version 63.0 and later.

These values are used in Channel Revenue Management. Available in API
version 64.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `adjustPartnerInvShipAndDebit`                        - Adjusts the point of sales
record during ship and debit claim processing to a different partner unsold
inventory. Available in API version 64.0 and later.

**•** `adjustPartnerUnsoldInventory`                        - Adjusts the partner unsold
inventory quantities and prices. Available in API version 64.0 and later.

These values are reserved for future use.

**•** `thanks`

**•** `metricRefresh`

**•** `exportSurveyResponses`

StrategyNodeInvocableActionArg

Defines arguments passed to an Apex invocable action that generates or enhances a list of recommendations.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the parameter to pass to the invocable action. The
name must match a parameter that's defined in the invocable action.

`value` string Required. A Salesforce formula expression that is evaluated with the result used
as the parameter value for the action.

StrategyNodeRecommendationLimit

Filters out recommendations that have already been accepted or rejected. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

```
filterMode

```

StrategyReactionType
Available reactions to filter out. The valid values are:
(enumeration of type

**•** `Accepted`

string)

**•** `Rejected`

`lookbackDuration` int Number of days to search back.

`maxRecommendationCount` int Maximum number of times recommendation has been accepted or rejected.

StrategyNodeRecommendationLoad

Retrieves Recommendation objects. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`condition` RecommendationLoadCondition[] Array of conditions specifying which recommendations to load.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

`conditionLogic` string Logic to combine conditions, either AND or OR. All conditions are combined
(not mixed). For example: `Cond1 AND Cond2 AND Cond3` .

`object` string Required. Specifies the API name of the sObject from which recommendations
are loaded. For example, the field references `Account` or

`MyCustomObject__c` and not a specific record of that object. Available
in API version 48.0 and later.

`sortField` StrategyNodeSortField The field to sort on. Available in API version 48.0 and later.

RecommendationLoadCondition

Represents a condition used as part of the query constructed by StrategyNodeRecommendationLoad.

**Field Name** **Field Type** **Description**

`field` string Required. Any field from Recommendation BPO (SOAP) object.

Required.

Valid values are:

**•** `EQUALS`

**•** `GREATER_THAN`

**•** `GREATER_THAN_OR_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_OR_EQUAL_TO`

**•** `NOT_EQUALS`

**•** `LIKE`

**•** `STARTS_WITH`

**•** `ENDS_WITH` =

**•** `CONTAINS`

```
operator

```

RecommendationCond **i** tonOperator
(enumeration of type
string)

`value` RecommendationConditionValue Required. Constant value to use in query.

RecommendationConditionValue

Represents a value used as part of a RecommendationCondition.

**Field Name** **Field Type** **Description**

Required.

Valid values are:

**•** `TEXT`

**•** `NUMBER`


```
type

```

RecommendationCondtonValueType **i**
(enumeration of type
string)

Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `BOOLEAN`

**•** `DATE`

**•** `DATE_TIME`

**•** `TIME`

`value` string Required. The constant value.

StrategyNodeSortField

Defines the field to sort on for StrategyNodeSort and StrategyNodeRecommendationLoad.

**Field Name** **Field Type** **Description**

`name` string Required. Name of the field to sort.

`nullsFirst` boolean If `true`, null values are sorted to the beginning of the list. Defaults to `false` .

```
order

```

StrategyNodeSort

SortOrder
Order in which the list is sorted. Defaults to `Asc` . Valid values are:
(enumeration of type

**•** `Asc` (ascending)

string)

**•** `Desc` (descending)

Sorts the recommendations. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`field` StrategyNodeSortField Required. Field to sort on.

StrategyNodeUnion

StrategyNodeUnion combines the output of all its child nodes. StrategyNodeUnion is a concrete implementation of StrategtNodeUnionBase
and inherits all its fields.

StrategyNodeMap

Set recommendation fields with values. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`mapExpression` MapExpression on List of MaxExpressions.
page 1843[]


Metadata Types RecommendationStrategy

StrategyNodeExclusive

Returns results from the first child node that has results and no other. Extends StrategyNodeUnionBase and inherits all its fields.

MapExpression

Sets the value for a recommendation field used by the strategy.

**Field Name** **Field Type** **Description**

`expression` string Required. A formula expression that results in a valid value supported by the
data type specified in the `type` field.

`name` string Required. Recommendation field name that the expression sets the value for.

`type` string

Required. The data type of the value resulting from the value in the
`expression` field.

Valid values are:

**•** `BOOLEAN`

**•** `CURRENCY`

**•** `DATE`

**•** `DOUBLE`

**•** `DATE_TIME`

**•** `INTEGER`

**•** `LONG`

**•** `PERCENT`

**•** `TEXT`

**•** `TIME`

Declarative Metadata Sample Definition

The following is an example of a RecommendationStrategy component that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<RecommendationStrategy xmlns="http://soap.sforce.com/2006/04/metadata">

   <contextRecordType>Asset</contextRecordType>

   <description>Hills Brothers Coffee strategy to handle machine down

incidents</description>

   <if>

     <childNode>IfNoEscaladeOrBetterSupport</childNode>

     <childNode>IfModel</childNode>

     <description>If Machine Down</description>

     <label>RootNode</label>

     <name>RootNode</name>

     <childNodeExpression>

        <childName>IfModel</childName>

        <expression>ISPICKVAL($Record.Status, &quot;OutOfOrder&quot;)</expression>

     </childNodeExpression>

```


Metadata Types RecommendationStrategy

```
        <childNodeExpression>

           <childName>IfNoEscaladeOrBetterSupport</childName>

           <expression>ISPICKVAL($Record.Status, &quot;OutOfOrder&quot;)</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <if>

        <childNode>LoadEscalade</childNode>

        <description>If Customer does not have escalade support plan</description>

        <label>IfNoEscaladeOrBetterSupport</label>

        <name>IfNoEscaladeOrBetterSupport</name>

        <childNodeExpression>

           <childName>LoadEscalade</childName>

           <expression>NOT(ISPICKVAL($Record.Account.SLA__c, &quot;Gold&quot;) ||

   ISPICKVAL($Record.Account.SLA__c, &quot;Platinum&quot;))</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <if>

        <childNode>LoadMiniDiagnostic</childNode>

        <childNode>LoadMaxiDiagnostic</childNode>

        <description>If Machine Model switch node</description>

        <label>IfModel</label>

        <name>IfModel</name>

        <childNodeExpression>

           <childName>LoadMiniDiagnostic</childName>

         <expression>$Record.Product2.Name == &quot;Mini Coffee Roaster&quot;</expression>

        </childNodeExpression>

        <childNodeExpression>

           <childName>LoadMaxiDiagnostic</childName>

         <expression>$Record.Product2.Name == &quot;Maxi Coffee Roaster&quot;</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <label>HillsBrothersCoffee</label>

      <recommendationLoad>

        <description>Load upgrade to escalade support plan</description>

        <label>LoadEscalade</label>

        <name>LoadEscalade</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Upgrade your Maintenance Package</value>

           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <recommendationLoad>

        <description>Load Mini Coffee Roaster Diagnostic Troubleshooting

   proposition</description>

```


Metadata Types RecommendationStrategy

```
        <label>LoadMiniDiagnostic</label>

        <name>LoadMiniDiagnostic</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Mini Coffee Roaster Diagnostic Troubleshooting</value>

           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <recommendationLoad>

        <description>Load Maxi Coffee Roaster Diagnostic Troubleshooting

   proposition</description>

        <label>LoadMaxiDiagnostic</label>

        <name>LoadMaxiDiagnostic</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Maxi Coffee Roaster Diagnostic Troubleshooting</value>

           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <union>

        <childNode>RootNode</childNode>

        <label>Output</label>

        <name>Output</name>

      </union>

      <invocableAction>

        <action>MyInvocableApexClass</action>

        <isGenerator>true</isGenerator>

        <type>apex</type>

        <argument>

           <name>MyNameParam</name>

           <value>$User.FirstName</value>

        </argument>

        <argument>

           <name>MyIdParam</name>

           <value>$Record.Id</value>

        </argument>

      </invocableAction>

      <map>

        <expression>

           <name>Name</name>

           <expression>'Hello' & $User.FirstName</expression>

           <type>TEXT</type>

        </expression>

        <expression>

           <name>MyDynamicField</name>

           <expression>Id == $Record.Id</expression>

```


### Metadata Types RecordActionDeployment

```
           <type>BOOLEAN</type>

        </expression>

      </map>

   </RecommendationStrategy>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RecordActionDeployment

Represents configuration settings for the Actions & Recommendations, Action Launcher, and Bulk Action Panel components. For example,
you can have a deployment that specifies which types of actions to display, default actions for channels, and the actions that users can
add at runtime. If the component shows Next Best Action recommendations, the deployment configures which strategies to use and
how recommendations appear. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### RecordActionDeployment values are stored in the developer_name .deployment file in the recordActionDeployments

directory.

Note: We don’t recommend programmatically changing the API name of a RecordActionDeployment.

Version

### RecordActionDeployment is available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

### channelConfigurations RecordActionDeploymentChannel Specifies configuration settings for different channels in an Actions

& Recommendations deployment.

`componentName` ComponentName (enumeration Specifies the name of the component used in the deployment:
of type string)

**•** `ActionsAndRecommendations` —0

**•** `ActionLauncher` —1

**•** `BulkActionPanel` —2. This value is available in API
version 60.0 and later

For example, a value of 1 indicates that 1 is stored in the database
if Action Launcher is used to create a deployment. Available in API
version 56.0 and later.


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

`deploymentContexts` RecordActionDeploymentContext Specifies the object context for quick actions and Next Best Action
strategies. Available in API version 46.0 and later.

`hasComponents` boolean

Indicates whether the record actions deployment includes
components ( `true` ) or not ( `false` ). Available in API version 61.0
and later.

`hasGuidedActions` boolean Specifies that the component shows standard actions; for example,
flows and quick actions. Available in API version 46.0 and later.

hasOmniscripts boolean

Indicates whether the record actions deployment includes
OmniScripts ( `true` ) or not ( `false` ). Available in API version 56.0
and later. The default value is `false` .

`hasRecommendations` boolean Specifies that the component shows recommendations from a
Next Best Action strategy. Available in API version 46.0 and later.

`masterLabel` string Required. Specifies the name of the deployment.

`recommendation` RecordActionRecommendation Specifies settings for how Next Best Action recommendations
appear in the component. Available in API version 46.0 and later.

`selectableItems` RecordActionDeploymentSelectableItems Specifies the actions that users can add at runtime.

`shouldLaunchActionOnReject` boolean Required. If `true`, launch the flow when the recommendation is
rejected by the agent. Available in API version 48.0 and later.

RecordActionDefaultItem

Represents actions and attributes specified as channel defaults in a deployment.

**Field Name** **Field Type** **Description**

`action` string Required. Specifies the API name of an action. For example, the API name of a
flow, such as `Verify_Information` .

`isMandatory` boolean Specifies whether the action is marked as mandatory. The default value is
`false` .

`isUiRemoveHidden` boolean Specifies whether the remove option is hidden in the UI. The default value is
false. If `true`, the UI hides the ability to remove the action from the list.

```
pinned

```

PinnedAction Required. Indicates whether the action is pinned to the `Top` or `Bottom`, or
(enumeration of type unpinned ( `None` ). The default value is `None` .
string)

`position` int Required. Indicates the order of the action among all actions associated with
this record.

```
type

```

RecordActionType Required. The type of action that’s associated with the record. Valid values are:
(enumeration of type

**•** `Flow`

string)

**•** `Flow`

**•** `QuickAction` (Available in API version 46.0 and later.)


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

**•** `OmniScript` (Available in API version 56.0 and later.)

**•** `LWC` (Available in API version 62.0 and later.)

**•** `SvcCatalogItemDef` (Available in API version 62.0 and later.)

**•** `WebLink` (Available in API version 62.0 and later.)

RecordActionDeploymentChannel

Specifies channel-specific defaults to show in the Actions & Recommendations component. The component displays the channel defaults
when the list is otherwise empty.

**Field Name** **Field Type** **Description**

`channel` ChannelSource Required. Specifies the channel. Valid values are `Phone`, `Chat`, or
(enumeration of type string) `Default` .

`channelItems` RecordActionDefaultItem

`isAutopopEnabled` boolean

RecordActionDeploymentContext

Specifies default actions for a channel and attributes for each action,
such as whether the action is pinned to the list top or bottom or whether
an action is considered mandatory.

Specifies whether the first action in the list is launched when the record
page opens. If `true`, the first action is launched. The default value is
`false` .

Specifies an object that provides context for quick actions and Next Best Action strategies. When the component appears on this type
of page, it includes object-specific quick actions and uses an object-specific strategy to filter recommendations. Available in API version
46.0 and later.

Note: We support a maximum of 10 objects that provide context within a deployment.

**Field Name** **Field Type** **Description**

`entityName` string Required. Specifies the API name of an object to use as context.

`recommendationStrategy` string Specifies the API name of a Next Best Action strategy that overrides the default
strategy on this page. A strategy is a metadata type RecommendationStrategy.

RecordActionRecommendation

Specifies settings to display Next Best Action recommendations in the component. Available in API version 46.0 and later.

**Field Name** **Field Type** **Description**

`defaultStrategy` string Specifies the API name of the default Next Best Action strategy, which is a
metadata type, RecommendationStrategy.


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

`hasDescription` boolean Required. If `true`, display the description for the recommendation.

`hasImage` boolean Required. If `true`, display the image for the recommendation.

`hasRejectAction` boolean Required. If `true`, display the label that the user clicks to reject the
recommendation.

`hasTitle` boolean Required. If `true`, display the title for the recommendation.

`maxDisplayRecommendations` int Required. Specifies the maximum number of recommendations to display.
Valid values are 1–4.

RecordActionSelectableItem

Represents the set of actions available for users to add to the component at runtime.

**Field Name** **Field Type** **Description**

`action` string Required. Specifies the API name of an action. For example, the API name of a
flow, such as `Verify_Information` .

```
type

```

RecordActionType Required. The type of action that’s associated with the record. Valid values are:
(enumeration of type

**•** `Flow`

string)

**•** `Flow`

**•** `QuickAction` (Available in API version 46.0 and later.)

`isFrequentAction` boolean

frequentActionSequenceNbr integer

**•** `OmniScript` (Available in API version 56.0 and later.)

**•** `LWC` (Available in API version 62.0 and later.)

**•** `SvcCatalogItemDef` (Available in API version 62.0 and later.)

**•** `WebLink` (Available in API version 62.0 and later.)

Indicates whether an action is frequently accessed by users ( `true` ) or not
( `false` ). Available in version 57.0 and later.

This field applies only to Action Launcher.

The sequence number that's assigned to a frequently used action that's shown
on Action Launcher. Available in version 57.0 and later.

This field applies only to Action Launcher.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


Metadata Types RecordActionDeployment

Declarative Metadata Sample Definition

The following is a sample of a `recordActionDeployment` file.

```
   <RecordActionDeployment xmlns="http://soap.sforce.com/2006/04/metadata">

      <channelConfigurations>

        <channel>Phone</channel>

        <channelItems>

           <action>Sample_Flow</action>

           <isMandatory>false</isMandatory>

           <isUiRemoveHidden>false</isUiRemoveHidden>

           <position>1</position>

           <pinned>Top</pinned>

           <type>Flow</type>

        </channelItems>

        <channelItems>

           <action>Another_Sample_Flow</action>

           <isMandatory>false</isMandatory>

           <isUiRemoveHidden>true</isUiRemoveHidden>

           <position>2</position>

           <pinned>Top</pinned>

           <type>Flow</type>

        </channelItems>

        <isAutopopEnabled>true</isAutopopEnabled>

      </channelConfigurations>

      <masterLabel>Sample Deployment</masterLabel>

      <selectableItems>

        <action>Sample_Flow</action>

        <type>Flow</type>

        <isFrequentAction>true</isFrequentAction>

        <frequentActionSequenceNbr>1</frequentActionSequenceNbr>

      </selectableItems>

      <selectableItems>

        <action>Sample_Flow_2</action>

        <type>Flow</type>

        <isFrequentAction>false</isFrequentAction>

      </selectableItems>

      <hasGuidedActions>true</hasGuidedActions>

      <hasRecommendations>true</hasRecommendations>

      <recommendation>

        <defaultStrategy>Sample_Global_Strategy</defaultStrategy>

        <maxDisplayRecommendations>4</maxDisplayRecommendations>

        <hasImage>true</hasImage>

        <hasDescription>true</hasDescription>

        <hasRejectAction>true</hasRejectAction>

        <hasTitle>true</hasTitle>

      </recommendation>

      <deploymentContexts>

        <entityName>Case</entityName>

        <recommendationStrategy>Sample_Case_Strategy</recommendationStrategy>

      </deploymentContexts>

      <deploymentContexts>

        <entityName>Account</entityName>

        <recommendationStrategy>Sample_Acc_Strategy</recommendationStrategy>

```


### Metadata Types RecordAggregationDefinition

```
      </deploymentContexts>

   </RecordActionDeployment>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>SecondTest</fullName>

      <types>

        <members>Sample_Flow</members>

        <members>Another_Sample_Flow</members>

        <members>Sample_Flow_2</members>

        <name>Flow</name>

      </types>

      <types>

        <members>SampleDeployment</members>

        <name>RecordActionDeployment</name>

      </types>

      <version>45.0</version>

   </Package>

```

SEE ALSO:

RecommendationStrategy

### RecordAggregationDefinition

Represents a data aggregation from one object to another object to which it is connected by other objects in the data model.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RecordAggregationDefinition components have the suffix .RecordAggregationDefinition and are stored in the RecordAggregationDefinitions folder.

Version

### RecordAggregationDefinition components are available in API version 59.0 and later.

Special Access Rules

To access the RecordAggregationDefinition metadata type, you must have the Record Aggregation permission set license and the Record
Aggregation Access permission.


Metadata Types RecordAggregationDefinition

Fields

**Field Name** **Description**

```
aggregateFromObject

aggregateToObject

aggregationType

batchProcessingDefinition

description

displayName

onDemandProcDefinition

```

**Field Type**
string

**Description**

Required.

API name of the object from which data is aggregated.

**Field Type**
string

**Description**

Required.

API name of the object to which data is aggregated.

**Field Type**
RecordAggregationDefinitionAggregationType (enumeration of type string)

**Description**

Required.

Type of the data aggregation.

Valid value is:

**•** `Record`

**Field Type**
string

**Description**
Data Processing Engine definition that aggregates data from one record to another.

**Field Type**
string

**Description**
Description for this record aggregation definition.

**Field Type**
string

**Description**

Required.

Name of the record aggregation definition that's displayed in the record page.

**Field Type**
string


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

**Description**
Data Processing Engine definition that aggregates data from one record to another
on demand. Available in API version 63.0 and later.

```
recordAggregationObject

status

```

**Field Type**

RecordAggregationObject[]

**Description**
List of record aggregation objects in the record aggregation join sequence.

**Field Type**
RecordAggregationDefinitionStatus (enumeration of type string)

**Description**

Required.

Status of this record aggregation definition.

Values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

RecordAggregationObject

Represents an object in the record aggregation join sequence.

**Field Name** **Description**

```
associatedObject

developerName

filterLogic

```

**Field Type**
string

**Description**
Required.

API name of the object associated with this record aggregation object.

**Field Type**
string

**Description**
Developer name of the record aggregation object. May contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

**Description**
Logical sequence in which the record aggregation object filters associated with this
record aggregation object are applied to the associated object's records. If you define
two or more record aggregation object filters, but don’t specify the sequence in which
to apply the filters, the filters are applied by using a logical AND expression.

Available in API version 60.0 and later.

```
masterLabel

recordAggregationJoinCondition

recordAggregationObjectFilter

```

**Field Type**
string

**Description**

Required.

A user-friendly name for RecordAggregationDefinition, which is defined when the
RecordAggregationDefinition is created.

**Field Type**

RecordAggregationJoinCondition[]

**Description**
List of join conditions that apply to this record aggregation object.

**Field Type**

RecordAggregationObjectFilter[]

**Description**
List of filters that are applied to the records of this record aggregation object.

Available in API version 60.0 and later.

RecordAggregationJoinCondition

Represents a condition in a join between two record aggregation objects.

**Field Name** **Description**

```
joinField

navigationSequenceNumber

```

**Field Type**
string

**Description**
Required.

API name of the field on the record aggregation object's associated object that is used
in the join condition.

**Field Type**
int


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

**Description**
Required.

Sequence number corresponding to this join in the join sequence from the object to
which the data is aggregated to the object that contains the data being aggregated.

```
relatedJoinField

relatedRecordAggregationObject

type

```

**Field Type**
string

**Description**
Required.

API name of the field on the related record aggregation object's associated object that
is used in the join condition.

**Field Type**
string

**Description**
Required.

Second record aggregation object in the join condition.

**Field Type**
RecordAggregationJoinConditionType (enumeration of type string)

**Description**
Required.

Type of this record aggregation join in the join path from the object to which the data
is aggregated to the object that contains the data being aggregated.

Valid values are:

**•** `AggregateFrom`

**•** `AggregateTo`

**•** `Intermediate`

RecordAggregationObjectFilter

Represents a filter that is applied to the records of an object in the record aggregation join sequence. Available in API version 60.0 and
later.

**Field Name** **Description**

```
associatedObjectField

```

**Field Type**
string

**Description**

Required.


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

API name of the associated object's field whose value is used to filter the object's
records. The associated object is specified in the record aggregation object.

```
operator

sequenceNumber

value

```

**Field Type**
RecordAggregationObjectFilterOperator (enumeration of type string)

**Description**

Required.

Operator used in the filter expression.

Values are:

**•** `Contains`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEquals`

**•** `In`

**•** `LessThan`

**•** `LessThanOrEquals`

**•** `NotEquals`

**•** `NotIn`

**Field Type**
int

**Description**

Required.

Sequence number of this record aggregation object filter.

**Field Type**
string

**Description**

Required.

Reference value with which the designated field's values are compared when the filter
is applied on the associated object's records.

Declarative Metadata Sample Definition

The following is an example of a RecordAggregationDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RecordAggregationDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aggregateToObject>PartyRelationshipGroup</aggregateToObject>

   <aggregateFromObject>PartyIncome</aggregateFromObject>

```


Metadata Types RecordAggregationDefinition

```
      <status>Active</status>

      <aggregationType>Record</aggregationType>

      <description>Aggregate head of household's income to household</description>

      <displayName>Party Income to Party Relationship Group</displayName>

      <recordAggregationObject>

        <associatedObject>PartyRelationshipGroup</associatedObject>

        <masterLabel>Party Relationship Group Object</masterLabel>

        <developerName>PartyRelationshipGroupObject</developerName>

        <recordAggregationJoinCondition>

           <joinField>Account</joinField>

           <navigationSequenceNumber>1</navigationSequenceNumber>

           <relatedJoinField>Account</relatedJoinField>

   <relatedRecordAggregationObject>AccountContactrelationObject</relatedRecordAggregationObject>

           <type>Intermediate</type>

        </recordAggregationJoinCondition>

        <recordAggregationObjectFilter>

         <associatedObjectField>Type</associatedObjectField>

         <operator>Equals</operator>

         <value>Household</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

      <recordAggregationObject>

        <associatedObject>AccountContactRelation</associatedObject>

        <masterLabel>Account Contact Relation Object</masterLabel>

        <developerName>AccountContactRelationObject</developerName>

        <recordAggregationJoinCondition>

           <joinField>Contact</joinField>

           <navigationSequenceNumber>2</navigationSequenceNumber>

           <relatedJoinField>Party</relatedJoinField>

   <relatedRecordAggregationObject>PartyIncomeObject</relatedRecordAggregationObject>

           <type>Intermediate</type>

        </recordAggregationJoinCondition>

        <recordAggregationObjectFilter>

         <associatedObjectField>IsPrimaryMember</associatedObjectField>

         <operator>Equals</operator>

         <value>true</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

      <recordAggregationObject>

        <associatedObject>PartyIncome</associatedObject>

        <masterLabel>Party Income Object</masterLabel>

        <developerName>PartyIncomeObject</developerName>

        <filterLogic>1 AND 2</filterLogic>

        <recordAggregationObjectFilter>

         <associatedObjectField>IncomeFrequency</associatedObjectField>

         <operator>Equals</operator>

         <value>Monthly</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

```


### Metadata Types RecordAlertCategory

```
        <recordAggregationObjectFilter>

         <associatedObjectField>IncomeStatus</associatedObjectField>

         <operator>Equals</operator>

         <value>Active</value>

         <sequenceNumber>2</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

   </RecordAggregationDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RecordAggregationDefinition</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

### RecordAlertCategory

Represents a category to group and present record alerts.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RecordAlertCategory components have the suffix recordAlertCategory and are stored in the recordAlertCategories

folder.

Version

### RecordAlertCategory components are available in API version 54.0 and later.


Metadata Types RecordAlertCategory

Fields

**Field Name** **Description**

```
description

masterLabel

severity

```

**Field Type**
string

**Description**
The description of the record alert category.

**Field Type**
string

**Description**

Required.

The user-interface name of the record alert category.

**Field Type**
string

**Description**
Indicates the degree of impact that an alert in this category can have.

Possible Education Cloud values are:

**•** `High`

**•** `Low`

**•** `Medium`

Possible Financial Service Cloud values are:

**•** `Error`

**•** `Info`

**•** `Minor`

**•** `Warning`

Declarative Metadata Sample Definition

The following is an example of a RecordAlertCategory component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RecordAlertCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Tracks Financial Account Fraud Alerts</description>

   <masterLabel>Fraud</masterLabel>

   <severity>Error</severity>

</RecordAlertCategory>

```


### Metadata Types RegisteredExternalService

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Fraud</members>

        <name>RecordAlertCategory</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RegisteredExternalService

Represents a registered external service, which provides an extension or integration.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RegisteredExternalService components have the suffix .registeredExternalService and are stored in the

`registeredExternalServices` folder.

Version

### RegisteredExternalService components are available in API version 49.0 and later.

Special Access Rules

This metadata type is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field Name** **Description**

```
configUrl

```

**Field Type**
string

**Description**
Link to the configuration page for the integration.


Metadata Types RegisteredExternalService

**Field Name** **Description**

```
description

documentationUrl

extensionPointName

```

**Field Type**
string

**Description**
Description of the external service provider.

This field is available in API version 59.0 and later.

**Field Type**
string

**Description**
Link to documentation for the registered external service.

**Field Type**
ExtensionPointName (enumeration of type string)

**Description**
This field is available in API version 55.0 and later. Name of an extension point.

Possible values are:

**•** `Commerce_Domain_BuyerGroup_EvaluationService` —Available
in API version 65.0 and later.

**•** `Commerce_Domain_Cart_Calculate`

**•** `Commerce_Domain_Checkout_CreateOrder`

**•** `Commerce_Domain_Inventory_CartCalculator`

**•** `Commerce_Domain_Inventory_Service`

**•** `Commerce_Domain_OrderManagement_Product`

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

**•** `Commerce_Endpoint_Cart_Item` —Available in API version 62.0 and
later.

**•** `Commerce_Endpoint_Cart_ItemCollection` —Available in API
version 62.0 and later.

**•** `Commerce_Endpoint_Catalog_Product`

**•** `Commerce_Endpoint_Catalog_Products`


Metadata Types RegisteredExternalService

**Field Name** **Description**

**•** `Commerce_Endpoint_Search_ProductSearch`

**•** `Commerce_Endpoint_Gift_Wraps` —Available in API version 65.0 and
later.

**•** `Commerce_Endpoint_Search_Products`

**•** `Commerce_Endpoint_Search_ProductsByCategory`

```
externalServiceProvider

externalServiceProviderType

iconUri

```

**Field Type**
string

**Description**
Required. The ID of an Apex class functioning as a provider. The Apex class can either
implement one of the following interfaces:

**•** sfdc_checkout.CartInventoryValidation

**•** sfdc_checkout.CartPriceCalculations

**•** sfdc_checkout.CartShippingCharges

**•** sfdc_checkout.CartTaxCalculations

[or the Apex class can extend one of the base classes for an extension. See Available](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)
[Extensions.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)

**Field Type**
RegistryProviderType (enumeration of type string)

**Description**
Required. The type of external service provider. For an extension, you set the type to
`Extension`, and you specify an `extensionPointName` . For example, for a
Pricing Cart Calculator extension, you specify
`Commerce_Domain_Pricing_CartCalculator` as the
`extensionPointName` . For an integration, you set the type to one of the other
possible values, such as `Price`, and you omit `extensionPointName` .

Possible values are:

**•** `Extension` (this value is available in API version 55.0 and later)

**•** `Inventory`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Field Type**
string

**Description**
URI of icon for the extension provider.

This field is available in API version 59.0 and later.


Metadata Types RegisteredExternalService

**Field Name** **Description**

```
isApplication

isProtected

masterLabel

```

**Field Type**
boolean

**Description**
Indicates if the extension provider is contained within a managed package.

The default value is `false` .

This field is available in API version 59.0 and later.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
string

**Description**

Required. The primary label for the RegisteredExternalService.

Declarative Metadata Sample Definition

The following is an example of a RegisteredExternalService component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RegisteredExternalService xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalServiceProvider>TaxSample</externalServiceProvider>

   <externalServiceProviderType>Tax</externalServiceProviderType>

   <documentationUrl>http://sample.com/doc</documentationUrl>

   <configUrl>http://sample.com/config</configUrl>

   <masterLabel>TaxService</masterLabel>

   <isProtected>false</isProtected>

</RegisteredExternalService>

```

The following is an example `package.xml` that references the previous definition.

```
<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>TaxSample</members>

     <name>ApexClass</name>

   </types>

   <types>

     <members>TaxService</members>

     <name>RegisteredExternalService</name>

   </types>

   <version>60.0</version>

</Package>

```


### Metadata Types ReferencedDashboard ReferencedDashboard

Represents the ReferencedDashboard object in CRM Analytics. A referenced dashboard stores information about an externally referenced
dashboard.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ReferencedDashboard components have the suffix .refdash and are stored in the wave folder.

Version

### ReferencedDashboard components are available in API version 57.0 and later.

Special Access Rules

To view referenced dashboards, you need the Enables Tableau Dashboards in CRM Analytics permission.

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the Analytics app.

`description` string The dashboard description that appears in the user interface.

`embedUrl` string Required. The URL to the referenced dashboard.

`masterLabel` string Required. The dashboard name that appears in the user interface.

`templateAssetSourceName` string Links the dashboard to the template used to create it. Null for assets not
created from a template.

`visibility` string The visibility of the dashboard. Valid values are: `ALL` and `LIMITED` .

Declarative Metadata Sample Definition

The following is an example of a WaveDashboard component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ReferencedDashboard xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <application>my_app</application>

```


### Metadata Types RelatedRecordAssocCriteria

```
      <masterLabel>ReferencedDashboard1</masterLabel>

      <description>My Tableau Dashboard</description>

      <embedUrl>https://public.tableau.com/views/Superstore_24/Overview</embedUrl>

      <visibility>ALL</visibility>

   </ReferencedDashboard>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RelatedRecordAssocCriteria

Represents criteria for automatically linking records like accounts, leads, opportunities, and cases with the branches that work with them.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RelatedRecordAssocCriteria components have the suffix .relatedRecordAssocCriteria and are stored in the

`relatedRecordAssocCriteria` folder.

Version

### RelatedRecordAssocCriteria components are available in API version 52.0 and later.

Special Access Rules

To use this object, you must have the Financial Services Cloud Extension permission set.

Fields

**Field Name** **Description**

```
associationHandlerApexClass

```

**Field Type**
string

**Description**
The name of a custom Apex class that handles the creation of association records for
specific association criteria. This class must:

**•** Apply to an object that the Record Association Builder doesn't directly support


Metadata Types RelatedRecordAssocCriteria

**Field Name** **Description**

**•** Implement the `fscwmgen.BranchManagement`
`AssociationHandler` interface

**•** Return a list of Branch Unit Related Records

**•** Populate at least the minimum required fields in each Branch Unit Related Record:

**–** `BranchUnitId` : Represents the current branch unit of the user or contact

**–** `BusinessUnitMemberId` : The Banker ID of the user or contact

**–** `RelatedRecordId` : The ID of the custom object to be related

This field is a relationship field.

```
associationType

description

eventType

isProtected

masterLabel

```

**Field Type**
AssociationType (enumeration of type string)

**Description**

Required.

The association type. Values are:

**•** `BranchManagement`

**Field Type**
string

**Description**
A description of the association criteria.

**Field Type**
AssociationEventType (enumeration of type string)

**Description**

Required.

The type of reference object event that triggers creation of the association. Values are:

**•** `Create`

**•** `Update`

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required.


Metadata Types RelatedRecordAssocCriteria

**Field Name** **Description**

The master label of the association criteria. This internal label doesn’t get translated.

```
preCondition

referenceObject

selectedOwnerField

status

```

**Field Type**
string

**Description**

Required.

A formula that, when true, causes a new association to be created.

**Field Type**
string

**Description**

Required.

The reference object for the association criteria.

**Field Type**
string

**Description**
A field to use instead of the default Owner ID.

**Field Type**
AssociationStatusType (enumeration of type string)

**Description**

Required.

The status of the association criteria. Values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Declarative Metadata Sample Definition

The following is an example of a RelatedRecordAssocCriteria component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RelatedRecordAssocCriteria xmlns="http://soap.sforce.com/2006/04/metadata">

  <associationType>BranchManagement</associationType>

  <eventType>Create</eventType>

  <masterLabel>RevenueThreeMillion</masterLabel>

  <preCondition>[Account].AnnualRevenue > 3000000</preCondition>

  <referenceObject>Account</referenceObject>

  <status>Active</status>

</RelatedRecordAssocCriteria>

```


### Metadata Types RelationshipGraphDefinition

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RelatedRecordAssocCriteria</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RelationshipGraphDefinition

Represents a definition of a graph that you can configure in your organization to traverse object hierarchies and record details, giving
you a glimpse of how your business works.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RelationshipGraphDefinition components have the suffix .relationshipGraphDefinition and are stored in the

`relationshipGraphDefinitions` folder.

Version

### RelationshipGraphDefinition components are available in API version 55.0 and later.

Special Access Rules

The Financial Services Cloud permission set license is required to access this object.

Fields

**Field Name** **Description**

```
isActive

```

**Field Type**
boolean


Metadata Types RelationshipGraphDefinition

**Field Name** **Description**

**Description**

Required.

Indicates whether the relationship graph is available for use ( `true` ) or not
( `false` ). The default value is `true` .

Note: This field is read-only in API version 55.0.

```
isTemplate

masterLabel

relationshipGraphDefVersions

```

**Field Type**
boolean

**Description**

Required.

Indicates whether you can configure this relationship graph as a template ( `true`
or not `false` ). The default value is `false` . In the UI, this field is _Set as Template_ .

**Field Type**
string

**Description**

Required.

A user-friendly name for RelationshipGraphDefinition, which is defined when the
RelationshipGraphDefinition is created. In the UI, this field is _Label_ .

**Field Type**

RelationshipGraphDefVersion[]

**Description**
Represents a list of graph versions associated with the relationship graph definition.

RelationshipGraphDefVersion

The list of graph versions associated with the relationship graph definition.

**Field Name** **Description**

```
graphDefinition

graphType

```

**Field Type**
string

**Description**

Required.

Specifies a set of properties required to create a relationship graph, such as parent node,
child relationships, filter and sort fields, and graph UI elements.

**Field Type**
string


Metadata Types RelationshipGraphDefinition

**Field Name** **Description**

**Description**

Required.

Specifies the type of graph. In API version 55.0, only `HorizontalHierarchy` graph
type is supported.

Declarative Metadata Sample Definition

The following is an example of a RelationshipGraphDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RelationshipGraphDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

      <isActive>false</isActive>

      <isTemplate>true</isTemplate>

      <masterLabel>Account Graph</masterLabel>

      <relationshipGraphDefVersions>

         <graphDefinition>{

     "graph" : {

      "rootNode" : {

        "object" : {

         "entity" : "Account"

        },

        "configurationType" : "Primary",

        "sortFields" : [ {

         "field" : {

          "field" : "LastModifiedDate",

          "whichEntity" : "TARGET"

         },

         "order" : "DESC"

        } ],

        "nodeUiConfig" : {

         "fieldsToDisplay" : [ ],

         "showFieldLabels" : true,

         "actions" : { }

        },

        "childRelationships" : [ {

         "OneToMany" : {

          "targetObjectNode" : {

           "object" : {

            "entity" : "Contact"

           },

           "configurationType" :"Custom",

           "sortFields" : [ {

            "field" : {

              "field" : "LastModifiedDate",

              "whichEntity" : "TARGET"

            },

            "order" : "DESC"

           } ],

           "nodeUiConfig" : {

```


Metadata Types RelationshipGraphDefinition

```
            "fieldsToDisplay" : [ {

              "field" : "Name",

              "whichEntity" : "TARGET"

            }, {

              "field" : "Phone",

              "whichEntity" :"TARGET"

            } ],

            "showFieldLabels" : true,

            "actions" : {

              "containerActions" : [ {

               "action" : "New"

              } ],

              "recordActions" : [ {

               "action" : "Edit"

              }, {

               "action" : "Delete"

              } ]

            }

           },

           "childRelationships" : [ ]

          },

          "relationshipUiConfig" : { },

          "filter" : {

           "filterCriteria" : [ {

            "field" : {

              "field" : "Name",

              "whichEntity" : "TARGET"

            },

            "operator" : "eq",

            "value" : "Salesforce"

           } ],

           "booleanFilter" : "1"

          },

          "targetObjectField" : {

           "field" : "AccountId",

           "whichEntity" : "TARGET"

          }

         }

        } ]

      },

      "globalUiConfig" : {

        "borderColor" : "Green2",

        "borderThickness" : "2px";,

        "colorShading" : "Black",

        "fieldLayout" : "Vertically Stacked",

        "recordContainerExpansion" : true,

        "recordExpansion" : true

      }

     }

    }</graphDefinition>

         <graphType>HorizontalHierarchy</graphType>

      </relationshipGraphDefVersions>

   </RelationshipGraphDefinition>

```


### Metadata Types RemoteSiteSetting

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Package1</fullName>

     <types>

        <members>*</members>

        <name>RelationshipGraphDefinition</name>

     </types>

     <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RemoteSiteSetting

Represents a remote site setting. Before any Visualforce page, Apex callout, or JavaScript code using XmlHttpRequest in an s-control or
custom button can call an external site, that site must be registered in the Remote Site Settings page, or the call fails.

### RemoteSiteSetting on page 1872 extends the Metadata metadata type and inherits its fullName field.

Declarative Metadata File Suffix and Directory Location

### RemoteSiteSetting on page 1872 components are stored in the remoteSiteSettings directory of the corresponding package

directory. The file name matches the unique name of the remote site setting, and the extension is `.remoteSite` .

Version

### RemoteSiteSetting on page 1872 components are available in API version 19.0 and later.

Fields

**Field** **Field Type** **Description**

`description` string The description explaining what this remote site setting is used
for.

`disableProtocolSecurity` boolean Required. Indicates whether code within Salesforce can access
the remote site regardless of whether the user's connection is

over HTTP or HTTPS ( `true` ) or not ( `false` ). When `true`, code
within Salesforce can pass data from an HTTPS session to an
HTTP session, and vice versa.

Only set to `true` if you understand the security implications.


### Metadata Types Report

**Field** **Field Type** **Description**

`fullName` string The name can only contain characters, letters, and the
underscore (_) character. The name must start with a letter, and

can’t end with an underscore or contain two consecutive
underscore characters.

Inherited from the Metadata component, this field isn’t defined
in the WSDL for this component. It must be specified when
creating, updating, or deleting. See create() to see an example
of this field specified for a call.

`isActive` boolean Required. Indicates if the remote site setting is active ( `true` ) or
not ( `false` ).

`url` string Required. The URL for the remote site.

Declarative Metadata Sample Definition

A sample XML definition of a remote site setting is shown in this code block.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RemoteSiteSetting xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Used for Apex callout to mapping web service</description>

      <disableProtocolSecurity>false</disableProtocolSecurity>

      <isActive>true</isActive>

      <url>https://www.maptestsite.net/mapping1</url>

   </RemoteSiteSetting>

### Report

```

Represents a custom report. This metadata type only supports custom reports; standard reports aren’t supported.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

### Reports are stored in the reports directory of the package directory. The file name consists of the report title with the extension

`.report` .

Retrieving Reports

You can’t use the wildcard (*) symbol with reports in `package.xml` .

To retrieve the list of explicit report names to populate `package.xml` with, first call `listMetadata(ListMetadataQuery[])`
### with a ListMetadataQuery entry with the type field set to ReportFolder and the folder field to * (wildcard). This

call returns an array of FileProperties objects with the names of report folders in the `fullName` field.


Metadata Types Report

Now call `listMetadata` with `ListMetadataQuery` entries where the `type` field is Report and the `folder` fields are the
full name values from the first `listMetadata` call. These calls return `FileProperties` objects where the `fullName` field is
the combination of the folder name and report name. Use these values in the `package.xml` to designate the members for the Report
metadata type.

ReportFolder isn’t returned as a type in `describeMetadata()` . Report is returned from `describeMetadata()` with an
associated attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component name
with the word Folder, such as ReportFolder.

The following example shows folders in `package.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

                  </Package>

```

To retrieve or deploy `ReportFolder` s, use the `Report` metadata type in your `package.xml` . When you reference a nested
folder by itself (without its contents), the API can misinterpret the path as a report component.

For example, the API interprets `<members>TopLevel/SubLevel</members>` as a request for a report named `SubLevel` .

To correctly reference the nested folder, append a trailing slash (/) to its full name. This syntax explicitly identifies the member as a folder.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>TopLevel/SubLevel/</members>

        <members>TopLevel/SubLevel/MyReport</members>

        <name>Report</name>

      </types>

      <version>58.0</version>

   </Package>

```

Omitting the trailing slash (/) for the folder causes the operation to fail with an error: "Entity of type 'Report' named 'TopLevel/SubLevel'
cannot be found".


Metadata Types Report

Version

Report components are available in API version 14.0 and later.

Fields

[The following information assumes that you’re familiar with creating and running reports. For more information on these fields, see Build](https://help.salesforce.com/s/articleView?id=analytics.rd_reports_build.htm&type=5&language=en_US)
[a Report in Salesforce Help.](https://help.salesforce.com/s/articleView?id=analytics.rd_reports_build.htm&type=5&language=en_US)

**Field** **Field Type** **Description**

`aggregateFilters` ReportAggregateFilter[]

List that defines filters on custom summary
formulas for summary, matrix, and joined reports.

Available in API version 64.0 and later.

`aggregates` ReportAggregate[] List that defines custom summary formulas for
summary, matrix, and joined reports.

`block` Report[] Represents each block in a joined report where
every block can be of a different report type.

`blockInfo` ReportBlockInfo Defines attributes for each block in a joined
report.

`buckets` ReportBucketField[] Defines a bucket field to be used in the report.
This field is available in API version 24.0 and later.

`chart` ReportChart Defines a chart for summary and matrix reports.

`colorRanges` ReportColorRange[] List that specifies conditional highlighting for
report summary data. Salesforce Classic only.

`columns` ReportColumn[]

`crossFilters` ReportCrossFilter[]

List that specifies the fields displayed in the
report. Fields appear in the report in the same
order as they appear in the Metadata API file.

Defines a cross filter's object, related object, and
condition (WITH or WITHOUT). This field is
available in API version 66.0 and later.

`currency` `CurrencyIsoCode` (enumeration of type When using multiple currencies, some reports
string) allow you to display converted amounts by

selecting the appropriate column to display. For
example, in opportunity reports, you can include
the Amount (converted) column on the report.
This field is an enumeration of type string that
defines the currency in which to display
converted amounts. Valid values: Must be one
of the valid alphabetic, three-letter currency ISO
codes defined by the ISO 4217 standard, such
as `USD`, `GBPSLE`, or `JPY` .

`dataCategoryFilters` string Specifies a filter according to the data category.


Metadata Types Report

**Field** **Field Type** **Description**

`description` string

Specifies a general description, which is
displayed with the report name. Maximum
characters: 255 characters.

`division` string If your organization uses divisions to segment
data and the Affected by Divisions permission

is enabled, records in the report must match this
division.

This field is available in API version 17.0 and later.

`filter` ReportFilter Limits report results to records with specific data.
For example, you can limit report results to

opportunities for which the amount is greater
than $1,000:

```
                                   <filter>

                                   <criteriaItems>

                                    <column>AMOUNT</column>

                                   <operator>greaterThan</operator>

                                    <value>1000</value>

                                   </criteriaItems>

                                   </filter>

```

`folderName` string

`format` ReportFormat (enumeration of type string)

Name of the folder that houses the report.

This field is available in API version 35.0 and later.

Defines the report format. For example,
`Tabular` for a simple data list without
subtotals.

`formattingRules` ReportFormattingRule[] (enumeration of type List that specifies conditional highlighting for
string) report data. Lightning Experience only.

`groupingsAcross` ReportGrouping[] List that defines the fields by which you want to
group and subtotal data across a matrix report

(row headings). When grouping by a date field,
you can further group the data by a specific time
period such as days, weeks, or months.
Maximum: 2 fields.

`groupingsDown` ReportGrouping[] For Summary and Matrix reports: List that defines
the fields by which you want to group and

subtotal. For summary reports, choosing more
than one sort field allows you to subsort your
data. For matrix reports, specifies summary fields
for column headings. When grouping by a date
field, you can further group the data by a specific
time period such as days, weeks, or months.


Metadata Types Report

**Field** **Field Type** **Description**

Maximum for matrix reports: 2. Maximum for
summary reports: 3

`historicalSelector` ReportHistoricalSelector

`isSmartTotalDisabled` boolean

Defines a date range for which historical trend
reporting data is to be captured. Default is “Any
Historical Date.”

Available in API version 29.0 and later.

`false` displays smart totalling on the report.

Available in API version 29.0 and later.

`name` string Required. The report name. For example,

```
                                 Opportunity Pipeline

```

`numSubscriptions` int

Indicates whether a user has subscribed to this
report Lightning Experience (1) or not (0). Tied
to user context.

This field is available in API version 38.0 and later.

`params` ReportParam[] List that specifies settings specific to each report
type, in particular options that let you filter a

report to obtain useful subsets. For example, the
Activities report type lets you specify whether
you want to see open or closed activities or both
and whether you want to see tasks or events or
both. Valid values depend on the report type.

`reportCustomDetailFormula` CustomDetailFormulas Allows you to apply row-level formulas to
reports.

`reportType` string

`reportTypeApiName` string

Required. Defines the type of data in the report.
For example, `Opportunity` to create a report
of opportunities data.

Defines the API Name for the report type.

This field is available in API version 48.0 and later.

`roleHierarchyFilter` string The role name for a report drill down. Some
reports, such as opportunity and activity reports,

display Hierarchy links that allow you to drill
down to different datasets based on the role
hierarchy.

This field is available in API version 17.0 and later.

`rowLimit` int Defines the maximum number of rows that can
be returned for the report.

`scope` string Defines the scope of data on which you run the
report. For example, whether you want to run


Metadata Types Report

**Field** **Field Type** **Description**

the report against all opportunities,
opportunities you own, or opportunities your
team owns. Valid values depend on the
`reportType` . For example, for Accounts
reports:

**•** `MyAccounts`

**•** `MyTeamsAccounts`

**•** `AllAccounts`

`showCurrentDate` boolean

`showDetails` boolean

Can be set to `true` for historical trending
reports in matrix format.

Available in API version 29.0 and later.

`false` shows a collapsed view of the report
with only the headings, subtotals, and total.
Default: `true`

`showGrandTotal` boolean `true` displays the calculated total for the full
report.

`showSubTotals` boolean `true` displays the calculated subtotals for
sections of the report.

`sortColumn` string

Specifies the field on which to sort data in the
report. Use `sortOrder` to specify the sort
order.

`sortOrder` SortOrder (enumeration of type string) Specifies the sort order. Use `sortColumn` to
specify the field on which to sort.

`territoryHierarchyFilter` string The territory name for a report drill down. If your
organization uses territory management, some

reports display Hierarchy links that allow you to
drill down to different datasets based on the
territory hierarchy.

This field is available in API version 17.0 and later.

`timeFrameFilter` ReportTimeFrameFilter Limits report results to records within a specified
time frame.

`userFilter` string The username for a report drill down. Some
reports, such as opportunity and activity reports,

display Hierarchy links that allow you to drill
down to different datasets based on the user
hierarchy.

This field is available in API version 17.0 and later.


Metadata Types Report

ReportAggregateFilter

ReportAggregateFilter defines custom summary formula filters on summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`aggregate` string Required. The name of the report aggregate to apply the filter
to.

`operator` string Required. The filter operator.

`value` string Required. The filter value.

ReportAggregate

ReportAggregate defines custom summary formulas on summary, matrix, and joined reports. For more information on these fields, see
[Add a Summary Formula Column to a Report in Salesforce Help.](https://help.salesforce.com/s/articleView?id=analytics.building_custom_summary_formulas.htm&type=5&language=en_US)

**Field** **Field Type** **Description**

`acrossGroupingContext` string

Defines the row grouping level at which you want your custom
summary formula to be displayed. This field is available in API
version 15.0.

`calculatedFormula` string Required. The custom summary formula. For example,

```
                           AMOUNT:SUM + OPP_QUANTITY:SUM

```

`datatype` ReportAggregateDatatype Required. Specifies the data type for formatting and display of
(enumeration of type string) the custom summary formula results.

`description` string The custom summary formula description. Maximum: 255
characters.

`developerName` string Required. The internal development name of the custom
summary formula, for example, `FORMULA1` . This name is used

to reference custom summary formulas from other report
components, including conditional highlighting.

`downGroupingContext` string

Defines the column grouping level at which you want your
custom summary formula to be displayed. This field is available
in API version 15.0 and later.

`isActive` boolean Required. `true` displays the formula result in the report.
`false` doesn’t display the result in the report.

`isCrossBlock` boolean Determines whether the custom summary formula is a
cross-block formula, which is available with joined reports.

`true` indicates a cross-block custom summary formula.
`false` indicates a standard custom summary formula.

This field is available in API version 25.0 and later.

`masterLabel` string Required. The custom summary formula label (name).


Metadata Types Report

**Field** **Field Type** **Description**

`reportType` string Required for joined reports. Specifies the `reportType` of the
blocks to which the `aggregate` can be added.

`scale` int The formula result is calculated to the specified number of
decimal places. Valid values `0` through `18` .

ReportBlockInfo

ReportBlockInfo defines blocks in a joined report.

**Field** **Field Type** **Description**

`aggregateReferences` ReportAggregateReference[] Lists the `aggregates` that represent the custom summary
formulas used in a joined report block.

`blockId` string Required. `blockId` is used in cross-block custom summary
formulas and joined report charts to identify the block containing

each summary field. `blockId` is assigned automatically. Valid
values are B1 through B5.

This field is available in API version 25.0 and later.

`joinTable` string

ReportAggregateReference

Required. Refers to the entity used to join blocks in a joined
report. The entity provides a list of fields that are available for
globally grouping across the blocks.

ReportAggregateReference defines the developer name used for custom summary formulas in joined reports.

**Field** **Field Type** **Description**

`aggregate` string

ReportBucketField

ReportBucketField defines a bucket to be used in the report.

Required. The `developerName` of the ReportAggregate,
which specifies the custom summary formula used in a block
of a joined report.

**Field** **Field Type** **Description**

`bucketType` ReportBucketFieldType Required. Specifies the type of bucket. Valid values:
(enumeration of type string)

**•** text

**•** number

**•** picklist


Metadata Types Report

**Field** **Field Type** **Description**

`developerName` string Required. A unique name used as the `<field>` value to
display a bucket field in the column list and other report

components, including sort, filter, list, group, and chart. Must
be of the format `BucketField_` _**`name`**_ . For example,
`BucketField_BusinessSize` .

`masterLabel` string Required. The bucket field label. Maximum 40 characters. Any
line breaks, tabs, or multiple spaces at the beginning or end of

the label are removed. Any of these characters within the label
are reduced to a single space.

`nullTreatment` ReportBucketFieldNullTreatment For numeric bucket fields only. Specifies whether empty values
(enumeration of type string) are treated as zeros ( `z` ) or not ( `n` ).

`otherBucketLabel` string The label of the container for unbucketed values.

`sourceColumnName` string Required. The source field that the bucket is applied to. For
example, `SALES` or `INDUSTRY` .

`values` ReportBucketFieldValue
(enumeration of type string)

ReportBucketFieldValue

Defines one bucket value used in the bucket field.

While this name is plural, it represents a single bucket. In typical
use, a bucket field contains multiple buckets.

ReportBucketFieldValue defines a bucket value used in the bucket field.

**Field** **Field Type** **Description**

`sourceValues` ReportBucketFieldSourceValue The value of a bucket in the bucket field. Valid values:
(enumeration of type string)

**•** `sourceValue` —Used for picklist and text bucket fields.
For picklists, describes the picklist item in the bucket. For
example, the sourceValue of a bucket on `TYPE` could be
`Customer` . For text, the full string for the item in the
bucket. For example, the sourceValue of a bucket on
`ADDRESS_STATE1` could be `NY` .

**•** `from` —Used only on numeric bucket fields. A non-inclusive
lower bound for a numeric bucket range. This value must
be a number.

**•** `to` —Used only on numeric bucket fields. The inclusive
upper bound for a numeric bucket range. This value must
be a number.

In numeric buckets, the first value must only have `to` and last
value must only have `from` . All other values must have both
`to` and `from` .


Metadata Types Report

**Field** **Field Type** **Description**

`value` string Required. The name of a specific bucket value within the bucket
field.

ReportGrouping

ReportGrouping defines how to group, subtotal, and sort data for summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`aggregateType` ReportAggrType (enumeration The type of aggregate value to sort by. Valid values are:
of type string)

**•** `Sum`

**•** `Average`

**•** `Maximum`

**•** `Minimum`

**•** `RowCount`

**•** `Unique`

**•** `Median`

**•** `Noop`

`dateGranularity` UserDateGranularity When grouping by a date field, the time period by which to
(enumeration of type string) group.

`field` string Required. The field by which you want to summarize data. For
example, `CAMPAIGN_SOURCE`

`sortByName` string The API name of the column, aggregate, or custom summary
field used to order the grouping.

`sortOrder` SortOrder Required. Whether to sort data in ascending or descending
alphabetical and numerical order.

`sortType` ReportSortType (enumeration Indicates if the grouping is sorted by a column, aggregate, or
of type string) custom summary field. Valid values are:

**•** `Column`

**•** `Aggregate`

**•** `CustomSummaryFormula`

ReportHistoricalSelector

ReportHistoricalSelector defines a date range for historical data.

**Field** **Field Type** **Description**

`snapshot` string Represents the date value to apply a historical filter, either
relative (in the format `N_DAYS_AGO:2` ) or absolute (in the


Metadata Types Report

**Field** **Field Type** **Description**

format `yyyy-MM-dd` ). If unspecified, it’s assumed that the
filter is applied to all the columns the user sees.

Available in API version 29.0 and later.

CustomDetailFormulas

CustomDetailFormulas defines row-level formulas for reports.

**Field** **Field Type** **Description**

`calculatedFormula` string Required. The custom formula. For example, `AMOUNT:SUM`

```
                              + OPP_QUANTITY:SUM

```

`datatype` ReportCustomDetailFormulaDatatype Required. Specifies the data type for formatting and display of
(enumeration of type string) the formula results.

`description` string The formula description. Maximum: 255 characters.

`developerName` string Required. The internal development name of the formula, for
example, `FORMULA1` . This name is used to reference custom

formulas from other report components, including conditional
highlighting.

`label` string Required. The name that identifies this formula.

`scale` int The formula result is calculated to the specified number of
decimal places. Valid values `0` through `18` .

ReportCustomDetailFormulaDatatype

An enumeration of type string that specifies the data type for formatting and display of row-level formula results. Valid values:

**Enumeration Value**

```
   Double

   DateOnly

   DateTime

   Text

```

SortOrder

An enumeration of type string that defines the order in which data is sorted in the report fields. Valid values:


Metadata Types Report

**Field** **Description**

`Asc` Sorts data in ascending alphabetical and numerical order.

`Desc` Sorts data in descending alphabetical and numerical order.

UserDateGranularity

An enumeration of type string that defines the time period by which to group data. Valid values:

**Enumeration Value** **Description**

`None` No grouping by date

`Day` By day

`Week` By week

`Month` By month

`Quarter` By quarter

`Year` By year

`FiscalQuarter` [By fiscal quarter. You can set the fiscal year for your organization. See Set the Fiscal Year in](https://help.salesforce.com/s/articleView?id=xcloud.setting_the_fiscal_year.htm&type=5&language=en_US)
Salesforce Help.

`FiscalYear` By fiscal year

`MonthInYear` By calendar month in year

`DayInMonth` By calendar day in month

`FiscalPeriod` When custom fiscal years are enabled: By fiscal period

`FiscalWeek` When custom fiscal years are enabled: By fiscal week

ReportSummaryType

An enumeration of type string that defines how report fields are summarized. Valid values:

**Enumeration Value** **Description**

`Sum` Total

`Average` Average

`Maximum` Largest value

`Minimum` Smallest value

`Unique` Unique values

`Median` Median value

`Noop` The summary is a no-op.


Metadata Types Report

**Enumeration Value** **Description**

`None` The field isn’t summarized.

ReportColorRange

ReportColorRange defines conditional highlighting for report summary data.

**Field** **Field Type** **Description**

`aggregate` ReportSummaryType Required. Defines how the field specified in `columnName` is
(enumeration of type string) summarized. For example, `Sum` .

`columnName` string Required. Specifies the field whose value ranges are represented
by background colors.

`highBreakpoint` double Required. Specifies the number that separates the mid color
from the high color.

`highColor` string

Required. Specifies the color (in HTML format) to represent data
that falls into the high number range. This color spans from the
`highBreakpoint` value.

`lowBreakpoint` double Required. Specifies the number that separates the low color
from the mid color.

`lowColor` string

Required. Specifies a color (in HTML format) to represent data
that falls into the low value range, below the
`lowBreakpoint` value.

`midColor` string Required. Specifies a color (in HTML format) to represent data
that falls into the mid value range.

ReportColumn

ReportColumn defines how fields (columns) are displayed in the report.

**Field** **Field Type** **Description**

`aggregateTypes` ReportSummaryType[] List that defines if and how each report field is summarized.
(enumeration of type string)

`field` string Required. The field name. For example, `AGE` or

```
                           OPPORTUNITY_NAME

```

`isExtendedColumn` boolean

Indicates whether the column is extended ( `true` ) or not
( `false` ).

Available in API version 65.0 and later.


Metadata Types Report

**Field** **Field Type** **Description**

`reverseColors` boolean

`showChanges` boolean

ReportFilter

ReportFilter limits the report results by filtering data on specified fields.

In historical trend reports, displays greater Date values as green
and greater Amount values as red, reversing the default colors.

Available in API version 29.0 and later.

In historical trend reports, adds a column displaying the
difference between current and historical Date and Amount
values.

Available in API version 29.0 and later.

**Field** **Field Type** **Description**

`booleanFilter` string Specifies filter logic conditions.

`criteriaItems` ReportFilterItem

`language` Language (enumeration of type
string)

ReportFilterItem

The criteria by which you want to filter report data, either by
comparing historical values or by applying a date range.

```
<criteriaItems>

  criteriaItems ReportFilterItem

<column>Opportunity.Opportunity__hd$Amount__hst</column>

  <columnToColumn>false</columnToColumn>

  <operator>equals</operator>

  <snapshot>N_DAYS_AGO:90</snapshot>

  <value>100</value>

</criteriaItems>

```

The language used when a report filters against a picklist value
using the operators `contains` or `startsWith` . For a list
of valid language values, see Language.

ReportFilterItem limits the report results by filtering data on specified fields.

**Field** **Field Type** **Description**

`column` string Required. The field in which to filter data. For example, `AMOUNT`

`columnToColumn` boolean

Indicates whether the filter is a column-to-column (field-to-field)
filter.


Metadata Types Report

**Field** **Field Type** **Description**

Available in API version 29.0 and later for historical trending
reports. Available in API version 48.0 and later for general reports.

`isUnlocked` boolean Optional. Indicates whether the report filter is unlocked ( `true` )
or locked ( `false` ). You can edit unlocked filters on the report

run page in Lightning Experience. If unspecified, the default
value is `false` .

Available in API version 38.0 and later.

`operator` FilterOperation (enumeration of
type string)

`snapshot` string

Required. An enumeration of type string that defines the
operator used to filter the data, for example, `greaterThan` .
Valid values are:

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

Represents the date value, either relative (in the format
`N_DAYS_AGO:2` ) or absolute (in the format `yyyy-MM-dd` ).

Available in API version 29.0 and later.

`value` string The value by which you want to filter the data, for example,
`1000` . The Metadata API filter condition values don’t always

match the values that you enter in the report wizard. For
example, in the Metadata API dates are always converted to the
US date format and values entered in a non-US English language
can be converted to a standard US English equivalent.

ReportFormat

An enumeration of type string that defines the report format. Valid values:

**Enumeration Value** **Description**

`Matrix` Summarizes data in a grid. Use to compare related totals.


Metadata Types Report

**Enumeration Value** **Description**

`Summary` Lists, sorts, and subtotals data.

`Tabular` Lists data with no sorting or subtotals.

`Joined` Joins data from different report types storing each report’s data in its own block.

ReportFormattingRule

Defines conditional highlighting for report summary data. You can specify up to 5 formatting rules per report.

**Field** **Field Type** **Description**

`aggregate` ReportFormattingSummaryType Defines how the field specified in `columnName` is
(enumeration of type string) summarized. For example, `Sum` .

`columnName` string Required. Specifies the field whose value ranges are represented
by colors.

`values` ReportFormattingRuleValue Required. Specifies the background colors and associated ranges
(enumeration of type string) for formatted data values.

ReportFormattingSummaryType

An enumeration of type string that defines how report fields are summarized. Valid values:

**Enumeration Value** **Description**

`Sum` Total

`Average` Average

`Maximum` Largest value

`Minimum` Smallest value

`Unique` Unique values

ReportFormattingRuleValue

Specifies the background colors and associated ranges for formatted data values. You can specify up to 3 background colors and 0–3
range upper bounds. Valid values:

**Field** **Field Type** **Description**

`backgroundColor` string (Required) Specifies a highlighting color for the field in
`columnName` . Must be a valid hex color string such as

#54C254. At least one color is required. You can optionally specify
a different color for up to 3 ranges as determined by


Metadata Types Report

**Field** **Field Type** **Description**

`rangeUpperBound` . If you don’t specify a color for a
particular range, the background is transparent.

`rangeUpperBound` double Delineates a range to which a background color applies. If you
don’t specify an upper bound for a particular range, the bound

is assumed to be plus infinity. The following example sets the
background color for the Sales column to #B50E03 for aggregate
sales less than or equal to 100, sets no background for sales from
100 to 1000, and sets the background color to #006714 for sales
greater than 1000.

```
                                <formattingRules>

                                <aggregate>Sum</aggregate>

                                <columnName>Sales</columnName>

                                     <values>

                                <backgroundColor>#B50E03</backgroundColor>

                                <rangeUpperBound>100.0</rangeUpperBound>

                                     </values>

                                     <values>

                                <rangeUpperBound>1000.0</rangeUpperBound>

                                     </values>

                                     <values>

                                <backgroundColor>#006714</backgroundColor>

                                     </values>

                                </formattingRules>

```

ReportParam

ReportParam represents settings specific to a report type, especially options that let you filter a report to certain useful subsets.

**Field** **Field Type** **Description**

`name` string Required. Specifies a specific `reportType` setting.

`value` string Required. The setting value.

ReportAggregateDatatype

An enumeration of type string that specifies the data type for formatting and display of custom summary formula results. Valid values:


Metadata Types Report

**Enumeration Value**

```
   currency

   number

   percent

```

ReportChart

ReportChart represents charts on summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`backgroundColor1` string Specifies the beginning color (in HTML format) for a gradient
color background.

`backgroundColor2` string Specifies the end color (in HTML format) for a gradient color
background.

`backgroundFadeDir` ChartBackgroundDirection Specifies the direction for a gradient color background. Use with
(enumeration of type string) `backgroundColor1` to specify the beginning color and

`backgroundColor2` to specify the end color for the
gradient design. Use white for both if you don’t want a
background design. Valid values:

**•** `Diagonal`

**•** `LeftToRight`

**•** `TopToBottom`

`chartSummaries` ChartSummary[] Specifies the summaries you want to use for the chart. Invalid
summaries are ignored without notification. If there are no valid

summaries, RowCount is used by default for the axis value. This
field is available in API version 17.0 and later.

`chartType` ChartType (enumeration of type Required. Specifies the chart type. Available chart types depend
string) on the `report type` .

`enableHoverLabels` boolean Specifies whether to display values, labels, and percentages
when hovering over charts. Hover details depend on chart type.

Percentages apply to pie, donut, and funnel charts only. This
field is available in API version 17.0 and later.

`expandOthers` boolean Specifies whether to combine all groups less than or equal to
3% of the total into a single 'Others' wedge or segment. Only

applies to pie, donut, and funnel charts. Set to `true` to show
all values individually on the chart; set to `false` to combine
small groups into 'Others.' This field is available in API version
17.0 and later.


Metadata Types Report

**Field** **Field Type** **Description**

`groupingColumn` string

`legendPosition` ChartLegendPosition
(enumeration of type string)

Specifies the field by which to group data. This data is displayed
on the X-axis for vertical column charts and on the Y-axis for
horizontal bar charts.

Required.

The location of the legend with respect to the chart. The valid
values are:

**•** `Bottom`

**•** `OnChart`

**•** `Right`

`location` ChartPosition (enumeration of Required. Specifies whether the chart is displayed at the top or
type string) bottom of the report.

`secondaryGroupingColumn` string For grouped chart types: Specifies the field by which to group
the data.

`showAxisLabels` boolean For bar and line charts: Specifies whether the chart displays
names for each axis.

`showPercentage` boolean

Indicates if percentages are displayed for wedges and segments
of pie, donut, and funnel charts, as well as for gauges ( `true` ),
or not ( `false` ).

`showTotal` boolean Indicates if the total is displayed for donut charts and gauges
( `true` ), or not ( `false` ).

`showValues` boolean Indicates if the values of individual records or groups are
displayed for charts ( `true` ), or not ( `false` ).

`size` ReportChartSize (enumeration Required. Specifies the chart size.
of type string)

`summaryAggregate` ReportSummaryType
(enumeration of type string)

Defines how to summarize the chart data. For example, `Sum` .
No longer supported in version API 17.0 and later. See
`chartSummaries` .

`summaryAxisManualRangeEnd` double When specifying the axis range manually: Defines the ending
value.

`summaryAxisManualRangeStart` double When specifying the axis range manually: Defines the starting
value.

`summaryAxisRange` ChartRangeType (enumeration Required. For bar, line, and column charts: Defines whether to
of type string) specify the axis range manually or automatically.

`summaryColumn` string Required. Specifies the field by which to summarize the chart
data. Typically this field is displayed on the Y-axis. No longer

supported in version API 17.0 and later. See
`chartSummaries` .

`textColor` string The color (in HTML format) of the chart text and labels.


Metadata Types Report

**Field** **Field Type** **Description**

`textSize` int The size of the chart text and labels. Valid values:

**•** `8`

**•** `9`

**•** `10`

**•** `12`

**•** `14`

**•** `18`

**•** `24`

**•** `36`

The maximum size is 18. Larger values are shown at 18 points.

`title` string The chart title. Max 255 characters.

`titleColor` string The color (in HTML format) of the title text.

`titleSize` int The size of the title text. Valid values:

**•** `8`

**•** `9`

**•** `10`

**•** `12`

**•** `14`

**•** `18`

**•** `24`

**•** `36`

The maximum size is 18. Larger values are shown at 18 points.

ChartType

[An enumeration of type string that defines the chart type. For information on each of these chart types, see Chart Types in Salesforce](https://help.salesforce.com/s/articleView?id=analytics.chart_types.htm&type=5&language=en_US)
Help. Valid values:

**Enumeration Value**

```
   None

   HorizontalBar

   HorizontalBarGrouped

   HorizontalBarStacked

   HorizontalBarStackedTo100

   VerticalColumn

```


Metadata Types Report

**Enumeration Value**

```
   VerticalColumnGrouped

   VerticalColumnStacked

   VerticalColumnStackedTo100

   Line

   LineGrouped

   LineCumulative

   LineCumulativeGrouped

   Pie

   Donut

   Funnel

   Scatter

   ScatterGrouped

   VerticalColumnLine

   VerticalColumnGroupedLine

   VerticalColumnStackedLine

   Plugin

```

Reserved for future use. This value is available in API version 31.0 and later.

ChartPosition

An enumeration of type string that specifies the position of the chart in the report. Valid values:

**Enumeration Value**

```
   CHART_TOP

   CHART_BOTTOM

```

ChartSummary

ChartSummary defines how data in the chart is summarized. Valid values:

**Field** **Field Type** **Description**

`aggregate` ReportSummaryType Specifies the aggregation method—such as `Sum`, `Average`,
`Min`, and `Max` —for the summary value. Use the `column`

field to specify the summary value to use for the aggregation.


Metadata Types Report

**Field** **Field Type** **Description**

You don't need to specify this field for RowCount or custom
summary formulas.

`axisBinding` ChartAxis Specifies the axis or axes to use on the chart. Use the `column`
field to specify the summary value to use for the axis.

`column` string Required. Specifies the summary field for the chart data. If all
columns are invalid, RowCount is used by default for the axis

value. For vertical column and horizontal bar combination charts,
you can specify up to four values.

ChartAxis

An enumeration of type string that specifies the axis or axes to be used in charts. Valid values:

**Enumeration Value** **Description**

`x` The summary value to use for the X-axis of a scatter chart.

`y` The Y-axis for the chart.

`y2` The secondary Y-axis for vertical column combination charts with a line added.

ReportChartSize

An enumeration of type string that specifies the chart size. Valid values:

**Enumeration Value**

```
   Tiny

   Small

   Medium

   Large

   Huge

```

ChartRangeType

An enumeration of type string that defines the report format. Valid values:

**Enumeration Value**

```
   Auto

   Manual

```


Metadata Types Report

ReportTimeFrameFilter

ReportTimeFrameFilter represents the report time period.

**Field** **Field Type** **Description**

`dateColumn` string Required. The date field on which to filter data. For example,

```
                              CLOSE_DATE

```

`endDate` date When `interval` is `INTERVAL_CUSTOM`, specifies the end
of the custom time period.

`interval` UserDateInterval (enumeration Required. Specifies the period.
of type string)

`startDate` date When `interval` is `INTERVAL_CUSTOM`, specifies the
start of the custom time period.

ReportCrossFilter

ReportCrossFilter represents the cross filter functionality in reports.

**Field** **Field Type** **Description**

`criteriaItems` ReportFilterItem Represents the subfilters of a cross filter. There can be up to five
subfilters. This field requires the following attributes.

**•** `Column`

**•** `Operator`

**•** `Value`

`operation` ObjectFilterOperator The action indicating whether to include or exclude an object.
(Enumeration of type string) Valid values: `with` and `without` .

`primaryTableColumn` string The field from the parent object used for the cross filter.

`relatedTable` string The child object used for the cross filter.

`relatedTableJoinColumn` string The field from the child object that is used to join the parent.

Declarative Metadata Sample Definition

A sample XML snippet using cross filters to build an Accounts report for cases where case status isn’t closed:

```
      <crossFilters>

        <criteriaItems>

           <column>Status</column>

           <operator>notequal</operator>

           <value>Closed</value>

        </criteriaItems>

        <operation>with</operation>

        <primaryTableColumn>ACCOUNT_ID</primaryTableColumn>

```


Metadata Types Report

```
        <relatedTable>Case</relatedTable>

        <relatedTableJoinColumn>Account</relatedTableJoinColumn>

      </crossFilters>

```

Note: This sample was generated using the API version 23.0.

UserDateInterval

An enumeration of type string that defines the period. Valid values:

**Enumeration Value** **Description**

`INTERVAL_CURRENT` Current fiscal quarter

`INTERVAL_CURNEXT1` Current and next fiscal quarters

`INTERVAL_CURPREV1` Current and previous fiscal quarters

`INTERVAL_NEXT1` Next fiscal quarter

`INTERVAL_PREV1` Previous fiscal quarter

`INTERVAL_CURNEXT3` Current and next three fiscal quarters

`INTERVAL_CURFY` Current fiscal year

`INTERVAL_PREVFY` Previous fiscal year

`INTERVAL_PREV2FY` Previous two fiscal years

`INTERVAL_AGO2FY` Two fiscal years ago

`INTERVAL_NEXTFY` Next fiscal year

`INTERVAL_PREVCURFY` Current and previous fiscal years

`INTERVAL_PREVCUR2FY` Current and previous two fiscal years

`INTERVAL_CURNEXTFY` Current and next fiscal year

`INTERVAL_CUSTOM` A custom time period. Use `startDate` and `endDate` fields to specify the
time period's start date and end date.

`INTERVAL_YESTERDAY` Yesterday

`INTERVAL_TODAY` Today

`INTERVAL_TOMORROW` Tomorrow

`INTERVAL_LASTWEEK` Last calendar week

`INTERVAL_THISWEEK` This calendar week

`INTERVAL_NEXTWEEK` Next calendar week

`INTERVAL_LASTMONTH` Last calendar month

`INTERVAL_THISMONTH` This calendar month


Metadata Types Report

**Enumeration Value** **Description**

`INTERVAL_NEXTMONTH` Next calendar month

`INTERVAL_LASTTHISMONTH` Current and previous calendar months

`INTERVAL_THISNEXTMONTH` Current and next calendar months

`INTERVAL_CURRENTQ` Current calendar quarter

`INTERVAL_CURNEXTQ` Current and next calendar quarters

`INTERVAL_CURPREVQ` Current and previous calendar quarters

`INTERVAL_NEXTQ` Next calendar quarter

`INTERVAL_PREVQ` Previous calendar quarter

`INTERVAL_CURNEXT3Q` Current and next three calendar quarters

`INTERVAL_CURY` Current calendar year

`INTERVAL_PREVY` Previous calendar year

`INTERVAL_PREV2Y` Previous two calendar years

`INTERVAL_AGO2Y` Two calendar years ago

`INTERVAL_NEXTY` Next calendar year

`INTERVAL_PREVCURY` Current and previous calendar years

`INTERVAL_PREVCUR2Y` Current and previous two calendar years

`INTERVAL_CURNEXTY` Current and next calendar years

`INTERVAL_LAST7` Last 7 days

`INTERVAL_LAST30` Last 30 days

`INTERVAL_LAST60` Last 60 days

`INTERVAL_LAST90` Last 90 days

`INTERVAL_LAST120` Last 120 days

`INTERVAL_NEXT7` Next 7 days

`INTERVAL_NEXT30` Next 30 days

`INTERVAL_NEXT60` Next 60 days

`INTERVAL_NEXT90` Next 90 days

`INTERVAL_NEXT120` Next 120 days

`LAST_FISCALWEEK` When custom fiscal years are enabled: Last fiscal week

`THIS_FISCALWEEK` When custom fiscal years are enabled: This fiscal week

`NEXT_FISCALWEEK` When custom fiscal years are enabled: Next fiscal week


Metadata Types Report

**Enumeration Value** **Description**

`LAST_FISCALPERIOD` When custom fiscal years are enabled: Last fiscal period

`THIS_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period

`NEXT_FISCALPERIOD` When custom fiscal years are enabled: Next fiscal period

`LASTTHIS_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period and last fiscal period

`THISNEXT_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period and next fiscal period

`CURRENT_ENTITLEMENT_PERIOD` Current entitlement period

`PREVIOUS_ENTITLEMENT_PERIOD` Previous entitlement period

`PREVIOUS_TWO_ENTITLEMENT_PERIODS` Previous two entitlement periods

`TWO_ENTITLEMENT_PERIODS_AGO` Two entitlement periods ago

`CURRENT_AND_PREVIOUS_ENTITLEMENT_PERIOD` Current and previous entitlement period

`CURRENT_AND_PREVIOUS_TWO_ENTITLEMENT_PERIODS` Current and previous two entitlement periods

Declarative Metadata Sample Definition

A sample XML report definition:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Report xmlns="http://soap.sforce.com/2006/04/metadata">

      <aggregates>

        <acrossGroupingContext>CRT_Object__c$Id</acrossGroupingContext>

        <calculatedFormula>PREVGROUPVAL(CRT_Object__c.Currency__c:AVG, CRT_Object__c.Id)

   *

             PARENTGROUPVAL(CRT_Object__c.Number__c:MAX, CRT_Object__c.CreatedBy.Name,

             COLUMN_GRAND_SUMMARY)/RowCount</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA1</developerName>

        <downGroupingContext>CRT_Object__c$CreatedBy</downGroupingContext>

        <isActive>true</isActive>

        <masterLabel>CurrCSF</masterLabel>

        <scale>2</scale>

      </aggregates>

      <aggregates>

        <acrossGroupingContext>CRT_Object__c$LastModifiedDate</acrossGroupingContext>

        <calculatedFormula>IF(RowCount&gt;10,

             BLANKVALUE(ROUND(PREVGROUPVAL(CRT_Object__c.Currency__c:SUM,

             CRT_Object__c.LastModifiedDate),3),

             PARENTGROUPVAL(CRT_Object__c.Number__c:SUM, ROW_GRAND_SUMMARY,

             CRT_Object__c.Id)), 1000)</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA2</developerName>

        <downGroupingContext>GRAND_SUMMARY</downGroupingContext>

        <isActive>true</isActive>

        <masterLabel>numCSF</masterLabel>

```


Metadata Types Report

```
        <scale>2</scale>

      </aggregates>

      <buckets>

        <bucketType>number</bucketType>

        <developerName>BucketField_BusinessSize</developerName>

        <masterLabel>NumericBucket</masterLabel>

        <nullTreatment>z</nullTreatment>

        <sourceColumnName>SALES</sourceColumnName>

        <values>

           <sourceValues>

             <to>10000</to>

           </sourceValues>

           <value>low</value>

        </values>

        <values>

           <sourceValues>

             <from>10000</from>

             <to>25000</to>

           </sourceValues>

           <value>mid</value>

        </values>

        <values>

           <sourceValues>

             <from>25000</from>

           </sourceValues>

           <value>high</value>

        </values>

      </buckets>

      <buckets>

        <bucketType>text</bucketType>

        <developerName>BucketField_Region</developerName>

        <masterLabel>TextBucket</masterLabel>

        <nullTreatment>n</nullTreatment>

        <otherBucketLabel>Other</otherBucketLabel>

        <sourceColumnName>ADDRESS1_STATE</sourceColumnName>

        <values>

           <sourceValues>

             <sourceValue>CA</sourceValue>

           </sourceValues>

           <value>west</value>

        </values>

        <values>

           <sourceValues>

             <sourceValue>NY</sourceValue>

           </sourceValues>

           <sourceValues>

             <sourceValue>Ontario</sourceValue>

           </sourceValues>

           <value>east</value>

        </values>

      </buckets>

      <chart>

        <backgroundColor1>#FFFFFF</backgroundColor1>

        <backgroundColor2>#FFFFFF</backgroundColor2>

```


Metadata Types Report

```
        <backgroundFadeDir>Diagonal</backgroundFadeDir>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>FORMULA1</column>

        </chartSummaries>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>FORMULA2</column>

        </chartSummaries>

        <chartSummaries>

           <aggregate>Maximum</aggregate>

           <axisBinding>y</axisBinding>

           <column>CRT_Object__c$Number__c</column>

        </chartSummaries>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>RowCount</column>

        </chartSummaries>

        <chartType>VerticalColumn</chartType>

        <groupingColumn>CRT_Object__c$LastModifiedDate</groupingColumn>

        <legendPosition>Right</legendPosition>

        <location>CHART_TOP</location>

        <size>Medium</size>

        <summaryAxisRange>Auto</summaryAxisRange>

        <textColor>#000000</textColor>

        <textSize>12</textSize>

        <titleColor>#000000</titleColor>

        <titleSize>18</titleSize>

      </chart>

      <columns>

        <field>CRT_Object__c$Name</field>

      </columns>

      <columns>

        <aggregateTypes>Average</aggregateTypes>

        <field>CRT_Object__c$Currency__c</field>

      </columns>

      <columns>

        <aggregateTypes>Maximum</aggregateTypes>

        <field>CRT_Object__c$Number__c</field>

      </columns>

      <columns>

        <field>BucketField__Region</field>

      </columns>

      <format>Matrix</format>

      <groupingsAcross>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$Id</field>

        <sortOrder>Asc</sortOrder>

      </groupingsAcross>

      <groupingsAcross>

        <dateGranularity>Year</dateGranularity>

        <field>CRT_Object__c$LastModifiedDate</field>

        <sortOrder>Asc</sortOrder>

      </groupingsAcross>

```


Metadata Types Report

```
      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$CreatedBy</field>

        <sortOrder>Asc</sortOrder>

      </groupingsDown>

      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$Currency__c</field>

        <sortOrder>Desc</sortOrder>

      </groupingsDown>

      <name>CrtMMVC</name>

      <reportType>CRT1__c</reportType>

      <scope>organization</scope>

      <showDetails>false</showDetails>

      <timeFrameFilter>

        <dateColumn>CRT_Object__c$CreatedDate</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

      </timeFrameFilter>

   </Report>

```

Declarative Metadata Sample Definition for a Joined Report

A sample XML report definition:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Report xmlns="http://soap.sforce.com/2006/04/metadata">

   <!-- This is a cross-block custom summary formula. Note that the calculated formula reference

    for a blocks reference uses the BlockId#Aggregate. -->

      <aggregates>

        <calculatedFormula>B1#AMOUNT:SUM+B2#EMPLOYEES:SUM</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA</developerName>

        <isActive>true</isActive>

        <isCrossBlock>true</isCrossBlock>

        <masterLabel>Cross-Block CSF Example</masterLabel>

        <scale>2</scale>

      </aggregates>

   <!-- This is a standard custom summary formula. Note that the calculated formula reference

    does not have block reference but just the aggregate name of the report type associated

   (Opportunity).-->

      <aggregates>

        <calculatedFormula>AMOUNT:SUM</calculatedFormula>

        <developerName>FORMULA2</developerName>

        <isActive>true</isActive>

        <isCrossBlock>false</isCrossBlock>

        <masterLabel>Standard CSF Example</masterLabel>

        <reportType>Opportunity</reportType>

        <scale>2</scale>

      </aggregates>

      <block>

       <blockInfo>

   <!-- This is how the block defines that the custom summary formula should be referenced.

   In this example, it’s the in standard FORMULA 2 defined above. This block report has blockID

    B1.-->

```


Metadata Types Report

```
        <aggregateReferences>

         <aggregate>FORMULA2</aggregate>

        </aggregateReference>

        <blockId>B1</blockId>

        <joinTable>a</joinTable>

       </blockInfo>

       <columns>

        <field>TYPE</field>

       </columns>

       <format>Summary</format>

       <name>Opportunities BLock 3</name>

       <params>

        <name>role_territory</name>

        <value>role</value>

       </params>

       <params>

        <name>terr</name>

        <value>all</value>

       </params>

       <params>

        <name>open</name>

        <value>all</value>

       </params>

       <params>

        <name>probability</name>

        <value>0</value>

       </params>

       <params>

        <name>co</name>

        <value>1</value>

       </params>

       <reportType>Opportunity</reportType>

       <scope>organization</scope>

       <timeFrameFilter>

        <dateColumn>CLOSE_DATE</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

       </timeFrameFilter>

      </block>

      <block>

       <blockInfo>

   <!-- This is how the block defines that the custom summary formula should be referenced.

   In this example, it’s the cross-block custom summary formula FORMULA 1 defined above. This

    block report has blockId B2.-->

        <aggregateReferences>

         <aggregate>FORMULA1</aggregate>

        </aggregateReferences>

        <blockId>B2</blockId>

        <joinTable>a</joinTable>

       </blockInfo>

       <columns>

        <field>USERS.NAME</field>

       </columns>

       <columns>

        <field>TYPE</field>

```


Metadata Types Report

```
       </columns>

       <columns>

         <field>DUE_DATE</field>

       </columns>

       <columns>

        <field>LAST_UPDATE</field>

       </columns>

       <columns>

        <field>ADDRESS1_STATE</field>

       </columns>

       <format>Summary</format

       <name>Accounts block 5</name>

       <params>

        <name>terr</name>

        <value>all</value>

       </params>

       <params>

        <name>co</name>

        <value>1</value>

       </params>

       <reportType>AccountList</reportType>

       <scope>organization</scope>

       <timeFrameFilter>

        <dateColumn>CREATED_DATE</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

       </timeFrameFilter>

      </block>

      <blockInfo>

       <blockId xsi:nil="true"/>

       <joinTable>a</joinTable>

      </blockInfo>

   <chart>

        <backgroundColor1>#FFFFFF</backgroundColor1>

        <backgroundColor2>#FFFFFF</backgroundColor2>

        <backgroundFadeDir>Diagonal</backgroundFadeDir>

        <chartSummaries>

           <axisBinding>y</axisBinding>

   <!-- This is how chart aggregates are designed in multiblock. We're using RowCount from

   Block 1.-->

           <column>B1#RowCount</column>

        </chartSummaries>

        <chartType>HorizontalBar</chartType>

        <enableHoverLabels>false</enableHoverLabels>

        <expandOthers>true</expandOthers>

        <groupingColumn>ACCOUNT_NAME</groupingColumn>

        <location>CHART_TOP</location>

        <showAxisLabels>true</showAxisLabels>

        <showPercentage>false</showPercentage>

        <showTotal>false</showTotal>

        <showValues>false</showValues>

        <size>Medium</size>

        <summaryAxisRange>Auto</summaryAxisRange>

        <textColor>#000000</textColor>

        <textSize>12</textSize>

```


### Metadata Types ReportType

```
        <titleColor>#000000</titleColor>

        <titleSize>18</titleSize>

      </chart>

      <format>MultiBlock</format>

      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>ACCOUNT_NAME</field>

        <sortOrder>Asc</sortOrder>

      </groupingsDown>

      <name>mb_mbapi</name>

      <reportType>Opportunity</reportType>

      <showDetails>true</showDetails>

   </Report>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Dashboard

### ReportType

Represents the metadata associated with a custom report type. Custom report types allow you to build a framework from which users
can create and customize reports.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.reportType` for the custom report type definition. There’s one file per custom report type. Report types are stored
in the `reportTypes` directory of the corresponding package directory.

Version

Custom report types are available in API version 14.0 and later.


Metadata Types ReportType

Fields

**Field Name** **Field Type** **Description**

`autogenerated` boolean

`baseObject` string

Indicates that the report type was automatically generated when historical
trending was enabled for an entity.

Available in API version 29 and later.

Required. The primary object for the custom report type, for example,
Account. All objects, including custom and external objects, are supported.
You can’t edit this field after initial creation.

Support for external objects is available in API version 38.0 and later.

`category` ReportTypeCategory This field controls the category for the report. The valid values are:
(enumeration of type string)

**•** `accounts`

**•** `opportunities`

**•** `forecasts`

**•** `cases`

**•** `leads`

**•** `campaigns`

**•** `activities`

**•** `busop`

**•** `products`

**•** `admin`

**•** `territory`

**•** `territory2` (This value is available in API version 31.0 and later.)

**•** `usage_entitlement`

**•** `wdc` (This value is available in API version 29.0 and later.)

**•** `calibration` (This value is available in API version 29.0 and later.)

**•** `other`

**•** `content`

**•** `quotes`

**•** `individual` (This value is available in API version 45.0 and later.)

**•** `employee` (This value is available in API version 46.0 and later.)

**•** `data_cloud` (This value is available in API version 55.0 and later.)

**•** `commerce` (This value is available in API version 60.0 and later.)

**•** `flow` (This value is available in API version 60.0 and later.)

**•** `semantic_model` (This value is available in API version 60.0 and
later.)

`deployed` boolean Required. Indicates whether the report type is available to users ( `true` )
or whether it's still in development ( `false` ).


Metadata Types ReportType

**Field Name** **Field Type** **Description**

`description` string The description of the custom report type.

`fullName` string The report type developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

`join` ObjectRelationship The object joined to the `baseObject` . For example, Contacts can be
joined to the primary Accounts object.

`label` string Required. The report type label.

`sections` ReportLayoutSection[] The groups of columns available for the report type. Though columns
aren’t strictly required, a report without columns isn’t useful.

ObjectRelationship

ObjectRelationship represents a join to another object.

**Field Name** **Field Type** **Description**

`join` ObjectRelationship This field is a recursive reference that allows you to join more than two objects.
A maximum of four objects can be joined in a custom report type. When more

than two objects are joined, an inner join isn’t allowed if there has been an outer
join earlier in the join sequence. The `baseObject` is first joined to the object
specified in `relationship` ; the resulting dataset is then joined with any
objects specified in this field.

`outerJoin` boolean

Required. Indicates whether it’s an outer join ( `true` ) or not ( `false` ). An outer
join returns a row even if the joined table doesn’t contain a matching value in
the join column.

`relationship` string Required. The object joined to the primary object; for example, Contacts.

ReportLayoutSection

ReportLayoutSection represents a group of columns used in the custom report type.

**Field Name** **Field Type** **Description**

`columns` ReportTypeColumn[] The list of columns projected from the query, defined by
this custom report type.

`masterLabel` string Required. The label for this group of columns in the report
wizard.


Metadata Types ReportType

ReportTypeColumn

ReportTypeColumn represents a column in the custom report type.

**Field Name** **Field Type** **Description**

`checkedByDefault` boolean Required. Indicates whether this column is selected by default ( `true` ) or not
( `false` ).

`displayNameOverride` string A customized column name, if desired.

`field` string Required. The field name associated with the report column.

`table` string Required. The table associated with the field; for example, Account.

Declarative Metadata Sample Definition

The definition of a custom report type is shown in this example. Account is joined to Contacts and the resulting dataset is joined with
Assets.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ReportType xmlns="http://soap.sforce.com/2006/04/metadata">

      <baseObject>Account</baseObject>

      <category>accounts</category>

      <deployed>true</deployed>

      <description>Account linked to Contacts and Assets</description>

      <join>

        <join>

           <outerJoin>false</outerJoin>

           <relationship>Assets</relationship>

        </join>

        <outerJoin>false</outerJoin>

        <relationship>Contacts</relationship>

      </join>

      <label>Account Contacts and Assets</label>

      <sections>

        <columns>

           <checkedByDefault>true</checkedByDefault>

           <field>obj_lookup__c.Id</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>obj_lookup__c.Name</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Opportunity__c.Amount</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Owner.IsActive</field>

```


### Metadata Types RestrictionRule

```
           <table>Account</table>

        </columns>

        <masterLabel>Accounts</masterLabel>

      </sections>

      <sections>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Owner.Email</field>

           <table>Account.Contacts</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>byr__c</field>

           <table>Account.Contacts</table>

        </columns>

        <columns>

           <checkedByDefault>true</checkedByDefault>

           <field>ReportsTo.CreatedBy.Contact.Owner.MobilePhone</field>

           <table>Account.Contacts</table>

        </columns>

        <masterLabel>Contacts</masterLabel>

      </sections>

   </ReportType>

```

Usage

The custom report type refers to fields by using their API names. For a historical field (one that has `trackTrending` set to `true` )
the API name includes `hst`, such as `Field2__c_hst` .

```
   <sections>

      <columns>

        <checkedByDefault>false</checkedByDefault>

        <field>Field2__c_hst</field>

        <table>CustomTrendedObject__c.CustomTrendedObject__c_hst</table>

      </columns>

      <masterLabel>History</masterLabel>

   </sections>

```

For more information, see `trackTrending` on page 780.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RestrictionRule Represents a restriction rule or a scoping rule. A restriction rule has enforcementType set to Restrict and controls the access

that specified users have to designated records. A scoping rule has `enforcementType` set to `Scoping` and controls the default
records that your users see without restricting access. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types RestrictionRule

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

RestrictionRule components have the suffix `.rule` and are stored in the `restrictionRules` folder.

Version

RestrictionRule components are available in API version 52.0 and later.

Special Access Rules

Only users with the View Restriction and Scoping Rules permission can view restriction rules and scoping rules via the API. Only users
with the Manage Sharing permission can view, create, update, and delete restriction rules and scoping rules.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the rule is active ( `true` ) or not ( `false` ). The default
value is `false` .

`description` string Required. The description of the rule.

```
enforcementType

```

EnforcementType Required. The type of rule. Valid values are:
(enumeration of

**•** `FieldRestrict` —Don’t use.

type string)

**•** `FieldRestrict` —Don’t use.

**•** `Restrict` —Restriction rule.

**•** `Scoping` —Scoping rule.

`masterLabel` string Required. The name of the rule.

`recordFilter` string Required. The criteria that determine which records are accessible via
the rule.

`targetEntity` string

Required. The object for which you're creating the rule. We recommend
that you don’t edit this field after the rule is created.

If `enforcementType` is set to `Restrict`, custom objects, external
objects, and these objects are supported:

**•** Contract

**•** Event

**•** Quote

**•** Task

**•** TimeSheet

**•** TimeSheetEntry


Metadata Types RestrictionRule

**Field Name** **Field Type** **Description**

If `enforcementType` is set to `Scoping`, custom objects and these
objects are supported:

**•** Account

**•** Case

**•** Contact

**•** Event

**•** Lead

**•** Opportunity

**•** Task

`userCriteria` string Required. The users that this rule applies to, such as all active users or
users with a specified role or profile.

`version` int Required. The rule's version number.

Declarative Metadata Sample Definition

The following is an example of a RestrictionRule component representing a restriction rule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>Allows users with a specific profile to see only tasks that they

   own.</description>

      <enforcementType>Restrict</enforcementType>

      <masterLabel>Tasks You Own</masterLabel>

      <recordFilter>OwnerId = $User.Id</recordFilter>

      <targetEntity>Task</targetEntity>

      <userCriteria>$User.ProfileId = '00exxxxxxxxxxxx'</userCriteria>

      <version>1</version>

   </RestrictionRule>

```

The following is an example of a RestrictionRule component representing a scoping rule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>View tasks contacts from Department A.</description>

      <enforcementType>Scoping</enforcementType>

      <masterLabel>SR for Department A contacts</masterLabel>

      <recordFilter>Department=$User.Department</recordFilter>

      <targetEntity>Contact</targetEntity>

      <userCriteria>$User.UserRoleId = '00Exxxxxxxxxxxx'</userCriteria>

      <version>1</version>

   </RestrictionRule>

```


### Metadata Types RetrievalSummaryDefinition

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RestrictionRule</name>

      </types>

      <version>55.0</version>

   </Package>

### RetrievalSummaryDefinition

```

Represents a metadata type that stores the header information of a retrieval definition. It enables the configuration of data retrieval
patterns for summarizing related records across object relationships.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RetrievalSummaryDefinition components have the suffix .retrievalSummaryDefinition and are stored in the

`.retrievalSummaryDefinitions` folder.

Version

### RetrievalSummaryDefinition components are available in API version 61.0 and later. Individual fields may have specific minimum API

version requirements as mentioned in the field descriptions.

Fields

**Field Name** **Description**

```
masterLabel

retrievalSummaryDefFields

```

**Field Type**
string

**Description**

Required.

A user-friendly name when RetrievalSummaryDefinition is created.

**Field Type**

RetrievalSummaryDefField[]

**Description**
Collection of fields to retrieve from the root object of the retrieval definition. Each field
definition specifies which field from the target object should be included in the retrieval
and the order in which it should be processed.


Metadata Types RetrievalSummaryDefinition

**Field Name** **Description**

```
retrievalSummaryDefObjects

rootObject

```

**Field Type**

RetrievalSummaryDefObject[]

**Description**
Collection of rollup definitions that aggregate data from related objects. Each object
definition specifies a related object, the aggregation logic to apply, and the fields to
retrieve from that object. This enables hierarchical data aggregation across object
relationships.

**Field Type**
string

**Description**

Required.

API name of the primary object that serves as the starting point for the retrieval
definition. This object serves as the anchor point for all retrieval and rollup operations
defined in this metadata. The value must be a valid Salesforce object API name.

RetrievalSummaryDefField

Represents a field definition that specifies a single field to retrieve from a target object. Each field definition includes the field API name
and a sequence number that determines the processing order.

**Field Name** **Description**

```
field

sequenceNumber

```

**Field Type**
string

**Description**

Required.

API name of the field to retrieve from the target object. This must be a valid field API
name on the specified object.

**Field Type**
int

**Description**

Required.

Processing order of the field in the retrieval operation. Fields are processed in ascending
sequence number order. This allows you to control the order in which fields are
displayed.


Metadata Types RetrievalSummaryDefinition

RetrievalSummaryDefObject

Represents a rollup definition that aggregates data from a related object. Each rollup definition specifies the aggregation logic, the fields
to retrieve, and the processing order for summarizing data across object relationships.

**Field Name** **Description**

```
recordAggregationDefinition

retrievalSummaryDefFields

sequenceNumber

```

Usage

**Field Type**
string

**Description**

Required.

Reference to the aggregation definition that specifies how data from the related object
must be aggregated. This parameter references a RecordAggregationDefinition.

**Field Type**

RetrievalSummaryDefField[]

**Description**
Collection of fields to retrieve from this related object. Each field definition specifies
which field should be included and in what order. This is an optional array that allows
you to specify additional fields beyond those defined in the aggregation definition.

**Field Type**
int

**Description**

Required.

Processing order of the rollup operation. Rollups are processed in ascending sequence
number order, allowing you to control the hierarchy of data aggregation when multiple
related objects are involved.

RetrievalSummaryDefinition is commonly used in Financial Services Cloud to define patterns for retrieving and summarizing data across
related objects. Typical use cases include:

**•** Rollup Summarization: Aggregate data from child records to parent records, such as summing transaction amounts or counting
related activities.

**•** Hierarchical Data Aggregation: Retrieve and summarize data across multiple levels of object relationships, enabling complex reporting
and analytics.

**•** Data Consolidation: Combine information from multiple related objects into a single summary view for easier analysis and
decision-making.

**•** Performance Optimization: Pre-define retrieval patterns to improve query performance when accessing related data across multiple
objects.


### Metadata Types Role

Declarative Metadata Sample Definition

The following is an example of a RetrievalSummaryDefinition component that retrieves data from an Account object and includes a
rollup from related Opportunity records.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RetrievalSummaryDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

     <masterLabel>Account Revenue Summary</masterLabel>

     <rootObject>Account</rootObject>

     <retrievalSummaryDefFields>

       <field>Name</field>

       <sequenceNumber>1</sequenceNumber>

     </retrievalSummaryDefFields>

     <retrievalSummaryDefFields>

       <field>Industry</field>

       <sequenceNumber>2</sequenceNumber>

     </retrievalSummaryDefFields>

     <retrievalSummaryDefObjects>

       <recordAggregationDefinition>OpportunityRevenueRollup</recordAggregationDefinition>

       <sequenceNumber>1</sequenceNumber>

       <retrievalSummaryDefFields>

         <field>Amount</field>

         <sequenceNumber>1</sequenceNumber>

       </retrievalSummaryDefFields>

       <retrievalSummaryDefFields>

         <field>CloseDate</field>

         <sequenceNumber>2</sequenceNumber>

       </retrievalSummaryDefFields>

     </retrievalSummaryDefObjects>

   </RetrievalSummaryDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RetrievalSummaryDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Role

Represents a role in your organization.


### Metadata Types RoleOrTerritory

Declarative Metadata File Suffix and Directory Location

The file suffix for role components is `.role` and components are stored in the `roles` directory of the corresponding package
directory.

Version

Role components are available in API version 24.0 and later.

Fields

This metadata type extends to subtype RoleOrTerritory on page 1915.

**Field Name** **Field Type** **Description**

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component. Corresponds to **Role Name** in the user interface.

`parentRole` string The role above this role in the hierarchy.

Declarative Metadata Sample Definition

The following is the definition of a role.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Role xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Role</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>R22</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Role>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RoleOrTerritory

Represents the common base type and valid values for role or territory.


Metadata Types RoleOrTerritory

Version

RoleOrTerritory components are available in API version 24.0 and later.

You can’t create a RoleOrTerritory component directly. Use the Role or Territory metadata types instead.

Fields

**Field Name** **Field Type** **Description**

`caseAccessLevel` string Specifies whether a user can access other users’ cases that are associated
with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`

**•** `None`

This field is not visible if your organization’s sharing model for cases is
Public Read/Write.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

`contactAccessLevel` string Specifies whether a user can access other users’ contacts that are
associated with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`

**•** `None`

This field is not visible if your organization’s sharing model for contacts
is Public Read/Write or Controlled by Parent.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

`description` string The description of the role or territory.

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component.

`mayForecastManagerShare` boolean Indicates whether the forecast manager can manually share their own
forecast.

`name` string Required. The name of the role or territory.

`opportunityAccessLevel` string Specifies whether a user can access other users’ opportunities that are
associated with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`


### Metadata Types RpaRobotPoolMetadata

**Field Name** **Field Type** **Description**

**•** `None`

This field is not visible if your organization’s sharing model for
opportunities is Public Read/Write.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

Declarative Metadata Sample Definition

The following is the definition of a role.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Role xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Role</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>R22</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Role>

```

The following is the definition of a territory.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Territory xmlns="http://soap.sforce.com/2006/04/metadata">

      <accountAccessLevel>Edit</accountAccessLevel>

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Territory</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>T22name</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Territory>

```

SEE ALSO:

Role

Territory

### RpaRobotPoolMetadata

Reserved for future use.


### Metadata Types SalesWorkQueueSettings SalesWorkQueueSettings

Represents settings used to customize work queue options for third-party scoring. In Sales Engagement, you can add a custom number
field on person accounts, contacts, or leads. Then, use the custom number field to sort the work queue. This type extends the Metadata
metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SalesWorkQueueSettings components have the suffix .salesworkqueuesetting and are stored in the

`salesworkqueuesettings` folder.

Version

### SalesWorkQueueSettings components are available in API version 49.0 and later.

Special Access Rules

You must be a Sales Engagement customer to access this metadata type.

Fields

**Field Name** **Field Type** **Description**

`featureName` string The feature that the SalesWorkQueueSettings record is configuring. The allowed
value is `ThirdPartyScore` .

`targetEntity` string The type that the SalesWorkQueueSettings record is configuring. Possible values
are:

**•** `Contact`

**•** `Lead`

**•** `PersonAccount`

`targetField` string The developer name or ID of the custom number field that is used to sort the
work queue. Custom fields must have a custom number data type.

**•** To use Einstein Intelligence Score for lead scoring, use
`ScoreIntelligence.Score` for the developer name.

**•** To remove custom number fields from the work queue, use `None` .

Declarative Metadata Sample Definition

The following is an example of a SalesWorkQueueSettings component. The value for `targetField` is set to `00NRM000001g55D`
as an example of a custom field ID. Replace this value with the ID of your custom field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SalesWorkQueueSettings xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types SamlSsoConfig

```
      <featureName>ThirdPartyScore</featureName>

      <targetEntity>Contact</targetEntity>

      <targetField>00NRM000001g55D</targetField>

   </SalesWorkQueueSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>SalesWorkQueueSettings</name>

      </types>

      <version>49.0</version>

   </Package>

```

Usage

Create one SalesWorkQueueSettings record for each type. For example, suppose that you want to create a work queue to sort leads by
your custom field called `customLeadScore` . Create a SalesWorkQueueSettings record and set `featureName` to
`ThirdPartyScore`, `targetEntity` to `Lead`, and `targetField` to `customLeadScore` .

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SamlSsoConfig

Represents a SAML Single Sign-On configuration. This type extends the Metadata metadata type and inherits its `fullName` field.
Single sign-on (SSO) is an authentication method that enables users to access multiple applications with one login and one set of
credentials. For example, after users log in to your org, they can automatically access all apps from the App Launcher. You can set up
your Salesforce org to trust a third-party identity provider to authenticate users. Or you can configure a third-party app to rely on your
org for authentication.

File Suffix and Directory Location

### SamlSsoConfig components have the suffix .samlssoconfig and are stored in the samlssoconfigs folder.

Version

### SamlSsoConfig components are available in API version 28.0 and later.

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission or both the Customize Application and Modify
All Data permissions can access this type.


Metadata Types SamlSsoConfig

Fields

**Field Name** **Field Type** **Description**

`attributeNameIdFormat` string For SAML 2.0, only and when `identityLocation` is set to
`Attribute` . Possible values include `unspecified`,

`emailAddress`, or `persistent` . All legal values can be found in
[the “Name Identifier Format Identifiers” section of the Assertions and](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)
[Protocols SAML 2.0 specification.](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

`attributeName` string The name of the identity provider’s application. Get this name from your
identity provider.

`decryptionCertificate` string

`errorUrl` string

The name of the certificate to use for decrypting incoming SAML
assertions. This certificate is saved in the organization’s Certificate and
Key Management list. Available in API version 30.0 and later.

When there's an error during login, specify the URL of the page where
users are directed. It must be publicly accessible, such as a public site
Visualforce page. The URL can be absolute or relative.

`executionUserId` string The user that runs the Apex handler class. The user must have the Manage
Users permission. If you specify a SAML JIT handler class, a user is required.

```
identityLocation

identityMapping

```

SamlIdentityLocationType The location in the assertion where a user is identified. Valid values are:
(enumeration of type

**•** `SubjectNameId`           - The identity is in the `<Subject>`

string)

statement of the assertion.

**•** `Attribute`           - The identity is specified in an
`<AttributeValue>`, located in the `<Attribute>` of the
assertion.

SamlIdentityType The identifier the service provider uses for the user during Just-in-Time
(enumeration of type user provisioning. Valid values are:
string)

**•** `Username`           - The user’s Salesforce username.

**•** `FederationId`           - The federation ID from the user object; the
identifier used by the service provider for the user.

**•** `UserId`           - The user ID from the user’s Salesforce organization.

`issuer` string The identification string for the Identity Provider.

`loginUrl` string For SAML 2.0 only: The URL where Salesforce sends a SAML request to
start the login sequence.

`logoutUrl` string For SAML 2.0 only: The URL to direct the user to when they click the
Logout link. The default is `https://salesforce.com` .

`name` string The unique name used by the API and managed packages. The name
must begin with a letter and use only alphanumeric characters and

underscores. The name cannot end with an underscore or have two
consecutive underscores.


Metadata Types SamlSsoConfig

**Field Name** **Field Type** **Description**

`oauthTokenEndpoint` string For SAML 2.0 only: The ACS URL used with enabling Salesforce as an
identity provider in the web single sign-on OAuth assertion flow.

`redirectBinding` boolean Choose the binding mechanism your identity provider requests for your
SAML messages. Values are:

**•** `HTTP POST`                          - HTTP POST binding sends SAML messages using
base64-encoded HTML forms.

**•** `HTTP Redirect`                          - HTTP Redirect binding sends base64-encoded
and URL-encoded SAML messages within URL parameters.

`requestSignatureMethod` string The method that’s used to sign the SAML request. Valid values are
`RSA-SHA1` and `RSA-SHA256` .

`requestSigningCertId` string

The 18-digit ID for the certificate used to generate the signature on a
SAML request to the identity provider. The certificate is saved in the
Certificate and Key Management page in Setup.

`salesforceLoginUrl` string The URL associated with login for the web single sign-on flow.

Note: When encryption is enabled, the URL has a parameter
containing the ID of the SAML configuration,

`sc=` _**`samlSsoConfigId`**_ . For example,
`https://mycompany.my.salesforce.com?sc=0LEB0000000CCC` .
This change applies to API Version 47.0 and later.

`samlEntityId` string

The issuer in SAML requests generated by Salesforce, and is also the
expected audience of any inbound SAML Responses. Salesforce
recommends that you use your My Domain login URL.

`samlJitHandlerId` string The name of an existing Apex class that implements the
`Auth.SamlJitHandler` interface.

`samlVersion` SamlType (enumeration of The SAML version in use. Valid values are:
type string)

**•** `SAML1_1`                       - SAML 1.1

**•** `SAML2_0`                       - SAML 2.0

The HTTP binding type. This value determines where to put the
LogoutRequest or LogoutResponse in the SAML request during single
logout (SLO). The value is base64 encoded. Valid values are:

**•** `RedirectBinding` - Sent in the query string, deflated.

**•** `PostBinding` - Sent in the POST body, not deflated.

The SAML single logout endpoint. This URL is the endpoint where
Salesforce sends LogoutRequests (when Salesforce initiates a logout), or
LogoutResponses (when the identity provider initiates a logout).

```
singleLogoutBinding

```

SamlSpSLOBinding
(enumeration of type
string)

`singleLogoutUrl` string

`useConfigRequestMethod` boolean If `true`, applies the selected Request Signature Method (RSM) during
single logout. If `false`, the default RSM (RSA-SHA1) is applied.


Metadata Types SamlSsoConfig

**Field Name** **Field Type** **Description**

`useSameDigestAlgoForSigning` boolean

`userProvisioning` boolean

If `true`, uses a digest algorithm based on the selected Request Signature
Method (RSM). For example, if the selected RSM is `RSA-SHA256`, the
digest algorithm is set to `SHA-256` .

If `false`, uses the default digest algorithm ( `SHA-1` ), regardless of the
selected RSM.

This field is available in API version 55.0 and later. You can edit this field
only for legacy SAML configurations created before Spring ’22. For
configurations created after Spring ’22, this field is `true` by default.

If `true`, Just-in-Time user provisioning is enabled, which creates users
the first time they log in. Specify `Federation ID` for the
`identityMapping` value to use this feature.

`validationCert` string The certificate used to validate the request. Get this certificate from your
identity provider.

Declarative Metadata Sample Definition

The following is an example of a SamlSsoConfig component. The validation certificate string has been truncated for readability.

```
<?xml version="1.0" encoding="UTF-8"?>

<SamlSsoConfig xmlns="http://soap.sforce.com/2006/04/metadata">

  <identityLocation>SubjectNameId</identityLocation>

  <identityMapping>FederationId</identityMapping>

  <issuer>https://my-idp.my.salesforce.com</issuer>

  <loginUrl>

   https://my-idp.my.salesforce.com/idp/endpoint/HttpRedirect

  </loginUrl>

  <logoutUrl>https://www.salesforce.com</logoutUrl>

  <name>SomeCompany</name>

  <oauthTokenEndpoint>

   https://login.salesforce.com/services/oauth2/token?so=00DD0000000

  </oauthTokenEndpoint>

  <redirectBinding>true</redirectBinding>

  <requestSignatureMethod>RSA-SHA1</requestSignatureMethod>

  <salesforceLoginUrl>

   https://login.salesforce.com?so=00DD0000000JxeI

  </salesforceLoginUrl>

  <samlEntityId>

   https://saml.salesforce.com/customPath

  </samlEntityId>

  <samlVersion>SAML2_0</samlVersion>

  <useConfigRequestMethod>true</useConfigRequestMethod>

  <userProvisioning>false</userProvisioning>

  <validationCert>

   MIIEojCCA4qgAwIBAgIOATtxsoBFAAAAAD4...

  </validationCert>

</SamlSsoConfig>

```


### Metadata Types SchedulingObjective

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SchedulingObjective

Represents a scheduling objective in Workforce Engagement. Scheduling objectives define business goals that the scheduling tools
consider when identifying agents for shifts.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SchedulingObjective components have the suffix .SchedulingObjective and are stored in the SchedulingObjective folder.

Version

### SchedulingObjective components are available in API version 55.0 and later.

Special Access Rules

This type is available only if Workforce Engagement is enabled in your org. To view, create, edit, and delete records, the user requires
the Workforce Engagement Planner permission set.

Fields

**Field Name** **Description**

```
isProtected

masterLabel

```

**Field Type**
boolean

**Description**
Indicates whether the component is protected ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
string

**Description**
Required. The name of the objective.


Metadata Types SchedulingObjective

**Field Name** **Description**

```
schedulingCategory

schedulingObjectiveParameters

schedulingObjectiveType

```

**Field Type**
SchedulingCategory (enumeration of type string)

**Description**
Required. What the scheduling logic applies the objective to. The valid values are:

**•** `A` —Service Appointment

**•** `B` —Shift

**Field Type**

```
  SchedulingObjectiveParameter[] on page 1924

```

**Description**
Parameters associated with a scheduling objective, such as the number of days before
and after a shift that the logic considers when balancing assignments.

**Field Type**
SchedulingObjectiveType (enumeration of type string)

**Description**
Required. Specifies the type of objective. Possible values are:

**•** `AgentPreference` —In the UI, this value appears as Maximized Preferences.

**•** `BalanceNonStandardShifts`

**•** `BalanceShifts`

SchedulingObjectiveParameter

Represents a parameter that’s associated with a scheduling objective.

**Field Name** **Description**

```
parameterKey

value

```

**Field Type**
ObjectiveParameterKey (enumeration of type string)

**Description**
Required. The scheduling objective parameter key. Possible values are:

**•** `DaysAhead`

**•** `DaysBack`

**Field Type**
string

**Description**
The scheduling objective parameter value.


### Metadata Types SchedulingRule

Declarative Metadata Sample Definition

The following is an example of a `SchedulingObjective` component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SchedulingObjective xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>Balance Shifts</masterLabel>

      <schedulingCategory>B</schedulingCategory>

      <schedulingObjectiveType>BalanceShifts</schedulingObjectiveType>

      <schedulingObjectiveParameters>

        <parameterKey>DaysAhead</parameterKey>

        <value>30</value>

      </schedulingObjectiveParameters>

   </SchedulingObjective>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>SchedulingObjective</name>

    <members>Balance Shifts</members>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SchedulingRule

Represents a scheduling rule in Workforce Engagement Management. Scheduling rules determine when agents are assigned to shifts.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SchedulingRule components have the suffix .schedulingRule and are stored in the SchedulingRules folder.

Version

### SchedulingRule components are available in API version 53.0 and later.


Metadata Types SchedulingRule

Special Access Rules

This type is available only if Workforce Engagement is enabled in your org. To view, create, edit, and delete records, the user requires
the Workforce Engagement Planner permission set.

Fields

**Field Name** **Description**

```
isProtected

masterLabel

schedulingCategory

schedulingRuleParameters

schedulingRuleType

```

**Field Type**
boolean

**Description**
Indicates whether the component is protected ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
string

**Description**
Required. The name of the rule.

**Field Type**
SchedulingCategory (enumeration of type string)

**Description**
Required. What the scheduling logic applies the rule to. The valid values are:

**•** `A` —Service Appointment

**•** `B` —Shift

**Field Type**

```
  SchedulingRuleParameter[] on page 1927

```

**Description**
Parameters associated with a scheduling rule, such as work limits.

**Field Type**
SchedulingRuleType (enumeration of type string)

**Description**
Required. Specifies the type of rule. The valid values are:

**•** `A` —Active Resources

**•** `B` —Match Skills

**•** `C` —Availability

**•** `M` —Match Territory

**•** `Q` —Match Queue

**•** `RestTimeMinutes` —Rest Time in Minutes. Available in API version 56.0 and
later.


Metadata Types SchedulingRule

**Field Name** **Description**

**•** `W` —Work Limit

**•** `LimitNonstandardShifts` —Specifies a rule type that limits how many
non-standard shifts can be assigned to each agent. Available in API version 54.0
and later.

SchedulingRuleParameter

Represents a scheduling rule parameter, such as a work limit, that’s associated with a scheduling rule.

**Field Name** **Description**

```
schedulingParameterKey

value

```

**Field Type**
SchedulingParameterKey (enumeration of type string)

**Description**
Required. The scheduling rule parameter key.

**•** `C` —Constraint Field Name

**•** `L` —Limit Type

**•** `R` —Resolution

**•** `T` —Time Resolution

**•** `W` —Work Unit

**•** `ConsiderAbsence` —Consider resource absences when evaluating availability.
Available in API version 56.0 and later.

**•** `ConsiderSTM` —Consider service territory membership, which defines working
hours, when evaluating availability. Available in API version 56.0 and later.

**Field Type**
string

**Description**
The scheduling rule parameter value.

Declarative Metadata Sample Definition

The following is an example of a `SchedulingRule` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SchedulingRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Max Shifts Per Week</masterLabel>

   <schedulingCategory>B</schedulingCategory>

   <schedulingRuleParameters>

     <schedulingParameterKey>C</schedulingParameterKey>

     <value>MaxShiftsPerWeek</value>

   </schedulingRuleParameters>

   <schedulingRuleParameters>

```


### Metadata Types Scontrol

```
        <schedulingParameterKey>W</schedulingParameterKey>

        <value>Shifts</value>

      </schedulingRuleParameters>

      <schedulingRuleParameters>

        <schedulingParameterKey>R</schedulingParameterKey>

        <value>Week</value>

      </schedulingRuleParameters>

      <schedulingRuleParameters>

        <schedulingParameterKey>L</schedulingParameterKey>

        <value>Max</value>

      </schedulingRuleParameters>

      <schedulingRuleType>W</schedulingRuleType>

   </SchedulingRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>SchedulingRule</name>

    <members>MaxShiftsPerWeek</members>

      </types>

      <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Scontrol

Deprecated. Represents an Scontrol component, corresponding to an s-control in the Salesforce user interface.

Important: Visualforce pages supersede s-controls. Organizations that haven't previously used s-controls can’t create them.
Existing s-controls are unaffected and can still be edited.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Declarative Metadata File Suffix and Directory Location

### The file suffix is .scf for the s-control file. The accompanying metadata file is named ScontrolName -meta.xml . Scontrol components are stored in the scontrols folder in the corresponding package directory.

Version

### Scontrols are available in API version 10.0 and later.


Metadata Types Scontrol

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`content` base64Binary Content of the s-control. Base 64-encoded binary data. Before making
an API call, client applications must encode the binary attachment

data as base64. Upon receiving a response, client applications must
decode the base64 data to binary. This conversion is handled for you
by a SOAP client. This field is inherited from the MetadataWithContent
component.

`contentSource` SControlContentSource (enumeration Required. Determines how you plan to use the s-control:
of type string)

**•** `HTML` : Select this option if you want to enter the content for your
s-control in `content` .

**•** `URL` : Select this option if you want to enter the link or URL of an
external website in `content` .

**•** `Snippet` : Snippets are s-controls that are designed to be
included in other s-controls. Select this option if you want to enter
the content for your s-control snippet in `content` .

`description` string Optional text that describes the s-control. This only displays to users
with View All Data permission (administrator).

`encodingKey` Encoding (enumeration of type string) Required. The default encoding setting is Unicode: `UTF-8` . Change
it if you’re passing information to a URL that requires data in a different

format. This option is available when you select `URL` as the value for
`contentSource` .

`fileContent` base64 File contents displayed if you add this s-control to a custom link. The
file can contain a Java applet, Active-X control, or any other type of

content you want. This option only applies to s-controls with a value
of `HTML` for `contentSource` .

`fileName` string The unique name for the s-control. This name can contain only
underscores and alphanumeric characters, and must be unique in

your org. It must begin with a letter, not include spaces, not end with
an underscore, and not contain two consecutive underscores. This
field can’t be changed for components installed by a managed
package. It’s only relevant if the `fileContent` field also has a value.
This field is available in API version 14.0.

`fullName` string The s-control developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. If this field contained characters before version 14.0 that
are no longer allowed, the characters were stripped out of this field,
and the previous value of the field was saved in the name field. This
field is inherited from the Metadata component.


### Metadata Types SearchCustomization

**Field Name** **Field Type** **Description**

`name` string

Required. The unique name for the s-control. It must contain
alphanumeric characters only and begin with a letter. For example
`example_s_control` .

`supportsCaching` boolean Required. Indicates whether the s-control supports caching ( `true` )
or not ( `false` ). Caching optimizes the page so that it remembers

which s-controls are on the page when it reloads. This option only
applies to HTML s-controls.

Declarative Metadata Sample Definition

The following sample creates the `Myriad_Publishing.scf` s-control, which creates a link to the website specified in the s-control.
The corresponding `Myriad_Publishing.scf-meta.xml` metadata file follows the s-control file.

`Myriad_Publishing.scf` file:

```
http://www.myriadpubs.com

```

`Myriad_Publishing.scf-meta.xml` :

```
<?xml version="1.0" encoding="UTF-8"?>

<Scontrol xmlns="http://soap.sforce.com/2006/04/metadata">

   <contentSource>URL</contentSource>

   <description>s-control to open Myriad Publishing website.</description>

   <encodingKey>UTF-8</encodingKey>

   <name>Myriad Publishing</name>

   <supportsCaching>true</supportsCaching>

</Scontrol>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SearchCustomization

Represents the configuration of search settings created in Search Manager. The configuration includes the search channel, searchable
objects and fields, and rules to filter search results.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types SearchCustomization

File Suffix and Directory Location

SearchCustomization components have the suffix `.searchCustomization` and are stored in the `searchCustomizations`
folder.

Version

SearchCustomization components are available in API version 61.0 and later.

Special Access Rules

Only users with the View Setup and Configuration permission can access this object, and only users with the Customize Application
permission can edit it.

Fields

**Field Name** **Description**

```
channel

masterLabel

objectOverride

objectToAlwaysSearch

profile

```

**Field Type**
string

**Description**

Required.

The search channel that the configuration applies to.

**Field Type**
string

**Description**

Required.

The name of the configuration.

**Field Type**

SearchCustomizationObjectOverride[]

**Description**
A list of object configurations.

**Field Type**
string[]

**Description**
A list of the objects that are always searched for the user profile if the search channel
is Einstein Global Search Bar.

**Field Type**
string


Metadata Types SearchCustomization

**Field Name** **Description**

**Description**
Specifies user profile if the search channel is Einstein Global Search Bar.

```
selectedObject

selectedProfile

```

**Field Type**
string[]

**Description**
A list of the objects that are selected in the configuration if the search channel is LWR
Experience Sites.

**Field Type**
string[]

**Description**
Specifies all user profiles that are associated with a Search configuration if the search
channel is Einstein Global Search Bar. This field is available in API version 62.0 and later.

SearchCustomizationObjectOverride

Represents the configuration for a specific object.

**Field Name** **Description**

```
fieldOverride

objectApiName

rule

searchable

```

**Field Type**

SearchCustomizationFieldOverride[]

**Description**
A list of field configurations.

**Field Type**
string

**Description**

Required.

The API name of the object that the configuration is applied to.

**Field Type**

SearchCustomizationRule[]

**Description**
A list of rules applied to filter search results.

**Field Type**
boolean

**Description**
Indicates whether the object is searchable ( `true` ) or not ( `false` ).


Metadata Types SearchCustomization

SearchCustomizationFieldOverride

Represents the configuration for a specific field within an object.

**Field Name** **Description**

```
fieldApiName

searchable

```

**Field Type**
string

**Description**

Required.

The API name of the field that the configuration is applied to.

**Field Type**
boolean

**Description**

Required.

Indicates whether the field is searchable ( `true` ) or not ( `false` ).

SearchCustomizationRule

Represents the rules defined in an object to filter search results.

**Field Name** **Description**

```
fieldApiName

operator

ruleValue

```

**Field Type**
string

**Description**

Required.

The field that the rule applies to.

**Field Type**
string

**Description**

Required.

The operator for the rule.

**Field Type**

SearchCustomizationRuleValue[]

**Description**
A list of rule values.


Metadata Types SearchCustomization

SearchCustomizationRuleValue

Represents the value of a rule used to filter search results.

**Field Name** **Description**

```
targetObjectApiName

value

```

**Field Type**
string

**Description**
The API name of the target object, in case the rule applies to a lookup field.

**Field Type**
string

**Description**

Required.

The value of the rule.

Declarative Metadata Sample Definition

The following is an example of a SearchCustomization component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SearchCustomization xmlns="http://soap.sforce.com/2006/04/metadata">

   <channel>GlobalSearch</channel>

   <masterLabel>My_Standard_User_Configuration</masterLabel>

   <objectOverride>

     <fieldOverride>

        <fieldApiName>Description</fieldApiName>

        <searchable>false</searchable>

     </fieldOverride>

     <fieldOverride>

        <fieldApiName>Rating</fieldApiName>

        <searchable>true</searchable>

     </fieldOverride>

     <objectApiName>Account</objectApiName>

     <rule>

        <fieldApiName>My_Custom_Field__c</fieldApiName>

        <operator>ne</operator>

        <ruleValue>

          <value>Other</value>

        </ruleValue>

     </rule>

     <rule>

        <fieldApiName>Rating</fieldApiName>

        <operator>in</operator>

        <ruleValue>

          <value>Hot</value>

        </ruleValue>

        <ruleValue>

          <value>Warm</value>

```


### Metadata Types SearchOrgWideObjectConfig

```
           </ruleValue>

        </rule>

      </objectOverride>

      <objectOverride>

        <objectApiName>Asset</objectApiName>

        <searchable>false</searchable>

      </objectOverride>

      <objectOverride>

        <objectApiName>Contact</objectApiName>

        <rule>

           <fieldApiName>AccountId</fieldApiName>

           <operator>ne</operator>

           <ruleValue>

             <targetObjectApiName>Account</targetObjectApiName>

             <value>A Company</value>

           </ruleValue>

        </rule>

        <rule>

           <fieldApiName>DoNotCall</fieldApiName>

           <operator>eq</operator>

           <ruleValue>

             <value>false</value>

           </ruleValue>

        </rule>

      </objectOverride>

      <objectToAlwaysSearch>Account</objectToAlwaysSearch>

      <objectToAlwaysSearch>Contact</objectToAlwaysSearch>

      <objectToAlwaysSearch>My_Custom_Object__c</objectToAlwaysSearch>

      <objectToAlwaysSearch>Product2</objectToAlwaysSearch>

      <profile>standard</profile>

   </SearchCustomization>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>SearchCustomization</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SearchOrgWideObjectConfig

Represents an object in the search index. The search index contains org-wide search settings created in Search Manager. Each object in
the search index includes searchable fields and fields protected by field-level security in search.


Metadata Types SearchOrgWideObjectConfig

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

SearchOrgWideObjectConfig components have the suffix `.searchOrgWideObjectConfig` and are stored in the
`searchOrgWideConfiguration` folder.

Version

SearchOrgWideObjectConfig components are available in API version 61.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
masterLabel

objectReference

searchOrgWideFieldConfig

```

**Field Type**
string

**Description**

Required.

The name of the configuration.

**Field Type**
string

**Description**

Required.

The API name of the object.

**Field Type**

SearchOrgWideFieldConfig[]

**Description**
A list of field configurations.


Metadata Types SearchOrgWideObjectConfig

SearchOrgWideFieldConfig

Represents the configuration in the search index for a field in an object.

**Field Name** **Description**

```
fieldReference

isSearchable

isSecure

```

**Field Type**
string

**Description**

Required.

The API name of the field.

**Field Type**
boolean

**Description**
Indicates if the field is searchable ( `true` ) or not ( `false` ). If `true`, the field is shown
in search results and used to match results.

**Field Type**
boolean

**Description**
Indicates if the field is protected by field-level security in search ( `true` ) or not ( `false` ).
If `true`, the search engine uses this field to match results only for users with
permissions. If `false`, the search engine uses this field to match results even if the
user doesn’t have permissions to view this field.

Declarative Metadata Sample Definition

The following is an example of a SearchOrgWideObjectConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SearchOrgWideObjectConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>CustomerLabel</masterLabel>

   <objectReference>Customer</objectReference>

   <searchOrgWideFieldConfig>

     <fieldReference>Custom_Field_1__c</fieldReference>

     <isSearchable>false</isSearchable>

     <isSecure>false</isSecure>

   </searchOrgWideFieldConfig>

   <searchOrgWideFieldConfig>

     <fieldReference>Custom_Field_2__c</fieldReference>

     <isSearchable>true</isSearchable>

     <isSecure>true</isSecure>

   </searchOrgWideFieldConfig>

</SearchOrgWideObjectConfig>

```


### Metadata Types ServiceAISetupDefinition

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>SearchOrgWideObjectConfig</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceAISetupDefinition

Represents settings for an Einstein for Service feature such as Einstein Article Recommendations. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceAISetupDefinition components have the suffix .serviceAISetupDescription and are stored in the

`serviceAISetupDescriptions` folder.

Version

### ServiceAISetupDefinition components are available in API version 51.0 and later.

Special Access Rules

This type is available only when an org is configured to access the application in the `appSourceType` field. For example, if
`appSourceType` is set to ARTICLE_RECOMMENDATION, this type is available only if Einstein Article Recommendations is enabled
in the org and the Main Services Agreement has been accepted.

Fields

**Field Name** **Field Type** **Description**

```
appSourceType

```

ApplicationSourceType Required. The target application for the configuration. Valid values are:
(enumeration of

**•** `REPLY_RECOMMENDATION` —Einstein Reply Recommendations

type string)

**•** `REPLY_RECOMMENDATION` —Einstein Reply Recommendations

**•** `ARTICLE_RECOMMENDATION` —Einstein Article
Recommendations

**•** `UTTERANCE_RECOMMENDATION` —Einstein Bot utterances


Metadata Types ServiceAISetupDefinition

**Field Name** **Field Type** **Description**

**•** `FAQ` —Einstein Bot frequently asked questions

`name` string Required. A reference to the configuration.

```
setupStatus

```

ServiceAISetupDefStatus Required. The status of the configuration. Valid values are:
(enumeration of

**•** `FIELDS_SELECTED`

type string)

**•** `FIELDS_SELECTED`

**•** `TRAINING`

`supportedLanguages` string

**•** `READY_TO_ACTIVATE`

**•** `SERVING`

**•** `RETIRED`

**•** `ARCHIVED`

**•** `READY_FOR_REVIEW`

Required when `appSourceType` is
`ARTICLE_RECOMMENDATION` . Language codes for selected and
supported languages.

Declarative Metadata Sample Definition

Here’s an example of a ServiceAISetupDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceAISetupDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <appSourceType>ARTICLE_RECOMMENDATION</appSourceType>

   <name>SA1601228426202</name>

   <setupStatus>ARCHIVED</setupStatus>

   <supportedLanguages>en,de,fr,it,es,pt,nl</supportedLanguages>

</ServiceAISetupDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ServiceAISetupDefinition</name>

   </types>

</Package>

```

Usage

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ServiceAISetupField ServiceAISetupField

Represents a field on cases or knowledge articles that Einstein uses to identify relevant articles in Einstein Article Recommendations. This
type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceAISetupField components have the suffix .serviceAiSetupField and are stored in the serviceAiSetupFields

folder.

Version

### ServiceAISetupField components are available in API version 51.0 and later.

Special Access Rules

This type is available only if Einstein Article Recommendations is enabled in your org and the Main Services Agreement has been accepted.

Fields

**Field Name** **Field Type** **Description**

`entity` string Required. The Case or KnowledgeArticle object for the field.

`field` string Required. The API name of the field.

```
fieldMappingType

```

### ServiceAISetupFieldType Required. The field type. Valid values are:

(enumeration of

**•** `CASE_DESC`

type string)

**•** `CASE_SUBJ`

`fieldPosition` int

**•** `ARTICLE_TITLE`

**•** `ARTICLE_CONTENT`

**•** `ARTICLE_SUMMARY`

Required. A positive number used to rank the field’s importance. The
value 1 is most important; higher numbers indicate less important fields.
Einstein considers fields in the order of importance.

`name` string Required. A reference to the field.

`setupDefinition` string Required. A reference to the parent ServiceAISetupDefinition.

Declarative Metadata Sample Definition

The following is an example of a ServiceAISetupField component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceAISetupField xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types ServiceChannel

```
      <entity>Case</entity>

      <field>Subject</field>

      <fieldMappingType>CASE_SUBJ</fieldMappingType>

      <fieldPosition>1</fieldPosition>

      <name>SF16039900475920</name>

      <setupDefinition>4hQRM0000004CDK</setupDefinition>

   </ServiceAISetupField>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceAISetupField</name>

      </types>

   </Package>

```

Usage

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceChannel

Represents a channel of work items that are received from your organization—for example, cases, chats, or leads.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceChannel components have the suffix .serviceChannel and are stored in the serviceChannels folder.

Version

### ServiceChannel components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`acwExtensionDuration` int The maximum length of time, measured in seconds, an agent can spend
on After Conversation Work (ACW) each time they extend the timer. You

must set this field if `hasAcwExtensionEnabled` is set to `true` .


Metadata Types ServiceChannel

**Field Name** **Field Type** **Description**

Specify a value from 10 through 3600. Available only for service channels
of type Messaging or Voice.

`afterConvoMaxTime` int The maximum length of time, measured in seconds, an agent has to
complete After Conversation Work (ACW). You must set this field if

`hasAfterConvoWorkTimer` is set to `true` . Specify a value from
10 through 3600. Available only for service channels of type Messaging
or Voice.

For service channels of type Voice, this field is available in API version
52.0 and later. For service channels of type Messaging, this field is
available in API version 56.0 and later.

`capacityModel` picklist The method that determines when an agent's capacity for a work item
is released. With the status-based capacity routing model, work remains

assigned and applied to an agent’s capacity until the work is completed
or reassigned to a different agent. In contrast, the tab-based capacity
routing model releases an agent’s capacity when a work tab is closed in
the service console. This field is available in API version 65.0 and later.

Values are:

**•** `STATUS_BASED`

**•** `TAB_BASED`

`doesCheckCapOnOwnerChange` boolean Indicates whether the override for capacity check is on (true) or not
(false). If it is on, when work is reassigned to another agent it overrides

it and keeps the work assigned to the specific agent. The default value
is false.This field is available in API version 65.0 and later.

`doesCheckCapOnStatusChange` boolean Indicates whether the override for capacity check is on (true) or not
(false). If it is on, when work is reopened it is re-assigned to a specific

agent. The default value is false. This field is available in API version 65.0
and later.

`doesMinimizeWidgetOnAccept` boolean Automatically minimizes the Omni-Channel widget when an agent
accepts work. This field is available in API version 48.0 and later.

`hasAcwExtensionEnabled` boolean If set to `true`, agents can extend their After Conversation Work (ACW)
time. Available only if `hasAfterConvoWorkTimer` is set to `true` .

If set to `true`, you must also set the `acwExtensionDuration`
and `maxExtensions` fields. The default value is `false` . Available
only for service channels of type Messaging or Voice. This field is available
in API version 56.0 and later.

`hasAfterConvoWorkTimer` boolean If set to `true`, After Conversation Work (ACW) time can be configured
for the channel. If set to `true`, you must also set the

`afterConvoWorkMaxTime` field. The default value is `false` .
Available only for service channels of type Messaging or Voice.


Metadata Types ServiceChannel

**Field Name** **Field Type** **Description**

For service channels of type Voice, this field is available in API version
52.0 and later. For service channels of type messaging, this field is
available in API version 56.0 and later.

`hasAutoAcceptEnabled` boolean Work items in a service channel open automatically in the agent’s
workspace so that the agent doesn’t have to manually accept them.

`interactionComponent` string The custom console component to open in the footer when an agent
accepts a work item from this service channel.

`isInterruptible` boolean

Indicates whether a work item consumes interruptible or primary
capacity. The default value is false. Available in API version 57.0 and later
when the Interruptible Capacity feature is enabled.

`label` string Required. The label of the service channel.

`maxExtensions` picklist The maximum number of times an agent can extend their After Work
Conversation (ACW) time. Specify a value from 1 through 10. You must

set this field if `hasAcwExtensionEnabled` is set to `true` .
Available only for service channels of type Messaging or Voice. This field
is available in API version 56.0 and later.

`relatedEntityType` string Required. The type of object that’s associated with this service channel.

`secondaryRoutingPriorityField` string

`serviceChannelStatusFieldMappings` ServiceChannelFieldPriority

The name of the standard field or the ID of the custom field that is used
for secondary routing priority. This field is available in API version 47.0
and later.

Represents the value to indicate completed and in-progress work item
status in the Status-Based Capacity routing model. This field is available
in API version 65.0 and later.

`serviceChannelFieldPriorities` ServiceChannelFieldPriority[] Required. A set of mappings between secondary routing priority field
values and priorities. This field is available in API version 47.0 and later.

`statusField` picklist The field that you use to track work status in the Status-Based capacity
routing model. Use `ServiceChannelStatusField` to specify

the values that indicate completed and in-progress work-item status.
This field is available in API version 65.0 and later.

ServiceChannelFieldPriority

Represents a secondary routing priority field value mapping. Available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`priority` int Required. The priority number assigned to the mapped field value.

`type` picklist Required. The work item status assigned to the mapped field value.
Possible types are `IN_PROGRESS`, `PAUSED`, `COMPLETED` .

`value` string Required. The value of Status Field defined in the parent ServiceChannel.


### Metadata Types ServicePresenceStatus

**Field Name** **Field Type** **Description**

`value` string Required. The value of the secondaryRoutingPriorityField field defined
in the parent ServiceChannel.

Declarative Metadata Sample Definition

The following is an example of a ServiceChannel component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServiceChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesMinimizeWidgetOnAccept>true</doesMinimizeWidgetOnAccept>

      <interactionComponent>ConsoleComponent</interactionComponent>

      <label>Case</label>

      <relatedEntityType>Case</relatedEntityType>

      <secondaryRoutingPriorityField>Status</secondaryRoutingPriorityField>

      <serviceChannelFieldPriorities>

        <priority>1</priority>

        <value>Escalated</value>

      </serviceChannelFieldPriorities>

      <serviceChannelFieldPriorities>

        <priority>2</priority>

        <value>On Hold</value>

      </serviceChannelFieldPriorities>

   </ServiceChannel>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceChannel</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServicePresenceStatus

Represents a presence status that can be assigned to a service channel. This type extends the Metadata metadata type and inherits its
`fullName` field.


Metadata Types ServicePresenceStatus

File Suffix and Directory Location

ServicePresenceStatus components have the suffix `.servicePresenceStatus` and are stored in the
`servicePresenceStatuses` folder.

Version

ServicePresenceStatus components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`channels` ServiceChannelStatus Represents the status that’s associated with a specific service channel.

`label` string The label of the presence status.

ServiceChannelStatus

Represents the status that’s associated with a specific service channel.

**Field Name** **Field Type** **Description**

`channel` string Represents the channels assigned to the presence status.

Declarative Metadata Sample Definition

The following is an example of a ServicePresenceStatus component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServicePresenceStatus xmlns="http://soap.sforce.com/2006/04/metadata">

      <channels>

        <channel>Case</channel>

      </channels>

      <label>Available for Cases</label>

   </ServicePresenceStatus>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServicePresenceStatus</name>

      </types>

```


### Metadata Types ServiceProcess

```
      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceProcess

Represents a process created in Service Process Studio and its associated attributes.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceProcess components have the suffix .serviceprocess and are stored in the .serviceprocess folder.

Version

### ServiceProcess components are available in API version 57.0 and later.

Special Access Rules

Access to the ServiceProcess type requires the AccessToServiceProcess permission.

Fields

**Field Name** **Description**

```
description

processLabel

```

**Field Type**
string

**Description**
A meaningful explanation of the service process.

**Field Type**
string

**Description**

Required.

A meaningful name for the service process.


Metadata Types ServiceProcess

**Field Name** **Description**

```
serviceProcessAttributes

serviceProcessDependencies

serviceProcessItemGroups

shortDescription

usageType

```

ServiceProcessAttribute

**Field Type**

ServiceProcessAttribute[]

**Description**
Custom attributes that store the data associated with the service process.

**Field Type**

ServiceProcessDependency[]

**Description**
Dependent components of the service process, such as OmniScripts or flows.

**Field Type**

ServiceProcessItemGroup[]

**Description**
Groups of related ServiceProcessAttribute records.

**Field Type**
string

**Description**
A brief meaningful explanation of the service process.

**Field Type**
SvcCatalogItemUsageType (enumeration of type string)

**Description**

Required.

The Cloud that uses this service process.

Values are:

**•** `CustomerService`

**•** `Employee`

**•** `FinancialServices`

**•** `Industry (available in version 58.0 and later)`

A custom attribute that stores data associated with a service process. For example, a service process that reverses a fee can have a Fee
Type attribute.

**Field Name** **Description**

```
attributeType

```

**Field Type**
SvcCtlgItemAttrAttributeType (enumeration of type string)


Metadata Types ServiceProcess

**Field Name** **Description**

**Description**
A `Base` attribute corresponds to a SvcCatalogRequest field, which is subject to
field-level security. An `Extended` attribute is only a ServiceProcessAttribute object
record, which isn't subject to field-level security.

Values are:

**•** `Base`

**•** `Extended`

The default is `Extended` .

```
dataType

```

**Field Type**
SvcCatalogItemAttrDataType (enumeration of type string)

**Description**
The data type of the attribute.

Values are:

**•** `Attachment`

**•** `Checkbox`

**•** `Currency`

**•** `Date`

**•** `Datetime`

**•** `DisplayText`

**•** `Email`

**•** `IPAddress`

**•** `Integer`

**•** `ListOfAttachment` (available in API version 65.0 and later)

**•** `ListOfBoolean`

**•** `ListOfDouble`

**•** `ListOfInteger`

**•** `ListOfMaps`

**•** `ListOfString`

**•** `Lookup`

**•** `Map`

**•** `MultilineText`

**•** `MultiSelectPicklist` (available in API version 65.0 and later)

**•** `Number`

**•** `NumericScale`

**•** `Password` (available in API version 65.0 and later)

**•** `Percentage`

**•** `Picklist`


Metadata Types ServiceProcess

**Field Name** **Description**

**•** `Queue`

**•** `RadioButton` (available in API version 65.0 and later)

**•** `SingleCheckbox` (available in API version 59.0 and later)

**•** `SinglelineText`

**•** `Text`

**•** `Toggle` (available in API version 59.0 and later)

**•** `Url`

The default is `Text` .

Note: Selecting `Currency` doesn't cause an error, but currency conversions
aren't supported.

```
description

developerName

fieldIdentifier

groupApiName

inputVariableValue

isRequired

```

**Field Type**
string

**Description**
A meaningful explanation of the attribute.

**Field Type**
string

**Description**

Required.

A system name for the attribute.

**Field Type**
string

**Description**
For a `Base` attribute, the Developer Name of the SvcCatalogRequest field. This field
can be standard or custom.

**Field Type**
string

**Description**
The `apiName` of the ServiceProcessItemGroup to which this attribute belongs.

**Field Type**
string

**Description**
The default value of the attribute.

**Field Type**
boolean


Metadata Types ServiceProcess

**Field Name** **Description**

**Description**
Specifies whether the attribute is required. The default is `false` .

```
label

parentAttribute

sortOrder

```

**Field Type**
string

**Description**

Required.

A meaningful name for the attribute.

**Field Type**
string

**Description**
The parent attribute of this attribute. For example, a Latitude attribute can have
GeoLocation as a parent.

**Field Type**
int

**Description**
The position of the attribute in the payload relative to other attributes having no parent
or the same parent.

ServiceProcessDependency

A dependent component of the service process, which can be a flow, an OmniScript, an Integration Definition, or a preprocessor Apex
class.

**Field Name** **Description**

```
dependencyReference

processStepName

```

**Field Type**
string

**Description**

Required.

The Developer Name of the flow, OmniScript, Integration Definition, or preprocessor
Apex class.

**Field Type**
SvcCtlgItemDpndProcType (enumeration of type string)

**Description**
Name of the step in a service process.

Values are:

**•** `FulfillmentFlow`


Metadata Types ServiceProcess

**Field Name** **Description**

**•** `IntegrationDefinition`

**•** `Preprocessor`

**•** `RequestForm`

```
type

```

**Field Type**
SvcCatalogItemDependencyType (enumeration of type string)

**Description**

Required.

The type of dependent component.

Values are:

**•** `FlowDefinition`

**•** `IntegrationProviderDef`

**•** `OmniScriptConfig`

**•** `PreprocessorApexClass`

ServiceProcessItemGroup

A group of related ServiceProcessAttribute records.

**Field Name** **Description**

```
apiName

groupName

sortOrder

```

**Field Type**
string

**Description**

Required.

The API Name of the group.

**Field Type**
string

**Description**

Required.

The name of the group.

**Field Type**
int

**Description**

Required.

The group display order.


Metadata Types ServiceProcess

Declarative Metadata Sample Definition

The following is an example of a ServiceProcess component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServiceProcess xmlns="http://soap.sforce.com/2006/04/metadata">

     <processLabel>EmailUpdate</processLabel>

     <usageType>FinancialServices</usageType>

     <serviceProcessAttributes>

       <label>EmailAddress</label>

       <developerName>EmailAddress</developerName>

       <dataType>Text</dataType>

       <groupApiName>Info</groupApiName>

     </serviceProcessAttributes>

     <serviceProcessDependencies>

       <dependencyReference>EmailPreprocessor</dependencyReference>

       <type>PreprocessorApexClass</type>

     </serviceProcessDependencies>

     <serviceProcessItemGroups>

        <apiName>Info</apiName>

        <groupName>Info</groupName>

        <sortOrder>1</sortOrder>

      </serviceProcessItemGroups>

   </ServiceProcess>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceProcess</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage Type

We recommend that you review these considerations before you retrieve or deploy service process metadata.

**•** If you deploy metadata with the same name as the definition when your service process definition is active, you get an error message.
Deactivate the service process definition and try again.

**•** When your service process definition is inactive, consider these guidelines.

**–** If a service process definition contains service catalog requests and service catalog request extended attribute values and you
deploy metadata with the same name as the definition, you get an error message. You can’t delete or change a service process
that has service catalog requests with attribute values in it. Make sure that all records are deleted in service catalog requests and
service catalog request extended attribute values before you deploy the metadata.


### Metadata Types Settings

**–** If a service process definition contains service catalog requests but doesn’t contain service catalog request extended attribute
values and you deploy the metadata with the same name, the deployment works as expected.

**–** If a service process definition doesn’t contain service catalog requests and you deploy the metadata with the same name, the
deployment works as expected.

### Settings

Represents the organization settings related to a feature. For example, your password policies, session settings and network access
controls are all available in the SecuritySettings component type.

Not all feature settings are available in the Metadata API. See Unsupported Metadata Types on page 171 for information on which feature
settings are not available.

### Settings can be accessed using the specific component member or via wildcard. For example, in the package manifest file you would

use the following section to access SecuritySettings:

```
      <types>

        <members>Security</members>

        <name>Settings</name>

      </types>

```

The member format when used in the package manifest is the component metadata type name without the “Settings” suffix, so in the
preceding example “Security” is used instead of “SecuritySettings”.

File Suffix and Directory Location

Each settings component gets stored in a single file in the `settings` directory of the corresponding package directory. The filename
uses the format _`Setting feature`_ `.settings` . For example, the SecuritySettings file would be `Security.settings` . See
“File Suffix and Directory Location” information for the individual settings components to determine the exact filename.

Version

### Settings is available in API version 27.0 and later. See the version information for the individual setting component to determine which

API version the settings component became available.

Declarative Metadata Sample Definition

The following is an example package manifest used to deploy or retrieve only the MobileSettings for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Mobile</members>

        <name>Settings</name>

      </types>

      <version>27.0</version>

   </Package>

```


Metadata Types Settings

The following is an example package manifest used to deploy or retrieve all the available settings metadata for an organization, using
a wildcard:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>Settings</name>

      </types>

      <version>27.0</version>

   </Package>

```

AccountPlanSettings
Represents an org’s account plan settings. These settings control features that make it easy for sales reps to set objectives with
actionable metrics and to store account research and analysis.

AccountSettings
Represents an org’s account settings for account teams, account owner report, and the **View Hierarchy** link.

AccountInsightsSettings
Represents an org’s Einstein Account Insights settings. This setting controls features that help your reps maintain their relationships
with their customers.

AccountIntelligenceSettings
Represents an org’s Account Intelligence settings. These settings control features that make it easy for sales reps to create accounts,
see relevant news articles, and add logos to account records. This type extends the Metadata metadata type and inherits its
`fullName` field.

AccountingSettings
Represents the settings for the Accounting Subledger feature.

ActionsSettings
Represents an org’s actions settings for default quick actions, multi-dimensional publisher, and third-party actions. This type extends
the Metadata metadata type and inherits its `fullName` field.

ActivitiesSettings
Represents an org's activity settings, and its user interface settings for the calendar. This type extends the Metadata metadata type
and inherits its `fullName` field.

AddressSettings
Represents the configuration of country/territory and state picklists. Use the AddressSettings component type to configure state
and country/territory data in your organization so that you can convert text-based values into standard picklist values. To convert
your state and country/territory values, from Setup, enter _`State and Country/Territory Picklists`_ in the Quick
Find box, then select **State and Country/Territory Picklists** .

AIReplyRecommendationsSettings
Represents the metadata used to manage settings for Einstein Reply Recommendations. This type extends the Metadata metadata
type and inherits its `fullName` field.

AgentPlatformSettings
Represents settings for Agentforce.

AgentforceAccountManagementSettings
Represents an org’s Agentforce Account Management settings.


Metadata Types Settings

AgentforceForDevelopersSettings
Represents Agentforce for Developers settings.

AnalyticsSettings
Represents Analytics settings in Salesforce. CRM Analytics lets you explore all your data quickly and easily by providing AI-powered
advanced Analytics right inside Salesforce. Manage your datasets, query data with Salesforce Analytics Query Language (SAQL), and
customize dashboards. You can use these settings to configure which Analytics features are available to users in your organization.

ApexSettings
Represents Apex-related org settings. This type extends the Metadata metadata type and inherits its `fullName` field.

AppAnalyticsSettings
Represents settings to retrieve AppExchange App Analytics usage data.

AppExperienceSettings
Represents settings for the app experience.This type extends the Metadata metadata type and inherits its `fullName` field.

AssociationEngineSettings
Represents the record association builder settings for an org. This type extends the Metadata metadata type and inherits its
`fullName` field.

AutomatedContactsSettings
Represents an org’s Einstein Automated Contacts settings. These settings let you find new contacts and opportunity contact roles.
This type extends the Metadata metadata type and inherits its `fullName` field.

BotSettings
Represents an organization’s Einstein Bot settings, such as whether or not Einstein Bots is enabled. This type extends the Metadata
metadata type and inherits its `fullName` field.

BranchManagementSettings
Represents the branch management settings for an org. This type extends the Metadata metadata type and inherits its `fullName`
field.

BusinessHoursSettings
Represents the metadata used to manage settings for business hours and holidays in entitlements, entitlement templates, campaigns,
and cases. This type extends the Metadata metadata type and inherits its `fullName` field.

CampaignSettings
Represents an org’s Campaign Influence, Einstein Attribution, Einstein Key Accounts, and campaign member settings. These features
help you understand how your campaigns and accounts are affecting your opportunity pipeline.

CaseSettings
Represents an organization’s case settings, such as the default case owner, which case-related features are enabled, and which
Classic email templates are used for various case activities. This type extends the Metadata metadata type and inherits its `fullName`
field.

ChatterAnswersSettings
Represents the metadata used to manage settings for Chatter Answers.

ChatterEmailsMDSettings
Represents an org’s settings for Chatter email when Chatter is enabled. This type extends the Metadata metadata type and inherits
its `fullName` field.

ChatterSettings
Represents an org’s settings for their Chatter instance when Chatter is enabled for the org. This type extends the Metadata metadata
type and inherits its `fullName` field.


Metadata Types Settings

CodeBuilderSettings
Represents Code Builder settings. This type extends the Metadata metadata type and inherits its `fullName` field.

CollectionsDashboardSettings
Represents an org’s settings to add the Collections Dashboard application to an org.

CommunitiesSettings
Represents community settings for an org. Enable digital experiences and workspaces. Manage moderation, guest user and partner
settings, and more. This type extends the Metadata metadata type and inherits its `fullName` field.

CompanySettings
Represents global settings that affect multiple features in your organization. This type extends the Metadata metadata type and
inherits its `fullName` field.

ConnectedAppSettings
Represents settings for connected apps. This type extends the Metadata metadata type and inherits its `fullName` field.

ContentSettings
Represents content settings for an org. This type extends the Metadata metadata type and inherits its `fullName` field.

ContractSettings
Represents contract settings.

ConversationalIntelligenceSettings
Represents the org's Einstein Conversation Insights settings, such as whether Einstein Conversation Insights is enabled. Einstein
Conversation Insights lets you analyze your rep's call recordings, and gives you the insights you need to optimize every call.

ConversationChannelDefinition
Represents the conversation channel definition that’s implemented for Interaction Service for Bring Your Own Channel for Messaging
and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

CurrencySettings
Represents an organization’s currency settings, including supporting multiple currencies and currency effective dates. This type
extends the Metadata metadata type and inherits its `fullName` field.

CustomAddressFieldSettings
Represents the settings for custom address fields.

DataDotComSettings
Represents the org's Data.com settings. This type extends the Metadata metadata type and inherits its `fullName` field.

DataImportManagementSettings
Represents an org's contact and leads import settings.

DeploymentSettings
Represents the settings affecting how deployments behave in the org. This type extends the Metadata metadata type and inherits
its `fullName` field.

DevHubSettings
Represents Dev Hub settings.

DocumentGenerationSetting
Represents an org's settings for automatic document generation from templates. This type extends the Metadata metadata type
and inherits its `fullName` field.

DynamicFormsSettings
Represents the settings related to Dynamic Forms.


Metadata Types Settings

EACSettings
Represents the Einstein Activity Capture metadata type. Use Einstein Activity Capture to add emails and events from your Microsoft
or Google account to the activity timeline of related Salesforce records. Automatically sync contact and event data between your
Microsoft or Google account and Salesforce. This type extends the Metadata metadata type and inherits its `fullName` field.

EinsteinAISettings
Represents Einstein AI settings, including AI feedback integration with Data 360 and PII masking for AI trust features.

EinsteinAgentSettings
Represents settings for Einstein classification apps, Einstein Case Classification and Einstein Case Wrap-Up, in an org. This type
extends the Metadata metadata type and inherits its `fullName` field.

EinsteinGptSettings
Represents settings for Einstein Generative AI features in an org. This type extends the Metadata metadata type and inherits its
`fullName` field

EmailAdministrationSettings
Represents an organization’s email administration settings, including email deliverability, security compliance, relay configurations,
and system notifications. This type extends the Metadata metadata type and inherits its `fullName` field.

EmailAuthorizationSettings
Represents your org’s email authorization settings. This type extends the MetadataForSettings metadata type and inherits its
`fullName` field.

EmailIntegrationSettings
Represents an org’s settings for the Outlook integration, Gmail integration, and Salesforce Inbox. This type extends the Metadata
metadata type and inherits its `fullName` field.

EmailTemplateSettings
Represents an org’s email template settings. This type extends the Metadata metadata type and inherits its `fullName` field.

EmployeeUserSettings
Represents the employee-user settings used for automatically creating or syncing employee and user data in work.com orgs. This
type extends the Metadata metadata type and inherits its `fullName` field.

EnhancedNotesSettings
Represents an org’s enhanced note settings, such as enabling enhanced notes and enabling tasks in enhanced notes.This type
extends the Metadata metadata type and inherits its `fullName` field.

EncryptionKeySettings
Represents an org’s encryption key settings, such as customer-supplied keys options and key derivation settings. This type extends
the Metadata metadata type and inherits its `fullName` field.

EntitlementSettings
Represents an organization’s entitlement settings.

EventSettings
Represents an org's platform event settings for Event Monitoring.

ExperienceBundleSettings
Represents the org setting that enables the ExperienceBundle metadata type for Aura sites in Experience Cloud. The setting doesn’t
affect LWR sites, which use ExperienceBundle by default. This type extends the Metadata metadata type and inherits its `fullName`
field.

ExternalClientAppSettings
Represents settings to enable external client app features.


Metadata Types Settings

ExternalServicesSettings
Represents settings for an External Services registration.

FieldServiceSettings
Represents an organization’s Field Service settings.

FilesConnectSettings
Represents the settings that modify the Files Connect feature.This type extends the Metadata metadata type and inherits its
`fullName` field.

FileUploadAndDownloadSecuritySettings
Represents the security settings for uploading and downloading files. This type extends the Metadata metadata type and inherits
its `fullName` field.

FlowSettings
Represents the Salesforce settings for processes and flows, such as whether Lightning runtime for flows is enabled.

ForecastingObjectListSettings
Represents an org’s forecasting object list settings. Use these settings to control which object types and field types appear in the list
of object details on the forecasts page. For example, pipeline forecasts use the Opportunity object, and the object list settings specify
which fields from that object are available in the opportunity list section of the forecasts page. This type extends the Metadata
metadata type and inherits its `fullName` field.

ForecastingSettings
Represents the Forecasts settings options. This type extends the Metadata metadata type and inherits its `fullName` field.

HighVelocitySalesSettings
Represents an org’s Sales Engagement settings. With Sales Engagement, you can make your inside sales team as effective as possible.

IdeasSettings
Represents the metadata used to manage settings for Ideas.

IdentityProviderSettings
Represents the settings used to enable or disable Salesforce as a SAML identity provider for single sign-on (SSO).

IframeWhiteListUrlSettings
Represents settings related to the list of trusted external domains that you allow to frame your Visualforce pages or surveys. This
type extends the Metadata metadata type and inherits its `fullName` field.

IncidentMgmtSettings
Represents settings for Customer Service Incident Management and Broadcast Communications.

IndustriesEinsteinFeatureSettings
Represents the settings for enabling the Industries Einstein feature.

IndustriesLoyaltySettings
Represents the settings to enable capabilities of Loyalty Management.

IndustriesSettings
Represents settings for industries verticals such as Financial Services Cloud, Consumer Goods Cloud, Public Sector Solutions, Education
Cloud, Salesforce Scheduler, Life Sciences Cloud, and Health Cloud.

InterestTaggingSettings
Represents settings for Interest Tags, which your users can add to client records to capture client needs, interests, and prospecting
opportunities.


Metadata Types Settings

InventorySettings
Represents options for the Salesforce Omnichannel Inventory product.This type extends the Metadata metadata type and inherits
its `fullName` field.

InvLatePymntRiskCalcSettings
Represents the org’s settings to identify the level of risks associated with payment of invoices.

InvocableActionSettings
Represents the org’s invocable action settings, such as whether partial save is allowed.This type extends the Metadata metadata
type and inherits its `fullName` field.

KnowledgeSettings
Represents the metadata used to manage settings for Salesforce Knowledge.

LanguageSettings
Represents an organization’s language settings. Language settings control end-user language selection, locale formats, and translation
options. This type extends the Metadata metadata type and inherits its `fullName` field.

LeadConfigSettings
Represents configuration settings for Leads that control how they are converted and displayed, and what actions are available. This
type extends the Metadata metadata type and inherits its `fullName` field.

LeadConvertSettings
Represents an organization’s custom field mappings for lead conversion. Custom fields can be mapped from Leads to Accounts,
Contacts, and Opportunities. Options for creating opportunities during lead conversion can also be specified. This type extends the
Metadata metadata type and inherits its `fullName` field.

LiveAgentSettings
Represents an organization’s Chat settings, such as whether Chat is enabled. This type extends the Metadata metadata type and
inherits its `fullName` field.

LightningExperienceSettings
Represents the settings that modify an org’s Lightning Experience configuration. This type extends the Metadata metadata type and
inherits its `fullName` field.

LiveMessageSettings
Represents an org’s LiveMessage settings.

MacroSettings
Represents an organization’s Macro settings, such as whether or not folders is enabled. This type extends the Metadata metadata
type and inherits its `fullName` field.

MailMergeSettings
Represents the settings for Extended Mail Merge functionality.

MapAndLocationSettings
Represents an org’s map and location settings.

MeetingsSettings
Represents the settings to enable Salesforce Meetings and the integration with Zoom video conferencing.

MobileSettings
Represents an organization’s mobile settings. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Settings

MyDomainSettings
Represents your org’s My Domain settings. With My Domain, you can include your company name in your URLs, for example,
`https://yourcompanyname.my.salesforce.com` . This type extends the Metadata metadata type and inherits its
`fullName` field.

MfgServiceConsoleSettings
Represents the settings to access the Service Console for Manufacturing.

NameSettings
Enables or disables the formal name, middle name, and suffix attributes for these person objects: Contact, Lead, Person Account,
and User. This type extends the Metadata metadata type and inherits its `fullName` field.

NotificationsSettings
Represents an organization’s mobile settings.

OauthOidcSettings
Represents org settings for disabling OAuth OpenID Connect authorization flows.

ObjectHierarchyRelationship
Represents an organization’s custom field mappings for sales agreement conversion. Fields can be mapped from Opportunity and
Quotes to SalesAgreement and SalesAgreementProduct.

ObjectLinkingSettings (Beta)
Represents the channel-object linking settings for an org. This type extends the Metadata metadata type and inherits its `fullName`
field.

OmniChannelSettings
Represents the Omni-Channel settings for an org.

OpportunityInsightsSettings
Represents an org’s Einstein Opportunity Insights settings. This setting controls features that give you relevant updates about your
opportunities.

OpportunitySettings
Represents org preferences for features such as automatic opportunity updates and similar-opportunity filters.

OpportunityScoreSettings
Represents an org’s Einstein Opportunity Scoring settings, such as whether or not Einstein Opportunity Scoring is enabled. Einstein
Opportunity Scoring helps determine the likelihood of an opportunity being won. This type extends the Metadata metadata type
and inherits its `fullName` field.

OrderManagementSettings
Represents options for the Salesforce Order Management product. This type extends the Metadata metadata type and inherits its
`fullName` field.

OrderSettings
Represents order settings.

OrgPreferenceSettings
Removed in API version 48.0. Represents the unique org preference settings in a Salesforce org.

OrgSettings
Represents the settings for org-wide functionality that isn’t associated with any specific feature.This type extends the Metadata
metadata type and inherits its `fullName` field.


Metadata Types Settings

PartyDataModelSettings
Represents an organization’s party data model settings, including options around the Individual object and consent enablement.
This type extends the Metadata metadata type and inherits its `fullName` field.

PardotSettings
Represents Marketing Cloud Account Engagement settings in your Salesforce org. Account Engagement, formerly known as Pardot,
is a B2B marketing automation solution that helps you create meaningful connections, generate more pipeline, and close more
deals. Use these settings to configure how Account Engagement collects and displays data.

PardotEinsteinSettings
Represents PardotEinsteinSettings. Use these settings to learn what factors drive your campaign performance, and get the best
possible engagement score for your prospects. This type extends the Metadata metadata type and inherits its `fullName` field.

PathAssistantSettings
Represents the Path preference setting. This type extends the Metadata metadata type and inherits its `fullName` field.

PaymentsSettings
Represents the Salesforce Payments settings when this feature is enabled for the org.

PicklistSettings
Represents an org’s picklist settings. These settings control the behavior of a picklist. This type extends the Metadata metadata type
and inherits its `fullName` field.

PlatformEncryptionSettings
Represents an org’s Platform Encryption settings, such as settings for available encryption schemes, permissions, encryption policy
access, and which fields can be encrypted. This type extends the Metadata metadata type and inherits its `fullName` field.

PlatformEventSettings
Represents settings for platform events and change data capture events.

PredictionBuilderSettings
Represents the settings that determine how a user can interact with Einstein Prediction Builder. This type extends the Metadata
metadata type and inherits its `fullName` field.

PrivacySettings
Represents an organization’s settings for data privacy and consent management. This type extends the Metadata metadata type
and inherits its `fullName` field.

ProcessFlowMigration
Represents a process's migrated criteria and the resulting migrated flow.

ProductSettings
Represents organization preferences for quantity schedules, revenue schedules, and active flag interaction with prices. This type
extends the Metadata metadata type and inherits its `fullName` field.

QuoteSettings
Represents an org’s quotes settings, such as enabling quotes or creating quotes without an associated opportunity. This type extends
the Metadata metadata type and inherits its `fullName` field.

RealTimeEventSettings
Represents the list of Real-Time Event entities that you want to enable or disable. This type extends the Metadata metadata type
and inherits its `fullName` field.

RecordPageSettings
Represents an org’s record page settings. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Settings

RetailExecutionSettings
Represents settings to manage your inventory, promotions, planograms, and in-store activities.

SalesAgreementSettings
Represents settings that control the display of agreement terms metrics in sales agreements and the calculation of the actual quantity
of products in sales agreements. These settings also control the approval of sales agreements.

SandboxSettings
Represents Sandbox settings. This type extends the Metadata metadata type and inherits its `fullName` field.

SchemaSettings
Represents an org’s schema settings, which manage the availability of custom settings and custom metadata type values. This type
extends the Metadata metadata type and inherits its `fullName` field.

SearchSettings
Represents an org's search settings.

SecuritySettings
Represents an org’s security settings. For example, settings define trusted IP ranges for network access, password and login
requirements, session expiration, and single sign-on settings.

ServiceCloudVoiceSettings
Represents an organization’s Service Cloud Voice settings.

ServiceSetupAssistantSettings
Represents an organization’s Service Setup Assistant settings. The Service Setup Assistant can be used to set up a basic service
console app.

SharingSettings
Represents an organization’s sharing, visibility, and data access settings. This type extends the Metadata metadata type and inherits
its `fullName` field.

SiteSettings
[Represents the settings for Experience Cloud sites and for Salesforce Sites.](https://help.salesforce.com/articleView?id=sites_overview.htm&type=5&language=en_US)

SocialCustomerServiceSettings
Represents Social Customer Service settings such as how to format inbound content from social posts to cases. This type extends
the Metadata metadata type and inherits its `fullName` field.

SocialProfileSettings
Represents org preferences for social media features such as enabling Twitter and Facebook.Represents org preferences for social
media features such as enabling Twitter and Facebook. This type extends the Metadata metadata type and inherits the fullName
field.

SourceTrackingSettings (Beta)
Represents settings for source tracking, so that changes you make in your Developer and Developer Pro sandboxes or local workspace
can be tracked. This type extends the Metadata metadata type and inherits its `fullName` field.

SubscriptionManagementSettings
Represents the settings used to manage recurring subscriptions.

SurveySettings
Represents an org’s survey settings. Use the SurveySettings component to enable Salesforce Surveys, enable Customer Lifecycle
Maps, and choose whether the owner of a survey can manage the responses.


#### Metadata Types AccountPlanSettings

Territory2Settings
Represents an org’s Territory2 settings. Use Territory2 settings to set the access level that Sales Territories users have to records
associated with sales territories, and to enable features. The standard record access settings apply to accounts and opportunities.
With _`Private`_ default internal access for contacts or cases, you can also set access for those records.

TrailheadSettings
Represents an org’s integration with Trailhead for Learning Paths or Enablement programs, including access to enablement sites
(formerly myTrailhead).

TrialOrgSettings
Represents the settings in a trial user’s org. This type extends the Metadata metadata type and inherits its `fullName` field.

UserEngagementSettings
Represents the metadata associated with various feature settings around Lightning Experience transition and adoption, user
engagement and adoption assistance, and adoption apps.

UserInterfaceSettings
Represents the settings that modify the behavior of the org’s user interface.

UserManagementSettings
Represents a selection of user management options that appear on the User Management Settings Setup page. This type extends
the Metadata metadata type and inherits its `fullName` field.

VoiceSettings
Represents an org’s Sales Dialer settings, such as call recording, conferencing, and voicemail.

WarrantyLifeCycleMgmtSettings
Represents settings that control the Warranty Administration for your org.

WorkDotComSettings
Represents WorkDotCom settings. This type extends the Metadata metadata type and inherits its `fullName` field.

WorkforceEngagementSettings
Represents settings for Workforce Engagement Management.

#### AccountPlanSettings

Represents an org’s account plan settings. These settings control features that make it easy for sales reps to set objectives with actionable
metrics and to store account research and analysis.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### AccountPlanSettings values are stored in the AccountPlan.settings file in the settings folder. The .settings

files are different from other named components, because there is only one settings file for each settings component.

Version

#### AccountPlanSettings components are available in API version 63.0 and later.


#### Metadata Types AccountSettings

Fields

**Field Name** **Description**

```
enableAccountPlan

```

**Field Type**
boolean

**Description**
Indicates whether Account Plans is enabled `(true)` or not `(false)` . The default
value is false.

Declarative Metadata Sample Definition

The following is an example of an AccountPlanSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountPlanSettings xmlns="http://soap.sforce.com/2006/04/metadata">

 <enableAccountPlan>true</enableAccountPlan>

</AccountPlanSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

      <members>AccountPlan</members>

      <name>Settings</name>

   </types>

   <version>63.0</version>

</Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### AccountSettings

Represents an org’s account settings for account teams, account owner report, and the **View Hierarchy** link.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### AccountSettings values are stored in the Account.settings file in the settings folder. The .settings files are different

from other named components because there’s only one settings file for each settings component.


Metadata Types AccountSettings

Version

AccountSettings is available in API versions 29.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableAccountDiscovery` boolean When `true`, sets up Einstein Account Management dashboards and
installs the related CRM Analytics and Customer Insights apps. The

dashboards give users access to account health analytics including
metrics on open pipeline, risk, and engagement scores.

Einstein Account Management is part of Revenue Intelligence, which is
available for an additional cost.

Available in API version 57.0 and later.

`enableAccountHistoryTracking` boolean Indicates whether history tracking is enabled for accounts ( `true` ) or
not ( `false` ). The default value is `false` . If history tracking is disabled,

the History related list is removed from account page layouts. However,
history data is still available for reporting up to the date and time when
tracking was disabled. Available in API version 47.0 and later.

`enableAccountInsightsInMobile` boolean Deprecated in API version 59.0 and later because the feature is no longer
available. Indicates whether users can see Einstein Account Insights on

their mobile device ( `true` ) or not ( `false` ). Insights appear in the
Einstein Insights component, which is on account records and the Home
page.

To use this feature, users must have the Einstein Account Insights
permission.

Available in API version 47.0 to 58.0.

`enableAccountOwnerReport` boolean Indicates whether the Account Owner Report can ( `true` ) or can’t
( `false` ) be run by all users.

`enableAccountTeams` boolean

Indicates whether account teams are enabled ( `true` ) or not ( `false` ).

The Metadata API can’t be used to disable account teams.

`enableContactHistoryTracking` boolean Indicates whether history tracking is enabled for contacts ( `true` ) or not
( `false` ). Available in API version 46.0 and later.

`enableRelateContactToMultipleAccounts` boolean Indicates whether users can relate a contact to multiple accounts ( `true` )
or only one account ( `false` ). The default value is `false` . If this feature

(Contacts to Multiple Accounts) is disabled, secondary contact–account
relationships created while the feature was enabled are deleted. Available
in API version 47.0 and later.

Avoid using the Metadata API to enable this feature. Use the Account
Settings page in Setup to enable Contacts to Multiple Accounts.


Metadata Types AccountSettings

**Field Name** **Field Type** **Description**

`enableReportsToOnPersonAccount` boolean Indicates whether the **Reports To** field on Person Account, which
corresponds to the `PersonReportsToId` field on the Account

object, is enabled. The field allows users to associate person accounts
and contacts with other person accounts or contacts that they report
to.

Available in API version 62.0 and later.

`showViewHierarchyLink` boolean Indicates whether the default **View Hierarchy** link on all business
account detail pages is visible ( `true` ) or hidden ( `false` ).

Declarative Metadata Sample Definition

The following is an example of the Account.settings file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AccountSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <enableAccountDiscovery>true</enableAccountDiscovery>

    <enableAccountHistoryTracking>true</enableAccountHistoryTracking>

    <enableAccountInsightsInMobile>false</enableAccountInsightsInMobile>

    <enableAccountOwnerReport>true</enableAccountOwnerReport>

    <enableAccountTeams>true</enableAccountTeams>

    <enableContactHistoryTracking>true</enableContactHistoryTracking>

    <enableRelateContactToMultipleAccounts>true</enableRelateContactToMultipleAccounts>

    <enableReportsToOnPersonAccount>true</enableReportsToOnPersonAccount>

    <showViewHierarchyLink>true</showViewHierarchyLink>

   </AccountSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the Account settings metadata:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>Account</members>

     <name>Settings</name>

    </types>

    <version>29.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types AccountInsightsSettings AccountInsightsSettings

Represents an org’s Einstein Account Insights settings. This setting controls features that help your reps maintain their relationships with
their customers.

Note: This metadata type has been deprecated as of API version 59.0.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### AccountInsightsSettings values are stored in the AccountInsights.settings file in the settings folder. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

#### AccountInsightsSettings is available in API versions 48.0 to 58.0.

Fields

**Field Name** **Field Type** **Description**

`enableAccountInsights` boolean Indicates whether Einstein Account Insights is enabled ( `true` ) or not
( `false` ). The default value is `false` .

Declarative Metadata Sample Definition

The following is an example of the AccountInsights.settings file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AccountInsightsSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <enableAccountInsights>true</enableAccountInsights>

   </AccountInsightsSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the AccountInsights settings metadata:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>AccountInsights</members>

     <name>Settings</name>

    </types>

    <version>29.0</version>

   </Package>

```


#### Metadata Types AccountIntelligenceSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### AccountIntelligenceSettings

Represents an org’s Account Intelligence settings. These settings control features that make it easy for sales reps to create accounts, see
relevant news articles, and add logos to account records. This type extends the Metadata metadata type and inherits its `fullName`
field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### AccountIntelligenceSettings values are stored in the AccountIntelligence.settings file in the settings folder. The

`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

#### AccountIntelligenceSettings is available in API versions 48.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableAccountLogos` boolean

Indicates whether your sales reps can see available company logos
( `true` ) or not ( `false` ). The logos are for US-based companies only.
The default value is `false` .

`enableAutomatedAccountFields` must be `true` to use this
setting.

`enableAutomatedAccountFields` boolean Indicates whether Automated Account Fields is enabled ( `true` ) or not
( `false` ). The default value is `false` .

`enableNewsStories` boolean

Indicates whether News is enabled ( `true` ) or not ( `false` ). The default
value is `false` .

`enableAutomatedAccountFields` must be `true` to use this
setting.

Declarative Metadata Sample Definition

The following is an example of the AccountIntelligence.settings file:

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountIntelligenceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

 <enableAccountLogos>true</enableAccountLogos>

```


#### Metadata Types AccountingSettings

```
    <enableAutomatedAccountFields>true</enableAutomatedAccountFields>

    <enableNewsStories>true</enableNewsStories>

   </AccountIntelligenceSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the AccountIntelligence settings metadata:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>AccountIntelligence</members>

     <name>Settings</name>

    </types>

    <version>48.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### AccountingSettings

Represents the settings for the Accounting Subledger feature.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### AccountingSettings values are stored in the AccountingSettings.settings file in the settings folder. The

`.settings` files are different from other named components, because there is only one settings file for each settings component.

Version

#### AccountingSettings components are available in API version 57.0 and later.

Fields

**Field Name** **Description**

```
enableAccountingSubledger

```

**Field Type**
boolean


Metadata Types AccountingSettings

**Field Name** **Description**

**Description**
Indicates whether Transaction Journal creation is enabled for the organization ( `true` )
or not ( `false` ).

```
enableAslDataCloud

enableFinancePeriod

enablePaymentMethodAdjust

enableScheduledJob

enableSkipReversalLogicEnabled

```

**Field Type**
boolean

**Description**
Requires Data Cloud and Accounting Subledger access.

Indicates whether Data Cloud Runtime for Accounting Subledger feature is enabled
for the organization ( `true` ) or not ( `false` ).

This field is available in API version 66.0 and later.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether changes to the Payment Method generate adjustments on
Transaction Journal records ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether Skip Reversal Logic is enabled ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of an AccountingSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

 <enableAccountingSubledger>true</enableAccountingSubledger>

 <enableAslDataCloud>true</enableAslDataCloud>

 <enablePaymentMethodAdjust>true</enablePaymentMethodAdjust>

```


#### Metadata Types ActionsSettings

```
    <enableSkipReversalLogicEnabled>false</enableSkipReversalLogicEnabled>

   </AccountingSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>Accounting</members>

     <name>Settings</name>

    </types>

    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActionsSettings

Represents an org’s actions settings for default quick actions, multi-dimensional publisher, and third-party actions. This type extends
the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### ActionsSettings values are stored in the Actions.settings file in the settings folder. The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

Components are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableDefaultQuickActionsOn` boolean Indicates whether default quick actions are created in the org ( `true`,
the default setting) or not ( `false` ).

`enableMdpEnabled` boolean Indicates whether multi-dimensional publisher is enabled ( `true`, the
default setting) or not ( `false` ).

`enableThirdPartyActions` boolean Indicates whether third-party actions are displayed in the
multi-dimensional publisher ( `true` ) or not ( `false`, the default setting).


#### Metadata Types ActivitiesSettings

**Field Name** **Field Type** **Description**

`enableOfflineWebLinks` boolean Indicates whether a button or link is available offline ( `true` ), or if it's
only available online ( `false`, the default setting).

Declarative Metadata Sample Definition

The following is an example of an ActionsSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ActionsSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <DefaultQuickActionsOn>true</DefaultQuickActionsOn>

    <MdpEnabled>true</MdpEnabled>

    <ThirdPartyActions>true</ThirdPartyActions>

   </ActionsSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActivitiesSettings

Represents an org's activity settings, and its user interface settings for the calendar. This type extends the Metadata metadata type and
inherits its `fullName` field.

Use the ActivitiesSettings component type to control the following activity settings:

**•** Configure group and recurring tasks, recurring and multiday events, and email tracking

**•** Relate multiple contacts to tasks and events (shared activities)

**•** Display custom logos in meeting requests

Also use the ActivitiesSettings component type to control user interface settings for the calendar, including hover links and drag-and-drop
editing.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### ActivitiesSettings values are stored in the Activities.settings file in the settings directory. The .settings files are

different from other named components because there’s only one settings file for each settings component.

Version

#### ActivitiesSettings is available in API versions 28.0 and later.

Fields

Settings for all types listed below are controlled on the Activity Settings page or the User Interface settings page as noted.


Metadata Types ActivitiesSettings

**Field Name** **Field Type** **Description**

`allowUsersToRelateMultipleContactsToTasksAndEvents` boolean This field indicates whether Shared Activities is enabled. When the value
is true, allows users to relate multiple contacts to a task or event.

Important: Beginning with API v36.0, this field is read-only in
all versions of the API. You can’t change the value of this field.
Even though this field was updateable before Spring '16, changing
this field’s value wasn't supported and could have resulted in an
incorrect integration. If you have code in older API versions that
changes the value of this field, ensure that you update that code
to prevent any errors.

`autoRelateEventAttendees` boolean

`enableActivityReminders` boolean

`enableCalendarHomeLWC` boolean

When users add attendees to events, events are automatically related
to up to 50 contacts or one lead. An attendee is matched by their email
address to a contact or lead.

Admins control this field on the Activity Settings page.

Available in API version 42.0 and later.

Enables popup activity reminders for an organization.

Admins control this field on the Activity Settings page.

Enables Lightning Web Components for Calendar. Increases the default
item limit in Calendar Home and applies styling enhancements to
improve readability.

Admins control this field on the Activity Settings page.

`enableClickCreateEvents` boolean Lets users create events in day and weekly calendar views by
double-clicking a specific time slot and entering the details of the event

in an overlay. Hovering over an event displays an overlay where users
can view the event details or delete the event without leaving the page.
Admins use a mini page layout to configure the fields shown in the
overlays. Doesn’t support recurring events or multi-person events.

Admins control this field on the User Interface settings page.

`enableDragAndDropScheduling` boolean Lets users create events associated with records by dragging a record
from a list view onto a calendar view and entering the details of the

event in an overlay. Hovering over an event displays an overlay where
users can view the event details or delete the event without leaving the
page. Admins use a mini page layout to configure the fields shown in
the overlays.

Admins control this field on the User Interface settings page.

`enableEmailTracking` boolean

Enables tracking of outbound HTML emails if an organization uses HTML
email templates.

Admins control this field on the Activity Settings page.


Metadata Types ActivitiesSettings

**Field Name** **Field Type** **Description**

`enableFlowTaskNotifsViaApex` boolean If Apex invokes Process Builder to create a task, determines whether an
email is sent ( `true` ) or not ( `false` ).

`enableGroupTasks` boolean

Lets users assign independent copies of a new task to multiple users.

Admins control this field on the Activity Settings page.

`enableHideChildEventsPreference` boolean Enables hiding child events from the calendar or activity views. This
setting is useful if you have complex event hierarchies and want to

simplify the views by hiding less relevant details. This field is available in
API version 50.0 and later.

Admins control this field on the Activity Settings page.

`enableListViewScheduling` boolean

Extends the functionality of `enableDragAndDropScheduling`
and `enableClickCreateEvents` to list view calendars.

Admins control this field on the User Interface settings page.

`enableLogNote` boolean Enables the option to create and associate a note on an existing record.

`enableMLSingleClientProfile` boolean Enable creating a client profile using machine learning. When this setting
is enabled, Salesforce uses machine learning algorithms to analyze and

consolidate client data, providing a more comprehensive client profile.
This can help sales and service teams to better understand their clients
and provide more personalized interactions. This field is available in API
version 50.0 and later.

Admins control this field on the Activity Settings page.

`enableMultidayEvents` boolean

`enableRecurringEvents` boolean

`enableRecurringTasks` boolean

`enableRollUpActivToContactsAcct` boolean

`enableSidebarCalendarShortcut` boolean

`enableSimpleTaskCreateUI` boolean

Enables creation of events that end more than 24 hours after they start.

Admins control this field on the Activity Settings page.

Enables creation of events that repeat at specified intervals.

Admins control this field on the Activity Settings page.

Enables creation of tasks that repeat at specified intervals.

Admins control this field on the Activity Settings page.

Enables a contact’s activities to be rolled up and displayed on the
contact’s primary account. Default value is `true` .

Available in API versions 47.0 and later.

In the sidebar, displays a shortcut link to a user’s last-used calendar view.

Admins control this field on the Activity Settings page.

Allows admins to specify whether tapping New Task in Salesforce opens
a regular task record edit page or a page that displays key task fields first.

Admins control this field on the Activity Settings page.


Metadata Types ActivitiesSettings

**Field Name** **Field Type** **Description**

`enableTimelineCompDateSort` boolean

`enableUNSTaskDelegatedToNotifications` boolean

Allows admins to sort past activities by completed date ( `true` ). If
`false`, activities are sorted by due date.

Admins control this field on the Activity Settings page.

On the Activity Settings page, exposes a setting for Admins to hide or
show a user setting that lets individual users enable or disable email
notifications when tasks are assigned to them.

`enableUserListViewCalendars` boolean Allows users to create and view user list view calendars in Lightning
Experience. Available in API versions 47.0 and later

`meetingRequestsLogo` string

`showCustomLogoMeetingRequests` boolean

`showEventDetailsMultiUserCalendar` boolean

Available when `showCustomLogoMeetingRequests` is enabled.
Uploads a custom logo. An administrator can select only a logo that has
been uploaded to certain folders in the Documents tab.

Admins control this field on the Activity Settings page.

Displays a custom logo in meeting request emails and on a meeting’s
Web page. Invitees see the logo when a user either invites them to an
event or requests a meeting.

Admins control this field on the Activity Settings page.

Displays event details on-screen rather than in hover text.

Admins control this field on the Activity Settings page.

`showHomePageHoverLinksForEvents` boolean In the calendar section of the Home tab:

**•** When a user hovers over the subject of an event, a hover link displays
an overlay with selected event details. (Hover links are always
available in other calendar views.)

**•** When a user clicks the subject of an event, displays the event detail
page.

Admins use a mini page layout to configure the fields shown in the
overlay.

Admins control this field on the User Interface settings page.

`showMyTasksHoverLinks` boolean In the My Tasks section of the Home tab and on the calendar day view:

**•** When a user hovers over the subject of a task, a hover link displays
an overlay with selected task details.

**•** When a user clicks the subject of a task, displays the task detail page.

Admins use a mini page layout to configure the fields shown in the
overlay.

Admins control this field on the User Interface settings page.


Metadata Types ActivitiesSettings

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the activity settings metadata for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Activities</members>

        <name>Settings</name>

      </types>

      <version>28.0</version>

   </Package>

```

Declarative Metadata Sample Definition

The following is an example of an activity settings file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ActivitiesSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableActivityReminders>true</enableActivityReminders>

      <autoRelateEventAttendees>true</autoRelateEventAttendees>

      <enableClickCreateEvents>true</enableClickCreateEvents>

      <enableDragAndDropScheduling>true</enableDragAndDropScheduling>

      <enableEmailTracking>true</enableEmailTracking>

      <enableGroupTasks>true</enableGroupTasks>

      <enableListViewScheduling>true</enableListViewScheduling>

      <enableMultidayEvents>true</enableMultidayEvents>

      <enableRecurringEvents>true</enableRecurringEvents>

      <enableRollUpActivToContactsAcct>true</enableRollUpActivToContactsAcct>

      <enableRecurringTasks>true</enableRecurringTasks>

      <enableTimelineCompDateSort>true</enableTimelineCompDateSort>

      <enableUserListViewCalendars>true</enableUserListViewCalendars>

      <enableSidebarCalendarShortcut>true</enableSidebarCalendarShortcut>

      <meetingRequestsLogo>Folder02/logo03.png</meetingRequestsLogo>

      <showCustomLogoMeetingRequests>true</showCustomLogoMeetingRequests>

      <showEventDetailsMultiUserCalendar>true</showEventDetailsMultiUserCalendar>

      <showHomePageHoverLinksForEvents>true</showHomePageHoverLinksForEvents>

      <showMyTasksHoverLinks>true</showMyTasksHoverLinks>

   </ActivitiesSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Document


#### Metadata Types AddressSettings AddressSettings

Represents the configuration of country/territory and state picklists. Use the AddressSettings component type to configure state and
country/territory data in your organization so that you can convert text-based values into standard picklist values. To convert your state
and country/territory values, from Setup, enter _`State and Country/Territory Picklists`_ in the Quick Find box, then
select **State and Country/Territory Picklists** .

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

Declarative Metadata File Suffix and Directory Location

#### AddressSettings values are stored in a single file named Address.settings in the settings directory. The .settings files

are different from other named components because there’s only one settings file for each settings component.

Version

#### AddressSettings is available in API versions 27.0 and later.

Salesforce CLI Usage

When working with the Salesforce CLI, use the metadata type `Settings:Address` to deploy or retrieve address settings.

CountriesAndStates

This complex metadata type represents valid definitions of states and countries/territories in picklists.

Note: You can use the Metadata API to edit existing states, countries, and territories in state and country/territory picklists. You
can’t use the Metadata API to create or delete new states, countries, or territories.

**Field** **Field Type** **Description**

`countries` Country[] The countries and territories available in picklists.

Country

This metadata type provides the definition for a country/territory in a picklist.

**Field** **Field Type** **Description**

`active` boolean Determines whether the value is available in the API.

Important: After you enable state and country/territory
picklists in your Salesforce organization, you can’t set the
`active` status to _`false`_ .

`integrationValue` string

A customizable text value that is linked to a state or
country/territory code. Integration values for standard states,

countries, and territories default to the full ISO-standard state,
country, and territory names. Integration values function similarly


Metadata Types AddressSettings

**Field** **Field Type** **Description**

to the API names of custom fields and objects. Configuring
integration values allows integrations that you set up before
enabling state and country/territory picklists to continue to work.

Important: If you don’t specify integration values before
enabling state and country/territory picklists in your
organization, records use the default value provided by
Salesforce. If you change integration values later, records
created or updated from that point on use your edited
values.

`isoCode` string The ISO-standard code populates this field when you issue a
`retrieve()` call. This field is read only in the API but you

can edit the label in Setup. You can’t edit the `isoCode` of
`standard` states, countries, and territories.

`label` string The label is what users see in picklists in Salesforce. This field is
read only in the API but you can edit the label in Setup.

`orgDefault` boolean Sets a country or territory as the default value for new records
in the Salesforce organization.

`standard` boolean

Standard states and countries are states and countries that are
included with Salesforce. You can’t edit the `standard`
attribute.

`states` State[] The states or provinces that are part of the country or territory.

`visible` boolean

State

This metadata type provides the definition for a state in a picklist.

Makes the state, country, or territory available to users in
Salesforce. States, countries, or territories that are `visible`
must also be `active` .

**Field** **Field Type** **Description**

`active` boolean Determines whether the value is available in the API.

Important: After you enable state and country/territory
picklists in your Salesforce organization, you can’t set the
`active` status to _`false`_ .

`integrationValue` string

A customizable text value that is linked to a state or
country/territory code. Integration values for standard states,

countries, and territories default to the full ISO-standard state,
country, and territory names. Integration values function similarly
to the API names of custom fields and objects. Configuring


Metadata Types AddressSettings

**Field** **Field Type** **Description**

integration values allows integrations that you set up before
enabling state and country/territory picklists to continue to work.

Important: If you don’t specify integration values before
enabling state and country/territory picklists in your
organization, records use the default value provided by
Salesforce. If you change integration values later, records
created or updated from that point on use your edited
values.

`isoCode` string

The ISO-standard code populates this field when you issue a
`retrieve()` call. This field is read only in the API but you
can edit the label in Setup.

`label` string The label is what users see in picklists in Salesforce. This field is
read only in the API but you can edit the label in Setup.

`standard` boolean

`visible` boolean

Declarative Metadata Sample Definition

Standard states and countries are states and countries that are
included with Salesforce. You can’t edit the `standard`
attribute.

Makes the state, country, or territory available to users in
Salesforce. States, countries, or territories that are `visible`
must also be `active` .

The following is sample XML that configures state and country picklists for the United States and Canada for use in an organization. It
also makes the country of Greenland available only in the API. This example is supported in API version 66.0.

```
<?xml version="1.0" encoding="UTF-8"?>

<AddressSettings xmlns="http://soap.sforce.com/2006/04/metadata">

  <countriesAndStates>

   <countries>

    <country>

     <active>true</active>

     <integrationValue>United States</integrationValue>

     <isoCode>US</isoCode>

     <label>United States</label>

     <orgDefault>true</orgDefault>

     <standard>true</standard>

     <states>

      <state>

        <active>true</active>

        <integrationValue>Alabama</integrationValue>

        <isoCode>AL</isoCode>

        <label>Alabama</label>

        <standard>true</standard>

        <visible>true</visible>

      </state>

      <state>

```


Metadata Types AddressSettings

```
           <active>true</active>

           <integrationValue>Alaska</integrationValue>

           <isoCode>AK</isoCode>

           <label>Alaska</label>

           <standard>true</standard>

           <visible>true</visible>

         </state>

        </states>

        <visible>true</visible>

       </country>

       <country>

        <active>true</active>

        <integrationValue>Canada</integrationValue>

        <isoCode>CA</isoCode>

        <label>Canada</label>

        <orgDefault>false</orgDefault>

        <states>

         <state>

           <active>true</active>

           <integrationValue>Alberta</integrationValue>

           <isoCode>AB</isoCode>

           <label>Alberta</label>

           <standard>true</standard>

           <visible>true</visible>

         </state>

         <state>

           <active>true</active>

           <integrationValue>British Columbia</integrationValue>

           <isoCode>BC</isoCode>

           <label>British Columbia</label>

           <standard>true</standard>

           <visible>true</visible>

         </state>

        </states>

        <visible>true</visible>

       </country>

       <country>

        <active>true</active>

        <integrationValue>Greenland</integrationValue>

        <isoCode>GL</isoCode>

        <label>Greenland</label>

        <standard>true</standard>

        <visible>false</visible>

       </country>

      </countries>

     </countriesAndStates>

   </AddressSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types AIReplyRecommendationsSettings AIReplyRecommendationsSettings

Represents the metadata used to manage settings for Einstein Reply Recommendations. This type extends the Metadata metadata type
and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

Einstein Reply Recommendations settings are stored in a single file named `aireplyrecommendations.settings` in the
`settings` folder. The `.settings` files are different from other named components because there’s only one settings file for each
settings component.

Version

#### AIReplyRecommendationsSettings is available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableAIReplyRecommendations` boolean If `true` (default), Einstein Reply Recommendations is enabled. If
`false`, it is disabled.

`enableGenReplyRecommendations` boolean If `true` (default), Einstein Service Replies is enabled. If `false`, it is
disabled. Available in API version 58.0 or later.

`enableServiceEinsteinGPTGrounding` boolean If `true` (default), Service AI Grounding is enabled. If `false`, it is
disabled. Available in API version 58.0 or later.

Declarative Metadata Sample Definition

The following is an example aireplyrecommendations.settings metadata file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AIReplyRecommendationsSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <enableAIReplyRecommendations>true</enableAIReplyRecommendations>

   </AIReplyRecommendationsSettings>

```

Example Package Manifest

The following is an example package.xml manifest that references the AIReplyRecommendationsSettings definitions:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>AIReplyRecommendations</members>

     <name>Settings</name>

    </types>

    <version>49.0</version>

   </Package>

```


#### Metadata Types AgentPlatformSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Copyright

Rights of ALBERT EINSTEIN are used with permission of The Hebrew University of Jerusalem. Represented exclusively by Greenlight.

#### AgentPlatformSettings

Represents settings for Agentforce.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### AgentPlatformSettings values are stored in the AgentPlatformSettings.settings file in the settings folder.

The `.settings` files are different from other named components, because there is only one settings file for each settings component.

Version

#### AgentPlatformSettings components are available in API version 64.0 and later.

Special Access Rules

Einstein Generative AI ( `EinsteinGptSettings.enableEinsteinGptPlatform` ) must be enabled for your org.

Fields

**Field Name** **Description**

```
enableAgentPlatform

```

**Field Type**
boolean

**Description**
Indicates whether Agentforce is turned on. The default value is `false` .


#### Metadata Types AgentforceAccountManagementSettings

Declarative Metadata Sample Definition

The following is an example of an AgentPlatformSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AgentPlatformSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableAgentPlatform>true</enableAgentPlatform>

   </AgentPlatformSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>AgentPlatform</members>

        <name>Settings</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

#### AgentforceAccountManagementSettings

Represents an org’s Agentforce Account Management settings.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### AgentforceAccountManagementSettings values are stored in the AgentforceAccountManagement.settings file in the

`settings` folder. The `.settings` files are different from other named components because there’s only one settings file for each
settings component.

Version

#### AgentforceAccountManagementSettings components are available in API version 65.0 and later.


#### Metadata Types AgentforceForDevelopersSettings

Fields

**Field Name** **Description**

```
enableAccountManagement

```

**Field Type**
boolean

**Description**
Indicates whether Agentforce Account Management is enabled ( `true` ) or not
( `false` ).

Declarative Metadata Sample Definition

The following is an example of the `AgentforceAccountManagement.settings` file:

```
<?xml version="1.0" encoding="UTF-8"?>

<AgentforceAccountManagementSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableAccountManagement>true</enableAccountManagement>

</AgentforceAccountManagementSettings>

```

The following is an example `package.xml` manifest that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>AgentforceAccountManagement</members>

     <name>Settings</name>

   </types>

   <version>65.0</version>

</Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### AgentforceForDevelopersSettings

Represents Agentforce for Developers settings.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all org settings metadata types are accessed using the Settings name. See Settings for more details.


Metadata Types AgentforceForDevelopersSettings

File Suffix and Directory Location

AgentforceForDevelopersSettings values are stored in the `AgentforceForDevelopers.settings` file in the `settings`
folder. The `.settings` files are different from other named components because there’s only one settings file for each settings
component.

Version

`AgentforceForDevelopersSettings` are available in API versions 62.0 and later.

Fields

**Field Name** **Field Type** **Description**

`agentforceForDevelopersOptOut` boolean Indicates whether Agentforce for Developers is enabled: `true` or
`false` . If `true`, Agentforce for Developers isn't enabled in your org,

which means that you've opted out of using it. If `false`, Agentforce
for Developers is enabled. The default value is `false` .

Declarative Metadata Sample Definition

The following is an example of the `AgentforceForDevelopers.settings` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

        <AgentforceForDevelopersSettings xmlns="http://soap.sforce.com/2006/04/metadata">

        <agentforceForDevelopersOptOut>false</agentforceForDevelopersOptOut>

        </AgentforceForDevelopersSettings>

```

The following is an example `package.xml` manifest that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

         <members>AgentforceForDevelopersSettings</members>

         <name>Settings</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types AnalyticsSettings AnalyticsSettings

Represents Analytics settings in Salesforce. CRM Analytics lets you explore all your data quickly and easily by providing AI-powered
advanced Analytics right inside Salesforce. Manage your datasets, query data with Salesforce Analytics Query Language (SAQL), and
customize dashboards. You can use these settings to configure which Analytics features are available to users in your organization.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### AnalyticsSettings values are stored in the Analytics.settings file in the settings folder. The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

#### AnalyticsSettings components are available in API version 46.0 and later.

Special Access Rules

The AnalyticsSettings metadata type is accessible in all organizations. The fields that pertain to Reports and Dashboards are available in
all organizations, but fields that pertain to CRM Analytics are only available in organizations with CRM Analytics enabled.

Fields

**Field Name** **Field Type** **Description**

`alwaysGenPreviews` boolean

`analyticsAdoptionMetadata` boolean

`analyticsCalendarApp` boolean

`autoInstallApps` boolean

`bundleCachingOptOut` boolean

`canAccessAnalyticsViaAPI` boolean

Indicates whether Analytics asset previews are generated ( `true` ) or not
( `false` ). Available in API version 47.0 and later.

Indicates whether Adoption Analytics metadata collection can be
installed via a dataflow in Salesforce ( `true` ) or not ( `false` ). Available
in API version 47.0 and later.

Indicates whether the Analytics Calendar app for Industry templates can
be installed in Salesforce ( `true` ) or not ( `false` ). Available in API version
49.0. Removed in API version 50.0.

Indicates whether CRM Analytics apps can be auto-installed in Salesforce
( `true` ) or not ( `false` ). Available in API version 54.0 and later.

Indicates whether the default CRM Analytics dashboard bundle caching
behavior is disabled ( `true` ) or enabled ( `false` ). Available in API version
58.0 and later.

Indicates whether Analytics assets can be accessed via the Analytics REST
API in Salesforce ( `true` ) or not ( `false` ). Available in API version 47.0
and later.


Metadata Types AnalyticsSettings

**Field Name** **Field Type** **Description**

`canAnnotateDashboards` boolean

`canEnableBYOMZeroDay` boolean

```
Scoring

```

`canEnableLiveMetrics` boolean

`canEnableSavedView` boolean

`canExploreData` boolean

```
Conversationally

```

`canShareAppsWith` boolean

```
Communities

```

`canSubscribeDashboard` boolean

```
Widgets

```

`canViewThumbnailAssets` boolean

`cdpQueryCachingOptIn` boolean

`concurrencyLimitSharing` boolean

`disableIncrementalDataset` boolean

```
Creation

```

Indicates whether the Analytics dashboards Chatter annotation feature
is enabled in Salesforce ( `true` ) or not ( `false` ). Available in API version
47.0 and later.

Indicates whether zero day scoring on user uploaded Einstein Discover
model is enabled in Salesforce ( `true` ) or not ( `false` ). Available in API
version 54.0 to 56.0. Removed in API version 57.0.

Indicates whether the Data Discovery live model metrics calculation
feature is enabled in Salesforce ( `true` ) or not ( `false` ). Available in API
version 48.0 and 49.0. Removed in API version 50.0.

Indicates whether the saved view feature for Analytics dashboards is
enabled in Salesforce ( `true` ) or not ( `false` ). Available in API version
47.0 and later.

Indicates whether Analytics data can be explored via NLQ ( `true` ) rather
than using strict SAQL statements ( `false` ). For example, "Show me all
accounts that are closed won". Available in API version 47.0 and later.

Indicates whether Analytics apps can be shared with Experience Builder
sites and their users, outside of the standard Analytics Studio experience
( `true` ) or not ( `false` ). Available in API version 47.0 and later.

Indicates whether a user can subscribe to Analytics dashboard widgets
in Salesforce ( `true` ) or not ( `false` ). Available in API version 47.0 to
50.0. Removed in API version 51.0.

Indicates whether the thumbnail representations of Analytics lenses and
dashboards are viewable ( `true` ) or not ( `false` ). Available in API version
47.0 and later.

Indicates whether caching is enabled for direct queries to Data 360
( `true` ) or not ( `false` ). Available in API version 65.0 and later.

Indicates whether the concurrency limits of Data Prep dataflows and
recipes can be shared ( `true` ) or not ( `false` ). Available in API version
60.0 and later.

Indicates whether incremental dataset optimization is disabled ( `true` )
or not ( `false` ). Available in API version 65.0 and later.


Metadata Types AnalyticsSettings

**Field Name** **Field Type** **Description**

`enableAmazonRedshift` boolean

```
OutputConnector

```

`enableAnalyticsEncryption` boolean

`enableAnalyticsSharing` boolean

```
Enable

```

`enableAutoCompleteCombo` boolean

`enableAutonomous` boolean

```
Experience

```

`enableAzureDLGen2Output` boolean

```
Connector

```

`enableC360GlobalProfile` boolean

```
Data

```

`enableCreateLegacy` boolean

```
Dataflows

```

`enableCrmaDataCloud` boolean

```
Integration

```

`enableCrmaSubsForExpCloud` boolean

`enableCrtSetupLightning` boolean

```
UiPref

```

`enableDashboardChange` boolean

```
OwnerPref

```

Indicates whether the Amazon Redshift Output connector is enabled in
Salesforce ( `true` ) or not ( `false` ). Available in API version 58.0 and
later.

Indicates whether encryption is enabled for Analytics in Salesforce
( `true` ) or not ( `false` ). Available in API version 48.0 and later.

Indicates whether the Analytics sharing is enabled in Salesforce ( `true` )
or not ( `false` ). Available in API version 48.0 and later.

Indicates whether using auto-complete when choosing reports and
