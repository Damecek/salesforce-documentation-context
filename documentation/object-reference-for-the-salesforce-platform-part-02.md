**•** `Order.OwnerId`

**•** `PartnerFundAllocation.CreatedById`

**•** `PartnerFundAllocation.ChannelPartnerId`

**•** `PartnerFundAllocation.OwnerId`

**•** `PartnerFundClaim.CreatedById`

**•** `PartnerFundClaim.OwnerId`

**•** `PartnerFundRequest.ChannelPartnerId`

**•** `PartnerFundRequest.CreatedById`

**•** `PartnerFundRequest.OwnerId`

**•** `PartnerMarketingBudget.CreatedById`

**•** `PartnerMarketingBudget.ChannelPartnerId`

**•** `PartnerMarketingBudget.OwnerId`


Standard Objects AccountRelationshipShareRule

**Field** **Details**

```
Description

DeveloperName

EntityType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A meaningful explanation of the sharing rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of data shared by this rule. Values are:

**•** `Account`

**•** `Campaign`

**•** `Case`

**•** `Contact`

**•** `Lead`

**•** `Order`

**•** `PartnerFundAllocation`

**•** `PartnerFundClaim`

**•** `PartnerFundRequest`

**•** `PartnerMarketingBudget`


Standard Objects AccountRelationshipShareRule

**Field** **Details**

```
Language

MasterLabel

NamespacePrefix

StaticFormulaCriteria

```

**Type**
picklist

**Properties**
Create, Defaulted on create. Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the account relationship share rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label assigned to the sharing rule to identify it.

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
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A way to further filter what data gets shared. This must be a deterministic formula and
spanning is not allowed.


### Standard Objects AccountShare

**Field** **Details**

```
Type

### AccountShare

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Must match the type of an account relationship for data to be shared according to the
`AccountToCriteriaField` and the `StaticForumulaCriteria` .

Represents a sharing entry on an account.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Account object can access this object. Customer Portal users can't access this
object.

Fields

The properties available for some fields depend on the default org-wide sharing settings. The properties listed are true for the default
settings of such fields.

**Field** **Details**

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Account. The possible values are:

**•** `Read`


Standard Objects AccountShare

**Field** **Details**

**•** `Edit`

**•** `All` (This value isn't valid for create or update calls.)

This field must be set to an access level that is at least equal to the organization’s default
Account access level. In addition, either this field, the `OpportunityAccessLevel`
field, or the `CaseAccessLevel` field must be set higher than the organization’s default
access level.

```
AccountId

CaseAccessLevel

ContactAccessLevel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to cases associated with the account. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
`CaseAccessLevel` . This field can't be updated via the API if the
`AccountAccessLevel` field is set to `All` . You can't update this field for the associated
account owner via the API. You must update the account owner’s `CaseAccessLevel`
via the Salesforce user interface.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects AccountShare

**Field** **Details**

**Description**
Level of access that the User or Group has to contacts associated with the account. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
`ContactAccessLevel` . This field can't be updated via the API if the
`ContactAccessLevel` field is set to “Controlled by Parent.” You can't update this field
for the associated account owner using the API. You must update the account owner’s
`ContactAccessLevel` via the Salesforce user interface.

```
OpportunityAccessLevel

RowCause

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to opportunities associated with the Account. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
opportunity access level. This field can’t be updated via the API if the
`AccountAccessLevel` field is set to `All` . You can't use the API to update this field
for the associated Account owner. You must update the Account owner’s
opportunityAccessLevel via the Salesforce user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a User with “All” access manually
shared the Account with the user or group.

**•** `Owner` —The User is the owner of the Account

**•** `Team` —The User or Group has team access (is an AccountTeamMember).


Standard Objects AccountShare

**Field** **Details**

**•** `Rule` —The User or Group has access via an Account sharing rule.

**•** `GuestRule` —The user or group has access via an Account guest user sharing rule.

**•** `ImplicitParent` —The User or Group has access because they’re the owner of or
have sharing access to records related to the account, such as opportunities, cases,
contacts, contracts, or orders.

**•** `GuestParentImplicit` —The guest user has access because they have access to
records related to the Account, such as opportunities, cases, contacts, contracts, or orders.

**•** `LpuParentImplicit` —The User has access because they have access to records
related to the Account, which are owned by high-volume Experience Cloud site users
and shared via a share group.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `PortalImplicit` —The Account is associated with the portal user.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Account via an account relationship data sharing rule.

**•** `Territory2AssociationManual` —With Sales Territories in API version 44.0
and earlier, the `TerritoryManual` reason code was written to AccountShare records
when you manually assigned an account to a territory. In API version 45.0 and later,
`Territory2AssociationManual` replaces all instances of
`TerritoryManual`, and the `Territory2AssociationManual` reason
code is written to AccountShare records when you manually assign an account to a
territory.

**•** `Territory` —The territory has access via a territory assignment rule.

**•** `TerritoryManual` —Deprecated starting in API version 45.0 and replaced by the
`Territory2AssociationManual` value.

```
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Account. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects AccountTag

Usage

This object allows you to determine which users and groups can view or edit Account records owned by other users.

If you attempt to create an AccountShare record that matches an existing record, the request updates any modified fields and returns
the existing record.

For example, the following code finds all accounts owned by a user and manually shares them to a portal user.

```
   QueryResult result = conn.query("SELECT Id FROM Account WHERE OwnerId = '005D0000001LPFB'");

   // Create a new AccountShare object

   List<AccountShare> shares = new ArrayList<AccountShare>();

   for (SObject rec : result.getRecords()) {

      AccountShare share = new AccountShare();

      share.setAccountId(rec.getId());

      //Set the portal user Id to share the accounts with

      share.setUserOrGroupId("003D000000QA8Tl");

      share.setAccountAccessLevel("Edit");

      share.setOpportunityAccessLevel("Read");

      share.setCaseAccessLevel("Edit");

      shares.add(share);

   }

   conn.create(shares.toArray(new AccountShare[shares.size()]));

```

This code shares the accounts that the user owns at the time, but not those accounts that are owned later. For these types of shares,
use an owner-based sharing rule, such as AccountOwnerSharingRule.

If an account is shared in multiple ways with a user, you don’t always see multiple sharing records. If a user has access to an account for
one or more of the following RowCause values, the records in the AccountShare object are compressed into one record with the highest
level of access.

**•** `ImplicitParent`

**•** `Manual`

**•** `Owner`

SEE ALSO:

### Account

CaseShare

LeadShare

OpportunityShare

### AccountTag

Associates a word or short phrase with an Account.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects AccountTag

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

AccountTag stores the relationship between its parent TagDefinition and the Account being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.


### Standard Objects AccountTeamMember

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### AccountTeamMember

Represents a User who is a member of an Account team.

See also UserAccountTeamMember, which represents a User who is on the default account team of another user.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only for Enterprise, Unlimited, and Performance Edition users who have enabled the account team functionality.

**•** Customer Portal users can't access this object.

Fields

**Field Name** **Details**

```
AccountAccessLevel

AccountId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Level of access that the User has to the Account. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

This field must be set to an access level that is at least equal to the organization’s default
Account access level. In addition, the users’s `AccountAccessLevel`,
`ContactAccessLevel`, `OpportunityAccessLevel`, or `CaseAccessLevel`
field must be set higher than the organization’s default access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Account to which this user is a team member. Must be a valid account
ID.


Standard Objects AccountTeamMember

**Field Name** **Details**

```
CaseAccessLevel

ContactAccessLevel

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Level of access that the User has to cases associated with the account. The possible values
are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
case access level. In addition, the users’s `AccountAccessLevel`,
`ContactAccessLevel`, `OpportunityAccessLevel`, or `CaseAccessLevel`
field must be set higher than the organization’s default access level. This field is available in
API version 37.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Level of access that the User has to contacts associated with the account. The possible values
are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `Controlled By Parent`

This field must be set to an access level that is at least equal to the organization’s default
contact access level. In addition, the users’s `AccountAccessLevel`,
`ContactAccessLevel`, `OpportunityAccessLevel`, or `CaseAccessLevel`
field must be set higher than the organization’s default access level. If the org-wide default
for contacts is set to Controlled By Parent, users can’t see or edit the Contact Access field.
This field is available in API version 37.0 and later.

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.


Standard Objects AccountTeamMember

**Field Name** **Details**

```
IsDeleted

OpportunityAccessLevel

PhotoURL

TeamMemberRole

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

Note: An AccountTeamMember record that is deleted is not moved to the Recycle Bin.
A deleted AccountTeamMember record can’t be undeleted unless the record was
cascade-deleted when deleting a related Account. For directly deleted
AccountTeamMember records, don’t use the isDeleted field to detect deleted records in
SOQL queries or `queryAll()` calls.

The `getDeleted()` call also doesn’t show deleted account team members unless
the record was deleted from an account related list or the Developer Console.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Level of access that the User has to opportunities associated with the account. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
opportunity access level. In addition, the users’s `AccountAccessLevel`,
`ContactAccessLevel`, `OpportunityAccessLevel`, or `CaseAccessLevel`
field must be set higher than the organization’s default access level. This field is available in
API version 37.0 and later.

**Type**
URL

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the users Chatter photo URL. This field is available in API version 37.0
and later.

**Type**
picklist


### Standard Objects AccountTerritoryAssignmentRule

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
Role associated with this team member. One of the valid team member roles defined for
your organization. Label is **Team Role** .

```
Title

 UserId

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the user’s title. This field is available in API version 37.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of this account team. Must be a valid User ID.

Use this object to manage the team members of a particular Account and to specify team member roles for those users on that account.

If team members are added by a user with group-based access, those members are removed after an account’s owner is changed. This
applies even if the **Keep account team** option is selected. A Salesforce admin, the account owner, or someone higher in the role
hierarchy should add team members to keep team members related to the account.

[If you use SOQL statements to query all records in an organization, the ALL ROWS keywords don’t query deleted account team member](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_query_all_rows.htm)
records.

SEE ALSO:

### Account AccountTerritoryAssignmentRule

An account assignment rule that assigns accounts to territories based on account fields. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects AccountTerritoryAssignmentRule

Special Access Rules

Users with the View Setup and Configuration permission can access this object. Users with the Manage Territories permission can edit
this object.

Fields

**Field** **Details**

```
BooleanFilter

IsActive

IsInherited

Name

```

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
Advanced filter conditions that were specified for the rule in the online application. For
example, “(1 AND 2) OR 3.”

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the rule is active ( `true` ) or inactive ( `false` ). Via the API, active rules run
automatically when new accounts are created and existing accounts are edited. The exception
is when the `IsExcludedFromRealign` field on an account is `true`, which prevents
account assignment rules from evaluating that account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the rule is an inherited rule ( `true` ) or a local rule ( `false` ). An inherited
rule also acts upon territories below it in the territory hierarchy. A local rule is created at the
immediate territory and only impacts the immediate territory.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
A name for the rule. Limit is 80 characters.


### Standard Objects AccountTerritoryAssignmentRuleItem

**Field** **Details**

```
 TerritoryId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
ID of the territory where accounts that satisfy this rule are assigned.

A territory will not have any accounts (with the exception of manually assigned accounts) unless at least one account assignment rule
is active for the territory.

SEE ALSO:

### AccountTerritoryAssignmentRuleItem

Territory

UserTerritory

### AccountTerritoryAssignmentRuleItem

A row of selection criteria for an AccountTerritoryAssignmentRule object. Available if Sales Territories has been enabled.

### AccountTerritoryAssignmentRuleItem can be created or deleted if the BooleanFilter field on its corresponding

AccountTerritoryAssignmentRule object is a null value.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Users with the View Setup and Configuration permission can access this object. Users with the Manage Territories permission can edit
this object.

Fields

**Field** **Details**

```
Field

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AccountTerritoryAssignmentRuleItem

**Field** **Details**

**Description**
The standard or custom account field to use as a criteria.

```
 Operation

 RuleID

 SortOrder

 Value

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
ID of the associated AccountTerritoryAssignmentRule.

**Type**
int

**Properties**
Create, Filter, Update

**Description**
The order in which this row is evaluated compared to other
AccountTerritoryAssignmentRuleItem objects for the given AccountTerritoryAssignmentRule.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The field value(s) to evaluate, such as `94105` if the Field is `Billing Zip/Postal`
`Code` .

**•** Both standard and custom account fields can be used as criteria for account assignment rules.


### Standard Objects AccountTerritorySharingRule

**•** A territory will not have any accounts (with the exception of manually assigned accounts) unless at least one account assignment
rule is active for the territory.

SEE ALSO:

AccountTerritoryAssignmentRule

Territory

UserTerritory

### AccountTerritorySharingRule

Represents the rules for sharing an Account within a territory.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
AccountAccessLevel

CaseAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target group for all child cases of
the account. The possible values are:

**•** `None`


Standard Objects AccountTerritorySharingRule

**Field** **Details**

**•** `Read`

**•** `Edit`

```
ContactAccessLevel

Description

DeveloperName

GroupId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A value that represents the type of access granted to the target group for all related contacts
on the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: This field is read only.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available in
API version 29.0 and later.

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

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference


Standard Objects AccountTerritorySharingRule

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Accounts owned by users in the source territory trigger
the rule to give access.

```
Name

OpportunityAccessLevel

UserOrGroupId

```

Usage

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
A value that represents the type of access granted to the target group for all opportunities
associated with the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the user or group being given access, or, if a territory ID, the users assigned
to that territory.

Use this object to manage the sharing rules for a particular object. General sharing and territory-related sharing use this object.

SEE ALSO:

Account

AccountShare


### Standard Objects AccountUserTerritory2View AccountUserTerritory2View

Represents the view of the Users in Assigned Territories related list in Lightning Experience for Sales Territories. Available in API version
42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Standard and partner users can access this object.

Fields

**Field Name** **Details**

```
AccountId

RoleInTerritory2

Territory2Id

UserId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the account associated with the Users in Assigned Territories
related list.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of each user in the Users in Assigned Territories related list.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for each territory in the Users in Assigned Territories related list.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ActionCadence

**Field Name** **Details**

**Description**
Unique identifier for each user in the Users in Assigned Territories related list.

Usage

Use this object to show the users who are assigned to the territories assigned to an account.

A filter criterion with one `AccountId` is required when you execute a SOQL query on this object.

### ActionCadence

Represents the definition of a cadence. This object is available in API version 45.0 and later.

Use ActionCadence and its related objects to learn about an action cadence, including:

**•** The current state of the action cadence.

**•** The steps that the action cadence contains.

**•** Which leads, contacts, or person accounts are assigned to the action cadence.

The ActionCadence, ActionCadenceStep, ActionCadenceRule, and ActionCadenceRuleCondition objects define an action cadence and
the steps that it contains. ActionCadenceTracker and ActionCadenceStepTracker track a prospect's movement through an active action
cadence.

By learning when the action cadence objects are created and deleted, you can make the most of the action cadence API.

**•** An ActionCadence record is created when you use the Sales Engagement app to create a cadence.

**•** An ActionCadenceStep record is created to represent a step. If the step is a branch step, then corresponding ActionCadenceRule
and ActionCadenceRuleCondition records are also created.

**•** An ActionCadenceTracker record is created when you assign a prospect to an action cadence.

**•** An ActionCadenceStepTracker record is created each time the prospect moves to a new step.

All of these action cadence records exist until you use the Sales Engagement app to delete an action cadence. If many prospects have
been assigned to the action cadence, there can be many associated ActionCadenceTracker and ActionCadenceStepTracker records. In
this case, deleting the action cadence can take some time. While the action cadence is being deleted, the value for the State field is
`Deleting` on the ActionCadence record.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`,

Fields

**Field** **Details**

```
ActivatedDate

```

**Type**
date


Standard Objects ActionCadence

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the user activated the action cadence. ActionCadence objects are created in
a draft state and must be manually activated before they’re used.

```
ActiveTargets

Description

ErrorMessage

FolderId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of active targets that are currently assigned with this cadence. Available
in API version 58.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of this action cadence.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If there was an error when activating the action cadence, this field contains the error message.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the folder that contains the action cadence. Available in API version 49.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User


Standard Objects ActionCadence

**Field** **Details**

```
FolderName

IsWaitAllowedBeforeDaisyChain

LastEditedDateTime

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name of the folder that contains the action cadence. Available in API version 49.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the cadence is allowed to have a wait step before a daisy chain step ( `true` ) or not
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time this object was last edited.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this object was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action cadence was last viewed in the Sales Engagement app.

**Type**
string


Standard Objects ActionCadence

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this action cadence. Every action cadence in an org must have a unique name.

```
OwnerId

State

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the action cadence (typically the user who created it).

Note: To change the owner of an action cadence, the new owner must have read
access to action cadences enabled in their user profile.

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This entity's state.

Possible values are:

**•** `Active`

The user finished modifying the action cadence and has activated it. At this point, you
can't make any more changes to the steps in the action cadence.

**•** `Deleting`

All records associated with this action cadence, including the ActionCadence record and
all its related records, are being deleted. While in this state, the ActionCadence can’t be
attached to a prospect.

**•** `Draft`

ActionCadence objects are in the draft state when they’re created. In this state, the
ActionCadence can’t be assigned to any prospect.

**•** `Error`


Standard Objects ActionCadence

**Field** **Details**

An error occurred while trying to activate the action cadence.

**•** `Inactive`

The user deactivated the action cadence. New targets can’t be added to the action
cadence. Existing targets continue in the action cadence until completion.

```
SuccessfulCompletions

TotalSteps

TotalTargets

Type

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of successful dispositions this cadence has upon completion. For example,
customer engaged or customer connected. Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of total steps associated with this cadence. This value doesn’t include special
step types such as root, branch, and daisy chain. Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of targets that have been assigned with this cadence. Available in API
version 58.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the type of ActionCadence. Available in API version 56.0 and later.

Possible values are:

**•** `Standard`

Standard cadences can contain multiple steps and are usually built by sales managers
in the Cadence Builder.

**•** `Quick`


### Standard Objects ActionCadenceRule

**Field** **Details**

Quick cadences can contain only one step, are built by reps for their personal use, and
don't require the Cadence Builder.

Usage

Use ActionCadence to learn how many action cadences are currently active:

```
   select COUNT() from ActionCadence where State="Active"

```

Retrieve all ActionCadence records that have "West Coast" in their name:

```
   SELECT ActionCadenceId FROM ActionCadence WHERE NAME LIKE '[West Coast Cadence]%'

```

Retrieve all ActionCadence records owned by a specific user:

```
   SELECT ActionCadenceId FROM ActionCadence WHERE OwnerId = '<owner id>'

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceChangeEvent (API version 48.0)**
Change events are available for the object.

**ActionCadenceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ActionCadenceShare on page 67**
Sharing is available for the object.

SEE ALSO:

### ActionCadenceRule ActionCadenceRuleCondition

ActionCadenceStep

ActionCadenceStepTracker

### ActionCadenceRule

Represents the logic that a branch step uses to determine which branch an action cadence tracker follows in an action cadence. Use
### ActionCadenceRule to learn about a branch step, including its logic and what the next step is. This object is available in API version 48.0

and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```


Standard Objects ActionCadenceRule

Fields

**Field** **Details**

```
ActionCadenceStepId

ConditionLogic

GlobalEventType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ActionCadenceStep that this rule is associated with.

This field is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The logical operator used to evaluate the rule conditions. Possible values are:

**•** `AND`

If this rule has several conditions, all of them must be `true` for this step to be
`true` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the action cadence rule contains a global exit condition, this field contains the type
of event that the rule represents.

Possible values are:

**•** `EmailReply`

**•** `EmailHardBounce`

**•** `EmailSoftBounce`

**•** `CallMeaningfulConnect`

**•** `CallNotInterested`

**•** `CallUnqualified`


Standard Objects ActionCadenceRule

**Field** **Details**

**•** `CallLeftVoicemail`

**•** `CallCallBackLater`

This field is available in API version 49.0 and later.

```
GraphState

OutcomeNextStepName

ParentRuleName

RuleName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the state of the `ActionCadenceRule` within the step graph, or
sequence, of the related action cadence. Available in API version 53.0 and later.

Possible values are:

**•** `Included` —This step rule is part of the step graph.

**•** `Orphaned` —This step rule was removed from the step graph before the action
cadence was activated. Orphaned step rules are deleted upon activation.

**•** `Pending` —This step rule has been created but hasn’t been added to the step
graph. Pending step rules can be added to the step graph in the future.

**•** `Retired` —This step rule was previously part of an active action cadence step
graph and was removed during an edit after activation. Retired step rules can have
associated step trackers.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next step in the action cadence if this rule evaluates as `true` . If this rule evaluates
as `false`, the next step is `ActionCadenceStep.BranchDefaultStepName` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `RuleName` field of the previous rule in the action cadence. Must
contain a valid rule name value unless this rule is the root rule. `null` if this rule is a
root rule.

This field is available in API version 49.0 and later.

**Type**
string


### Standard Objects ActionCadenceRuleCondition

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name given to the rule. Every rule in an action cadence must have a unique name.

```
RuleType

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of step that this rule applies to. Possible values are:

**•** `BranchStep`  - The rule evaluates the condition of a branch step. A branch step
is an ActionCadenceStep record with the field `type` equal to `Branch` .

**•** `RepeatedStep`  - The rule evaluates the repeat steps for quick cadence. Available
in API version 58.0 and later.

**•** `RootStep`  - The rule evaluates a global exit condition.

**•** `SubRootStep` —Available in API version 58.0 and later.

This field is available in API version 49.0 and later.

Use ActionCadenceRule to see all the rules associated with a branch step:

```
select RuleName from ActionCadenceRule where ActionCadenceStep.ActionCadence.Name = "High

 Priority CFO"

```

SEE ALSO:

### ActionCadence ActionCadenceRuleCondition

ActionCadenceStep

ActionCadenceStepTracker

### ActionCadenceRuleCondition

Represents the logic for a branch step. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ActionCadenceRuleCondition

Fields

**Field** **Details**

```
ActionCadenceRuleId

Operator

Resource

RuleConditionName

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ActionCadenceRule that this condition is associated with.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The conditional operator for this rule. Possible values are:

**•** `Equal`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to evaluate. Possible values are:

**•** `CallDispositionCategory`

Use by branch steps.

**•** `EmailEngagement`

Used by ListenerBranch steps.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the rule condition. Every rule condition in a cadence must have a unique name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The event that your cadence rule condition listens for to decide when the event is complete.

Possible values for emails are:

**•** `EmailOpen`

**•** `EmailLinkClick`

Possible values for calls are:

**•** `CallMeaningfulConnect`

**•** `CallUnqualified`

**•** `CallLeftVoicemail`

**•** `CallNotInterested`

**•** `CallCallBackLater`

Usage

Use ActionCadenceRuleContion to see all the rule conditions associated with a branch step:

```
   select RuleConditionName from ActionCadenceRuleCondition where ActionCadenceStepId= <ID

   of a branch step>

```

SEE ALSO:

### ActionCadence

ActionCadenceRule

### ActionCadenceStep ActionCadenceStepTracker ActionCadenceStep

Represents a step in a cadence. Use ActionCadenceStep to learn which steps belong to a cadence, and how the steps are connected to
each other. This object is available in API version 48.0 and later.

An ActionCadenceStep record is created to represent a step. If the step is a branch step, then corresponding ActionCadenceRule and
ActionCadenceRuleCondition records are also created.

Note: An ActionCadenceStep with `IsOrphan` equal to `true` can be part of a cadence but is never executed. To retrieve the
steps that can be executed by the cadence, query for ActionCadenceStep records with `IsOrphan` equal to `false` .
### ActionCadenceStep records with IsOrphan equal to true are deleted.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```


Standard Objects ActionCadenceStep

Fields

**Field** **Details**

```
ActionCadenceId

AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ActionCadence that this step belongs to.

This field is a relationship field.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Call Back Later** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Left Voicemail** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Meaningful Connect** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The number of calls having the call outcome **Not Interested** .

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where the call outcome isn’t categorized.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome **Unqualified** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that weren’t delivered successfully.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails delivered.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails returned for a permanent reason — for example, the email address
doesn’t exist. This field is available in API version 50.0 and later.


Standard Objects ActionCadenceStep

**Field** **Details**

```
AllEmailsLinkClickedCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link count towards this total. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that the target opened while working on this step. Multiple opens of
the same email count towards this total.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were returned because the recipient set an out-of-office responder.
Multiple replies count towards this total. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email count towards this total, This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails.

**Type**
int


Standard Objects ActionCadenceStep

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were returned for temporary reasons — for example, the email
is too large. This field is available in API version 50.0 and later.

```
AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllManuallyCompletedCount

AllOnTimeCompletedCount

AllOverdueCompletedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps manually completed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps completed on time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of overdue steps that were completed.


Standard Objects ActionCadenceStep

**Field** **Details**

```
AllSkippedCount

AllTotalCallsCount

BranchDefaultStepName

ChainedCadenceId

GoToStepIntervalInMinutes

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps skipped.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls that the sales rep made during this step.

This field is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the default step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ActionCadence for the linked action cadence. Available only if the step type is
`DaisyChain` (meaning that another action cadence is connected to this action cadence).

This field is a relationship field.

**Relationship Name**
ChainedCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
Contains information about when the step should be repeated next, in minutes. Available
in API version 58.0 and later.

```
GoToStepIterationLimit

GoToStepName

GraphState

HasVariant

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the maximum number of repeat (goto) step iterations allowed. Available in API
version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If this step’s original next step was removed during an edit after activation, this field specifies
the updated next step.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the state of the `ActionCadenceStep` within the step graph, or sequence,
of the action cadence.

Possible values are:

**•** `Included` —This step is part of the step graph.

**•** `Orphaned` —This step was removed from the step graph before the action cadence
was activated. Orphaned steps are deleted upon activation.

**•** `Pending` —This step has been created but hasn’t been added to the step graph.
Pending steps can be added to the step graph in the future.

**•** `Retired` —This step was previously part of an active action cadence step graph and
was removed during an edit after activation. Retired steps can have associated step
trackers.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
This field is valid for email and call step types. If `true`, the step has email or call template
variants. The template variants are defined in ActionCadenceStepVariant records. Available
in API version 53.0 and later.

The default value is `false` .

```
IsImmediateWakeUp

IsOrphan

IsScheduledDueDateLocked

IsScreenFlowActive

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a listener branch is immediate wake up ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, this step isn’t executed by the action cadence and will be deleted. Steps with
`IsOrphan` equal to `true` have `ParentStepName` equal to `null` .

Note: To retrieve the active steps in an action cadence, include `IsOrphan=false`
in your query.

The default value is `false` .

This field is available in API version 49.0 and later.

This field is a calculated field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether assignees can change the due date ( `true` ) or not ( `false` ). Available in
API version 58.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
Indicates whether the flow is active and can be executed ( `true` ) or not ( `false` ).

The default value is `false` .

```
IsStepAutomationActive

IsThreaded

ParentStepName

RootStepId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the flow referenced in the StepAutmationReference field is active. If false, the flow
isn’t active. Only active flows can be executed. The default value is `false` . This field is
available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is valid for email steps. Email steps have ActionCadence.StepType equal to
`SendAnEmail` . If `true`, the email for this email step is sent as a reply to the email
conversation from the previous email step. By sending the email as a reply to a previous
email, customers see a "conversation" view of the emails. Only emails from the same action
cadence are grouped as conversations.

This field can’t be true for the first email step in an action cadence, because the first email
from an action cadence must start a new conversation with the prospect.

The default value is `false` . This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The step name ( `ActionCadenceStep.StepName` ) of the previous step in the action
cadence. Must contain a valid step name value unless this step is the root step. `null` if this
step is a parent step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The ID of the root step for this action cadence. Every action cadence has exactly one root
step (so that the Salesforce API can find all the steps for this cadence).

This field is a relationship field.

**Relationship Name**
RootStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
ScheduledDaysUntilDue

ScheduledDaysUntilStart

ScheduledStartDelayInMinutes

ScheduledStartTimeInMinutes

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days after which this current step is due. Available in API version 58.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days when this step starts after the previous step completes. For delays of
greater than one day from `ScheduledStartTimeInMinutes` . Available in API version
58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Any hard waits in minutes is captured in this field. Waits greater than 1 day need to set
`ScheduledDaysUntilStart` . Available in API version 58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionCadenceStep

**Field** **Details**

**Description**
The specific time of day when the step starts. The time represents minutes after 00:00.
Available in API version 58.0 and later.

```
ScreenFlowReference

StepAutomationReference

StepComments

StepName

StepTitle

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The `namespace__fullname` of the screen flow. Used to describe flow objects and
launch flows client side.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that the step uses. Cadence steps can launch a cadence step flow as
the step or as a cadence autolaunched flow when a rep completes the step. The format is
`namespace__fullName` . This field is available in API version 56.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A comment that provides additional information about this step.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier for this step. Generated by Salesforce.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title given to the step when it was created.


Standard Objects ActionCadenceStep

**Field** **Details**

```
TemplateId

Type

TypeDetail

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If a template was added to this step, this field contains the template's ID. For example, if this
step is a call step it can contain a template for a call script. Or, if this step is an email step, it
can contain a template for an email.

This field is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of step. Possible values are:

**•** `AutoSendAnEmail`  - Salesforce automatically sends the specified email.

**•** `Branch`  - A branch step in the action cadence.

**•** `CreateTask`  - Used for custom steps.

**•** `DaisyChain`  - A daisy chain step. A daisy chain step connects this action cadence
to another action cadence. It must be the last step in the path.

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`  - A branch step for emails.

**•** `MakeACall`  - The sales rep must call the prospect at this step.

**•** `PlatformScreenFlow`

**•** `Root`  - This step is the root step for the action cadence.

**•** `SendAnEmail`  - The sales rep must send the prospect an email at this step.

**•** `Wait`  - A wait step tells the sales rep not to do anything at this point in the action
cadence.

**Type**
string


Standard Objects ActionCadenceStep

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
More detail about the step type. If the step is a cadence step flow, this field contains the flow
name. Otherwise, this field contains the same value as the Type field. This field is available
in API version 56.0 and later.

```
UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

WaitTimeInSeconds

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that the target opened as part of this step. Multiple openings of the
same email aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email aren’t counted. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the step type is `Wait` . The time in seconds for this step to wait.


### Standard Objects ActionCadenceStepTracker

Usage

Use ActionCadenceStep to see what steps your action cadence has:

```
   select StepTitle from ActionCadenceStep where ActionCadence.ID= <the id of an action

   cadence> and IsOrphan=false

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceStepChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

### ActionCadence

ActionCadenceRule

ActionCadenceRuleCondition

### ActionCadenceStepTracker ActionCadenceStepTracker

Represents a step in an active cadence for a specific cadence target. This object is available in API version 48.0 and later.

An ActionCadenceStepTracker record is created when a target moves to a new step in a cadence. Use ActionCadenceStepTracker to
find information such as the step's current state, the reason it completed, and its type.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActionCadenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ActionCadence that is related to the ActionCadenceStep.

This field is a relationship field.

**Relationship Name**
### ActionCadence


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ActionCadence

```
ActionCadenceName

ActionCadenceStepId

ActionCadenceTrackerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the related ActionCadence object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ActionCadenceStepTracker is the runtime version of an ActionCadenceStep. This field contains
the ID of the related ActionCadenceStep.

This field is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ActionCadenceTracker.

This field is a relationship field.

**Relationship Name**
ActionCadenceTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceTracker


Standard Objects ActionCadenceStepTracker

**Field** **Details**

```
ActionTakenDateTime

CompletedById

CompletionDate

CompletionReason

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the action described in this step was taken.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID of the sales rep who completed this step. A step can be assigned to several users
before it’s completed. This field is available in API version 50.0 and later.

This field is a relationship field.

**Relationship Name**
CompletedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this step completed. A step is completed either when the action is taken, or the
step is skipped.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that this step completed: Possible values are:

**•** `AutomaticallyCompleted`  - The sales rep successfully completed this step
and moved to the next one. Salesforce automatically marks this step as completed.

**•** `AutomaticallyExited`  - The step exited because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `ManuallyCompleted`  - The sales rep manually marked this step as completed.


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**•** `ManuallySkipped`                   - The sales rep skipped this step.

```
DueDateTime

ErrorCode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Some steps have a due date to indicate when they must be completed. If this step has been
assigned a due date, this field contains the date and time it is due.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AUTO_EMAIL_DAILY_LIMIT_REACHED`

**•** `AUTO_EMAIL_ORG_SETTING_OFF`

**•** `AUTO_LIST_MQ_MAX_RETRIES_FAILED`

**•** `BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED`

**•** `EAC_GLOBAL_DATA_SOURCE_ERROR` —EAC data source error

**•** `EMAIL_ORG_SETTING_OFF`

**•** `EXCHANGE_MAX_MAILBOX_SIZE` —Max Exchange mailbox size reached

**•** `EXCHANGE_SEND_AS_DENIED`

**•** `FIX_WITH_RECONNECT` —Data connection failed

**•** `GOOGLE_MAIL_SERVICE_NOT_ENABLED` —Gmail service not enabled

**•** `INVALID_DRAFT` —Invalid email draft

**•** `INVALID_TARGET_EMAIL`

**•** `INVALID_TEMPLATE_ID`

**•** `INVALID_USER_EMAIL`

**•** `MAIL_PROVIDER_RATE_LIMIT_REACHED` —Email provider rate limit reached

**•** `NON_EMAIL_UNKNOWN_ERROR` —Unknown error

**•** `NO_ATTACHMENT_ACCESS`

**•** `NO_CONTENT_VERSION_ACCESS`

**•** `NO_LIST_EMAIL_PERMISSION`

**•** `NO_TARGET_ACCESS`

**•** `ORG_WIDE_AUTO_EMAIL_LIMIT_REACHED`

**•** `ORG_WIDE_DAILY_EMAIL_LIMIT_REACHED`

**•** `OTHER_REQ_FIELD_MISSING` —Other required field missing


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**•** `PARDOT_MERGE_FIELD_RENDERING_ERROR`

**•** `POST_SEND_EXCEPTION`

**•** `RETRIES_MAX_EXCEEDED` —Maximum retries exceeded

**•** `RETRY_LATER`

**•** `SCHEDULED_EMAIL_FAILED` —Unknown error

**•** `SENDER_MAILBOX_NOT_FOUND`

**•** `TARGET_DO_NOT_CONTACT_ON` —Target has Do Not Contact on

**•** `TARGET_EMAIL_BOUNCED`

**•** `TARGET_EMAIL_EMPTY`

**•** `TEMPLATE_DELETED`

**•** `TEMPLATE_EMPTY` —Email subject or body missing

**•** `TEMPLATE_HAS_INVALID_MERGE_FIELD`

**•** `TEMPLATE_MERGE_FIELD_RENDERING_ERROR`

**•** `TEMPLATE_NOT_PUBLIC` —No access to template

**•** `TEMPLATE_TOO_LARGE`

**•** `UNKNOWN` —Email unknown error

**•** `USER_HAS_LOST_HVS_ACCESS`

**•** `USER_IS_INACTIVE`

```
GoToStepIterationCount

IsActionTaken

ScheduledStartDateTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the action cadence step tracker was created for the same step in a
cadence. Available in API version 58.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the sales rep completed an action during this step, such as making a phone call,
otherwise `false` .

The default value is `false` .

This field is a calculated field.

**Type**
dateTime


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the step starts. Available in API version 58.0 and later.

```
SecondsOverdue

State

StepTitle

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this step has a due date that has passed, this field contains the number of seconds that
has elapsed since the due date. Once a sales rep takes action on the cadence step, the value
of this field is the number of seconds elapsed between the due date and the time the action
was taken.

This field is a calculated field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The current state of this step. Possible values are:

Possible values are:

**•** `Active`  - The current step that the sales rep is performing. There can only be one
active step for a given target.

**•** `Cancelled`  - The sales rep canceled the step. Salesforce doesn’t run any canceled
steps.

**•** `Completed`  - This step is finished. Either the work in the step completed, or the step
was skipped.

**•** `Error`  - An error occurred while executing this step.

**•** `InProgress`  - The sales rep has started the step, but it isn’t yet completed.

**•** `Paused` —The sales rep paused the step.

**•** `Queued`  - Used for automated email steps. The email step has started but the email
is waiting in the queue to be sent.

**•** `Scheduled`  - Used for email steps. An email can be scheduled to be sent later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCadenceStepTracker

**Field** **Details**

**Description**
The name of the related step.

```
StepType

TargetId

WasEverPaused

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of step to execute. Possible values are:

**•** `AutoSendAnEmail`

**•** `Branch`

**•** `CreateTask`

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow`

**•** `Root`

**•** `SendAnEmail`

**•** `SubRoot`

**•** `Wait`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the prospect that is assigned to this cadence.

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

**Type**
boolean


### Standard Objects ActionCadenceStepVariant

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the sales rep had ever paused this step ( `true` ), or not ( `false` ). This field
is available in API version 50.0 and later.

Usage

List all the steps that this prospect has completed in a given cadence:

```
   select StepTitle from ActionCadenceStepTracker where TargetID = <target ID>

         and ActionCadenceId=<action cadence id> and StepType="Completed"

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceStepTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

### ActionCadence

ActionCadenceRule

### ActionCadenceStep

ActionCadenceRuleCondition

### ActionCadenceStepVariant

Represents an email template or call script variant associated with an action cadence step. Email and call steps can have up to 3 variants
associated so sales teams can compare the engagement results. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Sales Engagement and Allow Email Template and Call Script Variant Testing must be enabled.


Standard Objects ActionCadenceStepVariant

Fields

**Field** **Details**

```
ActionCadenceStepId

SplitPercentage

TemplateId

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related action cadence step.

This is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of emails to send or calls to make using this email template or call script
variant. The total for all variants must be 100%.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated email template or call script.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
picklist


### Standard Objects ActionCadenceTracker

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated action cadence step.

Possible values are:

**•** `AutoSendAnEmail`

**•** `Branch`

**•** `CreateTask`

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow` —Available in version 55.0 and later.

**•** `Root`

**•** `SendAnEmail`

**•** `Wait`

Only email and call steps can have an associated action cadence step variant.

Usage

Use ActionCadenceStepVariant to retrieve the email template or call script for an action cadence step:

```
   SELECT SplitPercentage, TemplateId FROM ActionCadenceStepVariant WHERE

   ActionCadenceStepId=:[idValue]

```

Use ActionCadenceStepVariant to retrieve the call scripts from all call steps:

```
   SELECT SplitPercentage, TemplateId, ActionCadenceStepId FROM ActionCadenceStepVariant WHERE

    Type='MakeACall'

### ActionCadenceTracker

```

Represents an active cadence target. This object is available in API version 45.0 and later.

An ActionCadenceTracker record is created when you add a target to a cadence. Use ActionCadenceTracker to learn about a running
cadence target, including its state, current step, assigned prospect, and reason for completion.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ActionCadenceTracker

Fields

**Field** **Details**

```
ActionCadenceId

CompletionDisposition

CompletionReason

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related ActionCadence.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The target’s disposition when it exited the action cadence. This field contains a value if the
target’s `State` is `Complete` . Sales reps can set this value when removing a target from
a cadence. This field is available in API version 51.0 and later. Possible values are:

**•** `Bad Data`  - some of the target’s data is incorrect or invalid.

**•** `Contact Later`  - the target asked to be contacted at a later date.

**•** `Customer Connected`  - the sales rep contacted the target.

**•** `Customer Engaged`  - the target engaged with an email.

**•** `Disqualified`  - a sales rep determined that the target isn’t qualified.

**•** `Duplicate`  - the target has a duplicate lead, contact, or person account record.

**•** `No Response`  - the target didn’t reply to any outreach.

**•** `Not Interested`  - the target stated a lack of interest.

**•** `Success`  - the cadence outreach was successful.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that the target completed the cadence. This field contains a value if the target’s
`State` is `Complete` . Possible values are:


Standard Objects ActionCadenceTracker

**Field** **Details**

**•** `AutomaticallyExited`                   - the target completed because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `AutomaticallyExitedDeletedStep`

**•** `AutomaticallyExitedInvalidParentStep`

**•** `DaisyChained`                   - the target completed because it’s connected to another action
cadence.

**•** `LeadConverted`                   - the target completed because the lead converted.

**•** `ManuallyRemoved`                   - the target completed because the sales rep removed it from
the cadence.

**•** `ManuallyRemovedNoAccess`                   - reserved for future use.

**•** `NoMoreSteps`                   - the target completed the action cadence because all the action
cadence steps were completed.

```
CurrentStepId

DaisyChainIteration

ErrorMessage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the current ActionCadenceStepTracker.

**Relationship Name**
CurrentStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of this action cadence in a sequence of linked action cadences followed by this
target. This value starts at 1 with the initial action cadence. A target can follow a sequence
of up to 10 linked action cadences. Available in API version 53.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If an error occurs while this target is being completed, this field contains the error message.


Standard Objects ActionCadenceTracker

**Field** **Details**

```
ExitGlobalRuleId

IsTrackerActive

LastCompletedStepId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If a global exit condition occurs, a target completes. One example of a global exit condition
is an email returned because of an invalid address. If the target completed because a global
exit condition occurred, this field contains the ID of the ActionCadenceRule record that
evaluated as `true` .

This field is available in API version 49.0 and later.

**Relationship Name**
ExitGlobalRule

**Relationship Type**
Lookup

**Refers To**
ActionCadenceRule

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action cadence target is active `(true)` or not `(false)` . The
default value is `false` . An action cadence target is active if the state is `Running`, `Paused`,
`Processing`, or `Initializing` . Only active targets count against the org limit of
150,000 trackers.

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the last completed ActionCadenceStepTracker.

**Relationship Name**
LastCompletedStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker


Standard Objects ActionCadenceTracker

**Field** **Details**

```
OwnerId

RelatedToAttributionType

RelatedToId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who is assigned to complete the cadence steps for the target.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines when the cadence is related to an opportunity or invoice. Available in API version
51.0 and later.

Possible values are:

**•** `Activation` —Attribute the opportunity to the cadence when the opportunity is
created.

**•** `Collected` —Attribute the value to the cadence after payment for the invoice is
collected.

**•** `Collection Advancement` —Attribute the value to the cadence when the invoice
is out for collection.

**•** `Maturation` —Attribute the opportunity to the cadence only when the opportunity
stage advances.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related opportunity if there’s one. Available in API version 51.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
RelatedTo

**Relationship Type**
Lookup


Standard Objects ActionCadenceTracker

**Field** **Details**

**Refers To**
Opportunity, Invoice

```
ScheduledResumeDateTime

State

TargetId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. Available in API version 53.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing` —Salesforce is working on changing the state of this action cadence
tracker. We recommend that you filter out steps that have this state from your dashboards.

**•** `Running`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the target that is assigned to this action cadence.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


### Standard Objects ActionCdncStpMonthlyMetric

Usage

Use ActionCadenceTracker to see what targets are currently assigned to an active action cadence.

```
   select TargetId from ActionCadenceTracker where ActionCadenceId=<Id of the action cadence>

    and State= "Running"

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

**ActionCadenceTrackerOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ActionCadenceTrackerShare on page 67**
Sharing is available for the object.

### ActionCdncStpMonthlyMetric

Represents the monthly engagement metrics for an action cadence step. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related action cadence step.

This is a relationship field.

**Relationship Name**
ActionCadenceStep


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Relationship Type**
This is an overview-detail relationship field, where ActionCadenceStep is the master object.

**Refers To**
ActionCadenceStep

```
AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with no call result specified.

**Type**
int


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Unqualified.

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of sent emails that were bounced for all recipients on the email. Bounced emails
aren’t marked as delivered. Available in API version 54.0 and later.

```
AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this step in the month.

**Type**
int


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this step in the month.
Available in API version 51.0 and later.

```
AllEmailsUntrackedSentCount

AllTotalCallsCount

DeliveredRecipientCount

DeliveredRecipientRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this step in the month. Available
in API version 51.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls with all call results for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that were successfully delivered an email. Available in API version
54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. Available in API version
54.0 and later.

This field is a calculated field.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
HardBounceTrackableSends

HasTemplateAssigned

HrdBncTrackableRecipientSends

IsCompoundMetric

LinkClickTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this step has an associated email template or call script. Available in API
version 52.0 and later.

The default value is 'false'.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. Available in API
version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When true, indicates that this metric represents engagement for a combination of the action
cadence step and a single email template. The value is true for all action cadence steps
created in Summer ’21 and later.

When false, indicates that the metric represents engagement for the action cadence step
and all email templates used on the step. The value is false for all action cadence steps created
in Spring ’21 and earlier. The default value is 'false'.

Available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent with link click tracking. Available in API version 54.0 and later.

```
LinkClkTrackableRecipientSends

Month

MonthInt

OooTrackableRecipientSends

OpenTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking. Available in API version
54.0 and later.

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
The month in which the engagement occurred, in `yyyymm` format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with out-of-office tracking. Out-of-office
tracking requires Inbox. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking. Available in API version
54.0 and later.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
OpenTrackableSends

OutOfOfficeTrackableSends

RecipientReplies

RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email. Available in API version 54.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique email recipients. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email. Hard bounces can mean that the
recipient's email address doesn't exist or is misspelled. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The number of recipients that responded with an out-of-office reply. Available in API version
54.0 and later.

```
RecipientsSoftBounced

ReplyTrackableRecipientSends

ReplyTrackableSends

SftBncTrackableRecipientSends

SoftBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email. A soft bounce often indicates a
temporary issue with the recipient's email server, such as a full inbox. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with reply tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking. Available in API
version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 54.0 and later.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
SomeEmailsDeliveredCount

SomeEmailsDeliveredRate

TemplateId

TrackableRecipientSendHrdBncRt

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the email template or call script associated with this step. Available in API version
52.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced. Available in API version 54.0 and later.

This field is a calculated field.


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

```
TrackableRecipientSendOooRate

TrackableRecipientSendReplyRt

TrackableRecipientSendSftBncRt

TrackableSendHardBounceRate

TrackableSendLinkClickRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects ActionCdncStpMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
54.0 and later.

This field is a calculated field.

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
The percentage of emails sent with open tracking that were opened by the recipient. Available
in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This field is a calculated field.


### Standard Objects ActionLinkGroupTemplate

**Field** **Details**

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
The number of unique recipients who clicked a link in an email for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email for this step in the month.

### ActionLinkGroupTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking on an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external
server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. Every action link belongs to an action
link group and action links within the group are mutually exclusive. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with the “Customize Application” permission can modify or delete this object.


Standard Objects ActionLinkGroupTemplate

Fields

**Field Name** **Details**

```
Category

DeveloperName

ExecutionsAllowed

HoursUntilExpiration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The location of the action link group within the feed element. Values are:

**•** `Primary` —The action link group is displayed in the body of the feed
element.

**•** `Overflow` —The action link group is displayed in the overflow menu of
the feed element.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template to use in code.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The number of times an action link can be executed. Values are:

**•** `Once` —An action link can be executed only once across all users.

**•** `OncePerUser` —An action link can be executed only once for each user.

**•** `Unlimited` —An action link can be executed an unlimited number of
times by each user. If the action link’s `actionType` is `Api` or `ApiAsync`,
you can’t use this value.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ActionLinkGroupTemplate

**Field Name** **Details**

**Description**
The number of hours from when the action link group is created until it's removed
from associated feed elements and can no longer be executed. The maximum
value is 8,760.

```
IsPublished

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, the action link group template is published. Action link group templates
shouldn’t be published until at least one ActionLinkTemplate is associated with
it. Once set to `true`, this can’t be set back to `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the `MasterLabel` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template.

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


### Standard Objects ActionLinkTemplate

**Field Name** **Details**

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

Usage

Define action link templates in Setup and use `ConnectApi` in Apex or Connect REST API to instantiate action links from the templates
and to post feed elements with the action links.

If you delete a published action link group template, you delete all related action link information which includes deleting all action links
that were instantiated using the template from feed items.

### ActionLinkTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external server
or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. This object is available in API version 33.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with the “Customize Application” permission can modify or delete this object.

Fields

**Field Name** **Details**

```
ActionLinkGroupTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ActionLinkGroupTemplate with which this action link template is
associated.

This is a relationship field.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

**Relationship Name**
ActionLinkGroupTemplate

**Relationship Type**
Lookup

**Refers To**
ActionLinkGroupTemplate

```
ActionUrl

Headers

IsConfirmationRequired

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The action link URL. For example, a `Ui` action link URL is a Web page. A
`Download` action link URL is a link to the file to download. `Ui` and `Download`
action link URLs are provided to clients. An `Api` or `ApiAsync` action link URL
is a REST resource. `Api` and `ApiAsync` action link URLs aren’t provided to
clients. Links to Salesforce can be relative. All other links must be absolute and
start with `https://` .

Links to resources hosted on Salesforce servers can be relative, starting with a
`/` . All other links must be absolute and start with `https://` . This field can
contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}`, for example,
`https://www.example.com/{!Bindings.itemId}` . Set the binding
variable’s value when you instantiate the action link group from the template.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP headers sent when corresponding action links are invoked.
This field can be used only for `Api` and `ApiAsync` action links. This field can
contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, a confirmation dialog appears before the action is executed.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

```
IsGroupDefault

Label

LabelKey

LinkType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, action links derived from this template are the default or primary action
in their action groups. There can be only one default action per action group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A custom label to display on the action link button. If none of the `LabelKey`
values make sense for an action link, use a custom label. Set the `LabelKey`
field to `None` and enter a label name in the `Label` field.

Action links have four states: new, pending, success, and failed. These strings are
appended to the label for each state:

**•** _Label_

**•** _Label_ Pending

**•** _Label_ Success

**•** _Label_ Failed

For example, if the value of `Label` is “Call Home,” the values of the four action
link states are: Call Home, Call Home Pending, Call Home Success, and Call Home
Failed.

If `LabelKey` has any value other than `None`, the `Label` field is empty.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Key for the set of labels to display for these action link states: new, pending,
success, failed. For example, the Approve set contains these labels: Approve,
[Pending, Approved, Failed. For a complete list of keys and labels, see Action Link](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)
[Labels in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm) _Connect REST API Developer Guide_ .

If none of the label key values make sense for an action link, set this field to `None`
and enter a custom label name in the `Label` field.

**Type**
picklist


Standard Objects ActionLinkTemplate

**Field Name** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action link. One of these values:

**•** `Api` —The action link calls a synchronous API at the action URL. Salesforce
sets the status to `SuccessfulStatus` or `FailedStatus` based on
the HTTP status code returned by your server.

**•** `ApiAsync` —The action link calls an asynchronous API at the action URL.
The action remains in a `PendingStatus` state until a third party makes
a request to `/connect/action-links/` _**`actionLinkId`**_ to set the
status to `SuccessfulStatus` or `FailedStatus` when the
asynchronous operation is complete.

**•** `Download` —The action link downloads a file from the action URL.

**•** `Ui` —The action link takes the user to a web page at the action URL.

```
Method

Position

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
HTTP method for the action URL. One of these values:

**•** `HttpDelete` —Returns HTTP 204 on success. Response body or output
class is empty.

**•** `HttpGet` —Returns HTTP 200 on success.

**•** `HttpHead` —Returns HTTP 200 on success. Response body or output class
is empty.

**•** `HttpPatch` —Returns HTTP 200 on success or HTTP 204 if the response
body or output class is empty.

**•** `HttpPost` —Returns HTTP 201 on success or HTTP 204 if the response
body or output class is empty. Exceptions are the batch posting resources
and methods, which return HTTP 200 on success.

**•** `HttpPut` —Return HTTP 200 on success or HTTP 204 if the response body
or output class is empty.

`Ui` and `Download` action links must use `HttpGet` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
An integer specifying the position of the action link template relative to other
action links in the group. 0 is the first position.


Standard Objects ActionLinkTemplate

**Field Name** **Details**

```
RequestBody

UserAlias

UserVisibility

```

Usage

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP request body sent when corresponding action links are
invoked. This field can be used only for `Api` and `ApiAsync` action links. This
field can contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If you selected `CustomUser` or `CustomExcludedUser` for
`UserVisibility`, this field is the alias for the custom user. Use the alias in
a template binding to specify the custom user when an action link group is
created using the template.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Who can see the action link. This value is set per action link, not per action link
group. One of these values:

**•** `Creator` —Only the creator of the action link can see the action link.

**•** `Everyone` —Everyone can see the action link.

**•** `EveryoneButCreator` —Everyone but the creator of the action link
can see the action link.

**•** `Manager` —Only the manager of the creator of the action link can see the
action link.

**•** `CustomUser` —Only the custom user can see the action link.

**•** `CustomExcludedUser` —Everyone but the custom user can see the
action link.

Create action link templates in Setup. Use Apex classes in the `ConnectApi` namespace or Connect REST API to instantiate action
links from templates and to post feed elements with the action links.


### Standard Objects ActionPlan

[For information about action links, see Working with Action Links in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/pages/connectapi_features_action_links.htm?search_text=working%20with%20action%20links) _Apex Developer Guide_ or the _Connect REST API Developer Guide_ .

### ActionPlan

Represents the instance of an action plan, a set of tasks created from an action plan template. This object is available in API version 44.0
and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

```

Fields

**Field Name** **Details**

### `ActionPlanState` `ActionPlanTemplateVersionId` `ActionPlanType`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The status of work being done for the action plan.

Possible values are:

**•** `Canceled`

**•** `Complete`

**•** `In Progress`

**•** `Not Started`

The default value is `Not Started` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the version of the action plan template used to create this action plan.
At creation, the referenced action plan template must be in the published state.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The action plan’s type.


Standard Objects ActionPlan

**Field Name** **Details**

Possible values are:

**•** `Industries`

**•** `Sales` —This value is available in API version 63.0 and later with the Sales
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** `Service`

```
IsLocked

IsUsingHolidayHours

LastReferencedDate

LastViewedDate

MayEdit

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the action plan is locked or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether task completion dates have been calculated by incrementing
the task offset for each non-work day, excluding recurring holidays.

**Type**
dateTime

**Properties**
Filter, Nllable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionPlan

**Field Name** **Details**

**Description**

Indicates whether the action plan can be edited or not.

```
Name

OwnerId

StartDate

TargetId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the action plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this record.

**Type**
date

**Properties**
Create, Default on create, Filter, Group, Sort

**Description**

The start date of the action plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the parent object record that relates to this action plan.

For API version 63.0 and later, supported parent objects are Account,
AccountPlanObjective, Applicant, ApplicationForm, ApplicationFormProduct,
Asset, BusinessLicense, BusinessMilestone, Campaign, Case, ChangeRequest,
Claim, Contact, Contract, FinancialGoal, Incident, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, Problem,
ResidentialLoanApplication, WorkOrder, and WorkOrderLineItem.

For API version 62.0 and later, supported parent objects are
ApplicationFormEvaluation and VettingEvaluation.

For API version 48.0 and later, supported parent objects are Account,
AssetsAndLiabilities, BusinessMilestone, Campaign, Card, Case, Claim, Contact,


### Standard Objects ActionPlanItem

**Field Name** **Details**

Contract, Financial Account, Financial Goal, Financial Holding, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent,
ResidentialLoanApplication, and Visit as well as custom objects with activities
enabled.

For API version 47.0 and later, supported parent objects are Account,
BusinessMilestone, Campaign, Case, Claim, Contact, Contract, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, and Visit as well
as custom objects with activities enabled.

For API version 46.0 and later, supported parent objects are Account, Campaign,
Case, Contact, Contract, Lead, and Opportunity as well as custom objects with
activities enabled.

For API version 45.0 and earlier, the only supported parent object is Account.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanItem

Represents the instance of an action plan item.This object is available in API version 44.0 and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanId

```

**Type**
reference


Standard Objects ActionPlanItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan that this item belongs to.

```
ActionPlanTemplateItemId

IsLocked

IsRequired

ItemEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the action plan template item this item was created from.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is locked or not. The default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is required or not.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of object used with the item. This field is available in API version 61.0
and later.

Possible values are:

**•** `AssessmentTask` —Assessment Task

**•** `DocumentChecklistItem` —Document Checklist Item

**•** `Event` -Available only with sales action plans in API version 63.0 and later
with the Sales Action Plans add-on license and the Sales Action Plans default
permission set.


Standard Objects ActionPlanItem

**Field Name** **Details**

**•** `GenericVisitTask` —Generic Visit Task

**•** `OtherComponentTask` —Other Component Task

**•** `RecordAction`

**•** `SignatureTask` —Signature Task

**•** `Task`

```
ItemId

ItemState

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the record created by this action plan item. This field is a polymorphic
relationship field.

**Relationship Name**
Item

**Refers To**
DocumentChecklistItem, Event, RecordAction, Task

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan item’s work state.

Possible values are:

**•** `Canceled`

**•** `Completed`

**•** `Deleted`

**•** `In Progress`

**•** `Pending`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan item.


### Standard Objects ActionPlanTemplate

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanItemFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanItemHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanItemShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplate

Represents the instance of an action plan template. This object is available in API version 44.0 and later.

Supported Calls

`create()delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`,

Fields

**Field Name** **Details**

```
ActionPlanType

Category

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

This action plan template’s type. Possible values are:

**•** `Industries`

**•** `Sales` —This value is available in API version 63.0 and later with the Sales
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** Service

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Description**
Specifies the category that the action plan template belongs to.

Available in API version 64.0 and later.

Possible values are:

**•** `Onboarding`

**•** `Application`

```
Description

EstimatedCompletionDays

FileBasedTemplatePath

IsAdHocItemCreationEnabled

IsLocked

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The description of this action plan template.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated number of days to complete the action plan.

Available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The path of the file based template using which the action plan template is
created.

Available in API version 64.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can add tasks or other items to generated action plans
( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template is locked or not. The default value is
`false` .

```
LastReferencedDate

LastViewedDate

MayEdit

Name

OwnerId

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template can be edited or not. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**Description**

The ID of the user who owns this action plan template. This field is a polymorphic
relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
SourceType

Status

Subcategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the source type to which the action plan template belongs to.

Available in API version 64.0 and later.

Possible values are:

**•** `CRM`

**•** `MigratedFromSandbox`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The status of this action plan template.

Possible values are:

**•** `Draft`

**•** `Final—Published`

**•** `Obsolete`

**•** `ReadOnly`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The subcategory to which the action plan template belongs.

Available in API version 64.0 and later.

Possible values are:


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**•** `Product Onboarding`

**•** `Customer Onboarding`

```
TargetEntityType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Restricted picklist, Sort

**Description**

The parent object this action plan template relates to.

Possible values are organized by the API version in which they were introduced.
Values are available in all versions after introduction unless noted otherwise.

API Version 62.0 and later with Financial Services:

**•** `AccountPlanObjective`

**•** `FinancialDeal`

**•** `PartyProfile`

API Version 62.0 and later with Public Sector Solutions:

**•** `ApplicationFormEvaluation`

**•** `VettingEvaluation`

API version 60.0 and later with Education Cloud

**•** `ProgramEnrollment`

API version 58.0 and later with Health Cloud

**•** `CareBarrier`

API version 58.0 and later with Nonprofit Cloud:

**•** `Benefit`

**•** `Program`

API Version 58.0 and later with Public Sector Solution and Education Cloud:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Program`

API Version 56.0 and later with Automotive Cloud:

**•** `Account`

**•** `Asset`

**•** `Asset Account Participant`

**•** `Asset Contact Participant`

**•** `Asset Milestone`

**•** `Fleet`


Standard Objects ActionPlanTemplate

**Field Name** **Details**

**•** `Lead`

**•** `Opportunity`

**•** `Record Alert`

**•** `Vehicle`

**•** `Case`

**•** `Claim`

**•** `Contact`

API Version 58.0 and later with Grantmaking:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Budget`

**•** `BudgetAllocation`

**•** `CareBarrier`

**•** `FundingAward`

**•** `FundingAwardAmendment`

**•** `FundingAwardRequirement`

**•** `FundingDisbursement`

**•** `FundingOpportunity`

**•** `Program`

API Version 52.0 and later:

**•** `BusinessLicenseApplication`

**•** `IndividualApplication`

**•** `PublicComplaint`

**•** `RegulatoryCodeViolation`

**•** `ViolationEnforcementAction`

API Version 47.0 and later:

**•** `BusinessMilestone`

**•** `Claim`

**•** `InsurancePolicy`

**•** `InsurancePolicyCoverage`

**•** `PersonLifeEvent`

**•** `Visit`

API Version 46.0 and later:

**•** `Campaign` —Unsupported for Grantmaking.

**•** `Case`

**•** `Contact`


### Standard Objects ActionPlanTemplateItem

**Field Name** **Details**

**•** `Contract`

**•** `Lead`

**•** `Opportunity`

**•** `Custom objects with activities enabled`

API Version 44.0 and later:

Account

```
UniqueName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template. This field is unique within your
organization.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplateItem

Represents the instance of an item on an action plan template version. This object is available in API version 44.0 and later.

Supported Calls

```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

```


Standard Objects ActionPlanTemplateItem

Fields

**Field Name** **Details**

```
ActionPlanTemplateVersionId

DisplayOrder

IsActive

IsLocked

IsRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**

The version of the action plan template this item is for.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The order in which this item is displayed within the action plan template version.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item is locked or not. The default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is required. The default
value is `false` .


Standard Objects ActionPlanTemplateItem

**Field Name** **Details**

```
ItemEntityType

LastReferencedDate

LastViewedDate

MayEdit

Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of action plan template item entity..

Possible values are:

**•** `Document Checklist Item`

**•** `Event` —This value is available in API version 63.0.

**•** `RecordAction`

**•** `Task`

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item can be edited or not. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, idLookup, Update


### Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Description**

The unique identifier for this action plan template item record.

```
UniqueName

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template item. This field is unique within
your organization.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateItemFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateItemHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateItemShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActionPlanTemplateItemValue

Represents the value associated with an action plan template item. This object is available in API version 44.0 and later.

Supported Calls

```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanTemplateItemId

```

**Type**
reference


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan template item that this value relates to.

**Relationship Name**
ActionPlanTemplateItem

**Relationship Type**
Master-detail

**Refers To**
ActionPlanTemplateItem (the master object)

```
IsActive

IsLocked

ItemEntityFieldName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item value is locked or not. The
default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The name of the field on the action plan template item that this value is for.
Available fields include:

**•** `AssessmentTask.AssessmentTaskDefinitionId` —Assessment
Task Definition ID

**•** `AssessmentTask.AssignedToId` —AssignedTo ID

**•** `AssessmentTask.Description` —Description

**•** `AssessmentTask.EndTime` —End Time

**•** `AssessmentTask.IsRequired` —Required


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `AssessmentTask.Name` —Name

**•** `AssessmentTask.OwnerId` —Owner ID

**•** `AssessmentTask.ParentId` —Visit ID

**•** `AssessmentTask.ReferenceRecordId` —ReferenceRecord ID

**•** `AssessmentTask.SequenceNumber` —Sequence

**•** `AssessmentTask.StartTime` —Start Time

**•** `AssessmentTask.Status` —Status

**•** `AssessmentTask.TaskDefinitionId` —TaskDefinition ID

**•** `AssessmentTask.TaskType` —Task Type

**•** `DocumentChecklistItem.Comments` —Comments

**•** `DocumentChecklistItem.DocumentCategoryId` —Document
Category ID

**•** `DocumentChecklistItem.DocumentTypeId` —Document Type
ID

**•** `DocumentChecklistItem.Instruction` —Instructions

**•** `DocumentChecklistItem.IsAccepted` —Accepted

**•** `DocumentChecklistItem.IsFrozen` —Frozen

**•** `DocumentChecklistItem.IsRequired` —Required

**•** `DocumentChecklistItem.Name` —Name

**•** `DocumentChecklistItem.OwnerId` —Owner ID

**•** `DocumentChecklistItem.ParentRecordId` —Parent Record ID

**•** `DocumentChecklistItem.ReceivedDocumentId` —Received
Document ID

**•** `DocumentChecklistItem.Status` —Status

**•** `DocumentChecklistItem.ValidatedById` —User ID

**•** `DocumentChecklistItem.ValidationDateTime` —Validation
Date Time

**•** `DocumentChecklistItem.WhoId` —Who ID

**•** `Event.ActivityDate` —Due Date Only

**•** `Event.ActivityDateTime` —Due Date Time

**•** `Event.Description` —Description

**•** `Event.DurationInMinutes` —Duration

**•** `Event.EndDateTime` —End Date Time

**•** `Event.EventSubtype` —Event Subtype

**•** `Event.IsAllDayEvent` —All-Day Event

**•** `Event.IsPrivate` —Private

**•** `Event.IsRecurrence` —Create Recurring Series of Events

**•** `Event.IsReminderSet` —Reminder Set

**•** `Event.Location` —Location


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `Event.OwnerId` —Assigned To ID

**•** `Event.Recurrence2PatternText` —Recurrence Pattern

**•** `Event.RecurrenceDayOfMonth` —Recurrence Day of Month

**•** `Event.RecurrenceDayOfWeekMask` —Recurrence Day of Week
Mask

**•** `Event.RecurrenceEndDateOnly` —Recurrence End

**•** `Event.RecurrenceInstance` —Recurrence Instance

**•** `Event.RecurrenceInterval` —Recurrence Interval

**•** `Event.RecurrenceMonthOfYear` —Recurrence Month of Year

**•** `Event.RecurrenceStartDateTime` —Recurrence Start

**•** `Event.RecurrenceTimeZoneSidKey` —Recurrence Time Zone

**•** `Event.RecurrenceType` —Recurrence Type

**•** `Event.ReminderDateTime` —Reminder Date/Time

**•** `Event.ShowAs` —Show Time As

**•** `Event.StartDateTime` —Start Date Time

**•** `Event.Subject` —Subject

**•** `Event.Type` —Type

**•** `Event.WhatId` —Related To ID

**•** `Event.WhoId` —Name ID

**•** `GenericVisitTask.DefinitionReferenceId` —Generic Visit
Task ID

**•** `GenericVisitTask.Description` —Description

**•** `GenericVisitTask.EndDateTime` —End Date Time

**•** `GenericVisitTask.IsRequired` —Required

**•** `GenericVisitTask.Name` —Name

**•** `GenericVisitTask.OwnerId` —Owner ID

**•** `GenericVisitTask.Sequence` —Sequence

**•** `GenericVisitTask.StartDateTime` —Start Date Time

**•** `GenericVisitTask.Status` —Status

**•** `GenericVisitTask.VisitId` —Visit ID

**•** `OtherComponentTask.Description` —Description

**•** `OtherComponentTask.FullyQualifiedName` —Fully Qualified
Name

**•** `OtherComponentTask.Name` —Name

**•** `OtherComponentTask.OwnerId` —Owner ID

**•** `OtherComponentTask.ParentTaskId` —Assessment Task ID

**•** `OtherComponentTask.ParticipantRoleId` —ParticipantRole
ID

**•** `RecordAction.ActionDefinition` —Action Definition


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `RecordAction.ActionType` —Action Type

**•** `RecordAction.FlowDefinition` —Interaction Definition ID

**•** `RecordAction.FlowInterviewId` —FlowInterview ID

**•** `RecordAction.IsMandatory` —Is Mandatory

**•** `RecordAction.IsUiRemoveHidden` —Hide Remove Action in UI

**•** `RecordAction.Order` —Order

**•** `RecordAction.ParticipantRoleId` —ParticipantRole ID

**•** `RecordAction.Pinned` —Pinned

**•** `RecordAction.RecordId` —Parent Record ID

**•** `RecordAction.Status` —Status

**•** `SignatureTask.Description` —Description

**•** `SignatureTask.Name` —Name

**•** `SignatureTask.ParentTaskId` —Assessment Task ID

**•** `Task.APT_Custom_Text_1_c__c` —APT Custom Text - 1

**•** `Task.ActivityDate` —Due Date Only

**•** `Task.Boolean_Test__c` —Boolean Test

**•** `Task.CallDisposition` —Call Result

**•** `Task.CallDurationInSeconds` —Call Duration

**•** `Task.CallObject` —Call Object Identifier

**•** `Task.CallType` —Call Type

**•** `Task.Custom_Picklist__c` —Custom Picklist

**•** `Task.Description` —TEstActivityDEs

**•** `Task.IsRecurrence` —Create Recurring Series of Tasks

**•** `Task.IsReminderSet` —Reminder Set

**•** `Task.OwnerId` —Assigned To ID

**•** `Task.Priority` —Priority

**•** `Task.RecurrenceDayOfMonth` —Recurrence Day of Month

**•** `Task.RecurrenceDayOfWeekMask` —Recurrence Day of Week Mask

**•** `Task.RecurrenceEndDateOnly` —Recurrence End

**•** `Task.RecurrenceInstance` —Recurrence Instance

**•** `Task.RecurrenceInterval` —Recurrence Interval

**•** `Task.RecurrenceMonthOfYear` —Recurrence Month of Year

**•** `Task.RecurrenceRegeneratedType` —Repeat This Task

**•** `Task.RecurrenceStartDateOnly` —Recurrence Start

**•** `Task.RecurrenceTimeZoneSidKey` —Recurrence Time Zone

**•** `Task.RecurrenceType` —Recurrence Type

**•** `Task.ReminderDateTime` —Reminder Date/Time

**•** `Task.Status` —Status


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**•** `Task.Subject` —Subject

**•** `Task.TaskSubtype` —Task Subtype

**•** `Task.Type` —Type

**•** `Task.WhatId` —Related To ID

**•** `Task.WhoId` —Name ID

**•** `Task.test__c` —test

**•** `Task.text_3__c` —text 3

```
ItemEntityType

LastReferencedDate

LastViewedDate

MayEdit

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of action plan template item.

Possible values are:

**•** `Document Checklist Item`

**•** `Event` —Available in API version 63.0 and later with the Sales Action Plans
add-on license and the Sales Action Plans default permission set.

**•** `RecordAction`

**•** `Task`

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ActionPlanTemplateItemValue

**Field Name** **Details**

**Description**

Indicates whether this action plan template item value can be edited or not. The
default value is `false` .

```
Name

ValueFormula

ValueLiteral

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique identifier for this record.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A formula used to calculate the value for this action plan template item.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**

The value for this action plan template item.

This object has the following associated objects. If the API version isn't specified, they're available in the same API versions as this object.
Otherwise, they're available in the specified API version and later.

**[ActionPlanTemplateItemValueChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateItemValueFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateItemValueHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateItemValueOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateItemValueShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects ActionPlanTemplateVersion ActionPlanTemplateVersion

Represents the version of an action plan template. This object is available in API version 44.0 and later.

Supported Calls

```
   create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search

   ( )undelete()update()upsert()

```

Fields

**Field Name** **Details**

```
ActionPlanTemplateId

ActivationDateTime

InactivationDateTime

IsLocked

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Filter, Group, Sort

**Description**

The ID of the action plan template this version represents.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort,

**Description**

The date and time at which this version became active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

The date and time at which this version became inactive.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version is locked or not. The default
value is `false` .


Standard Objects ActionPlanTemplateVersion

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

MayEdit

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort,, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version can be edited. The default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update,

**Description**

The name of this version item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan template version’s state. Possible values are:

**•** `Draft`

**•** `Final – Published`

**•** `Obsolete`

**•** `ReadOnly`


### Standard Objects ActiveFeatureLicenseMetric

**Field Name** **Details**

```
Version

```

Associated Objects

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

The index number of this action plan template version.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ActionPlanTemplateVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ActionPlanTemplateVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ActionPlanTemplateVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateVersionShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### ActiveFeatureLicenseMetric

Represents the number of active, assigned, and purchased feature licenses in the org. This object is available in API version 52.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license who have logged in within the last 30 days.


Standard Objects ActiveFeatureLicenseMetric

**Field** **Details**

```
AssignedUserCount

FeatureType

MetricsDate

TotalLicenseCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of feature license.

Possible values are:

**•** `AvantgoUser` —AvantGo User

**•** `ChatterAnswersUser` —Chatter Answers User

**•** `InteractionUser` —Flow User

**•** `JigsawProspectingUser` —Data.com User

**•** `KnowledgeUser` —Knowledge User

**•** `LiveAgentUser` —Chat User

**•** `MarketingUser` —Marketing User

**•** `MobileUser` —Apex Mobile User

**•** `OfflineUser` —Offline User

**•** `SFContentUser` —Salesforce CRM Content User

**•** `SiteforceContributorUser` —Site.com Contributor User

**•** `SiteforcePublisherUser` —Site.com Publisher User

**•** `SupportUser` —Service Cloud User

**•** `WirelessUser` —Wireless User

**•** `WorkDotComUserFeature` —WDC User

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that feature license metrics were collected.

**Type**
int


### Standard Objects ActivePermSetLicenseMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of feature licenses in the organization.

### ActivePermSetLicenseMetric

Represents the number of active, assigned, and purchased permission set licenses in the org. This object is available in API version 52.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

AssignedUserCount

DeveloperName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license who have logged in within the last 30
days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of this permission set license object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must begin


Standard Objects ActivePermSetLicenseMetric

**Field** **Details**

with a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

```
MasterLabel

MetricsDate

PermissionSetLicenseId

TotalLicenses

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the permission set license.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that permission set license metrics were collected.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the permission set license.

This is a relationship field.

**Relationship Name**
PermissionSetLicense

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicense

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of this permission set licenses that are available to your org.


### Standard Objects ActiveProfileMetric ActiveProfileMetric

Represents the profile associated with the active, assigned, and purchased user licenses. This object is available in API version 52.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActiveUserCount

AssignedUserCount

MetricsDate

ProfileId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile who have logged in within the last 30 days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that profile metrics were collected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the profile.

This is a relationship field.

**Relationship Name**
Profile


### Standard Objects ActiveScratchOrg

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Profile

```
UserLicenseId

### ActiveScratchOrg

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user license.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense

Represents an active scratch org. This object is available in API version 41.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
update()

```

Fields

**Field Name** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this scratch org.


Standard Objects ActiveScratchOrg

**Field Name** **Details**

```
Edition

ExpirationDate

Features

HasSampleData

LastLoginDate

LastReferencedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org edition of this scratch org. Possible values are `Group`, `Developer`,
`Enterprise`, and `Professional` . This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org expires. This field is read only.

**Type**
textarea

**Properties**
Nillable

**Description**
The features enabled in this scratch org, such as `MultiCurrency` . See the
_Salesforce DX Developer Guide_ for the full list of valid features. This field is read
only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the scratch org contains sample data. If set to `true`, the
sample data is similar to the data in a Salesforce free trial org.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date of the last user login to the scratch org. This field is read only.

**Type**
dateTime


Standard Objects ActiveScratchOrg

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record. This field is read only.

```
LastViewedDate

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
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated ID of this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace associated with this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the scratch org. This field is read only.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this scratch org. This field is read only.


Standard Objects ActiveScratchOrg

**Field Name** **Details**

```
ScratchOrg

ScratchOrgInfoId

SignupEmail

SignupInstance

SignupTrialDays

SignupUsername

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The org ID of the scratch org. This field is read only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The id of the associated `ScratchOrgInfo` object. This field is read only.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the Administration user. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce instance on which this scratch org resides. This field is read only.

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
Filter, Group, Nillable, Sort


Standard Objects ActiveScratchOrg

**Field Name** **Details**

**Description**
The username of the Administration user of the scratch org. This field is read only.

```
Snapshot

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this scratch org was created from a scratch org snapshot, then this field contains
either the name or ID of the snapshot. Specifically, the name corresponds to the
`Name` field of the snapshot’s record in the OrgSnapshot standard object; the ID
corresponds to the record ID.

If this scratch org wasn’t created from a snapshot, this field is empty. This field is
read only.

This field is available in API version 61.0 and later.

Salesforce automatically creates an instance of this object after a `ScratchOrgInfo` record moves to the Active state. The new
`ActiveScratchOrg` gets many of its field values from the `ScratchOrgInfo` object with which it’s associated.

When you delete an `ActiveScratchOrg` record, its associated scratch org is deleted and its associated `ScratchOrgInfo`
record is moved to the Deleted state.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ActiveScratchOrgFeed**

Feed tracking is available for the object.

**ActiveScratchOrgHistory**

History is available for tracked fields of the object.

**ActiveScratchOrgShare**

Sharing is available for the object.

SEE ALSO:

ScratchOrgInfo

NamespaceRegistry

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev)_


### Standard Objects ActivityFieldHistory ActivityFieldHistory

Represents a change in a field value for a tracked object or field. This object is a big object. This object is available in API version 55.0 and
later.

Supported Calls

`delete()describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, users must have ViewAllData permissions.

Fields

**Field** **Details**

```
ActivityId

ChangedById

ChangedDate

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the task or event that changed.

This field is a polymorphic relationship field.

**Relationship Name**
### Activity

**Refers To**
Event, Task

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the user who made the change.

This field is a relationship field.

**Relationship Name**
ChangedBy

**Refers To**
User

**Type**
dateTime


Standard Objects ActivityFieldHistory

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The date the field value changed.

```
DataType

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The type of the field with the changed value.

Possible values are:

**•** `Address`

**•** `AnyType`

**•** `AutoNumber`

**•** `Base64`

**•** `BitVector`

**•** `Boolean`

**•** `Content`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `DateOnly`

**•** `DateTime`

**•** `Division`

**•** `Double`

**•** `DynamicEnum`

**•** `Email`

**•** `EncryptedBase64`

**•** `EncryptedText`

**•** `EntityId`

**•** `EnumOrId`

**•** `ExternalId`

**•** `Fax`

**•** `File`

**•** `HtmlMultiLineText`

**•** `HtmlStringPlusClob`

**•** `InetAddress`

**•** `Json`


Standard Objects ActivityFieldHistory

**Field** **Details**

**•** `Location`

**•** `MultiEnum`

**•** `MultiLineText`

**•** `Namespace`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Raw`

**•** `RecordType`

**•** `SfdcEncryptedText`

**•** `SimpleNamespace`

**•** `StringPlusClob`

**•** `Switchable_PersonName`

**•** `Text`

**•** `TimeOnly`

**•** `Url`

**•** `YearQuarter`

```
FieldName

IsDataAvailable

NewValueDateTime

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the field changed.

**Type**
boolean

**Properties**
Defaulted on create

**Description**
Indicates whether valid data is available in the old and new value fields. This field is `false`
if, for example, the fields are encrypted or the changed values are too large, such as for
Description field types.

The default value is `false` .

**Type**
dateTime

**Properties**
Nillable


Standard Objects ActivityFieldHistory

**Field** **Details**

**Description**
The new value for date type fields.

```
NewValueNumber

NewValueText

OldValueDateTime

OldValueNumber

OldValueText

Operation

```

**Type**
double

**Properties**
Nillable

**Description**
The new value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The new value for all other field types that are not a date or number type.

**Type**
dateTime

**Properties**
Nillable

**Description**
Old value for date type fields.

**Type**
double

**Properties**
Nillable

**Description**
Old value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The old value for all other field types that are not a date or number type.

**Type**
picklist

**Properties**
Restricted picklist


### Standard Objects ActivityHistory

**Field** **Details**

**Description**
The operation of the field value change.

Possible values are:

**•** `delete`

**•** `update`

Indexed Fields

When you're querying ActivityFieldHistory with SOQL, you must specify indexed fields in the `WHERE` clause filter starting from the first
field defined in the index. If you specify a partial list of indexed fields, don't leave any gaps between indexed fields after the first field.
Here are the indexed fields for ActivityFieldHistory, listed from first to last in the index order.

1. `ActivityId`

2. `ChangedDate`

3. `ChangedById`

4. `FieldName`

5. `ActivityFieldChange`

For example, this SOQL query succeeds because the first three indexed fields are in the `WHERE` clause.

```
   SELECT ActivityId, OldValueText, NewValueText, FieldName, ChangedDate

   FROM ActivityFieldHistory

   WHERE ActivityId = 'SomeId' AND ChangedDate >= :startDate AND ChangedDate <= :endDate

   ORDER BY ChangedDate

```

If you remove the `ActivityId` field from the `WHERE` clause, the query fails.

```
   SELECT ActivityId, OldValueText, NewValueText, FieldName, ChangedDate

   FROM ActivityFieldHistory

   WHERE ChangedDate >= :startDate AND ChangedDate <= :endDate

   ORDER BY ChangedDate

```

SEE ALSO:

[Big Objects Implementation Guide: SOQL with Big Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.bigobjects.meta/bigobjects/big_object_querying.htm)

[Big Objects Implementation Guide: Big Objects](https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object.htm)

### ActivityHistory

This read-only object is displayed in a related list of closed activities—past events and closed tasks—related to an object. It includes
activities for all contacts related to the object. ActivityHistory fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.


Standard Objects ActivityHistory

Supported Calls

```
   describeSObjects()

```

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
AccountId

ActivityDate

ActivityDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the related account, which is determined as follows:

**•** The account associated with the `WhatId`, if it exists; or

**•** The account associated with the `WhoId`, if it exists; otherwise

**•** `null`

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates one of the following:

**•** The due date of a task

**•** The due date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time Coordinated
(UTC) time zone. The time stamp doesn’t represent the time of the activity; don’t attempt
to alter it to accommodate time zone differences. Label is `Date` .

**Type**
dateTime


Standard Objects ActivityHistory

**Field** **Details**

**Properties**
Aggregate, Filter, Nillable, Sort

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` . The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is **Due Date Time** .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

```
ActivitySubtype

ActivityType

AlternateDetailId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.
This field isn’t updateable.

Possible values are:

**•** Task

**•** Email

**•** Call

**•** Event

**•** LinkedIn —Available in API version 56.0 and later.

**•** List Email

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents one of the following values: `Call`, `Email`, `Meeting`, or `Other` . Label is
`Type` . These are default values, and can be changed.

`ActivityType` is the union of `TaskType` and `EventType` . If the same activity appears
in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are distinct from
each other.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ActivityHistory

**Field** **Details**

**Description**
The ID of a record the activity is related to which contains more details about the activity.
For example, an activity can be related to an EmailMessage record.

This is a relationship field.

**Relationship Name**
AlternateDetail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
CallDisposition

CallDurationInSeconds

CallObject

CallType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Duration of the call in seconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of a call center. Limit is 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of call being answered: Inbound, Internal, or Outbound.


Standard Objects ActivityHistory

**Field** **Details**

```
CompletedDateTime

ConnectionReceivedId

ConnectionSentId

Description

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.

**•** For insert, if the task is saved with a Closed status the field is set. If the task is saved with
an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is no change
to the field.

Note: The status is a dynamic enum. If the Closed mapping is changed it won’t cause
an update of existing tasks. Only new insert/update operations are affected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that shared this record with your
organization. This field is available only if your organization has enabled Salesforce to
Salesforce and only in API versions 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that your organization shared this record
with. This field is available only if your organization has enabled Salesforce to Salesforce, and
only in API versions 28.0 and later. The value is always `null` . You can use the
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Nillable

**Description**

Contains a description of the event or task. Limit is 32 KB.


Standard Objects ActivityHistory

**Field** **Details**

```
Division

DurationInMinutes

EndDateTime

IsAllDayEvent

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Indicates the duration of the event or task.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0 and later. This
field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a full day, and
the `ActivityDate` defines the date of the event. If the value of this field is set to `false`,
then the activity may be an event spanning less than a full day, or it may be a task. The default
value of this field is `false` . Label is `All-Day Event` .


Standard Objects ActivityHistory

**Field** **Details**

```
IsClosed

IsDeleted

IsHighPriority

IsOnlineMeeting

IsReminderSet

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default value of this
field is `false` . This field is set indirectly by setting the `Status` field on the task—each
picklist value has a corresponding `IsClosed` value. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the activity has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. This field is derived from the `Priority` field. The default
value of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**

Indicates whether the activity represents an online meeting ( `true` ) or not ( `false` ).

Note: This field is not available in API version 16.0 or later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ).The default value
of this field is `false` .


Standard Objects ActivityHistory

**Field** **Details**

```
IsTask

IsVisibleInSelfService

Location

OwnerId

PrimaryAccountId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If the value of this field is set to `true`, then the activity is a task. If the value is set to `false`,
then the activity is an event. The default value of this field is `false` . Label is `Task` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If the value of this field is set to `true`, then the activity can be viewed in the self-service
portal. The default value of this field is `false` . Label is `Visible in Self-Service` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

If the activity is an event, then this field contains the location of the event. If the activity is a
task, then the value is `null` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Indicates the ID of the user or group who owns the activity.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

**Type**
reference


Standard Objects ActivityHistory

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `AccountId` value from the activity record. Available in API versions 30.0 and
later to organizations that use Shared Activities.

```
PrimaryWhoId

Priority

ReminderDateTime

StartDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `WhoId` value from the activity record. Available in API versions 30.0 and later
to organizations that have enabled Shared Activities.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of this field is
`Normal` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time when the reminder is scheduled to fire, if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then the user may have deselected the
reminder checkbox in the Salesforce user interface, or the reminder has already fired at the
time indicated by the value.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

Indicates the start date and time of the event.

Available in versions 29.0 and later.

If the event’s `IsAllDayEvent` flag is set to true (indicating an all-day event), then the
time stamp in `StartDateTime` is always set to midnight in the Coordinated Universal
Time (UTC) time zone.


Standard Objects ActivityHistory

**Field** **Details**

Note: Don’t attempt to alter the time stamp to account for any time zone differences.

If the event’s `IsAllDayEvent` flag is set to false, then you must translate the time portion
of the time stamp in `StartDateTime` to or from a local time zone for the user or the
application, as appropriate. The translation must be in the Coordinated Universal Time (UTC)
time zone.

If this field has a value, then `ActivityDate` and `ActivityDateTime` either must
be null or must match the value of this field.

If the activity is a task, `StartDateTime` is null

```
Status

Subject

WhatId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Indicates the current status of a task,. The default value of this field is `Not Started` . Each
predefined status field sets a value for `IsClosed` . To obtain picklist values, query TaskStatus.

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

**Type**
combobox

**Properties**
Filter, Nillable, Sort

**Description**

Contains the subject of the task or event.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatId` s are polymorphic. Polymorphic means a `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID` .

This is a polymorphic relationship field.


Standard Objects ActivityHistory

**Field** **Details**

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant, ContactRequest,
Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo, DelegatedAccount,
DocumentChecklistItem, EnrollmentEligibilityCriteria, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
ListEmail, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .


Standard Objects ActivityHistory

**Field** **Details**

If your organization uses Shared Activities, when you query activities in API version 30.0 or
later, the returned value of the `WhoId` field matches the value in the queried object, not
necessarily in the activity record itself.

If Shared Activities is enabled, the value of this field is not populated and the field
`PrimaryWhoId` should be queried instead.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

**Query activities that are related to an object**

**1.** Optionally, issue a describe call against the object whose activities you wish to query, to get a suggestion of the correct SOQL
to use.

**2.** Issue a SOQL relationship query with a main clause that references the object, and an inner clause that references the activity
history; for example:

```
       SELECT

        (SELECT ActivityDate, Description

         FROM ActivityHistories)

       FROM Account

       WHERE Name Like 'XYZ%'

```

The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following constraints on users who don’t have the “View All Data” permission help prevent performance issues.

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with “A.” Instead, you must reference a single account record.

```
       SELECT

        (SELECT ActivityDate, Description

         FROM ActivityHistories

         ORDER BY ActivityDate DESC NULLS LAST, LastModifiedDate DESC

         LIMIT 500)

       FROM Account

       WHERE Name = 'Acme'

       LIMIT 1

```

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.


### Standard Objects ActivityMetric

**•** In the inner clause of the query, you must sort on `ActivityDate` in descending order and `LastModifiedDate` in
descending order. You can optionally display nulls last. For example: `ORDER BY ActivityDate DESC NULLS LAST,`
`LastModifiedDate DESC` .

SEE ALSO:

Task

### ActivityMetric

Represents activities that were added to Salesforce automatically by Einstein Activity Capture and manually by users.

This object is available in API version 45.0.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Unless otherwise noted, Einstein Activity Capture and Activity Metrics must be enabled.

Fields

**Field** **Details**

```
BaseId

BaseType

FirstCallDateTime

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort

**Description**
The ID of the record that the activities apply to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entity that corresponds to the BaseId

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ActivityMetric

**Field** **Details**

**Description**
Indicates the date when the first call was made. This field is available only to Sales Engagement
users. Einstein Activity Capture and Activity Metrics aren’t required.

```
FirstEmailDateTime

InactiveDays

LastActivityDateLastModDate

LastActivityDateTime

LastCallDateLastModDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the first email was sent. This field is available only to Sales
Engagement users. Einstein Activity Capture and Activity Metrics aren’t required.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the number of days since the most recent activity was completed. This field is
derived from the Last Activity Date field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastActivityDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent activity was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastCallDateTime field was last modified.


Standard Objects ActivityMetric

**Field** **Details**

```
LastCallDateTime

LastEmailDateLastModDate

LastEmailDateTime

LastEmailReceivedDateTime

LastEmailSentDateTime

LastEventDateLastModDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent call was made through Sales Dialer or Inbox.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastEmailDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent or received.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was received.

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent.

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ActivityMetric

**Field** **Details**

**Description**
Indicates when the LastEventDateTime field was last modified.

```
LastEventDateTime

LastTaskDateLastModDate

LastTaskDateTime

NextActivityDateLastModDate

NextActivityDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent event was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastTaskDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the last task was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the NextActivityDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date of the next scheduled task or event. Only open tasks in the future are
included.


### Standard Objects ActivityUsrConnectionStatus

Usage

Use this object to see data about sales activities that were added to Salesforce manually and by Einstein Activity Capture. Activity Metric
fields are derived from your activity data. For example, the Inactive Days field indicates the number of days since the most recent activity
was completed. Create a trigger that notifies a user when there isn’t any activity on an account for a certain amount of time.

### ActivityUsrConnectionStatus

Represents the status of the email connections for Einstein Activity Capture users. You can also see whether users accepted the required
terms of service to capture emails. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, enable Einstein Activity Capture in your org.

Fields

**Field** **Details**

```
ConfigurationName

ConnectivityStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Einstein Activity Capture configuration that the user is assigned to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user’s email connection.

Possible values are:

**•** `ACTIVE`

**•** `DISABLED`

**•** `INITIALIZING`

**•** `NEEDSATTENTION`

**•** `NEEDSATTENTIONGLOBAL` (used when an org-level connection isn’t working)


Standard Objects ActivityUsrConnectionStatus

**Field** **Details**

**•** `NEEDSATTENTIONHYBRID` (used when both org-level and user-level connections
aren’t working)

**•** `PENDING`

**•** `PROCESSING`

```
ContactsSynced

EmailAddress

EventsSynced

ExternalId

GlobalOauthTermsState

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of contacts synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address that’s used to capture and sync data between Salesforce and the user’s
Microsoft or Google account.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of events synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ActivityUsrConnectionStatus

**Field** **Details**

**Description**
Indicates the user’s terms of service status. When emails are enabled for Einstein Activity
Capture, each user must accept the terms of service.

Possible values are:

**•** `ACCEPTED`

**•** `DECLINED`

**•** `PENDING`

This field is available only if you use an org-level OAuth 2.0 or a service account authentication
method. In connection report CSV files downloaded from Einstein Activity Capture Status &
Metrics, this field is labeled Global Auth User Email Consent Status.

```
IsTermsOfServiceAccepted

RecommendedActionDescription

RecommendedActionTitle

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has accepted the Einstein Activity Capture terms of service or
not. When emails are enabled for Einstein Activity Capture, each user must accept the terms
of service.

The default value is `false` .

This field is available only if you use a user-level authentication method. In connection report
CSV files downloaded from Einstein Activity Capture Status & Metrics, this field is labeled
User Auth Terms of Service Accepted.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Recommended action to take when the user’s `ConnectivityStatus` is
`NEEDSATTENTION` . Available in API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reason for the user's `ConnectivityStatus` when the status is `NEEDSATTENTION` .
Available in API version 58.0 and later.

**Type**
string


### Standard Objects AdditionalNumber

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user.

```
UserName

UserOnboardingStatus

### AdditionalNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the Einstein Activity Capture user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The initial sync status when the user connects Salesforce with their external email account
and syncs data for the first time. This field is available in API version 59.0 and later.

Possible values are:

**•** `NOT_STARTED`

**•** `IN_PROGRESS`

**•** `NOT_CONFIGURED`

**•** `COMPLETE`

**•** `FAILED`

Represents an optional additional number for a call center. This additional number is visible in the call center's phone directory.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can't access this object.


Standard Objects AdditionalNumber

Fields

**Field** **Details**

```
CallCenterId

Description

Name

Phone

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
System field that contains the ID of the user who created the call center associated with this
additional number. If value is null, this additional number is displayed in every call center's
phone directory.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the additional number, such as Conference Room B.

Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the additional number.

Limit: 80 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
The phone number that corresponds to this additional number.

Create an additional number for a call center directory. Use this object if the number is not easily categorized as a User, Contact, Lead,
Account, or the other object. Examples include phone queues or conference rooms.


### Standard Objects Address Address

Represents a mailing, billing, or home address.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The following access checks must be enabled:

**•** Industries Insurance

**•** Retail Execution

**•** Industries Visit

**•** Field Service

**•** Order Management

**–** Perms: FulfillmentOrder, OrderSummary,AdvancedOrderManagement, OrderCCS

**–** Prefs: OrdersEnabled, EnhancedCommerceOrders

**•** Public Sector

**•** Employee Experience

**•** Contact Tracing For Employees

You can create an address only when creating a location.

Fields

**Field Name** **Details**

### `Address` `AddressType`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The full address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Mailing


Standard Objects Address

**Field Name** **Details**

**•** Shipping

**•** Billing

**•** Home

```
City

Country

Description

DrivingDirections

GeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address country.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the address.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.


Standard Objects Address

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Latitude

LocationType

Longitude

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
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Filter, Group, Sort, Update

**Description**
Picklist of location types. The available values are:

**•** Warehouse (default)

**•** Site

**•** Van

**•** Plant

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Address

**Field Name** **Details**

**Description**
Used with `Latitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal
places.

```
Name

ParentId

PostalCode

State

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the address.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A lookup field to the parent location.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.


### Standard Objects AgentWork

**Field Name** **Details**

```
Street

TimeZone

```

Usage

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.

Important: “Address” in Salesforce can also refer to the Address compound field found on many standard objects. When referencing
the Address object in your Apex code, always use `Schema.Address` instead of `Address` to prevent confusion with the
standard Address compound field. If referencing both the address object and the Address field in the same snippet, you can
differentiate between the two by using `System.Address` for the field and `Schema.Address` for the object.

Associated Object

This object has the following associated object. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AddressHistory (API version 62.0)**
History is available for tracked fields of the object.

### AgentWork

Represents a work assignment that’s been routed to an agent. If the work is transferred to another agent, a new AgentWork record is
created. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


Standard Objects AgentWork

Fields

**Field** **Details**

```
AcceptDateTime

ActiveTime

AcwExtensionCount

AcwExtensionDuration

AfterConversationActualTime

```

**TypedateTime**

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was accepted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time an agent is actively working on a work item in their console. Active time
is tracked only for tasks routed using the tab-based capacity model. It's tracked only when
the work tab is open and in focus in the console. If the agent switches console tabs, the time
spent on the other tabs isn't counted. Active time continues to count if you switch to a new
browser tab or window. Active time stops when the agent closes the work item or the after
conversation work time ends, whichever happens first.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that an agent extended the After Conversation Work (ACW) timer. This
field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of time (in seconds) that the After Conversation Work (ACW) timer was extended
each time that the agent extended the timer. This field is available in API version 55.0 and
later.

To find the total extension duration, multiply this field by `AcwExtensionCount` or use
`AfterConversationActualTime` .

**Type**
int


Standard Objects AgentWork

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of seconds an agent spent on After Conversation Work (ACW) after customer
contact ended. This field is available in API version 52.0 and later.

```
AgentCapacityWhenDeclined

AssignedDateTime

BotId

BotType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The agent’s capacity when declining work, either explicitly or through push timeout.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was assigned to an agent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Enhanced Einstein Bot or AI agent that performed the work. This is a relationship
field. This field is available in API version 52.0 and later.

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


Standard Objects AgentWork

**Field** **Details**

**•** ExternalCopilot. Refers to an AI agent with whom your customers can interact.

The default value is Bot. This field is available in API version 63.0 and later.

```
CancelDateTime

CapacityModel

CapacityPercentage

CapacityWeight

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was canceled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the capacity model used to determine agent capacity. Valid values are
`StatusBased` and `TabBased` . This field is available in API version 50.0 and later.

A work item consumes agent capacity only if it was first assigned to the agent by Omni-Channel
using queues or skills.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is in progress.
Valid values are from 0 to 100.

The agent can receive a new work item only if they have enough available capacity for the
item. Voice calls must have a capacity percentage of _`100`_, so an agent on a call doesn’t
receive new work items until the call ends.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The amount of an agent’s capacity that’s consumed when this work item is in progress.

For example, if cases are assigned a capacity weight of _`2`_, an agent with a capacity of _`6`_ can
accept up to 3 cases before the agent is at capacity and can’t receive new work items.

Voice calls must use the entire capacity weight.


Standard Objects AgentWork

**Field** **Details**

```
CloseDateTime

DeclineDateTime

DeclineReason

ExternalBotId

HandleTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was closed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the agent declined this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The provided reason for why an agent declined the work request.

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

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The amount of time an agent had the work item open, calculated by `CloseDateTime`

                          - `AcceptedDateTime` . Handle time stops when the agent closes the work item or the
after conversation work time ends, whichever happens first.

```
IsConference

IsInterruptible

IsOwnerChangeInitiated

IsPreferredUserRequired

IsStatusChangeInitiated

```

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the agent was conferenced on the work item by another agent ( `true` )
or not ( `false` ). The default value is `false` . Available in API version 44.0 and later. This
field is accessible in Reports, but not via the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item consumes interruptible or primary capacity. The default value
is false. Available in API version 57.0 and later when the Interruptible Capacity feature is
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item owner change triggered the direct assignment of the work
item to the agent. The default value is `false` . Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item stays with the preferred user even when the user isn’t available.
The default value is false. This field is available in API version 50.0 and later.

**Type**
boolean


Standard Objects AgentWork

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item status change triggered the direct assignment of the work
item to the agent. The default value is false. Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

```
IsTransfer

Name

OriginalGroupId

OriginalQueueId

```

**Type**
boolean

**Properties**
Filter,Group, Sort

**Description**
Indicates whether the agent received the work item through transfer from another agent
( `true` ) or not ( `false` ). The default value is `false` . Available in API version 38.0 and later.
This field is accesible in Reports, but not via the API.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the queue that the work assignment was originally routed to. This field is a
relationship field.

**Relationship Name**
OriginalGroup

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The ID of the queue that the work assignment was originally routed to. Due to API changes,
`OriginalQueueId` is no longer recommended. Use `OriginalGroupId` instead.

```
OwnerId

PausedCapacityPercentage

PausedCapacityWeight

PendingServiceRoutingId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the AgentWork. This field is a polymorphic relationship field. This field
is available in API version 50.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity and Enhanced Omni-Channel
only. This field is available in API version 62.0 and later.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity and Enhanced Omni-Channel
only. This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects AgentWork

**Field** **Details**

**Description**
The ID of the PendingServiceRouting on page 4102 from which the AgentWork was created.
This field is a relationship field. This field is available in API version 50.0 and later.

**Relationship Name**
PendingServiceRouting

**Relationship Type**
Lookup

**Refers To**
PendingServiceRouting

```
PreferredUserId

PushTimeout

PushTimeoutDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the preferred user to handle the work. This field is a relationship field. This field is
available in API v46.0 and later.

**Relationship Name**
PreferredUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time limit set for an agent to respond to an item before it’s pushed to another agent.
The time limit is measured in seconds. This field is available in API version 36.0 and later.

Effective API version 57.0, for inbound Voice calls, this field represents the time limit set for
an agent to respond to a call before it’s declined. The value must be between 0 and 20. The
value is capped at 20, so any number greater than that is treated as 20 seconds. This applies
to the following telephony models:

**•** Service Cloud Voice with Amazon Connect

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Type**
dateTime


Standard Objects AgentWork

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the push timeout event occurred. This field is available in
API version 36.0 and later.

```
RequestDateTime

RoutingModel

RoutingPriority

RoutingType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work was requested.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines how incoming work items are routed to agents assigned to a service channel.
Possible values are:

**•** `ExternalRouting`

**•** `LeastActive`

**•** `MostAvailable`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which work items from the queue that are associated with the routing
configuration are routed to agents.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Omni-Channel routing. Possible values are:

**•** `QueueBased`

**•** `SkillsBased`


Standard Objects AgentWork

**Field** **Details**

```
SecondaryRoutingPriority

ServiceChannelId

ShouldSkipCapacityCheck

SpeedToAnswer

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the secondary routing priority.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel that’s associated with the work assignment. This field is a
relationship field.

**Relationship Name**
ServiceChannel

**Relationship Type**
Lookup

**Refers To**
ServiceChannel

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to skip checking an agent’s available capacity ( `true` ) or not ( `false` )
when an externally routed work item is created. This field is used when agents can
simultaneously handle work from both Omni-Channel queues and queues using external
routing.

When `true`, the receiving agent can exceed their set capacity to accept the item, but they
don’t receive more Omni-Channel routed work. When `false`, the receiving agent can’t
exceed their set capacity and must have enough open capacity to accept the item.

The default value is `false` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time between when the work was requested and when an agent accepted
it.


Standard Objects AgentWork

**Field** **Details**

```
Status

TargetAcceptDateTime

TransferRequesterId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The working status of the work item. Valid values are:

**•** `Assigned`  - The item is assigned to the agent but hasn’t been opened.

**•** `Canceled`  - The item no longer needs to be routed. For example: a chat visitor cancels
their Omni-Channel routed chat request before it reaches an agent.

**•** `Closed`  - The item is closed.

**•** `Declined`  - The item was assigned to the agent but the agent explicitly declined it.

**•** `DeclinedOnPushTimeout`  - The item was declined because push time-out is
enabled and the item request timed out with the agent.

**•** `Opened`  - The agent opened the item.

**•** `Transferred` –The item was transferred from an agent to another agent, queue, or
skill.

**•** `Unavailable`  - The item was assigned to the agent but the agent became unavailable
(went offline or lost connection).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time by when a rep must accept a work item. Influences backlog ordering by
prioritizing work items with earlier target acceptance deadlines. The field can be dynamically
set using Flow for each work item during the routing process. This allows for flexible
prioritization based on case urgency, customer tier, or other business rules. Available in API
version 65.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the rep who reassigned the work using the Reassign action. This field is
populated in reassigned AgentWork records only, not the original AgentWork record. This
is a relationship field. This field is available in API version 63.0 and later.

**Relationship Name**
TransferRequester

**Relationship Type**
Lookup


Standard Objects AgentWork

**Field** **Details**

**Refers To**
User

```
UserId

WorkItemId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that the work item was assigned to. This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object that’s routed to the agent through Omni-Channel.

This field is a polymorphic relationship field.

**Relationship Name**
WorkItem

**Relationship Type**
Lookup

**Refers To**
Custom objects and these standard objects: Account, Activity, Case, Claim, ClaimCoverage,
ClaimRecovery, Contact, ContactRequest, CustomEntityData, Incident, Lead,
LiveChatTranscript, MessagingSession, Opportunity, Orchestration Work Items, Order,
PaymentRequest, PersonTraining,Referral, SocialPost, SwarmMember, and VoiceCall.
WorkOrder is available in version 58.0 and later.

`AgentWork` records can only be deleted if they have the status Closed, Declined, or Unavailable. They can’t be deleted if their status
is Assigned or Opened because they’re active in Omni-Channel.

When `AgentWork` records are created, they have the status Assigned. After a record is created, it’s automatically pushed to the
assigned agent.


### Standard Objects AgentWorkConversationalData While the metadata for AgentWork indicates support for upsert() and update(), these calls aren’t used with AgentWork

because none of its fields can be updated.

### Apex triggers are supported with AgentWork .

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**AgentWorkChangeEvent (API version 63.0)**
Change events are available for the object.

**AgentWorkOwnerSharingRule**

Sharing rules are available for the object.

**AgentWorkShare**

Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Understand the Details of the Routing Lifecycle](https://help.salesforce.com/s/articleView?id=service.omnichannel_psr_lifecycle.htm&type=5&language=en_US)

### AgentWorkConversationalData

Stores conversation data for agent work sessions, such as agent interactions, transfer information, and operational metrics. This object
is available in API version 66.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

You must have the Agentforce Contact Center Admin (Salesforce Voice) permission set enabled in your org.

Fields

**Field** **Details**

```
AgentChannelRecordingId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier for the recording associated with the agent channel conversation.

This field is a relationship field.

**Relationship Name**
AgentChannelRecording


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Refers To**
VoiceCallRecording

```
AgentConnectDateTime

AgentCustomerMergeTime

AgentDisconnectDateTime

AgentId

AgentType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the agent connected to the conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the service rep and customer conversations are merged after consultation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the agent disconnected from the conversation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of an agent or a rep involved in the conversation.

This field is a polymorphic relationship field.

**Relationship Name**
Agent

**Refers To**
BotDefinition, ExternalConversationBotDef, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Description**
Type of agent handling the conversation.

Possible values are:

**•** `ExternalBot`

**•** `Human`

**•** `InternalBot`

```
AgentWorkId

ChannelSessionRecordId

LongestPauseDuration

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the `AgentWork` record associated with the conversational data.

This field is a relationship field.

**Relationship Name**
AgentWork

**Refers To**
AgentWork

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the channel session for the conversation.

This field is a relationship field.

**Relationship Name**
ChannelSessionRecord

**Refers To**
VoiceCall

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Duration of the longest pause during the conversation, measured in seconds.

**Type**
string


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the agent work conversational data record.

```
NextAgentWorkConvId

OwnerId

OwnershipEndDateTime

OwnershipStartDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the next record in a sequence of conversations.

This field is a relationship field.

**Relationship Name**
NextAgentWorkConv

**Refers To**
AgentWorkConversationalData

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the conversational data record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when ownership of the conversation ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AgentWorkConversationalData

**Field** **Details**

**Description**
Timestamp for when ownership of this conversation started.

```
PauseCount

PrevAgentWorkConvId

QualityScore

TotalPauseDuration

TransferType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of times the conversation was paused.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the previous record in a sequence of conversations.

This field is a relationship field.

**Relationship Name**
PrevAgentWorkConv

**Refers To**
AgentWorkConversationalData

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Value of the Mean Opinion Score (MOS) that measures voice call quality.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total duration of all pauses during the conversation, measured in seconds.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects AgentWorkSkill

**Field** **Details**

**Description**
Type of transfer for the conversation.

Possible values are:

**•** `Cold`

**•** `Warm`

### AgentWorkSkill

Represents a skill used to route a work assignment to an agent. AgentWorkSkill is used for reporting and represents the result of a routing
decision. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
AgentWorkId

IsAdditionalSkill

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The AgentWork object associated with this skill.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
After a designated timeout period, a skill marked as additional is dropped from Omni-Channel
routing. The case is then routed to the best-matched agent, even if the agent doesn’t have
all the skills. The default value is false. Available in API version 48.0 and later.


Standard Objects AgentWorkSkill

**Field** **Details**

```
Name

SkillId

SkillLevel

SkillPriority

WasDropped

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The skill that is required or additional.

**Type**
double

**Properties**
Filter, Sort

**Description**
The level of the required or additional skill. Skill levels can range from 1 to 10. Depending on
your business needs, you might want the skill level to reflect years of experience, certification
levels, or license classes.

**Type**
int

**Properties**
Aggregatable, Filter, Group, Nillable, Sort

**Description**
For additional skills, specifies the order in which skills are dropped if after the specified timeout
no agent with that skill is available. Higher priority-value skills are dropped first. Lower
priority-value skills, for example 0, are dropped last. Skills with the same priority value are
dropped as a group. You can set skill priority using attribute setup for skills-based routing or
Apex code.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
For skills marked as additional, indicates if the skill was dropped from Omni-Channel routing
because an agent with this skill was not available. The default value is false. Available in API
version 48.0 and later.


### Standard Objects AIApplication

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AgentWorkSkillChangeEvent (API version 62.0)**
Change events are available for the object.

### AIApplication

Represents an AI application such as Einstein Prediction Builder. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeveloperName

Language

```

**Type**
string

**Properties**
Filter, Group, Sort

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
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the application. Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish


Standard Objects AIApplication

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

Status

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the AI application throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the application if installed with a managed package.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of the AI application. Possible values are:

**•** `Disabled`

**•** `Enabled`

**•** `Migrated`


### Standard Objects AIApplicationConfig

**Field** **Details**

```
Type

### AIApplicationConfig

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of application. Possible values are:

**•** `PredictionBuilder`

Additional prediction information related to an AI application. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeveloperName

Language

```

**Type**
string

**Properties**
Filter, Group, Sort

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
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the application. Possible values are:


### Standard Objects AiGenActionItem

**Field** **Details**

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

```
MasterLabel

NamespacePrefix

### AiGenActionItem

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the AI application throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the application config, if installed with a managed package.

Represents business actions suggested by generative AI. AI-generated action items are sent to either agents for automatic execution or
human users for review, depending on org preference and if there are any errors in the process. This object is available in API version
64.0 and later.


Standard Objects AiGenActionItem

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`

Special Access Rules

Agentforce Pipeline Management must be enabled. Only the agent user can create AiGenActionItem records.

Fields

**Field** **Details**

```
ActionItemOwnerId

ActionResult

AgentType

```

BotDefinitionId

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID associated with the owner of the AI-generated action item. The owner can be an
agent or human user, and can change during the review and execution process. By default,
the owner is an agent or queue.

This field is a polymorphic relationship field.

**Relationship Name**
ActionItemOwner

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The result generated when the agent action is executed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The specific agent that processes the AI-generated action item.

**Type**
reference


Standard Objects AiGenActionItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bot record with a template name that matches the value in the Sales Management agent
template.

This field is a relationship field.

**Relationship Name**
BotDefinition

**Refers To**
BotDefinition

BotVersionId

```
Description

ExpirationDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bot version from the bot record with an ID that matches the ID of the Sales Management
agent bot record.

This field is a relationship field.

**Relationship Name**
BotVersion

**Refers To**
BotVersion

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The explanation of why the action item has been suggested. The description provides
additional context to guide human users and agents in their decision-making.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date that the action item expires and is deleted. AI-generated action items are no longer
visible to users after 14 days and removed from records after 30 days.


Standard Objects AiGenActionItem

**Field** **Details**

```
GeneratedResponseIdRef

OwnerId

Status

Subject

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of generated result in the GenAIGeneration DMO. This field can be used by human
users to provide feedback on the AI-generated action item.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the AI-generated action item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject line that displays to users indicating what the action item is.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that the action item falls under. This field can be used to search for specific
action items, such as field updates or follow-up sales emails.


### Standard Objects AIInsightAction

**Field** **Details**

```
UnmodActionItemOutput

WhatId

### AIInsightAction

```

**Type**
textarea

**Properties**
Nillable

**Description**
The unmodified output for the action item produced by AI, whether from a prompt template
or other generation method.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that the AI-generated action item is for.

This field is a polymorphic relationship field.

**Relationship Name**
What

**Refers To**
Account, Opportunity

Represents an Einstein prediction insight action. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightAction is a one-to-many child of AIRecordInsight. AIInsightAction contains information about predicted actions for this particular

insight. AIInsightAction has one or more AIInsightValue children which contain predicted values for the action. For example, an
### AIInsightAction could represent a quick action, and have a child AIInsightValue with the recommended value used by the quick action.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.


Standard Objects AIInsightAction

Fields

**Field** **Details**

```
ActionId

ActionName

AiRecordInsightId

Confidence

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated action, such as the ID of a Macro.

This is a polymorphic relationship field.

**Relationship Name**
Action

**Relationship Type**
Lookup

**Refers To**
ApexClass, AuraDefinitionBundle

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The ID of the action. For example, a value of “Case.SendEmail” indicates a send email quick
action on Case.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

**Type**
double


Standard Objects AIInsightAction

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

```
 Name

 Type

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightAction.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of action. Possible values are:

**•** `InvocableAction` —Invocable Action

**•** `Macro` —Macro

**•** `QuickAction` —Quick action.

**•** `StandardAction` —Standard Action. An example standard action would be to
update a record.

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.


### Standard Objects AIInsightFeedback AIInsightFeedback

Represents an Einstein prediction insight feedback. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightFeedback is a one-to-many child of AIRecordInsight. AIInsightFeedback contains information about explicit and implicit feedback

collected from users for a particular insight.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
ActualValue

AiFeedback

AiInsightFeedbackType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The raw feedback value. This field is null when no recommendation is selected.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The feedback user sentiment. Possible values are:

**•** `Negative` —Negative feedback

**•** `Neutral` —Neutral feedback

**•** `Positive` —Positive feedback

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The nature of the feedback. Possible values are:


Standard Objects AIInsightFeedback

**Field** **Details**

**•** `Explicit` —Explicit feedback. For example, a user applies and saves an Einstein
recommendation on a case.

**•** `Implicit` —Implicit feedback. For example, a user edits or updates a case field without
viewing or applying field recommendations from Einstein.

```
AiRecordInsightId

Name

Rank

ValueId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightFeedback.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feedback score.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightValue.

This is a polymorphic relationship field.


### Standard Objects AIInsightReason

**Field** **Details**

**Relationship Name**
Value

**Relationship Type**
Lookup

**Refers To**
AIInsightAction, AIInsightValue

Usage

Salesforce creates AIInsightFeedback records based on user responses to predictions after the prediction has been created. User feedback,
such as a thumbs up/down response or accepting a recommended value, results in the creation of a feedback record in which the
feedback type is explicit. An implicit feedback record is created when Einstein makes a recommendation but the field is updated in
another way, for example, by a process. Once the AIInsightFeedback record has been created, it’s immutable.

Custom fields can’t be added to Einstein insight objects.

### AIInsightReason

Represents an Einstein prediction insight reason. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIInsightReason is a one-to-many child of AIInsightValue. AIInsightReason contains details about how Einstein predicted an insight value.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
AiInsightValueId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIInsightValue.


Standard Objects AIInsightReason

**Field** **Details**

This is a relationship field.

**Relationship Name**
AiInsightValue

**Relationship Type**
Lookup

**Refers To**
AIInsightValue

```
Contribution

FeatureType

FeatureValue

FieldName

FieldValue

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The contribution weight for this insight reason.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the feature, such as BOOL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the feature, such as TRUE or FALSE.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the field the insight uses for its evaluation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AIInsightReason

**Field** **Details**

**Description**
The value for the field the insight uses for its evaluation.

```
Intensity

Name

Operator

ReasonLabelKey (Beta)

RelatedInsightReasonId

(Beta)

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The intensity weight for this insight reason.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightReason.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The logical operator the insight uses to compare the field value with the expression value.
For example, if the prediction evaluates whether the fieldValue for the field `bonus__c` is
greater than $5,000, the logical operator is `greater than` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key used to map an Einstein Key Accounts Identification (Beta) insight phrase or phrases
to the correct messaging template.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID used to relate multiple insights to a single model reason in the Einstein Key Accounts
Identification (Beta) feature.

This is a relationship field.


### Standard Objects AIInsightValue

**Field** **Details**

**Relationship Name**
RelatedInsightReason

**Relationship Type**
Lookup

**Refers To**
AIInsightReason

```
SortOrder (Beta)

 Variance

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number value used to organize the phrases in the model’s insights message in the Einstein
Key Accounts Identification (Beta) feature.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The variance weight for this insight reason.

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

### AIInsightValue

Represents an Einstein prediction insight value. This object is available in API version 47.0 and later.


Standard Objects AIInsightValue

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIInsightValue is a one-to-many child of AIRecordInsight. AIInsightValue represents a predicted value of a predicted insight.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available when Einstein features such as Prediction Builder or Case Classification are enabled. To access an AIInsightValue record, you
must have access to the related AIRecordInsight record. To grant a user the right to create an AIInsightValue record, you can use the
AICreateInsightObjects or the CreateAIInsights permission.

Fields

**Field** **Details**

```
AiInsightActionId

AiRecordInsightId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightAction.

This is a relationship field.

**Relationship Name**
AiInsightAction

**Relationship Type**
Lookup

**Refers To**
AIInsightAction

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup


Standard Objects AIInsightValue

**Field** **Details**

**Refers To**
AIRecordInsight

```
Confidence

Field

FieldValueLowerBound

FieldValueUpperBound

Name

SobjectLookupValueId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the target field Einstein is making predictions for, such as “AnnualRevenue”.

**Type**
textarea

**Properties**
Nillable

**Description**
The lower bound value.

**Type**
textarea

**Properties**
Nillable

**Description**
The upper bound value.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightValue.

**Type**
reference


Standard Objects AIInsightValue

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the value object, if this insight value references an object.

This is a relationship field.

**Relationship Name**
SobjectLookupValue

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskIndDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, AssociatedLocation,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CampaignMember, CardPaymentMethod, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CodeSetBundle, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, ContactRequest, ContentVersion, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo, CreditMemoLine,
DataUseLegalBasis, DataUsePurpose, DelegatedAccount, DigitalWallet,
DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument,
Image, Individual, IndividualApplication, Invoice, InvoiceLine, Lead, Location,
LocationTrustMeasure, MemberPlan, MessagingEndUser, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, Order, OrderItem, OtherComponentTask,
PartyConsent, Payment, PaymentAuthAdjustment, PaymentAuthorization, PaymentGateway,
PaymentGroup, PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry, ProcessException,
Product2, ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,


Standard Objects AIInsightValue

**Field** **Details**

ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PurchaserPlan,
PurchaserPlanAssn, QuickText, ReceivedDocument, Recommendation, Refund,
RefundLinePayment, ReportAnomalyEventStore, ResourceAbsence, ResourcePreference,
ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore,
SharingRecordCollection, Shift, Shipment, ShipmentItem, SkillRequirement, SocialPersona,
SocialPost, Solution, Task, TimeSlot, UnitOfMeasure, UserProvisioningRequest, VideoCall, Visit,
VisitedParty, Visitor, VoiceCall, VolunteerProject, WorkBadge, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
SobjectType

Value

ValueType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the value object, such as Account or Case, if this insight value references an
object.

**Type**
textarea

**Properties**
Nillable

**Description**
The prediction result insight value.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the prediction result insight value. Possible values are:

**•** `Boolean` —Boolean

**•** `Currency` —Currency

**•** `DateTime` —DateTime

**•** `Enum` —Enum

**•** `Lookup` —Lookup

**•** `Number` —Number

**•** `String` —String


### Standard Objects AiJobRun

Usage

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

### AiJobRun

Represents an execution instance of an AI job. This object tracks the overall status and manages the lifecycle of the job from initiation
to completion. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EndTime

ErrorCode

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the job run ends.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the job run fails, this field indicates the specific error that occurred.


Standard Objects AiJobRun

**Field** **Details**

```
ErrorMessage

JobType

Label

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a detailed, human-readable message that explains the reason for the job run failure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines the job's logic.

Possible values are:

**•** `PromptTemplate`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A user-defined name or label for the job run, which can be used for identification and tracking.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique, system-generated identifier for the `AiJobRun` record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user group that owns the `AiJobRun` record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


### Standard Objects AiJobRunItem

**Field** **Details**

```
StartTime

Status

Target

### AiJobRunItem

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when the job run's status changes to `InProgress` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tracks the lifecycle of the job run. Valid values are:

**•** `New` : The job run has been created.

**•** `ReadyToStart` : The job run is ready for the user to initiate processing.

**•** `Queued` : The job run is queued to start.

**•** `InProgress` : The job run is currently processing.

**•** `Completed` : The job run completed.

**•** `Failed` : The job run failed.

**•** `Aborted` : The job run was aborted by the user.

**•** `Archived` : The job run was archived by the user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A metadata field used to specify job-specific details, such as a `PromptTemplateId`,
`PromptTemplateName`, or `ModelId` . This provides further context for the job
execution.

Stores an individual item associated with a parent AiJobRun, including the inputs and resulting response. This object is available in API
version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects AiJobRunItem

Fields

**Field** **Details**

```
AiJobRunId

ErrorCode

ErrorMessage

Input

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A required reference to the parent AiJobRun record that this item belongs to.

This field is a relationship field.

**Relationship Name**
AiJobRun

**Refers To**
AiJobRun

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If processing for this item fails, this field contains a numeric code indicating the error.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a detailed, human-readable message that explains the reason for the job run item
failure.

**Type**
textarea

**Properties**
Create, Update

**Description**
Contains the input data for a single item within the job run. For example, in a PromptTemplate
job, this is the JSON input for the prompt template.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects AiJobRunItem

**Field** **Details**

**Description**
A unique, system-generated identifier for the AiJobRunItem record.

```
OwnerId

PreprocessedInput

Response

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user or group that owns the AiJobRunItem record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Stores an intermediate version of the input data after the preprocessing step. For example,
this field could be a hydrated JSON prompt.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the generated response for the job item after processing is complete.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tracks the status of the individual job item. Valid values are:

**•** `Ready` : The default value. The job run item is ready to start processing.

**•** `Completed` : Processing for the job run item is complete.

**•** `Failed` : Processing for the job run item failed.


### Standard Objects AiModelLanguage AiModelLanguage

An object that stores language related information that is generated for each AI model. This object is available in API version 55.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

For Einstein Reply Recommendations:

Requires the Einstein Reply Recommendations org permissions, Einstein Reply Recommendations org pref, and Admin user or user with
Einstein Reply Manager permissions.

Fields

**Field** **Details**

```
ApplicationType

ExternalAiModelId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of application using the AI model.

Possible values are:

**•** `ARTICLE_RECOMMENDATION`

**•** `EAR_FOR_CONVERSATION`

**•** `EAR_FOR_VOICE`

**•** `FAQ`

**•** `REPLY_RECOMMENDATION`

**•** `USE_CASE_EXPLORER`

**•** `UTTERANCE_RECOMMENDATION`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the AI model used to generate predictions.

This field is a relationship field.


Standard Objects AiModelLanguage

**Field** **Details**

**Relationship Name**
ExternalAiModel

**Relationship Type**
Lookup

**Refers To**
ExternalAIModel

```
Language

Name

ServingStatus

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Languages supported by this AI model.

Possible values are:

**•** `Arabic`

**•** `Chinese-simplified`

**•** `Chinese-traditional`

**•** `Dutch`

**•** `English`

**•** `French`

**•** `German`

**•** `Italian`

**•** `Japanese`

**•** `Korean`

**•** `Polish`

**•** `Portuguese`

**•** `Russian`

**•** `Spanish`

**•** `Thai`

**•** `Turkish`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
AI model name.

**Type**
picklist


### Standard Objects AIRecordInsight

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the language is enabled or disabled for this AI model.

```
TranscriptCount

### AIRecordInsight

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Transcript count detected for each language.

Represents an Einstein prediction insight. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

### AIRecordInsight contains information on the Einstein prediction, the AI prediction field where results were written, and other details

such as the type of prediction.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

Prediction insight objects are available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

Fields

**Field** **Details**

```
AiApplicationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the AiApplication that generated this prediction.

This is a relationship field.


Standard Objects AIRecordInsight

**Field** **Details**

**Relationship Name**
AiApplication

**Relationship Type**
Lookup

**Refers To**
AIApplication

```
Confidence

MlPredictionDefinitionId

ModelId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight, from 0.0 to 1.0. Higher
values (near 1.0) indicate stronger confidence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is a relationship field.

**Relationship Name**
MlPredictionDefinition

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the model to use when generating the insight.

This field is a polymorphic relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel


Standard Objects AIRecordInsight

**Field** **Details**

```
Name

PredictionField

RunGuid

RunStartTime

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIRecordInsight.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the field that Einstein is making predictions for, such as “Case.IsEscalated”.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A unique identifier for the Einstein process that made the prediction.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the Einstein prediction process was started.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this insight. Possible values are:

**•** `Defunct` —The insight has been consumed by the Einstein feature that owns the
prediction. For example, Case Classification marks an insight as defunct if a predicted
recommendation was presented to a user and the user either accepted or ignored the
recommendation. This behavior ensures that the same recommendation isn’t presented
multiple times to the user.

**•** `New` —The insight hasn’t been consumed by the Einstein feature.


Standard Objects AIRecordInsight

**Field** **Details**

```
TargetField

TargetId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The field to which prediction results are written. Case Classification doesn’t use this field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the record Einstein is making predictions for.

This is a relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskIndDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, AssociatedLocation,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CampaignMember, CardPaymentMethod, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CodeSetBundle, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, ContactRequest, ContentVersion, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo, CreditMemoLine,
DataUseLegalBasis, DataUsePurpose, DelegatedAccount, DigitalWallet,
DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthCareDiagnosis,


Standard Objects AIRecordInsight

**Field** **Details**

HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument,
Image, Individual, IndividualApplication, Invoice, InvoiceLine, Lead, Location,
LocationTrustMeasure, MemberPlan, MessagingEndUser, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, Order, OrderItem, OtherComponentTask,
PartyConsent, Payment, PaymentAuthAdjustment, PaymentAuthorization, PaymentGateway,
PaymentGroup, PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry, ProcessException,
Product2, ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PurchaserPlan,
PurchaserPlanAssn, QuickText, ReceivedDocument, Recommendation, Refund,
RefundLinePayment, ReportAnomalyEventStore, ResourceAbsence, ResourcePreference,
ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore,
SharingRecordCollection, Shift, Shipment, ShipmentItem, SkillRequirement, SocialPersona,
SocialPost, Solution, Task, TimeSlot, UnitOfMeasure, UserProvisioningRequest, VideoCall, Visit,
VisitedParty, Visitor, VoiceCall, VolunteerProject, WorkBadge, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
TargetSobjectType

Type

ValidUntil

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target object, such as Account or Case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values are:

**•** `Action` —An insight that indicates a suggested action, such as sending an email.

**•** `Lookup` —An insight that indicates a related value not directly related to the target
object and field.

**•** `MultiValue` —An insight with multiple values, such as a multi-class classification.

**•** `SimilarRecord` —An insight that indicates similar or duplicate records.

**•** `SingleValue` —A single value insight, such as a regression number or a score.

**Type**
dateTime


### Standard Objects AIResearchPromptResult

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The day and time this insight is valid until. After this day and time, the insight might no longer
be valid due to new prediction results from new or changed data. If this field is `null`, this
insight never expires.

Usage

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.

Considerations for Case Classification

To generate reports on the effectiveness of Einstein Case Classification predictions, use the root AIRecordInsight object and its child
[objects, AIInsightFeedback and AIInsightValue. For example, you can determine how many cases received predictions, or how often](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_aiinsightfeedback.htm)
agents accepted or rejected them.

**•** To determine how many cases received recommendations, the AIRecordInsight table identifies the case and contains a row for each
field and each recommendation. In AIRecordInsight, the TargetId field contains the case ID. The PredictionField indicates which case
field is being predicted. Each field value recommendation is contained in a separate AIInsightValue object with AIRecordInsight as
the parent. For a picklist field, Einstein creates AIInsightValue objects with up to 10 field value recommendations. However, just the
top three predictions appear to agents in the Einstein Field Recommendations component.

**•** To learn whether agents acted on any of the top three predictions, use the AIInsightFeedback object. When an agent updates fields
after viewing Einstein’s recommendations, or when Einstein applies a recommendation automatically, the object’s
AiInsightFeedbackType field contains Explicit. If the agent updates fields without viewing the predictions, such as on the case details
tab, AiInsightFeedbackType is set to Implicit. When the agent applies the recommended value, the object’s AiFeedback field is set
to Positive; if the agent applies a different value, AiFeedback is Negative.

### AIResearchPromptResult

Represents the research result generated by Agentforce or by Einstein from a standard or custom prompt template. This object is
available in API version 64.0 and later.


Standard Objects AIResearchPromptResult

When an Agentforce or an Einstein feature researches a record and saves the results, an AIResearchPromptResult record is created and
populated with information about the researched record.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Research results are only available in orgs that have Einstein features with Einstein generative AI enabled.

Fields

**Field** **Details**

AiGenActionItemId

IsToxicityDetected

```
LatestErrorMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business action suggested by generative AI.

This field is a polymorphic relationship field.

**Relationship Name**
AiGenActionItem

**Refers To**
AiGenActionItem

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the generated response contains toxic language ( `true` ) or not ( `false` ).
The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error message that displays if the result can't be generated.


Standard Objects AIResearchPromptResult

**Field** **Details**

```
LatestGenResponseIdRef

LatestGenerationDate

LatestResult

LatestSafetyScore

LatestStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the most recently generated result in the GenAIGeneration object. The object is
derived from the Data Cloud data model object (DMO).

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the result was most recently generated.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The AI-generated result.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Overall safety score for the generated research. A higher value means the generated response
is more likely to be safe. Minimum value of 0.0. Maximum value of 1.0.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the generated result.

Possible values are:

**•** `Generating`

**•** `Success`

**•** `Failed`


Standard Objects AIResearchPromptResult

**Field** **Details**

```
OwnerId

ReferenceRecordId

StandardPromptTemplate

```

Version

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the generated research result.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID that the research result was generated for.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Refers To**
Account, Lead, Opportunity

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The standard prompt template used to generate the result.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prompt template version number.


### Standard Objects AllowedEmailDomain

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AIResearchPromptResultFeed on page 55**
Feed tracking is available for the object.

**AIResearchPromptResultHistory on page 63**
History is available for tracked fields of the object.

**AIResearchPromptResultOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AIResearchPromptResultShare on page 67**
Sharing is available for the object.

### AllowedEmailDomain

Represents an allowed email domain for users in your organization. You can define an allowlist to restrict the email domains allowed in
a user’s `Email` field. This object is available in API version 29.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “Manage Internal Users” user permission to use this object.

Note: If you don't see this object, contact your Salesforce representative to enable it.

Fields

**Field** **Details**

```
Domain

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
An allowed email domain for users.


### Standard Objects AlternativePaymentMethod AlternativePaymentMethod

Represents a payment method that isn’t cash, a debit card, or a credit card. This object defines methods that aren’t defined by the
CardPaymentMethod or DigitalWallet objects. Examples of alternative payment methods include CashOnDeliver, Klarna, and Direct
### Debit. AlternativePaymentMethod functions the same as any other type of payment method for processing transactions

through a payment gateway. This object is available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

### `AlternativePaymentMethod`

Number

AuditEmail

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account for the alternative payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce ID number for the alternative payment method.

**Type**
email


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the payment owner where audit information about payments is sent.

```
BankAccountHolderType

BankAccountType

BillingFirstName

BillingLastName

BillingName

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines if the bank account is held by a business or an individual.

Possible values are:

**•** `Business`

**•** `Individual`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of bank account such as a checking or savings account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
string


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first and last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

```
Comments

CompanyName

Email

```

ExtendedPaymentMethodType

```
GatewayToken

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name for this payment method. Part of the payment method’s address.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Other alternative payment methods used for the transaction. This field is available in API
version 66.0 and later.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
Tokenized form of the alternative payment method, returned by the gateway. Stored as
encrypted text.

```
GatewayTokenDetails

IpAddress

IsAutoPayEnabled

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique tokenized ID generated by the payment gateway when this payment method first
interacts with the gateway. Used to identify the payment method during future transactions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address for the payment method owner.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Alternative Payment Method page layout in the UI. It isn't automatically
added.

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


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view (LastReferencedDate) but not
viewed it.

```
MacAddress

NickName

OwnerId

PaymentGatewayId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mac Address of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined nickname for this payment method.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the alternative payment method.

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
Create, Filter, Group, Nillable, Sort

**Description**
ID of the payment gateway entity used to handle transactions from this payment method.

This field is a relationship field.


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

```
PaymentMethodAddress

PaymentMethodCity

PaymentMethodCountry

PaymentMethodDetails

PaymentMethodGeocode

Accuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Full address associated with the alternative payment method. For more information about
address fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects AlternativePaymentMethod

**Field** **Details**

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

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
PaymentMethodLatitude

PaymentMethodLongitude

PaymentMethodPostalCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Longitude of the payment method address. Used with the PaymentMethodLatitude to
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.


Standard Objects AlternativePaymentMethod

**Field** **Details**

```
PaymentMethodState

PaymentMethodStreet

PaymentMethodSubType

PaymentMethodType

Phone

ProcessingMode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be a digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction, such as Visa, Mastercard, EPS, SepaDebit, and
Klarna. This field is available in API version 57.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payment method's owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects AlternativePaymentMethod

**Field** **Details**

**Description**
Indicates whether the payment method was created in Salesforce or externally. Required.

Possible values are:

**•** `External` : Select this value if you create the alternative payment method record
through any method other than the Salesforce Payments Connect API.

**•** `Salesforce` : Select this value if you use Salesforce Payments Connect API to create
the alternative payment method record.

```
SavedPaymentMethodId

StandardEntryClassCode

Status

```

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
A three-letter code that indicates how a customer or a business initiated and authorized an
ACH payment.

Possible values are:

**•** `CCD` —Corporate credit or debit entry

**•** `PPD` —Pre-arranged payment and deposit entry

**•** `TEL` —Telephone-initiated entry

**•** `WEB` —Internet or mobile-initiated entry

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the payment method. Required.


### Standard Objects AnalyticsChangeEventLog

**Field** **Details**

Possible values are:

**•** `Active` —The Payments platform can use the alternative payment method to make
payments. Active alternative payment methods can't be deleted.

**•** `Canceled` —The Payments platform can no longer use the payment method to make
payments. A value of `Canceled` can't be changed back to `Active` or `Inactive`

**•** `InActive` —The Payment platform currently can't use the payment method to make
payments. Admins can change this value to `Active` or `Canceled` when needed.

### AnalyticsChangeEventLog

Analytics Change Event Logs represent route or page changes made in the CRM Analytics. This object is available in API version 61.0 and
later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsMode

AnalyticsSessionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location where the dashboard is displayed. In the Salesforce mobile app, embedded
dashboards are logged as embedded first.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

```
AnalyticsTimestamp

ClientIp

CpuTime

IsMobile

IsNew

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

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

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the dashboard is displayed in mobile (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The field indicates that this action opens a new tab ( `true` ) or goes back to a previously
opened tab ( `false` ).

The default value is `false` .


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

```
LoginKey

PageContext

PageIdentifier

RecordIdentifier

ReopenCount

RequestIdentifier

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
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CRM Analytics dashboard page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the CRM Analytics object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If `IsNew` is `false`, the number of times that an existing page opens.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AnalyticsChangeEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

```
RunTime

SavedViewIdentifier

SessionKey

TabIdentifier

Timestamp

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
The ID of the CRM Analytics dashboard saved view.

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
The ID of the particular Analytics tab in the user interface.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.


### Standard Objects AnalyticsDashboard

**Field** **Details**

```
Type

Uri

UserIdentifier

ViewMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Apex callout. For example: REST or AJAX.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character Identifier of the user who’s using Salesforce services through the UI or the
API. For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

### AnalyticsDashboard

Represents a Tableau Next dashboard. This object is available in API version 64.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`


Standard Objects AnalyticsDashboard

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsWorkspaceId

Description

DeveloperName

Language

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Tableau Next workspace the dashboard is associated with.

This field is a relationship field.

**Relationship Name**
AnalyticsWorkspace

**Refers To**
AnalyticsWorkspace

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the dashboard.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the dashboard.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The supported languages for the visualization. There are over 50+ supported language and
dialect values.


Standard Objects AnalyticsDashboard

**Field** **Details**

```
LastDraftModifiedDate

LastPublishedDate

MasterLabel

NamespacePrefix

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date for the dashboard in draft mode.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last published date for the dashboard.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label for the dashboard.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the dashboard.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID of the user who created the dashboard.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User


### Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

```
Style

TemplateAssetSourceName

TemplateSource

Version

```

**Type**
textarea

**Properties**
Nillable

**Description**
The widget style for the dashboard, represented as a JSON string. For example,

```
  {"widgetStyle":{"backgroundColor":"#ffffff","borderEdges":[],"borderColor":"#cccccc","borderWidth":1,"borderRadius":0}}

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the dashboard was created from a template, this is name of the asset source.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the dashboard was created from a template, this is name of the template.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for the dashboard.

### AnalyticsDownloadEventLog AnalyticsDownloadEventLog represent downloads made from lens and dashboard in the CRM Analytics. This object is available in API

version 61.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects AnalyticsDownloadEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

AnalyticsTimestamp

AssetIdentifier

AssetType

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset ID from the user download.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset type from the user download.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .


Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

```
CpuTime

DatasetIdentifiers

DownloadFormat

LoginKey

RecordCount

RequestIdentifier

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
A comma-separated list of used dataset IDs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The format of the data for export.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records exported.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AnalyticsDownloadEventLog

**Field** **Details**

**Description**
Globally unique identifier for a given request.

```
RunTime

SessionKey

Timestamp

Uri

UserIdentifier

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .


### Standard Objects AnalyticsInteractEventLog

**Field** **Details**

```
UserType

```

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

### AnalyticsInteractEventLog

Analytics Interact Event Log represents route or page changes made in the CRM Analytic UI. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects AnalyticsInteractEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

AnalyticsTimestamp

ClickCount

ClientIp

CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of clicks performed on a page in the CRM Analytics UI.

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


Standard Objects AnalyticsInteractEventLog

**Field** **Details**

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

```
LoginKey

ReadTime

RecordIdentifier

RequestIdentifier

RunTime

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time a user spent on a particular tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the CRM Analytics object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.


Standard Objects AnalyticsInteractEventLog

**Field** **Details**

```
SessionCount

SessionKey

TabIdentifier

Timestamp

TotalTime

Type

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a user returned to a particular page.

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
The ID of the particular Analytics tab in the UI.

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
The total amount of time (in milliseconds) a tab is open.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AnalyticsLicensedAsset

**Field** **Details**

**Description**
The CRM Analytics object type.

```
Uri

UserIdentifier

ViewMode

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

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

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

This event type is captured when a tab is closed. It collates the interaction statistics over the life of the tab, including total open time,
read time, and so on. These statistics are aggregated as you go to other tabs and then return, and logged only when the tab is closed.

### AnalyticsLicensedAsset

Represents a licensed Analytics asset. In this context, Analytics is CRM Analytics, Sonic, or Mulesoft Data Path. Available in API version
52.0 and later.


### Standard Objects AnalyticsPerfEventLog

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsumerNamespace

LicenseType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consumer namespace for the asset. The possible values are:

**•** `Industries`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The license type for the asset. The possible values are:

**•** `Aqs` (Analytics Query Service)

**•** `Cdp` (Data Cloud)

**•** `DataPipelineQuery` (Data Pipeline Query)

**•** `EinsteinAnalytics` (CRM Analytics)

**•** `MulesoftDataPath` (Mulesoft DataPath)

**•** `Sonic` (Salesforce Data Pipelines)

The default value is `EinsteinAnalytics` .

### AnalyticsPerfEventLog

Analytics Perf Event Log helps track trends in your Analytics performance. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects AnalyticsPerfEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AnalyticsSessionIdentifier

AnalyticsTimestamp

ClientIp

CpuTime

EffectivePageTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line is generated.

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

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects AnalyticsPerfEventLog

**Field** **Details**

**Description**
The experienced page time in milliseconds.

```
IsInitialLoad

LoginKey

QueriedName

RecordIdentifier

RequestIdentifier

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is for the initial load of the Dashboard ( `true` ) or not ( `false` ).

The default value is `false` .

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
The asset title or query string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the CRM Analytics object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.


Standard Objects AnalyticsPerfEventLog

**Field** **Details**

```
RunTime

SessionKey

TabIdentifier

Timestamp

Uri

UserIdentifier

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
The ID of the particular Analytics tab in the UI.

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AnalyticsVisualization

**Field** **Details**

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

```
ViewMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

### AnalyticsVisualization

Represents a Tableau Next viusalization. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AnalyticsWorkspaceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Tableau Next workspace the visualization is associated with.

This field is a relationship field.

**Relationship Name**
AnalyticsWorkspace


Standard Objects AnalyticsVisualization

**Field** **Details**

**Refers To**
AnalyticsWorkspace

```
Description

DeveloperName

Language

LastDraftModifiedDate

LastPublishedDate

MasterLabel

```

**Type**
string

**Properties**
Create, Nillable, Update

**Description**
The description of the visualization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the visualization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The supported languages for the visualization. There are over 50+ supported language and
dialect values.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last modified date for the visualization in draft mode.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last published date for the visualization.

**Type**
string


Standard Objects AnalyticsVisualization

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label for the visualization.

```
NamespacePrefix

OwnerId

TemplateAssetSourceName

TemplateSource

Version

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the visualization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The user ID of the user who created the visualization.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the visualization was created from a template, this is name of the asset source.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the visualization was created from a template, this is name of the template.

**Type**
double


### Standard Objects AnalyticsVizField

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for the visualization.

### AnalyticsVizField

Represents a Tableau Next viusalization field. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
AdHocCalc

DisplayCategory

FieldKey

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An ad-hoc calculation for the visualization field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The display category for the visualization field.

Possible values are:

**•** `Continuous` —continuous

**•** `Discrete` —discrete

**Type**
string


Standard Objects AnalyticsVizField

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The key for for the visualization field.

```
Function

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The function for the visualization field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `CountD`

**•** `DatePartDay`

**•** `DatePartMonth`

**•** `DatePartQuarter`

**•** `DatePartWeek`

**•** `DatePartWeekDay`

**•** `DatePartYear`

**•** `DateTruncDay`

**•** `DateTruncMonth`

**•** `DateTruncQuarter`

**•** `DateTruncWeek`

**•** `DateTruncYear`

**•** `FiscalDatePartMonth`

**•** `FiscalDatePartQuarter`

**•** `FiscalDatePartWeek`

**•** `FiscalDatePartYear`

**•** `FiscalDateTruncMonth`

**•** `FiscalDateTruncQuarter`

**•** `FiscalDateTruncWeek`

**•** `FiscalDateTruncYear`

**•** `Max`

**•** `Mdy`

**•** `Median`

**•** `Min`


Standard Objects AnalyticsVizField

**Field** **Details**

**•** `My`

**•** `Stdev`

**•** `Stdevp`

**•** `Sum`

**•** `UserAgg`

**•** `Var`

**•** `Varp`

```
Label

Role

SemanticFieldApiName

SemanticObjectApiName

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label for the visualization field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role for the visualization field.

Possible values are:

**•** `Dimension`

**•** `Measure`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API for the field in the semantic model.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name for object the field belongs to in the semantic model.

**Type**
picklist


### Standard Objects AnalyticsVizViewDef

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type for the visualization field.

Possible values are:

**•** `Field`

**•** `MeasureNames`

**•** `MeasureValues`

```
UniqueIndex

VisualizationId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique index value for the visualization field.

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the visualization the field belongs to.

This field is a relationship field.

**Relationship Name**
Visualization

**Relationship Type**
Master-detail

**Refers To**
AnalyticsVisualization (the master object)

### AnalyticsVizViewDef

Represents a Tableau Next viusalization view definition. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects AnalyticsVizViewDef

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
DeveloperName

IsOriginal

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the visualization view definition.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the view definition is original ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The supported languages for the visualization view definition.

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


Standard Objects AnalyticsVizViewDef

**Field** **Details**

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

NamespacePrefix

OwnerId

Version

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label for the visualization view definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the visualization view definition.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The user ID of the user who created the visualization view definition.

This field is a relationship field.

**Relationship Name**
Owner

**Refers To**
User

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for the visualization view definition.


### Standard Objects AnalyticsWorkspace

**Field** **Details**

```
VisualizationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

This field is a relationship field.

**Relationship Name**
Visualization

**Refers To**
AnalyticsVisualization

### AnalyticsWorkspace

Represents a Tableau Next workspace. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description for the workspace.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name for the workspace.


Standard Objects AnalyticsWorkspace

**Field** **Details**

```
Language

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The supported languages for the workspace.

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
Filter, Group, idLookup, Sort

**Description**
The label for the workspace.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for the workspace.


### Standard Objects AnalyticsWorkspaceAsset AnalyticsWorkspaceAsset

Represents a Tableau Next asset in a workspace. This object is available in API version 54.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, you must have Tableau Next enabled in your org and a Tableau Next permission set.

Fields

**Field** **Details**

```
ActivePromotionRequestId

AnalyticsWorkspaceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active promotion request for the workspace asset.

This field is a relationship field.

**Relationship Name**
ActivePromotionRequest

**Refers To**
DataAssetPromotionRequest

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Tableau Next workspace the asset is associated with.

This field is a relationship field.

**Relationship Name**
### AnalyticsWorkspace

**Relationship Type**
Master-detail

**Refers To**
AnalyticsWorkspace (the master object)


Standard Objects AnalyticsWorkspaceAsset

**Field** **Details**

```
AssetId

AssetType

AssetUsageType

HistoricalPromotionStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the asset.

This field is a polymorphic relationship field.

**Relationship Name**
Asset

**Refers To**
AnalyticsDashboard, AnalyticsVisualization

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of asset.

Possible values are:

**•** `AnalyticsDashboard` —Analytics Dashboard

**•** `AnalyticsVisualization` —Analytics Visualization

**•** `MktCalculatedInsightObject` —Calculated Insight Object

**•** `MktDataConnection` —Data Cloud Connection

**•** `MktDataLakeObject` —Data Lake Object

**•** `MktDataModelObject` —Data Model Object

**•** `SemanticModel` —Semantic Model

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of usage for the asset.

Possible values are:

**•** `Created`

**•** `Referenced`

**Type**
picklist


### Standard Objects Announcement

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The historical promotion status for the asset.

Possible values are:

**•** `pending`

**•** `promoted`

**•** `unpromoted`

```
MetadataSourceType

### Announcement

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The source type of the asset metadata.

Possible values are:

**•** `Promoted`

**•** `Reused`

Represents a Chatter group announcement. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ExpirationDate

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

Required. The date on which the announcement expires. Announcements display
on the group UI until 11:59 p.m. local time on the selected date.


Standard Objects Announcement

**Field Name** **Details**

```
FeedItemId

ParentId

SendEmails

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

Required. The ID of the FeedItem that contains the content of the announcement.
Announcements are stored as text posts.

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
Filter, Group, Nillable, Sort

**Description**

The ID of the parent CollaborationGroup that the announcement belongs to. An
announcement can belong only to a single Chatter group.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Set to `true` to email all group members when an announcement is posted to
the group. The default is `false` . This requires the user to have the “Send
announcement on email” permission.

This field is available in API version 36.0 and later.


### Standard Objects ApexCalloutEventLog

**Field Name** **Details**

Note: This field is currently available to select customers through a pilot
program. To be nominated to join this pilot program, contact Salesforce.
Additional terms and conditions may apply to participate in the pilot
program. Please note that pilot programs are subject to change, and as
such, we cannot guarantee acceptance into this pilot program or a
particular time frame in which this feature can be enabled. Any unreleased
services or features referenced in this document, press releases, or public
statements are not currently available and may not be delivered on time
or at all. Customers who purchase our services should make their purchase
decisions based upon features that are currently available.

Usage

Group owners, managers, and users with the “Modify All Data” permission can use the Announcement object to create, edit, and delete
group announcements. Creating a group announcement is a three-step process.

**1.** Use the FeedItem object to create a text post with the announcement’s content. Use the CollaborationGroup record you want to
post the announcement to as the parent of this feed item.

**2.** Next, use the feed item ID and an expiration date to create the announcement record.

**3.** Finally, update the `AnnouncementId` field in the CollaborationGroup record with the ID of the announcement you created.

To delete the group announcement, simply delete the `AnnouncementId` value in the CollaborationGroup record. To restore a group
announcement, update the `AnnouncementId` field for a group with the announcement’s ID. The expiration date for the announcement
should be in the future and the feed item used to create the announcement should be parented by the same group.

### ApexCalloutEventLog

Apex Callout event logs contain details about callouts (external requests) during Apex code execution. This object is available in API
version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects ApexCalloutEventLog

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ClientIp

CpuTime

IsSuccess

LoginKey

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

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the callout request was successful.

**Type**
string


Standard Objects ApexCalloutEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

```
Method

PlannerIdentifier

RequestIdentifier

RequestSize

RequestTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the callout. For example: `GET`, `POST`, `PUT`, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout request body, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ApexCalloutEventLog

**Field** **Details**

**Description**
The amount of time that the request took in milliseconds.

```
ResponseSize

RunTime

SessionKey

StatusCode

Timestamp

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Not used for this event type. Use the `RequestTime` field instead.

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
The returned status code of the request.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.


### Standard Objects ApexClass

**Field** **Details**

```
Type

Uri

Url

UserIdentifier

### ApexClass

```

Represents an Apex class.

Supported Calls

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Apex callout. For example: `REST` or `AJAX` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The callout endpoint URL. For example, `www.salesforce.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()update()`, `upsert()`


Standard Objects ApexClass

Fields

**Field** **Details**

```
ApiVersion

Body

BodyCrc

IsValid

LengthWithoutComments

Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex class definition.

Limit: 1 million characters.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the class was last compiled
( `true` ) or not ( `false` ). The default value is `false` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Length of the class without comments.

**Type**
string


Standard Objects ApexClass

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Name of the class.

Limit: 255 characters

```
NamespacePrefix

Status

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

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex class. The following string values are valid:

**•** `Active` —The class is active.

**•** `Deleted` —The class is marked for deletion. This is useful for managed packages,
because it allows a class to be deleted when a managed package is updated.

**•** `Inactive` —This option is unused and is only supported for ApexTrigger. For more
[information, see the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/)


### Standard Objects ApexComponent

Usage

Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexTrigger

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/)

### ApexComponent

Represents a definition for a custom component that can be used in a Visualforce page alongside standard components such as

`<apex:relatedList>` and `<apex:dataTable>` .

Represents a definition for a custom component that can be used in a Visualforce page alongside standard components such as

`<apex:relatedList>` and `<apex:dataTable>` . For information, see the _[Visualforce Developers Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)_ .

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

ControllerKey

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this custom component. Every custom component has an API version
specified at creation. If the API version is less than 15.0 and `ApiVersion` is not specified,
`ApiVersion` defaults to 15.0.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier for the controller associated with this custom component:

**•** If the `ControllerType` parameter is set to `Standard` or `StandardSet`, this
value is the name of the sObject that defines the controller.


Standard Objects ApexComponent

**Field** **Details**

**•** If the `ControllerType` parameter is set to `Custom`, this value is the name of the
Apex class that defines the controller.

```
ControllerType

Description

Markup

MasterLabel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of controller associated with this Visualforce custom component. Possible values
include:

**•** `Not Specified`, for custom components defined without a value for the
`controller` attribute on the `<apex:component>` tag

**•** `Standard`, a value that can't be used with custom components or errors may occur

**•** `StandardSet`, a value that can't be used with custom components or errors may
occur

**•** `Custom`, for components that have a value for the `controller` attribute on the

`<apex:component>` tag

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the Visualforce custom component.

**Type**
textarea

**Properties**
Create, Update

**Description**
The Visualforce markup, HTML, Javascript, and any other Web-enabled code that defines the
content of the custom component.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text used to identify the Visualforce custom component in the Setup area of Salesforce.
The Label for this field is **Label** .


### Standard Objects ApexEmailNotification

**Field** **Details**

```
Name

NamespacePrefix

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this Visualforce custom component.

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

Use custom components to encapsulate a common design pattern and then reuse that pattern several times in one or more Visualforce
pages. All users who can view Visualforce pages can view custom components, but the “Customize Application” permission is required
to create or update custom components.

SEE ALSO:

ApexPage

StaticResource

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

### ApexEmailNotification

Stores a Salesforce user ID or external email address to be notified when unhandled Apex exceptions occur. This object is available in
API version 35.0 and later.


### Standard Objects ApexExecutionEventLog

Note: Each ApexEmailNotification contains either an email or a user ID, but not both.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Email

UserId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The external email address to which the notification is sent. Mutually exclusive with the
`UserId` field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user to which the notification is sent. Mutually exclusive with the `Email` field.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

To notify users of your org at the email addresses they have on record, use `UserId` . To notify external users or alternate email addresses,
use `Email` .

### ApexExecutionEventLog

Apex Execution event logs contain details about Apex classes that are used. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects ApexExecutionEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

CalloutTime

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
double

**Properties**
Filter, Nillable, Sort

**Description**
Time spent waiting on webservice callouts, in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

**Type**
double


Standard Objects ApexExecutionEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

```
DatabaseTotalTime

EntryPoint

ExecutionTime

IsLongRunningRequest

LoginKey

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entry point for this Apex execution. For example,
`GeneralCloner.cloneAndInsertRecords` or `VF- /apex/CloneUser` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time (in milliseconds).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the request is counted against your org’s concurrent long-running Apex
request limit ( `true` ) or not ( `false` ).

Asynchronous Apex jobs (batch, queueable, scheduled, and future), background processes,
and bulk API requests are not counted against the concurrent long-running limit.

**Type**
string


Standard Objects ApexExecutionEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

```
PlannerIdentifier

Quiddity

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of outer execution associated with this event. For example:

**•** `A` –ACS Batch Apex

**•** `C` –Scheduled Apex

**•** `E` –Inbound Email Service

**•** `F` –Future

**•** `H` –Apex REST

**•** `I` –Invocable Action

**•** `K` –Quick Action

**•** `L` –Lightning

**•** `M` –Remote Action

**•** `P` –Bulk Apex jobs running in parallel

**•** `Q` –Queueable

**•** `R` –Synchronous uncategorized (which is where all transactions not specified elsewhere
end up)

**•** `S` –QueryLocator Batch Apex (Batch Apex jobs run faster when the start method returns
a QueryLocator object that doesn't include related records via a subquery. See Batch
[Apex Best Practices in Using Batch Apex.)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_best_practices)

**•** `T` –Tests Apex

**•** `V` –Visualforce

**•** `W` –SOAP Webservices

**•** `X` –Execute Anonymous


Standard Objects ApexExecutionEventLog

**Field** **Details**

Implementations of the Process.Plugin interface use the quiddity value `R` .

```
RequestIdentifier

RunTime

SessionKey

SoqlQueryCount

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time the request took, as measured by SFDC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of SOQL queries that were executed during the event.

This value is the aggregate across all namespaces, and can exceed the per-namespace limits.
For test executions, the aggregate total value across all test methods executed in the request
is used. If you are using this value to track limit consumption, consider filtering out test
execution quiddities (indicated by the `Quiddity` field).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Uri

UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### ApexExtlCalloutEventLog

Apex Extl Callout EventLog represent external data callouts via custom adapters for Salesforce Connect. This object is available in API
version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
Action

```

**Type**
string


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Action performed by the callout.

```
ExecutionTime

FetchTime

IsSuccess

Message

ObjectType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time in milliseconds.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Duration (in milliseconds) it takes to retrieve the query results from the external system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the query was successful ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Error or warning message associated with the failed call.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of event. The value is always BulkApi2.


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

```
QueryFilter

QueryLimit

QueryOffset

QueryOrderBy

QuerySelect

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field expressions to filter the rows to return. Corresponds to `WHERE` in SOQL queries.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in SOQL
queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Comma-delineated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexExtlCalloutEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

```
RowCount

RowsFetched

Subqueries

Throughput

Timestamp

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of records in the result set.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of rows fetched by the callout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of subqueries this query has been split into.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of records retrieved in one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.


### Standard Objects ApexInlineEventLog

**Field** **Details**

```
TotalTime

UserIdentifier

### ApexInlineEventLog

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
How long it takes (in milliseconds) to prepare and execute the query and to retrieve the
query results.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

This object is reserved for future use. This object is available in API version 66.0 and later.

### ApexLog

Represents a debug log containing information about a transaction, including information about Apex, Visualforce, and workflow and
validation rules. This object is available in API version 19.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Application

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
This value depends on the client type that triggered the log.

**•** For API clients, this value is the client ID.


Standard Objects ApexLog

**Field** **Details**

**•** For browser clients, this value is `Browser` .

```
DurationMilliseconds

Location

LogLength

LogUserId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Duration of the transaction in milliseconds.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the location of the origin of the log. Values are:

**•** `Monitoring` —Log is generated as part of debug log monitoring. These types of logs
are maintained for seven days or until a user deletes them.

**•** `SystemLog` —Log is generated from the Developer Console. These types of logs are
maintained for 24 hours or until the user clears them.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Length of the log in bytes.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user whose actions triggered the debug log.

This is a polymorphic relationship field.

**Relationship Name**
LogUser

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects ApexLog

**Field** **Details**

```
Operation

Request

RequestIdentifier

StartTime

Status

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the operation that triggered the debug log, such as `APEXSOAP`, `Apex Sharing`
`Recalculation`, and so on.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Request type. Values are:

**•** `API` —Request came from the API

**•** `Application` —Request came from the Salesforce user interface

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the request that triggered the debug log. Use this request identifier
to correlate multiple debug logs triggered by the same request.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Start time of the transaction.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Status of the transaction. This value is either `Success`, or the text of an unhandled Apex
exception.


### Standard Objects ApexPage

Usage

You can read information about this object, as well as delete it, but you can't update or insert it.

SEE ALSO:

ApexClass

ApexTrigger

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/)

### ApexPage

Represents a single Visualforce page.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

ControllerKey

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this page. Every page has an API version specified at creation. If the API
version is less than 15.0 and `ApiVersion` is not specified, `ApiVersion` defaults to
15.0.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier for the controller associated with this page:

**•** If the `ControllerType` parameter is set to `Standard` or `StandardSet`, this
value is the name of the sObject that defines the controller.

**•** If the `ControllerType` parameter is set to `Custom`, this value is the name of the
Apex class that defines the controller.


Standard Objects ApexPage

**Field** **Details**

```
ControllerType

Description

IsAvailableInTouch

IsConfirmationTokenRequired

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of controller associated with this Visualforce page. Possible values include:

**•** `Not Specified`, for pages defined with neither a `standardController` nor
a `controller` attribute on the `<apex:page>` tag

**•** `Standard`, for pages defined with the `standardController` attribute on the

`<apex:page>` tag

**•** `StandardSet`, for pages defined using the `standardController` and
`recordSetVar` attribute on the `<apex:page>` tag

**•** `Custom`, for pages defined with the `controller` attribute on the `<apex:page>`
tag

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the Visualforce page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if Visualforce tabs associated with the Visualforce page can be used in the Salesforce
mobile app ( `true` ) or not ( `false` ). (Use of this field for Salesforce Touch is deprecated.)
This field is available in API version 27.0 and later.

Standard object tabs that are overridden with a Visualforce page aren’t supported in the
Salesforce mobile app, even if you set this field for the page. The default Salesforce app page
for the object is displayed instead of the Visualforce page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether `GET` requests for the page require a CSRF confirmation token ( `true` ) or
not ( `false` ). This field is available in API version 28.0 and later.


Standard Objects ApexPage

**Field** **Details**

If you change this field’s value from `false` to `true`, links to the page require a CSRF token
to be added to them, or the page will be inaccessible.

```
Markup

MasterLabel

Name

NamespacePrefix

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The Visualforce markup, HTML, Javascript, and any other Web-enabled code that defines the
content of the page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text used to identify the Visualforce page in the Setup area of Salesforce. The Label is
**Label** .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this Visualforce page.

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


### Standard Objects ApexPageInfo

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Usage

Use Visualforce pages to add custom content that extends the base Salesforce application functionality. All users in Visualforce-enabled
organizations can view Visualforce pages, but the “Customize Application” permission is required to create or update them.

SEE ALSO:

ApexComponent

StaticResource

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

### ApexPageInfo

Represents metadata about a single Visualforce page. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

As of Summer '20 and later, this object can only be accessed by users who can view a particular Visualforce page, and users with the
View Setup and Configuration permission.

Fields

**Field** **Details**

```
ApexPageId

ApiVersion

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID for the Visualforce page.

**Type**
double


Standard Objects ApexPageInfo

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The API version for the page. Every page has an API version specified at creation. If the API
version is less than `15.0` and `ApiVersion` is not specified, `ApiVersion` defaults to
`15.0` .

```
Description

DurableId

IsAvailableInTouch

IsShowHeader

MasterLabel

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Description of the Visualforce page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if Visualforce tabs associated with the Visualforce page can be used in the Salesforce
app ( `true` ) or not ( `false` ). The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The `showHeader` value for the Visualforce page. This will be “unknown” if the Visualforce
page uses an expression to compute `showHeader` . The default value is `true` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ApexRestApiEventLog

**Field** **Details**

**Description**
The text used to identify the Visualforce page in the Setup area of Salesforce.

```
Name

NameSpacePrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the Visualforce page.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition org that creates
a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a
component in a managed package by using the
`namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, the namespace prefix is set to the namespace prefix of the
org for all objects that support it.

Note: If an object is in an installed managed package, the object has the
namespace prefix of the installed managed package. This field’s value is the
namespace prefix of the Developer Edition org of the package developer.

**•** In non-Developer Edition orgs, `NamespacePrefix` is only set for objects that are
part of an installed managed package. Objects outside of an installed managed package
do not have a namespace prefix.

Use `ApexPageInfo` to query limited metadata about Visualforce pages. Some of this metadata corresponds to settings for a Visualforce
page available in Visualforce Pages. To access Visualforce Pages, from _`Setup`_, in the _`Quick Find`_ box, enter _`Custom Code`_ . Then,
select Visualforce Pages. Other values are only available via API. Use `ApexPageInfo` [in Visualforce pages to add custom content that](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_apexpage.htm)
extends the base Salesforce application functionality.

Users can only query `ApexPageInfo` records if they can display the associated Visualforce page, or if they have the View Setup &
Configuration permission. Allow users to view Visualforce pages by modifying their user profile or assigning permission sets.

### ApexRestApiEventLog

Apex REST API event logs capture information about every Apex REST API request. This object is available in API version 55.0 and later.


Standard Objects ApexRestApiEventLog

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

DatabaseBlocks

DatabaseCpuTime

```

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

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

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


Standard Objects ApexRestApiEventLog

**Field** **Details**

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

```
DatabaseTotalTime

ExceptionMessage

FieldCount

LoginKey

MediaType

```

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
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of fields or columns, where applicable.

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


Standard Objects ApexRestApiEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The media type of the response.

```
Method

ObjectName

RequestIdentifier

RequestSize

RequestStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The apex method name.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API objects that are accessed. For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout request body, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:


Standard Objects ApexRestApiEventLog

**Field** **Details**

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

```
ResponseSize

RowsProcessed

RunTime

SessionKey

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the request. For example: `150` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time the request took, as measured by SFDC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .


Standard Objects ApexRestApiEventLog

**Field** **Details**

```
StatusCode

Timestamp

Uri

UserIdentifier

UserType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP status code for the response.

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.For
example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.


### Standard Objects ApexSoapApiEventLog

**Field** **Details**

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

### ApexSoapApiEventLog

Apex SOAP event logs contain details about custom SOAP web service calls. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClassName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The Apex class name. If the class is part of a managed package, this string includes the
package namespace.

```
ClientIp

ClientName

CpuTime

DatabaseTotalTime

LimitUsagePercent

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
The name of the client that’s using Salesforce services. This field is an optional parameter
that can be passed in API calls. If blank, the caller didn't specify a client in the CallOptions
header.

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
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The percentage of Apex SOAP calls that were made against the organization’s limit.

```
LoginKey

MethodName

QueryString

RateLimitUsage

RequestIdentifier

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
The name of the calling Apex method.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query, if one was performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The percent of the current usage of your rate limit.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects ApexSoapApiEventLog

**Field** **Details**

```
RequestStatus

RunTime

SessionKey

Timestamp

```

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
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered long-running requests for the purposes
of the Concurrent Long-Running Apex Limit.

HTTP callout processing time isn't included when calculating the 5-second limit. We pause
the timer for the callout and resume it when the callout completes.

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


Standard Objects ApexSoapApiEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

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
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

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


### Standard Objects ApexTestQueueItem

**Field** **Details**

**•** `SelfService` —Users whose access is limited because they’re organization customers
and access the application through a self-service portal.

**•** `Standard` —Standard user license. This user type also includes Salesforce Platform
and Salesforce Platform One user licenses, and admins for this org.

### ApexTestQueueItem

Represents a single Apex class in the Apex job queue. This object is available in API version 23.0 and later.

This object is available in API version 23.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
ApexClassId

ExtendedStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The Apex class whose tests are to be executed.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects ApexTestQueueItem

**Field Name** **Description**

**Description**

The pass rate of the test run.

For example: “(4/6)”. This means that four out of a total of six tests passed.

If the class fails to execute, this field contains the cause of the failure.

```
ParentJobId

ShouldSkipCodeCoverage

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Points to the AsyncApexJob that represents the entire test run.

If you insert multiple Apex test queue items in a single bulk operation, the queue
items share the same parent job. This means that a test run can consist of the
execution of the tests of several classes if all the test queue items are inserted in
the same bulk operation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to opt out of collecting code coverage information during
Apex test runs. Available in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the job. Valid values are:

**•** `Holding` [1]

**•** `Queued`

**•** `Preparing`

**•** `Processing`

**•** `Aborted`

**•** `Completed`

**•** `Failed`

1 This status applies to batch jobs in the Apex flex queue.


### Standard Objects ApexTestResult

**Field Name** **Description**

```
TestRunResultId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the associated ApexTestRunResult object.

Insert an `ApexTestQueueItem` object to place its corresponding Apex class in the Apex job queue for execution. The Apex job
executes the test methods in the class.

To abort a class that is in the Apex job queue, perform an update operation on the ApexTestQueueItem object and set its `Status`
field to _`Aborted`_ .

If you insert multiple Apex test queue items in a single bulk operation, the queue items share the same parent job. This means that a
test run can consist of the execution of the tests of several classes if all the test queue items are inserted in the same bulk operation.

### ApexTestResult

Represents the result of an Apex test method execution. This object is available in API version 23.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Details**

```
ApexClassId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The Apex class whose test methods were executed.

This is a relationship field.


Standard Objects ApexTestResult

**Field Name** **Details**

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

```
ApexLogId

ApexTestRunResultId

AsyncApexJobId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexLog for this test method execution if debug logging is enabled;
otherwise, `null` .

This is a relationship field.

**Relationship Name**
ApexLog

**Relationship Type**
Lookup

**Refers To**
ApexLog

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the ApexTestRunResult that represents the entire test run.

This is a relationship field.

**Relationship Name**
ApexTestRunResult

**Relationship Type**
Lookup

**Refers To**
ApexTestRunResult

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ApexTestResult

**Field Name** **Details**

**Description**

Points to the AsyncApexJob that represents the entire test run.

This field points to the same object as
`ApexTestQueueItem.ParentJobId` .

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

```
IsTestSetup

Message

MethodName

Outcome

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates if the results are for a test setup method. The default is false.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The exception error message if a test failure occurs; otherwise, `null` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The test method name.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The result of the test method execution. Can be one of these values:


Standard Objects ApexTestResult

**Field Name** **Details**

**•** Pass

**•** Fail

**•** CompileFail

**•** Skip

```
QueueItemId

RunTime

StackTrace

TestTimestamp

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexTestQueueItem which is the class that this test method is part
of.

This is a relationship field.

**Relationship Name**
QueueItem

**Relationship Type**
Lookup

**Refers To**
ApexTestQueueItem

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test method to run, in milliseconds.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The Apex stack trace if the test failed; otherwise, `null` .

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

The start time of the test method.


### Standard Objects ApexTestResultLimits

Usage

### You can query the fields of the ApexTestResult record that corresponds to a test method executed as part of an Apex class

execution.

### Each test method execution is represented by a single ApexTestResult record. For example, if an Apex test class contains six test methods, six ApexTestResult records are created. These records are in addition to the ApexTestQueueItem record that

represents the Apex class.

Each ApexTestResult record has an associated ApexTestResultLimits on page 610 record, which captures the Apex limits used during
execution of the test method.

### ApexTestResultLimits

Captures the Apex test limits used for a particular test method execution. An instance of this object is associated with each ApexTestResult
record. This object is available in API version 37.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Details**

```
ApexTestResultId

AsyncCalls

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the associated ApexTestResult object.

This is a relationship field.

**Relationship Name**
### ApexTestResult

**Relationship Type**
Lookup

**Refers To**
### ApexTestResult

**Type**
int


Standard Objects ApexTestResultLimits

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of asynchronous calls made during the test run.

```
Callouts

Cpu

Dml

DmlRows

Email

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of callouts made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The amount of CPU used during the test run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of DML statements made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of rows accessed by DML statements during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of email invocations made during the test run.


Standard Objects ApexTestResultLimits

**Field Name** **Details**

```
LimitContext

LimitExceptions

MobilePush

QueryRows

Soql

Sosl

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether the test run was synchronous or asynchronous.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether your org has any limits that differ from the default limits.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of mobile push calls made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of rows queried during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of SOQL queries made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects ApexTestRunResult

**Field Name** **Details**

**Description**

The number of SOSL queries made during the test run.

Usage

The ApexTestResultLimits object is populated for each test method execution, and it captures the limits used between the Test.startTest()
and Test.stopTest() methods. If startTest() and stopTest() aren’t called, limits usage isn’t captured. Note the following:

**•** The associated test method must be run asynchronously.

**•** Limits for asynchronous Apex operations (batch, scheduled, future, and queueable) that are called within test methods aren’t
captured.

**•** Limits are captured only for the default namespace.

### ApexTestRunResult

Contains summary information about all the test methods that were run in a particular Apex job. This object is available in API version
37.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Details**

```
AsyncApexJobId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The parent Apex job ID for the result.

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup


Standard Objects ApexTestRunResult

**Field Name** **Details**

**Refers To**
AsyncApexJob

```
ClassesCompleted

ClassesEnqueued

EndTime

IsAllTests

JobName

MethodsCompleted

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The total number of classes executed during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The total number of classes enqueued during the test run.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The time at which the test run ended.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether all Apex test classes were run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Reserved for future use.

**Type**
int


Standard Objects ApexTestRunResult

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods completed during the test run. This value is updated
after each class is run.

```
MethodsEnqueued

MethodsFailed

Source

StartTime

Status

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods enqueued for the test run. This value is initialized
before the test runs.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods that failed during this test run. This value is updated
after each class is run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The source of the test run, such as the Developer Console.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

The time at which the test run started.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects ApexTestRunResult

**Field Name** **Details**

**Description**

The status of the test run. Values include:

**•** Queued

**•** Preparing

**•** Processing

**•** Aborted

**•** Completed

**•** Failed

```
TestSetupTime

TestTime

UserId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the setup methods to run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test to run, in milliseconds.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user who ran the test run.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects ApexTestSuite ApexTestSuite

Represents a suite of Apex classes to include in a test run. A TestSuiteMembership object associates each class with the suite. This object
is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
TestSuiteName

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Unique, Update

**Description**

The name of the Apex test suite. This label appears in the user interface.

This value is case-sensitive and must be unique.

Insert a TestSuiteMembership object using an API call to associate an Apex class with an ApexTestSuite object. (ApexTestSuite and
TestSuiteMembership aren’t editable through Apex DML.) To remove the class from the test suite, delete the TestSuiteMembership
object. If you delete an Apex test class or test suite, all TestSuiteMembership objects that contain that class or suite are deleted.

The following SOQL query returns the membership object that relates this Apex class to this test suite.

```
SELECT Id FROM TestSuiteMembership WHERE ApexClassId = '01pD0000000Fhy9IAC'

   AND ApexTestSuiteId = '05FD00000004CDBMA2'

```

SEE ALSO:

TestSuiteMembership

### ApexTrigger

Represents an Apex trigger.


Standard Objects ApexTrigger

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

Body

```

BodyCrc

```
IsValid

LengthWithoutComments

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this trigger. Every trigger has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex trigger definition.

Limit: 1 million characters.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the trigger was last compiled
( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ApexTrigger

**Field** **Details**

**Description**
Length of the trigger without comments

```
Name

NamespacePrefix

Status

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the trigger.

Limit: 255 characters

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
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex trigger. The following string values are valid:

**•** `Active` —The trigger is active.

**•** `Inactive` —The trigger is inactive, but not deleted.

**•** `Deleted` —The trigger is marked for deletion. This is useful for managed packages,
because it allows a class to be deleted when a managed package is updated.


Standard Objects ApexTrigger

**Field** **Details**

Note: `Inactive` is not valid for ApexClass. For more information, see the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/)_ .

```
TableEnumOrId

UsageAfterDelete

UsageAfterInsert

UsageAfterUndelete

UsageAfterUpdate

UsageBeforeDelete

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the object associated with the trigger, such as Account or Contact.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after delete` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after insert` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after undelete` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after update` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update


### Standard Objects ApexTriggerEventLog

**Field** **Details**

**Description**
Specifies whether the trigger is a `before delete` trigger ( `true` ) or not ( `false` ).

```
UsageBeforeInsert

UsageBeforeUpdate

UsageIsBulk

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before insert` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before update` trigger ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is defined as a bulk trigger ( `true` ) or not ( `false` ).

Note: This field is not used for Apex triggers saved using Salesforce API version 10.0
or higher: all triggers starting with that version are automatically considered bulk, and
this field will always return `true` .

Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexClass

_Developer Guide_ [: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/)

### ApexTriggerEventLog

Apex Trigger event logs contain details about triggers that fire in an organization. This object is available in API version 55.0 and later.


Standard Objects ApexTriggerEventLog

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

DatabaseTotalTime

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
Double

**Properties**
Filter, Nillable, Sort


Standard Objects ApexTriggerEventLog

**Field** **Details**

**Description**
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

```
ExecutionTime

LoginKey

ObjectName

PlannerIdentifier

RequestIdentifier

```

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time (in milliseconds).

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object affected by the trigger.

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
`GeJCsym5eyvtEK2I` .


Standard Objects ApexTriggerEventLog

**Field** **Details**

```
RequestStatus

RunTime

SessionKey

Timestamp

```

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
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered long-running requests for the purposes
of the Concurrent Long-Running Apex Limit.

HTTP callout processing time isn't included when calculating the 5-second limit. We pause
the timer for the callout and resume it when the callout completes.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
DateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ApexTriggerEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
TriggerIdentifier

TriggerName

TriggerType

Uri

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the trigger that was fired.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
For triggers coming from managed packages, `TriggerName` includes a namespace prefix
separated with a `.` character. If no namespace prefix is present, the trigger is from an
unmanaged trigger. For example:

**•** `examplePackage.managedExampleTrigger` —Managed trigger from the
examplePackage namespace

**•** `unmanagedExampleTrigger` —Unmanaged trigger

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of this trigger.

Possible values are:

**•** AfterInsert

**•** AfterUpdate

**•** BeforeInsert

**•** BeforeUpdate

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .


### Standard Objects ApexTypeImplementor

**Field** **Details**

```
UserIdentifier

UserType

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who is using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
String

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

### ApexTypeImplementor

Represents Apex classes that directly or indirectly implement an interface. Using a SOQL query, this object gets information about public
or global classes and only global classes for installed managed packages. This object is available in API version 54.0 and later.


Standard Objects ApexTypeImplementor

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApexClassId

ClassName

ClassNamespacePrefix

DurableId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the outer class that contains the Apex class implementing the interface.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Apex class name that implements the interface. For an inner class that implements the
interface, the outer class and inner name separated by a period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that implements the interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the interface and implementor.


Standard Objects ApexTypeImplementor

**Field** **Details**

```
InterfaceApexClassId

InterfaceName

InterfaceNamespacePrefix

IsConcrete

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The foreign key to the outer class that contains the Apex class defining the interface. Null
for built-in system interfaces, such as `System.Batchable` .

This is a relationship field.

**Relationship Name**
InterfaceApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The interface name for which Apex class implementation is retrieved. For an inner interface,
the outer Apex class name and the inner interface name separated by a period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the class that defines the interface.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the implementing class is abstract ( `false` ) or not ( `true` ).

ApexTypeImplementor considers access modifiers based on the context, such as the namespace from which the ApexTypeImplementor
entity is queried. These are additional usage considerations.


Standard Objects ApexTypeImplementor

**•** In installed managed packages, you get information about all global implementors in the org, and public implementors from the
managed package itself.

**•** ApexTypeImplementor appropriately filters classes that are annotated with `@Deprecated` . For example it respects the package
version dependency settings of a class when queried from that class.

**•** ApexTypeImplementor returns implementors where `ApexClass.IsValid` is set to `False` (invalid classes) in addition to
when it’s set to `True` . Classes that don’t compile or execute can be returned. An implementor class is only guaranteed to be usable
if `ApexClass.IsValid` is set to `True` for the implementor.

**•** If a package is installed but not yet compiled because Compile on Deploy is disabled, ApexTypeImplementor returns no values until
compilation is complete. In environments like sandboxes where Compile on Deploy can be disabled, you must perform a manual
compilation to get complete results.

**•** To avoid cross-namespace collisions, always specify an InterfaceNamespacePrefix as a WHERE clause in SOQL queries for
ApexTypeImplementor. Otherwise, the query includes all namespaces instead of only the current namespace. If a package contains
an interface with the same name as an interface in a different namespace, a query without a specified InterfaceNamespacePrefix
can return false implementors that can’t be assigned to the interface.

For example, say a managed package contains a global interface named `RoundingStrategy` and a global class named
`HalfDown` that implements `RoundingStrategy` . If a subscriber org has an interface that’s also named `RoundingStrategy`,
then the query `[SELECT ApexClass.Id FROM ApexTypeImplementor WHERE InterfaceName =`
`'RoundingStrategy']`, if performed in the subscriber org, can return the ID of `HalfDown` instead of an implementor in
the subscriber org. To avoid this issue, perform a query that specifies a InterfaceNamespacePrefix: `[SELECT ApexClass.Id`

```
    FROM ApexTypeImplementor WHERE InterfaceName = 'RoundingStrategy' AND
```

`InterfaceNamespacePrefix = 'PackageNamespace']` .

Example

This example demonstrates how an interface allows flexibility in a configuration, record, or user-driven selection of the rounding strategy
to apply. The multiple implementations of the interface can be discovered using ApexTypeImplementor and the specific implementation
chosen based on user requirements.

```
   // Common interface that all rounding strategies will implement

   public interface RoundingStrategy {

      Decimal round(Decimal toRound);

   }

   public abstract class RoundingStrategies {

      public class Ceiling implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.round(System.RoundingMode.CEILING);

        }

      }

      public class HalfDown implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.round(System.RoundingMode.HALF_DOWN);

        }

      }

      public class TwoDecimalPlaces implements RoundingStrategy {

        public Decimal round(Decimal toRound) {

           return toRound.setScale(2, System.RoundingMode.HALF_UP);

```


### Standard Objects ApexUnexpectedExcpEventLog

```
        }

      }

   }

   List<ApexTypeImplementor> interfaceImpls = [

           SELECT ClassName, ClassNamespacePrefix

           FROM ApexTypeImplementor

           WHERE InterfaceName = 'RoundingStrategy' and IsConcrete = true and

   InterfaceNamespacePrefix = ''

           ORDER BY ClassName ASC NULLS LAST];

   // For example, an admin can be presented with a list of Apex classes

   // that can be applied. Simulated selection of 2 decimal places

   ApexTypeImplementor selectedRoundingStrategy = interfaceImpls[2];

   System.assertEquals('RoundingStrategies.TwoDecimalPlaces',

      selectedRoundingStrategy.ClassName);

   // Create an instance of the class that implements the interface

   RoundingStrategy rs = (RoundingStrategy)

   Type.forName(selectedRoundingStrategy.ClassNamespacePrefix,

      selectedRoundingStrategy.ClassName).newInstance();

   Decimal rounded = rs.round(7.1459);

   System.assertEquals(7.15, rounded);

### ApexUnexpectedExcpEventLog

```

Apex Unexpected Excp Event Log captures information about unexpected exceptions in Apex code execution. This object is available
in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ExceptionCategory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ApexUnexpectedExcpEventLog

**Field** **Details**

**Description**
The category of the unexpected Apex exception. For example, the LimitException exception
type is split into subcategories that indicate if you exceeded a limit, such as the total heap
size or CPU time. Possible values:

**•** Subcategories of LimitException that indicate the Apex limit you’ve exceeded. Examples:

**•** LimitException: CpuTime: Maximum CPU time on the Salesforce servers.

**•** LimitException: HeapSize: Total heap size

**•** LimitException: Queries: Total number of SOQL queries issued.

**•** LimitException: QueryRows: Total number of records retrieved by SOQL queries.

**•** LimitException: DmlStatements: Total number of DML statements issued.

**•** LimitException: Callouts: Total number of callouts (HTTP requests or web services calls)
in a transaction.

```
ExceptionMessage

ExceptionType

RequestIdentifier

StackTrace

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The class type of the unexpected exception. For example: System.MathException

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

**Properties**
Filter, Nillable, Sort


### Standard Objects ApiTotalUsageEventLog

**Field** **Details**

**Description**
The stack trace for the exception. For example:

```
                   Class.OpportunityUtility.insert: line 22, column 1

                   AnonymousBlock: line 1, column 1

```

```
Timestamp

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

### ApiTotalUsageEventLog

API Total Usage Event Log contains details about Platform SOAP API, Platform REST API, and Bulk API requests. This object is available in
API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiFamily

ApiResource

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API family. For example, REST, SOAP, or Bulk.

**Type**
string


Standard Objects ApiTotalUsageEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API method or resource. For example, `describeSObjects` for SOAP.

```
BotIdentifier

BotSessionIdentifier

ClientIp

ClientName

ConnectedAppIdentifier

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
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the client making the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the connected app making the API request.


Standard Objects ApiTotalUsageEventLog

**Field** **Details**

```
HttpMethod

IsApiLimitCounted

ObjectName

PlannerIdentifier

RequestIdentifier

StatusCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method. For example, `GET` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the request counted against the API limit ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

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


### Standard Objects AppAnalyticsQueryRequest

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP response status code for the request.

```
Timestamp

UserIdentifier

```

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

### AppAnalyticsQueryRequest

Represents a request for AppExchange App Analytics data.

AppExchange App Analytics is available for packages that passed security review and are registered to a License Management App
(LMA). Usage data is provided as package usage logs, as month-based package usage summaries, or as point-in-time subscriber snapshots.
Usage logs, monthly usage summaries, and subscriber snapshots are downloadable comma-separated value (.csv) files. For information
[on how to optimize your use of App Analytics, see AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

[Note: Usage data from Government Cloud and Government Cloud Plus orgs isn’t available in App Analytics.](https://www.salesforce.com/solutions/industries/government1/products/government-cloud/)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

[See Get Started with AppExchange App Analytics in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_intro_2gp.htm) _Second-Generation Managed Packaging Developer Guide_ .


Standard Objects AppAnalyticsQueryRequest

Fields

**Field Name** **Details**

```
AvailableSince

DataType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

An optional value used to limit the requested results file to data newly arrived in
the data lake after the specified date and time. This field is always transferred in
the Coordinated Universal Time (UTC) time zone. Use the `AvailableSince`
field as part of your catch-up query strategy.

`AvailableSince` must be later than `StartTime` and `EndTime`, if
specified. `AvailableSince` must be earlier than now. A query must include
`StartTime`, `AvailableSince`, or both.

For example, to schedule a catch-up query on `2021-04-03T18:00:00Z`
for this date range:

**•** `StartTime=2021-03-29T00:00:00Z`

**•** `EndTime=2021-03-30T00:00:00Z`

Valid `AvailableSince` values range from `2021-03-30T00:00:00Z`
`to 2021-04-03T18:00:00Z` .

For more information on `AvailableSince` and catch-up queries, read
[AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The type of usage data being requested. Valid values include:

**•** `PackageUsageLog`

**•** `PackageUsageSummary`

**•** `SubscriberSnapshot`

Note: In Summer ’20, we changed the enum names from
`CustomObjectUsageSummary` and `CustomObjectUsageLog`
to `PackageUsageSummary` and `PackageUsageLog` .

If you wrote integrations using `CustomObjectUsageSummary` or
`CustomObjectUsageLog`, they continue to work only with v47 and
earlier. After you upgrade to v48, you must update the `DataType` to
`PackageUsageSummary` and `PackageUsageLog` .


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

```
DownloadExpirationTime

DownloadSize

DownloadUrl

EndTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The time when the download URL is no longer valid. The expiration time is 60
minutes after the query is completed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the AppExchange App Analytics results file available for download,
in bytes.

**Type**
textarea

**Properties**
Nillable

**Description**

URL that the user can download data from. Populated after the request is
completed. This URL expires and is removed after the expiration time is reached.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter end time in format yyyy-MM-ddTHH:mm:ss.

Example:

2019-04-15T12:00:00

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

```
ErrorMessage

FileCompression

FileType

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Stores error message text that results from this query.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The file compression format of your requested results file. `FileCompression`
and `FileType` must align. If `FileType` is `csv`, `FileCompression`
defaults to `none` and can be `none` or `gzip` . If `FileType` is `parquet`,
`FileCompression` is `snappy` by default and can be `snappy`, `gzip`, or
`none` .

Valid values include:

**•** `gzip`

**•** `snappy`

**•** `none`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The data format of your requested results file. The default is `csv` .
`FileCompression` and `FileType` must align. If `FileType` is `csv`,
`FileCompression` defaults to `none` and can be `none` or `gzip` . If
`FileType` is `parquet`, `FileCompression` is `snappy` by default and
can be `snappy`, `gzip`, or `none` .

Valid values include:

**•** `csv`

**•** `parquet`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

**Description**

The timestamp for when the current user last viewed a record related to this
record.

```
LastViewedDate

Name

OrganizationIds

PackageIds

```

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The auto-generated name of the App Analytics query request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

Optional. Enter up to 16 comma-separated org IDs without spaces between IDs.
Or enter up to 15 comma-separated org IDs with spaces between the IDs.

To request data for all the orgs the package is installed in, leave the field blank.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

Optional. Enter up to 16 comma-separated package IDs without spaces between
IDs. Or enter up to 15 comma-separated package IDs with spaces between the
IDs. Use the subscriber package ID that begins with `033` . To retrieve a list of your
second-generation managed package IDs, run `sf package list`
`--verbose` in Salesforce CLI.

To request data on all packages registered to this License Management App,
leave the field blank.


Standard Objects AppAnalyticsQueryRequest

**Field Name** **Details**

```
QuerySubmittedTime

RequestState

StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time that the App Analytics query request was received for
processing, in Coordinated Universal Time (UTC). `QuerySubmittedTime`
is read only.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Status of the query request. Valid values are:

**•** `New`

**•** `Pending`

**•** `Complete`

**•** `Expired`

**•** `Failed`

**•** `NoData`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter start time in format yyyy-MM-ddTHH:mm:ss. All App Analytics query requests
must include `StartTime` or `AvailableSince` or both.

Example:

2019-04-14T12:00:00

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`


### Standard Objects AppDefinition

Usage

To request usage data, log in to the License Management Org (LMO) that your package is registered to, and initiate the API request from
the LMO. In a 24-hour period, you can download a maximum 20 GB of AppExchange App Analytics data.

[See Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_download_mp_logs.htm) _Second Generation Managed Packaging_
_Developer Guide_ .

If requests to view package usage log or subscriber snapshot data are inactive for 90 days, we reserve the right to stop collecting this
[data. To resume data collection, log a support case in the Salesforce Partner Community. For product, specify](https://partners.salesforce.com) **Partner Programs &**
**Benefits** . For topic, specify **ISV Technology Request** .

### AppDefinition

Represents the metadata of an app and its navigation items. Metadata is returned only for apps that the current user can access. This
object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
Description

DeveloperName

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The optional description of the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name of the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique virtual Salesforce ID for the application.


Standard Objects AppDefinition

**Field Name** **Details**

```
HeaderColor

Id

IsLargeFormFactorSupported

IsMediumFormFactorSupported

IsNavAutoTempTabsDisabled

IsNavPersonalizationDisabled

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The header color in the application. Specify the color with a hexadecimal code,
such as #0000FF for blue.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
A default Salesforce ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Large form factor is set in the `CustomApplication`
metadata.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Medium form factor is set in the `CustomApplication`
metadata.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the navigation automatically creates temporary tabs settings.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AppDefinition

**Field Name** **Details**

**Description**
Indicates whether navigation personalization is disabled.

```
IsNavTabPersistenceDisabled

IsOmniPinnedViewEnabled

IsOverrideOrgTheme

IsSmallFormFactorSupported

Label

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether workspace tabs are cleared for each new console session.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Omni-Channel component is enabled in sidebar view. The
default is false.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to override the global theme for the org. When true, the color
scheme and logo that the user has set are used. When false, the global theme
for the org is used, even if the user has set a color scheme and logo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Small form factor is set in the `CustomApplication`
metadata.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The localized label value corresponding to the MasterLabel field.


Standard Objects AppDefinition

**Field Name** **Details**

```
LogoUrl

MasterLabel

NamespacePrefix

NavType

UiType

UtilityBar

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logo URL of the application as selected by the admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The non-translated label entered when the application was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the application.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of navigation for the application. The value `Standard` is for Lightning
Experience. The value `Console` is for Salesforce console. A null value is for
Salesforce Classic.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of custom application. The value `Aloha` is for Salesforce
Classic, and `Lightning` is for Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AppExtension

**Field Name** **Details**

**Description**
The ID of the utility bar associated with this application.

### AppExtension

Represents a connection between the Field Service mobile app and another app, typically for passing record data to the Salesforce
mobile app or other apps. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

### `AppExtensionLabel` `AppExtensionName`

```
FieldServiceMobileSettingsId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label in the UI for the app extension.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the app extension.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a set of field service mobile settings.


Standard Objects AppExtension

**Field Name** **Details**

```
InstallationUrl

LaunchValue

ScopedToObjectTypes

Type

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL that takes the user to the app install location, such as the App Store or
Google Play.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A value directing the Field Service app to the appropriate app extension. The
Launch Value can be a static URL or a dynamic value that you can represent with
certain tokens. These tokens pass field information from the record that the user
is currently viewing. The basic format for these tokens is based on the field names;
for example: **{!$Name}** .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the types of records from which the app extension can be activated.
Scoping an app extension to an object lets users activate the app extension from
records of the specified type. For example, to scope to both work orders and
service appointments you would use the value
`WorkOrder,ServiceAppointment` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A picklist of types of app extensions: iOS, Android, Flow, and Lightning Apps

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ApplicationFormTemplate

**AppExtensionChangeEvent**

Change events are available for the object. Available in API version 55.0 and later.

### ApplicationFormTemplate

Represents the fields to capture application metadata as a template which is used in application tracking and processing. This object is
available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
ApprovalFlowName

ApplicationType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of application or template.

Possible values are:

**•** `Contractor`

**•** `EVCharger` —EV Charger

**•** `EnergyEfficiency` —Energy Efficiency

**•** `NewConnection` —New Connection

The default value is `NewConnection` .


Standard Objects ApplicationFormTemplate

**Field** **Details**

```
ApprovalLimitAmount

ApprovalFlowName

ApproverId

Description

Name

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount up to which the approver has the authority to approve applications.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user who must approve the application payout.

This field is a relationship field.

**Relationship Name**
Approver

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the application form template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects AppMenuItem

**Field** **Details**

**Description**
The name of the application form template.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ApplicationFormTemplateChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ApplicationFormTemplateFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ApplicationFormTemplateHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ApplicationFormTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ApplicationFormTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### AppMenuItem

Represents the organization’s default settings for items in the app menu or App Launcher.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
ApplicationId

CanvasAccessMethod

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
picklist


Standard Objects AppMenuItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The access method for the canvas app. Values can be:

**•** `Get` —OAuth Webflow

**•** `Post` —Signed Request

```
CanvasEnabled

CanvasOptions

CanvasReferenceId

CanvasSelectedLocations

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the app menu item is a canvas app ( `true` ) or not ( `false` ). The default setting
is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the options enabled for a canvas connected app. The options are:

**•** `PersonalEnabled` —The app is enabled as a canvas personal app.

**•** `HideHeader` —The publisher header, which contains the “What are you working on?”
text, is hidden.

**•** `HideShare` —The publisher **Share** button is hidden.

This field is available in API version 34.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The canvas app unique identifier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AppMenuItem

**Field** **Details**

**Description**
The selected locations for the canvas app which define where the canvas app can appear in
the user interface. For example:

```
                    Chatter,ChatterFeed,Publisher,ServiceDesk

```

```
CanvasUrl

Description

IconUrl

InfoUrl

IsAccessible

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the canvas app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of this menu item.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The icon for the menu item’s application.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for more information about the application.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, the current user is authorized to use the app. The default setting is `false` .


Standard Objects AppMenuItem

**Field** **Details**

```
IsRegisteredDeviceOnly

IsUsingAdminAuthorization

IsVisible

Label

LogoUrl

MobileAppBinaryId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, indicates that the app is available to registered devices only. The default setting is
`false` . Available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the app is pre-authorized for certain users by the administrator. The default setting
is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**

If `true`, the app is visible to users of the organization. The default setting is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app’s name.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logo for the menu item’s application. The default is the initials of the `Label` value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AppMenuItem

**Field** **Details**

**Description**
The URL for the Mobile App Binary file.

```
MobileAppInstallUrl

MobileAppInstalledDate

MobileAppInstalledVersion

MobileAppVer

MobileDeviceType

MobileMinOsVer

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to install the app. Available in API version 49.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a user installed a mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the user’s installed mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The supported device form factors for the mobile app. Available in API version 49.0 and later.

**Type**
string


Standard Objects AppMenuItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The minimum version required for the app. Available in API version 49.0 and later.

```
MobilePlatform

MobileStartUrl

Name

NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mobile platform for the app. Possible values include:

**•** `android – Android`

**•** `ios – iOS`

Available in API version 49.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to after they’ve authenticated. This field is used with
connected apps and Experience Builder sites. For sites only, this location is a fully qualified
domain name. For other apps, it’s a relative URL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:


Standard Objects AppMenuItem

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
SortOrder

StartUrl

Type

UserSortOrder

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The index value that controls where this item appears in the menu. For example, a menu
item with a sort order of 5 appears between items with sort order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a connected app, the location users are directed to after they’ve authenticated. Otherwise,
the application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of application represented by this item. The types are:

**•** `ConnectedApplication`

**•** `Network`

**•** `ServiceProvider`

**•** `TabSet`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AppointmentAssignmentPolicy

**Field** **Details**

**Description**

The index value that represents where the user set this item in the menu (or App Launcher).
For example, an item with a sort order value of 5 appears between items with sort order
values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both values. For
example, if you want the user-sorted items to appear first, followed by the organization order
for the rest, use:

```
                    SELECT ApplicationId,SortOrder,UserSortOrder FROM AppMenuItem

                     order by userSortOrder NULLS LAST, sortOrder NULLS LAST

```

Usage

Use this read-only object to view an entry in the Lightning Platform app menu or the App Launcher. You can create a SOQL query to
retrieve all items, even items the user does not see from the user interface.

There are many ways you can use AppMenuItem. Here are some examples:

**•** Build your own App Launcher or app menu in Salesforce. Create a custom page showing all the apps you have access to and that
lets you run them using single sign-on.

**•** Build your own App Launcher or app menu on a tablet or mobile app. You can have your own app for launching applications on
various mobile devices.

**•** Build an app launcher into your company’s intranet. There’s no need to have it run on Salesforce because Salesforce APIs let you
integrate with Salesforce programmatically and build an app launcher.

Tip: To get metadata information about apps and their tabs, use the Apex `Schema.describeTabs()` method, REST API
`/vXX.X/tabs/` resource, or SOAP API `describeTabs()` call.

### AppointmentAssignmentPolicy

Stores information about resource assignment rules. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
FullName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AppointmentAssignmentPolicy

**Field** **Details**

**Description**
The API name of the AppointmentAssignmentPolicy object.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment assignment policy.

Possible values are:

**•** `Possible` values are:

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

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the appointment assignment policy.


### Standard Objects AppointmentScheduleAggr

**Field** **Details**

```
PolicyApplicableDuration

PolicyType

UtilizationFactor

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which the utilization of service resources is calculated. This field is available
in API version 53.0 and later.

Possible values are:

**•** `Parameter-Based`

**•** `Monthly`

**•** `Weekly`

The default value is Parameter-Based.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of appointment assignment policy.

Possible values are:

**•** `loadBalancing`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the count type for the resource utilization. This field is available in API version 53.0
and later.

Possible values are:

**•** `NumberOfAppointments`

**•** `TotalAppointmentDuration`

The default value is TotalAppointmentDuration.

### AppointmentScheduleAggr

Records the utilization of a service resource, by date, for the Load Balancing appointment assignment policy. This object is available in
API version 52.0 and later.


Standard Objects AppointmentScheduleAggr

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppointmentDate

Name

ResourceUtilizationCount

ServiceResourceId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name or ID of the AppointmentScheduleAggr object.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of appointments scheduled for a service resource. Available in API version 53.0
and later.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling aggregate.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup


### Standard Objects AppointmentScheduleLog

**Field** **Details**

**Refers To**
ServiceResource

```
TotalResourceUtilization

UsageType

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of minutes for which the service resource has scheduled appointments.

This is a calculated field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the usage type of the AppointmentScheduleAggr object.

Possible values are:

**•** `FSL_Daily`

**•** `FSL_Monthly`

**•** `FSL_Weekly`

**•** `LightningScheduler`

The default value is 'LightningScheduler'.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleAggrOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentScheduleAggrShare on page 67**
Sharing is available for the object.

### AppointmentScheduleLog

Stores service appointments of each service Resource. This object is used to calculate the utilization of a service resource for the
AppointmentScheduleAggr object. This object is available in API version 52.0 and later.


Standard Objects AppointmentScheduleLog

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppointmentDate

AppointmentScheduleAggrId

IsUsedForResourceUtilization

Name

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The appointment scheduling aggregate associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
AppointmentScheduleAggr

**Relationship Type**
Lookup

**Refers To**
AppointmentScheduleAggr

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the appointment scheduling log is used for deriving the appointment
scheduling aggregate.

The default value is 'false'.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects AppointmentScheduleLog

**Field** **Details**

**Description**
The name or ID of the AppointmentScheduleLog object.

```
RelatedRecordId

ResourceUtilization

ServiceResourceId

UsageType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service appointment, resource absence, event, or any other related record associated
with the appointment scheduling log.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Event, ServiceAppointment

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes the service resource already has scheduled appointments for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
picklist


### Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the product associated with the AppointmentScheduleLog object.

Possible values are:

**•** `FSL_Daily` —FSL - Daily

**•** `FSL_Monthly` —FSL - Monthly

**•** `FSL_Weekly` —FSL - Weekly

**•** `LightningScheduler` —Lightning Scheduler

The default value is 'LightningScheduler'.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleLogChangeEvent on page 68**
Change events are available for the object.

**AppointmentScheduleLogFeed on page 55**
Feed tracking is available for the object.

**AppointmentScheduleLogHistory on page 63**
History is available for tracked fields of the object.

**AppointmentScheduleLogOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentScheduleLogShare on page 67**
Sharing is available for the object.

### AppointmentSchedulingPolicy

Represents a set of rules for scheduling appointments using Salesforce Scheduler. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppointmentAssignmentPolicyId

```

**Type**
reference


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name or ID of the appointment assignment policy. This is a relationship field, available
in version 52.0 and later.

**Relationship Name**
AppointmentAssignmentPolicy

**Relationship Type**
Lookup

**Refers To**
AppointmentAssignmentPolicy

```
AppointmentStartTimeInterval

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The proposed time interval in minutes between appointment start times. For example, set
the interval to 15. Appointments can then begin at the top of the hour and at 15-minute
intervals thereafter (10:00 AM, 10:15 AM, 10:30 AM, and so on). Possible values are:

**•** `5`

**•** `10`

**•** `15`

**•** `20`

**•** `30`

**•** `45`

**•** `60`

**•** `90`

**•** `120`

**•** `150`

**•** `180`

**•** `240`

**•** `300`

**•** `360`

**•** `420`

**•** `480`

**Type**
string


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the AppointmentSchedulingPolicy object.

```
ExtCalEventHandlerId

IsOrgDefault

IsSvcTerrOpHoursWithShiftsUsed

IsSvcTerritoryMemberShiftUsed

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the custom Apex class that checks service resources’ external calendar
events and returns the time slots where service resources are already booked. Available in
API version 50.0 and later.

This is a relationship field.

**Relationship Name**
ExtCalEventHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this scheduling policy is the default appointment scheduling policy for
Lightning Scheduler appointments in this org.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this scheduling policy considers the intersection of shifts and service
territory operating hours when determining the availability of service resources for
appointments (true). The default value is false. Available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

**Description**
Indicates whether this scheduling policy considers shifts of service territory members when
determining the availability of service resources for appointments (true). The default value
is false. Available in API version 56.0 and later.

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment scheduling policy.

Possible values are:

**•** `Possible` values are:

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

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the appointment scheduling policy.


Standard Objects AppointmentSchedulingPolicy

**Field** **Details**

```
ShouldConsiderCalendarEvents

ShouldEnforceExcludedResource

ShouldEnforceRequiredResource

ShouldMatchSkill

ShouldMatchSkillLevel

ShouldRespectVisitingHours

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this policy checks the Salesforce calendar for resource availability.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents excluded service resources
from being assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills and skill levels to be assigned to appointments.

**Type**
boolean


### Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents users from scheduling
appointments outside of an account’s visiting hours.

```
ShouldUsePrimaryMembers

ShouldUseSecondaryMembers

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only service resources who are
primary members of a service territory to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows service resources who are
secondary members of a service territory to be assigned to appointments.

### AppointmentTopicTimeSlot

Represents a lookup to a work type or a work type group for a time slot This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `AppointmentTopicTimeSlotKey`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Description**
Non-editable validating field used to ensure no two rows have the same time slot and work
type or work type group values in an instance.

```
Name

OperatingHoursId

TimeSlotId

WorkTypeGroupId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name or ID of the AppointmentTopicTimeSlot object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating hours that contain the time slot.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the time slot.

This is a relationship field.

**Relationship Name**
TimeSlot

**Relationship Type**
Lookup

**Refers To**
TimeSlot

**Type**
reference


Standard Objects AppointmentTopicTimeSlot

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type group associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

```
WorkTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentTopicTimeSlotChangeEvent on page 68**
Change events are available for the object.

**AppointmentTopicTimeSlotFeed on page 55**
Feed tracking is available for the object.

**AppointmentTopicTimeSlotHistory on page 63**
History is available for tracked fields of the object.

**AppointmentTopicTimeSlotOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AppointmentTopicTimeSlotShare on page 67**
Sharing is available for the object.


### Standard Objects Approval Approval

Represents an approval request for a Contract.

Note: This object is read-only and is specific to approvals on the Contract object. It isn't equal to or involved in the approval
processes represented by the ProcessInstance, which is more powerful.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ApproveComment

IsDeleted

OwnerId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Text entered by the user when they approved or rejected this approval request. Required.
Limit: 4,000 characters.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the User being asked to approve or reject the approval request. Must be a
valid User ID. Required.


Standard Objects Approval

**Field** **Details**

```
 ParentId

 RequestComment

 Status

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the Contract associated with this approval request. Must be a valid contract
ID.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Text entered by the User who created the approval request. Optional. This field can't be
updated after the Approval has been created. Limit: 4,000 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. Status of this approval request. One of the following picklist values:

**•** `Pending` —Specified only when the Approval request is created ( `create()` call)

**•** `Approved` —Specified only when the Approval request is approved ( `update()`
call)

**•** `Rejected` —Specified when the Approval request is rejected ( `update()` call) or
when it is created ( `create()` call) and immediately rejected for archival/historical
purposes.

This object allows client applications to programmatically handle approval requests for a Contract. Initially, to request a Contract approval,
a client application might create a new Approval request record, specifying the `ParentId`, OwnerId (user approving or rejecting the
request), Status (Pending), and (optionally) RequestComment fields. Note that when a client application creates the first approval request,
if the value of the Contract `Status` field is Draft, then the Approval `Status` for this record is automatically changed to In Approval
Process (see ContractStatus for more information).

A client application might subsequently update an existing Approval request, specifying the `Status` (Approved or `Rejected` ) and
an `ApproveComment` (required); the `RequestComment` field can't be updated. Updating an Approval record (either to approve
or reject) requires the client application to be logged in with “Approve Contract” permission. To update an Approval request, its `Status`
must be Pending—a client application can't update an Approval that has already been Approved or Rejected. To re-submit an approval
request for a given Contract, a client application must create a new, separate Approval record and repeat the approval process.


### Standard Objects ApprovalAlertContentDef

Once a Contract has been approved (not rejected), the Contract `LastApprovedDate` field is automatically updated, however the
Contract `Status` field isn't updated, it keeps the value InApproval.

An approved Contract must be activated explicitly. Client applications can activate a Contract by setting the value in its `Status` field
to Activated, or a User can activate a Contract via the Salesforce user interface.

A Contract can have multiple approval requests in various states (Pending, Approved, and Rejected). In addition, one User can have
multiple approval requests associated with the same Contract.

Client applications can't explicitly deleteApproval records. Approval records are deleted automatically if the parent Contract is deleted.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ApprovalAlertContentDef

Represents the mapping that links specific user-created email templates to different notification events such as initial assignment or
reassignment within an Advanced Approvals flow. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled.

Fields

**Field** **Details**

```
ApprovalFlowApiName

ApprovalStepApiName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the approval workflow.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique API name of the approval step.


Standard Objects ApprovalAlertContentDef

**Field** **Details**

```
EmailTemplateId

Name

NotificationReason

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email template that's associated with an approval step in the approval workflow.

This field is a relationship field.

**Relationship Name**
EmailTemplate

**Refers To**
EmailTemplate

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the approval alert content definition.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The reason within an approval step's lifecycle that triggers the notification for which an email
is sent. For example, when an approval work item is moved from one user to another, a
reassignment notification email is sent to the user.

Possible values are:

**•** `ApprovalCreationSuccess`

**•** `ApprovalStepAssignment`

**•** `ApprovalStepAssignmentToDelegate`

**•** `ApprovalStepReassignment`

**•** `ApprovalStepReassignmentToDelegate`

**•** `ApprovalSubmissionApprovedOrRejectedStatusUpdate`

**•** `ApprovalWorkItemStatusUpdate`

**•** `AutoApprovalConfirmation`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.


### Standard Objects ApprovalSubmission

**ApprovalAlertContentDefHistory on page 63**
History is available for tracked fields of the object.

### ApprovalSubmission

Represents the instance of an approval request that's submitted for a record of the related object. This object is available in API version
62.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available for users with a Salesforce user license of type Salesforce in Enterprise, Performance, Unlimited, and Developer
Editions.

Fields

**Field** **Details**

```
Comments

DoesSendApprovalEmail

FlowOrchestrationInstanceId

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they submit the request for approval.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether approval request emails are sent to approvers and delegates
( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the flow orchestration instance record that's associated with the approval.


Standard Objects ApprovalSubmission

**Field** **Details**

This field is a relationship field.

**Relationship Name**
FlowOrchestrationInstance

**Refers To**
FlowOrchestrationInstance

```
IsEligibleForSmartApproval

IsSmartApprovalRun

Name

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the approval submission is eligible for smart approval ( `true` ) or not
( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this approval submission either is run in smart approval mode ( `true` ) or
not ( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval submission record, for example
AS-000000001.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user or the group that owns the approval submission record.

This field is a polymorphic relationship field.


Standard Objects ApprovalSubmission

**Field** **Details**

**Relationship Name**
Owner

**Refers To**
User

```
RelatedRecordId

RelatedRecordObjectName

SmartApprvlBasisSubmissionId

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The API name of the related record that’s submitted for approval.

**Relationship Name**
RelatedRecord

**Refers To**
The objects that you have access to for approvals.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The type of record that was submitted for approval.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The previous approval submission used as reference for the auto-approval evaluation.

This field is a relationship field.

This field is only available with Advanced Approvals enabled.

**Relationship Name**
SmartApprvlBasisSubmission

**Refers To**
ApprovalSubmission

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update


### Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**Description**
Required. The status of the approval.

Valid values are:

**•** `Approved`

**•** `Canceled`

**•** `Errored`

**•** `InProgress`

**•** `Recalled`

**•** `Rejected`

**•** `Suspended`

```
SubmittedById

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the user who submitted the record for approval.

This field is a relationship field.

**Relationship Name**
SubmittedBy

**Refers To**
User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ApprovalSubmissionShare on page 67**
Sharing is available for the object.

**ApprovalSubmissionHistory on page 63**
History is available for tracked fields of the object.

### ApprovalSubmissionDetail ApprovalSubmissionDetail contains additional information about operations happening during the approval lifecycle. It will not hold

any information that’s already captured in the existing ApprovalSubmission and ApprovalWorkItem entities. This object is available in
API version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Standard Objects ApprovalSubmissionDetail

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Performance, Unlimited, and Developer Editions for users with access to the Approval Submission
object.

Fields

**Field** **Details**

```
ActionChannelName

ActionContext

ActionName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the channel where the action was performed.

Valid values are:

**•** `ApprovalRecord`

**•** `Email`

**•** `InvocableAction`

**•** `ScreenFlow`

**•** `Slack`

**•** `System`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The context of the action taken for the item assigned for approval. For example, if the approval
has been reassigned the string would be `Reassigned from User Id -`
_**`<original_assignee_id>`**_ .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The action taken for the item assigned for approval.

Valid values are:


Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**•** `Cancel`

**•** `Override`

**•** `Reassign`

**•** `Recall`

**•** `Review`

```
ActionPerformedById

ActionPerformerRole

ApprovalSubmissionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who performed the action on the item submitted for approval.

This field is a relationship field.

**Relationship Name**
ActionPerformedBy

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the user who performed the action on the item submitted for approval.

Valid values are:

**•** `Admin`

**•** `Assignee`

**•** `Delegate`

**•** `Submitter`

**•** `System`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval submission that's associated with the detail record.

This field is a relationship field.

**Relationship Name**
ApprovalSubmission


Standard Objects ApprovalSubmissionDetail

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ApprovalSubmission (the master object)

```
ApprovalWorkItemId

Comments

Name

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The approval assignment associated with the detail record.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItem

**Refers To**
ApprovalWorkItem

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they cancel, review, reassign or recall the request.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval submission detail record, for example
ASD-000000026.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ApprovalSubmissionDetailHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ApprovalWorkItem ApprovalWorkItem

Contains run-time information about each step in an approval workflow, such as assignees and their decisions regarding the object's
approval. Has a master-detail relationship with ApprovalSubmission. This object is available in API version 61.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Performance, Unlimited, and Developer Editions for users with access to the Approval Submission
object.

Fields

**Field** **Details**

```
ApprovalChainName

ApprovalConditionName

ApprovalSubmissionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the related approval chain. This field is populated when there are multiple
approval chains that are run in parallel. This field is only available with Advanced Approvals
enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the condition that assigns the work item to a user or group for approval.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval submission that's associated with this item.

This field is a relationship field.

**Relationship Name**
ApprovalSubmission


Standard Objects ApprovalWorkItem

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ApprovalSubmission (the master object)

```
AssignedToId

Comments

FlowOrchestrationWorkItemId

IsAutoReviewed

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The user, group, or queue that was assigned the work item.

This field is a polymorphic relationship field.

**Relationship Name**
AssignedTo

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The comments that the user adds when they review or override the work item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the associated flow orchestration work item.

This field is a relationship field.

**Relationship Name**
FlowOrchestrationWorkItem

**Refers To**
FlowOrchestrationWorkItem

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update


Standard Objects ApprovalWorkItem

**Field** **Details**

**Description**
Indicates whether the work item was auto-reviewed ( `true` ) or not ( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

```
IsEligibleForAutoApproval

IsEligibleForSmartApproval

Name

RelatedRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether custom logic is used for auto-approval of this approval work item (true)
or not (false).

This field is only available with Advanced Approvals enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the approval work item is eligible for smart approval ( `true` ) or not
( `false` ).

The default value is `false` .

This field is only available with Advanced Approvals enabled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the related record that’s submitted for approval, for
example AWI-000000001.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of the related record that's submitted for approval.

**Relationship Name**
RelatedRecord


Standard Objects ApprovalWorkItem

**Field** **Details**

**Refers To**
The objects that you have access to for approvals.

```
RelatedRecordObjectName

ReviewedById

ReviewedDate

SmartApprovalBasisWorkItemId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the related record that's submitted for approval.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the user that reviewed the work item.

This field is a relationship field.

**Relationship Name**
ReviewedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time when the work item was reviewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The previous approval work item used as a reference for the auto-approval evaluation.

This field is a relationship field.

This field is only available with Advanced Approvals enabled.

**Relationship Name**
SmartApprovalBasisWorkItem

**Refers To**
ApprovalWorkItem


### Standard Objects ApprovalWorkItemCondition

**Field** **Details**

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the approval work item.

Possible values are:

**•** `Approved`

**•** `Assigned`

**•** `Canceled`

**•** `Errored` —Error

**•** `Recalled`

**•** `Rejected`

**•** `Withdrawn`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ApprovalWorkItemHistory on page 63**
History is available for tracked fields of the object.

### ApprovalWorkItemCondition

Represents a condition for starting and concluding an approval step that's evaluated as part of the smart approval process. This object
is available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled with the
Modify All Data or the Approval Admin user permission.


Standard Objects ApprovalWorkItemCondition

Fields

**Field** **Details**

```
ApprovalWorkItemCriteriaId

ConditionSequencePosition

HasEvaluationSucceeded

IsConditionExcluded

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval work item criteria associated with the approval work item condition. The
approval work item criteria defines the logic by which the approval conditions are evaluated.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItemCriteria

**Relationship Type**
Master-detail

**Refers To**
ApprovalWorkItemCriteria (the master object)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order in which the condition is evaluated relative to other conditions that are part of the
requirement logic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the first value (left side) evaluates against the second value (right side)
successfully ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the condition must be excluded from evaluation ( `true` ) or not ( `false` )
in an auto-approval process.


Standard Objects ApprovalWorkItemCondition

**Field** **Details**

The default value is `false` .

```
LeftValue

LeftValueDataType

Name

OperatorType

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The first value of the condition that's evaluated against the second value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the first operand (left side) in this condition.

Possible values are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —Date/Time

**•** `MultiSelectPicklist` —Multi-Select Picklist

**•** `Number`

**•** `Other`

**•** `Picklist`

**•** `Text`

**•** `Time`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval work item condition record, for example
AWCO-000000071.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ApprovalWorkItemCondition

**Field** **Details**

**Description**
The operator for the condition.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqualTo`

**•** `HasError`

**•** `In`

**•** `IsBlank`

**•** `IsChanged`

**•** `IsEmpty`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqualTo`

**•** `None`

**•** `NotEqualTo`

**•** `NotIn`

**•** `StartsWith`

**•** `WasSelected`

**•** `WasSet`

**•** `WasVisited`

```
RightValue

RightValueDataType

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The second value (right side) of the condition that's evaluated against the first value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the second operand for the condition.

Possible values are:

**•** `Apex`


### Standard Objects ApprovalWorkItemCriteria

**Field** **Details**

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —Date/Time

**•** `MultiSelectPicklist` —Multi-Select Picklist

**•** `Number`

**•** `Other`

**•** `Picklist`

**•** `Text`

**•** `Time`

### ApprovalWorkItemCriteria

Represents the logic by which a smart approval request is evaluated. This object is available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available in Enterprise, Professional, Unlimited, and Developer Editions where Advanced Approvals is enabled with the
Modify All Data or the Approval Admin user permission.

Fields

**Field** **Details**

```
ApprovalStepApiName

ApprovalWorkItemId

```

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The unique API name of the approval step that uses the logic in the approval work item
criteria.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects AppTabMember

**Field** **Details**

**Description**
The parent approval work item associated with the approval work item criteria.

This field is a relationship field.

**Relationship Name**
ApprovalWorkItem

**Relationship Type**
Master-detail

**Refers To**
ApprovalWorkItem (the master object)

```
CriteriaType

Name

RequirementLogic

### AppTabMember

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the requirement logic is for an entry or exit condition.

Possible values are:

**•** `Entry`

**•** `Exit`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The sequentially-generated name of the approval work item criteria record, for example
AWCR-000000071.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The requirement logic of all entry or exit conditions.

Represents the list of tabs for each of the available apps. This object is available in API version 43.0 and later.


Standard Objects AppTabMember

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
AppDefinitionId

DurableId

SortOrder

TabDefinitionId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `AppDefinition` object.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number used to sort this tab in the application.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `TabDefinition` object.


### Standard Objects ApptBundleAggrDurDnscale

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

```
WorkspaceDriverField

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Refers to the workspace mapping in the `CustomApplication` Metadata
API object.

### ApptBundleAggrDurDnscale

Sums the duration of the bundle members, reduced by a predefined percentage. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundleAggregationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ApptBundleAggrDurDnscale

**Field** **Details**

**Description**
The ID of the parent appointment bundle aggregation policy.

This is a relationship field.

**Relationship Name**
BundleAggregationPolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundleAggrPolicy

```
FromBundleMemberNumber

LastReferencedDate

LastViewedDate

MaxReduction

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the first bundle member to which the downscale is applied.

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
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum reduction that can be applied to a bundle member.


### Standard Objects ApptBundleAggrPolicy

**Field** **Details**

```
Name

PercentageOfReduction

ToBundleMemberNumber

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle aggregation downscale policy.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The percentage of duration reduction.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the last bundle member to which the downscale is applied.

### ApptBundleAggrPolicy

Policy that defines how the property values of the bundle members are aggregated and assigned to the bundle. This object is available
in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.


Standard Objects ApptBundleAggrPolicy

Fields

**Field** **Details**

```
AggregationAction

AggregationFieldType

AggregationOrder

BundleFieldName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The aggregation action to be performed.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The target field type in the bundle to which the aggregation is directed.

Possible values are:

**•** `Boolean`

**•** `Date`

**•** `Numeric`

**•** `Picklist`

**•** `Picklist-Multi`

**•** `Skills`

**•** `String`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order the aggregation is triggered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle where the value is taken from the bundle member.

Possible values are: All default and custom Service Appointment fields.


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

```
BundleMemberAddiFieldName

BundleMemberFieldName

BundlePolicyId

ConstantValue

DateValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of an additional source field that is connected to the initial source field in the bundle
member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value that is used in the aggregation.

**Type**
picklist


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value will be determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

```
DoesAllowDuplicateStrings

DownscaleSortDirection

FilterCriteriaId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to allow the same string to appear more than once when using the
'Sum based on Bundle Members' action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Applies only if the Set Downscaled Duration action is set. The downscaling sorting direction
of the bundle member service appointments, according to their duration.

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for aggregating the bundle members.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup


Standard Objects ApptBundleAggrPolicy

**Field** **Details**

**Refers To**
RecordsetFilterCriteria

```
LastReferencedDate

LastViewedDate

MaxBundleDuration

Name

ShouldUpdateOnCreationOnly

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
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum bundle duration that can be accumulated from the bundle members (after
downscaling).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle aggregation policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to update the field in the bundle only when it is created.


### Standard Objects ApptBundleConfig ApptBundleConfig

Represents the general parameters that define the behavior of the bundle. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
AddToBundleStatuses

BundleStatusesToPropagate

```

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointment that are allowed to be bundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update


Standard Objects ApptBundleConfig

**Field** **Details**

**Description**
The bundle statuses that when updated are inherited by the bundle members.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
CriteriaForAutoUnbundlingId

DoesAddTravelTime

DoesDeleteEmptyBundles

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The criteria that causes a bundle service appointment to be unbundled.

This is a relationship field.

**Relationship Name**
CriteriaForAutoUnbundling

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If the bundle members aren’t in the same location, add travel time between them to the
bundle’s duration according to their sort order. The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ApptBundleConfig

**Field** **Details**

**Description**
If the bundle has no remaining bundle members, the bundle is deleted.

```
EmptyBundleStatus

LastReferencedDate

LastViewedDate

MemberStatusesNotToPropagate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status from the Canceled category that a bundle service appointment changes to if it
has no remaining bundle members, but still appears in the appointment list.

Possible values are determined by the org’s statuses.

The default value is None.

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
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The bundle member statuses that aren’t overridden when the bundle's status is updated.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`


Standard Objects ApptBundleConfig

**Field** **Details**

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
Name

OwnerId

RemoveFromBundleStatuses

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Appointment Bundle Config.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointments that are allowed to be removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`


Standard Objects ApptBundleConfig

**Field** **Details**

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

```
StatusOnRemovalFromBundle

StatusesNotToUpdateOnUnbundle

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status that a service appointment is given when it’s removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses that aren’t updated when a bundle is unbundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`


### Standard Objects ApptBundlePolicy

**Field** **Details**

**•** `Scheduled`

The default value is None.

### ApptBundlePolicy

Policy that defines how the bundling of service appointments should be handled. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundleEndTimeFieldName

BundleStartTimeFieldName

CanAllowSchleDepndInBundle

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the end time of the bundle.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the start time of the bundle.

**Type**
boolean


Standard Objects ApptBundlePolicy

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is reserved for future use.

```
ConstantTimeValue

FilterCriteriaId

IsAutomaticBundling

IsManualBundling

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the total time of the bundle
as a preset constant value.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for the bundle members. Only service appointments
that meet the criteria can be bundled.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for automatic bundling.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for manual bundling.


Standard Objects ApptBundlePolicy

**Field** **Details**

The default value is ‘false’.

```
IsTimeCalcByBundleDurationFld

LastReferencedDate

LastViewedDate

LimitAmountOfBundleMembers

LimitDurationOfBundle

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the bundle’s duration is validated. If true, the bundle’s start time is subtracted
from the bundle’s end time. If the result is a negative value, it uses ConstantTimeValue as
the bundle’s duration.

The default value is ‘false’.

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
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of bundle members that can be included in a bundle.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum duration of a bundle.


### Standard Objects ApptBundlePolicySvcTerr

**Field** **Details**

```
Name

OwnerId

Priority

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the bundle policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
The priority level that this bundle policy should be given when the bundle policies are
analyzed using the automatic mode.

### ApptBundlePolicySvcTerr

Represents a link between the BundlePolicy and the ServiceTerritory. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ApptBundlePolicySvcTerr

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

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


### Standard Objects ApptBundlePropagatePolicy

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle service territory.

```
ServiceTerritoryId

```

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

### ApptBundlePropagatePolicy

Policy that defines which property values are inherited from the bundle to the bundle members or are assigned as constant values in
the bundle members. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.


Standard Objects ApptBundlePropagatePolicy

Fields

**Field** **Details**

```
AdditionalConstantValue

BundleFieldName

BundleMemberFieldName

BundlePolicyId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The additional constant value that is connected to the initial constant value to be added to
the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle member where the value is inherited from the bundle.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This field is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ApptBundlePropagatePolicy

**Field** **Details**

```
ConstantValue

DateValue

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value to be added to the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value is determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

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


### Standard Objects ApptBundleRestrictPolicy

**Field** **Details**

**Description**
The name of the appointment bundle propagation policy.

```
ShouldAddConstantValue

ShouldUpdateOnAdd

ShouldUpdateOnRemove

ShouldUpdateOnUnbundle

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable adding a constant value to the bundle members.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
added to the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
removed from the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when performing
the Unbundle action.

### ApptBundleRestrictPolicy

Policy that defines the restrictions that are considered while forming a bundle. This object is available in API version 54.0 and later.


Standard Objects ApptBundleRestrictPolicy

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

DoesAllowEmpty

DoesRestrictAutomaticMode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows a bundle member service appointment with an empty Restriction Field Name to be
bundled.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the automatic mode.


Standard Objects ApptBundleRestrictPolicy

**Field** **Details**

```
DoesRestrictManualMode

IsRestrictByDateOnly

LastReferencedDate

LastViewedDate

Name

RestrictionFieldName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the manual mode.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want the bundle to be restricted according to the calendar date only, ignoring
the time of day.

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
The name of the appointment bundle restriction policy.

**Type**
picklist


### Standard Objects ApptBundleSortPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for applying the restriction.

Possible values are: All default and custom Service Appointment fields.

### ApptBundleSortPolicy

Policy that defines the properties by which the bundle members are sorted within the bundle. Can also be used in the automatic mode
for determining the order of the automatic selection of bundle members. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

Fields

**Field** **Details**

```
BundlePolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


Standard Objects ApptBundleSortPolicy

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

SortDirection

SortFieldName

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
Name of the appointment bundle sort policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The order of the appointments in a bundle

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for sorting the bundle members.

Possible values are: All default and custom Service Appointment fields.


### Standard Objects AppUsageAssignment

**Field** **Details**

```
SortOrder

SortType

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order of fields used for sorting the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The applied sort type for arranging the bundle. Sort for Automatic Bundling defines the order
that automated bundling uses to examine the candidate service appointments to be bundled.
Sort Within a Bundle defines the order of bundle members. It’s also used when you unbundle
to define the order that the service appointments are scheduled on the Gantt.

Possible values are:

**•** `SortForAutomaticBundling` —Sort For Automatic Bundling

**•** `SortWithinaBundle` —Sort Within a Bundle

### AppUsageAssignment

Provides application context for a record. A record can have different allowed actions or different related objects when it’s created for
different applications. For example, a Revenue Lifecycle Management order has a related `RevenueLifecycleManagement`
### AppUsageAssignment, so Salesforce knows it can create assets for that order. Available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AppUsageType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort


### Standard Objects ArchiveActivity

**Field** **Details**

**Description**
The application context for the record. Allowed values are determined by the available
licenses. For example, the `RevenueLifecycleManagement` and `BuyNow`
AppUsageTypes are available with the Subscription Management license.

```
Name

RecordId

### ArchiveActivity

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Autogenerated name for the AppUsageAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the AppUsageAssignment provides context for. For example, the order
record.

This is a relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**

**•** Order in API version 58.0 and later

**•** Asset, Contract, Quote in API version 59.0 and later

**•** WebCart in API version 60.0 and later

**•** OrderSummary in API version 61.0 and later

Represents metadata retrieved for a single Archive process initiated by an action. Retrieved metadata can include status tracking, start
and end times, record counts, and monitoring and auditing outcomes. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ArchiveActivity

Special Access Rules

This object is Read-Only and can't be deleted. Storage consumed by this object doesn't count toward your org's data storage limits.

Fields

**Field** **Details**

```
ArchivePolicyId

AttemptedRootRecordsCount

EndTime

FailedCount

FailureReason

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated policy that triggered the process. Links each execution back to its
configuration.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of root records that the action tried to process. Excludes records that were
filtered out before processing began.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the process executed successfully, or was terminated due to error.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of records that failed to process due to errors such as validation failures, missing
references, or system exceptions.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ArchiveActivity

**Field** **Details**

**Description**
Description of why process failed or only partially completed. Can include system error
messages or policy-level failures.

```
Name

ProgressPercentage

RecordsSizeInMb

SkippedRootRecordsCount

StartTime

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The autogenerated name of the action instance.

**Type**
double

**Properties**
Filter, Sort

**Description**
The percentage of records that were successfully processed.

**Type**
double

**Properties**
Filter, Sort

**Description**
Estimated total size, in megabytes (MB), of the records processed during an action, including
metadata and payload.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of root records skipped due to validation errors, exclusion filters, or data
protection thresholds.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the action started.


Standard Objects ArchiveActivity

**Field** **Details**

```
Status

SucceededCount

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Status of the current activity.

Valid values are:

**•** `Aborted` —Policy manually aborted during policy run.

**•** `Aborting` - `Aborted` process has started.

**•** `Archive Timeout` —Process automatically stopped because it took too long to execute
a specific task, or the entire run.

**•** `Completed` —Process completed successfully, and all records were processed.

**•** `Ended with Delete Failures` —Process finished its run, but failed to delete one
or more designated items.

**•** `Ended With Errors` —Process finished successfully, but some records weren't
processed. A CSV of the failed records can be downloaded from the Execution Details page.

**•** `Failed` —Process failed, and no records were archived. A CSV of the failed records is
available on the Activities tab.

**•** `No Records` —Process ran successfully but found no records matching the policy criteria.

**•** `Pending` —Process is in a queue waiting to be executed.

**•** `Process Exceeds 23h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run daily, this status indicates partial success before exceeding
the time limit.

**•** `Process Exceeds 120h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run one time in a five-day period, this status indicates partial
success before exceeding the time limit.

**•** `Process Exceeds 168h` —Activity started and ran successfully until it reached a time
limit. When a policy is set to run weekly, this status indicates partial success before exceeding
the time limit.

**•** `Query Timeout` —Process stopped because database query took too long to execute.

**•** `Running` —Process is actively executing its tasks.

**•** `Started` —Process has been initiated and is currently in progress.

**•** `Too Many Failures` —Process was abandoned after too many records failed to read
or delete.

**Type**
int

**Properties**
Filter, Sort

**Description**
The number of records processed successfully.


Standard Objects ArchiveActivity

**Field** **Details**

```
TotalRecordCount

Type

```

**Type**
int

**Properties**
Filter, Sort

**Description**
The total number of records initially selected for processing, including successful, failed, and
skipped records.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Specifies the type of archive process to be executed. This static enum categorizes the purpose
or mode of the run.

Valid values are:

**•** `Analyzer`

**•** `Archive`

**•** `Archive-fail-to-delete`

**•** `Estimate`

**•** `Export`

**•** `Export-and-download`

**•** `Export-to-external-bucket`

**•** `Import-data-archive`

**•** `Import-data-load`

**•** `Index-request`

**•** `None`

**•** `Purge`

**•** `Purge-by-retention`

**•** `Purge-estimation`

**•** `RTBF-SDK`

**•** `Unarchive`

**•** `Unarchive-retry`

**•** `Unarchive-sdk`


### Standard Objects ArchivePolicyDefinition ArchivePolicyDefinition

Represents a data lifecycle policy that, in each row, defines the scope, frequency, and rules for automated archiving or purging of records
from a root entity, such as Contact or Lead. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Create, Update, and Delete operations are restricted to the Archive Admin profile. All other profiles have Read-Only access.

Fields

**Field** **Details**

```
DataProtectionThreshold

Description

IsActive

Name

```

**Type**
int

**Properties**
Create, Filter, Sort, Update

**Description**
Specifies a retention buffer, in days, during which recently updated or sensitive records must
not be archived or deleted. Enforces data protection compliance.

**Type**
textarea

**Properties**
Create, Update

**Description**
The purpose or scope of the policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the policy is active and eligible for execution. Only active policies can be
executed by scheduled or manual processes.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ArchivePolicyDefinition

**Field** **Details**

**Description**
The unique name assigned to the policy.

```
Type

Query

QueryLimit

RootEntityName

RunFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Process type that the policy executes.

Valid values are:

**•** `Archive`

**•** `Import`

**•** `Purge`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A complete SOQL or custom query defining the set of records to archive or purge, based on
policy rules. Determines which records are eligible for processing.

**Type**
int

**Properties**
Create, Filter, Sort, Update

**Description**
The maximum number of root records this policy can process in a single run. Used to throttle
execution for scalability and control.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the Salesforce object targeted by the policy. Determines which object’s
records are queried and processed.

**Type**
picklist


### Standard Objects Article Type __DataCategorySelection

__DataCategorySelection

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies how often the policy is executed—manually or on a regular interval. Enables
automation for recurring data lifecycle operations.

Valid values are:

**•** `None`

This option is specifically for manual policy runs.

**•** `Daily`

**•** `Weekly`

**•** `Monthly`

### Article Type __DataCategorySelection __DataCategorySelection

A data category selection represents a data category that classifies an article. This object is available in API version 19.0 and later.

This object can be used to associate an article with data categories from a data category group or to query the category selections for
an article.

### The object name is variable and has a syntax of Article Type __DataCategorySelection, where Article Type is the Object

`Name` for the article type associated with the article. For example, `Offer__DataCategorySelection` represents the association
between the `Offer` article type and its data categories. Every article is associated with an article type.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `getDeleted()`, `retrieve()`

Special Access Rules

Knowledge must be enabled in your org. Not available in Lightning Knowledge. Users can only access, create or delete data category
selection visible to their role, permission set, or profile. If a user has partial visibility on an article's categorization, only the visible categories
are returned.

Fields

**Field Name** **Details**

```
DataCategoryGroupName

```

**Type**

DataCategoryGroupReference

**Properties**
Create


Standard Objects Article Type __DataCategorySelection
__DataCategorySelection

**Field Name** **Details**

**Description**
Unique name of the data category group which has categories associated with the article.

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
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the article associated with the data category selection.

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use the _`Article Type`_ __DataCategorySelection object to query and manage article categorization in
your org. Client applications can create a categorization for an article with a Draft status. They can also delete and query article
categorizations.

Note: When using _`Article Type`_ __DataCategorySelection to classify an article, you can't select both a category (for example
USA) and one of its descendants (California) or ascendant categories (North America). In this case, only the first category is selected.

Answers zones use QuestionDataCategorySelection to classify questions.

SOQL Sample

The following SOQL query returns the data category selections used to classify the article whose ID is `ka0D000000005ApIAI` .

```
SELECT Id,DataCategoryName, ParentId

     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```

This clause only returns category unique names. To retrieve category labels use the following clause:

```
SELECT Id,toLabel(DataCategoryName), ParentId

     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```

Tip: You can also use relationship queries to retrieve categorizations from an article type.

SEE ALSO:

QuestionDataCategorySelection


### Standard Objects Asset Asset

Represents an item of commercial value, such as a product sold by your company or a competitor, that a customer has purchased.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

Address

### `AssetLevel`

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Required) ID of the Account associated with this asset. Must be a valid account ID. Required
if `ContactId` isn’t specified.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
Represents the physical address or geolocation of the asset.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset’s position in an asset hierarchy. If the asset has no parent or child assets, its level
is 1. Assets that belong to a hierarchy have a level of 1 for the root asset, 2 for the child assets
of the root asset, 3 for their children, and so forth. On assets created before the introduction


Standard Objects Asset

**Field** **Details**

of this field, the asset level defaults to –1. After the asset record is updated, the asset level is
calculated and automatically updated.

```
AssetProvidedById

AssetServicedById

AssetTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account that provided the asset, typically a manufacturer.

This field is a relationship field.

**Relationship Name**
AssetProvidedBy

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account in charge of servicing the asset.

This field is a relationship field.

**Relationship Name**
AssetServicedBy

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset type associated with the asset.

This field is a relationship field.

This field is available in API version 62.0 and later for users with the Health Cloud Appointment
Management permission set.


Standard Objects Asset

**Field** **Details**

**Relationship Name**
AssetType

**Relationship Type**
Lookup

**Refers To**
AssetType

```
Availability

AveragetimetoRepair

AveragetimeBetweenFailure

AverageUptimePerDay

City

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of expected uptime where the asset was available for use.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the number of hours it typically takes to repair an asset after a failure.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the number of hours that typically elapses before the asset is likely to fail again.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The average number of hours per day the asset is expected to be available for use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city detail for the address.


Standard Objects Asset

**Field** **Details**

```
ConsequenceOfFailure

ContactId

Country

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business impact associated with the asset’s failure. Using this field, you can address the
[asset’s health and take action using Flows. To enable this field, use Object Manager to update](https://help.salesforce.com/s/articleView?id=platform.flow.htm&type=5&language=en_US)
the field availability. Make sure that the field is visible for field-level security and for page
[layout. To learn more, see What Determines Field Access. The picklist values aren’t predefined](https://help.salesforce.com/s/articleView?id=platform.customize_fieldaccess.htm&type=5&language=en_US)
in orgs created before Winter ’22 that aren’t Field Service enabled. This field is available in
API version 53.0 and later.

Possible values are:

**•** `Insignificant`

**•** `Minor`

**•** `Moderate`

**•** `Major`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if `AccountId` isn’t specified. ID of the Contact associated with this asset. Must
be a valid contact ID that has an account parent (but doesn’t need to match the asset’s
`AccountId` ).

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country detail for the address.


Standard Objects Asset

**Field** **Details**

```
CurrencyIsoCode

CurrentAmount

CurrentLifecycleEndDate

CurrentMrr

CurrentQuantity

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the invoice. The default value is USD.

This field is available in API version 55.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for future use.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the end of the period shown as current. System-populated field inherited from
the end date of the current asset state period. If that field is empty, as with an evergreen
subscription, the Current Lifecycle End Date field is also empty.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The asset’s monthly recurring revenue during the current asset state period. System-populated
field inherited from the monthly recurring revenue on the current asset state period. If no
asset state period is current, the value is `0` . Label is Current Monthly Recurring Revenue.

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
double


Standard Objects Asset

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The asset’s quantity during the current asset state period. System-populated field inherited
from the quantity on the current asset state period. If no asset state period is current, the
value is `0` .

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

```
Description

DigitalAssetStatus

ExternalIdentifier

GeocodeAccuracy

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the asset.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of digital tracking of the asset. The default picklist includes the following values:

**•** `On`

**•** `Off`

**•** `Warning`

**•** `Error`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the matching record in an external system. This field is available in API version 49.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address.


Standard Objects Asset

**Field** **Details**

```
HasLifecycleManagement

InstallDate

IsCompetitorProduct

IsInternal

LastReferencedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this asset is a lifecycle-managed asset, otherwise false. You can’t switch an asset to a
lifecycle-managed asset or the reverse. This field is system populated.

The default value is _`false`_ .

This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the asset was installed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this Asset represents a product sold by a competitor ( `true` ) or not
( `false` ). The default value is `false` . Its UI label is Competitor Asset.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the asset is produced or used internally ( `true` ) or not ( `false` ). The default
value is `false` . Its UI label is Internal Asset.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. Its UI label is Last Modified Date.


Standard Objects Asset

**Field** **Details**

```
LastViewedDate

Latitude

LifecycleEndDate

LifecycleStartDate

LocationId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
double

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the end of the asset’s lifecycle. System-populated field inherited from the end
date of the final asset state period. If that field is empty, as with an evergreen subscription,
the lifecycle has no end date. This field is available in API version 50.0 and later. This field is
available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the beginning of the asset’s lifecycle. System-populated field inherited from the
start date of the earliest asset state period. This field can’t be edited. When a new asset action
affects the start date of an asset state period, the period is deleted and a new one is generated.
This field is available in API version 50.0 and later. This field is available when CPQ Plus,
Salesforce Billing, or Revenue Cloud is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset’s location. Typically, this location is the place where the asset is stored, such as a
warehouse or van.


Standard Objects Asset

**Field** **Details**

If you have access to the location entity, it doesn’t necessarily mean you can access the
location id field. To access the location, you must have `userHasLocation` user access.

```
Longitude

ManufactureDate

Name

OwnerId

ParentId

```

**Type**
double

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the asset was manufactured. This field is available from API version 49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
(Required) Name of the asset. Label is Asset Name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The asset’s owner. By default, the asset owner is the user who created the asset record. Its
UI label is Asset Owner.

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


Standard Objects Asset

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset’s parent asset. Its UI label is Parent Asset.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Asset

```
PostalCode

Price

PricingSource

Product2Id

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the address.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Price paid for this asset.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Pricing source to use when amending or renewing an asset.

Valid values are:

**•** `LastTransaction` —Last Transaction

**•** `PriceBookListPrice` —Price Book or List Price

Available in API version 60.0 and later.

**Type**
reference


Standard Objects Asset

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Optional) ID of the Product2 associated with this asset. Must be a valid Product2 ID. Its UI
label is Product.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductCode

ProductDescription

ProductFamily

PurchaseDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product code of the related product.

**Type**
string

**Properties**
Filter, Sort, Nillable

**Description**
The product description of the related product.

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The product family of the related product.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date on which this asset was purchased.


Standard Objects Asset

**Field** **Details**

```
Quantity

QuantityIncreasePricingType

RecordTypeId

Reliability

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity purchased or installed. The Quantity field value isn’t set by Customer Asset Lifecycle
Management. Instead, you can populate the field as you need.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specify which pricing type to use when the quantity of this asset is increased. Its UI label is
Pricing Type for Quantity Increase. This field is available in API version 56.0 and later. This
field is available when Revenue Cloud is enabled.

Possible values are:

**•** `LastNegotiatedPrice` —Available in API version 58.0 and later.

**•** `ListPrice`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier for the asset.

This field is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of expected uptime where the asset wasn’t subject to unplanned downtime.


Standard Objects Asset

**Field** **Details**

```
RenewalPricingType

RenewalTerm

RenewalTermUnit

RootAssetId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The price used when renewing a subscription. Its UI label is Pricing Type for Renewal. This
field is available in API version 55.0 and later. This field is available when Revenue Cloud is
enabled.

Possible values are:

**•** `LastNegotiatedPrice`

**•** `ListPrice`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
With Renewal Term Unit, defines the default subscription term for renewal quotes. This field
is available in API version 55.0 and later. This field is available when Revenue Cloud is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time for a subscription term. This field is available in API version 55.0 and later.
This field is available when Revenue Cloud is enabled.

Possible values are:

**•** `Annual` —Available in API version 58.0 and later. —UI label is `Years` .

**•** `Months`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level asset in an asset hierarchy. Depending on where an asset lies in
the hierarchy, its root could be the same as its parent. Its UI label is Root Asset.

This field is a relationship field.

**Relationship Name**
RootAsset


Standard Objects Asset

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Asset

```
SalesStoreId

SerialNumber

State

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the RetailStore or WebStore associated with this Asset.

This field is a polymorphic relationship field.

To access this field, your org must have a Salesforce Order Management license or a B2B
Commerce License.

This field is available in API v60.0 and later.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
RetailStore, WebStore

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Serial number for this asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state detail for the address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Asset

**Field** **Details**

**Description**
Customizable picklist of values. The default picklist includes the following values:

**•** `Purchased`

**•** `Shipped`

**•** `Installed`

**•** `Registered`

**•** `Obsolete`

```
StatusReason

StockKeepingUnit

Street

SumDowntime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The explanation of the device status. This field is available from API version 49.0 and later.

Possible values are:

**•** `Not Ready`

**•** `Off`

**•** `Offline`

**•** `Online`

**•** `Paused`

**•** `Standby`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SKU assigned to the related product.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street detail for the address.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects Asset

**Field** **Details**

**Description**
Accumulated downtime (planned and unplanned), determined as follows:

**•** When only `UptimeRecordStart` is set, the sum of all downtime from

```
                     UptimeRecordStart

```

**•** When `UptimeRecordStart` and `UptimeRecordEnd` are set, the sum of all
downtime from `UptimeRecordStart` to `UptimeRecordEnd`

Otherwise, downtime isn’t accumulated.

```
SumUnplannedDowntime

TotalLifecycleAmount

UptimeRecordEnd

UptimeRecordStart

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Accumulated unplanned downtime, determined as follows:

**•** When only `UptimeRecordStart` is set, the sum of all unplanned downtime from

```
   UptimeRecordStart

```

**•** When `UptimeRecordStart` and `UptimeRecordEnd` are set, the sum of all
unplanned downtime from `UptimeRecordStart` to `UptimeRecordEnd`

Otherwise, unplanned downtime isn’t accumulated.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of revenue for the asset, including revenue from each stage in the asset
lifecycle. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date until which `SumDowntime` and `SumUnplannedDowntime` are accumulated.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date from which `SumDowntime` and `SumUnplannedDowntime` are accumulated.


Standard Objects Asset

**Field** **Details**

```
UsageEndDate

Uuid

```

Usage

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when usage for this asset ends or expires.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID for the asset. This field is available in API version 49.0 and later.

Use this object to track products sold to customers. With asset tracking, a client application can quickly determine which products were
previously sold or are currently installed at a specific account. You can also create hierarchies of up to 10,000 assets.

For example, suppose that your company wants to renew and upsell opportunities on products sold in the past. Similarly, your company
can track competitive products in a customer environment where products can be replaced or swapped out.

Asset tracking is also useful for product support, providing detailed information to assist with product-specific support issues. For example,
the `PurchaseDate` or `SerialNumber` can indicate whether a given product has certain maintenance requirements, including
product recalls. Similarly, the `UsageEndDate` can indicate when the asset was removed from service or when a license or warranty
expires.

If an application creates an Asset record, it must specify a `Name` and either an `AccountId`, `ContactId`, or both.

With REST API, use the `getRelatedListInfo` function to get information about related lists on the asset. Note that when requesting
information about _`PrimaryAssets`_, the response is labeled `Related Assets`, and the response for _`RelatedAssets`_ is
labeled `Primary Assets` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, those objects are available in the same API versions as
this object. Otherwise, they’re available in the specified API version and later.

**[AssetChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AssetFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**AssetOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects AssetAction

**AssetShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### AssetAction

Represents a change made to a lifecycle-managed asset. The fields can’t be edited. This object is available in API version 50.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
ActionDate

ActualTaxChange

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date when an asset action change is recorded. This date can differ from the start date
of the related asset state period. For example, suppose that a customer cancels a subscription
in June, and the subscription expires in October. The date the customer cancels the
subscription (June) is the action date of the asset action. The cancellation's effective date
(October) is the start date of the asset state period.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of actual tax from all asset action sources. This field is populated by the system.
Label is **Change in Actual Tax** .

This field is a calculated field.


Standard Objects AssetAction

**Field** **Details**

```
AdjustmentAmountChange

Amount

AssetActionNumber

AssetId

CanRollBack

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of adjustment amount from all asset action sources. This field is populated by the
system. Label is **Change in Adjustment Amount** .

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The delta in the total asset amount resulting from an asset action.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action. Label is **Name** .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lifecycle-managed asset. Label is **Asset** .

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AssetAction

**Field** **Details**

**Description**
Indicates whether the last asset action can be rolled back ( `true` ). If this property is set to
`false`, the asset and the last asset action can’t be rolled back.

The default value is `false` . This field is available in API version 65.0 and later.

```
CategoryEnum

EstimatedTaxChange

MrrChange

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The business category of the asset action, for use in reporting. Asset action totals are broken
out by the picklist values on this required field, and those totals are in turn reflected on assets.
These categories are available and aren’t customizable. Label is **Business Category** .

Possible values are:

**•** `Cancellations`

**•** `Cross-Sells`

**•** `Downgrades` Indicates a transition to a lower-level version or tier of an asset.

**•** `Downsells` Indicates a negative quantity amendment or a decreased Line Item total
price with no change in quantity.

**•** `Initial Sale` Indicates that the asset is initially purchased by an account.

**•** `Other`

**•** `Renewals`

**•** `Swaps` Indicates the exchange of one asset for another. Applies to both swapped-out
and swapped-in actions.

**•** `Terms And Conditions Changes`

**•** `Transfers` Indicates that an asset is transferred from one account to another.

**•** `Upgrades` Indicates a transition to a higher-level version or tier of an asset.

**•** `Upsells` Indicates a positive quantity amendment or an increased Line Item total
price with no change in quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of estimated tax from all asset action sources. This field is populated by the system.
Label is **Change in Estimated Tax** .

This field is a calculated field.

**Type**
currency


Standard Objects AssetAction

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The delta in the asset’s monthly recurring revenue resulting from an asset action. For example,
suppose that the MRR during an asset state period is $200 and the next asset action adds
$100. Then this field’s value is $100. Label is **Change in Monthly Recurring Revenue** .

```
ProductAmountChange

QuantityChange

```

RolledbackAssetAction

```
SubtotalChange

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of product amount from all asset action sources. This field is populated by the
system. Label is **Change in Product Amount** .

This field is a calculated field.

**Type**
double

**Properties**
Filter, Sort

**Description**
The delta in the asset quantity resulting from an asset action. For example, suppose that the
asset quantity during an asset state period is 20 and the next asset action adds 10. Then this
field’s value is 10. Label is **Change in Quantity** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last asset action rolled back in the current rollback transaction. This field is available in
API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of subtotal from all asset action sources. This field is populated by the system.
Label is **Change in Subtotal** .

This field is a calculated field.


Standard Objects AssetAction

**Field** **Details**

```
Subtype

TotalAmount

TotalCancellationsAmount

TotalCrossSellsAmount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The subtype of the action on the asset.

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

This field is available in API version 65.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the current and previous asset action amount. This field is populated by the
system.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Cancellations` .
This field is populated by the system.

**Type**
currency


Standard Objects AssetAction

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Cross-Sells` . This
field is populated by the system.

```
TotalDowngradesAmount

TotalDownsellsAmount

TotalInitialSaleAmount

TotalMrr

TotalOtherAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Downgrades` . This
field is populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Downsells` . This
field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Initial Sale` .
This field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the monthly recurring revenue for the current and previous asset action. This
field is populated by the system. Label is **Total Monthly Recurring Revenue** .

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects AssetAction

**Field** **Details**

**Description**
The sum of current and previous asset action amounts categorized as `Other` . This field is
populated by the system.

```
TotalQuantity

TotalRenewalsAmount

TotalSwapsAmount

TotalTermsAndConditionsAmount

TotalTransfersAmount

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the changes in quantity for the current and previous asset action. This field is
populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Renewals` . This field
is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Swaps` . This field is
populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Terms and`
`Conditions Changes` . This field is populated by the system. Label is **Total Terms**
**and Conditions Changes Amount** .

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects AssetActionSource

**Field** **Details**

**Description**
The sum of current and previous asset action amounts categorized as `Transfers` . This
field is populated by the system.

```
TotalUpgradesAmount

TotalUpsellsAmount

Type

### AssetActionSource

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Upgrades` . This field
is populated by the system and is available in API version 66.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Upsells` . This field
is populated by the system.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The REST API used to generate the asset action. This field is populated by the system.

Valid values are:

**•** `Cancel`

**•** `Change`

**•** `Convert`

**•** `Generate`

Represents an optional way to record what transactions caused changes to lifecycle-managed assets. Use it to trace financial and other
information about asset actions. This object supports Salesforce order products and work order line items, and transaction IDs from other
systems. The fields can’t be edited. This object is available in API version 50.0 and later.


Standard Objects AssetActionSource

Supported Calls

`createable()`, `deletable()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`,
`query()`, `retrieve()`, `search()`, `undeletable()`, `updateable()` .

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
ActualTax

AdjustmentAmount

AssetActionId

```

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The region-specific tax amount determined at time of the order.

This field is not used for price and tax calculations.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
An adjustment to the product amount, such as a discount.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort

**Description**
The related asset action, that is, the change caused by an asset action source transaction.

This field is a relationship field.

**Relationship Name**
AssetAction

**Relationship Type**
Lookup

**Refers To**
AssetAction


Standard Objects AssetActionSource

**Field** **Details**

```
AssetActionSourceNumber

BillingReference

Discount

DiscountAmount

EffectiveGrantDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action source. Label is **Name** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the OrderItem or OrderItemDetail record that this AssetActionSource record is
created for.

**Type**
percent

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The discount, expressed as a percentage, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The discount, expressed as currency, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The date when the resources associated with the asset were granted.

This field is available in orgs that have Revenue Cloud when Rate Management is enabled.

This field is available in API version 62.0 and later.


Standard Objects AssetActionSource

**Field** **Details**

```
EndDate

EstimatedTax

ExternalReference

ExternalReferenceDataSource

LegalEntityId

```

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The end date of the service or change.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The estimate of the region-specific tax amount made at time of the transaction.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of an asset action source transaction originating in a system outside of Salesforce.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
A system outside of Salesforce that contains asset action source transactions.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the legal entity record associated with the asset action source transaction.

This field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup


Standard Objects AssetActionSource

**Field** **Details**

**Refers To**
LegalEntity

```
ListPrice

NetUnitPrice

ObligatedAmount

OriginalLineNumber

```

**Type**
currency

**Properties**
Creatable, Filter, Nillable, Sort, Updateable

**Description**
List price for the order product. Value is inherited from the associated PriceBookEntry upon
order product creation.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The final adjusted unit price, inclusive of all adjustments, but exclusive of tax. The unit price
after all price adjustments are applied.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
When a line amount is prorated, this amount shows the service amount that’s been consumed.

**Type**
int

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The number of the original order item detail line. Salesforce uses this information to create
a record to amend, renew, or cancel an order. This field is available in API version 64.0 and
later.

**Relationship Name**
OrderItemDetail

**Relationship Type**
Lookup

**Refers To**
LineNumber


Standard Objects AssetActionSource

**Field** **Details**

```
PeriodBoundary

PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
picklist

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Boundary delimiters for periods. It determines when a period starts and/or ends.

Valid values are:

**•** `AlignToCalendar`

**•** `Anniversary`

**•** `DayOfPeriod`

**•** `LastDayOfPeriod`

**Type**
int

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The number specifying the day number when Period Boundary is a specific day in a
week/month/year. It only applies when PeriodBoundary is set to "day of period.”

**Type**
picklist

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency2 is Annual or by manual user entry. Possible values are:

1-January

2-February

3-March

4-April

5-May

6-June

7-July

8-August

9-September

10-October

11-November

12-December


Standard Objects AssetActionSource

**Field** **Details**

```
PricebookEntryId

PricingTermCount

ProductAmount

ProductSellingModelId

ProrationPolicyId

Quantity

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
PricebookEntry is used as a lookup for price information in order to pre-populate OrderItem's
ListPrice and UnitPrice.

**Type**
double

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Number of pricing terms is this subscription product.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The product amount after the asset action source transaction.

**Type**
reference

**Properties**
Creatable, Filter, Group, Nillable, Sort, Updateable

**Description**
Specifies the product selling model type. Foreignkey to ProductSellingModel entity.

**Type**
reference

**Properties**
Creatable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the ProrationPolicy used for pricing.

**Type**
double

**Properties**
Creatable, Filter, Nillable, Sort, Updateable


Standard Objects AssetActionSource

**Field** **Details**

**Description**
The product quantity or the change in product quantity after the asset action source
transaction.

```
ReferenceEntityItemId

SegmentIdentifier

StartDate

Subtotal

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of an asset action source transaction originating in Salesforce. The transaction can be
an order product or a work order line item.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, WorkOrderLineItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ramp segment associated with the asset action source transaction.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The start date of the service or change.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the product amount and the adjustment amount.

This field is a calculated field.


Standard Objects AssetActionSource

**Field** **Details**

```
TaxTreatmentId

TotalLineAmount

TotalPrice

TransactionDate

UnitPrice

```

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
Lookup to Tax Treatment entity. It's used to calculate tax.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The price of the line before any price adjustments were applied. SalesTransactionItem:
ProratedStartingTotal / StartingPriceTotal. Note: TotalPrice is computed using the UnitPrice,
which includes discounts (price adjustments), while TotalLineAmount doesn’t include price
adjustments.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Calculated by the pricing engine for ARC. Summation of TotalAdjustmentAmount plus
TotalLineAmount for this item.

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The date of a source transaction, such as an order date.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The unit price of the item before any discounts or tax calculation.


### Standard Objects AssetAttribute AssetAttribute

Stores asset attributes to track and analyze asset conditions to improve their uptime. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `update()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
AssetId

AttributeDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset.

This field is a relationship field.

**Relationship Name**
### Asset

**Relationship Type**
Lookup

**Refers To**
### Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the attribute definition for this asset attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup


Standard Objects AssetAttribute

**Field** **Details**

**Refers To**
AttributeDefinition

```
AttributeName

AttributePicklistValueId

AttributeValue

ExternalId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name given to the asset attribute in the UI by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the attribute picklist value if the attribute is a picklist type.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**
AttributePicklistValue

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores the value of an asset attribute, for example 5-TB storage .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An auto-generated ID of the attribute record saved in an external system (for example an
HBase database). This field is reserved and used for internal purpose.


### Standard Objects AssetContractRelationship

Usage

Add asset descriptors to the AssetAttribute object instead of creating multiple custom attributes on an asset. This helps scale to a high
asset volume in the system.

SEE ALSO:

AttributeDefinition

AttributePicklist

AttributePicklistValue

RecordsetFltrCritMonitor

### AssetContractRelationship

Represents a relationship between an asset and a contract. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud.

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the asset related to the contract.

This field is a relationship field.

**Relationship Name**
### Asset

**Relationship Type**
Lookup

**Refers To**
### Asset


Standard Objects AssetContractRelationship

**Field** **Details**

```
ContractId

EndDate

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the contract related to the asset.

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The end date and time of the relationship between contract and asset.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. The associated UI label is **Last Modified Date** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user accessed this record or list view ( `LastReferencedDate` ) but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects AssetDowntimePeriod

**Field** **Details**

**Description**
The auto-generated number assigned to AssetContractRelationship. (Read Only)

```
StartDate

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date and time of the relationship between contract and asset.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetContractRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetContractRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

### AssetDowntimePeriod

Represents a period during which an asset is not able to perform as expected. Downtime periods include planned activities, such as
maintenance, and unplanned events, such as mechanical breakdown. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `AssetDowntimePeriodNumber`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number of this asset downtime period record.


Standard Objects AssetDowntimePeriod

**Field** **Details**

```
AssetId

Description

DowntimeType

EndTime

IsExcluded

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset this asset downtime period record is for.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of this asset downtime period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of this asset downtime period. Possible values are:

**•** `Planned`

**•** `Unplanned`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The time this asset downtime period ended.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether this asset downtime period is excluded from the calculation of accumulated
downtime and accumulated unplanned downtime, and therefore not included in availability
and reliability calculations.

**Type**
dateTime


### Standard Objects AssetOwnerSharingRule

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The time this asset downtime period started.

### AssetOwnerSharingRule

Represents the rules for sharing an Asset with users other than the owner. This object is available in API version 33.0 and later.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal users can’t access this object.


Standard Objects AssetOwnerSharingRule

Fields

**Field** **Details**

```
AssetAccessLevel

Description

DeveloperName

GroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

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
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Cases owned by users in the source group
trigger the rule to give access.


### Standard Objects AssetRateAdjustment

**Field** **Details**

```
Name

UserOrGroupId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. Target users or groups are given access.

Use this object to manage the sharing rules for assets. General sharing uses this object.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### AssetRateAdjustment

Stores the tier rate adjustments for the asset rate card entries. This object is available in API version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.


Standard Objects AssetRateAdjustment

Fields

**Field** **Details**

```
AdjustmentType

AdjustmentValue

AssetRateCardEntryId

LowerBound

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of rate adjustment.

Valid values are:

**•** `Amount` —Adjusts rate by using a specific amount.

**•** `Override` —Adjusts rate by using the override rate.

**•** `Percentage` —Adjusts rate by using a percentage.

**Type**
double

**Properties**
Filter, Sort

**Description**
The value of the adjustment.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent asset rate card entry record associated with the asset rate adjustment.

This field is a relationship field.

**Relationship Name**
AssetRateCardEntry

**Relationship Type**
Master-detail

**Refers To**
AssetRateCardEntry (the master object)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The minimum quantity for the adjustment to be applicable.


### Standard Objects AssetRateCardEntry

**Field** **Details**

```
Name

UpperBound

### AssetRateCardEntry

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the asset rate adjustment.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The maximum quantity for the adjustment to be applicable.

Stores the negotiated rate card entries that are associated with an asset in Revenue Cloud. This object is available in API version 62.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the asset rate card entry record.

This field is a relationship field.


Standard Objects AssetRateCardEntry

**Field** **Details**

**Relationship Name**
Asset

**Relationship Type**
Master-detail

**Refers To**
Asset (the master object)

```
BindingObjectFormula

BindingObjectId

BindingObjectRateOrder

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The formula that returns the ID of the associated binding object, if specified. If binding object
isn't added, the formula returns the asset ID of the asset related to this asset rate card entry.
This field is read-only. Available in API version 65.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the binding object associated with the asset rate card entry. Available in API version
65.0 and later.

This field is a relationship field.

**Relationship Name**
BindingObject

**Refers To**
Asset

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that determines the applicable binding object rate when multiple rates are defined
for an Anchor binding object within a effective period. Available in API version 65.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects AssetRateCardEntry

**Field** **Details**

**Description**
The ID of the binding object associated with the asset rate card entry.

Possible values are:

**•** AED - UAE Dirham

**•** AUD - Australian Dollar

**•** BRL - Brazilian Real

**•** CAD - Canadian Dollar

**•** EUR - Euro

**•** GBP - British Pound

**•** INR - Indian Rupee

**•** JPY - Japanese Yen

**•** SEK - Swedish Krona

**•** USD - U.S. Dollar

The default value is USD. Available in API version 65.0 and later.

```
EndDate

Name

NegotiatedRate

RateCardEntryId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the rate card's time period becomes inactive. The rate card becomes inactive
at 11:59:00 PM on the end date.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number assigned to the asset rate card entry. Read-only.

**Type**
double

**Properties**
Filter, Sort

**Description**
The base negotiated rate used to charge overage consumption.

**Type**
reference


Standard Objects AssetRateCardEntry

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card entry record containing the catalog rates that's associated with the
asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCardEntry

**Refers To**
RateCardEntry

```
RateCardId

RateUnitOfMeasureId

StartDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCard

**Refers To**
RateCard

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the unit of measure record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateUnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
dateTime

**Properties**
Filter, Sort


### Standard Objects AssetRelationship

**Field** **Details**

**Description**
The date when the rate card's time period becomes active. The rate card becomes active at
12:00:00 AM on the start date.

```
UsageResourceId

### AssetRelationship

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the usage resource record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
UsageResource

**Refers To**
UsageResource

Represents a non-hierarchical relationship between assets due to an asset modification; for example, a replacement, upgrade, or other
circumstance. In Revenue Lifecycle Management, this object represents an asset or assets grouped in a bundle or set. This object is
available in API version 41.0 and later.

Asset relationships appear in the Primary Assets and Related Assets related lists on asset records in the UI.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Some fields are available only in Revenue Cloud. Field availability is noted in the field detail column.

Fields

**Field Name** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects AssetRelationship

**Field Name** **Details**

**Description**
The unique identifier of the new asset, which is the asset that is taking the place
of the existing asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

```
AssetRelationshipNumber

AssetRole

CurrencyIsoCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the asset relationship.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the main asset relative to the other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

Possible values are:

**•** `Add-on` —The main asset is an add-on.

**•** `Bundle` —The main asset is the bundle parent.

**•** `Set` —The asset is the main asset in the set.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the asset. The default value
is USD.


Standard Objects AssetRelationship

**Field Name** **Details**

```
FromDate

GroupingKey

ProductRelationshipTypeId

ProductRelatedComponent

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the new asset was installed.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Read-only field used to indicate the bundle that an asset belongs to. For example,
if two assets have the same GroupingKey value, then it means that the assets are
bundled together.

This field is available in API v.60.0 and later. This field is available in orgs with
Revenue Cloud.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the record that describes the relationship between the
main and associated assets.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related component that’s associated with the asset relationship.


Standard Objects AssetRelationship

**Field Name** **Details**

This field is a relationship field.

This field is available in API 60.0 and later in Revenue Cloud.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup

**Refers To**
ProductRelatedComponent

```
RelatedAssetId

RelatedAssetPricing

RelatedAssetQtyScaleMethod

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The existing asset that is being modified.

This field is a relationship field.

**Relationship Name**
RelatedAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the price of the related asset is included in the bundle price.
Valid values are:

**•** `IncludedInBundlePrice`

**•** `NotIncludedInBundlePrice`

This field is available in API version 59.0 and later in Revenue Cloud.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies how the quantity of the related asset changes relative to the quantity
of the parent asset. Valid values are:


Standard Objects AssetRelationship

**Field Name** **Details**

**•** `Constant`

**•** `Proportional`

This field is available in API version 59.0 and later in Revenue Cloud.

```
RelatedAssetRole

RelationshipType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated asset relative to other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Revenue Cloud.

Valid values are:

**•** `Add-on` —The main asset is an add-on.

**•** `Bundle` —The main asset is the bundle parent.

**•** `Set` —The asset is the main asset in the set.

**•** `Simple` —The asset is purchased individually and isn’t associated with
variations.

**•** `Variation Parent` ——The main asset is the variation parent.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of relationship between the existing asset and the new asset. This field
comes with three values—Replacement, Upgrade, and Crossgrade—, but you
can create more values in Setup.

Possible values are:

**•** `Crossgrade` —The new asset is a crossgrade of an existing asset. For
example, changing a subscription to a plan with the same service, but that
runs for a longer amount of time.

**•** `Replacement` —The new asset is replacing an existing asset. For example,
a customer’s faulty widget that was under warranty is being replaced with
a new one.

**•** `Upgrade` —The new asset is an upgrade of an existing asset. For example,
upgrading a customer’s existing subscription plan to a new plan with more
services.

The default value is `Replacement` .


### Standard Objects AssetShare

**Field Name** **Details**

```
ToDate

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the modified asset is uninstalled.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetRelationshipChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AssetRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AssetRelationshipOwnerSharingRule (API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**
Sharing rules are available for the object.

**[AssetRelationshipShare (API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**
Sharing is available for the object.

### AssetShare

Represents a sharing entry on an Asset. This object is available in API version 33.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can’t access this object.


Standard Objects AssetShare

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
AssetAccessLevel

AssetId

IsDeleted

RowCause

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to the Asset. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid for creating or deleting records.

This field must be set to an access level that is higher than the organization’s default access
level for cases.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Asset associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist


### Standard Objects AssetStatePeriod

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Asset with them.

**•** `Owner` —The User is the owner of the Asset.

**•** `Rule` —The User or Group has access via an Asset sharing rule.

**•** `GuestRule` —The User or Group has access via an Asset guest user sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Asset. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view and edit Asset records owned by other users.

If you attempt to create a new record that matches an existing record, request updates any modified fields and returns the existing
record.

### AssetStatePeriod

Represents a time span when an asset has the same quantity, amount, and monthly recurring revenue (MRR). An asset has as many asset
state periods as there are changes to it (asset actions) during its lifecycle. The dashboard and related pages show the current asset state
period. The fields can’t be edited. This object is available in API version 50.0 and later.


Standard Objects AssetStatePeriod

Supported Calls

`createable()`, `deletable()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`,
`query()`, `retrieve()`, `search()`, `updateable()` .

Special Access Rules

To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

Fields

**Field** **Details**

```
Amount

AssetId

AssetStatePeriodNumber

```

**Type**
currency

**Properties**
Createable, Filter, Sort, Updateable

**Description**
An asset’s total amount during an asset state period. Revenue Cloud doesn't set or use this
field's value currently.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort

**Description**
The asset related to an asset state period. Label is **Asset** .

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset state period. Label is **Name** .


Standard Objects AssetStatePeriod

**Field** **Details**

```
BillingFrequency

BindingInstanceTargetId

Discount

DiscountAmount

```

**Type**
picklist

**Properties**
Createable, Filter, Group, Nillable, Restricted picklist, Sort, Updateable

**Description**
The time period that indicates how often the line item is billed.

Possible values are:

**•** `Annual`

**•** `Monthly`

**•** `Quarterly`

**•** `Semi-Annual`

Available in API version 65.0 and later.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of a custom product target for a usage-based quote line item, order Item, or asset
allocation.

This field is a polymorphic relationship field.

**Relationship Name**
BindingInstanceTarget

**Refers To**
Account, Asset, BindingObjectCustomExt, Contract

**Type**
percent

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Editable number from 0 to 100. Available in API version 65.0 and later.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The fixed amount discount to apply to the line item. Available in API version 65.0 and later.


Standard Objects AssetStatePeriod

**Field** **Details**

```
EndDate

LegalEntityId

Mrr

PriceRevisionPolicy

```

**Type**
dateTime

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The end date and time of an asset state period. On an asset that is an evergreen subscription,
the last asset state period has no end date.

**Type**
reference

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The ID of the related legal entity.

This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Createable, Filter, Sort, Updateable

**Description**
An asset’s monthly recurring revenue during an asset state period.

**Type**
reference

**Properties**
Createable, Filter, Group, Sort, Updateable

**Description**
Specifies the price uplift policy associated with this asset state period.

This field is a relationship field.

This field is available in API version 65.0 and later.

**Relationship Name**
Price Revision Policy

**Relationship Type**
Lookup

**Refers To**
PriceRevisionPolicy


Standard Objects AssetStatePeriod

**Field** **Details**

```
Quantity

RampIdentifier

SegmentIdentifier

SegmentName

SegmentType

```

**Type**
double

**Properties**
Createable, Filter, Sort, Updateable

**Description**
The total quantity of an asset during an asset state period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp record used to group order item segments for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Createable, Filter, Group, Nillable, Sort, Updateable

**Description**
The name of the order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Updateable

**Description**
The period for the order item segment for this asset state period. Valid values are:


### Standard Objects AssetStatePeriodAttribute

**Field** **Details**

**•** `Custom`

**•** `Free Trial`

**•** `Yearly`

The default value is `Yearly` .

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

```
StartDate

UnitPrice

UnitPriceUplift

```

**Type**
dateTime

**Properties**
Createable, Filter, Sort, Updateable

**Description**
The start date and time of an asset state period.

**Type**
currency

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
The price per unit for the line item. Available in API version 65.0 and later. Revenue Cloud
won't populate this field in API version 66.0 and later.

**Type**
percent

**Properties**
Createable, Filter, Nillable, Sort, Updateable

**Description**
Indicates the percentage increase of a line item's unit price. Available in API version 65.0 and
later.

### AssetStatePeriodAttribute

Represents a virtual object that holds the key-value pair of the asset attribute in a specified asset state period. This object is a child object
of AssetStatePeriod. This object is available in API version 60.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects AssetStatePeriodAttribute

Special Access Rules

[This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud with the Access Lifecycle-Managed Assets](https://help.salesforce.com/s/articleView?id=ind.rev_cloud_asset_migration_permission.htm&language=en_US)
[user permission. This object is editable only through API and not the UI.](https://help.salesforce.com/s/articleView?id=ind.rev_cloud_asset_migration_permission.htm&language=en_US)

Fields

**Field** **Details**

```
AssetStatePeriodId

AttributeDefinitionId

AttributeName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The asset state period that's associated with the asset attribute.

This field is a relationship field.

**Relationship Name**
AssetStatePeriod

**Relationship Type**
Master-detail

**Refers To**
AssetStatePeriod (the master object)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The attribute definition that's associated with the asset state period attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup

**Refers To**
AttributeDefinition

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the asset attribute.


### Standard Objects AssetTag

**Field** **Details**

```
AttributePicklistValueId

AttributeValue

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value specified in the picklist type field that corresponds to the attribute in the
AttributePicklistValue object.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**
AttributePicklistValue

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the asset state period attribute. For example, a shirt can have the value of `blue`,
which indicates the shirt's color, or it can have the value of `small`, which indicates the
shirt's size.

You can use this field to filter records only if the DataType value in the related
`AttributeDefinitionId` record is `Text` . If the DataType value is `Picklist`, use
the value in the `AttributePicklistValueId` field for filtering. You can’t use this
field to filter records if the DataType value is `Checkbox`, `Currency`, `Date`, `Datetime`,
`Multipicklist`, `Number`, or `Percent` .

This object doesn’t support custom fields, validation rules, or triggers. In SOQL queries, you can filter records by using `Id` and
`AttributeDefinition` . You can’t use `AttributeValue` in the `WHERE` clause.

### AssetTag

Associates a word or short phrase with an Asset.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects AssetTag

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

AssetTag stores the relationship between its parent TagDefinition and the Asset being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects AssetTokenEvent

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### AssetTokenEvent

[The documentation has moved to AssetTokenEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_assettokenevent.htm) _Platform Events Developer Guide_ .

### AssetWarranty

Defines the warranty terms applicable to an asset along with any exclusions and extensions. This object is available in API version 50.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

### `AssetWarrantyNumber`

EndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset this warranty term applies to.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier of the asset warranty record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which this warranty term expires.


Standard Objects AssetWarranty

**Field** **Details**

```
ExchangeType

Exclusions

ExpensesCovered

ExpensesCoveredEndDate

IsTransferable

LaborCovered

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of exchange offered by this warranty term.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of any exclusions.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of expenses covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for expenses ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty term can be transferred to a new owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of labor covered.


Standard Objects AssetWarranty

**Field** **Details**

```
LaborCoveredEndDate

LastReferencedDate

LastViewedDate

PartsCovered

PartsCoveredEndDate

Pricebook2Id

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for labor ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last modified. Its label in the user interface is
`Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last viewed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of parts covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for parts ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects AssignedResource

**Field** **Details**

**Description**
The ID of the price book item associated with this asset warranty term.

```
StartDate

WarrantyTermId

WarrantyType

```

Associated Objects

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date on which cover under this warranty term starts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the warranty term this asset warranty term extends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of the warranty.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetWarrantyChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

### AssignedResource

Represents a service resource who is assigned to a service appointment in Field Service and Lightning Scheduler. Assigned resources
appear in the Assigned Resources related list on service appointments. This object is available in API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects AssignedResource

Fields

**Field Name** **Details**

```
ActualTravelTime

ApptAssistantInfoUrl

AssignedResourceNumber

EstimatedTravelTime

LocationStatus

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that the service resource needs to travel to the assigned
service appointment. You can enter a value with up to two decimal places.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that contains the status of the mobile worker approaching the service
appointment, the Community URL, and the expiry of the URL. Available in version
51.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource assignment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated number of minutes needed for the service resource to travel to
the service appointment they’re assigned to. You can enter a value with up to
two decimal places.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the mobile worker approaching the service appointment. When
the location status changes to one of these values, a status update containing


Standard Objects AssignedResource

**Field Name** **Details**

`ApptAssistantInfoUrl` is sent to the customer. Available in version 51.0
and later.

Possible values are:

**•** `EnRoute`

**•** `LastMile`

```
IsPrimaryResource

ServiceAppointmentId

ServiceCrewId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service resource is a primary resource or not. The default
value is false. Available in API version 47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service appointment that the resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceAppointment

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort, Nillable

**Description**
The service crew that the resource is assigned to.

Note: Since service resources can represent crews or individuals,
appointments are typically assigned to crews in the following way:

**1.** Create a service resource of the Crew type that represent the crew.

**2.** Create an assigned resource on the service appointment and select
the crew resource in the `ServiceResourceId` field.


Standard Objects AssignedResource

**Field Name** **Details**

As an alternative, you can assign appointments to crew members
separately. This lets you track each member’s travel time and see a list of
the crew members in the Assigned Resources related list. To take this
approach, create an assigned resource for each crew member. List the
crew member in the `ServiceResourceId` field and the crew they
belong to in the `ServiceCrewId` field.

```
ServiceResourceId

Transaction

```

Usage

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort

**Description**
The resource who is assigned to the service appointment.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last transaction ID of the scheduling and optimization request that updated
this object. The transaction ID is automatically generated and populated by the
Enhanced Scheduling and Optimization engine. Available in API version 63.0 and
later.

You can assign multiple service resources to a service appointment. Service resources who are assigned to service appointments cannot
be deactivated until they are removed from the appointments.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AssignedResourceChangeEvent (API version 48.0)**
Change events are available for the object.


### Standard Objects AssignmentRule

**AssignedResourceHistory on page 63(API version 61.0)**
History is available for tracked fields of the object.

**AssignedResourceFeed**

Feed tracking is available for the object.

### AssignmentRule

Represents an assignment rule associated with a Case or Lead.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

**•** This object is read only. Assignment rules are created, configured, and deleted in the user interface.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Active

Name

SobjectType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this assignment rule is active ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this assignment rule.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of assignment rule—Case or Lead.


### Standard Objects AssociatedLocation

Usage

Before creating or updating a new Case or Lead, a client application can query (by name) the AssignmentRule to obtain the ID of the
assignment rule to use, and then assign that ID to the `assignmentRuleId` field of the AssignmentRuleHeader. The
AssignmentRuleHeader can be set using either SOAP API or REST API.

Assignment rules can also be specified when creating or upserting Case or Lead objects via the Bulk API or the Bulk 2.0 API.

SEE ALSO:

Overview of Salesforce Objects and Fields

### AssociatedLocation

Represents a link between an account and a location in Field Service. You can associate multiple accounts with one location. For example,
a shopping center location may have multiple customer accounts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
ActiveFrom

ActiveTo

### `AssociatedLocationNumber`

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location is active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location stops being active.

**Type**
string


Standard Objects AssociatedLocation

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number identifying the associated location.

```
LastReferencedDate

LastViewedDate

LocationId

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date the associated location was last modified.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the associated location was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location associated with the address.

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
Create, Filter, Group, Sort

**Description**
The account associated with the location.

This is a relationship field.


### Standard Objects AsyncApexJob

**Field Name** **Details**

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Bill To

**•** Ship To

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AssociatedLocationChangeEvent (API version 62.0)**
Change events are available for the object.

**AssociatedLocationHistory**

History is available for tracked fields of the object.

### AsyncApexJob

Represents an individual Apex sharing recalculation job, a batch Apex job, a method with the `future` annotation, or a job that
implements `Queueable` or `Schedulable` . Use this object to query Apex batch jobs in your organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

If Apex isn’t running in system mode, users must have the View Setup and Configuration permission to access this object and to enqueue
asynchronous Apex jobs.


Standard Objects AsyncApexJob

Fields

**Field Name** **Details**

```
ApexClassId

CompletedDate

CronTriggerId

ExtendedStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex class executing the job. Label is `Class ID` .

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job was completed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronTrigger for the AsyncApexJob. This field only applies to ScheduledApex
job type. This field is available in API version 53.0 and later. For scheduled jobs created before
version 53.0, this field is populated on subsequent execution.

This is a relationship field.

**Relationship Name**
CronTrigger

**Relationship Type**
Lookup

**Refers To**
CronTrigger

**Type**
string


Standard Objects AsyncApexJob

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
If one or more errors occurred during the batch processing, this field contains a short
description of the first error. A more detailed description of that error, along with any
subsequent errors, is emailed to the last user who modified the batch class. This field is
available in API version 19.0 and later.

```
JobItemsProcessed

JobType

LastProcessed

LastProcessedOffset

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of job items processed. Label is `Batches Processed` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job being processed. Valid values are:

**•** `ApexToken`

**•** `[BatchApex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)`

**•** `BatchApexWorker`

**•** `[Future](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_invoking_future_methods.htm)`

**•** `[Queueable](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)`

**•** `[ScheduledApex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_scheduler.htm)`

**•** `[SharingRecalculation](https://help.salesforce.com/s/articleView?id=platform.security_apex_sharing_recalc.htm&type=5&language=en_US)`

**•** `TestRequest`

**•** `TestWorker`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Last ID that was processed and committed.

**Type**
int


Standard Objects AsyncApexJob

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Offset of the last ID that was processed and committed.

```
MethodName

NumberOfErrors

ParentJobId

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Apex method being executed. Label is `Apex Method` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of batches with a failure. A batch is considered transactional, so any unhandled
exceptions constitute an entire failure of the batch. Label is `Failures` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For batch Apex jobs that run using chunking implementation, multiple child jobs of type
`BatchApexWorker` are created. Each of these child job records contains the job Id of
the parent Apex job that started their execution. For batch Apex jobs that run using a
non-chunking implementation, child jobs aren’t created.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the job. Valid values are:

**•** `Aborted`

**•** `Completed`

**•** `Failed`

**•** `Holding` [1]

**•** `Preparing`


### Standard Objects AsyncOperationLog

**Field Name** **Details**

**•** `Processing`

**•** `Queued`

1 This status applies to batch jobs in the Apex flex queue.

```
TotalJobItems

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of batches processed. Each batch contains a set of records. Label is `Total`
`Batches` .

Use this object to query Apex batch jobs in your organization.

### AsyncOperationLog

Represents an async operations log containing progress and status information about external synchronizations to the Omnichannel
Inventory service. This object is available in API version 51.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Special Access Rules

This object is only available in Omnichannel Inventory orgs.

Fields

**Field** **Details**

```
AsyncOperationNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number assigned to the operation.


Standard Objects AsyncOperationLog

**Field** **Details**

```
Description

Error

ExternalReference

FinishedAt

LastStatusUpdateAt

RelatedRecordId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique external reference ID per type.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the status of the operation was last updated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The related record ID for the async request. This field is available in API version 60.0 and later.


Standard Objects AsyncOperationLog

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Asset, OrderItemSummary

```
Request

Response

StartedAt

Status

```

**Type**
textarea

**Properties**
Nillable

**Description**
The request sent to the external service.

**Type**
textarea

**Properties**
Nillable

**Description**
The full response from the external service.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation started.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the operation.

Possible values are:

**•** `Completed`

**•** `Error`

**•** `In Progress`

**•** `New`


### Standard Objects AsyncOperationTracker

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of operation that is being tracked.

Possible values are:

**•** `CancelAsset` —This value is available in API version 60.0 and later.

**•** `CreateAsset` —This value is available in API version 60.0 and later.

**•** `CancelOrderItemSummaries`

**•** `ImportInventory`

**•** `LocationManagement`

**•** `OrderSummaryAdjustmentAggregate`

### AsyncOperationTracker

Represents the status of an asynchronous request initiated from the Quote, Order, and CreditMemo entities. This object is available in
API version 61.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AsyncOperationNumber

CorrelationIdentifier

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A string that identifies the operation being tracked in AsyncOperationTracker.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AsyncOperationTracker

**Field** **Details**

**Description**
A string that identifies an operation across services.

```
ExpiresAt

FailedJobItems

FinishedAt

JobType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items within the job that have failed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job.

Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion` —Automated Negative
Invoice Line Conversion

**•** `AutomaticRefunds` —Automatic Refunds

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`


Standard Objects AsyncOperationTracker

**Field** **Details**

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PearAmendQtyAssets` —Initiate Amend Quantity

**•** `PearCancelAssets` —Initiate Cancellation

**•** `PearRenewAssets` —Initiate Renewal

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote` —Place Quote

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment` —Price Rule Deployment

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom` —Create Material Lines

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.


Standard Objects AsyncOperationTracker

**Field** **Details**

```
OwnerId

ParentOperationId

ReferenceEntityId

StartedAt

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is a relationship field.

**Relationship Name**
ParentOperation

**Refers To**
AsyncOperationTracker

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Refers To**
CreditMemo, InvoiceBatchRun, Order, Product2, Quote

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AsyncOperationTracker

**Field** **Details**

**Description**
The timestamp indicating when Salesforce started the asynchronous process.

```
Status

StepName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the asynchronous request.

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures` —Completed With Failures

**•** `Failure`

**•** `InProgress` —In Progress

**•** `Submitted`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion` —Automated Negative
Invoice Line Conversion

**•** `AutomaticRefunds` —Automatic Refunds

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `DeltaCatalogSyndicationAsyncJob`

**•** `FullCatalogSyndicationAsyncJob`

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PSTCommonSyncStep`

**•** `PSTConfigAndPersist`

**•** `PSTOrderTaxAsync`

**•** `PSTPriceAndPersist`


Standard Objects AsyncOperationTracker

**Field** **Details**

**•** `PSTQuoteTaxAsync`

**•** `PearAmendQtyAssets` —Initiate Amend Quantity

**•** `PearCancelAssets` —Initiate Cancellation

**•** `PearRenewAssets` —Initiate Renewal

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote` —Place Quote

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment` —Price Rule Deployment

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom` —Create Material Lines

```
SubmittedAt

SuccessfulJobItems

TotalJobItems

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successful items in this job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of items in this job.


### Standard Objects AsyncOpSyndicationFeedFile AsyncOpSyndicationFeedFile

Represents the sync status of file-related information shared with external channels such as Facebook and Instagram. This object is
available in API version 64.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

### `AsyncOpSyndicationFeedFileNumber`

```
AsyncOperationTrackerId

FeedContentBody

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID assigned to each syndication feed file record, and used for tracking and reference purposes.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID assigned to the Async Operation Tracker record, which monitors and manages the lifecycle
of the syndication process.

This field is a relationship field.

**Relationship Name**
AsyncOperationTracker

**Refers To**
AsyncOperationTracker

**Type**
base64

**Properties**
Nillable

**Description**
The content of the feed file that is syndicated to the external platform.


Standard Objects AsyncOpSyndicationFeedFile

**Field** **Details**

```
FeedContentContentType

FeedContentLength

FeedContentName

FeedScope

LastReferencedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the format of the feed file to ensure proper processing. For example, CSV, JSON, or
XML files.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the feed file in bytes, which is used for validation and processing requirements.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the feed file, which includes identifiers like timestamp or sequence number.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Defines the scope or category of the feed. For example, if the feed applies to main,
country-specific, or language-specific catalog segments.

Possible values are:

**•** `CountryFeed`

**•** `LanguageFeed`

**•** `MainFeed`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
For internal use only.


### Standard Objects AttachedContentDocument

**Field** **Details**

```
LastViewedDate

PlatformConnections

SyncMode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
For internal use only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The external channel or destination for syndication.

Possible values are:

**•** `Meta`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of sync being performed.

Possible values are:

**•** `FullSync`

### AttachedContentDocument

This read-only object contains all `ContentDocument` objects associated with an object.

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


Standard Objects AttachedContentDocument

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the attached `ContentDocument` .

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

The size of the document in bytes for notes smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for notes smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes up to 10 GB.

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


Standard Objects AttachedContentDocument

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the external data source in which the document is stored. This field is
set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

```
ExternalDataSourceType

FileExtension

FileType

LinkedEntityId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in APIAPI version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentDocument` .

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentDocument` is attached to.

This is a relationship field.

**Relationship Name**
LinkedEntity


Standard Objects AttachedContentDocument

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentWorkspace, Contract, ConversationEntry,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria,
Event, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingSession,
MktCalculatedInsight, OperatingHours, Opportunity, Order, OrderItem,
Organization, OtherComponentTask, PartyConsent, PersonEducation,
PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit, PlanBenefitItem,
Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report,
ReportAnomalyEventStore, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement,
SocialPost, Solution, Task, ThreatDetectionFeedback, User, Visit, VisitedParty,
Visitor, VoiceCall, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember


### Standard Objects AttachedContentNote

**Field Name** **Details**

```
 SharingOption

Title

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Controls whether or not sharing is frozen for a file. Only administrators and file
owners with Collaborator access to the file can modify this field. Default is
`Allowed`, which means that new shares are allowed. When set to
`Restricted`, new shares are prevented without affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Title of the attached `ContentDocument` .

Use this object to list all `ContentDocument` objects attached to an object via a feed post.

To retrieve `ContentDocument` objects, issue a describe call on an object, which returns a query result for each activity since the
record was created. You can’t directly query this object.

### AttachedContentNote

This read-only object contains all ContentNote objects associated with an object.This object is available in API version 35.0 and later.

Supported Calls

```
describeSObjects()

```

Special Access Rules

**•** Notes must be enabled.

**•** Chatter must be enabled.


Standard Objects AttachedContentNote

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentSize

ContentSizeLong

FileExtension

FileType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the attached `ContentNote`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the note in bytes for notes smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for notes smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentNote` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of file for the note. All notes have a file type of `SNOTE` .


### Standard Objects Attachment

**Field Name** **Details**

```
LinkedEntityId

TextPreview

Title

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentNote` is attached to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A preview of the note, up to 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

Title of the note.

Use this object to list all `ContentNote` objects attached to an object.

To retrieve `ContentNote` objects, issue a describe call on an object, which returns a describe result for each note created or attached.
You can’t directly query this object.

### Attachment

Represents a file that a User has uploaded and attached to a parent object.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`


Standard Objects Attachment

Fields

**Field** **Details**

```
Body

BodyLength

ConnectionReceivedId

ConnectionSentId

ContentType

```

**Type**
base64

**Properties**
Create, Update

**Description**
Required. Encoded file data.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Size of the file (in bytes).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The content type of the attachment.

If the `Don't allow HTML uploads as attachments or document`
`records` security setting is enabled for your organization, you cannot upload files with


Standard Objects Attachment

**Field** **Details**

the following file extensions: `.htm`, `.html`, `.htt`, `.htx`, `.mhtm`, `.mhtml`, `.shtm`,
`.shtml`, `.acgi`, `.svg` .

When you insert a document or attachment through the API, make sure that this field is set
to the appropriate MIME type.

```
Description

IsEncrypted

IsPartnerShared

IsPrivate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the attachment. Maximum size is 500 characters. This field is available in API
version 18.0 and later.

This information is about Shield Platform Encryption and not Classic Encryption.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the attachment is encrypted using Shield Platform Encryption ( `true` ) or
not ( `false` ). This field is available in API version 34.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is shared with a connection using Salesforce to Salesforce.
Label is `Is Shared With Partner` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is viewable only by the owner and administrators ( `true` ) or
viewable by all otherwise-allowed users ( `false` ). During a create or update call, it is possible
to mark an Attachment record as private even if you are not the owner. This can result in a
situation in which you can no longer access the record that you just inserted or updated.
Label is **Private** .

Attachments on tasks or events can't be marked private.


Standard Objects Attachment

**Field** **Details**

```
Name

OwnerId

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the attached file. Maximum size is 255 characters. Label is **File Name** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the attachment. This field isn’t required for API version 9.0 or later.

The owner of an attachment on a task or event must be the same as the owner of the task
or event.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the parent object of the attachment. The following objects are supported as
parents of attachments:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contact

**•** Contract

**•** Custom objects

**•** EmailMessage

**•** EmailTemplate

**•** Event


Standard Objects Attachment

**Field** **Details**

**•** Lead

**•** Opportunity

**•** Product2

**•** Solution

**•** Task

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, Campaign,
CareBarrier, CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EmailMessage, EmailTemplate,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
Lead, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PersonEducation,
PersonLifeEvent, Product2, ProductRequest, ProductRequestLineItem, PurchaserPlan,
ReceivedDocument, ServiceAppointment, ServiceResource, Shift, SocialPost, Solution, Task,
Visit, VisitedParty, Visitor, VolunteerProject, WorkOrder, WorkOrderLineItem

Note: If you are importing Attachment data and want to set the value for an audit field, such as `CreatedDate`, contact
Salesforce. For example, for compliance reasons, you may prefer to set the `CreatedDate` to the date the record was originally
created in your system, rather than the date it was imported into Salesforce. Audit fields are automatically updated during API
operations unless you request to set these fields yourself.

Usage

The API sends and receives the binary file attachment data encoded as a base64Binary data type. Before creating a record, client
applications must encode the binary attachment data as base64. Upon receiving a response, client applications must decode the base64
data to binary (this conversion is usually handled for you by the SOAP client).


### Standard Objects AttachmentEventLog

The create call restricts these files to a maximum size of 25 MB. For a file attached to a Solution, the limit is 1.5 MB. The maximum email
attachment size is 3 MB.

The API supports attachments on email in create, delete, or update calls. The query call does not return attachments parented by email,
unless the user performing the query has the “Modify All Data” permission.

Note:

**•** Attachment records are not searched during text searches.

**•** When issued by an administrator, the query results include Attachment records from the Recycle Bin.

**•** When issued by a non-administrator, the `queryAll()` call results do not include Attachment records from the Recycle Bin.

Access to fields depends on the method being used:

**•** All of the fields are accessible using the `describeSObjects()` and `query()` calls. With the `create()` call, you can insert
the `Name`, `ParentId`, `Body`, `IsPrivate`, and `OwnerId` fields.

**•** To modify existing records, the `update()` call gives you access to change the `Name`, `Body`, `IsPrivate`, and `OwnerId`
fields.

**•** You can access all of the fields using a `query()` call. However, you can't receive the `Body` field for multiple records in a single
`query()` call. If your query returns the `Body` field, your client application must ensure that only one row with one Attachment
is returned; otherwise, an error occurs. A more effective approach is to return IDs (but not Attachment records in the `Body` field)
from a `query()` call and then pass them into `retrieve()` calls that return the `Body` field.

**•** For information about accessing the attachments of archived activities, see Archived Activities.

SEE ALSO:

Note

### AttachmentEventLog

Attachment event logs contain information about attachments. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AttachmentIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AttachmentEventLog

**Field** **Details**

**Description**
The ID of the attachment.

```
ContentType

IsPrivateOn

OperationType

ParentIdentifier

RequestIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the attachment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the attachment is flagged as private or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation type of the attachment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent object of the attachment. For example, `a07EE00001LgsUH`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
dateTime


### Standard Objects AttribModel

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
UserIdentifier

### AttribModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

Represents an attribution model used with Personalization, Attribution, and Campaign Influence, including model weights and touch
type. This object is available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

### `AttribModelStatus`

```
AttributionModelType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates a model’s current status. The default value is `Draft`, and accepted values are

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
picklist


Standard Objects AttribModel

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of attribution model, which determines which touchpoints to evaluate.
The default value is `LastTouch`, and accepted values are

**•** `First touch`

**•** `LastTouch`

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
Unique identifier that refers to the data space where a model's resources originate. This is a
required field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the attribution model. Optional.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AttribModel

**Field** **Details**

**Description**
Auto-generated or user-generated API name for the attribution model. This is a required
field.

```
Error Code

GlobalAttributionWindowDays

IdentityResolutionMode

IsZeroDayLoadRequired

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the issue that’s causing an error. The default value is `None`, and accepted values
are

**•** `ConfigurationMissingError` indicates that a required configuration setting
is missing.

**•** `DpcJobError` indicates a problem during processing.

**•** `InternalError` indicates an internal error during processing.

**•** `ModelValidationError` indicates that the model is invalid.

**•** None

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Defines a timeframe for tracking attribution-related engagement. This is a required field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Defines which identity resolution method to use when tracking engagement activities.
Default value is `Individual`, and acceptable values are

**•** `Individual`

**•** `Unified`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AttribModel

**Field** **Details**

**Description**
Defines whether to sync data before the attribution window begins. The default value is
`false` .

```
LastReferencedDate

LastRefresh

LastSuccessfulRefresh

LastViewedDate

LatestRefreshedStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the model was referenced by another resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates the last time engagement data was refreshed and evaluated
by the model.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates the last time the model was successfully refreshed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the model.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the status of last refresh process. The default value is `None`, and
accepted values are

**•** `Canceled`

**•** `Complete`


Standard Objects AttribModel

**Field** **Details**

**•** `Failure`

**•** `None`

**•** `Processing`

```
ModelContext

ModelRevision

Name

Partner

ProfileDataGraphId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the app or feature in which the attribution model is used. The default value is
`Personalization`, and accepted values are

**•** `Attribution` : indicates the use with Attribution in Salesforce Personalization.

**•** `CampaignInfluence` : indicates the use with Campaign Influence in Unified
Marketing Analytics.

**•** `Personalization` : indicates the use with Personalization in Salesforce
Personalization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A version number that indicates the latest save of the model.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the attribution model. This is a required field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates who's using the model. This field is required if the value of `ModelContext` is
`Attribution` .

**Type**
reference


Standard Objects AttribModel

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the profile data graph that’s used with the model.

**Relationship Name**
ProfileDataGraph

**Refers To**
DataGraph

```
ScheduledFrequencyMins

SyncStatus

Tags

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The scheduled frequency (in minutes) at which the attribution model is processed.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the current status of the attribution model while an action is being performed. The
default value is `Processing`, and acceptable values are:

**•** `Active`

**•** `CreateError`

**•** `DeleteError`

**•** `Deleting`

**•** `EditError`

**•** `Processing`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
User-generated strings that can be used to organize attribution models.


### Standard Objects AttribModelStage

Usage

Use this object to get information about attribution models that are in use with personalization and influence features. For example,
you can:

**•** Retrieve status and error details.

**•** Identify model settings such as type (first-touch, last-touch).

**•** Find out when the model was last used, refreshed, or synced.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AttribModelChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### AttribModelStage

Represents a funnel stage that’s used in a predefined or custom attribution configuration. Available in API version 62.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
AttribModelId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the attribution configuration that uses this stage. This is a
required field.


Standard Objects AttribModelStage

**Field** **Details**

**Relationship Name**
AttribModel

**Relationship Type**
Master-detail

**Refers To**
AttribModel (the master object)

```
CurrencyIsoCode

EngagementSignalEnum

IsContentMatchRequired

Name

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the engagement signal that’s selected for an attribution stage.
This value represents a step in a customer journey.

The accepted values are the engagement signals that are configured in the selected data
space.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether to link item attribution from one funnel stage to the next. The default
value is `false`, meaning not required. If you set this value to `true`, only engagement
with the same item from the previous stage is linkable.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the attribution model stage. This is a required field.


Standard Objects AttribModelStage

**Field** **Details**

```
Sequence

StageUnionGroupName

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**

Indicates the position of a stage in its journey sequence, reflecting funnel engagement from
start to finish. The funnel requires a minimum of two stages, with a maximum of four stages.
Accepted values are `1`, `2`, `3`, or `4` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of a certain group of stages. It can be used to reference individual, consecutive stages
as a combined group with a common name.

Use this object to create attribution funnel stages. The funnel mirrors key touchpoints of an individual’s personalization journey, which
you define by selecting an engagement signal and any relevant metrics. The order that you create stages in describes funnel engagement
from start to finish.

For example, view a product, click the product, add it to cart, and submit the order. The funnel requires a minimum of two stages, with
a maximum of four stages in a journey.

Associated Objects

This object has the these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AttribModelStageChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelStageFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelStageHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelStageOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelStageShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects AttribModelStageMetric AttribModelStageMetric

Represents the engagement signal metrics that you select when you configure a funnel stage for an attribution configuration. Available
in API version 63.0 and later.

Supported Calls

describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

Fields

**Field** **Details**

```
Alias

AttribModelStageId

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

Indicates the name of the output data metric. This name appears as the column name for
the metric on the attribution output table.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

Unique identifier that refers to the attribution configuration stage that uses this metric.

**Relationship Name**
### AttribModelStage

**Relationship Type**
Primary-detail

**Refers To**
AttribModelStage (the primary object)

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. The default value is `USD` . This is
an optional field.


Standard Objects AttribModelStageMetric

**Field** **Details**

```
EngagementSignalMetricId

Name

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the engagement signal that defines this stage.

**Relationship Name**
EngagementSignalMetric

**Refers To**
EngagementSignalMetric

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The text label that identifies the attribution model stage metric.

An engagement signal metric is an aggregation of an engagement signal data field. These metrics are reported in the attribution model
dashboard. For example, sum of clicks on a link, number of products added to a cart, email sends, or distinct article downloads.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AttribModelStageMetricChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AttribModelStageMetricFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AttribModelStageMetricHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AttribModelStageMetricOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AttribModelStageMetricShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects AttributeDefinition AttributeDefinition

Represents a product, asset, or object attribute, for example, a hardward specification or software detail. This object is available in API
version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
DataType

DefaultValue

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The data type of the attribute definition.

Possible values are:

**•** `Checkbox`

**•** `Date`

**•** `Datetime`

**•** `Number`

**•** `Picklist`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value for this attribute.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects AttributeDefinition

**Field** **Details**

**Description**
Description of this attribute.

```
DeveloperName

IsActive

IsRequired

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the attribute definition record.

This name must begin with a letter and use only alphanumeric characters and underscores.
It can't include spaces, end with an underscore, or have two consecutive underscores.

The developer name is used for internal purpose and must be unique for all records (including
deleted records). If the system doesn't find the name unique, it automatically overrides the
user input and creates a unique name. For external use, the developer name need not be
fixed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the attribute definition is active. Active attributes definitions can be selected
for assets.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the attribute definition is required for an asset.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
[The label for the attribute. Displays a friendly name for the attribute, for example, threshold](https://help.salesforce.com/s/articleView?id=service.fs_asset_attrib_manage_monit_filter.htm&type=5&language=en_US)
[monitor lightning component and recordset filter criteria rule.](https://help.salesforce.com/s/articleView?id=service.fs_asset_attrib_manage_monit_filter.htm&type=5&language=en_US)


Standard Objects AttributeDefinition

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

PicklistId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute definition was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute definition was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the attribute definition.

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
The ID of the attribute picklist with the valid values for this attribute.


Standard Objects AttributeDefinition

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Picklist

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

```
SourceSystemIdentifier

UnitOfMeasureId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the attribute definition in an external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the measurement unit for this attribute.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

Add asset descriptors to the Asset object instead of creating multiple custom attributes on an asset. This helps scale to a high volume
of various assets in the system. When you create the AttributeDefinition, you can provide a unique API name. If the API name is not
unique, the system appends a number to the end of the API name. The value of this number depends on how many times the same
name has been used.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects AttributePicklist

**AttributeDefinitionHistory on page 63**
History is available for tracked fields of the object.

**AttributeDefinitionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AttributeDefinitionShare on page 67**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

### AttributePicklist AttributePicklistValue

RecordsetFltrCritMonitor

### AttributePicklist

Represents a custom picklist for an asset attribute. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this picklist.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Datetime`

**•** `Number`


Standard Objects AttributePicklist

**Field** **Details**

**•** `Percent`

**•** `Text`

The default value is `Boolean` .

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
Create, Nillable, Update

**Description**
A description of the picklist. Maximum size is 32000 alphanumeric characters. Can include
the following special characters: @! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the picklist. Names must be unique.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the attribute picklist record.

This field is a polymorphic relationship field.


Standard Objects AttributePicklist

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Status

UnitOfMeasureId

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft` .

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

The AttributePicklist object is the parent object and the AttributePicklistValue object contains the picklist values. Let’s say you need an
asset attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for
the T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate
them with the parent record.


### Standard Objects AttributePicklistValue

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributePicklistHistory on page 63**
History is available for tracked fields of the object.

**AttributePicklistOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AttributePicklistShare on page 67**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

### AttributePicklistValue

RecordsetFltrCritMonitor

### AttributePicklistValue

Represents the values of an asset attribute picklist. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
Abbreviation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short name of the picklist value that's displayed at run time. Use up to 255 alphanumeric
characters. Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $
”.


Standard Objects AttributePicklistValue

**Field** **Details**

```
Code

DisplayValue

IsDefault

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A picklist value code unique to the picklist. Maximum size is 80 alphanumeric characters.
Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The displayed picklist value if it’s different from the Name field. For example, the Name ‘5’
could have a DisplayValue ‘Five’.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the picklist value is the default for the associated picklist. Only one value
can be the default for a picklist.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last viewed.

**Type**
string


Standard Objects AttributePicklistValue

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute picklist value.

```
PicklistId

Sequence

Status

Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the picklist that the value is associated with.

This field is a relationship field.

**Relationship Name**
Picklist

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The order in which the picklist value appears in the picklist.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist value.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft` .

**Type**
string


### Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text value for a picklist item if the picklist data type is text. This value must be unique
within a picklist. Maximum size is 255 alphanumeric characters. Can include the following
special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

Usage

The AttributePicklistValue object is the child object and the AttributePicklist object contains the picklist. Let’s say you need an asset
attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for the
T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate them
with the parent record..

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributePicklistValueHistory on page 63**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

RecordsetFltrCritMonitor

### AsyncReportRunEventLog

Async Report Run Event Log is used for reporting scheduled requests. This category includes dashboard refreshes, asynchronous reports,
schedule reports, and analytics snapshots. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects AsyncReportRunEventLog

Fields

**Field** **Details**

```
AverageRowSize

BucketCount

ClientIp

ColumnCount

CpuTime

DashboardIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average row size (in bytes) of all rows in the Asynchronous Report Run event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of buckets used in the report.

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
Filter, Group, Nillable, Sort

**Description**
The number of columns in the report.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dashboard that was run.

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
How much activity is occurring in the database.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time (in milliseconds) to complete the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total time spent in OracleJdbc calls, counting the Jdbc driver, Network, and Oracle time for
execs, fetches, and get-connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Possible values are:

**•** D—Dashboard

**•** S—Show Details

**•** H—Hide Details

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Description**
The number of exception filters used in the report.

```
IsPreview

LoginKey

ObjectName

Origin

RenderingType

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is reserved for future use.

The default value is `false` .

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
The name of the object affected by the trigger.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Where the report is being executed, such as from a UI (Classic, Lightning, Mobile), through
an API (synchronous, asynchronous, Apex), or through a dashboard.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the format of the report output in Salesforce Classic. If the report was exported in
Lightning Experience, this field is blank.


Standard Objects AsyncReportRunEventLog

**Field** **Details**

```
ReportIdentifier

RequestIdentifier

RequestStatus

RowCount

RunTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The report’s ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the Asynchronous Report Run event.

**Type**
double


Standard Objects AsyncReportRunEventLog

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

```
SessionKey

SortOrder

Timestamp

Uri

UserIdentifier

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Audience

**Field** **Details**

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

```
UserType

### Audience

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license. Possible values are:

**•** CsnOnly—Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** CspLitePortal—CSP Lite Portal license. Users whose access is limited because they’re
organization customers and access the application through a customer portal or an
Experience Cloud site.

**•** CustomerSuccess—Customer Success license. Users whose access is limited because
they’re organization customers and access the application through a customer portal

**•** Guest—Users whose access is limited so that your customers can view and interact with
your site without logging in.

**•** PowerCustomerSuccess—Power Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal. Users with this license type can view and edit data they directly own or data
owned by or shared with users below them in the customer portal role hierarchy.

**•** PowerPartner—Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** SelfService—Users whose access is limited because they’re organization customers and
access the application through a self-service portal.

**•** Standard—Standard user license. This user type also includes Salesforce Platform and
Salesforce Platform One user licenses, and admins for this org.

Represents an audience that is defined by criteria and can be assigned and used for targeting in an Experience Cloud site. This object is
available in API version 44.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects Audience

Fields

**Field** **Details**

```
AudienceName

ContainerId

Description

DeveloperName

FormulaFilterType

```

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Name of the audience.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the site or org that contains the audience. ContainerId is nillable in API versions 47.0
and earlier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the audience.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The unique name of the audience in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated, but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist


Standard Objects Audience

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Formula filter for the criteria used to define the audience. Valid values are:

**•** `AllCriteriaMatch` —Matching all the conditions (AND).

**•** `AnyCriterionMatches` —Matching at least one condition (OR).

**•** `CustomLogicMatches` —Matching condition logic (AND and OR) and numbered
criteria groups. This value is available in API version 45.0 and later.

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the audience. Valid values are:

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

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

**Type**
string

**Properties**
Filter, Group, Sort, Update


### Standard Objects AuraDefinition

**Field** **Details**

**Description**
Master label for the audience. This internal name doesn’t get translated.

### AuraDefinition

Represents an Aura component definition, such as component markup, a client-side controller, or an event. This object is available in
API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

### `AuraDefinitionBundleId`

```
DefType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the bundle containing the definition. A bundle contains a Lightning
definition and all its related resources.

This is a relationship field.

**Relationship Name**
### AuraDefinitionBundle

**Relationship Type**
Lookup

**Refers To**
### AuraDefinitionBundle

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AuraDefinition

**Field Name** **Details**

**Description**

The definition type. Valid values are:

**•** `APPLICATION`                       - Lightning Aura Components app

**•** `CONTROLLER`                       - client-side controller

**•** `COMPONENT`                       - component markup

**•** `EVENT`                       - event definition

**•** `HELPER`                       - client-side helper

**•** `INTERFACE`                       - interface definition

**•** `RENDERER`                       - client-side renderer

**•** `STYLE`                       - style (CSS) resource

**•** `PROVIDER`                       - reserved for future use

**•** `MODEL`                       - deprecated, do not use

**•** `TESTSUITE`                       - reserved for future use

**•** `DOCUMENTATION`                       - documentation markup

**•** `TOKENS`                       - tokens collection

**•** `DESIGN`                       - design definition

**•** `SVG`                       - SVG graphic resource

**•** `MODULE`                       - reserved for future use

```
Format

Source

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The format of the definition. Valid values are:

**•** `XML` for component markup

**•** `JS` for JavaScript code

**•** `CSS` for styles

**•** `TEMPLATE_CSS` reserved for future use

**•** `SVG` for an SVG graphic

**Type**
textarea

**Properties**
Create, Update

**Description**
The contents of the definition. This is all the markup or code for the definition.


### Standard Objects AuraDefinitionBundle

Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/)

### AuraDefinitionBundle

Represents a Lightning Aura component definition bundle, such as a component or application bundle. A bundle contains a Lightning
Aura component definition and all its related resources. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
ApiVersion

Description

DeveloperName

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this bundle. Every bundle has an API version specified at
creation.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text description of the bundle. Maximum size of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.


Standard Objects AuraDefinitionBundle

**Field Name** **Details**

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

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
The language of the `MasterLabel` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for the Lightning bundle. This internal label doesn’t get translated.

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


### Standard Objects AuraDefinitionBundleInfo

Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/)

### AuraDefinitionBundleInfo

For internal use only.

### AuraDefinitionInfo

For internal use only.

### AuraRequestEventLog

Aura Request Event Log contains details of requests to Apex methods from Aura and Lightning web components. This object is available
in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ActionMessage

ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action (Apex method) names and times for all the actions in the request in the format.
For example: `action1Name=action1Time;action2Name=action2Time...`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AuraRequestEventLog

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: `96.43.144.26` .

```
CpuTime

DatabaseTotalTime

LoginKey

RequestIdentifier

RequestMethod

```

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
network to the database, and `DatabaseCpuTime` . Compare this field to `CpuTime`
to determine whether performance issues are occurring in the database layer or in your own
code.

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
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier.` For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string


Standard Objects AuraRequestEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request, such as `GET` or `POST` .

```
RequestStatus

RunTime

SessionKey

Timestamp

```

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
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AuraRequestEventLog

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

```
Uri

UserAgent

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

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
The ID of the user who’s using Salesforce services through the UI or the API. For example:
`00530000009M943` .

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


### Standard Objects AuthConfig

**Field** **Details**

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

### AuthConfig

Represents authentication options for My Domain and Experience Cloud site login pages. This object is available in API version 32.0 and
later.

The fields for this object control the options that display on the login page of an org. By default, you have a My Domain and corresponding
login page. If you use Digital Experiences, you can also set up a login page for each of your Experience Cloud sites.

**•** Logging in with a username and password

**•** Using SAML for single sign-on

**•** Authentication provider logins from a third-party service, such as Facebook or Twitter

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have “View Setup and Configuration” permission to view the settings.

Fields

**Field Name** **Details**

```
AuthOptionsAuthProvider

```

**Type**
boolean

**Properties**
Filter


Standard Objects AuthConfig

**Field Name** **Details**

**Description**

If `true`, at least one Auth. Provider is selected to show up on the login page,
and this object has child AuthConfigProvider objects for each provider.

```
AuthOptionsCertificate

AuthOptionsSaml

AuthOptionsUsernamePassword

DeveloperName

```

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, certificate-based login displays on the My Domain login page.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, at least one SAML configuration is selected to show up on the login
page. If the organization has only one SAML configuration, this value indicates
whether that configuration is selected to show up on the login page. If the
organization has multiple SAML configurations, see the child AuthConfigProvider
objects for each configuration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, the login option for a username and password appears on the login
page.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the domain created using My Domain or, for an Experience Cloud
site, a concatenated string of _`site name`_ _ _`site prefix`_ .

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


Standard Objects AuthConfig

**Field Name** **Details**

```
IsActive

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Whether this configuration is in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text that’s used to identify the Visualforce page in Setup.

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


### Standard Objects AuthConfigProviders

**Field Name** **Details**

```
Type

Url

### AuthConfigProviders

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The organization type for this object.

**•** `Org` (includes custom domains)

**•** `Community`

**•** `Site`

**•** Portal

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The login URL of the organization for this AuthConfig object. Each URL has only
one associated AuthConfig object.

Represents an authentication provider that’s configured in an organization. AuthConfigProviders is a child of the AuthConfig object. This
object is available in API version 32.0 and later.

This object links the authentication configuration for an organization to the Auth Provider through the `AuthOptionsAuthProvider`
[field of the AuthConfig object. The login page of a My Domain or Experience Cloud site can allow multiple SAML configurations and](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_authconfig.htm)
multiple authentication providers. These configurations can be set to show up as buttons on the login page. Each configuration has an
AuthConfigProvider object. For more information about how to display these configurations on the login page, see these resources in
Salesforce Help.

**•** [My Domain: Add Identity Providers to the My Domain Login Page](https://help.salesforce.com/s/articleView?id=products.domain_name_login_id_prov.htm&type=5&language=en_US)

**•** [Experience Cloud: Configure Your Login Page](https://help.salesforce.com/s/articleView?id=xcloud.external_identity_login_pages_configure.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have “View Setup and Configuration” permission to view the settings.


### Standard Objects AuthorizationForm

Fields

**Field Name** **Details**

```
AuthConfigId

AuthProviderId

### AuthorizationForm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID for this configuration.

This is a relationship field.

**Relationship Name**
AuthConfig

**Relationship Type**
Lookup

**Refers To**
AuthConfig

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Auth. Provider or SAML configuration.

This is a polymorphic relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig

Represents the specific version and effective dates of a form that is associated with consent, such as a privacy policy or terms and
conditions. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects AuthorizationForm

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
DefaultAuthFormTextId

EffectiveFromDate

EffectiveToDate

IsSignatureRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the default authorization form text to use if text isn’t available
for a specific language.

This is a relationship field.

**Relationship Name**
DefaultAuthFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form takes effect.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form is no longer in effect.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the authorization form requires a signature.


Standard Objects AuthorizationForm

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

RevisionNumber

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
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form.

**Type**
reference

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

**Type**
string


### Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The revision number of the authorization form. For example, "rev1.21."

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormHistory**

History is available for tracked fields of the object.

**AuthorizationFormOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormShare**

Sharing is available for the object.

### AuthorizationFormConsent

Represents the date and way in which a user consented to an authorization form. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormTextId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The authorization form text that the Individual consented to.


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
AuthorizationFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

```
ConsentCapturedDateTime

ConsentCapturedSource

ConsentCapturedSourceType

ConsentGiverId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The date and time that consent was given.

**Type**
string

**Properties**
Create, Filter, Group, Nillable Sort, Update

**Description**
Required. The source through which consent was captured. For example,
user@example.com, www.example.com.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The source type through which consent was captured. For example,
phone, email, or website.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the person consenting to the authorization form.

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, CareProgramEnrollee, Contact, Individual, User

```
DocumentVersionId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the document version for which consent is given.

This is a relationship field.

**Relationship Name**
DocumentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

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
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects AuthorizationFormConsent

**Field Name** **Details**

**Description**

Required. The name of the authorization form consent.

```
OwnerId

RelatedRecordId

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The ID of the owner of the account associated with this customer.

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

The ID of a record showing consent of an authorization form.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Visit

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the authorization form.

Possible values are:

**•** `Rejected`

**•** `Seen`


### Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**•** `Signed`

```
PartyId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field was removed in API version 47.0. Use `ConsentGiverId` instead.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AuthorizationFormConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**AuthorizationFormConsentHistory**

History is available for tracked fields of the object.

**AuthorizationFormConsentOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormConsentShare**

Sharing is available for the object.

### AuthorizationFormDataUse

Represents the data use consented to in an authorization form. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormId

```

**Type**
reference


Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
AuthorizationForm

```
DataUsePurposeId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Identifies the data use purpose record associated with the authorization
form.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

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


Standard Objects AuthorizationFormDataUse

**Field Name** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

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
Required. The name of the authorization form data use.

**Type**
reference

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

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormDataUseChangeEvent (API version 62.0)**
Change events are available for the object.

**AuthorizationFormDataUseHistory**

History is available for tracked fields of the object.

**AuthorizationFormDataUseOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormDataUseShare**

Sharing is available for the object.


### Standard Objects AuthorizationFormText AuthorizationFormText

Represents an authorization form’s text and language settings. This object is available in API version 46.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
AuthorizationFormId

ContentDocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
### AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
### AuthorizationForm

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentDocument that provides the authorization form’s text.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup


Standard Objects AuthorizationFormText

**Field Name** **Details**

**Refers To**
ContentDocument

```
DetailAuthorizationFormText

FullAuthorizationFormUrl

LastReferencedDate

LastViewedDate

Locale

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A detailed version of the authorization form.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL where the full text of the authorization form is located.

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
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**

picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. `Locale` and `LocaleSelection` have the same
function.


### Standard Objects AuthProvider

**Field Name** **Details**

Note: `Locale` can contain custom values not included in the picklist
if added before version 47.0.

```
LocaleSelection

Name

SummaryAuthFormText

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. `Locale` and `LocaleSelection` have the same
function.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form text.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A shortened version of the authorization form that is displayed to the user.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormTextChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormTextHistory**

History is available for tracked fields of the object.

### AuthProvider

Represents an authentication provider (auth provider). An auth provider lets users log in to your Salesforce org from an external service
provider, such as Facebook, Google, or GitHub. This object is available in API version 27.0 and later.


Standard Objects AuthProvider

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Only users with Customize Application and Manage AuthProviders permissions can access this object.

Fields

**Field Name** **Details**

```
AppleTeam

AuthorizeUrl

ConsumerKey

ConsumerSecret

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. A
10-character team ID, obtained from an Apple developer account. Available in
API version 48.0 and later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required when creating an OpenID Connect authentication provider. The OAuth
authorization endpoint URL. Available in API version 29.0 and later. In API version
33.0 and later, for Salesforce-managed auth providers, leave the field blank to let
Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The app’s key that is registered at the third-party (external) authentication
provider. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Nillable


Standard Objects AuthProvider

**Field Name** **Details**

**Description**

The consumer secret of the authentication provider that is registered at the
third-party SSO provider. It’s used by the consumer for identification to Salesforce.
In API version 33.0 and later, for Salesforce-managed auth providers, leave the
field blank to let Salesforce supply and manage the value. You can create your
own consumer secret on `create()` . However, after you set it, you can’t change
the value.

```
CustomMetadataTypeRecord

DefaultScopes

DeveloperName

EcKey

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when creating a custom authentication provider plug-in. The API name
of the custom authentication provider. Available in API version 36.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

For OpenID Connect authentication providers, the scopes to send with the
authorization request, if not specified when a flow starts. Available in API version
29.0 and later. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Required. Used when referring to the authentication provider from a program.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. Available
in API version 48.0 and later.


Standard Objects AuthProvider

**Field Name** **Details**

```
ErrorUrl

ExecutionUserId

FlowDefaultAccountId

FlowDefaultProfileId

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

A custom error URL for the authentication provider to use to report errors.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Required to specify a registration handler. The username of the Salesforce admin
or system user who runs the Apex handler or flow. The execution user provides
the context in which the registration handler runs. For example, if the handler
creates a contact, the creation can be easily traced back to the registration process.
In production, use a system user. The user must have the Manage Users
permission. Available in API version 27.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For authentication providers that use a flow registration handler, the default
account that new external users are assigned to. If you include this field, Salesforce
automatically uses it for the `defaultAccountId` variable in the
Authentication Provider User Registration standard flow.

A default account is required to use a flow registration handler for external users.
You can specify a default account here or in the flow itself. If you use both, the
default account that's configured in the flow takes precedent.

Available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For authentication providers that use a flow registration handler, the default
profile that new users are assigned to. If you include this field, Salesforce
automatically uses it for the `defaultProfileId` variable in the
Authentication Provider User Registration standard flow.


Standard Objects AuthProvider

**Field Name** **Details**

A default profile is required to use a flow registration handler. You can specify a
default profile here or in the flow itself. If you use both, the default profile that's
configured in the flow takes precedent.

Available in API version 64.0 and later.

```
FriendlyName

IconUrl

IdTokenIssuer

LinkKickoffUrl

LogoutUrl

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Required. A user-friendly name for the authentication provider.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The path to an icon to use as a button on the login page. Users click the button
to log in with the associated authentication provider, such as Twitter or Facebook.
Available in API version 32.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The source of the authentication token in `https:` URI format. This field is
available when configuring an OpenID Connect or Microsoft authentication
provider. If provided, Salesforce validates the returned `id_token` value. OpenID
Connect requires returning an `id_token` value with the `access_token`
value. Available in API version 30.0 and later.

**Type**
url

**Properties**
Nillable

**Description**
The URL for linking existing Salesforce users to a third-party account. This field is
read-only. Available in API version 43.0 and later.

**Type**
url


Standard Objects AuthProvider

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The destination for users after they log out if they authenticated using single
sign-on. The URL must be fully qualified with an http or https prefix, such as
`https://acme.my.salesforce.com` . Available in API version 33.0 and
later.

```
OauthKickoffUrl

OptionsIncludeOrgIdInId

OptionsIsPkceEnabled

```

**Type**
url

**Properties**
Nillable

**Description**
The URL for obtaining OAuth access tokens for a third party. This field is read-only.
Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Used to differentiate between users with the same user ID from two sources
(such as two sandboxes). If enabled ( `true` ), Salesforce stores the org ID of the
third-party identity in addition to the user ID. After you enable this setting, you
can’t disable it. Applies only to a Salesforce-managed auth provider. Available in
API version 32.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If set to `true`, the authentication provider uses the OAuth 2.0 Proof Key for Code
Exchange (PKCE) extension, which improves the security of the provider’s
authorization flow. This field applies only to these `providerType` values:

**•** `Custom`

**•** `Facebook`

**•** `Google`

**•** `Microsoft`

**•** `OpenIdConnect`

**•** `Salesforce` .


Standard Objects AuthProvider

**Field Name** **Details**

This field is available in API version 59.0 and later.

```
OptionsRequireMfa

OptionsSendAccessTokenInHeader

OptionsSendClientCredentialsInHeader

OptionsSendSecretInApis

```

**Type**
boolean

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this auth
provider based on the MFA status of each user. For this setting to trigger MFA,
you must apply MFA directly to users via one of two methods. 1) Assign the user
permission Multi-Factor Authentication for User Interface Logins. 2) Enable the
org setting Require multi-factor authentication (MFA) for all direct UI logins to
your Salesforce org.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

If enabled ( `true` ), the access token is sent to the `UserInfoUrl` in a header
instead of a query string. Available in API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Required when creating an OpenID Connect authentication provider. If enabled
( `true` ), the client credentials are sent in a header to the `tokenUrl` instead
of a query string. The credentials are in the standard OpenID Connect Basic
Credentials header format, which is `Basic <token>`, where `<token>` is
the base64-encoded string `"clientkey:clientsecret"` . Available in
API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Determines whether the encrypted consumer secret appears in API responses.
If enabled (default), the secret appears in the response. If disabled ( `false` ),


Standard Objects AuthProvider

**Field Name** **Details**

responses don’t include the consumer secret. For security, you can disable the
setting. However, keep in mind that:

**•** By disabling this setting, the consumer secret is excluded from API responses
in all API versions.

**•** Change sets and other metadata deployments break because both the
consumer key and secret are expected. To fix this problem, insert the
consumer key manually during deployment.

Available in API version 47.0 and later.

```
PluginId

ProviderType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An existing Apex class that extends the
`Auth.AuthProviderPluginClass` abstract class. Available in API version
39.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Required. The third-party authentication provider to use. Valid values include:

**•** `Apple` . Available in API version 48.0 and later.

**•** `Bitbucket` —Provides authentication for a `Bitbucket` provider. Enables
you to connect to Bitbucket from a Lightning Platform application. When
logged in to Bitbucket, the app can makes calls to Bitbucket APIs. The
`Bitbucket` provider isn’t available as an SSO provider, so users can’t log
in to a Salesforce org using their Bitbucket login credentials. Available in API
version 61.0 and higher.

**•** `Custom` —A provider configured with a custom authentication provider
plug-in. Available in API version 36.0 and later.

**•** `Facebook` .

**•** `GitHub` —Provides authentication for a `GitHub` provider. Used to log in
users of your Lightning Platform app to GitHub using OAuth. When logged
in to GitHub, your app can make calls to GitHub APIs. The `GitHub` provider
isn’t available as an SSO provider, so users can’t log in to your Salesforce org
using their GitHub login credentials. Available in API version 35.0 and later.

**•** `Google` .

**•** `Janrain` .

**•** `LinkedIn` . Available in API version 32.0 and later.


Standard Objects AuthProvider

**Field Name** **Details**

**•** `Microsoft` . Provides authentication for all services that can be accessed
via Microsoft Azure Active Directory. Available in API version 55.0 and later.

**•** `MicrosoftACS` —Microsoft Access Control Service provides authentication
for a Microsoft Office 365 service, like SharePoint Online. The
`MicrosoftACS` provider doesn't support SSO. Available in API version
31.0 and later.

**•** `OpenIdConnect` . Available in API version 29.0 and later.

**•** `Salesforce` .

**•** `Slack` . Available in API version 54.0 and later.

**•** `Twitter` . Available in API version 32.0 and later.

```
RegistrationHandlerId

SsoKickoffUrl

TokenUrl

UserInfoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An existing Apex class that implements the `Auth.RegistrationHandler`
interface.

**Type**
url

**Properties**
Nillable

**Description**
The URL for performing SSO into Salesforce from a third party by using its
third-party credentials. This field is read-only. Available in API version 43.0 and
later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The OAuth token endpoint URL of an OpenID Connect authentication provider.
Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers for sandbox use cases only, leave the field
blank to let Salesforce supply and manage the value.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects AuthProvParamFwdAllowlist

**Field Name** **Details**

**Description**

The OpenID Connect endpoint URL of the OpenID Connect authentication
provider. Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers, leave the field blank to let Salesforce supply
and manage the value.

### AuthProvParamFwdAllowlist

Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization
URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales` parameter and use
it to send a user's language preference from Salesforce to the third-party provider's login page. This object is available in API version
62..0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AuthProviderId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the authentication provider associated with the allowlist.

This field is a relationship field.

**Relationship Name**
AuthProvider

**Refers To**
AuthProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description for the allowlisted URL parameter.


### Standard Objects AuthSession

**Field** **Details**

```
Param

### AuthSession

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the parameter, such as `ui_locales` or `login_hint` .

The AuthSession object represents an individual user session in your organization. This object is available in versions 29.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
CreatedDate

Id

IsAssociatedWithJwtAccessToken

```

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was created. This field is a standard system field.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, ID Lookup, Sort

**Description**
The current session’s ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the session is associated with a JSON Web Token (JWT)-based access
token. This field is available in API version 64.0 and later.


Standard Objects AuthSession

**Field Name** **Details**

```
IsCurrent

LastModifiedDate

LoginGeoId

LoginHistoryId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the session is a member of the user’s current session family. This field
is available in API version 37.0 and later.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was last updated. A session expires when the
current date and time equals `LastModifiedDate` + `NumSecondsValid` .
This field is a standard system field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
login event. Due to the nature of geolocation technology, the accuracy of
geolocation fields (for example, country, city, postal code) can vary. This field is
available in API version 34.0 and later.

This is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

**Refers To**
LoginGeo

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for a successful login event. When a session is reused,
Salesforce updates the `LoginHistoryId` with the value from the most
recent login. This field is available in API version 33.0 and later.


Standard Objects AuthSession

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
LoginHistory

**Relationship Type**
Lookup

**Refers To**
LoginHistory

```
LoginType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** `AJAX Toolkit`

**•** `Apex Office Toolkit`

**•** `AppExchange`

**•** `Application`

**•** `AppStore`

**•** `Certificate-based login`

**•** `Chatter Communities External User`

**•** `Chatter Communities External User Third Party SSO`

**•** `Community`

**•** `Customer Service Portal Third-Party SSO`

**•** `Customer Service Portal`

**•** `DataJunction`

**•** `DB Replication`

**•** `Employee Login to Community`

**•** `Excel Integration`

**•** `Help and Training`

**•** `HOTP YubiKey`

**•** `Lightning Login`

**•** `Networks Portal API Only`

**•** `Offline Client`

**•** `Order Center`

**•** `Other Apex API`

**•** `Outlook Integration`

**•** `Partner Portal Third-Party SSO`

**•** `Partner Portal`


Standard Objects AuthSession

**Field Name** **Details**

**•** `Partner Product`

**•** `Passwordless Login`

**•** `Remote Access 2.0`

**•** `Remote Access Client`

**•** `Sales Anywhere`

**•** `Salesforce Outlook Integration`

**•** `Salesforce.com Website`

**•** `SAML Chatter Communities External User SSO`

**•** `SAML Customer Service Portal SSO`

**•** `SAML Idp Initiated SSO`

**•** `SAML Partner Portal SSO`

**•** `SAML Sfdc Initiated SSO`

**•** `SAML Site SSO`

**•** `Self-Service`

**•** `Signup`

**•** `Sync`

**•** `SysAdmin Switch`

**•** `Third Party SSO`

**•** `Unknown`

**•** `Validate`

```
LogoutUrl

NumSecondsValid

ParentId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The page or view to display after users log out of an Experience Cloud site, or an
org if they authenticated using SAML. This field is available in API version 32.0
and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of seconds before the session expires, starting from the last update
time.

**Type**
reference


Standard Objects AuthSession

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the parent session, if one exists (for example, if the current
session is for a canvas app). If the current session doesn’t have a parent, this value
is the current session’s own ID.

```
SessionSecurityLevel

SessionType

SourceIp

UserType

UsersId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Standard or High, depending upon the authentication method used.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of session. Common ones are UI, Content, API, and Visualforce.

[For more information, see User Session Types in the](https://help.salesforce.com/s/articleView?id=xcloud.security_session_types.htm&type=5&language=en_US) _Object Reference Guide_ .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
IP address of the end user’s device from which the session started. This address
can be an IPv4 or IPv6 address.

The `SourceIp` field doesn't support the `LIKE` [comparison operator.](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_comparisonoperators.htm)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The kind of user for this session. Types include Standard, Partner, Customer Portal
Manager, High Volume Portal, and CSN Only.

**Type**
reference


### Standard Objects AutomatedAction

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s Salesforce user ID.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

Usage

The AuthSession object exposes session data and enables read and delete operations on that data. For example, use this object to see
who is signed in to your org. Or you can use this object to create a tool to delete a session, ending that user’s session. For a user, only
their own sessions are available, while administrators can see all sessions.

You can’t change user sessions with this object. You can only read and delete them.

### AutomatedAction

Represents the configuration of an automated action, such as a workflow rule. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ApiVersion

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. API version to use for executing the automated action.


Standard Objects AutomatedAction

**Field** **Details**

```
Description

ErrorDetail

ErrorMessage

EvalType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the error encountered when executing the automated action.

Possible values are:

**•** `invalidCondition`

**•** `invalidConditionReference`

**•** `invalidConditionValue`

**•** `invalidInvocableAction`

**•** `invalidInvocableActionParam`

**•** `invalidReferenceEntity`

**•** `unknownError`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the error encountered when executing the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
When the automated action runs.

Possible values are:

**•** `OnCreate`

**•** `OnCreateAndUpdate`


Standard Objects AutomatedAction

**Field** **Details**

```
ExecutionType

ExtraFilterExpression

ExtraFilterType

FilterExpression

FilterType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Whether the action runs automatically or generates a reminder.

Possible values are:

**•** `Automatic`

**•** `Reminder`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional condition logic for cross-object filters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Additional criteria for cross-object filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If `FilterType` is `Advanced`, this field contains the condition logic.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AutomatedAction

**Field** **Details**

**Description**
Criteria for filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`

```
InvocationName

IsLocked

LastEditedDateTime

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Invocable action to execute.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record is locked or not.

The default value is `false` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the automated action had a change that impacted rule evaluation.

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


Standard Objects AutomatedAction

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record was likely referenced ( `LastReferencedDate` ) and not viewed.

```
MayEdit

Name

ReferenceEntity

RuleType

State

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the automated action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Entity on which the automated action operates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of workflow rule.

Possible values are:

**•** `ManagerAssigned`

**•** `ManagerSubscribed`

**•** `Personal`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects AutomatedActionCondition

**Field** **Details**

**Description**
The status of the alert.

Possible values are:

**•** `Active`

**•** `Error`

**•** `Inactive`

```
SubscriptionState

Summary

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
For users who don’t have an override, the default value of the subscription.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A human-readable explanation of the automated action, its conditions, and its parameters.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionShare on page 67**
Sharing is available for the object.

### AutomatedActionCondition

Represents the logical operator details for evaluating conditions in an automated action. This object is available in API version 57.0 and
later.


Standard Objects AutomatedActionCondition

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutomatedActionId

ConditionNumber

IsLocked

MayEdit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference number of the condition containing advanced filter logic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AutomatedActionCondition

**Field** **Details**

**Description**
Indicates whether the automated action condition record can be edited or not.

The default value is `false` .

```
Operator

ReferenceField

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The logical operator for this condition.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `IsChanged`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `StartsWith`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to use for this condition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of condition.

Possible values are:

**•** `ExtraFilterCondition`

**•** `PrimaryFilterCondition`


### Standard Objects AutomatedActionOverride

**Field** **Details**

```
Value

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to compare to the `ReferenceField` .

### AutomatedActionOverride

Represents a modified attribute of a shared automated action. For example, the modified attribute can contain customizations for your
business. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
FieldName

IsLocked

IsRelatedRecordOverridable

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the field to override.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects AutomatedActionOverride

**Field** **Details**

**Description**
Indicates whether the parent automated action record can be overridden.

The default value is `false` .

```
MayEdit

Name

RelatedRecordApiName

RelatedRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the automated action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object name of the `RelatedRecordId` .

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the automated action.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
AutomatedAction, FtestUser


### Standard Objects AutomatedActionParameter

**Field** **Details**

```
Value

```

Associated Objects

**Type**
textarea

**Properties**
Create, Update

**Description**
The overridden value used for `FieldName` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionOverrideOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionOverrideShare on page 67**
Sharing is available for the object.

### AutomatedActionParameter

Represents the values or field references evaluated by the automated action. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AutomatedActionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
### AutomatedAction

**Relationship Type**
Lookup


Standard Objects AutomatedActionParameter

**Field** **Details**

**Refers To**
AutomatedAction

```
DataType

IsLocked

MayEdit

ParameterName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the value or field reference value.

Possible values are:

**•** `Boolean`

**•** `Double`

**•** `Int`

**•** `None`

**•** `String`

**•** `ValueList`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the invocable action parameter the value maps to.


### Standard Objects AutomatedActionReminder

**Field** **Details**

```
ReferenceField

Value

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reference to the field that’s resolved at runtime. For example, LeadID. If `Value` has a
value, this field is null.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to be passed to the invocable action parameter at runtime. If `ReferenceField`
has a value, this field is null.

### AutomatedActionReminder

Represents a reminder to the end user to take an action in the future. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionTakenDateTime

AutomatedActionId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Timestamp of when the user took the action suggested by the reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AutomatedActionReminder

**Field** **Details**

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

```
IsLocked

IsValidForUser

MayEdit

ReferenceRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record is locked or not.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action is active and accessible to the user who owns the
record ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record can be edited or not.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects AutomatedActionReminder

**Field** **Details**

**Description**
The record that triggered the reminder. For example, when a rule is set to Case, the value of
this field is `CaseId` .

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact, Invoice, Lead, Opportunity

```
StartDateTime

State

Type

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time this reminder is scheduled to be displayed to the user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the reminder.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Disabled`

**•** `Dismissed`

**•** `Expired`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of automated action reminder.

Possible values are:

**•** `Reminder`


### Standard Objects BackgroundOperation

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionReminderOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AutomatedActionReminderShare on page 67**
Sharing is available for the object.

### BackgroundOperation

Represents a background operation in an asynchronous job queue. This object is available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `retrieve()`

Special Access Rules

### • BackgroundOperation doesn’t support search.

Fields

**Field Name** **Details**

```
Error

ExecutionGroup

ExpiresAt

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the execution group.

**Type**
dateTime


Standard Objects BackgroundOperation

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
After this time, the operation is removed from the asynchronous job queue.
Applies only if the operation has a status of complete, canceled, error, or merged.

```
FinishedAt

GroupLeaderId

Name

NumFollowers

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation reached the status of completed or error.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the operation that’s selected as the
leader of the execution group.

This field is a relationship field.

**Relationship Name**
GroupLeader

**Relationship Type**
Lookup

**Refers To**
BackgroundOperation

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Identifies the background operation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BackgroundOperation

**Field Name** **Details**

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Number of other operations that are in the
execution group.

```
ParentKey

ProcessAfter

RetryBackoff

RetryCount

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Tag that identifies related sets of operations, if any.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The operation is scheduled to be processed after this time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation has an error status. The first retry is attempted
immediately. Each subsequent retry is increasingly delayed according to an
exponential expression that’s multiplied by the `RetryBackoff`, in milliseconds.

Specifically, the delay time is `(2` `[n]` `-1)×R`, where `n` is the `RetryCount`, and
`R` is the `RetryBackoff` .

The default value for `RetryBackoff` depends on the type of operation. For
example, the `RetryBackoff` default for write operations on external objects
is 1,000 milliseconds. For write operations, retries are attempted immediately,
after 3 seconds, after 7 seconds, after 15 seconds, and so on.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Number of attempted retries. Applies only if the operation has an error status.


Standard Objects BackgroundOperation

**Field Name** **Details**

```
RetryLimit

SequenceGroup

SequenceNumber

StartedAt

Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Maximum number of retries to attempt. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence group. Applies only if the operation is merged with other
operations into an execution group to be processed in bulk. Within an execution
group, operations can be placed into a sequence group to be executed in a
specific order.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Order position within the sequence group. Applies only if the operation is merged
with other operations into an execution group to be processed in bulk. Within
an execution group, operations can be placed into a sequence group to be run
in a specific order.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

When the operation started running.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the background operation. The options are:


Standard Objects BackgroundOperation

**Field Name** **Details**

**•** `New`

**•** `Scheduled`

**•** `Canceled`

**•** `Merged`

**•** `Waiting`

**•** `Running`

**•** `Error`

**•** `Complete`

```
SubmittedAt

Timeout

Type

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation was added to the job queue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maximum time in milliseconds to wait for results after the operation started
running.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the background operation. The options are:

**•** `ApiCatalogPoller`

**•** `BlockchainEventPoller`

**•** `CdpMetadataDeploy`

**•** `ExternalChangeDataCapture`

**•** `ExternalConnectivityPoller`

**•** `ExternalObject`

**•** `ExternalObjectSync`

**•** `ExternalServiceCallback`

**•** `MetadataChangesetOperation`

**•** `MfgBulkUpdate`


### Standard Objects BackgroundOperationResult

**Field Name** **Details**

**•** `PrivateConnectMigration`

**•** `SingularityAutoSync`

**•** `SingularityMDSSync`

**•** `SingularitySchemaEvolutionTrigger`

**•** `SiteTaskCreate`

**•** `SiteTaskPublish`

**•** `Sweeper`

**•** `WebCart`

**•** `XClean`

```
WorkerUri

```

Usage

Use the BackgroundOperation object to:

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
URI of the worker that performed the operation.

Example for a Salesforce Connect OData operation:

```
  services/data/v35.0/xds/upsert

```

**•** Monitor the job status of asynchronous operations.

**•** View errors that are related to the asynchronous operations.

**•** Extract statistics for the asynchronous job queue.

### BackgroundOperationResult

Stores error messages generated when or importing data into big objects using Bulk API. This is a big object, available in API version
37.0 and later.

### Each instance of BackgroundOperationResult represents one error. The Message field stores the text of the error message.

The `ParentID` field stores the:

**•** Batch ID for the data import, in case of Bulk API

Bulk API validates data at the time of import, and generates an error message for the first occurrence of invalid data in any row of the
data file. The validation performed depends on the type of data being imported.

**•** **Text** —The length of the input string must be less than or equal to the length of the corresponding text field in the target object.

**•** **Number** —The input data must be a number, whose scale and precision are compatible with the corresponding number field in
the target object.


Standard Objects BackgroundOperationResult

**•** **ID—** The input data must be a valid 15- or 18-character ID.

**•** **DateTime** —The input data must be a valid dateTime value, in the approved format.

**•** **Lookup** —The lookup value must be a valid 15- or 18-character ID.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
CreatedById

CreatedDate

Data

Id

Message

```

**Type**
ID

**Properties**
Nillable

**Description**
The user ID of the user initiating the Bulk API request.

**Type**
dateTime

**Properties**
Defaulted on create

**Description**
The date and time at which the Bulk API request was made.

**Type**
string

**Properties**
Nillable

**Description**
The data that generated the error message. The total length is limited to 2,000
characters, and each column can occupy a maximum of 50 characters. Any data
exceeding those limits is truncated.

**Type**
ID

**Properties**
Defaulted on create, idLookup

**Description**
The ID of the error message.

**Type**
string


### Standard Objects BatchApexErrorEvent

**Field Name** **Details**

**Properties**
Nillable

**Description**
The text of the error message.

```
MessageType

ParentId

```

Usage

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The type of error message. The possible values are: ERROR, WARNING, or INFO.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The batch ID in Bulk API.

You can check for errors by querying the `BackgroundOperationResult` object. For example, this query returns details of all
errors in a data file imported using Bulk API, whose batch ID is `751xx000000006OAAQ` .

```
SELECT CreatedbyId, CreatedDate, Id, Message, MessageType, ParentId FROM

BackgroundOperationResult WHERE ParentId = “751xx000000006OAAQ”

```

Note: You can only view errors resulting from Bulk API requests that you initiated, unless you have the global permission to view
all data.

### BatchApexErrorEvent

[The documentation has moved to BatchApexErrorEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_batchapexerrorevent.htm) _Platform Events Developer Guide_ .

### BillingBatchScheduler

Represents a scheduled processing job that triggers recurring invoice batch runs and payment batch runs in Subscription Management.
This object is available in API version 55.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`


Standard Objects BillingBatchScheduler

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchscheduler.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchscheduler.htm)

Fields

**Field** **Details**

```
BillingSchedulerName

Comments

CronExpression

EndDate

FrequencyCadence

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the scheduler.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional field for comments about the scheduler.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Determines how often the scheduler recurs.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the scheduler stops triggering batch processing jobs.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects BillingBatchScheduler

**Field** **Details**

**Description**
Indicates how often the scheduler triggers the invoice batch run or the payment batch run.

Possible values are:

**•** `Daily` —The scheduled job recurs every day.

**•** `Monthly` —The scheduled job recurs every month.

**•** `Once` —The scheduled job occurs one time and doesn’t recur.

**•** `Weekly` —The scheduled job recurs every week.

```
FrequencyOptions

JobType

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Nillable

**Description**
Derived field that stores the scheduler configuration.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of batch processing job that the scheduler triggers.

Possible values are:

**•** `Invoice` —The scheduler starts a batch invoice run.

**•** `Payment` —The scheduler starts a batch payment run.

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


Standard Objects BillingBatchScheduler

**Field** **Details**

```
NextRunTime

OwnerId

RecurringSubType

RecurringType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and timestamp of the next scheduled batch invoice run or batch payment run are
shown in the user's time zone.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who created the scheduler.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the frequency at which the batch processing job recurs when the
`FrequencyCadence` is set to _Monthly_ .

Possible values are:

**•** `Every` —The processing job recurs at every instance of the frequency of the value. For
example, if the `RecurringSubType` is _`Every`_ and the `FrequencyCadence`
is _`Weekly`_, then the batch processing job recurs every week.

**•** `SpecificDate` —The scheduler triggers the batch processing job on the selected
date. For example, if the selected date is _`5`_, and the `FrequencyCadence` is
_`Monthly`_, then the job recurs on the fifth day of each month.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects BillingBatchScheduler

**Field** **Details**

**Description**
Specifies the frequency at which the batch processing job is repeated when the
`FrequencyCadence` is set to _Weekly_ .

Possible values are:

**•** `Every`

```
RecursOn

RecursOnDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the interval at which the scheduler triggers a batch processing job.

If the FrequencyCadence is _`Monthly`_, you must select either the specific date or the interval
when the schedule triggers the job.

Possible values are:

**•** `First`

**•** `Fourth`

**•** `Last`

**•** `Second`

**•** `Third`

**Example:** To tell the scheduler to trigger the job on the first Monday of the month, set the
following fields:

**•** `FrequencyCadence` = _`Monthly`_

**•** `RecursOn` = _`First`_

**•** `RecursOnDay` = _`Monday`_

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the date on which the scheduler triggers a batch processing job.

**Example:** To tell the scheduler to trigger the job on the fifth day of the month, set the
following fields:

**•** `FrequencyCadence` = _`Monthly`_

**•** `RecursOnDate` = _`5`_

**Example:** To tell the scheduler to trigger the job on the second to last day of the month,
set the following fields:

**•** `FrequencyCadence` = _`Monthly`_


Standard Objects BillingBatchScheduler

**Field** **Details**

**•** `RecursOnDate` = _`SecondToLast`_

If you select _`Last`_, _`SecondToLast`_, or _`ThirdToLast`_, the date of the batch processing
job varies depending on the number of days in the month.

For example, suppose _`SecondToLast`_ is selected. If the month has 30 days, such as June,
then the batch processing job occurs on the 28th day. If the month has 31 days, such as July,
then the batch processing job occurs on the 29th day.

```
RecursOnDay

RunCriteriaId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the day on which the scheduler triggers a batch processing job.

If the `FrequencyCadence` field is set to _`Weekly`_, then you must select the day when
the scheduler runs. The scheduler recurs every week on the selected day; for example, weekly
on Monday.

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the filter criteria that’s defined for the invoice batch run or the payment batch run.

This field is a polymorphic relationship field.

**Relationship Name**
RunCriteria

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRunCriteria, PaymentBatchRunCriteria


### Standard Objects BillingPeriodItem

**Field** **Details**

```
StartDate

StartTime

Status

TimeZone

### BillingPeriodItem

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date when the scheduler triggers its first batch processing job.

**Type**
time

**Properties**
Filter, Sort

**Description**
The time when the scheduler triggers the batch processing job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the scheduler. Only Active schedulers can trigger batch processing jobs.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone is either the value selected when the run was configured, or it's the user's
time zone. The time zone is shown in Greenwich Mean Time (GMT).

Represents one payment period for a subscription. The billing period item is used to pass billing information to an invoice line item in
Subscription Management. This object is available in API version 55.0 and later.

When a billing schedule is invoiced, Subscription Management creates a billing period item to store the billing and payment information
that’s passed to an invoice line. Subscription Management next creates an invoice line for billing period items that match the invoice's


Standard Objects BillingPeriodItem

target date. One billing period item is created for each billing period in the billing schedule. For example, a one-year subscription that's
billed quarterly creates a billing schedule with four billing period items.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingperioditem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingperioditem.htm)

Fields

**Field** **Details**

```
Amount

BillingPeriodEndDate

BillingPeriodItemNumber

BillingPeriodStartDate

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Price for the billing period item. Used to calculate the invoice line's Amount field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's end date.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined number that refers to the billing period item.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's start date.


Standard Objects BillingPeriodItem

**Field** **Details**

```
BillingScheduleId

CurrencyIsoCode

InvoiceBatchRunId

InvoiceLineId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Parent billing schedule of the billing period item.

This field is a relationship field.

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the org. Available only for orgs with the
multicurrency feature enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Parent invoice batch run of the billing period item.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingPeriodItem

**Field** **Details**

**Description**
This field looks up to the invoice line that's generated from the billing period item. This field
is populated only when a billing period item is generated via an invoice batch run. Otherwise,
this field is empty.

This field is a relationship field.

**Relationship Name**
InvoiceLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

```
InvoiceStatus

Status

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the invoice that contains the invoice line created from the billing period item.

Valid values are:

**•** `Canceled` —The invoice for this billing period item was canceled.

**•** `Draft` —The invoice has been created but hasn’t been posted. Available in API version
60.0 and later.

**•** `DraftInProgress` —The invoice hasn’t been created yet. When the invoice is
created, the `InvoiceStatus` field value is changed to `Draft` . If the invoice
generation process fails, the `InvoiceStatus` field value shows
`DraftInProgress` . Available in API version 60.0 and later.

**•** `Error` —The invoice for this billing period item was generated in error.

**•** `Pending` —The invoice for this billing period item is being generated.

**•** `Posted` —An invoice line based on this billing period has been created and added
successfully to the invoice.

**•** `PostingInProgress` —An invoice line based on this billing period has been created
and is in the process of being added to the invoice. Available in API version 60.0 and
later.

**•** `Voided` —An invoice line based on this billing period was voided.

**•** `VoidInProgress` —An invoice line based on this billing period is in the process of
being voided.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects BillingPolicy

**Field** **Details**

**Description**
Status of the billing period item. Draft billing period items aren't evaluated for invoice line
creation.

Valid values are:

**•** `Canceled`

**•** `Draft`

**•** `Reviewed`

### BillingPolicy

Represents a group of billing treatments, which define the rules for how to invoice a customer for an order item. This object is available
in API version 55.0 and later.

Billing policies are related to products, which pass the policy on to the resulting order items. When an order is activated, Subscription
Management assigns a billing treatment to each order item based on the values in the `BillingTreatmentSelection` field.
Then Subscription Management uses the billing treatment to create billing schedules.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingpolicy.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingpolicy.htm)

Fields

**Field** **Details**

```
BillingTreatmentSelection

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management assigns billing treatments to order items and to
assets related to the billing policy.

Possible values are:


Standard Objects BillingPolicy

**Field** **Details**

**•** `Default` —The value specified in the DefaultBillingTreatmentId field is automatically
applied to order items and assets.

**•** `Manual` —Users must specify the billing treatment that's applied to the order items
and assets.

```
DefaultBillingTreatmentId

Description

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When `BillingTreatmentSelection` has a value of `Default`, Subscription
Management uses the selected billing treatment for all order items and assets related to the
billing policy.

This field is a relationship field.

**Relationship Name**
DefaultBillingTreatment

**Relationship Type**
Lookup

**Refers To**
BillingTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description that describes the billing policy.

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


### Standard Objects BillingSchedule

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
Name

Status

### BillingSchedule

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the billing policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The billing policy's status.

Possible values are:

**•** `Active` —Indicates that the billing policy is available for use on products.

**•** `Draft` —Indicates that the billing policy isn't available for use on products. Use this
status when creating billing policies that aren't ready to be activated.

**•** `Inactive` —Indicates that the billing policy isn't available for use on products.

Stores the order item information used in the invoicing process. This object is available in API version 55.0 and later.

When you activate an order, Subscription Management creates one billing schedule for each order item in an order. For example, if an
order contains 15 order items, Subscription Management creates 15 billing schedules, one billing schedule for each item. The invoice
scheduler uses the information in the billing schedule to determine when it's time to invoice an order item.

Billing schedules for all order items that are generated from one asset are summarized in a billing schedule group.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).


Standard Objects BillingSchedule

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedule.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedule.htm)

Fields

**Field** **Details**

```
BillDayOfMonth

BilledAmount

BillingAccountId

BillingPeriodAmount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
An integer from 1 to 31 that indicates the day of the month.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount (excluding tax) that has been invoiced from the billing schedule.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
BillingAccount

**Refers To**
Account

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount to be invoiced each billing period.

For example, if the billing period is monthly, this field shows the monthly amount that appears
on the invoice line.


Standard Objects BillingSchedule

**Field** **Details**

```
BillingScheduleEndDate

BillingScheduleGroupId

BillingScheduleNumber

BillingScheduleStartDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last date that the billing schedule is available for invoicing. Inherited from the EndDate
field on the order item.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the billing schedule group that contains the billing schedule. Billing schedules are
grouped when they have the same source order item. The source order item is the original
order item that a customer bought. Afterwards, if the customer amends, cancels, or renews
the order item, a new billing schedule is created with the BillingScheduleGroupId for the
original order item.

This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Relationship Type**
Lookup

**Refers To**
BillingScheduleGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated reference number for the billing schedule.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the billing schedule is available for invoicing. Inherited from the ServiceDate
on the order item.


Standard Objects BillingSchedule

**Field** **Details**

```
BilledThroughPeriod

BillingTreatmentItemId

CancellationDate

Category

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last billing period that includes this date.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The billing treatment item used to configure invoiceable amounts on the billing schedule.

This field is a relationship field.

**Relationship Name**
BillingTreatmentItem

**Relationship Type**
Lookup

**Refers To**
BillingTreatmentItem

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date on which the subscriber can no longer access the service. For example, if a service
ends on August 31, then the cancellation date is September 1, because that’s the date when
the subscriber can no longer use the service.

Subscription Management doesn't invoice billing schedules past their cancellation date.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The business action represented by the billing schedule.

Possible values are:

**•** AmendQuantity—A billing schedule for an order that changes the quantity. This object
is available in API version 56.0 and later.

**•** Cancellation—A billing schedule for an order that was canceled


Standard Objects BillingSchedule

**Field** **Details**

**•** Original—A billing schedule for the initial order

**•** Renewal—A billing schedule for an order that was renewed

```
CurrencyIsoCode

InvoiceBatchRunId

InvoiceRunBatch

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the invoice.

The default value is USD.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The invoice batch run that evaluated this billing schedule and its billing period items to
produce an invoice.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The batch value used by the invoice run that evaluated this billing schedule. During an
invoice run, billing schedules with the same batch value (including null) are grouped to the
same invoice run.

For example, create one batch of invoices for Premium Customers and another batch for
Regular Customers.

Possible values are:

**•** Premium Customers

**•** Regular Customers


Standard Objects BillingSchedule

**Field** **Details**

```
NextBillingDate

NextChargeFromDate

OriginalBillingScheduleId

PendingAmount

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the next billing period starts for the invoice. Used to calculate which invoice
lines are included on an invoice. When an invoice scheduler or API evaluates an order for
invoicing, billing schedules with a next billing date on or before the invoice's target date are
included on the invoice.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the billing schedule is invoiced in the upcoming billing period. For example,
if you invoiced a customer for a billing period of 01/01/22 through 01/31/22, the billing
schedule's `NextChargeFromDate` is 02/01/22.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this billing schedule is an amended or canceled billing schedule, then this field shows the
original billing schedule. Otherwise, this field is null.

This field is a relationship field.

**Relationship Name**
OriginalBillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount from the current billing term that hasn't been billed yet. For example, the unbilled
amount for a month, quarter, or year, depending on this billing schedule's billing term.


Standard Objects BillingSchedule

**Field** **Details**

```
Quantity

ReferenceEntityId

ReferenceEntityItemId

Status

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The quantity of the order item that created the billing schedule.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent order of the order item that created the billing schedule.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order item or asset that created the billing schedule.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustementLineTime, or OrderItemSummary

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the order item that the billing schedule represents.


### Standard Objects BillingScheduleGroup

**Field** **Details**

Possible values are:

**•** `CompletelyBilled`

**•** `Error`

**•** `Processing`

**•** `ReadyForInvoicing`

```
TaxTreatmentId

TotalAmount

UnitPrice

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Shows the treatment used to calculate tax for the billing schedule. Defined based on the
order item's tax policy.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of the order item represented by the billing schedule.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The price for an individual unit of the billing schedule's parent order item, including charges,
adjustments, and discounts. Inherited from the order item's `UnitPrice` field.

### BillingScheduleGroup

Represents a consolidated view of all billing schedules related to the order items generated from one asset, including new orders and
amendment orders. This object is available in API version 55.0 and later.


Standard Objects BillingScheduleGroup

When an order is created, a billing schedule is generated for each order item. The billing schedule group summarizes fields from each
billing schedule. For example, it summarizes financial fields such as Total Billed Amount and Total Pending Amount and billing fields
such as Billing Day of Month and Billing Term.

The billing schedule group includes schedules generated from a new order item and schedules generated from amendment order items.
The billing schedule group shows users the summarized financial data that includes any changes, such as new orders or amendments,
made to the asset.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Subscription Management, Commerce Subscriptions, and Billing (Revenue Cloud). If your org has both
Subscription Management and Commerce Subscriptions, then Subscription Management takes precedence.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulegroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulegroup.htm)

Fields

**Field** **Details**

```
BillDayOfMonth

BillToContactId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Billing Day of Month for the billing schedules that comprise the billing schedule group.

Subscription Management uses the order item's billing day of month to calculate the order
item’s next billing date, which the billing schedule then inherits. For example, an order item
can be billed on the first day of the month.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The contact related to the billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.

**Relationship Name**
BillToContact


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
BillingAccountId

BillingAddress

BillingCity

BillingCountry

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Salesforce account for the billing schedule group.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the billing address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.


Standard Objects BillingScheduleGroup

**Field** **Details**

```
BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

BillingMethod

BillingPostalCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the billing address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLongitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –90 and 90 with up to 15 decimal places. See Compound Field](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of billing used for the source item.

Possible values are:

**•** `Evergreen`

**•** `OrderAmount`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
Details for the billing address of this billing schedule group. Maximum size is 20 characters.

```
BillingScheduleGroupNumber

BillingStartMonth

BillingState

BillingStreet

BillingTerm

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the billing schedule group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field used with annual billing. The field shows the numbers from 1 to 12, which
indicate the month when billing begins for an annual subscription. For example, if billing
starts in January, the value is 1; if billing starts in June, the value is 6. This field is available in
API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this billing schedule group.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used with `BillingTermUnit` to define a billing cycle. For example, bill every 20 days
or every two months. In this example, the `BillingTerm` is _`20`_ and the
`BillingTermUnit` is _`days`_


Standard Objects BillingScheduleGroup

**Field** **Details**

```
BillingTermUnit

BillingType

CancellationDate

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The frequency with which the billing schedule is invoiced.

Possible values are:

**•** `Day`

**•** `Month`

**•** `OneTime`

**•** `Quarter`

**•** `Semi-Annual`

**•** `Year`

Used with `BillingTermUnit` to define a billing cycle.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Inherited from the shared value of each billing schedule in the billing schedule group. Defines
when Subscription Management bills a product or service relative to when it’s provided to
the customer. Advance billing invoices a product or service before you provide it, while
arrears billing invoices a product or service after you provide it. Subscription Management
evaluates the billing type when it calculates an order's next billing date.

Possible values are:

**•** `Advance`  - If the billing schedule is billed in advance, Subscription Management
evaluates the order’s billing day of month to choose the nearest date on or before the
order product’s start date. For example, if a monthly order product’s start date is January
1, and the order’s billing day of month is 15, the next billing date is December 15.

**•** `Arrears`  - If the billing schedule is billed in arrears, Subscription Management evaluates
the order’s billing day of month to choose the nearest date after the order product’s start
date. For example, if a monthly order product’s start date is January 1 and the order’s
billing day of month is 15, the order product’s next billing date is January 15.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
The date that a cancellation was made against the billing schedule. Subscription Management
doesn't invoice billing schedules past their cancellation date.

```
Controller

CurrentBillingPeriodAmount

CurrentQuantity

EffectiveNextBillingDate

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
During the invoicing process, this field determines which date is used when the billing
schedule group and billing schedule have a related field with conflicting values.

For example, when `Controller` has a value of `BillingScheduleGroup`, if the
billing schedule's billing day of month is 5 while the billing schedule group's billing day of
month is 10, the invoice is sent on the 10th day of the month.

Possible values are:

**•** `BillingScheduleGroup` —The date on the billing schedule group controls.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The earliest `NextBillingDate` from all billing schedules in the billing schedule group.
This field is a reference field that isn't used for any features or calculations.

This field is a calculated field.


Standard Objects BillingScheduleGroup

**Field** **Details**

```
EndDate

LastReferencedDate

LastViewedDate

OwnerId

PaymentTermId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The latest end date from all billing schedules in the billing schedule group.

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
Filter, Group, Sort, Update

**Description**
The Salesforce user who owns the billing schedule group.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


Standard Objects BillingScheduleGroup

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the payment term used in this billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

```
PeriodBoundary

Product2Id

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Inherited from the order item's parent quote line item or sales transaction item. The period
boundary helps determine the start and end date of the billing periods.

Possible values are:

**•** `AlignToCalendar` —the period starts on the first day of the term unit; for example,
the first day of the month.

**•** `Anniversary` —The start date determines the boundary. For example, if a monthly
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod` —the period starts on the day indicated by `PeriodBoundaryDay` .

**•** `EndOfPeriod` —the period starts on the last day of the pricing term unit.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the product for the order item represented by each billing schedule in the billing
schedule group.

This field is a relationship field.

**Relationship Name**
Product2


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductName

ProrationPolicyId

ReferenceEntityId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product for the order item represented by each billing schedule in the
billing schedule group.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Refers to the proration policy that applies to this billing schedule group. The proration policy
defines how time periods are calculated for subscription orders. For example, whether partial
periods are allowed.

Inherited from the shared proration policy for each billing schedule in the billing schedule
group.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset used to create the billing schedules in the billing schedule group.

This field is a relationship field.

**Relationship Name**
ReferenceEntity


Standard Objects BillingScheduleGroup

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Asset

```
ShippingAddress

ShippingCity

ShippingCountry

ShippingGeocodeAccuracy

ShippingLatitude

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the shipping address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. City maximum size is 40
characters

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Country maximum size is 80
characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the shipping address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects BillingScheduleGroup

**Field** **Details**

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

```
ShippingLongitude

ShippingPostalCode

ShippingState

ShippingStreet

StartDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with ShippingLatitude to specify the precise geolocation of an address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Postal code maximum size
is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. State maximum size is 80
characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address for this billing schedule group. Maximum of 255
characters.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects BillingTreatment

**Field** **Details**

**Description**
The earliest start date from all billing schedules in the billing schedule group.

```
TotalBilledAmount

TotalPendingAmount

### BillingTreatment

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that has been invoiced for all billing schedules within the billing schedule group.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that hasn't yet been invoiced for all billing schedules within the billing schedule
group.

This field is a calculated field.

Defines how Subscription Management bills an order item. The Exclude From Billing field controls whether the order item is invoiced.
Child billing treatment items control how much of the order item's balance is invoiced for each invoice across the subscription's lifecycle.
Billing treatments are assigned to order items based on the parent billing policy's Billing Treatment Selection field. This object is available
in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatment.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatment.htm)


Standard Objects BillingTreatment

Fields

**Field** **Details**

```
BillingPolicyId

Description

ExcludeFromBilling

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the billing policy for the billing treatment.

This field is a relationship field.

**Relationship Name**
BillingPolicy

**Relationship Type**
Lookup

**Refers To**
BillingPolicy

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description of the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Excludes any order items assigned to the treatment from creating billing schedules.

Possible values are:

**•** `No`

**•** `Yes`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects BillingTreatment

**Field** **Details**

```
LastViewedDate

LegalEntityId

Name

Status

```

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the legal entity used to assign the treatment to order items when the parent billing
policy's `BillingTreatmentSelection` is `LegalEntity` .

This field is a relationship field.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup

**Refers To**
LegalEntity

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Draft or inactive billing treatments can't be assigned to order items.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`


### Standard Objects BillingTreatmentItem

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BillingTreatmentHistory (API version 55.0)**
History is available for tracked fields of the object.

### BillingTreatmentItem

A billing treatment item defines how the order item's total amount is distributed into billing schedules over the course of the order
item's lifecycle. In the Subscription Management pilot, billing treatments must have only one billing treatment item, so that the billing
treatment item covers 100% of the order item's total value. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatmentitem.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatmentitem.htm)

Fields

**Field** **Details**

```
BillingTreatmentId

BillingType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent billing treatment for the billing treatment item.

This field is a relationship field.

**Relationship Name**
### BillingTreatment

**Relationship Type**
Lookup

**Refers To**
### BillingTreatment

**Type**
picklist


Standard Objects BillingTreatmentItem

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines when Subscription Management invoices a product or service relative to when it’s
provided to the customer. Advance billing invoices a product or service before it's provided,
while arrears billing invoices a product or service after it has provided Subscription
Management evaluates billing type when calculating an order product’s next billing date.

Possible values are:

**•** `Advance`                   - If the order item is billed in advance, Subscription Management evaluates
the order’s billing day of month to choose the nearest date on or before the order
product’s start date. For example, if a monthly order product’s start date is January 1,
and the order’s billing day of month is 15, the next billing date is December 15.

**•** `Arrears`                   - If the order item is billed in arrears, Subscription Management evaluates
the order’s billing day of month to choose the nearest date after the order product’s start
date. For example, if a monthly order product’s start date is January 1 and the order’s
billing day of month is 15, the order product’s next billing date is January 15.

Important: Arrears billing isn't available in Subscription Management API Version
54.0.

```
Controller

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
During the invoicing process, this field determines which value Subscription Management
uses when the billing schedule group and billing schedule have a shared field with different
values. For example, when `Controller` has a value of `BillingScheduleGroup`,
if the billing schedule's billing day of month is 5 while the billing schedule group's billing
day of month is 10, Subscription Management uses the value of 10.

In the Subscription Management API version 54.0, only `BillingScheduleGroup` is
supported.

Possible values are:

**•** `BillingScheduleGroup`  

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three-letter ISO 4217 currency code associated with the billing treatment item.


Standard Objects BillingTreatmentItem

**Field** **Details**

```
Description

FlatAmount

Handling0Amount

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for the billing treatment item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount in terms of units of currency (such as $10 or $21.52) to invoice from the order
item. Used only when `Type` has a value of `FlatAmount` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows how Subscription Management invoices billing period items that have an amount
of $0.

Possible values are:

**•** `CreateInvoice` —Create a $0 invoice line.

**•** Null —No invoice line is created.

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


Standard Objects BillingTreatmentItem

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

```
Name

Percentage

ProcessingOrder

Sequencing

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage (such as 10% or 12.5%) to invoice from the order item. Used only when
`Type` has a value of `Percentage` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Defines the order in which Subscription Management creates billing schedules based on
each billing treatment item. Lower numbers are evaluated first. For example, if your billing
treatment has a billing treatment item that invoices at 25 `Percentage` and a
`ProcessingOrder` of 1, and another item that invoices at 75 `Percentage` and a
`ProcessingOrder` of 2, your first billing schedule will be for 25 percent of the order
item's total amount, and your second billing schedule will be for 75% of the order item's
total amount.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows users to define the number used to start invoice numbers on invoices generated from
this billing treatment item.

Subscription Management API Version 54.0 supports only manual sequencing.

Possible values are:


### Standard Objects BlockedRedirectEventLog

**Field** **Details**

**•** `Manual—` Invoices created from this billing treatment item begin with an invoice number
of 1.

```
Status

Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Draft billing treatment items aren't evaluated for creating billing schedules.

Possible values are:

**•** `Active`

**•** `Draft`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines whether billing schedules created from this billing treatment item are based on a
flat amount or a percentage of the order item's total amount.

Possible values are:

**•** `FlatAmount` —The billing schedule is for a flat currency amount of the order item's
total amount (for example, $50 or $200.50.)

**•** `Percentage` —The billing schedule is for a percentage of the order item's total amount
(for example, 12.5% or 54%).

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BillingTreatmentItemHistory (API version 55.0)**
History is available for tracked fields of the object.

### BlockedRedirectEventLog

Blocked Redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. This object
is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects BlockedRedirectEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BlockedUri

BlockedUriDomain

IsMalformedUrl

Origin

Referrer

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The full string of the target for the redirection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If BLOCKED_URI is a URL, the domain for that URL. To allow future redirections to the
[BLOCKED_URI, BLOCKED_URI_DOMAIN is the value to add to RedirectWhitelistUrl.](https://developer.salesforce.com/docs/atlas.en-us.256.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm?q=%22Trusted%20URL%22)

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this redirection was blocked because the target URL failed a syntax check
or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin that caused the request to the BLOCKED_URI. For example, if a form on an
Experience Cloud Visualforce site page redirects a user to an untrusted URL via the saveURL
parameter, ORIGIN contains the base URL of that site.

**Type**
string


### Standard Objects Bookmark

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The absolute or partial address from which the request to the BLOCKED_URI came. The
`Referrer-Policy HTTP` Header of the request determines how much of the URL is
shared.

```
RemoteAddress

RequestIdentifier

Timestamp

### Bookmark

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Remote IP address of the client making the request.

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

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

Represents a link between opportunities that share common information.

This object is available to organizations with the Similar Opportunities feature enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects Bookmark

Fields

**Field** **Details**

```
ID

FromId

ToId

 IsDeleted

```

Usage

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
ID of the bookmark. Label is **Bookmark ID** .

**Type**
ID

**Properties**
Filter

**Description**
The originating opportunity. Label is **Bookmarked From ID**

**Type**
ID

**Properties**
Filter

**Description**
The opportunity to which the originating opportunity is linked. Label is **Bookmarked To**
**ID** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

The Bookmark object works with the Opportunity object only.

Use this read-only object to query the bookmarks between opportunities in your organization. In the online application, users can search
for opportunities that share attributes with their opportunity. The user can then bookmark the appropriate opportunities for future
reference.


### Standard Objects BotDefinition BotDefinition

Represents a top level object for Einstein Bots or Agentforce Agents. This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
AgentTemplate

AgentType

BotUserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this BotDefinition represents an agent, this field represents the name of the agent template
used to create it.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The agent type. For example, Agentforce Service Agent (ASA) or Agentforce Employee Agent
(AEA).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID associated with the bot definition.

**Relationship Name**
BotUser

**Refers To**
User


### Standard Objects BotVersion

**Field** **Details**

```
Description

DeveloperName

MasterLabel

Type

### BotVersion

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description for the bot or agent.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name for this object.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The master label of the bot.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
### This field represents the configuration type of the bot. The default value is Bot .

Possible values are:

### • Bot —Default Einstein Bot configuration.

**•** `ExternalCopilot`  - An external-facing agent. For example, Agenforce Service
Agent.

**•** `InternalCopilot`  - An internal-facing agent. For example, Agentforce (Default).

Represents a version of a bot or agent defined by a BotDefinition record. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects BotVersion

Fields

**Field** **Details**

```
BotDefinitionId

CopilotPrimaryLanguage

CopilotSecondaryLanguages

DeveloperName

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

Required. This field relates a bot version to its parent BotDefinition record.

This field is a relationship field.

**Relationship Name**
BotDefinition

**Refers To**
BotDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The primary language that the bot or agent communicates in.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

A comma-separated list of additional languages that the bot or agent supports.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects BrandingSet

**Field** **Details**

**Description**
Required. Indicates whether the bot version is active or inactive. Only one version for a related
BotDefinition can be active at once.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Inactive` .

```
ToneType

VersionNumber

### BrandingSet

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines the tone of the bot.

Possible values are:

**•** `Casual`  

**•** `Formal`  

**•** `Neutral`  

The default value is `Casual` .

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number for this version of the bot or agent.

Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder. This object is available in API version 40.0 and later.

Supported Calls

create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

Special Access Rules

The BrandingSet type is available when at least one of the following is enabled in your org: Digital Experiences, Surveys, or Lightning
Experience. All users, including unauthenticated guest users, can access this type.


Standard Objects BrandingSet

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

NamespacePrefix

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the set of branding properties.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. API name of the BrandingSet object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the branding set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user-facing label of the set of branding properties.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix with a 15 character limit. You
can refer to a component in a managed package by using
the `namespacePrefix__componentName` notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.


### Standard Objects BrandTemplate

**Field** **Details**

In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix. `NamespacePrefix` is null if the publisher is Salesforce.

### BrandTemplate

Letterhead for HTML EmailTemplate.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the letterhead. Limited to 1000 characters.

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
are reflected in a subscriber’s organization. Label is **Letterhead Unique Name** .


Standard Objects BrandTemplate

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

```
IsActive

Name

NamespacePrefix

Value

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the letterhead is available for use ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the template as it appears in the user interface. Limited to 255 characters. Label is
**Brand Template Name** .

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
Create, Update


### Standard Objects Brief

**Field** **Details**

**Description**
The contents of the letterhead, in HTML, including any logos.

Usage

Use this object to brand EmailTemplate records with your letterhead. You can also set a brand template to active or inactive. For example,
if you have five different marketing brands, you can maintain each different brand in one template, and assign to the appropriate
EmailTemplate.

SEE ALSO:

EmailTemplate

### Brief

Represents a marketing brief. A brief contains information that’s used for positioning and grounding a marketing campaign. Agentforce
can help you create a campaign that best fits the goals and requirements in your brief. This object is available in API version 61.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdditionalNotes

AgentGuardrails

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Context related to the campaign that isn’t represented in the other fields.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Guardrails that the agent must follow when creating a campaign. Use these guardrails to
prevent damage to your brand and to ensure safety and compliance.


Standard Objects Brief

**Field** **Details**

```
BrandId

Description

IsConversational

KeyMessage

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of your brand.

This field is a relationship field.

**Relationship Name**
Brand

**Refers To**
ManagedContent

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the brief.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the campaign contains conversational elements.

The default value is `false` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The main theme or message that you want to deliver to your customers through the campaign
that’s associated with the brief.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last referenced by a campaign.


Standard Objects Brief

**Field** **Details**

```
LastViewedDate

Name

PlanName

PrimaryCtas

PrimaryGoal

PrimaryKpi

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the brief.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An agent-generated name for the campaign. When you save a campaign preview, the
resulting campaign has this name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The main calls-to-action (CTAs) for the brief. The agent uses this information to understand
the actions that it can use to meet the goals of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The goal of the campaign that’s associated with the brief. The agent uses this field to
understand the main objective of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects BriefcaseAssignment

**Field** **Details**

**Description**
The main key performance indicator (KPI) for measuring progress toward the goal. The agent
uses this field to prioritize actions that contribute to the goal of the campaign.

```
Priority

TargetAudience

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The priority of the brief. The agent uses this field to prioritize actions that contribute to the
goal of the campaign.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the characteristics of the audience that you want to reach through the
campaign that’s associated with this brief.

### BriefcaseAssignment

Represents the assignment of a briefcase definition to selected users and user groups. This object is available in API version 50.0 and
later.

Use this object to assign selected records for users and groups to view offline. Briefcase objects are available in orgs that have Briefcase
Builder and Field Service enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is **Briefcase Definition ID** .


### Standard Objects BriefcaseDefinition

**Field** **Details**

```
UserOrGroupId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the user or group requiring access to the briefcase. Label is **User or Group**
**ID** .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseAssignmentChangeEvent (API version 55.0)**
Change events are available for the object.

### BriefcaseDefinition

Represents a briefcase definition. A briefcase makes selected records available for users to view when they’re offline in the Salesforce
Field Service mobile app for iOS and Android. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Briefcase objects are available in orgs that have Briefcase Builder and Field Service enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Packaging Considerations

An org can have up to 5 briefcases. Installed briefcases are counted against this limit. You can’t install a package that includes a briefcase
if your org already has 5 briefcases. When a managed package includes a briefcase, the only changes allowed for the briefcase are
activating or deactivating and assigning users or groups to the briefcase.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects BriefcaseDefinition

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Description of the briefcase definition. Limited to 1024 characters.

```
DeveloperName

IsActive

Language

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Limited to 80 characters. Label is **Name** .

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the briefcase is available for use ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the briefcase. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned.

Possible values are:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`


Standard Objects BriefcaseDefinition

**Field** **Details**

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

```
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The master label for the briefcase. This internal label doesn’t get translated. Limited to 80
characters.

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


### Standard Objects BriefcaseRule

Usage

Use this object to query a briefcase or a list of briefcases with selected records and user assignments. For example:

```
   SELECT Id, Description FROM BriefcaseDefinition

   WHERE Id in (SELECT BriefcaseId FROM BriefcaseRule

   WHERE TargetEntity='Account')

   AND Id in (SELECT BriefcaseId FROM BriefcaseAssignment where

   UserOrGroupId='00GR0000000VtwUMAS')

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseDefinitionChangeEvent (API version 55.0)**
Change events are available for the object.

### BriefcaseRule

Represents a rule that specifies records for a briefcase definition. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is **Briefcase Definition ID** .

This field is a relationship field.

**Relationship Name**
### Briefcase

**Relationship Type**
Lookup


Standard Objects BriefcaseRule

**Field** **Details**

**Refers To**
BriefcaseDefinition

```
FilterLogic

IsAscendingOrder

OptionsIsRelatedFilesRule

OrderBy

ParentRuleId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The filter logic for record selection, for example, `1 AND 2` where 1 and 2 correspond to
filter 1 and filter 2. Filter logic operators include `AND` and `OR` . Limited to 255 characters.
Label is **Filter Logic** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the records should be sorted in ascending order. Label is
**Ascending** .

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the briefcase rule is part of a hierarchical set of rules that configure the
offline priming of file attachments. Available only for the Offline App (Salesforce Mobile App
Plus).

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The field to order the records by, which determines how the records can be sorted. For
example, `AccountName` or `CreatedBy` . Label is **Order By** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects BriefcaseRule

**Field** **Details**

**Description**
The ID of the parent rule of this briefcase rule. This field is a relationship field.

**Relationship Name**
ParentRule

**Relationship Type**
Lookup

**Refers To**
BriefcaseRule

```
QueryScope

RecordLimit

RelationshipField

RelationshipType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. A group of records to restrict the scope of this rule.

Possible values are:

**•** `assignedToMe`

**•** `everything`

**•** `mine`

The default value is `everything` (All Records). The value `assignedToMe` is available
only for the `ServiceAppointment` object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record limit for the object. The recommended number for record limit is up to 500 records
per object for optimal performance. The maximum number is 2000. Label is **Limit** .

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The Salesforce object field that relates the briefcase rule to another briefcase rule. For example,
an Account rule can be related to a Contact rule using the Account ID object field. In this
example, the value for the briefcase rule's `RelationshipField` is `AccountID` .

**Type**
picklist


### Standard Objects BriefcaseRuleFilter

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The relationship of the briefcase rule to another briefcase rule. Possible values are:

**•** `ParentToChild`

**•** `ChildToParent`

```
TargetEntity

### BriefcaseRuleFilter

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The standard object, custom object, or custom metadata type that the briefcase rule selects
records from. The UI label is **Target Object** .

Represents a filter criteria for a briefcase rule. This object is available in API version 50.0 and later.

Special Access Rules

This object is read-only.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
BriefcaseRuleId

FilterOperator

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase rule.

**Type**
picklist


Standard Objects BriefcaseRuleFilter

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. The comparison operator for this rule filter.

Possible values are:

**•** `d` —Ends with

**•** `e`                   - Equals

**•** `g` —Greater than

**•** `h` —Greater than or equal

**•** `i` —Like

**•** `l` —Less than

**•** `m` —Less than or equal

**•** `s` —Starts with

```
FilterSeqNumber

FilterValue

TargetEntityField

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. The filter number. When you apply multiple filters, the filters are numbered
sequentially, 1, 2, 3, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value for the field and criteria. For example, `true` or `false` for a boolean field whose
criteria or filter operator is Equals. Capitalization matters with date filter operators. Be sure
to specify date literals in uppercase. Some valid date literals include TODAY, YESTERDAY and
TOMORROW.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Required. The field to filter by. Compound fields and encrypted fields aren’t supported. Label
is **Field** .


### Standard Objects BroadcastCommAudience BroadcastCommAudience

Represents the audience that the broadcast communication is sent to. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object with Service Cloud, enable Incident Management in Setup and set up Broadcast Communications.

Fields

**Field** **Details**

```
AudienceId

### `BroadcastCommAudienceNumber`

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication audience.

**•** If `BroadcastType` is `Alert`, this value is the ID of the Group record where the
message is sent to.

**•** If `BroadcastType` is `Email`, this value is the ID of the ListEmail record where the
email is sent to.

**•** If `BroadcastType` is `ExperienceSiteBanner`, this value is the ID of the
Network record where the banner is displayed at.

**•** If `BroadcastType` is `Slack`, this value is the ID of the CollaborationRoom record
where the message is sent to.

This field is a polymorphic relationship field.

**Relationship Name**
Audience

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom, Group, ListEmail, Network

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


Standard Objects BroadcastCommAudience

**Field** **Details**

**Description**
Auto-generated number for the BroadcastCommAudience record.

```
BroadcastCommunicationId

BroadcastFailureReason

BroadcastType

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication record.

This field is a relationship field.

**Relationship Name**
BroadcastCommunication

**Relationship Type**
Lookup

**Refers To**
BroadcastCommunication

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason the broadcast communication failed to send.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`

**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects BroadcastCommAudience

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

```
LastViewedDate

MessageTimeStamp

OwnerId

SiteBannerText

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If `BroacastType` is `Slack`, this value is the timestamp when the broadcast Slack
message was sent.

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
Create, Nillable

**Description**
If `BroadcastType` is `ExperienceSiteBanner`, this field contains the banner text
displayed on the associated site.


Standard Objects BroadcastCommAudience

**Field** **Details**

```
SiteBannerVisibility

Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `BroadcastType` is `ExperienceSiteBanner`, this field contains information
about who can view the banner.

Possible values are:

**•** `AuthenticatedUsers`

**•** `GuestUsers`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the broadcast communication.

Possible values are:

**•** `Active` —The site banner is visible on the site. Only applies if `BroadcastType` is
`ExperienceSiteBanner` .

**•** `Deleted` —The message is successfully deleted and isn’t visible anymore. Only applies
if `BroadcastType` is `Slack` .

**•** `DeleteFailed` —The message failed to delete but is still visible. Only applies if
`BroadcastType` is `Slack` .

**•** `Failed` —The message failed to send. Applies to any `BroadcastType` .

**•** `Inactive` —The site banner isn’t visible on the site. Only applies if `BroadcastType`
is `ExperienceSiteBanner` .

**•** `Sent` —The message is sent successfully. Only applies if the `BroadcastType` is
`Email` or `Slack` .

**•** `Updated` —The message is successfully edited. Only applies if the `BroadcastType`
is `Slack` .

**•** `UpdateFailed` —The message failed to edit and the update isn’t visible. Only applies
if the `BroadcastType` is `Slack` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommAudienceChangeEvent on page 68**
Change events are available for the object.


### Standard Objects BroadcastCommunication

**BroadcastCommAudienceFeed on page 55**
Feed tracking is available for the object.

**BroadcastCommAudienceHistory on page 63**
History is available for tracked fields of the object.

**BroadcastCommAudienceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BroadcastCommAudienceShare on page 67**
Sharing is available for the object.

### BroadcastCommunication

Represents a broadcast communication related to an incident. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`

Special Access Rules

To access this object with Service Cloud, enable Incident Management in setup and set up Broadcast Communications.

Fields

**Field** **Details**

```
Body

### `BroadcastCommunicationNumber`

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert`, this field contains the alert message.

**•** If `BroadcastType` is `Email`, this field contains the email body text.

**•** If `BroadcastType` is `ExperienceSiteBanner`, this field is empty.

**•** If `BroadcastType` is `Slack`, this field contains the Slack message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for every BroadcastCommunication record.


Standard Objects BroadcastCommunication

**Field** **Details**

```
BroadcastType

CustomNotificationTypeId

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`

**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the custom notification template used to frame the Slack message. Only applies if
`BroadcastType` is `Slack` .

Available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
CustomNotificationType

**Relationship Type**
Lookup

**Refers To**
CustomNotificationType

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


Standard Objects BroadcastCommunication

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

```
OwnerId

RelatedRecordId

Subject

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

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
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the incident associated with the broadcast communication.

This field is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert`, this field is the alert message in the format “Incident
Alert | <Incident subject> | <Incident Number>.”

**•** If `BroadcastType` is `Email`, this field is the subject of the email sent.


### Standard Objects BroadcastTopic

**Field** **Details**

**•** If `BroadcastType` is `ExperienceSiteBanner`, this field is empty.

**•** If `BroadcastType` is `Slack`, this field is in the format “Incident Alert | <Incident
Subject>."

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommunicationChangeEvent on page 68**
Change events are available for the object.

**BroadcastCommunicationFeed on page 55**
Feed tracking is available for the object.

**BroadcastCommunicationHistory on page 63**
History is available for tracked fields of the object.

**BroadcastCommunicationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**BroadcastCommunicationShare on page 67**
Sharing is available for the object.

### BroadcastTopic

Represents a definition of a broadcast topic. A broadcast topic is associated with a list of Experience Cloud network sites for Service Cloud
and collaboration rooms for Sales Cloud. The topic is created for a specific user role. Collaboration rooms are linked to Slack channels.
This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object with Sales Cloud, enable Slack Terms of Service and Sales Cloud for Slack App.

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.


Standard Objects BroadcastTopic

Fields

**Field** **Details**

```
BroadcastReason

Description

IsFeatured

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Reason for the broadcast topic. This field differentiates between Service Cloud and Sales
Cloud use cases.

Possible values are:

**•** `FeedChannels` —Used in Sales Cloud and associates the topic with collaboration
rooms.

**•** `IncidentCommunication` —Used in Service Cloud for Customer Service Incident
Management and associates the topic with networks.

The default value is `FeedChannels` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the broadcast topic.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the broadcast topic is featured ( `true` ) or not ( `false` ). This field is
applicable only when BroadcastReason is FeedChannels. A featured topic displays the
associated collaboration rooms to new users.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.


Standard Objects BroadcastTopic

**Field** **Details**

```
LastViewedDate

Name

OwnerId

TopicType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the broadcast topic.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the broadcast topic.

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
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Category for the broadcast topic.

Possible values are:

**•** `DealsWon` —Feed of won deals to see your team's successes. This value appears when
the Sales Cloud special access rules are enabled.


### Standard Objects BroadcastTopicGroup

**Field** **Details**

**•** `DealsToWatch` —Feed of deals that have an amount above a specified value and
are likely to close. This value appears when the Sales Cloud special access rules are
enabled.

**•** `Incident Communication` —This value appears when the Service Cloud special
access rules are enabled.

### BroadcastTopicGroup

Represents a junction object that relates a group to an alert type broadcast topic. The broadcast sends the alert to this group. This object
is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Enable Customer Service Incident Management and Broadcast Alert. To create a BroadcastTopicGroup record, set the BroadcastReason
field of the associated BroadcastTopic to Incident Communication.

Fields

**Field** **Details**

```
BroadcastTopicId

GroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast topic.

This field is a relationship field.

**Relationship Name**
### BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
### BroadcastTopic

**Type**
reference


### Standard Objects BroadcastTopicNetwork

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group where the alert of the associated BroadcastTopic record with an `Alert`
`BroadcastType` is sent to.

This field is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

```
Name

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the broadcast topic group.

This field is optional.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastTopicGroupChangeEvent on page 68**
Change events are available for the object.

Available in API version 58.0

### BroadcastTopicNetwork

Represents a link between a broadcast topic and the Experience Cloud network site for Service Cloud. This object is available in API
version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects BroadcastTopicNetwork

Special Access Rules

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.

Fields

**Field** **Details**

```
BroadcastTopicId

Name

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The BroadcastTopic ID that's linked to the Network.

This field is a relationship field.

**Relationship Name**
BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
BroadcastTopic

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the broadcast topic that's assigned to the network.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Network ID that's linked to the BroadcastTopic..

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network


### Standard Objects BrowserPolicyViolation

Associated Objects

